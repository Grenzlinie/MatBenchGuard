#!/usr/bin/env python3
"""Probe materials resources and run an optional isolated E2 smoke."""

from __future__ import annotations

import hashlib
import ipaddress
import json
import math
import re
import shutil
import socket
import ssl
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from prepare_audit_output import REQUIRED_ROLES, iter_public_files


USER_AGENT = "materials-benchmark-review/0.1"
MAX_ARTIFACT_BYTES = 1024 * 1024
LEVEL_NAMES = {
    0: "L0",
    1: "L1",
    2: "L2",
    3: "L3",
    4: "L4",
    5: "L5",
    6: "L6",
}
LEVEL_VALUES = {name: level for level, name in LEVEL_NAMES.items()}


class UnsafeResourceURL(ValueError):
    """Raised before accessing a resource URL outside the allowed boundary."""


def sanitized_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    hostname = parsed.hostname or ""
    netloc = hostname
    if parsed.port is not None:
        netloc += f":{parsed.port}"
    return urllib.parse.urlunsplit(
        (parsed.scheme, netloc, parsed.path, "", "")
    )


def validate_network_url(url: str, allow_private_network: bool) -> None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise UnsafeResourceURL("resource URL must use http or https")
    if parsed.username is not None or parsed.password is not None:
        raise UnsafeResourceURL("resource URL must not contain credentials")
    if allow_private_network:
        return
    try:
        addresses = {
            item[4][0]
            for item in socket.getaddrinfo(
                parsed.hostname,
                parsed.port or (443 if parsed.scheme == "https" else 80),
                type=socket.SOCK_STREAM,
            )
        }
    except socket.gaierror:
        return
    for address in addresses:
        ip = ipaddress.ip_address(address)
        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_multicast
            or ip.is_reserved
            or ip.is_unspecified
        ):
            raise UnsafeResourceURL(
                "resource URL resolves to a private or unsafe network address"
            )


def is_literal_private_address(hostname: str | None) -> bool:
    if not hostname:
        return False
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        return False
    return address.is_private or address.is_loopback or address.is_link_local


class ValidatingRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, allow_private_network: bool) -> None:
        super().__init__()
        self.allow_private_network = allow_private_network

    def redirect_request(
        self,
        req: urllib.request.Request,
        fp: Any,
        code: int,
        msg: str,
        headers: Any,
        newurl: str,
    ) -> urllib.request.Request | None:
        validate_network_url(newurl, self.allow_private_network)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_access(value: Any) -> dict[str, Any]:
    if isinstance(value, str):
        return {"method": "url", "url": value}
    return dict(value) if isinstance(value, dict) else {}


def classify_resource(item: dict[str, Any]) -> str:
    declared = str(item.get("type", "")).lower().replace("-", "_")
    text = f"{declared} {item.get('name', '')}".lower()
    checks = (
        ("commercial_software", ("commercial", "vasp", "dmol", "comsol")),
        ("pseudopotential", ("pseudopotential", "pseudo", "potcar")),
        ("basis_set", ("basis_set", "basis set", "basis")),
        ("materials_database", ("materials_database", "database")),
        ("structure", ("structure", "cif", "poscar")),
        ("potential", ("potential", "force field", "eam", "meam", "openkim")),
        ("package", ("package",)),
        ("tool", ("tool", "software")),
    )
    for category, terms in checks:
        if any(term in text for term in terms):
            return category
    return declared or "other"


def resource_role(item: dict[str, Any]) -> str:
    declared = str(item.get("role", "")).upper()
    if declared in {"CRITICAL", "REPLACEABLE", "OPTIONAL"}:
        return declared
    if item.get("required") is False:
        return "OPTIONAL"
    return "CRITICAL"


def _http_probe_once(
    url: str,
    timeout: float,
    allow_private_network: bool,
) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(url)
    homepage_only = parsed.path in {"", "/"} and not parsed.query
    try:
        validate_network_url(url, allow_private_network)
    except UnsafeResourceURL as exc:
        return {
            "ok": False,
            "status_code": None,
            "final_url": sanitized_url(url),
            "homepage_only": homepage_only,
            "error_type": "blocked_private_network",
            "error": str(exc),
            "elapsed_sec": 0.0,
        }
    request = urllib.request.Request(
        url,
        method="GET",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
            "Range": f"bytes=0-{MAX_ARTIFACT_BYTES - 1}",
        },
    )
    handlers: list[Any] = [ValidatingRedirectHandler(allow_private_network)]
    if allow_private_network and is_literal_private_address(parsed.hostname):
        handlers.insert(0, urllib.request.ProxyHandler({}))
    opener = urllib.request.build_opener(*handlers)
    started = time.time()
    try:
        with opener.open(request, timeout=timeout) as response:
            body = response.read(MAX_ARTIFACT_BYTES + 1)
            truncated = len(body) > MAX_ARTIFACT_BYTES
            if truncated:
                body = body[:MAX_ARTIFACT_BYTES]
            return {
                "ok": 200 <= response.getcode() < 400,
                "status_code": response.getcode(),
                "final_url": sanitized_url(response.geturl()),
                "homepage_only": homepage_only,
                "content_type": response.headers.get("Content-Type"),
                "content_length": response.headers.get("Content-Length"),
                "bytes_read": len(body),
                "truncated": truncated,
                "sha256": "sha256:" + hashlib.sha256(body).hexdigest(),
                "body_text": body.decode("utf-8", errors="replace")[:4096],
                "elapsed_sec": round(time.time() - started, 3),
            }
    except urllib.error.HTTPError as exc:
        return {
            "ok": False,
            "status_code": exc.code,
            "final_url": sanitized_url(exc.geturl()),
            "homepage_only": homepage_only,
            "error_type": (
                "authentication"
                if exc.code in {401, 403}
                else "rate_limit"
                if exc.code == 429
                else "not_found"
                if exc.code in {404, 410}
                else "http_server"
                if exc.code >= 500
                else "http_client"
            ),
            "error": str(exc),
            "elapsed_sec": round(time.time() - started, 3),
        }
    except UnsafeResourceURL as exc:
        return {
            "ok": False,
            "status_code": None,
            "final_url": sanitized_url(url),
            "homepage_only": homepage_only,
            "error_type": "blocked_private_network",
            "error": str(exc),
            "elapsed_sec": round(time.time() - started, 3),
        }
    except urllib.error.URLError as exc:
        reason = exc.reason
        error_type = (
            "dns"
            if isinstance(reason, socket.gaierror)
            else "tls"
            if isinstance(reason, ssl.SSLError)
            else "timeout"
            if isinstance(reason, TimeoutError)
            else "network"
        )
        return {
            "ok": False,
            "status_code": None,
            "final_url": url,
            "homepage_only": homepage_only,
            "error_type": error_type,
            "error": str(exc),
            "elapsed_sec": round(time.time() - started, 3),
        }
    except (TimeoutError, socket.timeout) as exc:
        return {
            "ok": False,
            "status_code": None,
            "final_url": url,
            "homepage_only": homepage_only,
            "error_type": "timeout",
            "error": str(exc),
            "elapsed_sec": round(time.time() - started, 3),
        }


def http_probe(
    url: str,
    timeout: float,
    allow_private_network: bool,
    attempts: int = 2,
) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    transient = {
        "dns",
        "tls",
        "timeout",
        "network",
        "rate_limit",
        "http_server",
    }
    for _ in range(attempts):
        result = _http_probe_once(url, timeout, allow_private_network)
        results.append(result)
        if result.get("ok") or result.get("error_type") not in transient:
            break
    final = dict(results[-1])
    final["attempt_count"] = len(results)
    final["attempt_error_types"] = [
        item.get("error_type") for item in results if not item.get("ok")
    ]
    return final


def status_for_failure(detail: dict[str, Any]) -> str:
    error_type = detail.get("error_type")
    if error_type == "authentication":
        return "REQUIRES_AUTH"
    if error_type == "rate_limit":
        return "RATE_LIMITED"
    if error_type == "not_found":
        return "PERMANENT_UNAVAILABLE"
    if error_type == "blocked_private_network":
        return "BLOCKED_PRIVATE_NETWORK"
    return "TRANSIENT_FAILURE"


def probe_url_access(
    access: dict[str, Any],
    timeout: float,
    allow_private_network: bool,
) -> dict[str, Any]:
    url = str(access.get("url", ""))
    if not url:
        return {
            "verified_level": 0,
            "status": "DECLARED_ONLY",
            "identity_match": None,
            "probe": {"error_type": "missing_url"},
        }
    detail = http_probe(url, timeout, allow_private_network)
    if not detail["ok"]:
        return {
            "verified_level": 0,
            "status": status_for_failure(detail),
            "identity_match": None,
            "probe": detail,
        }
    if detail["homepage_only"]:
        level = 1
    else:
        level = 4 if detail["bytes_read"] > 0 else 3
    status = "AVAILABLE" if level >= 4 else "PARTIALLY_AVAILABLE"
    identity_match: bool | None = None
    declared_checksum = str(access.get("checksum", "")).lower()
    if declared_checksum and level >= 4 and not detail["truncated"]:
        identity_match = detail["sha256"].lower() == declared_checksum
        if identity_match:
            level = 5
        else:
            status = "IDENTITY_MISMATCH"
    return {
        "verified_level": level,
        "status": status,
        "identity_match": identity_match,
        "probe": detail,
    }


def probe_accession_access(
    access: dict[str, Any],
    timeout: float,
    allow_private_network: bool,
) -> dict[str, Any]:
    accession = str(access.get("accession", ""))
    metadata_url = str(access.get("metadata_url", ""))
    artifact_url = str(access.get("artifact_url", ""))
    if not accession or not metadata_url:
        return {
            "verified_level": 0,
            "status": "DECLARED_ONLY",
            "identity_match": None,
            "probe": {"error_type": "underspecified_accession"},
        }
    metadata = http_probe(
        metadata_url, timeout, allow_private_network
    )
    if not metadata["ok"]:
        return {
            "verified_level": 0,
            "status": status_for_failure(metadata),
            "identity_match": None,
            "probe": {"metadata": metadata},
        }
    identity_match = accession.lower() in metadata["body_text"].lower()
    level = 2
    status = "PARTIALLY_AVAILABLE"
    artifact: dict[str, Any] | None = None
    if artifact_url:
        level = 3
        artifact = http_probe(
            artifact_url, timeout, allow_private_network
        )
        if artifact["ok"] and artifact["bytes_read"] > 0:
            level = 4
            status = "AVAILABLE"
        elif not artifact["ok"]:
            status = status_for_failure(artifact)
    if not identity_match:
        status = "IDENTITY_MISMATCH"
    return {
        "verified_level": level,
        "status": status,
        "identity_match": identity_match,
        "probe": {"metadata": metadata, "artifact": artifact},
    }


def probe_package_access(
    access: dict[str, Any],
    timeout: float,
    allow_private_network: bool,
) -> dict[str, Any]:
    package = str(access.get("package", ""))
    registry_url = str(
        access.get("registry_url")
        or f"https://pypi.org/pypi/{urllib.parse.quote(package)}/json"
    )
    detail = http_probe(
        registry_url, timeout, allow_private_network
    )
    if not detail["ok"]:
        return {
            "verified_level": 0,
            "status": status_for_failure(detail),
            "identity_match": None,
            "probe": detail,
        }
    identity_match = package.lower() in detail["body_text"].lower()
    declared_version = str(access.get("version", ""))
    resolved_version: str | None = None
    try:
        metadata = json.loads(detail["body_text"])
        if isinstance(metadata, dict):
            resolved_version = str(
                metadata.get("version")
                or (metadata.get("info") or {}).get("version")
                or ""
            )
    except (TypeError, ValueError, json.JSONDecodeError):
        pass
    if declared_version and resolved_version:
        identity_match = identity_match and declared_version == resolved_version
    return {
        "verified_level": 2,
        "status": (
            "PARTIALLY_AVAILABLE"
            if identity_match
            else "IDENTITY_MISMATCH"
        ),
        "identity_match": identity_match,
        "probe": {
            **detail,
            "declared_version": declared_version or None,
            "resolved_version": resolved_version,
        },
    }


def probe_inline_access(root: Path, access: dict[str, Any]) -> dict[str, Any]:
    evidence = access.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        return {
            "verified_level": 0,
            "status": "DECLARED_ONLY",
            "identity_match": None,
            "probe": {"inline": True, "evidence_verified": False},
        }
    verified: list[dict[str, str]] = []
    for index, item in enumerate(evidence, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"inline evidence {index} must be an object")
        relative = item.get("file")
        quote = item.get("quote")
        if relative not in REQUIRED_ROLES:
            raise ValueError(
                f"inline evidence {index} uses unsupported file: {relative}"
            )
        if not isinstance(quote, str) or not quote:
            raise ValueError(f"inline evidence {index} requires a quote")
        text = (root / relative).read_text(
            encoding="utf-8", errors="replace"
        )
        if quote not in text:
            raise ValueError(
                f"inline evidence {index} quote is absent from {relative}"
            )
        verified.append({"file": relative, "quote": quote})
    return {
        "verified_level": 5,
        "status": "AVAILABLE",
        "identity_match": True,
        "probe": {
            "inline": True,
            "evidence_verified": True,
            "evidence": verified,
        },
    }


def sanitized_access(access: dict[str, Any]) -> dict[str, Any]:
    value = dict(access)
    for key in ("url", "metadata_url", "artifact_url", "registry_url"):
        if value.get(key):
            value[key] = sanitized_url(str(value[key]))
    return value


def probe_item(
    root: Path,
    item: dict[str, Any],
    timeout: float,
    allow_private_network: bool,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    access = normalize_access(item.get("access"))
    method = str(access.get("method", "")).lower()
    role = resource_role(item)
    category = classify_resource(item)
    raw_required_level = str(
        item.get(
            "required_level",
            "L2" if category in {"tool", "package"} else "L4",
        )
    ).upper()
    invalid_required_level = raw_required_level not in LEVEL_VALUES
    default_required_level = (
        "L2" if category in {"tool", "package"} else "L4"
    )
    required_level = (
        default_required_level
        if invalid_required_level
        else raw_required_level
    )
    if method == "url":
        outcome = probe_url_access(
            access, timeout, allow_private_network
        )
    elif method == "accession":
        outcome = probe_accession_access(
            access, timeout, allow_private_network
        )
    elif method == "package":
        outcome = probe_package_access(
            access, timeout, allow_private_network
        )
    elif method == "inline":
        outcome = probe_inline_access(root, access)
    elif method == "license":
        authorized = access.get("authorization_provided") is True
        outcome = {
            "verified_level": 2 if authorized else 0,
            "status": "PARTIALLY_AVAILABLE" if authorized else "REQUIRES_LICENSE",
            "identity_match": authorized,
            "probe": {
                "license": access.get("license"),
                "authorization_provided": authorized,
            },
        }
    elif method == "auth":
        authorized = access.get("authorization_provided") is True
        outcome = {
            "verified_level": 2 if authorized else 0,
            "status": (
                "PARTIALLY_AVAILABLE"
                if authorized
                else "REQUIRES_AUTH"
            ),
            "identity_match": authorized,
            "probe": {
                "authentication": "instruction-declared",
                "authorization_provided": authorized,
            },
        }
    else:
        outcome = {
            "verified_level": 0,
            "status": "DECLARED_ONLY",
            "identity_match": None,
            "probe": {"error_type": "unsupported_method", "method": method},
        }
    level = int(outcome["verified_level"])
    report = {
        "resource_id": item.get("id"),
        "name": item.get("name"),
        "category": category,
        "role": role,
        "identifier": (
            access.get("accession")
            or access.get("package")
            or access.get("url")
        ),
        "required_level": required_level,
        "verified_level": LEVEL_NAMES[level],
        "status": outcome["status"],
        "identity_match": outcome["identity_match"],
        "environment_verified": False,
        "access": sanitized_access(access),
        "probe": outcome["probe"],
        "tested_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    findings: list[dict[str, Any]] = []

    def add(severity: str, code: str, message: str) -> None:
        findings.append(
            {
                "severity": severity,
                "code": code,
                "message": message,
                "affected_files": ["resources.json"],
                "evidence": {
                    "resource_id": item.get("id"),
                    "status": report["status"],
                    "verified_level": report["verified_level"],
                    "required_level": required_level,
                },
            }
        )

    if invalid_required_level:
        add(
            "HIGH",
            "INVALID_REQUIRED_LEVEL",
            f"required_level {raw_required_level!r} is not one of L0-L6",
        )
    if outcome["probe"].get("homepage_only") and level == 1:
        add(
            "HIGH" if role == "CRITICAL" else "MEDIUM",
            "RESOURCE_HOMEPAGE_ONLY",
            "a homepage does not identify the required material artifact",
        )
    if category == "package" and not access.get("version"):
        add("MEDIUM", "UNPINNED_PACKAGE", "software package version is unpinned")
    if category in {"potential", "pseudopotential", "basis_set"}:
        missing_context = [
            key
            for key in ("version", "compatibility")
            if not access.get(key)
        ]
        if missing_context:
            add(
                "HIGH" if role == "CRITICAL" else "MEDIUM",
                "MATERIAL_RESOURCE_COMPATIBILITY_UNDECLARED",
                "material resource lacks " + ", ".join(missing_context),
            )
    if report["status"] == "REQUIRES_LICENSE":
        add(
            "FATAL" if role == "CRITICAL" else "HIGH",
            "COMMERCIAL_LICENSE_UNAVAILABLE",
            "commercial software lacks declared authorization",
        )
    if report["status"] == "REQUIRES_AUTH":
        add(
            "FATAL" if role == "CRITICAL" else "HIGH",
            "RESOURCE_REQUIRES_AUTH",
            "resource requires undeclared authentication",
        )
    if report["status"] == "PERMANENT_UNAVAILABLE":
        add(
            "FATAL" if role == "CRITICAL" else "HIGH",
            "CRITICAL_RESOURCE_UNAVAILABLE"
            if role == "CRITICAL"
            else "RESOURCE_UNAVAILABLE",
            "declared resource is permanently unavailable",
        )
    if report["status"] == "IDENTITY_MISMATCH":
        add(
            "FATAL"
            if role == "CRITICAL"
            else "HIGH"
            if role == "REPLACEABLE"
            else "MEDIUM",
            "RESOURCE_IDENTITY_MISMATCH",
            "retrieved resource identity differs from the declaration",
        )
    if report["status"] in {"TRANSIENT_FAILURE", "RATE_LIMITED"}:
        add(
            "HIGH"
            if role == "CRITICAL"
            else "MEDIUM"
            if role == "REPLACEABLE"
            else "LOW",
            "RESOURCE_TRANSIENT_FAILURE",
            "resource access failed transiently after retry",
        )
    if report["status"] == "BLOCKED_PRIVATE_NETWORK":
        add(
            "HIGH" if role == "CRITICAL" else "MEDIUM",
            "RESOURCE_PRIVATE_NETWORK_BLOCKED",
            "resource URL targets a private or unsafe network address",
        )
    if level < LEVEL_VALUES[required_level]:
        add(
            "HIGH"
            if role == "CRITICAL"
            else "MEDIUM"
            if role == "REPLACEABLE"
            else "LOW",
            "RESOURCE_VERIFICATION_INSUFFICIENT",
            f"resource reached {LEVEL_NAMES[level]} but requires {required_level}",
        )
    return report, findings


def instruction_direct_inputs(instruction: str) -> list[dict[str, Any]]:
    """Parse URLs from explicit Markdown list/paragraph/section entries."""
    heading_pattern = re.compile(r"^\s*#{1,6}\s+")
    list_pattern = re.compile(r"^(\s*)(?:[-+*]|\d+[.)])\s+")
    fence_pattern = re.compile(r"^\s*(`{3,}|~{3,})")
    fenced_lines: set[int] = set()
    active_fence: tuple[str, int] | None = None
    instruction_lines = instruction.splitlines()
    for line_number, line in enumerate(instruction_lines, start=1):
        marker = fence_pattern.match(line)
        if active_fence is not None:
            fenced_lines.add(line_number)
            if (
                marker
                and marker.group(1)[0] == active_fence[0]
                and len(marker.group(1)) >= active_fence[1]
            ):
                active_fence = None
            continue
        if marker:
            fenced_lines.add(line_number)
            active_fence = (marker.group(1)[0], len(marker.group(1)))

    sections: list[
        tuple[tuple[int, str] | None, list[tuple[int, str]]]
    ] = []
    heading: tuple[int, str] | None = None
    body: list[tuple[int, str]] = []
    for line_number, line in enumerate(instruction_lines, start=1):
        if (
            line_number not in fenced_lines
            and heading_pattern.match(line)
        ):
            if heading is not None or body:
                sections.append((heading, body))
            heading = (line_number, line)
            body = []
        else:
            body.append((line_number, line))
    if heading is not None or body:
        sections.append((heading, body))

    entries: list[
        tuple[tuple[int, str] | None, list[tuple[int, str]]]
    ] = []
    for section_heading, section_body in sections:
        index = 0
        while index < len(section_body):
            line_number, line = section_body[index]
            if not line.strip():
                index += 1
                continue
            marker = list_pattern.match(line)
            entry: list[tuple[int, str]] = []
            if marker:
                item_indent = len(marker.group(1))
                entry.append((line_number, line))
                index += 1
                while index < len(section_body):
                    next_number, next_line = section_body[index]
                    next_marker = list_pattern.match(next_line)
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if (
                        next_marker
                        and len(next_marker.group(1)) <= item_indent
                    ):
                        break
                    if next_line.strip() and next_indent <= item_indent:
                        break
                    entry.append((next_number, next_line))
                    index += 1
            else:
                while index < len(section_body):
                    next_number, next_line = section_body[index]
                    if (
                        not next_line.strip()
                        or list_pattern.match(next_line)
                    ):
                        break
                    entry.append((next_number, next_line))
                    index += 1
            entries.append((section_heading, entry))

    def semantic_text(entry: list[tuple[int, str]]) -> str:
        return "\n".join(
            line
            for line_number, line in entry
            if line_number not in fenced_lines
        ).lower()

    def direct_topic(text: str) -> bool:
        return bool(
            re.search(
                r"\b(?:direct|external|required)?\s*inputs?\b"
                r"|\binput\s+resources?\b",
                text,
            )
        )

    def data_resource_clause(text: str) -> bool:
        prefix = text.split("http", 1)[0]
        return bool(
            re.search(
                r"\b(?:dataset|data\s+file|input\s+file"
                r"|external\s+service|remote\s+service)\b",
                prefix,
            )
        )

    def indispensable(text: str) -> bool:
        if re.search(
            r"\bnot\s+(?:indispensable|required)\b"
            r"|\b(?:indispensable|required)\s*:\s*(?:no|false)\b",
            text,
        ):
            return False
        return any(
            term in text
            for term in ("indispensable", "required", "must", "必要")
        )

    def no_scientific_equivalent(text: str) -> bool:
        return any(
            term in text
            for term in (
                "no equivalent",
                "without equivalent",
                "no scientifically equivalent",
                "不可替代",
            )
        ) or bool(
            re.search(
                r"\b(?:scientific\s+)?(?:equivalent|equivalence)"
                r"(?:\s+source)?\s*:\s*"
                r"(?:none|no|false|not\s+available)\b",
                text,
            )
        )

    def extract_urls(text: str) -> list[str]:
        return [
            url.rstrip(".,;:!?\"'")
            for url in re.findall(r"https?://[^\s)\]}>]+", text)
        ]

    def docs_clause(text: str) -> bool:
        prefix = text.split("http", 1)[0]
        return bool(
            re.search(
                r"\b(?:docs?|documentation|guide|readme|reference)\b",
                prefix,
            )
        )

    def entity_role(text: str) -> str:
        lowered = text.lower()
        is_docs = docs_clause(lowered)
        is_resource = bool(
            re.match(
                r"^\s*(?:the\s+)?(?:required\s+|optional\s+)?"
                r"(?:dataset|data\s+file|input\s+file"
                r"|external\s+service|remote\s+service"
                r"|resource|input|service)\b",
                lowered,
            )
        )
        if is_docs and is_resource:
            return "mixed"
        if is_docs:
            return "docs"
        if is_resource:
            return "resource"
        return "neutral"

    def markdown_clauses(
        semantic_lines: list[tuple[int, str]],
    ) -> tuple[
        list[tuple[int, str, str]],
        dict[str, str],
        dict[str, str | None],
    ]:
        label_pattern = re.compile(
            r"\b(?:dataset|data(?:\s+file)?|docs?|documentation"
            r"|guide|reference|input|resource|service)\s*:",
            re.IGNORECASE,
        )

        def label_segments(text: str) -> list[str]:
            segments: list[str] = []
            start = 0
            seen_label = False
            url_spans = [
                match.span()
                for match in re.finditer(
                    r"https?://[^\s)\]}>]+", text
                )
            ]
            for match in label_pattern.finditer(text):
                if any(
                    span_start <= match.start() < span_end
                    for span_start, span_end in url_spans
                ):
                    continue
                prefix = text[start : match.start()]
                if match.start() > start and (
                    seen_label or bool(extract_urls(prefix))
                ):
                    if prefix.strip():
                        segments.append(prefix.strip())
                    start = match.start()
                    seen_label = False
                seen_label = True
            remainder = text[start:].strip()
            if remainder:
                segments.append(remainder)
            return segments

        clauses: list[tuple[int, str, str]] = []
        if not semantic_lines:
            return clauses, {}, {}
        root_key = f"{semantic_lines[0][0]}:root"
        branch_roles = {root_key: "neutral"}
        branch_parents: dict[str, str | None] = {root_key: None}
        stack: list[tuple[int, str]] = []
        paragraph_branch = root_key
        for line_number, line in semantic_lines:
            marker = list_pattern.match(line)
            content = list_pattern.sub("", line, count=1).strip()
            punctuation_parts = re.split(
                r";(?=\s|$)"
                r"|(?<=[.!?])\s+(?=[A-Z0-9\[])"
                r"|,(?=\s+(?:Dataset|Data|Docs?|Documentation"
                r"|Guide|Reference|Input|Resource|Service)\s*:)",
                content,
            )
            segments = [
                segment
                for part in punctuation_parts
                for segment in label_segments(part)
                if segment
            ]
            if marker:
                indent = len(marker.group(1))
                while stack and stack[-1][0] >= indent:
                    stack.pop()
                parent_key = stack[-1][1] if stack else root_key
                line_role = entity_role(content)
                if not stack and not clauses:
                    line_key = root_key
                    branch_roles[root_key] = line_role
                elif line_role in {"docs", "resource"}:
                    line_key = f"{line_number}:item"
                    branch_roles[line_key] = line_role
                    branch_parents[line_key] = parent_key
                else:
                    line_key = parent_key
                stack.append((indent, line_key))
            else:
                line_key = stack[-1][1] if stack else paragraph_branch
            for segment_index, segment in enumerate(segments):
                role = entity_role(segment)
                if role in {"docs", "resource"} and (
                    branch_roles.get(line_key) != role
                ):
                    clause_key = (
                        f"{line_number}:clause:{segment_index}"
                    )
                    branch_roles[clause_key] = role
                    branch_parents[clause_key] = (
                        stack[-2][1]
                        if marker and len(stack) > 1
                        else root_key
                    )
                    if not marker:
                        paragraph_branch = clause_key
                else:
                    clause_key = line_key
                clauses.append((line_number, segment, clause_key))
        return clauses, branch_roles, branch_parents

    def scoped_resource_metadata(text: str) -> dict[str, Any]:
        checksums = {
            "sha256:" + value.lower()
            for value in re.findall(
                r"sha-?256\s*[:=]\s*(?:sha256:)?([0-9a-f]{64})",
                text,
                re.IGNORECASE,
            )
        }
        identities = {
            value
            for value in re.findall(
                r"(?:expected\s+)?identity\s*[:=]\s*"
                r"([A-Za-z0-9_.:/+-]+)",
                text,
                re.IGNORECASE,
            )
        }
        license_unavailable = bool(
            re.search(
                r"license(?:\s+authorization)?\s+is\s+not\s+provided"
                r"|no\s+license\s+authorization"
                r"|license\s*:\s*(?:unavailable|not\s+provided)",
                text,
                re.IGNORECASE,
            )
        )
        auth_unavailable = bool(
            re.search(
                r"(?:authentication|credentials?|api\s+token|login)"
                r"(?:\s+authorization)?\s+is\s+not\s+provided"
                r"|no\s+(?:authentication|credentials?|api\s+token)"
                r"|auth(?:entication)?\s*:\s*"
                r"(?:required|unavailable|not\s+provided)",
                text,
                re.IGNORECASE,
            )
        )
        license_match = re.search(
            r"\blicense\s*:\s*([^,;.\n]+)",
            text,
            re.IGNORECASE,
        )
        license_name = (
            license_match.group(1).strip()
            if license_match is not None and not license_unavailable
            else None
        )
        present = bool(
            checksums
            or identities
            or license_unavailable
            or auth_unavailable
            or license_name
        )
        return {
            "present": present,
            "ambiguous": (
                len(checksums) > 1
                or len(identities) > 1
                or (license_unavailable and auth_unavailable)
            ),
            "checksum": next(iter(checksums)) if len(checksums) == 1 else None,
            "identity": (
                next(iter(identities)) if len(identities) == 1 else None
            ),
            "license": license_name,
            "license_unavailable": license_unavailable,
            "auth_unavailable": auth_unavailable,
        }

    def explicitly_shared_metadata(text: str) -> bool:
        return bool(
            re.search(
                r"\b(?:both|all|each)\s+"
                r"(?:urls?|links?|mirrors?|resources?)\b"
                r"|\b(?:urls?|links?|mirrors?)\s+share\b"
                r"|\bsame\s+(?:checksum|identity|license|authorization)\b",
                text,
                re.IGNORECASE,
            )
        )

    section_scope_starts: dict[int, int] = {}
    for entry_index, (section_heading, entry) in enumerate(entries):
        section_key = (
            section_heading[0] if section_heading is not None else 0
        )
        heading_text = (
            section_heading[1].lower()
            if section_heading is not None
            else ""
        )
        entry_text = semantic_text(entry)
        heading_scope = (
            (
                direct_topic(heading_text)
                or bool(re.search(r"\bresources?\b", heading_text))
            )
            and bool(re.search(r"\b(?:all|every|each)\b", heading_text))
            and indispensable(heading_text)
            and no_scientific_equivalent(heading_text)
        )
        paragraph_scope = (
            (
                direct_topic(heading_text)
                or direct_topic(entry_text)
                or bool(re.search(r"\bresources?\b", entry_text))
            )
            and bool(re.search(r"\b(?:all|every|each)\b", entry_text))
            and bool(
                re.search(
                    r"\b(?:below|following|listed|in\s+this\s+section"
                    r"|contained)\b",
                    entry_text,
                )
            )
            and indispensable(entry_text)
            and no_scientific_equivalent(entry_text)
        )
        if heading_scope:
            section_scope_starts[section_key] = min(
                section_scope_starts.get(section_key, entry_index),
                entry_index,
            )
        elif paragraph_scope:
            section_scope_starts[section_key] = min(
                section_scope_starts.get(section_key, entry_index + 1),
                entry_index + 1,
            )

    resources: list[dict[str, Any]] = []
    for entry_index, (section_heading, entry) in enumerate(entries):
        semantic_lines = [
            (line_number, line)
            for line_number, line in entry
            if line_number not in fenced_lines
        ]
        entry_text = "\n".join(line for _, line in semantic_lines)
        lowered = entry_text.lower()
        heading_text = (
            section_heading[1].lower()
            if section_heading is not None
            else ""
        )
        heading_defines_direct_topic = direct_topic(heading_text)
        section_key = (
            section_heading[0] if section_heading is not None else 0
        )
        section_wide_declaration = entry_index >= section_scope_starts.get(
            section_key, len(entries)
        )
        software_only = (
            any(
                term in lowered
                for term in (
                    "software package",
                    "python package",
                    "library dependency",
                    "solver executable",
                )
            )
            and not any(
                term in lowered
                for term in (
                    "dataset",
                    "data file",
                    "input file",
                    "external service",
                )
            )
        )
        if software_only:
            continue
        clauses, branch_roles, branch_parents = markdown_clauses(
            semantic_lines
        )
        branch_metadata: dict[str, list[str]] = {}
        for _, clause, branch_key in clauses:
            if not extract_urls(clause):
                branch_metadata.setdefault(branch_key, []).append(
                    clause.lower()
                )

        def inherited_metadata(branch_key: str) -> str:
            keys = [branch_key]
            if branch_roles.get(branch_key) not in {"docs", "mixed"}:
                parent = branch_parents.get(branch_key)
                while parent is not None:
                    if branch_roles.get(parent) in {"docs", "mixed"}:
                        break
                    keys.append(parent)
                    parent = branch_parents.get(parent)
            return "\n".join(
                text
                for key in keys
                for text in branch_metadata.get(key, [])
            )
        branch_url_counts: dict[str, int] = {}
        for _, clause, branch_key in clauses:
            branch_url_counts[branch_key] = (
                branch_url_counts.get(branch_key, 0)
                + len(extract_urls(clause))
            )
        position = 0
        for line_number, clause, branch_key in clauses:
            clause_urls = extract_urls(clause)
            if not clause_urls:
                continue
            clause_lowered = clause.lower()
            local_critical = indispensable(clause_lowered)
            local_no_equivalent = no_scientific_equivalent(
                clause_lowered
            )
            local_optional = bool(
                re.search(
                    r"\b(?:optional|recommended)\b", clause_lowered
                )
            )
            if local_optional and (
                local_critical or local_no_equivalent
            ):
                continue
            shared_text = inherited_metadata(branch_key)
            shared_optional = bool(
                re.search(
                    r"\b(?:optional|recommended)\b", shared_text
                )
            )
            shared_critical = indispensable(shared_text)
            shared_no_equivalent = no_scientific_equivalent(shared_text)
            shared_direct = (
                direct_topic(shared_text)
                or data_resource_clause(shared_text)
                or branch_roles.get(branch_key) == "resource"
            )
            effective_critical = (
                local_critical
                or shared_critical
                or section_wide_declaration
            )
            effective_no_equivalent = (
                local_no_equivalent
                or shared_no_equivalent
                or section_wide_declaration
            )
            effective_direct = (
                direct_topic(clause_lowered)
                or data_resource_clause(clause_lowered)
                or shared_direct
                or heading_defines_direct_topic
                or section_wide_declaration
            )
            if (
                local_optional
                or shared_optional
                or not effective_critical
                or not effective_no_equivalent
                or not effective_direct
            ):
                continue
            local_metadata = scoped_resource_metadata(clause)
            shared_metadata = scoped_resource_metadata(shared_text)
            metadata_ambiguous = (
                local_metadata["ambiguous"]
                or shared_metadata["ambiguous"]
            )
            assigned_metadata: list[dict[str, Any]] = []
            if local_metadata["present"]:
                if len(clause_urls) == 1 or explicitly_shared_metadata(
                    clause
                ):
                    assigned_metadata.append(local_metadata)
                else:
                    metadata_ambiguous = True
            if shared_metadata["present"]:
                if branch_url_counts.get(branch_key, 0) == 1 or (
                    explicitly_shared_metadata(shared_text)
                ):
                    assigned_metadata.append(shared_metadata)
                else:
                    metadata_ambiguous = True
            checksums = {
                item["checksum"]
                for item in assigned_metadata
                if item["checksum"] is not None
            }
            identities = {
                item["identity"]
                for item in assigned_metadata
                if item["identity"] is not None
            }
            licenses = {
                item["license"]
                for item in assigned_metadata
                if item["license"] is not None
            }
            license_unavailable = any(
                item["license_unavailable"]
                for item in assigned_metadata
            )
            auth_unavailable = any(
                item["auth_unavailable"]
                for item in assigned_metadata
            )
            metadata_ambiguous = metadata_ambiguous or (
                len(checksums) > 1
                or len(identities) > 1
                or len(licenses) > 1
                or (license_unavailable and auth_unavailable)
            )
            for url in clause_urls:
                position += 1
                access: dict[str, Any] = {
                    "method": (
                        "url"
                        if metadata_ambiguous
                        else "license"
                        if license_unavailable
                        else "auth"
                        if auth_unavailable
                        else "url"
                    ),
                    "url": url,
                }
                if metadata_ambiguous:
                    access.update(
                        {
                            "metadata_status": "NOT_ASSESSABLE",
                            "metadata_reason": (
                                "ambiguous per-URL metadata scope"
                            ),
                        }
                    )
                else:
                    if checksums:
                        access["checksum"] = next(iter(checksums))
                    if identities:
                        access["expected_identity"] = next(
                            iter(identities)
                        )
                    if licenses or license_unavailable:
                        access["license"] = (
                            next(iter(licenses))
                            if licenses
                            else "instruction-declared-license"
                        )
                    if license_unavailable or auth_unavailable:
                        access["authorization_provided"] = False
                resources.append(
                    {
                        "id": (
                            f"instruction-direct-input-{line_number}-{position}"
                        ),
                        "name": "Indispensable direct instruction input",
                        "type": "file",
                        "role": "CRITICAL",
                        "required_level": "L4",
                        "access": access,
                        "_instruction_line": line_number,
                    }
                )
    return resources


def probe_resources(
    root: Path,
    output: Path,
    timeout: float,
    allow_private_network: bool = False,
) -> dict[str, Any]:
    instruction_path = root / "instruction.md"
    instruction = (
        instruction_path.read_text(encoding="utf-8", errors="replace")
        if instruction_path.is_file()
        else ""
    )
    resources = instruction_direct_inputs(instruction)
    reports: list[dict[str, Any]] = []
    findings: list[dict[str, Any]] = []
    for item in resources:
        if not isinstance(item, dict):
            raise ValueError("every resource declaration must be an object")
        report, item_findings = probe_item(
            root,
            item,
            timeout,
            allow_private_network,
        )
        report["declaration_source"] = "instruction.md"
        report["instruction_line"] = item["_instruction_line"]
        report["indispensable"] = True
        for finding_item in item_findings:
            finding_item["affected_files"] = ["instruction.md"]
            if report["status"] in {
                "REQUIRES_AUTH",
                "REQUIRES_LICENSE",
                "PERMANENT_UNAVAILABLE",
                "IDENTITY_MISMATCH",
            } and finding_item["code"] in {
                "COMMERCIAL_LICENSE_UNAVAILABLE",
                "RESOURCE_REQUIRES_AUTH",
                "CRITICAL_RESOURCE_UNAVAILABLE",
                "RESOURCE_IDENTITY_MISMATCH",
            }:
                finding_item["code"] = (
                    "INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE"
                )
                finding_item["severity"] = "FATAL"
            elif report["status"] in {
                "TRANSIENT_FAILURE",
                "RATE_LIMITED",
                "BLOCKED_PRIVATE_NETWORK",
            } and finding_item["code"] in {
                "RESOURCE_TRANSIENT_FAILURE",
                "RESOURCE_PRIVATE_NETWORK_BLOCKED",
            }:
                finding_item["code"] = (
                    "INDISPENSABLE_DIRECT_INPUT_" + report["status"]
                )
                finding_item["severity"] = "HIGH"
        reports.append(report)
        findings.extend(item_findings)
    e2_recommended = any(
        int(item["verified_level"][1:]) < int(item["required_level"][1:])
        or item["status"]
        in {
            "REQUIRES_AUTH",
            "REQUIRES_LICENSE",
            "PERMANENT_UNAVAILABLE",
            "IDENTITY_MISMATCH",
            "TRANSIENT_FAILURE",
            "RATE_LIMITED",
        }
        for item in reports
    )
    result = {
        "schema_version": "0.1",
        "status": (
            "FAIL"
            if any(item["severity"] == "FATAL" for item in findings)
            else "WARNING"
            if findings
            else "PASS"
        ),
        "summary": {
            "resource_count": len(reports),
            "finding_count": len(findings),
            "e2_recommended": e2_recommended,
        },
        "resources": reports,
        "findings": findings,
        "limitations": [
            "resources.json, manifest, steps, task, and environment declarations are not quality evidence",
            "only instruction text explicitly marking a direct input indispensable and without an equivalent is probed",
            "L6 requires verification inside the declared Harbor runtime",
            "license and terms-of-use conclusions use declared evidence only",
        ],
    }
    output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return result


def copy_runtime(root: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    instruction = root / "instruction.md"
    if instruction.is_file():
        shutil.copy2(instruction, destination / "instruction.md")
    if (root / "tests").is_dir():
        shutil.copytree(root / "tests", destination / "tests")


def run_e2_smoke(
    root: Path,
    plan_path: Path,
    resource_result: dict[str, Any],
) -> dict[str, Any]:
    resolved_plan = plan_path.expanduser().resolve()
    if resolved_plan.is_relative_to(root.resolve()):
        raise ValueError("E2 smoke plan must be outside the Harbor 题包")
    plan = read_json(resolved_plan)
    script_name = plan.get("script")
    if (
        not isinstance(script_name, str)
        or Path(script_name).name != script_name
    ):
        raise ValueError("E2 smoke script must be a filename beside the plan")
    script = (resolved_plan.parent / script_name).resolve()
    if script.is_relative_to(root.resolve()) or not script.is_file():
        raise ValueError("E2 smoke script must be an external file")
    verifies = plan.get("verifies_resources")
    if not isinstance(verifies, list) or not all(
        isinstance(item, str) for item in verifies
    ):
        raise ValueError("verifies_resources must be a string list")
    known_ids = {item["resource_id"] for item in resource_result["resources"]}
    unknown = sorted(set(verifies) - known_ids)
    if unknown:
        raise ValueError(f"unknown E2 resource ids: {unknown}")
    timeout = float(plan.get("timeout_sec", 60))
    if not math.isfinite(timeout) or not 0 < timeout <= 300:
        raise ValueError("E2 timeout_sec must be between 0 and 300")
    with tempfile.TemporaryDirectory(prefix="materials_e2_smoke_") as temporary:
        runtime = Path(temporary) / "package"
        copy_runtime(root, runtime)
        runtime_script = runtime / "e2_smoke.py"
        shutil.copy2(script, runtime_script)
        wrapper = """
import pathlib
import runpy
import sys

runtime = pathlib.Path(sys.argv[1]).resolve()
script = pathlib.Path(sys.argv[2]).resolve()
allowed_roots = {
    runtime,
    pathlib.Path(sys.base_prefix).resolve(),
    pathlib.Path(sys.exec_prefix).resolve(),
}

def audit_boundary(event, args):
    if event != "open" or not args:
        return
    target = args[0]
    if isinstance(target, int):
        return
    try:
        path = pathlib.Path(target)
    except TypeError:
        return
    if not path.is_absolute():
        path = pathlib.Path.cwd() / path
    resolved = path.resolve(strict=False)
    if not any(resolved.is_relative_to(root) for root in allowed_roots):
        raise PermissionError(
            f"E2 smoke cannot open files outside its isolated runtime: {resolved}"
        )

sys.addaudithook(audit_boundary)
runpy.run_path(str(script), run_name="__main__")
"""
        try:
            process = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-c",
                    wrapper,
                    str(runtime),
                    str(runtime_script),
                ],
                cwd=runtime,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
            )
            returncode: int | None = process.returncode
            stdout = process.stdout[-4000:]
            stderr = process.stderr[-4000:]
        except subprocess.TimeoutExpired as exc:
            returncode = None
            stdout = (exc.stdout or "")[-4000:]
            stderr = ((exc.stderr or "") + "\nE2 smoke timed out.")[-4000:]

        exercised: list[str] = []
        result_error: str | None = None
        result_path = runtime / "e2_smoke_result.json"
        if returncode == 0:
            try:
                smoke_result = read_json(result_path)
                raw_exercised = smoke_result.get("exercised_resources")
                if not isinstance(raw_exercised, list) or not all(
                    isinstance(item, str) for item in raw_exercised
                ):
                    raise ValueError(
                        "exercised_resources must be a string list"
                    )
                exercised = list(dict.fromkeys(raw_exercised))
                missing = sorted(set(verifies) - set(exercised))
                if missing:
                    raise ValueError(
                        f"smoke evidence omits planned resources: {missing}"
                    )
            except (
                FileNotFoundError,
                TypeError,
                ValueError,
                json.JSONDecodeError,
            ) as exc:
                result_error = str(exc)
    status = (
        "PASS"
        if returncode == 0 and result_error is None
        else "FAIL"
    )
    return {
        "status": status,
        "claim": "SMOKE_RUN",
        "scientific_reproduction": False,
        "environment": "AUDIT_HOST_ISOLATED_COPY",
        "environment_verified": False,
        "verifies_resources": verifies,
        "exercised_resources": exercised,
        "returncode": returncode,
        "stdout": stdout,
        "stderr": stderr,
        "result_error": result_error,
        "reason": (
            "The minimal workflow started successfully on an isolated audit-host copy; "
            "this does not establish scientific reproduction or Harbor-container access."
            if status == "PASS"
            else (
                "The E2 smoke failed on the isolated audit-host copy: "
                + (
                    result_error
                    or stderr.strip()
                    or f"return code {returncode}"
                )
            )
        ),
    }
