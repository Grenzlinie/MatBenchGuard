# Green's Function Analysis of a 2D Square Lattice of Euler–Bernoulli Beams with Torsional Stiffness

## Problem background
The paper investigates a two-dimensional square lattice of thin Euler–Bernoulli beams. Each junction between beams has mass and rotational inertia, and each beam possesses flexural rigidity and torsional stiffness. This coupling between out-of-plane flexural motion and torsional rotation leads to a rich dynamic response, including band gaps and anisotropic wave propagation. The central object is the dynamic Green's function, which describes the flexural displacement of the lattice under a point forcing (out-of-plane force and/or moments). The dispersion relation, derived from the equation of motion, governs which frequencies propagate and which form band gaps. The task is to implement the dispersion function and the spectral Green's function for a specific set of material parameters, verify the dispersion at known invariant points, and evaluate the real-space flexural displacement in a band gap regime via numerical inverse Fourier transform.

## Approach
The approach is based on the equation of motion for the lattice, which is obtained by combining the Euler–Bernoulli beam equation (fourth-order) for out-of-plane flexural deformation and the torsion equation (second-order) with continuity and equilibrium conditions at the nodes. Applying the discrete Fourier transform yields a 3×3 system in reciprocal space. The solvability condition gives the dispersion function σ(ω,k1,k2). Inverting the system gives a spectral Green's function, whose first component W^F(k1,k2) describes the flexural displacement amplitude for a given forcing vector f.

To reproduce the key results, one must implement:
- The function ζ(P,Q) = -2C cos(P) + 2C + 4 cos(Q) - μ ω^2 + 8, where μ is the rotational inertia and C is the torsional stiffness.
- The dispersion function σ(ω,k1,k2) = 144 sin²(k1) ζ(k1,k2) + 144 sin²(k2) ζ(k2,k1) + (24 cos(k2)+24 cos(k1)+ω²−48) ζ(k1,k2) ζ(k2,k1).
- The spectral flexural displacement W^F(k1,k2) = ζ(k1,k2) ζ(k2,k1) f_w / σ(ω,k1,k2) for out-of-plane forcing (f_w = -1, other components zero).
- The real-space displacement w(m,n) = (1/(4π²)) ∫₋π^π ∫₋π^π W^F(k1,k2) e^{i(k1 m + k2 n)} dk1 dk2, evaluated numerically using, e.g., scipy.integrate.nquad.

The computation is carried out for μ=0.01, C=0.1, and two tasks are performed: (a) evaluating σ at four special (ω,k1,k2) points that are invariant with respect to μ and C, and (b) evaluating w(m,n) for a chosen band-gap frequency ω=9.8 at all integer positions in a 5×5 grid centred at the origin.

## Reproduction target
Implement the dispersion function σ(ω,k1,k2) and the flexural spectral Green's function W^F(k1,k2) as described above for parameters μ=0.01, C=0.1.

1. Compute σ at the four invariant wavenumber–frequency points:
   - ω = 4√6, k1 = π, k2 = π
   - ω = 0, k1 = 0, k2 = 0
   - ω = 4√3, k1 = 0, k2 = π
   - ω = 4√3, k1 = π, k2 = 0
   Write the resulting four numbers to a JSON object with keys "omega_4sqrt6_pi_pi", "omega_0_0_0", "omega_4sqrt3_0_pi", "omega_4sqrt3_pi_0". The checker will independently verify correctness.

2. For ω=9.8, forcing vector f = [-1, 0, 0]ᵀ (out-of-plane force only), compute the real-space flexural displacement w(m,n) for all integer (m,n) with m,n ∈ {-2,-1,0,1,2} (25 points) by numerically evaluating the inverse Fourier transform with an appropriate quadrature (e.g., scipy.integrate.nquad). Output a JSON array of objects, each containing keys "m" (int), "n" (int), and "w" (float).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Dispersion invariant check
- Role: scored
- Action: Implement the dispersion function sigma(omega,k1,k2) = 144 sin²(k1) ζ(k1,k2) + 144 sin²(k2) ζ(k2,k1) + (24 cos(k2)+24 cos(k1)+ω²−48) ζ(k1,k2) ζ(k2,k1), with ζ(P,Q) = −2C cos(P) + 2C + 4 cos(Q) − μ ω² + 8, using μ=0.01 and C=0.1. Compute sigma at the four invariant points: (i) ω=4√6, k1=π, k2=π; (ii) ω=0, k1=0, k2=0; (iii) ω=4√3, k1=0, k2=π; (iv) ω=4√3, k1=π, k2=0. Write the four results to a JSON object.
- Output file: `/app/outputs/step_01_dispersion_check.json`
- Format: json
- Contract: A JSON object with four numeric fields: "omega_4sqrt6_pi_pi", "omega_0_0_0", "omega_4sqrt3_0_pi", "omega_4sqrt3_pi_0", each holding the computed float value of sigma.
- Scoring: scored by hidden verifier

### Step 2: Band-gap Green's function evaluation
- Role: scored (load-bearing)
- Action: For the same parameters μ=0.01, C=0.1, frequency ω=9.8, and forcing vector f=[−1,0,0]ᵀ (out-of-plane force only), compute the flexural displacement w(m,n) for all integer m,n in the range [-2,2] inclusive (25 points). Use the spectral Green's function W^F(k1,k2) = ζ(k1,k2)ζ(k2,k1) f_w / σ(ω,k1,k2) (with f_w=−1, f_θx=0, f_θy=0) and evaluate the inverse Fourier transform w(m,n) = (1/(4π²)) ∫₋π^π ∫₋π^π W^F(k1,k2) e^{i(k1 m + k2 n)} dk1 dk2 numerically. Output a JSON array of objects, each containing the integer indices m, n, and the computed float w.
- Output file: `/app/outputs/step_02_greens_function.json`
- Format: json
- Contract: A JSON array of 25 objects, each with integer fields "m" and "n" and a numeric field "w".
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dispersion_check.json`
- `/app/outputs/step_02_greens_function.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dispersion_check.json
- path: `/app/outputs/step_01_dispersion_check.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Values of the dispersion function σ at four invariant (ω,k1,k2) points. The checker recomputes σ using the same formula and parameters, then compares each value with absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `omega_4sqrt6_pi_pi`: number
    - `omega_0_0_0`: number
    - `omega_4sqrt3_0_pi`: number
    - `omega_4sqrt3_pi_0`: number

### step_02_greens_function.json
- path: `/app/outputs/step_02_greens_function.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Flexural displacement w(m,n) for the square lattice in the band gap (ω=9.8) under out-of-plane forcing f=[-1,0,0]ᵀ, evaluated at 25 integer grid points from (-2,-2) to (2,2). The checker recomputes each w value independently using numerical integration and compares with relative and absolute tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`:
      - `m`: integer
      - `n`: integer
      - `w`: number

Notes: Both outputs are derived from the specified formulas and parameters. The checker independently recomputes the expected values and scores closeness. No paper identity or gold values are present in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dispersion_check.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "omega_4sqrt6_pi_pi": "number",
          "omega_0_0_0": "number",
          "omega_4sqrt3_0_pi": "number",
          "omega_4sqrt3_pi_0": "number"
        }
      },
      "description": "Values of the dispersion function σ at four invariant (ω,k1,k2) points. The checker recomputes σ using the same formula and parameters, then compares each value with absolute tolerance."
    },
    {
      "file": "step_02_greens_function.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": {
            "m": "integer",
            "n": "integer",
            "w": "number"
          }
        }
      },
      "description": "Flexural displacement w(m,n) for the square lattice in the band gap (ω=9.8) under out-of-plane forcing f=[-1,0,0]ᵀ, evaluated at 25 integer grid points from (-2,-2) to (2,2). The checker recomputes each w value independently using numerical integration and compares with relative and absolute tolerances."
    }
  ],
  "notes": "Both outputs are derived from the specified formulas and parameters. The checker independently recomputes the expected values and scores closeness. No paper identity or gold values are present in the public contract."
}
```

## How you are scored
Each workflow step is evaluated independently by a hidden verifier. The verifier re-implements the same formulas, recomputes the quantities, and compares them against your submitted values using pre-set absolute and relative tolerances. The overall reward is a weighted sum of the scores of the two steps.

- Step 1 (Dispersion check): The verifier recomputes σ at the four invariant points and compares each with your submitted number using an absolute tolerance. You must compute these numbers yourself; the verifier independently recomputes the expected value and scores closeness.
- Step 2 (Green's function): The verifier recomputes W^F and the inverse Fourier integral independently using the same integration method and compares your reported w(m,n) values with relative or absolute tolerance.

You must run the actual computation; fabricating or hardcoding numbers that match the paper will not pass because the verifier re-derives the answer from the same problem specification, and small implementation differences (integration grid, numerical integration parameters) are expected and accounted for in the tolerances. The check is monotonic: a more accurate computation that matches the verifier's recomputation within tolerance earns full credit.
