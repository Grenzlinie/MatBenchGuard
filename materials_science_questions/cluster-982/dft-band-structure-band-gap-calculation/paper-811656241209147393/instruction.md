# Compute CBM Band Edge Positions of Semiconductors Relative to Water H2O/H2 Level

## Problem background
Design of water-splitting photocatalysts requires knowledge of the conduction band minimum (CBM) positions of semiconductors relative to the H₂O/H₂ redox level in water. This knowledge is critical to select materials that can drive the hydrogen evolution reaction without an external bias. The task is to compute, from first principles, the CBM band edge positions (denoted E_{C_edge} – A_{edge}) for six semiconductor photocatalyst materials (TiO₂, WO₃, CdS, ZnSe, GaAs, GaP) using a three-step alignment method that combines bulk semiconductor electronic structure, liquid water acceptor levels, and the semiconductor–water interface Hartree potential.

## Approach
The band edge position is obtained by a three-step electrostatic alignment procedure:
1. Bulk semiconductor calculation: Compute the energy of the CBM relative to the average Hartree potential in the bulk crystal (E_C_bulk – H_semi_bulk).
2. Bulk liquid water acceptor level: Using classical molecular dynamics snapshots of liquid water, insert an optimized hydronium ion (H₃O⁺) and compute its lowest unoccupied molecular orbital (LUMO) energy relative to the average Hartree potential in the water cell (A_bulk – H_sol_bulk). The configuration with the lowest total energy is selected.
3. Interface Hartree potential offset: Construct a semiconductor–water interface slab supercell and compute the planar-averaged Hartree potential on both sides to obtain the difference H_semi_edge – H_sol_edge.
The final CBM band edge position is then obtained from the combination formula:
E_{C_edge} – A_{edge} = (E_C_bulk – H_semi_bulk) – (A_bulk – H_sol_bulk) + (H_semi_edge – H_sol_edge).
For WO₃, an additional GGA+U calculation (with U=2.0 eV) is performed to correct the d‑electron self‑interaction error.

## Reproduction target
Through the ordered workflow steps listed below, compute the CBM band edge positions E_{C_edge} – A_{edge} for the six photocatalyst materials (TiO₂, WO₃, CdS, ZnSe, GaAs, GaP) and the GGA+U corrected value for WO₃. All intermediate calculations (classical MD of water, DFT validation, hydronium relaxation, insertion runs, bulk semiconductor DFT, and interface slab DFT) must be executed. The final result is a JSON file `computed_band_edges.json` containing the seven numeric band edge positions (in eV).

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- GPAW DFT code with PAW: https://wiki.fysik.dtu.dk/gpaw/
- TIP4P water model: lammps
- PBE PAW pseudopotentials (GPAW setups): https://wiki.fysik.dtu.dk/gpaw/setups/setups.html

## Workflow steps

### Step 1: Classical MD simulation of liquid water
- Role: process
- Action: Run LAMMPS simulation of 128 H2O molecules at 300 K using the TIP4P potential. Equilibrate, then run NVT production for 100 ps. Save atomic configurations at t=50 ps and t=100 ps as water_50ps.xyz and water_100ps.xyz.
- Evidence: `/app/outputs/water_50ps.xyz, water_100ps.xyz`

### Step 2: DFT consistency check of water snapshots
- Role: process
- Action: Using GPAW with PBE and Γ‑only k‑point, compute the band gaps for the two water snapshots without relaxation and for the 100 ps snapshot after full ionic relaxation. Verify consistent electronic structures and record the band gaps in water_validation.json.
- Evidence: `/app/outputs/water_validation.json`

### Step 3: Relax isolated H3O+ ion
- Role: process
- Action: Using GPAW, fully relax the geometry of an isolated H3O+ ion. Save the optimized structure to h3o_structure.xyz.
- Evidence: `/app/outputs/h3o_structure.xyz`

### Step 4: Water acceptor level calculation via hydronium insertion
- Role: process
- Action: Insert the relaxed H3O+ into the 100 ps water cell by replacing four different H2O molecules. For each, relax the H3O+ ionic positions, then run static DFT to compute the LUMO energy and average Hartree potential. Determine A_bulk - H_sol_bulk for each configuration and select the value corresponding to the lowest total energy. Save the selected value (in eV) to acceptor_value.txt and detailed results to acceptor_details.json.
- Evidence: `/app/outputs/acceptor_value.txt, acceptor_details.json`

### Step 5: Semiconductor bulk DFT calculations
- Role: process
- Action: For TiO2, WO3, CdS, ZnSe, GaAs, GaP, perform full geometry optimization with PBE and high‑quality k‑point mesh, then a static calculation to obtain E_C_bulk - H_semi_bulk (CBM energy relative to average Hartree potential). For WO3, also compute with GGA+U (U=2.0 eV). Save all values to semiconductor_bulk.json.
- Evidence: `/app/outputs/semiconductor_bulk.json`

### Step 6: Semiconductor–water interface Hartree potential difference
- Role: process
- Action: For each semiconductor, construct an interface slab supercell from the optimized bulk and the undoped water cell. Run GPAW with Γ‑only, compute the planar‑averaged Hartree potential on both sides, and extract H_semi_edge - H_sol_edge. For WO3, also compute using the GGA+U bulk cell. Save results to interface_differences.json.
- Evidence: `/app/outputs/interface_differences.json`

### Step 7: Combine alignment terms to obtain CBM band edge positions
- Role: scored (load-bearing)
- Action: Read the selected acceptor value from acceptor_value.txt, bulk semiconductor terms from semiconductor_bulk.json, and interface differences from interface_differences.json. Compute E_{C_edge} - A_{edge} = (E_C_bulk - H_semi_bulk) - (A_bulk - H_sol_bulk) + (H_semi_edge - H_sol_edge) for TiO2, WO3, CdS, ZnSe, GaAs, GaP, and the GGA+U corrected WO3. Output the computed band edge positions to computed_band_edges.json.
- Output file: `/app/outputs/computed_band_edges.json`
- Format: json
- Contract: A JSON object with keys 'TiO2', 'WO3', 'CdS', 'ZnSe', 'GaAs', 'GaP', 'WO3_GGA+U'; values are floats in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_band_edges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_band_edges.json
- path: `/app/outputs/computed_band_edges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed CBM band edge positions (E_C_edge - A_edge) relative to the water H2O/H2 level for six semiconductors and the GGA+U corrected value for WO3.
- schema:
  - `type`: object
  - `required`:
    - `TiO2`: float (eV)
    - `WO3`: float (eV)
    - `CdS`: float (eV)
    - `ZnSe`: float (eV)
    - `GaAs`: float (eV)
    - `GaP`: float (eV)
    - `WO3_GGA+U`: float (eV)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_band_edges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "TiO2": "float (eV)",
          "WO3": "float (eV)",
          "CdS": "float (eV)",
          "ZnSe": "float (eV)",
          "GaAs": "float (eV)",
          "GaP": "float (eV)",
          "WO3_GGA+U": "float (eV)"
        }
      },
      "description": "Computed CBM band edge positions (E_C_edge - A_edge) relative to the water H2O/H2 level for six semiconductors and the GGA+U corrected value for WO3."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently evaluate your submission. The primary scored artifact is `computed_band_edges.json`. The verifier compares each of the seven values against hidden reference values (derived from the original study) with an absolute tolerance that accommodates expected spread between different DFT implementations. Full credit is awarded if all seven values fall within the tolerance; partial credit is proportional to the fraction of values that are within tolerance. Simply reporting known literature values without actually performing the computational workflow will not receive credit, because the verifier also checks for the presence of the required intermediate evidence artifacts (e.g., water snapshots, bulk and interface output files). To succeed, you must genuinely execute the procedure and produce the numbers from your own calculations.
