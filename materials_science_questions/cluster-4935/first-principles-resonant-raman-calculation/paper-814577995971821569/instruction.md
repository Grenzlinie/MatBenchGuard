# First-Principles LDA Calculation of Fermi-Surface Mass Fluctuations and Collision-Limited Raman Efficiencies for YBa2Cu3O7

## Problem background
In cuprate high-temperature superconductors, the normal-state electronic Raman scattering continuum is nearly frequency-independent and strongly depends on the polarization of the incident and scattered light. One proposed explanation attributes this continuum to mass-density fluctuations on the Fermi surface, which can be computed from first-principles local density approximation (LDA) band structure. This task will compute the Fermi-surface mass fluctuations and the resulting collision-limited Raman scattering efficiencies for orthorhombic YBa₂Cu₃O₇ (Y-123), providing quantitative predictions that can be compared against experiment.

## Approach
The core idea is to compute the Kohn-Sham band energies of orthorhombic YBa₂Cu₃O₇ using an LDA-DFT code, then extract the inverse mass tensor (second k-derivatives of the band energies) by numerical differentiation. Fermi-surface averages of these inverse mass tensors yield bare, screened, and unscreened mass-fluctuation quantities for five in-plane polarization geometries (yy, x+y,x+y, xx, x+y,x−y, xy). Applying the collision-limited Raman formula with an energy-dependent scattering rate Γ = 0.5 ω and the Fermi-level density of states gives the absolute Raman scattering efficiencies; these are also normalized to the yy channel. Additionally, the mass fluctuations are decomposed into contributions from the four individual Fermi-surface sheets (chain, antibonding plane, bonding plane, apical oxygen), each weighted by its partial density of states. The resulting numbers for the five polarizations form the target data products.

## Reproduction target
Perform a full-potential or pseudopotential LDA DFT calculation for orthorhombic YBa₂Cu₃O₇ using the publicly available crystal structure. From the resulting Kohn–Sham band structure on a sufficiently dense k‑mesh, compute Fermi‑surface mass fluctuations and the corresponding collision‑limited Raman scattering efficiencies for the in‑plane polarization geometries: yy, x+y,x+y, xx, x+y,x−y, and xy. Report two tables as CSV files:

1. `table_II_efficiencies.csv` – absolute (bare, screened, unscreened) and normalized unscreened efficiencies, with the normalization such that the yy unscreened efficiency equals 1.
2. `table_III_mass_fluctuations.csv` – per‑sheet decomposition of the bare and screened mass fluctuations, multiplied by the appropriate partial density‑of‑states factors.

The values must be obtained from the DFT calculation and post‑processing described in the workflow steps, without relying on pre‑computed tables or fitted parameters.

## Assets

- YBa2Cu3O7-δ crystal structure (orthorhombic, space group Pmmm): https://materialsproject.org/materials/mp-12660
- Open-source DFT code (e.g., Quantum ESPRESSO, Elk, WIEN2k): https://www.quantum-espresso.org
- Python numerical libraries (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: DFT band structure calculation
- Role: process
- Action: Perform a full-potential/pseudopotential LDA DFT calculation for YBa2Cu3O7-δ using the public crystal structure. Compute Kohn-Sham band energies ε(k) on a dense k-mesh (at least 845 irreducible points) for all bands crossing the Fermi level. Save the band energies and k-point coordinates for subsequent processing.
- Evidence: `/app/outputs/bands.npy`

### Step 2: Compute inverse mass tensors and Fermi-surface averages
- Role: process
- Action: From the band energies obtained in step 1, compute the inverse mass tensor components (second derivatives ∂²ε/∂kᵢ∂kⱼ) via numerical differentiation. Perform Fermi-surface integration (linear tetrahedron method) to obtain the bare, screened, and unscreened mass-fluctuation averages for the polarizations yy, x+y,x+y, xx, x+y,x-y, xy, as well as the per-sheet decomposition (chain, antibonding plane, bonding plane, apical oxygen). The Fermi-surface averages must incorporate the partial density-of-states weighting. Store these intermediate results for the scored steps.
- Evidence: `/app/outputs/mass_fluctuations_intermediate.json`

### Step 3: Collision-limited Raman efficiencies (Table II)
- Role: scored (load-bearing)
- Action: Take the unscreened mass-fluctuation averages from step 2, together with the Fermi-level density of states N(ε_F) (extracted from the DFT DOS) and the fundamental constants. Apply the collision-limited Raman formula (Γ=0.5ω) to compute absolute Raman scattering efficiencies (bare, screened, unscreened) for the five polarization configurations. Normalize the efficiencies such that the yy value equals 1, and report both absolute and normalized values in the required CSV format.
- Output file: `/app/outputs/table_II_efficiencies.csv`
- Format: csv
- Contract: CSV columns: polarization (string), bare (float), screened (float), unscreened (float), unscreened_normalized (float). Row order: yy, x+y,x+y, xx, x+y,x-y, xy. Units: unscreened and bare/screened are in 10⁻⁸ cm⁻¹ sr⁻¹ cm. unscreened_normalized is dimensionless, with yy = 1.
- Scoring: scored by hidden verifier

### Step 4: Per-sheet mass fluctuations (Table III)
- Role: scored
- Action: From the intermediate mass-fluctuation data computed in step 2, extract the bare and screened mass-fluctuation contributions for each Fermi-surface sheet (chain, antibonding plane, bonding plane, apical oxygen) and the total, for each of the five polarizations. Multiply the raw values by the appropriate partial density-of-states factor (chain 0.16, antibonding plane 0.41, bonding plane 0.17, apical oxygen 0.26) as described in the paper. Report them in the required CSV format.
- Output file: `/app/outputs/table_III_mass_fluctuations.csv`
- Format: csv
- Contract: CSV columns: polarization (string), sheet (string), bare (float), screened (float). Polarization values: yy, x+y,x+y, xx, x+y,x-y, xy. Sheet values: chain, antibonding_plane, bonding_plane, apical_oxygen, total. Mass fluctuations in units of (1/m_e)² multiplied by the respective DOS fraction.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_II_efficiencies.csv`
- `/app/outputs/table_III_mass_fluctuations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_II_efficiencies.csv
- path: `/app/outputs/table_II_efficiencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Collision-limited electronic Raman scattering efficiencies computed from LDA mass fluctuations, to be compared with paper-reported values (Table II).
- schema:
  - `type`: table
  - `columns`:
    - `name`: polarization
    - `type`: string
    - `description`: Polarization geometry label (yy, x+y,x+y, xx, x+y,x-y, xy)
    - `name`: bare
    - `type`: number
    - `unit`: 10^-8 cm^{-1} sr^{-1} cm
    - `description`: Bare mass fluctuation contribution to Raman efficiency
    - `name`: screened
    - `type`: number
    - `unit`: 10^-8 cm^{-1} sr^{-1} cm
    - `description`: Screened mass fluctuation contribution to Raman efficiency
    - `name`: unscreened
    - `type`: number
    - `unit`: 10^-8 cm^{-1} sr^{-1} cm
    - `description`: Unscreened Raman efficiency (bare minus screened)
    - `name`: unscreened_normalized
    - `type`: number
    - `unit`: dimensionless
    - `description`: Unscreened efficiency normalized to yy = 1
  - `row_order`: Fixed: yy, x+y,x+y, xx, x+y,x-y, xy

### table_III_mass_fluctuations.csv
- path: `/app/outputs/table_III_mass_fluctuations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-sheet decomposition of Fermi-surface mass fluctuations in units of (1/m_e)^2 times the partial density-of-states fraction, to be compared with paper-reported values (Table III).
- schema:
  - `type`: table
  - `columns`:
    - `name`: polarization
    - `type`: string
    - `description`: Polarization geometry label (yy, x+y,x+y, xx, x+y,x-y, xy)
    - `name`: sheet
    - `type`: string
    - `description`: Fermi surface sheet (chain, antibonding_plane, bonding_plane, apical_oxygen, total)
    - `name`: bare
    - `type`: number
    - `unit`: (1/m_e)^2 * DOS_fraction
    - `description`: Bare mass fluctuation for this sheet and polarization, multiplied by the partial DOS factor
    - `name`: screened
    - `type`: number
    - `unit`: (1/m_e)^2 * DOS_fraction
    - `description`: Screened mass fluctuation for this sheet and polarization, multiplied by the partial DOS factor
  - `row_order`: All combinations of polarization (5) and sheet (5) in any order; must cover all 25 rows.

Notes: The agent must run the full DFT pipeline to produce these values. The hidden reference values are the paper's calculated numbers. The checker uses tolerance-based comparison (reference_match). The normalized efficiency for yy is defined as 1; the absolute efficiencies may differ due to DFT implementation details but the trends should be consistent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_II_efficiencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "polarization",
            "type": "string",
            "description": "Polarization geometry label (yy, x+y,x+y, xx, x+y,x-y, xy)"
          },
          {
            "name": "bare",
            "type": "number",
            "unit": "10^-8 cm^{-1} sr^{-1} cm",
            "description": "Bare mass fluctuation contribution to Raman efficiency"
          },
          {
            "name": "screened",
            "type": "number",
            "unit": "10^-8 cm^{-1} sr^{-1} cm",
            "description": "Screened mass fluctuation contribution to Raman efficiency"
          },
          {
            "name": "unscreened",
            "type": "number",
            "unit": "10^-8 cm^{-1} sr^{-1} cm",
            "description": "Unscreened Raman efficiency (bare minus screened)"
          },
          {
            "name": "unscreened_normalized",
            "type": "number",
            "unit": "dimensionless",
            "description": "Unscreened efficiency normalized to yy = 1"
          }
        ],
        "row_order": "Fixed: yy, x+y,x+y, xx, x+y,x-y, xy"
      },
      "description": "Collision-limited electronic Raman scattering efficiencies computed from LDA mass fluctuations, to be compared with paper-reported values (Table II)."
    },
    {
      "file": "table_III_mass_fluctuations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "polarization",
            "type": "string",
            "description": "Polarization geometry label (yy, x+y,x+y, xx, x+y,x-y, xy)"
          },
          {
            "name": "sheet",
            "type": "string",
            "description": "Fermi surface sheet (chain, antibonding_plane, bonding_plane, apical_oxygen, total)"
          },
          {
            "name": "bare",
            "type": "number",
            "unit": "(1/m_e)^2 * DOS_fraction",
            "description": "Bare mass fluctuation for this sheet and polarization, multiplied by the partial DOS factor"
          },
          {
            "name": "screened",
            "type": "number",
            "unit": "(1/m_e)^2 * DOS_fraction",
            "description": "Screened mass fluctuation for this sheet and polarization, multiplied by the partial DOS factor"
          }
        ],
        "row_order": "All combinations of polarization (5) and sheet (5) in any order; must cover all 25 rows."
      },
      "description": "Per-sheet decomposition of Fermi-surface mass fluctuations in units of (1/m_e)^2 times the partial density-of-states fraction, to be compared with paper-reported values (Table III)."
    }
  ],
  "notes": "The agent must run the full DFT pipeline to produce these values. The hidden reference values are the paper's calculated numbers. The checker uses tolerance-based comparison (reference_match). The normalized efficiency for yy is defined as 1; the absolute efficiencies may differ due to DFT implementation details but the trends should be consistent."
}
```

## How you are scored
A hidden verifier checks both CSV files. For `table_II_efficiencies.csv`, it compares your normalized unscreened efficiencies against reference values derived from the same theoretical model, and also checks the absolute unscreened efficiencies. For `table_III_mass_fluctuations.csv`, it compares the bare and screened values for each polarization and sheet against the corresponding reference. The evaluation uses a tolerance‑based comparison: if your values fall within acceptable thresholds (or surpass the reference in the direction of improvement where applicable), you earn full credit; greater deviations lead to a proportionally lower reward. The two files contribute roughly equal weight to the final score. A valid output format is required but does not contribute to the numeric reward. The verifier does not reveal the reference numbers or the tolerances.
