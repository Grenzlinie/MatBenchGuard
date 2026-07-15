# Correlation Functions of the Linear Ising Model with Three-Spin Interaction via Green's Function Method

## Problem background
The linear Ising model with many-particle interactions is an important lattice model in the theory of phase transitions. This task focuses on the case of a three-spin interaction (n=3). The goal is to determine the two-spin correlation functions and the magnetic susceptibility as a function of temperature, using a Green's function approach that yields exact analytic expressions. You will implement the computational derivation and solve for the numeric values at a specific temperature, producing the main quantitative results of the study.

## Approach
The approach is based on the Green's function equation-of-motion method for spin-1/2 operators. You will implement the Hamiltonian for a linear chain with three-spin interaction, construct the cluster operator σ_k, and compute its eigenvalues to obtain a reduction relation that closes the hierarchy of equations of motion. From this reduction relation, a generating equation is derived, which leads to a homogeneous system of linear equations relating two-spin and three-spin correlation functions within a three-spin cluster. Solving this system together with the normalization condition yields the two-spin correlation functions; the magnetic susceptibility is then obtained from an analytic expression in terms of the model parameters.

## Reproduction target
Implement the Green's function derivation and solve for the two-spin correlation functions ⟨S_i^z S_0^z⟩ for i = 1, 2, 3 and the magnetic susceptibility χ for the linear Ising model with three-spin interaction at temperature T = 1, taking J = 1 and k_B = 1. Output the numeric values to a JSON file with keys `corr_1`, `corr_2`, `corr_3`, `susceptibility`.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy
- SymPy: sympy

## Workflow steps

### Step 1: Derive cluster operator and reduction relation
- Role: process
- Action: Define the spin-1/2 algebra and the Hamiltonian for n=3. Derive the cluster operator σ_k. Enumerate the 2^{n-1}=4 spin configurations of the interacting cluster and compute eigenvalues ε_l to obtain the reduction relation ∏(σ-ε_l)=0.
- Evidence: `/app/outputs/reduction_relation_log.txt`

### Step 2: Construct generating equation and correlation system
- Role: process
- Action: Using the reduction relation, derive the generating equation and set up the homogeneous linear system relating two-spin correlation functions φ_2^{(1)}=⟨S_1^z S_0^z⟩, φ_2^{(2)}=⟨S_2^z S_0^z⟩ and three-spin correlation functions φ_3^{(2)}, φ_3^{(3)} within a three-spin cluster. Express the system in terms of known parameters (J, T) and the hyperbolic functions that appear in the paper's analytic development.
- Evidence: `/app/outputs/system_equations_log.txt`

### Step 3: Solve for correlation functions and susceptibility
- Role: scored (load-bearing)
- Action: Solve the homogeneous system together with the normalization condition ⟨S_0^z S_0^z⟩ = 1/4 to obtain the two-spin correlation functions ⟨S_i^z S_0^z⟩ for i=1,2,3. Then compute the magnetic susceptibility χ using the analytic expression from the paper. Use J=1, k_B=1, T=1. Write the results to correlation_results.json with keys corr_1, corr_2, corr_3, susceptibility (all floating-point numbers).
- Output file: `/app/outputs/correlation_results.json`
- Format: json
- Contract: {"type": "object", "required": {"corr_1": "float", "corr_2": "float", "corr_3": "float", "susceptibility": "float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlation_results.json
- path: `/app/outputs/correlation_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Two-spin correlation functions (corr_1 = ⟨S_1^z S_0^z⟩, corr_2 = ⟨S_2^z S_0^z⟩, corr_3 = ⟨S_3^z S_0^z⟩) and magnetic susceptibility χ for the linear Ising model with three-spin interaction at T=1 (J=1, k_B=1).
- schema:
  - `type`: object
  - `required`:
    - `corr_1`: float
    - `corr_2`: float
    - `corr_3`: float
    - `susceptibility`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "corr_1": "float",
          "corr_2": "float",
          "corr_3": "float",
          "susceptibility": "float"
        }
      },
      "description": "Two-spin correlation functions (corr_1 = ⟨S_1^z S_0^z⟩, corr_2 = ⟨S_2^z S_0^z⟩, corr_3 = ⟨S_3^z S_0^z⟩) and magnetic susceptibility χ for the linear Ising model with three-spin interaction at T=1 (J=1, k_B=1)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. It independently scores the artifact(s) produced at each workflow stage, weighting them according to their importance, and combines them into a final reward between 0 and 1. It checks the contents of the output files you write under `/app/outputs`. Merely reporting the paper's values is insufficient—you must execute the described computation and produce the required files with the correct structure.
