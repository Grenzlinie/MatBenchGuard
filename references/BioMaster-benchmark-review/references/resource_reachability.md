# Resource identity, reachability, and sufficiency

## Resource roles

- `CRITICAL`: no valid answer is possible without it.
- `REPLACEABLE`: a stable, equivalent source is allowed.
- `OPTIONAL`: absence does not block completion.

## Reachability levels

- `L0 DECLARED_ONLY`: name only; no identifier or endpoint.
- `L1 HOMEPAGE_REACHABLE`: a website opens, but no exact artifact is identified.
- `L2 METADATA_RESOLVED`: accession or persistent identifier resolves to matching metadata.
- `L3 ARTIFACT_DISCOVERED`: exact file, API object, or object ID is identified.
- `L4 ARTIFACT_DOWNLOADABLE`: non-empty data can be fetched without manual interaction.
- `L5 IDENTITY_VERIFIED`: version, size, checksum, sample count, organism, build, and content type match.
- `L6 ENVIRONMENT_VERIFIED`: access succeeds from the benchmark runtime.

A core resource normally requires L4. Exact reproduction normally requires L5 or L6.

## Required checks

Record where applicable:

- identifier, version, organism, strain, tissue, condition, assay, reference build;
- sample and file counts;
- filenames, sizes, checksum, ETag, and Last-Modified;
- redirect chain and actual content type;
- license, authentication, click-through, CAPTCHA, manual approval, rate limits, and automated-access restrictions;
- test timestamp, host, and runtime environment;
- mirrors, archives, and immutable snapshots;
- failure class: DNS, TLS, timeout, rate limit, 4xx, 5xx, login, license, missing object, or identity mismatch.

Do not confuse homepage access with artifact access. Retry misleading HEAD requests using a small GET Range request. Do not treat a transient network failure as permanent disappearance without retries and environment context.

## Software and environment

Verify ecosystem, package, exact version, operating system, architecture, external binaries, shared libraries, GPU support, solver capability, license, and an installable lock file or container digest.

A package name alone is not a reproducible environment. Confirm that the declared solver supports the mathematical problem actually used.

## Data sufficiency

Reachable data may still be insufficient. Verify the presence of all load-bearing assets, such as sample sheets, group labels, references, annotations, indexes, blacklists, weights, tokenizers, supplementary models, biomass definitions, reaction mappings, manual curation tables, fixed splits, controls, calibration files, and checker references.
