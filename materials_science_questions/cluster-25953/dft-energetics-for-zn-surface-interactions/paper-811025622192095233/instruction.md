# DFT calculations of ZnS phase transition pressures, activation enthalpies, and band gaps

## Problem background
Zinc sulfide (ZnS) undergoes a pressure-induced phase transition from the tetrahedrally coordinated zinc blende (B3, F‑43m) structure to the octahedrally coordinated rocksalt (B1, Fm‑3m) structure. Understanding the microscopic mechanism of such solid‑state transformations requires determining the equilibrium transition pressure, the energy barrier along competing atomic pathways, and the evolution of the electronic structure (band gap) during the transformation. First‑principles density‑functional theory (DFT) can address these questions by computing the enthalpies of the end phases and of intermediate configurations along candidate pathways, thereby identifying the most favoured kinetic route and the associated activation enthalpies, as well as the pressure‑dependent band gaps.

## Approach
Use periodic DFT calculations with both the B3LYP hybrid functional and the LDA functional. Perform the calculations with any DFT code that supports these functionals (e.g., Quantum ESPRESSO with appropriate pseudopotentials). The workflow has three stages: (1) Equation‑of‑state fits and transition pressure determination: for each functional, compute the total energies of zinc blende and rocksalt ZnS over a range of volumes, fit an equation of state, and evaluate the enthalpy difference between the two phases at several pressures. Fit the enthalpy difference as a function of pressure to obtain the equilibrium transition pressure. (2) Enthalpy profiles along the Pmm2 and R3m transformation pathways: at the equilibrium pressure obtained for each functional, construct a series of intermediate structures along the orthorhombic Pmm2 pathway and the rhombohedral R3m pathway by varying the zinc fractional coordinate z from 0.25 (zinc blende) to 0.5 (rocksalt). For each value of z, minimize the enthalpy with respect to the lattice parameters while keeping z fixed, and record the enthalpy relative to the zinc blende end‑member. The maximum enthalpy on each curve gives the activation enthalpy; compare the two pathways to see which one has the lower barrier. (3) Band gaps: using the B3LYP functional at its equilibrium pressure, optimize the structures of the zinc blende (z=0.25), the intermediate Pmm2 structure at z=0.35, and the rocksalt (z=0.5) states, then perform self‑consistent‑field calculations to obtain the Kohn‑Sham band gap (energy difference between the highest occupied and lowest unoccupied eigenvalues). All required crystal structures are fully defined by their space groups and can be generated from standard crystallographic data; no external structure files are needed.

## Reproduction target
Produce the following scored artifacts in `/app/outputs`:

1. `transition_pressures.json` — a JSON object with keys `"B3LYP"` and `"LDA"` giving the equilibrium transition pressures (in GPa) obtained from the equation‑of‑state fits.
2. `activation_enthalpy_B3LYP.csv` — a CSV file with columns `pathway` (string, either `"Pmm2"` or `"R3m"`), `z` (float from 0.25 to 0.5 in steps of 0.025), and `enthalpy_diff` (eV) giving the enthalpy difference relative to zinc blende along both pathways at the B3LYP equilibrium pressure.
3. `activation_enthalpy_LDA.csv` — the same format as above, but evaluated at the LDA equilibrium pressure.
4. `band_gaps_B3LYP.json` — a JSON object with keys `"B3"`, `"Pmm2_z0.35"`, and `"B1"` giving the band gaps (in eV) computed with the B3LYP functional at its equilibrium pressure.

The activation enthalpies are defined as the maximum enthalpy difference on each pathway curve. The calculations must follow the workflow steps in order, and all intermediate log files should be written to the evidence files listed in the steps.

## Assets

- DFT software supporting B3LYP and LDA exchange‑correlation functionals (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org
- Pseudopotentials for Zn and S (e.g., SSSP or PseudoDojo libraries): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Equation‑of‑state fitting and transition pressure determination
- Role: process
- Action: For both B3LYP and LDA functionals, compute total energies of zinc blende (B3) and rocksalt (B1) ZnS over a range of volumes, fit to an equation of state, and evaluate the enthalpy difference ΔH_t(p) = H(rocksalt) − H(zinc blende) at the pressures specified by the paper. Fit ΔH_t(p) to a parabola and solve for the equilibrium transition pressure p_t for each functional.
- Evidence: `/app/outputs/eos_calc.log`

### Step 2: Report transition pressures
- Role: scored
- Action: Write the computed equilibrium transition pressures p_t (in GPa) for the B3LYP and LDA functionals to a JSON file.
- Output file: `/app/outputs/transition_pressures.json`
- Format: json
- Contract: {"B3LYP": <float (GPa)>, "LDA": <float (GPa)>}
- Scoring: scored by hidden verifier

### Step 3: Compute enthalpy profiles along Pmm2 and R3m pathways
- Role: process
- Action: For both B3LYP and LDA functionals, at their respective equilibrium pressure p_t, construct Pmm2 and R3m intermediate structures by varying the Zn fractional coordinate z(Zn) from 0.25 to 0.5 in steps of 0.025. At each z, minimize the enthalpy with respect to the lattice parameters while keeping z fixed, and record the enthalpy difference relative to the zinc blende end‑member.
- Evidence: `/app/outputs/pathway_calc.log`

### Step 4: Report activation enthalpies (B3LYP)
- Role: scored (load-bearing)
- Action: Write a CSV file containing the enthalpy differences (relative to the zinc blende structure) along the Pmm2 and R3m pathways at the B3LYP equilibrium pressure. Each row corresponds to one z(Zn) value.
- Output file: `/app/outputs/activation_enthalpy_B3LYP.csv`
- Format: csv
- Contract: columns: pathway (string: 'Pmm2' or 'R3m'), z (float), enthalpy_diff (eV). Data at the B3LYP equilibrium pressure.
- Scoring: scored by hidden verifier

### Step 5: Report activation enthalpies (LDA)
- Role: scored
- Action: Write a CSV file containing the enthalpy differences along the Pmm2 and R3m pathways at the LDA equilibrium pressure. Each row corresponds to one z(Zn) value.
- Output file: `/app/outputs/activation_enthalpy_LDA.csv`
- Format: csv
- Contract: columns: pathway (string: 'Pmm2' or 'R3m'), z (float), enthalpy_diff (eV). Data at the LDA equilibrium pressure.
- Scoring: scored by hidden verifier

### Step 6: Compute band gaps for key structures
- Role: process
- Action: Using the B3LYP functional at its equilibrium pressure, perform self‑consistent‑field calculations for the optimized structures of zinc blende (z=0.25), the intermediate Pmm2 structure at z=0.35, and rocksalt (z=0.5). Compute the Kohn‑Sham band gap (energy difference between the highest occupied and lowest unoccupied eigenvalues).
- Evidence: `/app/outputs/band_gap_calc.log`

### Step 7: Report band gaps (B3LYP)
- Role: scored
- Action: Write the computed band gaps (in eV) for the three characteristic structures to a JSON file.
- Output file: `/app/outputs/band_gaps_B3LYP.json`
- Format: json
- Contract: {"B3": <float (eV)>, "Pmm2_z0.35": <float (eV)>, "B1": <float (eV)>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_pressures.json`
- `/app/outputs/activation_enthalpy_B3LYP.csv`
- `/app/outputs/activation_enthalpy_LDA.csv`
- `/app/outputs/band_gaps_B3LYP.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_pressures.json
- path: `/app/outputs/transition_pressures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium transition pressures from B3LYP and LDA equation‑of‑state fits.
- schema:
  - `type`: object
  - `required`:
    - `B3LYP`: float (GPa)
    - `LDA`: float (GPa)

### activation_enthalpy_B3LYP.csv
- path: `/app/outputs/activation_enthalpy_B3LYP.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Enthalpy profiles along Pmm2 and R3m pathways at B3LYP equilibrium pressure. The checker recomputes activation enthalpies (max of each curve) and verifies the Pmm2 < R3m trend.
- schema:
  - `type`: table
  - `required_columns`: `pathway`, `z`, `enthalpy_diff`
  - `units`:
    - `enthalpy_diff`: eV

### activation_enthalpy_LDA.csv
- path: `/app/outputs/activation_enthalpy_LDA.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Enthalpy profiles along Pmm2 and R3m pathways at LDA equilibrium pressure. Same checking logic as the B3LYP file.
- schema:
  - `type`: table
  - `required_columns`: `pathway`, `z`, `enthalpy_diff`
  - `units`:
    - `enthalpy_diff`: eV

### band_gaps_B3LYP.json
- path: `/app/outputs/band_gaps_B3LYP.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gaps of zinc blende, Pmm2 intermediate (z=0.35), and rocksalt structures at the B3LYP equilibrium pressure.
- schema:
  - `type`: object
  - `required`:
    - `B3`: float (eV)
    - `Pmm2_z0.35`: float (eV)
    - `B1`: float (eV)

Notes: Crystal structures are fully defined by their space groups and can be generated from standard crystallographic data; no external structure file is needed. All calculations are pure DFT and do not require wet‑lab inputs. Tolerances for the hidden gold are set wide enough to accommodate legitimate toolchain spread while still excluding random guesses.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B3LYP": "float (GPa)",
          "LDA": "float (GPa)"
        }
      },
      "description": "Equilibrium transition pressures from B3LYP and LDA equation‑of‑state fits."
    },
    {
      "file": "activation_enthalpy_B3LYP.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pathway",
          "z",
          "enthalpy_diff"
        ],
        "units": {
          "enthalpy_diff": "eV"
        }
      },
      "description": "Enthalpy profiles along Pmm2 and R3m pathways at B3LYP equilibrium pressure. The checker recomputes activation enthalpies (max of each curve) and verifies the Pmm2 < R3m trend."
    },
    {
      "file": "activation_enthalpy_LDA.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pathway",
          "z",
          "enthalpy_diff"
        ],
        "units": {
          "enthalpy_diff": "eV"
        }
      },
      "description": "Enthalpy profiles along Pmm2 and R3m pathways at LDA equilibrium pressure. Same checking logic as the B3LYP file."
    },
    {
      "file": "band_gaps_B3LYP.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B3": "float (eV)",
          "Pmm2_z0.35": "float (eV)",
          "B1": "float (eV)"
        }
      },
      "description": "Band gaps of zinc blende, Pmm2 intermediate (z=0.35), and rocksalt structures at the B3LYP equilibrium pressure."
    }
  ],
  "notes": "Crystal structures are fully defined by their space groups and can be generated from standard crystallographic data; no external structure file is needed. All calculations are pure DFT and do not require wet‑lab inputs. Tolerances for the hidden gold are set wide enough to accommodate legitimate toolchain spread while still excluding random guesses."
}
```

## How you are scored
A hidden verifier will examine each of the four scored output files. For the transition pressures, the verifier compares the values in `transition_pressures.json` to hidden reference values within a tolerance. For each activation enthalpy CSV, the verifier extracts the maximum enthalpy difference on the Pmm2 and R3m pathways and checks that (i) the Pmm2 maximum is lower than the R3m maximum, and (ii) the activation enthalpies are within a tolerance of hidden gold values. For the band gaps, the verifier compares the values in `band_gaps_B3LYP.json` to hidden reference values within a tolerance. The checks are combined with weights (approximately 0.3 for transition pressures, 0.25 for each of the two activation enthalpy files, and 0.2 for band gaps) to produce a final reward between 0.0 and 1.0. The hidden gold numbers and tolerances are not provided to you; you must obtain the results by honestly performing the DFT calculations as described.
