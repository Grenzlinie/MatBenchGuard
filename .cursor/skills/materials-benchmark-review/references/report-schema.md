# Review decision schema

Write `agent_final_decision.json` outside the Harbor package using
`materials-agent-final-decision/2.3` and the bundled template. Version 2.2 and
older records are not accepted; re-audit them before validation.

Required sections:

- package identity, mode, reproduction intent, and verdict;
- all eight criteria with status, rationale, and structured evidence;
- C01–C07 normalized scores and positive evidence;
- exactly six Hard Gates, each with `code`, `status`, `disposition`, rationale,
  evidence, and `failure_modes`;
- all eleven checker probe classes;
- all five readiness categories plus required resource records;
- parameter assessment covering fixed/source-required, derived/coupled,
  representation-equivalent, and solver-selectable choices. Each parameter
  records source status, value/rule, dependencies, consumers, scoring impact,
  execution necessity, paper-reference dependency, resolution, and evidence;
- all required `scientific_risk_patterns`, each with canonical criterion,
  status, rationale, and evidence;
- confirmed findings and diagnostic adjudications. Every confirmed finding has
  `disposition` (`REPAIR` or `ABANDON`), `hard_gate_code` (canonical code or
  `null`), and `failure_modes` (normally empty).
- limitations and reviewed scope.

Also retain `mechanical_evidence.json` and `checker_observations.json` (or record
why a collector was inapplicable). Cite their observation IDs in the Agent
decision where they support a conclusion; never copy candidates directly into
findings without adjudication.

Every applicable checker probe must cite an exact raw observation `case_id`.
Validate the decision with all builtin and task-specific observation files:

```bash
python .cursor/skills/materials-benchmark-review/scripts/validate_agent_decision.py \
  agent_final_decision.json \
  --probe-observations evidence/checker_observations.json \
  --probe-observations evidence/task_specific_observations.json
```

The validator rejects declared `PASS`/`FAIL` probe states that lack an executed
`OBSERVED` case and rejects `NOT_ASSESSABLE` without a matching raw
`NOT_ASSESSED`/`UNUSABLE` record.

Every failed scientific pattern must fail its mapped criterion and have a
matching confirmed finding with the same `pattern_id`. A pattern evidence gap
forces `NOT_ASSESSABLE`; `NOT_APPLICABLE` requires an explicit rationale and
evidence.

Evidence items contain `source_kind`, `path`, `locator`, and `quote_or_result`.
The validator checks record completeness, score arithmetic, readiness/probe
gates, and verdict consistency. It deliberately does not parse the package or
reinterpret the Agent's science.

`SCIENTIFIC_REASONING_ABSENT` maps to C03. When it fails, its disposition and
the matching confirmed finding must be `ABANDON`; the finding is non-repairable,
the decision is `REJECT`, and `failure_modes` contains one or both of
`PURE_INFORMATION_EXTRACTION` and `PURE_ALGEBRAIC_COMPUTATION`.

`ESSENTIAL_SIMULATION_PARAMETER_UNAVAILABLE` also maps to C03. A paper-required
essential `MISSING` parameter and this Gate must agree. Failure requires
`SIMULATION_CONTRACT_UNDERDETERMINED` FAIL, a matching non-repairable `ABANDON`
finding, and verdict `REJECT`.
