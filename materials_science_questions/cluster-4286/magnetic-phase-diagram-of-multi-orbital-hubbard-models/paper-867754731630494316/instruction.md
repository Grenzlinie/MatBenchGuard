# Correlation Effects on Antiferromagnetism via Variational Monte Carlo

## Problem background
Iron pnictide high-temperature superconductors host a parent antiferromagnetic (AF) phase with ordering vector (π,0) and an ordered magnetic moment that is much smaller than what conventional Hartree-Fock (HF) calculations predict for a two-orbital Hubbard model when the Coulomb interaction is comparable to the bandwidth. Understanding how strong electronic correlations modify the magnetic ground state is therefore critical. The variational Monte Carlo (VMC) method with a Gutzwiller-projected wavefunction provides a way to capture local correlation effects beyond HF. This task investigates the magnitude of the ordered magnetic moment and the energy stabilization of the AF phase in the two-orbital Hubbard model using VMC, focusing on the half-filled 8×8 square lattice with realistic hopping parameters and interactions.

## Approach
The system is modelled by a two-orbital (d_zx, d_yz) Hubbard Hamiltonian on a square lattice. The kinetic part uses the hopping parameterisation of Raghu et al.: t1 = -t, t2 = 1.3t, t3 = t4 = -0.85t, corresponding to a bandwidth W = 12t. The on-site interactions consist of intra-orbital Coulomb U, inter-orbital Coulomb U', Hund’s exchange J and pair-hopping J', related by U' = U − 2J and J' = J (with J = 0.1U for the target calculations).

The trial wavefunction is a Gutzwiller-projected Slater determinant. The Gutzwiller projector P_G = ∏_iγ [1 − (1 − g_γ) |iγ⟩⟨iγ|] uses 16 on-site variational parameters g_γ that control the weight of each local electron configuration. The Slater determinant |Φ⟩ is constructed from the eigenstates of a 4×4 one-body Hamiltonian that mixes the k and k+Q sectors (Q=(π,0)) through gap parameters. For the paramagnetic state, all gap parameters are set to zero and only the Gutzwiller parameters are optimised. For the antiferromagnetic state, the orbital gap Δ_o, spin gap Δ_sQ, and spin-orbital gap Δ_soQ are additionally varied (other gap parameters are kept zero). The variational energy is evaluated by Monte Carlo sampling and the parameters are optimised to find the lowest-energy configuration.

All calculations are performed on an 8×8 square lattice with antiperiodic boundary conditions in both directions. After optimising the wavefunction at each U/t value (7, 8, 9, 10) with J = 0.1U, we compute two quantities: (a) the ordered magnetic moment per site m_sQ, defined as the staggered spin density at wavevector Q=(π,0): m_sQ = (1/N) Σ_iτ e^{i Q·r_i} ⟨n_{iτ↑} − n_{iτ↓}⟩; and (b) the energy per site difference E_diff = E_AF − E_para (in units of t).

## Reproduction target
For the two-orbital Hubbard model at half-filling with hopping parameters t1=-t, t2=1.3t, t3=t4=-0.85t, and J = 0.1U, use variational Monte Carlo to optimise the Gutzwiller-projected wavefunction (16 Gutzwiller parameters plus, for the AF state, the gaps Δ_o, Δ_sQ, Δ_soQ) on an 8×8 lattice with antiperiodic boundary conditions. Carry out the optimisation for paramagnetic and antiferromagnetic states at each of the following U/t values: 7, 8, 9, 10. Compute:
- the ordered magnetic moment per site m_sQ (definition above)
- the energy per site difference E_diff = E_AF – E_para (units of t).
Write the results to a CSV file at `/app/outputs/results_step_03.csv`. The file must be a UTF-8 CSV with header `U_t,m_sQ,E_diff`, where U_t is the dimensionless U/t ratio, m_sQ is dimensionless, and E_diff is dimensionless (energy per site in units of t). Provide one row for each U/t value.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Setup Hamiltonian and VMC framework
- Role: process
- Action: Implement the two-orbital Hubbard model with the hopping parameters t1=-t, t2=1.3t, t3=t4=-0.85t on an 8×8 square lattice with antiperiodic boundary conditions. Construct the Gutzwiller-projected trial wavefunction with 16 on-site variational parameters and a Hartree-Fock-type Slater determinant that couples k and k+Q sectors (Q=(π,0)). Implement a Monte Carlo energy evaluator and a variational parameter optimizer.
- Evidence: none

### Step 2: Paramagnetic state optimization
- Role: process
- Action: For each U/t = 7, 8, 9, 10 with J = 0.1U, optimize the Gutzwiller parameters (all gap parameters set to zero) to minimize the variational energy via Monte Carlo sampling. Record the converged paramagnetic energy per site for later use.
- Evidence: none

### Step 3: Antiferromagnetic VMC optimization and scored results
- Role: scored (load-bearing)
- Action: For the same U/t values, optimize the Gutzwiller parameters together with the antiferromagnetic gap parameters Δ_o, Δ_sQ, Δ_soQ (other gaps zero) to minimize the variational energy. Compute the ordered magnetic moment m_sQ and the antiferromagnetic energy E_AF. Compute the energy difference E_diff = E_AF - E_para. Write results to results_step_03.csv with columns U_t, m_sQ, E_diff for U/t=7,8,9,10.
- Output file: `/app/outputs/results_step_03.csv`
- Format: csv
- Contract: UTF-8 CSV with header: U_t,m_sQ,E_diff. U_t dimensionless U/t; m_sQ ordered magnetic moment per site (dimensionless); E_diff energy per site in units of t (E_AF - E_para).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_step_03.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_step_03.csv
- path: `/app/outputs/results_step_03.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ordered magnetic moment and energy difference between antiferromagnetic and paramagnetic states for U/t = 7, 8, 9, 10.
- schema:
  - `type`: table
  - `required_columns`: `U_t`, `m_sQ`, `E_diff`
  - `units`:
    - `U_t`: dimensionless (U/t)
    - `m_sQ`: dimensionless (magnetic moment per site)
    - `E_diff`: units of t (energy per site)

Notes: The hidden checker will compare the reported values against the paper's own reference numbers with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_step_03.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U_t",
          "m_sQ",
          "E_diff"
        ],
        "units": {
          "U_t": "dimensionless (U/t)",
          "m_sQ": "dimensionless (magnetic moment per site)",
          "E_diff": "units of t (energy per site)"
        }
      },
      "description": "Ordered magnetic moment and energy difference between antiferromagnetic and paramagnetic states for U/t = 7, 8, 9, 10."
    }
  ],
  "notes": "The hidden checker will compare the reported values against the paper's own reference numbers with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will examine your submitted `/app/outputs/results_step_03.csv`. It will:
1. Validate the CSV format and the required columns.
2. Compare your reported m_sQ and E_diff at each of the four U/t points against a hidden reference (the paper’s own published numbers, with allowance for statistical noise and implementation-dependent fluctuations).
3. Check that E_diff is negative for U/t = 8, 9, 10 (indicating that the AF state is energetically favoured).
The verifier computes a score per quantity and per U/t; the overall reward is a weighted combination of these checks. To earn full credit, you must faithfully implement the model and optimisation procedure described in the workflow steps – submitting arbitrary numbers without performing the computation will not lead to values that match the hidden gold within the required tolerance.
