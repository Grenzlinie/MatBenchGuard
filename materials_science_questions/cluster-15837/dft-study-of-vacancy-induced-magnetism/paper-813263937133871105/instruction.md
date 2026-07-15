# Formation energies and magnetic moments of defects in 2D h-BNC₂ from DFT

## Problem background
Two-dimensional hybrid h-BNC₂ monolayers, composed of phase-separated graphene and hexagonal boron nitride domains, offer a tunable platform for electronic and magnetic applications. The presence of structural defects — single vacancies, double vacancies, and Stone–Wales rotations — can significantly alter the material’s stability and induce magnetism, but the energetic and magnetic landscape depends strongly on the defect's location relative to the C–N and C–B interfaces. This task aims to compute the formation energies, magnetic moments, and local structural distortions of a comprehensive set of such defects in an 80‑atom supercell, providing a detailed defect map that reveals how interface proximity controls these properties.

## Approach
Use spin‑polarized density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional. The calculations are performed with an open‑source plane‑wave code (Quantum ESPRESSO) and projector‑augmented‑wave (PAW) pseudopotentials from the SSSP efficiency library. 

Start from an 80‑atom h‑BNC₂ supercell with five zigzag chains each of C and BN, separated by zigzag C–N and C–B interfaces, and a lattice constant of 2.5 Å. Create 35 defective structures: 11 single vacancies (C1–C5, B1–B3, N1–N3), 12 double vacancies (CC1–CC5, BN1–BN5, CB, CN), and 12 Stone–Wales defects (SW1-N…SW6-N, SW1-B…SW6-B). Relax each structure, including the pristine supercell, until forces fall below 0.01 eV/Å, keeping the lattice constants fixed. 

Formation energies are obtained from the total energies of the defective and pristine sheets together with reference chemical potentials: 
Ef = E_defect + Σ n_X μ_X − E_pristine, 
where μ_C is taken from graphene, μ_B from α‑boron, and μ_N from an α‑N₂ molecule (all computed with the same DFT protocol). For single vacancies, the three nearest‑neighbour distances (x, y, z) around each vacancy are also extracted from the relaxed geometries. Finally, organise the results into three JSON files as specified in the workflow steps.

## Reproduction target
Produce three JSON artifacts under /app/outputs:

1. `single_vacancy_results.json` – an array of 11 objects, one for each single vacancy (C1–C5, B1–B3, N1–N3), each containing the defect label, formation energy (eV), total magnetic moment (μB), and the three interatomic distances x, y, z (Å).

2. `double_vacancy_results.json` – an array of 12 objects, one for each double vacancy (CC1–CC5, BN1–BN5, CB, CN), with the defect label, formation energy (eV), and total magnetic moment (μB).

3. `stone_wales_results.json` – an array of 12 objects, one for each Stone–Wales defect (SW1‑N…SW6‑N, SW1‑B…SW6‑B), with the defect label, formation energy (eV), and total magnetic moment (μB).

The values must be computed by re‑running the DFT workflow as described; simply reporting numbers from the literature is not sufficient.

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct pristine 80-atom h-BNC₂ supercell
- Role: process
- Action: Build the atomic structure of the 80-atom h-BNC₂ supercell with five zigzag chains of C and BN each, phase-separated domains with zigzag C–N and C–B interfaces, lattice constant 2.5 Å, and add at least 12 Å vacuum between periodic images. Save as pristine_80atom.xyz.
- Evidence: `/app/outputs/pristine_80atom.xyz`

### Step 2: DFT relaxation and total energy of pristine 80-atom supercell
- Role: process
- Action: Perform spin-polarized DFT structural relaxation on the pristine 80-atom supercell using Quantum ESPRESSO with a plane-wave cutoff of 550 eV, a (9×3×1) Monkhorst–Pack k-point grid, PBE functional, and SSSP pseudopotentials. Relax all internal coordinates until forces are below 0.01 eV/Å while keeping lattice constants fixed. Write the relaxed geometry to pristine_relaxed.xyz and record the total energy for formation energy calculations.
- Evidence: `/app/outputs/pristine_relaxed.xyz`

### Step 3: Construct all defective 80-atom supercells
- Role: process
- Action: Starting from the pristine 80-atom supercell, create the 35 defective structures: 11 single vacancies (C1–C5, B1–B3, N1–N3), 12 double vacancies (CC1–CC5, BN1–BN5, CB, CN), and 12 Stone–Wales defects (SW1-N…SW6-N, SW1-B…SW6-B) as labeled in the paper. Save their initial geometries (e.g., in a directory or archive).
- Evidence: `/app/outputs/defect_structures.txt`

### Step 4: DFT relaxations and total energies of all defective supercells
- Role: process
- Action: For each defective structure, run spin-polarized DFT relaxation with the same parameters as the pristine calculation (cutoff 550 eV, (9×3×1) k‑mesh, PBE, SSSP pseudopotentials, force tolerance 0.01 eV/Å). Collect the relaxed geometry, total energy, and raw magnetic moment for each defect. Package the relaxed geometries into an archive defect_relaxed_geometries.zip.
- Evidence: `/app/outputs/defect_relaxed_geometries.zip`

### Step 5: Compute reference chemical potentials
- Role: process
- Action: Perform separate DFT calculations for the reference phases: graphene (C), α-boron (B), and α-N₂ molecule, using the same DFT protocol. Extract the energy per atom (or per molecule) to obtain μ_C, μ_B, μ_N. Write these numbers to reference_energies.txt.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 6: Formation energies, magnetic moments, and distances for single vacancies
- Role: scored (load-bearing)
- Action: From the DFT outputs, compute the formation energy for each single vacancy using Ef = E_defect + Σ n_X μ_X - E_pristine. Extract the total magnetic moment from the self‑consistent calculation. Measure the three interatomic distances x, y, z between the three nearest atoms around the vacancy. Write all results to single_vacancy_results.json.
- Output file: `/app/outputs/single_vacancy_results.json`
- Format: json
- Contract: array of objects with fields defect_label, formation_energy_ev, magnetic_moment_muB, x_angstrom, y_angstrom, z_angstrom
- Scoring: scored by hidden verifier

### Step 7: Formation energies and magnetic moments for double vacancies
- Role: scored
- Action: For each double vacancy, compute formation energy and total magnetic moment as above. Write results to double_vacancy_results.json.
- Output file: `/app/outputs/double_vacancy_results.json`
- Format: json
- Contract: array of objects with fields defect_label, formation_energy_ev, magnetic_moment_muB
- Scoring: scored by hidden verifier

### Step 8: Formation energies and magnetic moments for Stone–Wales defects
- Role: scored
- Action: For each of the 12 Stone–Wales defects, compute formation energy and total magnetic moment. Write results to stone_wales_results.json.
- Output file: `/app/outputs/stone_wales_results.json`
- Format: json
- Contract: array of objects with fields defect_label, formation_energy_ev, magnetic_moment_muB
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_vacancy_results.json`
- `/app/outputs/double_vacancy_results.json`
- `/app/outputs/stone_wales_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_vacancy_results.json
- path: `/app/outputs/single_vacancy_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies (eV), total magnetic moments (μB), and the three nearest-neighbor distances (Å) for each of the 11 single vacancies.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect_label`, `formation_energy_ev`, `magnetic_moment_muB`, `x_angstrom`, `y_angstrom`, `z_angstrom`
    - `properties`:
      - `defect_label`:
        - `type`: string
      - `formation_energy_ev`:
        - `type`: number
      - `magnetic_moment_muB`:
        - `type`: number
      - `x_angstrom`:
        - `type`: number
      - `y_angstrom`:
        - `type`: number
      - `z_angstrom`:
        - `type`: number

### double_vacancy_results.json
- path: `/app/outputs/double_vacancy_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies (eV) and total magnetic moments (μB) for the 12 double-vacancy defects.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect_label`, `formation_energy_ev`, `magnetic_moment_muB`
    - `properties`:
      - `defect_label`:
        - `type`: string
      - `formation_energy_ev`:
        - `type`: number
      - `magnetic_moment_muB`:
        - `type`: number

### stone_wales_results.json
- path: `/app/outputs/stone_wales_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies (eV) and total magnetic moments (μB) for the 12 Stone–Wales defects.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect_label`, `formation_energy_ev`, `magnetic_moment_muB`
    - `properties`:
      - `defect_label`:
        - `type`: string
      - `formation_energy_ev`:
        - `type`: number
      - `magnetic_moment_muB`:
        - `type`: number

Notes: The checker compares each defect's reported values against the paper's Tables 1–3 using tolerances that absorb toolchain differences (Quantum ESPRESSO vs VASP) and verifies key relative orderings. No absolute values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_vacancy_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect_label",
            "formation_energy_ev",
            "magnetic_moment_muB",
            "x_angstrom",
            "y_angstrom",
            "z_angstrom"
          ],
          "properties": {
            "defect_label": {
              "type": "string"
            },
            "formation_energy_ev": {
              "type": "number"
            },
            "magnetic_moment_muB": {
              "type": "number"
            },
            "x_angstrom": {
              "type": "number"
            },
            "y_angstrom": {
              "type": "number"
            },
            "z_angstrom": {
              "type": "number"
            }
          }
        }
      },
      "description": "Formation energies (eV), total magnetic moments (μB), and the three nearest-neighbor distances (Å) for each of the 11 single vacancies."
    },
    {
      "file": "double_vacancy_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect_label",
            "formation_energy_ev",
            "magnetic_moment_muB"
          ],
          "properties": {
            "defect_label": {
              "type": "string"
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
      "description": "Formation energies (eV) and total magnetic moments (μB) for the 12 double-vacancy defects."
    },
    {
      "file": "stone_wales_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect_label",
            "formation_energy_ev",
            "magnetic_moment_muB"
          ],
          "properties": {
            "defect_label": {
              "type": "string"
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
      "description": "Formation energies (eV) and total magnetic moments (μB) for the 12 Stone–Wales defects."
    }
  ],
  "notes": "The checker compares each defect's reported values against the paper's Tables 1–3 using tolerances that absorb toolchain differences (Quantum ESPRESSO vs VASP) and verifies key relative orderings. No absolute values or tolerances are disclosed here."
}
```

## How you are scored
Each of the three output files is evaluated independently by a hidden verifier. The verifier compares your reported formation energies, magnetic moments, and distances (where applicable) to a hidden reference, using tolerances that account for the expected spread when switching from one DFT code to another. In addition, the verifier checks that the relative ordering of formation energies within each defect group follows physically expected trends (e.g., certain defects at the interface should be less costly than those deeper in the domains). The final score is a weighted combination of the three stages: single vacancies carry the largest weight because they include structural distances as well, double vacancies an intermediate weight, and Stone–Wales defects a smaller weight. Meeting the reference or the expected ordering within tolerance earns full credit for that stage; credit decreases as the deviation grows.
