# Nonparabolic Electron-LO-Confined-Phonon Scattering Rates in GaAs-AlGaAs Quantum Wells

## Problem background
Electron–longitudinal-optical (LO) phonon scattering is a key process governing carrier cooling, transport, and capture in semiconductor quantum wells. In narrow GaAs-AlGaAs wells, the subband energy dispersion deviates from a simple parabolic band, and this nonparabolicity can modify the electron–phonon interaction. This task investigates how much subband nonparabolicity changes the scattering rates for both intrasubband and intersubband transitions, and for what well widths and barrier heights the effect is important.

## Approach
Implement the nonparabolic electronic structure using the Nag–Mukhopadhyay energy dispersion, which gives the electron kinetic energy as a function of in-plane and perpendicular wavevectors with effective mass and a nonparabolicity parameter γ. Solve the finite-barrier quantum well problem to obtain the confined subband energies, wavevector components, envelope wavefunctions, and the occupation probabilities in the well and barrier layers.

Use the corrected slab model for confined LO phonon modes to compute the electron–phonon overlap integrals G_n and the phonon coefficients a_n, b_n.

Compute the electron–LO-confined-phonon scattering rate from Fermi's golden rule. The nonparabolic rate formula includes a term depending on γ that modifies the density of states and wavevector. The parabolic limit is obtained by setting γ=0 and evaluating the limit, which reduces to the standard parabolic scattering rate. In both cases, the kinematic condition is that the electron is at the threshold for emitting one LO phonon: for intrasubband transitions, the initial electron is at the bottom of the subband; for intersubband transitions, the final electron is at the bottom of the destination subband. The average scattering rate for each transition is the weighted sum of the rates in the well and barrier layers, with weights given by the occupation probabilities.

Material parameters:
- GaAs: effective mass m* = 0.0665 m0, static dielectric constant ε0 = 12.35, high-frequency dielectric constant ε∞ = 10.48, LO phonon energy ℏω_LO = 36.8 meV, nonparabolicity parameter γ = 4.9×10^{-19} m².
- For Al_xGa_{1-x}As, the conduction band offset relative to GaAs is V0 (eV) ≈ 0.748 x. The effective mass is m*(x) = (0.0665 + 0.0835 x) m0. The nonparabolicity parameter is γ(x) = 4.9×10^{-19} − 7.43×10^{-19} x m². (At x=0.3, this gives m*=0.0901 m0 and γ=2.67×10^{-19} m², consistent with the GaAs-Al0.3Ga0.7As well.) The dielectric constants can be taken as composition-weighted averages between GaAs and AlAs (ε0_AlAs = 10.06, ε∞_AlAs = 8.16) or use published interpolation formulas; the differences are minor.

## Reproduction target
You must compute the nonparabolic scattering rate W_np and the parabolic scattering rate W_p for the following transitions: intrasubband 1→1, 2→2, 3→3 and intersubband 2→1, 3→1, under two sweeps:
1. As a function of well width L (in Å): L = 20, 50, 100, 200, 300 at fixed Al concentration x = 0.3.
2. As a function of Al concentration x: x = 0.1, 0.2, 0.3, 0.4, 0.5 at fixed well width L = 100 Å.
For each (L,x) combination, compute the five transitions, yielding the three columns W_np, W_p, and the ratio W_np / W_p. Save all results in a single CSV file /app/outputs/scattering_rates.csv with exactly these columns: L, x, transition, W_np, W_p, ratio. Ensure the units are s^{-1} for rates, dimensionless for ratio, L in Å, x dimensionless.

## Assets
This task does not require any external datasets, models, or pre-trained weights. The only asset is a standard Python environment with the scientific computing libraries NumPy, SciPy, and optionally matplotlib for any plots. You must write the numerical routines yourself. All necessary material parameters and model descriptions are provided in the approach section.

## Workflow steps

### Step 1: Nonparabolic electronic structure calculation
- Role: process
- Action: Solve the Nag–Mukhopadhyay model (energy dispersion with nonparabolicity) for a given quantum well width L and Al concentration x, using the material parameters provided in the paper, to obtain subband energies, z-wavevectors k_z, envelope functions, and well/barrier occupation probabilities p_W, p_B. Run this for all required (L, x) combinations.
- Evidence: none

### Step 2: Confined phonon mode calculation
- Role: process
- Action: For each well width L, compute confined LO-phonon coefficients a_n, b_n and electron–phonon overlap integrals G_n using the corrected slab model and the electronic envelope functions from Step 1.
- Evidence: none

### Step 3: Scattering rate evaluation and table generation
- Role: scored (load-bearing)
- Action: For each transition (1→1, 2→2, 3→3, 2→1, 3→1) and for the two sweeps (well width L at fixed x=0.3; Al concentration x at fixed L=100 Å), compute the nonparabolic scattering rate W_np using the derived nonparabolic formula, the parabolic rate W_p using the parabolic limit formula, and their ratio W_np/W_p. Use the kinematic assumptions (electron at threshold for phonon emission) as described in the paper. Use the electronic structure and phonon data from the previous steps. Output the results as a single CSV file.
- Output file: `/app/outputs/scattering_rates.csv`
- Format: csv
- Contract: CSV with columns: L (float, in Å), x (float, Al mole fraction), transition (string, e.g., '1→1'), W_np (float, s^{-1}), W_p (float, s^{-1}), ratio (float). Must contain rows for at least L=20,50,100,200,300 Å at x=0.3, and x=0.1,0.2,0.3,0.4,0.5 at L=100 Å for all five transitions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scattering_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scattering_rates.csv
- path: `/app/outputs/scattering_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of scattering rates for intrasubband (1→1, 2→2, 3→3) and intersubband (2→1, 3→1) transitions as a function of well width (L) and Al concentration (x). Must include data for L=20,50,100,200,300 Å at x=0.3, and for x=0.1,0.2,0.3,0.4,0.5 at L=100 Å, for all five transitions.
- schema:
  - `type`: table
  - `required_columns`: `L`, `x`, `transition`, `W_np`, `W_p`, `ratio`
  - `units`:
    - `L`: Å
    - `x`: dimensionless
    - `transition`: string
    - `W_np`: s^{-1}
    - `W_p`: s^{-1}
    - `ratio`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scattering_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "x",
          "transition",
          "W_np",
          "W_p",
          "ratio"
        ],
        "units": {
          "L": "Å",
          "x": "dimensionless",
          "transition": "string",
          "W_np": "s^{-1}",
          "W_p": "s^{-1}",
          "ratio": "dimensionless"
        }
      },
      "description": "CSV table of scattering rates for intrasubband (1→1, 2→2, 3→3) and intersubband (2→1, 3→1) transitions as a function of well width (L) and Al concentration (x). Must include data for L=20,50,100,200,300 Å at x=0.3, and for x=0.1,0.2,0.3,0.4,0.5 at L=100 Å, for all five transitions."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your scattering_rates.csv and compares your computed values of W_np, W_p, and the ratio to a set of reference values. The score is the fraction of data points (rows) for which all three quantities satisfy an acceptance criterion. The verifier does not reveal the reference values or tolerances; simply ensure your calculations are faithful to the physics and parameters described.
