# Electronic Structure and Bonding of A3Pd5 Compounds

## Problem background
Intermetallic compounds of composition A3Pd5 (A = Mg, Al, Ga) crystallize in the orthorhombic space group Pbam and feature five independent crystallographic positions. The experimentally observed distribution of A and Pd atoms among these sites (coloring model Conf.1) is believed to be the thermodynamically most stable arrangement, but several alternative orderings exist with the same stoichiometry. Understanding which ordering is lowest in energy and how the chemical bonding drives this preference is the central question. Your task is to compute the relative stability of four distinct atomic configurations using first‑principles methods and to quantify the bond strengths by analyzing the crystal orbital Hamilton populations.

## Approach
Use density functional theory (DFT) as implemented in Quantum Espresso with projector augmented‑wave (PAW) pseudopotentials and the PBE exchange‑correlation functional. For each of the three title compounds – Mg3Pd5, Al3Pd5, Ga3Pd5 – construct the four site‑coloring models (Conf.1–4) described below. Perform a full geometry relaxation for every model to obtain the total energy per unit cell. Compute the formation energy per formula unit for Conf.1 from the total energies of the elemental bulk phases (hcp Mg, fcc Al, orthorhombic Ga, fcc Pd). Then, for the relaxed Conf.1 structures, carry out Crystal Orbital Hamilton Population (COHP) analysis using the LOBSTER package. Sum the integrated –ICOHP over all bonds belonging to each of the three bond types – A–A, A–Pd, and Pd–Pd – and compute the percentage contribution of each type.

Structural models:
- Lattice parameters (a × b × c, all in Å): Mg3Pd5: 5.414 × 10.781 × 4.154; Al3Pd5: 5.411 × 10.796 × 4.169; Ga3Pd5: 5.544 × 11.133 × 4.239.
- The five independent Wyckoff sites are 2a (0,0,0), 4g (xA2,yA2,0), 4g (xPd1,yPd1,0), 4h (xPd2,yPd2,½), and 2d (0,½,0). For Mg3Pd5: (xA2,yA2) = (0.229,0.132); (xPd1,yPd1) = (0.181,0.403); (xPd2,yPd2) = (0.175,0.088). For Al3Pd5: (0.231,0.132), (0.181,0.404), (0.177,0.088). For Ga3Pd5: (0.230,0.133), (0.182,0.404), (0.174,0.087).
- The four coloring models (Conf.1–4) define how A and Pd atoms occupy these sites while maintaining the overall A3Pd5 stoichiometry (6 A atoms and 10 Pd atoms per unit cell):
  Conf.1 (experimental): A at 2a and 4g(A2), Pd at 4g(Pd1), 4h(Pd2), 2d.
  Conf.2: A at 2a and 4g(Pd1), Pd at 4g(A2), 4h(Pd2), 2d.
  Conf.3 (P2/m): A at 2a and 4h(Pd2), Pd at 4g(A2), 4g(Pd1), 2d.
  Conf.4 (Pmc2₁): A at 4g(A2) and 2d, Pd at 2a, 4g(Pd1), 4h(Pd2).

## Reproduction target
Compute and write two JSON files: (1) relative_total_energies.json containing, for each compound, the relative total energy per unit cell (Conf.1 set to 0) of the four configurations and the formation energy per formula unit of Conf.1. (2) icohp_analysis.json containing, for the Conf.1 structure of each compound, the total –ICOHP per unit cell and the percentage contribution of the three bond types (A–A, A–Pd, Pd–Pd).

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- LOBSTER: https://www.cohp.de/
- SSSP PAW-PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Prepare structural models
- Role: process
- Action: Obtain the crystal structure parameters (space group Pbam, lattice parameters, Wyckoff positions) and construct the four atomic coloring models (Conf.1–Conf.4) for each compound Mg3Pd5, Al3Pd5, Ga3Pd5. Generate DFT input files.
- Evidence: `/app/outputs/structure_prep.log`

### Step 2: DFT geometry relaxation and total energy calculation
- Role: process
- Action: For each compound and configuration (Conf.1–Conf.4), perform a full DFT geometry optimization and compute the total energy per unit cell. Also compute the total energies of the elemental reference states (Mg, Al, Ga, Pd) in their standard crystal structures.
- Evidence: `/app/outputs/relax_outputs`

### Step 3: Compile relative total energies and formation energies
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute the relative total energy per unit cell for each configuration (Conf.1 set to 0) and the formation energy per formula unit for Conf.1. Write the results to relative_total_energies.json.
- Output file: `/app/outputs/relative_total_energies.json`
- Format: json
- Contract: JSON object with keys 'Mg3Pd5','Al3Pd5','Ga3Pd5'. Each value is an object containing 'conf1','conf2','conf3','conf4' (relative total energy per unit cell in eV) and 'formation_energy_fu' (formation energy per formula unit in eV).
- Scoring: scored by hidden verifier

### Step 4: Single-point DFT and LOBSTER analysis preparation
- Role: process
- Action: For the relaxed Conf.1 structure of each compound, run a single-point DFT calculation with a denser k-point mesh to generate wavefunctions, then run LOBSTER to compute Crystal Orbital Hamilton Populations (COHP).
- Evidence: `/app/outputs/lobster_outputs`

### Step 5: Report -ICOHP analysis
- Role: scored
- Action: From LOBSTER output, extract the integrated -ICOHP for each bond, classify bonds as A–A, A–Pd, Pd–Pd, sum contributions per bond type, and compute the total -ICOHP per unit cell and percentage contribution of each bond type. Write the results to icohp_analysis.json.
- Output file: `/app/outputs/icohp_analysis.json`
- Format: json
- Contract: JSON object with keys 'Mg3Pd5','Al3Pd5','Ga3Pd5'. Each value contains objects 'A_A','A_Pd','Pd_Pd', each having 'total_icohp_per_cell' (eV) and 'percentage_contribution' (%). Sum of percentages should be 100.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_total_energies.json`
- `/app/outputs/icohp_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_total_energies.json
- path: `/app/outputs/relative_total_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative total energies per unit cell (Conf.1=0) and formation energies per formula unit. The checker compares each value to the hidden reference from the paper using appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Mg3Pd5`:
      - `type`: object
      - `required`:
        - `conf1`: number (eV)
        - `conf2`: number (eV)
        - `conf3`: number (eV)
        - `conf4`: number (eV)
        - `formation_energy_fu`: number (eV)
    - `Al3Pd5`:
      - `type`: object
      - `required`:
        - `conf1`: number (eV)
        - `conf2`: number (eV)
        - `conf3`: number (eV)
        - `conf4`: number (eV)
        - `formation_energy_fu`: number (eV)
    - `Ga3Pd5`:
      - `type`: object
      - `required`:
        - `conf1`: number (eV)
        - `conf2`: number (eV)
        - `conf3`: number (eV)
        - `conf4`: number (eV)
        - `formation_energy_fu`: number (eV)

### icohp_analysis.json
- path: `/app/outputs/icohp_analysis.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: ICOHP contributions per bond type for the Conf.1 structures. The checker compares each field to the hidden reference with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Mg3Pd5`:
      - `type`: object
      - `required`:
        - `A_A`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
        - `A_Pd`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
        - `Pd_Pd`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
    - `Al3Pd5`:
      - `type`: object
      - `required`:
        - `A_A`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
        - `A_Pd`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
        - `Pd_Pd`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
    - `Ga3Pd5`:
      - `type`: object
      - `required`:
        - `A_A`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
        - `A_Pd`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)
        - `Pd_Pd`:
          - `type`: object
          - `required`:
            - `total_icohp_per_cell`: number (eV)
            - `percentage_contribution`: number (%)

Notes: All scored outputs are compared to the paper's reported values. The exact values and tolerances are hidden. The structural data needed for step_01 will be provided in the instruction text.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Mg3Pd5": {
            "type": "object",
            "required": {
              "conf1": "number (eV)",
              "conf2": "number (eV)",
              "conf3": "number (eV)",
              "conf4": "number (eV)",
              "formation_energy_fu": "number (eV)"
            }
          },
          "Al3Pd5": {
            "type": "object",
            "required": {
              "conf1": "number (eV)",
              "conf2": "number (eV)",
              "conf3": "number (eV)",
              "conf4": "number (eV)",
              "formation_energy_fu": "number (eV)"
            }
          },
          "Ga3Pd5": {
            "type": "object",
            "required": {
              "conf1": "number (eV)",
              "conf2": "number (eV)",
              "conf3": "number (eV)",
              "conf4": "number (eV)",
              "formation_energy_fu": "number (eV)"
            }
          }
        }
      },
      "description": "Relative total energies per unit cell (Conf.1=0) and formation energies per formula unit. The checker compares each value to the hidden reference from the paper using appropriate tolerances."
    },
    {
      "file": "icohp_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Mg3Pd5": {
            "type": "object",
            "required": {
              "A_A": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              },
              "A_Pd": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              },
              "Pd_Pd": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              }
            }
          },
          "Al3Pd5": {
            "type": "object",
            "required": {
              "A_A": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              },
              "A_Pd": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              },
              "Pd_Pd": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              }
            }
          },
          "Ga3Pd5": {
            "type": "object",
            "required": {
              "A_A": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              },
              "A_Pd": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              },
              "Pd_Pd": {
                "type": "object",
                "required": {
                  "total_icohp_per_cell": "number (eV)",
                  "percentage_contribution": "number (%)"
                }
              }
            }
          }
        }
      },
      "description": "ICOHP contributions per bond type for the Conf.1 structures. The checker compares each field to the hidden reference with tolerances."
    }
  ],
  "notes": "All scored outputs are compared to the paper's reported values. The exact values and tolerances are hidden. The structural data needed for step_01 will be provided in the instruction text."
}
```

## How you are scored
A hidden verifier reads your two output files and compares each numeric field to a set of reference values using pre‑defined tolerances. The total reward is a weighted combination of the scores earned by relative_total_energies.json and icohp_analysis.json. Merely writing numbers that happen to match the reference without executing the required DFT and COHP calculations is not the intended path, but the verifier only checks the final submitted numbers. Running the described protocol faithfully is the expected way to achieve a high score.
