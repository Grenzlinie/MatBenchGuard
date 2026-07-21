# Reproduce bond-order parameters for circulating-current states in extended Hubbard model

## Problem background
The aim is to investigate circulating-current (flux) phases that may arise in the extended Hubbard model relevant to cuprate superconductors. Two such phases are of interest: the charge-flux (CF) phase, where spin-up and spin-down electrons carry currents in the same direction, and the spin-flux (SF) phase, where the two spin species carry opposite currents. The key quantities characterising these phases are the bond-order parameters, whose real part (T) represents the bond kinetic energy and whose imaginary part (I) corresponds to the bond current. Understanding how T and I depend on doping, interaction strength, ring-exchange coupling, and the projection of doubly-occupied sites (simulating strong electronic correlations) provides insight into the competitiveness of flux states in strongly correlated systems.

## Approach
Use a real-space Hartree-Fock approximation (HFA) on a 12×12 square lattice with periodic boundary conditions. The Hamiltonian is an extended single-band Hubbard model with nearest-neighbour hopping t=1, on-site Coulomb repulsion U, superexchange J, intersite Coulomb V, and a four-spin ring-exchange interaction K. The Hamiltonian is decoupled into single-particle terms by introducing expectation values for site charge n_i, site magnetic moment S_i, and bond-order parameter s_{ijσ} = ⟨c_iσ† c_jσ⟩. The specific decouplings are:

- For H_U: replace n_i↑ n_i↓ → ⟨n_i↑⟩ n_i↓ + n_i↑ ⟨n_i↓⟩ − ⟨c_i↓† c_i↑⟩ c_i↑† c_i↓ − ⟨c_i↑† c_i↓⟩ c_i↓† c_i↑, plus constant terms.

- For H_J and H_V: let g_{ijσ} = s_{ijσ} + ½ s_{ij σ̄} (σ̄ opposite spin). Then
  H_J ≃ −½ J Σ_{⟨ij⟩,σ} (g_{ji σ̄} c_iσ† c_jσ + g_{ij σ̄} c_jσ† c_iσ)
       + ½ J Σ_{⟨ij⟩,σ} (λ_σ S_i^z c_jσ† c_jσ + λ_σ S_j^z c_iσ† c_iσ)
       + ½ J Σ_{⟨ij⟩,σ} [(S_i^x − i λ_σ S_i^y) c_jσ† c_i σ̄ + (S_j^x − i λ_σ S_j^y) c_iσ† c_i σ̄],
  with λ↑=1, λ↓=−1.
  H_V ≃ V Σ_{⟨ij⟩,σ} (n_i c_jσ† c_jσ + n_j c_iσ† c_iσ) − V Σ_{⟨ij⟩,σ} (s_{jiσ} c_iσ† c_jσ + s_{ijσ} c_jσ† c_iσ).

- For H_K: the decoupling is similar to H_J but each term is multiplied by the plaquette spin-spin correlation function ⟨S_k·S_l⟩, which itself is computed self-consistently as ⟨S_k⟩⟨S_l⟩ − ½ (s_{kl↑} s_{lk↓} + s_{kl↓} s_{lk↑}) − ¼ (|s_{kl↑}|^2 + |s_{kl↓}|^2).

Starting from an initial guess for the order parameters, the Hartree-Fock Hamiltonian matrix (2N × 2N, N=144 sites) is diagonalised at each iteration. New expectation values are recomputed from the occupied eigenstates and the guess is updated until self-consistency is reached.

For the strongly-correlated regime, the effect of projecting out double site occupancy is approximated via Gutzwiller factors. First, a reference Hartree-Fock calculation is performed for the pure Hubbard model (only t and U=12t) to obtain the average double occupancy d₀(n) for a range of electron fillings n. Then, for a given target double occupancy d (full projection corresponds to d=0), the Gutzwiller factors g_t, g_J, g_V are computed from d₀(n) using the formulas given in the model description. These factors renormalise the hopping and interaction terms in an effective Hamiltonian without the on-site U, allowing a Hartree-Fock treatment of the projected model.

## Reproduction target
The task is to implement the Hartree-Fock solver described above and to self-consistently compute the bond-order parameters s_{ijσ} for the extended Hubbard model on the 12×12 cluster. From each converged state extract, for a chosen bond direction and one spin component, the real part T = Re s_{ijσ} and the imaginary part I = Im s_{ijσ}. These quantities must be computed for the following four separate studies, with results saved to the corresponding output files:

1. Doping dependence of the unprojected CF (J>0) and SF (J<0) phases at fixed U=|J|=4V=4t for hole dopings x = 0, 0.028, 0.056, 0.083, 0.111, 0.139, 0.167, 0.194.
2. Interaction-strength dependence at fixed doping x=0.028, with |J|/U=4V/U=1, scanning U/t = 0,1,2,3,4,5,6,7,8 for both CF and SF phases.
3. Ring-exchange dependence at doping x=0.083, fixed U=|J|=4V=4t, where the ring-exchange coupling K/t is varied from -1.0 to +1.0 in steps of 0.25, recording only the bond current I for CF and SF phases.
4. Doping dependence of the fully projected CF phase using the reference double occupancy d₀(n) from the preliminary Hubbard-model calculation. The same doping values as in (1) must be used, and the effective Hamiltonian has no on-site U but renormalised hopping and interaction strengths computed from the Gutzwiller factors for d=0. Record T and I.

For each study the required output CSV file, its columns, and the file path under /app/outputs are specified in the workflow steps below. Producing numerically accurate T and I values that capture the reported behaviour of the flux phases—including how the currents evolve with doping and interaction strength, and how ring exchange and strong correlations modify them—constitutes the reproduction target.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute reference double occupancy d0(n) for Hubbard model (U=12)
- Role: process
- Action: Run unrestricted Hartree-Fock on the single-band Hubbard model (only t, U=12t) on a 12×12 periodic cluster for a range of electron fillings n from 0.8 to 1.0 (hole doping x = 1-n). Self-consistently compute the average double occupancy d0(n) = ⟨n_i↑ n_i↓⟩ for each filling and save the mapping n → d0.
- Evidence: `/app/outputs/d0_vs_doping.csv`

### Step 2: Unprojected HFA: doping dependence of CF and SF phases
- Role: scored
- Action: Implement self-consistent Hartree-Fock decoupling for the extended Hubbard model (t=1, t'=0, J, V, U) on a 12×12 periodic cluster. For parameters U=|J|=4V=4t, find converged charge-flux (CF, J>0) and spin-flux (SF, J<0) solutions at hole doping x = 0, 0.028, 0.056, 0.083, 0.111, 0.139, 0.167, 0.194. For each converged state extract the real (T) and imaginary (I) parts of the bond-order parameter s_{ijσ} for one representative bond direction and one spin species.
- Output file: `/app/outputs/step_01_cf_sf_doping.csv`
- Format: csv
- Contract: Columns: phase (string, 'CF' or 'SF'), doping_x (float), T (float), I (float)
- Scoring: scored by hidden verifier

### Step 3: Unprojected HFA: interaction strength dependence of CF and SF phases
- Role: scored
- Action: Using the same HFA solver, fix doping at x=0.028 and vary interaction strength. Set ratios |J|/U = 4V/U = 1 and scan U/t = 0, 1, 2, 3, 4, 5, 6, 7, 8 (t=1). For each U find self-consistent CF and SF solutions and record T and I per bond per spin species.
- Output file: `/app/outputs/step_02_cf_sf_interaction.csv`
- Format: csv
- Contract: Columns: phase (string, 'CF' or 'SF'), U_over_t (float), T (float), I (float)
- Scoring: scored by hidden verifier

### Step 4: Unprojected HFA: ring-exchange effect on flux-phase currents
- Role: scored
- Action: Augment the HFA solver with the ring-exchange decoupling. Run calculations for CF and SF phases at doping x=0.083 with fixed U=|J|=4V=4t. Vary the ring-exchange coupling K/t from -1.0 to +1.0 in steps of 0.25. For each converged solution extract the bond current I (Im s_{ijσ}) per spin species.
- Output file: `/app/outputs/step_03_ring_exchange.csv`
- Format: csv
- Contract: Columns: phase (string, 'CF' or 'SF'), K_over_t (float), I (float)
- Scoring: scored by hidden verifier

### Step 5: Projected HFA: doping dependence of the CF phase with Gutzwiller factors
- Role: scored (load-bearing)
- Action: Using the d0(n) function obtained in step_d0, construct Gutzwiller projection factors g_t, g_J, g_V for full projection. Build the effective Hamiltonian without on-site U but with renormalized hopping and interactions. Run HFA self-consistently on the 12×12 cluster for the CF phase at the same doping values as in step_01. Extract T and I per bond per spin.
- Output file: `/app/outputs/step_04_projected_cf_doping.csv`
- Format: csv
- Contract: Columns: doping_x (float), T (float), I (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_cf_sf_doping.csv`
- `/app/outputs/step_02_cf_sf_interaction.csv`
- `/app/outputs/step_03_ring_exchange.csv`
- `/app/outputs/step_04_projected_cf_doping.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_cf_sf_doping.csv
- path: `/app/outputs/step_01_cf_sf_doping.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Doping dependence of bond kinetic energy T and bond current I per spin for charge-flux (CF) and spin-flux (SF) phases. Each row is one phase at one doping value.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `doping_x`, `T`, `I`
  - `units`: object

### step_02_cf_sf_interaction.csv
- path: `/app/outputs/step_02_cf_sf_interaction.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Interaction-strength dependence of bond kinetic energy T and bond current I per spin for CF and SF phases at fixed doping x=0.028.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `U_over_t`, `T`, `I`
  - `units`: object

### step_03_ring_exchange.csv
- path: `/app/outputs/step_03_ring_exchange.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bond current I as a function of ring-exchange coupling K for CF and SF phases at doping x=0.083.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `K_over_t`, `I`
  - `units`: object

### step_04_projected_cf_doping.csv
- path: `/app/outputs/step_04_projected_cf_doping.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Doping dependence of bond kinetic energy T and bond current I for the fully projected CF phase. The data depend on the previously computed reference double occupancy d0(n).
- schema:
  - `type`: table
  - `required_columns`: `doping_x`, `T`, `I`
  - `units`: object

Notes: All numeric values are dimensionless bond order parameters. The checker compares each value to a hidden reference using predefined tolerances and also verifies qualitative trends (e.g., monotonic decrease of I with doping, saturation of CF current, suppression by positive K, peak of I in projected model near x≈0.08).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_cf_sf_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "doping_x",
          "T",
          "I"
        ],
        "units": {}
      },
      "description": "Doping dependence of bond kinetic energy T and bond current I per spin for charge-flux (CF) and spin-flux (SF) phases. Each row is one phase at one doping value."
    },
    {
      "file": "step_02_cf_sf_interaction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "U_over_t",
          "T",
          "I"
        ],
        "units": {}
      },
      "description": "Interaction-strength dependence of bond kinetic energy T and bond current I per spin for CF and SF phases at fixed doping x=0.028."
    },
    {
      "file": "step_03_ring_exchange.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "K_over_t",
          "I"
        ],
        "units": {}
      },
      "description": "Bond current I as a function of ring-exchange coupling K for CF and SF phases at doping x=0.083."
    },
    {
      "file": "step_04_projected_cf_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping_x",
          "T",
          "I"
        ],
        "units": {}
      },
      "description": "Doping dependence of bond kinetic energy T and bond current I for the fully projected CF phase. The data depend on the previously computed reference double occupancy d0(n)."
    }
  ],
  "notes": "All numeric values are dimensionless bond order parameters. The checker compares each value to a hidden reference using predefined tolerances and also verifies qualitative trends (e.g., monotonic decrease of I with doping, saturation of CF current, suppression by positive K, peak of I in projected model near x≈0.08)."
}
```

## How you are scored
Each of the four required CSV files is scored independently by a hidden verifier. The verifier compares the numeric values of T and I (and, where appropriate, the phase label) to reference data derived from the original study. Small deviations due to implementation details are allowed, but the values must lie within prescribed tolerances to receive full credit. In addition, the verifier checks qualitative trends in the data, such as the overall dependence of the bond current on doping, interaction strength, or ring-exchange coupling, and whether certain expected structural features (e.g., peak positions, sign changes, relative ordering between CF and SF phases) are present. The final score is the average of the scores awarded to the four CSV artifacts, each weighted equally. Simply reporting numbers that match the hidden reference without genuinely running the self-consistent Hartree-Fock calculations is not sufficient—the verifier's structural checks are designed to detect that the computational pipeline was executed correctly.
