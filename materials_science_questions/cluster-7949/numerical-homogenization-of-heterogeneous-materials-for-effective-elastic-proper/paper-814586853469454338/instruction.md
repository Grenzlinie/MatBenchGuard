# Effective Elastic Properties via Two-Step Mean-Field Homogenization

## Problem background
Short-fiber-reinforced metal matrix composites (MMCs) combine lightweight matrices with high-stiffness fibers, making them attractive for structural applications. Accurately predicting their effective elastic properties is important for material selection and design. Mean-field homogenization methods offer a computationally efficient alternative to full-field numerical simulations. The central challenge is to develop a homogenization procedure that accounts for the random orientation and aspect ratio of fibers while maintaining both accuracy and computational speed. This task addresses the prediction of the effective stiffness tensor and derived isotropic elastic constants for a magnesium matrix composite reinforced with randomly oriented short carbon fibers, using a modified two-step mean-field homogenization framework.

## Approach
The method decomposes the composite into infinitesimal pseudo-grains, each containing aligned fibers at a specific orientation. In the first homogenization step, the effective stiffness of each pseudo-grain is estimated by interpolating between the Mori–Tanaka and double-inclusion strain concentration tensors. The interpolation uses a smooth quadratic function of the fiber volume fraction. The underlying single-inclusion problem employs the Eshelby tensor computed for an equivalent fiber aspect ratio that accounts for both the geometric aspect ratio and a factor to improve accuracy for high-aspect-ratio fibers. The per-orientation pseudo-grain stiffnesses are then averaged over all orientations assuming a random uniform orientation distribution; both Voigt (orientation average of stiffness) and Reuss (inverse of orientation average of compliance) bounds are computed. In the second homogenization step, the overall effective stiffness tensor is obtained as the arithmetic mean of the Voigt and Reuss estimates. From this full 6×6 stiffness tensor in Voigt notation, the effective isotropic Young's modulus, shear modulus, and Poisson's ratio are derived using standard isotropic homogenization relations.

## Reproduction target
For a Csf/Mg composite with fiber volume fraction 0.10, matrix Young's modulus 45 GPa and Poisson's ratio 0.35, fiber Young's modulus 230 GPa and Poisson's ratio 0.25, fiber aspect ratio l/d = 15, and an equivalent aspect ratio factor f = 1.25, under a random uniform fiber orientation distribution, compute the effective stiffness tensor in Voigt notation (components C11, C22, C33, C12, C13, C23, C44, C55, C66) and save it to `stiffness_matrix.json`. From this tensor, compute the effective isotropic elastic constants: Young's modulus E (GPa), shear modulus G (GPa), and Poisson's ratio ν (dimensionless), and save them to `effective_constants.json`. All numbers must be derived from the implemented homogenization procedure.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute homogenized stiffness tensor via modified two-step mean-field procedure
- Role: process
- Action: Implement the full modified two-step mean-field homogenization method: compute the Eshelby tensor for equivalent aspect ratio α = 1.25·(l/d) and matrix Poisson's ratio νm; form the single-inclusion strain concentration tensor H^ε; build the Mori–Tanaka and double-inclusion strain concentration tensors B_MT and B_DI; interpolate via the quadratic model to obtain the pseudo-grain strain concentration tensor; compute the effective stiffness tensor of a pseudo-grain; integrate over all orientations assuming a random uniform orientation distribution function to obtain the Voigt and Reuss averages; apply the second-step Voigt-Reuss interpolative model ⟨C⟩_ω = 0.5*(⟨C⟩_ω^Reuss + ⟨C⟩_ω^Voigt) to obtain the final 6×6 stiffness tensor in Voigt notation. Use the following material and geometric parameters: matrix Em = 45 GPa, νm = 0.35; fiber Ef = 230 GPa, νf = 0.25; fiber aspect ratio l/d = 15; equivalent aspect ratio factor f = 1.25; fiber volume fraction v_f = 0.10; random uniform orientation distribution.
- Evidence: `/app/outputs/homogenization_log.txt`

### Step 2: Save effective stiffness tensor to stiffness_matrix.json
- Role: scored (load-bearing)
- Action: Write the computed effective stiffness tensor (in GPa) to a JSON file with keys C11, C22, C33, C12, C13, C23, C44, C55, C66. All off-diagonal entries not listed are zero or negligible.
- Output file: `/app/outputs/stiffness_matrix.json`
- Format: json
- Contract: {"type":"object","required":{"C11":"float","C22":"float","C33":"float","C12":"float","C13":"float","C23":"float","C44":"float","C55":"float","C66":"float"}}
- Scoring: scored by hidden verifier

### Step 3: Extract effective isotropic elastic constants and save to effective_constants.json
- Role: scored
- Action: From stiffness_matrix.json, compute the effective isotropic constants using the following method: (1) compute the bulk modulus K = (C11 + 2*C12)/3, using C12 as the mean of the three off-diagonal entries if they differ; (2) compute the shear modulus G = (C44 + C55 + C66)/3; (3) compute Young's modulus E = 9*K*G/(3*K + G) and Poisson's ratio ν = (3*K - 2*G)/(2*(3*K + G)). Write E (GPa), G (GPa), and ν (dimensionless) to effective_constants.json.
- Output file: `/app/outputs/effective_constants.json`
- Format: json
- Contract: {"type":"object","required":{"E":"float","G":"float","nu":"float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stiffness_matrix.json`
- `/app/outputs/effective_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stiffness_matrix.json
- path: `/app/outputs/stiffness_matrix.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The 6x6 effective stiffness tensor in Voigt notation. Each of the nine independent components is a floating-point number in GPa.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float
    - `C22`: float
    - `C33`: float
    - `C12`: float
    - `C13`: float
    - `C23`: float
    - `C44`: float
    - `C55`: float
    - `C66`: float

### effective_constants.json
- path: `/app/outputs/effective_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Effective isotropic elastic constants: Young's modulus E (GPa), shear modulus G (GPa), and Poisson's ratio ν (dimensionless).
- schema:
  - `type`: object
  - `required`:
    - `E`: float
    - `G`: float
    - `nu`: float

Notes: The checker compares the stiffness matrix components and derived isotropic constants against hidden gold values from the paper using relative tolerances (hidden). The agent must implement the full homogenization procedure; the stiffness matrix step is load-bearing to ensure the computation was performed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stiffness_matrix.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float",
          "C22": "float",
          "C33": "float",
          "C12": "float",
          "C13": "float",
          "C23": "float",
          "C44": "float",
          "C55": "float",
          "C66": "float"
        }
      },
      "description": "The 6x6 effective stiffness tensor in Voigt notation. Each of the nine independent components is a floating-point number in GPa."
    },
    {
      "file": "effective_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E": "float",
          "G": "float",
          "nu": "float"
        }
      },
      "description": "Effective isotropic elastic constants: Young's modulus E (GPa), shear modulus G (GPa), and Poisson's ratio ν (dimensionless)."
    }
  ],
  "notes": "The checker compares the stiffness matrix components and derived isotropic constants against hidden gold values from the paper using relative tolerances (hidden). The agent must implement the full homogenization procedure; the stiffness matrix step is load-bearing to ensure the computation was performed."
}
```

## How you are scored
A hidden verifier will check both output files. The verifier independently scores the stiffness matrix components and the derived isotropic constants against reference values using appropriate tolerances. The two artifacts are weighted equally in the final score. You must implement the full two-step homogenization procedure; simply writing plausible numbers without running the computation will not survive the verifier's checks. The exact scoring criteria and tolerances are hidden to avoid gaming.
