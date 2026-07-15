# Reproduce Interatomic Exchange Couplings from a DMFT Solution of a Minimal Three-Orbital Model

## Problem background
This task investigates the microscopic origins of ferromagnetism in CrO₂, a canonical half-metallic ferromagnet widely used in spintronic applications. The paper constructs a realistic low-energy model for the Cr t₂g bands near the Fermi level and solves it with dynamical mean-field theory (DMFT) to analyze interatomic magnetic exchange interactions. Understanding which interactions stabilize the ferromagnetic ground state is a key open question, and this study aims to quantify the exchange couplings and to elucidate the roles of different contributions (such as double exchange, superexchange, and long-range interactions).

## Approach
First, construct a minimal three-orbital t₂g tight-binding model on the rutile CrO₂ lattice (space group P4₂/mnm, two Cr sites per primitive cell). Use explicitly provided one-electron Hamiltonian matrices (crystal-field splitting and hopping integrals for the nearest-neighbour bonds) and on-site Coulomb interactions in the Kanamori parametrisation (U=2.84 eV, J=0.70 eV, U′=U−2J). Then solve this model self-consistently within DMFT at temperature T=232 K and an external magnetic field μ_B H=5 meV, using an exact diagonalization impurity solver with four bath orbitals per t₂g orbital. From the converged Green’s functions and self-energy, compute the Heisenberg exchange couplings J₁ through J₈ (including the split pairs J₇^<, J₇^> and J₈^<, J₈^>) via the Liechtenstein formula for infinitesimal spin rotations. The result is a set of exchange parameters that characterise the magnetic interactions between Cr sites on the lattice.

## Reproduction target
Compute the Heisenberg exchange couplings J₁ through J₈ (in meV) from the DMFT solution of the minimal t₂g model and write them to the file `/app/outputs/exchange_couplings.json` according to the specified schema. The hidden verifier will compare these couplings against reference values and will also use them to perform a spin-wave stability analysis on the rutile lattice to assess the physical consistency of the obtained magnetic interactions.

## Assets

- Open-source DMFT solver with exact diagonalization impurity solver
- Crystal structure of rutile CrO₂

## Workflow steps

### Step 1: Construct the minimal t₂g model
- Role: process
- Action: Set up the one-electron Hamiltonian matrices (site-diagonal crystal-field matrix and hopping matrices for bonds 1‑1′ and 1‑2) in the three‑orbital t₂g basis and the Kanamori interaction parameters (U=2.84 eV, J=0.70 eV, U′=U−2J). Build the full lattice model on the rutile CrO₂ lattice (space group P4₂/mnm, two Cr sites per primitive cell).
- Evidence: `/app/outputs/model_setup_log.txt`

### Step 2: Solve the DMFT equations
- Role: process
- Action: Perform self-consistent DMFT calculations at temperature T=232 K and external magnetic field μ_B H=5 meV. Use an exact diagonalization impurity solver with four bath orbitals per t₂g orbital. Iterate until convergence of the local self-energy and orbital populations.
- Evidence: `/app/outputs/dmft_convergence.json`

### Step 3: Compute interatomic exchange couplings
- Role: scored (load-bearing)
- Action: From the converged DMFT self-energy and Green’s functions, compute the Heisenberg exchange parameters J₁ through J₈ (including J₇^<, J₇^>, J₈^<, J₈^>) using the Liechtenstein formula (infinitesimal spin rotations). Write the results to exchange_couplings.json.
- Output file: `/app/outputs/exchange_couplings.json`
- Format: json
- Contract: {"J1" (meV): float, "J2": float, "J3": float, "J4": float, "J5": float, "J6": float, "J7_less": float, "J7_greater": float, "J8_less": float, "J8_greater": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exchange_couplings.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exchange_couplings.json
- path: `/app/outputs/exchange_couplings.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Heisenberg exchange parameters J₁ through J₈ computed from the DMFT solution of the minimal t₂g model.
- schema:
  - `type`: object
  - `required`:
    - `J1`: float (meV)
    - `J2`: float (meV)
    - `J3`: float (meV)
    - `J4`: float (meV)
    - `J5`: float (meV)
    - `J6`: float (meV)
    - `J7_less`: float (meV)
    - `J7_greater`: float (meV)
    - `J8_less`: float (meV)
    - `J8_greater`: float (meV)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exchange_couplings.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "J1": "float (meV)",
          "J2": "float (meV)",
          "J3": "float (meV)",
          "J4": "float (meV)",
          "J5": "float (meV)",
          "J6": "float (meV)",
          "J7_less": "float (meV)",
          "J7_greater": "float (meV)",
          "J8_less": "float (meV)",
          "J8_greater": "float (meV)"
        }
      },
      "description": "Heisenberg exchange parameters J₁ through J₈ computed from the DMFT solution of the minimal t₂g model."
    }
  ],
  "notes": ""
}
```

## How you are scored
The hidden verifier processes each workflow-step artifact independently. For the scored step, it reads `exchange_couplings.json` and compares each exchange parameter to a hidden reference value within appropriate tolerances. It also performs a structural spin-wave calculation from the reported couplings to verify that they satisfy a predefined physical stability criterion. The final reward is a weighted combination of the numerical accuracy of the couplings and the outcome of the spin-wave check. Simply reporting numbers from the paper is not sufficient; the submitted values must result from a genuine DMFT solution of the model as described.
