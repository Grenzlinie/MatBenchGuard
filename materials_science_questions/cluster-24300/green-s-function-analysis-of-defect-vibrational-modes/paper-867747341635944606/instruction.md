# Two-species TLS model on a disordered lattice: density of states and universal parameters

## Problem background
Disordered solids – from amorphous glasses to mixed crystals – exhibit surprisingly universal low-temperature properties below about 3 K: a nearly linear specific heat, a T² thermal conductivity, and a temperature‑independent internal friction that varies little between materials of very different microscopic structure. Understanding the origin of this universality is a long‑standing puzzle. The present work proposes that two distinct species of two‑level systems (TLSs) – those symmetric (τ) and those asymmetric (S) under local inversion – interact via phonon‑mediated potentials, with the symmetric TLSs coupling only weakly to phonons. A numerical simulation on a disordered cubic lattice computes the densities of states of both species and extracts a universal crossover temperature and a small dimensionless tunneling strength; these quantities are thought to explain the observed low‑temperature behaviour. Your task is to reproduce this simulation and obtain those quantities.

## Approach
The effective model describes two kinds of pseudo‑spins (S and τ) on a disordered cubic lattice with periodic boundary conditions. Each impurity site carries an S‑spin (asymmetric under inversion, coupling strongly to the strain field) and a τ‑spin (symmetric under inversion, coupling weakly). The mutual interactions have the form  
J_ij^{ab} = c_ij^{ab} γ_a γ_b / (ρ c² (R_ij³ + ã³)),  
with random angular factors c_ij^{ab} drawn from a zero‑mean unit‑variance Gaussian distribution. The phonon couplings are described by a ratio g = γ_τ / γ_S ≈ 0.02 and a reference energy scale J_o = γ_S² / (ρ c²) ≈ 500 K. The short‑distance cutoff ã and the impurity concentration x (e.g. 0.2 or 0.5) are adjustable parameters.

The simulation proceeds by (i) randomly placing impurities on the lattice, (ii) computing all pairwise interactions from the above radial form, (iii) solving for the lowest‑energy τ‑spin configuration (flipping any spin whose total effective field is negative), (iv) for each S spin finding the minimal excitation energy that satisfies the many‑body stability condition  ∏_j Θ(E + E_τ_j − 2 U_ij) > 0, and (v) building normalized histograms of the τ and S excitation energies to obtain the densities of states n_τ(E) and n_S(E). From these curves the crossover temperature T_U is defined by the equality of phonon scattering rates γ_τ² n_τ(T_U) = γ_S² n_S(T_U), and the universal tunneling strength is C_o = κ g, with κ ≈ 0.1.

## Reproduction target
Implement the two‑species TLS model on a cubic lattice with periodic boundary conditions. Run the simulation for at least one finite impurity concentration (e.g. x = 0.2 or 0.5) and for several values of the short‑distance cutoff ã/a₀ (e.g. 0, 1.5, 3). From the simulation produce two density‑of‑states curves (normalized per impurity) as CSV files:
- dos_tau.csv : the τ‑TLS density of states n_τ(E),
- dos_s.csv   : the S‑TLS density of states n_S(E).
Using these curves and the known coupling ratio g, determine (a) the crossover temperature T_U (in Kelvin) at which γ_τ² n_τ(T_U) = γ_S² n_S(T_U), and (b) the dimensionless tunneling strength C_o = κ g with κ ≈ 0.1. Output both values in universality_params.json, together with the reference energy scale J_o (K) and g if desired.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute τ-TLS density of states
- Role: scored
- Action: Construct a cubic lattice with periodic boundary conditions, randomly place impurities at a finite concentration x (e.g., 0.2 or 0.5). Assign each impurity an S spin and a τ spin. Compute pairwise interactions J_ij^{ab} from the paper's radial form (using random angular factors drawn from a zero-mean unit-variance Gaussian, coupling ratio g≈0.02, reference energy scale J_o≈500 K, and adjustable short-distance cutoff ã). Solve for the stable τ-spin configuration (flip spins with negative total field) and build the normalized histogram of τ-TLS excitation energies to obtain n_τ(E).
- Output file: `/app/outputs/dos_tau.csv`
- Format: csv
- Contract: Columns: energy_K (float, energy bin centre in Kelvin), density (float, number of states per energy interval per impurity).
- Scoring: scored by hidden verifier

### Step 2: Compute S-TLS density of states
- Role: scored
- Action: From the same simulation configuration (interactions, τ-spin energies), for each S spin find the minimal excitation energy E_S_min that satisfies the stability condition ∏_j Θ(E_S_min + E_τ_j - 2 U_ij) > 0. Build the normalized histogram of these minimal energies to obtain n_S(E).
- Output file: `/app/outputs/dos_s.csv`
- Format: csv
- Contract: Columns: energy_K (float, energy bin centre in Kelvin), density (float, number of states per energy interval per impurity).
- Scoring: scored by hidden verifier

### Step 3: Extract universal parameters C_o and T_U
- Role: scored (load-bearing)
- Action: From the computed n_S(E) and n_τ(E) curves, determine the crossover temperature T_U where γ_τ² n_τ(T_U) = γ_S² n_S(T_U) (using the known coupling ratio g = γ_τ/γ_S). Then compute the universal tunneling strength C_o = κ g, with κ ≈ 0.1. Report both values in a JSON file.
- Output file: `/app/outputs/universality_params.json`
- Format: json
- Contract: Top-level keys: C_o (float, dimensionless), T_U_K (float, crossover temperature in Kelvin). Optionally include J_o_K (float, reference energy scale) and g (float, coupling ratio).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_tau.csv`
- `/app/outputs/dos_s.csv`
- `/app/outputs/universality_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_tau.csv
- path: `/app/outputs/dos_tau.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Density of states for τ-TLSs computed from the lattice simulation.
- schema:
  - `type`: table
  - `required_columns`: `energy_K`, `density`
  - `units`:
    - `energy_K`: K
    - `density`: states per energy per impurity

### dos_s.csv
- path: `/app/outputs/dos_s.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Density of states for S-TLSs computed from the lattice simulation.
- schema:
  - `type`: table
  - `required_columns`: `energy_K`, `density`
  - `units`:
    - `energy_K`: K
    - `density`: states per energy per impurity

### universality_params.json
- path: `/app/outputs/universality_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Extracted universal tunneling strength C_o and crossover temperature T_U.
- schema:
  - `type`: object
  - `required`:
    - `C_o`: float (dimensionless)
    - `T_U_K`: float (K)
  - `optional`:
    - `J_o_K`: float (K)
    - `g`: float (dimensionless)
  - `units`:
    - `C_o`: dimensionless
    - `T_U_K`: K

Notes: The density-of-states CSV files are scored by structural audit (the checker verifies that n_S(E) drops sharply below ~10 K and n_τ(E) shows only a weak dip below ~0.2 K, and that the overall shapes are physically reasonable). The universality parameters are compared to the paper's reference values with a generous tolerance that accounts for implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_tau.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_K",
          "density"
        ],
        "units": {
          "energy_K": "K",
          "density": "states per energy per impurity"
        }
      },
      "description": "Density of states for τ-TLSs computed from the lattice simulation."
    },
    {
      "file": "dos_s.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_K",
          "density"
        ],
        "units": {
          "energy_K": "K",
          "density": "states per energy per impurity"
        }
      },
      "description": "Density of states for S-TLSs computed from the lattice simulation."
    },
    {
      "file": "universality_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C_o": "float (dimensionless)",
          "T_U_K": "float (K)"
        },
        "optional": {
          "J_o_K": "float (K)",
          "g": "float (dimensionless)"
        },
        "units": {
          "C_o": "dimensionless",
          "T_U_K": "K"
        }
      },
      "description": "Extracted universal tunneling strength C_o and crossover temperature T_U."
    }
  ],
  "notes": "The density-of-states CSV files are scored by structural audit (the checker verifies that n_S(E) drops sharply below ~10 K and n_τ(E) shows only a weak dip below ~0.2 K, and that the overall shapes are physically reasonable). The universality parameters are compared to the paper's reference values with a generous tolerance that accounts for implementation differences."
}
```

## How you are scored
A hidden verifier inspects each workflow stage artifact and combines their scores into a final reward. For the dos_tau.csv and dos_s.csv files, the verifier performs a structural audit: it checks that n_S(E) drops sharply below the expected energy scale (on the order of 10 K) and that n_τ(E) shows only a weak dip at much lower energies, and confirms that the overall shapes are physically plausible and internally consistent. For universality_params.json the verifier compares your reported C_o and T_U_K against known reference values with a generous tolerance that absorbs legitimate implementation and parameter differences. Reporting the paper’s values without genuinely executing the simulation will not satisfy the structural checks; you must produce internally consistent DOS curves.
