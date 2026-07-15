# Dislocation Core Energetics in Wurtzite InN via Stillinger-Weber Potential

## Problem background
Wurtzite InN is a promising material for optoelectronic devices, but high densities of threading dislocations degrade performance. Understanding the atomic-scale core structures and relative stability of a‑edge dislocations (Burgers vector 1/3[1‑210], line [0001]) is essential for controlling material quality. This task investigates the dislocation core energetics using a Stillinger‑Weber (SW) interatomic potential fitted to InN. All SW parameters for In–N, In–In, and N–N bonds are provided, so the agent need only implement the potential form. The target is to compute the core energies for the three experimentally accessible core configurations and determine which configuration is the most stable.

## Approach
The simulation follows a standard dislocation modelling workflow. First, a large wurtzite InN supercell is built with periodic boundaries along the dislocation line and fixed boundaries perpendicular to it. An isotropic linear elasticity displacement field for an a‑edge dislocation is then imposed on the perfect lattice, with three different origins chosen between specific (10‑10) lattice planes to generate three distinct core topologies. Each configuration is relaxed using quench molecular dynamics with the supplied SW potential: the atomic positions are integrated via a velocity‑Verlet algorithm while velocities are aggressively rescaled until the system reaches an effective temperature below a very low threshold, indicating convergence to a local energy minimum. For each relaxed core, the total energy is computed within cylindrical shells of increasing radius centred on the dislocation line. The far‑field linear elastic behaviour allows the energy to be written as a logarithmic function of radius; the linear portion of the plot of total energy versus the natural logarithm of radius is fitted to extract the core energy. The three core energies are then compared, and the core with the lowest energy is identified as the most stable configuration.

### SW potential specification

The potential is of the Stillinger‑Weber form with two-body and three-body terms. The total energy is φ = φ₂ + φ₃ with:
- φ₂(rᵢⱼ) = ε A (B (rᵢⱼ/σ)⁻⁴ - 1) exp[1/(rᵢⱼ/σ - a)] for rᵢⱼ/σ < a, 0 otherwise.
- φ₃(i,j,k) = ε (hᵢⱼₖ + hⱼᵢₖ + hⱼₖᵢ) where hᵢⱼₖ = exp[γ( (rᵢⱼ/σ - a)⁻¹ + (rⱼₖ/σ - a)⁻¹ )] (cos θᵢⱼₖ + 1/3)² for each bond length less than the cutoff, 0 otherwise.

The parameters are:

| Parameter | In–N   | In–In  | N–N    |
|-----------|--------|--------|--------|
| A         | 7.755  | 7.755  | 7.718  |
| B         | 0.699  | 0.699  | 0.694  |
| a         | 1.8    | 1.8    | 1.8    |
| γ         | 1.2    | 1.2    | 1.2    |
| λ         | 18.5   | 18.5   | 28.5   |
| ε (eV)    | 1.99   | 1.40   | 1.24   |
| σ (Å)     | 1.879  | 2.430  | 1.333  |

The cutoff radius for each bond type is a·σ. The two-body term applies to all atom pairs within the cutoff; the three-body term applies to all triplets where both rᵢⱼ and rⱼₖ are within the cutoff. Implement this functional form with the given parameters to compute energies and forces.

## Reproduction target
Reproduce the dislocation core energy analysis by: (1) constructing the initial supercell with the dislocation displacement fields for three different origins to generate three core geometries; (2) relaxing each configuration with quench MD using the provided SW potential parameters; (3) computing the total energy as a function of radial distance from the dislocation line for each relaxed core, fitting the linear regime to obtain the core energy, and writing the three core energies together with the identity of the most stable (lowest energy) core to the scored output file `/app/outputs/core_energies.json`.

## Assets

- Molecular dynamics simulation environment
- Linear fitting and numerical analysis library

## Workflow steps

### Step 1: Set up dislocation configurations
- Role: process
- Action: Construct a wurtzite InN supercell (61×61√3/2×2 unit cells) with periodic boundaries along [0001] and fixed boundaries otherwise. Introduce an a-edge dislocation (Burgers vector 1/3[1-210], line [0001], glide plane (10-10)) by imposing isotropic linear elasticity displacement fields for three different origins (P1, P2, P3) to generate four-, eight-, and five/seven-atom cores.
- Evidence: `/app/outputs/initial_configurations.log`

### Step 2: Relax cores with quench molecular dynamics
- Role: process
- Action: Using the supplied SW potential parameters, relax each initial configuration via quench molecular dynamics (velocity-Verlet integrator with aggressive velocity scaling) until the thermodynamic temperature falls below 1e-7 K.
- Evidence: `/app/outputs/relaxed_cores.xyz`

### Step 3: Extract core energies and stability
- Role: scored (load-bearing)
- Action: For each relaxed core, compute the total energy E_total(R) within cylindrical regions of increasing radius R centered on the dislocation line. Plot E_total vs ln(R) and fit the linear regime to E_total = Ath ln(R/rc) + Ec. Extract the core energy Ec for the four-atom, five/seven-atom, and eight-atom cores. Identify which core has the smallest Ec.
- Output file: `/app/outputs/core_energies.json`
- Format: json
- Contract: {
  "core_energies": {
    "four_atom": <float (eV)>,
    "five_seven_atom": <float (eV)>,
    "eight_atom": <float (eV)>
  },
  "most_stable_core": "four"
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/core_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### core_energies.json
- path: `/app/outputs/core_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The agent's computed core energies (Ec) for the three a-edge dislocation core configurations and the identification of the most stable core.
- schema:
  - `type`: object
  - `required`: `core_energies`, `most_stable_core`
  - `properties`:
    - `core_energies`:
      - `type`: object
      - `required`: `four_atom`, `five_seven_atom`, `eight_atom`
      - `properties`:
        - `four_atom`:
          - `type`: number
          - `unit`: eV
        - `five_seven_atom`:
          - `type`: number
          - `unit`: eV
        - `eight_atom`:
          - `type`: number
          - `unit`: eV
    - `most_stable_core`:
      - `type`: string

Notes: The checker verifies the computed core energies and most stable core against the paper-reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "core_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "core_energies",
          "most_stable_core"
        ],
        "properties": {
          "core_energies": {
            "type": "object",
            "required": [
              "four_atom",
              "five_seven_atom",
              "eight_atom"
            ],
            "properties": {
              "four_atom": {
                "type": "number",
                "unit": "eV"
              },
              "five_seven_atom": {
                "type": "number",
                "unit": "eV"
              },
              "eight_atom": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "most_stable_core": {
            "type": "string"
          }
        }
      },
      "description": "The agent's computed core energies (Ec) for the three a-edge dislocation core configurations and the identification of the most stable core."
    }
  ],
  "notes": "The checker verifies the computed core energies and most stable core against the paper-reported values."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the required output files from `/app/outputs`. The verifier does not rely on self‑reported aggregates alone; it independently checks the structural evidence and the final reported core energies. Correctness is determined by comparing your extracted core energies and the stability ordering against reference values derived from the original work, using appropriate tolerances that accommodate legitimate implementation differences. Note that the verifier checks that the procedure was followed and that the reported numbers are consistent with evidence artifacts (e.g., relaxed structure files, energy‑radius plots). The final reward is a weighted combination of the scores for each workflow stage; simply reporting a number without executing the required steps will not yield a high score.
