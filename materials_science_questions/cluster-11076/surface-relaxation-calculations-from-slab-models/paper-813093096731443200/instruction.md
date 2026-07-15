# Surface relaxation and adsorption energy calculations of LiF molecules on CaF₂(111)

## Problem background
Lithium fluoride (LiF) molecules adsorb on the (111) surface of calcium fluoride (CaF₂), an alkaline earth fluoride with fluorite structure. Understanding this adsorption is crucial for epitaxial growth and nucleation, where LiF crystallites form on CaF₂ substrates. The adsorption energies, site preferences, and the fate of molecular dimers (rhombic Li₂F₂ and linear Li₂F₂) influence growth modes and dissociation behaviour. Reproducing these adsorption energies from a classical force-field model provides a benchmark for surface science computations and validates the theoretical framework underpinning experimental observations.

## Approach
The approach uses classical pair potentials (Catlow-type) to describe interactions between ions (Li⁺, F⁻, Ca²⁺). The CaF₂(111) surface is modelled as a periodic slab of four F⁻–Ca²⁺–F⁻ triple layers. Long-range Coulomb interactions are computed via a two-dimensional Ewald summation, while short-range interactions include Born–Mayer repulsion and van der Waals attraction. First, the free molecules are minimized to obtain reference geometries and energies. Then the pristine surface and a [10-1] type I monatomic step are relaxed by allowing the outermost ion layers to move. Finally, for each adsorbate (LiF monomer, rhombic dimer, linear dimer), the molecule plus a region of crystal ions near the adsorption site are relaxed to determine the equilibrium adsorption energy and its components. The workflow separates contributions into region relaxation energy, molecular deformation energy, and molecule–crystal interaction energy.

## Reproduction target
Compute the total adsorption energies (E_ad) and their decomposition (E_reg_rel, E_mol_rel, E_int) for each of the three molecular species (monomer M, rhombic dimer Dr, linear dimer Dl) on the relaxed CaF₂(111) terrace and at the relaxed [10-1] type I step. Output the six cases as a JSON file with energies in eV. The result must reproduce the correct ordering of adsorption strengths among different species and between terrace and step sites, and the monomer step adsorption energy must be consistent with the known experimental value (the verifier will check against a reference).

## Assets

- Catlow-type empirical pair potentials for LiF and CaF2: 10.1088/0022-3719/10/8/032 and 10.1088/0022-3719/10/9/032
- CaF2 lattice constant: https://nvlpubs.nist.gov/nistpubs/Legacy/MONO/nbsmonograph25-21.pdf

## Workflow steps

### Step 1: Free molecule reference calculations
- Role: process
- Action: Compute equilibrium geometries, binding energies, and dissociation energies for the free LiF monomer, rhombic Li₂F₂ dimer, and linear Li₂F₂ dimer using the Catlow-type pair potentials. These serve as reference states for the adsorption energy decomposition.
- Evidence: `/app/outputs/free_molecule_ref.json`

### Step 2: CaF₂(111) surface relaxation
- Role: process
- Action: Construct a slab of four F⁻–Ca²⁺–F⁻ triple layers with the bulk lattice constant. Using 2D Ewald summation for long‑range Coulomb and the Catlow potentials, minimize the energy of the outermost triple layer to obtain the relaxed (111) surface geometry.
- Evidence: `/app/outputs/surface_relaxation.json`

### Step 3: Step relaxation (type I [10-1])
- Role: process
- Action: Starting from the relaxed surface, build a [10-1] type I step and relax the four key ion rows (Ca, F1, F2, F3) at the step edge using hybrid direct real‑space summation for the near‑step region and 2D Ewald for the bulk.
- Evidence: `/app/outputs/step_relaxation.json`

### Step 4: Adsorption energy calculations on terrace and step
- Role: scored (load-bearing)
- Action: For each admolecule (monomer M, rhombic dimer Dr, linear dimer Dl) perform energy minimizations on the relaxed terrace and at the relaxed step. In each minimization, allow the admolecule and an adregion of crystal ions from the outer triple layer to relax. Compute the total adsorption energy E_ad and its components (E_reg_rel, E_mol_rel, E_int) using the free‑molecule references. Output all six cases in a single JSON file.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {"type":"object","required":["terrace_M","terrace_Dr","terrace_Dl","step_M","step_Dr","step_Dl"],"properties":{"terrace_M":{"type":"object","required":["E_ad","E_reg_rel","E_mol_rel","E_int"],"properties":{"E_ad":{"type":"number"},"E_reg_rel":{"type":"number"},"E_mol_rel":{"type":"number"},"E_int":{"type":"number"}}},"terrace_Dr":{"type":"object","required":["E_ad","E_reg_rel","E_mol_rel","E_int"]},"terrace_Dl":{"type":"object","required":["E_ad","E_reg_rel","E_mol_rel","E_int"]},"step_M":{"type":"object","required":["E_ad","E_reg_rel","E_mol_rel","E_int"]},"step_Dr":{"type":"object","required":["E_ad","E_reg_rel","E_mol_rel","E_int"]},"step_Dl":{"type":"object","required":["E_ad","E_reg_rel","E_mol_rel","E_int"]}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total adsorption energies and components (in eV) for LiF monomer, rhombic dimer, and linear dimer on the relaxed CaF₂(111) terrace and at the relaxed [10-1] type I step.
- schema:
  - `type`: object
  - `required`: `terrace_M`, `terrace_Dr`, `terrace_Dl`, `step_M`, `step_Dr`, `step_Dl`
  - `properties`:
    - `terrace_M`:
      - `type`: object
      - `required`: `E_ad`, `E_reg_rel`, `E_mol_rel`, `E_int`
      - `properties`:
        - `E_ad`:
          - `type`: number
        - `E_reg_rel`:
          - `type`: number
        - `E_mol_rel`:
          - `type`: number
        - `E_int`:
          - `type`: number
    - `terrace_Dr`:
      - `type`: object
      - `required`: `E_ad`, `E_reg_rel`, `E_mol_rel`, `E_int`
    - `terrace_Dl`:
      - `type`: object
      - `required`: `E_ad`, `E_reg_rel`, `E_mol_rel`, `E_int`
    - `step_M`:
      - `type`: object
      - `required`: `E_ad`, `E_reg_rel`, `E_mol_rel`, `E_int`
    - `step_Dr`:
      - `type`: object
      - `required`: `E_ad`, `E_reg_rel`, `E_mol_rel`, `E_int`
    - `step_Dl`:
      - `type`: object
      - `required`: `E_ad`, `E_reg_rel`, `E_mol_rel`, `E_int`

Notes: All energies must be in electronvolts (eV). The free-molecule reference energies are required to compute E_mol_rel; the relaxation of the pure surface and step provides the starting configurations. The check compares each E_ad to a reference value with tolerance and verifies relative ordering and consistency with an experimental monomer step value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "terrace_M",
          "terrace_Dr",
          "terrace_Dl",
          "step_M",
          "step_Dr",
          "step_Dl"
        ],
        "properties": {
          "terrace_M": {
            "type": "object",
            "required": [
              "E_ad",
              "E_reg_rel",
              "E_mol_rel",
              "E_int"
            ],
            "properties": {
              "E_ad": {
                "type": "number"
              },
              "E_reg_rel": {
                "type": "number"
              },
              "E_mol_rel": {
                "type": "number"
              },
              "E_int": {
                "type": "number"
              }
            }
          },
          "terrace_Dr": {
            "type": "object",
            "required": [
              "E_ad",
              "E_reg_rel",
              "E_mol_rel",
              "E_int"
            ]
          },
          "terrace_Dl": {
            "type": "object",
            "required": [
              "E_ad",
              "E_reg_rel",
              "E_mol_rel",
              "E_int"
            ]
          },
          "step_M": {
            "type": "object",
            "required": [
              "E_ad",
              "E_reg_rel",
              "E_mol_rel",
              "E_int"
            ]
          },
          "step_Dr": {
            "type": "object",
            "required": [
              "E_ad",
              "E_reg_rel",
              "E_mol_rel",
              "E_int"
            ]
          },
          "step_Dl": {
            "type": "object",
            "required": [
              "E_ad",
              "E_reg_rel",
              "E_mol_rel",
              "E_int"
            ]
          }
        }
      },
      "description": "Total adsorption energies and components (in eV) for LiF monomer, rhombic dimer, and linear dimer on the relaxed CaF₂(111) terrace and at the relaxed [10-1] type I step."
    }
  ],
  "notes": "All energies must be in electronvolts (eV). The free-molecule reference energies are required to compute E_mol_rel; the relaxation of the pure surface and step provides the starting configurations. The check compares each E_ad to a reference value with tolerance and verifies relative ordering and consistency with an experimental monomer step value."
}
```

## How you are scored
A hidden verifier evaluates your `adsorption_energies.json` output. It compares your reported E_ad values to reference values (per-case tolerance) and checks that the relative ordering of adsorption strengths follows the expected physical trend (monomer vs dimers, step vs terrace). The monomer step adsorption energy is also compared to a known experimental value. Each check contributes a weighted score, and the final reward is a number between 0 and 1 combining all checks. The verifier runs without network access; the ground truth is embedded in the hidden test suite.
