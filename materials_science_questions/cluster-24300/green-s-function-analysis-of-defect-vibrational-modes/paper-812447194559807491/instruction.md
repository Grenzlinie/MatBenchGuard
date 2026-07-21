# Electron-Impurity Scattering in Indium: Pseudopotential Study

## Problem background
Indium is a trivalent metal with a face‑centred tetragonal (FCT) structure and a complex Fermi surface. Electron‑impurity scattering governs transport properties such as residual resistivity and Dingle temperatures. This computational reproduction calculates scattering rates, transport relaxation times, residual resistivities, and Dingle temperatures for a vacancy and 11 substitutional impurities (Ag, Mg, Zn, Cd, Hg, Ga, Tl, Sn, Pb, Sb, Bi) in indium, using the 6‑plane‑wave pseudopotential (6‑ψPW) method with Heine–Abarenkov–Animalu model potentials and including lattice distortion via an exact structure factor. The target is to reproduce the predicted scattering characteristics from this pseudopotential framework.

## Approach
To capture the host electronic structure, the indium Fermi surface is represented in the 6‑ψPW scheme, which mixes six plane waves per k‑point. The host wavefunction coefficients and velocities are obtained by solving the 6×6 pseudo‑Hamiltonian eigenvalue problem at many k‑points on a 1/16th irreducible wedge of the Brillouin zone. For each impurity, the exact lattice‑distortion structure factor S(q) is computed by an Ewald summation using a given distortion parameter D. The impurity‑scattering matrix element between Bloch states is evaluated in the Born approximation from the host plane‑wave coefficients, impurity pseudopotential form factors, and the structure factor. From this, the local inverse lifetime τ₀⁻¹(k) and inverse transport relaxation time τ⁻¹(k) are obtained via the Ziman approximation, then averaged over defined Fermi‑surface regions (α‑arm, β‑arm, second zone, total). Residual resistivity is derived from the Boltzmann equation, solved iteratively for a few defects and using the Ziman approximation for all. Dingle temperatures are calculated from orbit‑averaged scattering rates using preset cyclotron masses and mass‑renormalization factors. The workflow, which mirrors a typical pseudopotential scattering computation, is structured as five ordered steps detailed below.

## Reproduction target
Generate three scored output files containing: (1) For each defect and each Fermi‑surface region (α‑arm, β‑arm, second zone, total), the averages of the inverse lifetime and inverse transport relaxation time (in units of 10¹³ s⁻¹ per at%). (2) For each defect, the average residual resistivity (in μΩ cm per at%). (3) For each defect, the Dingle temperatures for the second‑zone and β‑arm central [110] orbits (in K per at%). All quantities must be computed with the 6‑ψPW method using the exact q‑dependent structure factor, as specified in the workflow steps and output contract.

## Assets

- Heine-Abarenkov-Animalu model potential parameters for In, Ag, Mg, Zn, Cd, Hg, Ga, Tl, Sn, Pb, Sb, Bi: 10.1080/14786436408217525
- Indium face-centred tetragonal (FCT) crystal structure

## Workflow steps

### Step 1: Compute host Fermi surface and wavefunctions
- Role: process
- Action: Generate k-points on the indium Fermi surface in the irreducible 1/16th wedge of the FCT Brillouin zone. Solve the 6×6 pseudo-Hamiltonian eigenvalue problem at the Fermi energy to obtain wavefunction coefficients a_j(k) and velocities v(k). Compute cyclotron masses for the second-zone and β-arm central [110] orbits (m_c = 0.777 and 0.114 respectively, but do not hardcode these; they are a result of this step).
- Evidence: `/app/outputs/host_fs_info.json`

### Step 2: Compute exact structure factor S(q) for each defect
- Role: process
- Action: For each of the 12 defects (vacancy, Ag, Mg, Zn, Cd, Hg, Ga, Tl, Sn, Pb, Sb, Bi), use the provided lattice distortion parameter D and the indium FCT host lattice to compute the exact q-dependent structure factor S(q) via Ewald summation for all momentum transfers q = k' - k - G_{j'} + G_j that will appear in the matrix element sums.
- Evidence: `/app/outputs/struct_factor_data.npz`

### Step 3: Compute inverse lifetimes and transport relaxation times
- Role: scored (load-bearing)
- Action: For each defect, combine host wavefunction coefficients, impurity pseudopotential form factors (from the HAA model, and Ashcroft empty core for Ag), and the exact structure factor to compute the transition matrix element V_{k'k} in the Born approximation. Then compute the local inverse lifetime τ₀⁻¹(k) and the inverse transport relaxation time τ⁻¹(k) using the Ziman approximation. Average these quantities separately over the α-arm, β-arm, second zone, and the total Fermi surface. Write the results to the output file with columns for impurity, zone, and both averaged rates (in units 10¹³ s⁻¹/at%).
- Output file: `/app/outputs/table_I_scattering_rates.csv`
- Format: csv
- Contract: Columns: impurity (text), zone (text: alpha_arm, beta_arm, second_zone, total_FS), tau0_inv (float, unit 10^13 s^{-1}/at%), tau_inv (float, unit 10^13 s^{-1}/at%).
- Scoring: scored by hidden verifier

### Step 4: Compute residual resistivities
- Role: scored
- Action: Using the scattering rates and velocities, solve the Boltzmann equation iteratively for a subset of defects (vacancy, Zn, Ga, Pb) to obtain anisotropic resistivities ρ_a and ρ_c, and use the Ziman approximation to compute the average resistivity for all 12 defects. Write the resulting average resistivity for each impurity to the output file.
- Output file: `/app/outputs/table_IV_resistivities.csv`
- Format: csv
- Contract: Columns: impurity (text), resistivity_6psiPW (float, unit μΩ cm/at%).
- Scoring: scored by hidden verifier

### Step 5: Compute Dingle temperatures
- Role: scored
- Action: For each defect, average the local scattering rate τ₀⁻¹(k) over the second-zone and β-arm central [110] orbits. Convert to Dingle temperature T_D* using the formula T_D* = (ħ m_c)/(2π k_B m_c*) ⟨τ₀⁻¹(k)⟩_orbit, with the cyclotron masses m_c = 0.777 (second zone) and 0.114 (β-arm) and the renormalization factors m_c*/m_c = 1.52 and 1.79 respectively. Write the results to the output file.
- Output file: `/app/outputs/table_VI_Dingle_temperatures.csv`
- Format: csv
- Contract: Columns: impurity (text), orbit (text: second_zone, beta_arm), T_D (float, unit K/at%).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_I_scattering_rates.csv`
- `/app/outputs/table_IV_resistivities.csv`
- `/app/outputs/table_VI_Dingle_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_I_scattering_rates.csv
- path: `/app/outputs/table_I_scattering_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fermi-surface-averaged inverse lifetimes and inverse transport relaxation times (zone-resolved and total) for 12 defects.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `zone`, `tau0_inv`, `tau_inv`
  - `units`:
    - `tau0_inv`: 10^13 s^{-1}/at%
    - `tau_inv`: 10^13 s^{-1}/at%

### table_IV_resistivities.csv
- path: `/app/outputs/table_IV_resistivities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average residual resistivity for each of the 12 defects.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `resistivity_6psiPW`
  - `units`:
    - `resistivity_6psiPW`: μΩ cm/at%

### table_VI_Dingle_temperatures.csv
- path: `/app/outputs/table_VI_Dingle_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dingle temperatures for second-zone and β-arm [110] orbits for all 12 defects.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `orbit`, `T_D`
  - `units`:
    - `T_D`: K/at%

Notes: All quantities are to be computed using the 6-ψPW method with the exact q-dependent structure factor. Lattice distortion parameters D are provided in the instruction. The checker will compare each numeric value against hidden reference values from the paper using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_I_scattering_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "zone",
          "tau0_inv",
          "tau_inv"
        ],
        "units": {
          "tau0_inv": "10^13 s^{-1}/at%",
          "tau_inv": "10^13 s^{-1}/at%"
        }
      },
      "description": "Fermi-surface-averaged inverse lifetimes and inverse transport relaxation times (zone-resolved and total) for 12 defects."
    },
    {
      "file": "table_IV_resistivities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "resistivity_6psiPW"
        ],
        "units": {
          "resistivity_6psiPW": "μΩ cm/at%"
        }
      },
      "description": "Average residual resistivity for each of the 12 defects."
    },
    {
      "file": "table_VI_Dingle_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "orbit",
          "T_D"
        ],
        "units": {
          "T_D": "K/at%"
        }
      },
      "description": "Dingle temperatures for second-zone and β-arm [110] orbits for all 12 defects."
    }
  ],
  "notes": "All quantities are to be computed using the 6-ψPW method with the exact q-dependent structure factor. Lattice distortion parameters D are provided in the instruction. The checker will compare each numeric value against hidden reference values from the paper using appropriate tolerances."
}
```

## How you are scored
A hidden verifier inspects each of your three CSV artifacts. It extracts the numeric values from the required columns and compares them against a set of reference values derived from the same method. Correspondence to the reference is measured with appropriate tolerances; if your computed values are within tolerance, you earn full credit for that artifact. Larger discrepancies result in a proportionally lower score per artifact. The verifier combines the individual artifact scores into an overall reward between 0 and 1. The reference values and exact tolerances are not visible to you. Providing plausible values without actually performing the workflow will not score well.
