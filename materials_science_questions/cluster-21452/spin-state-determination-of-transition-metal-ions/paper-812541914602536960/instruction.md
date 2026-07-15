# Mean-Field Simulation of Cooperative Jahn-Teller Spin Crossover in Co(II) Compounds

## Problem background
Octahedral Co(II) complexes exhibit spin crossover (SCO) between low-spin (²E) and high-spin (⁴T₁) states. Unlike Fe(II) SCO, the low-spin state is subject to a Jahn–Teller effect that couples to tetragonal lattice distortions, competing with the cooperative electron-deformational interaction that drives the transition. This interplay controls the temperature dependence of the magnetic susceptibility product χT. The task is to compute χT (in cm³ K mol⁻¹) as a function of temperature for three [Co(pyterpy)₂]-based compounds, using a microscopic mean-field model that includes both full-symmetric and Jahn–Teller cooperative interactions.

## Approach
Implement a mean-field theory of cooperative Jahn–Teller-driven spin crossover. The electronic Hamiltonian includes:

- A fictitious angular momentum L=1 representation (T–P isomorphism) for spin–orbit coupling within the ⁴T₁ high-spin state (factor −3/2, coupling constant λ).
- A low-symmetry crystal-field splitting Δ for the low-spin ²E orbital doublet.
- Zeeman interaction with g₀=2.0 for both spin configurations and an orbital contribution for the high-spin state.
- An effective energy gap Δ_hl between the centres of gravity of the low-spin and high-spin multiplets.

Vibrational contributions from 15 normal modes are included via average frequencies ℏω_ls and ℏω_hs (with an implicit frequency factor that scales the entropy difference).

Cooperative interactions arise from coupling to two spontaneous lattice strains: a fully symmetric strain ε₁ (interaction constant v₁) and a tetragonal E_u strain ε₂ (interaction constant v₂ for the low-spin state). In the mean-field (infinite-range) approximation these yield the molecular-field terms

  H_st = −( Δ_hl/2 + J₁ τ̄ ) τ − J₂ Ī₂ I₂ ,

where τ and I₂ are electronic operators (τ = +1 for high-spin, −1 for low-spin; I₂ = ±1 for the two components of the ²E doublet).

At each temperature the order parameters τ̄ = ⟨τ⟩ and Ī₂ = ⟨I₂⟩ are determined self-consistently from the Boltzmann (thermal equilibrium) density matrix.

The magnetic susceptibility product is obtained from the squared magnetic moment averaged over the thermally populated electronic states:

  χT = (N_A μ_B² / 3 k_B T) ⟨μ²⟩ ,

using the eigenstates of the total Hamiltonian (electronic + Zeeman + molecular-field + vibrational).

The following fixed model parameters are provided:

- λ = −180 cm⁻¹ (spin–orbit constant)
- κ = 0.8 (orbital reduction factor)
- ℏω_ls = 105 cm⁻¹, ℏω_hs = 95 cm⁻¹ (average vibrational frequencies; the quantum number of modes n=15 is implicitly accounted for).
- g₀ = 2.0

Compound-specific parameters:

**Compound 1** ([Co(pyterpy)₂](PF₆)₂):
  J₁ = 24.4 cm⁻¹, J₂ = 132 cm⁻¹, Δ_hl = 885 cm⁻¹, Δ = −300 cm⁻¹, y_hs = 20.4 %

**Compound 2** ([Co(pyterpy)₂](TCNQ)₂·DMF·MeOH):
  J₁ = 18.6 cm⁻¹, J₂ = 100.7 cm⁻¹, Δ_hl = 1264 cm⁻¹, Δ = −300 cm⁻¹, y_hs = 4.0 %

**Compound 3** ([Co(pyterpy)₂](TCNQ)₂·MeCN·MeOH):
  J₁ = 18.6 cm⁻¹, J₂ = 100.7 cm⁻¹, Δ_hl = 894 cm⁻¹, Δ = −300 cm⁻¹, y_hs = 1.8 %

The fraction y_hs of complexes is permanently high-spin; the remaining (1−y_hs) fraction participates in the spin transition and is treated with the mean-field model. The bulk magnetic response is the weighted sum of both contributions.

## Reproduction target
Compute, for each of the three compounds (identifier strings "1", "2", "3"), the χT product (cm³ K mol⁻¹) at every temperature from 50 K to 350 K inclusive, in steps of 5 K (i.e., temperatures 50, 55, 60, …, 350 K). Output the results as a single CSV file with no header row, containing exactly three columns: compound (string), T (float, K), χT (float, cm³ K mol⁻¹), one row per compound per temperature.

## Assets
The simulation can be performed with standard scientific Python packages. You will need:
- numpy (for numerical arrays and linear algebra)
- scipy (for matrix diagonalization and root-finding)

No external datasets, supplementary files, or proprietary software are required. Install the packages yourself inside the sandbox (the recommended mirror is `https://pypi.tuna.tsinghua.edu.cn/simple`).

## Workflow steps

### Step 1: Compute χT for three Co(II) compounds
- Role: scored
- Action: Implement the mean-field spin crossover model: construct the electronic Hamiltonians (fully symmetric strain coupling, tetragonal Jahn-Teller coupling, spin-orbit coupling, Zeeman interaction, and electron-vibrational terms) using the provided parameter values. For each compound (1, 2, 3) and for each temperature from 50 K to 350 K in steps of 5 K, solve the self-consistent equations for the order parameters τ̄ and Ī₂, compute the magnetic susceptibility product χT via the Van Vleck formula, and record the χT value (cm³ K mol⁻¹).
- Output file: `/app/outputs/step_01_chiT_values.csv`
- Format: csv
- Contract: Include a header row with columns compound, T, chiT. Three columns in strict order: column 1 = compound identifier (string '1', '2', or '3'), column 2 = temperature T (float, in Kelvin), column 3 = χT product (float, in cm³ K mol⁻¹). One row per compound per temperature step.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_chiT_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_chiT_values.csv
- path: `/app/outputs/step_01_chiT_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed χT product for compounds 1, 2, and 3 as a function of temperature over 50–350 K in 5 K steps. The hidden checker compares selected temperature points against a digitized reference curve with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `T`, `chiT`
  - `units`:
    - `T`: K
    - `chiT`: cm³ K mol⁻¹

Notes: All model parameters required for the simulation (J₁, J₂, Δ_hl, Δ, y_hs, λ, κ, ω_hs, ω_ls, elastic constants, etc.) are supplied directly in the instruction. Only the χT curves are scored; the order parameters and hs-fraction are not required for verification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_chiT_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "T",
          "chiT"
        ],
        "units": {
          "T": "K",
          "chiT": "cm³ K mol⁻¹"
        }
      },
      "description": "Computed χT product for compounds 1, 2, and 3 as a function of temperature over 50–350 K in 5 K steps. The hidden checker compares selected temperature points against a digitized reference curve with tolerance."
    }
  ],
  "notes": "All model parameters required for the simulation (J₁, J₂, Δ_hl, Δ, y_hs, λ, κ, ω_hs, ω_ls, elastic constants, etc.) are supplied directly in the instruction. Only the χT curves are scored; the order parameters and hs-fraction are not required for verification."
}
```

## How you are scored
A hidden verifier reads your `step_01_chiT_values.csv` and extracts the χT values at a secret set of sampling temperatures for each compound. These values are compared to the correct reference χT values (computed by the verifier’s own implementation of the same model with the same parameters). The final reward is the fraction of compared temperature–compound points where your χT falls within an acceptable tolerance of the reference. Higher agreement yields a higher score. Simply reporting a number is not sufficient; you must implement the model correctly.
