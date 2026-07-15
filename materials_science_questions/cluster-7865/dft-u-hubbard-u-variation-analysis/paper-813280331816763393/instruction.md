# Pressure-induced ferromagnetic transition in BaFeO3: DFT+U helical spin energy and moment

## Problem background
Cubic perovskite BaFeO3 exhibits a helical spin order at ambient pressure. The spin configuration arises from a competition between double-exchange (DE) and superexchange (SE) interactions that couple Fe magnetic moments. Applying pressure reduces the lattice constant and modifies the balance of these interactions, potentially changing the stable spin order. Understanding how the spin order evolves with compression requires first‑principles electronic structure calculations that can capture the interplay of DE and SE as a function of lattice constant.

## Approach
We use density functional theory with an LSDA+U treatment (U = 4.0 eV, J = 0.9 eV) to account for the strong electron correlation on Fe. Noncollinear spin‑polarized calculations are performed for cubic BaFeO3 in a primitive cell. G‑type helical spin order is imposed via a wavevector q = (2π/a)(φ, φ, φ), where φ (in units of 2π) controls the pitch of the helix. For four lattice constants that span ambient to compressed regimes (a = 3.97, 3.85, 3.75, 3.70 Å), the total energy per unit cell and the Fe local spin moment are computed over a set of φ values ranging from 0 (ferromagnetic) to 0.20, with sufficient sampling to locate energy minima. The calculations are performed with an open‑source DFT code such as Quantum ESPRESSO, using standard pseudopotentials. This generates an energy landscape ΔE(φ) = E(φ) − E(φ=0) that reveals the preferred spin order at each compression, together with the associated Fe moment.

## Reproduction target
Produce a CSV file with columns `a` (Å), `phi` (dimensionless fraction of 2π), `total_energy` (eV per unit cell), and `fe_spin_moment` (μ_B per Fe atom). The file must contain the computed total energy and Fe spin moment for each combination of lattice constant (3.97, 3.85, 3.75, 3.70 Å) and helical angle φ from 0 to 0.20, with a density of φ points that allows the energy minimum to be located. The target is to provide these raw quantities so that the ΔE(φ) curves and the behavior of the Fe moment can be extracted and analyzed; no further post‑processing is required in the artifact.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Compute total energy and Fe spin moment for BaFeO3 G-type helical order
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO with LSDA+U (U=4.0 eV, J=0.9 eV), perform noncollinear spin-polarized calculations for cubic BaFeO3 in a primitive cell. For each lattice constant a = 3.97, 3.85, 3.75, 3.70 Å, compute total energy per unit cell and Fe local spin moment for a set of helical angles φ spanning 0 to 0.20 (in units of 2π) with sufficient resolution to locate energy minima. Extract total energy per cell and Fe spin moment magnitude from each calculation.
- Output file: `/app/outputs/energy_moment.csv`
- Format: csv
- Contract: Columns: a (float, Å), phi (float, dimensionless, fraction of 2π), total_energy (float, eV per unit cell), fe_spin_moment (float, μ_B per Fe atom).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_moment.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_moment.csv
- path: `/app/outputs/energy_moment.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed total energy (eV per unit cell) and Fe local spin moment (μ_B) for BaFeO3 at specified lattice constants and helical angles.
- schema:
  - `type`: table
  - `required_columns`: `a`, `phi`, `total_energy`, `fe_spin_moment`
  - `units`:
    - `a`: Å
    - `phi`: dimensionless
    - `total_energy`: eV
    - `fe_spin_moment`: μ_B

Notes: The checker will recompute ΔE(φ) = E(φ)-E(0) for each lattice constant, locate energy minima, and compare φ_min and ΔE_min to hidden gold values derived from the paper's Fig. 2, along with verifying the monotonic decrease of Fe spin moment at φ_min with decreasing a. Tolerances account for open-source vs. VASP differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_moment.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "a",
          "phi",
          "total_energy",
          "fe_spin_moment"
        ],
        "units": {
          "a": "Å",
          "phi": "dimensionless",
          "total_energy": "eV",
          "fe_spin_moment": "μ_B"
        }
      },
      "description": "Computed total energy (eV per unit cell) and Fe local spin moment (μ_B) for BaFeO3 at specified lattice constants and helical angles."
    }
  ],
  "notes": "The checker will recompute ΔE(φ) = E(φ)-E(0) for each lattice constant, locate energy minima, and compare φ_min and ΔE_min to hidden gold values derived from the paper's Fig. 2, along with verifying the monotonic decrease of Fe spin moment at φ_min with decreasing a. Tolerances account for open-source vs. VASP differences."
}
```

## How you are scored
A hidden verifier reads your CSV and independently determines, for each lattice constant, the φ that minimizes ΔE(φ) and the Fe spin moment at that minimum. It then checks that the location and depth of the energy minimum, and the trend of the Fe moment across lattice constants, match the reference expectations with tolerances appropriate for open‑source DFT implementations. The final reward is a weighted combination of these checks; reporting values without performing the required DFT calculations will not satisfy the verifier.
