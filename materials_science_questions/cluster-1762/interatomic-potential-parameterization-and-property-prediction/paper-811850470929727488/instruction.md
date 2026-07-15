# YAP Interatomic Potential Fitting and Intrinsic Defect Simulation

## Problem background
Yttrium orthoaluminate (YAlO₃) single crystals are important host materials for laser, scintillator, and data-storage applications. Intrinsic defects such as vacancies, interstitials, and antisite disorder that arise during growth or under external stimuli profoundly influence crystal properties, but direct experimental evidence on the dominant defect types and their energetic barriers is limited. Atomistic computer simulation based on static lattice energy minimization with empirical interatomic potentials offers a way to predict defect formation energies, redox behavior, and ion migration pathways. This task reproduces a simulation study that derives an interatomic potential for YAlO₃ and uses it to compute perfect crystal properties, intrinsic defect energies, redox reaction energies, and oxygen vacancy migration barriers, all of which can be compared against hidden reference values.

## Approach
The work follows a compute-driven methodology using the General Utility Lattice Program (GULP). First, short-range Buckingham potential parameters (O²⁻–O²⁻, O²⁻–Al³⁺, O²⁻–Y³⁺) and shell-model parameters (for O²⁻, Al³⁺, Y³⁺) are fitted to experimental perfect crystal properties of orthorhombic YAP (space group Pnma, a=5.33 Å, b=7.375 Å, c=5.18 Å). The fitting targets are the unit cell dimensions, static dielectric constant, high-frequency dielectric constant, and density. The resulting potential is then used to minimize the perfect lattice and compute lattice parameters, interatomic distances, dielectric constants, and lattice energy. Defect calculations employ the Mott-Littleton two-region method with an inner region radius of 8.5 Å to obtain formation energies for isolated vacancies, interstitials, and cation antisite defects. Frenkel disorder energies are derived by combining the isolated defect energies, while Schottky disorder energies require supplementary lattice energy calculations for the binary oxides Y₂O₃ and Al₂O₃ using the same potential. Electronic defects are treated in a simplified small-polaron approximation: holes are modeled as O⁻ on O²⁻ sites and electrons as Y²⁺ on Y³⁺ sites, with only the Coulomb term changing; the total energies incorporate literature values for electron affinities of O²⁻, ionization potentials of Y, and the oxygen molecule dissociation energy. Redox reaction energies are computed from these electronic defect energies together with the oxygen dissociation energy. Finally, oxygen vacancy migration activation energies for 12 jump paths around the AlO₆ octahedron are estimated by placing the migrating ion at the midpoint between adjacent oxygen sites and computing the energy barrier relative to the initial equilibrium configuration. All calculations are performed with GULP. The workflow proceeds stepwise: fit potential → perfect crystal properties → isolated defect energies → binary oxide lattice energies → Frenkel/Schottky disorder energies → electronic defect energies → redox reaction energies → migration barriers.

## Reproduction target
Produce the following quantities, each in its own JSON file under /app/outputs:
- step_01_perfect_crystal.json: unit cell parameters a, b, c (Å), density (g/cm³), static and high-frequency dielectric constants, lattice energy (eV/formula unit), and a list of key interatomic distances (atom pair, calculated value, experimental value).
- step_02_isolated_defects.json: formation energies (eV) of oxygen vacancy, oxygen interstitial, aluminum vacancy, aluminum interstitial, yttrium vacancy, yttrium interstitial, yttrium antisite on aluminum, and aluminum antisite on yttrium.
- step_03_disorder_energies.json: formation energies per defect (eV/defect) for oxygen Frenkel, yttrium Frenkel, aluminum Frenkel, and Schottky disorders (YAlO₃, Al₂O₃, Y₂O₃).
- step_04_redox_energies.json: redox reaction energies (eV) for oxidation by oxygen vacancy filling, oxidation by oxygen interstitial formation, and reduction, plus an estimated band gap (eV).
- step_05_migration_barriers.json: activation energies (eV) for twelve oxygen vacancy jump paths (identified by strings like '1->2', etc.) around the AlO₆ octahedron.
The results should be obtained by executing the workflow described in the approach; all intermediate process steps (potential fitting, binary oxide lattice energies, electronic defect energies) that are necessary to derive these scored outputs must be executed, and the required evidence files saved.

## Assets

- General Utility Lattice Program (GULP): https://gulp.curtin.edu.au/

## Workflow steps

### Step 1: Fit interatomic potential for YAP
- Role: process
- Action: Using GULP, perform a relaxed fitting of short-range Buckingham parameters (O²⁻–O²⁻, O²⁻–Al³⁺, O²⁻–Y³⁺) and shell-model parameters (O²⁻, Al³⁺, Y³⁺) to experimental perfect crystal properties of orthorhombic YAP (space group Pnma, a=5.33 Å, b=7.375 Å, c=5.18 Å). Target observables are the unit cell dimensions, static dielectric constant (~16.0), high-frequency dielectric constant (~3.83), and density (~5.35 g/cm³). Start from initial parameters from GULP libraries.
- Evidence: `/app/outputs/fitted_potential.gin`

### Step 2: Perfect crystal property calculation
- Role: scored
- Action: Using the fitted potential from step_00_fit, run a GULP single-point lattice energy minimization of the YAP perfect crystal and compute unit cell parameters (a,b,c), density, static dielectric constant, high-frequency dielectric constant, lattice energy, and key interatomic distances.
- Output file: `/app/outputs/step_01_perfect_crystal.json`
- Format: json
- Contract: JSON object with keys: a (float, Å), b (float, Å), c (float, Å), density (float, g/cm³), static_dielectric_constant (float), high_frequency_dielectric_constant (float), lattice_energy (float, eV/formula unit), interatomic_distances (array of objects, each with keys: atom_pair (string, must be exactly one of the following: "Y-Y", "Al-Al", "Y-Al (3.145)", "Y-Al (3.234)", "Y-Al (3.023)", "Y-Al (3.471)", "Al-Oi", "Al-Oii (1.910)", "Al-O (1.929)", "Y-Oi (2.326)", "Y-Oi (3.097)", "Y-Oi (2.232)", "Y-Oi (3.002)", "Y-Oii (2.495)", "Y-Oii (3.268)", "Y-Oii (2.266)", "Y-Oii (2.567)"), calculated (float, Å), experimental (float, Å)).
- Scoring: scored by hidden verifier

### Step 3: Isolated point defect energies
- Role: scored
- Action: Using the fitted potential and GULP's Mott-Littleton two-region method (inner region radius 8.5 Å), calculate the formation energies of isolated vacancies (V_O, V_Al, V_Y), interstitials (O_i, Al_i, Y_i), and antisite defects (Y_Al, Al_Y).
- Output file: `/app/outputs/step_02_isolated_defects.json`
- Format: json
- Contract: JSON object with keys: O_vacancy (float, eV), O_interstitial (float, eV), Al_vacancy (float, eV), Al_interstitial (float, eV), Y_vacancy (float, eV), Y_interstitial (float, eV), Y_antisite_on_Al (float, eV), Al_antisite_on_Y (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Compute lattice energies of Y₂O₃ and Al₂O₃
- Role: process
- Action: Using the same fitted potential, run GULP lattice energy minimizations for bulk Y₂O₃ and Al₂O₃ to obtain their lattice energies (needed for Schottky disorder evaluation in step_03). Save the computed lattice energies.
- Evidence: `/app/outputs/binary_oxide_lattice_energies.json`

### Step 5: Frenkel and Schottky disorder energies
- Role: scored (load-bearing)
- Action: Combine the isolated defect energies from step_02 and the binary oxide lattice energies from step_02b to derive the formation energies per defect for oxygen Frenkel, yttrium Frenkel, aluminum Frenkel, and the three Schottky disorders (YAlO₃, Al₂O₃, Y₂O₃).
- Output file: `/app/outputs/step_03_disorder_energies.json`
- Format: json
- Contract: JSON object with keys: oxygen_Frenkel (float, eV/defect), yttrium_Frenkel (float, eV/defect), aluminum_Frenkel (float, eV/defect), YAlO3_Schottky (float, eV/defect), Al2O3_Schottky (float, eV/defect), Y2O3_Schottky (float, eV/defect).
- Scoring: scored by hidden verifier

### Step 6: Compute electronic defect energies
- Role: process
- Action: Calculate the formation energies of a hole (modelled as O⁻ on an O²⁻ site) and an electron (modelled as Y²⁺ on a Y³⁺ site) using only Coulombic changes with the fitted potential, and incorporate the required energy terms: electron affinities of O²⁻ (EA₁=1.47 eV, EA₂=-8.75 eV), ionization potentials of Y (IP₂=12.24 eV, IP₃=20.52 eV), and the oxygen molecule dissociation energy (Dₑ=5.16 eV). Follow the simplified small-polaron approach described in the paper.
- Evidence: `/app/outputs/electronic_defect_energies.json`

### Step 7: Redox reaction energies
- Role: scored
- Action: Using the electronic defect energies from step_03c and the oxygen dissociation energy, compute the reaction energies (in eV) for: oxidation by oxygen vacancy filling, oxidation by oxygen interstitial formation, and reduction. Also report the estimated band gap (difference between electron and hole formation energies).
- Output file: `/app/outputs/step_04_redox_energies.json`
- Format: json
- Contract: JSON object with keys: oxidation_vacancy_filling (float, eV), oxidation_interstitial (float, eV), reduction (float, eV), band_gap_estimate (float, eV).
- Scoring: scored by hidden verifier

### Step 8: Oxygen vacancy migration barriers
- Role: scored
- Action: For the 12 oxygen vacancy migration pathways along the AlO₆ octahedron edges, compute the activation energy for each jump using a saddle-point estimate in GULP. Place the migrating oxygen ion at the midpoint between the initial and final sites and compute the energy barrier relative to the initial equilibrium configuration.
- Output file: `/app/outputs/step_05_migration_barriers.json`
- Format: json
- Contract: JSON object mapping jump path strings (e.g., '1->2', '1->3', etc.) to activation energy (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_perfect_crystal.json`
- `/app/outputs/step_02_isolated_defects.json`
- `/app/outputs/step_03_disorder_energies.json`
- `/app/outputs/step_04_redox_energies.json`
- `/app/outputs/step_05_migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_perfect_crystal.json
- path: `/app/outputs/step_01_perfect_crystal.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Calculated perfect crystal properties from a GULP lattice energy minimization using the fitted potential.
- schema:
  - `type`: object
  - `required`: `a`, `b`, `c`, `density`, `static_dielectric_constant`, `high_frequency_dielectric_constant`, `lattice_energy`, `interatomic_distances`
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
    - `b`:
      - `type`: number
      - `unit`: Å
    - `c`:
      - `type`: number
      - `unit`: Å
    - `density`:
      - `type`: number
      - `unit`: g/cm³
    - `static_dielectric_constant`:
      - `type`: number
      - `unit`: dimensionless
    - `high_frequency_dielectric_constant`:
      - `type`: number
      - `unit`: dimensionless
    - `lattice_energy`:
      - `type`: number
      - `unit`: eV/formula unit
    - `interatomic_distances`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `atom_pair`, `calculated`, `experimental`
        - `properties`:
          - `atom_pair`:
            - `type`: string
            - `enum`: `Y-Y`, `Al-Al`, `Y-Al (3.145)`, `Y-Al (3.234)`, `Y-Al (3.023)`, `Y-Al (3.471)`, `Al-Oi`, `Al-Oii (1.910)`, `Al-O (1.929)`, `Y-Oi (2.326)`, `Y-Oi (3.097)`, `Y-Oi (2.232)`, `Y-Oi (3.002)`, `Y-Oii (2.495)`, `Y-Oii (3.268)`, `Y-Oii (2.266)`, `Y-Oii (2.567)`
          - `calculated`:
            - `type`: number
            - `unit`: Å
          - `experimental`:
            - `type`: number
            - `unit`: Å

### step_02_isolated_defects.json
- path: `/app/outputs/step_02_isolated_defects.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of eight isolated point defects computed with the Mott-Littleton method in GULP.
- schema:
  - `type`: object
  - `required`: `O_vacancy`, `O_interstitial`, `Al_vacancy`, `Al_interstitial`, `Y_vacancy`, `Y_interstitial`, `Y_antisite_on_Al`, `Al_antisite_on_Y`
  - `properties`:
    - `O_vacancy`:
      - `type`: number
      - `unit`: eV
    - `O_interstitial`:
      - `type`: number
      - `unit`: eV
    - `Al_vacancy`:
      - `type`: number
      - `unit`: eV
    - `Al_interstitial`:
      - `type`: number
      - `unit`: eV
    - `Y_vacancy`:
      - `type`: number
      - `unit`: eV
    - `Y_interstitial`:
      - `type`: number
      - `unit`: eV
    - `Y_antisite_on_Al`:
      - `type`: number
      - `unit`: eV
    - `Al_antisite_on_Y`:
      - `type`: number
      - `unit`: eV

### step_03_disorder_energies.json
- path: `/app/outputs/step_03_disorder_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies per defect for Frenkel and Schottky disorders derived from isolated defect and binary oxide lattice energies.
- schema:
  - `type`: object
  - `required`: `oxygen_Frenkel`, `yttrium_Frenkel`, `aluminum_Frenkel`, `YAlO3_Schottky`, `Al2O3_Schottky`, `Y2O3_Schottky`
  - `properties`:
    - `oxygen_Frenkel`:
      - `type`: number
      - `unit`: eV/defect
    - `yttrium_Frenkel`:
      - `type`: number
      - `unit`: eV/defect
    - `aluminum_Frenkel`:
      - `type`: number
      - `unit`: eV/defect
    - `YAlO3_Schottky`:
      - `type`: number
      - `unit`: eV/defect
    - `Al2O3_Schottky`:
      - `type`: number
      - `unit`: eV/defect
    - `Y2O3_Schottky`:
      - `type`: number
      - `unit`: eV/defect

### step_04_redox_energies.json
- path: `/app/outputs/step_04_redox_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Redox reaction energies for oxidation and reduction, and the estimated band gap.
- schema:
  - `type`: object
  - `required`: `oxidation_vacancy_filling`, `oxidation_interstitial`, `reduction`, `band_gap_estimate`
  - `properties`:
    - `oxidation_vacancy_filling`:
      - `type`: number
      - `unit`: eV
    - `oxidation_interstitial`:
      - `type`: number
      - `unit`: eV
    - `reduction`:
      - `type`: number
      - `unit`: eV
    - `band_gap_estimate`:
      - `type`: number
      - `unit`: eV

### step_05_migration_barriers.json
- path: `/app/outputs/step_05_migration_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Activation energies for 12 oxygen vacancy migration pathways computed by saddle-point energy estimation.
- schema:
  - `type`: object
  - `properties`:
    - `1->2`:
      - `type`: number
      - `unit`: eV
    - `2->6`:
      - `type`: number
      - `unit`: eV
    - `1->3`:
      - `type`: number
      - `unit`: eV
    - `3->6`:
      - `type`: number
      - `unit`: eV
    - `1->4`:
      - `type`: number
      - `unit`: eV
    - `4->6`:
      - `type`: number
      - `unit`: eV
    - `1->5`:
      - `type`: number
      - `unit`: eV
    - `5->6`:
      - `type`: number
      - `unit`: eV
    - `2->3`:
      - `type`: number
      - `unit`: eV
    - `3->4`:
      - `type`: number
      - `unit`: eV
    - `4->5`:
      - `type`: number
      - `unit`: eV
    - `5->2`:
      - `type`: number
      - `unit`: eV
  - `required`: `1->2`, `2->6`, `1->3`, `3->6`, `1->4`, `4->6`, `1->5`, `5->6`, `2->3`, `3->4`, `4->5`, `5->2`
  - `additionalProperties`: False

Notes: All scored outputs are compared against hidden reference values from the paper with numerical tolerances. The disorder energy step is load-bearing, requiring genuine execution of prior process steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_perfect_crystal.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "b",
          "c",
          "density",
          "static_dielectric_constant",
          "high_frequency_dielectric_constant",
          "lattice_energy",
          "interatomic_distances"
        ],
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å"
          },
          "b": {
            "type": "number",
            "unit": "Å"
          },
          "c": {
            "type": "number",
            "unit": "Å"
          },
          "density": {
            "type": "number",
            "unit": "g/cm³"
          },
          "static_dielectric_constant": {
            "type": "number",
            "unit": "dimensionless"
          },
          "high_frequency_dielectric_constant": {
            "type": "number",
            "unit": "dimensionless"
          },
          "lattice_energy": {
            "type": "number",
            "unit": "eV/formula unit"
          },
          "interatomic_distances": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "atom_pair",
                "calculated",
                "experimental"
              ],
              "properties": {
                "atom_pair": {
                  "type": "string",
                  "enum": [
                    "Y-Y",
                    "Al-Al",
                    "Y-Al (3.145)",
                    "Y-Al (3.234)",
                    "Y-Al (3.023)",
                    "Y-Al (3.471)",
                    "Al-Oi",
                    "Al-Oii (1.910)",
                    "Al-O (1.929)",
                    "Y-Oi (2.326)",
                    "Y-Oi (3.097)",
                    "Y-Oi (2.232)",
                    "Y-Oi (3.002)",
                    "Y-Oii (2.495)",
                    "Y-Oii (3.268)",
                    "Y-Oii (2.266)",
                    "Y-Oii (2.567)"
                  ]
                },
                "calculated": {
                  "type": "number",
                  "unit": "Å"
                },
                "experimental": {
                  "type": "number",
                  "unit": "Å"
                }
              }
            }
          }
        }
      },
      "description": "Calculated perfect crystal properties from a GULP lattice energy minimization using the fitted potential."
    },
    {
      "file": "step_02_isolated_defects.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "O_vacancy",
          "O_interstitial",
          "Al_vacancy",
          "Al_interstitial",
          "Y_vacancy",
          "Y_interstitial",
          "Y_antisite_on_Al",
          "Al_antisite_on_Y"
        ],
        "properties": {
          "O_vacancy": {
            "type": "number",
            "unit": "eV"
          },
          "O_interstitial": {
            "type": "number",
            "unit": "eV"
          },
          "Al_vacancy": {
            "type": "number",
            "unit": "eV"
          },
          "Al_interstitial": {
            "type": "number",
            "unit": "eV"
          },
          "Y_vacancy": {
            "type": "number",
            "unit": "eV"
          },
          "Y_interstitial": {
            "type": "number",
            "unit": "eV"
          },
          "Y_antisite_on_Al": {
            "type": "number",
            "unit": "eV"
          },
          "Al_antisite_on_Y": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Formation energies of eight isolated point defects computed with the Mott-Littleton method in GULP."
    },
    {
      "file": "step_03_disorder_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "oxygen_Frenkel",
          "yttrium_Frenkel",
          "aluminum_Frenkel",
          "YAlO3_Schottky",
          "Al2O3_Schottky",
          "Y2O3_Schottky"
        ],
        "properties": {
          "oxygen_Frenkel": {
            "type": "number",
            "unit": "eV/defect"
          },
          "yttrium_Frenkel": {
            "type": "number",
            "unit": "eV/defect"
          },
          "aluminum_Frenkel": {
            "type": "number",
            "unit": "eV/defect"
          },
          "YAlO3_Schottky": {
            "type": "number",
            "unit": "eV/defect"
          },
          "Al2O3_Schottky": {
            "type": "number",
            "unit": "eV/defect"
          },
          "Y2O3_Schottky": {
            "type": "number",
            "unit": "eV/defect"
          }
        }
      },
      "description": "Formation energies per defect for Frenkel and Schottky disorders derived from isolated defect and binary oxide lattice energies."
    },
    {
      "file": "step_04_redox_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "oxidation_vacancy_filling",
          "oxidation_interstitial",
          "reduction",
          "band_gap_estimate"
        ],
        "properties": {
          "oxidation_vacancy_filling": {
            "type": "number",
            "unit": "eV"
          },
          "oxidation_interstitial": {
            "type": "number",
            "unit": "eV"
          },
          "reduction": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_estimate": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Redox reaction energies for oxidation and reduction, and the estimated band gap."
    },
    {
      "file": "step_05_migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "1->2": {
            "type": "number",
            "unit": "eV"
          },
          "2->6": {
            "type": "number",
            "unit": "eV"
          },
          "1->3": {
            "type": "number",
            "unit": "eV"
          },
          "3->6": {
            "type": "number",
            "unit": "eV"
          },
          "1->4": {
            "type": "number",
            "unit": "eV"
          },
          "4->6": {
            "type": "number",
            "unit": "eV"
          },
          "1->5": {
            "type": "number",
            "unit": "eV"
          },
          "5->6": {
            "type": "number",
            "unit": "eV"
          },
          "2->3": {
            "type": "number",
            "unit": "eV"
          },
          "3->4": {
            "type": "number",
            "unit": "eV"
          },
          "4->5": {
            "type": "number",
            "unit": "eV"
          },
          "5->2": {
            "type": "number",
            "unit": "eV"
          }
        },
        "required": [
          "1->2",
          "2->6",
          "1->3",
          "3->6",
          "1->4",
          "4->6",
          "1->5",
          "5->6",
          "2->3",
          "3->4",
          "4->5",
          "5->2"
        ],
        "additionalProperties": false
      },
      "description": "Activation energies for 12 oxygen vacancy migration pathways computed by saddle-point energy estimation."
    }
  ],
  "notes": "All scored outputs are compared against hidden reference values from the paper with numerical tolerances. The disorder energy step is load-bearing, requiring genuine execution of prior process steps."
}
```

## How you are scored
Each of the five scored output files is evaluated independently by a hidden verifier. The verifier compares the reported values against hidden reference values (derived from the original study) using appropriate numerical tolerances and, where applicable, checks consistency of qualitative trends (e.g., relative ordering of defect energies). The final overall score is a weighted sum of the scores from the individual steps, with higher weight given to the load-bearing disorder energies step that depends on genuine execution of upstream process steps. Meeting or exceeding the reference accuracy—without simply looking up the paper's numbers—is the goal. The verifier's scoring code and tolerances are not disclosed; the agent should compute all quantities from the described procedure to achieve the best possible match.
