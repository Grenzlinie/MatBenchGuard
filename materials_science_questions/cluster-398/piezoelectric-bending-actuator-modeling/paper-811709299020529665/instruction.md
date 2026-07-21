# Static Deflection Prediction of Circular Piezoelectric Unimorph Actuators

## Problem background
Circular piezoelectric unimorph actuators (CPUAs) are widely used in microactuation, transducers, and microfluidics. A CPUA consists of a piezoelectric layer bonded to a substrate layer via a thin bonding layer. Accurate prediction of the static transverse deflection of a clamped CPUA under applied DC voltage is critical for design. This task reproduces an analytical static deflection model derived from classical laminated plate theory. The model treats the bonding layer as an individual layer, which may improve prediction accuracy compared to models that neglect the bonding layer.

## Approach
The analytical model is based on classical laminated plate theory for a thin, clamped circular plate. The actuator is axisymmetric; the transverse deflection $w(r)$ is expressed in closed form as a piecewise function of radial coordinate $r$, applied DC voltage $V$, and the geometry and material properties of the layers. Two cases are considered: the "with_bonding" model, which treats the bonding layer as an individual layer, and the "without_bonding" model, where the bonding layer thickness $h_b$ is set to zero.

Use the following material and geometric parameters from the source:

**Partially covered CPUA ($R_1=10$ mm, $R_2=8$ mm):**
- Piezoelectric layer (YT-5NM): $h_p=0.2$ mm, $s_{11}^E=1.82 \times 10^{-11}$ m$^2$/N, $\nu_p=0.29$, $d_{31}=-270 \times 10^{-12}$ C/N.
- Bonding layer (epoxy): $h_b=0.025$ mm, $s_b=1.934 \times 10^{-10}$ m$^2$/N, $\nu_b=0.30$.
- Substrate layer (brass): $h_m=0.1$ mm, $s_m=1.01 \times 10^{-11}$ m$^2$/N, $\nu_m=0.34$.

**Half-covered CPUA ($R_1=10$ mm, $R_2=5$ mm):**
- Piezoelectric layer: $h_p=0.16$ mm, other properties identical.
- Bonding layer: $h_b=0.01$ mm.
- Substrate layer: $h_m=0.1$ mm, other properties identical.

Use a common Poisson's ratio $\nu = \frac{0.29+0.30+0.34}{3} \approx 0.31$ for all layers in the deflection formulas.

**Full model (with bonding layer)**
Define the following constants:

$C_5 = s_m (1+\nu) \left(1 - \frac{R_2^2}{R_1^2}\right) (h_p h_b + h_b^2)$

$C_6 = s_b (4 h_m h_b + 2 h_m^2 + h_m h_p)$

$C_7 = 4 (s_{11}^E)^2 s_b^2 h_m^4$

$C_8 = s_b^2 s_m^2 h_p^4 + s_{11}^E s_b s_m^2 (4 h_p h_b^3 + 4 h_p^3 h_b + 6 h_p^2 h_b^2) + (s_{11}^E)^2 s_m^2 h_b^4$

$C_9 = s_{11}^E s_b^2 s_m (2 h_p^3 h_m + 2 h_p h_m^3 + 6 h_p^2 h_b h_m + 6 h_p h_b^2 h_m + 6 h_p h_b h_m^2 + 3 h_p^2 h_m^2)
      + (s_{11}^E)^2 s_b s_m (8 h_b h_m^3 + 8 h_b^3 h_m + 12 h_b^2 h_m^2)$

The transverse deflection for $0 \le r \le R_2$ is

$$
\omega(r) = \frac{3(1+\nu)\, d_{31} s_{11}^E s_b s_m (C_5 + C_6) \left[ \left(1 - \frac{R_2^2}{R_1^2}\right) r^2 + 2R_2^2 \ln\!\left(\frac{R_2}{R_1}\right) \right] V}
{C_7 + (1+\nu)^2 \left(1 - \frac{R_2^2}{R_1^2}\right)^2 C_8 + 4(1+\nu) \left(1 - \frac{R_2^2}{R_1^2}\right) C_9}.
$$

For $R_2 \le r \le R_1$,

$$
\omega_o(r) = \frac{3(1+\nu)\, d_{31} s_{11}^E s_b s_m (C_5 + C_6) \left[ 2R_2^2 \ln r - \frac{R_2^2}{R_1^2} r^2 - 2R_2^2 \ln R_1 + R_2^2 \right] V}
{C_7 + (1+\nu)^2 \left(1 - \frac{R_2^2}{R_1^2}\right)^2 C_8 + 4(1+\nu) \left(1 - \frac{R_2^2}{R_1^2}\right) C_9}.
$$

**Simplified model (bonding layer neglected, $h_b=0$)**
The constants reduce to:

$C_{10} = 2 h_m^2 + 2 h_m h_p$

$C_{11} = 4 s_{11}^E h_m^4$

$C_{12} = s_m^2 h_p^4$

$C_{13} = s_{11}^E s_m (2 h_p^3 h_m + 2 h_p h_m^3 + 3 h_p^2 h_m^2)$

The deflection for $0 \le r \le R_2$ is

$$
\omega_{\text{simp}}(r) = \frac{3(1+\nu)\, d_{31} s_{11}^E s_m C_{10} \left[ \left(1 - \frac{R_2^2}{R_1^2}\right) r^2 + 2R_2^2 \ln\!\left(\frac{R_2}{R_1}\right) \right] V}
{C_{11} + (1+\nu)^2 \left(1 - \frac{R_2^2}{R_1^2}\right)^2 C_{12} + 4(1+\nu) \left(1 - \frac{R_2^2}{R_1^2}\right) C_{13}}.
$$

For $R_2 \le r \le R_1$,

$$
\omega_{o,\text{simp}}(r) = \frac{3(1+\nu)\, d_{31} s_{11}^E s_m C_{10} \left[ 2R_2^2 \ln r - \frac{R_2^2}{R_1^2} r^2 - 2R_2^2 \ln R_1 + R_2^2 \right] V}
{C_{11} + (1+\nu)^2 \left(1 - \frac{R_2^2}{R_1^2}\right)^2 C_{12} + 4(1+\nu) \left(1 - \frac{R_2^2}{R_1^2}\right) C_{13}}.
$$

Use these formulas to compute the deflection on a radial grid from $r=0$ mm to $r=10$ mm in steps of $0.1$ mm for each voltage and model variant, as detailed in the workflow steps.

## Reproduction target
Produce the predicted transverse deflection profiles for two CPUA configurations — a partially covered actuator ($R_2/R_1=0.8$) and a half‑covered actuator ($R_2/R_1=0.5$) — at four DC voltages (25, 50, 75, 100 V) using both the full model (bonding layer included) and the simplified model (bonding layer neglected). For each case, output the deflection on a fine radial grid from 0 to 10 mm (step 0.1 mm) and also extract the central deflection (at $r = 0$ mm) as a summary. The artefacts must conform to the exact file schemas described in the output contract.

## Assets

- Python with NumPy: numpy

## Workflow steps

### Step 1: Compute deflections for partially covered CPUA
- Role: scored (load-bearing)
- Action: Implement the closed-form deflection formulas for a clamped circular piezoelectric unimorph actuator. Using the material parameters for YT-5NM piezoelectric, epoxy bonding, and brass substrate (thickness and compliance constants as given in the source's Table 1), compute the transverse deflection profile on a radial grid from 0 to 10 mm with step 0.1 mm for applied DC voltages of 25, 50, 75, and 100 V. Produce results for both the model that includes the bonding layer and the simplified model that neglects the bonding layer. Write the results to step_01_deflections_partial.csv.
- Output file: `/app/outputs/step_01_deflections_partial.csv`
- Format: csv
- Contract: Columns: r (mm, float), voltage (V, int), model (string, one of 'with_bonding' or 'without_bonding'), deflection (mm, float). Radial grid: 0 to 10 mm, step 0.1 mm (101 points). 4 voltages × 2 models = 8 profiles, total 808 rows.
- Scoring: scored by hidden verifier

### Step 2: Compute deflections for half-covered CPUA
- Role: scored
- Action: Implement the same closed-form deflection formulas using the material parameters for the half-covered CPUA (YT-5NM piezoelectric, epoxy bonding, brass substrate; thickness and compliance constants as given in the source's Table 2). Compute the transverse deflection profile on the same radial grid (0–10 mm, step 0.1 mm) for DC voltages of 25, 50, 75, and 100 V, for both the model with bonding layer and the model without bonding layer. Write the results to step_02_deflections_half.csv.
- Output file: `/app/outputs/step_02_deflections_half.csv`
- Format: csv
- Contract: Same columns as step_01: r (mm, float), voltage (V, int), model (string), deflection (mm, float). 101 radial points × 4 voltages × 2 models, total 808 rows.
- Scoring: scored by hidden verifier

### Step 3: Extract central deflections
- Role: scored
- Action: From the deflection profiles computed in steps 01 and 02, extract the deflection value at radial position r=0 for each CPUA type, voltage, and model. Write the summary to step_03_central_deflections.csv.
- Output file: `/app/outputs/step_03_central_deflections.csv`
- Format: csv
- Contract: Columns: cpu_type (string, 'partial' or 'half'), voltage (V, int), model (string), central_deflection (mm, float). 2 types × 4 voltages × 2 models = 16 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_deflections_partial.csv`
- `/app/outputs/step_02_deflections_half.csv`
- `/app/outputs/step_03_central_deflections.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_deflections_partial.csv
- path: `/app/outputs/step_01_deflections_partial.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Transverse deflection profile for partially covered CPUA (R1=10 mm, R2=8 mm) on radial grid 0-10 mm, for 4 voltages and 2 model variants.
- schema:
  - `type`: table
  - `required_columns`: `r`, `voltage`, `model`, `deflection`
  - `units`:
    - `r`: mm
    - `voltage`: V
    - `model`: none
    - `deflection`: mm

### step_02_deflections_half.csv
- path: `/app/outputs/step_02_deflections_half.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Transverse deflection profile for half-covered CPUA (R1=10 mm, R2=5 mm) on radial grid 0-10 mm, for 4 voltages and 2 model variants.
- schema:
  - `type`: table
  - `required_columns`: `r`, `voltage`, `model`, `deflection`
  - `units`:
    - `r`: mm
    - `voltage`: V
    - `model`: none
    - `deflection`: mm

### step_03_central_deflections.csv
- path: `/app/outputs/step_03_central_deflections.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Central (r=0) deflection summary for both CPUA types, all voltages and models.
- schema:
  - `type`: table
  - `required_columns`: `cpu_type`, `voltage`, `model`, `central_deflection`
  - `units`:
    - `cpu_type`: none
    - `voltage`: V
    - `model`: none
    - `central_deflection`: mm

Notes: The checker recomputes the deflection values from the same closed-form formulas and compares each submitted value with an absolute tolerance. The radial grid must be exactly 0–10 mm with step 0.1 mm. The model column must use the exact strings 'with_bonding' and 'without_bonding'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_deflections_partial.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "voltage",
          "model",
          "deflection"
        ],
        "units": {
          "r": "mm",
          "voltage": "V",
          "model": "none",
          "deflection": "mm"
        }
      },
      "description": "Transverse deflection profile for partially covered CPUA (R1=10 mm, R2=8 mm) on radial grid 0-10 mm, for 4 voltages and 2 model variants."
    },
    {
      "file": "step_02_deflections_half.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "voltage",
          "model",
          "deflection"
        ],
        "units": {
          "r": "mm",
          "voltage": "V",
          "model": "none",
          "deflection": "mm"
        }
      },
      "description": "Transverse deflection profile for half-covered CPUA (R1=10 mm, R2=5 mm) on radial grid 0-10 mm, for 4 voltages and 2 model variants."
    },
    {
      "file": "step_03_central_deflections.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cpu_type",
          "voltage",
          "model",
          "central_deflection"
        ],
        "units": {
          "cpu_type": "none",
          "voltage": "V",
          "model": "none",
          "central_deflection": "mm"
        }
      },
      "description": "Central (r=0) deflection summary for both CPUA types, all voltages and models."
    }
  ],
  "notes": "The checker recomputes the deflection values from the same closed-form formulas and compares each submitted value with an absolute tolerance. The radial grid must be exactly 0–10 mm with step 0.1 mm. The model column must use the exact strings 'with_bonding' and 'without_bonding'."
}
```

## How you are scored
A hidden verifier independently implements the same analytical model and material parameters to recompute the deflection profiles. It then scores your submitted CSV files as follows:

- **Structure and format**: The verifier checks that each file has the required columns, correct data types, and the exact model labels `"with_bonding"` and `"without_bonding"`. Minor structural mismatches result in a score of zero for that file.
- **Numerical accuracy**: For every row in `step_01_deflections_partial.csv` and `step_02_deflections_half.csv`, the verifier computes the absolute difference between your reported deflection and the checker’s recomputed value. If the difference is below a strict tolerance, that row is considered correct. The score for each profile file is the fraction of rows that pass.
- **Central deflections**: The file `step_03_central_deflections.csv` is verified by recomputing the central deflection directly from the formulas and also by cross‑checking that each entry matches the $r = 0$ row in the corresponding profile file. A similar tolerance‑based correctness fraction is computed.

The final reward is a weighted average of the three file scores, with the two full‑profile files together carrying most of the weight and the central‑deflection summary receiving a smaller share. Simply writing the expected file structure or approximate values without correct computation will yield a low reward; only a faithful implementation of the formulas earns high credit.
