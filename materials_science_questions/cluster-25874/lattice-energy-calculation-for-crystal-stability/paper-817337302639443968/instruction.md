# Reproduce QTAIM and Hirshfeld Surface Analysis for Crystal Polymorphs

## Problem background
Two new crystalline derivatives, a dipyrazolo-1,5-diazocine and a dipyrazolopyrimidine, were obtained unexpectedly from a reaction between an aminopyrazole and an aldehyde. The latter compound exhibits isostructural dimorphism, crystallizing in two morphologically distinct but structurally similar polymorphs. The crystal structures were solved by X-ray diffraction, and their noncovalent interactions were characterized using Quantum Theory of Atoms in Molecules (QTAIM) and Hirshfeld surface analysis. Reproducing the computed topological properties and interaction energies from the publicly deposited crystal structures provides a quantitative validation of these polymorphs' supramolecular features.

## Approach
The computational workflow proceeds in two stages. First, high-level DFT single-point calculations (B3LYP/6-311++G(2df,2pd)) are performed on the isolated molecules extracted from the CIF files, yielding wavefunctions for QTAIM analysis. QTAIM locates bond critical points (BCPs) and extracts topological descriptors: electron density ρ, Laplacian ∇²ρ, ellipticity ε, virial field V(r), and kinetic energy density G(r) for each intramolecular noncovalent contact. Second, lower-level DFT calculations (B3LYP/6-31G(d,p)) provide monomer wavefunctions for CrystalExplorer's CE-B3LYP energy model. Hirshfeld surfaces are computed to obtain contact percentages for H···H, C···H, and N···H interactions, and pairwise intermolecular interaction energies (electrostatic, polarization, dispersion, exchange-repulsion, and total) are computed for the molecular clusters in the two polymorphs. The analysis uses only public CIF files and open-source quantum chemistry and crystallographic tools.

## Reproduction target
Produce two JSON artifacts: one containing the QTAIM bond critical point parameters (ρ, ∇²ρ, ε, V(r), G(r)) and bond path distances for the main intramolecular contacts in compounds 8, 9a, and 9b; the other containing the Hirshfeld surface contact percentages (H···H, C···H, N···H) for all three crystals and the CE‑B3LYP intermolecular interaction energies (E_ele, E_pol, E_dis, E_rep, E_tot) for the symmetry-unique molecular pairs in polymorphs 9a and 9b. The required schemas and output paths are detailed in the workflow steps and output contract.

## Assets

- CIF files for compounds 8, 9a, 9b (CCDC 776294, 776293, 776295): https://www.ccdc.cam.ac.uk/structures/
- Open-source quantum chemistry package (Psi4 or ORCA): psi4
- Multiwfn: https://sobereva.com/multiwfn/
- CrystalExplorer: https://crystalexplorer.net/

## Workflow steps

### Step 1: Molecular geometry extraction
- Role: process
- Action: Download the CIF files from CCDC (entries 776294, 776293, 776295) and extract the isolated molecular geometries for compounds 8, 9a, 9b. Use the asymmetric unit coordinates; for each crystal one unique molecule is sufficient. Save the coordinates in a format ready for DFT input (e.g., XYZ or Gaussian input).
- Evidence: `/app/outputs/molecular_geometries.xyz`

### Step 2: High-level DFT wavefunction calculation
- Role: process
- Action: For each molecule (8, 9a, 9b), perform a single-point DFT calculation at the B3LYP/6-311++G(2df,2pd) level using an open-source quantum chemistry package. No geometry optimization; use the crystal coordinates. Save the wavefunction (e.g., .wfn or fchk) for QTAIM analysis.
- Evidence: `/app/outputs/qtaim_wavefunctions.tar.gz`

### Step 3: QTAIM topological analysis
- Role: scored (load-bearing)
- Action: Run Multiwfn on each high-level wavefunction to locate all bond critical points (BCPs). For each molecule, identify the intramolecular BCPs analogous to those described in the paper (e.g., C(17)···H'-C(37), N(16)···H-C(11)). Report for each BCP: the interaction label, bond path distances (R_X, R_Y), electron density ρ, Laplacian ∇²ρ, ellipticity ε, virial field V(r), and kinetic energy G(r). Save the results as JSON.
- Output file: `/app/outputs/qtaim_bcps.json`
- Format: json
- Contract: Array of objects: { "molecule": "8"|"9a"|"9b", "interaction": "string", "bond_path_RX": float, "bond_path_RY": float, "rho_b": float, "laplacian_rho": float, "ellipticity": float, "Vr": float, "Gr": float }
- Scoring: scored by hidden verifier

### Step 4: Low-level DFT monomer wavefunction calculation
- Role: process
- Action: For each molecule (8, 9a, 9b), perform a single-point DFT calculation at the B3LYP/6-31G(d,p) level using the same open-source package. Save the monomer wavefunction (e.g., .wfn) required by CrystalExplorer's CE‑B3LYP energy model.
- Evidence: `/app/outputs/monomer_wavefunctions.tar.gz`

### Step 5: Hirshfeld surface and CE‑B3LYP energy analysis
- Role: scored
- Action: Using CrystalExplorer, load the CIF files and the monomer wavefunctions from step4. For each crystal (8, 9a, 9b) compute the Hirshfeld surface and 2D fingerprint plots; extract the percentage contributions of H···H, C···H, and N···H contacts. For polymorphs 9a and 9b, compute the CE‑B3LYP intermolecular interaction energies for the molecular clusters defined in the paper (central molecule + symmetry-related neighbours). Report the energy components (E_ele, E_pol, E_dis, E_rep, E_tot) for each unique pair, labelled by the color/symop as in the paper. Save all results as JSON.
- Output file: `/app/outputs/hirshfeld_results.json`
- Format: json
- Contract: Object with keys "8", "9a", "9b". Each value: { "contact_percentages": { "HH": float, "CH": float, "NH": float }, "interaction_energies": [ { "polymorph": "9a"|"9b", "color": "string", "symop_AB": "string", "R_AB": float, "E_ele": float, "E_pol": float, "E_dis": float, "E_rep": float, "E_tot": float } ] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/qtaim_bcps.json`
- `/app/outputs/hirshfeld_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### qtaim_bcps.json
- path: `/app/outputs/qtaim_bcps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: QTAIM bond critical point parameters for compound 8 and polymorphs 9a, 9b.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `molecule`, `interaction`, `bond_path_RX`, `bond_path_RY`, `rho_b`, `laplacian_rho`, `ellipticity`, `Vr`, `Gr`
    - `properties`:
      - `molecule`:
        - `type`: string
        - `enum`: `8`, `9a`, `9b`
      - `interaction`:
        - `type`: string
        - `description`: Label of the interaction, e.g. 'C(17)...H'-C(37)'
      - `bond_path_RX`:
        - `type`: number
        - `description`: Bond path distance to X atom in atomic units
      - `bond_path_RY`:
        - `type`: number
      - `rho_b`:
        - `type`: number
        - `description`: Electron density at BCP in atomic units
      - `laplacian_rho`:
        - `type`: number
      - `ellipticity`:
        - `type`: number
      - `Vr`:
        - `type`: number
        - `description`: Virial field function in atomic units
      - `Gr`:
        - `type`: number
        - `description`: Kinetic energy density in atomic units

### hirshfeld_results.json
- path: `/app/outputs/hirshfeld_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hirshfeld surface contact percentages and CE‑B3LYP pair interaction energies for crystals 8, 9a, 9b.
- schema:
  - `type`: object
  - `required`: `8`, `9a`, `9b`
  - `properties`:
    - `8`:
      - `type`: object
      - `required`: `contact_percentages`, `interaction_energies`
      - `properties`:
        - `contact_percentages`:
          - `type`: object
          - `required`: `HH`, `CH`, `NH`
          - `properties`:
            - `HH`:
              - `type`: number
            - `CH`:
              - `type`: number
            - `NH`:
              - `type`: number
        - `interaction_energies`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `polymorph`, `color`, `symop_AB`, `R_AB`, `E_ele`, `E_pol`, `E_dis`, `E_rep`, `E_tot`
            - `properties`:
              - `polymorph`:
                - `type`: string
                - `enum`: `9a`, `9b`
              - `color`:
                - `type`: string
              - `symop_AB`:
                - `type`: string
              - `R_AB`:
                - `type`: number
                - `description`: Distance between molecular centroids in Å
              - `E_ele`:
                - `type`: number
                - `description`: Electrostatic component (kJ/mol)
              - `E_pol`:
                - `type`: number
                - `description`: Polarization component (kJ/mol)
              - `E_dis`:
                - `type`: number
                - `description`: Dispersion component (kJ/mol)
              - `E_rep`:
                - `type`: number
                - `description`: Exchange-repulsion component (kJ/mol)
              - `E_tot`:
                - `type`: number
                - `description`: Total interaction energy (kJ/mol)
    - `9a`:
      - `$ref`: #/properties/8
    - `9b`:
      - `$ref`: #/properties/8

Notes: All reported values must be derived from the CIF structures and the described computational workflow. The checker will compare the agent's values to the paper's published reference values within predefined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "qtaim_bcps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "molecule",
            "interaction",
            "bond_path_RX",
            "bond_path_RY",
            "rho_b",
            "laplacian_rho",
            "ellipticity",
            "Vr",
            "Gr"
          ],
          "properties": {
            "molecule": {
              "type": "string",
              "enum": [
                "8",
                "9a",
                "9b"
              ]
            },
            "interaction": {
              "type": "string",
              "description": "Label of the interaction, e.g. 'C(17)...H'-C(37)'"
            },
            "bond_path_RX": {
              "type": "number",
              "description": "Bond path distance to X atom in atomic units"
            },
            "bond_path_RY": {
              "type": "number"
            },
            "rho_b": {
              "type": "number",
              "description": "Electron density at BCP in atomic units"
            },
            "laplacian_rho": {
              "type": "number"
            },
            "ellipticity": {
              "type": "number"
            },
            "Vr": {
              "type": "number",
              "description": "Virial field function in atomic units"
            },
            "Gr": {
              "type": "number",
              "description": "Kinetic energy density in atomic units"
            }
          }
        }
      },
      "description": "QTAIM bond critical point parameters for compound 8 and polymorphs 9a, 9b."
    },
    {
      "file": "hirshfeld_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "8",
          "9a",
          "9b"
        ],
        "properties": {
          "8": {
            "type": "object",
            "required": [
              "contact_percentages",
              "interaction_energies"
            ],
            "properties": {
              "contact_percentages": {
                "type": "object",
                "required": [
                  "HH",
                  "CH",
                  "NH"
                ],
                "properties": {
                  "HH": {
                    "type": "number"
                  },
                  "CH": {
                    "type": "number"
                  },
                  "NH": {
                    "type": "number"
                  }
                }
              },
              "interaction_energies": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "polymorph",
                    "color",
                    "symop_AB",
                    "R_AB",
                    "E_ele",
                    "E_pol",
                    "E_dis",
                    "E_rep",
                    "E_tot"
                  ],
                  "properties": {
                    "polymorph": {
                      "type": "string",
                      "enum": [
                        "9a",
                        "9b"
                      ]
                    },
                    "color": {
                      "type": "string"
                    },
                    "symop_AB": {
                      "type": "string"
                    },
                    "R_AB": {
                      "type": "number",
                      "description": "Distance between molecular centroids in Å"
                    },
                    "E_ele": {
                      "type": "number",
                      "description": "Electrostatic component (kJ/mol)"
                    },
                    "E_pol": {
                      "type": "number",
                      "description": "Polarization component (kJ/mol)"
                    },
                    "E_dis": {
                      "type": "number",
                      "description": "Dispersion component (kJ/mol)"
                    },
                    "E_rep": {
                      "type": "number",
                      "description": "Exchange-repulsion component (kJ/mol)"
                    },
                    "E_tot": {
                      "type": "number",
                      "description": "Total interaction energy (kJ/mol)"
                    }
                  }
                }
              }
            }
          },
          "9a": {
            "$ref": "#/properties/8"
          },
          "9b": {
            "$ref": "#/properties/8"
          }
        }
      },
      "description": "Hirshfeld surface contact percentages and CE‑B3LYP pair interaction energies for crystals 8, 9a, 9b."
    }
  ],
  "notes": "All reported values must be derived from the CIF structures and the described computational workflow. The checker will compare the agent's values to the paper's published reference values within predefined tolerances."
}
```

## How you are scored
A hidden verifier independently checks your two output files. For QTAIM parameters, the verifier compares your reported values (ρ, ∇²ρ, ε, V(r), G(r)) for each interaction against reference values obtained from the original computational protocol, allowing for the expected spread due to different DFT implementations and basis sets. For Hirshfeld results, contact percentages are compared within a tolerance, and each interaction energy component is compared to reference values with a relative tolerance. The final reward is the weighted fraction of parameters that fall within the allowed tolerances, averaged over both files. The verifier does not see your workflow code; only the content of the two JSON files is evaluated.
