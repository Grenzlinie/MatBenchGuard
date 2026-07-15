# First-principles and thermodynamic properties of CrAlB

## Problem background
Transition metal borides with layered structures are promising for high-temperature and optoelectronic applications, but the properties of the ternary compound CrAlB have not been previously reported. This work addresses the need to predict the structural, electronic, optical, and thermal behavior of CrAlB using first‑principles calculations, providing quantitative estimates that can guide experimental synthesis and device design.

## Approach
The properties are obtained from density functional theory (DFT) with the PBEsol‑GGA exchange‑correlation functional. The crystal structure is relaxed to find the equilibrium geometry, and the electronic ground state provides wavefunctions for the optical response. The quasi‑harmonic Debye model is then applied to the energy‑volume data to derive thermodynamic quantities over a wide temperature and pressure range. The key outputs are equilibrium lattice parameters, the imaginary dielectric function for all three polarization directions, and a family of thermal properties including heat capacity, thermal expansion, and the Debye temperature.

## Reproduction target
Using Quantum ESPRESSO (an open‑source DFT code) with PBEsol‑GGA pseudopotentials for Cr, Al, and B, perform the following: (1) relax the CrAlB crystal structure (space group Cmcm, atomic positions: Cr (0, 0.4149, 0.25), Al (0, 0.1943, 0.25), B (0, 0.03360, 0.25)) to obtain equilibrium lattice constants; (2) run a self‑consistent calculation at the equilibrium volume to obtain the ground‑state wavefunctions; (3) compute the frequency‑dependent imaginary dielectric function ε₂(ω) for photon energies from 0 to 40 eV along the xx, yy, and zz directions; (4) calculate the total energy for a set of unit‑cell volumes around the equilibrium to obtain energy‑volume (E‑V) pairs; (5) implement the quasi‑harmonic Debye model using the E‑V data to compute thermodynamic properties (unit‑cell volume, bulk modulus, Debye temperature, thermal expansion coefficient, heat capacities Cv and Cp, entropy, internal energy) over the temperature range 0–5000 K at pressures 0, 20, and 50 GPa. From the computed data, extract (i) the equilibrium lattice constants a, b, c (in Å) from a Murnaghan fit, (ii) the three principal peaks of ε₂ (peak value and corresponding energy for each polarization), (iii) the plasma frequency (energy of the maximum in the loss function derived from the dielectric data), and (iv) the high‑temperature limiting value of Cv and the Debye temperature at 300 K and 0 GPa. Package these extracted quantities in a JSON file according to the output contract, and also provide the raw E‑V, dielectric, and thermal CSV files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Cr PBEsol pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- Al PBEsol pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- B PBEsol pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- CrAlB crystal structure definition

## Workflow steps

### Step 1: Geometry optimization and equation-of-state data
- Role: scored
- Action: Perform DFT geometry optimization using PBEsol-GGA. Compute total energy for 8-12 unit-cell volumes around equilibrium, covering compression and expansion. Fit the Murnaghan equation of state to obtain equilibrium lattice constants and bulk modulus. Save the energy-volume pairs.
- Output file: `/app/outputs/step_01_e_v_data.csv`
- Format: csv
- Contract: CSV with columns: volume (bohr^3), energy (Ry).
- Scoring: scored by hidden verifier

### Step 2: Self-consistent field calculation at equilibrium geometry
- Role: process
- Action: Run a self-consistent DFT calculation at the equilibrium lattice constants to obtain converged ground-state charge density, Kohn-Sham eigenvalues and wavefunctions, required for optical property calculation.
- Evidence: `/app/outputs/scf_convergence.log`

### Step 3: Optical dielectric function calculation
- Role: scored
- Action: From the ground-state wavefunctions obtained in step02, calculate the frequency-dependent imaginary part of the dielectric tensor (epsilon2) for photon energies from 0 to 40 eV, including a sufficient number of empty bands. Output epsilon2 for the xx, yy, zz components on a dense energy grid.
- Output file: `/app/outputs/step_02_dielectric_function.csv`
- Format: csv
- Contract: CSV with columns: energy_eV, eps2_xx, eps2_yy, eps2_zz.
- Scoring: scored by hidden verifier

### Step 4: Thermodynamic property simulation (quasi-harmonic Debye model)
- Role: scored
- Action: Implement the quasi‑harmonic Debye model. Fit the E‑V data from step_01_e_v_data.csv to a smooth E(V) curve (e.g., Murnaghan equation of state). For each pressure P in {0, 20, 50} GPa and temperature T in [0, 5000] K, compute the Debye temperature Θ_D = (h/k_B) [6π² V^{1/2} n]^{1/3} f(σ) √(B_S / M), where n=3 (atoms per formula unit), M is the molecular mass of one formula unit (CrAlB), f(σ)≈0.75 (Poisson factor), and B_S ≈ V d²E/dV². The non‑equilibrium Gibbs function is G*(V; P, T) = E(V) + P V + A_vib(Θ_D, T), with A_vib = n k_B T [9Θ_D/(8T) + 3 ln(1 − exp(−Θ_D/T)) − D(Θ_D/T)], where D(y) is the Debye integral. Minimize G* with respect to volume V to find the equilibrium volume at each (P,T). From the volume derivative of G* derive bulk modulus, thermal expansion α, heat capacities Cv and Cp, entropy, and internal energy using standard thermodynamic identities. Output all quantities for each (T,P) point.
- Output file: `/app/outputs/step_03_thermal_properties.csv`
- Format: csv
- Contract: CSV with columns: temperature_K, pressure_GPa, volume_bohr3, bulk_modulus_GPa, debye_temp_K, alpha_1e5_perK, cv_J_molK, cp_J_molK, entropy_J_molK, internal_energy_kJ_mol.
- Scoring: scored by hidden verifier

### Step 5: Extract final scored target quantities
- Role: scored (load-bearing)
- Action: From the computed E-V data and the dielectric and thermal CSV files, extract the following quantities: (1) equilibrium lattice constants a, b, c from the Murnaghan fit; (2) the three principal peaks of epsilon2 (their values and corresponding energies for xx, yy, zz polarizations); (3) the plasma frequency (energy of the maximum in the loss function derived from the dielectric data); (4) the high-temperature limiting value of Cv (Dulong-Petit limit) and the Debye temperature at 300 K and 0 GPa. Write a JSON file with these values.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON with keys: lattice_params (object with a,b,c in Å), epsilon2_peaks (object with xx_peak_val, xx_peak_energy, yy_peak_val, yy_peak_energy, zz_peak_val, zz_peak_energy), plasma_frequency (eV), cv_dulong_petit (J/mol·K), debye_temperature_0GPa_300K (K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_e_v_data.csv`
- `/app/outputs/step_02_dielectric_function.csv`
- `/app/outputs/step_03_thermal_properties.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_e_v_data.csv
- path: `/app/outputs/step_01_e_v_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DFT energy-volume data used as input for equation-of-state fit and thermodynamic model.
- schema:
  - `type`: table
  - `required_columns`: `volume`, `energy`
  - `units`:
    - `volume`: bohr^3
    - `energy`: Ry

### step_02_dielectric_function.csv
- path: `/app/outputs/step_02_dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Imaginary dielectric function components used to derive optical constants and locate characteristic peaks.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `eps2_xx`, `eps2_yy`, `eps2_zz`
  - `units`:
    - `energy_eV`: eV

### step_03_thermal_properties.csv
- path: `/app/outputs/step_03_thermal_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Complete thermodynamic table covering temperature range 0-5000 K at pressures 0, 20, 50 GPa.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pressure_GPa`, `volume_bohr3`, `bulk_modulus_GPa`, `debye_temp_K`, `alpha_1e5_perK`, `cv_J_molK`, `cp_J_molK`, `entropy_J_molK`, `internal_energy_kJ_mol`
  - `units`:
    - `temperature_K`: K
    - `pressure_GPa`: GPa
    - `volume_bohr3`: bohr^3
    - `bulk_modulus_GPa`: GPa
    - `debye_temp_K`: K
    - `alpha_1e5_perK`: 10^5/K
    - `cv_J_molK`: J/mol·K
    - `cp_J_molK`: J/mol·K
    - `entropy_J_molK`: J/mol·K
    - `internal_energy_kJ_mol`: kJ/mol

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated key reproduction targets: lattice constants, epsilon2 peaks, plasma frequency, heat capacity asymptote and Debye temperature.
- schema:
  - `type`: object
  - `required`: `lattice_params`, `epsilon2_peaks`, `plasma_frequency`, `cv_dulong_petit`, `debye_temperature_0GPa_300K`
  - `properties`:
    - `lattice_params`:
      - `type`: object
      - `units`:
        - `a`: Å
        - `b`: Å
        - `c`: Å
    - `epsilon2_peaks`:
      - `type`: object
      - `properties`:
        - `xx_peak_val`:
          - `type`: number
        - `xx_peak_energy`:
          - `type`: number
          - `units`: eV
        - `yy_peak_val`:
          - `type`: number
        - `yy_peak_energy`:
          - `type`: number
          - `units`: eV
        - `zz_peak_val`:
          - `type`: number
        - `zz_peak_energy`:
          - `type`: number
          - `units`: eV
    - `plasma_frequency`:
      - `type`: number
      - `units`: eV
    - `cv_dulong_petit`:
      - `type`: number
      - `units`: J/mol·K
    - `debye_temperature_0GPa_300K`:
      - `type`: number
      - `units`: K

Notes: The hidden checker recomputes metric from raw data (step_01, step_02, step_03) and compares the agent's reported final quantities (results.json) to hidden reference values, using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_e_v_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume",
          "energy"
        ],
        "units": {
          "volume": "bohr^3",
          "energy": "Ry"
        }
      },
      "description": "DFT energy-volume data used as input for equation-of-state fit and thermodynamic model."
    },
    {
      "file": "step_02_dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "eps2_xx",
          "eps2_yy",
          "eps2_zz"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Imaginary dielectric function components used to derive optical constants and locate characteristic peaks."
    },
    {
      "file": "step_03_thermal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pressure_GPa",
          "volume_bohr3",
          "bulk_modulus_GPa",
          "debye_temp_K",
          "alpha_1e5_perK",
          "cv_J_molK",
          "cp_J_molK",
          "entropy_J_molK",
          "internal_energy_kJ_mol"
        ],
        "units": {
          "temperature_K": "K",
          "pressure_GPa": "GPa",
          "volume_bohr3": "bohr^3",
          "bulk_modulus_GPa": "GPa",
          "debye_temp_K": "K",
          "alpha_1e5_perK": "10^5/K",
          "cv_J_molK": "J/mol·K",
          "cp_J_molK": "J/mol·K",
          "entropy_J_molK": "J/mol·K",
          "internal_energy_kJ_mol": "kJ/mol"
        }
      },
      "description": "Complete thermodynamic table covering temperature range 0-5000 K at pressures 0, 20, 50 GPa."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "lattice_params",
          "epsilon2_peaks",
          "plasma_frequency",
          "cv_dulong_petit",
          "debye_temperature_0GPa_300K"
        ],
        "properties": {
          "lattice_params": {
            "type": "object",
            "units": {
              "a": "Å",
              "b": "Å",
              "c": "Å"
            }
          },
          "epsilon2_peaks": {
            "type": "object",
            "properties": {
              "xx_peak_val": {
                "type": "number"
              },
              "xx_peak_energy": {
                "type": "number",
                "units": "eV"
              },
              "yy_peak_val": {
                "type": "number"
              },
              "yy_peak_energy": {
                "type": "number",
                "units": "eV"
              },
              "zz_peak_val": {
                "type": "number"
              },
              "zz_peak_energy": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "plasma_frequency": {
            "type": "number",
            "units": "eV"
          },
          "cv_dulong_petit": {
            "type": "number",
            "units": "J/mol·K"
          },
          "debye_temperature_0GPa_300K": {
            "type": "number",
            "units": "K"
          }
        }
      },
      "description": "Aggregated key reproduction targets: lattice constants, epsilon2 peaks, plasma frequency, heat capacity asymptote and Debye temperature."
    }
  ],
  "notes": "The hidden checker recomputes metric from raw data (step_01, step_02, step_03) and compares the agent's reported final quantities (results.json) to hidden reference values, using appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow artifact. For the raw data files (E‑V, dielectric function, thermal properties), the verifier recomputes the key quantities (e.g., locates ε₂ peaks, checks the Cv asymptote, verifies monotonic trends) and compares them to the expected behavior. For the final results JSON, the verifier compares your extracted values (lattice constants, peak positions/values, plasma frequency, heat capacity limit, Debye temperature) to hidden reference values with appropriate tolerances that account for the systematic shift caused by using an open‑source DFT code instead of the original WIEN2k implementation. The final reward is a weighted combination of the scores from each scored stage; the load‑bearing results.json stage carries the largest weight. Providing the paper's published numbers without executing the computational workflow will not yield a high score, because the verifier recomputes metrics from raw intermediate files and checks internal consistency.
