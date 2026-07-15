# Magnetic anisotropy energy and structural preference in CuFe2O4 systems from first-principles calculations

## Problem background
Copper ferrite (CuFe2O4) is a spinel-type oxide that can form in an inverse spinel structure where Fe3+ ions occupy tetrahedral A sites and a mixture of Cu2+ and Fe3+ ions occupy octahedral B sites. The distribution of Cu ions among the B sites affects the Jahn-Teller distortion and the material's magnetic properties. When interfaced with MgO, CuFe2O4 may exhibit tunable magnetic anisotropy, making it promising for spintronic applications. This task uses first-principles density functional theory (DFT) calculations with an on-site Hubbard U correction to determine the ground-state Cu arrangement among several octahedral configurations of the inverse spinel structure, the resulting lattice distortion, and the magnetic anisotropy energy (MAE) of CuFe2O4/MgO superlattices compared to Fe3O4/MgO. The key quantities to compute are the optimized in-plane lattice constant a, the c/a ratio for the most stable configuration, the energy differences of other configurations relative to the ground state, and the MAE for one-unit-cell and two-unit-cell superlattices with different interface terminations.

## Approach
The calculations are performed using the PBE generalized gradient approximation (GGA) with Hubbard U corrections (Ueff = 3.5 eV for Fe, 4.0 eV for Cu) as implemented in an open-source plane-wave DFT code (e.g., Quantum ESPRESSO). The workflow involves:

1. Constructing atomic structures for the inverse spinel CuFe2O4 with four distinct arrangements of Cu on the octahedral sites (types I, II, III, IV) and the normal spinel arrangement, as well as the inverse spinel Fe3O4.
2. Relaxing the ionic positions and cell parameters (allowing tetragonal distortion) to find the stable structure for each configuration, then identifying the ground-state configuration and computing energy differences.
3. Using the relaxed bulk structures to build periodic superlattice models of CuFe2O4(001)/MgO and Fe3O4(001)/MgO with one and two ferrite unit cells, considering both FeO and CuO interface terminations. The in-plane lattice is aligned to the MgO reference lattice constant.
4. Relaxing the superlattice geometries (ions only, in-plane lattice fixed).
5. Performing non-collinear spin-orbit coupling calculations to obtain total energies when magnetization is oriented in-plane (E_parallel) and out-of-plane (E_perpendicular), from which the magnetic anisotropy energy MAE = E_parallel − E_perpendicular is computed.

Comparing the results for CuFe2O4/MgO against Fe3O4/MgO provides insight into the effect of Cu substitution on magnetic anisotropy.

## Reproduction target
Produce two JSON artifacts containing the computed results:

1. `bulk_results.json`: contains the optimized in-plane lattice constant a (Å) and c/a ratio for the most stable CuFe2O4 configuration (type II), and the relative energies ΔE (eV/f.u.) of configurations type I, III, IV, and the normal spinel structure relative to type II.
2. `mae_results.json`: contains the magnetic anisotropy energy MAE (meV/f.u.) for: bulk CuFe2O4, one-unit-cell and two-unit-cell CuFe2O4/MgO superlattices with FeO interface termination, one-unit-cell CuFe2O4/MgO with CuO interface termination, and one-unit-cell and two-unit-cell Fe3O4/MgO superlattices with FeO interface termination.

All values must be obtained from first-principles calculations as described in the workflow steps; the structures and computational protocol are defined in the steps and the assets.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials or PSLibrary: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate CuFe2O4 configurations and reference structures
- Role: process
- Action: Construct atomic structures for the four inverse spinel Cu configurations (types I, II, III, IV) and the normal spinel CuFe2O4, as well as the inverse spinel Fe3O4. Use the crystal structure description: fcc lattice with Fd3m symmetry, tetrahedral A sites occupied by Fe3+, octahedral B sites occupied by the mixture of Fe2+/Fe3+ and Cu2+ according to each configuration. Write DFT input files.
- Evidence: none

### Step 2: Bulk DFT+U relaxation and energy differences
- Role: scored (load-bearing)
- Action: Perform GGA+U (PBE functional) DFT calculations on all generated bulk structures (types I–IV, normal, and Fe3O4). Apply Hubbard U parameters: Ueff = 3.5 eV for Fe and 4.0 eV for Cu. For each inverse spinel configuration, relax ionic positions and cell parameters (allowing tetragonal distortion). From the relaxed results, identify the ground-state configuration (type II) and record its optimized in-plane lattice constant a (Å) and c/a ratio. Compute the total energy differences ΔE (eV per formula unit) of types I, III, IV, and the normal spinel relative to type II. Store the results in bulk_results.json.
- Output file: `/app/outputs/bulk_results.json`
- Format: json
- Contract: JSON object with keys: a_type_II (float, Å), c_over_a_type_II (float), delta_E_type_I (float, eV/f.u.), delta_E_type_III (float, eV/f.u.), delta_E_type_IV (float, eV/f.u.), delta_E_normal (float, eV/f.u.)
- Scoring: scored by hidden verifier

### Step 3: Build superlattice heterostructure models
- Role: process
- Action: Using the relaxed bulk structures, build periodic superlattice cells for: (a) one-unit-cell CuFe2O4(001)/MgO with FeO interface termination, (b) one-unit-cell with CuO interface termination, (c) two-unit-cell CuFe2O4/MgO with FeO interface, (d) one-unit-cell Fe3O4/MgO with FeO interface, and (e) two-unit-cell Fe3O4/MgO with FeO interface. Align the in-plane lattice to the MgO lattice constant (4.212 Å) with appropriate matching. Write the DFT input files.
- Evidence: none

### Step 4: Relax superlattice geometries
- Role: process
- Action: Relax the ionic positions of all superlattice structures built in step 03 using DFT+U (same U parameters). Keep the in-plane lattice fixed to the MgO-derived constant during relaxation. The relaxed coordinates will be used for MAE calculations.
- Evidence: none

### Step 5: Compute magnetic anisotropy energy (MAE)
- Role: scored (load-bearing)
- Action: For the relaxed bulk CuFe2O4 type-II and each relaxed superlattice, perform non-collinear spin-orbit coupling (SOC) calculations. Compute the total energy for magnetization oriented in the xy-plane (E_parallel) and along the z-axis (E_perpendicular). Calculate MAE = E_parallel - E_perpendicular (meV/f.u.). Record the following MAE values in mae_results.json: bulk CuFe2O4, FeO-interface-terminated one-unit-cell and two-unit-cell CuFe2O4/MgO, CuO-interface-terminated one-unit-cell CuFe2O4/MgO, and one-unit-cell and two-unit-cell Fe3O4/MgO.
- Output file: `/app/outputs/mae_results.json`
- Format: json
- Contract: JSON object with keys: bulk_CuFe2O4_MAE (float, meV/f.u.), FeO_int_one_unit_CuFe2O4_MgO_MAE, FeO_int_two_unit_CuFe2O4_MgO_MAE, CuO_int_one_unit_CuFe2O4_MgO_MAE, FeO_int_one_unit_Fe3O4_MgO_MAE, FeO_int_two_unit_Fe3O4_MgO_MAE
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_results.json`
- `/app/outputs/mae_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_results.json
- path: `/app/outputs/bulk_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural parameters and energy differences for bulk CuFe2O4 configurations.
- schema:
  - `type`: object
  - `required`: `a_type_II`, `c_over_a_type_II`, `delta_E_type_I`, `delta_E_type_III`, `delta_E_type_IV`, `delta_E_normal`
  - `properties`:
    - `a_type_II`:
      - `type`: number
      - `unit`: Å
    - `c_over_a_type_II`:
      - `type`: number
      - `unit`: dimensionless
    - `delta_E_type_I`:
      - `type`: number
      - `unit`: eV/f.u.
    - `delta_E_type_III`:
      - `type`: number
      - `unit`: eV/f.u.
    - `delta_E_type_IV`:
      - `type`: number
      - `unit`: eV/f.u.
    - `delta_E_normal`:
      - `type`: number
      - `unit`: eV/f.u.

### mae_results.json
- path: `/app/outputs/mae_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic anisotropy energy values for bulk and superlattice systems.
- schema:
  - `type`: object
  - `required`: `bulk_CuFe2O4_MAE`, `FeO_int_one_unit_CuFe2O4_MgO_MAE`, `FeO_int_two_unit_CuFe2O4_MgO_MAE`, `CuO_int_one_unit_CuFe2O4_MgO_MAE`, `FeO_int_one_unit_Fe3O4_MgO_MAE`, `FeO_int_two_unit_Fe3O4_MgO_MAE`
  - `properties`:
    - `bulk_CuFe2O4_MAE`:
      - `type`: number
      - `unit`: meV/f.u.
    - `FeO_int_one_unit_CuFe2O4_MgO_MAE`:
      - `type`: number
      - `unit`: meV/f.u.
    - `FeO_int_two_unit_CuFe2O4_MgO_MAE`:
      - `type`: number
      - `unit`: meV/f.u.
    - `CuO_int_one_unit_CuFe2O4_MgO_MAE`:
      - `type`: number
      - `unit`: meV/f.u.
    - `FeO_int_one_unit_Fe3O4_MgO_MAE`:
      - `type`: number
      - `unit`: meV/f.u.
    - `FeO_int_two_unit_Fe3O4_MgO_MAE`:
      - `type`: number
      - `unit`: meV/f.u.

Notes: The original paper used VASP; this reproduction replaces it with Quantum ESPRESSO (or another open-source plane-wave DFT code) following the same PBE+GGA+U and SOC treatment. Tolerances applied by the hidden checker account for implementation-dependent differences in pseudopotentials and basis sets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a_type_II",
          "c_over_a_type_II",
          "delta_E_type_I",
          "delta_E_type_III",
          "delta_E_type_IV",
          "delta_E_normal"
        ],
        "properties": {
          "a_type_II": {
            "type": "number",
            "unit": "Å"
          },
          "c_over_a_type_II": {
            "type": "number",
            "unit": "dimensionless"
          },
          "delta_E_type_I": {
            "type": "number",
            "unit": "eV/f.u."
          },
          "delta_E_type_III": {
            "type": "number",
            "unit": "eV/f.u."
          },
          "delta_E_type_IV": {
            "type": "number",
            "unit": "eV/f.u."
          },
          "delta_E_normal": {
            "type": "number",
            "unit": "eV/f.u."
          }
        }
      },
      "description": "Structural parameters and energy differences for bulk CuFe2O4 configurations."
    },
    {
      "file": "mae_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bulk_CuFe2O4_MAE",
          "FeO_int_one_unit_CuFe2O4_MgO_MAE",
          "FeO_int_two_unit_CuFe2O4_MgO_MAE",
          "CuO_int_one_unit_CuFe2O4_MgO_MAE",
          "FeO_int_one_unit_Fe3O4_MgO_MAE",
          "FeO_int_two_unit_Fe3O4_MgO_MAE"
        ],
        "properties": {
          "bulk_CuFe2O4_MAE": {
            "type": "number",
            "unit": "meV/f.u."
          },
          "FeO_int_one_unit_CuFe2O4_MgO_MAE": {
            "type": "number",
            "unit": "meV/f.u."
          },
          "FeO_int_two_unit_CuFe2O4_MgO_MAE": {
            "type": "number",
            "unit": "meV/f.u."
          },
          "CuO_int_one_unit_CuFe2O4_MgO_MAE": {
            "type": "number",
            "unit": "meV/f.u."
          },
          "FeO_int_one_unit_Fe3O4_MgO_MAE": {
            "type": "number",
            "unit": "meV/f.u."
          },
          "FeO_int_two_unit_Fe3O4_MgO_MAE": {
            "type": "number",
            "unit": "meV/f.u."
          }
        }
      },
      "description": "Magnetic anisotropy energy values for bulk and superlattice systems."
    }
  ],
  "notes": "The original paper used VASP; this reproduction replaces it with Quantum ESPRESSO (or another open-source plane-wave DFT code) following the same PBE+GGA+U and SOC treatment. Tolerances applied by the hidden checker account for implementation-dependent differences in pseudopotentials and basis sets."
}
```

## How you are scored
The hidden verifier evaluates each output file independently using reference values and tolerances derived from the original study. For `bulk_results.json`, it checks the reported structural parameters and energy differences against expected results (a tolerance accounts for using a different DFT code and pseudopotentials). For `mae_results.json`, it compares the MAE values and also verifies that the sign and thickness dependence of the MAE fulfill the correct physical trends for these systems (e.g., the sign of MAE indicates the preferred magnetization orientation, and the trend across different thicknesses and compositions should be consistent with the underlying physics). The final reward is a weighted combination of the scores from these two artifacts. Self-reported numbers that do not result from genuine execution of the DFT pipeline will not score highly because the verifier checks tolerance ranges and internal consistency that require a correctly reproduced calculation.
