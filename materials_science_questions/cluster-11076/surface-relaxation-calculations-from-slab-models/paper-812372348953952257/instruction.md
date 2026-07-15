# Surface Relaxation and Attachment Energy Calculations for γ-Fe₂O₃ Low-Index Surfaces

## Problem background
γ-Fe₂O₃ (maghemite) is a spinel-type iron oxide with partially occupied octahedral Fe sites. Direct atomistic simulations of surfaces are challenging because of the non‑integer occupancy, which can be treated with a mean‑field approximation that scales the octahedral Fe charge, Buckingham A parameter, and shell force constant by the fractional occupancy, and adjusts oxygen‑oxygen interactions to recover the experimental lattice constant. Under this potential model, all low‑index surfaces are polar and must be reconstructed by introducing vacancies to cancel the surface dipole. The surface energy and attachment energy of several low‑index surfaces have been calculated with classical atomistic simulations to predict equilibrium and growth morphologies. The present task reproduces these calculations to establish which surface is thermodynamically most stable and which surfaces dominate crystal growth.

## Approach
Classical atomistic simulations based on the Born model are used. Short‑range interactions are described by Buckingham potentials, and ionic polarizability is included via the shell model. To account for the partial occupancy of octahedral iron sites, the potential parameters for octahedral Fe (charge, Buckingham A, shell force constant k) are scaled by the occupancy fraction 5/6, and the O–O Buckingham A is increased by 10 % to reproduce the experimental lattice constant of 8.35 Å. Starting from the known spinel structure (Fd3m), the bulk crystal is relaxed to obtain equilibrium coordinates and lattice energy. For each low‑index surface — (001), (011), (111), (012), (112), (122) — a 2D periodic slab model is built. Because every surface is polar, each must be reconstructed to cancel the perpendicular dipole. Harding’s formula is applied to determine the required charge change per plane, which is realized by introducing integer numbers of ion vacancies (or, for one termination, adding ions). Different arrangements of vacancies are considered to find the lowest‑energy configuration. Surface relaxation is performed with the MARVIN surface code (or an equivalent 2D periodic shell‑model code) using region I thicknesses of 4–6 repeat units and region II thicknesses of 6–12 repeat units. The relaxed surface energy is computed from the energy difference between the slab and the bulk, and the attachment energy is obtained as the difference between the crystal energy and the slice energy of a growth layer complementary to the relaxed surface. The most stable surface and the slowest‑growing surface are identified from these energies.

## Reproduction target
Compute the relaxed surface energy (in J/m²) and the relaxed attachment energy (in eV per molecule) for the six low‑index surfaces of γ‑Fe₂O₃: (001), (011), (111), (012), (112), (122). For each Miller index, determine the reconstructed termination that gives the lowest relaxed surface energy and the lowest relaxed attachment energy, and report these values in the required output files. The task must demonstrate which surface exhibits the lowest surface energy and which surface(s) have the smallest attachment energy, thereby predicting the equilibrium and growth crystal morphologies.

## Assets

- GULP – General Utility Lattice Program: https://gulp.curtin.edu.au/
- Islam & Catlow Fe₃O₄ potential parameters
- γ-Fe₂O₃ spinel crystal structure

## Workflow steps

### Step 1: Bulk relaxation with mean-field potential parameterization
- Role: process
- Action: Construct the mean-field potential parameters for γ-Fe₂O₃. Starting from the Fe₃O₄ Buckingham and shell parameters of Islam & Catlow, scale the octahedral iron charge to +2.5, scale its Buckingham A and shell force constant k by the fractional occupancy 5/6, and increase the oxygen–oxygen Buckingham A by 10% to reproduce the experimental lattice constant a=8.35 Å. Build the spinel unit cell (Fd3m) and relax the bulk structure to equilibrium using GULP or an equivalent classical simulation code. Record the relaxed lattice constant, final lattice energy, and relaxed atomic coordinates.
- Evidence: `/app/outputs/crystal_energy.txt`

### Step 2: Polar surface reconstruction design
- Role: process
- Action: For each low-index surface (001), (011), (111), (012), (112), (122), determine the plane compositions and interplanar spacings of the alternating charged planes. Apply Harding's formula to compute the α factor and the required charge change per plane to cancel the surface dipole. Determine the integer numbers of ions to add or remove to stabilize each surface termination, producing the reconstructed surface compositions as listed in the paper's Tables 2–3. For the (111) oxygen surface, double the cell area to accommodate the required integer vacancies. Generate candidate high- and low-symmetry vacancy arrangements for later screening.
- Evidence: none

### Step 3: Surface energy calculation
- Role: scored (load-bearing)
- Action: For each reconstructed surface termination, construct a 2D periodic slab model using the relaxed bulk coordinates from step_01. Perform slab relaxations with a classical shell-model code and the mean-field potentials. Use region thicknesses of 4–6 repeat units in region I and 6–12 in region II. For surfaces with multiple candidate vacancy arrangements, compute unrelaxed and relaxed surface energies and select the arrangement giving the lowest relaxed surface energy. For each Miller index, write the surface termination with the minimum relaxed surface energy and the corresponding relaxed surface energy in J/m² to surface_energies.csv.
- Output file: `/app/outputs/surface_energies.csv`
- Format: csv
- Contract: surface (string), termination (string), relaxed_surface_energy_J_m2 (float)
- Scoring: scored by hidden verifier

### Step 4: Attachment energy calculation
- Role: scored (load-bearing)
- Action: For each reconstructed surface, build a growth slice complementary to the relaxed surface. Compute the slice energy and the attachment energy using the relation E_att = E_crystal - E_slice, where E_crystal is the bulk energy from step_01 and E_crystal is the energy per formula unit. Perform the calculation for the unrelaxed and relaxed attachment energies. For each Miller index, write the termination with the lowest relaxed attachment energy and the corresponding relaxed attachment energy in eV per molecule to attachment_energies.csv.
- Output file: `/app/outputs/attachment_energies.csv`
- Format: csv
- Contract: surface (string), termination (string), relaxed_attachment_energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energies.csv`
- `/app/outputs/attachment_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energies.csv
- path: `/app/outputs/surface_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Relaxed surface energies of γ-Fe₂O₃ low-index surfaces. Each row gives the Miller index, the most stable reconstructed termination composition, and the minimum relaxed surface energy in J/m².
- schema:
  - `type`: table
  - `required_columns`: `surface`, `termination`, `relaxed_surface_energy_J_m2`
  - `units`:
    - `relaxed_surface_energy_J_m2`: J/m²

### attachment_energies.csv
- path: `/app/outputs/attachment_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Relaxed attachment energies of γ-Fe₂O₃ low-index surfaces. Each row gives the Miller index, the reconstructed termination, and the minimum relaxed attachment energy in eV per molecule.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `termination`, `relaxed_attachment_energy_eV`
  - `units`:
    - `relaxed_attachment_energy_eV`: eV

Notes: The surface energy and attachment energy outputs must be obtained by re-running the simulation workflow. Implementation can use any classical code that supports Buckingham potentials and a shell model. The main surfaces to include are (001), (011), (111), (012), (112), (122).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "termination",
          "relaxed_surface_energy_J_m2"
        ],
        "units": {
          "relaxed_surface_energy_J_m2": "J/m²"
        }
      },
      "description": "Relaxed surface energies of γ-Fe₂O₃ low-index surfaces. Each row gives the Miller index, the most stable reconstructed termination composition, and the minimum relaxed surface energy in J/m²."
    },
    {
      "file": "attachment_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "termination",
          "relaxed_attachment_energy_eV"
        ],
        "units": {
          "relaxed_attachment_energy_eV": "eV"
        }
      },
      "description": "Relaxed attachment energies of γ-Fe₂O₃ low-index surfaces. Each row gives the Miller index, the reconstructed termination, and the minimum relaxed attachment energy in eV per molecule."
    }
  ],
  "notes": "The surface energy and attachment energy outputs must be obtained by re-running the simulation workflow. Implementation can use any classical code that supports Buckingham potentials and a shell model. The main surfaces to include are (001), (011), (111), (012), (112), (122)."
}
```

## How you are scored
A hidden verifier independently evaluates each output file. For surface_energies.csv, the checker compares your reported surface energies to reference values and verifies that the surface with the lowest relaxed surface energy is correctly identified. For attachment_energies.csv, the checker compares your attachment energies to reference values and verifies that the surfaces with the smallest attachment energies are correctly identified. The final score is a weighted combination of the scores from these two stages. Legitimate differences due to alternative implementations are absorbed by the verification protocol, but you must faithfully follow the described computational protocol (potential parameters, reconstruction rules, slab setup) to achieve accurate results. Simply reporting the reference numbers without performing the simulations will not pass the hidden checks.
