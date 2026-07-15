# Materials resource policy

Resource availability has six independent evidence levels:

- `L0 DECLARED_ONLY` — a name exists without a resolvable object.
- `L1 HOMEPAGE_REACHABLE` — a site opens, but no exact artifact is named.
- `L2 METADATA_RESOLVED` — package or accession metadata resolves and matches.
- `L3 ARTIFACT_DISCOVERED` — an exact file or object endpoint is identified.
- `L4 ARTIFACT_DOWNLOADABLE` — non-empty artifact bytes are retrievable.
- `L5 IDENTITY_VERIFIED` — checksum or equivalent immutable identity matches.
- `L6 ENVIRONMENT_VERIFIED` — access succeeds inside the declared Harbor runtime.

Never infer a higher level from a lower one. In particular, an audit-host E2
smoke is not L6.

## Roles

- `CRITICAL` — no valid answer is possible without the resource.
- `REPLACEABLE` — a scientifically equivalent source is permitted.
- `OPTIONAL` — absence does not block the task.

If no role is declared, treat the resource as `CRITICAL`. A critical file,
dataset, structure, potential, pseudopotential, or basis set normally requires
at least L4. A tool or package normally requires L2 plus a pinned version.

## Materials resource categories

- **Materials database / structure ID** — resolve the exact accession metadata,
  then identify and retrieve the structure artifact. A database homepage is L1.
- **Potential / pseudopotential / basis set** — require an exact file, method or
  functional compatibility, version, and preferably checksum. A repository
  homepage is insufficient.
- **Package / open-source tool** — resolve registry metadata, pin version, and
  verify required capabilities and external binaries.
- **Commercial software** — record license type and whether automation
  authorization is actually available. Naming VASP, DMol, COMSOL, or another
  commercial solver without authorization is not access.
- **Inline resource** — verify that every load-bearing constant, unit, and
  condition is present through exact quotes from public task roles. An inline
  declaration without this evidence remains L0; inline evidence does not prove
  paper fidelity.

## Failure classes

- DNS, TLS, timeout, connection refusal, HTTP 5xx, and rate limiting are
  transient until retried with environment context.
- HTTP 401/403 means `REQUIRES_AUTH`; it is not a transient outage.
- HTTP 404/410 means `PERMANENT_UNAVAILABLE` for the declared endpoint.
- A checksum or accession mismatch means `IDENTITY_MISMATCH`.
- Missing commercial authorization means `REQUIRES_LICENSE`.

Do not turn a transient failure into abandonment without retries. A critical
permanent, authentication, license, or identity failure triggers a Hard gate.
Resource probes retry transient DNS, TLS, timeout, server, and rate-limit
failures before classification. URLs containing credentials or resolving to
private, loopback, link-local, multicast, reserved, or unspecified addresses
are blocked unless an operator explicitly enables a controlled private test
network.

Any resource below its declared required level produces a finding. Critical
under-verification is not silently reduced to an E2 recommendation. Package
identity includes the declared version when registry metadata exposes it;
potential, pseudopotential, and basis declarations must state version and
compatibility context.

## E2 smoke

E2 uses an Agent-authored JSON plan and Python script stored outside the Harbor
题包. The plan names the script, timeout, and resource IDs it exercises. The
runner executes the script with Python isolated mode in a copied runtime that
contains no `solution/`.

The script writes `e2_smoke_result.json` in the copied runtime:

```json
{"exercised_resources": ["resource-id"]}
```

Every planned resource must appear in this evidence. The runner blocks direct
Python file access outside the copied runtime and interpreter installation. A failed,
timed-out, boundary-violating, or unsubstantiated smoke creates
`E2_SMOKE_FAILED` and fails the execution gate.

Successful E2 evidence means only that the minimal workflow started on the
recorded environment. It sets:

- `claim: SMOKE_RUN`
- `scientific_reproduction: false`
- `environment_verified: false` for audit-host execution

Only a future runner that actually executes inside the declared Harbor
container may assign L6.
