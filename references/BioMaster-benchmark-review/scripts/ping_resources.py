#!/usr/bin/env python3
"""Resolve and probe benchmark resources without downloading full datasets."""

from __future__ import annotations

import argparse
import json
import os
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

USER_AGENT = "benchmark-biology-auditor/1.0"
TIMEOUT = 8


def load_resources(path: Path) -> tuple[Path, dict[str, Any]]:
    path = path.expanduser().resolve()
    if path.is_dir():
        path = path / "resources.json"
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8") as f:
        return path, json.load(f)


def request(url: str, method: str = "HEAD", range_bytes: bool = False) -> dict[str, Any]:
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if range_bytes:
        headers["Range"] = "bytes=0-1023"
    req = urllib.request.Request(url, method=method, headers=headers)
    started = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = b""
            if method != "HEAD":
                body = resp.read(1024)
            return {
                "ok": 200 <= resp.status < 400,
                "status": resp.status,
                "final_url": resp.geturl(),
                "content_type": resp.headers.get("Content-Type"),
                "content_length": resp.headers.get("Content-Length"),
                "etag": resp.headers.get("ETag"),
                "last_modified": resp.headers.get("Last-Modified"),
                "sample_bytes": len(body),
                "elapsed_sec": round(time.time() - started, 3),
            }
    except urllib.error.HTTPError as exc:
        return {
            "ok": False,
            "status": exc.code,
            "final_url": exc.geturl(),
            "error_class": "http",
            "error": str(exc),
            "elapsed_sec": round(time.time() - started, 3),
        }
    except urllib.error.URLError as exc:
        reason = exc.reason
        if isinstance(reason, socket.gaierror):
            cls = "dns"
        elif isinstance(reason, ssl.SSLError):
            cls = "tls"
        elif isinstance(reason, TimeoutError):
            cls = "timeout"
        else:
            cls = "network"
        return {
            "ok": False,
            "status": None,
            "final_url": url,
            "error_class": cls,
            "error": str(exc),
            "elapsed_sec": round(time.time() - started, 3),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "ok": False,
            "status": None,
            "final_url": url,
            "error_class": "unexpected",
            "error": repr(exc),
            "elapsed_sec": round(time.time() - started, 3),
        }


def probe_url(url: str) -> dict[str, Any]:
    parsed = urllib.parse.urlparse(url)
    homepage_only = parsed.path in {"", "/"} and not parsed.query
    head = request(url, "HEAD")
    get = None
    if not head.get("ok") or head.get("status") in {403, 405} or homepage_only:
        get = request(url, "GET", range_bytes=True)
    effective = get if get and get.get("ok") else head
    reachable = bool(effective.get("ok"))
    level = 1 if reachable else 0
    if reachable and not homepage_only:
        level = 3
        if (get or {}).get("sample_bytes", 0) > 0:
            level = 4
    return {
        "declared_url": url,
        "homepage_only": homepage_only,
        "head": head,
        "range_get": get,
        "highest_verified_level": level,
        "status": "reachable_but_underspecified" if reachable and homepage_only else "reachable" if reachable else "unreachable",
    }


def accession_endpoints(accession: str) -> list[tuple[str, str]]:
    acc = accession.strip()
    upper = acc.upper()
    if re.match(r"^(GCA|GCF)_\d+\.\d+$", upper):
        return [
            ("ncbi_datasets_report", f"https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/{upper}/dataset_report"),
            ("ncbi_datasets_page", f"https://www.ncbi.nlm.nih.gov/datasets/genome/{upper}/"),
        ]
    if re.match(r"^(GSE|GSM|GPL)\d+$", upper):
        return [("ncbi_geo", f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={upper}&targ=self&form=text&view=full")]
    if re.match(r"^(SRR|ERR|DRR|SRP|ERP|DRP|SRS|ERS|DRS|SRX|ERX|DRX)\d+$", upper):
        return [
            ("sra_runinfo", f"https://trace.ncbi.nlm.nih.gov/Traces/sra-db-be/runinfo?acc={upper}"),
            ("ncbi_sra", f"https://www.ncbi.nlm.nih.gov/sra/?term={upper}"),
        ]
    if re.match(r"^(ENCSR|ENCFF)[A-Z0-9]+$", upper):
        return [("encode_json", f"https://www.encodeproject.org/{upper}/?format=json")]
    if re.match(r"^[0-9A-Z]{4}$", upper):
        return [("rcsb_entry", f"https://data.rcsb.org/rest/v1/core/entry/{upper}")]
    if re.match(r"^[OPQ][0-9][A-Z0-9]{3}[0-9]$", upper):
        return [("uniprot_json", f"https://rest.uniprot.org/uniprotkb/{upper}.json")]
    return []


def probe_accession(accession: str) -> dict[str, Any]:
    endpoints = accession_endpoints(accession)
    if not endpoints:
        return {
            "accession": accession,
            "status": "unsupported_accession_pattern",
            "highest_verified_level": 0,
            "endpoints": [],
        }
    results = []
    best = 0
    for name, url in endpoints:
        probe = probe_url(url)
        if probe["highest_verified_level"] >= 3:
            best = max(best, 2)
        if (probe.get("range_get") or {}).get("sample_bytes", 0) > 0:
            best = max(best, 2)
        results.append({"name": name, "probe": probe})
    return {
        "accession": accession,
        "status": "metadata_resolved" if best >= 2 else "unresolved",
        "highest_verified_level": best,
        "endpoints": results,
        "note": "metadata resolution does not prove that all required artifacts are downloadable",
    }


def probe_package(package: str, access: dict[str, Any]) -> dict[str, Any]:
    ecosystem = str(access.get("ecosystem", "")).lower().strip()
    version = access.get("version")
    result: dict[str, Any] = {
        "package": package,
        "ecosystem": ecosystem or None,
        "version": version,
        "highest_verified_level": 0,
    }
    if not ecosystem:
        result["status"] = "ecosystem_unspecified"
        result["probes"] = {
            "pypi": probe_url(f"https://pypi.org/pypi/{urllib.parse.quote(package)}/json")
        }
        if result["probes"]["pypi"]["highest_verified_level"] >= 3:
            result["highest_verified_level"] = 2
        return result
    if ecosystem in {"pip", "pypi"}:
        probe = probe_url(f"https://pypi.org/pypi/{urllib.parse.quote(package)}/json")
        result["probes"] = {"pypi": probe}
        result["status"] = "metadata_resolved" if probe["highest_verified_level"] >= 3 else "unresolved"
        result["highest_verified_level"] = 2 if probe["highest_verified_level"] >= 3 else 0
    elif ecosystem in {"conda", "conda-forge"}:
        probe = probe_url(f"https://api.anaconda.org/package/conda-forge/{urllib.parse.quote(package)}")
        result["probes"] = {"conda_forge": probe}
        result["status"] = "metadata_resolved" if probe["highest_verified_level"] >= 3 else "unresolved"
        result["highest_verified_level"] = 2 if probe["highest_verified_level"] >= 3 else 0
    else:
        result["status"] = "unsupported_ecosystem"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="benchmark directory or resources.json")
    parser.add_argument("--output", default="resource_report.json")
    args = parser.parse_args()

    try:
        source, data = load_resources(Path(args.input))
        resources = data.get("resources", []) if isinstance(data, dict) else []
        def probe_item(item: dict[str, Any]) -> dict[str, Any]:
            access = item.get("access", {}) or {}
            method = str(access.get("method", "")).lower()
            if method == "url":
                detail = probe_url(str(access.get("url", "")))
            elif method == "accession":
                detail = probe_accession(str(access.get("accession", "")))
            elif method == "package":
                detail = probe_package(str(access.get("package", "")), access)
            else:
                detail = {
                    "status": "unsupported_or_undeclared_method",
                    "highest_verified_level": 0,
                    "method": method or None,
                }
            level = int(detail.get("highest_verified_level", 0) or 0)
            raw_status = str(detail.get("status", ""))
            if level >= 4:
                status = "AVAILABLE"
            elif level > 0:
                status = "PARTIALLY_AVAILABLE"
            elif raw_status in {"unreachable", "unresolved"}:
                status = "TRANSIENT_FAILURE"
            else:
                status = "NOT_TESTED"
            identifier = access.get("accession") or access.get("package") or access.get("url")
            return {
                "resource_id": item.get("id"),
                "role": str(item.get("role", "CRITICAL")).upper(),
                "name": item.get("name"),
                "type": item.get("type"),
                "identifier": identifier,
                "declared_url": access.get("url"),
                "required_level": item.get("required_level", "L4" if str(item.get("role", "CRITICAL")).upper() == "CRITICAL" else "L2"),
                "verified_level": f"L{level}",
                "status": status,
                "identity_match": None,
                "tested_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "test_environment": socket.gethostname(),
                "attempts": 1,
                "evidence": [],
                "error_type": detail.get("error_class"),
                "access": access,
                "probe": detail,
            }

        workers = min(8, max(1, len(resources)))
        with ThreadPoolExecutor(max_workers=workers) as pool:
            reports = list(pool.map(probe_item, resources))

        summary = {
            "resources": len(reports),
            "unreachable_or_unresolved": sum(r["probe"].get("highest_verified_level", 0) == 0 for r in reports),
            "homepage_only": sum(bool(r["probe"].get("homepage_only")) for r in reports),
            "metadata_only": sum(r["probe"].get("highest_verified_level", 0) == 2 for r in reports),
        }
        output = {
            "schema_version": "1.0",
            "source": str(source),
            "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "review_host": socket.gethostname(),
            "summary": summary,
            "resources": reports,
            "limitations": [
                "this probe downloads at most a small byte range",
                "metadata resolution does not verify complete data identity",
                "rerun inside the benchmark container for environment-level reachability",
                "license, authentication, and terms of use may require manual review",
            ],
        }
        Path(args.output).write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"summary": summary, "output": args.output}, indent=2))
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"resource probe failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
