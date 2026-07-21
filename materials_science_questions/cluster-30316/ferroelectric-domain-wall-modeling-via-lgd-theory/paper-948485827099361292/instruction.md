# 2D Discommensuration Optimization via Ginzburg-Landau Theory

## Problem background
Charge density waves (CDWs) in quasi-two-dimensional materials can form discommensuration patterns—ordered arrays of commensurate patches separated by domain walls (phase slips). McMillan's original Ginzburg–Landau theory described these structures in an effectively one‑dimensional setting, where domain walls are constrained to be perpendicular to the CDW wave vector. In realistic two‑dimensional crystals, however, the CDW freedom includes both dilatational and curl elastic energies, which may cause the domain walls to rotate. This task implements a fully two‑dimensional Ginzburg–Landau model for a single‑component CDW on a hexagonal lattice. Using a discommensuration ansatz based on the Jacobi amplitude function, it numerically determines the optimal domain wall orientation (slope parameter S) and the free energy ordering of the discommensuration phase relative to the uniform incommensurate (IC‑CDW) and commensurate (C‑CDW) phases at five temperatures.

## Approach
We consider the single‑Q Ginzburg–Landau free energy functional in two dimensions, consisting of terms that describe the lock‑in energy, the dilatational elastic energy (coefficient e₀), and the curl elastic energy (coefficient f₀). The discommensuration phase is modelled by the order parameter ψ = ψ₀ exp(i(φ(x,y) − C·r)), where C is the nearest commensurate wave vector and the phase is given by the Jacobi amplitude function: φ(x,y) = (2/3) am(c₁(x+Sy)+c₂, m) + π/3. The parameter m depends on ψ₀, b₁, e₀, f₀, c₁, the preferred incommensurate wave vector Q, and the slope S. This ansatz produces a staircase‑like phase with steps of 2π/3 at domain walls. The slope S controls the wall orientation; when S = √3 the walls are perpendicular to Q, while other values correspond to rotated walls.

The hexagonal atomic lattice is defined by the basis vectors a₁ = (√3/2, 1/2) and a₂ = (-√3/2, 1/2) with lattice constant a₀ = 1 (the coupling constants are dimensionless and the scale cancels). The shortest reciprocal lattice vector is K⁽¹⁾ = 2π (1/√3, 1). The preferred incommensurate CDW wave vector is Q₁ = (π/2.55)(1, √3), and the nearest commensurate wave vector is C = K⁽¹⁾/3 = (2π/3)(1/√3, 1). In the elastic energy terms, Q refers to Q₁.

The free energy is minimised on a discretised two‑dimensional lattice of at least 200×200 sites with periodic boundary conditions, using the hexagonal lattice vectors a₁,a₂ and the CDW wave vector Q₁. For completeness we also compute the free energy densities of the uniform IC‑CDW (phase gradient constant, q=Q) and the uniform C‑CDW (phase constant, q locked to the lattice). At each temperature T = 0.0, 0.35, 0.45, 0.7, 1.0, a numerical optimisation routine (e.g., Nelder–Mead) searches for the parameters (ψ₀, c₁, c₂, S) that minimise the spatially averaged free energy density of the discommensuration ansatz. The values of the three free energy densities for the optimised discommensuration and the two uniform reference states are recorded.

## Reproduction target
Produce a JSON file results.json containing the optimised parameters and free energy densities for the five specified temperatures. Each entry must include the temperature, the optimised slope S, the parameters c₁ and ψ₀, and the three free energy densities: free_energy_discomm (discommensuration ansatz), free_energy_ic (incommensurate CDW), and free_energy_cc (commensurate CDW). The verifier will examine the computed S at T=0.45 and the relative ordering of the free energies across the three phases at each temperature, comparing them against hidden reference values derived from the underlying physics. The objective is to determine whether the optimal domain wall orientation deviates from the purely geometric perpendicular direction and which CDW phase is thermodynamically stable at each temperature.

## Assets

- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Numerical optimization of the discommensuration ansatz
- Role: scored (load-bearing)
- Action: Implement the single-Q Ginzburg–Landau free energy functional for a two-dimensional CDW on a hexagonal lattice with the provided parameters (a'=0.01, b1=0.048, c0=0.04, e0=0.008, f0=0.002, Tc=4.5, lattice vectors a1, a2, CDW wave vector Q1). Define the phase ansatz φ(x,y) = (2/3) am(c₁(x+Sy)+c₂, m) + π/3 where m depends on ψ₀, b₁, e₀, f₀, c₁, Q, and S. Discretize a 2D domain of at least 200×200 sites with periodic boundary conditions. For temperatures T = 0.0, 0.35, 0.45, 0.7, 1.0: (a) compute the uniform incommensurate (IC-CDW) free energy density with constant phase gradient and the uniform commensurate (C-CDW) free energy density with phase locked to 2π/3; (b) perform numerical optimization (e.g., Nelder–Mead) to find the parameters (ψ₀, c₁, c₂, S) that minimize the spatially averaged free energy density of the discommensuration ansatz. Save the optimized parameters and the three free energy densities in a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: An array of five objects, one per temperature (T=0.0, 0.35, 0.45, 0.7, 1.0). Each object contains the keys: 'temperature' (float), 'S' (float, optimized slope parameter), 'c1' (float, optimized scale parameter), 'psi0' (float, optimized amplitude), 'free_energy_discomm' (float, spatially averaged free energy density of the discommensuration ansatz), 'free_energy_ic' (float, free energy density of the incommensurate CDW), 'free_energy_cc' (float, free energy density of the commensurate CDW). All free energy values are in the same units.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Agent's computed optimal parameters and phase free energies, checked against hidden gold thresholds derived from the paper.
- schema:
  - `type`: array
  - `items`:
    - `temperature`: float
    - `S`: float
    - `c1`: float
    - `psi0`: float
    - `free_energy_discomm`: float
    - `free_energy_ic`: float
    - `free_energy_cc`: float

Notes: The hidden checker verifies that the free energy ordering across the three CDW phases matches the expected physical trends and that the optimized slope S at T=0.45 deviates from √3 by a margin consistent with the paper's predictions. Detailed tolerance criteria are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "temperature": "float",
          "S": "float",
          "c1": "float",
          "psi0": "float",
          "free_energy_discomm": "float",
          "free_energy_ic": "float",
          "free_energy_cc": "float"
        }
      },
      "description": "Agent's computed optimal parameters and phase free energies, checked against hidden gold thresholds derived from the paper."
    }
  ],
  "notes": "The hidden checker verifies that the free energy ordering across the three CDW phases matches the expected physical trends and that the optimized slope S at T=0.45 deviates from √3 by a margin consistent with the paper's predictions. Detailed tolerance criteria are not disclosed."
}
```

## How you are scored
A hidden verifier reads your results.json and evaluates it against a set of reference checks. It does not require exact digit‑for‑digit reproduction; instead it uses tolerances that account for legitimate numerical differences arising from discretisation, optimisation, and implementation choices. The scoring incorporates several aspects: (1) whether the free energy densities obey the expected physical trend—in particular, which phase achieves the lowest free energy at low, intermediate, and high temperatures; (2) whether the optimised slope S at T=0.45 falls within a physically reasonable window. The verifier combines these tests into a reward between 0 and 1. Simply reporting numbers without performing the actual free energy minimisation will not pass the tolerance and trend checks, because the hidden references are derived from the true physical solution.
