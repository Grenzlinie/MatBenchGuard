# Latency and material-consumption thresholds for filament-based intercellular signaling

## Problem background
Intercellular communication often relies on diffusion of signaling molecules, but recent work suggests that long, thin filament-like structures (strings, analogous to cytonemes) can mediate faster and more material-efficient signaling. This task reproduces a physicochemical model that compares string-mediated signaling to diffusive signaling in terms of latency (speed) and consumption of signaling molecules, and evaluates the mechanical ability of these strings to transport cells. The model derives analytical thresholds above which string-mediated communication is faster or uses fewer molecules than diffusion, and computes the string formation speed, the time scale for cooperative radial assembly, and the maximum cell transport velocity limited by material strength.

## Approach
The model treats strings as extremely thin, one-dimensional objects formed by a helical generator in a solution of chiral molecules. The string formation speed v is derived from molecular diffusion, the number density n, molecular size a, and the generator geometry (radius r, pitch h). The time for radial cooperative assembly t_SD is estimated from the diffusion time across the pitch h. The strength-limited cell transport velocity [V] follows from the string's breaking stress [σ], diameter d, cell size D*, and medium viscosity η. For information exchange, the latency advantage over diffusion is quantified by two thresholds: a linear-growth threshold L* (when the string grows along a generator) and a radial-assembly threshold L_radial = sqrt(D*t_SD). The material efficiency advantage is quantified by a threshold L** that accounts for the number of signaling molecules required. Specifically, the model gives the following relations (in cgs units):

v = D * a² * h * n / r   (thin-string limit h ≈ r)
t_SD = h² / (6 * D)
[V] = [σ] * d² / (D* * η)
L* = a * (a⁻³ / n)
L_radial = sqrt(D * t_SD)
L** = d * (D*/a)^{3/2} * (32 * n_D)^{-1/2}

All quantities are computed from the following parameter set (use these exact values):

- a = 4.0×10⁻⁷ cm           (molecular size)
- n = 6.0×10¹⁷ cm⁻³         (number density of chiral molecules)
- D = 1.0×10⁻⁵ cm²/s        (diffusion coefficient)
- r = 2.0×10⁻⁶ cm           (generator radius)
- h = 2.0×10⁻⁶ cm           (generator pitch)
- d = 1.0×10⁻⁷ cm           (string diameter)
- D* = 1.0×10⁻³ cm          (cell diameter)
- n_D = 50                  (minimum detectable molecules)
- η = 1.0×10⁻² g/(cm·s)    (medium viscosity)
- [σ] = 5.0×10⁹ dyn/cm²    (breaking stress of string material)

These are the inputs to all computations.

## Reproduction target
Given the parameter set defined above, compute the following six quantities and write them as plain text (a single floating-point number) into the specified output files:
  1. String formation speed v (cm/s) → step_v.txt
  2. Cooperative assembly time t_SD (s) → step_t_SD.txt
  3. Strength-limited transport velocity [V] (cm/s) → step_V_strength.txt
  4. Latency threshold for linear growth L* (cm) → step_L_star.txt
  5. Radial assembly speed threshold L_radial (cm) → step_L_radial.txt
  6. Material-consumption threshold L** (cm) → step_L_dstar.txt
All outputs are deterministic; follow the formulas and parameter values exactly.

## Assets

- Python 3 with numpy: numpy

## Workflow steps

### Step 1: Parameter setup
- Role: process
- Action: Define and record all physical and material parameters (a, n, D, r, h, d, D*, eta, sigma, n_D) as specified in the instruction. Write them to parameters.json for documentation.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Calculate string formation speed v
- Role: scored (load-bearing)
- Action: Compute the string growth speed v from the molecular-scale formula v = D * a^2 * h * n / r (thin string approximation h ~ r). Write the result to step_v.txt.
- Output file: `/app/outputs/step_v.txt`
- Format: txt
- Contract: Plain text file containing a single floating-point number in cm/s.
- Scoring: scored by hidden verifier

### Step 3: Calculate cooperative assembly time t_SD
- Role: scored
- Action: Compute the radial cooperative assembly time t_SD = h^2 / (6 * D). Write the result to step_t_SD.txt.
- Output file: `/app/outputs/step_t_SD.txt`
- Format: txt
- Contract: Plain text file containing a single floating-point number in seconds.
- Scoring: scored by hidden verifier

### Step 4: Calculate strength-limited transport velocity [V]
- Role: scored
- Action: Compute the maximum cell transport speed limited by string strength: [V] = [sigma] * d^2 / (D* * eta). Write the result to step_V_strength.txt.
- Output file: `/app/outputs/step_V_strength.txt`
- Format: txt
- Contract: Plain text file containing a single floating-point number in cm/s.
- Scoring: scored by hidden verifier

### Step 5: Calculate latency threshold L* (linear growth)
- Role: scored
- Action: Compute L* = a * (a^{-3} / n). Write the result to step_L_star.txt.
- Output file: `/app/outputs/step_L_star.txt`
- Format: txt
- Contract: Plain text file containing a single floating-point number in cm.
- Scoring: scored by hidden verifier

### Step 6: Calculate radial assembly speed threshold
- Role: scored
- Action: Using the previously computed t_SD and the diffusion coefficient D, compute the distance threshold L_radial = sqrt(D * t_SD). Write the result to step_L_radial.txt.
- Output file: `/app/outputs/step_L_radial.txt`
- Format: txt
- Contract: Plain text file containing a single floating-point number in cm.
- Scoring: scored by hidden verifier

### Step 7: Calculate material-consumption threshold L**
- Role: scored
- Action: Compute L** = d * (D* / a)^{3/2} * (32 * n_D)^{-1/2}. Write the result to step_L_dstar.txt.
- Output file: `/app/outputs/step_L_dstar.txt`
- Format: txt
- Contract: Plain text file containing a single floating-point number in cm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_v.txt`
- `/app/outputs/step_t_SD.txt`
- `/app/outputs/step_V_strength.txt`
- `/app/outputs/step_L_star.txt`
- `/app/outputs/step_L_radial.txt`
- `/app/outputs/step_L_dstar.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_v.txt
- path: `/app/outputs/step_v.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: String formation speed v.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: cm/s

### step_t_SD.txt
- path: `/app/outputs/step_t_SD.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Cooperative radial assembly time t_SD.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: seconds

### step_V_strength.txt
- path: `/app/outputs/step_V_strength.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Strength-limited cell transport velocity [V].
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: cm/s

### step_L_star.txt
- path: `/app/outputs/step_L_star.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Latency threshold L* for linear generator growth.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: cm

### step_L_radial.txt
- path: `/app/outputs/step_L_radial.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Latency threshold for radial cooperative assembly.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: cm

### step_L_dstar.txt
- path: `/app/outputs/step_L_dstar.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Material consumption threshold L**.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: cm

Notes: All scored quantities are deterministic given the parameter set. The checker recomputes each value and compares with the paper's expected value within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_v.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "cm/s"
      },
      "description": "String formation speed v."
    },
    {
      "file": "step_t_SD.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "seconds"
      },
      "description": "Cooperative radial assembly time t_SD."
    },
    {
      "file": "step_V_strength.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "cm/s"
      },
      "description": "Strength-limited cell transport velocity [V]."
    },
    {
      "file": "step_L_star.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "cm"
      },
      "description": "Latency threshold L* for linear generator growth."
    },
    {
      "file": "step_L_radial.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "cm"
      },
      "description": "Latency threshold for radial cooperative assembly."
    },
    {
      "file": "step_L_dstar.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "cm"
      },
      "description": "Material consumption threshold L**."
    }
  ],
  "notes": "All scored quantities are deterministic given the parameter set. The checker recomputes each value and compares with the paper's expected value within tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes each quantity using the same formulas and parameters and compares your output against the expected value within a tight tolerance. The final reward is a weighted average over the six scored stages; full credit requires all values to be within tolerance. Partial credit is proportional to the number of correct outputs. The verifier handles tolerance thresholds automatically; you do not need to know them.
