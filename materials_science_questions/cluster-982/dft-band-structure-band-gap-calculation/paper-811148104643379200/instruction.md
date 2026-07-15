# Optoelectronic Properties of Nb3O7(OH) and H-Nb2O5 from DFT

## Problem background
Niobium oxide nanostructures, particularly orthorhombic Nb3O7(OH) and monoclinic H-Nb2O5, are promising photoelectrode materials. Their performance in photoelectrochemical applications depends critically on their optoelectronic properties: the size and nature of the electronic band gap, the dielectric response, optical conductivity, and charge transport characteristics. This task addresses the first-principles computation of these properties using density-functional theory, enabling a direct comparison between the two crystal phases.

## Approach
The computational workflow employs density-functional theory (DFT) with the TB-mBJ meta-GGA exchange-correlation functional, which has been shown to provide accurate band gaps for this class of oxides. Starting from the crystallographic information files (CIFs) of the two structures, atomic positions are first relaxed using the PBE functional. Self-consistent field calculations then yield the Kohn-Sham eigenvalues and wavefunctions on a dense k-point grid. The band structure is computed along high-symmetry lines to identify the fundamental (indirect) and optical band gaps and to later extract effective masses.

From the SCF wavefunctions, the frequency-dependent complex dielectric tensor is calculated using linear-response theory. The real and imaginary parts of the dielectric function are obtained for two polarization directions: perpendicular ([100]) and parallel ([001]), covering the energy range 0–20 eV. The optical conductivity spectrum is derived directly from the imaginary part of the dielectric function. The static dielectric constant ε₁(0) is read from the real part at zero energy.

Electron and hole effective masses are obtained by parabolic fitting of the band dispersion near the valence band maximum and conduction band minimum. Finally, the Boltzmann transport equation is solved within the constant relaxation-time approximation using the BoltzTraP code, taking the band structure as input, to compute the average thermoelectric conductivity at 300 K as a function of chemical potential.

## Reproduction target
For both Nb3O7(OH) and H-Nb2O5, compute and provide the following artifacts:

- The full real and imaginary parts of the dielectric function for perpendicular and parallel polarizations as CSV files (0–20 eV).
- The optical conductivity for the two polarizations as CSV files (0–20 eV).
- A summary JSON file containing the fundamental (indirect) band gap, optical band gap, static dielectric constants ε₁(0) for both polarizations, electron effective mass, hole effective mass, and the average thermoelectric conductivity at 300 K (n-type).

All files must follow the exact column schemas and units described in the workflow steps and output contract.

## Assets

- Nb3O7(OH) crystal structure (CIF): https://pubs.acs.org/doi/suppl/10.1021/acs.jpcc.6b06391
- H-Nb2O5 crystal structure (CIF): https://pubs.acs.org/doi/suppl/10.1021/acs.jpcc.6b06391
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP: https://www.boltztrapp.net/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Relax atomic positions of Nb3O7(OH) and H-Nb2O5 using the GGA (PBE) functional, starting from the provided CIF files. Ensure forces and stresses are converged.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Self-consistent field and band structure
- Role: process
- Action: Perform self-consistent field calculation with a meta-GGA functional approximating TB-mBJ (e.g., SCAN or mBJ via libxc) to obtain Kohn-Sham eigenvalues and wavefunctions. Compute band structure along high-symmetry paths of the Brillouin zone for both compounds. Extract the eigenvalues at k-points to enable effective mass computation.
- Evidence: `/app/outputs/scf_output.log`

### Step 3: Dielectric function of Nb3O7(OH)
- Role: scored
- Action: Using the TB-mBJ eigenvalues and wavefunctions, compute the frequency-dependent complex dielectric tensor components (perpendicular and parallel) for Nb3O7(OH) along the [100] and [001] directions. Write the real and imaginary parts as a function of energy to a CSV file.
- Output file: `/app/outputs/dielectric_function_Nb3O7OH.csv`
- Format: csv
- Contract: CSV with columns: Energy(eV), epsilon1_perp, epsilon1_par, epsilon2_perp, epsilon2_par. Energy range 0–20 eV.
- Scoring: scored by hidden verifier

### Step 4: Dielectric function of H-Nb2O5
- Role: scored
- Action: Using the TB-mBJ eigenvalues and wavefunctions, compute the frequency-dependent complex dielectric tensor components (perpendicular and parallel) for H-Nb2O5 along the [100] and [001] directions. Write the real and imaginary parts as a function of energy to a CSV file.
- Output file: `/app/outputs/dielectric_function_HNb2O5.csv`
- Format: csv
- Contract: CSV with columns: Energy(eV), epsilon1_perp, epsilon1_par, epsilon2_perp, epsilon2_par. Energy range 0–20 eV.
- Scoring: scored by hidden verifier

### Step 5: Optical conductivity of Nb3O7(OH)
- Role: scored
- Action: From the dielectric function, compute the optical conductivity sigma(omega) = (omega/2*pi) * epsilon2(omega) for perpendicular and parallel polarizations. Write the energy-dependent conductivity to CSV.
- Output file: `/app/outputs/optical_conductivity_Nb3O7OH.csv`
- Format: csv
- Contract: CSV with columns: Energy(eV), sigma_perp (s^-1), sigma_par (s^-1). Energy range 0–20 eV.
- Scoring: scored by hidden verifier

### Step 6: Optical conductivity of H-Nb2O5
- Role: scored
- Action: From the dielectric function, compute the optical conductivity sigma(omega) = (omega/2*pi) * epsilon2(omega) for perpendicular and parallel polarizations. Write the energy-dependent conductivity to CSV.
- Output file: `/app/outputs/optical_conductivity_HNb2O5.csv`
- Format: csv
- Contract: CSV with columns: Energy(eV), sigma_perp (s^-1), sigma_par (s^-1). Energy range 0–20 eV.
- Scoring: scored by hidden verifier

### Step 7: Summary of band gaps, effective masses, and transport properties
- Role: scored (load-bearing)
- Action: Extract the fundamental (indirect) and optical band gaps from the band structure. Compute electron and hole effective masses by fitting the band dispersion near the VBM and CBM. Run Boltzmann transport code (BoltzTraP) using the band structure to compute the average thermoelectric conductivity at 300 K as a function of chemical potential. Collect the static dielectric constants epsilon1(0) from the dielectric function CSVs. Assemble all quantities into a JSON file.
- Output file: `/app/outputs/summary_values.json`
- Format: json
- Contract: JSON object with keys 'Nb3O7(OH)' and 'H-Nb2O5'. Each value is an object containing: fundamental_gap (eV), optical_gap (eV), static_epsilon1_perp (float), static_epsilon1_par (float), electron_effective_mass (m_e), hole_effective_mass (m_e), thermoelectric_conductivity_300K ((Omega*m*s)^-1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dielectric_function_Nb3O7OH.csv`
- `/app/outputs/dielectric_function_HNb2O5.csv`
- `/app/outputs/optical_conductivity_Nb3O7OH.csv`
- `/app/outputs/optical_conductivity_HNb2O5.csv`
- `/app/outputs/summary_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dielectric_function_Nb3O7OH.csv
- path: `/app/outputs/dielectric_function_Nb3O7OH.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Real and imaginary parts of the dielectric function for Nb3O7(OH) for perpendicular and parallel polarizations, 0–20 eV.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `epsilon1_perp`, `epsilon1_par`, `epsilon2_perp`, `epsilon2_par`
  - `units`:
    - `Energy(eV)`: eV
    - `epsilon1_perp`: dimensionless
    - `epsilon1_par`: dimensionless
    - `epsilon2_perp`: dimensionless
    - `epsilon2_par`: dimensionless

### dielectric_function_HNb2O5.csv
- path: `/app/outputs/dielectric_function_HNb2O5.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Real and imaginary parts of the dielectric function for H-Nb2O5 for perpendicular and parallel polarizations, 0–20 eV.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `epsilon1_perp`, `epsilon1_par`, `epsilon2_perp`, `epsilon2_par`
  - `units`:
    - `Energy(eV)`: eV
    - `epsilon1_perp`: dimensionless
    - `epsilon1_par`: dimensionless
    - `epsilon2_perp`: dimensionless
    - `epsilon2_par`: dimensionless

### optical_conductivity_Nb3O7OH.csv
- path: `/app/outputs/optical_conductivity_Nb3O7OH.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Optical conductivity for Nb3O7(OH) for perpendicular and parallel polarizations, 0–20 eV.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `sigma_perp`, `sigma_par`
  - `units`:
    - `Energy(eV)`: eV
    - `sigma_perp`: s^-1
    - `sigma_par`: s^-1

### optical_conductivity_HNb2O5.csv
- path: `/app/outputs/optical_conductivity_HNb2O5.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Optical conductivity for H-Nb2O5 for perpendicular and parallel polarizations, 0–20 eV.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `sigma_perp`, `sigma_par`
  - `units`:
    - `Energy(eV)`: eV
    - `sigma_perp`: s^-1
    - `sigma_par`: s^-1

### summary_values.json
- path: `/app/outputs/summary_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Consolidated summary of band gaps, effective masses, static dielectric constants, and thermoelectric conductivity for both compounds.
- schema:
  - `type`: object
  - `required`:
    - `Nb3O7(OH)`:
      - `type`: object
      - `required`: `fundamental_gap`, `optical_gap`, `static_epsilon1_perp`, `static_epsilon1_par`, `electron_effective_mass`, `hole_effective_mass`, `thermoelectric_conductivity_300K`
      - `units`:
        - `fundamental_gap`: eV
        - `optical_gap`: eV
        - `static_epsilon1_perp`: dimensionless
        - `static_epsilon1_par`: dimensionless
        - `electron_effective_mass`: m_e
        - `hole_effective_mass`: m_e
        - `thermoelectric_conductivity_300K`: (Omega*m*s)^-1
    - `H-Nb2O5`:
      - `type`: object
      - `required`: `fundamental_gap`, `optical_gap`, `static_epsilon1_perp`, `static_epsilon1_par`, `electron_effective_mass`, `hole_effective_mass`, `thermoelectric_conductivity_300K`
      - `units`:
        - `fundamental_gap`: eV
        - `optical_gap`: eV
        - `static_epsilon1_perp`: dimensionless
        - `static_epsilon1_par`: dimensionless
        - `electron_effective_mass`: m_e
        - `hole_effective_mass`: m_e
        - `thermoelectric_conductivity_300K`: (Omega*m*s)^-1

Notes: Omitted: core-level EELS (Nb-M3 and O-K edges), experimental low-loss EELS, and the artificial Nb3O8 reference compound. The original WIEN2k code is replaced with Quantum ESPRESSO using a meta-GGA functional (e.g., mBJ via libxc or SCAN) that approximates TB-mBJ.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dielectric_function_Nb3O7OH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "epsilon1_perp",
          "epsilon1_par",
          "epsilon2_perp",
          "epsilon2_par"
        ],
        "units": {
          "Energy(eV)": "eV",
          "epsilon1_perp": "dimensionless",
          "epsilon1_par": "dimensionless",
          "epsilon2_perp": "dimensionless",
          "epsilon2_par": "dimensionless"
        }
      },
      "description": "Real and imaginary parts of the dielectric function for Nb3O7(OH) for perpendicular and parallel polarizations, 0–20 eV."
    },
    {
      "file": "dielectric_function_HNb2O5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "epsilon1_perp",
          "epsilon1_par",
          "epsilon2_perp",
          "epsilon2_par"
        ],
        "units": {
          "Energy(eV)": "eV",
          "epsilon1_perp": "dimensionless",
          "epsilon1_par": "dimensionless",
          "epsilon2_perp": "dimensionless",
          "epsilon2_par": "dimensionless"
        }
      },
      "description": "Real and imaginary parts of the dielectric function for H-Nb2O5 for perpendicular and parallel polarizations, 0–20 eV."
    },
    {
      "file": "optical_conductivity_Nb3O7OH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "sigma_perp",
          "sigma_par"
        ],
        "units": {
          "Energy(eV)": "eV",
          "sigma_perp": "s^-1",
          "sigma_par": "s^-1"
        }
      },
      "description": "Optical conductivity for Nb3O7(OH) for perpendicular and parallel polarizations, 0–20 eV."
    },
    {
      "file": "optical_conductivity_HNb2O5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "sigma_perp",
          "sigma_par"
        ],
        "units": {
          "Energy(eV)": "eV",
          "sigma_perp": "s^-1",
          "sigma_par": "s^-1"
        }
      },
      "description": "Optical conductivity for H-Nb2O5 for perpendicular and parallel polarizations, 0–20 eV."
    },
    {
      "file": "summary_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Nb3O7(OH)": {
            "type": "object",
            "required": [
              "fundamental_gap",
              "optical_gap",
              "static_epsilon1_perp",
              "static_epsilon1_par",
              "electron_effective_mass",
              "hole_effective_mass",
              "thermoelectric_conductivity_300K"
            ],
            "units": {
              "fundamental_gap": "eV",
              "optical_gap": "eV",
              "static_epsilon1_perp": "dimensionless",
              "static_epsilon1_par": "dimensionless",
              "electron_effective_mass": "m_e",
              "hole_effective_mass": "m_e",
              "thermoelectric_conductivity_300K": "(Omega*m*s)^-1"
            }
          },
          "H-Nb2O5": {
            "type": "object",
            "required": [
              "fundamental_gap",
              "optical_gap",
              "static_epsilon1_perp",
              "static_epsilon1_par",
              "electron_effective_mass",
              "hole_effective_mass",
              "thermoelectric_conductivity_300K"
            ],
            "units": {
              "fundamental_gap": "eV",
              "optical_gap": "eV",
              "static_epsilon1_perp": "dimensionless",
              "static_epsilon1_par": "dimensionless",
              "electron_effective_mass": "m_e",
              "hole_effective_mass": "m_e",
              "thermoelectric_conductivity_300K": "(Omega*m*s)^-1"
            }
          }
        }
      },
      "description": "Consolidated summary of band gaps, effective masses, static dielectric constants, and thermoelectric conductivity for both compounds."
    }
  ],
  "notes": "Omitted: core-level EELS (Nb-M3 and O-K edges), experimental low-loss EELS, and the artificial Nb3O8 reference compound. The original WIEN2k code is replaced with Quantum ESPRESSO using a meta-GGA functional (e.g., mBJ via libxc or SCAN) that approximates TB-mBJ."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier. The verifier will:
- Read the dielectric function and optical conductivity CSVs, recompute key features such as absorption thresholds, peak positions and magnitudes, and the static dielectric constant ε₁(0). These recomputed values are compared against reference data using appropriate tolerances.
- Read summary_values.json and compare each reported quantity against reference results.
- Check the relative anisotropy trend (the difference between perpendicular and parallel components) between the two compounds.

Each scored file carries a weight; the final score is the weighted sum of partial scores. Simply reporting numbers is not sufficient — the verifier recomputes quantities from your raw data. The reference results are derived from the original study and are not disclosed.
