# Bethe-cluster tight-binding model for hydrogen-impurity complexes in crystalline germanium

## Problem background
Hydrogen impurities in crystalline germanium, when associated with substitutional atoms such as carbon or oxygen, form electrically active shallow centers. The charge state of these complexes — whether they act as acceptors or donors — is believed to be linked to the occupancy of the hydrogen 1s orbital and to the distance between hydrogen and the substitutional impurity. Understanding this mechanism is important for semiconductor defect physics, but the detailed electronic structure that determines the orbital occupancy and its magnetic character remains an open computational question. Your task is to compute this electronic structure and determine the spin-resolved occupancies.

## Approach
Model the system with a Bethe-cluster tight-binding Hamiltonian: a 10-atom germanium cage (9 Ge + one substitutional impurity, either C or O, or none) plus 16 fourfold-coordinated Bethe lattices attached to the surface atoms. The basis consists of orthonormal sp³ orbitals on cage and Bethe-lattice atoms and a single 1s orbital on the hydrogen interstitial. Electron-electron repulsion is included via a Hubbard-U term on the hydrogen site only, treated in the Hartree-Fock approximation. The self-consistent solution is obtained using a Green's function projection method that computes the hydrogen-projected density of states and integrates it up to the Fermi level determined by the total electron count. This procedure yields spin-resolved occupancies ⟨n_H↑⟩ and ⟨n_H↓⟩ for six configurations: hydrogen at the cage center (R_H = 4.63 a.u. from the substitutional site) and hydrogen near the substitutional atom (R_H = 1.93 a.u. along the [111] antibonding direction) for each of the three impurity choices (no impurity, C, O). In addition, for the [H,C] and [H,O] complexes, vary R_H between 1.93 and 4.63 a.u. to locate the crossover distance where the solution changes from magnetic (|n_up - n_down| > 0.01) to nonmagnetic (|n_up - n_down| < 0.01). All needed tight-binding parameters (Ge-Ge hopping from Joannopoulos & Cohen 1974, scaled hopping for C-Ge and O-Ge bonds, site energy shifts, intra-atomic matrix elements, and hydrogen-lattice hopping integrals derived from Slater-orbital overlap integrals) are listed in the workflow step.

## Reproduction target
Perform the self-consistent Hartree-Fock calculation for the six configurations described above. Record the hydrogen 1s orbital spin occupancies n_up and n_down and classify each configuration as magnetic or nonmagnetic (threshold |n_up - n_down| = 0.01). Determine the crossover distance R_H for the [H,C] and [H,O] complexes. Assemble these results into a single JSON file, `/app/outputs/occupancies_results.json`, following the exact schema given in the output contract.

## Assets

- Python with NumPy and SciPy: numpy scipy
- Ge tight-binding parameters (Joannopoulos & Cohen 1974): https://doi.org/10.1103/PhysRevB.10.5075

## Workflow steps

### Step 1: Build Hamiltonian and solve self-consistent Hartree-Fock equations
- Role: process
- Action: Construct the tight-binding Hamiltonian for the Bethe-cluster model (10-atom cage, 16 Bethe lattices, with sp3 and hydrogen 1s basis) using specified parameters: Ge-Ge hopping from Joannopoulos & Cohen (1974), C-Ge and O-Ge hopping = 0.75 x Ge-Ge, site energies (C sp3 center 4 eV below Ge, O sp3 center 8 eV below Ge), intra-atomic interorbital matrix elements -2 eV for Ge and C, -4 eV for O, and hydrogen-lattice hopping integrals computed from overlap integrals of hydrogen 1s and Slater sp3 orbitals with standard Slater exponents. Use Hubbard-U on hydrogen: U=7 eV at cage center, U=5 eV near substitutional. For each of six configurations (impurity = none/C/O; H at center or near), solve self-consistently in Hartree-Fock using Green's function projection method, obtaining spin-resolved occupancies. Additionally, for [H,C] and [H,O], vary R_H between 1.93 and 4.63 a.u. to locate the crossover from magnetic to nonmagnetic (threshold |n_up - n_down| < 0.01). Record all computed occupancies and crossover distances.
- Evidence: `/app/outputs/calculation_log.txt`

### Step 2: Compile occupancy and crossover results
- Role: scored (load-bearing)
- Action: From the completed self-consistent calculations, assemble the hydrogen 1s orbital spin occupancies for all six configurations, classify each as magnetic (|n_up - n_down| > 0.01) or nonmagnetic, and include the estimated crossover distances for [H,C] and [H,O]. Write the results into occupancies_results.json following the specified schema.
- Output file: `/app/outputs/occupancies_results.json`
- Format: json
- Contract: {"H_C_center": {"n_up": <float>, "n_down": <float>, "magnetic": <boolean>}, "H_O_center": {"n_up": <float>, "n_down": <float>, "magnetic": <boolean>}, "H_center": {"n_up": <float>, "n_down": <float>, "magnetic": <boolean>}, "H_C_near": {"n_up": <float>, "n_down": <float>, "magnetic": <boolean>}, "H_O_near": {"n_up": <float>, "n_down": <float>, "magnetic": <boolean>}, "H_near": {"n_up": <float>, "n_down": <float>, "magnetic": <boolean>}, "crossover": {"H_C_crossover_R": <float>, "H_O_crossover_R": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/occupancies_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### occupancies_results.json
- path: `/app/outputs/occupancies_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hydrogen 1s orbital occupancies and magnetic classification for six configurations, plus crossover distances for [H,C] and [H,O].
- schema:
  - `type`: object
  - `required`: `H_C_center`, `H_O_center`, `H_center`, `H_C_near`, `H_O_near`, `H_near`, `crossover`
  - `properties`:
    - `H_C_center`:
      - `type`: object
      - `properties`:
        - `n_up`:
          - `type`: number
        - `n_down`:
          - `type`: number
        - `magnetic`:
          - `type`: boolean
      - `required`: `n_up`, `n_down`, `magnetic`
    - `H_O_center`:
      - `type`: object
      - `properties`:
        - `n_up`:
          - `type`: number
        - `n_down`:
          - `type`: number
        - `magnetic`:
          - `type`: boolean
      - `required`: `n_up`, `n_down`, `magnetic`
    - `H_center`:
      - `type`: object
      - `properties`:
        - `n_up`:
          - `type`: number
        - `n_down`:
          - `type`: number
        - `magnetic`:
          - `type`: boolean
      - `required`: `n_up`, `n_down`, `magnetic`
    - `H_C_near`:
      - `type`: object
      - `properties`:
        - `n_up`:
          - `type`: number
        - `n_down`:
          - `type`: number
        - `magnetic`:
          - `type`: boolean
      - `required`: `n_up`, `n_down`, `magnetic`
    - `H_O_near`:
      - `type`: object
      - `properties`:
        - `n_up`:
          - `type`: number
        - `n_down`:
          - `type`: number
        - `magnetic`:
          - `type`: boolean
      - `required`: `n_up`, `n_down`, `magnetic`
    - `H_near`:
      - `type`: object
      - `properties`:
        - `n_up`:
          - `type`: number
        - `n_down`:
          - `type`: number
        - `magnetic`:
          - `type`: boolean
      - `required`: `n_up`, `n_down`, `magnetic`
    - `crossover`:
      - `type`: object
      - `properties`:
        - `H_C_crossover_R`:
          - `type`: number
        - `H_O_crossover_R`:
          - `type`: number
      - `required`: `H_C_crossover_R`, `H_O_crossover_R`

Notes: Compare n_up and n_down for each configuration to paper values within tolerance; verify magnetic classification; check crossover distances within tolerance. T0 result-level compare.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "occupancies_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "H_C_center",
          "H_O_center",
          "H_center",
          "H_C_near",
          "H_O_near",
          "H_near",
          "crossover"
        ],
        "properties": {
          "H_C_center": {
            "type": "object",
            "properties": {
              "n_up": {
                "type": "number"
              },
              "n_down": {
                "type": "number"
              },
              "magnetic": {
                "type": "boolean"
              }
            },
            "required": [
              "n_up",
              "n_down",
              "magnetic"
            ]
          },
          "H_O_center": {
            "type": "object",
            "properties": {
              "n_up": {
                "type": "number"
              },
              "n_down": {
                "type": "number"
              },
              "magnetic": {
                "type": "boolean"
              }
            },
            "required": [
              "n_up",
              "n_down",
              "magnetic"
            ]
          },
          "H_center": {
            "type": "object",
            "properties": {
              "n_up": {
                "type": "number"
              },
              "n_down": {
                "type": "number"
              },
              "magnetic": {
                "type": "boolean"
              }
            },
            "required": [
              "n_up",
              "n_down",
              "magnetic"
            ]
          },
          "H_C_near": {
            "type": "object",
            "properties": {
              "n_up": {
                "type": "number"
              },
              "n_down": {
                "type": "number"
              },
              "magnetic": {
                "type": "boolean"
              }
            },
            "required": [
              "n_up",
              "n_down",
              "magnetic"
            ]
          },
          "H_O_near": {
            "type": "object",
            "properties": {
              "n_up": {
                "type": "number"
              },
              "n_down": {
                "type": "number"
              },
              "magnetic": {
                "type": "boolean"
              }
            },
            "required": [
              "n_up",
              "n_down",
              "magnetic"
            ]
          },
          "H_near": {
            "type": "object",
            "properties": {
              "n_up": {
                "type": "number"
              },
              "n_down": {
                "type": "number"
              },
              "magnetic": {
                "type": "boolean"
              }
            },
            "required": [
              "n_up",
              "n_down",
              "magnetic"
            ]
          },
          "crossover": {
            "type": "object",
            "properties": {
              "H_C_crossover_R": {
                "type": "number"
              },
              "H_O_crossover_R": {
                "type": "number"
              }
            },
            "required": [
              "H_C_crossover_R",
              "H_O_crossover_R"
            ]
          }
        }
      },
      "description": "Hydrogen 1s orbital occupancies and magnetic classification for six configurations, plus crossover distances for [H,C] and [H,O]."
    }
  ],
  "notes": "Compare n_up and n_down for each configuration to paper values within tolerance; verify magnetic classification; check crossover distances within tolerance. T0 result-level compare."
}
```

## How you are scored
Your reproduction is evaluated by a hidden verifier that independently inspects each scored artifact. For this task, the verifier reads `/app/outputs/occupancies_results.json` and compares your computed occupancies and crossover distances to reference values derived from the literature. The comparison uses appropriate tolerances to account for numerical differences arising from your implementation choices. The verifier also checks that the magnetic/nonmagnetic classifications are consistent with the occupancies you report. The total reward is a weighted sum of the scores across the evaluated stages; simply reporting the expected numbers from memory is not sufficient — your workflow must genuinely execute the required calculations.
