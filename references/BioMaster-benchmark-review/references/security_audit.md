# Benchmark and checker security audit

Inspect untrusted archives, submissions, and checker code in an isolated environment.

Check for:

- ZIP path traversal, symlink escapes, decompression bombs, huge file counts, and unexpected executables;
- `eval`, `exec`, unsafe imports, dynamic code loading, and shell injection;
- unsafe pickle, joblib, torch, YAML, XML, or model deserialization;
- XML external entities and entity expansion;
- arbitrary filesystem reads, environment-variable disclosure, hidden-test access, and path traversal;
- uncontrolled network access or data exfiltration;
- subprocess execution without argument isolation;
- fork bombs, unbounded threads, memory, disk, CPU, recursion, and output size;
- submission-controlled paths, filenames, archive members, or commands;
- credentials, cookies, tokens, private URLs, or personal data in logs and reports.

Use safe loaders, explicit allowlists, size limits, timeouts, process isolation, read-only hidden tests, disabled network unless required, and sanitized logs.

A checker that allows a submission to read hidden gold or execute arbitrary host code is fatal because it invalidates both safety and benchmark fairness.
