# Keating Deformation Energy of Si-Centered Tetrahedra at Si/a-SiN:H Interfaces

## Problem background
Amorphous silicon nitride (a-SiN:H) interfaces with crystalline or amorphous silicon are technologically important, especially for electronic devices. Bond-angle distortions and hydrogenation at these interfaces influence local electronic properties. Evaluating the local elastic deformation potentials for Si-centered tetrahedra using the Keating bending formalism can help explain observed physico-chemical trends. In particular, hydrogenated Si tetrahedra can exhibit bond-angle minima that deviate from the regular tetrahedron, which may correlate with experimental findings on interface composition.

## Approach
The deformation energy of a Si-centered tetrahedron is modeled using the Keating bending-only approximation, which sums contributions from all bond angles around the central Si atom. Each bending term depends on the deviation of the bond angle cos from the ideal tetrahedral value (cosθ° = -1/3) and is scaled by a bond-dependent bending parameter β_K. To reduce the number of independent angular variables, cylindrical symmetry is assumed, leading to geometric relations for different site classes (ABBB, ABCC, AABB) with limiting interplane orientations (perpendicular and parallel). For H-terminated bonds with small distortions, a first-order relaxation constraint couples the angular changes on the two H-containing bonds.

Given a set of Keating bending parameters (Si-Si, Si-N, Si-H, N-N, N-H, H-H) and reference bond lengths of 1.0, V^θ can be computed for any Si-centered tetrahedron as a function of the mean Si-Si-Si bond angle θ. By evaluating V^θ for the configurations of interest over a range of θ, one can locate the angle that minimizes the elastic energy for each configuration. For mixed-bond configurations, the deformation energy can also be decomposed onto specific bonds (e.g., Si-N vs. Si-Si) to assess the relative stiffness.

## Reproduction target
Compute the Keating bending-only deformation energy V^θ for the following Si-centered tetrahedral configurations: Si Si₄, Si NSi₃, Si HSi₃, Si HN₃, Si HNSi₂, Si H₂N₂, Si H₂NSi, Si H₂Si₂. For each configuration, evaluate V^θ as a function of the mean Si-Si-Si bond angle θ from 90° to 120° in steps of 0.5°, applying the appropriate cylindrical symmetry reduction and, for H-terminated bonds, the first-order relaxation constraint. Write the full V^θ curves to deformation_energies.csv.

From these curves, extract two quantities:
1. The bond angle that minimizes V^θ for the Si HNSi₂ configuration (fit a quadratic near the minimum).
2. The ratio V^θ(Si-N) / V^θ(Si-Si) for the Si H₂NSi configuration in the perpendicular (+) interplane orientation at θ = 109.5°.
Write these two values to results.yaml.

## Assets
This task is self-contained and requires no external data downloads. All needed Keating parameters and geometric constraints are provided in the instructions. The computation can be implemented using standard Python numerical libraries (e.g., numpy, scipy, pyyaml). No GPU or external services are required.

## Workflow steps

### Step 1: Compute Keating deformation energies
- Role: scored (load-bearing)
- Action: Implement the Keating bending formula V^θ = (3/16) Σ_k β_K^{jik} r_ij r_ik (cosθ_jik - cosθ°)^2 with cosθ° = -1/3 and reference bond lengths set to 1.0. Use the bending parameters: β_K(Si-Si)=0.073, (Si-N)=0.19, (Si-H)=0.06, (N-N)=0.3, (N-H)=0.21, (H-H)=0.12 mdyne/Å. Apply cylindrical symmetry geometric reductions for site classes ABBB, ABCC, AABB with perpendicular (+) and parallel (=) interplane limits, and for H-terminated bonds the first-order relaxation constraint β_K^{HSiA}Δθ_HSiA = -β_K^{HSiB}Δθ_HSiB. Compute V^θ for the configurations: Si Si₄, Si NSi₃, Si HSi₃, Si HN₃, Si HNSi₂, Si H₂N₂, Si H₂NSi, Si H₂Si₂, as a function of the mean Si-Si-Si bond angle θ (90° to 120° in steps of 0.5°). Write all data to deformation_energies.csv.
- Output file: `/app/outputs/deformation_energies.csv`
- Format: csv
- Contract: Columns: configuration (string), theta (float, degrees), V_theta (float, mdyne·Å). Theta range 90-120 in 0.5° steps.
- Scoring: scored by hidden verifier

### Step 2: Extract minimum angle and ratio
- Role: scored
- Action: From the deformation_energies.csv, determine the bond angle that minimizes V^θ for the Si HNSi₂ configuration. Also compute the ratio of V^θ on the Si-N bond to V^θ on the Si-Si bond for the Si H₂NSi configuration in the perpendicular (+) interplane orientation at θ=109.5°. Write these to results.yaml.
- Output file: `/app/outputs/results.yaml`
- Format: other
- Contract: Keys: si_hns2_minimum_angle (float), si_h2nsi_perp_ratio (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deformation_energies.csv`
- `/app/outputs/results.yaml`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deformation_energies.csv
- path: `/app/outputs/deformation_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw V^θ values for each tetrahedral configuration as a function of bond angle θ.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `theta`, `V_theta`

### results.yaml
- path: `/app/outputs/results.yaml`
- format: other
- purpose: scored
- target_policy: exact_match
- description: Extracted minimizing bond angle for Si HNSi₂ and deformation-energy ratio for Si H₂NSi (perpendicular) at θ=109.5°.
- schema:
  - `type`: object
  - `required`:
    - `si_hns2_minimum_angle`: float
    - `si_h2nsi_perp_ratio`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deformation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "theta",
          "V_theta"
        ]
      },
      "description": "Raw V^θ values for each tetrahedral configuration as a function of bond angle θ."
    },
    {
      "file": "results.yaml",
      "format": "other",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "si_hns2_minimum_angle": "float",
          "si_h2nsi_perp_ratio": "float"
        }
      },
      "description": "Extracted minimizing bond angle for Si HNSi₂ and deformation-energy ratio for Si H₂NSi (perpendicular) at θ=109.5°."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier scores your outputs independently. The verifier reads your deformation_energies.csv and results.yaml. For the CSV, it validates data integrity (all required configurations and θ values present, positive energies, smooth variation) and recomputes the minimizing angle for Si HNSi₂ by fitting a quadratic to the V^θ vs. θ data you provide. For the YAML, it compares your reported ratio against a hidden reference derived from the paper's reported result. The final reward combines the accuracy of both extracted quantities with a consistency check on the raw CSV. Producing the required files in the specified format is essential; the verifier will not search for alternatives.
