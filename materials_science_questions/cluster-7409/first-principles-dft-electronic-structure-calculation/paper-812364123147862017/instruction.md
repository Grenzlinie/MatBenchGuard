# First-principles FP-LAPW electronic structure and optical properties of cubic SrTiO₃

## Problem background
Strontium titanate (SrTiO₃) is a prototypical perovskite with applications in ferroelectrics, optoelectronics and microelectronics. First-principles electronic-structure calculations are essential to understanding its optical response. Density functional theory (DFT) with a scissor correction can predict band gaps and dielectric functions, but reliable reproduction of these properties across different implementations validates the theoretical description. This task reproduces the computed electronic band structure and optical constants of cubic SrTiO₃ from a full-potential linearized augmented plane-wave (FP-LAPW) calculation.

## Approach
The core method is an all-electron FP-LAPW calculation within DFT, treating exchange and correlation with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation. A scissor operator rigidly shifts the conduction bands to correct the GGA underestimation of the band gap; the shift magnitude is obtained from experiment. Optical spectra are derived within the independent-particle approximation by evaluating interband transition matrix elements and using the Kramers–Kronig relations. The workflow proceeds from a self-consistent ground-state calculation to band-gap extraction, then to the computation of the dielectric function's imaginary part, its real part via Kramers–Kronig transformation, and the energy-loss spectrum. Finally, characteristic peak positions and selected optical constants are extracted. The open-source Elk code is used as the FP-LAPW implementation.

## Reproduction target
Compute the electronic structure and optical properties of cubic SrTiO₃ (space group Pm3̅m) using an FP-LAPW DFT calculation with GGA-PBE and a scissor correction. From the computed data, report:

- The indirect band gap (R→Γ) and the direct band gap at Γ, both before and after applying the scissor correction.
- The energies of the nine labelled peaks (A through I) in ε₂(ω) in the energy range 0–30 eV.
- The static real dielectric constant ε₁(ω=0).
- The energy of the plasma peak in the energy-loss spectrum L(ω) = –Im(1/ε(ω)).

## Assets

- Elk FP-LAPW code: http://elk.sourceforge.net/

## Workflow steps

### Step 1: Self-consistent FP-LAPW DFT calculation
- Role: process
- Action: Set up the cubic SrTiO₃ crystal structure (space group Pm3̅m, Sr at origin, Ti at body centre, O at face centres). Perform a self‑consistent FP‑LAPW calculation using the Elk code with GGA‑PBE exchange‑correlation, full relativistic treatment, muffin‑tin radii Sr=2.0 a.u., Ti=1.8 a.u., O=1.5 a.u., Rmt×Kmax=0.7, lmax=14, and a 12×12×12 k‑point mesh. Converge the charge density to obtain ground‑state eigenvalues and wavefunctions.
- Evidence: `/app/outputs/scf_energy.dat`

### Step 2: Extract band gaps
- Role: scored
- Action: From the SCF eigenvalues, identify the indirect band gap (R→Γ) and direct band gap at Γ. Compute both without and with a conduction‑band rigid shift (scissor) of 1.33 eV. Write the four values to /app/outputs/band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: Columns: gap_type (indirect_no_scissor, direct_no_scissor, indirect_with_scissor, direct_with_scissor), energy_eV (float). One row per gap type.
- Scoring: scored by hidden verifier

### Step 3: Optical properties calculation
- Role: process
- Action: Using the scissor‑corrected eigenvalues and wavefunctions from the SCF run, compute the imaginary part ε₂(ω) of the dielectric function via the interband expression (independent‑particle approximation). Then obtain the real part ε₁(ω) via the Kramers‑Kronig relation. Also compute the energy‑loss spectrum L(ω)=Im(−1/ε(ω)).
- Evidence: `/app/outputs/epsilon_spectrum.dat`

### Step 4: Identify ε₂ peaks
- Role: scored
- Action: From the computed ε₂(ω) spectrum, locate the major peaks labelled A through I in the energy range 0–30 eV. Record the peak energies in /app/outputs/epsilon2_peaks.csv.
- Output file: `/app/outputs/epsilon2_peaks.csv`
- Format: csv
- Contract: Columns: peak_label (A, B, C, D, E, F, G, H, I), energy_eV (float). Nine rows, one per peak.
- Scoring: scored by hidden verifier

### Step 5: Extract static dielectric constant and plasma peak
- Role: scored (load-bearing)
- Action: From the computed spectra, extract ε₁(ω=0) (the real part of the dielectric function at zero frequency) and the energy of the maximum in the energy‑loss spectrum L(ω). Write them to /app/outputs/optical_constants.json.
- Output file: `/app/outputs/optical_constants.json`
- Format: json
- Contract: JSON object with keys: epsilon1_at_0 (float), plasma_peak_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/epsilon2_peaks.csv`
- `/app/outputs/optical_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Direct and indirect band gaps (raw GGA and after 1.33 eV scissor correction).
- schema:
  - `required_columns`: `gap_type`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### epsilon2_peaks.csv
- path: `/app/outputs/epsilon2_peaks.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Positions of the nine major peaks (A–I) in ε₂(ω) between 0 and 30 eV.
- schema:
  - `required_columns`: `peak_label`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### optical_constants.json
- path: `/app/outputs/optical_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static dielectric constant ε₁(0) and energy of the plasma peak in L(ω).
- schema:
  - `type`: object
  - `required`:
    - `epsilon1_at_0`: float
    - `plasma_peak_energy_eV`: float
  - `units`:
    - `epsilon1_at_0`: dimensionless
    - `plasma_peak_energy_eV`: eV

Notes: All quantities are fixed physical properties obtained from a first‑principles DFT workflow; the checker compares each value to the paper‑reported reference within hidden tolerances (result‑level compare, T0). No metrics are “better” than the reference, so exact_match is the appropriate target policy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "gap_type",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Direct and indirect band gaps (raw GGA and after 1.33 eV scissor correction)."
    },
    {
      "file": "epsilon2_peaks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "peak_label",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Positions of the nine major peaks (A–I) in ε₂(ω) between 0 and 30 eV."
    },
    {
      "file": "optical_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon1_at_0": "float",
          "plasma_peak_energy_eV": "float"
        },
        "units": {
          "epsilon1_at_0": "dimensionless",
          "plasma_peak_energy_eV": "eV"
        }
      },
      "description": "Static dielectric constant ε₁(0) and energy of the plasma peak in L(ω)."
    }
  ],
  "notes": "All quantities are fixed physical properties obtained from a first‑principles DFT workflow; the checker compares each value to the paper‑reported reference within hidden tolerances (result‑level compare, T0). No metrics are “better” than the reference, so exact_match is the appropriate target policy."
}
```

## How you are scored
A hidden verifier independently checks each of your three scored output files. It compares the values you report against independently determined references with appropriate tolerances and combines the checks into an overall reward. Each scored step carries a weight that contributes to the final score. Reporting the paper's numbers without executing the described workflow is not sufficient; the verifier expects your output to be the result of performing the required calculations.
