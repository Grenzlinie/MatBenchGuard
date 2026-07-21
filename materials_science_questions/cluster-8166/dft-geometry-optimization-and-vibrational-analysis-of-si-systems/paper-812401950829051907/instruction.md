# Keating Bending Energy Minimization for Si-Centered Tetrahedra at Si/a-SiN:H Interface

## Problem background
Bond-angle distortions and hydrogenation at the Si / a-SiN:H interface play a central role in the electronic and physico-chemical properties of this technologically important heterojunction. In the classical Keating model of elastic deformation, the energy cost of bond-angle bending can be expressed in terms of local tetrahedral distortions. For Si-centered tetrahedra, the angular deformation potential V^θ depends on the site composition (SiSi4, SiNSi3, SiHSi3, SiHNSi₂, SiH₂Si₂, etc.) and on the mean Si-Si-Si bond angle. This task evaluates the Keating bending energy for the relevant tetrahedral configurations and determines the bond angles that minimize the deformation energy, providing insight into the relative stability of hydrogenated and unhydrogenated sites at the interface.

## Approach
Use the Keating bending-only formula V^θ = (3/16) Σ_k β_K r_ij r_ik (cosθ_{jik} − cosθ°_{jik})² with cosθ° = −1/3, neglecting bond-stretching terms because angular distortions dominate. Reduce the number of independent angular variables by applying an average cylindrical symmetry to each tetrahedral site, leading to specific geometric relations for ABBB, AABB, and ABCC site types. For Si AABB sites, implement both limiting interplane orientations (perpendicular and parallel). For hydrogen-terminated bonds, apply the first-order H-relaxation constraint β_K Δθ_HSiA = −β_K Δθ_HSiB. Use the Keating parameters from the literature (the central-atom Si row of the table: α_K and β_K for neighbor pairs Si–Si, Si–N, Si–H, N–N, N–H, H–H as appropriate). Sweep the mean Si‑Si‑Si bond angle from 90° to 130° in 1° steps for all required tetrahedral site types. For each site, compute V^θ separately for Si–Si bonds, Si–N bonds, and an average bond where applicable, then write the complete angle–energy curves to a CSV file. From those curves, determine the angle that minimizes V^θ for each site type and bond, and record the results in a JSON summary.

## Reproduction target
Compute the Keating angular deformation potential V^θ as a function of the mean Si-Si-Si bond angle for the following Si-centered tetrahedral site types: SiSi4, SiNSi3, SiHSi3, SiHNSi₂, SiH₂Si₂, SiH₂N₂, SiH₂NSi, and any other variants described in the framework. For each site type and each bond category (Si-Si, Si-N, average), produce the full V^θ curve from 90° to 130° in 1° steps and save it as a CSV. From these curves, extract the bond angle that minimizes V^θ for each (site_type, bond) combination and write those minimum-energy angles to a JSON file. The target is the pair of output files (V_theta_curves.csv and minima.json) that faithfully result from the Keating bending model with the specified symmetry and relaxation constraints.

## Assets

- Python 3 runtime
- NumPy: numpy
- pandas: pandas

## Workflow steps

### Step 1: Compute V^θ curves
- Role: scored (load-bearing)
- Action: Implement the Keating bending-only formula V^θ = (3/16) Σ_k β_K r_ij r_ik (cosθ_{jik} - cosθ°_{jik})² with cosθ° = -1/3, using the cylindrical symmetry geometric relations for ABBB, AABB, ABCC site types, the two interplane orientation limits, the first-order H-relaxation constraint, and the Keating parameters from the literature (Table 1 of the paper). Sweep the mean Si-Si-Si bond angle from 90° to 130° in 1° steps for all required tetrahedral site types (including SiSi4, SiNSi3, SiHSi3, SiHNSi₂, SiH₂Si₂, SiH₂N₂, SiH₂NSi, etc.). For each bond type (Si-Si, Si-N, or average) at each site, compute V^θ and write all angle–energy pairs to V_theta_curves.csv.
- Output file: `/app/outputs/V_theta_curves.csv`
- Format: csv
- Contract: columns: site_type (string), mean_angle_deg (float), V_theta (float), bond (string, one of 'Si-Si','Si-N','average')
- Scoring: scored by hidden verifier

### Step 2: Extract minimum angles
- Role: scored
- Action: From the computed V^θ curves in V_theta_curves.csv, for each site_type determine the minimum V^θ across all bonds and record the corresponding mean_angle_deg. Write the results to minima.json as a mapping from site_type (string) to min_angle_deg (float).
- Output file: `/app/outputs/minima.json`
- Format: json
- Contract: JSON object with keys: site_type (string), values: min_angle_deg (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/V_theta_curves.csv`
- `/app/outputs/minima.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### V_theta_curves.csv
- path: `/app/outputs/V_theta_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV of computed V^θ values for each site type, bond, and angle.
- schema:
  - `type`: table
  - `required_columns`: `site_type`, `mean_angle_deg`, `V_theta`, `bond`
  - `units`:
    - `mean_angle_deg`: degree

### minima.json
- path: `/app/outputs/minima.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON summary of minimum-energy angles for each site type.
- schema:
  - `type`: object
  - `description`: Object mapping site_type (string) to the minimum angle in degrees (float) that minimizes V^θ.

Notes: The checker will recompute the minimum angles from the CSV and compare against the paper-reported values; the JSON is also cross-checked for consistency with the CSV-derived minima.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "V_theta_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "site_type",
          "mean_angle_deg",
          "V_theta",
          "bond"
        ],
        "units": {
          "mean_angle_deg": "degree"
        }
      },
      "description": "CSV of computed V^θ values for each site type, bond, and angle."
    },
    {
      "file": "minima.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "description": "Object mapping site_type (string) to the minimum angle in degrees (float) that minimizes V^θ."
      },
      "description": "JSON summary of minimum-energy angles for each site type."
    }
  ],
  "notes": "The checker will recompute the minimum angles from the CSV and compare against the paper-reported values; the JSON is also cross-checked for consistency with the CSV-derived minima."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the output artifacts and independently recomputes key quantities. For the V^θ curves, the verifier checks that the computed energies follow the expected Keating model (shape, smoothness, and relative ordering between sites). From the CSV, it re-derives the minimum-energy angles and compares them to hidden reference values. The JSON minima are also cross-checked for consistency with the CSV-derived minima. Each workflow stage carries a weight, and the final reward is a combined score between 0.0 and 1.0. Reporting the correct numbers is not enough—the verifier inspects the full curves to ensure the model was implemented faithfully.
