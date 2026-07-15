# Nested vs. Un-nested System Readiness Level Calculation

## Problem background
System Readiness Assessment (SRA) methods evaluate the development status of complex systems of emerging technologies. The System Readiness Level (SRL) combines Technology Readiness Levels (TRLs) of components and Integration Readiness Levels (IRLs) of their interfaces into a composite score. Nesting treats a subsystem of components as a single entity with an Equivalent TRL (ETRL). This task analyzes the impact of nesting on the computed SRL for an advanced power plant that incorporates an Advanced Combustion and Carbon Capture (ACCC) subsystem.

## Approach
The composite SRL for a (sub)system is calculated from a digraph representation: each node is a technology with a TRL estimate, each directed edge is an interface with an IRL estimate. The formula is SRLc = (TRL_vector × IRL_matrix × TRL_vector^T) / (TRL_vector × TRL_vector^T).

First, the ACCC subsystem is evaluated independently—its composite SRL is computed and then converted to an Equivalent TRL (ETRL) using a bunded SRL Translation Table that maps SRL ranges to integer TRL levels. Next, the power plant system SRL is computed twice: once with the ACCC nested (treated as a single component at the ETRL with assigned external interfaces) and once without nesting (all ACCC components kept separate with their own TRLs and all interfaces). The necessary TRL vectors and IRL matrices are constructed from the bundled digraph data and system interface definitions.

## Reproduction target
Compute and report three composite SRL scores:
1. The composite SRL of the ACCC subsystem.
2. The composite SRL of the nested power plant system.
3. The composite SRL of the un-nested power plant system.
All values must be calculated using the provided digraph data and the SRL Translation Table.

## Assets

- ACCC subsystem digraph and TRL/IRL data
- System interfaces for nested and un-nested models
- SRL Translation Table (Table I)
- numpy: numpy

## Workflow steps

### Step 1: Load ACCC subsystem data and construct matrices
- Role: process
- Action: Read the bundled ACCC digraph data file. Extract the TRL vector and the IRL adjacency matrix for the subsystem components.
- Evidence: none

### Step 2: Compute ACCC subsystem composite SRL
- Role: scored
- Action: Compute the composite SRL using the matrix normalization formula: SRLc = (TRL_vector * IRL_matrix * TRL_vector^T) / (TRL_vector * TRL_vector^T). Write the resulting number to the output file.
- Output file: `/app/outputs/accc_subsystem_srl.txt`
- Format: txt
- Contract: A single floating-point number representing the composite SRL score.
- Scoring: scored by hidden verifier

### Step 3: Translate ACCC SRL to Equivalent TRL
- Role: process
- Action: Read the bundled SRL Translation Table, find the ETRL range containing the computed ACCC subsystem SRL, and assign the corresponding ETRL integer.
- Evidence: none

### Step 4: Prepare nested system matrices
- Role: process
- Action: Using the bundled system interfaces file, construct the TRL vector for the nested system (replacing the ACCC components with the ETRL value) and the IRL matrix including external interfaces for the nested configuration.
- Evidence: none

### Step 5: Compute nested system composite SRL
- Role: scored (load-bearing)
- Action: Compute the composite SRL for the nested power plant system using the nested TRL vector and IRL matrix, then write the result.
- Output file: `/app/outputs/nested_system_srl.txt`
- Format: txt
- Contract: A single floating-point number representing the nested composite SRL score.
- Scoring: scored by hidden verifier

### Step 6: Prepare un-nested system matrices
- Role: process
- Action: Construct the TRL vector using the original ACCC component TRLs (not nested) and the IRL matrix including all internal and external interfaces from the system interfaces file.
- Evidence: none

### Step 7: Compute un-nested system composite SRL
- Role: scored (load-bearing)
- Action: Compute the composite SRL for the un-nested power plant system and write the result.
- Output file: `/app/outputs/unnested_system_srl.txt`
- Format: txt
- Contract: A single floating-point number representing the un-nested composite SRL score.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/accc_subsystem_srl.txt`
- `/app/outputs/nested_system_srl.txt`
- `/app/outputs/unnested_system_srl.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### accc_subsystem_srl.txt
- path: `/app/outputs/accc_subsystem_srl.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Composite SRL score for the ACCC subsystem computed from the provided digraph and TRL/IRL data.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the composite SRL score for the ACCC subsystem.

### nested_system_srl.txt
- path: `/app/outputs/nested_system_srl.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Composite SRL score for the advanced power plant system with the ACCC subsystem nested as a single component.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the composite SRL score for the nested power plant system.

### unnested_system_srl.txt
- path: `/app/outputs/unnested_system_srl.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Composite SRL score for the advanced power plant system with ACCC components kept separate (un-nested).
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the composite SRL score for the un-nested power plant system.

Notes: All three composite SRL scores are computed using the same matrix normalization formula with provided digraph data and the SRL Translation Table. The checker compares each value to the paper's reported hidden gold with an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "accc_subsystem_srl.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the composite SRL score for the ACCC subsystem."
      },
      "description": "Composite SRL score for the ACCC subsystem computed from the provided digraph and TRL/IRL data."
    },
    {
      "file": "nested_system_srl.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the composite SRL score for the nested power plant system."
      },
      "description": "Composite SRL score for the advanced power plant system with the ACCC subsystem nested as a single component."
    },
    {
      "file": "unnested_system_srl.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the composite SRL score for the un-nested power plant system."
      },
      "description": "Composite SRL score for the advanced power plant system with ACCC components kept separate (un-nested)."
    }
  ],
  "notes": "All three composite SRL scores are computed using the same matrix normalization formula with provided digraph data and the SRL Translation Table. The checker compares each value to the paper's reported hidden gold with an appropriate tolerance."
}
```

## How you are scored
A hidden verifier independently scores each scored workflow artifact. For each composite SRL output file, the verifier reads the numeric value you wrote and compares it to a reference value using an appropriate tolerance. The final reward is a weighted combination of these comparisons. To achieve full credit, you must honestly implement the methodology and compute the values correctly—merely reporting expected numbers is not sufficient because the tolerance is unknown to you.
