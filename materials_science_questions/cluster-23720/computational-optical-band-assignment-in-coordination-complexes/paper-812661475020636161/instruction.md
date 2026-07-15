# Problem background

Cr3+ defects in the elpasolite host crystals Cs2NaYCl6 and Cs2NaYBr6 exhibit laser‑relevant electronic properties whose accurate description requires quantum‑chemical treatment. The local geometry, vibrational frequencies, Jahn–Teller distortions, and electronic transition energies of the ground and low‑lying excited states are key quantities for understanding absorption, emission, and excited‑state absorption. These properties can be predicted non‑empirically using the ab initio model potential (AIMP) embedded‑cluster approach combined with complete active space SCF (CASSCF) and averaged coupled‑pair functional (ACPF) calculations.

In this task you will reproduce the computed structural and spectroscopic results for the Cr3+ defect clusters embedded in the two host lattices. You will perform CASSCF geometry optimisations on the ground and several excited states, extract bond distances, vibrational frequencies, and the Jahn–Teller stabilisation energy of the 4T2g state, and then run ACPF single‑point calculations to obtain vertical absorption/emission energies, Stokes shifts, and the magnetic dipole origin. All calculations must use the AIMP embedding potentials and the specified basis sets.

# Approach

The computational workflow employs the AIMP embedding technique to represent the crystalline lattice surrounding the (CrCl6)3− and (CrBr6)3− defect clusters. AIMP potentials for the host ions (Cs+, Na+, Y3+, Cl−, Br−) are available as a pre‑computed library; you must fetch them and construct the embedded clusters using the experimental lattice parameters of Cs2NaYCl6 and Cs2NaYBr6.

Quantum‑chemical calculations use OpenMolcas. The ground (4A2g) and low‑lying excited states (4T2g, 2Eg, 4T1ga) are treated with CASSCF (three active electrons in the mainly Cr(3d) t2g and eg molecular orbitals). Geometry optimisations are carried out along the totally symmetric a1g coordinate and, for the 4T2g state, along the eg(θ) coordinate (which lowers the symmetry to D4h) to obtain Jahn–Teller distortion magnitudes and the Jahn–Teller stabilisation energy. Vibrational frequencies are computed for each stationary point.

Dynamic correlation is then included via ACPF‑15 (correlating 15 electrons in the orbitals of Cr 3d and halogen p character) at the CASSCF‑optimised geometries. The vertical absorption energies from the 4A2g ground state to the 4T2g, 4T1ga, 4T1gb, 2Eg, 2T1g, 2T2g, and 2A1g states are computed, together with vertical emission energies from the 4T2g octahedral and D4h minima. Empirical free‑ion correlation corrections (−2642 cm‑1 for transitions to 4T1gb and −2304 cm‑1 for transitions to the 2Eg/2T1g/2T2g/2A1g manifold) are applied as described.

# Reproduction target

You must produce two JSON files, `structural_results.json` and `spectroscopic_results.json`, that contain all the computed quantities listed in the output contract below. The chloride and bromide clusters must be treated independently, but both sets of results are required. All values must originate from your own quantum‑chemical calculations using the AIMP embedding potentials and the specified basis sets.

# Assets

- **OpenMolcas quantum chemistry package** (tool) — open‑source CASSCF/ACPF implementation, available at https://gitlab.com/Molcas/OpenMolcas. Install and use it for all calculations.
- **AIMP embedding potential library for elpasolites** (dataset) — pre‑computed AIMP potentials for Cs+, Na+, Y3+, Cl−, Br− in Cs2NaYCl6 and Cs2NaYBr6. Available at http://sara.qfa.uam.es/Data/AIMPLibs.html. You must download and use the appropriate potentials for each host.
- **Basis sets** — standard atomic basis functions must be constructed as follows:
  * Cr: all‑electron (14s11p5d) Wachters basis augmented with one diffuse d function and one (3f) polarisation function, contracted as (62111111/4211111/3111/3).
  * Cl: [Ne]‑core AIMP valence (7s6p) basis with a diffuse p function and one d polarisation, contracted as (61/511/1).
  * Br: [Ar,3d]‑core spin‑free CG‑AIMP (9s8p4d) basis with the outermost p exponent 0.09, contracted as (81/611/31).
  * Na ghost functions: (7s4p)/[4s2p] from the SCEI calculation placed at the nearest‑neighbour Na+ sites.
  These basis sets are described in standard references; you may obtain them from the Basis Set Exchange (https://www.basissetexchange.org/) or construct them according to the given contractions.
- **Lattice constants** — experimental host parameters for Cs2NaYCl6 (a0 = 10.73967 Å, x_Cl = 0.24393) and Cs2NaYBr6 (a0 = 11.30476 Å, x_Br = 0.24462), both space group O5h–Fm 3m. Use these to position the embedding potentials and point charges. Reference: https://doi.org/10.1021/ic00211a006.

# Workflow steps

### Step 1: Embedding model setup
- Role: process
- Action: Construct the (CrCl6)3− and (CrBr6)3− clusters embedded in the AIMP representation of the respective host lattices. Download the AIMP potentials from the library and build the embedding with >400 AIMP model potentials plus long‑range Madelung point charges located at the experimental sites. Assign the basis sets listed in the Assets section. Place ghost functions on the nearest Na+ sites. Record the details of the setup in the evidence file.
- Evidence: `/app/outputs/embedding_setup.log`

### Step 2: CASSCF geometry optimisations and structural properties
- Role: scored (load‑bearing)
- Action: Perform CASSCF geometry optimisations on the embedded clusters using an active space of three electrons in the mainly Cr(3d) t2g and eg orbitals. For both the chloride and bromide clusters:
  1. Optimise the 4A2g ground state along the a1g coordinate; obtain the equilibrium Cr–X distance R_Cr‑X and vibrational frequencies ν(a1g) and ν(eg).
  2. Optimise the 4T2g excited state in octahedral symmetry along a1g; obtain R_Cr‑X, ΔR(a1g) relative to the ground state, and ν(a1g).
  3. Optimise the 4T2g state along the eg(θ) coordinate in D4h symmetry (state 4B2g); obtain the axial bond‑length change ΔR_Cr‑Xz, the equatorial bond‑length change ΔR_Cr‑Xxy, the eg vibrational frequency ν(eg), and the Jahn–Teller stabilisation energy E_JT (energy lowering due to the eg distortion).
  4. Optimise the 2Eg state in Oh symmetry along a1g; obtain R_Cr‑X and ν(a1g).
  5. Optimise the 4T1ga state in Oh symmetry along a1g; obtain R_Cr‑X and ν(a1g).
  All bond distances are in Å, vibrational frequencies in cm‑1, and energies in cm‑1. Write the complete set of results into the output file following the schema below.
- Output file: `/app/outputs/structural_results.json`
- Format: json
- Contract: The file must be a JSON object with top‑level keys `"chloride"` and `"bromide"`. Each key contains a nested object with the following sub‑keys and fields (all values are floats):
  * `"4A2g"`: `"R_Cr-X"`, `"nu_a1g"`, `"nu_eg"`.
  * `"4T2g_Oh"`: `"R_Cr-X"`, `"Delta_R_a1g"`, `"nu_a1g"`.
  * `"4B2g_D4h"`: `"Delta_R_Cr-X_z"`, `"Delta_R_Cr-X_xy"`, `"nu_eg"`, `"E_JT"`.
  * `"2Eg"`: `"R_Cr-X"`, `"nu_a1g"`.
  * `"4T1ga"`: `"R_Cr-X"`, `"nu_a1g"`.
  Units are as stated above (Å for bond lengths, cm‑1 for frequencies and E_JT).
- Scoring: scored by hidden verifier

### Step 3: ACPF vertical transition energies
- Role: scored
- Action: Using the optimised geometries from Step 2, perform ACPF‑15 calculations (correlating 15 electrons) for both clusters. Calculate:
  1. Vertical absorption energies from the 4A2g ground state to 4T2g, 4T1ga, 4T1gb, 2Eg, 2T1g, 2T2g, and 2A1g.
  2. Vertical emission energies from the 4T2g (Oh) minimum and from the 4B2g(D4h) Jahn–Teller minimum to the 4A2g ground state.
  Apply the empirical free‑ion correlation corrections: subtract 2642 cm‑1 for transitions involving the 4T1gb state and subtract 2304 cm‑1 for transitions involving the 2Eg, 2T1g, 2T2g, and 2A1g states. Report the corrected energies. Compute the Stokes shift (difference between the 4A2g→4T2g absorption maximum and the 4T2g(Oh)→4A2g emission maximum) and the magnetic dipole origin of the 4A2g↔4T2g transition. Write all values into the output file.
- Output file: `/app/outputs/spectroscopic_results.json`
- Format: json
- Contract: The file must be a JSON object with top‑level keys `"chloride"` and `"bromide"`. Each key contains:
  * `"vertical_absorption"`: an object with keys `"4A2g->4T2g"`, `"->4T1ga"`, `"->4T1gb"`, `"->2Eg"`, `"->2T1g"`, `"->2T2g"`, `"->2A1g"` (all float, cm‑1).
  * `"vertical_emission_from_4T2g"`: an object with keys `"4A2g<-4T2g_Oh"` and `"4B1g(4A2g)<-4B2g(4T2g)_D4h"` (float, cm‑1).
  * `"Stokes_shift"`: float, cm‑1.
  * `"MD_origin"`: float, cm‑1.
- Scoring: scored by hidden verifier

# Output files

- `/app/outputs/embedding_setup.log`
- `/app/outputs/structural_results.json`
- `/app/outputs/spectroscopic_results.json`

# Output contract

(see the structured contract appended below)

# How you are scored

A hidden verifier independently reads your `structural_results.json` and `spectroscopic_results.json` and compares each scalar value to a reference gold standard (based on the original publication) within appropriate tolerances. The overall reward is a weighted average across all compared numbers; the main structural quantities (Cr–X distances, E_JT) and spectroscopic quantities (4T2g absorption and emission energies) carry higher weight. Intermediate process evidence (the embedding log) is not directly scored, but the load‑bearing nature of the CASSCF step ensures that the core calculations must be genuinely executed to produce the required values.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_results.json
- path: `/app/outputs/structural_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium bond distances (Å), vibrational frequencies (cm⁻¹), and Jahn–Teller stabilisation energy (cm⁻¹) for the specified electronic states of the two defect clusters.
- schema:
  - `type`: object
  - `required`:
    - `chloride`: object
    - `bromide`: object
  - `properties`:
    - `chloride`:
      - `type`: object
      - `required`:
        - `4A2g`: object
        - `4T2g_Oh`: object
        - `4B2g_D4h`: object
        - `2Eg`: object
        - `4T1ga`: object
      - `properties`:
        - `4A2g`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `nu_a1g`: float (cm⁻¹)
            - `nu_eg`: float (cm⁻¹)
        - `4T2g_Oh`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `Delta_R_a1g`: float (Å)
            - `nu_a1g`: float (cm⁻¹)
        - `4B2g_D4h`:
          - `type`: object
          - `fields`:
            - `Delta_R_Cr-X_z`: float (Å)
            - `Delta_R_Cr-X_xy`: float (Å)
            - `nu_eg`: float (cm⁻¹)
            - `E_JT`: float (cm⁻¹)
        - `2Eg`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `nu_a1g`: float (cm⁻¹)
        - `4T1ga`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `nu_a1g`: float (cm⁻¹)
    - `bromide`:
      - `type`: object
      - `required`:
        - `4A2g`: object
        - `4T2g_Oh`: object
        - `4B2g_D4h`: object
        - `2Eg`: object
        - `4T1ga`: object
      - `properties`:
        - `4A2g`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `nu_a1g`: float (cm⁻¹)
            - `nu_eg`: float (cm⁻¹)
        - `4T2g_Oh`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `Delta_R_a1g`: float (Å)
            - `nu_a1g`: float (cm⁻¹)
        - `4B2g_D4h`:
          - `type`: object
          - `fields`:
            - `Delta_R_Cr-X_z`: float (Å)
            - `Delta_R_Cr-X_xy`: float (Å)
            - `nu_eg`: float (cm⁻¹)
            - `E_JT`: float (cm⁻¹)
        - `2Eg`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `nu_a1g`: float (cm⁻¹)
        - `4T1ga`:
          - `type`: object
          - `fields`:
            - `R_Cr-X`: float (Å)
            - `nu_a1g`: float (cm⁻¹)

### spectroscopic_results.json
- path: `/app/outputs/spectroscopic_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Vertical absorption and emission transition energies (cm⁻¹), Stokes shift (cm⁻¹), and magnetic dipole origin (cm⁻¹) after empirical correlation corrections.
- schema:
  - `type`: object
  - `required`:
    - `chloride`: object
    - `bromide`: object
  - `properties`:
    - `chloride`:
      - `type`: object
      - `required`:
        - `vertical_absorption`: object
        - `vertical_emission_from_4T2g`: object
        - `Stokes_shift`: float
        - `MD_origin`: float
      - `properties`:
        - `vertical_absorption`:
          - `type`: object
          - `fields`:
            - `4A2g->4T2g`: float (cm⁻¹)
            - `->4T1ga`: float (cm⁻¹)
            - `->4T1gb`: float (cm⁻¹)
            - `->2Eg`: float (cm⁻¹)
            - `->2T1g`: float (cm⁻¹)
            - `->2T2g`: float (cm⁻¹)
            - `->2A1g`: float (cm⁻¹)
        - `vertical_emission_from_4T2g`:
          - `type`: object
          - `fields`:
            - `4A2g<-4T2g_Oh`: float (cm⁻¹)
            - `4B1g(4A2g)<-4B2g(4T2g)_D4h`: float (cm⁻¹)
        - `Stokes_shift`:
          - `type`: float
          - `unit`: cm⁻¹
        - `MD_origin`:
          - `type`: float
          - `unit`: cm⁻¹
    - `bromide`:
      - `type`: object
      - `required`:
        - `vertical_absorption`: object
        - `vertical_emission_from_4T2g`: object
        - `Stokes_shift`: float
        - `MD_origin`: float
      - `properties`:
        - `vertical_absorption`:
          - `type`: object
          - `fields`:
            - `4A2g->4T2g`: float (cm⁻¹)
            - `->4T1ga`: float (cm⁻¹)
            - `->4T1gb`: float (cm⁻¹)
            - `->2Eg`: float (cm⁻¹)
            - `->2T1g`: float (cm⁻¹)
            - `->2T2g`: float (cm⁻¹)
            - `->2A1g`: float (cm⁻¹)
        - `vertical_emission_from_4T2g`:
          - `type`: object
          - `fields`:
            - `4A2g<-4T2g_Oh`: float (cm⁻¹)
            - `4B1g(4A2g)<-4B2g(4T2g)_D4h`: float (cm⁻¹)
        - `Stokes_shift`:
          - `type`: float
          - `unit`: cm⁻¹
        - `MD_origin`:
          - `type`: float
          - `unit`: cm⁻¹

Notes: The hidden verifier compares each scalar value in these files to a reference gold standard (derived from the original publication) within allowed tolerances. The main structural and spectroscopic quantities carry higher weight in the overall score.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "chloride": "object",
          "bromide": "object"
        },
        "properties": {
          "chloride": {
            "type": "object",
            "required": {
              "4A2g": "object",
              "4T2g_Oh": "object",
              "4B2g_D4h": "object",
              "2Eg": "object",
              "4T1ga": "object"
            },
            "properties": {
              "4A2g": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)",
                  "nu_eg": "float (cm⁻¹)"
                }
              },
              "4T2g_Oh": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "Delta_R_a1g": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)"
                }
              },
              "4B2g_D4h": {
                "type": "object",
                "fields": {
                  "Delta_R_Cr-X_z": "float (Å)",
                  "Delta_R_Cr-X_xy": "float (Å)",
                  "nu_eg": "float (cm⁻¹)",
                  "E_JT": "float (cm⁻¹)"
                }
              },
              "2Eg": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)"
                }
              },
              "4T1ga": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)"
                }
              }
            }
          },
          "bromide": {
            "type": "object",
            "required": {
              "4A2g": "object",
              "4T2g_Oh": "object",
              "4B2g_D4h": "object",
              "2Eg": "object",
              "4T1ga": "object"
            },
            "properties": {
              "4A2g": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)",
                  "nu_eg": "float (cm⁻¹)"
                }
              },
              "4T2g_Oh": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "Delta_R_a1g": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)"
                }
              },
              "4B2g_D4h": {
                "type": "object",
                "fields": {
                  "Delta_R_Cr-X_z": "float (Å)",
                  "Delta_R_Cr-X_xy": "float (Å)",
                  "nu_eg": "float (cm⁻¹)",
                  "E_JT": "float (cm⁻¹)"
                }
              },
              "2Eg": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)"
                }
              },
              "4T1ga": {
                "type": "object",
                "fields": {
                  "R_Cr-X": "float (Å)",
                  "nu_a1g": "float (cm⁻¹)"
                }
              }
            }
          }
        }
      },
      "description": "Computed equilibrium bond distances (Å), vibrational frequencies (cm⁻¹), and Jahn–Teller stabilisation energy (cm⁻¹) for the specified electronic states of the two defect clusters."
    },
    {
      "file": "spectroscopic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "chloride": "object",
          "bromide": "object"
        },
        "properties": {
          "chloride": {
            "type": "object",
            "required": {
              "vertical_absorption": "object",
              "vertical_emission_from_4T2g": "object",
              "Stokes_shift": "float",
              "MD_origin": "float"
            },
            "properties": {
              "vertical_absorption": {
                "type": "object",
                "fields": {
                  "4A2g->4T2g": "float (cm⁻¹)",
                  "->4T1ga": "float (cm⁻¹)",
                  "->4T1gb": "float (cm⁻¹)",
                  "->2Eg": "float (cm⁻¹)",
                  "->2T1g": "float (cm⁻¹)",
                  "->2T2g": "float (cm⁻¹)",
                  "->2A1g": "float (cm⁻¹)"
                }
              },
              "vertical_emission_from_4T2g": {
                "type": "object",
                "fields": {
                  "4A2g<-4T2g_Oh": "float (cm⁻¹)",
                  "4B1g(4A2g)<-4B2g(4T2g)_D4h": "float (cm⁻¹)"
                }
              },
              "Stokes_shift": {
                "type": "float",
                "unit": "cm⁻¹"
              },
              "MD_origin": {
                "type": "float",
                "unit": "cm⁻¹"
              }
            }
          },
          "bromide": {
            "type": "object",
            "required": {
              "vertical_absorption": "object",
              "vertical_emission_from_4T2g": "object",
              "Stokes_shift": "float",
              "MD_origin": "float"
            },
            "properties": {
              "vertical_absorption": {
                "type": "object",
                "fields": {
                  "4A2g->4T2g": "float (cm⁻¹)",
                  "->4T1ga": "float (cm⁻¹)",
                  "->4T1gb": "float (cm⁻¹)",
                  "->2Eg": "float (cm⁻¹)",
                  "->2T1g": "float (cm⁻¹)",
                  "->2T2g": "float (cm⁻¹)",
                  "->2A1g": "float (cm⁻¹)"
                }
              },
              "vertical_emission_from_4T2g": {
                "type": "object",
                "fields": {
                  "4A2g<-4T2g_Oh": "float (cm⁻¹)",
                  "4B1g(4A2g)<-4B2g(4T2g)_D4h": "float (cm⁻¹)"
                }
              },
              "Stokes_shift": {
                "type": "float",
                "unit": "cm⁻¹"
              },
              "MD_origin": {
                "type": "float",
                "unit": "cm⁻¹"
              }
            }
          }
        }
      },
      "description": "Vertical absorption and emission transition energies (cm⁻¹), Stokes shift (cm⁻¹), and magnetic dipole origin (cm⁻¹) after empirical correlation corrections."
    }
  ],
  "notes": "The hidden verifier compares each scalar value in these files to a reference gold standard (derived from the original publication) within allowed tolerances. The main structural and spectroscopic quantities carry higher weight in the overall score."
}
```
