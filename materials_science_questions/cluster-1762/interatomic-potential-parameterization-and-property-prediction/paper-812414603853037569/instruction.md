# Defect energetics of vacancies in β-SiC

## Problem background
Quantifying point-defect energetics in covalent ceramics like β‑SiC is essential for understanding radiation‑damage evolution and diffusion‑controlled processes. This task develops a hybrid two‑body plus three‑body interatomic potential for β‑SiC and uses it to compute formation energies, migration barriers, attempt frequencies, and vacancy‑mediated diffusion coefficients for silicon and carbon vacancies. The goal is to compare the predicted activation energies and pre‑exponential factors with experimental self‑diffusion data to validate the potential and computational protocol.

## Approach
Implement the interatomic potential using the two‑body (Lennard‑Jones type) and three‑body (Axilrod‑Teller) parameters given below. The two‑body interaction for each atom pair is of the form
V^(2)(r) = (ε/(m-n))[n(R0/r)^m - m(R0/r)^n]
with m=12, n=6. The three‑body term for each triplet is
V^(3)(r_ij, r_ik, r_jk) = Z (1 + 3 cosθ_ij cosθ_ik cosθ_jk) / (r_ij r_ik r_jk)^3.
The numerical parameters are:

| Pair | ε (eV) | R0 (Å) |
|------|--------|--------|
| Si-Si | 2.817 | 2.2951 |
| Si-C | 3.895 | 1.7400 |
| C-C | 5.437 | 1.4806 |

| Triplet | Z (eV·Å^9) |
|---------|------------|
| Si-Si-Si | 3484.0 |
| Si-Si-C | 796.8 |
| Si-C-C | 597.5 |
| C-C-C | 167.3 |

Use these parameters exactly. Build a β‑SiC microcrystal computational cell with inner mobile atoms and a boundary layer that exceed the potential cutoff; apply external balancing forces to the boundary to mimic an infinite crystal. Relax the perfect crystal via molecular dynamics with velocity quenching to obtain the reference potential energy. Introduce a silicon vacancy and a carbon vacancy separately, relax each defected cell, and compute the formation energy as the relaxed energy difference from the perfect reference. For each vacancy, identify the equilibrium and saddle‑point configurations along a plausible migration path, relax the saddle point, and obtain the migration energy as the barrier height. From the energy profile curvature near equilibrium compute the attempt frequency using a Debye‑like formula with the migrating atom’s mass, then calculate the diffusion pre‑exponential factor using the jump distance and number of equivalent nearest‑neighbor jumps. Collect the computed quantities into a CSV file.

## Reproduction target
Write a CSV file containing, for the silicon vacancy and the carbon vacancy, the formation energy (eV), migration energy (eV), and diffusion pre‑exponential factor (cm²/s). The results will be evaluated by a hidden verifier against reference data. The verifier will also compute the activation energy (formation + migration) internally; you do not need to include it in the CSV.

## Assets

- Atomic Simulation Environment (ASE): ase
- β-SiC zincblende structure and lattice constant

## Workflow steps

### Step 1: Construct computational cell and relax perfect crystal
- Role: process
- Action: Build a β-SiC microcrystal computational cell with inner mobile atoms and a boundary layer of fixed/flexible atoms that exceed the potential cutoff. Apply external balancing forces to boundary atoms to mimic an infinite crystal. Relax the perfect crystal via molecular dynamics with velocity quenching to obtain the reference potential energy.
- Evidence: none

### Step 2: Compute defect formation energies
- Role: process
- Action: Introduce a silicon vacancy (remove a Si atom) and a carbon vacancy (remove a C atom) separately into the pre-relaxed perfect cell. Relax each defected configuration via MD with velocity quenching. Compute the defect formation energy as the relaxed potential-energy difference between the defected cell and the perfect reference cell.
- Evidence: none

### Step 3: Compute defect migration energies
- Role: process
- Action: For each vacancy, identify the equilibrium and saddle-point configurations along a plausible migration path (e.g., V_Si → T_Si → nearest Si lattice, or analogous for C), relax the saddle-point configuration, and compute the migration energy as E_mig = E_saddle - E_eq.
- Evidence: none

### Step 4: Compute attempt frequencies and diffusion pre-exponential factors
- Role: process
- Action: From the potential energy profile along the migration coordinate near the equilibrium position, estimate the curvature d²E/dx². Compute the attempt frequency using the Debye-like formula ν = (1/(2π))√[(1/m) d²E/dx²] with the mass of the migrating atom. Then compute the diffusion pre-exponential factor D0 = (1/6) λ² δ ν, where λ = (√2/2)a₀ is the jump distance and δ = 12 is the number of equivalent nearest-neighbor jumps.
- Evidence: none

### Step 5: Output scored defect properties
- Role: scored (load-bearing)
- Action: Collect the computed formation_energy (eV), migration_energy (eV), and diffusion_prefactor (cm²/s) for the silicon vacancy and the carbon vacancy into a CSV file.
- Output file: `/app/outputs/defect_energies.csv`
- Format: csv
- Contract: columns: defect (string; must be exactly "Si vacancy" or "C vacancy"), formation_energy (float, eV), migration_energy (float, eV), diffusion_prefactor (float, cm²/s)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_energies.csv
- path: `/app/outputs/defect_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with two rows (Si vacancy and C vacancy) containing the computed formation energy, migration energy, and diffusion pre-exponential factor. The checker will compare each numeric column to a hidden reference derived from the paper's reported values.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `formation_energy`, `migration_energy`, `diffusion_prefactor`
  - `units`:
    - `formation_energy`: eV
    - `migration_energy`: eV
    - `diffusion_prefactor`: cm²/s

Notes: Only Si and C vacancies are scored; He-related defects and complex clusters are not required. The checker computes activation energy internally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "formation_energy",
          "migration_energy",
          "diffusion_prefactor"
        ],
        "units": {
          "formation_energy": "eV",
          "migration_energy": "eV",
          "diffusion_prefactor": "cm²/s"
        }
      },
      "description": "CSV file with two rows (Si vacancy and C vacancy) containing the computed formation energy, migration energy, and diffusion pre-exponential factor. The checker will compare each numeric column to a hidden reference derived from the paper's reported values."
    }
  ],
  "notes": "Only Si and C vacancies are scored; He-related defects and complex clusters are not required. The checker computes activation energy internally."
}
```

## How you are scored
A hidden verifier will read your submitted defect_energies.csv and compare each numeric value (formation energy, migration energy, diffusion pre‑exponential factor) to hidden reference values. The verifier will also compute the activation energy (formation + migration) from your reported energies and compare it to a hidden reference. Each comparand is assessed using a relative tolerance. The final reward is the fraction of comparands that meet the tolerance; higher is better. Reporting a number alone is not sufficient – the verifier checks the actual computed values.
