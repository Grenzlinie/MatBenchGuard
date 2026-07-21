# Porosity-Dependent Elastic Property Modeling via Equivalent Poly-Inclusion Homogenization

## Problem background
Mechanical stiffness is a critical design parameter for biocomposites used in bone tissue engineering. The effective elastic properties (Young's modulus and shear modulus) of a multi-phase composite depend on the mechanical properties of each phase, their volume concentrations, and the shape of pores and reinforcing particles. A mathematical homogenization model can predict these effective moduli from the constituent properties. In this task you will implement the equivalent poly-inclusion (EPI) homogenization method and compute the effective Young's modulus \(E\) and shear modulus \(G\) for a poly(propylene fumarate) (PPF) matrix containing ellipsoidal pores and ellipsoidal silicon particles. The predictions will be evaluated against hidden reference values for a range of configurations.

## Approach
The EPI homogenization method treats the composite as a matrix with embedded ellipsoidal inclusions. For a bi-phasic composite, the effective stiffness tensor \(\mathbf{C}\) is computed from the matrix stiffness, inclusion stiffness, inclusion volume fraction, and the Eshelby tensor for the given ellipsoid shape, followed by orientational averaging to account for uniform random orientation. For a three-phase composite (porous matrix with particles), the method is applied twice: first the pores are treated as zero‑stiffness inclusions to obtain the effective properties of the porous matrix, then the reinforcing particles are added to this porous matrix.

The inputs are:
- Matrix material: PPF with Young's modulus \(E = 2.0\) GPa, shear modulus \(G = 0.77\) GPa.
- Inclusion material (stiff particles): silicon with \(E = 164\) GPa, \(G = 67\) GPa.
- Inclusion shape: ellipsoidal defined by semi‑principal axes \(a_1, a_2, a_3\) with \(a_3=1\) and aspect ratios \(k_1 = a_1/a_3\), \(k_2 = a_2/a_3\). The derived shape‑anisotropy parameter \(A\) is computed as \(A = (1+k_1+k_2)(1+1/k_1+1/k_2)/3 - 3\).
- Volume fractions: porosity \(\alpha_p\) (pores) and particle concentration \(\alpha_s\) (silicon particles).

You will implement the bi‑phasic EPI equations: compute the Eshelby tensor for an ellipsoidal inclusion, the strain concentrator, and the effective stiffness tensor via orientational averaging over all possible orientations (uniform distribution). For three‑phase composites, first compute the effective stiffness tensor of the porous matrix (pores with zero stiffness) then add the stiff particles as a second inclusion step. From the final effective stiffness tensor (which will be isotropic for uniform random orientation) extract the isotropic Young's modulus \(E\) and shear modulus \(G\).

## Reproduction target
Produce a CSV file `epi_predictions.csv` containing the computed \(E\) (GPa) and \(G\) (GPa) for a set of configurations that systematically explore the effects of porosity, particle concentration, and particle shape. The required configurations are detailed in the workflow step below. The CSV must include the columns: `case_id`, `porosity_alpha_p`, `particle_alpha_s`, `k1`, `k2`, `A`, `E_GPa`, `G_GPa`. The predictions will be compared to hidden reference values and checked for structural trends: \(E\) must decrease monotonically with increasing porosity, increase monotonically with increasing particle concentration, and be higher for highly oblate particles (\(k_1,k_2 \gg 1\)) than for spherical particles at the same volume fractions, among other consistency checks.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute EPI elastic moduli for all configurations
- Role: scored (load-bearing)
- Action: Implement the equivalent poly-inclusion (EPI) homogenization model using the given material properties (PPF: Young's modulus E=2.0 GPa, shear modulus G=0.77 GPa; silicon: E=164 GPa, G=67 GPa). For each prescribed configuration (porosity α_p, particle concentration α_s, ellipsoid aspect ratios k1 and k2), compute the effective stiffness tensor via the EPI bi-phasic equations with uniform random orientation and the Eshelby tensor for ellipsoidal shape, then extract isotropic Young's modulus E and shear modulus G. Generate predictions for the following sweeps: (a) porous PPF with spherical pores (k1=k2=1) at porosities 0.1,0.2,...,0.7; (b) dense PPF with spherical silicon particles at concentrations 0.00,0.05,0.10,0.15,0.20; (c) three-phase composites with spherical pores (α_p=0.6) and spherical particles (α_s=0.00,0.05,0.10,0.15,0.20); (d) three-phase composites with spherical pores (α_p=0.6) and highly oblate silicon particles (k1=k2=1000) at α_s=0.10; (e) additional shape-anisotropy sweeps to allow checking of E_P/E_S and E_O/E_S trends. Write all results to epi_predictions.csv.
- Output file: `/app/outputs/epi_predictions.csv`
- Format: csv
- Contract: CSV file with header: case_id, porosity_alpha_p, particle_alpha_s, k1, k2, A, E_GPa, G_GPa. Each row corresponds to one configuration. E and G in GPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/epi_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### epi_predictions.csv
- path: `/app/outputs/epi_predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Effective elastic moduli predictions for the specified configurations.
- schema:
  - `type`: table
  - `required_columns`: `case_id`, `porosity_alpha_p`, `particle_alpha_s`, `k1`, `k2`, `A`, `E_GPa`, `G_GPa`
  - `units`:
    - `E_GPa`: GPa
    - `G_GPa`: GPa

Notes: Structural checks include monotonic decrease of E with porosity, monotonic increase with particle concentration, higher E for oblate particles than spherical, and linear fit coefficients for the spherical three-phase case matching within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "epi_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "case_id",
          "porosity_alpha_p",
          "particle_alpha_s",
          "k1",
          "k2",
          "A",
          "E_GPa",
          "G_GPa"
        ],
        "units": {
          "E_GPa": "GPa",
          "G_GPa": "GPa"
        }
      },
      "description": "Effective elastic moduli predictions for the specified configurations."
    }
  ],
  "notes": "Structural checks include monotonic decrease of E with porosity, monotonic increase with particle concentration, higher E for oblate particles than spherical, and linear fit coefficients for the spherical three-phase case matching within tolerance."
}
```

## How you are scored
A hidden verifier independently examines your submitted `epi_predictions.csv`. Scoring is divided into several weighted components:
- **Quantitative accuracy:** the computed \(E\) and \(G\) values are compared to hidden gold reference values using a tolerance that accounts for reasonable numerical differences. Meeting or exceeding the reference (directional metric: lower absolute error is better) earns full credit; credit degrades as error increases.
- **Structural consistency:** the verifier checks that the moduli satisfy expected monotonic trends with respect to porosity and particle concentration, and that differences between spherical and non‑spherical particles are in the expected direction (e.g., oblate particles yield higher \(E\) than spherical particles at equal volume fractions).

The weighted sum of these components gives your final reward (range 0–1). The specific gold values, tolerances, and exact check weights are hidden; you only need to implement the EPI model faithfully and compute predictions for the configurations described in the workflow step.
