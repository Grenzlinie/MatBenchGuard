# Compute Effective Field Mobility of Si/SiO2 Interface Inversion Layer Using Dipole, Phonon, and Surface Roughness Scattering Models

## Problem background
In Si/SiO₂ interfaces of MOSFETs, carrier mobility is limited by scattering from substrate impurities, bulk phonons, and surface roughness. Recent theoretical work suggests that strong Si–O dipoles formed at the interface by charge transfer between silicon and oxygen atoms act as an additional scattering center. These dipoles, with a concentration on the order of 10¹⁴ cm⁻², cause both elastic and inelastic scattering that can significantly reduce mobility. This task reproduces the effective field mobility μeff as a function of effective electric field Eeff by implementing the interface dipole scattering model together with conventional phonon and surface roughness scattering models, thereby validating the claim that dipole scattering is a main component limiting carrier transport.

## Approach
The computational pipeline consists of six stages:
1. **Subband structure:** Self‑consistently solve the Poisson and Schrödinger equations for a (100) Si inversion layer to obtain subband energies, envelope wavefunctions, and carrier density profiles for all relevant valleys.
2. **Elastic dipole scattering amplitudes:** Using the interface dipole geometry and the effective charge e* = –1.1 e, solve the projected Poisson equations with the layered‑dielectric Green’s function and a screening model (Eq. 21 in the source paper) that accounts for both free‑carrier screening and dipole‑overlap screening. Perform orientational averaging to obtain the orientation‑averaged squared scattering amplitudes ⟨‖A_i^k(q)‖²⟩ for each subband and valley.
3. **Dipole‑limited mobility:** Compute elastic and inelastic dipole scattering relaxation times. The inelastic component arises from Si‑atom vibration with energy ħω = 17 meV (only the Si atom vibrates; the oxygen atom is essentially fixed). Average over subbands to obtain the dipole‑limited mobility μdipole as a function of Eeff.
4. **Phonon‑limited mobility:** Implement intravalley acoustic phonon scattering (isotropic deformation potential D_ac = 10 eV, sound velocity s_l = 9037 m/s) and intervalley phonon scattering using the f‑ and g‑phonon parameters listed below. Compute the phonon‑limited mobility μphonon.
5. **Surface‑roughness‑limited mobility:** Use the Matsumoto–Uemura model with the Pirovano power spectrum (exponent n = 4) and roughness parameters Δ = 0.35 nm, Λ = 1.2 nm. Obtain the surface‑roughness‑limited mobility μsr.
6. **Effective mobility:** Combine the three mobilities via Matthiessen’s rule: μeff⁻¹ = μdipole⁻¹ + μphonon⁻¹ + μsr⁻¹. Evaluate over Eeff from 0.1 to 1.0 MV/cm with at least 50 evenly spaced points and write the curve to `effective_mobility.csv`.

**Physical parameters supplied:**
- Si crystal density = 2329 kg m⁻³, sound velocity s_l = 9037 m s⁻¹, acoustic deformation potential D_ac = 10 eV.
- Intervalley phonons (energies and deformation potentials):
  - f‑phonons: ħω = 19.0 meV (D = 0.3 × 10⁸ eV/cm), 47.5 meV (2.0 × 10⁸ eV/cm), 59.1 meV (2.0 × 10⁸ eV/cm).
  - g‑phonons: ħω = 12.1 meV (0.5 × 10⁸ eV/cm), 18.6 meV (0.8 × 10⁸ eV/cm), 62.2 meV (11.0 × 10⁸ eV/cm).
- Effective masses, valley degeneracies, and other standard silicon parameters follow widely known theoretical values; the required subband solver may be built with any available open‑source code or implemented from scratch.
- Dipole concentration N_dipole = 6.87 × 10¹⁴ cm⁻².
- The first‑principles DFT calculation that determined e* and ħω is **excluded** from the workflow; use the reported values as fixed inputs.

## Reproduction target
Produce a CSV file `effective_mobility.csv` with columns `Eeff` (effective electric field in MV/cm) and `mu_eff` (effective mobility in cm² V⁻¹ s⁻¹). The file must contain at least 50 rows covering the range 0.1–1.0 MV/cm in evenly spaced steps. The curve is obtained by executing the six‑step workflow: solving the subband structure, computing dipole, phonon, and surface‑roughness mobilities, and combining them via Matthiessen’s rule. The result is compared against a hidden reference curve derived from the paper’s reported universal mobility curve.

## Assets

- All physical model parameters

## Workflow steps

### Step 1: Self-consistent Poisson-Schrödinger solver for inversion layer subbands
- Role: process
- Action: Solve the Poisson and Schrödinger equations self-consistently for a (100) Si inversion layer to obtain subband energies, envelope wavefunctions, and carrier density profiles for all relevant valleys. Use an appropriate open-source tool or implement the solver; retain results for later scattering rate calculations.
- Evidence: `/app/outputs/subband_data.json`

### Step 2: Compute elastic dipole scattering matrix elements
- Role: process
- Action: Using the interface dipole geometry (R_z, z_a, |r_a|) and effective charge e* = -1.1 e, solve the projected Poisson equations with the layered-dielectric Green's function and the screening model. Perform orientational averaging over random dipole positions to obtain the orientation-averaged squared scattering amplitudes <||A_i^k(q)||^2> for each subband and valley.
- Evidence: `/app/outputs/dipole_scattering_amplitudes.csv`

### Step 3: Compute dipole-limited mobility
- Role: process
- Action: Compute elastic and inelastic dipole scattering relaxation times using the averaged squared amplitudes from step 2 and the Si-atom vibrational energy 17 meV. Then compute the subband-resolved mobilities and average them (with subband occupancies) to obtain the total dipole-limited mobility μ_dipole as a function of effective electric field Eeff.
- Evidence: `/app/outputs/dipole_mobility.csv`

### Step 4: Compute phonon-limited mobility
- Role: process
- Action: Implement intravalley acoustic phonon scattering (using an isotropic deformation potential model with D_ac = 10 eV and sound velocity s_l = 9037 m/s) and intervalley phonon scattering using the parameters provided in the instructions. Compute the subband-resolved relaxation times and average to obtain the phonon-scattering-limited mobility μ_phonon as a function of Eeff.
- Evidence: `/app/outputs/phonon_mobility.csv`

### Step 5: Compute surface-roughness-limited mobility
- Role: process
- Action: Use the Matsumoto–Uemura surface roughness model with the Pirovano power spectrum (n=4) and parameters Δ=0.35 nm, Λ=1.2 nm. Compute the surface-roughness-limited mobility μ_sr as a function of Eeff.
- Evidence: `/app/outputs/surface_roughness_mobility.csv`

### Step 6: Compute effective universal mobility curve
- Role: scored (load-bearing)
- Action: Combine μ_dipole, μ_phonon, and μ_sr via Matthiessen's rule: μeff⁻¹ = μ_dipole⁻¹ + μ_phonon⁻¹ + μ_sr⁻¹. Evaluate for Eeff in the range 0.1–1.0 MV/cm with at least 50 evenly spaced points. Export the resulting μeff(Eeff) curve to effective_mobility.csv.
- Output file: `/app/outputs/effective_mobility.csv`
- Format: csv
- Contract: Eeff (float, MV/cm), mu_eff (float, cm^2/Vs)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_mobility.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_mobility.csv
- path: `/app/outputs/effective_mobility.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed effective field mobility as a function of effective electric field, obtained by combining dipole, phonon, and surface roughness mobilities via Matthiessen's rule.
- schema:
  - `type`: table
  - `required_columns`: `Eeff`, `mu_eff`
  - `units`:
    - `Eeff`: MV/cm
    - `mu_eff`: cm^2/Vs

Notes: The hidden reference curve is extracted from the paper's universal curve; the checker will interpolate the hidden data to the same Eeff points and compute the relative error. Full credit is awarded if every point has relative error ≤15%, with reward decaying linearly for larger errors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_mobility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Eeff",
          "mu_eff"
        ],
        "units": {
          "Eeff": "MV/cm",
          "mu_eff": "cm^2/Vs"
        }
      },
      "description": "Computed effective field mobility as a function of effective electric field, obtained by combining dipole, phonon, and surface roughness mobilities via Matthiessen's rule."
    }
  ],
  "notes": "The hidden reference curve is extracted from the paper's universal curve; the checker will interpolate the hidden data to the same Eeff points and compute the relative error. Full credit is awarded if every point has relative error ≤15%, with reward decaying linearly for larger errors."
}
```

## How you are scored
A hidden verifier loads your submitted `effective_mobility.csv` and compares each μeff value to the hidden reference curve. Full credit is awarded if every point satisfies a relative‑error threshold; reward decreases linearly for larger errors. The checker also confirms that all required intermediate artifacts (`subband_data.json`, `dipole_scattering_amplitudes.csv`, `dipole_mobility.csv`, `phonon_mobility.csv`, `surface_roughness_mobility.csv`) are present as evidence of the workflow, but the final score is determined by the accuracy of the effective mobility curve. Simply reporting a known number without executing the required computation will not pass the verifier.
