# Point defect formation and electronic structure from DFT

## Problem background
Wadsleyite (β-Mg₂SiO₄) is a high‑pressure mineral thought to be the dominant component of the Earth’s mantle between depths of 410 and 520 km. It can incorporate significant amounts of water through point defects, where H⁺ replaces missing Mg²⁺ cations. The local arrangement of these defects—which Mg sites are vacant, which oxygens are protonated, and how the hydroxyl groups are oriented—governs the mineral’s physical and chemical properties, yet it remains challenging to determine experimentally because of structural disorder. Solid‑state NMR spectroscopy probes local environments without requiring long‑range order, but interpreting the spectra requires a large ensemble of plausible structural models and their predicted NMR parameters.

## Approach
The workflow combines ab initio random structure searching (AIRSS) with plane‑wave DFT geometry optimization, k‑means clustering, and GIPAW NMR calculations. Starting from the known anhydrous wadsleyite crystal structure, Mg vacancies are introduced to create semihydrous (1.65 wt% H₂O) and fully hydrous (3.3 wt% H₂O) compositions, with charge‑balancing H atoms placed randomly near the vacancies. These candidate structures are relaxed with a low‑accuracy DFT protocol, then clustered into distinct motifs using structural descriptors and relative enthalpies. A diverse, low‑enthalpy subset is re‑optimised at high accuracy (including dispersion corrections, higher cutoffs, and cell relaxation) and predicted ¹H isotropic chemical shifts and relative enthalpies are extracted. The final step identifies the low‑enthalpy protonation motifs that match experimental NMR signatures.

## Reproduction target
Execute the pipeline to produce a JSON file containing the relative enthalpies (ΔH, in eV, with respect to the most stable structure of the same hydration level) and the predicted ¹H isotropic chemical shifts (δ_iso, in ppm) for the five key protonation motifs: a semihydrous motif with a single Mg3 vacancy and two O1–H hydroxyls; and fully hydrous motifs with (i) two isolated Mg3 vacancies separated by ~7.1 Å, (ii) two closely‑spaced Mg3 vacancies along the y direction, (iii) two closely‑spaced Mg3 vacancies along the x direction, and (iv) edge‑sharing Mg1 and Mg3 vacancies. All quantities must be written to `/app/outputs/motif_properties.json` according to the schema specified in the output contract.

## Assets

- ASE (Atomic Simulation Environment): python package (pip install ase)
- Soprano: python package (pip install soprano) — https://ccp-nc.github.io/soprano/
- CASTEP or open-source plane-wave DFT code with GIPAW (e.g., Quantum ESPRESSO with GIPAW module): CASTEP available at http://www.castep.org/; Quantum ESPRESSO open-source.
- Anhydrous wadsleyite crystal structure (β-Mg₂SiO₄): ICSD entry or from Horiuchi & Sawamoto 1981 (doi:10.1021/jacs.8b11519 supporting information)

## Workflow steps

### Step 1: Generate defect-containing structures
- Role: process
- Action: Generate hydrated wadsleyite candidate structures for semihydrous (1.65 wt% H₂O) and fully hydrous (3.3 wt% H₂O) compositions using the AIRSS protocol: start from anhydrous unit cell, create Mg vacancies by removing selected Mg²⁺ cations, add charge-balancing H⁺ (two per Mg vacancy) randomly within a 3.0 Å radius of the vacancy while keeping other atoms fixed, enforce minimum interatomic separation of 0.75 Å. Produce ensembles of several hundred candidates per composition.
- Evidence: `/app/outputs/airss_structures.xyz`

### Step 2: Low-accuracy DFT geometry optimization
- Role: process
- Action: Perform plane-wave DFT geometry optimization on all AIRSS-generated structures using a GGA functional (e.g., PBE), moderate planewave cutoff and coarse k-point mesh (~0.1 2π/Å). Relax atomic positions only; output total energies.
- Evidence: `/app/outputs/low_opt_energies.json`

### Step 3: k-means clustering and structure selection
- Role: process
- Action: Compute structural descriptors (genes) for each relaxed structure: relative enthalpy, Mg vacancy type, type of protonated oxygen, and relative orientation of OH bond vectors. Cluster the candidate ensembles with k-means algorithm and select a diverse, low-enthalpy subset of representative structures (~50–100 per composition).
- Evidence: `/app/outputs/selected_structure_indices.json`

### Step 4: High-accuracy DFT optimization and GIPAW NMR calculation
- Role: process
- Action: Re-optimize the selected structures using a more accurate protocol: GGA+dispersion correction, higher planewave cutoff (≥60 Ry), denser k-point mesh (spacing ~0.04 2π/Å), relaxation of atomic positions and unit cell vectors. After optimization, compute absolute shielding tensors via the GIPAW method, convert isotropic shielding to ¹H isotropic chemical shift (δ_iso) using a suitable reference. For each structure, store total enthalpy and list of all ¹H δ_iso values.
- Evidence: `/app/outputs/high_accuracy_results.csv`

### Step 5: Compile motif properties
- Role: scored (load-bearing)
- Action: From the high-accuracy results, identify the structures corresponding to the key protonation motifs and compile a JSON file. Semihydrous motif A: ground-state structure with a single Mg3 vacancy and two O1–H hydroxyls. Fully hydrous motif G: lowest-enthalpy structure with two isolated Mg3 vacancies separated by ~7.1 Å. Motif H: structure with two Mg3 vacancies separated by ~2.9 Å along the y lattice vector. Motif I: structure with two Mg3 vacancies separated by ~2.9 Å along the x lattice vector. Motif J: structure with edge-sharing Mg1 and Mg3 vacancies at ~2.9 Å. For each motif, report the relative enthalpy ΔH (eV) with respect to the most stable structure of that hydration level, and a list of all ¹H isotropic chemical shifts (ppm).
- Output file: `/app/outputs/motif_properties.json`
- Format: json
- Contract: JSON object with keys "A", "G", "H", "I", "J". Each value is an object: { "delta_H_eV": float, "H1_chemical_shifts_ppm": [float, ...] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/motif_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### motif_properties.json
- path: `/app/outputs/motif_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Relative enthalpies (eV) and ¹H isotropic chemical shifts (ppm) for the five low-enthalpy protonation motifs (A, G, H, I, J).
- schema:
  - `type`: object
  - `required`: `A`, `G`, `H`, `I`, `J`
  - `properties`:
    - `A`:
      - `type`: object
      - `required`: `delta_H_eV`, `H1_chemical_shifts_ppm`
      - `properties`:
        - `delta_H_eV`:
          - `type`: number
        - `H1_chemical_shifts_ppm`:
          - `type`: array
          - `items`:
            - `type`: number
    - `G`:
      - `type`: object
      - `required`: `delta_H_eV`, `H1_chemical_shifts_ppm`
      - `properties`:
        - `delta_H_eV`:
          - `type`: number
        - `H1_chemical_shifts_ppm`:
          - `type`: array
          - `items`:
            - `type`: number
    - `H`:
      - `type`: object
      - `required`: `delta_H_eV`, `H1_chemical_shifts_ppm`
      - `properties`:
        - `delta_H_eV`:
          - `type`: number
        - `H1_chemical_shifts_ppm`:
          - `type`: array
          - `items`:
            - `type`: number
    - `I`:
      - `type`: object
      - `required`: `delta_H_eV`, `H1_chemical_shifts_ppm`
      - `properties`:
        - `delta_H_eV`:
          - `type`: number
        - `H1_chemical_shifts_ppm`:
          - `type`: array
          - `items`:
            - `type`: number
    - `J`:
      - `type`: object
      - `required`: `delta_H_eV`, `H1_chemical_shifts_ppm`
      - `properties`:
        - `delta_H_eV`:
          - `type`: number
        - `H1_chemical_shifts_ppm`:
          - `type`: array
          - `items`:
            - `type`: number

Notes: The checker will compare the reported values against hidden gold values from the paper using tolerances ±0.1 eV for ΔH and ±0.5 ppm for chemical shift. Meeting or exceeding the reference within these tolerances earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "motif_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "A",
          "G",
          "H",
          "I",
          "J"
        ],
        "properties": {
          "A": {
            "type": "object",
            "required": [
              "delta_H_eV",
              "H1_chemical_shifts_ppm"
            ],
            "properties": {
              "delta_H_eV": {
                "type": "number"
              },
              "H1_chemical_shifts_ppm": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "G": {
            "type": "object",
            "required": [
              "delta_H_eV",
              "H1_chemical_shifts_ppm"
            ],
            "properties": {
              "delta_H_eV": {
                "type": "number"
              },
              "H1_chemical_shifts_ppm": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "H": {
            "type": "object",
            "required": [
              "delta_H_eV",
              "H1_chemical_shifts_ppm"
            ],
            "properties": {
              "delta_H_eV": {
                "type": "number"
              },
              "H1_chemical_shifts_ppm": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "I": {
            "type": "object",
            "required": [
              "delta_H_eV",
              "H1_chemical_shifts_ppm"
            ],
            "properties": {
              "delta_H_eV": {
                "type": "number"
              },
              "H1_chemical_shifts_ppm": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          },
          "J": {
            "type": "object",
            "required": [
              "delta_H_eV",
              "H1_chemical_shifts_ppm"
            ],
            "properties": {
              "delta_H_eV": {
                "type": "number"
              },
              "H1_chemical_shifts_ppm": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Relative enthalpies (eV) and ¹H isotropic chemical shifts (ppm) for the five low-enthalpy protonation motifs (A, G, H, I, J)."
    }
  ],
  "notes": "The checker will compare the reported values against hidden gold values from the paper using tolerances ±0.1 eV for ΔH and ±0.5 ppm for chemical shift. Meeting or exceeding the reference within these tolerances earns full credit."
}
```

## How you are scored
A hidden verifier evaluates each scored artifact independently and combines the stage scores into a final reward (a float between 0 and 1). The verifier checks structural correctness of the output files and compares your reported values to reference expectations without revealing them. Reporting numbers that match the paper is not sufficient; the verifier assesses whether the quantities are physically plausible and consistent with a correct execution of the pipeline. The exact tolerances and weighting are applied server‑side; you must follow the output contract exactly and write every required file under `/app/outputs` for full credit.
