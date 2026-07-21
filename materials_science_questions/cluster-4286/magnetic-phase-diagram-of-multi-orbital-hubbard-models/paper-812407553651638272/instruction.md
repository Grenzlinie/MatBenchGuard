# Itinerant Ferromagnetism in Two-Orbital Hubbard Model via Generalized Gutzwiller Method

## Problem background
This project investigates itinerant ferromagnetism in a two-band Hubbard model with two degenerate e_g orbitals on a simple cubic lattice. The generalized Gutzwiller variational method introduces correlation-induced hopping reduction factors (loss factors) and a multi-occupancy energy functional; minimizing this functional yields the ground-state magnetization as a function of the on-site interaction U. The work contrasts the Gutzwiller predictions with those of Hartree–Fock mean-field theory, highlighting differences in the onset and evolution of the magnetization. The goal is to compute the magnetization Δ (the spin-splitting parameter) for two band fillings as a function of U (with J = 0.2 U), and to map the paramagnetic-to-ferromagnetic phase boundary in the J/U vs U plane at a fixed filling, using the Gutzwiller formalism and, for comparison, the Hartree–Fock approximation.

## Approach
Begin by constructing the tight‑binding Hamiltonian for the two‑orbital e_g model on a simple cubic lattice, using the published Slater–Koster hopping parameters (first‑ and second‑nearest‑neighbour integrals and ratios). Compute the density of states and obtain the uncorrelated kinetic energy per single‑particle label ε̄(m) as a function of the occupancy m. This function is an essential building block for both Gutzwiller and Hartree–Fock energy functionals.

For the Gutzwiller method, introduce seven average multiple‑occupancy variables (net probabilities for empty, singly‑, doubly‑, triply‑, and quadruply‑occupied configurations) and the magnetization variational parameter Δ (so that the spin‑dependent occupancies become m_± = m ± Δ; the total electron number per atom is 4 m). From these, construct the hopping loss factors q₊ and q₋ that renormalize the kinetic energy. Combine with the on‑site interaction terms: the intra‑orbital Hubbard U, the inter‑orbital U′, and the Hund’s exchange J, using the e_g‑orbital relation U′ = U − 2 J. Form the total energy functional E(Δ, occupancies) as the sum of the renormalized kinetic energy and the interaction energy. Numerically minimize E for each (U, J, m) configuration to obtain the equilibrium magnetization Δ. A similar minimization is performed for the Hartree–Fock mean‑field decoupling of the same Hamiltonian, where the interaction terms are replaced by an effective Zeeman‑like splitting. All minimizations assume charge homogeneity and a ferromagnetic spin splitting.

## Reproduction target
Produce three output files under `/app/outputs`:

1. `magnetization_curves.csv` (scored). Columns: `U` (eV), `delta_G_m0.35` (dimensionless magnetization from Gutzwiller), `delta_G_m0.30` (dimensionless magnetization from Gutzwiller). For both fillings m = 0.35 and m = 0.30, at fixed J/U = 0.2 (so J = 0.2 U, U′ = U − 2 J), cover a suitable U range such that the onset and saturation of ferromagnetism are visible; provide at least 20 U points per filling.

2. `phase_diagram.csv` (scored). Columns: `J_over_U` (dimensionless), `U_c` (eV). For filling m = 0.30, vary J/U from 0 to 0.4 (at least 10 points) and determine the critical interaction strength U_c at which the Gutzwiller ground state first acquires a non‑zero magnetization (onset of ferromagnetism).

3. `hf_magnetization.csv` (supporting, not scored). Columns: `U` (eV), `delta_HF_m0.35`, `delta_HF_m0.30`. Hartree–Fock magnetization curves computed under the same conditions as the Gutzwiller curves. This file is required to demonstrate the full comparative pipeline but does not contribute to the score.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute uncorrelated kinetic energy function
- Role: process
- Action: Construct the tight-binding Hamiltonian for a two-degenerate-e_g-orbital model on a simple cubic lattice using the published Slater–Koster hopping parameters. The parameters are: nearest-neighbor (1NN) T_ddσ = 1 eV, next-nearest-neighbor (2NN) T_ddσ = 0.25 eV; the ratios are T_ddδ : T_ddπ : T_ddσ = 0.1 : 0.3 : -0.3 : 1 (with T_ddσ as reference). Compute the density of states and the uncorrelated kinetic energy per single-particle label ε̄(m) as a function of occupancy m. This function is required for subsequent variational energy functionals.
- Evidence: none

### Step 2: Hartree–Fock magnetization curves (supporting)
- Role: process
- Action: Implement Hartree–Fock mean-field decoupling for the same two-orbital model. Minimize the HF total energy with respect to magnetization Δ for a grid of U values (with J=0.2U, U'=U−2J) at fillings m=0.35 and m=0.30. Save the obtained magnetization versus U as a supporting artifact.
- Evidence: `/app/outputs/hf_magnetization.csv`

### Step 3: Gutzwiller magnetization curves (scored)
- Role: scored (load-bearing)
- Action: Implement the generalized Gutzwiller variational energy functional with seven multiple-occupancy parameters and the spin-splitting variational parameter Δ. For fillings m=0.35 and m=0.30, minimize the energy numerically over a grid of interaction strengths U (J=0.2U, U'=U−2J) to obtain the equilibrium magnetization Δ. Write the results to a CSV.
- Output file: `/app/outputs/magnetization_curves.csv`
- Format: csv
- Contract: Columns: U (float, eV), delta_G_m0.35 (float, dimensionless magnetization), delta_G_m0.30 (float, dimensionless magnetization). At least 20 points per filling.
- Scoring: scored by hidden verifier

### Step 4: Gutzwiller magnetic phase diagram (scored)
- Role: scored
- Action: For filling m=0.30, vary the ratio J/U from 0 to 0.4. For each ratio, determine the critical interaction strength U_c where the Gutzwiller ground state acquires a non-zero magnetization Δ (onset of ferromagnetism). Save the phase boundary to a CSV.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: J_over_U (float, dimensionless), U_c (float, eV). At least 10 points covering J/U from 0 to 0.4.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_curves.csv`
- `/app/outputs/phase_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_curves.csv
- path: `/app/outputs/magnetization_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Agent-computed Gutzwiller magnetization as a function of U for fillings m=0.35 and m=0.30. Compared to the paper’s reference curves with an absolute tolerance on Δ.
- schema:
  - `type`: table
  - `required_columns`: `U`, `delta_G_m0.35`, `delta_G_m0.30`
  - `units`:
    - `U`: eV
    - `delta_G_m0.35`: 
    - `delta_G_m0.30`: 

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Agent-computed Gutzwiller magnetic phase boundary (critical U_c vs J/U ratio) for filling m=0.30. Compared to the paper’s reference boundary with an absolute tolerance on U_c.
- schema:
  - `type`: table
  - `required_columns`: `J_over_U`, `U_c`
  - `units`:
    - `J_over_U`: 
    - `U_c`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "delta_G_m0.35",
          "delta_G_m0.30"
        ],
        "units": {
          "U": "eV",
          "delta_G_m0.35": "",
          "delta_G_m0.30": ""
        }
      },
      "description": "Agent-computed Gutzwiller magnetization as a function of U for fillings m=0.35 and m=0.30. Compared to the paper’s reference curves with an absolute tolerance on Δ."
    },
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "J_over_U",
          "U_c"
        ],
        "units": {
          "J_over_U": "",
          "U_c": "eV"
        }
      },
      "description": "Agent-computed Gutzwiller magnetic phase boundary (critical U_c vs J/U ratio) for filling m=0.30. Compared to the paper’s reference boundary with an absolute tolerance on U_c."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will inspect your output files. For `magnetization_curves.csv`, it compares your Δ values at a set of U points against reference values derived from the paper’s reported curves; the comparison considers both the quantitative magnitude and the qualitative shape (continuous/second‑order onset, first‑order jumps, saturation behaviour). For `phase_diagram.csv`, the verifier compares your critical U_c values at several J/U ratios to the paper’s phase boundary. The final score is a weighted combination of these two scored artifacts. To receive full credit you must perform the actual variational minimisations; simply reporting the paper’s quoted numbers without running the physics will not pass the verifier.
