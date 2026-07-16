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
    """Parse explicit direct-input declarations within Markdown blocks."""
    blocks: list[list[tuple[int, str]]] = []
    current: list[tuple[int, str]] = []
    for line_number, line in enumerate(instruction.splitlines(), start=1):
        if re.match(r"^\s*#{1,6}\s+", line) and current:
            blocks.append(current)
            current = [(line_number, line)]
        elif line.strip():
            current.append((line_number, line))
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)

    resources: list[dict[str, Any]] = []
    for block in blocks:
        position = 0
        for line_index, (line_number, line) in enumerate(block):
            for url in re.findall(r"https?://[^\s)\]}>]+", line):
                context = block[
                    max(0, line_index - 5) : min(
                        len(block), line_index + 3
                    )
                ]
                lowered = "\n".join(
                    context_line for _, context_line in context
                ).lower()
                explicitly_direct = (
                    "indispensable direct input" in lowered
                    or (
                        "direct input" in lowered
                        and any(
                            term in lowered
                            for term in (
                                "indispensable",
                                "required",
                                "must",
                                "必要",
                            )
                        )
                    )
                )
                no_equivalent = any(
                    term in lowered
                    for term in (
                        "no equivalent",
                        "without equivalent",
                        "no scientifically equivalent",
                        "不可替代",
                    )
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
                if (
                    not (explicitly_direct and no_equivalent)
                    or software_only
                ):
                    continue
                checksum_match = re.search(
                    r"sha-?256\s*[:=]\s*(?:sha256:)?([0-9a-f]{64})",
                    lowered,
                )
                no_agent_license = (
                    "license authorization is not provided to the solving agent"
                    in lowered
                    or "solving agent has no license authorization" in lowered
                )
                position += 1
                access = (
                    {
                        "method": "license",
                        "license": "instruction-declared-license",
                        "url": url.rstrip(".,;"),
                        "authorization_provided": False,
                    }
                    if no_agent_license
                    else {
                        "method": "url",
                        "url": url.rstrip(".,;"),
                        **(
                            {
                                "checksum": (
                                    "sha256:" + checksum_match.group(1)
                                )
                            }
                            if checksum_match
                            else {}
                        ),
                    }
                )
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
