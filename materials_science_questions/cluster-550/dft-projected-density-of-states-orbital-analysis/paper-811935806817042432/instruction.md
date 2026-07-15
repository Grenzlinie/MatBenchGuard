# Spin-polarized DFT electronic structure of iron tape-porphyrin and NO adsorption

## Problem background
Iron tape-porphyrin (FeTP) is a one-dimensional molecular wire formed by fusing porphyrin macrocycles via three conjugating C–C bonds. Due to its small HOMO-LUMO gap, it is a candidate for molecular electronics. This task investigates the electronic properties of FeTP and its complex with nitric oxide (NO) using spin-polarized density functional theory. You will compute the spin-polarized band structure and projected density of states (PDOS) to determine the nature of the electronic states near the Fermi level and how they change upon NO adsorption.

## Approach
Construct a periodic one-dimensional model of iron tape-porphyrin with a central Fe atom, three C–C links between macrocycles, and hydrogen termination. Perform spin-polarized density functional theory (DFT) calculations at the generalized gradient approximation (GGA-PBE) level using an open-source plane-wave code (Quantum ESPRESSO) and standard pseudopotentials. First, relax the atomic positions of the isolated FeTP wire. Then compute the electronic band structure along the 1D Brillouin zone and the projected density of states onto Fe d_yz, meso-C p_z, and β-C p_z orbitals to analyze orbital contributions near the Fermi level. Next, place an NO molecule near the Fe site, relax the FeTP–NO geometry, and compute its band structure. The comparison between the isolated FeTP and the FeTP–NO complex yields the key electronic and geometric changes.

## Reproduction target
Produce the following quantitative results from the DFT calculations: (1) For isolated FeTP, determine if the majority-spin channel is metallic (bands crossing the Fermi level) or has a band gap; report the gap value if any. (2) Provide the projected density of states of Fe d_yz, meso-C p_z, and β-C p_z orbitals within ±1 eV of the Fermi level for FeTP. (3) For the FeTP–NO complex, compute the overall band gap (any spin) and the Fe–N–O bond angle from the relaxed geometry.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: FeTP geometry optimization
- Role: process
- Action: Construct a periodic 1D model of iron tape-porphyrin (FeTP) with Fe centre, three C–C links, and hydrogen termination. Relax the atomic positions using spin-polarized GGA-DFT (PBE) with a 1D k-point grid and vacuum. Converge forces to under 0.05 eV/Å. Save the relaxed geometry.
- Evidence: `/app/outputs/feTP_relaxed.xyz`

### Step 2: FeTP electronic structure calculation
- Role: process
- Action: From the relaxed FeTP, perform a self-consistent field (SCF) calculation, then a non-self-consistent band structure along the 1D path (Γ–X) and a projected density of states (PDOS) calculation projecting onto Fe d_yz, meso-C p_z, and β-C p_z orbitals. Save the raw band structure data and the raw PDOS data.
- Evidence: `/app/outputs/feTP_band_structure.csv`

### Step 3: FeTP majority-spin band gap
- Role: scored (load-bearing)
- Action: From the FeTP band structure data, determine the majority-spin band gap by finding the smallest energy gap between occupied and unoccupied majority-spin bands with Fermi level at zero. Write a single line: either the numeric gap value in eV or the word 'metallic' if bands cross the Fermi level.
- Output file: `/app/outputs/step_01_FeTP_band_gap.txt`
- Format: txt
- Contract: single line: a floating-point value in eV, or the exact string 'metallic'
- Scoring: scored by hidden verifier

### Step 4: FeTP PDOS orbital character near Fermi level
- Role: scored (load-bearing)
- Action: From the PDOS calculation data, produce a CSV file with columns: energy (eV relative to Fermi level), d_yz_Fe, pz_meso_C, pz_beta_C. Cover at least ±1 eV around the Fermi level. PDOS contributions in consistent units (e.g., states/eV/atom).
- Output file: `/app/outputs/step_03_FeTP_PDOS.csv`
- Format: csv
- Contract: header: energy, d_yz_Fe, pz_meso_C, pz_beta_C; rows of floating-point numbers
- Scoring: scored by hidden verifier

### Step 5: FeTP–NO geometry optimization
- Role: process
- Action: Place an NO molecule near the Fe site of the relaxed FeTP model, testing several initial orientations if desired, and relax the full geometry of FeTP–NO using the same DFT settings. Converge forces to under 0.05 eV/Å. Save the final structure.
- Evidence: `/app/outputs/feTPNO_relaxed.xyz`

### Step 6: FeTP–NO electronic structure calculation
- Role: process
- Action: From the relaxed FeTP–NO, perform SCF and band structure calculation; output the band structure data for all spin channels.
- Evidence: `/app/outputs/feTPNO_band_structure.csv`

### Step 7: FeTP–NO band gap and Fe–N–O angle
- Role: scored (load-bearing)
- Action: From the FeTP–NO band structure data, compute the overall band gap (any spin) as the smallest energy difference between occupied and unoccupied bands at the Fermi level. From the relaxed FeTP–NO geometry XYZ file, compute the Fe–N–O bond angle. Write a two-line file: band gap (eV) on line 1, angle (degrees) on line 2.
- Output file: `/app/outputs/step_02_FeTP_NO_results.txt`
- Format: txt
- Contract: line 1: <float> eV, line 2: <float> degrees
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_FeTP_band_gap.txt`
- `/app/outputs/step_03_FeTP_PDOS.csv`
- `/app/outputs/step_02_FeTP_NO_results.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_FeTP_band_gap.txt
- path: `/app/outputs/step_01_FeTP_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Majority-spin band gap of isolated FeTP, extracted from the computed band structure.
- schema:
  - `type`: text
  - `description`: A single line containing either a floating-point number (eV) or the word 'metallic'.

### step_03_FeTP_PDOS.csv
- path: `/app/outputs/step_03_FeTP_PDOS.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Projected density of states of Fe d_yz, meso-C p_z, and β-C p_z orbitals for FeTP within ±1 eV of the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `d_yz_Fe`, `pz_meso_C`, `pz_beta_C`
  - `units`:
    - `energy`: eV
    - `d_yz_Fe`: states/eV/atom
    - `pz_meso_C`: states/eV/atom
    - `pz_beta_C`: states/eV/atom

### step_02_FeTP_NO_results.txt
- path: `/app/outputs/step_02_FeTP_NO_results.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Band gap of FeTP–NO complex and Fe–N–O adsorption geometry angle.
- schema:
  - `type`: text
  - `description`: Line 1: band gap in eV; line 2: Fe–N–O angle in degrees.

Notes: The checker recomputes the FeTP band gap metric from the raw band structure CSV (provided as process evidence) and compares the submitted text against a threshold. The PDOS fraction is recomputed from the CSV and compared against a threshold. The FeTP–NO gap and angle are extracted from the two-line file and checked against paper-comparable tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_FeTP_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single line containing either a floating-point number (eV) or the word 'metallic'."
      },
      "description": "Majority-spin band gap of isolated FeTP, extracted from the computed band structure."
    },
    {
      "file": "step_03_FeTP_PDOS.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "d_yz_Fe",
          "pz_meso_C",
          "pz_beta_C"
        ],
        "units": {
          "energy": "eV",
          "d_yz_Fe": "states/eV/atom",
          "pz_meso_C": "states/eV/atom",
          "pz_beta_C": "states/eV/atom"
        }
      },
      "description": "Projected density of states of Fe d_yz, meso-C p_z, and β-C p_z orbitals for FeTP within ±1 eV of the Fermi level."
    },
    {
      "file": "step_02_FeTP_NO_results.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Line 1: band gap in eV; line 2: Fe–N–O angle in degrees."
      },
      "description": "Band gap of FeTP–NO complex and Fe–N–O adsorption geometry angle."
    }
  ],
  "notes": "The checker recomputes the FeTP band gap metric from the raw band structure CSV (provided as process evidence) and compares the submitted text against a threshold. The PDOS fraction is recomputed from the CSV and compared against a threshold. The FeTP–NO gap and angle are extracted from the two-line file and checked against paper-comparable tolerances."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact. The verifier compares your results against reference values from the original study, using tolerances that account for the use of a different DFT implementation. It may recompute derived quantities directly from your raw data. Each artifact carries a weight, and the final reward is a value between 0 and 1. Simply reporting numbers is not enough; your outputs must be consistent with a genuine DFT calculation.
