# Validation of DFT+U Method for Oxygen Binding on Co3O4 Surfaces

## Problem background
Spinel Co3O4 is an important oxidation catalyst used in reactions such as CO oxidation, ammonia oxidation, and hydrocarbon combustion. Accurate computational modelling of its surface reactivity requires a DFT method that properly accounts for strong electron correlation on cobalt sites. The pure GGA functional PBE often yields inaccurate heats of formation and band gaps, while the screened hybrid functional HSE06 gives more reliable results but is computationally demanding. The DFT+U method (PBE+U) with a calibrated Hubbard U parameter offers a potential compromise. This task investigates whether PBE+U (Ueff = 3.3 eV on Co d‑orbitals) can reproduce the binding energies and adsorption geometries of atomic oxygen on three distinct Co3O4 surface terminations, using HSE06 single‑point energies as a benchmark. You will compute the binding energies and key bond lengths for oxygen adsorbed at low coverage on the (100)-A, (100)-B, and (110)-A surfaces, and the verifier will assess the agreement between the two methods.

## Approach
The computational protocol consists of spin‑polarised periodic DFT calculations using a plane‑wave basis and projector‑augmented wave (PAW) pseudopotentials, carried out with the open‑source Quantum ESPRESSO package. The general workflow is:

1. **Bulk optimisation** – Determine the equilibrium lattice constant of bulk Co3O4 (spinel) with PBE+U (U = 3.3 eV on Co d‑states).
2. **Slab construction and relaxation** – Build three slab models from the optimised bulk: Co3O4(100)-A (√2×√2)R45° unit cell, 6 layers, non‑symmetric; Co3O4(100)-B (√2×√2)R45°, 5 layers, symmetric; Co3O4(110)-A (1×1), 5 layers, symmetric. All slabs include 15 Å vacuum. Relax all atoms except the bottom three layers with PBE+U.
3. **Oxygen adsorption relaxation (PBE+U)** – Place one oxygen atom at the specified low‑coverage adsorption site on each relaxed slab: on‑top of a surface tetrahedral Co (Coᵗ) for (100)-A at θ_O = 0.16 ML; bridging a surface octahedral Co (Coᵒ) and a surface three‑coordinate lattice O (O³ᵒ) for (100)-B at θ_O = 0.25 ML; bridging two surface Coᵗ atoms for (110)-A at θ_O = 0.25 ML. Relax the adsorbate+slab system with PBE+U (bottom three layers fixed). Compute the oxygen binding energy (E_b⁰) from the total energies of the adsorbate-covered slab, the clean slab, and an isolated gas‑phase oxygen atom (spin‑polarised, 15 Å box). Record the relevant bond lengths: Coᵗ–O, Coᵒ–O, and O–O³ᵒ (where applicable).
4. **HSE06 single‑point calculations** – For each relaxed PBE+U geometry from step 3, perform a single‑point total energy calculation with the HSE06 functional (screening length μ = 0.2 Å⁻¹) using the same plane‑wave cutoff and k‑point sampling. Re‑evaluate the binding energies with these HSE06 total energies, using a consistently computed HSE06 gas‑phase O atom energy.
5. **Compile results** – Collect the PBE+U and HSE06 binding energies (in kJ mol⁻¹) and the bond lengths (in Å) into the CSV file `step_05_binding_energies.csv` as specified in the output contract.

## Reproduction target
Produce the output file `/app/outputs/step_05_binding_energies.csv` containing six data rows: for each surface `100-A`, `100-B` and `110-A`, include one row with `method = PBE+U` and one row with `method = HSE06`. The columns must be exactly: `surface`, `method`, `binding_energy_kJmol`, `Co_O_bond_A`, `O_O_lattice_bond_A`. The `O_O_lattice_bond_A` column should contain the O–O distance between the adsorbed oxygen and the nearest lattice oxygen; if no such bond exists, leave the cell empty or use `null`. The verifier will compare your reported values to independently derived reference data and will evaluate the agreement between the PBE+U and HSE06 results (i.e., whether the binding energies from the two methods are consistent with each other and with expected physical values).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency) for Co and O: https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Bulk Co3O4 lattice constant optimization
- Role: process
- Action: Perform DFT optimization of the bulk Co3O4 spinel unit cell using PBE+U with Ueff=3.3 eV on Co d-states to obtain the equilibrium lattice constant. Use a reasonable k‑point mesh and energy cutoff.
- Evidence: `/app/outputs/bulk_lattice_constant.txt`

### Step 2: Construction and relaxation of bare surface slabs
- Role: process
- Action: Build the three slab models from the optimized bulk structure: Co3O4(100)-A (√2×√2)R45° unit cell, 6 layers, non-symmetric), Co3O4(100)-B (√2×√2)R45°, 5 layers, symmetric), and Co3O4(110)-A (1×1 unit cell, 5 layers, symmetric). Include a 15 Å vacuum. Relax all atoms except the bottom three layers using PBE+U with appropriate k‑point meshes for each surface.
- Evidence: none

### Step 3: Atomic oxygen adsorption site relaxation (PBE+U)
- Role: process
- Action: Place one O atom at the specified adsorption sites: (100)-A Co^t top (θ_O=0.16 ML), (100)-B Co^o–O^3o bridge (θ_O=0.25 ML), and (110)-A Co^t–Co^t bridge (θ_O=0.25 ML). Relax the adsorbate+slab systems with PBE+U (Ueff=3.3 eV on Co d-states), keeping the bottom three layers fixed. Record the total energies, the binding energy computed from the energy of the isolated O atom and the bare slab energy, and the relevant bond lengths (Co^t–O, Co^o–O, O–O^3o).
- Evidence: none

### Step 4: HSE06 single‑point calculations
- Role: process
- Action: For each of the three PBE+U relaxed geometries from step_03, perform a single‑point energy calculation using the HSE06 functional with a screening length of 0.2 Å⁻¹. Use the same k‑point meshes and energy cutoff as in the PBE+U calculations. Compute the binding energy for each system using the HSE06 total energy, the bare slab energy, and a consistently computed energy of the gas‑phase O atom.
- Evidence: none

### Step 5: Compile and save binding energies and geometries
- Role: scored (load-bearing)
- Action: Create a CSV file `step_05_binding_energies.csv` containing the binding energies (in kJ/mol) and key bond lengths (in Å) for each of the three surfaces for both PBE+U (relaxed) and HSE06 (single‑point on the PBE+U geometry).
- Output file: `/app/outputs/step_05_binding_energies.csv`
- Format: csv
- Contract: Columns: surface (string: '100-A', '100-B', '110-A'), method (string: 'PBE+U', 'HSE06'), binding_energy_kJmol (float), Co_O_bond_A (float), O_O_lattice_bond_A (float or null if not applicable). One row per surface per method.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_05_binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_05_binding_energies.csv
- path: `/app/outputs/step_05_binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies and bond lengths for O adsorption on three Co3O4 surfaces, computed with PBE+U (relaxed) and HSE06 (single-point on PBE+U geometry). The checker will compare these values to paper-reported reference values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `method`, `binding_energy_kJmol`, `Co_O_bond_A`, `O_O_lattice_bond_A`
  - `units`:
    - `binding_energy_kJmol`: kJ/mol
    - `Co_O_bond_A`: Å
    - `O_O_lattice_bond_A`: Å

Notes: The task reproduces the low-coverage validation of PBE+U against HSE06 for three surface terminations. Coverage-dependent studies, vacancy formation, and reaction barriers are omitted (see plan).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_05_binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "method",
          "binding_energy_kJmol",
          "Co_O_bond_A",
          "O_O_lattice_bond_A"
        ],
        "units": {
          "binding_energy_kJmol": "kJ/mol",
          "Co_O_bond_A": "Å",
          "O_O_lattice_bond_A": "Å"
        }
      },
      "description": "Binding energies and bond lengths for O adsorption on three Co3O4 surfaces, computed with PBE+U (relaxed) and HSE06 (single-point on PBE+U geometry). The checker will compare these values to paper-reported reference values with appropriate tolerances."
    }
  ],
  "notes": "The task reproduces the low-coverage validation of PBE+U against HSE06 for three surface terminations. Coverage-dependent studies, vacancy formation, and reaction barriers are omitted (see plan)."
}
```

## How you are scored
A hidden verifier reads your CSV file and checks each binding energy and bond length against reference data derived from published results. It verifies that the numbers are realistic, that the PBE+U and HSE06 binding energies are in close agreement, and that the relative ordering across surfaces is preserved. The final reward is a weighted sum of several checks: validity of the surface identifiers, presence and plausibility of all numeric entries, conformity of the binding energies and bond lengths with expected ranges, and the magnitude of the differences between the PBE+U and HSE06 values. The score ranges from 0 to 1. Note that the verifier uses hidden tolerances; simply providing a well‑formatted file with arbitrary numbers will not yield a high score.
