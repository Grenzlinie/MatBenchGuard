# Hard-Sphere Fluid-Solid Coexistence and Crystal Stability Using GELA

## Problem background
Classical density-functional theory describes the equilibrium thermodynamics of nonuniform systems such as crystalline solids. A key challenge is to predict the free energy and phase behavior of a crystal using only knowledge of the uniform fluid. The generalized effective liquid approximation (GELA) maps the excess thermodynamic properties of the solid onto those of an effective liquid, requiring only the direct correlation function of the uniform fluid as input. When applied to the hard-sphere system, this theory yields quantitative predictions for fluid–face-centered-cubic (fcc) solid coexistence and for the relative stability of body-centered-cubic (bcc) and simple-cubic (sc) crystals.

## Approach
The GELA excess free energy functional is expressed in terms of the fluid’s direct correlation function evaluated at an effective density. That effective density is defined self-consistently as a functional of the local solid density. For hard spheres, the solid density is represented by a sum of Gaussian peaks centered on the lattice sites of the fcc crystal; the Gaussian width α acts as the order parameter. The fluid input is the analytic Percus–Yevick hard-sphere direct correlation function, and the uniform-fluid equation of state is the Carnahan–Starling form. Using these, the spatial integrals in the GELA functional are evaluated analytically, giving closed-form expressions for the free energy and the effective density in terms of the average solid density ρS and α. The effective density is then solved numerically by iterating the self-consistency condition. With the free energy and pressure of the fcc, bcc, and sc crystals computed as functions of the packing fraction η, the fluid–fcc solid coexistence is located by a common-tangent construction (equating chemical potentials and pressures). Finally, the free energies of the three cubic phases are compared at a density near coexistence to determine their relative stability ordering.

## Reproduction target
Compute the fluid–fcc solid coexistence parameters for the hard-sphere system using the GELA approximation: the fluid and solid packing fractions η_F and η_S, the density change Δρ* = ρ*_S − ρ*_F, the reduced coexistence pressure P* = β P σ³, the entropy change per particle Δs/k_B, and the Lindemann parameter L. Additionally, determine the stability ordering of the fcc, bcc, and sc hard-sphere crystals, listing the phases from most stable to least stable near the solid coexistence density.

## Assets

- Percus–Yevick hard-sphere direct correlation function
- Carnahan–Starling hard-sphere equation of state

## Workflow steps

### Step 1: Analytic evaluation of GELA integrals
- Role: process
- Action: Implement the GELA excess free energy and effective density definition for the hard-sphere system. Use the Gaussian-peak parametrization of the solid density and the Percus–Yevick direct correlation function to evaluate the spatial integrals analytically, obtaining closed-form expressions for the free energy and the effective density function in terms of the order parameter α and average solid density ρ_S.
- Evidence: `/app/outputs/analytic_integration_note.txt`

### Step 2: Numerical solution for effective density
- Role: process
- Action: Solve the coupled equations for the effective liquid density ρ̂(α,ρ_S) numerically. At each (α,ρ_S) pair, iterate the self-consistency condition defined by the analytic expressions until convergence, producing a tabulated mapping.
- Evidence: `/app/outputs/effective_density_table.csv`

### Step 3: Free energy and pressure computation for cubic crystals
- Role: process
- Action: Using the analytic free energy expression and the numerically solved ρ̂, compute the Helmholtz free energy and reduced pressure P* = β P σ³ of the perfect fcc, bcc, and sc hard-sphere crystals as functions of packing fraction η = π σ³ ρ_S / 6. For each phase and each density, minimize the free energy with respect to the order parameter α to obtain the equilibrium thermodynamic values. Record the optimal α, free energy, and pressure.
- Evidence: `/app/outputs/free_energy_pressure.csv`

### Step 4: Fluid–fcc solid coexistence determination
- Role: scored (load-bearing)
- Action: Using the solid free energy and pressure from the previous step and the Carnahan–Starling fluid equation of state, perform a common-tangent construction (or equate chemical potentials and pressures) to locate the fluid–fcc solid coexistence. Extract the coexisting fluid and solid packing fractions η_F, η_S, the density change Δρ*, the coexistence reduced pressure P*, the entropy change per particle Δs/k_B, and the Lindemann parameter L from the optimal α at coexistence. Write these six values to the output file.
- Output file: `/app/outputs/coexistence_parameters.json`
- Format: json
- Contract: JSON object with keys: eta_F (float), eta_S (float), Delta_rho_star (float), P_star (float), Delta_s_over_kB (float), L (float).
- Scoring: scored by hidden verifier

### Step 5: Phase stability ordering of cubic crystals
- Role: scored
- Action: From the free energy data in step_3, compare the equilibrium free energies of the fcc, bcc, and sc phases at a density near the solid coexistence (e.g., at η ≈ η_S). Determine the stability ordering (most stable → least stable) and output it as an ordered list.
- Output file: `/app/outputs/phase_stability.json`
- Format: json
- Contract: JSON object with key 'phase_order': array of strings in order of decreasing stability (most stable first).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coexistence_parameters.json`
- `/app/outputs/phase_stability.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coexistence_parameters.json
- path: `/app/outputs/coexistence_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fluid-fcc solid coexistence parameters (packing fractions, density change, coexistence pressure, entropy change per particle, Lindemann parameter) computed using the GELA theory. The checker compares each parameter to the paper's reference values with appropriate numerical tolerances.
- schema:
  - `type`: object
  - `required`:
    - `eta_F`: float
    - `eta_S`: float
    - `Delta_rho_star`: float
    - `P_star`: float
    - `Delta_s_over_kB`: float
    - `L`: float

### phase_stability.json
- path: `/app/outputs/phase_stability.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Ordered list of the cubic phases (fcc, bcc, sc) from most stable to least stable, as predicted by the GELA theory. The checker verifies the ordering.
- schema:
  - `type`: object
  - `required`:
    - `phase_order`: array of strings

Notes: The coexistence parameters are compared against the paper's published GELA results. The phase stability ordering is checked against the expected sequence (fcc > bcc > sc).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coexistence_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "eta_F": "float",
          "eta_S": "float",
          "Delta_rho_star": "float",
          "P_star": "float",
          "Delta_s_over_kB": "float",
          "L": "float"
        }
      },
      "description": "Fluid-fcc solid coexistence parameters (packing fractions, density change, coexistence pressure, entropy change per particle, Lindemann parameter) computed using the GELA theory. The checker compares each parameter to the paper's reference values with appropriate numerical tolerances."
    },
    {
      "file": "phase_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "phase_order": "array of strings"
        }
      },
      "description": "Ordered list of the cubic phases (fcc, bcc, sc) from most stable to least stable, as predicted by the GELA theory. The checker verifies the ordering."
    }
  ],
  "notes": "The coexistence parameters are compared against the paper's published GELA results. The phase stability ordering is checked against the expected sequence (fcc > bcc > sc)."
}
```

## How you are scored
A hidden verifier inspects the artifacts you produce and assigns a reward between 0 and 1. For the coexistence parameters, each of the six quantities is compared against a reference value using an appropriate numerical tolerance; the reward increases with the number of parameters within tolerance. For the phase stability file, the verifier checks that the phase_order list matches the expected ordering. The final reward is a weighted combination of the two checks. Simply reporting the paper’s numbers without running the full computation will not suffice; the verifier reads the actual output files you write.
