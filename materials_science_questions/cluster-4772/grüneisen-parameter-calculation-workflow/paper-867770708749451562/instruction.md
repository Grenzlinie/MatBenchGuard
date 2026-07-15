# MgSiO3 Post-Perovskite Phase Transition Thermodynamics and Phase Boundary

## Problem background
MgSiO₃ perovskite (Pv, bridgmanite) is the most abundant mineral in the Earth’s lower mantle. Under pressure‑temperature conditions near the core‑mantle boundary it undergoes a structural phase transition to post‑perovskite (PPv). Accurate knowledge of the thermodynamic properties of both phases and the Pv→PPv transition parameters (transition pressure, Clapeyron slope) is essential for interpreting seismic discontinuities and modelling mantle dynamics. Standard quasiharmonic approaches neglect intrinsic lattice anharmonicity, which can alter properties such as thermal expansivity, Grüneisen parameter, and the curvature of the phase boundary. The phonon quasiparticle (PHQ) method captures full anharmonicity from ab‑initio molecular dynamics and yields temperature‑dependent phonon frequencies. This task computes the anharmonic thermodynamic quantities and the Pv–PPv phase boundary using the PHQ approach with two exchange‑correlation functionals (LDA and PBE).

## Approach
The PHQ approach starts from harmonic phonon reference calculations for Pv and PPv using DFT. Supercells are then used in ab‑initio molecular dynamics (AIMD) simulations at several volumes and temperatures to obtain atomic trajectories. Mode‑projected velocity autocorrelation functions (VAFs) are computed from the velocities and the harmonic polarization vectors; fitting the VAFs to a damped cosine model extracts renormalized (anharmonic) phonon frequencies. These frequencies are Fourier‑interpolated onto dense q‑point meshes to reach the thermodynamic limit. The vibrational entropy is obtained from the anharmonic dispersions and integrated to give the Helmholtz free energy F(V,T) for each phase and functional. Numerical derivatives of F(V,T) provide pressure and the desired thermodynamic properties (thermal expansivity α, Grüneisen parameter γ, isochoric heat capacity C_V). Gibbs free energies G = F + PV are constructed to locate the Pv–PPv transition pressure at each temperature, and Clapeyron slopes are obtained by finite differences. The entire workflow is executed independently for both LDA and PBE functionals to bracket any exchange‑correlation uncertainty.

## Reproduction target
Produce two scored artifacts:

1. **Anharmonic thermodynamic properties at a single condition** — Using the PHQ method, compute the thermal expansivity α, the thermodynamic Grüneisen parameter γ, and the isochoric heat capacity C_V for both Pv and PPv at T = 4000 K and P = 120 GPa. Report values separately for the LDA and PBE functionals (α in K⁻¹, γ dimensionless, C_V in J/(mol·K)).

2. **Pv–PPv phase boundary parameters** — From the Gibbs free‑energy data, determine the transition pressure between Pv and PPv at T = 2500 K for each functional (GPa). For both functionals, compute the Clapeyron slope dP/dT at 1000 K, 2500 K, and 4000 K, then average the LDA and PBE slopes at each temperature (MPa/K).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LDA pseudopotentials for Mg, Si, O: https://www.materialscloud.org/discover/sssp/table/efficiency
- PBE pseudopotentials for Mg, Si, O: https://www.materialscloud.org/discover/sssp/table/efficiency
- MgSiO3 perovskite (Pv) crystal structure: https://materialsproject.org/materials/mp-1037/
- MgSiO3 post‑perovskite (PPv) crystal structure: https://materialsproject.org/materials/mp-10060/

## Workflow steps

### Step 1: Harmonic phonon reference calculations
- Role: process
- Action: Compute harmonic phonon frequencies, eigenvectors, and static energies for MgSiO3 Pv and PPv using DFT (LDA and PBE) at multiple volumes covering the pressure range of interest.
- Evidence: none

### Step 2: Ab initio molecular dynamics (AIMD) simulations
- Role: process
- Action: Build supercells for Pv and PPv and run NVT AIMD simulations at several volumes and temperatures (covering ~1000–4000 K) using both LDA and PBE to obtain atomic trajectories (positions and velocities).
- Evidence: none

### Step 3: Mode‑projected velocity autocorrelation analysis
- Role: process
- Action: From the AIMD velocities and harmonic eigenvectors, compute the mode‑projected velocity autocorrelation function (VAF) for each supercell q‑point and extract renormalized phonon frequencies and linewidths by fitting to an exponentially damped cosine.
- Evidence: none

### Step 4: Anharmonic phonon dispersion interpolation and temperature fitting
- Role: process
- Action: Fourier‑interpolate the renormalized frequencies onto a dense q‑mesh to reach the thermodynamic limit, and fit the temperature dependence of each mode to a second‑order polynomial to obtain temperature‑dependent anharmonic phonon dispersions.
- Evidence: none

### Step 5: Helmholtz free energy computation
- Role: process
- Action: Calculate the vibrational entropy using the phonon gas model with the anharmonic dispersions and integrate to obtain the Helmholtz free energy F(V,T) for both phases and both functionals over the computed volume‑temperature grid.
- Evidence: none

### Step 6: Derivation of thermodynamic properties
- Role: process
- Action: From F(V,T), numerically compute pressure P = –(∂F/∂V)_T, thermal expansivity α, isochoric heat capacity C_V, and thermodynamic Grüneisen parameter γ as functions of V and T for each phase and functional.
- Evidence: none

### Step 7: Extract anharmonic thermodynamic properties at target condition
- Role: scored
- Action: For each phase (Pv, PPv) and each functional (LDA, PBE), evaluate thermal expansivity α, thermodynamic Grüneisen parameter γ, and isochoric heat capacity C_V at T=4000 K and P=120 GPa. Write the results as a single JSON file.
- Output file: `/app/outputs/thermo_properties.json`
- Format: json
- Contract: JSON object with numeric keys: 'Pv_alpha_LDA', 'Pv_alpha_PBE', 'PPv_alpha_LDA', 'PPv_alpha_PBE' (α in K⁻¹, e.g. ×10⁻⁶ K⁻¹); 'Pv_gamma_LDA', 'Pv_gamma_PBE', 'PPv_gamma_LDA', 'PPv_gamma_PBE' (γ dimensionless); 'Pv_CV_LDA', 'Pv_CV_PBE', 'PPv_CV_LDA', 'PPv_CV_PBE' (C_V in J/(mol·K)).
- Scoring: scored by hidden verifier

### Step 8: Determine Pv–PPv phase boundary parameters
- Role: scored (load-bearing)
- Action: Construct Gibbs free energy G = F + PV from the F(V,T) data. For T = 2500 K, find the pressure where G_Pv = G_PPv for each functional. Compute Clapeyron slopes dP/dT by finite differences over the transition pressures at 1000 K, 2500 K and 4000 K. Average the LDA and PBE values at each temperature. Output the transition pressures and average Clapeyron slopes.
- Output file: `/app/outputs/phase_boundary.json`
- Format: json
- Contract: JSON object with numeric keys: 'transition_pressure_2500K_LDA' (GPa), 'transition_pressure_2500K_PBE' (GPa), 'Clapeyron_slope_1000K' (MPa/K, average of LDA and PBE), 'Clapeyron_slope_2500K' (MPa/K, average), 'Clapeyron_slope_4000K' (MPa/K, average).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_properties.json`
- `/app/outputs/phase_boundary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_properties.json
- path: `/app/outputs/thermo_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Anharmonic thermodynamic properties (α, γ, C_V) at T=4000 K and P=120 GPa for both phases and both LDA and PBE functionals.
- schema:
  - `type`: object
  - `required`:
    - `Pv_alpha_LDA`: number (thermal expansivity, unit: K⁻¹, e.g. ×10⁻⁶ K⁻¹)
    - `Pv_alpha_PBE`: number
    - `PPv_alpha_LDA`: number
    - `PPv_alpha_PBE`: number
    - `Pv_gamma_LDA`: number (dimensionless)
    - `Pv_gamma_PBE`: number
    - `PPv_gamma_LDA`: number
    - `PPv_gamma_PBE`: number
    - `Pv_CV_LDA`: number (J/(mol·K))
    - `Pv_CV_PBE`: number
    - `PPv_CV_LDA`: number
    - `PPv_CV_PBE`: number

### phase_boundary.json
- path: `/app/outputs/phase_boundary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pv–PPv transition pressure at 2500 K and PHQ Clapeyron slopes at three temperatures.
- schema:
  - `type`: object
  - `required`:
    - `transition_pressure_2500K_LDA`: number (GPa)
    - `transition_pressure_2500K_PBE`: number (GPa)
    - `Clapeyron_slope_1000K`: number (MPa/K, average of LDA and PBE)
    - `Clapeyron_slope_2500K`: number (MPa/K, average)
    - `Clapeyron_slope_4000K`: number (MPa/K, average)

Notes: The hidden checker compares these values against the paper‑reported numbers using tolerances appropriate for DFT re‑runs (relative tolerance for thermodynamic properties, absolute tolerance for transition pressures and slopes).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Pv_alpha_LDA": "number (thermal expansivity, unit: K⁻¹, e.g. ×10⁻⁶ K⁻¹)",
          "Pv_alpha_PBE": "number",
          "PPv_alpha_LDA": "number",
          "PPv_alpha_PBE": "number",
          "Pv_gamma_LDA": "number (dimensionless)",
          "Pv_gamma_PBE": "number",
          "PPv_gamma_LDA": "number",
          "PPv_gamma_PBE": "number",
          "Pv_CV_LDA": "number (J/(mol·K))",
          "Pv_CV_PBE": "number",
          "PPv_CV_LDA": "number",
          "PPv_CV_PBE": "number"
        }
      },
      "description": "Anharmonic thermodynamic properties (α, γ, C_V) at T=4000 K and P=120 GPa for both phases and both LDA and PBE functionals."
    },
    {
      "file": "phase_boundary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "transition_pressure_2500K_LDA": "number (GPa)",
          "transition_pressure_2500K_PBE": "number (GPa)",
          "Clapeyron_slope_1000K": "number (MPa/K, average of LDA and PBE)",
          "Clapeyron_slope_2500K": "number (MPa/K, average)",
          "Clapeyron_slope_4000K": "number (MPa/K, average)"
        }
      },
      "description": "Pv–PPv transition pressure at 2500 K and PHQ Clapeyron slopes at three temperatures."
    }
  ],
  "notes": "The hidden checker compares these values against the paper‑reported numbers using tolerances appropriate for DFT re‑runs (relative tolerance for thermodynamic properties, absolute tolerance for transition pressures and slopes)."
}
```

## How you are scored
A hidden verifier reads your `thermo_properties.json` and `phase_boundary.json` files and compares the values you report against reference PHQ results obtained from the published source. Each quantity is evaluated with a domain‑appropriate tolerance that accounts for the run‑to‑run spread expected when re‑implementing DFT‑based workflows (different pseudopotentials, codes, and numerical choices). The final reward is a weighted combination of the scores for the thermodynamic properties and the phase‑boundary parameters. Simply copying numbers from a paper without executing the workflow will not produce values that pass the verifier.
