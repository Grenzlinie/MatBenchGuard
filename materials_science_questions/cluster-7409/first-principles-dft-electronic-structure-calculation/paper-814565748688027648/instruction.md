# First-principles DFT study of Ag extended adlayers on NbO-terminated KNbO3(101) surface

## Problem background
Silver nanoparticles supported on perovskite KNbO₃ nanowires exhibit enhanced photocatalytic activity for the degradation of organic pollutants, but the underlying interaction between the Ag adlayer and the oxide surface is not fully understood. Density functional theory (DFT) calculations have been used to investigate the adsorption behaviour of extended Ag layers on the NbO-terminated KNbO₃(101) surface, providing key quantities such as adsorption energies, structural parameters, work function changes, and charge transfer. This task aims to reproduce these first-principles predictions for a series of Ag coverages.

## Approach
The method employs spin-polarized DFT with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and plane-wave basis sets, using ultra-soft or PAW pseudopotentials. The KNbO₃(101) surface is modelled with a three-bi-layer slab terminated by NbO, and Ag adlayers of 1, 2, and 4 monolayers (ML) are placed in a close-packed arrangement on the surface. Geometry relaxations are performed for the bare surface, an isolated Ag atom, and each Ag-covered slab, allowing the topmost bi-layer and the Ag atoms to relax while the lower layers remain fixed. The total energies are then used to compute the adsorption energy per Ag atom as the difference between the adsorbed system and the sum of the bare slab and isolated Ag energies, divided by the number of Ag atoms. Post-processing evaluates the shortest Ag–O bond length, the change in work function relative to the bare surface, and the surface dipole moment derived from the Bader charge and the distance between the Ag layer and the surface. The work is carried out with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and the Bader charge analysis tool.

## Reproduction target
The goal is to compute the following properties for Ag coverages of 1 ML, 2 ML, and 4 ML on the NbO-terminated KNbO₃(101) surface:
- Adsorption energy per Ag atom (eV/atom)
- Shortest Ag–O bond distance (Å)
- Work function change Δφ (eV)
- Surface dipole moment (D)
In addition, the net Bader charge transferred to the Ag adlayer (e) must be determined. All results should be collected into a single JSON file `dft_results.json` under `/app/outputs`, following the structure given in the output contract.

## Assets

- Orthorhombic KNbO3 crystal structure (JCPDS 71-2171 / Materials Project mp-19056): https://materialsproject.org/materials/mp-19056/
- SSSP pseudopotential library (PBE) – Ag, K, Nb, O: https://www.materialscloud.org/discover/sssp
- Quantum ESPRESSO (or equivalent open‑source DFT package): https://www.quantum-espresso.org/download
- Bader charge analysis code (Henkelman group): https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build slab models and Ag adlayer configurations
- Role: process
- Action: Construct a three‑bi‑layer orthorhombic KNbO3(101) slab with NbO‑termination from the bulk crystal structure. Create the bare slab geometry and Ag‑covered slab geometries for coverages of 1, 2, and 4 ML (1 ML = 1 Ag atom per 1×1 surface unit cell). Fix the bottom two bi‑layers; the top bi‑layer and Ag will be relaxed later.
- Evidence: none

### Step 2: DFT relaxation of bare KNbO3(101) surface
- Role: process
- Action: Perform spin‑polarized DFT geometry relaxation of the bare NbO‑terminated KNbO3(101) slab, relaxing the top bi‑layer atoms until forces are < 0.01 eV/Å while the bottom two bi‑layers remain fixed. Save the total energy (Esurf) and the relaxed geometry for reference.
- Evidence: none

### Step 3: DFT calculation of gas‑phase Ag atom
- Role: process
- Action: Compute the total energy of a single Ag atom in a large isolated unit cell using the same DFT method and pseudopotential as for the slab calculations. Save the resulting energy (EAg) for the adsorption energy formula.
- Evidence: none

### Step 4: DFT relaxation of Ag/KNbO3(101) for each coverage
- Role: process
- Action: For each Ag coverage (1, 2, 4 ML), perform a spin‑polarized DFT geometry relaxation of the Ag adlayer placed on the NbO‑terminated KNbO3(101) slab, allowing the top bi‑layer and Ag atoms to relax until forces are < 0.01 eV/Å. Save the total energies (EnAg/surf) and the relaxed structures for post‑processing.
- Evidence: none

### Step 5: Extract adsorption properties and Bader charge
- Role: scored (load-bearing)
- Action: From the DFT outputs of the previous steps, compute for each coverage: (i) adsorption energy per Ag atom using Eads = [E(nAg/surf) – Esurf – n·EAg]/n; (ii) shortest Ag–O bond distance; (iii) work function change Δφ (difference between the electrostatic potential of the covered and bare slab); (iv) dipole moment μ = (charge from Bader analysis)×(distance from Ag layer to surface); and (v) net Bader charge on the Ag adlayer. Collect all results into a single JSON file dft_results.json with the structure described in the output schema.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {
  "coverage_data": [
    {
      "coverage": "1 ML",
      "E_ads_eV_per_atom": number,
      "d_Ag_O_angstrom": number,
      "Delta_phi_eV": number,
      "mu_D": number
    },
    {
      "coverage": "2 ML",
      "E_ads_eV_per_atom": number,
      "d_Ag_O_angstrom": number,
      "Delta_phi_eV": number,
      "mu_D": number
    },
    {
      "coverage": "4 ML",
      "E_ads_eV_per_atom": number,
      "d_Ag_O_angstrom": number,
      "Delta_phi_eV": number,
      "mu_D": number
    }
  ],
  "bader_charge_Ag_e": number
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored JSON file containing adsorption energies per Ag atom, Ag–O bond lengths, work function changes, dipole moments for 1,2,4 ML Ag coverages, and net Bader charge on Ag.
- schema:
  - `type`: object
  - `required`: `coverage_data`, `bader_charge_Ag_e`
  - `properties`:
    - `coverage_data`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `coverage`, `E_ads_eV_per_atom`, `d_Ag_O_angstrom`, `Delta_phi_eV`, `mu_D`
        - `properties`:
          - `coverage`:
            - `type`: string
            - `enum`: `1 ML`, `2 ML`, `4 ML`
          - `E_ads_eV_per_atom`:
            - `type`: number
            - `units`: eV/atom
          - `d_Ag_O_angstrom`:
            - `type`: number
            - `units`: Å
          - `Delta_phi_eV`:
            - `type`: number
            - `units`: eV
          - `mu_D`:
            - `type`: number
            - `units`: D
    - `bader_charge_Ag_e`:
      - `type`: number
      - `units`: e

Notes: The checker compares each numeric field against hidden paper‑reported values with a tolerance and verifies monotonic coverage trends. Meeting or exceeding the reference (more negative Eads, larger d, Δφ, decreasing μ) within tolerance earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "coverage_data",
          "bader_charge_Ag_e"
        ],
        "properties": {
          "coverage_data": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "coverage",
                "E_ads_eV_per_atom",
                "d_Ag_O_angstrom",
                "Delta_phi_eV",
                "mu_D"
              ],
              "properties": {
                "coverage": {
                  "type": "string",
                  "enum": [
                    "1 ML",
                    "2 ML",
                    "4 ML"
                  ]
                },
                "E_ads_eV_per_atom": {
                  "type": "number",
                  "units": "eV/atom"
                },
                "d_Ag_O_angstrom": {
                  "type": "number",
                  "units": "Å"
                },
                "Delta_phi_eV": {
                  "type": "number",
                  "units": "eV"
                },
                "mu_D": {
                  "type": "number",
                  "units": "D"
                }
              }
            }
          },
          "bader_charge_Ag_e": {
            "type": "number",
            "units": "e"
          }
        }
      },
      "description": "Scored JSON file containing adsorption energies per Ag atom, Ag–O bond lengths, work function changes, dipole moments for 1,2,4 ML Ag coverages, and net Bader charge on Ag."
    }
  ],
  "notes": "The checker compares each numeric field against hidden paper‑reported values with a tolerance and verifies monotonic coverage trends. Meeting or exceeding the reference (more negative Eads, larger d, Δφ, decreasing μ) within tolerance earns full credit."
}
```

## How you are scored
A hidden verifier will examine `dft_results.json`. It compares each numeric field against independently established reference values using appropriate tolerances and checks that the monotonic trends expected across coverages are satisfied. Credit is full when all values meet their tolerances and all trends hold; partial credit may be awarded proportionally if some coverages pass while others do not. The reward is monotonic in performance: a result that equals or improves upon the reference within tolerance earns full points, while a result that deviates by more than the allowed amount loses points. The verifier does not penalise a result that is more extreme than the paper's value in the favourable direction.
