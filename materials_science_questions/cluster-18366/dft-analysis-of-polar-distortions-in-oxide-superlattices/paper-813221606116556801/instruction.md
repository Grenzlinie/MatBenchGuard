# Reproduce SrTiO3 surface and thin film properties via SMTB-Q variable-charge model

## Problem background
Strontium titanate (SrTiO₃) is a model perovskite oxide widely used as a substrate for functional oxide heterostructures and in electronic devices. The structure, energetics, and charge distribution of its (001) surfaces, as well as the relaxation behaviour of strained thin films, are critical for interface engineering. Atomistic simulations that can accurately describe the mixed iono‑covalent bonding, charge equilibration, and large‑scale surface relaxation are needed to predict these properties. This work develops a second‑moment tight‑binding variable‑charge model (SMTB‑Q) that self‑consistently treats charges and bonding, aiming to obtain reliable predictions of bulk, surface, and thin‑film properties of SrTiO₃ without relying on first‑principles calculations for every configuration.

## Approach
The SMTB‑Q model expresses the cohesive energy as a sum of ionization, Coulomb, covalent, and repulsive terms, with equilibrium charges determined by a charge equilibration (QEq) scheme that includes a charge‑dependent covalent energy. The model parameters are separately determined for the binary oxides SrO and TiO₂. For the ternary SrTiO₃, the hopping parameters are rescaled using the oxygen coordination numbers and a charge‑preservation condition that keeps the product β√Z_O constant for each cation; all other short‑range and QEq parameters are inherited. The resulting “raw” SrTiO₃ parameters are then refined by adjusting a small number of quantities to match experimental reference values for the lattice constant, cohesive energy, and bulk modulus, yielding a “fitted” set. All subsequent simulations use the fitted parameters. Slab models of the SrTiO₃(001) surface with SrO and TiO₂ terminations are constructed, and sublattices are defined using generalized coordination numbers to assign initial charges via the inhomogeneous QEq equations. Metropolis Monte Carlo relaxation at low temperature produces surface formation energies, atomic displacements along [001], and charge transfers. For thin films, slabs of several nanometer thicknesses are strained in‑plane (compressive and tensile) and relaxed at 273 K, from which the out‑of‑plane lattice parameter and the in‑plane/out‑of‑plane ratio are extracted.

## Reproduction target
The goal is to compute the following quantities:
1. Bulk properties: equilibrium lattice parameters, cohesive energy, bulk modulus, elastic constants, and ionic charges for SrO (rock‑salt), TiO₂ (rutile), and for SrTiO₃ using both the raw transferred parameters and the fitted parameter set.
2. SrTiO₃(001) surface properties at low temperature: surface energies, atomic relaxations (displacements of labelled atoms along the surface normal), and charge transfers (difference from bulk charge) for both the SrO‑ and TiO₂‑terminated surfaces.
3. Strained thin‑film properties: out‑of‑plane lattice parameter (a_⊥) and the ratio a_⊥/a_∥ for film thicknesses of 2, 5, 10, 20, and 40 nm under in‑plane compressive strain of −1.66% and tensile strain of +1.66%, relaxed at 273 K.
All results must be written as the specified JSON artifacts in the output directory.

## Assets

- Python 3 interpreter: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement SMTB-Q model and compute binary oxide bulk properties
- Role: process
- Action: Implement the SMTB-Q cohesive energy expression (ionization, Coulomb, covalent, repulsive terms) and the QEq charge equilibration. Using the SrO and TiO2 parameters from the known model, compute equilibrium lattice parameters, cohesive energy, bulk modulus, elastic constants, and ionic charges for bulk SrO (rock-salt) and TiO2 (rutile).
- Evidence: `/app/outputs/binary_validation.json`

### Step 2: Derive raw SrTiO3 parameters and compute raw bulk properties
- Role: process
- Action: Rescale the hopping parameters β and ξ for SrTiO3 using the oxygen coordination numbers and the charge-preservation condition that β√Z_O is constant for each cation. Inherit remaining parameters from the binary oxides (with R_O set to 0.52 Å). Using these raw parameters, compute bulk lattice parameter, cohesive energy, bulk modulus, elastic constants, and ionic charges for cubic SrTiO3.
- Evidence: `/app/outputs/raw_sto_properties.json`

### Step 3: Adjust parameters and compute fitted SrTiO3 bulk properties
- Role: process
- Action: Starting from the raw parameters, adjust the five quantities ξ_Sr, A_Sr, ξ_Ti, A_Ti, and R_O to minimise deviations from experimental lattice parameter (3.903 Å), cohesive energy (−31.7 eV), and bulk modulus (183 GPa). After fitting, recompute the full set of bulk properties.
- Evidence: `/app/outputs/fitted_params.json`

### Step 4: Output bulk properties
- Role: scored
- Action: Collect the computed bulk properties for SrO, TiO2, raw SrTiO3, and fitted SrTiO3 into a single JSON file.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: JSON object with keys 'SrO', 'TiO2', 'SrTiO3_raw', 'SrTiO3_fitted'. Each value is an object containing: a (float, Å), c (float, Å, only present for TiO2), E_coh (float, eV), B (float, GPa), elastic constants C11, C12, C44, etc. (floats, GPa), Q (float, absolute oxygen charge), and ionic_charges (object with element symbols as keys and float values).
- Scoring: scored by hidden verifier

### Step 5: Build SrTiO3 (001) slab models and initialise charges
- Role: process
- Action: Construct slabs for both SrO- and TiO2-terminated (001) surfaces, using a sufficiently large supercell with periodic in-plane conditions. Define sublattices using generalised coordination numbers and solve the inhomogeneous QEq equations to assign initial charges. Fix deep bulk layers to their bulk positions and charges.
- Evidence: `/app/outputs/slab_initialisation.log`

### Step 6: Monte Carlo surface relaxation at low temperature and output surface properties
- Role: scored (load-bearing)
- Action: Perform Metropolis Monte Carlo relaxation at a temperature near 2 K for both terminations until convergence. Record the slab energy and a bulk reference to compute surface formation energies. Measure the displacements of key labelled atoms along the [001] direction and collect final charge transfers for surface atoms.
- Output file: `/app/outputs/surface_properties.json`
- Format: json
- Contract: JSON object with keys 'SrO_terminated' and 'TiO2_terminated'. Each value is an object containing: 'surface_energy' (float, J/m²), 'atomic_relaxations' (object mapping atom labels like 'Sr(9)', 'Ti(1)', 'O(3)' to displacement along [001] in Å, positive outward), 'charge_transfers' (object mapping same labels to change in elementary charge).
- Scoring: scored by hidden verifier

### Step 7: Simulate strained thin films at 273 K
- Role: process
- Action: For film thicknesses of 2, 5, 10, 20, and 40 nm, build slab models with both terminations. Apply in-plane compressive (−1.66%) and tensile (+1.66%) strain by fixing the in-plane lattice parameters. Perform Monte Carlo relaxation at 273 K. Extract the out-of-plane lattice parameter a_⊥, the in‑plane parameter a_∥, and the inter‑plane distances.
- Evidence: `/app/outputs/thin_film_trajectories.log`

### Step 8: Output thin film properties
- Role: scored (load-bearing)
- Action: Compile the out-of-plane lattice parameters and the ratio a_⊥/a_∥ for each strain and each thickness into a structured file.
- Output file: `/app/outputs/thin_film_properties.json`
- Format: json
- Contract: JSON object with keys for each strain value (e.g., '-1.66%', '+1.66%'). Each value is an array of objects with keys: 'thickness_nm' (float), 'a_perp' (float, Å), 'a_parallel' (float, Å), 'ratio' (float, a_perp/a_parallel). The array must be sorted by 'thickness_nm' in ascending order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/surface_properties.json`
- `/app/outputs/thin_film_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bulk properties of binary oxides and raw/fitted SrTiO3 computed with the SMTB-Q model.
- schema:
  - `type`: object
  - `required`: `SrO`, `TiO2`, `SrTiO3_raw`, `SrTiO3_fitted`
  - `items`: object
  - `description`: Each key maps to an object containing: a (float, Å), c (float, Å, only present for TiO2), E_coh (float, eV), B (float, GPa), elastic constants (C11, C12, C44, etc. as floats, GPa), Q (float, absolute oxygen charge), and ionic_charges (object with element keys and float values).

### surface_properties.json
- path: `/app/outputs/surface_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Surface energies, atomic relaxations, and charge transfers for SrTiO3 (001) surfaces at low temperature.
- schema:
  - `type`: object
  - `required`: `SrO_terminated`, `TiO2_terminated`
  - `items`: object
  - `description`: Each termination object contains: 'surface_energy' (float, J/m²), 'atomic_relaxations' (object mapping atom label to displacement in Å, positive outward), 'charge_transfers' (object mapping same labels to change in elementary charge).

### thin_film_properties.json
- path: `/app/outputs/thin_film_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Out-of-plane lattice parameters and ratios for strained SrTiO3 thin films of different thicknesses.
- schema:
  - `type`: object
  - `required`: `-1.66%`, `+1.66%`
  - `items`: object
  - `description`: Each strain key maps to an array of objects, each with: 'thickness_nm' (float), 'a_perp' (float, Å), 'a_parallel' (float, Å), 'ratio' (float).

Notes: All numerical comparisons will use appropriate tolerances for each quantity (e.g., ±0.02 Å for lattice parameters, ±0.05 J/m² for surface energies, ±0.02 Å for atomic displacements). The checker will also verify structural relations (TiO2-terminated surface energy lower than SrO-terminated, and a_perp decreasing/increasing with thickness for compressive/tensile strain).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "SrO",
          "TiO2",
          "SrTiO3_raw",
          "SrTiO3_fitted"
        ],
        "items": {},
        "description": "Each key maps to an object containing: a (float, Å), c (float, Å, only present for TiO2), E_coh (float, eV), B (float, GPa), elastic constants (C11, C12, C44, etc. as floats, GPa), Q (float, absolute oxygen charge), and ionic_charges (object with element keys and float values)."
      },
      "description": "Bulk properties of binary oxides and raw/fitted SrTiO3 computed with the SMTB-Q model."
    },
    {
      "file": "surface_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "SrO_terminated",
          "TiO2_terminated"
        ],
        "items": {},
        "description": "Each termination object contains: 'surface_energy' (float, J/m²), 'atomic_relaxations' (object mapping atom label to displacement in Å, positive outward), 'charge_transfers' (object mapping same labels to change in elementary charge)."
      },
      "description": "Surface energies, atomic relaxations, and charge transfers for SrTiO3 (001) surfaces at low temperature."
    },
    {
      "file": "thin_film_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "-1.66%",
          "+1.66%"
        ],
        "items": {},
        "description": "Each strain key maps to an array of objects, each with: 'thickness_nm' (float), 'a_perp' (float, Å), 'a_parallel' (float, Å), 'ratio' (float)."
      },
      "description": "Out-of-plane lattice parameters and ratios for strained SrTiO3 thin films of different thicknesses."
    }
  ],
  "notes": "All numerical comparisons will use appropriate tolerances for each quantity (e.g., ±0.02 Å for lattice parameters, ±0.05 J/m² for surface energies, ±0.02 Å for atomic displacements). The checker will also verify structural relations (TiO2-terminated surface energy lower than SrO-terminated, and a_perp decreasing/increasing with thickness for compressive/tensile strain)."
}
```

## How you are scored
A hidden verifier independently examines each scored artifact (bulk_properties.json, surface_properties.json, thin_film_properties.json). For every quantity, the verifier checks that the submitted value lies within a predefined tolerance of the expected result; directional metrics are scored in a monotonic way (better‑than‑reference never penalized). The verifier also enforces structural expectations, such as the ordering of the two surface energies and the correct thickness‑dependent trends of the out‑of‑plane lattice parameter under strain. The three artifacts are weighted according to their importance (surface properties > thin‑film properties > bulk properties), and the final reward is the weighted sum across all scored stages. Simply reporting numbers without executing the model and Monte Carlo relaxations does not produce the required intermediate evidence and will receive no credit.
