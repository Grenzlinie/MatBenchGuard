# Convergence of impurity model vertex function in Lanczos exact diagonalization

## Problem background
In strongly correlated electron systems, the two-dimensional half-filled Hubbard model exhibits a metal-insulator transition whose accurate theoretical description requires methods that go beyond dynamical mean-field theory (DMFT). The ladder dual fermion approximation (LDFA) is one such extension, where the local four-point vertex function of the impurity Anderson model plays the role of an effective interaction. Efficient computation of this vertex function is challenging with conventional exact diagonalization (ED) techniques. The present work introduces a new Lanczos-based ED algorithm that expresses the two-body Green’s function via resolvents, making it possible to obtain accurate vertex functions with manageable computational effort. A key ingredient of the algorithm is the treatment of the central resolvent using a finite set of reference energy points. The accuracy and convergence of the resulting vertex function with respect to the number of these reference points must be quantified to validate the method.

## Approach
The core idea is to compute the local four-point vertex function γ^(4) of the impurity Anderson model (IAM) solely from the model Hamiltonian using a hybrid Lanczos diagonalization procedure. The two-body Green’s function is expressed as a sum of terms each containing up to three resolvents. Low-energy eigenstates of the IAM Hamiltonian are obtained with high precision using the restart Lanczos method. The left and right resolvents are approximated by ordinary Lanczos runs starting from appropriate creation/annihilation-operator vectors. The central (bosonic) resolvent is treated with a band Lanczos technique: initial vectors are constructed from a set of reference energy points Ω_α that sample the relevant energy range, and the Lanczos basis is shared among several related resolvent terms. From the approximated resolvents the full two-body Green’s function and subsequently the reducible vertex function γ are assembled. The IAM parameters are fixed to U=4, β=5, μ=2, with N_b=7 bath sites having energies ε_b = [-6, -3, -1, 0, 1, 3, 6] and hybridizations V = [0.55, 0.9, 0.85, 0.6, 0.85, 0.9, 0.55]. The real part of the spin-antisymmetric vertex component Re γ_{ωω';Ω}^{↑↓↑↓} is evaluated at ω' = π/β and Ω = 4π/β for all fermionic Matsubara frequencies ω_n. This calculation is repeated for different numbers of reference energy points N_α = 2, 4, 6, 8, 10, with Ω_1 = 0, Ω_{N_α} = 5.12W, Ω_α = 0.02·2^(α-2)·W (α=2,…,N_α−1), where W = sqrt(U²+64t²) and t=1. For each N_α, the relative difference with respect to the N_α=10 reference is computed, providing a quantitative measure of convergence.

## Reproduction target
Implement the Lanczos ED algorithm for the two-body Green’s function and compute the vertex function Re γ_{ωω';Ω}^{↑↓↑↓} for the specified IAM parameters, ω' = π/β, Ω = 4π/β, over all fermionic Matsubara frequencies ω_n. Perform the computation for N_α = 2, 4, 6, 8, 10 reference energy points using the scheme defined above. For each N_α, calculate the frequency-resolved relative difference δγ(N_α, ω_n) = |γ(N_α) − γ(N_α=10)| / |γ(N_α=10)| and the mean relative difference across all frequencies. Write the complete results—frequency-by-frequency vertex values, reference values (N_α=10), relative differences, and summary rows with the mean relative difference per N_α—into a CSV file named vertex_convergence.csv placed in /app/outputs. The goal is to demonstrate that as N_α increases, the vertex function converges: the relative differences become small and decrease monotonically.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute vertex function convergence
- Role: scored (load-bearing)
- Action: Implement the Lanczos exact diagonalization algorithm for the two-body Green's function as described in the paper's Section IV and Appendix C. Use restart Lanczos to obtain low-energy eigenvectors, ordinary Lanczos for left/right resolvents, and band Lanczos with combined reference energy initial vectors for the central resolvent. Compute the impurity Anderson model with U=4, beta=5, mu=2, and N_b=7 bath sites with energies [-6, -3, -1, 0, 1, 3, 6] and hybridizations [0.55, 0.9, 0.85, 0.6, 0.85, 0.9, 0.55]. Calculate the real part of the vertex function gamma^{up down up down} at omega' = pi/beta, Omega = 4pi/beta for all fermionic Matsubara frequencies omega_n. Repeat for N_alpha = 2, 4, 6, 8, 10 reference energy points with scheme: Omega_1 = 0, Omega_{N_alpha} = 5.12*W, Omega_alpha = 0.02 * 2^(alpha-2) * W for alpha=2..N_alpha-1, where W = sqrt(U^2 + 64*t^2) with t=1. For each N_alpha, compute the relative difference delta_gamma(N_alpha, omega_n) = |gamma(N_alpha) - gamma(N_alpha=10)| / |gamma(N_alpha=10)|, and calculate the mean relative difference across all frequencies for each N_alpha. Write the full frequency-resolved table and summary rows to vertex_convergence.csv.
- Output file: `/app/outputs/vertex_convergence.csv`
- Format: csv
- Contract: Columns: N_alpha (int), omega_index (int), omega_value (float), gamma_re (float), gamma_re_ref (float), relative_difference (float). After all frequency rows, summary rows per N_alpha with omega_index='mean' and mean_relative_difference in the relative_difference column, and other columns empty or zero.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vertex_convergence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vertex_convergence.csv
- path: `/app/outputs/vertex_convergence.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The checker will extract the mean relative differences for N_alpha=4 and N_alpha=6, verify they are below specified accuracy thresholds, and confirm the mean relative difference decreases monotonically with increasing N_alpha.
- schema:
  - `type`: table
  - `required_columns`: `N_alpha`, `omega_index`, `omega_value`, `gamma_re`, `gamma_re_ref`, `relative_difference`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vertex_convergence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "N_alpha",
          "omega_index",
          "omega_value",
          "gamma_re",
          "gamma_re_ref",
          "relative_difference"
        ]
      },
      "description": "The checker will extract the mean relative differences for N_alpha=4 and N_alpha=6, verify they are below specified accuracy thresholds, and confirm the mean relative difference decreases monotonically with increasing N_alpha."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your vertex_convergence.csv. It first confirms that the file contains the required columns and includes both frequency-level rows and summary rows. The verifier then extracts the mean relative differences for each N_α and checks that the values for N_α=4 and N_α=6 lie below predetermined accuracy thresholds (which reflect the paper’s reported convergence behavior). It also verifies that the mean relative difference decreases monotonically from N_α=2 up to N_α=10. Additionally, the verifier may examine the overall shape of the vertex function to ensure it is physically reasonable. Your final reward is based on how well your submitted convergence metrics satisfy these checks; merely reporting numbers without the correct underlying computation will not pass.
