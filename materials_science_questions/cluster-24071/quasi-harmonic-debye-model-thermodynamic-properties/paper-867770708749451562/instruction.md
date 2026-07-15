# Anharmonic MgSiO₃ Pv–PPv phase boundary and thermodynamic properties via phonon quasiparticle method

## Problem background
MgSiO₃ perovskite (Pv) transforms to post-perovskite (PPv) under Earth's lower mantle conditions. Predicting the phase boundary and its Clapeyron slope requires accurate free energies that include lattice anharmonicity. The phonon quasiparticle (PHQ) approach uses ab initio molecular dynamics to obtain temperature-dependent renormalised phonon frequencies, from which anharmonic Helmholtz free energies, key thermodynamic properties, and the Pv→PPv transition pressure can be computed. This task aims to compute such anharmonic thermodynamic quantities and the phase boundary for pure MgSiO₃ using one exchange‑correlation functional.

## Approach
The workflow begins with the crystal structures of MgSiO₃ perovskite (Pbnm) and post‑perovskite (Cmcm). Static DFT and harmonic phonon calculations provide reference static energies, harmonic phonon frequencies, and polarisation vectors. Ab initio molecular dynamics (AIMD) simulations on sufficiently large supercells at a set of volumes and temperatures generate atomic velocity trajectories. For each mode compatible with the supercell, the mode‑projected velocity autocorrelation function (VAF) is computed using the harmonic polarisation vectors. Each VAF is fit to an exponentially decaying cosine to extract a renormalised (temperature‑dependent) phonon frequency. The renormalised frequencies are then Fourier interpolated onto a dense q‑mesh to approach the thermodynamic limit. Using the phonon gas model, the vibrational entropy and Helmholtz free energy are obtained at each volume and temperature. Fitting the free‑energy–volume relation gives the thermal equation of state, from which anharmonic thermodynamic properties (thermal expansivity, bulk modulus, heat capacity, Grüneisen parameter) are derived. Finally, the Helmholtz free energy is converted to Gibbs free energy to locate the Pv→PPv phase boundary and its Clapeyron slope. Only the PBE exchange‑correlation functional is required; comparison with the quasiharmonic approximation is not part of the scored task.

## Reproduction target
Compute the anharmonic thermodynamic properties (thermal expansivity, isothermal bulk modulus, isochoric heat capacity, and thermodynamic Grüneisen parameter) at 4000 K for both Pv and PPv at pressures of 30, 60, 90, and 120 GPa. Report the results in a CSV file with the columns: phase (string), temperature_K (always 4000), pressure_GPa (float), thermal_expansivity_1_per_K (float), isothermal_bulk_modulus_GPa (float), isochoric_heat_capacity_J_per_mol_per_K (float), thermodynamic_Gruneisen_parameter (float). Determine the Pv→PPv transition pressure (in GPa) and the Clapeyron slope dP/dT (in MPa/K) at 2500 K, and write them to a JSON file with the keys 'Pv_PPv_transition_pressure_GPa_at_2500K' and 'Clapeyron_slope_MPa_per_K_at_2500K'. All outputs must be produced by the PHQ workflow described above, using the PBE functional and the provided public crystal structures and pseudopotentials.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- MgSiO₃ perovskite crystal structure (ICSD 200511): ICSD 200511; also available from Materials Project (mp-6031)
- MgSiO₃ post-perovskite crystal structure (ICSD 155405): ICSD 155405

## Workflow steps

### Step 1: Static DFT and harmonic phonon calculations
- Role: process
- Action: Using Quantum ESPRESSO with the PBE functional, perform static DFT calculations and harmonic phonon calculations on the Pv and PPv crystal structures to obtain equilibrium geometries, static energies, harmonic phonon frequencies and polarization vectors at sufficient k-point and q-point sampling.
- Evidence: none

### Step 2: AIMD simulations
- Role: process
- Action: Run ab initio molecular dynamics (NVT ensemble) for 160-atom Pv and 180-atom PPv supercells at a set of volumes and temperatures spanning lower mantle conditions (e.g., 5 volumes, 6 temperatures between 300–5000 K) using the PBE functional and a Gamma-point k-point sampling. Generate atomic velocity trajectories.
- Evidence: none

### Step 3: PHQ analysis and Helmholtz free energy surfaces
- Role: process
- Action: For each (V,T) condition, compute mode-projected velocity autocorrelation functions using harmonic polarization vectors, fit renormalised phonon frequencies. Perform Fourier interpolation onto a dense q-mesh (to approach the thermodynamic limit), compute vibrational entropy via the phonon gas model, and integrate to obtain anharmonic Helmholtz free energy surfaces F(V,T) for both Pv and PPv.
- Evidence: none

### Step 4: Anharmonic thermodynamic properties at 4000 K
- Role: scored (load-bearing)
- Action: From the PHQ F(V,T) surfaces, derive the isothermal equation of state at 4000 K. Compute thermal expansivity (α), isothermal bulk modulus (K_T), isochoric heat capacity (C_V), and thermodynamic Grüneisen parameter (γ) at 4000 K and pressures 30, 60, 90, 120 GPa for both Pv and PPv. Write the results to thermodynamic_properties.csv.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: Columns: phase (string), temperature_K (float, always 4000), pressure_GPa (float), thermal_expansivity_1_per_K (float), isothermal_bulk_modulus_GPa (float), isochoric_heat_capacity_J_per_mol_per_K (float), thermodynamic_Gruneisen_parameter (float).
- Scoring: scored by hidden verifier

### Step 5: Pv-PPv phase boundary: transition pressure and Clapeyron slope
- Role: scored (load-bearing)
- Action: Convert the PHQ Helmholtz free energies to Gibbs free energy G = F + PV. At T = 2500 K, locate the pressure where G_Pv = G_PPv; this is the transition pressure. Compute the Clapeyron slope dP/dT at 2500 K by evaluating the transition pressure at two closely spaced temperatures. Write the results to phase_boundary_results.json.
- Output file: `/app/outputs/phase_boundary_results.json`
- Format: json
- Contract: Required keys: 'Pv_PPv_transition_pressure_GPa_at_2500K' (float), 'Clapeyron_slope_MPa_per_K_at_2500K' (float). Optional: 'Clapeyron_slope_MPa_per_K_at_1000K', 'Clapeyron_slope_MPa_per_K_at_4000K', 'transition_temperature_at_CMB_K'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_properties.csv`
- `/app/outputs/phase_boundary_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Anharmonic thermodynamic properties at 4000 K and four specified pressures for both perovskite (Pv) and post-perovskite (PPv) phases. Includes isothermal/adiabatic bulk moduli and isochoric/isobaric heat capacities.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `temperature_K`, `pressure_GPa`, `thermal_expansivity_1_per_K`, `isothermal_bulk_modulus_GPa`, `adiabatic_bulk_modulus_GPa`, `isochoric_heat_capacity_J_per_mol_per_K`, `isobaric_heat_capacity_J_per_mol_per_K`, `thermodynamic_Gruneisen_parameter`
  - `units`:
    - `temperature_K`: K
    - `pressure_GPa`: GPa
    - `thermal_expansivity_1_per_K`: 1/K
    - `isothermal_bulk_modulus_GPa`: GPa
    - `adiabatic_bulk_modulus_GPa`: GPa
    - `isochoric_heat_capacity_J_per_mol_per_K`: J/(mol·K)
    - `isobaric_heat_capacity_J_per_mol_per_K`: J/(mol·K)
    - `thermodynamic_Gruneisen_parameter`: dimensionless

### phase_boundary_results.json
- path: `/app/outputs/phase_boundary_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: PHQ-derived Pv-PPv phase boundary results: transition pressure, Clapeyron slope at 2500 K, and transition temperature at the core-mantle boundary (CMB). May also include slopes at other temperatures.
- schema:
  - `type`: object
  - `required`:
    - `Pv_PPv_transition_pressure_GPa_at_2500K`: float
    - `Clapeyron_slope_MPa_per_K_at_2500K`: float
    - `transition_temperature_at_CMB_K`: float

Notes: The task reproduces the PHQ (phonon quasiparticle) results for the PBE exchange-correlation functional only. QHA comparison, LDA results, and geophysical interpretation are excluded from the scored scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "temperature_K",
          "pressure_GPa",
          "thermal_expansivity_1_per_K",
          "isothermal_bulk_modulus_GPa",
          "adiabatic_bulk_modulus_GPa",
          "isochoric_heat_capacity_J_per_mol_per_K",
          "isobaric_heat_capacity_J_per_mol_per_K",
          "thermodynamic_Gruneisen_parameter"
        ],
        "units": {
          "temperature_K": "K",
          "pressure_GPa": "GPa",
          "thermal_expansivity_1_per_K": "1/K",
          "isothermal_bulk_modulus_GPa": "GPa",
          "adiabatic_bulk_modulus_GPa": "GPa",
          "isochoric_heat_capacity_J_per_mol_per_K": "J/(mol·K)",
          "isobaric_heat_capacity_J_per_mol_per_K": "J/(mol·K)",
          "thermodynamic_Gruneisen_parameter": "dimensionless"
        }
      },
      "description": "Anharmonic thermodynamic properties at 4000 K and four specified pressures for both perovskite (Pv) and post-perovskite (PPv) phases. Includes isothermal/adiabatic bulk moduli and isochoric/isobaric heat capacities."
    },
    {
      "file": "phase_boundary_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Pv_PPv_transition_pressure_GPa_at_2500K": "float",
          "Clapeyron_slope_MPa_per_K_at_2500K": "float",
          "transition_temperature_at_CMB_K": "float"
        }
      },
      "description": "PHQ-derived Pv-PPv phase boundary results: transition pressure, Clapeyron slope at 2500 K, and transition temperature at the core-mantle boundary (CMB). May also include slopes at other temperatures."
    }
  ],
  "notes": "The task reproduces the PHQ (phonon quasiparticle) results for the PBE exchange-correlation functional only. QHA comparison, LDA results, and geophysical interpretation are excluded from the scored scope."
}
```

## How you are scored
A hidden verifier will read your output artifacts (thermodynamic_properties.csv and phase_boundary_results.json) and compare your computed values to independently derived reference values from the same PHQ+PBE protocol. The comparison uses numeric tolerances that account for legitimate implementation spread. Each load‑bearing output contributes a weighted share to the final reward. Structural checks (correct columns/keys, file format, and completeness) are also evaluated but carry little weight. The verifier does not accept numbers simply restated from published sources; they must originate from your own execution of the described simulation workflow.
