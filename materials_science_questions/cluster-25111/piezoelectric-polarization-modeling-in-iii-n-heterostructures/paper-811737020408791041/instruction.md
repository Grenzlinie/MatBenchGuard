# Semi-analytic modeling of quantum-confined Stark effects in a cylindrical GaN quantum dot

## Problem background
Gallium nitride quantum dots exhibit quantum-confined Stark effects where built-in polarization fields and external electric fields modify single-particle energy levels and optical transition properties. Understanding how lateral and vertical electric fields shift these energies is important for optoelectronic device design. This task models a cylindrical GaN quantum dot and computes the optical transition energy under different field directions using a semi-analytic separation of radial and axial potentials.

## Approach
The model uses an approximation that separates the confinement potential into a radial and an axial (growth direction) part. The built-in polarization potential along the growth direction is computed analytically from the dot geometry and material constants (piezoelectric, spontaneous polarization, misfit strain). For the radial part, the polarization-induced potential is approximated as a harmonic oscillator, whose curvature is obtained from the second derivative of the axial potential at the wavefunction maximum. Under a lateral electric field, the radial confinement energy includes a field-dependent term. For the axial part, the polarization slope and an external vertical field form a triangular-well potential; the unperturbed Schrödinger equation is solved using Airy functions with boundary condition matching, and a first-order perturbation correction accounts for the field outside the dot. The total transition energy is the sum of radial and axial energies for electrons and holes plus the band gap. The workflow implements this approach and then sweeps lateral field, vertical field, and combined field at varying angles, and finally fits the vertical-field energy shift to extract the permanent dipole moment, polarizability, and an estimate of the internal piezoelectric field.

## Reproduction target
Compute the optical transition energy \(E_T\) (in eV) for the cylindrical GaN quantum dot with radius 10.5 nm, height 4 nm, and aspect ratio \(f = 0.38\), using the described semi-analytical method, under the following conditions:
1. Lateral electric field \(F_1\) = 0, 50, 100, 150, 200 kV/cm with zero vertical field; also compute the electron and hole energy shifts relative to zero field.
2. Vertical electric field \(F_2\) = 0, 50, 100, 150, 200, 250, 300 kV/cm with zero lateral field.
3. Combined field at total magnitudes 100 and 200 kV/cm, decomposed into lateral and vertical components via \(F_1 = F_3 \sin\theta\), \(F_2 = F_3 \cos\theta\), for angles \(\theta = 0, 0.1, 0.2, 0.3, 0.4, 0.5\,\text{rad}\).
From the vertical-field sweep data, fit the energy shift \(\Delta E(F_2) = \mu F_2 + \alpha F_2^2\) to obtain the permanent dipole moment \(\mu\) (eÅ), polarizability \(\alpha\) (meV/(MV/cm)\(^2\)), and estimate the internal piezoelectric field (MV/cm) at which the shift is maximal.

## Assets

- Williams et al. 2005, Phys. Rev. B 72, 235318: 10.1103/PhysRevB.72.235318
- Pearton 2000, GaN and Related Materials (Book): https://www.routledge.com/GaN-and-Related-Materials/Pearton/p/book/9789056992901

## Workflow steps

### Step 1: Define geometry, material parameters, and implement the semi-analytic model
- Role: process
- Action: Implement the cylindrical GaN quantum dot model with geometry R=10.5 nm, h=4 nm, f=0.38. Code functions to: compute polarization potential φ(z) from analytical formulas using the dot dimensions and piezoelectric/spontaneous polarization constants; for a given vertical field F2, solve the axial Schrödinger equation (triangular well with band offset) using Airy functions and first-order perturbation theory to obtain axial energies and wavefunctions for electrons and holes; determine the radial curvature parameter k from the second derivative of φ(z) evaluated at the axial wavefunction maximum; compute the lateral harmonic confinement energy for a given lateral field F1; and assemble the optical transition energy E_T = E_r^e + E_r^h + E_z^e + E_z^h + E_G. Use material parameters (effective masses, band gap, band offsets, piezoelectric constants, dielectric constant, spontaneous polarizations, misfit strain, Poisson ratio) from Williams et al. 2005 and Pearton 2000.
- Evidence: `/app/outputs/model_log.txt`

### Step 2: Compute transition energies and carrier energy shifts for a lateral electric field sweep
- Role: scored (load-bearing)
- Action: Using the model, for lateral electric field F1 = 0, 50, 100, 150, 200 kV/cm with vertical field F2=0, compute the optical transition energy E_T (eV), the electron energy shift ΔE_c = E_e(F1) - E_e(0) (meV), and the hole energy shift ΔE_h = E_h(F1) - E_h(0) (meV). Write the results to a CSV file with columns: field_lateral_kV_per_cm, energy_eV, electron_shift_meV, hole_shift_meV.
- Output file: `/app/outputs/lateral_energies.csv`
- Format: csv
- Contract: columns: field_lateral_kV_per_cm (float), energy_eV (float), electron_shift_meV (float), hole_shift_meV (float)
- Scoring: scored by hidden verifier

### Step 3: Compute transition energies for a vertical electric field sweep
- Role: scored
- Action: Using the model, for vertical electric field F2 = 0, 50, 100, 150, 200, 250, 300 kV/cm with lateral field F1=0, compute the optical transition energy E_T (eV). Write a CSV with columns: field_vertical_kV_per_cm, energy_eV.
- Output file: `/app/outputs/vertical_energies.csv`
- Format: csv
- Contract: columns: field_vertical_kV_per_cm (float), energy_eV (float)
- Scoring: scored by hidden verifier

### Step 4: Compute transition energies for combined field at varying angles
- Role: scored
- Action: For total field magnitudes F3 = 100 and 200 kV/cm, compute the optical transition energy E_T for angles θ = 0, 0.1, 0.2, 0.3, 0.4, 0.5 rad, where the lateral component is F3 * sin(θ) and the vertical component is F3 * cos(θ). Write a CSV with columns: total_field_kV_per_cm, angle_rad, energy_eV.
- Output file: `/app/outputs/angle_energies.csv`
- Format: csv
- Contract: columns: total_field_kV_per_cm (float), angle_rad (float), energy_eV (float)
- Scoring: scored by hidden verifier

### Step 5: Extract permanent dipole, polarizability, and internal field from vertical-field data
- Role: scored
- Action: Read the vertical_energies.csv produced in the previous step. Compute the energy shift ΔE(F2) = E_T(F2) - E_T(0). Fit the quadratic model ΔE = μ F2 + α F2² via least squares to obtain the permanent dipole moment μ (in eÅ) and polarizability α (in meV/(MV/cm)²). Estimate the internal piezoelectric field as the field value where the quadratic shift reaches its maximum (or by appropriate extrapolation). Write a JSON file with keys: permanent_dipole_eA, polarizability_meV_per_MVcm2, internal_piezoelectric_field_MV_per_cm.
- Output file: `/app/outputs/fit_params.json`
- Format: json
- Contract: keys: permanent_dipole_eA (float), polarizability_meV_per_MVcm2 (float), internal_piezoelectric_field_MV_per_cm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lateral_energies.csv`
- `/app/outputs/vertical_energies.csv`
- `/app/outputs/angle_energies.csv`
- `/app/outputs/fit_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lateral_energies.csv
- path: `/app/outputs/lateral_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing optical transition energy and carrier energy shifts at five lateral field values (0, 50, 100, 150, 200 kV/cm) with zero vertical field. The hidden checker compares each value to the paper's reported numbers within a tolerance based on the expected precision of the semi-analytic method.
- schema:
  - `type`: table
  - `required_columns`: `field_lateral_kV_per_cm`, `energy_eV`, `electron_shift_meV`, `hole_shift_meV`
  - `units`:
    - `field_lateral_kV_per_cm`: kV/cm
    - `energy_eV`: eV
    - `electron_shift_meV`: meV
    - `hole_shift_meV`: meV

### vertical_energies.csv
- path: `/app/outputs/vertical_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing optical transition energy at seven vertical field values (0 to 300 kV/cm) with zero lateral field. The hidden checker compares the energies to the paper's reported values to verify the predicted blueshift and its magnitude.
- schema:
  - `type`: table
  - `required_columns`: `field_vertical_kV_per_cm`, `energy_eV`
  - `units`:
    - `field_vertical_kV_per_cm`: kV/cm
    - `energy_eV`: eV

### angle_energies.csv
- path: `/app/outputs/angle_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV containing optical transition energy for two total field magnitudes (100 and 200 kV/cm) at six angles (0 to 0.5 rad). The checker audits the structural trend: energy should be lower (redshift) at small angles and increase (blueshift) as angle grows, with the larger total field producing a larger net shift.
- schema:
  - `type`: table
  - `required_columns`: `total_field_kV_per_cm`, `angle_rad`, `energy_eV`
  - `units`:
    - `total_field_kV_per_cm`: kV/cm
    - `angle_rad`: rad
    - `energy_eV`: eV

### fit_params.json
- path: `/app/outputs/fit_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the fitted permanent dipole moment (eÅ), polarizability (meV/(MV/cm)^2), and estimated internal piezoelectric field (MV/cm) extracted from the vertical-field energy shift. The hidden checker compares these values to the paper's reported quantities within tolerances derived from the paper's stated uncertainties.
- schema:
  - `type`: object
  - `required`:
    - `permanent_dipole_eA`: number
    - `polarizability_meV_per_MVcm2`: number
    - `internal_piezoelectric_field_MV_per_cm`: number

Notes: All outputs must be placed under /app/outputs. The model_definition process step is required to build the computational model; it may write a log file but its output is not scored. The lateral_sweep step is load-bearing to ensure the model is actually executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lateral_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_lateral_kV_per_cm",
          "energy_eV",
          "electron_shift_meV",
          "hole_shift_meV"
        ],
        "units": {
          "field_lateral_kV_per_cm": "kV/cm",
          "energy_eV": "eV",
          "electron_shift_meV": "meV",
          "hole_shift_meV": "meV"
        }
      },
      "description": "CSV containing optical transition energy and carrier energy shifts at five lateral field values (0, 50, 100, 150, 200 kV/cm) with zero vertical field. The hidden checker compares each value to the paper's reported numbers within a tolerance based on the expected precision of the semi-analytic method."
    },
    {
      "file": "vertical_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_vertical_kV_per_cm",
          "energy_eV"
        ],
        "units": {
          "field_vertical_kV_per_cm": "kV/cm",
          "energy_eV": "eV"
        }
      },
      "description": "CSV containing optical transition energy at seven vertical field values (0 to 300 kV/cm) with zero lateral field. The hidden checker compares the energies to the paper's reported values to verify the predicted blueshift and its magnitude."
    },
    {
      "file": "angle_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_field_kV_per_cm",
          "angle_rad",
          "energy_eV"
        ],
        "units": {
          "total_field_kV_per_cm": "kV/cm",
          "angle_rad": "rad",
          "energy_eV": "eV"
        }
      },
      "description": "CSV containing optical transition energy for two total field magnitudes (100 and 200 kV/cm) at six angles (0 to 0.5 rad). The checker audits the structural trend: energy should be lower (redshift) at small angles and increase (blueshift) as angle grows, with the larger total field producing a larger net shift."
    },
    {
      "file": "fit_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "permanent_dipole_eA": "number",
          "polarizability_meV_per_MVcm2": "number",
          "internal_piezoelectric_field_MV_per_cm": "number"
        }
      },
      "description": "JSON file containing the fitted permanent dipole moment (eÅ), polarizability (meV/(MV/cm)^2), and estimated internal piezoelectric field (MV/cm) extracted from the vertical-field energy shift. The hidden checker compares these values to the paper's reported quantities within tolerances derived from the paper's stated uncertainties."
    }
  ],
  "notes": "All outputs must be placed under /app/outputs. The model_definition process step is required to build the computational model; it may write a log file but its output is not scored. The lateral_sweep step is load-bearing to ensure the model is actually executed."
}
```

## How you are scored
A hidden verifier independently checks each of the four output artifacts. For the lateral-field energies, vertical-field energies, and fitted parameters, the verifier compares your computed numbers to reference physical values (obtained by an independent reimplementation) with appropriate tolerances; the reward is higher the closer your results agree. For the angle-scan energies, the verifier performs a structural audit: it checks that the energy trends are physically consistent (e.g., the transition energy varies monotonically with angle in a manner consistent with the interplay of lateral and vertical fields) without requiring exact numerical agreement. The final reward is a weighted combination of the scores from all stages. Simply writing down numbers that look plausible is not sufficient; the verifier expects results that follow from correctly implementing the physical model described in the approach.
