# DFT Calculations of H2 Dissociative Chemisorption on Dialuminum and Al-Si Oxide Clusters

## Problem background
Aluminum oxide and silica-alumina catalysts contain coordinatively unsaturated aluminum sites that can dissociatively chemisorb hydrogen. Understanding how the coordination environment and the presence of neighboring aluminum or silicon atoms influence the reactivity is important for designing catalysts. This task investigates the reaction of H₂ with three hydroxide cluster models—a tricoordinated–tetracoordinated dialuminum cluster, a tetracoordinated–tetracoordinated dialuminum cluster, and an aluminum–silicon cluster—to determine the relative stability of physisorbed and chemisorbed complexes and the energy barrier for the hydrogen migration step.

## Approach
The calculations are performed with density functional theory (DFT) at the B3LYP/6-31G** level, which has previously been shown to give results comparable to correlated wavefunction methods for these systems. First, initial structures for the hydrated precursors are built and optimized. From these, water molecules are removed to generate the reactive clusters; some terminal atoms are frozen to mimic the rigidity of an extended solid. For each reactive cluster, a H₂ molecule is introduced and the physisorbed complex, the transition state for H–H bond cleavage and hydrogen migration to a bridging oxygen, and the final chemisorbed product are optimized. Vibrational frequency calculations provide zero-point energy corrections and confirm the nature of each stationary point (no imaginary frequencies for minima, exactly one for transition states). Relative electronic and ZPE-corrected energies are computed with respect to the separated cluster + H₂ reactants, and key geometric parameters are extracted.

## Reproduction target
Compute the relative electronic energy and the ZPE-corrected energy (in kcal/mol) for each stationary point—physisorbed complex, transition state, and chemisorbed complex—for the following three reactive clusters:  
- tricoordinated–tetracoordinated dialuminum cluster (2)  
- tetracoordinated–tetracoordinated dialuminum cluster (3)  
- aluminum–silicon cluster (9).  
For cluster 2, also measure the Al–H distance and the O–H distance in the transition state, and the dihedral angle O1–O2–Al–Ob in the chemisorbed product. All results must be written to final_results.json with the exact structure given in the output contract.

## Assets

- ORCA quantum chemistry package (or any DFT package supporting B3LYP/6-31G**): https://orcaforum.kofo.mpg.de/index.html

## Workflow steps

### Step 1: Construct initial cluster geometries
- Role: process
- Action: Build initial 3D structures for the hydrated cluster (HO)2(H2O)Al-O-Al(OH)2(H2O) (cluster 4, the precursor to reactive clusters 2 and 3) and for the hydrated aluminum-silicon cluster (HO)2(H2O)Al-O-Si(OH)3 (cluster 9). Use a molecular editor or script; set reasonable starting bond lengths and angles.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: Optimize hydrated cluster geometries
- Role: process
- Action: Perform geometry optimizations at the B3LYP/6-31G** level on the hydrated cluster 4 and on the Si-Al hydrated cluster 9. The optimized geometries will later provide reference positions for terminal atoms that are frozen in constrained optimizations of the reactive clusters.
- Evidence: `/app/outputs/hydrated_opt.log`

### Step 3: Generate and optimize reactive clusters
- Role: process
- Action: From the optimized hydrated cluster 4, remove one water molecule to create the tricoordinated–tetracoordinated reactive cluster 2. Re‑optimize at B3LYP/6-31G** with constraints (Mode B): freeze the two terminal hydrogens of the OH groups at the active Al site and the two oxygen atoms of the OH groups bonded to the neighboring Al atom. From the same hydrated cluster 4, remove one water to create the tetracoordinated–tetracoordinated reactive cluster 3; freeze the terminal oxygen atoms in the OH groups and optimize. For cluster 9, remove one water to create the reactive Si‑Al cluster and optimize without any constraints.
- Evidence: `/app/outputs/reactive_clusters.xyz`

### Step 4: Optimize physisorbed H₂ complexes
- Role: process
- Action: Place a H₂ molecule near the aluminum active site of each reactive cluster (from step_03) and optimize the geometry at B3LYP/6-31G** to locate the weakly bound physisorbed minima: complex 5 (cluster 2 + H₂), complex 7 (cluster 3 + H₂), and complex 10 (cluster 9 + H₂).
- Evidence: `/app/outputs/physisorbed_complexes.xyz`

### Step 5: Optimize chemisorbed complexes
- Role: process
- Action: From each reactive cluster + H₂, locate the dissociative chemisorption minima at B3LYP/6-31G**: complex 6 (cluster 2), complex 8A (cluster 3, where H adds to the bridging oxygen), and complex 11 (cluster 9). (Verify later via frequency analysis that these are true minima.)
- Evidence: `/app/outputs/chemisorbed_complexes.xyz`

### Step 6: Locate transition states
- Role: process
- Action: Using initial guesses similar to the transition state of one‑aluminum clusters (a geometry where one H bridges between Al and the bridging O), optimize the transition states for H₂ chemisorption on clusters 2, 3, and 9 at B3LYP/6-31G**. A frequency analysis at each optimized geometry must show exactly one imaginary frequency corresponding to the H‑migration coordinate.
- Evidence: `/app/outputs/transition_states.xyz`

### Step 7: Compute vibrational frequencies and ZPE corrections
- Role: process
- Action: Run harmonic vibrational frequency calculations (B3LYP/6-31G**) on all stationary points: isolated reactants (cluster 2 + H₂, cluster 3 + H₂, cluster 9 + H₂), the physisorbed complexes from step_04, the transition states from step_06, and the chemisorbed complexes from step_05. Extract the zero‑point energy (ZPE) for each. Confirm that the minima have no imaginary frequencies and that each transition state has exactly one.
- Evidence: `/app/outputs/zpe.log`

### Step 8: Compute relative energies and assemble final results
- Role: scored (load-bearing)
- Action: Using the electronic energies from the optimization runs (steps 02‑06) and the ZPE corrections from step_07, compute relative energies (in kcal/mol) with respect to the isolated cluster + H₂ for each species: physisorbed complex, transition state, chemisorbed complex. For cluster 2, also extract from the optimized geometries: the Al–H distance and O–H distance in the transition state, and the dihedral angle O1–O2–Al–Ob in the chemisorbed product. Write all results into final_results.json following the output schema.
- Output file: `/app/outputs/final_results.json`
- Format: json
- Contract: {
  "cluster_2": {
    "physisorbed": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>},
    "transition": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>},
    "chemisorbed": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>},
    "transition_AlH_Angstrom": <float>,
    "transition_OH_Angstrom": <float>,
    "chemisorbed_dihedral_O1_O2_Al_Ob_deg": <float>
  },
  "cluster_3": {
    "physisorbed": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>},
    "transition": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>},
    "chemisorbed": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>}
  },
  "cluster_9": {
    "physisorbed": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>},
    "transition": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>},
    "chemisorbed": {"electronic_energy_rel_kcal_mol": <float>, "zpe_corrected_energy_rel_kcal_mol": <float>}
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_results.json
- path: `/app/outputs/final_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains relative electronic and ZPE-corrected energies (kcal/mol) for the physisorbed complex, transition state, and chemisorbed complex of clusters 2, 3, and 9, plus key geometric parameters for cluster 2.
- schema:
  - `type`: object
  - `required`: `cluster_2`, `cluster_3`, `cluster_9`
  - `properties`:
    - `cluster_2`:
      - `type`: object
      - `required`: `physisorbed`, `transition`, `chemisorbed`, `transition_AlH_Angstrom`, `transition_OH_Angstrom`, `chemisorbed_dihedral_O1_O2_Al_Ob_deg`
      - `properties`:
        - `physisorbed`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
        - `transition`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
        - `chemisorbed`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
        - `transition_AlH_Angstrom`:
          - `type`: number
          - `units`: Å
        - `transition_OH_Angstrom`:
          - `type`: number
          - `units`: Å
        - `chemisorbed_dihedral_O1_O2_Al_Ob_deg`:
          - `type`: number
          - `units`: degrees
    - `cluster_3`:
      - `type`: object
      - `required`: `physisorbed`, `transition`, `chemisorbed`
      - `properties`:
        - `physisorbed`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
        - `transition`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
        - `chemisorbed`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
    - `cluster_9`:
      - `type`: object
      - `required`: `physisorbed`, `transition`, `chemisorbed`
      - `properties`:
        - `physisorbed`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
        - `transition`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
        - `chemisorbed`:
          - `type`: object
          - `required`: `electronic_energy_rel_kcal_mol`, `zpe_corrected_energy_rel_kcal_mol`
          - `properties`:
            - `electronic_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol
            - `zpe_corrected_energy_rel_kcal_mol`:
              - `type`: number
              - `units`: kcal/mol

Notes: All energies are relative to the isolated cluster + H2 reactants. The agent must compute electronic energies and ZPE corrections from the DFT calculations. The hidden checker compares each numeric field to the paper's reported values using defined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "cluster_2",
          "cluster_3",
          "cluster_9"
        ],
        "properties": {
          "cluster_2": {
            "type": "object",
            "required": [
              "physisorbed",
              "transition",
              "chemisorbed",
              "transition_AlH_Angstrom",
              "transition_OH_Angstrom",
              "chemisorbed_dihedral_O1_O2_Al_Ob_deg"
            ],
            "properties": {
              "physisorbed": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              },
              "transition": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              },
              "chemisorbed": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              },
              "transition_AlH_Angstrom": {
                "type": "number",
                "units": "Å"
              },
              "transition_OH_Angstrom": {
                "type": "number",
                "units": "Å"
              },
              "chemisorbed_dihedral_O1_O2_Al_Ob_deg": {
                "type": "number",
                "units": "degrees"
              }
            }
          },
          "cluster_3": {
            "type": "object",
            "required": [
              "physisorbed",
              "transition",
              "chemisorbed"
            ],
            "properties": {
              "physisorbed": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              },
              "transition": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              },
              "chemisorbed": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              }
            }
          },
          "cluster_9": {
            "type": "object",
            "required": [
              "physisorbed",
              "transition",
              "chemisorbed"
            ],
            "properties": {
              "physisorbed": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              },
              "transition": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              },
              "chemisorbed": {
                "type": "object",
                "required": [
                  "electronic_energy_rel_kcal_mol",
                  "zpe_corrected_energy_rel_kcal_mol"
                ],
                "properties": {
                  "electronic_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  },
                  "zpe_corrected_energy_rel_kcal_mol": {
                    "type": "number",
                    "units": "kcal/mol"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Contains relative electronic and ZPE-corrected energies (kcal/mol) for the physisorbed complex, transition state, and chemisorbed complex of clusters 2, 3, and 9, plus key geometric parameters for cluster 2."
    }
  ],
  "notes": "All energies are relative to the isolated cluster + H2 reactants. The agent must compute electronic energies and ZPE corrections from the DFT calculations. The hidden checker compares each numeric field to the paper's reported values using defined tolerances."
}
```

## How you are scored
After you submit your solution, a hidden verifier reads your final_results.json and independently compares every numeric field—energies, distances, and angle—against reference values. It computes the fraction of fields that fall within an allowed tolerance (the tolerances are not revealed to you). Your overall reward is that fraction (a number between 0 and 1). The verifier's comparison is the only assessment; you must obtain the values from your DFT calculations, not from any external lookup.
