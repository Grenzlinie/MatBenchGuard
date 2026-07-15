# Computational Study of Water and Methanoic Acid Adsorption on Calcite and Fluorite Surfaces

## Problem background
Flotation is a widely used mineral separation process that relies on the selective adsorption of collector (surfactant) molecules to render the desired mineral hydrophobic. Understanding the competitive adsorption of water and collector molecules at mineral surfaces is critical for designing efficient flotation schemes. This task investigates the atomistic interactions of water and a model collector – methanoic acid – with the surfaces of two important minerals, calcite ($CaCO_3$) and fluorite ($CaF_2$). The goal is to compute the surface energies and adsorption energies for both adsorbates on several crystal planes, in order to assess whether methanoic acid adsorbs preferentially to one mineral over the other and under what conditions it can displace pre‑adsorbed water.

## Approach
The calculations use classical static energy minimisation based on the Born model of solids. Ions interact via long‑range Coulombic forces and short‑range repulsion/dispersion terms. Electronic polarisability is included for oxygen and fluorine via a core‑shell model. Molecular degrees of freedom (bond stretches, angle bends) are described by the cvff force field for methanoic acid and by a dedicated flexible water model.

Simulations are performed with the open‑source LAMMPS code. For each mineral, the bulk crystal unit cell is first relaxed to obtain a reference bulk energy $U_b$. Surface slabs are then created by cleaving the relaxed bulk along the targeted planes: calcite {10‑14} and fluorite {011}, {111}, {310}. Each slab is split into a Region I (upper layers, free to relax) and a Region II (lower layers, fixed at bulk positions). The slab energy $U_s$ is obtained via energy minimisation, giving the unhydrated surface energy $\gamma = (U_s - U_b)/A$ where $A$ is the surface area.

Adsorbate molecules (water or methanoic acid) are subsequently placed on the surface slabs at the coverages described in the workflow. The system is again minimised, and the adsorption energy is computed as
$U_{\text{ads}} = U_{\text{def}} - (U_s + U_{\text{mol}})$,
where $U_{\text{def}}$ is the energy of the covered slab and $U_{\text{mol}}$ is the energy of a single isolated molecule. 

Interatomic potentials used:
‑ Calcite: Pavese et al. (1996) force field.
‑ Fluorite: Catlow et al. (1977) force field.
‑ Water–mineral interactions: parameters from de Leeuw & Parker (1998).
‑ Methanoic acid: cvff force field, with cross‑interactions scaled according to the partial charges of the mineral atoms.

The workflow proceeds from bulk optimisation, through bare surface relaxation and pure surface energy calculation, to the evaluation of hydrated surfaces and finally methanoic acid adsorption on each surface.

## Reproduction target
Produce two JSON output files containing all computed quantities:

1. `surface_energies.json` – for each surface (calcite {10‑14}, fluorite {011}, {111}, {310}), report the unhydrated and hydrated surface energies in J/m².
2. `adsorption_energies.json` – for the same surfaces, report the water and methanoic acid adsorption energies in kJ/mol (negative values indicate exothermic adsorption).

The values must be obtained by performing the static energy minimisations described in the workflow. The relative ordering of the adsorption energies (e.g., whether methanoic acid on fluorite is more exothermic than on calcite, and whether on a given surface water or acid binds more strongly) forms a critical part of the reproduction.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org
- Pavese et al. (1996) calcite potential: 10.1007/BF00153999
- Catlow et al. (1977) fluorite potential: 10.1088/0022-3719/10/13/009
- de Leeuw & Parker (1998) water potential: 10.1103/PhysRevB.58.13901
- cvff force field for methanoic acid: cvff as implemented in common MD packages (e.g., LAMMPS, GULP)
- Experimental crystal structures of calcite and fluorite: https://icsd.products.fiz-karlsruhe.de

## Workflow steps

### Step 1: Build and optimize bulk crystals
- Role: process
- Action: Construct bulk unit cells for calcite (R-3c) and fluorite (Fm-3m) using experimental lattice parameters. Assign the respective force field parameters (Pavese et al. for calcite, Catlow et al. for fluorite) and perform static energy minimization to obtain relaxed bulk structures and reference bulk energies.
- Evidence: `/app/outputs/bulk_crystals.log`

### Step 2: Create and relax surface slabs; compute pure surface energies
- Role: process
- Action: From the relaxed bulk structures, cleave slabs for calcite {10-14} and fluorite {011}, {111}, {310}. Define Region I (free to relax) and Region II (fixed). Perform energy minimization of each surface block to obtain U_s, then compute the unhydrated surface energy γ = (U_s - U_b)/A for each surface.
- Evidence: `/app/outputs/surface_slabs.log`

### Step 3: Calculate hydrated surface energies and water adsorption energies
- Role: scored
- Action: Place water molecules on each surface at the coverages described: full monolayer on calcite {10-14} and fluorite {011}, {310}; 50% coverage on fluorite {111}. Perform energy minimization and compute the hydrated surface energy and the water adsorption energy U_ads. Record all unhydrated and hydrated surface energies in surface_energies.json.
- Output file: `/app/outputs/surface_energies.json`
- Format: json
- Contract: {"calcite_104": {"unhydrated": <float>, "hydrated": <float>}, "fluorite_011": {...}, "fluorite_111": {...}, "fluorite_310": {...}}
- Scoring: scored by hidden verifier

### Step 4: Calculate methanoic acid adsorption energies
- Role: scored (load-bearing)
- Action: On each surface, place methanoic acid molecules at the coverages described (50% on calcite, full on fluorite {011} and {310}, 50% on {111}). Perform energy minimization and compute the methanoic acid adsorption energy U_ads. Compile all water and methanoic acid adsorption energies into adsorption_energies.json.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {"calcite_104": {"water": <float>, "methanoic_acid": <float>}, "fluorite_011": {...}, "fluorite_111": {...}, "fluorite_310": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energies.json`
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energies.json
- path: `/app/outputs/surface_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Provides unhydrated and hydrated surface energies for calcite and fluorite surfaces.
- schema:
  - `type`: object
  - `required_keys`: `calcite_104`, `fluorite_011`, `fluorite_111`, `fluorite_310`
  - `value_shape`:
    - `type`: object
    - `required_keys`: `unhydrated`, `hydrated`
    - `value_units`: J/m²

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Provides water and methanoic acid adsorption energies on each surface.
- schema:
  - `type`: object
  - `required_keys`: `calcite_104`, `fluorite_011`, `fluorite_111`, `fluorite_310`
  - `value_shape`:
    - `type`: object
    - `required_keys`: `water`, `methanoic_acid`
    - `value_units`: kJ/mol

Notes: Surface energies are in J/m² (float). Adsorption energies are in kJ/mol (float, negative for exothermic). The keys are: calcite_104, fluorite_011, fluorite_111, fluorite_310. The checker will compare these values to hidden paper-reported references with tolerances and verify the thermodynamic ordering among them.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "calcite_104",
          "fluorite_011",
          "fluorite_111",
          "fluorite_310"
        ],
        "value_shape": {
          "type": "object",
          "required_keys": [
            "unhydrated",
            "hydrated"
          ],
          "value_units": "J/m²"
        }
      },
      "description": "Provides unhydrated and hydrated surface energies for calcite and fluorite surfaces."
    },
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "calcite_104",
          "fluorite_011",
          "fluorite_111",
          "fluorite_310"
        ],
        "value_shape": {
          "type": "object",
          "required_keys": [
            "water",
            "methanoic_acid"
          ],
          "value_units": "kJ/mol"
        }
      },
      "description": "Provides water and methanoic acid adsorption energies on each surface."
    }
  ],
  "notes": "Surface energies are in J/m² (float). Adsorption energies are in kJ/mol (float, negative for exothermic). The keys are: calcite_104, fluorite_011, fluorite_111, fluorite_310. The checker will compare these values to hidden paper-reported references with tolerances and verify the thermodynamic ordering among them."
}
```

## How you are scored
A hidden verifier reads your `surface_energies.json` and `adsorption_energies.json` files. Each numerical entry (surface energies and adsorption energies) is compared against reference values that were obtained from the original study. Additionally, the verifier checks whether the relative ordering of the adsorption energies across surfaces and between adsorbates satisfies the thermodynamic conditions that underpin selective adsorption.

The final reward is a weighted combination of how many entries fall within acceptable agreement and how many of the required ordering relations are correctly reproduced. Simply reporting plausible numbers is not sufficient – they must result from the LAMMPS simulations as described in the workflow steps.
