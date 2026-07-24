# Security and anti-gaming audit

Check archive paths, symlinks, unsafe deserialization, YAML/XML parsing,
subprocess and shell construction, path traversal, unbounded reads, filesystem
escape, network use, resource limits, and hidden-answer access.

Probe malformed files, duplicate identifiers, NaN/Inf, oversized/sparse input,
unexpected encodings, extra fields, missing artifacts, and output-path tricks.
The checker must fail safely without granting credit or exposing protected data.
These are checker `AUTO_FIX` targets when rejection behavior is uniquely
determined; NaN/Inf, wrong types, missing fields, duplicate identifiers, invalid
formats, or unsafe parsing do not independently justify abandonment.

An automation failure is not a security finding until reproduced from the
package. Record tool limitations separately.
