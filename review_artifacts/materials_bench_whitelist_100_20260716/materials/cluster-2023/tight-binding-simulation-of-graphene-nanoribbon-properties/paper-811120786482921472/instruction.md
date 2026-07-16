# DFT Relaxation and NEGF Transport of Folded Zigzag Graphene Nanoribbons

## Problem background
Zigzag graphene nanoribbons (ZGNRs) exhibit electronic and transport properties that are highly sensitive to folding. When an external electric field is applied perpendicular to the ribbon plane, the nanoribbon folds, causing changes in C–C bond lengths and electronic structure. These structural modifications in turn affect the current–voltage characteristics and the presence of negative differential conductance (NDC). This task reproduces density-functional theory (DFT) geometry relaxations and nonequilibrium Green’s function (NEGF) transport simulations to quantify how the folding degree alters the geometry and transport of a hydrogen‑terminated ZGNR.

## Approach
First, construct a supercell of a hydrogen‑terminated zigzag graphene nanoribbon and relax it with DFT using the generalized‑gradient approximation (GGA‑PBE), a double‑ζ plus polarization basis set, and a real‑space grid cutoff of 200 Ry. Periodic boundary conditions are applied along the ribbon axis, with vacuum regions in the transverse directions. Four relaxations are performed: one without an external electric field and three with fields of increasing strength applied across the ribbon. Each relaxed geometry represents a different folding degree. From the relaxed structures, extract four representative C–C bond lengths that characterise the deformation. Then, using the same relaxed cells, build two‑probe devices and run NEGF‑DFT transport simulations to obtain current as a function of bias voltage. From the I‑V curves compute the differential conductance at a fixed bias to assess the presence of NDC.

## Reproduction target
Produce two JSON artifacts under `/app/outputs`:

1. `bond_lengths.json` — an object with keys `A`, `B`, `C`, each mapping to a list of four C–C bond lengths (in Ångström) for the three folded configurations.

2. `transport_data.json` — an object with keys `Per`, `A`, `B`, `C`. For each, provide the bias grid (from –2.0 V to 2.0 V in steps no larger than 0.2 V), the corresponding current, and the differential conductance at 1.0 V bias computed from the I‑V data.

A hidden verifier will evaluate the transport data against the expected trends reported in the paper. The bond lengths will be compared to reference values.

## Assets

- SIESTA DFT code (including TranSIESTA for transport): https://gitlab.com/siesta-project/siesta
- PBE pseudopotentials for C and H: https://gitlab.com/siesta-project/siesta/-/tree/master/Pseudo

## Workflow steps

### Step 1: DFT Geometry Relaxation
- Role: process
- Action: Construct a hydrogen-terminated zigzag graphene nanoribbon supercell containing 48 carbon atoms with hydrogen-terminated edges. Perform DFT geometry relaxation using the open-source SIESTA code with GGA-PBE exchange-correlation functional, DZP basis set, and a real-space grid cutoff of 200 Ry. Apply periodic boundary conditions along the ribbon axis (z direction) and a vacuum region larger than 10 Å in x and y directions. Carry out four separate relaxations: one with no external field (Per configuration) and three with external electric fields of 0.5, 2.0, and 4.0 V/Å applied along the x direction (configurations A, B, C respectively). Save the final relaxed atomic structures.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: C–C Bond Length Extraction
- Role: scored
- Action: From the relaxed structures of configurations A, B, C, extract the four central C–C bond lengths along the fold crest (the bonds that experience the largest elongation due to folding). Report these lengths in Angstrom as a JSON object.
- Output file: `/app/outputs/bond_lengths.json`
- Format: json
- Contract: { "A": [float, float, float, float], "B": [float, float, float, float], "C": [float, float, float, float] }
- Scoring: scored by hidden verifier

### Step 3: Transport Simulation and Analysis
- Role: scored (load-bearing)
- Action: Using the relaxed structures, construct two-probe models for each configuration (Per, A, B, C). Perform NEGF-DFT transport simulation with TranSIESTA to compute current at bias voltages from -2.0 V to 2.0 V in steps no larger than 0.2 V. Compute differential conductance at 1.0 V bias via central difference on the I-V data. Save the complete I-V data and the differential conductance value as a JSON file.
- Output file: `/app/outputs/transport_data.json`
- Format: json
- Contract: { "Per": {"bias": [float,...], "current": [float,...], "diff_cond_at_1V": float}, "A": {...}, "B": {...}, "C": {...} }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bond_lengths.json`
- `/app/outputs/transport_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bond_lengths.json
- path: `/app/outputs/bond_lengths.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: C–C bond lengths for configurations A, B, C. The checker compares each value to hidden gold within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `A`: array of 4 floats
    - `B`: array of 4 floats
    - `C`: array of 4 floats
  - `units`:
    - `bond_lengths`: Angstrom

### transport_data.json
- path: `/app/outputs/transport_data.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Transport data with I-V curves and differential conductance at 1.0 V. The checker will evaluate these quantities against the expected transport trends from the paper.
- schema:
  - `type`: object
  - `required`:
    - `Per`:
      - `bias`: array of floats (V)
      - `current`: array of floats (A)
      - `diff_cond_at_1V`: float (A/V)
    - `A`: same structure
    - `B`: same structure
    - `C`: same structure
  - `units`:
    - `bias`: V
    - `current`: A
    - `diff_cond_at_1V`: A/V

Notes: Band structure and subband width analysis omitted because it requires subjective band identification and is not needed for the headline verifiable claims. Verification for bond lengths uses tolerance-based comparison. Transport verification evaluates key trends as reported in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bond_lengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "A": "array of 4 floats",
          "B": "array of 4 floats",
          "C": "array of 4 floats"
        },
        "units": {
          "bond_lengths": "Angstrom"
        }
      },
      "description": "C–C bond lengths for configurations A, B, C. The checker compares each value to hidden gold within a tolerance."
    },
    {
      "file": "transport_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Per": {
            "bias": "array of floats (V)",
            "current": "array of floats (A)",
            "diff_cond_at_1V": "float (A/V)"
          },
          "A": "same structure",
          "B": "same structure",
          "C": "same structure"
        },
        "units": {
          "bias": "V",
          "current": "A",
          "diff_cond_at_1V": "A/V"
        }
      },
      "description": "Transport data with I-V curves and differential conductance at 1.0 V. The checker will evaluate these quantities against the expected transport trends from the paper."
    }
  ],
  "notes": "Band structure and subband width analysis omitted because it requires subjective band identification and is not needed for the headline verifiable claims. Verification for bond lengths uses tolerance-based comparison. Transport verification evaluates key trends as reported in the paper."
}
```

## How you are scored
A hidden verifier reads your two JSON files. The bond‑length section carries the largest weight: each reported bond length is compared to a reference with an absolute tolerance. The transport section scores how well your I‑V characteristics and differential conductance at 1 V match the trends established in the paper. The final score is the weighted sum of these checks. Simply reporting the paper’s numbers is not sufficient; the verifier expects results that emerge from a genuine DFT‑NEGF calculation.
