# DFT Projected Density of States Orbital Analysis

## Problem background
Persistent luminescence materials such as Sr2MgSi2O7:Eu2+ can store energy and release it as light over long periods. The electronic structure, in particular the band gap of the host and the position of the Eu2+ 4f ground state inside that gap, is critical for understanding the luminescence mechanism. Density functional theory (DFT) calculations, especially with Hubbard U corrections, can predict these properties and show how the 4f level's position depends on the treatment of electron correlation. This task asks you to reproduce those DFT predictions using public tools and data.

## Approach
You will use a publicly available DFT code with GGA+U capability (e.g., Quantum ESPRESSO) and standard pseudopotentials. First, construct the tetragonal crystal structure of pure Sr2MgSi2O7 (space group P-42₁m, a=7.996 Å, c=5.152 Å) and compute its Kohn–Sham band gap using GGA. Then, build a Eu-doped supercell by substituting one Sr atom with Eu. On the doped supercell, perform spin‑polarized GGA+U calculations with spin–orbit coupling for several values of the Hubbard U parameter spanning 4.35–7.62 eV, keeping the exchange parameter J fixed at 0.68 eV. For each U, extract the spin‑resolved total and projected density of states, identify the occupied Eu 4f ground‑state peak and the band edges, and compute the energy differences between the 4f level and the valence/conduction bands. All inputs (crystal structure, pseudopotentials, DFT code) are openly available; the procedure is self‑contained.

## Reproduction target
Produce two output artifacts:
1. A text file with the computed GGA band gap (eV) of pure Sr2MgSi2O7.
2. A CSV file with columns U (eV), delta_VB (eV), delta_CB (eV) for at least four U values between 4.35 and 7.62 eV. delta_VB is the energy difference from the occupied Eu 4f peak to the valence‑band maximum; delta_CB is the difference from the conduction‑band minimum to that peak.
The verifier will independently check that the 4f state lies inside the gap and will analyze the relationship between the energy differences and the Hubbard U.

## Assets

- Crystal structure of Sr2MgSi2O7
- Quantum ESPRESSO (or other open-source DFT code with DFT+U capability): https://www.quantum-espresso.org/
- SSSP efficiency PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare host crystal structure
- Role: process
- Action: Obtain the crystal structure of Sr2MgSi2O7 (tetragonal P-42_1m, a=7.996 Å, c=5.152 Å) from public structural databases or literature. Build the unit cell and create the DFT input file for the pure host.
- Evidence: none

### Step 2: Compute band gap of pure Sr2MgSi2O7 (GGA)
- Role: scored
- Action: Using the DFT code, perform a GGA-PBE calculation on the pure Sr2MgSi2O7 host. Extract the Kohn-Sham band gap (the energy difference between the valence band maximum and conduction band minimum) and write the value in eV to the output file.
- Output file: `/app/outputs/bandgap_pure_host.txt`
- Format: txt
- Contract: A single line containing a floating-point number in units of eV (e.g. 6.7).
- Scoring: scored by hidden verifier

### Step 3: Build Eu-doped supercell
- Role: process
- Action: Construct the Eu2+-doped supercell by substituting one Sr atom with Eu in the unit cell, keeping lattice parameters unchanged, to serve as the input for DFT+U calculations.
- Evidence: none

### Step 4: Run DFT+U calculations for doped system with varying U
- Role: process
- Action: Using the DFT+U capability of the chosen code, run GGA+U calculations on the Eu-doped supercell at four or more U values covering the range 4.35–7.62 eV, with fixed exchange parameter J=0.68 eV. Include spin-orbit coupling if supported. For each U, save the spin-resolved total and projected density of states (DOS) or the required band-edge and 4f peak positions for later extraction.
- Evidence: none

### Step 5: Extract 4f position vs U
- Role: scored (load-bearing)
- Action: From the DOS of the doped system for each U, identify the occupied Eu2+ 4f ground-state peak (majority spin), the valence band maximum (VBM), and the conduction band minimum (CBM). Compute ΔE_VB = E_4f – VBM and ΔE_CB = CBM – E_4f. Write the results to a CSV file with columns U, delta_VB, delta_CB (all in eV).
- Output file: `/app/outputs/energy_differences_vs_U.csv`
- Format: csv
- Contract: CSV with header: U,delta_VB,delta_CB. Each row gives the Hubbard U value (eV), the energy difference from the occupied 4f peak to the VBM (eV), and the energy difference from that peak to the CBM (eV). At least four rows covering the U range 4.35–7.62 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap_pure_host.txt`
- `/app/outputs/energy_differences_vs_U.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap_pure_host.txt
- path: `/app/outputs/bandgap_pure_host.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Computed GGA band gap of Sr2MgSi2O7. The value is compared against the paper-reported reference band gap with a tolerance.
- schema:
  - `type`: text
  - `description`: A single line containing a floating-point number in eV.

### energy_differences_vs_U.csv
- path: `/app/outputs/energy_differences_vs_U.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy differences between the occupied Eu 4f peak and the band edges for each U. The checker verifies all deltas are positive (4f lies inside gap) and performs linear regression: slope of delta_VB vs U must be negative, slope of delta_CB vs U must be positive, with R² > 0.7 for both fits.
- schema:
  - `type`: table
  - `required_columns`: `U`, `delta_VB`, `delta_CB`
  - `units`:
    - `U`: eV
    - `delta_VB`: eV
    - `delta_CB`: eV

Notes: The two scored artifacts capture the main headline quantities: the host band gap and the linear dependence of the occupied 4f position on Hubbard U.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap_pure_host.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single line containing a floating-point number in eV."
      },
      "description": "Computed GGA band gap of Sr2MgSi2O7. The value is compared against the paper-reported reference band gap with a tolerance."
    },
    {
      "file": "energy_differences_vs_U.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "delta_VB",
          "delta_CB"
        ],
        "units": {
          "U": "eV",
          "delta_VB": "eV",
          "delta_CB": "eV"
        }
      },
      "description": "Energy differences between the occupied Eu 4f peak and the band edges for each U. The checker verifies all deltas are positive (4f lies inside gap) and performs linear regression: slope of delta_VB vs U must be negative, slope of delta_CB vs U must be positive, with R² > 0.7 for both fits."
    }
  ],
  "notes": "The two scored artifacts capture the main headline quantities: the host band gap and the linear dependence of the occupied 4f position on Hubbard U."
}
```

## How you are scored
A hidden verifier scores the two artifacts independently. The band gap value is compared against a reference with an appropriate tolerance. The energy‑differences CSV is checked for internal consistency: all delta_VB and delta_CB must be positive, and the dependence on U is tested for linearity and statistical significance. The final reward is a weighted sum (40% band gap, 60% energy‑differences) that rewards reproduction of the expected physical behavior. Reporting numbers without a correct underlying calculation is not sufficient.
