# First-principles calculation of hydrogen partial atomic volume in palladium

## Problem background
Palladium hydride is a prototypical interstitial metal-hydride system. When hydrogen atoms are absorbed into the palladium lattice, the crystal expands. The volume increase per added hydrogen atom, known as the partial atomic volume of hydrogen (v_H), is a key thermodynamic quantity that governs the stability and expansion of the hydride phase. First-principles density functional theory (DFT) can predict this quantity from the equilibrium lattice constants of pure Pd and PdH, but the predicted v_H depends on the assumed interstitial site occupancy (octahedral only vs. mixed octahedral/tetrahedral). The task is to compute the equilibrium conventional-unit-cell lattice constants for Pd, PdH with only octahedral hydrogen, and PdH with a 25% tetrahedral / 75% octahedral mixture. From these lattice constants, the partial atomic volume of hydrogen can be derived and compared between the two occupancy models.

## Approach
Use plane-wave DFT with the PBE exchange-correlation functional and PAW pseudopotentials, as implemented in the open-source Quantum ESPRESSO package. Build 2×2×2 supercells of the primitive FCC lattice (8 Pd atoms) for three compositions: pure Pd, PdH with all H in octahedral sites (Pd₈H₈), and PdH with 2 H in tetrahedral and 6 H in octahedral sites (25% tet). Because several spatial arrangements are possible for the mixed-occupancy case, generate at least two random placements, evaluate their energies with a fast energy model, and select the lowest-energy configuration for the subsequent relaxation. Then, for each supercell, perform a full geometry relaxation (cell vectors and atomic positions) to find the zero-temperature equilibrium structure. Finally, extract the conventional FCC lattice constant a (in Å) from each relaxed structure and record them together with the scheme label 'PBE/PAW'.

## Reproduction target
Compute the equilibrium conventional-cell lattice constant a (in Å) for three phases — pure Pd, PdH with 100% octahedral H, and PdH with 25% tetrahedral / 75% octahedral H — using zero-temperature DFT with PBE/PAW. Produce a CSV file (`equilibrium_lattice_constants.csv`) with columns `phase`, `lattice_constant_a`, and `scheme`. The phase names must be `Pd`, `PdH_oct`, and `PdH_mixed`. The column `scheme` must contain the string `PBE/PAW` for every row. The checker will recompute the partial atomic volume v_H from your lattice constants and compare them to the expected v_H values for the two hydride phases.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pd PBE PAW pseudopotential: https://pseudopotentials.quantum-espresso.org/upf_files/Pd.pbe-n-rrkjus_psl.1.0.0.UPF
- H PBE PAW pseudopotential: https://pseudopotentials.quantum-espresso.org/upf_files/H.pbe-rrkjus_psl.1.0.0.UPF

## Workflow steps

### Step 1: Supercell construction and mixed-configuration screening
- Role: process
- Action: Build 2×2×2 supercells of the primitive FCC lattice (8 Pd atoms) for pure Pd, PdH with all H in octahedral sites, and PdH with 2 H in tetrahedral and 6 H in octahedral sites (25% tet occupancy). For the mixed case, generate at least two random placements and perform a brief energy evaluation (e.g., a fast DFT or simple interatomic potential) to select the lowest-energy configuration.
- Evidence: `/app/outputs/selected_mixed_configuration.xyz`

### Step 2: DFT geometry relaxation
- Role: process
- Action: Perform DFT geometry optimization (relaxing lattice vectors and atomic positions) for the Pd, PdH_oct, and the selected PdH_mixed supercell using Quantum Espresso with the PBE functional and PAW pseudopotentials. Use a plane-wave cutoff of 60 Ry and a 12×12×12 k‑point mesh (or convergence‑tested values).
- Evidence: `/app/outputs/relaxation_summary.json`

### Step 3: Extract lattice constants
- Role: scored (load-bearing)
- Action: From the relaxed structures, determine the conventional FCC lattice constant a (in Å) for each phase. Write a CSV file with columns: phase, lattice_constant_a, scheme. Enter 'PBE/PAW' for scheme.
- Output file: `/app/outputs/equilibrium_lattice_constants.csv`
- Format: csv
- Contract: CSV with columns: phase (string), lattice_constant_a (float, Å), scheme (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_lattice_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_lattice_constants.csv
- path: `/app/outputs/equilibrium_lattice_constants.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing the DFT-predicted equilibrium conventional FCC lattice constant for each phase. The checker recomputes the partial atomic volume v_H from these lattice constants and compares to the paper's reported values.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `lattice_constant_a`, `scheme`
  - `units`:
    - `lattice_constant_a`: angstrom

Notes: Only the PBE/PAW scheme is required; other functionals and pseudopotentials from the paper are out of scope. The mixed-occupancy configuration is fixed at 25% tetrahedral. The checker performs a T1 recompute: v_H = (a³(PdH) − a³(Pd)) / 4 for each hydride, and checks v_H against hidden gold values with tolerance, plus a relative ordering check that v_H_mixed > v_H_oct.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_lattice_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "lattice_constant_a",
          "scheme"
        ],
        "units": {
          "lattice_constant_a": "angstrom"
        }
      },
      "description": "CSV file containing the DFT-predicted equilibrium conventional FCC lattice constant for each phase. The checker recomputes the partial atomic volume v_H from these lattice constants and compares to the paper's reported values."
    }
  ],
  "notes": "Only the PBE/PAW scheme is required; other functionals and pseudopotentials from the paper are out of scope. The mixed-occupancy configuration is fixed at 25% tetrahedral. The checker performs a T1 recompute: v_H = (a³(PdH) − a³(Pd)) / 4 for each hydride, and checks v_H against hidden gold values with tolerance, plus a relative ordering check that v_H_mixed > v_H_oct."
}
```

## How you are scored
A hidden verifier will read your `equilibrium_lattice_constants.csv` and compute, for each hydride phase, the volume increase ΔV = a³(PdH) – a³(Pd) and the partial atomic volume v_H = ΔV / 4 (because each supercell contains 4 formula units of PdH). It will compare your computed v_H for the octahedral-only and mixed-occupancy cases against the expected values derived from the reference first-principles study. Additionally, it checks that v_H for the mixed-occupancy case is larger than for the octahedral-only case (a relative trend). Your score reflects how closely your lattice constants reproduce the correct v_H values; a correct DFT execution that yields lattice constants matching the reference will receive full credit, while deviations due to incorrect relaxations or wrong configurations will reduce the score.
