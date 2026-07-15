# CNT-Grafted FRP Effective Elastic Moduli Prediction

## Problem background
Carbon nanotube (CNT) grafted fiber reinforced polymer (CG-FRP) composites exhibit enhanced mechanical properties compared to conventional fiber composites. Predicting their effective elastic moduli is challenging due to the multi-scale structure: CNTs are grafted radially around micrometer-sized fibers, creating a functionally graded interphase. A hierarchical two-scale micromechanical model can estimate the overall elastic response by separately homogenizing the CNT-reinforced polymer region and then the whole composite. The central question is to compute the effective tensile modulus (E11, along the fiber axis) and the effective transverse modulus (E22, perpendicular to the fibers) for several material cases and compare them with known experimental references.

## Approach
The model proceeds in two scales. At the micro-scale, the CNTs around a single fiber define a cylindrical region whose local CNT volume fraction varies radially. That region is homogenized using the Mori–Tanaka scheme with the Eshelby tensor for cylindrical inclusions in an isotropic polymer matrix, yielding a transversely isotropic effective stiffness that depends on the local CNT volume fraction. At the meso-scale, the CG-FRP is treated as a multi-coated cylindrical inclusion consisting of the fiber, a discrete set of concentric interphase layers that approximate the graded CNT region, and the surrounding polymer matrix. A sequentially homogenization technique is applied from the outer matrix inward to obtain the overall effective transversely isotropic stiffness tensor. The engineering constants E11 and E22 are then extracted from the final stiffness components. The computation is implemented in Python, relying only on standard numeric libraries (NumPy/SciPy). For the interphase, a sufficient number of layers (e.g., 10) is used to capture the gradient.

## Reproduction target
Using the hierarchical model described above, compute E11 and E22 for three validation cases:

1. Fiber volume fraction Vf = 0.3%, CNT volume fraction Vcnt = 0.08%
2. Vf = 67%, Vcnt = 20%
3. Vf = 41%, Vcnt = 2%

Constituent properties and geometry are taken from the problem statement:
- Carbon fiber (transversely isotropic): axial modulus E_FI = 15410 MPa, transverse modulus E_FT = 230000 MPa, axial Poisson ratio ν_FI = 0.46, transverse Poisson ratio ν_FT = 0.29, axial shear modulus G_FI = 10040 MPa, transverse shear modulus G_FT = 25000 MPa.
- CNT (isotropic): elastic modulus E_CN = 1,000,000 MPa, Poisson ratio ν_CN = 0.3.
- Polymer matrix (isotropic): elastic modulus E_M = 2890 MPa, Poisson ratio ν_M = 0.3.
- Fiber radius r_F = 7 µm, CNT radius r_CN = 1.357 nm, CNT length l_CN = 1.5 µm.
- CNT areal density ρ_CN = 200 for the Vcnt = 0.08% case. For the other cases, ρ_CN must be scaled proportionally (or derived from the CNT volume fraction relation) so that the stated CNT volume fractions are achieved.

Output a CSV file with exactly three rows (one per case) containing columns 'Case' (one of 'Vf0.3_Vcnt0.08', 'Vf67_Vcnt20', 'Vf41_Vcnt2'), 'E11_GPa' (float), and 'E22_GPa' (float).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Micro-scale CNRP homogenization and interphase discretization
- Role: process
- Action: Compute the local CNT volume fraction around the fiber using the radial law V_CN_LOC(r) = r_CF * rho_CN * pi * r_CN^2 / r. Homogenize the CNT-reinforced polymer (CNRP) for each radial position using the Mori-Tanaka method with the Eshelby tensor for cylindrical inclusions in an isotropic matrix. Discretize the functionally graded interphase into N-2 uniform layers of thickness t_lay = l_CN/(N-2). For each layer i, calculate its local CNT volume fraction V_i_LOC by integration, assign the homogenized transversely isotropic stiffness tensor after transforming from local to global coordinates, and compute its global volume fraction.
- Evidence: `/app/outputs/layer_stiffness_tensors.json`

### Step 2: Meso-scale sequentially homogenization and effective moduli
- Role: scored (load-bearing)
- Action: Using the layer stiffness tensors and global volume fractions from step1, apply the sequentially homogenization method to obtain the effective transversely isotropic stiffness tensor of the CG-FRP. Extract the engineering constants: effective tensile modulus E11 (E_I^eff) and effective transverse modulus E22 (E_T^eff). Perform this computation for the three validation cases (Vf=0.3% with Vcnt=0.08%, Vf=67% with Vcnt=20%, Vf=41% with Vcnt=2%). Write the results to a CSV file as specified.
- Output file: `/app/outputs/effective_moduli.csv`
- Format: csv
- Contract: Columns: 'Case' (string, values: 'Vf0.3_Vcnt0.08', 'Vf67_Vcnt20', 'Vf41_Vcnt2'), 'E11_GPa' (float), 'E22_GPa' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_moduli.csv
- path: `/app/outputs/effective_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted effective moduli for three CG-FRP validation cases. The checker compares these values to hidden reference values (paper-reported model predictions) within prescribed relative tolerances and verifies a monotonic trend of E11 with respect to fiber volume fraction.
- schema:
  - `type`: table
  - `required_columns`: `Case`, `E11_GPa`, `E22_GPa`
  - `units`:
    - `E11_GPa`: GPa
    - `E22_GPa`: GPa

Notes: The agent must choose appropriate discretization (N>=10) and derive the CNT areal density for the higher-Vcnt cases from the volume fraction relation to achieve the stated CNT volume fractions. The gold reference is the paper's own hierarchical model predictions, not experimental data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Case",
          "E11_GPa",
          "E22_GPa"
        ],
        "units": {
          "E11_GPa": "GPa",
          "E22_GPa": "GPa"
        }
      },
      "description": "Predicted effective moduli for three CG-FRP validation cases. The checker compares these values to hidden reference values (paper-reported model predictions) within prescribed relative tolerances and verifies a monotonic trend of E11 with respect to fiber volume fraction."
    }
  ],
  "notes": "The agent must choose appropriate discretization (N>=10) and derive the CNT areal density for the higher-Vcnt cases from the volume fraction relation to achieve the stated CNT volume fractions. The gold reference is the paper's own hierarchical model predictions, not experimental data."
}
```

## How you are scored
A hidden verifier reads your effective_moduli.csv. It compares each reported value (E11, E22) against hidden reference values that represent the expected hierarchical model predictions for these cases, using relative tolerances appropriate for a re-implementation with a finite number of interphase layers. Additionally, it checks that the predicted E11 increases with increasing fiber volume fraction (monotonic trend). The verifier combines these checks into a reward between 0 and 1. You do not need to know the exact reference numbers; just implement the described model faithfully.
