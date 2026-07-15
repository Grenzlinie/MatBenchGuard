# MD defect migration rate calculation for rigid-ion CoO

## Problem background
Point defects in solids control atomic transport, and their migration rates are central to understanding diffusion. The standard theory due to Vineyard expresses the hopping rate of a defect using an Arrhenius form with a frequency prefactor derived from harmonic vibrational frequencies at the stable site and at the saddle point, and it assumes every saddle-plane crossing results in a successful jump. In many materials these harmonic and dynamical approximations are questionable, and a more direct approach is needed that does not rely on them. Molecular dynamics can, in principle, compute migration rates from first principles by simulating the defect dynamics explicitly, but spontaneous hopping is too rare to observe directly at temperatures where the migration barrier is large compared to thermal energy. This task asks you to implement a molecular dynamics method that circumvents the rarity problem: using constrained dynamics, umbrella sampling, and stochastically initiated hopping trajectories, you will compute the saddle-plane probability, the transmission coefficient, the effective hopping rate, and the frequency prefactor for anion vacancy migration in a rigid-ion model of cobalt oxide — all without invoking Vineyard theory.

## Approach
You will treat the defect migration as a transition between two adjacent anion sites in the rock-salt lattice. A reaction coordinate ξ is defined from the positions of the hopping ion and its two neighbouring cations, ensuring translational invariance. The total rate at which the system crosses the saddle plane (ξ=0) in thermal equilibrium is given exactly by the statistical mechanics expression Γ₀ = 2 √(k_B T / (2πμ)) P(0), where P(0) is the equilibrium probability density of ξ at the saddle plane and μ is an effective mass determined by the coefficients of the reaction coordinate. To obtain P(0), you will first compute the minimum-energy profile ΔE(ξ) along the migration path using damped constrained molecular dynamics. Then, using umbrella sampling with an external bias potential equal to −ΔE(ξ), you will run unconstrained MD at each temperature, accumulate a biased histogram of ξ, and invert the biasing to extract the unbiased P(ξ) and its value at ξ=0. The fraction of saddle-plane crossings that correspond to a successful jump — the transmission coefficient ⟨S⟩ — will be obtained from an ensemble of trajectories initiated at the saddle plane: you will perform constrained MD at ξ=0 to generate an equilibrium ensemble of configurations, assign each a random reaction velocity drawn from the appropriate crossing distribution, release the constraint, and integrate the unconstrained equations of motion to determine the outcome. The effective hopping rate follows as Γ = ⟨S⟩ Γ₀, and the frequency prefactor ν̄ is extracted via the relation Γ = ν̄ exp(−ΔE_mig / (k_B T)). The method will be applied to a rigid-ion model of CoO whose interatomic interactions are given by Born-Mayer-Huggins potentials; the parameters are listed in the assets section below. All stages will be repeated at four temperatures: 995 K, 1368 K, 1520 K, and 1760 K.

## Reproduction target
Using a molecular dynamics implementation of the procedures outlined above, compute for the oxygen vacancy in the rigid-ion CoO model the following quantities at each of the four temperatures: the saddle-plane probability density P(0) (units Å⁻¹), the transmission coefficient ⟨S⟩ (dimensionless), the effective hopping rate Γ (units s⁻¹), and the frequency prefactor ν̄ (units 10¹² s⁻¹). The final numerical results must be written to `/app/outputs/migration_results.csv`. Additionally, the per-temperature P(0) values must be recorded in `/app/outputs/saddle_plane_probabilities.csv` and the per-temperature ⟨S⟩ values in `/app/outputs/transmission_coefficients.csv`. The intermediate relaxed energy profile ΔE(ξ) may optionally be saved to `/app/outputs/energy_profile.csv`. The MD simulations must be performed with the rigid-ion potential parameters given in the assets section and with the reaction coordinate defined as ξ = √(2/3) (r₁ − (r₂ + r₃)/2)·n, where ions 1, 2, and 3 are the hopping anion and its two neighbouring cations, and n is the unit hop direction. The goal is to obtain these quantities from first-principles MD; simply quoting numbers from the literature without running the simulation is not acceptable.

## Assets

- Rigid-ion potential parameters for CoO
- Molecular dynamics simulation software

## Workflow steps

### Step 1: Compute migration energy profile ΔE(ξ)
- Role: process
- Action: Use damped constrained molecular dynamics with the reaction coordinate ξ (defined in terms of the hopping anion and its two cation neighbors) to relax the system at a set of fixed ξ values spanning the stable-site to stable-site range. The damped dynamics removes kinetic energy, converging to the minimum energy configuration for each ξ. Record the relaxed energy ΔE(ξ) with zero at the regular lattice site.
- Evidence: `/app/outputs/energy_profile.csv`

### Step 2: Umbrella-sampling MD for saddle-plane probability P(0)
- Role: scored (load-bearing)
- Action: Run unconstrained molecular dynamics with an external potential equal to −ΔE(ξ) (using the profile from step1) at each of the four temperatures (995, 1368, 1520, 1760 K). Accumulate a histogram of ξ to obtain the biased distribution P'(ξ). Invert the umbrella biasing to recover the unbiased probability distribution P(ξ) and extract the value P(ξ=0) (units Å⁻¹). Record the results per temperature.
- Output file: `/app/outputs/saddle_plane_probabilities.csv`
- Format: csv
- Contract: T (K), P0 (Å⁻¹)
- Scoring: scored by hidden verifier

### Step 3: Constrained MD and stochastic hopping for transmission coefficient ⟨S⟩
- Role: scored (load-bearing)
- Action: Perform constrained molecular dynamics at the saddle plane ξ=0 to generate an equilibrium ensemble of configurations at each temperature. For each configuration, assign a random reaction velocity drawn from the crossing distribution, release the constraint, and integrate the unconstrained equations of motion. Classify each trajectory as successful or unsuccessful based on whether the system ends in the product well. Compute the transmission coefficient ⟨S⟩ as the plateau value of the correlation function (effectively the fraction of successful crossings). Report ⟨S⟩ for each temperature.
- Output file: `/app/outputs/transmission_coefficients.csv`
- Format: csv
- Contract: T (K), S (dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Calculate effective hopping rate and frequency prefactor
- Role: scored (load-bearing)
- Action: From P(0) (step2) and ⟨S⟩ (step3), compute the total crossing rate Γ₀ = 2 √(k_B T / (2πμ)) P(0), where μ is the effective mass determined by the reaction coordinate coefficients. Then effective hopping rate Γ = ⟨S⟩ Γ₀. Using the migration energy ΔE_mig = ΔE(ξ=0) from step1, extract the frequency prefactor ν̄ = Γ exp(ΔE_mig / (k_B T)). Assemble all quantities into the final migration_results.csv.
- Output file: `/app/outputs/migration_results.csv`
- Format: csv
- Contract: T, P_0_Angstrom_inv, transmission_coeff, Gamma_per_s, nu_bar_1e12_per_s
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/saddle_plane_probabilities.csv`
- `/app/outputs/transmission_coefficients.csv`
- `/app/outputs/migration_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### saddle_plane_probabilities.csv
- path: `/app/outputs/saddle_plane_probabilities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Saddle-plane probability P(0) for each temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `P0`
  - `units`:
    - `T`: K
    - `P0`: Å⁻¹

### transmission_coefficients.csv
- path: `/app/outputs/transmission_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transmission coefficient ⟨S⟩ for each temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `S`
  - `units`:
    - `T`: K
    - `S`: dimensionless

### migration_results.csv
- path: `/app/outputs/migration_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final migration quantities: saddle-plane probability, transmission coefficient, effective hopping rate, and frequency prefactor for each temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `P_0_Angstrom_inv`, `transmission_coeff`, `Gamma_per_s`, `nu_bar_1e12_per_s`
  - `units`:
    - `T`: K
    - `P_0_Angstrom_inv`: Å⁻¹
    - `transmission_coeff`: dimensionless
    - `Gamma_per_s`: s⁻¹
    - `nu_bar_1e12_per_s`: 10¹² s⁻¹

Notes: The checker will compare these values to hidden reference values (paper Table 2) with generous relative tolerances (P0 ±35%, S ±40%, Γ and ν̄ ±50%). Internal consistency (recomputing Γ from P0, S, and the known pre-factor) may also be verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "saddle_plane_probabilities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P0"
        ],
        "units": {
          "T": "K",
          "P0": "Å⁻¹"
        }
      },
      "description": "Saddle-plane probability P(0) for each temperature."
    },
    {
      "file": "transmission_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "S"
        ],
        "units": {
          "T": "K",
          "S": "dimensionless"
        }
      },
      "description": "Transmission coefficient ⟨S⟩ for each temperature."
    },
    {
      "file": "migration_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P_0_Angstrom_inv",
          "transmission_coeff",
          "Gamma_per_s",
          "nu_bar_1e12_per_s"
        ],
        "units": {
          "T": "K",
          "P_0_Angstrom_inv": "Å⁻¹",
          "transmission_coeff": "dimensionless",
          "Gamma_per_s": "s⁻¹",
          "nu_bar_1e12_per_s": "10¹² s⁻¹"
        }
      },
      "description": "Final migration quantities: saddle-plane probability, transmission coefficient, effective hopping rate, and frequency prefactor for each temperature."
    }
  ],
  "notes": "The checker will compare these values to hidden reference values (paper Table 2) with generous relative tolerances (P0 ±35%, S ±40%, Γ and ν̄ ±50%). Internal consistency (recomputing Γ from P0, S, and the known pre-factor) may also be verified."
}
```

## How you are scored
A hidden verifier inspects your submitted artifacts independently. The primary scoring comes from three load-bearing CSV files: `saddle_plane_probabilities.csv`, `transmission_coefficients.csv`, and `migration_results.csv`. For each file, the checker reads the reported values and compares them to the reference values obtained from the paper's reported results. Because MD simulations with different implementations, random seeds, and numerical details produce some spread, the comparison uses generous relative tolerance windows — you do not need to match the paper's numbers exactly, but your results must fall within those windows. In addition, the verifier performs an internal consistency check: it recomputes the effective hopping rate Γ from your reported P(0) and ⟨S⟩ using the known expression for Γ₀ and verifies that the recomputed Γ matches your reported Γ within a tight tolerance. The overall reward is a weighted combination of the scores from the three scored artifacts, with the main `migration_results.csv` carrying the largest share. Simply hardcoding the paper's reported numbers without genuinely performing the molecular dynamics simulation will almost certainly fail the consistency check and will not be accepted.
