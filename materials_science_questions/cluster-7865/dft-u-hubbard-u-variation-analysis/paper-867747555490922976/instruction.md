# Orbital Order and Conductivity in Spinel Vanadates from DFT

## Problem background
The spinel vanadate CoV₂O₄ sits near the itinerant limit and exhibits a debated structural transition below 100 K. Experiments suggest two low‑temperature tetragonal phases with different symmetries (I4₁/amd and I4₁/a), each possibly hosting a distinct type of vanadium orbital order. Separately, doping Co into the insulating MnV₂O₄ is known to increase electron itinerancy. The key open questions are: (1) What is the nature of the orbital order—real or complex—in each tetragonal phase of CoV₂O₄, and how do the vanadium orbital moments differ? (2) How does the electrical conductivity change with Co doping in the MnV₂O₄–CoV₂O₄ series, and does the fundamental orbital‑order type persist?

## Approach
We use first‑principles density functional theory (DFT) with Hubbard‑U correction and spin‑orbit coupling (GGA+U+SO) to compute the electronic structure and vanadium orbital moments of CoV₂O₄ in its cubic (Fd‑3m) and two tetragonal phases (I4₁/amd and I4₁/a). Wannier function analysis of the V t₂g bands reveals whether the occupied orbitals form a complex combination (dₓz ± i d_yz) or an A‑type real alternating pattern. For the doping study, we substitute 50% of Mn by Co in MnV₂O₄ and perform analogous DFT+U calculations for the parent and doped compounds. Electrical conductivity at 300 K is then evaluated using semi‑classical Boltzmann transport theory for three compositions: MnV₂O₄ (x=0.0), Mn₀.₅Co₀.₅V₂O₄ (x=0.5), and CoV₂O₄ (x=1.0). The collinear ferrimagnetic order with V spins antiparallel to Mn/Co spins is assumed throughout. All calculations use open‑source tools (Quantum ESPRESSO, WANNIER90, BoltzTraP2) and publicly available crystal structures.

## Reproduction target
1. For the I4₁/amd and I4₁/a phases of CoV₂O₄, compute the vanadium orbital moment (a single signed number in μB for each phase) and determine whether each phase exhibits complex orbital order (dₓz ± i d_yz) or A‑type real orbital order (alternating dₓz/d_yz).
2. For the three doping levels x = 0.0 (MnV₂O₄), 0.5 (Mn₀.₅Co₀.₅V₂O₄), and 1.0 (CoV₂O₄), compute the electrical conductivity at 300 K. The target is to reproduce the trend in conductivity as a function of Co content. Produced values are checked for consistency with the expected ordering.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- WANNIER90: https://github.com/wannier-developers/wannier90
- BoltzTraP2: https://bitbucket.org/sousaw/boltzmanntransport/
- PBE pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table
- Experimental crystal structures for CoV2O4 and MnV2O4: 10.1103/PhysRevB.96.144424 and 10.1103/PhysRevB.86.125142

## Workflow steps

### Step 1: Structural optimization
- Role: process
- Action: Optimize lattice parameters and atomic positions for CoV2O4 (cubic, I41/amd, I41/a) and MnV2O4 (I41/a) phases using GGA-PBE functional.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: DFT self-consistent field for CoV2O4 phases
- Role: process
- Action: Perform GGA+U+SO self-consistent calculations for CoV2O4 cubic, I41/amd, and I41/a phases with U_eff=3 eV on V and 4 eV on Co, collinear ferrimagnetic ordering, using the optimized structures.
- Evidence: none

### Step 3: Extract vanadium orbital moment for I41/amd phase
- Role: scored (load-bearing)
- Action: From the DFT output, extract the vanadium orbital moment for the I41/amd phase and write the value to co_phase2_orbital_moment.txt.
- Output file: `/app/outputs/co_phase2_orbital_moment.txt`
- Format: txt
- Contract: A single floating-point number (negative value expected).
- Scoring: scored by hidden verifier

### Step 4: Extract vanadium orbital moment for I41/a phase
- Role: scored (load-bearing)
- Action: From the DFT output, extract the vanadium orbital moment for the I41/a phase and write the value to co_phase3_orbital_moment.txt.
- Output file: `/app/outputs/co_phase3_orbital_moment.txt`
- Format: txt
- Contract: A single floating-point number (negative value expected).
- Scoring: scored by hidden verifier

### Step 5: Wannierization of V t2g bands
- Role: process
- Action: Fit maximally-localized Wannier functions to the V t2g bands of the I41/amd and I41/a phases using WANNIER90.
- Evidence: none

### Step 6: Classify orbital order type
- Role: scored (load-bearing)
- Action: Using the Wannier orbital shapes and hole-density analysis, determine whether each tetragonal phase has complex orbital order (d_xz ± i d_yz) or A-type real orbital order, and write the classification to orbital_order_classification.json.
- Output file: `/app/outputs/orbital_order_classification.json`
- Format: json
- Contract: JSON object with keys 'I41/amd' and 'I41/a', each a string (either 'complex' or 'A-type real').
- Scoring: scored by hidden verifier

### Step 7: DFT calculations for doped compounds
- Role: process
- Action: Perform GGA+U SCF calculations for MnV2O4 (I41/a), Mn0.5Co0.5V2O4 (50% Co substitution in MnV2O4), and CoV2O4 (I41/a phase) using optimized structures.
- Evidence: none

### Step 8: Wannier fits for transport
- Role: process
- Action: Construct maximally-localized Wannier functions for the V t2g bands of the three compositions (MnV2O4, Mn0.5Co0.5V2O4, CoV2O4).
- Evidence: none

### Step 9: Boltzmann transport conductivity extraction
- Role: scored (load-bearing)
- Action: Compute electrical conductivity at 300 K for x=0.0 (MnV2O4), x=0.5 (Mn0.5Co0.5V2O4), and x=1.0 (CoV2O4) using Boltzmann transport theory and write the values to conductivity_values.json.
- Output file: `/app/outputs/conductivity_values.json`
- Format: json
- Contract: JSON object with keys 'x0.0', 'x0.5', 'x1.0', each a positive number (conductivity in S/m).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/co_phase2_orbital_moment.txt`
- `/app/outputs/co_phase3_orbital_moment.txt`
- `/app/outputs/orbital_order_classification.json`
- `/app/outputs/conductivity_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### co_phase2_orbital_moment.txt
- path: `/app/outputs/co_phase2_orbital_moment.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Vanadium orbital moment for the I41/amd phase; scored by checking that its absolute value exceeds a hidden threshold consistent with a large unquenched orbital moment.
- schema:
  - `type`: text
  - `required`: object
  - `description`: A single floating-point number representing the vanadium orbital moment in μB for the I41/amd phase. The sign must be included.

### co_phase3_orbital_moment.txt
- path: `/app/outputs/co_phase3_orbital_moment.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Vanadium orbital moment for the I41/a phase; scored by checking that its absolute value is below a hidden threshold consistent with a quenched orbital moment.
- schema:
  - `type`: text
  - `required`: object
  - `description`: A single floating-point number representing the vanadium orbital moment in μB for the I41/a phase. The sign must be included.

### orbital_order_classification.json
- path: `/app/outputs/orbital_order_classification.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Classification of orbital order for the two tetragonal phases. 'I41/amd' must be either 'complex' or 'A-type real'; 'I41/a' likewise. Exact string matching is used.
- schema:
  - `type`: object
  - `required`:
    - `I41/amd`: string
    - `I41/a`: string

### conductivity_values.json
- path: `/app/outputs/conductivity_values.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Electrical conductivity values at 300 K for three Co doping levels. The structural audit verifies that the values increase monotonically: σ(x0.0) < σ(x0.5) < σ(x1.0).
- schema:
  - `type`: object
  - `required`:
    - `x0.0`: positive number
    - `x0.5`: positive number
    - `x1.0`: positive number
  - `units`:
    - `conductivity`: S/m

Notes: All scored artifacts must be generated from first-principles calculations using the public tools and structures listed in resources. Hidden thresholds for orbital moments and the expected classification strings are derived from the paper's reported values; the exact magnitude separation is part of the hidden grading.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "co_phase2_orbital_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "required": {},
        "description": "A single floating-point number representing the vanadium orbital moment in μB for the I41/amd phase. The sign must be included."
      },
      "description": "Vanadium orbital moment for the I41/amd phase; scored by checking that its absolute value exceeds a hidden threshold consistent with a large unquenched orbital moment."
    },
    {
      "file": "co_phase3_orbital_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "required": {},
        "description": "A single floating-point number representing the vanadium orbital moment in μB for the I41/a phase. The sign must be included."
      },
      "description": "Vanadium orbital moment for the I41/a phase; scored by checking that its absolute value is below a hidden threshold consistent with a quenched orbital moment."
    },
    {
      "file": "orbital_order_classification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "I41/amd": "string",
          "I41/a": "string"
        }
      },
      "description": "Classification of orbital order for the two tetragonal phases. 'I41/amd' must be either 'complex' or 'A-type real'; 'I41/a' likewise. Exact string matching is used."
    },
    {
      "file": "conductivity_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "x0.0": "positive number",
          "x0.5": "positive number",
          "x1.0": "positive number"
        },
        "units": {
          "conductivity": "S/m"
        }
      },
      "description": "Electrical conductivity values at 300 K for three Co doping levels. The structural audit verifies that the values increase monotonically: σ(x0.0) < σ(x0.5) < σ(x1.0)."
    }
  ],
  "notes": "All scored artifacts must be generated from first-principles calculations using the public tools and structures listed in resources. Hidden thresholds for orbital moments and the expected classification strings are derived from the paper's reported values; the exact magnitude separation is part of the hidden grading."
}
```

## How you are scored
A hidden verifier reads your four scored output files. It checks that the absolute value of the orbital moment for the I4₁/amd phase is above a hidden threshold (indicating a large unquenched moment) and that for the I4₁/a phase it is below another threshold (indicating quenching). The orbital order classification file is compared exactly against the expected string for each phase. The conductivity file is audited to confirm that the three values satisfy σ(x=0.0) < σ(x=0.5) < σ(x=1.0). Each check carries a pre‑defined weight, and the combined score (a float between 0 and 1) is your reward. Reproducing the paper’s reported numbers without genuine computation will not pass all checks.
