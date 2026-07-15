# First-Principles DFT of TiO2 Rutile and Anatase: Structure, Bulk Modulus, and Band Gap

## Problem background
Titanium dioxide (TiO₂) crystallizes in several polymorphs, the most studied being rutile and anatase. These two phases are central to photocatalysis, photoelectrochemical water splitting, and dye-sensitized solar cells, where their structural, elastic, and electronic properties directly influence performance. Accurate first‑principles predictions of equilibrium crystal structures, bulk moduli, band gaps, and the relative stability of the two phases are therefore of great interest. Density‑functional theory within the local density approximation (LDA), combined with norm‑conserving pseudopotentials, provides a well‑established framework for computing these properties from the atomic numbers and crystal symmetries alone.

## Approach
You will perform first‑principles DFT calculations using the open‑source plane‑wave pseudopotential code ABINIT with the LDA exchange‑correlation functional. Two families of norm‑conserving pseudopotentials will be used: Troullier‑Martins (TM) type and Teter‑type extended norm‑conserving pseudopotentials. For titanium the valence configuration includes the 3s, 3p, 4s, and 3d states; for oxygen it consists of the 2s and 2p states. The workflow proceeds in stages: (i) obtain or generate the pseudopotentials; (ii) for rutile (space group P4₂/mnm) and anatase (I4₁/amd), perform symmetry‑constrained geometry optimizations to find the equilibrium lattice constants, internal atomic positions, and total energies; (iii) carry out total‑energy calculations at several fixed unit‑cell volumes while relaxing internal coordinates, then fit the energy–volume data to the Murnaghan equation of state to extract the bulk modulus; (iv) compute the electronic band structures along the high‑symmetry k‑point paths and determine the band‑gap energy and whether the gap is direct or indirect; (v) collect all quantities and the total‑energy difference per TiO₂ formula unit between rutile and anatase for each pseudopotential.

## Reproduction target
Using the ABINIT code and the pseudopotentials described above, compute the following properties for both rutile and anatase with each pseudopotential type (TM and Teter): equilibrium lattice constants a and c (in Å), their ratio c/a, the internal oxygen coordinate u, the mass density d (g/cm³), the bulk modulus B (GPa), the band‑gap energy (eV) and whether the gap is direct or indirect, and the total‑energy difference per TiO₂ formula unit between rutile and anatase (kcal/mol). Assemble all results into the JSON file computed_results.json with the exact structure specified in the output contract and the final workflow step. The hidden verifier will independently evaluate each quantity and check that the reported values obey physically required relationships.

## Assets

- ABINIT code: https://www.abinit.org/
- Norm-conserving pseudopotentials for Ti and O: ABINIT pseudopotential library or generate via FHI98PP
- FHI98PP pseudopotential generation package: https://www.abinit.org/ or standalone
- Rutile and anatase TiO2 crystal structures: 10.1107/S0567740871001156 (rutile) and 10.1524/zkri.1972.136.16.273 (anatase)

## Workflow steps

### Step 1: Pseudopotential preparation
- Role: process
- Action: Obtain or generate Troullier-Martins (TM) and Teter-type extended norm-conserving pseudopotentials for Ti (3s,3p,4s,3d valence) and O (2s,2p).
- Evidence: `/app/outputs/pseudopotential_files`

### Step 2: Geometry optimization
- Role: process
- Action: For rutile and anatase phases with both pseudopotential types, run ABINIT structural optimizations with plane-wave basis, Monkhorst-Pack k-point grids, and symmetry-imposed geometry relaxation to minimize forces. Record optimized lattice constants, internal coordinates, total energy, and density.
- Evidence: `/app/outputs/optimization_outputs`

### Step 3: Volume-dependent DFT and EOS fitting
- Role: process
- Action: Perform total-energy calculations at several fixed cell volumes spanning a range around the experimental volume for each optimized phase and pseudopotential while relaxing internal coordinates. Fit the resulting energy-volume points to Murnaghan's equation of state to extract the bulk modulus.
- Evidence: `/app/outputs/eos_data_and_fit`

### Step 4: Band structure calculation
- Role: process
- Action: Using the optimized crystal structures, compute electronic band structures along high-symmetry k-point paths and determine the band gap energy and whether the gap is direct or indirect.
- Evidence: `/app/outputs/band_structure_data`

### Step 5: Compile final results
- Role: scored (load-bearing)
- Action: From the preceding steps, collect equilibrium lattice constants a, c, c/a, internal oxygen coordinate u, density d, bulk modulus B, band gap and direct/indirect character, and total energy difference per formula unit between rutile and anatase for both pseudopotential types. Write all quantities into a JSON file computed_results.json.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: Top-level JSON with keys: 'rutile_TM', 'rutile_Teter', 'anatase_TM', 'anatase_Teter' each an object containing numeric fields 'a' (Å), 'c' (Å), 'c_over_a', 'u', 'density' (g/cm³), 'bulk_modulus' (GPa), 'band_gap' (eV), 'gap_direct' (boolean); and keys 'energy_TM' and 'energy_Teter' each an object containing 'E_rutile' (a.u.), 'E_anatase' (a.u.), 'difference_kcal_per_mol', and 'difference_sign_convention' fixed string 'E_anatase_minus_E_rutile'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated structural, elastic, electronic and energetic properties of rutile and anatase TiO2 computed with TM and Teter pseudopotentials.
- schema:
  - `type`: object
  - `description`: JSON with top-level keys rutile_TM, rutile_Teter, anatase_TM, anatase_Teter, energy_TM, energy_Teter. Each polymorph-pseudopotential key is an object with numeric properties a, c, c_over_a, u, density, bulk_modulus, band_gap, gap_direct (boolean). Energy difference keys contain E_rutile, E_anatase, difference_kcal_per_mol, difference_sign_convention (string, value 'E_anatase_minus_E_rutile').

Notes: All numeric values in stated units; energy differences sign convention is E_anatase_minus_E_rutile.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "JSON with top-level keys rutile_TM, rutile_Teter, anatase_TM, anatase_Teter, energy_TM, energy_Teter. Each polymorph-pseudopotential key is an object with numeric properties a, c, c_over_a, u, density, bulk_modulus, band_gap, gap_direct (boolean). Energy difference keys contain E_rutile, E_anatase, difference_kcal_per_mol, difference_sign_convention (string, value 'E_anatase_minus_E_rutile')."
      },
      "description": "Aggregated structural, elastic, electronic and energetic properties of rutile and anatase TiO2 computed with TM and Teter pseudopotentials."
    }
  ],
  "notes": "All numeric values in stated units; energy differences sign convention is E_anatase_minus_E_rutile."
}
```

## How you are scored
A hidden verifier independently reads your computed_results.json and compares each numeric quantity to the correct values. The comparisons allow generous tolerances appropriate for the LDA pseudopotential method, so legitimate run‑to‑run spread is absorbed. Additionally, the verifier checks that the computed quantities respect certain physical ordering relationships (e.g., relative magnitudes of band gaps and bulk moduli between the two phases) and that the correct sign convention for the energy difference is reported. The final reward is a weighted combination of all checks; reporting only a plausible number without executing the required DFT workflow will not pass.
