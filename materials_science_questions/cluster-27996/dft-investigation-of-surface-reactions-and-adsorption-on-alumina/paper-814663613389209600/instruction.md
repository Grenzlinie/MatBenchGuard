# DFT Adsorption Energies on Cu and Cu₄/γ-Al₂O₃ Surfaces

## Problem background
Glycerol hydrogenolysis to 1,2-propanediol is a promising route for upgrading bio-derived glycerol. Cu-based catalysts supported on γ-Al<sub>2</sub>O<sub>3</sub> exhibit high activity and selectivity, and experiments suggest that the acidic Al sites on the alumina support and their partial hydroxylation play a crucial role. However, the atomic-scale understanding of how the support and its hydroxylation affect the adsorption of key intermediates (glycerol and acetol) and the initial O–H bond cleavage step is still lacking. This task addresses that gap by using density functional theory (DFT) to compute the binding energies and activation barriers on model Cu surfaces and supported Cu<sub>4</sub> clusters on γ-Al<sub>2</sub>O<sub>3</sub> under different hydroxylation conditions.

## Approach
Plane-wave DFT calculations using the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and projector augmented wave (PAW) pseudopotentials are employed. Surface models are constructed for Cu(111), Cu(100), and for a tetrahedral Cu<sub>4</sub> cluster adsorbed on the (110) surface of γ-Al<sub>2</sub>O<sub>3</sub>. Two states of the alumina surface are considered: a clean (non-hydroxylated) surface and a partially hydroxylated surface obtained by dissociatively adsorbing 4 H<sub>2</sub>O molecules (equivalent to 5.9 OH nm<sup>-2</sup>). For each model, the most stable adsorption configurations of glycerol and acetol at both Cu and Al sites are located by geometry relaxation. For glycerol, transition states for the initial O–H bond cleavage (for both the terminal and central hydroxyl groups) are identified using nudged elastic band and dimer methods. The raw total energies of all relevant systems (isolated molecules, bare surfaces, adsorbate complexes, and transition states) are computed and saved, from which binding energies and activation barriers can be independently recomputed.

## Reproduction target
Produce a JSON file containing the raw total energies (in eV) for the following systems:
- Gas-phase glycerol and acetol molecules.
- Clean Cu(111) and Cu(100) slabs.
- Non-hydroxylated Cu<sub>4</sub>/γ-Al<sub>2</sub>O<sub>3</sub>(110) surface.
- Hydroxylated Cu<sub>4</sub>/γ-Al<sub>2</sub>O<sub>3</sub>(110) surface.
- For each combination of surface, adsorbate (glycerol, acetol), and adsorption site (Cu, Al), the total energy of the adsorbate-surface complex (or, for the case of glycerol on the non‑hydroxylated Al site, a note indicating spontaneous dissociation).
- For glycerol on Cu(111), Cu(100), and the hydroxylated Cu<sub>4</sub>/γ-Al<sub>2</sub>O<sub>3</sub>(110) model (both Cu and Al sites), the total energies of the initial state and the transition state for O–H bond cleavage (for both the terminated and central O–H groups).
The file format is described in the output contract. From these raw energies, binding energies (BE = E_complex − E_surface − E_adsorbate_gas) and activation barriers (E_TS − E_initial) can be computed.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- γ-Al2O3 bulk structure (from Digne et al., J. Catal. 2004): 10.1016/S0021-9517(04)00299-4
- Bulk copper FCC structure

## Workflow steps

### Step 1: Bulk Cu lattice constant optimization
- Role: process
- Action: Optimize the lattice constant of bulk fcc Cu using plane-wave DFT to obtain the equilibrium Cu lattice constant for constructing Cu(111) and Cu(100) slabs.
- Evidence: `/app/outputs/cu_lattice_constant.txt`

### Step 2: Optimize gas-phase glycerol and acetol molecules
- Role: process
- Action: Perform DFT geometry optimization of isolated glycerol and acetol molecules in a sufficiently large vacuum cell to obtain their total energies.
- Evidence: `/app/outputs/gas_phase_energies.json`

### Step 3: Build and relax bare Cu(111) and Cu(100) slabs
- Role: process
- Action: Construct Cu(111) (4×4, 4 layers) and Cu(100) (3×3, 4 layers) slab models using the optimized lattice constant, fix the bottom two layers, and relax the top two layers with DFT to obtain bare surface total energies.
- Evidence: `/app/outputs/cu_slabs_energies.json`

### Step 4: Build and relax non-hydroxylated Cu₄/γ-Al₂O₃(110) model
- Role: process
- Action: Construct the γ-Al₂O₃(110) slab (24 Al2O3 units) from the Digne et al. bulk structure, place a tetrahedral Cu₄ cluster on the surface, fix bottom atomic layers, and relax with DFT to obtain the total energy of the dry supported catalyst model.
- Evidence: `/app/outputs/nonhydrox_surface_energy.json`

### Step 5: Build and relax hydroxylated Cu₄/γ-Al₂O₃(110) model
- Role: process
- Action: Add 4 water molecules (dissociatively adsorbed as OH groups, corresponding to 5.9 OH nm⁻²) near the Cu cluster on the relaxed non-hydroxylated model and relax the hydroxylated surface with DFT to obtain the total energy.
- Evidence: `/app/outputs/hydrox_surface_energy.json`

### Step 6: Compute adsorption energies and O–H cleavage barriers for glycerol and acetol
- Role: scored (load-bearing)
- Action: For each surface model (Cu(111), Cu(100), non-hydroxylated Cu₄/γ-Al₂O₃(110), hydroxylated Cu₄/γ-Al₂O₃(110)), determine the most stable adsorption configurations of glycerol and acetol at Cu and Al sites using DFT geometry optimizations. For glycerol on Cu(111), Cu(100), and the hydroxylated model (both Cu and Al sites), locate transition states for the initial O–H bond cleavage (terminated and central O–H groups where applicable) using nudged elastic band and dimer methods. Record the raw total energies (in eV) of the bare surface, isolated gas-phase adsorbate, the adsorbed complex, and (for barriers) the initial state and transition state for each system.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with a 'systems' array. Each element is an object with keys: 'id' (string, must be exactly one of the required system identifiers listed below), 'E_surface' (float, eV), 'E_adsorbate_gas' (float or null), 'E_complex' (float or null), 'E_initial' (float or null), 'E_TS' (float or null), and optionally 'note' (string). For adsorption systems without TS searches, E_initial and E_TS should be null. If a stable molecular adsorption complex cannot be found for glycerol on the non-hydroxylated Al site (glycerol_nonhydrox_Al_site), then E_complex should be omitted and a note provided describing the outcome. The required system identifiers are: glycerol_Cu111_BE, acetol_Cu111_BE, glycerol_Cu100_BE, acetol_Cu100_BE, glycerol_nonhydrox_Cu_site_BE, glycerol_nonhydrox_Al_site, acetol_nonhydrox_Cu_site_BE, acetol_nonhydrox_Al_site_BE, glycerol_hydrox_Cu_site_BE, glycerol_hydrox_Al_site_BE, acetol_hydrox_Cu_site_BE, acetol_hydrox_Al_site_BE, barrier_Cu111_terminated_OH, barrier_Cu111_central_OH, barrier_Cu100_terminated_OH, barrier_Cu100_central_OH, barrier_hydrox_Al_site, barrier_hydrox_Cu_site_terminated, barrier_hydrox_Cu_site_central.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw total energies for recomputation of binding energies and activation barriers. System ids must exactly match the prescribed identifiers.
- schema:
  - `type`: object
  - `required`: `systems`
  - `properties`:
    - `systems`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `id`, `E_surface`, `E_adsorbate_gas`, `E_complex`, `E_initial`, `E_TS`
        - `properties`:
          - `id`:
            - `type`: string
            - `enum`: `glycerol_Cu111_BE`, `acetol_Cu111_BE`, `glycerol_Cu100_BE`, `acetol_Cu100_BE`, `glycerol_nonhydrox_Cu_site_BE`, `glycerol_nonhydrox_Al_site`, `acetol_nonhydrox_Cu_site_BE`, `acetol_nonhydrox_Al_site_BE`, `glycerol_hydrox_Cu_site_BE`, `glycerol_hydrox_Al_site_BE`, `acetol_hydrox_Cu_site_BE`, `acetol_hydrox_Al_site_BE`, `barrier_Cu111_terminated_OH`, `barrier_Cu111_central_OH`, `barrier_Cu100_terminated_OH`, `barrier_Cu100_central_OH`, `barrier_hydrox_Al_site`, `barrier_hydrox_Cu_site_terminated`, `barrier_hydrox_Cu_site_central`
          - `E_surface`:
            - `type`: number
            - `description`: in eV
          - `E_adsorbate_gas`:
            - `type`: `number`, `null`
          - `E_complex`:
            - `type`: `number`, `null`
          - `E_initial`:
            - `type`: `number`, `null`
          - `E_TS`:
            - `type`: `number`, `null`
          - `note`:
            - `type`: string

Notes: The checker will recompute binding energies (BE = E_complex - E_surface - E_adsorbate_gas) and activation barriers (E_TS - E_initial) from the provided raw energies and compare to hidden gold values. If no stable molecular adsorption complex is found for glycerol on the non-hydroxylated Al site (glycerol_nonhydrox_Al_site), a note should be provided instead of E_complex.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "systems"
        ],
        "properties": {
          "systems": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "id",
                "E_surface",
                "E_adsorbate_gas",
                "E_complex",
                "E_initial",
                "E_TS"
              ],
              "properties": {
                "id": {
                  "type": "string",
                  "enum": [
                    "glycerol_Cu111_BE",
                    "acetol_Cu111_BE",
                    "glycerol_Cu100_BE",
                    "acetol_Cu100_BE",
                    "glycerol_nonhydrox_Cu_site_BE",
                    "glycerol_nonhydrox_Al_site",
                    "acetol_nonhydrox_Cu_site_BE",
                    "acetol_nonhydrox_Al_site_BE",
                    "glycerol_hydrox_Cu_site_BE",
                    "glycerol_hydrox_Al_site_BE",
                    "acetol_hydrox_Cu_site_BE",
                    "acetol_hydrox_Al_site_BE",
                    "barrier_Cu111_terminated_OH",
                    "barrier_Cu111_central_OH",
                    "barrier_Cu100_terminated_OH",
                    "barrier_Cu100_central_OH",
                    "barrier_hydrox_Al_site",
                    "barrier_hydrox_Cu_site_terminated",
                    "barrier_hydrox_Cu_site_central"
                  ]
                },
                "E_surface": {
                  "type": "number",
                  "description": "in eV"
                },
                "E_adsorbate_gas": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "E_complex": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "E_initial": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "E_TS": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "note": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "description": "Raw total energies for recomputation of binding energies and activation barriers. System ids must exactly match the prescribed identifiers."
    }
  ],
  "notes": "The checker will recompute binding energies (BE = E_complex - E_surface - E_adsorbate_gas) and activation barriers (E_TS - E_initial) from the provided raw energies and compare to hidden gold values. If no stable molecular adsorption complex is found for glycerol on the non-hydroxylated Al site (glycerol_nonhydrox_Al_site), a note should be provided instead of E_complex."
}
```

## How you are scored
A hidden verifier reads the results.json file you produce and recomputes binding energies and activation barriers from the raw total energies. The recomputed values are compared against reference values (the expected gold) using tolerances that account for legitimate variations due to different DFT implementations, pseudopotential parameters, and convergence settings. Additionally, the verifier checks structural trends: for example, the relative strength of adsorption at Al vs. Cu sites, and the effect of hydroxylation on binding energies and barriers. Your score is determined by how well the recomputed quantities and trends match the expected ones. Reporting the final numbers without the underlying DFT workflow will not satisfy the verification step because the checker recomputes from the raw energies you supply; therefore, correct raw total energies are essential.
