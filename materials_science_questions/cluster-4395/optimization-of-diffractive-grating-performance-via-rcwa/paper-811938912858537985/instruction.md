# Monochromatic Radial Binary Grating Incoupling Efficiency Simulation

## Problem background
Diffractive incouplers using surface‑relief gratings are crucial for coupling light into thin light guides for mobile displays and backlights. A radial binary grating coupler, consisting of concentric rings with locally constant periods, can efficiently couple monochromatic light into a guide. The incoupling efficiency depends on the local grating period and incidence angle and is modeled rigorously with the Fourier modal method (FMM/RCWA). This task requires computing the first‑order and total incoupling efficiencies for eight incidence angles using FMM/RCWA simulations.

## Approach
Model each concentric ring as a one‑dimensional binary grating with a fixed fill‑factor f=0.5, groove depth h=380 nm, wavelength λ=575 nm, and guide refractive index n=1.5. For each incidence angle (0°, 10°, …, 70°) use the corresponding local grating period d_l (0.50, 0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 1.00 µm). Implement an FMM/RCWA solver (or use an open‑source implementation) to compute the diffraction efficiency for TE and TM polarizations and average the two to obtain the efficiency for unpolarized illumination. The first‑order efficiency η_l is the fraction of incident power coupled into the +1 (or −1) diffraction order that satisfies the total internal reflection condition inside the guide; the total incoupling efficiency η is the sum of efficiencies of all orders that propagate inside the guide. Run the simulation independently for each angle‑period pair and collect the results.

## Reproduction target
Write the computed efficiencies to `/app/outputs/monochromatic_radial_efficiencies.csv`, a CSV file with the columns `incidence_angle_deg`, `period_um`, `eta_l_percent`, and `eta_percent`. The file must contain exactly eight rows, one for each of the eight incidence angles (0°, 10°, 20°, 30°, 40°, 50°, 60°, 70°), with the period values listed above, and the efficiencies in percent. The values must be derived from the FMM/RCWA simulations; no external lookup or hard‑coded numbers are allowed.

## Assets

- Open-source FMM/RCWA simulation software (e.g., S4, pyRCWA): https://github.com/vlsi-lab/S4

## Workflow steps

### Step 1: Compute monochromatic radial grating incoupling efficiencies
- Role: scored (load-bearing)
- Action: Implement an FMM/RCWA simulation of a radial binary grating incoupler consisting of concentric rings with fixed fill-factor f=0.5, groove depth h=380 nm, wavelength λ=575 nm, and guide refractive index n=1.5. For each incidence angle (0°, 10°, 20°, 30°, 40°, 50°, 60°, 70°) use the corresponding local grating period d_l: 0.50, 0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 1.00 μm. For every angle/period pair, compute the first‑order efficiency η_l (efficiency of the +1 or −1 order that satisfies the total internal reflection condition inside the guide) and the total incoupling efficiency η (sum of efficiencies of all orders that propagate inside the guide), both as the average of TE and TM polarizations. Write the eight rows to the CSV output.
- Output file: `/app/outputs/monochromatic_radial_efficiencies.csv`
- Format: csv
- Contract: Columns: incidence_angle_deg (integer), period_um (float, μm), eta_l_percent (float, percent), eta_percent (float, percent). 8 rows, one per incidence angle.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monochromatic_radial_efficiencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monochromatic_radial_efficiencies.csv
- path: `/app/outputs/monochromatic_radial_efficiencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: First‑order and total incoupling efficiencies for a radial binary grating at eight incidence angles, computed via FMM/RCWA simulation.
- schema:
  - `type`: table
  - `required_columns`: `incidence_angle_deg`, `period_um`, `eta_l_percent`, `eta_percent`
  - `units`:
    - `incidence_angle_deg`: degrees
    - `period_um`: micrometers
    - `eta_l_percent`: percent
    - `eta_percent`: percent

Notes: The hidden checker compares the submitted eta_l_percent and eta_percent values to the paper’s reported reference efficiencies, accepting an absolute tolerance to account for numerical differences between simulation implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monochromatic_radial_efficiencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "incidence_angle_deg",
          "period_um",
          "eta_l_percent",
          "eta_percent"
        ],
        "units": {
          "incidence_angle_deg": "degrees",
          "period_um": "micrometers",
          "eta_l_percent": "percent",
          "eta_percent": "percent"
        }
      },
      "description": "First‑order and total incoupling efficiencies for a radial binary grating at eight incidence angles, computed via FMM/RCWA simulation."
    }
  ],
  "notes": "The hidden checker compares the submitted eta_l_percent and eta_percent values to the paper’s reported reference efficiencies, accepting an absolute tolerance to account for numerical differences between simulation implementations."
}
```

## How you are scored
A hidden verifier reads your CSV file and compares each of the 16 numerical entries (8 rows × 2 efficiency columns) against a set of independently determined reference values. Your reward is the fraction of entries that fall within an allowed tolerance (the tolerance accounts for legitimate numerical differences between simulation implementations). Reporting the correct numbers by any means other than running the simulation will not be sufficient; the verifier does not re‑run the simulation but directly checks your reported results. Only the contents of `/app/outputs/monochromatic_radial_efficiencies.csv` are scored.
