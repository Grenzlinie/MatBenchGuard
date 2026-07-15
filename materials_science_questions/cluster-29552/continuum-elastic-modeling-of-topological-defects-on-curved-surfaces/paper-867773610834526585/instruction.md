# Escaped‑Twist Director Configuration and Defect Energetics in Liquid Crystal Capillaries

## Problem background
Lyotropic chromonic liquid crystals (LCLCs) confined in cylindrical capillaries with degenerate planar boundary conditions can adopt a variety of director configurations depending on the elastic constants. The Frank free energy includes a saddle‑splay term with modulus K24 that, under the right conditions, can stabilize a chiral escaped‑twist (ET) configuration. When the saddle‑splay modulus is sufficiently large compared to the twist modulus, the ET configuration can spontaneously break chiral symmetry, yielding a twist profile β(r) that is zero on axis and reaches a finite tilt angle β₁ = β(r=R) at the capillary wall. The free energy of the ET state depends on the ratios of the elastic moduli. In longer capillaries, domains of opposite handedness are separated by topological defects; the system can accommodate either point defects or smooth domain walls. Understanding the phase diagram of the surface tilt angle and the relative energies of these defect structures is essential for interpreting experimental observations and for determining the saddle‑splay modulus.

## Approach
The task proceeds in two parts: analytical and numerical.

1. **Analytical escaped‑twist solution.** Using the Frank free energy with the saddle‑splay term and assuming the director depends only on the radial coordinate r (α = π/2 throughout the capillary), the Euler–Lagrange equations yield an analytical expression for the tilt angle β(r). The boundary condition at the capillary surface involves K24 and K2. From this solution, the surface tilt angle β₁ and the normalized free energy per unit length, F/(πL), can be evaluated for any combination of elastic ratios K24/K2 and K3/K2 (K₁ does not appear because there is no splay in this configuration). You will compute these quantities over a grid of (K24/K2, K3/K2) to map out the phase diagram.

2. **Numerical defect energies.** When separate regions of opposite ET handedness meet, the director field becomes fully 2‑D (r, z). You will implement the full Frank free energy functional in cylindrical coordinates, including the saddle‑splay contribution, on a finite‑difference grid. Using a relaxational technique (such as gradient‑descent or Newton‑based iteration), you will find equilibrium director fields for two types of defect:
   - a *point defect* (hedgehog) configuration,
   - a *domain wall* configuration that smoothly reverses the handedness.
   For each configuration, you will compute the total elastic energy in units of πRK, where R is the capillary radius and K is the common splay/bend modulus (K₁ = K₃ ≡ K). The twist and saddle‑splay moduli are set to K₂/K = 0.1 and varying K₂₄/K. By comparing the energies of the two defect types, you will identify the crossover value of K₂₄/K beyond which point defects become energetically favored over domain walls.

## Reproduction target
Produce the following two scored artifacts:

- **phase_diagram.csv**: For a grid of K24/K2 values from 2.0 to 10.0 and K3/K2 values from 1.0 to 10.0 (at least 20 points per dimension), provide the computed surface tilt angle β₁ in radians and the normalized free energy per πL. This maps out the ET phase diagram.

- **defect_energies.csv**: For K24/K ranging from 2 to 10 (at least 10 points) with fixed K2/K=0.1, K1/K=1.0, K3/K=1.0, provide the numerically computed elastic energies (in units of πRK) of the point defect and the domain wall. Use these energies to determine the crossover K24/K where point defects become more stable than domain walls.

The verifier will check that the analytical values are consistent with the submitted elastic ratios and that the numerical energies exhibit the expected monotonic trends and crossover location.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Analytical escaped‑twist solution and phase diagram
- Role: scored
- Action: Implement the analytical escaped‑twist director profile β(r) and the normalized free energy per length from the Frank free energy functional. For a grid of elastic constant ratios (K24/K2 from 2.0 to 10.0, K3/K2 from 1.0 to 10.0, at least 20 points each), compute the surface tilt angle β1 = β(r=R) in radians and the free energy per πL. Save the results to /app/outputs/phase_diagram.csv.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: CSV with columns: K24_over_K2 (float), K3_over_K2 (float), beta1_rad (float), free_energy_per_piL (float). Include a header.
- Scoring: scored by hidden verifier

### Step 2: Numerical defect energy calculation
- Role: scored (load-bearing)
- Action: Implement the Frank free energy functional in cylindrical coordinates including the saddle‑splay term on a 2D (r,z) domain. Numerically solve the Euler–Lagrange equations using a relaxational technique for point defect and domain wall configurations. For a range of K24/K values from 2 to 10 (at least 10 points) with fixed K1/K=1.0, K2/K=0.1, K3/K=1.0, compute the total elastic energy in units of πRK. Write the energies to /app/outputs/defect_energies.csv.
- Output file: `/app/outputs/defect_energies.csv`
- Format: csv
- Contract: CSV with columns: K24_over_K (float), energy_point (float), energy_wall (float). Energies in units of πRK. Include a header.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/defect_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase diagram of surface tilt angle and free energy from the analytical escaped‑twist solution. The checker recomputes the expected β1 and free energy from the submitted elastic constant ratios and compares the agent’s values to the recomputed references within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `K24_over_K2`, `K3_over_K2`, `beta1_rad`, `free_energy_per_piL`

### defect_energies.csv
- path: `/app/outputs/defect_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Defect energies from numerical relaxation. The checker verifies structural properties: columns present, energies monotonic (energy_point decreasing, energy_wall increasing with K24), and the crossover point near K24/K ≈ 4.0.
- schema:
  - `type`: table
  - `required_columns`: `K24_over_K`, `energy_point`, `energy_wall`

Notes: The task reproduces the two headline computational results of the paper: the analytical ET phase diagram and the numerical defect energetics. The checker reconstitutes the analytical reference from the agent‑provided parameter grid and uses structural heuristics for the simulation outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "K24_over_K2",
          "K3_over_K2",
          "beta1_rad",
          "free_energy_per_piL"
        ]
      },
      "description": "Phase diagram of surface tilt angle and free energy from the analytical escaped‑twist solution. The checker recomputes the expected β1 and free energy from the submitted elastic constant ratios and compares the agent’s values to the recomputed references within a tolerance."
    },
    {
      "file": "defect_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "K24_over_K",
          "energy_point",
          "energy_wall"
        ]
      },
      "description": "Defect energies from numerical relaxation. The checker verifies structural properties: columns present, energies monotonic (energy_point decreasing, energy_wall increasing with K24), and the crossover point near K24/K ≈ 4.0."
    }
  ],
  "notes": "The task reproduces the two headline computational results of the paper: the analytical ET phase diagram and the numerical defect energetics. The checker reconstitutes the analytical reference from the agent‑provided parameter grid and uses structural heuristics for the simulation outputs."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that scores each workflow stage independently.

- **Step 1 (phase_diagram.csv)**: The verifier recomputes β₁ and the free energy per πL from the elastic constant ratios you supply, using the analytical expressions. Your reported values are compared to the recomputed references within an appropriate tolerance. Accurate values earn credit; systematic deviations lead to reduced reward.

- **Step 2 (defect_energies.csv)**: The verifier performs a structural audit. It confirms the CSV columns, checks that the energies are monotonic functions of K24/K (energy_point decreases, energy_wall increases), and verifies that the crossover point lies in the expected region. Correct trends and crossover location earn full credit for this load‑bearing step.

The two stage scores are combined with weights (the majority from the load‑bearing step). Simply reporting the paper’s numbers is not sufficient; the verifier requires re‑derivable results consistent with a correct implementation.
