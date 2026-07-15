## Problem background

Strontium chalcogenides (SrS, SrSe, SrTe) are technologically important ionic materials with applications in X-ray cathodes and photoluminophors. Accurate knowledge of their structural stability and electronic band gaps is essential for understanding phase transitions and optoelectronic properties. This task reproduces first-principles density-functional theory (DFT) calculations of the equilibrium lattice constants, bulk moduli, and pressure derivatives of these compounds in both the NaCl-type (B1) and CsCl-type (B2) crystal structures, and the indirect electronic band gap along the Γ–X direction for the B1 structure.

## Approach

You will use an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with the Perdew–Wang local-density approximation (LDA) functional including gradient corrections (GGA). For each compound (SrS, SrSe, SrTe) and each crystal structure (B1 and B2), compute the total energy as a function of lattice constant over a range of volumes spanning the expected equilibrium. Fit the resulting energy–volume curves to the Murnaghan equation of state to extract the equilibrium lattice constant, bulk modulus, and pressure derivative. Then, using the equilibrium B1 structures, perform non-self-consistent band structure calculations along a high-symmetry path that includes the Γ and X points, and determine the indirect band gap.

## Reproduction target

Compute and report:
- For SrS, SrSe, SrTe in both B1 and B2 structures: equilibrium lattice constant a_eq (Å), bulk modulus B0 (Mbar), and pressure derivative B0'.
- For SrS, SrSe, SrTe in the B1 structure only: the indirect band gap (Γ–X) in eV.

The results are to be produced from a DFT workflow as described, without using pre-existing reference values.

## Assets

- **Quantum ESPRESSO** – open-source plane-wave DFT code (https://www.quantum-espresso.org/).
- **SSSP pseudopotential library (efficiency version)** – pseudopotentials for Sr, S, Se, Te (https://www.materialscloud.org/discover/sssp/table/efficiency).

You may install these and any needed dependencies at runtime.

## Workflow steps

### Step 1: Total energy calculations for equation of state
- Role: process
- Action: For each compound (SrS, SrSe, SrTe) and each crystal structure (B1: NaCl, B2: CsCl), generate Quantum ESPRESSO input files for at least 7 different lattice constants covering a range around the expected equilibrium volume. Perform self-consistent field (SCF) total energy calculations using the Perdew–Wang LDA functional with gradient corrections and appropriate pseudopotentials. Record the volume and total energy for each calculation.
- Evidence: /app/outputs/step_01_total_energies.csv

### Step 2: Fit equation of state and report structural properties (load-bearing)
- Role: scored
- Action: For each compound‑structure combination, fit the total energy vs volume data to the Murnaghan equation of state. Extract the equilibrium lattice constant a_eq (Å), bulk modulus B0 (Mbar), and pressure derivative B0'. Write the results to the output file.
- Output file: /app/outputs/step_02_structural_properties.csv
- Format: csv
- Contract: columns: compound (e.g., SrS), structure (B1 or B2), a_eq_angstrom, B0_Mbar, B0_prime
- Scoring: scored by hidden verifier

### Step 3: Band structure calculation for B1 structures
- Role: process
- Action: Using the equilibrium B1 lattice constants obtained in Step 2, run a non‑self‑consistent band structure calculation with Quantum ESPRESSO along a high‑symmetry path that includes the Γ and X points for each compound (SrS, SrSe, SrTe). Obtain the Kohn‑Sham eigenvalues along the path.
- Evidence: /app/outputs/step_03_bands.dat

### Step 4: Extract indirect band gap
- Role: scored
- Action: From the band structure data, identify the valence band maximum and conduction band minimum along the Γ–X segment. Compute the indirect band gap (E_g^(Γ‑X)) in eV for each B1 compound. Write the results to the output file.
- Output file: /app/outputs/step_04_band_gaps.csv
- Format: csv
- Contract: columns: compound (e.g., SrS), indirect_gap_Gamma_X_eV
- Scoring: scored by hidden verifier

## Output files

All files must be placed under /app/outputs. The scored output files are:
- /app/outputs/step_02_structural_properties.csv
- /app/outputs/step_04_band_gaps.csv

Intermediate evidence files (step_01_total_energies.csv, step_03_bands.dat) should be produced but are not directly scored.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_structural_properties.csv
- path: `/app/outputs/step_02_structural_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Structural parameters for SrS, SrSe, SrTe in B1 and B2 structures, extracted from DFT equation-of-state fitting.
- schema:
  - `required_columns`: `compound`, `structure`, `a_eq_angstrom`, `B0_Mbar`, `B0_prime`
  - `units`:
    - `a_eq_angstrom`: Å
    - `B0_Mbar`: Mbar
    - `B0_prime`: dimensionless

### step_04_band_gaps.csv
- path: `/app/outputs/step_04_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Indirect band gap (Γ–X) in eV for SrS, SrSe, SrTe in the B1 (NaCl) structure, obtained from DFT band structure calculations.
- schema:
  - `required_columns`: `compound`, `indirect_gap_Gamma_X_eV`
  - `units`:
    - `indirect_gap_Gamma_X_eV`: eV

Notes: No gold values or tolerances are public. The verifier uses hidden reference values and verifies qualitative trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_structural_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "compound",
          "structure",
          "a_eq_angstrom",
          "B0_Mbar",
          "B0_prime"
        ],
        "units": {
          "a_eq_angstrom": "Å",
          "B0_Mbar": "Mbar",
          "B0_prime": "dimensionless"
        }
      },
      "description": "Structural parameters for SrS, SrSe, SrTe in B1 and B2 structures, extracted from DFT equation-of-state fitting."
    },
    {
      "file": "step_04_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "compound",
          "indirect_gap_Gamma_X_eV"
        ],
        "units": {
          "indirect_gap_Gamma_X_eV": "eV"
        }
      },
      "description": "Indirect band gap (Γ–X) in eV for SrS, SrSe, SrTe in the B1 (NaCl) structure, obtained from DFT band structure calculations."
    }
  ],
  "notes": "No gold values or tolerances are public. The verifier uses hidden reference values and verifies qualitative trends."
}
```

## How you are scored

A hidden verifier independently checks each scored workflow stage's output file. The verifier compares your reported values for structural properties and band gaps to hidden reference values derived from the original study, using appropriate tolerances. It also verifies qualitative trends (e.g., lattice constant ordering, bulk modulus ordering). Every scored stage contributes a weighted share to a final reward between 0 and 1. Reporting numbers alone is not sufficient; the verifier expects artifacts that are consistent with a genuine DFT workflow.
