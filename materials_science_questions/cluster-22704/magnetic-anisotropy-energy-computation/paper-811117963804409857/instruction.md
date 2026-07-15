# Magnetic Anisotropy Energy in Cu/FeCo/Hf and Cu/FeCo/Ta Multilayers

## Problem background
Understanding and controlling magnetic anisotropy (MA) in heavy-metal/ferromagnet heterostructures is central to spintronic device design, as it determines magnetization stability and switching behaviour. Density functional theory (DFT) with spin‑orbit coupling can predict the MA per unit interfacial area from first principles, allowing a systematic investigation of how the choice and thickness of a heavy‑metal cap layer affect the preferred magnetization direction. The goal of this task is to compute the thickness‑dependent MA for two prototypical cap materials, Hf and Ta, on a Cu/FeCo slab, providing a quantitative picture of the cap‑thickness effect on perpendicular magnetic anisotropy.

## Approach
The slab systems are modelled as a 4‑ML fcc Cu(001) layer (rotated 45°), a 3‑ML B2‑type FeCo ferromagnetic layer, and a cap layer of Hf or Ta with varying thickness. The in‑plane lattice constant is fixed to the equilibrium bulk value of FeCo, and the vacuum region above the cap is thick enough to decouple periodic images. Atomic positions are relaxed with DFT‑GGA while keeping the lateral dimensions fixed. For each relaxed structure, non‑collinear spin‑orbit coupled DFT total‑energy calculations are performed with the magnetization constrained along the in‑plane [100] direction and the out‑of‑plane [001] direction. The MA per unit area is obtained from the energy difference E[100]−E[001] divided by the slab area. All DFT calculations are carried out with an open‑source plane‑wave code (e.g., Quantum ESPRESSO) using PAW pseudopotentials from a standard library. The volume of computations requires systematic runs over Hf thicknesses from 0 to 10 monolayers and Ta thicknesses from 0 to 4 monolayers.

## Reproduction target
Produce a CSV file named MA_values.csv containing the computed magnetic anisotropy per unit area (in erg/cm²) for every combination of cap material and thickness listed below. Each row must contain three columns: cap_material (string, 'Hf' or 'Ta'), thickness_ML (integer number of cap monolayers), and MA_erg_per_cm2 (float).
- For Hf caps: include thicknesses of 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 MLs.
- For Ta caps: include thicknesses of 0, 1, 2, 3, and 4 MLs.
The MA must be computed from SOC‑DFT total‑energy differences as described in the workflow steps: MA = (E[100] − E[001]) / A, where A is the in‑plane area of the slab supercell. All intermediate calculations (lattice constant, relaxations, SOC energies) must be executed; the final CSV is the only scored artifact.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk FeCo lattice constant
- Role: process
- Action: Perform DFT relaxation of bulk B2-type FeCo to determine the equilibrium lattice constant using GGA exchange-correlation. Record the optimized lattice constant.
- Evidence: `/app/outputs/feCo_lattice_constant.txt`

### Step 2: Slab construction and relaxation
- Role: process
- Action: For each combination of cap material (Hf, Ta) and thickness n (Hf: 0-10 ML, Ta: 0-4 ML), build a slab supercell: 4 ML fcc Cu (rotated 45°), 3 ML B2 FeCo, n ML cap, and 15 Å vacuum. Fix in-plane lattice constant to the value from step_01. Relax atomic positions using DFT-GGA until forces are below a tight convergence criterion.
- Evidence: none

### Step 3: Spin-orbit coupled total energy calculations
- Role: process
- Action: For each relaxed slab, perform non-collinear spin-orbit coupled DFT calculations with magnetization constrained along the [100] (in-plane) and [001] (out-of-plane) directions. Use a high plane-wave cutoff and a dense k-point mesh. Extract total energies E[100] and E[001] for every system.
- Evidence: `/app/outputs/soc_energies.json`

### Step 4: MA computation and reporting
- Role: scored (load-bearing)
- Action: Read the total energies from step_03. For each slab compute the in-plane area A from the supercell dimensions. Calculate MA = (E[100] - E[001]) / A and convert to erg/cm². Write all results to MA_values.csv with columns: cap_material, thickness_ML, MA_erg_per_cm2. Include entries for Hf thicknesses 0-10 and Ta thicknesses 0-4.
- Output file: `/app/outputs/MA_values.csv`
- Format: csv
- Contract: Header: cap_material,thickness_ML,MA_erg_per_cm2. cap_material: 'Hf' or 'Ta'. thickness_ML: integer. MA_erg_per_cm2: float, positive for perpendicular, negative for in-plane.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/MA_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### MA_values.csv
- path: `/app/outputs/MA_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing computed magnetic anisotropy per unit area (erg/cm²) for Cu/FeCo/Hf(n) (n=0-10) and Cu/FeCo/Ta(n) (n=0-4). The checker compares each entry to hidden reference values within a tolerance and also evaluates structural consistency.
- schema:
  - `type`: table
  - `required_columns`: `cap_material`, `thickness_ML`, `MA_erg_per_cm2`

Notes: The MA values must be computed from total-energy differences of SOC-DFT calculations on the specified slab systems. The shape anisotropy estimate (approx -0.6 erg/cm²) is for context only and not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "MA_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cap_material",
          "thickness_ML",
          "MA_erg_per_cm2"
        ]
      },
      "description": "CSV containing computed magnetic anisotropy per unit area (erg/cm²) for Cu/FeCo/Hf(n) (n=0-10) and Cu/FeCo/Ta(n) (n=0-4). The checker compares each entry to hidden reference values within a tolerance and also evaluates structural consistency."
    }
  ],
  "notes": "The MA values must be computed from total-energy differences of SOC-DFT calculations on the specified slab systems. The shape anisotropy estimate (approx -0.6 erg/cm²) is for context only and not scored."
}
```

## How you are scored
Your submission MA_values.csv is evaluated by a hidden verifier that compares each entry against reference data derived from the original DFT study. The verifier checks both the numerical accuracy of individual MA values (with physically motivated tolerances) and the qualitative thickness dependence across the two cap materials. To earn a high score, your computed MA values must not only be close to the expected numbers but also correctly capture the essential structural trends as a function of cap thickness. Points are distributed across the entries and trend checks; there is no requirement to hit exact integer values, and reproducing the overall physical behaviour is more important than matching a single decimal digit.
