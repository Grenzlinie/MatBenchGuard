# Derivation of Longitudinal Spin Correlation via Green's Function Method

## Problem background
The longitudinal spin correlation function is a key observable in ferromagnets, encoding the spatial correlations of spin fluctuations. For a spin-1 Heisenberg ferromagnet with single-ion uniaxial anisotropy on a two-dimensional square lattice, a Green's function equation-of-motion method within the random phase approximation (RPA) can be used to derive it. A crucial technical step is treating the anisotropy term as a differential operator acting on generating functions, which avoids the need to decouple on-site spin operators and yields results that remain valid for arbitrary anisotropy strength D. Your task is to implement this formalism: compute the generating function Ω(x)=⟨exp(x S^z)⟩ and the associated self-consistent spin averages, then obtain the longitudinal correlation function χ_q^{zz} for a set of wavevectors.

## Approach
The method proceeds by first defining a differential operator D_x(ω) and a spectral quantity ∅(m) that arise from the RPA decoupling of the exchange interactions. The anisotropy contribution is kept as a derivative with respect to x, leading to a differential equation for the generating function Ω(x). Solving this self-consistently yields the moments ⟨S^z⟩ and ⟨(S^z)^2⟩ and the explicit form of Ω(x) as a sum of exponentials weighted by coefficients determined by ∅(m). Using Ω(x), you then construct the generating function Λ_{i,j}(x)=⟨exp(x S_i^z) Ŝ_j^z⟩, whose expansion coefficients follow from ∅(m) and the Ω(x) coefficients. Differentiating Λ_{i,j}(x) at x=0 gives the real-space longitudinal correlation ⟨Ŝ_i^z Ŝ_j^z⟩, and a spatial Fourier transform produces χ_q^{zz}. Finally, you evaluate this function for several anisotropy strengths and compare its paramagnetic limit with known asymptotic forms.

## Reproduction target
Compute and output the longitudinal correlation function χ_q^{zz} for a spin-1 Heisenberg ferromagnet on a two-dimensional square lattice (nearest-neighbor coordination z=4, lattice constant a=1) with exchange coupling J=1, temperature T=10J, and external field ω_0=0, for three values of the single-ion anisotropy: D=0.1, 1.0, and 10.0. The target quantity is χ_q^{zz} as a function of wavevector q=(q_x,q_y). Evaluate it at the four high-symmetry points of the first Brillouin zone: (0,0), (π,0), (π,π), (0,π), and on a uniform 10×10 grid covering the full zone [−π,π]×[−π,π] (in units of 1/a). The results must be written to a CSV file with columns q_x, q_y, chi_qzz.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve for generating function Ω(x) and self-consistent averages
- Role: process
- Action: Implement the self-consistent Green's function equations for S=1. Construct the differential operator D_x(ω), evaluate the spectral quantity ∅(m) by Brillouin-zone integration, and solve the system of equations to obtain ⟨S^z⟩, ⟨(S^z)^2⟩, and the generating function Ω(x)=⟨exp(x S^z)⟩ over a range of x. Use parameters: J=1, D=0.1,1.0,10.0, T=10*J, ω_0=0, 2D square lattice with z=4.
- Evidence: `/app/outputs/omega_x_values.csv`

### Step 2: Compute coefficients of the generating function Λ
- Role: process
- Action: Using the obtained Ω(x) and the spectral quantity ∅(m), compute the coefficients c_{ij}^{(m)} for the longitudinal generating function Λ_{i,j}(x)=⟨exp(x S_i^z) Ŝ_j^z⟩ from the closed-form expression derived in the RPA-Green's function formalism.
- Evidence: `/app/outputs/lambda_ij_coefficients.csv`

### Step 3: Compute longitudinal correlation χ_q^{zz} for specified wavevectors
- Role: scored (load-bearing)
- Action: For the same system (S=1, J=1, D=0.1,1.0,10.0, T=10*J, ω_0=0, square lattice), differentiate the generating function Λ(x) at x=0 to obtain ⟨Ŝ_i^z Ŝ_j^z⟩, then perform the spatial Fourier transform to get χ_q^{zz}. Evaluate χ_q^{zz} at the high-symmetry points (0,0), (π,0), (π,π), (0,π) and on a 10×10 uniform grid covering [-π,π]×[-π,π] (in units of 1/a). Write the results to a CSV.
- Output file: `/app/outputs/chi_qzz_values.csv`
- Format: csv
- Contract: CSV with columns: q_x, q_y, chi_qzz (all floats). q_x and q_y in radians per lattice constant.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chi_qzz_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi_qzz_values.csv
- path: `/app/outputs/chi_qzz_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Longitudinal correlation function for S=1 Heisenberg ferromagnet with single-ion anisotropy, computed at given wavevectors.
- schema:
  - `type`: table
  - `required_columns`: `q_x`, `q_y`, `chi_qzz`
  - `units`:
    - `q_x`: radians per lattice constant
    - `q_y`: radians per lattice constant
    - `chi_qzz`: arbitrary

Notes: The hidden checker reads the supporting evidence files 'omega_x_values.csv' and 'lambda_ij_coefficients.csv' (produced by the process steps) to recompute chi_q^{zz} and verify consistency, then compares the recomputed values against a hidden gold reference and the agent's chi_qzz_values.csv. The scoring is based on the accuracy of the chi_q^{zz} values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chi_qzz_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_x",
          "q_y",
          "chi_qzz"
        ],
        "units": {
          "q_x": "radians per lattice constant",
          "q_y": "radians per lattice constant",
          "chi_qzz": "arbitrary"
        }
      },
      "description": "Longitudinal correlation function for S=1 Heisenberg ferromagnet with single-ion anisotropy, computed at given wavevectors."
    }
  ],
  "notes": "The hidden checker reads the supporting evidence files 'omega_x_values.csv' and 'lambda_ij_coefficients.csv' (produced by the process steps) to recompute chi_q^{zz} and verify consistency, then compares the recomputed values against a hidden gold reference and the agent's chi_qzz_values.csv. The scoring is based on the accuracy of the chi_q^{zz} values."
}
```

## How you are scored
A hidden verifier independently recomputes χ_q^{zz} from the intermediate data you provide in omega_x_values.csv and lambda_ij_coefficients.csv. It then compares these recomputed values against hidden reference values that have been calculated from the same theoretical formulation with high precision. Consistency checks verify that the computed χ_q^{zz} values approximate the expected asymptotic form in the paramagnetic limit (k_B T / [1/χ_0 + 2(J(0)−J(q))]) for both small and large D. Your submission is scored per artifact: each wavevector point that passes accuracy and consistency criteria contributes to the final reward, which is a weighted average across all scored outputs. The better your implementation matches the physical results, the higher your score.
