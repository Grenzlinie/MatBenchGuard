# Orbital occupancies, pairing eigenvalues, and magnetic crossover temperature from FLEX for the three-band CuO2 model

## Problem background
The high-temperature superconductivity of the cuprate oxides is believed to originate in the CuO₂ planes, which are often described by a three-band model that includes the Cu 3d_{x²−y²} orbital and the O 2p orbitals. Understanding how orbital structure, hybridization, and strong local Coulomb repulsion on copper sites combine to determine the occupancy of the different orbitals, the leading pairing symmetry, and the scale of antiferromagnetic correlations is an open computational problem. The fluctuation‑exchange (FLEX) approximation, a conserving Baym‑Kadanoff theory that incorporates the interaction of single‑particle excitations with magnetic, charge, and particle‑pair fluctuations, provides a self‑consistent framework for computing these quantities. The central task is to implement the FLEX approximation for the three‑band model and to produce the average orbital occupancies, the singlet pairing eigenvalues in the d_{x²−y²} and extended‑s channels, and the magnetic crossover temperature T_N for specific model parameter sets.

## Approach
We consider a three‑band CuO₂ Hamiltonian with nearest‑neighbor copper‑oxygen hopping t_pd, an on‑site Coulomb repulsion U_d on the copper sites, and an oxygen level splitting ε. The total hole occupancy ⟨n⟩ per unit cell is controlled by a chemical potential. The non‑interacting band structure (bonding, antibonding, and nonbonding) and the associated wave‑function coefficients are first computed from tight‑binding. The FLEX self‑energy Σ_d is then built as a functional of the dressed copper Green’s function G_d, using the diagrams that capture the coupling to magnetic, charge, and singlet‑pair fluctuations. This self‑energy is inserted into the Dyson equation for G_d, which together with the corresponding oxygen Green’s function and the self‑consistent determination of μ yields the re‑normalized propagators. From the converged Green’s functions, the orbital occupancies are obtained by summing over Matsubara frequencies with tail corrections. The irreducible particle‑hole and particle‑particle scattering kernels are constructed, and the leading eigenvalues in the antiferromagnetic magnetic channel and in the d_{x²−y²} and extended‑s singlet pairing channels are computed. The magnetic crossover temperature T_N is identified as the temperature where the antiferromagnetic eigenvalue reaches unity.

## Reproduction target
Produce three scored artifacts that fully characterise the FLEX solution of the three‑band model:

1. `occupancies.csv`: average orbital occupancies ⟨n_d⟩, ⟨n_p^h⟩, and ⟨n_p^n⟩ for the parameter set U_d/t_pd = 6, ε/t_pd = 2, ⟨n⟩ = 1, and for ⟨n⟩ varying from 0.8 to 1.2 in steps of 0.1 at the same U_d and ε.

2. `eigenvalues.csv`: the largest singlet pairing eigenvalues λ_{d_{x²−y²}} and λ_{extended‑s} for U_d/t_pd = 10, ε/t_pd = 2, ⟨n⟩ = 0.875 at the temperatures T/t_pd = 0.05, 0.1, 0.15, 0.2.

3. `TN.csv`: the magnetic crossover temperature T_N/t_pd for U_d/t_pd = 4, 6, 8, 10, 12, all with ε/t_pd = 2 and ⟨n⟩ = 1.

All computations must use the self‑consistent FLEX approximation with a finite k‑point mesh and a Matsubara frequency cutoff; the agent must handle the frequency summations, tail corrections, and eigenvalue projections autonomously.

## Assets

- numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Non-interacting band structure
- Role: process
- Action: Compute the tight-binding band dispersions E_k^+, E_k^-, E_k^0 and wavefunction coefficients alpha_k, beta_k for the three-band CuO2 model using the model parameters t_pd and epsilon.
- Evidence: none

### Step 2: FLEX self-consistent simulation
- Role: process
- Action: Solve the fluctuation-exchange (FLEX) equations self-consistently for the three-band CuO2 model. For each required parameter set (varying Ud, epsilon, filling, temperature), solve for the dressed Green's functions G_d(k,iomega_n) and G_p(k,iomega_n), the self-energy Sigma_d, and the chemical potential mu until convergence, using a finite k-point grid and Matsubara frequency cutoff. This step produces the converged Green's functions and self-energy needed for all subsequent analysis.
- Evidence: none

### Step 3: Average orbital occupancies
- Role: scored (load-bearing)
- Action: From the converged FLEX Green's functions, compute the orbital occupancies using the frequency summation with correction terms (the agent must derive the expressions from the method description). Produce a CSV file with rows for the parameter set Ud/tpd=6, epsilon/tpd=2, <n>=1 and for <n> varying from 0.8 to 1.2 in steps of 0.1. For each parameter set, report <n_d>, <n_p^h>, and <n_p^n>.
- Output file: `/app/outputs/occupancies.csv`
- Format: csv
- Contract: columns: param_set (string), n_d (float), n_p_h (float), n_p_n (float); rows for at least Ud/tpd=6, eps/tpd=2, <n>=1 and for <n> varying 0.8 to 1.2 step 0.1
- Scoring: scored by hidden verifier

### Step 4: Singlet pairing eigenvalues
- Role: scored
- Action: From the converged FLEX Green's functions and self-energy, build the irreducible particle-particle scattering kernel and compute the largest eigenvalues for the d_{x^2-y^2} and extended-s pairing channels via projection at each temperature (T/tpd = 0.05, 0.1, 0.15, 0.2) for parameters Ud/tpd=10, epsilon/tpd=2, <n>=0.875. Output a CSV with T/tpd, lambda_d, lambda_sstar.
- Output file: `/app/outputs/eigenvalues.csv`
- Format: csv
- Contract: columns: T_over_tpd (float), lambda_d (float), lambda_sstar (float); rows for at least T/tpd=0.05,0.1,0.15,0.2
- Scoring: scored by hidden verifier

### Step 5: Magnetic crossover temperature T_N
- Role: scored
- Action: For each Ud value (Ud/tpd = 4, 6, 8, 10, 12) with epsilon/tpd=2, <n>=1, compute the antiferromagnetic particle-hole eigenvalue as a function of temperature from the FLEX kernel. Determine the temperature T_N where the eigenvalue reaches 1 (interpolate if necessary). Output a CSV with Ud/tpd and TN/tpd.
- Output file: `/app/outputs/TN.csv`
- Format: csv
- Contract: columns: Ud_over_tpd (float), TN_over_tpd (float); rows for Ud/tpd = 4,6,8,10,12
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/occupancies.csv`
- `/app/outputs/eigenvalues.csv`
- `/app/outputs/TN.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### occupancies.csv
- path: `/app/outputs/occupancies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average orbital occupancies from FLEX. Checked against reference values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `param_set`, `n_d`, `n_p_h`, `n_p_n`
  - `units`: object

### eigenvalues.csv
- path: `/app/outputs/eigenvalues.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Singlet pairing eigenvalues for d-wave and extended-s. Values and inequality λ_d > λ_s* will be checked.
- schema:
  - `type`: table
  - `required_columns`: `T_over_tpd`, `lambda_d`, `lambda_sstar`
  - `units`: object

### TN.csv
- path: `/app/outputs/TN.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetic crossover temperature. Checked against reference and monotonic trend.
- schema:
  - `type`: table
  - `required_columns`: `Ud_over_tpd`, `TN_over_tpd`
  - `units`: object

Notes: The Wannier-state analysis and one-band model comparison are not required. Only the three-band results are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "occupancies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "param_set",
          "n_d",
          "n_p_h",
          "n_p_n"
        ],
        "units": {}
      },
      "description": "Average orbital occupancies from FLEX. Checked against reference values from the paper."
    },
    {
      "file": "eigenvalues.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_over_tpd",
          "lambda_d",
          "lambda_sstar"
        ],
        "units": {}
      },
      "description": "Singlet pairing eigenvalues for d-wave and extended-s. Values and inequality λ_d > λ_s* will be checked."
    },
    {
      "file": "TN.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ud_over_tpd",
          "TN_over_tpd"
        ],
        "units": {}
      },
      "description": "Magnetic crossover temperature. Checked against reference and monotonic trend."
    }
  ],
  "notes": "The Wannier-state analysis and one-band model comparison are not required. Only the three-band results are scored."
}
```

## How you are scored
A hidden verifier independently reads each output file and compares the submitted values against reference results. Separate, weighted scores are computed for the occupancies, the singlet eigenvalues, and the magnetic crossover temperature. The final reward is a combination of these weights. Reporting a plausible number is not enough; the verifier checks that the computed quantitites are consistent with the expected physical trends and numerical benchmarks, within hidden tolerances that account for legitimate implementation differences. The verifier also validates the required CSV column schema.
