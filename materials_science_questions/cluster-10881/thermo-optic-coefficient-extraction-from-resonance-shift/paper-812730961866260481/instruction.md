# LPG Thermal Gradient Response Simulation with Asymmetric Effective Index

## Problem background
Long-period gratings (LPGs) can sense temperature, but a single uniform LPG subjected to a thermal gradient across its length produces a resonance depth change that depends only on the magnitude of the temperature difference, not its sign. If the effective refractive index difference Δn_eff varies spatially along the grating, the depth change can become asymmetric, potentially enabling discrimination of both the magnitude and the direction of the gradient. This task numerically explores this effect by simulating the transmitted intensity spectra of a two-section LPG and extracting the depth change of the resonance dip as a function of the temperature difference between the two halves, for several values of spatial asymmetry in Δn_eff.

## Approach
The LPG is modeled as two cascaded uniform sections, each containing an equal number of periods. Each section is characterized by its temperature-dependent period and effective refractive index difference. An asymmetry is introduced by shifting the effective index of the two sections in opposite directions by a fixed amount dn, so that half 1 has Δn_eff⁰ − dn and half 2 has Δn_eff⁰ + dn. A transfer-matrix formalism is used: for each wavelength and each combination of asymmetry dn and temperature step m, the detuning δ and coupling κ are computed for both sections, the section matrices are constructed, and the core-mode amplitude at the output is obtained. The normalized transmitted intensity in dB as a function of wavelength yields the resonance spectrum. From each spectrum the minimum intensity (dip depth) is located, and the change relative to the case of no temperature difference (m=0) is recorded as ΔIₘ. The procedure is repeated for a set of dn values covering cases with and without asymmetry.

## Reproduction target
Implement the two-section matrix model using the fixed grating parameters: nominal period Λ₀ = 250 μm, base effective refractive index difference Δn_eff⁰ = 0.0062, central wavelength λ_c = 1550 nm, bandwidth Δλ₀ = 39.6 nm, N₁ = N₂ = 100 periods per section, thermal coefficients σ_Λ' = 0.01 μm and σ_Δn' = 1×10⁻⁶ riu/°C (with δT = 1°C per temperature step). For each asymmetry value dn in the set {0, ±1×10⁻⁶, ±3×10⁻⁶} riu and for each integer temperature step m from −10 to +10, compute the transmitted intensity spectrum over a fine wavelength grid spanning the resonance, extract the depth change ΔIₘ, and write a CSV file `simulation_results.csv` with columns: dn (float, riu), m (int), DeltaI_m (float, dB). The output must contain exactly one row for every (dn, m) combination.

## Assets

- Python with NumPy/SciPy/Matplotlib: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Parameter setup and thermal expansion
- Role: process
- Action: Define the fixed grating parameters (Λ₀, Δn_eff⁰, λ_c, Δλ₀, N₁=N₂=100, thermal sensitivities) and the asymmetry values dn in {0, ±1×10⁻⁶, ±3×10⁻⁶} riu. For each temperature step m from −10 to +10 (δT=1°C), compute the temperature-dependent period and effective index difference for both halves using linear thermal expansion, with half 1 having Δn_eff⁰ − dn and half 2 having Δn_eff⁰ + dn. Save the generated parameter arrays.
- Evidence: `/app/outputs/thermal_params.npz`

### Step 2: Compute detuning, coupling, and transfer-matrix elements
- Role: process
- Action: For each (dn, m) combination and for wavelengths spanning the resonance, compute the detuning δ and coupling κ using the temperature-dependent effective index difference and period. Then compute the section matrix parameters (δβ, C, S, Δ, K) for both halves. Store these computed arrays.
- Evidence: `/app/outputs/matrix_elements.npz`

### Step 3: Simulate transmitted intensity spectra
- Role: process
- Action: For each combination of dn and m, evaluate the normalized transmitted intensity I(λ) in dB using the matrix model over the wavelength grid. Save the full spectrum data.
- Evidence: `/app/outputs/spectra.npz`

### Step 4: Extract resonance depth changes and build results table
- Role: scored (load-bearing)
- Action: From each simulated spectrum, locate the resonance minimum intensity Iₘ. Compute the depth change ΔIₘ for each m as the difference from the m=0 case (ΔIₘ(m) = Iₘ(m) − Iₘ(0)) for that dn. Write a CSV with columns dn (float, riu), m (int), and DeltaI_m (float, dB).
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with header: dn,m,DeltaI_m. dn: float (riu), m: int, DeltaI_m: float (dB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Depth change ΔI_m vs temperature step m for various effective index asymmetry values dn. The checker compares to hidden gold curves derived from the paper's Figs. 2 and 6, verifying symmetry for dn=0 and proportional offset for dn≠0 with tolerance ±0.5 dB.
- schema:
  - `type`: table
  - `required_columns`: `dn`, `m`, `DeltaI_m`
  - `units`:
    - `DeltaI_m`: dB

Notes: The task reproduces the numerical simulation of the LPG matrix model; no experimental data required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dn",
          "m",
          "DeltaI_m"
        ],
        "units": {
          "DeltaI_m": "dB"
        }
      },
      "description": "Depth change ΔI_m vs temperature step m for various effective index asymmetry values dn. The checker compares to hidden gold curves derived from the paper's Figs. 2 and 6, verifying symmetry for dn=0 and proportional offset for dn≠0 with tolerance ±0.5 dB."
    }
  ],
  "notes": "The task reproduces the numerical simulation of the LPG matrix model; no experimental data required."
}
```

## How you are scored
Your solution will be evaluated by an automated verifier. It will read your `simulation_results.csv` and compare the DeltaI_m values for each (dn, m) combination against hidden reference values derived from the theoretical model. It will also check the structural behavior of the response curves: for the case with no asymmetry (dn=0) it expects a specific symmetry, and for the nonzero dn cases it expects the curves to shift in a manner consistent with the sign and magnitude of dn. The final reward is a float between 0 and 1 that reflects how accurately your computed depth changes reproduce the expected numerical outcomes and qualitative behavior.
