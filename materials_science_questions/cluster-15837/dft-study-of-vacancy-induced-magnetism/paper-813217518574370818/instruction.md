# DFT study of Ga vacancy stabilization and magnetism in GaN

## Problem background
Diluted magnetic semiconductors based on GaN have attracted attention for spintronics because defects can induce ferromagnetism. In particular, Ga vacancies (V_Ga) create local magnetic moments, but their high formation energy limits their concentration. This study investigates three strategies to reduce the formation energy and thereby enhance magnetism: injecting negative charge into the vacancy, co-doping with donor-like impurities (e.g., substituting Ga with Si), and engineering nanostructures (thin films) to utilize surface proximity. The goal is to quantify these effects using density functional theory calculations.

## Approach
The work uses first-principles spin-polarized density functional theory within the generalized gradient approximation and pseudopotentials. The defect system is modelled using a supercell approach: bulk zinc blende (2×2×2) and wurtzite (3×3×2) supercells are constructed, and a single Ga vacancy is introduced with varying charge states (neutral, -1, -2, -3) compensated by a uniform background charge. Formation energies are computed from the total energies of the defective and perfect supercells, together with the chemical potentials of Ga and N determined under N-rich conditions (μ_N from an isolated N2 molecule, and μ_Ga from the enthalpy of formation of GaN). Spin-polarized calculations give the magnetic moment of the system. The effect of co-doping is studied by placing a Si atom at a Ga site in the vicinity of a Ga vacancy in wurtzite GaN and computing the binding energy of the complex. The effect of nanostructuring is studied by constructing a ten-layer (0001) slab of wurtzite GaN with vacuum and computing the formation energy of a neutral Ga vacancy as a function of depth from the surface. All calculations should use an open-source DFT code with publicly available pseudopotentials.

## Reproduction target
Using DFT as described, produce three JSON output files:
- vacancy_formation_data.json: For both zinc blende and wurtzite GaN, provide the formation energy (in eV) and magnetic moment (in μB) of a Ga vacancy for charge states 0, -1, -2, -3 under N-rich conditions.
- defect_complex_data.json: For the wurtzite GaN supercell, provide the formation energy, binding energy, and magnetic moment of the Si_Ga+V_Ga defect complex.
- slab_depth_data.json: For the (0001) wurtzite GaN slab, provide the formation energy of a neutral Ga vacancy at different layer depths (starting from the surface layer).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW-PBE pseudopotentials for Ga, N, Si: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Host supercell relaxation
- Role: process
- Action: Build 2×2×2 supercell for zinc blende GaN and 3×3×2 supercell for wurtzite GaN using known lattice constants; perform spin-polarized DFT structural relaxation until forces are converged. Record the relaxed total energy and geometry for each supercell.
- Evidence: `/app/outputs/host_relaxation.json`

### Step 2: Reference chemical potentials (N-rich)
- Role: process
- Action: Calculate the total energy of an isolated N2 molecule (spin-polarized) to obtain μ_N under N-rich conditions. Use the total energies of bulk Ga and the perfect GaN supercells from step_01 to compute ΔH(GaN). Derive μ_Ga = ΔH(GaN) - μ_N.
- Evidence: `/app/outputs/chemical_potentials.json`

### Step 3: Ga vacancy formation energies and magnetic moments
- Role: scored (load-bearing)
- Action: For each charge state q ∈ {0, -1, -2, -3} in both the zinc blende and wurtzite supercells from step_01, introduce one Ga vacancy, add compensating background charge, relax atomic positions, and compute total energy and net spin. Calculate the formation energy using the perfect supercell energy (step_01) and μ_Ga (step_02), setting the Fermi energy at the valence-band maximum. Output the results as vacancy_formation_data.json.
- Output file: `/app/outputs/vacancy_formation_data.json`
- Format: json
- Contract: {"zb": [{"charge": int, "formation_energy_ev": float, "magnetic_moment_muB": float}, ...], "wz": [...]}
- Scoring: scored by hidden verifier

### Step 4: Si_Ga+V_Ga defect complex
- Role: scored (load-bearing)
- Action: In the wurtzite GaN supercell, replace one Ga atom by Si (Si_Ga) and create a Ga vacancy. Relax the complex supercell, then compute its total energy and magnetic moment. Also compute the total energies of isolated Si_Ga and isolated V_Ga (neutral). Calculate the formation energy (using μ_Ga and μ_Si) and binding energy as the difference between the complex and isolated components. Output the results as defect_complex_data.json.
- Output file: `/app/outputs/defect_complex_data.json`
- Format: json
- Contract: {"Si_Ga+V_Ga": {"formation_energy_ev": float, "binding_energy_ev": float, "magnetic_moment_muB": float}}
- Scoring: scored by hidden verifier

### Step 5: Slab model relaxation
- Role: process
- Action: Build a (2×2) ten-layer wurtzite GaN slab along the (0001) orientation with a 10 Å vacuum layer. Fix the bottom three layers; fully relax the remaining atoms using DFT. Record the relaxed total energy and geometry.
- Evidence: `/app/outputs/slab_relaxation.json`

### Step 6: Ga vacancy formation energy in slab
- Role: scored (load-bearing)
- Action: Introduce a neutral Ga vacancy at different depths (top layer, second layer, …) in the relaxed slab from step_05, relax each structure (keeping bottom layers fixed), and compute the formation energy using the slab’s perfect total energy and μ_Ga from step_02. Output the formation energies as a function of depth in slab_depth_data.json.
- Output file: `/app/outputs/slab_depth_data.json`
- Format: json
- Contract: {"depth_profile": [{"layer": int, "formation_energy_ev": float}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_formation_data.json`
- `/app/outputs/defect_complex_data.json`
- `/app/outputs/slab_depth_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_formation_data.json
- path: `/app/outputs/vacancy_formation_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energy (eV) and magnetic moment (μB) for a Ga vacancy in zinc blende (zb) and wurtzite (wz) GaN for charge states 0, -1, -2, -3.
- schema:
  - `type`: object
  - `required`: `zb`, `wz`
  - `properties`:
    - `zb`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `charge`:
            - `type`: integer
          - `formation_energy_ev`:
            - `type`: number
          - `magnetic_moment_muB`:
            - `type`: number
    - `wz`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `charge`:
            - `type`: integer
          - `formation_energy_ev`:
            - `type`: number
          - `magnetic_moment_muB`:
            - `type`: number

### defect_complex_data.json
- path: `/app/outputs/defect_complex_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energy, binding energy, and magnetic moment for the Si_Ga+V_Ga defect complex in wurtzite GaN.
- schema:
  - `type`: object
  - `required`: `Si_Ga+V_Ga`
  - `properties`:
    - `Si_Ga+V_Ga`:
      - `type`: object
      - `properties`:
        - `formation_energy_ev`:
          - `type`: number
        - `binding_energy_ev`:
          - `type`: number
        - `magnetic_moment_muB`:
          - `type`: number

### slab_depth_data.json
- path: `/app/outputs/slab_depth_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energy (eV) of a neutral Ga vacancy as a function of depth from the surface (layer index).
- schema:
  - `type`: object
  - `required`: `depth_profile`
  - `properties`:
    - `depth_profile`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `layer`:
            - `type`: integer
          - `formation_energy_ev`:
            - `type`: number

Notes: All formation energies and binding energies are in eV; magnetic moments are in μB. The checker will compare the submitted values to the paper's reported data using appropriate tolerances and trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_formation_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "zb",
          "wz"
        ],
        "properties": {
          "zb": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "charge": {
                  "type": "integer"
                },
                "formation_energy_ev": {
                  "type": "number"
                },
                "magnetic_moment_muB": {
                  "type": "number"
                }
              }
            }
          },
          "wz": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "charge": {
                  "type": "integer"
                },
                "formation_energy_ev": {
                  "type": "number"
                },
                "magnetic_moment_muB": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Formation energy (eV) and magnetic moment (μB) for a Ga vacancy in zinc blende (zb) and wurtzite (wz) GaN for charge states 0, -1, -2, -3."
    },
    {
      "file": "defect_complex_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Si_Ga+V_Ga"
        ],
        "properties": {
          "Si_Ga+V_Ga": {
            "type": "object",
            "properties": {
              "formation_energy_ev": {
                "type": "number"
              },
              "binding_energy_ev": {
                "type": "number"
              },
              "magnetic_moment_muB": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Formation energy, binding energy, and magnetic moment for the Si_Ga+V_Ga defect complex in wurtzite GaN."
    },
    {
      "file": "slab_depth_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "depth_profile"
        ],
        "properties": {
          "depth_profile": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "layer": {
                  "type": "integer"
                },
                "formation_energy_ev": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Formation energy (eV) of a neutral Ga vacancy as a function of depth from the surface (layer index)."
    }
  ],
  "notes": "All formation energies and binding energies are in eV; magnetic moments are in μB. The checker will compare the submitted values to the paper's reported data using appropriate tolerances and trend checks."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. For each of the three scored output files (vacancy_formation_data.json, defect_complex_data.json, slab_depth_data.json), the verifier checks the reported values against expected ranges and verifies required trends (e.g., how formation energy changes with charge and depth). The three artifacts carry weights: 60% for vacancy data, 20% for the defect complex, and 20% for the slab profile. Simply reporting numbers without correctly executing the workflow will not pass the structural checks embedded in the verifier.
