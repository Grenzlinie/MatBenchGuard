# Gd-doped CeO2 defect formation and migration barrier calculation

## Problem background
Gadolinium-doped ceria (Gd-doped CeO₂) is a widely studied material for solid oxide fuel cell electrolytes, gas purification, and catalysis. Its performance depends critically on the formation and migration of oxygen vacancies (V_O). Substituting a tetravalent Ce ion with trivalent Gd is expected to alter the defect chemistry, but the detailed interplay between the dopant and oxygen vacancies—whether they remain isolated, pair, or form larger clusters—remains an active research topic. This work systematically examines three defect configurations in a 2×2×2 CeO₂ supercell: a single Gd substitution (Ce₃₁GdO₆₄), a Gd substitution with an adjacent oxygen vacancy (Gd+V_O, Ce₃₁GdO₆₃), and two Gd substitutions with a bridging oxygen vacancy (Gd-V_O-Gd, Ce₃₀Gd₂O₆₃). The objective is to determine the relative thermodynamic stability (formation energies) and kinetic stability (migration barriers) of these three defects, clarifying which arrangement is most likely to occur in Gd-doped CeO₂.

## Approach
Use density functional theory with a Hubbard U correction (DFT+U) and the Perdew-Burke-Ernzerhof (PBE) functional to describe the electronic structure of CeO₂. A Hubbard U parameter is applied to the Ce 4f and Gd 4f orbitals to account for strong electron correlation effects. The calculations are performed with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and appropriate pseudopotentials.

Start from a fluorite CeO₂ unit cell and build a 2×2×2 supercell. Construct and relax the three defect structures listed above using spin-polarized calculations with tight force convergence. Independently compute total energies per formula unit for bulk CeO₂, Ce₂O₃, and C-type Gd₂O₃ to serve as chemical potential references. From these energies, calculate the formation energy of each defect under both oxygen-rich and oxygen-poor conditions using the standard defect formation energy formalism.

To assess kinetic stability, perform nudged elastic band (NEB) calculations for each defect type to find the minimum-energy path for migration to a neighboring equivalent site and extract the highest-energy barrier along the path. The final outputs are the formation energies (in eV) and migration barriers (in eV) for single_Gd, Gd_V_O, and Gd_V_O_Gd.

## Reproduction target
Produce two scored output files:
- `formation_energies.json`: A JSON object containing, for each of the three defects (single_Gd, Gd_V_O, Gd_V_O_Gd), the formation energy in eV under oxygen-rich (`O_rich`) and oxygen-poor (`O_poor`) conditions. The values are to be computed per defect supercell using the DFT+U total energies.
- `migration_barriers.json`: A JSON array of objects, each with a `defect` field (one of `single_Gd`, `Gd_V_O`, `Gd_V_O_Gd`) and a `barrier_eV` field giving the minimum migration barrier in eV obtained from NEB.

Together, these quantities capture the thermodynamic and kinetic stability of the three defect configurations. The evaluation focuses on the relative ordering of these numbers, not on matching any pre-specified target values.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PAW, PBE functional): https://www.materialscloud.org/discover/sssp/table/efficiency
- CeO2 fluorite crystal structure: COD 9009009
- Ce2O3 crystal structure: COD 7200698
- C-type Gd2O3 crystal structure: COD 1010338

## Workflow steps

### Step 1: Bulk CeO2 lattice optimization
- Role: process
- Action: Optimize the lattice constant of stoichiometric CeO₂ (fluorite, Fm-3m) using DFT+U (PBE functional, U_eff=5 eV on Ce 4f) in Quantum ESPRESSO. Record the converged lattice parameter for supercell construction.
- Evidence: `/app/outputs/lattice_param.txt`

### Step 2: Reference total energies of pure phases
- Role: process
- Action: Using the same DFT+U parameters, compute the total energy per formula unit of bulk CeO₂, Ce₂O₃, and C-type Gd₂O₃. Use appropriate supercells and k-sampling for each phase. Save the per-formula-unit total energies to a JSON file.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Defect supercell relaxations
- Role: process
- Action: Construct a 2×2×2 CeO₂ supercell using the optimized lattice constant. Create and relax three defect structures: (a) a single Gd substituting one Ce (Ce₃₁GdO₆₄), (b) a Gd substitution with an oxygen vacancy at its nearest-neighbor site (Gd+V_O, 1NN configuration, Ce₃₁GdO₆₃), and (c) two Gd substitutions with an oxygen vacancy between them, both at nearest-neighbor distance (Gd-V_O-Gd, Ce₃₀Gd₂O₆₃). All relaxations use DFT+U, spin-polarized, with force convergence <0.01 eV/Å. Save the total energy and the final atomic coordinates of each relaxed supercell.
- Evidence: `/app/outputs/defect_total_energies.json`

### Step 4: Compute defect formation energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in steps 1 and 2, compute the formation energy of each defect (single Gd, Gd+V_O, Gd-V_O-Gd) under both O-rich and O-poor conditions using the standard defect formation energy formalism with chemical potentials derived from the reference total energies. Express formation energies in eV per defect. Write the results to formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {"single_Gd": {"O_rich": <float>, "O_poor": <float>}, "Gd_V_O": {"O_rich": <float>, "O_poor": <float>}, "Gd_V_O_Gd": {"O_rich": <float>, "O_poor": <float>}}
- Scoring: scored by hidden verifier

### Step 5: Compute NEB migration barriers
- Role: scored (load-bearing)
- Action: For each defect type, set up initial and final states corresponding to the shortest migration path using the relaxed structures from step 2. Run climbing-image NEB calculations with Quantum ESPRESSO to find the minimum-energy path. Extract the highest-energy barrier along the path (the migration barrier) for each defect. For Gd+V_O, the rate-limiting step is the Gd migration; for Gd-V_O-Gd, report the maximum barrier among the migration steps. Report the barrier for each defect in migration_barriers.json.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: [{"defect": "single_Gd", "barrier_eV": <float>}, {"defect": "Gd_V_O", "barrier_eV": <float>}, {"defect": "Gd_V_O_Gd", "barrier_eV": <float>}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of Gd defects under O-rich and O-poor conditions. The relative ordering among the three defects is scored to verify thermodynamic stability (Gd-V_O-Gd should be lowest).
- schema:
  - `type`: object
  - `required_keys`: `single_Gd`, `Gd_V_O`, `Gd_V_O_Gd`
  - `value_type`: object with numeric fields O_rich and O_poor (eV)

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Minimum migration barriers for the three defect types. The relative ordering is scored to verify kinetic stability (Gd-V_O-Gd should have the highest barrier).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect`, `barrier_eV`
  - `description`: Array of objects with defect name (single_Gd, Gd_V_O, Gd_V_O_Gd) and migration barrier in eV.

Notes: The checker verifies that under both O-rich and O-poor conditions, Gd_V_O_Gd has the lowest formation energy and the highest migration barrier, using appropriate tolerances for numeric values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required_keys": [
          "single_Gd",
          "Gd_V_O",
          "Gd_V_O_Gd"
        ],
        "value_type": "object with numeric fields O_rich and O_poor (eV)"
      },
      "description": "Formation energies of Gd defects under O-rich and O-poor conditions. The relative ordering among the three defects is scored to verify thermodynamic stability (Gd-V_O-Gd should be lowest)."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect",
            "barrier_eV"
          ]
        },
        "description": "Array of objects with defect name (single_Gd, Gd_V_O, Gd_V_O_Gd) and migration barrier in eV."
      },
      "description": "Minimum migration barriers for the three defect types. The relative ordering is scored to verify kinetic stability (Gd-V_O-Gd should have the highest barrier)."
    }
  ],
  "notes": "The checker verifies that under both O-rich and O-poor conditions, Gd_V_O_Gd has the lowest formation energy and the highest migration barrier, using appropriate tolerances for numeric values."
}
```

## How you are scored
A hidden verifier reads your submitted `formation_energies.json` and `migration_barriers.json` and scores them based on the relative ordering of the formation energies and migration barriers across the three defect types. For formation energies, the verifier checks that the values under each oxygen-chemical-potential condition satisfy a specific pattern that reflects the correct physical stability trend (e.g., which configuration is most stable under O-rich vs. O-poor environments). For migration barriers, it verifies that the barriers exhibit the expected kinetic stability ordering. The scoring tolerates numerical differences arising from different computational choices (pseudopotentials, k‑point sampling, convergence thresholds) and does not penalize better‑than‑reference performance. Each scored stage contributes a weight to the final reward. Simply reporting a list of numbers without consistent DFT+U energies and NEB calculations is unlikely to pass the ordering checks, so you must genuinely execute the computational workflow.
