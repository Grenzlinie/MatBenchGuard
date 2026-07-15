# First-principles thermoelectric transport modeling of ferromagnetic chalcogenide spinels

## Problem background
HgCr2Z4 (Z = S, Se) are ferromagnetic chalcogenide spinels that have attracted interest for spintronic and thermoelectric device applications. First-principles calculations can predict their ground-state structural stability, magnetic exchange interactions, and electronic transport coefficients. This task asks you to compute these physical properties using density functional theory and semiclassical Boltzmann transport theory, producing numerical results that characterise the materials' performance.

## Approach
The computational approach proceeds in two stages. First, spin-polarised density functional theory (DFT) with the PBEsol exchange-correlation functional is used to optimise the crystal structures of ferromagnetic HgCr2S4 and HgCr2Se4, determine their equilibrium lattice constants and bulk moduli via Murnaghan's equation of state, and compute formation enthalpies from total energies of the spinel and isolated atoms. The electronic band structure and density of states are then refined with the modified Becke-Johnson (TB-mBJ) exchange-correlation potential to obtain accurate band gaps and magnetic moments. From the mBJ electronic structure, magnetic exchange constants (N0α, N0β) are extracted. In the second stage, the converged eigenvalues and crystal symmetry are fed into the BoltzTraP2 code, which solves the Boltzmann transport equation within the constant relaxation time approximation to compute the temperature‑dependent Seebeck coefficient and power factor (S²σ/τ). The transport properties are evaluated at three representative temperatures (200 K, 400 K, 600 K).

## Reproduction target
For both HgCr2S4 and HgCr2Se4, compute and report: (1) structural parameters: lattice constant a0, bulk modulus B0, formation enthalpy ΔHf; (2) magnetic properties: total magnetic moment per formula unit and the exchange constants N0α and N0β; (3) thermoelectric transport coefficients: the Seebeck coefficient S and the power factor S²σ/τ at temperatures of 200 K, 400 K, and 600 K. These results must be written into two CSV files, `structural_magnetic.csv` and `transport_properties.csv`, following the exact schemas described in the output contract below.

## Assets

- All-electron full-potential DFT code with PBEsol and TB-mBJ support: https://exciting-code.org/
- BoltzTraP2: https://github.com/HShima/BoltzTraP2

## Workflow steps

### Step 1: DFT structural optimization and formation enthalpy
- Role: process
- Action: For each compound (HgCr2S4 and HgCr2Se4) in the ferromagnetic phase, perform spin-polarized DFT volume optimization using the PBEsol exchange-correlation functional. Determine equilibrium lattice constant and bulk modulus by fitting the energy-volume curve to Murnaghan's equation of state. Compute formation enthalpy from total energies of the spinel and isolated atoms.
- Evidence: none

### Step 2: Electronic band structure and DOS with TB-mBJ
- Role: process
- Action: Using the optimized structures from step_01, compute spin-polarized band structure and density of states with the TB-mBJ exchange-correlation potential on a dense k‑mesh suitable for transport. Save the eigenvalue spectrum and symmetry information in a format readable by BoltzTraP2.
- Evidence: none

### Step 3: Extract structural and magnetic properties
- Role: scored
- Action: From the outputs of steps 01 and 02, extract the lattice constant a0 (Å), bulk modulus B0 (GPa), formation enthalpy ΔHf (eV), total magnetic moment per formula unit (μB), and exchange constants N0α and N0β (eV) for both HgCr2S4 and HgCr2Se4. Report the results in a CSV file with header: compound, a0_angstrom, B0_GPa, deltaH_eV, total_magnetic_moment_mu_B, exchange_constant_N0alpha_eV, exchange_constant_N0beta_eV.
- Output file: `/app/outputs/structural_magnetic.csv`
- Format: csv
- Contract: CSV with columns: compound, a0_angstrom, B0_GPa, deltaH_eV, total_magnetic_moment_mu_B, exchange_constant_N0alpha_eV, exchange_constant_N0beta_eV. Two rows (one per compound).
- Scoring: scored by hidden verifier

### Step 4: Compute transport coefficients with BoltzTraP2
- Role: scored (load-bearing)
- Action: Using the band eigenvalues from step_02, run BoltzTraP2 to compute the temperature‑dependent Seebeck coefficient S (μV/K) and electrical conductivity σ/τ in the constant relaxation time approximation. Evaluate at temperatures 200 K, 400 K, and 600 K. Calculate the power factor as S²σ/τ and report in arbitrary (Boltzmann) units. Write a CSV file with header: compound, temperature_K, Seebeck_uV_K, power_factor_arb_units. Each compound appears in three rows (one per temperature).
- Output file: `/app/outputs/transport_properties.csv`
- Format: csv
- Contract: CSV with columns: compound, temperature_K, Seebeck_uV_K, power_factor_arb_units. Six rows (2 compounds × 3 temperatures).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_magnetic.csv`
- `/app/outputs/transport_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_magnetic.csv
- path: `/app/outputs/structural_magnetic.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored structural and magnetic properties: lattice constant, bulk modulus, formation enthalpy, total magnetic moment, and exchange constants for HgCr2S4 and HgCr2Se4. The hidden reference consists of paper‑reported values with domain‑appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a0_angstrom`, `B0_GPa`, `deltaH_eV`, `total_magnetic_moment_mu_B`, `exchange_constant_N0alpha_eV`, `exchange_constant_N0beta_eV`

### transport_properties.csv
- path: `/app/outputs/transport_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored transport coefficients: Seebeck coefficient and power factor at 200, 400, 600 K for HgCr2S4 and HgCr2Se4. The hidden reference includes digitized graph values and required monotonic trends and compound ordering.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature_K`, `Seebeck_uV_K`, `power_factor_arb_units`

Notes: All outputs are re‑derivable from the agent's own DFT and Boltzmann transport runs. The scoring tolerances and trend checks are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_magnetic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a0_angstrom",
          "B0_GPa",
          "deltaH_eV",
          "total_magnetic_moment_mu_B",
          "exchange_constant_N0alpha_eV",
          "exchange_constant_N0beta_eV"
        ]
      },
      "description": "Scored structural and magnetic properties: lattice constant, bulk modulus, formation enthalpy, total magnetic moment, and exchange constants for HgCr2S4 and HgCr2Se4. The hidden reference consists of paper‑reported values with domain‑appropriate tolerances."
    },
    {
      "file": "transport_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature_K",
          "Seebeck_uV_K",
          "power_factor_arb_units"
        ]
      },
      "description": "Scored transport coefficients: Seebeck coefficient and power factor at 200, 400, 600 K for HgCr2S4 and HgCr2Se4. The hidden reference includes digitized graph values and required monotonic trends and compound ordering."
    }
  ],
  "notes": "All outputs are re‑derivable from the agent's own DFT and Boltzmann transport runs. The scoring tolerances and trend checks are hidden."
}
```

## How you are scored
Your submitted CSV files are evaluated by a hidden verifier that independently scores each workflow stage. For the structural and magnetic properties, the verifier compares each reported quantity against a set of reference values with appropriate tolerance. For the transport properties, the verifier checks the reported Seebeck coefficients and power factors against reference values and also verifies that they satisfy physically expected trends (e.g., monotonic increase with temperature and correct relative ordering between the two compounds). The final score is a weighted combination of all stage scores: roughly half the weight is assigned to structural and magnetic properties, and half to transport properties. The verifier does not reward simply copying published numbers; a high score requires truly executing the DFT and Boltzmann transport workflow.
