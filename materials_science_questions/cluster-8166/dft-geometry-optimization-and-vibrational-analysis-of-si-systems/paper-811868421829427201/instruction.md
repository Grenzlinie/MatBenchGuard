# DFT Calculation of Twin Boundary and Stacking Fault Energies in Si, SiC, and Diamond

## Problem background
Twin boundaries and stacking faults are planar defects that can arise in 3C-SiC when the normal stacking sequence of Si–C bilayers is altered. Their formation energies determine which configurations are thermodynamically favorable, influencing the type and prevalence of defects observed in the material. First-principles calculations based on density functional theory (DFT) can provide quantitative formation energies for these defects, helping to clarify why certain stacking-fault structures are energetically favored over others.

## Approach
The planar defects are modeled using periodic supercells that contain 120 atoms each. The stacking sequences are described in Hägg notation, where a 'normal' bilayer is denoted '+' and a 'twinned' bilayer is denoted '−'. A perfect crystal is an all-plus or all-minus sequence. A single twin boundary is created by a single flip, e.g., …++++++ – – – – – –…, and n intrinsic stacking faults are introduced by n successive sign changes. For each configuration, a total-energy DFT calculation is performed in the local density approximation (LDA) with norm-conserving pseudopotentials, using the open-source plane-wave code Quantum ESPRESSO. Atomic positions are fully relaxed and the final total energy is extracted. The formation energy of a twin boundary is obtained from the energy difference between the supercell containing the boundary and the perfect crystal, divided by the total interface area in the supercell. The n‑th stacking fault energy for 3C‑SiC is computed as the energy per unit area needed to create an additional stacking fault beyond (n−1) existing faults, using the difference between the total energies of the n‑SF and (n−1)‑SF supercells.

## Reproduction target
Using LDA-DFT with norm-conserving pseudopotentials, calculate the twin boundary formation energy per unit area (mJ/m²) for 3C-SiC, Si, and diamond. Also, calculate the n‑th stacking fault energy (mJ/m²) for 3C-SiC for n = 1 to 10, defined as the energy per unit area to introduce one more stacking fault beyond (n−1) existing faults. Report the results in the two CSV files listed in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LDA norm-conserving pseudopotentials for Si and C: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Generate supercell structures
- Role: process
- Action: Construct 120-atom supercells for perfect 3C-SiC, Si, diamond and for configurations containing one twin boundary (…++++++-------…), as well as n intrinsic stacking faults (n=1..10) in 3C-SiC using Hägg notation and known lattice constants. Write the atomic coordinates for each configuration.
- Evidence: `/app/outputs/structures.json`

### Step 2: Run LDA-DFT geometry optimization and total energy calculations
- Role: process
- Action: For each supercell from step_01, perform a DFT calculation with LDA, norm-conserving pseudopotentials, a suitable plane-wave cutoff, and an appropriate k-point sampling. Fully relax atomic positions and extract the final total energy. Save all total energies.
- Evidence: `/app/outputs/energies.json`

### Step 3: Extract twin boundary formation energies
- Role: scored (load-bearing)
- Action: From the total energies in energies.json and the known interface area A, compute the formation energy per unit area for a twin boundary in each material. Write the results to formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: material, formation_energy. material is one of 'SiC', 'Si', 'diamond'. formation_energy is a float in mJ/m².
- Scoring: scored by hidden verifier

### Step 4: Extract stacking fault energy series
- Role: scored
- Action: From the total energies of the nSF and (n-1)SF supercells for 3C-SiC, compute the n-th stacking fault energy γ_n = (E(n)-E(n-1))/A for n=1..10. Write the results to sf_energies.csv.
- Output file: `/app/outputs/sf_energies.csv`
- Format: csv
- Contract: Columns: n, sf_energy. n is an integer from 1 to 10. sf_energy is a float in mJ/m².
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/sf_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Twin boundary formation energy per unit area for 3C-SiC, Si, and diamond. The checker will verify sign and approximate magnitude without requiring exact numerical reproduction.
- schema:
  - `type`: table
  - `required_columns`: `material`, `formation_energy`
  - `units`:
    - `formation_energy`: mJ/m²

### sf_energies.csv
- path: `/app/outputs/sf_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: n-th stacking fault energy for 3C-SiC (n=1..10). The checker will verify that the 2nd value is the most negative (minimum) and negative in sign.
- schema:
  - `type`: table
  - `required_columns`: `n`, `sf_energy`
  - `units`:
    - `sf_energy`: mJ/m²

Notes: Scoring uses T3 structural auditing: formation energies must show the correct sign pattern (SiC negative, Si positive, diamond large positive); the stacking fault series must show a negative minimum at n=2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "mJ/m²"
        }
      },
      "description": "Twin boundary formation energy per unit area for 3C-SiC, Si, and diamond. The checker will verify sign and approximate magnitude without requiring exact numerical reproduction."
    },
    {
      "file": "sf_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "sf_energy"
        ],
        "units": {
          "sf_energy": "mJ/m²"
        }
      },
      "description": "n-th stacking fault energy for 3C-SiC (n=1..10). The checker will verify that the 2nd value is the most negative (minimum) and negative in sign."
    }
  ],
  "notes": "Scoring uses T3 structural auditing: formation energies must show the correct sign pattern (SiC negative, Si positive, diamond large positive); the stacking fault series must show a negative minimum at n=2."
}
```

## How you are scored
Each score-carrying output file is evaluated independently by a hidden verifier. The verifier does not require exact numerical agreement with any specific literature values. Instead, it checks physically meaningful structural properties: the formation energies must exhibit correct sign patterns and physically plausible magnitudes for the three materials, and the stacking fault energy series must display a well-defined negative minimum. The final score is a weighted combination of the evaluations of the two artifacts.
