# DFT Adsorption of O2 and CO on α-Mo2C(0001)

## Problem background
α-Mo₂C is a transition metal carbide with catalytic properties resembling noble metals. The surface reactivity of α-Mo₂C(0001) depends critically on how oxygen and carbon monoxide adsorb, activate, and modify the surface. Understanding the atomic-scale adsorption configuration, energy, and geometry for O₂ and CO on both Mo‑terminated and C‑terminated surfaces is essential for interpreting catalytic activity and guiding surface engineering. This task asks you to compute the most stable dissociative adsorption arrangements, the associated adsorption energies, and key bond distances for these molecules on both terminations, thereby revealing the surface's preferential binding sites and lateral interaction effects.

## Approach
We use plane‑wave density functional theory (DFT) within the generalized gradient approximation (GGA) to model the α‑Mo₂C(0001) surface as stoichiometric six‑layer slabs with vacuum. The computational protocol consists of (i) bulk lattice optimization with the PBE functional, (ii) construction and relaxation of clean Mo‑terminated and C‑terminated surfaces, (iii) geometry optimization of adsorbate‑covered slabs for both dissociated O₂ (two O atoms on the surface) and molecular CO at the most stable hollow sites, as well as for a single O atom at lower coverage to gauge lateral interactions, and (iv) single‑point energy calculations with the RPBE functional on the PBE‑optimized geometries. Gas‑phase reference energies of O₂ and CO serve as the zero‑energy standard. Adsorption energies are computed as E_ads = E(slab+adsorbate) − [E(clean_slab) + E(gas_ref)] using the reference molecule (O₂ for the O₂‑dissociation case, half O₂ for atomic O, and CO for CO). The key structural parameters (Mo–O, O–O, C–O, Mo–C, C–C distances) are extracted from the optimized coordinates.

## Reproduction target
Compute the PBE and RPBE adsorption energies (in eV) and the important interatomic distances (in Å) for:
- O₂ dissociated on the Mo‑terminated surface at the most stable configuration (two O atoms above the V_C hollow sites);
- O₂ dissociated on the C‑terminated surface at the most stable configuration (two O atoms above the H_C hollow sites);
- CO molecularly adsorbed on the Mo‑terminated surface at the most stable configuration (tilted μ³‑form over the V_C site);
- CO molecularly adsorbed on the C‑terminated surface at the most stable configuration (atop surface carbon, ketenylidene‑like);
- atomic O on the Mo‑terminated surface at the most stable V_C hollow site (1/4 ML coverage);
- atomic O on the C‑terminated surface at the most stable H_C hollow site (1/4 ML coverage).
Report all results in a single JSON file `adsorption_energies.json` according to the output contract. The contract defines the exact keys and data types to provide.

## Assets

- α-Mo2C orthorhombic crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Bulk lattice optimization of α-Mo2C
- Role: process
- Action: Perform a variable‑cell relaxation of the bulk α‑Mo₂C orthorhombic unit cell using the PBE functional and converged k‑point sampling. Start from the experimental crystal structure with lattice parameters a=4.729 Å, b=6.028 Å, c=5.197 Å; atomic positions as in known α‑Mo₂C (Mo in slightly distorted hcp, C in octahedral sites). Converge forces and stresses.
- Evidence: `/app/outputs/bulk_opt.out`

### Step 2: Surface slab construction and relaxation
- Role: process
- Action: Build stoichiometric six‑layer slabs for both Mo‑terminated and C‑terminated α‑Mo₂C(0001)-(1×1) surfaces using the optimized bulk lattice. Set a vacuum gap of 10.29 Å between repeated slabs. For each termination, relax the atomic positions of the top four layers (2Mo+2C or 2C+2Mo) while keeping the bottom two layers fixed. Use the PBE functional, spin‑restricted, and a converged plane‑wave cutoff and k‑point mesh.
- Evidence: `/app/outputs/surface_relax.out`

### Step 3: Gas‑phase reference energies
- Role: process
- Action: Compute the total energies of an isolated triplet O₂ molecule and an isolated CO molecule in a large cubic box, using the same PBE functional, cutoffs, and pseudopotentials as for the slab calculations. For O₂ use spin‑unrestricted.
- Evidence: `/app/outputs/gas_ref_energies.txt`

### Step 4: Geometry optimization of O2 dissociated on Mo‑terminated (config 1)
- Role: process
- Action: Set up the Mo‑terminated slab with two O atoms placed above the V_C hollow sites (V_C/V_C arrangement). Optimize the geometry of the full system (adsorbed O atoms and relaxed slab layers) using the PBE functional; keep the bottom two slab layers fixed. Converge forces to a low threshold.
- Evidence: `/app/outputs/o2_moterm_opt.out`

### Step 5: Geometry optimization of O2 dissociated on C‑terminated (config 8)
- Role: process
- Action: Optimize the C‑terminated slab with two O atoms adsorbed at the H_C hollow sites (H_C/H_C arrangement), same convergence criteria.
- Evidence: `/app/outputs/o2_cterm_opt.out`

### Step 6: Geometry optimization of CO on Mo‑terminated (config 17)
- Role: process
- Action: Optimize the Mo‑terminated slab with one CO molecule placed over the V_C site in the tilted μ³‑form.
- Evidence: `/app/outputs/co_moterm_opt.out`

### Step 7: Geometry optimization of CO on C‑terminated (config 21)
- Role: process
- Action: Optimize the C‑terminated slab with one CO molecule adsorbed atop the surface carbon atom, forming a ketenylidene‑like species.
- Evidence: `/app/outputs/co_cterm_opt.out`

### Step 8: Geometry optimization of atomic O on Mo‑terminated (config 12)
- Role: process
- Action: Optimize a single O atom adsorbed on the Mo‑terminated slab at the V_C hollow site (coverage 1/4 ML).
- Evidence: `/app/outputs/o_atom_moterm_opt.out`

### Step 9: Geometry optimization of atomic O on C‑terminated (config 15)
- Role: process
- Action: Optimize a single O atom adsorbed on the C‑terminated slab at the H_C hollow site.
- Evidence: `/app/outputs/o_atom_cterm_opt.out`

### Step 10: RPBE single‑point energy calculations
- Role: process
- Action: For each optimized slab+adsorbate configuration (steps 4‑9) and for the clean slabs (step 2) and the gas‑phase molecules (step 3), perform a single‑point energy calculation using the RPBE functional (PBE‑optimized geometries) with the same cutoff, pseudopotentials, and k‑point grid as before. Record the total energies.
- Evidence: `/app/outputs/rpbe_total_energies.txt`

### Step 11: Compute adsorption energies and distances, assemble JSON
- Role: scored (load-bearing)
- Action: Using the PBE and RPBE total energies from the prior steps, compute the adsorption energies E_ads = E(slab+adsorbate) − [E(clean_slab) + E(gas_ref)] for each configuration. Note: for O2 cases the reference is O₂; for atomic O the reference is ½ O₂; for CO it is CO. Extract the key interatomic distances (Mo–O, O–O, C–O, Mo–C, C–C) from the optimized geometry output files. Write all results to a single JSON file `adsorption_energies.json` following the output contract.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: Top‑level keys: O2_Mo_term, O2_C_term, CO_Mo_term, CO_C_term, O_atom_Mo_term, O_atom_C_term. Each value is an object with keys: configuration_id (string), PBE_Eads (float, eV), RPBE_Eads (float, eV), Mo_O_distances (list of floats, Å). Additionally, O2_Mo_term and O2_C_term contain O_O_distance (float, Å); CO_Mo_term contains C_O_distance (float, Å), Mo_C_distance (float, Å); CO_C_term contains C_O_distance (float, Å), C_C_distance (float, Å); O_atom_Mo_term and O_atom_C_term contain only Mo_O_distances.
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
- target_policy: exact_match
- description: Adsorption energies and structural parameters for the most stable configurations of O2, CO, and atomic O on both terminations of α‑Mo₂C(0001).
- schema:
  - `type`: object
  - `required`:
    - `O2_Mo_term`: object
    - `O2_C_term`: object
    - `CO_Mo_term`: object
    - `CO_C_term`: object
    - `O_atom_Mo_term`: object
    - `O_atom_C_term`: object
  - `items`:
    - `configuration_id`: string
    - `PBE_Eads`: float (eV)
    - `RPBE_Eads`: float (eV)
    - `Mo_O_distances`: array of float (Å)
    - `O_O_distance`: float (Å)
    - `C_O_distance`: float (Å)
    - `Mo_C_distance`: float (Å)
    - `C_C_distance`: float (Å)
  - `required_columns`:
  - `units`: object

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "O2_Mo_term": "object",
          "O2_C_term": "object",
          "CO_Mo_term": "object",
          "CO_C_term": "object",
          "O_atom_Mo_term": "object",
          "O_atom_C_term": "object"
        },
        "items": {
          "configuration_id": "string",
          "PBE_Eads": "float (eV)",
          "RPBE_Eads": "float (eV)",
          "Mo_O_distances": "array of float (Å)",
          "O_O_distance": "float (Å)",
          "C_O_distance": "float (Å)",
          "Mo_C_distance": "float (Å)",
          "C_C_distance": "float (Å)"
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Adsorption energies and structural parameters for the most stable configurations of O2, CO, and atomic O on both terminations of α‑Mo₂C(0001)."
    }
  ],
  "notes": ""
}
```

## How you are scored
The hidden verifier will read your `adsorption_energies.json` and compare each reported adsorption energy and every specified interatomic distance against its own reference values. Credit is awarded based on how closely your computed energies and distances match the references, with appropriate tolerances to account for the inherent variability between different DFT implementations. The final reward is a weighted sum over all configuration entries and fields; more weight is assigned to the adsorption energies and geometries of the primary O₂ and CO adsorption configurations. To receive full credit you must have correctly identified the most stable adsorption configuration for each case and report values that fall within the expected numerical range. Simply listing the reference numbers is not sufficient — your geometry optimizations and total‑energy calculations must collectively support the reported quantities.
