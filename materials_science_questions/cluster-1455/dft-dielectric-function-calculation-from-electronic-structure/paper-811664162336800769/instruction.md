# DFT dielectric function and band gaps under pressure for GaP, GaAs, and GaSb

## Problem background
III-V zinc-blende semiconductors such as GaP, GaAs, and GaSb are tetrahedrally coordinated materials that can undergo a structural transformation under hydrostatic pressure. Their electronic structure is pressure-dependent, and at sufficiently high compression the fundamental gap changes from direct (Γ–Γ) to indirect (lowest of Γ–X or Γ–L). Accurately characterizing the pressure coefficients of the band gaps and the critical transition pressures, as well as the corresponding changes in the optical dielectric function, provides insight into the electronic response and is relevant for optoelectronic applications.

## Approach
The workflow uses full-potential linearized augmented plane-wave (FP-LAPW) density functional theory (DFT) with the Engel–Vosko generalized gradient approximation (EV-GGA) for band-structure and optical property calculations.
First, total-energy calculations at several volumes are performed for each compound in the zinc-blende structure to fit the Murnaghan equation of state, yielding the equilibrium lattice constant, bulk modulus, and its pressure derivative. Using the fitted parameters and the pressure–volume relation, a set of compressed unit-cell volumes corresponding to a range of hydrostatic pressures is generated.
For each volume/pressure, self-consistent FP-LAPW calculations are run to obtain Kohn–Sham eigenvalues and wavefunctions. Single‑particle energies are extracted at the Γ, X, and L high-symmetry k-points, giving the direct and indirect band gaps as functions of pressure. Linear regression of the minimum gap versus pressure yields the pressure coefficient dE_g/dP, and the critical pressure at which the fundamental gap becomes indirect is determined.
The imaginary part of the dielectric function ε₂(ω) is computed from the wavefunctions and eigenvalues at ambient pressure and at the identified critical pressure, via Kramers–Kronig transformation. The first prominent peak (lowest energy, significant intensity) in the ambient-pressure ε₂ spectrum is located.

## Reproduction target
For GaP, GaAs, and GaSb, produce the following three scored outcomes from FP‑LAPW (EV‑GGA) calculations:
1. The direct gap E_g^{ΓΓ} and the indirect gaps E_g^{ΓX} and E_g^{ΓL} at ambient pressure (0 Kbar).
2. The pressure dependence of these gaps up to and beyond the direct‑to‑indirect transition. Report the linear pressure coefficient dE_g/dP of the minimum gap and the critical hydrostatic pressure at which the fundamental gap becomes indirect.
3. The energy (in eV) of the first main peak in the imaginary part of the dielectric function ε₂(ω) at ambient pressure.
All results must be written to the JSON files specified in the workflow steps. The hidden verifier will compare every reported quantity against independently stored reference values.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.io
- Atomic species data for Ga, P, As, Sb: elk
- Python scientific stack (numpy, scipy, matplotlib): numpy, scipy, matplotlib

## Workflow steps

### Step 1: Structure optimization and equation-of-state fitting
- Role: process
- Action: For each of GaP, GaAs, and GaSb in the zinc-blende structure, perform total-energy DFT-GGA calculations at several volumes around the expected equilibrium. Fit the energy-volume data to the Murnaghan equation of state to obtain the equilibrium lattice constant, bulk modulus B₀, and pressure derivative B₀′. Using the fitted parameters, generate a set of compressed unit-cell volumes corresponding to hydrostatic pressures up to the expected critical transition pressures.
- Evidence: `/app/outputs/equilibrium_params.json`

### Step 2: FP-LAPW band-structure calculations at selected pressures
- Role: process
- Action: For each compound and for every volume (equilibrium and compressed), run self-consistent FP-LAPW calculations using Engel-Vosko GGA to obtain Kohn-Sham eigenvalues and wavefunctions. Extract the single-particle energies at the Γ, X, and L high-symmetry k-points for each pressure.
- Evidence: `/app/outputs/band_energies.json`

### Step 3: Extract ambient-pressure band gaps
- Role: scored
- Action: From the band energies at the equilibrium volume (P = 0), compute the direct gap E_g^ΓΓ and the indirect gaps E_g^ΓX and E_g^ΓL for each compound. Report the three gap values in eV.
- Output file: `/app/outputs/step_01_band_gaps_ambient.json`
- Format: json
- Contract: {"GaP": {"E_g_GammaGamma": float, "E_g_GammaX": float, "E_g_GammaL": float}, "GaAs": {"E_g_GammaGamma": float, "E_g_GammaX": float, "E_g_GammaL": float}, "GaSb": {"E_g_GammaGamma": float, "E_g_GammaX": float, "E_g_GammaL": float}}
- Scoring: scored by hidden verifier

### Step 4: Pressure-dependent gaps, coefficients, and critical pressures
- Role: scored (load-bearing)
- Action: For each compound, extract the energy gaps at all computed pressures. Fit the minimum gap as a function of pressure (eV vs. Kbar) to obtain the linear pressure coefficient dE_g/dP (in meV/bar). Determine the critical hydrostatic pressure at which the fundamental gap changes from direct (Γ-Γ) to indirect (lowest of Γ-X or Γ-L). Write the full pressure series, the coefficient, and the critical pressure to a JSON file.
- Output file: `/app/outputs/step_02_pressure_dependence.json`
- Format: json
- Contract: {"GaP": {"pressures_Kbar": [float], "E_g_GammaGamma": [float], "E_g_GammaX": [float], "E_g_GammaL": [float], "dE_g_dP_meV_per_bar": float, "critical_pressure_Kbar": float}, "GaAs": {...}, "GaSb": {...}}
- Scoring: scored by hidden verifier

### Step 5: Compute imaginary dielectric function ε₂(ω)
- Role: process
- Action: Using the wavefunctions and eigenvalues from the band-structure calculations, compute the frequency-dependent imaginary part of the dielectric function ε₂(ω) for each compound at ambient pressure and at the critical pressure identified in the pressure-dependence step. Cover the energy range 0–20 eV.
- Evidence: `/app/outputs/epsilon2_spectra.json`

### Step 6: Extract first main peak of ε₂ at ambient pressure
- Role: scored
- Action: From the ambient-pressure ε₂ spectrum of each compound, locate the energy of the first prominent peak (the lowest-energy peak with significant intensity, typically below 5 eV). Report the peak energy in eV.
- Output file: `/app/outputs/step_03_dielectric_peaks.json`
- Format: json
- Contract: {"GaP": {"ambient_peak_energy_eV": float}, "GaAs": {"ambient_peak_energy_eV": float}, "GaSb": {"ambient_peak_energy_eV": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gaps_ambient.json`
- `/app/outputs/step_02_pressure_dependence.json`
- `/app/outputs/step_03_dielectric_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gaps_ambient.json
- path: `/app/outputs/step_01_band_gaps_ambient.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Principal direct and indirect band gaps at ambient pressure (0 Kbar) for GaP, GaAs, and GaSb, as recomputed by the agent. The checker compares each value to the hidden paper reference within a tolerance appropriate for FP-LAPW re-implementations.
- schema:
  - `type`: object
  - `required`:
    - `GaP`: object
    - `GaAs`: object
    - `GaSb`: object
  - `items`:
    - `E_g_GammaGamma`: float (eV)
    - `E_g_GammaX`: float (eV)
    - `E_g_GammaL`: float (eV)
  - `required_columns`:
  - `units`:
    - `E_g_GammaGamma`: eV
    - `E_g_GammaX`: eV
    - `E_g_GammaL`: eV

### step_02_pressure_dependence.json
- path: `/app/outputs/step_02_pressure_dependence.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Full pressure-dependent band gap data, the linear pressure coefficient of the minimum gap, and the critical pressure for the direct-to-indirect gap transition for each compound. The checker verifies the coefficient and critical pressure against the hidden paper reference within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `GaP`: object
    - `GaAs`: object
    - `GaSb`: object
  - `items`:
    - `pressures_Kbar`: array of float (Kbar)
    - `E_g_GammaGamma`: array of float (eV)
    - `E_g_GammaX`: array of float (eV)
    - `E_g_GammaL`: array of float (eV)
    - `dE_g_dP_meV_per_bar`: float (meV/bar)
    - `critical_pressure_Kbar`: float (Kbar)
  - `required_columns`:
  - `units`:
    - `pressures_Kbar`: Kbar
    - `E_g_GammaGamma`: eV
    - `E_g_GammaX`: eV
    - `E_g_GammaL`: eV
    - `dE_g_dP_meV_per_bar`: meV/bar
    - `critical_pressure_Kbar`: Kbar

### step_03_dielectric_peaks.json
- path: `/app/outputs/step_03_dielectric_peaks.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Energy of the first main peak in the imaginary part of the dielectric function ε₂(ω) at ambient pressure for each compound. The checker compares each value to the hidden paper reference within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `GaP`: object
    - `GaAs`: object
    - `GaSb`: object
  - `items`:
    - `ambient_peak_energy_eV`: float (eV)
  - `required_columns`:
  - `units`:
    - `ambient_peak_energy_eV`: eV

Notes: All scored values are compared against the paper's reported results (Table 2 and Figure 4) using hidden tolerances that account for code-to-code variation. Internal consistency (positive pressure coefficients) is also checked. The reward is the fraction of values within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gaps_ambient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GaP": "object",
          "GaAs": "object",
          "GaSb": "object"
        },
        "items": {
          "E_g_GammaGamma": "float (eV)",
          "E_g_GammaX": "float (eV)",
          "E_g_GammaL": "float (eV)"
        },
        "required_columns": [],
        "units": {
          "E_g_GammaGamma": "eV",
          "E_g_GammaX": "eV",
          "E_g_GammaL": "eV"
        }
      },
      "description": "Principal direct and indirect band gaps at ambient pressure (0 Kbar) for GaP, GaAs, and GaSb, as recomputed by the agent. The checker compares each value to the hidden paper reference within a tolerance appropriate for FP-LAPW re-implementations."
    },
    {
      "file": "step_02_pressure_dependence.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GaP": "object",
          "GaAs": "object",
          "GaSb": "object"
        },
        "items": {
          "pressures_Kbar": "array of float (Kbar)",
          "E_g_GammaGamma": "array of float (eV)",
          "E_g_GammaX": "array of float (eV)",
          "E_g_GammaL": "array of float (eV)",
          "dE_g_dP_meV_per_bar": "float (meV/bar)",
          "critical_pressure_Kbar": "float (Kbar)"
        },
        "required_columns": [],
        "units": {
          "pressures_Kbar": "Kbar",
          "E_g_GammaGamma": "eV",
          "E_g_GammaX": "eV",
          "E_g_GammaL": "eV",
          "dE_g_dP_meV_per_bar": "meV/bar",
          "critical_pressure_Kbar": "Kbar"
        }
      },
      "description": "Full pressure-dependent band gap data, the linear pressure coefficient of the minimum gap, and the critical pressure for the direct-to-indirect gap transition for each compound. The checker verifies the coefficient and critical pressure against the hidden paper reference within tolerance."
    },
    {
      "file": "step_03_dielectric_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GaP": "object",
          "GaAs": "object",
          "GaSb": "object"
        },
        "items": {
          "ambient_peak_energy_eV": "float (eV)"
        },
        "required_columns": [],
        "units": {
          "ambient_peak_energy_eV": "eV"
        }
      },
      "description": "Energy of the first main peak in the imaginary part of the dielectric function ε₂(ω) at ambient pressure for each compound. The checker compares each value to the hidden paper reference within tolerance."
    }
  ],
  "notes": "All scored values are compared against the paper's reported results (Table 2 and Figure 4) using hidden tolerances that account for code-to-code variation. Internal consistency (positive pressure coefficients) is also checked. The reward is the fraction of values within tolerance."
}
```

## How you are scored
Each scored workflow step produces one output file. A hidden verifier reads these files and independently compares the reported band gaps, pressure coefficient, critical pressure, and dielectric peak energies against hidden reference values. The reward is a weighted combination of the accuracies across all three steps. Internal consistency (e.g., positive pressure coefficients) is also checked. The verifier does not require the intermediate process evidence; only the final scored JSON artifacts are evaluated. Simply reporting a fixed number without performing the actual DFT+EOS pipeline will result in low accuracy when checked against the reference.
