# Elastic Self-Energy and Critical Twist Angle for Planar Honeycomb Dislocation Networks

## Problem background
A planar periodic dislocation network can model a twist grain boundary. The elastic self- and interaction energy of such networks determines which configuration is thermodynamically favoured at a given twist angle. This task computes the elastic properties of a honeycomb dislocation network in a (111) twist boundary of a face-centred cubic metal, and compares its energy to that of a two-independent-set network to find the critical angle where the honeycomb network becomes more stable. The calculation uses a Fourier-sum method that expresses the interaction energy between two identical networks as a sum over reciprocal lattice vectors.

## Approach
The core method is the Fourier-sum calculation of interaction energy per unit area between two identical periodic planar dislocation networks, derived from continuum dislocation theory. For the honeycomb network, the geometry is specified by dislocation segments with screw character forming a regular hexagonal pattern. The interaction-energy function f(x), where x = r/l relates the separation r between two identical networks to the segment length l, is expressed as a sum over reciprocal lattice indices; the sum converges rapidly for non-zero separation. The self-energy is obtained by letting the separation approach zero, which yields a logarithmic divergence at small x. By computing f(x) for a range of small x, the coefficient of the logarithmic term is extracted. For the two-independent-set network, the self-energy has a closed-form expression in terms of the twist angle, the shear modulus, Poisson's ratio, the Burgers vector magnitude, and an assumed core cutoff radius. The critical twist angle is the angle where the honeycomb self-energy equals the two-set network self-energy; the agent must solve this equality using the numerically extracted logarithmic coefficient.

## Reproduction target
Compute the dimensionless interaction-energy function f(x) for a honeycomb screw dislocation network in the (111) twist boundary of an f.c.c. metal, for dimensionless separations x ranging from 1e-4 to 10, with at least 50 logarithmically spaced points. From these data, determine the critical twist angle θ_c below which the honeycomb network is elastically favoured over the two-independent-set network, assuming isotropic elasticity with Poisson ratio ν ≈ 1/3 and a core cutoff radius r_c ≈ b/e (where b is the Burgers vector magnitude and e is Euler's number). Write f(x) as a two-column CSV and θ_c as a single float in radians to the output files specified below.

## Assets

- Python 3.8+ interpreter: python3
- NumPy: numpy

## Workflow steps

### Step 1: Parameterize honeycomb network geometry
- Role: process
- Action: Define the honeycomb dislocation network for a (111) f.c.c. twist boundary: specify dislocation segment vectors, Burgers vectors, unit cell vectors, reciprocal lattice vectors, and derive the dimensionless expression for the interaction energy function f(x) as a Fourier sum over reciprocal lattice points.
- Evidence: none

### Step 2: Parameterize two-independent-sets network geometry
- Role: process
- Action: For the same twist boundary, define the two parallel-set dislocation network: determine line vectors, Burgers vectors, period vectors, and compute the coefficient matrices that enter the analytical self-energy formula.
- Evidence: none

### Step 3: Compute honeycomb interaction energy f(x)
- Role: scored
- Action: Evaluate the Fourier-sum expression for the honeycomb network interaction energy function over a range of dimensionless separations x covering at least 50 points in logarithmic spacing from 1e-4 to 10. Write the results as a two-column CSV.
- Output file: `/app/outputs/honeycomb_f_of_x.csv`
- Format: csv
- Contract: CSV file with header 'x,f_x'. Each row contains a float x and a float f_x separated by a comma.
- Scoring: scored by hidden verifier

### Step 4: Determine critical twist angle
- Role: scored (load-bearing)
- Action: Using the honeycomb_f_of_x.csv data, extract the small-separation logarithmic dependence. Compute the self-energy of the two-independent-sets network using its analytical formula. Compare the two self-energy expressions as functions of twist angle and find the critical angle where the honeycomb network becomes elastically favourable. Write the single critical angle value in radians to a plain text file.
- Output file: `/app/outputs/critical_angle.txt`
- Format: txt
- Contract: A single decimal number (float) in plain text, representing θ_c in radians.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/honeycomb_f_of_x.csv`
- `/app/outputs/critical_angle.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### honeycomb_f_of_x.csv
- path: `/app/outputs/honeycomb_f_of_x.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed dimensionless interaction energy function f(x) for the honeycomb network; checker will recompute the logarithmic slope at small x and compare to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `x`, `f_x`
  - `units`:
    - `x`: dimensionless
    - `f_x`: dimensionless

### critical_angle.txt
- path: `/app/outputs/critical_angle.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Critical twist angle θ_c below which the honeycomb network is stable; checker will read the reported value and compare it to a hidden reference within a tolerance.
- schema:
  - `type`: text
  - `units`:
    - `value`: radians

Notes: Long-range stress effects and lamellar compound analysis (Section 3 of the original paper) are omitted per task scope. Elastic constants, Burgers vector magnitude, and core cutoff assumption are to be chosen by the agent as appropriate for an f.c.c. metal.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "honeycomb_f_of_x.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "f_x"
        ],
        "units": {
          "x": "dimensionless",
          "f_x": "dimensionless"
        }
      },
      "description": "Computed dimensionless interaction energy function f(x) for the honeycomb network; checker will recompute the logarithmic slope at small x and compare to a hidden reference."
    },
    {
      "file": "critical_angle.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "radians"
        }
      },
      "description": "Critical twist angle θ_c below which the honeycomb network is stable; checker will read the reported value and compare it to a hidden reference within a tolerance."
    }
  ],
  "notes": "Long-range stress effects and lamellar compound analysis (Section 3 of the original paper) are omitted per task scope. Elastic constants, Burgers vector magnitude, and core cutoff assumption are to be chosen by the agent as appropriate for an f.c.c. metal."
}
```

## How you are scored
Your submission is scored by an automated verifier that examines each output file. For 'honeycomb_f_of_x.csv', the verifier will read the file, perform a linear fit of the computed f_x versus log10(x) in the small-separation regime (x < 0.1), and compare the resulting logarithmic coefficient to the expected value, awarding credit if it falls within an allowed tolerance. For 'critical_angle.txt', the verifier will read your reported θ_c and compare it to a hidden reference value. Both checks contribute to a single reward score between 0 and 1. No partial credit is given for files that are missing or do not follow the required format; the task is to produce the correct physical result through honest computation.
