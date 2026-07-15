# Monte Carlo Simulation of Polymer Brush Mechanical Response

## Problem background
Surfaces that are modified by grafting polymer chains can change mechanical properties without altering the bulk material. This work models a polymer brush on an elastic substrate, treating the brush as a discrete lattice of rotators with orientational (Keesom) interactions and a Lennard-Jones potential, while the substrate obeys Hooke's law. Monte Carlo simulations are used to compute the equilibrium response when the system is stretched. The open question is how the brush influences the effective force and Young's modulus of the composite as a function of the applied strain and the strength of inter-chain coupling.

## Approach
Implement the hybrid discrete-continuum model: a three-dimensional lattice of rigid rotators of length *l* that interact via an orientation-dependent dipole potential (Keesom energy) with parameters K₁ (longitudinal), K₂ (strain-dependent transverse) and K₃ (constant transverse), plus a Lennard-Jones contribution. The substrate provides an elastic restoring energy proportional to the square of the displacement. Normalize all energies by K₁ and lengths by the mean interatomic distance *a*. Set up the lattice with periodic boundaries in one transverse direction, a fixed attachment at the substrate, and free upper ends. Perform quasistatic loading: at each small strain increment, run Metropolis Monte Carlo equilibration at a fixed normalized temperature T* to obtain the total equilibrium energy. From the strain-dependent energy, apply work–energy relations to extract the normalized force and normalized Young's modulus. Explore three values of the inter-chain coupling K₃ (0.1, 0.05, 0.01, with K₁ = 1) to compare the mechanical response curves. The approach does not require an external dataset; the simulation itself is the experiment.

## Reproduction target
Compute and output the normalized force (*F·a/K₁*) and normalized Young's modulus (*E/E₀*, where *E₀* is the substrate modulus) as functions of the relative strain (*Δx/x₀*) for three values of the transverse coupling parameter: *K₃* = 0.1, 0.05, and 0.01, with *K₁* = 1 and normalized temperature *T** = 0.1. Use a representative lattice size (e.g., *N₁* = *N₂* = *N₃* ≈ 10). The results must be written to a CSV file with columns: K3, strain, force_normalized, youngs_modulus_normalized. Each row corresponds to one strain step for one *K₃* value. The curves should be produced by the simulation workflow described in the steps below.

## Assets

- Python 3: python
- NumPy: numpy

## Workflow steps

### Step 1: Monte Carlo simulation of stretching
- Role: process
- Action: Implement the Hamiltonian (orientational interactions with K₁, K₂(r), K₃, Lennard-Jones potential, and substrate elastic energy), normalize by K₁ and a. Set up a lattice of rotators with N₁=N₂=N₃≈10, periodic boundary conditions in n₃, fixed attachment at substrate, free upper ends. For each quasistatic strain step and for K₃ ∈ {0.1, 0.05, 0.01} at K₁=1, run Metropolis Monte Carlo equilibration at T*=0.1. Record the equilibrium total energy at every strain.
- Evidence: `/app/outputs/energy_curves.csv`

### Step 2: Extract force and Young's modulus
- Role: scored (load-bearing)
- Action: From the recorded equilibrium energies for each K₃ and strain, apply the work–energy relations A = −ΔH, and A = −F Δx/2 = −(E/2)(Δx/x₀)² to compute normalized force (F·a/K₁) and normalized Young's modulus (E/E₀) as functions of strain. Export the results as a CSV file.
- Output file: `/app/outputs/mechanical_curves.csv`
- Format: csv
- Contract: CSV with header: K3, strain, force_normalized, youngs_modulus_normalized. Each row corresponds to one strain step for one K₃ value. All columns are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_curves.csv
- path: `/app/outputs/mechanical_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized force (F·a/K₁) and normalized Young's modulus (E/E₀) as functions of relative strain for K₃ = 0.1, 0.05, 0.01. Each row is a strain step for one K₃ value.
- schema:
  - `type`: table
  - `required_columns`: `K3`, `strain`, `force_normalized`, `youngs_modulus_normalized`

Notes: The structural scoring verifies that for each K₃ the force–strain curve shows a peak at low strain followed by a plateau, and the Young's modulus–strain curve decreases monotonically from an elevated value toward 1 (substrate-dominated). Relative ordering is checked: lower K₃ gives a weaker coating effect (lower peak force and faster modulus decline).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "K3",
          "strain",
          "force_normalized",
          "youngs_modulus_normalized"
        ]
      },
      "description": "Normalized force (F·a/K₁) and normalized Young's modulus (E/E₀) as functions of relative strain for K₃ = 0.1, 0.05, 0.01. Each row is a strain step for one K₃ value."
    }
  ],
  "notes": "The structural scoring verifies that for each K₃ the force–strain curve shows a peak at low strain followed by a plateau, and the Young's modulus–strain curve decreases monotonically from an elevated value toward 1 (substrate-dominated). Relative ordering is checked: lower K₃ gives a weaker coating effect (lower peak force and faster modulus decline)."
}
```

## How you are scored
A hidden verifier examines the submitted `mechanical_curves.csv` independently. The scoring is based on structural properties of the curves, not on matching specific numeric values. For each *K₃*, the force–strain curve must display a peak at low strain followed by a plateau, and the modulus–strain curve must decrease monotonically from an elevated value towards 1 (the substrate value). Additionally, the relative ordering across *K₃* values is checked: a smaller *K₃* should produce a weaker coating effect (lower peak force and faster decline of the modulus). The verifier may use internal cross-checks derived from the energy data recorded during the simulation. The final reward combines the results of these checks.
