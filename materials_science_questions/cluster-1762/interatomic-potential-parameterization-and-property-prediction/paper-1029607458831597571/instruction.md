# Na4SiO4 Atomic-Scale Defect and Diffusion Simulation

## Problem background
Sodium-ion batteries are a promising low-cost and sustainable alternative to lithium-ion technologies, and polyanionic materials such as Na4SiO4 are under investigation as cathode or solid electrolyte candidates. The ionic conductivity and stability of these materials are governed by their intrinsic defect chemistry, the ease of sodium-ion migration, and the possibility to tune properties through aliovalent or isovalent doping. Atomistic simulations provide a means to compute defect formation energies, migration activation energies, and dopant solution energies, giving insight into the factors that control ion transport and enabling the rational design of optimized compositions.

## Approach
The crystal structure of Na4SiO4 is described using a classical pair potential model with Buckingham short-range repulsion and a core-shell representation for oxygen polarisability. Total energies, geometry optimisation, and defect calculations are performed with the open-source GULP code. Point defects (vacancies and interstitials) are modelled using the Mott-Littleton method, which partitions the lattice into an inner explicitly relaxed region and an outer elastic continuum. The defect energies for the key intrinsic processes (Frenkel, Schottky, and antisite defects) are assembled from the individual vacancy and interstitial energies. Sodium-ion migration is studied by constructing seven local Na–Na hops and evaluating defect energies at equally spaced interstitial points along each hop; activation energies are defined as the energy difference between the highest-energy saddle point and the lowest Na vacancy formation energy. Long-range pathways are built as concatenations of local hops, and the overall barrier is the maximum barrier along the sequence. Finally, the solution enthalpies of foreign ions (Li, K, Rb; Al, Ga, In, Sc, Y, Gd; Ge, Sn, Ti, Ce) are calculated using the corresponding Buckingham parameters, appropriate oxide reference energies, and the charge-compensation reactions that describe incorporation on Na or Si sites.

## Reproduction target
Compute and report (a) the formation energies (in eV) for the eight defect processes: Na Frenkel, Si Frenkel, O Frenkel, Schottky, Na2O Schottky, SiO2 Schottky, isolated Na/Si antisite, and clustered Na/Si antisite; (b) for each of the seven symmetry-distinct local Na hops labelled A through G, the Na–Na distance (Å) and the activation energy (eV), and for each of the five long-range pathways A–C–E–A, D–E–G–D–G, A–C–E–D–G, A–B–E–G–D–G, and A–C–E–F–A, the overall activation energy and the sequence of hop activation energies; (c) the solution energies of monovalent dopants (Li, K, Rb on the Na site), trivalent dopants (Al, Ga, In, Sc, Y, Gd on the Si site with charge compensation), and tetravalent dopants (Ge, Sn, Ti, Ce on the Si site). All quantities are to be produced as JSON files following the prescribed schemas.

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/
- Na4SiO4 crystal structure (ICSD CollCode62594 or published lattice parameters): ICSD_CollCode62594
- Buckingham potential parameters for host Na4SiO4
- Buckingham potential parameters for dopants: https://www.mdpi.com/article/10.3390/cryst14080718/s1

## Workflow steps

### Step 1: Structure optimization and validation
- Role: process
- Action: Construct the Na4SiO4 crystal using the structural data (CIF or lattice parameters + atomic coordinates) and the host Buckingham potentials. Perform full geometry optimization of the unit cell and atom positions with GULP to produce the equilibrium structure for subsequent defect calculations.
- Evidence: `/app/outputs/structure_optimization.log`

### Step 2: Defect energy calculations
- Role: scored
- Action: Using the optimized structure and the Mott-Littleton defect model in GULP, compute point defect formation energies (vacancies and interstitials). Assemble the Frenkel, Schottky, and anti-site defect energies. Write the resulting energies to a JSON file.
- Output file: `/app/outputs/defect_energies.json`
- Format: json
- Contract: {"Na_Frenkel": float, "Si_Frenkel": float, "O_Frenkel": float, "Schottky": float, "Na2O_Schottky": float, "SiO2_Schottky": float, "isolated_antisite": float, "clustered_antisite": float}
- Scoring: scored by hidden verifier

### Step 3: Na-ion migration pathways
- Role: scored (load-bearing)
- Action: Identify symmetry-distinct local Na-Na hops (A through G). For each hop, compute the Na-Na distance and the activation energy by evaluating defect energies at equally spaced interstitial points using the Mott-Littleton method. Then assemble the five long-range pathways and determine their overall activation energies (the maximum barrier along each concatenated hop sequence relative to the lowest Na vacancy formation energy). Write the results to a JSON file.
- Output file: `/app/outputs/migration_energies.json`
- Format: json
- Contract: {"local_hops": {"A": {"distance_angstrom": float, "activation_energy_eV": float}, "B": {...}, ... (C,D,E,F,G)}, "long_range_pathways": {"A-C-E-A": {"overall_activation_energy_eV": float, "hop_sequence_eV": [0.23, 0.03, 0.55, 0.23]}, "D-E-G-D-G": {...}, "A-C-E-D-G": {...}, "A-B-E-G-D-G": {...}, "A-C-E-F-A": {...}}}
- Scoring: scored by hidden verifier

### Step 4: Dopant solution energies
- Role: scored
- Action: Compute solution energies for monovalent dopants (Li, K, Rb) on the Na site, trivalent dopants (Al, Ga, In, Sc, Y, Gd) on the Si site with charge compensation, and tetravalent dopants (Ge, Sn, Ti, Ce) on the Si site. Use the dopant Buckingham parameters from the supplementary table, appropriate oxide reference energies, and the reaction equations for solution enthalpies. Write the results to a JSON file.
- Output file: `/app/outputs/dopant_solutions.json`
- Format: json
- Contract: {"monovalent": {"Li": float, "K": float, "Rb": float}, "trivalent": {"Al": float, "Ga": float, "In": float, "Sc": float, "Y": float, "Gd": float}, "tetravalent": {"Ge": float, "Sn": float, "Ti": float, "Ce": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_energies.json`
- `/app/outputs/migration_energies.json`
- `/app/outputs/dopant_solutions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_energies.json
- path: `/app/outputs/defect_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Defect formation energies per defect for major intrinsic processes. Lower energies indicate more favorable defects.
- schema:
  - `type`: object
  - `required`:
    - `Na_Frenkel`: float (eV)
    - `Si_Frenkel`: float (eV)
    - `O_Frenkel`: float (eV)
    - `Schottky`: float (eV)
    - `Na2O_Schottky`: float (eV)
    - `SiO2_Schottky`: float (eV)
    - `isolated_antisite`: float (eV)
    - `clustered_antisite`: float (eV)

### migration_energies.json
- path: `/app/outputs/migration_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Local Na hop distances and activation energies, and long-range pathway overall barriers. Lower activation energies indicate faster diffusion.
- schema:
  - `type`: object
  - `required`:
    - `local_hops`:
      - `A`:
        - `distance_angstrom`: float
        - `activation_energy_eV`: float
      - `B`:
        - `distance_angstrom`: float
        - `activation_energy_eV`: float
      - `C`:
        - `distance_angstrom`: float
        - `activation_energy_eV`: float
      - `D`:
        - `distance_angstrom`: float
        - `activation_energy_eV`: float
      - `E`:
        - `distance_angstrom`: float
        - `activation_energy_eV`: float
      - `F`:
        - `distance_angstrom`: float
        - `activation_energy_eV`: float
      - `G`:
        - `distance_angstrom`: float
        - `activation_energy_eV`: float
    - `long_range_pathways`:
      - `A-C-E-A`:
        - `overall_activation_energy_eV`: float
        - `hop_sequence_eV`: [float, float, float, float]
      - `D-E-G-D-G`:
        - `overall_activation_energy_eV`: float
        - `hop_sequence_eV`: [float, float, float, float, float]
      - `A-C-E-D-G`:
        - `overall_activation_energy_eV`: float
        - `hop_sequence_eV`: [float, float, float, float, float]
      - `A-B-E-G-D-G`:
        - `overall_activation_energy_eV`: float
        - `hop_sequence_eV`: [float, float, float, float, float, float]
      - `A-C-E-F-A`:
        - `overall_activation_energy_eV`: float
        - `hop_sequence_eV`: [float, float, float, float, float]

### dopant_solutions.json
- path: `/app/outputs/dopant_solutions.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Solution enthalpies for dopant incorporation. Lower energies indicate more thermodynamically favorable doping.
- schema:
  - `type`: object
  - `required`:
    - `monovalent`:
      - `Li`: float (eV)
      - `K`: float (eV)
      - `Rb`: float (eV)
    - `trivalent`:
      - `Al`: float (eV)
      - `Ga`: float (eV)
      - `In`: float (eV)
      - `Sc`: float (eV)
      - `Y`: float (eV)
      - `Gd`: float (eV)
    - `tetravalent`:
      - `Ge`: float (eV)
      - `Sn`: float (eV)
      - `Ti`: float (eV)
      - `Ce`: float (eV)

Notes: All energies are in eV. For the migration pathway, both distances (angstrom) and activation energies are required. The output files must contain the exact keys and structure shown. The checker will compare each numeric value to the paper-reported reference values with appropriate tolerances, awarding full credit when values meet or exceed the reference (lower energy is better).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Na_Frenkel": "float (eV)",
          "Si_Frenkel": "float (eV)",
          "O_Frenkel": "float (eV)",
          "Schottky": "float (eV)",
          "Na2O_Schottky": "float (eV)",
          "SiO2_Schottky": "float (eV)",
          "isolated_antisite": "float (eV)",
          "clustered_antisite": "float (eV)"
        }
      },
      "description": "Defect formation energies per defect for major intrinsic processes. Lower energies indicate more favorable defects."
    },
    {
      "file": "migration_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "local_hops": {
            "A": {
              "distance_angstrom": "float",
              "activation_energy_eV": "float"
            },
            "B": {
              "distance_angstrom": "float",
              "activation_energy_eV": "float"
            },
            "C": {
              "distance_angstrom": "float",
              "activation_energy_eV": "float"
            },
            "D": {
              "distance_angstrom": "float",
              "activation_energy_eV": "float"
            },
            "E": {
              "distance_angstrom": "float",
              "activation_energy_eV": "float"
            },
            "F": {
              "distance_angstrom": "float",
              "activation_energy_eV": "float"
            },
            "G": {
              "distance_angstrom": "float",
              "activation_energy_eV": "float"
            }
          },
          "long_range_pathways": {
            "A-C-E-A": {
              "overall_activation_energy_eV": "float",
              "hop_sequence_eV": "[float, float, float, float]"
            },
            "D-E-G-D-G": {
              "overall_activation_energy_eV": "float",
              "hop_sequence_eV": "[float, float, float, float, float]"
            },
            "A-C-E-D-G": {
              "overall_activation_energy_eV": "float",
              "hop_sequence_eV": "[float, float, float, float, float]"
            },
            "A-B-E-G-D-G": {
              "overall_activation_energy_eV": "float",
              "hop_sequence_eV": "[float, float, float, float, float, float]"
            },
            "A-C-E-F-A": {
              "overall_activation_energy_eV": "float",
              "hop_sequence_eV": "[float, float, float, float, float]"
            }
          }
        }
      },
      "description": "Local Na hop distances and activation energies, and long-range pathway overall barriers. Lower activation energies indicate faster diffusion."
    },
    {
      "file": "dopant_solutions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "monovalent": {
            "Li": "float (eV)",
            "K": "float (eV)",
            "Rb": "float (eV)"
          },
          "trivalent": {
            "Al": "float (eV)",
            "Ga": "float (eV)",
            "In": "float (eV)",
            "Sc": "float (eV)",
            "Y": "float (eV)",
            "Gd": "float (eV)"
          },
          "tetravalent": {
            "Ge": "float (eV)",
            "Sn": "float (eV)",
            "Ti": "float (eV)",
            "Ce": "float (eV)"
          }
        }
      },
      "description": "Solution enthalpies for dopant incorporation. Lower energies indicate more thermodynamically favorable doping."
    }
  ],
  "notes": "All energies are in eV. For the migration pathway, both distances (angstrom) and activation energies are required. The output files must contain the exact keys and structure shown. The checker will compare each numeric value to the paper-reported reference values with appropriate tolerances, awarding full credit when values meet or exceed the reference (lower energy is better)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the three output JSON files and compares every numeric value in them to reference values derived from the published literature. Each scored quantity contributes to a weighted overall reward, where meeting or exceeding the reference (i.e., producing a lower energy, which indicates a more favourable defect or dopant incorporation) earns full credit, and deviations that indicate worse performance are penalised. The reward is monotonic in quality: a more favourable computed value never receives a lower score. The verifier also validates that the output files contain all required keys and structures; missing or malformed fields receive zero credit. There are no partial scores for running only part of the workflow – all scored artifacts must be present.
