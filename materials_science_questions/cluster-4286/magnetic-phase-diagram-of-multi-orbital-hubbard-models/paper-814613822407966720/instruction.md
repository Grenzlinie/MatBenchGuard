# Ground-state magnetic phase diagram of multi-orbital Hubbard models

## Problem background
Divalent boride systems such as CaB₆ exhibit a semimetallic band structure where three pairs of valence and conduction bands overlap at the X points of the cubic Brillouin zone. The valence bands derive from t₂g molecular orbitals and the conduction bands from t₂u orbitals, each having threefold degeneracy due to cubic symmetry. The possibility of ferromagnetic (FM) ordering in these materials has been a subject of debate, and theoretical investigation of the ground state of a realistic multi-orbital Hubbard model with on-site Coulomb (U) and Hund's exchange (J_H) interactions is needed. This task addresses whether metallic ferromagnetism can be stabilized within Hartree mean-field theory for interaction strengths comparable to the bandwidth, and how the answer depends on the number of active band pairs (three in the cubic “multi‑X‑point” model versus one in a hypothetical tetragonal “single‑X‑point” model).

## Approach
Both models are solved within the Hartree mean-field approximation. The formalism introduces uniform order parameters: the self-doped charge δ, and the magnetization per valence band (mₐ) and per conduction band (m_b). For the multi‑X‑point model all three pairs are treated symmetrically; for the single‑X‑point model only one pair is active. The tight-binding kinetic energy is constructed using the hopping parameters t_g/t₀ = 0.2, t_u/t₀ = 0.6, t_eff/t₀ = 0.2 (t₀ sets the energy scale) and the constrained Slater-integral relations among the on-site interactions (U′ = U − 2J_H, inter-pair couplings as given in the interaction table). The self-consistency equations for the order parameters are derived from the mean-field energy, and the total energy per site is computed as E = E_kin + E_int. For the single‑X‑point model, the excitonic instability is also considered by solving the gap equation for a uniform excitonic order parameter Δ. The phase diagram is obtained by sweeping U/t₀ and J_H/t₀ over a grid, searching for self-consistent solutions corresponding to paramagnetic metal (PM), paramagnetic insulator (PI), three classes of ferromagnetic metals (FM_I, FM_II, FM_III), ferromagnetic insulator (FI), and, where relevant, excitonic insulator (EI). At each (U, J_H) point the ground state is identified by the lowest total energy. The computed order parameters, total energy, and state label are recorded in csv tables.

## Reproduction target
Produce two phase-diagram data files by executing the Hartree mean-field calculations described above. The **multi‑X‑point model** file must contain the ground-state assignment and raw order parameters on a grid of U and J_H values, covering the region where the interaction strengths are comparable to the bandwidth. The **single‑X‑point model** file must similarly span the same (U, J_H) plane and include all possible phases (PM, PI, FM variants, FI, EI). From these files the verifier will determine whether a metallic FM solution exists as the ground state in the realistic parameter range, identify the location of any PM‑to‑FI transition, and check the presence of an FM region and the excitonic insulator in the single‑X‑pair case. The goal is to reproduce the qualitative structure and mutual relations of the phases, not to match exact numerical thresholds (which are subject to tolerances).

## Assets

- Python scientific computing libraries: numpy scipy matplotlib
- Tight-binding and interaction parameters

## Workflow steps

### Step 1: Define the multi-orbital Hubbard model and mean-field formalism
- Role: process
- Action: Write code that defines the tight-binding energy dispersions for both the multi‑X‑point (cubic) and single‑X‑point (tetragonal) models, using the hopping parameters t_g/t0=0.2, t_u/t0=0.6, t_eff/t0=0.2, and the on-site interaction parameters with the Slater relations (U=U'+2J_H, inter-pair couplings from Table I). Also implement the Hartree mean-field energy expressions (E_kin, E_int) and the self-consistency relations for both models, including the excitonic gap equation for the single‑X‑point model.
- Evidence: `/app/outputs/model_code.py`

### Step 2: Compute multi‑X‑point phase diagram
- Role: scored (load-bearing)
- Action: For the multi‑X‑point model, numerically solve the Hartree mean-field equations on a grid of (U, J_H) values. At each point, find the self-consistent solutions for paramagnetic metal (PM) and ferromagnetic insulating (FI) states (and any partially or fully polarized ferromagnetic metallic states if they exist), compute the total energy per site, and determine the ground state. Output the state label, order parameters (δ, m_a, m_b), and total energy.
- Output file: `/app/outputs/multi_X_point_phase_data.csv`
- Format: csv
- Contract: CSV with columns: U (in units of t0), J_H (in units of t0), delta (dimensionless self-doped charge), m_a (dimensionless magnetization of valence band), m_b (dimensionless magnetization of conduction band), total_energy (per site), state_label (one of PM, FM_I, FM_II, FM_III, FI).
- Scoring: scored by hidden verifier

### Step 3: Compute single‑X‑point phase diagram
- Role: scored (load-bearing)
- Action: For the single‑X‑point model, numerically solve the Hartree mean-field equations on a grid of (U, J_H) values, including the possibility of excitonic insulator (EI) by solving the excitonic gap equation. Find the self-consistent solutions for PM, paramagnetic insulator (PI), ferromagnetic metallic (FM), FI, and EI states, compute the total energy per site, and determine the ground state. Output state label, order parameters (δ, m_a, m_b), and total energy.
- Output file: `/app/outputs/single_X_point_phase_data.csv`
- Format: csv
- Contract: CSV with columns: U (in units of t0), J_H (in units of t0), delta (dimensionless self-doped charge), m_a (dimensionless magnetization of valence band), m_b (dimensionless magnetization of conduction band), total_energy (per site), state_label (one of PM, PI, FM_I, FM_II, FM_III, FI, EI).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/multi_X_point_phase_data.csv`
- `/app/outputs/single_X_point_phase_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### multi_X_point_phase_data.csv
- path: `/app/outputs/multi_X_point_phase_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase diagram data for the multi‑X‑point model. The checker recomputes the ground-state assignment from the submitted order parameters and total energies, and verifies that no metallic ferromagnetic state is the ground state in the realistic parameter window and that the PM-FI transition occurs at U+J_H ≈ 12 t0.
- schema:
  - `type`: table
  - `required_columns`: `U`, `J_H`, `delta`, `m_a`, `m_b`, `total_energy`, `state_label`
  - `units`:
    - `U`: t0
    - `J_H`: t0
    - `delta`: dimensionless
    - `m_a`: dimensionless
    - `m_b`: dimensionless
    - `total_energy`: per site

### single_X_point_phase_data.csv
- path: `/app/outputs/single_X_point_phase_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase diagram data for the single‑X‑point model. The checker recomputes the ground-state assignment and verifies the existence of a ferromagnetic metallic region and that the excitonic insulator appears only near U ≈ 4 J_H.
- schema:
  - `type`: table
  - `required_columns`: `U`, `J_H`, `delta`, `m_a`, `m_b`, `total_energy`, `state_label`
  - `units`:
    - `U`: t0
    - `J_H`: t0
    - `delta`: dimensionless
    - `m_a`: dimensionless
    - `m_b`: dimensionless
    - `total_energy`: per site

Notes: The checker will recompute the ground state from the raw submitted data and check critical boundaries and phase existence. No hidden gold values are leaked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "multi_X_point_phase_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "J_H",
          "delta",
          "m_a",
          "m_b",
          "total_energy",
          "state_label"
        ],
        "units": {
          "U": "t0",
          "J_H": "t0",
          "delta": "dimensionless",
          "m_a": "dimensionless",
          "m_b": "dimensionless",
          "total_energy": "per site"
        }
      },
      "description": "Phase diagram data for the multi‑X‑point model. The checker recomputes the ground-state assignment from the submitted order parameters and total energies, and verifies that no metallic ferromagnetic state is the ground state in the realistic parameter window and that the PM-FI transition occurs at U+J_H ≈ 12 t0."
    },
    {
      "file": "single_X_point_phase_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "J_H",
          "delta",
          "m_a",
          "m_b",
          "total_energy",
          "state_label"
        ],
        "units": {
          "U": "t0",
          "J_H": "t0",
          "delta": "dimensionless",
          "m_a": "dimensionless",
          "m_b": "dimensionless",
          "total_energy": "per site"
        }
      },
      "description": "Phase diagram data for the single‑X‑point model. The checker recomputes the ground-state assignment and verifies the existence of a ferromagnetic metallic region and that the excitonic insulator appears only near U ≈ 4 J_H."
    }
  ],
  "notes": "The checker will recompute the ground state from the raw submitted data and check critical boundaries and phase existence. No hidden gold values are leaked."
}
```

## How you are scored
A hidden verifier reads the two submitted csv files and recomputes the ground-state assignment at every (U, J_H) point from the reported total energies. It then checks the following qualitative features against a hidden gold derived from the paper's reported phase diagrams: (a) for the multi‑X‑point model, that no metallic FM state (FM_I, FM_II, FM_III) is the ground state over the realistic interaction window and that the PM‑FI transition occurs at a U+J_H value consistent with the expected threshold; (b) for the single‑X‑point model, that a contiguous region of FM ground states exists for intermediate U and J_H, and that an excitonic insulator ground state appears only near the line U ≈ 4 J_H. Tolerances are chosen to accommodate grid discretization and differences in numerical root‑finding. The verifier assigns a score for each file and combines them into a final reward (float in [0,1]); reporting a plausible number without performing the mean-field computation is insufficient.
