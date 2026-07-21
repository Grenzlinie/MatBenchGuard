# Reproduction task

## Problem background
The paper investigates the effect of donor-electron doping on the stability of the ferromagnetic state in a quasi-one-dimensional organic ferromagnet. The system consists of a main carbon chain (80 sites) with itinerant π‑electrons, side radicals attached to odd‑indexed carbon atoms, and an extra donor electron. The interactions include electron hopping with Su‑Schrieffer‑Heeger (SSH) type electron‑phonon coupling, on‑site Hubbard electron‑electron repulsion, and antiferromagnetic exchange coupling between π‑electrons and the unpaired electrons of the side radicals. The ground state is obtained self‑consistently within a mean‑field approximation by solving coupled eigenvalue equations and optimizing the dimerization order parameter. Doping introduces a polaron, which locally distorts the spin density wave (SDW) and alters the effective exchange between side radicals, thereby affecting the overall ferromagnetic ordering. The task is to compute the total energy as a function of side‑radical spin expectation for neutral and doped systems, examine the spin density profile around the polaron, and extract energy differences that quantify the change in ferromagnetic stability.

## Approach
The method uses a mean‑field decoupling of the Hubbard and exchange terms, leading to separate eigenvalue equations for spin‑α and spin‑β electrons on a 80‑site chain with periodic boundary conditions. The SSH electron‑phonon coupling is accounted for by a dimerization order parameter yᵢ, which is updated at each iteration to minimize the total energy. The dimensionless parameters are fixed at t₀ = 2.5 eV, λ = 0.25, and u = 0.8. The exchange coupling constant j_f is varied over {0.2, 0.3, 0.5}. For each j_f, we consider three doping conditions: (a) neutral chain (no extra electron), (b) one extra donor electron with spin S = −1/2, and (c) one extra donor electron with spin S = +1/2. For each condition, the side‑radical spin expectation ⟨Sᶻ_R⟩ is scanned from 0 to 0.5 in steps of 0.1. The self‑consistent solution yields eigenenergies and wavefunction expansion coefficients, from which the total energy, charge density, and spin density δnᵢ are computed. The total energy curves allow extraction of ΔE₂ = E(⟨Sᶻ_R⟩=0) − E(⟨Sᶻ_R⟩=0.5) for each combination of doping and j_f. The spin density profile is obtained for the ferromagnetic configuration (⟨Sᶻ_R⟩=0.5) at j_f=0.3 for both doped cases. Additionally, the energy difference ΔE₁ between the polaronic levels of opposite spin is determined from the total energies of the two doped systems.

## Reproduction target
Produce three scored CSV artifacts under /app/outputs:
1. energy_curves.csv: total energy for every condition (donor_spin, j_f, srz_expectation). Columns: donor_spin (none, 1/2, -1/2), j_f (float), srz_expectation (float from 0.0 to 0.5 step 0.1), total_energy (dimensionless in units of t₀).
2. polaron_profile.csv: spin density δnᵢ along the 80‑site chain for the ferromagnetic state (⟨Sᶻ_R⟩=0.5) with j_f=0.3, for both S=+1/2 and S=−1/2 doping. Columns: donor_spin (1/2 or -1/2), j_f (0.3), site_index (1..80), spin_density (float).
3. energies_summary.csv: summary of energy differences for each (donor_spin, j_f). Columns: donor_spin, j_f, E_srz0, E_srz0p5, delta_E2 (= E_srz0 − E_srz0p5), delta_E1 (polaronic level difference; empty for neutral).
The solver must run the full mean‑field self‑consistency from scratch; simply reporting the paper’s numbers without actual computation will fail the hidden checker’s structural and cross‑consistency tests.

## Assets
The following non‑paper assets are required; the agent must install them itself:
- numpy (package, pip install numpy)
- scipy (package, pip install scipy)
No external datasets, models, or proprietary tools are needed; the computation is entirely from the specified model and parameters.

## Workflow steps

### Step 1: Run mean-field simulations
- Role: process
- Action: Implement the self-consistent mean-field solver for the Hamiltonian with parameters: chain length N=80, periodic boundary conditions, t0=2.5, λ=0.25, u=0.8. For each exchange coupling j_f ∈ {0.2, 0.3, 0.5} and for neutral, S=-1/2, and S=+1/2 doping, scan side-radical spin expectation ⟨S^z_R⟩ from 0.0 to 0.5 in steps of 0.1. Solve coupled eigenvalue equations and minimize total energy. Store wavefunction coefficients and energies.
- Evidence: none

### Step 2: Generate energy curves table
- Role: scored (load-bearing)
- Action: For every simulated condition, compute the total energy and write a CSV with columns: donor_spin (string: none, 1/2, -1/2), j_f (float), srz_expectation (float, from 0 to 0.5 step 0.1), total_energy (float, dimensionless).
- Output file: `/app/outputs/energy_curves.csv`
- Format: csv
- Contract: Columns: donor_spin, j_f, srz_expectation, total_energy. One row per unique (donor_spin, j_f, srz_expectation).
- Scoring: scored by hidden verifier

### Step 3: Extract polaron spin density profile
- Role: scored
- Action: For the ferromagnetic state (⟨S^z_R⟩=0.5) with j_f=0.3, compute the spin density δn_i on each site for the S=+1/2 and S=-1/2 doped cases using the stored wavefunctions. Write a CSV with columns: donor_spin (1/2 or -1/2), j_f (0.3), site_index (int, 1–80), spin_density (float).
- Output file: `/app/outputs/polaron_profile.csv`
- Format: csv
- Contract: Columns: donor_spin, j_f, site_index, spin_density.
- Scoring: scored by hidden verifier

### Step 4: Compute energy differences
- Role: scored (load-bearing)
- Action: From the energy curves, extract for each (donor_spin, j_f) the energies at ⟨S^z_R⟩=0 (E_srz0) and ⟨S^z_R⟩=0.5 (E_srz0p5), and compute delta_E2 = E_srz0 − E_srz0p5. For doped cases, compute delta_E1 as the energy difference between the total energies of the S=-1/2 and S=+1/2 systems (polaronic level splitting). Write a CSV with columns: donor_spin (none|1/2|-1/2), j_f, E_srz0, E_srz0p5, delta_E2, delta_E1 (empty for neutral).
- Output file: `/app/outputs/energies_summary.csv`
- Format: csv
- Contract: Columns: donor_spin, j_f, E_srz0, E_srz0p5, delta_E2, delta_E1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- energy_curves.csv
- polaron_profile.csv
- energies_summary.csv

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_curves.csv
- path: `/app/outputs/energy_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total energy for every (donor_spin, j_f, srz_expectation) condition.
- schema:
  - `columns`: `donor_spin`, `j_f`, `srz_expectation`, `total_energy`
  - `types`: `string`, `float`, `float`, `float`

### polaron_profile.csv
- path: `/app/outputs/polaron_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spin density profile along the 80-site chain for the FM state at j_f=0.3.
- schema:
  - `columns`: `donor_spin`, `j_f`, `site_index`, `spin_density`
  - `types`: `string`, `float`, `int`, `float`

### energies_summary.csv
- path: `/app/outputs/energies_summary.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy differences and the consistency relation ΔE₂(β)−ΔE₂(α)≈ΔE₁, verified via structural constraints.
- schema:
  - `columns`: `donor_spin`, `j_f`, `E_srz0`, `E_srz0p5`, `delta_E2`, `delta_E1`
  - `types`: `string`, `float`, `float`, `float`, `float`, `float`

Notes: All output files must be placed under /app/outputs. The solver runs the full mean-field self-consistency from the model parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/energy_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "columns": [
          "donor_spin",
          "j_f",
          "srz_expectation",
          "total_energy"
        ],
        "types": [
          "string",
          "float",
          "float",
          "float"
        ]
      },
      "description": "Total energy for every (donor_spin, j_f, srz_expectation) condition."
    },
    {
      "file": "/app/outputs/polaron_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "columns": [
          "donor_spin",
          "j_f",
          "site_index",
          "spin_density"
        ],
        "types": [
          "string",
          "float",
          "int",
          "float"
        ]
      },
      "description": "Spin density profile along the 80-site chain for the FM state at j_f=0.3."
    },
    {
      "file": "/app/outputs/energies_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "columns": [
          "donor_spin",
          "j_f",
          "E_srz0",
          "E_srz0p5",
          "delta_E2",
          "delta_E1"
        ],
        "types": [
          "string",
          "float",
          "float",
          "float",
          "float",
          "float"
        ]
      },
      "description": "Energy differences and the consistency relation ΔE₂(β)−ΔE₂(α)≈ΔE₁, verified via structural constraints."
    }
  ],
  "notes": "All output files must be placed under /app/outputs. The solver runs the full mean-field self-consistency from the model parameters."
}
```

## How you are scored
The hidden verifier reads each scored artifact and applies a multi‑faceted check. For energy_curves.csv, it verifies that the total energy curves satisfy certain structural constraints (e.g., monotonic behavior or presence of local minima, consistent with the underlying physics). For polaron_profile.csv, it checks that the spin density profile exhibits physically expected modulation rather than being uniform. For energies_summary.csv, the verifier recomputes derived quantities and checks a self-consistency relation among the reported energy differences. Each artifact contributes a weight to the final reward (energy_curves.csv and energies_summary.csv carry the highest weight). Passing requires that all checks succeed; reporting the paper's numbers without the underlying computation will fail these structural and consistency checks.
