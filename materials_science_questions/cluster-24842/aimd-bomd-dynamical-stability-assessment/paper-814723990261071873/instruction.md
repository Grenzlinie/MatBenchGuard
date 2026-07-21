# Molecular dynamics study of energetic material cocrystal versus composite: trigger bond, cohesive energy, binding energy, and mechanical properties

## Problem background
Energetic materials like CL-20 deliver high explosive power but suffer from high sensitivity, limiting practical applications. Cocrystallization with HMX has been proposed as a strategy to improve stability while preserving performance. This task uses classical molecular dynamics (MD) simulations with the COMPASS force field to assess how the formation of a ε-CL-20/HMX cocrystal versus a physical composite affects molecular trigger bond lengths (N–NO₂), cohesive energy density, binding energy, and mechanical properties — key indicators of sensitivity, thermal stability, and ductility. The goal is to quantify these properties for pure ε-CL-20, β-HMX, their cocrystal, and a composite across a range of temperatures, and to determine the relative ordering and temperature dependence that emerge from the simulations.

## Approach
The conceptual approach is to construct periodic atomistic models for four systems — pure ε-CL-20 crystal, pure β-HMX crystal, a ε-CL-20/HMX cocrystal with a 2:1 molar ratio and layer‑alternating arrangement, and a ε-CL-20/HMX composite with the same stoichiometry but with components mixed randomly in a periodic box — using published crystal structures. For each model, isothermal–isobaric (NPT) molecular dynamics simulations are performed at five temperatures (245, 295, 345, 395, 445 K) using the COMPASS force field. After equilibration, production trajectories of 1 ns are collected. From these trajectories, the following quantities are computed for each system and temperature: (1) average and maximum N–NO₂ bond lengths for CL-20 molecules; (2) cohesive energy density, decomposed into van der Waals and electrostatic contributions; (3) binding energy between CL-20 and HMX defined as E_bind = –(E_total – E_CL20 – E_HMX); (4) isotropic elastic moduli (tensile modulus, bulk modulus, shear modulus, and K/G ratio) via strain fluctuation analysis and Reuss averaging. The comparison across the four systems and five temperatures allows one to evaluate how cocrystallization alters sensitivity-related bond lengths, intermolecular cohesion, and mechanical response relative to the pure crystals and a simple composite.

## Reproduction target
Produce a CSV file `simulation_results.csv` containing, for each of the four systems ('epsilon-CL-20', 'composite', 'cocrystal', 'beta-HMX') and each temperature (245, 295, 345, 395, 445 K), the computed values: L_ave_A, L_max_A, CED_kJ_cm3, vdW_kJ_cm3, Electrostatic_kJ_cm3, E_bind_kJ_mol, E_modulus_GPa, bulk_modulus_K_GPa, shear_modulus_G_GPa, K_G_ratio. For β-HMX the trigger bond length and binding energy fields may be left empty because those are defined only for CL‑20‑containing systems. The file must be written to `/app/outputs/simulation_results.csv` and its columns must follow the exact schema given in the output contract. The verifier will compare these computed numbers to expected reference values (from independent computations using the same protocol) and will also check that the data satisfy physically meaningful relationships between systems and across temperatures.

## Assets

- ε-CL-20 crystal structure
- β-HMX crystal structure
- COMPASS force field parameters
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Python scientific stack: numpy, pandas, scipy

## Workflow steps

### Step 1: Build initial atomistic models
- Role: process
- Action: Construct supercells for the four systems: ε-CL-20 crystal (2×2×4), β-HMX crystal (5×3×3), ε-CL-20/HMX cocrystal (2×3×2, 48 CL-20 + 24 HMX), and ε-CL-20/HMX composite (periodic box with 48 CL-20 and 24 HMX, gradually compressed to theoretical density). Use the published crystal structures for the pure components and the cocrystal design described in the literature.
- Evidence: `/app/outputs/initial_models.tar.gz`

### Step 2: NPT molecular dynamics production runs
- Role: process
- Action: For each of the four models, perform isothermal–isobaric (NPT) molecular dynamics simulations at five temperatures (245, 295, 345, 395, 445 K) using the COMPASS force field. After equilibration, run 1 ns production, saving configurations and energies every 10 fs for analysis.
- Evidence: `/app/outputs/trajectory_logs.tar.gz`

### Step 3: Compute all headline quantities and compile results
- Role: scored (load-bearing)
- Action: From the production trajectories, compute for each system and temperature: average and maximum N–NO₂ bond lengths for CL-20 molecules (L_ave, L_max); cohesive energy density (CED) as sum of van der Waals and electrostatic non‑bonded energy per unit volume; binding energy between CL-20 and HMX as E_bind = -(E_total - E_CL20 - E_HMX); isotropic elastic moduli (tensile modulus E, bulk modulus K, shear modulus G, K/G ratio) via fluctuation analysis and Reuss average. Combine all results into a single CSV file simulation_results.csv.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with columns: System (string, one of 'epsilon-CL-20','composite','cocrystal','beta-HMX'), Temperature_K (int), L_ave_A (float), L_max_A (float), CED_kJ_cm3 (float), vdW_kJ_cm3 (float), Electrostatic_kJ_cm3 (float), E_bind_kJ_mol (float), E_modulus_GPa (float), bulk_modulus_K_GPa (float), shear_modulus_G_GPa (float), K_G_ratio (float). For β-HMX, L_ave_A, L_max_A, and E_bind_kJ_mol are not applicable and may be omitted or left empty.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: This CSV contains the agent's computed values for trigger bond lengths, cohesive energy density, binding energy, and elastic moduli. The checker will compare these values to hidden paper reference values (within tolerances) and verify the required trends (monotonic temperature dependence, ordering across systems).
- schema:
  - `type`: table
  - `required_columns`: `System`, `Temperature_K`, `L_ave_A`, `L_max_A`, `CED_kJ_cm3`, `vdW_kJ_cm3`, `Electrostatic_kJ_cm3`, `E_bind_kJ_mol`, `E_modulus_GPa`, `bulk_modulus_K_GPa`, `shear_modulus_G_GPa`, `K_G_ratio`
  - `units`:
    - `L_ave_A`: Å
    - `L_max_A`: Å
    - `CED_kJ_cm3`: kJ/cm³
    - `vdW_kJ_cm3`: kJ/cm³
    - `Electrostatic_kJ_cm3`: kJ/cm³
    - `E_bind_kJ_mol`: kJ/mol
    - `E_modulus_GPa`: GPa
    - `bulk_modulus_K_GPa`: GPa
    - `shear_modulus_G_GPa`: GPa
    - `K_G_ratio`: dimensionless

Notes: The checker evaluates both numeric agreement (within hidden tolerances) and the following structural relations: L_max increases monotonically with temperature and follows L_max(cocrystal) < L_max(composite) < L_max(ε-CL-20) at each temperature; CED, binding energy, and elastic moduli decrease with temperature; K/G of composite and cocrystal are larger than those of pure crystals.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "Temperature_K",
          "L_ave_A",
          "L_max_A",
          "CED_kJ_cm3",
          "vdW_kJ_cm3",
          "Electrostatic_kJ_cm3",
          "E_bind_kJ_mol",
          "E_modulus_GPa",
          "bulk_modulus_K_GPa",
          "shear_modulus_G_GPa",
          "K_G_ratio"
        ],
        "units": {
          "L_ave_A": "Å",
          "L_max_A": "Å",
          "CED_kJ_cm3": "kJ/cm³",
          "vdW_kJ_cm3": "kJ/cm³",
          "Electrostatic_kJ_cm3": "kJ/cm³",
          "E_bind_kJ_mol": "kJ/mol",
          "E_modulus_GPa": "GPa",
          "bulk_modulus_K_GPa": "GPa",
          "shear_modulus_G_GPa": "GPa",
          "K_G_ratio": "dimensionless"
        }
      },
      "description": "This CSV contains the agent's computed values for trigger bond lengths, cohesive energy density, binding energy, and elastic moduli. The checker will compare these values to hidden paper reference values (within tolerances) and verify the required trends (monotonic temperature dependence, ordering across systems)."
    }
  ],
  "notes": "The checker evaluates both numeric agreement (within hidden tolerances) and the following structural relations: L_max increases monotonically with temperature and follows L_max(cocrystal) < L_max(composite) < L_max(ε-CL-20) at each temperature; CED, binding energy, and elastic moduli decrease with temperature; K/G of composite and cocrystal are larger than those of pure crystals."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `simulation_results.csv` and any supporting evidence files. The verifier performs two independent checks: (1) numeric agreement – each reported value is compared to a hidden reference value (derived from the same computational protocol) within appropriate tolerances; (2) structural consistency – the verifier inspects the data for required physical trends such as monotonic temperature dependence and correct system ordering that are expected from the underlying physics (e.g., how bond lengths and cohesive energies should rank across the four systems). Each check contributes a weighted score, and the final reward is a number between 0 and 1, with full credit only when both numeric values and trend directions are correct. The verifier does not require you to reproduce exact numbers from a specific implementation; it accepts results within a tolerance that accounts for legitimate differences in implementation details, provided the overall pattern is consistent. Note: simply reporting the expected reference values without actually running the simulations will cause trend checks to fail because the verifier also expects self-consistency among the computed quantities.
