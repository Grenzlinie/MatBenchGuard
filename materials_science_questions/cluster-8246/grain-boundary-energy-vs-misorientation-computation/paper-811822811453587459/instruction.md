# Dopant Segregation at Σ=5 Tilt Grain Boundary in Germanium

## Problem background
Polycrystalline semiconductors often exhibit nonuniform dopant distributions because dopants can segregate to grain boundaries. The driving mechanisms behind this segregation—whether due to elastic relaxation, electronic effects, or both—are crucial for understanding device performance, but isolating them experimentally is difficult. This work focuses on the Σ=5 tilt (310) grain boundary in germanium, which preserves the bulk tetrahedral bonding network and lacks dangling bonds, making it an ideal platform to disentangle lattice and electronic contributions. The key question is: what drives dopant segregation at such boundaries? Using ab initio density functional theory (DFT), it is possible to compute the segregation energies of arsenic and gallium dopants and separate the roles of lattice relaxation and electronic mixing.

## Approach
The approach uses plane-wave DFT with pseudopotentials to model a 68-atom supercell containing the grain boundary. The boundary is constructed from bulk Ge, relaxed, and analyzed to identify interface electronic states. Substitutional dopants (neutral As, As⁺, and Ga) are then placed at three distinct sites: a grain-center site representative of the bulk, an intermediate site, and a boundary site. For each combination, two sets of total energies are computed: one with all atoms fixed at the undoped relaxed positions (fixed-ion) and one allowing relaxation of the dopant and its neighboring atoms. The total energies from these calculations provide the ingredients to derive:
- Segregation (binding) energies relative to the bulk-like site.
- Relaxation energy contributions at each site.
- The shift in ionization energy for As when moving from bulk to the boundary.
- The energy of the intrinsic interface electron band and the isolated donor binding energy of As in bulk Ge.
These quantities are computed and reported in a single JSON file. By comparing the site-dependent energies, one can assess the relative importance of elastic and electronic effects.

## Reproduction target
Compute the following quantities (all in meV) from the DFT workflow and write them to `/app/outputs/segregation_energies.json`:
- The segregation energy of neutral arsenic (As) at the boundary relative to the bulk-like site.
- The segregation energy of ionized arsenic (As⁺) under the same conditions.
- The segregation energy of gallium (Ga).
- The relaxation energy for As at the boundary site and at the bulk-like site.
- The relaxation energies for As⁺ and Ga at the boundary site.
- The increase in ionization potential for As when moving from bulk to the boundary (computed from total energy differences of neutral and charged As with fixed atoms).
- The interface electron band energy (position of the lowest empty band relative to the conduction band edge) from the undoped relaxed boundary.
- The isolated donor binding energy of As in bulk Ge (donor state energy relative to the conduction band edge) from the grain-center site.

These results capture the main computable predictions of the study and allow assessment of the segregation trends and the driving mechanisms.

## Assets

- Quantum ESPRESSO (or equivalent open-source plane-wave DFT code): https://www.quantum-espresso.org
- PBE pseudopotentials for Ge, As, Ga (e.g., SSSP library): https://www.materialscloud.org/discover/sssp/table
- Atomsk (or equivalent grain boundary construction tool): https://atomsk.univ-lille.fr

## Workflow steps

### Step 1: Build undoped Σ=5 (310) supercell
- Role: process
- Action: Construct the Σ=5 (310) tilt grain boundary supercell for germanium with 68 atoms (dimensions 5.65 Å × 8.94 Å in the boundary plane, 30.4 Å perpendicular). Start from the bulk diamond structure, place two grains with the experimentally determined relative translation state, and create the idealized atomic coordinates. Generate the DFT input file for the subsequent relaxation.
- Evidence: `/app/outputs/supercell.in`

### Step 2: Relax undoped GB and compute electronic structure
- Role: process
- Action: Using the DFT tool with a Ge pseudopotential, relax the atomic coordinates of the undoped grain boundary supercell while keeping cell dimensions fixed. After relaxation, perform a self-consistent field (SCF) calculation and a band structure analysis to identify the interface electron state energy relative to the conduction band edge. Save the relaxed coordinates and total energy output.
- Evidence: `/app/outputs/relaxed_gb.out`

### Step 3: DFT total-energy calculations for doped GB configurations
- Role: process
- Action: For each dopant (neutral As, As+, Ga) and each substitutional site defined in the study (bk – grain center, i – intermediate, gb – boundary), perform two DFT total-energy calculations using the same pseudopotential and parameters: (a) fixed-ion energy with all atoms at the undoped relaxed coordinates; (b) relaxed energy where the dopant and surrounding atoms up to third-nearest neighbors are allowed to relax. For As+, remove one electron and use a uniform compensating background charge. Also compute the bulk reference by treating the grain-center site 'bk' as bulk-like. Save all total energies and relaxed coordinates.
- Evidence: `/app/outputs/doped_calculations.log`

### Step 4: Derive and report segregation energies and related quantities
- Role: scored (load-bearing)
- Action: From the total energies obtained in Steps 2 and 3, compute the following quantities and write them to the output JSON: segregation (binding) energy of neutral As to the boundary (E(gb, relaxed, As) - E(bk, relaxed, As), in meV); segregation energy of ionized As+ (gb vs bk, relaxed); segregation energy of Ga (gb vs bk, relaxed); relaxation energy for As at site 'gb' (fixed-ion minus relaxed) and at site 'bk'; relaxation energy for As+ and Ga at site 'gb'; ionization potential increase for As on the boundary (difference in (E(neutral) - E(ionized)) with fixed atoms between boundary and bulk-like sites); interface electron band energy (lowest empty band relative to conduction band edge from undoped calculation); isolated hydrogenic binding energy of As in bulk Ge (donor state energy relative to conduction band for As at the grain-center site).
- Output file: `/app/outputs/segregation_energies.json`
- Format: json
- Contract: {"as_segregation_energy_meV": float, "asplus_segregation_energy_meV": float, "ga_segregation_energy_meV": float, "as_relaxation_energy_gb_meV": float, "as_relaxation_energy_bk_meV": float, "asplus_relaxation_energy_gb_meV": float, "ga_relaxation_energy_gb_meV": float, "as_ionization_increase_meV": float, "bulk_as_binding_energy_meV": float, "interface_band_energy_meV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/segregation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### segregation_energies.json
- path: `/app/outputs/segregation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: All key quantitative results: segregation energies for neutral As, ionized As+, and Ga; relaxation energy components; ionization potential increase for As on boundary; bulk donor binding energy; interface electron band energy. All values in meV.
- schema:
  - `type`: object
  - `required`: `as_segregation_energy_meV`, `asplus_segregation_energy_meV`, `ga_segregation_energy_meV`, `as_relaxation_energy_gb_meV`, `as_relaxation_energy_bk_meV`, `asplus_relaxation_energy_gb_meV`, `ga_relaxation_energy_gb_meV`, `as_ionization_increase_meV`, `bulk_as_binding_energy_meV`, `interface_band_energy_meV`
  - `properties`:
    - `as_segregation_energy_meV`:
      - `type`: number
      - `units`: meV
    - `asplus_segregation_energy_meV`:
      - `type`: number
      - `units`: meV
    - `ga_segregation_energy_meV`:
      - `type`: number
      - `units`: meV
    - `as_relaxation_energy_gb_meV`:
      - `type`: number
      - `units`: meV
    - `as_relaxation_energy_bk_meV`:
      - `type`: number
      - `units`: meV
    - `asplus_relaxation_energy_gb_meV`:
      - `type`: number
      - `units`: meV
    - `ga_relaxation_energy_gb_meV`:
      - `type`: number
      - `units`: meV
    - `as_ionization_increase_meV`:
      - `type`: number
      - `units`: meV
    - `bulk_as_binding_energy_meV`:
      - `type`: number
      - `units`: meV
    - `interface_band_energy_meV`:
      - `type`: number
      - `units`: meV

Notes: The agent must run all DFT calculations and derive these quantities from total energies. The hidden gold values come from the paper's reported results (~0.1 eV As binding, ~0.03 eV As+, ~0 meV Ga, ~13 meV bulk binding, ~80 meV ionization shift, ~10 meV interface band). Tolerances accommodate pseudopotential differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "segregation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "as_segregation_energy_meV",
          "asplus_segregation_energy_meV",
          "ga_segregation_energy_meV",
          "as_relaxation_energy_gb_meV",
          "as_relaxation_energy_bk_meV",
          "asplus_relaxation_energy_gb_meV",
          "ga_relaxation_energy_gb_meV",
          "as_ionization_increase_meV",
          "bulk_as_binding_energy_meV",
          "interface_band_energy_meV"
        ],
        "properties": {
          "as_segregation_energy_meV": {
            "type": "number",
            "units": "meV"
          },
          "asplus_segregation_energy_meV": {
            "type": "number",
            "units": "meV"
          },
          "ga_segregation_energy_meV": {
            "type": "number",
            "units": "meV"
          },
          "as_relaxation_energy_gb_meV": {
            "type": "number",
            "units": "meV"
          },
          "as_relaxation_energy_bk_meV": {
            "type": "number",
            "units": "meV"
          },
          "asplus_relaxation_energy_gb_meV": {
            "type": "number",
            "units": "meV"
          },
          "ga_relaxation_energy_gb_meV": {
            "type": "number",
            "units": "meV"
          },
          "as_ionization_increase_meV": {
            "type": "number",
            "units": "meV"
          },
          "bulk_as_binding_energy_meV": {
            "type": "number",
            "units": "meV"
          },
          "interface_band_energy_meV": {
            "type": "number",
            "units": "meV"
          }
        }
      },
      "description": "All key quantitative results: segregation energies for neutral As, ionized As+, and Ga; relaxation energy components; ionization potential increase for As on boundary; bulk donor binding energy; interface electron band energy. All values in meV."
    }
  ],
  "notes": "The agent must run all DFT calculations and derive these quantities from total energies. The hidden gold values come from the paper's reported results (~0.1 eV As binding, ~0.03 eV As+, ~0 meV Ga, ~13 meV bulk binding, ~80 meV ionization shift, ~10 meV interface band). Tolerances accommodate pseudopotential differences."
}
```

## How you are scored
A hidden verifier will compare the values in your submitted `segregation_energies.json` against a set of reference results derived from the original study. The comparison uses appropriate tolerances that accommodate differences in pseudopotentials and DFT implementations while still testing the correct physical trends and magnitudes. Your final reward is a weighted combination of scores for each field: segregation energies, relaxation energies, ionization shift, interface band energy, and bulk binding energy. Simply providing numbers that happen to match is not sufficient— the workflow must be executed and the quantities must be computed from the DFT results. The verifier will also check that the output adheres to the specified JSON schema.
