# Phase Diagram of Repulsive Rods on a Bethe-like Lattice

## Problem background
A system of rigid rods of length k on the random locally tree-like layered lattice (RLTL) with coordination number 4 shows interesting phase behaviour when rods of different orientations are allowed to intersect at a site with a repulsive weight u. At low densities, the rods are disordered, while at intermediate densities nematic order may emerge. The goal is to map out the phase diagram by computing the nematic order parameter ψ as a function of total rod density ρ and identifying the critical densities that bound the nematic phase.

## Approach
We use the analytic free energy functional derived for this model, which depends on the densities of rods in the x and y orientations, ρ_x and ρ_y, and an intersection density γ_hh that satisfies a quadratic self‑consistency equation. For fixed total density ρ = ρ_x + ρ_y, the free energy is minimized numerically with respect to ρ_x and ρ_y to obtain the equilibrium state. The nematic order parameter ψ = (ρ_x − ρ_y)/ρ signals nematic ordering when it is nonzero. The critical densities are found by tracking where the isotropic solution (ρ_x = ρ_y) becomes unstable – that is, where the quadratic coefficient of the free energy expansion around the isotropic point changes sign. This yields two densities, ρ_c1 and ρ_c2, that depend on the interaction weight u.

## Reproduction target
Produce two CSV artifacts:

1. `order_parameter_vs_density.csv` – the equilibrium order parameter ψ as a function of total density ρ for rod length k = 6 and interaction weight u = 0.15.

2. `phase_diagram_critical_densities.csv` – the critical densities ρ_c1 and ρ_c2 as functions of u for k = 6, covering the range from u = 0 up to where the nematic phase disappears.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement Free Energy Functional
- Role: process
- Action: Implement the analytic free energy functional f(ρ_x,ρ_y,u) for the q=4 RLTL model of repulsive rods of length k. The free energy depends on rod densities ρ_x, ρ_y, the intersection density γ_hh which must be solved from a quadratic self-consistency equation, and the interaction weight u. This implementation must be callable for arbitrary densities and parameters.
- Evidence: `/app/outputs/free_energy_implementation.log`

### Step 2: Order Parameter vs Density
- Role: scored (load-bearing)
- Action: For q=4, rod length k=6, and interaction weight u=0.15, compute the equilibrium nematic order parameter ψ = (ρ_x−ρ_y)/ρ as a function of total density ρ. Minimize the free energy numerically with respect to ρ_x and ρ_y subject to ρ_x+ρ_y=ρ, covering a sufficiently fine grid of ρ values to resolve the two transitions. Write the resulting (ρ, ψ) pairs to a CSV.
- Output file: `/app/outputs/order_parameter_vs_density.csv`
- Format: csv
- Contract: columns: density (float), order_parameter (float)
- Scoring: scored by hidden verifier

### Step 3: Phase Diagram Critical Densities
- Role: scored
- Action: For rod length k=6 and q=4, compute the critical densities ρ_c1 and ρ_c2 as functions of the interaction weight u. Determine the maximum u for which the nematic phase exists (u_c). For each u in a range from 0 to u_c, solve for the densities where the quadratic coefficient A2(ρ,u) of the free energy expansion around the isotropic point vanishes to obtain ρ_c1 and ρ_c2. Write the result (u, ρ_c1, ρ_c2) to a CSV.
- Output file: `/app/outputs/phase_diagram_critical_densities.csv`
- Format: csv
- Contract: columns: u (float), rho_c1 (float), rho_c2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/order_parameter_vs_density.csv`
- `/app/outputs/phase_diagram_critical_densities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### order_parameter_vs_density.csv
- path: `/app/outputs/order_parameter_vs_density.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Order parameter ψ as a function of total density ρ for k=6, u=0.15. The checker will extract the densities where ψ departs from zero and returns to zero, and compare those critical densities to reference values.
- schema:
  - `type`: table
  - `required_columns`: `density`, `order_parameter`
  - `items`:
    - `density`: float
    - `order_parameter`: float

### phase_diagram_critical_densities.csv
- path: `/app/outputs/phase_diagram_critical_densities.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Critical densities ρ_c1 and ρ_c2 as functions of interaction weight u for k=6, q=4. The checker will compare the computed values at sampled u against paper-reported references.
- schema:
  - `type`: table
  - `required_columns`: `u`, `rho_c1`, `rho_c2`
  - `items`:
    - `u`: float
    - `rho_c1`: float
    - `rho_c2`: float

Notes: The task covers only the q=4 case; the free energy expressions for q>=6 are not fully provided in the paper and are omitted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "order_parameter_vs_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "density",
          "order_parameter"
        ],
        "items": {
          "density": "float",
          "order_parameter": "float"
        }
      },
      "description": "Order parameter ψ as a function of total density ρ for k=6, u=0.15. The checker will extract the densities where ψ departs from zero and returns to zero, and compare those critical densities to reference values."
    },
    {
      "file": "phase_diagram_critical_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "u",
          "rho_c1",
          "rho_c2"
        ],
        "items": {
          "u": "float",
          "rho_c1": "float",
          "rho_c2": "float"
        }
      },
      "description": "Critical densities ρ_c1 and ρ_c2 as functions of interaction weight u for k=6, q=4. The checker will compare the computed values at sampled u against paper-reported references."
    }
  ],
  "notes": "The task covers only the q=4 case; the free energy expressions for q>=6 are not fully provided in the paper and are omitted."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output. For `order_parameter_vs_density.csv`, it extracts the densities at which the order parameter departs from and returns to zero and compares them to reference values, awarding partial credit based on accuracy. For `phase_diagram_critical_densities.csv`, it compares the computed ρ_c1 and ρ_c2 at several u values to reference values. Each stage contributes a weighted fraction to the final reward. The verifier does not simply check for matching numbers; it reconstructs the relevant quantities from your CSV and measures how well they align with the expected physical behaviour.
