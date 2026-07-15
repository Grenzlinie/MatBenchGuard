# Phonon-Limited Transport in Armchair Graphene Nanoribbons

## Problem background
Armchair graphene nanoribbons (ANRs) are promising building blocks for nanoscale transistors. Their electronic band structure depends on the ribbon width, falling into three families (3j, 3j±1) when the width is measured in dimer rows. In the phonon-limited semiclassical transport regime, the conductance and field-effect mobility are expected to be sensitive to the width, temperature, and the specific electronic family. Understanding these transport trends requires a computational pipeline that combines tight-binding electronic structure, phonon spectrum calculations, and a Boltzmann transport solver.

## Approach
The approach uses an orthogonal tight-binding model with Carbon–Hydrogen interactions, previously parameterized from ab initio data, to compute the relaxed electronic band structure E(k), density of states DOS(E), Fermi velocity v_F, and band gaps for ANRs of the requested widths. The vibrational spectrum is obtained from tight-binding molecular dynamics and velocity autocorrelation, and the acoustic phonon energies up to about 750 cm⁻¹ are retained.

Transport is simulated by solving a one-dimensional, near-equilibrium Boltzmann transport equation. The electron-phonon scattering rate is calculated to first order using the computed DOS, v_F, and phonon energies, together with the in-plane acoustic deformation potential D(q)=16 eV·q and the graphene mass density ρ=7.6×10⁻⁷ kg/m². For each ribbon width and temperature, the carrier distribution is solved under a small axial field, and the conductance G versus carrier density n is obtained. The on-state conductance (evaluated at a fixed carrier density threshold related to v_F) and the peak field-effect mobility are extracted. Finally, the dependence of on-conductance on width and temperature, as well as the ordering among the three families, is analyzed.

## Reproduction target
Compute the on-state conductance G_on and peak field-effect mobility μ_peak for armchair graphene nanoribbons of widths 10, 11, and 12 dimer rows at temperatures 200 K, 300 K, and 400 K. The on-state is defined at the threshold carrier density n₀ = 2/(h v_F), where v_F is the Fermi velocity obtained from the band structure. From these data, determine:
- the slope of G_on at 300 K versus width (dimer rows),
- the temperature exponent β obtained by fitting G_on(T) ∝ T^{-β} for each width,
- the ordering of G_on among the three families (3j, 3j‑1, 3j+1).
Write the results to /app/outputs/transport_results.json following exactly the output contract specified below.

## Assets

- C-H tight-binding parameters (NRL-TB): http://cst-www.nrl.navy.mil/bind/

## Workflow steps

### Step 1: Tight-binding electronic structure calculation
- Role: process
- Action: Using the supplied C-H tight-binding parameters, compute the electronic band structure E(k), density of states DOS(E), Fermi velocity v_F, and band gaps for armchair nanoribbons of widths 10, 11, and 12 dimer rows. Save the electronic structure data for later use.
- Evidence: `/app/outputs/electronic_structure.json`

### Step 2: Phonon spectrum calculation
- Role: process
- Action: Calculate vibrational spectra for graphene/armchair nanoribbons using tight-binding molecular dynamics (or a suitable approximation) and velocity autocorrelation. Extract acoustic phonon energies up to 750 cm⁻¹, which dominate low-energy scattering. Save the phonon energy distribution.
- Evidence: `/app/outputs/phonon_spectrum.json`

### Step 3: Boltzmann transport simulation and scaling analysis
- Role: scored (load-bearing)
- Action: Implement a 1D near-equilibrium Boltzmann transport solver. Use the electronic structure (DOS, v_F) from step 1 and phonon energies from step 2. The electron-phonon scattering rate is: S = ℏ D²(q) DOS(k+q) [N_ph + 0.5 ± 0.5] / (π ρ E_ph w), with deformation potential D(q)=16 eV·q, mass density ρ=7.6×10⁻⁷ kg/m², and width w. For ribbon widths of 10, 11, and 12 dimer rows at temperatures 200 K, 300 K, and 400 K, solve for conductance G vs carrier density n under a small axial field. Extract on-state conductance (at n = 2/(h v_F)) and peak field-effect mobility. Compute the slope of on-conductance vs dimer rows at 300 K, the power-law exponent β from a fit of G_on(T) ∝ (T)^(-β), and determine the on-conductance ordering among the three families. Save the results to transport_results.json.
- Output file: `/app/outputs/transport_results.json`
- Format: json
- Contract: {"widths": [10, 11, 12], "temperatures": [200, 300, 400], "on_conductance": [[G_w10_T200, G_w10_T300, G_w10_T400], [G_w11_T200, ...], ...], "peak_mobility": [[mu_w10_T200, ...], ...], "beta": <float>, "width_slope": <float>, "family_ordering": "<string, e.g. 'family_a > family_b > family_c'>"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transport_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transport_results.json
- path: `/app/outputs/transport_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent's computed transport properties for armchair graphene nanoribbons. The structural_audit checks on_conductance ordering with width (monotonic increase), family ordering (must be a valid > separated ordering of 3j, 3j-1, 3j+1), width_slope > 0, and 0 < β < 1.
- schema:
  - `type`: object
  - `required`:
    - `widths`: array of ints (dimer rows)
    - `temperatures`: array of ints (K)
    - `on_conductance`: array of arrays of floats (μS), dimension widths × temperatures
    - `peak_mobility`: array of arrays of floats (cm²/V·s), dimension widths × temperatures
    - `beta`: float (power-law exponent, 0 < β < 1)
    - `width_slope`: float (slope of on_conductance vs width at 300 K, μS/dimer-row)
    - `family_ordering`: string describing on-conductance ordering among families, e.g. 'family_a > family_b > family_c'
  - `items`: object
  - `required_columns`:
  - `units`:
    - `on_conductance`: μS
    - `peak_mobility`: cm²/V·s
    - `temperatures`: K
    - `widths`: dimer rows

Notes: The on_conductance values are to be extracted at the threshold carrier density n = 2/(h v_F). The absolute values may differ due to implementation details; structural trends (ordering, sign of slope, beta range) are the primary check. The family ordering for widths 12 (3j), 10 (3j+1), 11 (3j-1) must be assessed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transport_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "widths": "array of ints (dimer rows)",
          "temperatures": "array of ints (K)",
          "on_conductance": "array of arrays of floats (μS), dimension widths × temperatures",
          "peak_mobility": "array of arrays of floats (cm²/V·s), dimension widths × temperatures",
          "beta": "float (power-law exponent, 0 < β < 1)",
          "width_slope": "float (slope of on_conductance vs width at 300 K, μS/dimer-row)",
          "family_ordering": "string describing on-conductance ordering among families, e.g. 'family_a > family_b > family_c'"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "on_conductance": "μS",
          "peak_mobility": "cm²/V·s",
          "temperatures": "K",
          "widths": "dimer rows"
        }
      },
      "description": "Agent's computed transport properties for armchair graphene nanoribbons. The structural_audit checks on_conductance ordering with width (monotonic increase), family ordering (must be a valid > separated ordering of 3j, 3j-1, 3j+1), width_slope > 0, and 0 < β < 1."
    }
  ],
  "notes": "The on_conductance values are to be extracted at the threshold carrier density n = 2/(h v_F). The absolute values may differ due to implementation details; structural trends (ordering, sign of slope, beta range) are the primary check. The family ordering for widths 12 (3j), 10 (3j+1), 11 (3j-1) must be assessed."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/transport_results.json and compares the reported quantities—on_conductance values, width_slope, beta, family_ordering, and peak_mobility trends—against reference criteria derived from the published study. The scoring is tolerant to implementation spread: primary weight is placed on structural consistency (monotonicity with width, sign of the width slope, beta lying in a physically expected range, and correct family ordering) rather than exact numerical match. Each scored aspect contributes a weighted portion to the final reward. Producing a syntactically valid output file is necessary but not sufficient—the verifier checks that the reported trends and values are physically plausible and consistent with the computational pipeline described in the workflow steps.
