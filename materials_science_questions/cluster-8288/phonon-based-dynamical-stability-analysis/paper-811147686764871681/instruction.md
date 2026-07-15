# DFT electronic structure and dynamical stability of a graphitic monolayer

## Problem background
Graphene's zero electronic band gap limits its application in digital electronics. This has motivated the search for new two-dimensional carbon allotropes with tunable electronic properties. One such candidate is a monolayer formed by 10-atom carbon rings bridged by CH₂ groups, creating a rectangular unit cell with a slightly buckled geometry. First-principles calculations predict that this material hosts Dirac cones shifted away from high-symmetry points, and its band structure is expected to be sensitive to mechanical deformation. This task asks you to compute the electronic structure and dynamical stability of this material from density functional theory (DFT), and to determine how the band gap at the Dirac point responds to uniform strain and shear.

## Approach
The reproduction uses density functional theory within the generalized gradient approximation, implemented with open-source plane-wave pseudopotential code (Quantum ESPRESSO) and the phonon post-processing package PHONOPY. You will construct the rectangular unit cell of the material, perform a full geometry relaxation until forces are small, and then compute the Kohn-Sham band energies along a prescribed high-symmetry path in the Brillouin zone. To assess dynamical stability, you will calculate the phonon dispersion using finite atomic displacements in a supercell. Finally, you will apply a range of uniform in-plane strains (both tensile and compressive) and shear deformations, re-relaxing the atomic positions for each deformed cell, and extract the band gap at the Dirac point from the resulting band structures. No external training data or experimental measurements are required; all inputs are defined by the structural parameters provided in the workflow steps.

## Reproduction target
Your goal is to produce the three scored artifacts listed in the workflow steps:
1. **Band structure** — a JSON file with the Kohn-Sham eigenvalues and Fermi energy along the path Γ–X–S–Γ–Y–X.
2. **Phonon dispersion** — a JSON file with phonon frequencies along the same path, obtained from finite-displacement force constants.
3. **Strain and shear response** — a JSON file with the band gap at the Dirac point for uniform in-plane strains from −3% to +5% (both uniaxial and biaxial) and for shear angles between 80° and 100°.

The verifier will independently assess your calculated band structure, phonon frequencies, and band gaps; it will numerically evaluate physical consistency without requiring a match to any published table.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Geometry relaxation
- Role: process
- Action: Construct the heptagraphene unit cell (rectangular 4.78 × 5.70 Å, C10H4, with C_A atoms buckled 0.22 Å above C_B). Perform full DFT geometry relaxation (pw.x) until forces < 1e-3 eV/Å. Save relaxed structure as CIF.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Electronic band structure
- Role: scored
- Action: Using the relaxed geometry, compute Kohn-Sham band energies along the high-symmetry path Γ-X-S-Γ-Y-X. Extract band energies and Fermi energy. Save as JSON.
- Output file: `/app/outputs/step_01_band_structure.json`
- Format: json
- Contract: {"kpoints": [{"kpoint": [float,float,float], "labels": str, "eigenvalues": [float]}], "fermi_energy": float, "path": "Γ-X-S-Γ-Y-X"}
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion
- Role: scored
- Action: Compute interatomic force constants via finite displacements (DFT supercell ≥2×2×1) and obtain phonon dispersion with PHONOPY along the same high-symmetry path. Save frequencies as JSON.
- Output file: `/app/outputs/step_02_phonon_dispersion.json`
- Format: json
- Contract: {"qpoints": [{"qpoint": [float,float,float], "labels": str, "frequencies_THz": [float]}], "path": "Γ-X-S-Γ-Y-X"}
- Scoring: scored by hidden verifier

### Step 4: Strain and shear response
- Role: scored (load-bearing)
- Action: Apply uniform in-plane strain (-3% to +5%) and shear by varying in-plane cell angle θ from 80° to 100°. For each condition, re-relax ionic positions, compute band structure along Γ-Y, and extract the band gap at the Dirac point. Save results as JSON.
- Output file: `/app/outputs/step_03_strain_results.json`
- Format: json
- Contract: {"uniform_strain": [{"strain_percent": float, "biaxial": bool, "band_gap_eV": float}], "shear_strain": [{"theta_deg": float, "band_gap_eV": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_structure.json`
- `/app/outputs/step_02_phonon_dispersion.json`
- `/app/outputs/step_03_strain_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_structure.json
- path: `/app/outputs/step_01_band_structure.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed Kohn-Sham band energies and Fermi energy; used to verify Dirac cone existence and linear dispersion.
- schema:
  - `type`: object
  - `required`: `kpoints`, `fermi_energy`, `path`
  - `properties`:
    - `kpoints`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `kpoint`:
            - `type`: array
            - `items`:
              - `type`: number
          - `labels`:
            - `type`: string
          - `eigenvalues`:
            - `type`: array
            - `items`:
              - `type`: number
    - `fermi_energy`:
      - `type`: number
    - `path`:
      - `type`: string

### step_02_phonon_dispersion.json
- path: `/app/outputs/step_02_phonon_dispersion.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon frequencies along high-symmetry path; used to verify dynamical stability (absence of imaginary modes).
- schema:
  - `type`: object
  - `required`: `qpoints`, `path`
  - `properties`:
    - `qpoints`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `qpoint`:
            - `type`: array
            - `items`:
              - `type`: number
          - `labels`:
            - `type`: string
          - `frequencies_THz`:
            - `type`: array
            - `items`:
              - `type`: number
    - `path`:
      - `type`: string

### step_03_strain_results.json
- path: `/app/outputs/step_03_strain_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Band gap at Dirac point under uniform strain (-3% to +5%) and shear (θ=80°-100°); used to verify gap closure under strain and gap opening under shear.
- schema:
  - `type`: object
  - `required`: `uniform_strain`, `shear_strain`
  - `properties`:
    - `uniform_strain`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `strain_percent`:
            - `type`: number
          - `biaxial`:
            - `type`: boolean
          - `band_gap_eV`:
            - `type`: number
    - `shear_strain`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `theta_deg`:
            - `type`: number
          - `band_gap_eV`:
            - `type`: number

Notes: All scored artifacts are recomputed from first-principles DFT simulations. The checker verifies Dirac cone features, dynamical stability (no imaginary phonon modes), and band gap trends under strain and shear.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "kpoints",
          "fermi_energy",
          "path"
        ],
        "properties": {
          "kpoints": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "kpoint": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "labels": {
                  "type": "string"
                },
                "eigenvalues": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "fermi_energy": {
            "type": "number"
          },
          "path": {
            "type": "string"
          }
        }
      },
      "description": "Computed Kohn-Sham band energies and Fermi energy; used to verify Dirac cone existence and linear dispersion."
    },
    {
      "file": "step_02_phonon_dispersion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "qpoints",
          "path"
        ],
        "properties": {
          "qpoints": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "qpoint": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "labels": {
                  "type": "string"
                },
                "frequencies_THz": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "path": {
            "type": "string"
          }
        }
      },
      "description": "Phonon frequencies along high-symmetry path; used to verify dynamical stability (absence of imaginary modes)."
    },
    {
      "file": "step_03_strain_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "uniform_strain",
          "shear_strain"
        ],
        "properties": {
          "uniform_strain": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "strain_percent": {
                  "type": "number"
                },
                "biaxial": {
                  "type": "boolean"
                },
                "band_gap_eV": {
                  "type": "number"
                }
              }
            }
          },
          "shear_strain": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "theta_deg": {
                  "type": "number"
                },
                "band_gap_eV": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Band gap at Dirac point under uniform strain (-3% to +5%) and shear (θ=80°-100°); used to verify gap closure under strain and gap opening under shear."
    }
  ],
  "notes": "All scored artifacts are recomputed from first-principles DFT simulations. The checker verifies Dirac cone features, dynamical stability (no imaginary phonon modes), and band gap trends under strain and shear."
}
```

## How you are scored
A hidden automated verifier assesses your submission. It reads the three scored JSON files and re-derives the physical properties of interest (e.g., band dispersions, phonon frequencies, band gaps) to evaluate your simulation results. Each of these criteria contributes a fraction of the total score. The verifier does not simply compare your numbers against a look‑up table; it validates that your artifacts are physically consistent and demonstrate the expected behaviour. Therefore, you must genuinely execute the DFT workflow described in the steps — reporting plausible numbers without running the calculations will not yield a high score.
