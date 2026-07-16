# Indispensable direct-input policy

`resources.json`, environment declarations, package metadata, and paper
software lists are not review evidence and are never scored.

Probe an external object only when instruction itself makes all of these true:

1. it is a direct input or service consumed by the requested task;
2. it is indispensable to construct a valid answer;
3. no scientifically equivalent source or implementation is allowed.

These declarations may span adjacent Markdown lines in one instruction block;
the direct-input role, indispensability, no-equivalent statement, and locator
must all be explicit. Do not infer them from package metadata. A runtime
software dependency is not a direct data/service input merely because the
instruction requires that software.

Examples that may qualify: a named private training dataset, an immutable
experimental file used directly for fitting, or an unavoidable remote service.

Do not probe:

- structures, trajectories, models, or intermediate files the solver is
  expected to generate;
- ordinary DFT/MD meshes, cutoffs, convergence criteria, seeds, supercells, or
  search parameters left to the solver;
- software when an equivalent implementation is permitted;
- a paper's historical software, version, or parameter list;
- optional or replaceable references.

## Verification

Record the exact instruction line, sanitized locator, reachability, identity
when available, and failure class. Retry transient DNS, TLS, timeout, server,
and rate-limit failures. Block credential-bearing and private-network URLs
unless a controlled fixture explicitly enables them.

A permanently unavailable, authorization-gated, license-gated, or
identity-mismatched indispensable direct input with no equivalent triggers
`INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE`, one of the four Hard Gates. Transient
audit-host failure is temporary `NOT_ASSESSABLE`, not a scientific rejection.

An E2 audit-host smoke may show only that a minimal process starts. It does not
establish scientific reproduction, Harbor-environment equivalence, or L6.
