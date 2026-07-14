# Checker validity, gold quality, and dynamic testing

## Static enforcement map

Build this table for every load-bearing requirement:

```text
instruction requirement
→ required process or result
→ submitted evidence
→ checker read path
→ score contribution
```

Flag requirements that are declared but not read, read but not scored, or scored only through a hard-coded reported number.

## Score semantics

Check:

- metric direction;
- tolerance basis;
- partial-credit behavior;
- missing, duplicate, invalid, NaN, and Inf handling;
- whether one component can independently pass;
- whether file length or ordering improperly changes score;
- whether output quality is compressed into all-or-none behavior;
- whether the final reward actually includes every declared component.

## Gold standard

Record:

- source type: experimental, curated, computational proxy, or figure digitization;
- provenance chain;
- independence from the method being evaluated;
- uncertainty, measurement error, annotation disagreement, or digitization error;
- scientific basis for tolerance;
- whether the gold represents biological truth or only agreement with one tool.

## Dynamic probes

Always test missing, empty, malformed, duplicate, irrelevant, non-finite, random, constant, minimal gold-shaped, threshold-boundary, and supporting-evidence-omission cases.

Add quality-gradient tests. Scores should generally improve as correctness increases. Evaluate monotonicity, sensitivity, specificity, and saturation.

Add metamorphic tests for semantic invariants. Examples:

- row ordering should not matter;
- harmless metadata changes should not matter;
- equivalent serialization should not matter;
- synchronized matrix row or column permutations should preserve results;
- object ordering in SBML, PDB, JSON, or XML should not change scientific score.

## Domain-specific attacks

- BED or intervals: whole-chromosome coverage, mega-peaks, duplicates, wrong genome build.
- VCF: coordinate shift, REF/ALT mismatch, multiallelic handling, normalization.
- Classification: all-positive, all-negative, constant predictions, truncated output.
- Ranking: reversed scores, duplicate candidates, short top-k output.
- Count matrices: all zero, constant matrix, ID duplication, cell or gene reorder.
- Protein or structure: illegal residues, length mismatch, chain mismatch, partial structures.
- Metabolic model: omitted model, empty model, infeasible model, wrong objective, gene-reaction confusion.

A checker that passes a submission omitting the claimed scientific artifact has a fatal enforcement gap.
