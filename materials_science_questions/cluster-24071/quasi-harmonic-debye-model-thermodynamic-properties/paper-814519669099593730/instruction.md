# Compute thermodynamic properties of KZnF3 and AgZnF3 via DFT and quasi-harmonic Debye model

## Problem background
Cubic fluoride perovskites such as KZnF3 and AgZnF3 are candidate materials for technological applications ranging from piezoelectrics to thermal management. Reliable knowledge of their structural parameters (lattice constant, bulk modulus) and heat capacity is essential for assessing their suitability. First-principles density functional theory (DFT) calculations can predict these properties, complementing experimental measurements and providing insight into the materials' thermodynamic behavior.

## Approach
The reproduction follows a standard computational-thermodynamics workflow. First, DFT total-energy calculations are performed for the cubic perovskite structures of KZnF3 and AgZnF3 (space group Pm-3m) at a series of unit-cell volumes around equilibrium, using the GGA-PBEsol exchange-correlation functional with well-converged basis and k-point sampling. The resulting E(V) points are then fitted with the Murnaghan equation of state to extract the equilibrium lattice parameter a0, bulk modulus B0, and pressure derivative B′. Finally, the same E(V) data is used in the quasi-harmonic Debye model to compute the constant-volume heat capacity Cv at 300 K under zero pressure.

## Reproduction target
Produce accurate values for the equilibrium lattice parameter a0 (Å), bulk modulus B0 (GPa), and pressure derivative B′ from a Murnaghan fit for both KZnF3 and AgZnF3, and compute the constant-volume heat capacity Cv at 300 K using the quasi-harmonic Debye model. All results must be derived from DFT total-energy calculations performed with the GGA-PBEsol functional. Write the fitted parameters to `eos_parameters.json` and the heat capacities to `cv_300K.json` following the specified schemas.

## Assets

- ELK all-electron FP-LAPW code or equivalent open-source DFT package (e.g., Quantum ESPRESSO with hard pseudopotentials) supporting GGA-PBEsol: https://elk.sourceforge.io/
- Gibbs2 quasi-harmonic Debye model implementation: https://github.com/mahrossi/Gibbs2

## Workflow steps

### Step 1: DFT total-energy calculations for E(V) curves
- Role: process
- Action: Set up cubic perovskite structures (space group Pm-3m) for KZnF3 and AgZnF3. Perform self-consistent DFT total-energy calculations at a series of unit-cell volumes (at least 5–7 volumes around equilibrium) using the GGA-PBEsol exchange-correlation functional with a well-converged k-point mesh and basis set. Collect the total energy E for each volume V.
- Evidence: `/app/outputs/ev_curves.csv`

### Step 2: Murnaghan equation-of-state fitting
- Role: scored
- Action: Fit the computed E(V) points with the Murnaghan equation of state and extract equilibrium lattice parameter a0 (Å), bulk modulus B0 (GPa), and pressure derivative B′ for each compound.
- Output file: `/app/outputs/eos_parameters.json`
- Format: json
- Contract: Object with keys 'KZnF3' and 'AgZnF3', each an object with keys 'a0' (float, Å), 'B0' (float, GPa), 'Bprime' (float).
- Scoring: scored by hidden verifier

### Step 3: Quasi-harmonic Debye model heat capacity
- Role: scored (load-bearing)
- Action: Using the same E(V) data and a quasi-harmonic Debye model (e.g., Gibbs2 or reimplementation), compute the constant-volume heat capacity Cv at 300 K under zero pressure for both compounds.
- Output file: `/app/outputs/cv_300K.json`
- Format: json
- Contract: Object with keys 'KZnF3' and 'AgZnF3', each an object with key 'Cv_300' (float, J/(mol·K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_parameters.json`
- `/app/outputs/cv_300K.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_parameters.json
- path: `/app/outputs/eos_parameters.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Structural parameters from Murnaghan fit (GGA-PBEsol). Hidden tolerances: a0 within 2 %, B0 within 15 %, B′ within 20 % (or comparable spread).
- schema:
  - `type`: object
  - `required`:
    - `KZnF3`:
      - `a0`: float (Å)
      - `B0`: float (GPa)
      - `Bprime`: float
    - `AgZnF3`:
      - `a0`: float (Å)
      - `B0`: float (GPa)
      - `Bprime`: float

### cv_300K.json
- path: `/app/outputs/cv_300K.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Quasi-harmonic Debye heat capacity at 300 K, zero pressure. Hidden tolerance: ±5 J/(mol·K).
- schema:
  - `type`: object
  - `required`:
    - `KZnF3`:
      - `Cv_300`: float (J/(mol·K))
    - `AgZnF3`:
      - `Cv_300`: float (J/(mol·K))

Notes: Only a0, B0, B′ and Cv are scored, consistent with the approved plan. Tolerances are hidden to prevent gaming.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "KZnF3": {
            "a0": "float (Å)",
            "B0": "float (GPa)",
            "Bprime": "float"
          },
          "AgZnF3": {
            "a0": "float (Å)",
            "B0": "float (GPa)",
            "Bprime": "float"
          }
        }
      },
      "description": "Structural parameters from Murnaghan fit (GGA-PBEsol). Hidden tolerances: a0 within 2 %, B0 within 15 %, B′ within 20 % (or comparable spread)."
    },
    {
      "file": "cv_300K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "KZnF3": {
            "Cv_300": "float (J/(mol·K))"
          },
          "AgZnF3": {
            "Cv_300": "float (J/(mol·K))"
          }
        }
      },
      "description": "Quasi-harmonic Debye heat capacity at 300 K, zero pressure. Hidden tolerance: ±5 J/(mol·K)."
    }
  ],
  "notes": "Only a0, B0, B′ and Cv are scored, consistent with the approved plan. Tolerances are hidden to prevent gaming."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden verifier. For `eos_parameters.json`, the verifier compares your a0, B0, and B′ values (for both compounds) against hidden reference values. For `cv_300K.json`, it compares your Cv at 300 K against hidden reference values. Each comparison yields a score based on the deviation: meeting the reference within a predefined tolerance earns full credit, while larger deviations earn proportionally reduced credit, down to zero for very large errors. The final reward is a weighted combination of the scores from the two output files (the heat-capacity file carries more weight as the load-bearing artifact).
