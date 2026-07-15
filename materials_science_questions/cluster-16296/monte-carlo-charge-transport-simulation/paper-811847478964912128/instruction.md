# Monte Carlo Electron Mobility in Bulk Narrow Gap Semiconductors

## Problem background
Narrow band gap semiconductors such as InAs and InSb exhibit very high electron mobilities, making them promising for high-speed, low-power high electron mobility transistors. Reliable Monte Carlo (MC) simulation of electron transport in these materials requires an accurate and consistent set of material parameters. This task aims to compute the low-field electron mobility of bulk InSb, InAs, AlSb, and the alloy Al0.15In0.85Sb using a single-particle MC simulator with a three-valley spherical nonparabolic band model. The computed mobilities can then be compared with experimental reference values to assess the quality of the parameter set.

## Approach
Implement a single-particle Monte Carlo simulator for electron transport in bulk zincblende semiconductors. The conduction band is modelled by three spherical nonparabolic valleys: Gamma (Γ), L, and X. Scattering mechanisms include acoustic phonon (treated as elastic for the low-field mobility calculation), polar optical phonon, and intervalley phonon scattering (absorption and emission). Impact ionization is not required for mobility extraction, as the low-field mobility is independent of it.

The material parameters for InSb, InAs, and AlSb are listed in the table below. For the alloy Al0.15In0.85Sb, all parameters are obtained by linear interpolation between the corresponding InSb and AlSb values.

| Parameter | InSb | InAs | AlSb |
|-----------|------|------|------|
| Density (kg/m³) | 5790 | 5667 | 4260 |
| Sound velocity (m/s) | 4060 | 4282 | 4250 |
| Static dielectric constant | 15.68 | 12.25 | 10.24 |
| Optic dielectric constant | 17.65 | 15.15 | 12.04 |
| Band gap (eV) | 0.18 | 0.354 | 1.615 |
| Lattice parameter (Å) | 6.479 | 6.058 | 6.135 |
| Optical phonon energy (eV) | 24.4 × 10⁻³ | 30.0 × 10⁻³ | 36.0 × 10⁻³ |
| Effective mass (m*/m₀) – Γ | 0.014 | 0.023 | 0.14 |
| Effective mass (m*/m₀) – L | 0.220 | 0.29 | 0.70 |
| Effective mass (m*/m₀) – X | 0.130 | 0.64 | 0.53 |
| Nonparabolicity coefficient (eV⁻¹) – Γ | 5.72 | 1.39 | 5.72 |
| Nonparabolicity coefficient (eV⁻¹) – L | 5.72 | 0.54 | 5.72 |
| Nonparabolicity coefficient (eV⁻¹) – X | 5.72 | 0.90 | 5.72 |
| Valley offset from Γ (eV) – L | 0.76 | 1.1 | -0.09 |
| Valley offset from Γ (eV) – X | 0.46 | 1.6 | -0.68 |
| Acoustic deformation potential (eV) – Γ | 5.96 | 5.93 | 2.20 |
| Acoustic deformation potential (eV) – L | 5.96 | 7.23 | 2.20 |
| Acoustic deformation potential (eV) – X | 5.96 | 9.02 | 2.20 |
| Optic deformation potential (eV) – Γ | 0.0 | 0.0 | 0.0 |
| Optic deformation potential (eV) – L | 2.5 | 2.3 | 1.0 |
| Optic deformation potential (eV) – X | 0.0 | 0.0 | 0.0 |
| Intervalley deformation potential (10¹⁰ eV/m) – Γ→L | 5.0 | 5.6 | 1.0 |
| Intervalley deformation potential (10¹⁰ eV/m) – Γ→X | 5.0 | 6.3 | 1.0 |
| Intervalley deformation potential (10¹⁰ eV/m) – L→X | 10.0 | 5.6 | 1.0 |
| Intervalley phonon energy (meV) – Γ→L / Γ→X | 19.9 | 17.4 / 19.2 | 36.0 |
| Intervalley phonon energy (meV) – L→X | 19.9 | 17.4 | 36.0 |

For each material, run the MC simulation at several low electric fields (e.g., 500 V/cm to 2 kV/cm) to ensure the drift velocity is proportional to the field. Compute the low-field mobility as the slope of the drift velocity vs electric field curve. Report the mobilities for all four materials in /app/outputs/mobilities.json.

## Reproduction target
Produce the low-field electron mobility for each of the four bulk semiconductors: InAs, InSb, AlSb, and Al0.15In0.85Sb. Compute the mobilities using the single-particle Monte Carlo simulator with the material parameters listed in the approach. Output the results to `/app/outputs/mobilities.json` with the keys `InAs_mu`, `InSb_mu`, `AlSb_mu`, and `Al0.15In0.85Sb_mu`, each a number in units of cm²/V·s.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Implement MC simulator and load material parameters
- Role: process
- Action: Implement a single-particle Monte Carlo simulator for electron transport in bulk zincblende semiconductors using a three-valley (Gamma, L, X) nonparabolic spherical conduction band model. Define the material parameter dictionaries for InSb, InAs, AlSb exactly as listed in the paper (band gap, effective masses, nonparabolicity coefficients, valley offsets, deformation potentials, phonon energies, intervalley coupling strengths, density, sound velocity, dielectric constants). For Al0.15In0.85Sb, compute parameters by linear interpolation between InSb and AlSb.
- Evidence: none

### Step 2: Simulate bulk low-field electron mobility
- Role: scored (load-bearing)
- Action: For each material (InSb, InAs, AlSb, Al0.15In0.85Sb), run the single-particle MC simulation under a low electric field regime (fields small enough that the drift velocity is proportional to field). Compute the low-field mobility as the slope of drift velocity vs. electric field. Write the resulting mobilities to /app/outputs/mobilities.json with keys InAs_mu, InSb_mu, AlSb_mu, Al0.15In0.85Sb_mu in units of cm^2/V·s.
- Output file: `/app/outputs/mobilities.json`
- Format: json
- Contract: {"type":"object","properties":{"InAs_mu":{"type":"number","unit":"cm2/V·s"},"InSb_mu":{"type":"number","unit":"cm2/V·s"},"AlSb_mu":{"type":"number","unit":"cm2/V·s"},"Al0.15In0.85Sb_mu":{"type":"number","unit":"cm2/V·s"}},"required":["InAs_mu","InSb_mu","AlSb_mu","Al0.15In0.85Sb_mu"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mobilities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mobilities.json
- path: `/app/outputs/mobilities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electron low-field mobility values for four bulk semiconductors, computed from MC simulation. Checked against paper-reported reference within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `InAs_mu`: number
    - `InSb_mu`: number
    - `AlSb_mu`: number
    - `Al0.15In0.85Sb_mu`: number

Notes: Only bulk mobility reproduction is scored; heterostructure simulations are excluded as they require a non-public 2D MC simulator.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mobilities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "InAs_mu": "number",
          "InSb_mu": "number",
          "AlSb_mu": "number",
          "Al0.15In0.85Sb_mu": "number"
        }
      },
      "description": "Electron low-field mobility values for four bulk semiconductors, computed from MC simulation. Checked against paper-reported reference within tolerance."
    }
  ],
  "notes": "Only bulk mobility reproduction is scored; heterostructure simulations are excluded as they require a non-public 2D MC simulator."
}
```

## How you are scored
A hidden verifier reads your submitted `/app/outputs/mobilities.json` file, extracts the four mobility values, and compares each against a reference (gold) value reported in the literature for the same material and conditions. The comparison uses appropriate tolerances that account for implementation‑dependent spread in MC results. All four mobilities must fall within the required tolerances for the submission to receive full credit. The verifier also checks that the file is valid JSON and that the mobilities are positive and physically reasonable. The final reward is derived from this single scored artifact.
