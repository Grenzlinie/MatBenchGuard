# Ferroelectric fracture toughness with out-of-plane electric field

## Problem background
Ferroelectric ceramics exhibit domain switching that can significantly enhance fracture toughness. Understanding how an out-of-plane electric field applied parallel to the crack front affects the steady-state toughness of these materials is critical for device reliability. This task asks you to model an electromechanically coupled ferroelectric under plane-strain, Mode I steady crack growth, and to compute the normalized fracture toughness ratio (the far-field energy release rate required for crack propagation divided by the intrinsic toughness) for a range of applied electric fields and initial poling states. The results will quantify the balance between field-driven domain reorientation and the energy dissipation that gives rise to toughening.

## Approach
A multi-axial, phenomenological constitutive model captures the history-dependent switching of ferroelectric domains. The model defines a switching surface in stress–electric-field space, with back-stress and back-electric-field potentials that enforce strain and polarization saturation. Normality rules give the increments of remanent strain and polarization. The constitutive law is integrated using a backward-Euler scheme to produce realistic hysteresis loops and butterfly loops.

For the fracture problem, a boundary-layer approach is used: far-field displacements correspond to a pure Mode I K-field (small-scale switching). The steady-state crack growth formulation relates increments of all field quantities to derivatives along the crack growth direction. An iterative finite-element solver is implemented: the mechanical equilibrium equations are solved with current remanent fields as body-force-like terms, then the constitutive model is integrated along streamlines of constant height above the crack plane to update the remanent fields, and the process is repeated until convergence. The crack-tip energy release rate is extracted from a contour I-integral. For each electrical loading case, the applied far-field energy release rate is adjusted (via a search strategy) until the tip energy release rate equals the material’s intrinsic toughness G_0; the resulting ratio G_ss/G_0 is the normalized fracture toughness. All material parameters are fully specified in the step descriptions.

## Reproduction target
Implement the constitutive model and the steady-state finite-element fracture formulation for the soft PLZT material parameters listed in Step 1 (plane-strain conditions). Then, for the following initial poling states and applied out-of-plane electric fields (expressed in units of the coercive field E0), determine the far-field energy release rate G_ss that yields a tip energy release rate equal to G_0, and compute the ratio G_ss/G_0:

- Initially unpoled: E3/E0 = 0.0, 0.2, 0.5, 0.8
- Initially positively poled (E3^p/E0 = +3): E3/E0 = −1.0, −0.5, 0.0, 0.5, 1.0
- Initially negatively poled (E3^p/E0 = −3): E3/E0 = 1.0, 0.5, 0.0, −0.5, −1.0

Write the results to `/app/outputs/toughness_ratios.csv` with exactly three columns: `poling_field` (float, in units of E0), `applied_field` (float, in units of E0), and `Gss_over_G0` (float). Each row corresponds to one (poling, applied) combination.

## Assets

- Python scientific computing environment (numpy, scipy, matplotlib, etc.): python3

## Workflow steps

### Step 1: Constitutive model implementation and verification
- Role: process
- Action: Implement the electromechanically coupled constitutive model for ferroelectric switching, including the switching surface, back-stress and back-electric-field potentials, and a backward-Euler integration routine. Verify the implementation by computing quasi-static uniaxial electric-field loading/unloading loops and stress-depolarization loops for the specified soft PLZT material parameters (sigma0=27.5 MPa, E0=0.35 MV/m, P0=0.26 C/m^2, epsilon_c=0.12%, beta=2.95, kappa=3e-8 C/(mV), E=70 GPa, nu=0.4, d33=6e-10 m/V, d31=-d33/2, m=0.01, H0_sigma=0.5*sigma0, H0_E=0.05*E0). The response should qualitatively match the expected hysteresis and butterfly loops.
- Evidence: `/app/outputs/constitutive_verification.png`

### Step 2: Steady-state crack growth simulation
- Role: process
- Action: Build a finite element model for the small-scale switching problem under plane-strain conditions with far-field Mode I K-field tractions. Implement the iterative steady-state solution procedure: solve the linear elastic finite element equations, integrate the constitutive model along streamlines of constant height above the crack plane to update remanent fields, recompute body-force-like terms, and iterate until convergence. For a given applied far-field energy release rate G_ss, compute the crack-tip energy release rate G_tip using the I-integral contour integral.
- Evidence: none

### Step 3: Toughness ratio computation and CSV output
- Role: scored (load-bearing)
- Action: For each required initial poling state (unpoled, poled with E3^p/E0 = +3 and -3) and each required applied electric field E3/E0 (unpoled: 0.0, 0.2, 0.5, 0.8; positively poled: -1.0, -0.5, 0.0, 0.5, 1.0; negatively poled with corresponding negative fields), run the steady-state simulation to find the applied energy release rate G_ss that yields G_tip = G_0 (the intrinsic toughness). For each case compute the toughness ratio G_ss/G_0. Write the results to CSV.
- Output file: `/app/outputs/toughness_ratios.csv`
- Format: csv
- Contract: poling_field (float, units E0), applied_field (float, units E0), Gss_over_G0 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/toughness_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### toughness_ratios.csv
- path: `/app/outputs/toughness_ratios.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing the normalized steady-state fracture toughness ratio for each evaluated poling and applied electric field condition. Values are compared to numeric reference values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `poling_field`, `applied_field`, `Gss_over_G0`

Notes: The toughness ratios are compared against hidden reference values derived from the paper's Fig. 4.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "toughness_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "poling_field",
          "applied_field",
          "Gss_over_G0"
        ]
      },
      "description": "CSV containing the normalized steady-state fracture toughness ratio for each evaluated poling and applied electric field condition. Values are compared to numeric reference values with tolerance."
    }
  ],
  "notes": "The toughness ratios are compared against hidden reference values derived from the paper's Fig. 4."
}
```

## How you are scored
A hidden verifier reads your CSV file and compares each row’s `Gss_over_G0` value to an independently obtained reference for the same poling and applied electric field conditions. The tolerance criteria (relative and absolute) are fixed but not disclosed to you. Your final score is the fraction of rows whose reported value falls within the tolerated range. The verifier does not require any other files; only the CSV is evaluated.
