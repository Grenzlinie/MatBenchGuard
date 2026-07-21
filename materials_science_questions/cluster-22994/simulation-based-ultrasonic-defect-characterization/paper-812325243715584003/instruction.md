# Boundary-element simulation of eddy-current probe impedance for surface-breaking flaws

## Problem background
Eddy‑current probes are widely used in nondestructive evaluation (NDE) to detect surface‑breaking flaws such as cracks and slots. Predicting the probe’s impedance change is challenging because the flaw response depends on both the perfect‑conductor limit and finite‑conductivity corrections that are especially important when flaw dimensions are comparable to the electromagnetic skin depth. A first‑order perturbation theory that expresses the impedance change as a sum of a zero‑order (perfect‑conductor) term and a first‑order skin‑depth correction offers a practical route to simulation. This task focuses on computing the relative magnitude of the skin‑depth correction \(|\Delta Z_1^f|\) compared with the perfect‑conductor flaw signal \(|\Delta Z_0^f|\) for rectangular slots in a conducting half‑space, as a function of flaw size and overall geometric scaling.


## Approach
The approach combines a scalar‑potential formulation for perfectly conducting half‑space flaws with a boundary‑element discretisation, together with free‑space magnetic field expressions for a circular coil. For a given flaw geometry (a rectangular slot) and coil position, the BEM yields the scalar potential on the flaw surface and the normal magnetic field on the flaw mouth. These are inserted into the zero‑order and first‑order impedance integrals (Eqs. (12) and (13) of the model). The impedance change caused solely by the flaw is obtained by subtracting the no‑flaw half‑space contribution. Scaling relations derived from the theory allow the ratio to be computed for a family of geometrically similar configurations without re‑solving the BEM: the zero‑order flaw impedance scales linearly with every dimension, whereas the first‑order correction is scale‑invariant.


## Reproduction target
Produce two CSV files:

1. **`table_I_ratios.csv`** — the ratio \(|\Delta Z_1^f| / |\Delta Z_0^f|\) for five rectangular slot geometries:  
   \(5.0 \times 2.5 \times 0.5\) mm,  
   \(2.5 \times 1.25 \times 0.25\) mm,  
   \(1.0 \times 0.5 \times 0.1\) mm,  
   \(0.5 \times 0.25 \times 0.05\) mm,  
   \(0.25 \times 0.125 \times 0.025\) mm.  
   Coil: diameter 6.4 mm, lift‑off 1.3 mm, skin depth 0.17 mm, probe centred at origin.

2. **`scale_factor_ratios.csv`** — the same ratio when all dimensions (base flaw \(5.0 \times 2.5 \times 0.5\) mm, coil diameter 6.4 mm, lift‑off 1.3 mm) are multiplied by a scale factor varying from 0.1 to 1.0 in steps of 0.1. For these scaled configurations the ratio must decrease monotonically as the scale factor increases.


## Assets

- Python scientific stack (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Implement scalar potential BEM and free-space coil fields
- Role: process
- Action: Implement the boundary element method for a rectangular slot in a perfectly conducting half-space based on the scalar potential theory described in the paper's reference (Ref. 1 of the paper). Implement the free-space scalar potential and magnetic field for a circular coil using the formulas in the paper's Appendix.
- Evidence: `/app/outputs/bem_matrix_assembly.log`

### Step 2: Impedance ratio for five flaw sizes
- Role: scored (load-bearing)
- Action: For each of the five specified rectangular slot geometries (5.0×2.5×0.5, 2.5×1.25×0.25, 1.0×0.5×0.1, 0.5×0.25×0.05, 0.25×0.125×0.025 mm), with fixed coil diameter 6.4 mm, lift-off 1.3 mm, skin depth 0.17 mm, and probe centered at the origin, solve the BEM to obtain surface fields, compute ΔZ₀ and ΔZ₁ for the flaw and for the no-flaw half-space, extract the flaw contribution, and compute the ratio |ΔZ₁^f|/|ΔZ₀^f|. Write the results to table_I_ratios.csv.
- Output file: `/app/outputs/table_I_ratios.csv`
- Format: csv
- Contract: Header: flaw_length_mm,flaw_depth_mm,flaw_width_mm,|ΔZ0|,|ΔZ1|,ratio. Each row corresponds to one flaw size in the order of decreasing size. |ΔZ0| and |ΔZ1| are magnitudes in ohms.
- Scoring: scored by hidden verifier

### Step 3: Impedance ratio vs. scale factor
- Role: scored
- Action: Using the base flaw (5.0×2.5×0.5 mm) as reference, apply the scaling relationships (ΔZ₀ scales linearly with all dimensions, ΔZ₁ is scale-invariant) to compute the ratio |ΔZ₁^f|/|ΔZ₀^f| for scale factors 0.1 to 1.0 in steps of 0.1. Write the results to scale_factor_ratios.csv.
- Output file: `/app/outputs/scale_factor_ratios.csv`
- Format: csv
- Contract: Header: scale_factor,|ΔZ0|,|ΔZ1|,ratio. Rows for scale_factors 0.1 to 1.0. The ratio should decrease monotonically.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_I_ratios.csv`
- `/app/outputs/scale_factor_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_I_ratios.csv
- path: `/app/outputs/table_I_ratios.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed ratio of first-order skin-depth correction to perfect-conductor impedance change for five rectangular slot geometries, matching Table I of the paper.
- schema:
  - `type`: table
  - `required_columns`: `flaw_length_mm`, `flaw_depth_mm`, `flaw_width_mm`, `|ΔZ0|`, `|ΔZ1|`, `ratio`
  - `units`:
    - `flaw_length_mm`: mm
    - `flaw_depth_mm`: mm
    - `flaw_width_mm`: mm
    - `|ΔZ0|`: Ohms
    - `|ΔZ1|`: Ohms
    - `ratio`: dimensionless

### scale_factor_ratios.csv
- path: `/app/outputs/scale_factor_ratios.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Impedance ratio as a function of geometric scale factor applied to the base flaw and coil, corresponding to Fig. 6 of the paper.
- schema:
  - `type`: table
  - `required_columns`: `scale_factor`, `|ΔZ0|`, `|ΔZ1|`, `ratio`
  - `units`:
    - `scale_factor`: dimensionless
    - `|ΔZ0|`: Ohms
    - `|ΔZ1|`: Ohms
    - `ratio`: dimensionless

Notes: The ratios are compared to the paper's reported values with absolute tolerance 0.02 or relative tolerance 10%, whichever is larger. The BEM mesh density is left to the agent's choice; the computed ratios should converge to values close to the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_I_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "flaw_length_mm",
          "flaw_depth_mm",
          "flaw_width_mm",
          "|ΔZ0|",
          "|ΔZ1|",
          "ratio"
        ],
        "units": {
          "flaw_length_mm": "mm",
          "flaw_depth_mm": "mm",
          "flaw_width_mm": "mm",
          "|ΔZ0|": "Ohms",
          "|ΔZ1|": "Ohms",
          "ratio": "dimensionless"
        }
      },
      "description": "Computed ratio of first-order skin-depth correction to perfect-conductor impedance change for five rectangular slot geometries, matching Table I of the paper."
    },
    {
      "file": "scale_factor_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "scale_factor",
          "|ΔZ0|",
          "|ΔZ1|",
          "ratio"
        ],
        "units": {
          "scale_factor": "dimensionless",
          "|ΔZ0|": "Ohms",
          "|ΔZ1|": "Ohms",
          "ratio": "dimensionless"
        }
      },
      "description": "Impedance ratio as a function of geometric scale factor applied to the base flaw and coil, corresponding to Fig. 6 of the paper."
    }
  ],
  "notes": "The ratios are compared to the paper's reported values with absolute tolerance 0.02 or relative tolerance 10%, whichever is larger. The BEM mesh density is left to the agent's choice; the computed ratios should converge to values close to the paper."
}
```

## How you are scored
A hidden verifier scores each workflow stage’s output artifact independently and combines the scores into a final reward. For `table_I_ratios.csv` the verifier compares the computed ratio column against reference values derived from the paper’s published measurements. For `scale_factor_ratios.csv` it verifies both the ratio values and the required monotonic decrease with increasing scale factor. Tolerances are set to accommodate legitimate numerical differences that arise from different BEM implementations and mesh resolutions, while still requiring that the computed ratios closely match the expected physical trends. Reporting only a final number without generating the intermediate artifacts will not yield the full reward.
