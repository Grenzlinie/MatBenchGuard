# Green's Function Analysis of Localized Defect States in Semiconductors

## Problem background
Point defects in semiconductors can introduce electronic states within the band gap that strongly affect the material's properties. Calculating the energies of these localized states from first principles is nontrivial because the defect breaks the crystal periodicity. A powerful framework is the Green's function approach expanded in Wannier functions of the perfect crystal: one constructs the Green's function and the defect perturbation matrices on a Wannier basis, block‑diagonalizes by symmetry, and solves a determinantal equation for bound‑state energies. In this task you will implement that full pipeline for the neutral divacancy in silicon (two adjacent atoms removed without lattice relaxation). The energy of any bound states will be determined as a function of a defect potential strength parameter λ. Your implementation must reproduce the band structure, Wannier functions, Green's function, defect potential, and the symmetry‑reduced secular equations from scratch.

## Approach
You will implement a first‑principles Green's function / Wannier‑function method. The core idea is to expand the crystal wavefunctions in Wannier functions of the perfect silicon lattice and then construct the sub‑matrices of the Green's function G and the defect potential V in that basis. The determinantal equation det(G⁻¹(E) − λV) = 0 is solved for the energy E. The workflow proceeds as follows: (1) Perform a pseudopotential band structure calculation for silicon using Brust's parameters with 15 plane waves, obtain the energy bands Eₙ(k) and Bloch functions for the lowest eight bands on a grid covering the Brillouin zone. (2) Construct Wannier functions aₙ(r−R_μ) for those eight bands via Fourier transformation of the Bloch functions. (3) Compute the Green's function matrix elements (nμ|G(E)|lν) on the Wannier basis for the subspace consisting of the central unit cell and 12 neighbouring cells (13 sites total), using numerical integration over the Brillouin zone. (4) Build the defect potential V: represent the divacancy as the negative of the sum of neutral‑atom pseudopotentials centred at the two missing atom sites (a/8, a/8, a/8) and (−a/8, −a/8, −a/8). Evaluate its matrix elements in the same Wannier basis, exploiting symmetry to reduce the full 104×104 problem to 510 independent elements. (5) Apply D₃d group theory to form symmetrized combinations of Wannier functions that transform according to the one‑dimensional irreducible representations Γ₁ and Γ₂′. This yields reduced matrices G⁻¹ and V of size 13×13 for Γ₁ and 7×7 for Γ₂′. (6) For each λ in {1.0, 1.2, 1.4, 1.6, 1.8, 2.0}, solve det[G⁻¹(E) − λV] = 0 (with G⁻¹ evaluated at E) to find any bound‑state energy E. Record the energy in eV above the valence‑band maximum (VBM = 0.0 eV), or null if no bound state is found. The silicon crystal structure is the diamond lattice with lattice constant 5.43 Å, space group Fd 3 m, and a two‑atom basis at (0,0,0) and (a/4,a/4,a/4). All numerical steps must be implemented; no pre‑computed matrices, fitted curves, or lookup tables are permitted.

## Reproduction target
Compute the energies of localized electronic states associated with the neutral divacancy in silicon for the undistorted lattice (D₃d symmetry). Determine the bound‑state energies (if any) for the Γ₁ and Γ₂′ irreducible representations at six values of the defect potential strength parameter λ: 1.0, 1.2, 1.4, 1.6, 1.8, and 2.0. All energies are measured in eV above the valence‑band maximum (VBM = 0.0 eV). If no bound state exists at a given (symmetry, λ) pair, report a null value. Store the results in a JSON file with keys `"lambda"`, `"E_Gamma1"`, and `"E_Gamma2"`. Each key maps to a list of six values (floats or nulls) in the order of increasing λ. This file is the sole scored artifact.

## Assets

- Brust pseudopotential parameters for silicon: https://doi.org/10.1103/PhysRev.134.A1337
- Silicon diamond crystal structure
- NumPy and SciPy: scipy

## Workflow steps

### Step 1: Generate silicon band structure and Wannier functions
- Role: process
- Action: Implement a pseudopotential band structure calculation for silicon using Brust's parameters with 15 plane waves, compute energy bands on a grid covering the full Brillouin zone, and construct Wannier functions for the lowest eight bands via Fourier transform of Bloch functions.
- Evidence: none

### Step 2: Compute Green's function matrix elements
- Role: process
- Action: For the 8-band, 13-site subspace (central cell plus 12 neighboring cells), compute matrix elements (nμ|G(E)|lν) by numerical integration over the Brillouin zone using the previously obtained band energies and Wannier functions. Form the submatrix G(E) for the divacancy problem.
- Evidence: none

### Step 3: Compute defect potential matrix elements
- Role: process
- Action: Construct the divacancy defect potential as the negative sum of neutral-atom pseudopotentials at sites (a/8,a/8,a/8) and (-a/8,-a/8,-a/8). Compute its Wannier-basis matrix elements for all required site-band pairs, reducing by symmetry to the independent set (510 elements).
- Evidence: none

### Step 4: Symmetry block-diagonalization
- Role: process
- Action: Apply D₃d group theory to construct symmetrized Wannier function combinations for the Γ₁ and Γ₂′ irreducible representations. Form the reduced submatrices G⁻¹ and V (sizes 13×13 and 7×7) for each representation.
- Evidence: none

### Step 5: Solve determinantal equation for bound state energies
- Role: scored (load-bearing)
- Action: For λ ∈ [1.0, 1.2, 1.4, 1.6, 1.8, 2.0], find the energy E that satisfies det[G⁻¹(E) − λV] = 0 for Γ₁ and Γ₂′ symmetries. If a bound state exists, record its energy in eV above the valence‑band maximum (VBM = 0.0 eV); otherwise record null. Produce the JSON output file with the six λ values and the corresponding energy lists.
- Output file: `/app/outputs/step_01_energies_vs_lambda.json`
- Format: json
- Contract: A JSON object with keys 'lambda', 'E_Gamma1', 'E_Gamma2'. 'lambda' is a list [1.0,1.2,1.4,1.6,1.8,2.0]. 'E_Gamma1' and 'E_Gamma2' are each a list of six floats (or nulls), giving the bound state energy in eV above VBM (0.0 eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energies_vs_lambda.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energies_vs_lambda.json
- path: `/app/outputs/step_01_energies_vs_lambda.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Energies of divacancy bound states for Γ₁ and Γ₂′ symmetries as functions of defect potential strength λ, computed by solving det[G⁻¹(E)−λV]=0 after block-diagonalization. The checker compares each energy against hidden gold values with an absolute tolerance, awarding credit for each (symmetry, λ) pair that meets the threshold.
- schema:
  - `type`: object
  - `required`:
    - `lambda`: array
    - `E_Gamma1`: array
    - `E_Gamma2`: array
  - `properties`:
    - `lambda`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 6
      - `maxItems`: 6
    - `E_Gamma1`:
      - `type`: array
      - `items`:
        - `type`: number
        - `nullable`: True
      - `minItems`: 6
      - `maxItems`: 6
    - `E_Gamma2`:
      - `type`: array
      - `items`:
        - `type`: number
        - `nullable`: True
      - `minItems`: 6
      - `maxItems`: 6
  - `unit`:
    - `E_Gamma1`: eV above VBM
    - `E_Gamma2`: eV above VBM

Notes: The JSON must contain three keys: 'lambda' (list of six floats), 'E_Gamma1' and 'E_Gamma2' (each list of six floats or nulls). All energies are measured relative to the valence-band maximum (VBM=0 eV). The checker evaluates each pair against a hidden gold tolerance; the final reward is the fraction of pairs within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energies_vs_lambda.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "lambda": "array",
          "E_Gamma1": "array",
          "E_Gamma2": "array"
        },
        "properties": {
          "lambda": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 6,
            "maxItems": 6
          },
          "E_Gamma1": {
            "type": "array",
            "items": {
              "type": "number",
              "nullable": true
            },
            "minItems": 6,
            "maxItems": 6
          },
          "E_Gamma2": {
            "type": "array",
            "items": {
              "type": "number",
              "nullable": true
            },
            "minItems": 6,
            "maxItems": 6
          }
        },
        "unit": {
          "E_Gamma1": "eV above VBM",
          "E_Gamma2": "eV above VBM"
        }
      },
      "description": "Energies of divacancy bound states for Γ₁ and Γ₂′ symmetries as functions of defect potential strength λ, computed by solving det[G⁻¹(E)−λV]=0 after block-diagonalization. The checker compares each energy against hidden gold values with an absolute tolerance, awarding credit for each (symmetry, λ) pair that meets the threshold."
    }
  ],
  "notes": "The JSON must contain three keys: 'lambda' (list of six floats), 'E_Gamma1' and 'E_Gamma2' (each list of six floats or nulls). All energies are measured relative to the valence-band maximum (VBM=0 eV). The checker evaluates each pair against a hidden gold tolerance; the final reward is the fraction of pairs within tolerance."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/step_01_energies_vs_lambda.json` and compares each of the 12 reported energies (Γ₁ and Γ₂′ at each λ) against reference values derived from the original work. The comparison uses an absolute tolerance. Your reward is the fraction of (symmetry, λ) pairs whose energies are within tolerance, so higher accuracy yields a higher score. The verifier also checks that the JSON conforms to the required schema and that values are physically plausible. Simply copying numbers from a publication is insufficient; you must honestly execute the computational pipeline described in the workflow steps.
