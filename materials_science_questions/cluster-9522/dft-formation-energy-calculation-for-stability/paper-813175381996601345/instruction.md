# Half-metallic properties of V-doped SnTe from first-principles DFT

## Problem background
Half-metallic materials, which are metallic in one spin channel and insulating in the other, are promising for spintronic applications. This task investigates the half-metallic properties of V-doped SnTe, a IV-VI semiconductor, in both rock-salt (RS) and zinc-blende (ZB) structures. Transition metal doping at high concentrations on the Sn sublattice can significantly modify the electronic structure, potentially inducing half-metallicity. The objective is to compute, from first principles, the equilibrium lattice constants, electronic band gaps in the minority spin channel, and magnetic moments for four ordered supercells, and to determine which compositions are half-metals.

## Approach
The electronic structure is computed using spin-polarized density functional theory (DFT) within the generalized gradient approximation (GGA) using the PBE exchange-correlation functional. Ordered supercells are constructed for the four compositions: RS Sn3V1Te4, RS Sn2V2Te4, RS Sn1V3Te4, and ZB Sn1V3Te4. For each supercell, the equilibrium lattice constant is determined by total-energy minimization (full structural relaxation of the cell). At the optimized geometry, a self-consistent field calculation is performed to obtain the spin-resolved density of states (DOS). From the DOS, the minority-spin band gap (G_MIS), defined as the energy gap in the minority spin channel at the Fermi level, and the half-metallic gap (G_HM), the distance from the Fermi level to the nearest minority band edge, are extracted. The total magnetic moment per formula unit is obtained by summing site-projected moments and interstitial contributions. The workflow uses an open-source DFT code (e.g., Quantum ESPRESSO) with standard scalar-relativistic PBE pseudopotentials; no spin-orbit coupling is included, consistent with the original theoretical treatment.

## Reproduction target
For each of the four ordered V-doped supercells (RS Sn3V1Te4, RS Sn2V2Te4, RS Sn1V3Te4, ZB Sn1V3Te4), perform a volume relaxation to obtain the equilibrium lattice constant a. At those equilibrium volumes, compute the spin-polarized electronic structure and extract: the minority-spin gap G_MIS (eV), the half-metallic gap G_HM (eV), and the total magnetic moment Tot_muB (μB) per formula unit. Use these results to determine whether each compound is half-metallic: a compound is classified as half-metallic if it exhibits a nonzero minority-spin gap and a nonzero half-metallic gap, and its total moment is close to an integer number of Bohr magnetons per formula unit (as required by the Slater-Pauling rule for half-metals). Write a CSV file half_metal_results.csv with columns: compound (string), a (Å), G_MIS (eV), G_HM (eV), Tot_muB (float), is_HM (boolean). List exactly these four compounds in the given order.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, ABINIT, Elk): https://www.quantum-espresso.org/
- PBE pseudopotentials for Sn, V, Te: https://pseudodojo.quantum-espresso.org/
- Python and common libraries (numpy, pandas, etc.): numpy, pandas

## Workflow steps

### Step 1: Prepare supercell structures
- Role: process
- Action: Construct the ordered supercells for RS Sn3V1Te4, RS Sn2V2Te4, RS Sn1V3Te4, and ZB Sn1V3Te4 with the correct space groups (RS Pm3m or P4/mmm, ZB P43m or P4m2) and initial lattice parameters estimated from standard rules or experiments.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: For each supercell, perform spin-polarized DFT structural relaxation (vary cell volume/shape) to find the equilibrium lattice constant using GGA-PBE exchange-correlation functional.
- Evidence: `/app/outputs/optimization.log`

### Step 3: DFT electronic structure at equilibrium
- Role: process
- Action: For each supercell at its optimized lattice constant, run a self-consistent spin-polarized calculation and compute the spin-resolved density of states (DOS). From the DOS, extract the minority-spin gap G_MIS, half-metallic gap G_HM, and total magnetic moment per formula unit (sum of site-projected and interstitial contributions).
- Evidence: none

### Step 4: Compile half-metallic properties
- Role: scored (load-bearing)
- Action: Collect the equilibrium lattice constant a, minority-spin gap G_MIS, half-metallic gap G_HM, total magnetic moment Tot_muB, and half-metallicity flag is_HM (true if G_MIS>0, G_HM>0, and Tot_muB≈3.00 μB) for each compound. Write the results to half_metal_results.csv.
- Output file: `/app/outputs/half_metal_results.csv`
- Format: csv
- Contract: CSV with columns: compound (string), a (angstrom), G_MIS (eV), G_HM (eV), Tot_muB (float), is_HM (boolean). One row per compound in order: 'RS Sn3V1Te4', 'RS Sn2V2Te4', 'RS Sn1V3Te4', 'ZB Sn1V3Te4'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/half_metal_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### half_metal_results.csv
- path: `/app/outputs/half_metal_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium lattice constant, minority-spin gap, half-metallic gap, total magnetic moment per formula unit, and half-metallic flag for the four V-doped SnTe supercells.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a`, `G_MIS`, `G_HM`, `Tot_muB`, `is_HM`
  - `units`:
    - `a`: angstrom
    - `G_MIS`: eV
    - `G_HM`: eV
    - `Tot_muB`: mu_B
    - `is_HM`: boolean

Notes: The hidden checker compares each reported value against a reference (paper's values) with prescribed tolerances. The agent must compute these quantities solely from the DFT procedures; no knowledge of the reference is revealed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "half_metal_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a",
          "G_MIS",
          "G_HM",
          "Tot_muB",
          "is_HM"
        ],
        "units": {
          "a": "angstrom",
          "G_MIS": "eV",
          "G_HM": "eV",
          "Tot_muB": "mu_B",
          "is_HM": "boolean"
        }
      },
      "description": "Computed equilibrium lattice constant, minority-spin gap, half-metallic gap, total magnetic moment per formula unit, and half-metallic flag for the four V-doped SnTe supercells."
    }
  ],
  "notes": "The hidden checker compares each reported value against a reference (paper's values) with prescribed tolerances. The agent must compute these quantities solely from the DFT procedures; no knowledge of the reference is revealed."
}
```

## How you are scored
A hidden verifier will compare your submitted half_metal_results.csv against reference values for each compound. For each numerical column, the verifier allows a tolerance; the half-metallic flag must match exactly. The overall reward is computed from the agreement across all four compounds, with the main weight on the half-metallic status and the total magnetic moment. Reporting accurate results after running the full DFT workflow is essential; simply guessing the reference values will not pass the numerical checks.
