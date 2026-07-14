# Biological admissibility and capability alignment

## Classification

### BIO_CORE

The biological question is the central object of evaluation. Passing requires reasoning about biological entities, data generation, domain methods, and a biological endpoint.

### BIO_METHOD

The task primarily evaluates a computational method used in biology, and biological choices materially affect correctness.

### BIO_WRAPPER

Biological labels are present, but the scored work is generic copying, formatting, file conversion, or arithmetic. Relabeling the entities would not change the solution.

### NON_BIO

No material biological object, data, operation, or endpoint is involved.

### AMBIGUOUS

Core evidence is missing or biological and generic objectives are inseparable.

## Evidence axes

Score each 0-2 and cite evidence:

1. Biological object: organism, cell, tissue, gene, transcript, protein, pathway, phenotype, biospecimen, ecosystem.
2. Biological data: sequencing, expression, variants, structures, images, assays, networks, phylogeny, curated annotation.
3. Biological operation: alignment, assembly, quantification, statistical contrast, annotation, simulation, modeling, mechanistic inference.
4. Biological endpoint: function, phenotype, pathway, growth, response, structure, interaction, lineage, diagnosis, ecology.
5. Domain dependence: a competent generic programmer cannot reliably pass without biological or bioinformatics knowledge.

Suggested guide:

- `BIO_CORE`: at least 7/10, including endpoint and domain dependence.
- `BIO_METHOD`: at least 5/10, including operation and domain dependence.
- `BIO_WRAPPER`: biological words exist but domain dependence is 0.
- `NON_BIO`: 0-2/10.
- `AMBIGUOUS`: conflicting or missing evidence.

The score guides review; semantic judgment is final.

## Capability alignment

Extract primary, secondary, and explicitly excluded capabilities. Map:

```text
claimed capability
→ indispensable scientific operation
→ observable output
→ checker-enforced evidence
```

A broken link is a construct-validity defect. Passing by copying paper values, formatting files, or omitting the claimed model or workflow is fatal.

## Answer-type alignment

Classify the expected answer:

- deterministic exact;
- tolerance based;
- set valued;
- ranking based;
- evidence based;
- open ended.

Require checker semantics appropriate to that type. Multiple valid models, annotations, rankings, or feature sets must not be reduced to one exact artifact without a defensible equivalence rule.
