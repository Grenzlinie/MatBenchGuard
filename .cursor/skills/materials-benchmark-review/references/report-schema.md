# Review decision schema

Write `agent_final_decision.json` outside the Harbor package using
`materials-agent-final-decision/2.0` and the bundled template.

Required sections:

- package identity, mode, reproduction intent, and verdict;
- all eight criteria with status, rationale, and structured evidence;
- C01–C07 normalized scores and positive evidence;
- exactly four Hard Gates;
- all eleven checker probe classes;
- all five readiness categories plus required resource records;
- parameter assessment covering fixed/source-required and solver-selectable
  choices;
- confirmed findings and diagnostic adjudications;
- limitations and reviewed scope.

Also retain `mechanical_evidence.json` and `checker_observations.json` (or record
why a collector was inapplicable). Cite their observation IDs in the Agent
decision where they support a conclusion; never copy candidates directly into
findings without adjudication.

Evidence items contain `source_kind`, `path`, `locator`, and `quote_or_result`.
The validator checks record completeness, score arithmetic, readiness/probe
gates, and verdict consistency. It deliberately does not parse the package or
reinterpret the Agent's science.
