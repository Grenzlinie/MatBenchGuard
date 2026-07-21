# Deterministic Annealing Vector Quantization for Equivalent Homogeneous Surrogate Learning

## Problem background
Stochastic upscaling in random microstructures is a central challenge in solid mechanics: given a random heterogeneous medium described by a high-dimensional random field, how can we replace it with an equivalent homogeneous surrogate that preserves the macroscale response? This task follows an information-theoretic approach: we quantify the information contained in the microstructure and condense it into a lower-dimensional distribution of homogenized properties. The objective is to learn an optimal distribution of an equivalent modulus that minimizes the expected distortion between the predictions of the original microstructure and the homogeneous approximation. The paper casts this as a vector quantization problem and solves it with deterministic annealing. In this task you will reproduce the displacement-targeted experiment for a 2D two-phase random medium.

## Approach
The method works as follows. First, you generate an ensemble of random binary microstructures by thresholding a Gaussian random field with a specified correlation length. For each microstructure, you solve the plane-stress linear elasticity problem with a known loading and boundary conditions and record the horizontal and vertical displacements at a set of interior points; these serve as the reference responses. Then you train a deterministic annealing vector quantizer. The quantizer maintains a codebook of equivalent homogeneous modulus values (atoms) and their probabilities. The distortion is the average squared difference between the true displacement vector and the displacement vector of a homogeneous bar with that modulus. The training alternates between computing Gibbs association probabilities, updating the atoms via Monte Carlo expectations of the response, and cooling the temperature while doubling the codebook size to explore more complex distributions. The final output is the codebook and the achieved expected distortion. The algorithm converges on a minimal distortion representation that captures the macroscale behavior.

## Reproduction target
You will implement the full pipeline for the displacement case. Generate M=500 microstructure realizations on a 512x512 grid, assign phases with moduli E1=1 and E2=10 (Poisson ratio 0.3), and compute the displacement components at ten specified interior points. Use these as training data to train the deterministic annealing quantizer. The final artifact is a JSON file equivalent_surrogate.json containing three fields: atoms (array of float), probabilities (array of float), and final_distortion (float). The hidden verifier will compare your atoms and final_distortion to the paper's reference values. Report the learned codebook and distortion after convergence.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate microstructure realizations and compute reference displacement responses
- Role: process
- Action: Generate an ensemble of M=500 random binary microstructure realizations on a 512x512 grid by thresholding a Gaussian random field with autocorrelation ρ(‖z‖^2)=e^{-‖z‖^2/0.1}. For each realization, assign elastic moduli E1=1 or E2=10 and solve the plane-stress elasticity problem with left-edge unit horizontal traction and right-edge fixed to obtain the horizontal and vertical displacement components at the ten prescribed interior points (A(0.910,0.660), B(0.686,0.316), C(0.830,0.730), D(0.297,0.00195), E(0.943,0.393), F(0.0938,0.379), G(0.0977,0.309), H(0.771,0.926), I(0.990,0.719), J(0.873,0.770)). Collect the training pairs (microstructure vector X and displacement vector r(X)).
- Evidence: `/app/outputs/training_data.npz`

### Step 2: Train deterministic annealing quantizer and output equivalent surrogate
- Role: scored (load-bearing)
- Action: Implement the deterministic annealing vector quantization algorithm as described in the paper (Gibbs association probabilities, Monte Carlo update of codebook atoms and probabilities, atom doubling, temperature cooling). Define the distortion as the average squared displacement difference d(X,Y)=(1/10) Σ (r_i(X)-r_i(Y))^2, where r_i(Y) are the displacements of a homogeneous medium with modulus Y computed similarly. Train on the generated data until convergence. Write the final codebook (atoms y_i), their probabilities q_i, and the final expected distortion to /app/outputs/equivalent_surrogate.json.
- Output file: `/app/outputs/equivalent_surrogate.json`
- Format: json
- Contract: {"atoms": [list of floats], "probabilities": [list of floats], "final_distortion": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equivalent_surrogate.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equivalent_surrogate.json
- path: `/app/outputs/equivalent_surrogate.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The final codebook (atoms and probabilities) and the final expected distortion achieved by the trained deterministic annealing vector quantizer. The checker compares these against the paper's reported values, verifying that the equivalent homogeneous surrogate correctly captures the displacement-targeted upscaling result.
- schema:
  - `type`: object
  - `required`:
    - `atoms`: array of floats
    - `probabilities`: array of floats
    - `final_distortion`: float

Notes: Only the displacement-targeted experiment is reproduced; pointwise stress, total reaction, and other cases are omitted. The finite-element solver for computing displacements is left open-ended (the agent may use a direct stiffness solver on the pixel grid or an analytical approximation for the homogeneous case).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equivalent_surrogate.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "atoms": "array of floats",
          "probabilities": "array of floats",
          "final_distortion": "float"
        }
      },
      "description": "The final codebook (atoms and probabilities) and the final expected distortion achieved by the trained deterministic annealing vector quantizer. The checker compares these against the paper's reported values, verifying that the equivalent homogeneous surrogate correctly captures the displacement-targeted upscaling result."
    }
  ],
  "notes": "Only the displacement-targeted experiment is reproduced; pointwise stress, total reaction, and other cases are omitted. The finite-element solver for computing displacements is left open-ended (the agent may use a direct stiffness solver on the pixel grid or an analytical approximation for the homogeneous case)."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads your equivalent_surrogate.json. It checks that the atoms and probabilities are arrays of floats and that final_distortion is a float. The verifier compares the reported atom value(s) and final_distortion against the paper's hidden gold values, using tolerance-based comparisons. Full credit is awarded if your result is within the accepted tolerance (or better than the paper). The verifier does not disclose the target numbers; you must compute them genuinely. Simply copying the paper's values without running the full workflow will not pass the hidden checks. The final reward is a weight sum over the scored artifact. Your job is to produce the artifact as specified; the verification is fully automated.
