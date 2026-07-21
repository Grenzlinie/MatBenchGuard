# Magnetic Phase Diagram of Two-Orbital Hubbard Model

## Problem background
The iron-pnictide superconductors contain FeAs planes whose parent compounds exhibit antiferromagnetic order at a wave vector (π,0) on a square lattice, a feature that is difficult to explain with simple models. Unlike the (π,π) order in cuprates, (π,0) order requires strong geometric frustration. This task focuses on a minimal two-band Hubbard model that accounts for the orbital degeneracy of the Fe 3d_{xz} and 3d_{yz} orbitals and the anisotropic hopping mediated by arsenic 4p orbitals. The model naturally introduces frustration through next-nearest-neighbour hoppings t₁ and t₂, controlled by the ratio t_A/t_B (the relative strength of σ-like and π-like hybridization).

At half-filling (two electrons per Fe site in the two degenerate bands), the interplay between on-site Coulomb interactions (intra-orbital U, inter-orbital U₁, Hund’s coupling J) and kinetic frustration determines which magnetic order is favoured. Using a mean-field treatment for collinear spin density wave order at Q = (π, π) and Q = (π, 0), one can compute the critical interaction strength needed to open a magnetic gap as a function of the frustration ratio t_A/t_B. Your task is to carry out this calculation and produce the corresponding phase diagram.

## Approach
You will work with a two-orbital Hubbard model on a two-dimensional square lattice. The hopping Hamiltonian includes nearest-neighbour (t) and two diagonal next-nearest-neighbour hoppings (t₁ for the (1,1) direction and t₂ for the (1,-1) direction) that act differently on the two orbitals. These hoppings are expressed in terms of the microscopic parameters t_A and t_B (the hybridization amplitudes between Fe 3d and As 4p orbitals) and the charge-transfer energy Δ. The frustration is captured by the ratio t_A/t_B; the corresponding effective hopping parameters t, t₁, t₂ follow from the relations t = 2 t_A t_B / Δ, t₁ = t_A² / Δ, t₂ = t_B² / Δ.

The on-site interaction includes intra-orbital Hubbard U, inter-orbital Hubbard U₁, and Hund’s rule coupling J. In the mean-field treatment, the relevant parameter for magnetic order is the renormalised interaction Ũ = U + J/2. The order parameter M describes a collinear spin density wave with ordering vector Q = (π, π) or Q = (π, 0). The chemical potential is fixed by the half-filling condition.

The numerical procedure consists of: (1) For a given t_A/t_B ratio, compute the band dispersion ξ_k for each orbital. (2) For a chosen ordering vector Q, set up the mean-field Hamiltonian and derive the self-consistent equation for the magnetic order parameter M. (3) Solve the self-consistent equation at low temperature to find the critical interaction strength Ũ_c where M becomes non-zero. (4) Repeat this for a range of frustration ratios t_A/t_B from 0.5 to 4, for both Q = (π, π) and Q = (π, 0). You will then record the critical values Ũ_c for both ordering vectors at each t_A/t_B ratio.

## Reproduction target
Compute the critical renormalised interaction strength Ũ_c for collinear antiferromagnetic order at wave vectors Q = (π, π) and Q = (π, 0) in the two-band Hubbard model at half-filling, as a function of the frustration ratio t_A/t_B over the range [0.5, 4]. Produce a CSV file (magnetic_phase_diagram.csv) with columns tA_over_tB, Uc_pipi, Uc_pi0, containing at least 10 rows covering the range including values near 1.0, 1.5, 2.0, 2.5, and 3.0. The CSV will be scored against reference values derived from the published mean-field calculation.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute mean-field magnetic phase diagram
- Role: scored (load-bearing)
- Action: Implement the two-band Hubbard model with on-site interactions (U, U1, J) and As-bridged hopping (t, t1, t2) on a square lattice. Perform mean-field decoupling for collinear antiferromagnetic order at wave vectors Q=(π,π) and Q=(π,0) at half-filling. Solve the self-consistent equation for the order parameter to find the critical renormalized interaction strength (Ũ = U + J/2) where the order parameter becomes non-zero, as a function of the frustration ratio tA/tB (or equivalently t1/t, t2/t) over the range 0.5 to 4. Record the critical values Ũc for both ordering vectors at multiple tA/tB ratios.
- Output file: `/app/outputs/magnetic_phase_diagram.csv`
- Format: csv
- Contract: Columns: tA_over_tB (float in [0.5, 4]), Uc_pipi (float >= 0), Uc_pi0 (float >= 0). At least 10 rows covering the range.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_phase_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_phase_diagram.csv
- path: `/app/outputs/magnetic_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean-field critical interaction strength for collinear magnetic orders in the two-band Hubbard model, used to check the stability crossover: (π,0) order becomes more stable than (π,π) order when tA/tB > 2.
- schema:
  - `type`: table
  - `required_columns`: `tA_over_tB`, `Uc_pipi`, `Uc_pi0`
  - `description`: Columns: tA_over_tB (float), Uc_pipi (float >= 0), Uc_pi0 (float >= 0). Values are the critical renormalized interaction strength Ũc = U + J/2 for antiferromagnetic order at (π,π) and (π,0).

Notes: The checker compares the agent's reported Uc_pipi and Uc_pi0 at selected tA/tB values (e.g., 1.0, 1.5, 2.0, 2.5, 3.0) to the paper's reference values with a relative tolerance of 20%, and verifies that the condition Uc_pi0 < Uc_pipi holds for tA/tB > 2. The agent must determine the critical Ũc self-consistently from the mean-field equations; copying a pre-computed table without solving the model will not pass the hidden tolerance and crossing check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tA_over_tB",
          "Uc_pipi",
          "Uc_pi0"
        ],
        "description": "Columns: tA_over_tB (float), Uc_pipi (float >= 0), Uc_pi0 (float >= 0). Values are the critical renormalized interaction strength Ũc = U + J/2 for antiferromagnetic order at (π,π) and (π,0)."
      },
      "description": "Mean-field critical interaction strength for collinear magnetic orders in the two-band Hubbard model, used to check the stability crossover: (π,0) order becomes more stable than (π,π) order when tA/tB > 2."
    }
  ],
  "notes": "The checker compares the agent's reported Uc_pipi and Uc_pi0 at selected tA/tB values (e.g., 1.0, 1.5, 2.0, 2.5, 3.0) to the paper's reference values with a relative tolerance of 20%, and verifies that the condition Uc_pi0 < Uc_pipi holds for tA/tB > 2. The agent must determine the critical Ũc self-consistently from the mean-field equations; copying a pre-computed table without solving the model will not pass the hidden tolerance and crossing check."
}
```

## How you are scored
Your submitted magnetic_phase_diagram.csv is evaluated by a hidden verifier that compares your computed critical interaction strengths to the published reference values. The comparison is performed at selected tA_over_tB points (including roughly 1.0, 1.5, 2.0, 2.5, 3.0) using interpolation if needed. The verifier checks whether your values lie within a relative tolerance of the reference and also verifies the correct relative stability of the two magnetic orders: specifically, for tA_over_tB > 2 the (π,0) critical strength must be lower than the (π,π) critical strength. Reporting numbers alone is not sufficient; the verifier expects that your CSV results from a proper numerical solution of the mean-field equations, and it applies a hidden tolerance that distinguishes a genuinely computed curve from a copied or guessed one.
