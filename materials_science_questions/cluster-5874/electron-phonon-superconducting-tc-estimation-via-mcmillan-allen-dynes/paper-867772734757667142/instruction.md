# Pairing Symmetry and Tc from 3D Hubbard Model with Perturbative Approach

## Problem background
This task investigates the superconducting pairing mechanism in the heavy fermion compound CeIn₃ under pressure. The system is described by a three-dimensional single-band Hubbard model, and the effective interaction between quasiparticles is treated by third-order perturbation theory in the on-site Coulomb repulsion U. The pairing instability is driven by antiferromagnetic spin fluctuations near the wavevector Q = (π, π, π). The problem is to determine which pairing symmetry is most favorable and to compute the superconducting transition temperature T́ in the 3D system. A central question is how dimensionality affects T́: the same model (with a 2D square lattice, same electron density, and the same relative interaction strength U/W) yields a different T́, and the ratio T́(3D)/T́(2D) is a key quantity that characterizes the role of dimensionality in heavy fermion superconductivity.

## Approach
We use third-order perturbation theory (TOPT) for the single-band Hubbard model. The bare Green’s function on a discrete momentum-frequency grid defines the starting point. From it we compute the bare particle-hole susceptibility and an auxiliary function that enter the normal self-energy. The self-energy is used to dress the Green’s function self-consistently, keeping the electron density fixed. The effective singlet pairing interaction is built as the sum of RPA-like terms and vertex corrections, both evaluated to third order in U. The linearized Eliashberg equation is then solved as an eigenvalue problem for candidate pairing channels; the channel(s) with the largest eigenvalue indicate the leading pairing symmetry. Finally, by scanning temperature we locate the critical temperature T́ where the eigenvalue reaches unity. The procedure is carried out for a 3D simple cubic lattice at U ≈ 9.0 and for the corresponding 2D square lattice at U ≈ 6.0, keeping the ratio U/bandwidth ≈ 0.75 in both cases, and the ratio T́(3D)/T́(2D) is computed from the two transition temperatures.

## Reproduction target
Compute the dominant superconducting pairing symmetry and the transition temperature T́ (in units of the nearest-neighbor hopping t₁) for a 3D simple cubic Hubbard model with parameters t₂ = −0.2, electron density n = 0.45, and U ≈ 9.0 (corresponding to U/W ≈ 0.75). Also compute T́ for the equivalent 2D square lattice model (same t₂ and n, with U ≈ 6.0 to keep U/W ≈ 0.75). Report the ratio T́(3D)/T́(2D). The result must be written to /app/outputs/results.json, containing the fields: leading_symmetries (a list of strings naming the pairing channels with the largest eigenvalues), Tc_3D (float), Tc_2D (float), and Tc_ratio (float).

## Assets

- Python 3 scientific libraries (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Model setup and bare Green's function
- Role: process
- Action: Define the 3D single-band Hubbard model on a simple cubic lattice with nearest-neighbor hopping amplitude t1=1, next-nearest-neighbor hopping amplitude t2=-0.2, on-site Coulomb interaction U, and electron density n=0.45. Implement the dispersion relation E(k) = -2 t1 (cos kx + cos ky + cos kz) + 4 t2 (cos kx cos ky + cos ky cos kz + cos kz cos kx). Compute the bare chemical potential μ0 that satisfies n = Σ_k G0(k) and evaluate the bare Green's function G0(k) = 1 / (i ω_n - (E(k) - μ0)) on a discrete momentum grid and Matsubara frequency set.
- Evidence: `/app/outputs/bare_green_function.npz`

### Step 2: Compute bare susceptibilities χ0 and φ0
- Role: process
- Action: Using the bare Green's function G0(k), compute the bare particle-hole susceptibility χ0(q) = - Σ_k G0(k) G0(q+k) and the auxiliary function φ0(q) = - Σ_k G0(k) G0(q-k) on the same momentum grid, for a range of bosonic Matsubara frequencies.
- Evidence: `/app/outputs/bare_susceptibilities.npz`

### Step 3: Compute normal self-energy and dressed Green's function
- Role: process
- Action: For the 3D system with U=9.0, compute the third-order normal self-energy Σ_n(k) using the perturbative formula: Σ_n(k) = Σ_{k'} [ U^2 χ0(k-k') + U^3 ( χ0^2(k-k') + φ0^2(k+k') ) ] G0(k'). Iteratively adjust the chemical potential μ to enforce n = Σ_k G(k) with the dressed Green's function G(k) = 1 / ( i ω_n - (E(k) - μ) - Σ_n(k) ), and store the converged G(k). Separately, repeat the same procedure for the 2D square-lattice system (setting the interlayer hopping to zero, same t2=-0.2 and n=0.45, with U=6.0 to keep U/W≈0.75) and store its dressed Green's function.
- Evidence: `/app/outputs/dressed_green_3D.npz`

### Step 4: Construct effective pairing interaction
- Role: process
- Action: For both 3D and 2D systems, build the singlet pairing interaction V(k, k') = V_RPA + V_vertex using the third-order expressions: V_RPA = U + U^2 χ0(k-k') + 2 U^3 χ0^2(k-k'), and V_vertex = 2 U^3 Re Σ_{k''} G0(k+k''-k') [ χ0(k+k'') - φ0(k+k'') ] G0(k''). Store the total interaction matrix for the eigenvalue problem.
- Evidence: `/app/outputs/pairing_interaction.npz`

### Step 5: Solve linearized Eliashberg equation for leading pairing symmetry
- Role: process
- Action: For the 3D system at a low temperature (within the numerically reliable regime), solve the eigenvalue problem λ Σ_a^†(k) = - Σ_{k'} V(k,k') |G(k')|^2 Σ_a^†(k') for candidate singlet pairing channels (e.g., d_{x^2-y^2}, d_{3z^2-r^2}, d_{xy}). Identify the channel(s) with the largest eigenvalue as the dominant pairing symmetry.
- Evidence: `/app/outputs/symmetry_check.npz`

### Step 6: Determine Tc for 3D and 2D systems and compute ratio
- Role: scored (load-bearing)
- Action: For the leading pairing symmetry identified in the previous step, scan temperature to find the critical temperature Tc where the eigenvalue λ reaches 1 for the 3D system (U=9.0) and, separately, for the 2D system (U=6.0). Compute the ratio Tc_3D / Tc_2D. Write /app/outputs/results.json containing the keys: "leading_symmetries" (list of strings naming the dominant pairing channel(s)), "Tc_3D" (float, in units of t1), "Tc_2D" (float, in units of t1), and "Tc_ratio" (float).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"leading_symmetries": ["string", ...], "Tc_3D": 0.0, "Tc_2D": 0.0, "Tc_ratio": 0.0}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the leading superconducting pairing symmetries and the transition temperatures for the 3D and 2D Hubbard models.
- schema:
  - `type`: object
  - `properties`:
    - `leading_symmetries`:
      - `type`: array
      - `items`:
        - `type`: string
    - `Tc_3D`:
      - `type`: number
    - `Tc_2D`:
      - `type`: number
    - `Tc_ratio`:
      - `type`: number
  - `required`: `leading_symmetries`, `Tc_3D`, `Tc_2D`, `Tc_ratio`

Notes: The hidden checker compares the contents of results.json against the paper's reported values with appropriate tolerances. No other files are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "leading_symmetries": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "Tc_3D": {
            "type": "number"
          },
          "Tc_2D": {
            "type": "number"
          },
          "Tc_ratio": {
            "type": "number"
          }
        },
        "required": [
          "leading_symmetries",
          "Tc_3D",
          "Tc_2D",
          "Tc_ratio"
        ]
      },
      "description": "Scored artifact containing the leading superconducting pairing symmetries and the transition temperatures for the 3D and 2D Hubbard models."
    }
  ],
  "notes": "The hidden checker compares the contents of results.json against the paper's reported values with appropriate tolerances. No other files are scored."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/results.json. It checks whether the list of leading symmetries contains the correct pairing channels, and whether the reported Tc_3D, Tc_2D, and Tc_ratio are within numerically acceptable tolerance of the expected reference values. Full credit is awarded when all conditions are met; partial credit may be assigned for partially correct results. Intermediate process steps are required to produce the final result but are not directly scored.
