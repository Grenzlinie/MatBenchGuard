# Photocatalytic Water Splitting Band Edge Assessment

## Problem background
Design of water-splitting photocatalysts requires accurate knowledge of semiconductor conduction-band minimum (CBM) positions relative to the water H2O/H2 redox level. First-principles methods can predict these positions, enabling high-throughput computational screening of candidate materials. Traditional DFT approaches either neglect the semiconductor-water interface realignment or rely on a vacuum-level reference that introduces substantial errors. This work develops and validates a three-step method that directly accounts for the interface dipole and computes the CBM edge position for six commonly studied photocatalyst semiconductors. The challenge is to predict these CBM edge positions from first principles without fitting to experimental data.

## Approach
The method is built on a three-step scheme that avoids large supercells while capturing the band realignment at the semiconductor-water interface:

1. **Bulk semiconductor term** – Compute the CBM eigenvalue relative to the average Hartree potential (E_C_bulk − H_semi_bulk) for the bulk crystal using DFT with the PBE functional.

2. **Water acceptor term** – Generate a representative liquid water configuration via classical molecular dynamics (TIP4P water model). Replace one water molecule with a hydronium ion (H3O+) and perform DFT relaxation and static calculation to obtain the acceptor level (LUMO) relative to the average Hartree potential of the liquid water cell (A_bulk − H_sol_bulk). Repeat for several replacement positions and select the lowest total-energy configuration.

3. **Interface Hartree potential offset** – Build a slab model joining the semiconductor bulk cell and the water cell. From a static DFT calculation, extract the planar-averaged Hartree potential on each side of the interface and compute their difference (H_semi_edge − H_sol_edge).

The desired CBM edge position relative to the water H2O/H2 level is obtained by combining the three terms:

E_C_edge − A_edge = (E_C_bulk − H_semi_bulk) − (A_bulk − H_sol_bulk) + (H_semi_edge − H_sol_edge).

Apply this protocol to TiO2 (rutile), WO3 (tetragonal), CdS (wurtzite), ZnSe (zincblende), GaAs (zincblende), and GaP (zincblende). The crystal structure parameters (lattice constants and space groups) are provided in a table later in this instruction. Any open-source DFT code supporting the PBE functional (e.g., Quantum ESPRESSO) and a classical MD code with TIP4P (e.g., LAMMPS) are acceptable replacements for the proprietary tools used in the original study.

## Reproduction target
Recompute the CBM band edge positions (E_C_edge − A_edge) relative to the water H2O/H2 level for TiO2, WO3, CdS, ZnSe, GaAs, and GaP using the three-step method described above with a semilocal DFT functional (e.g., PBE).

Produce a JSON file `results.json` containing, for each material, the four component quantities:
- E_C_bulk_minus_H_semi_bulk (eV)
- A_bulk_minus_H_sol_bulk (eV)
- H_semi_edge_minus_H_sol_edge (eV)
- E_C_edge_minus_A_edge (eV), which must equal the algebraic combination of the three preceding terms.

The verifier will confirm that, for every material, the reported final value satisfies the algebraic relationship and will then compare each final value to the paper’s reference results. This is a standalone reproduction task; the training data and reference values come only from the instruction and the hidden checker, not from an external dataset.

## Assets

- Crystal structure parameters for TiO2 (rutile), WO3 (tetragonal), CdS (wurtzite), ZnSe (zincblende), GaAs (zincblende), GaP (zincblende)
- DFT code supporting PBE functional (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- Classical molecular dynamics code with TIP4P water model (e.g., LAMMPS): https://www.lammps.org
- PBE pseudopotentials for all elements (e.g., SSSP efficiency library): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Compute bulk semiconductor CBM positions
- Role: process
- Action: Using DFT with the PBE functional, optimize the crystal structures of TiO₂, WO₃, CdS, ZnSe, GaAs, and GaP (lattice parameters from provided table) and perform static calculations to obtain the CBM eigenvalue (lowest unoccupied state) and average Hartree potential for each material. Record the resulting E_C_bulk - H_semi_bulk values.
- Evidence: `/app/outputs/bulk_ec.json`

### Step 2: Generate liquid water configuration via classical MD
- Role: process
- Action: Run classical molecular dynamics (TIP4P water model) on a system of 128 H₂O molecules at 300 K (NVT ensemble, 100 ps). Extract a representative snapshot (e.g., at t=100 ps) for subsequent DFT calculations. Optionally verify that the DFT band gap (~3.8 eV at Γ-point) is consistent with published liquid water values.
- Evidence: `/app/outputs/water_snapshot.xyz`

### Step 3: Compute water acceptor term via H₃O⁺ insertion
- Role: process
- Action: Construct a 127H₂O + H₃O⁺ system by replacing one water molecule in the MD snapshot cell with a DFT‑relaxed H₃O⁺ ion. Perform DFT ionic relaxation on the H₃O⁺ within the liquid environment, then a static calculation to obtain the LUMO energy and average Hartree potential, yielding A_bulk - H_sol_bulk. Repeat for a few replacement positions; select the lowest total-energy configuration (expected around −0.70 eV). Record the chosen component data.
- Evidence: `/app/outputs/acceptor.json`

### Step 4: Construct semiconductor-water interface slabs and compute Hartree potential offset
- Role: process
- Action: For each semiconductor, build a slab model joining the semiconductor cell and the water cell. Perform DFT static calculations (Γ-point) to obtain planar-averaged Hartree potentials on both sides and compute the difference H_semi_edge - H_sol_edge. Ensure convergence of the offset with respect to slab thickness.
- Evidence: `/app/outputs/interface_offsets.json`

### Step 5: Compute CBM band edge positions relative to H₂O/H₂
- Role: scored (load-bearing)
- Action: For each semiconductor, compute the CBM edge position using the relation E_C_edge - A_edge = (E_C_bulk - H_semi_bulk) - (A_bulk - H_sol_bulk) + (H_semi_edge - H_sol_edge). Assemble all values into a JSON file containing an array of objects with keys: material, E_C_bulk_minus_H_semi_bulk, A_bulk_minus_H_sol_bulk, H_semi_edge_minus_H_sol_edge, E_C_edge_minus_A_edge.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of 6 objects; each object has string 'material', float 'E_C_bulk_minus_H_semi_bulk' (eV), float 'A_bulk_minus_H_sol_bulk' (eV), float 'H_semi_edge_minus_H_sol_edge' (eV), float 'E_C_edge_minus_A_edge' (eV).
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
- target_policy: exact_match
- description: Computed CBM band edge positions relative to water H2O/H2 level for six photocatalyst semiconductors.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `E_C_bulk_minus_H_semi_bulk`, `A_bulk_minus_H_sol_bulk`, `H_semi_edge_minus_H_sol_edge`, `E_C_edge_minus_A_edge`
    - `properties`:
      - `material`:
        - `type`: string
        - `description`: Semiconductor name (e.g., TiO2, WO3, CdS, ZnSe, GaAs, GaP).
      - `E_C_bulk_minus_H_semi_bulk`:
        - `type`: number
        - `units`: eV
        - `description`: CBM eigenvalue relative to average Hartree potential in the bulk semiconductor.
      - `A_bulk_minus_H_sol_bulk`:
        - `type`: number
        - `units`: eV
        - `description`: Water acceptor level (H3O+ LUMO) relative to average Hartree potential in bulk liquid water.
      - `H_semi_edge_minus_H_sol_edge`:
        - `type`: number
        - `units`: eV
        - `description`: Difference in average Hartree potentials between the semiconductor side and the water side at the interface.
      - `E_C_edge_minus_A_edge`:
        - `type`: number
        - `units`: eV
        - `description`: CBM band edge position relative to the H2O/H2 level; equals (E_C_bulk_minus_H_semi_bulk) - (A_bulk_minus_H_sol_bulk) + (H_semi_edge_minus_H_sol_edge).

Notes: The checker will verify that for each material the reported E_C_edge_minus_A_edge equals the algebraic combination of the three component fields (within a small numerical tolerance) and will then compare each final value to a hidden reference with an absolute tolerance of 0.2 eV. All six materials must be present.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "E_C_bulk_minus_H_semi_bulk",
            "A_bulk_minus_H_sol_bulk",
            "H_semi_edge_minus_H_sol_edge",
            "E_C_edge_minus_A_edge"
          ],
          "properties": {
            "material": {
              "type": "string",
              "description": "Semiconductor name (e.g., TiO2, WO3, CdS, ZnSe, GaAs, GaP)."
            },
            "E_C_bulk_minus_H_semi_bulk": {
              "type": "number",
              "units": "eV",
              "description": "CBM eigenvalue relative to average Hartree potential in the bulk semiconductor."
            },
            "A_bulk_minus_H_sol_bulk": {
              "type": "number",
              "units": "eV",
              "description": "Water acceptor level (H3O+ LUMO) relative to average Hartree potential in bulk liquid water."
            },
            "H_semi_edge_minus_H_sol_edge": {
              "type": "number",
              "units": "eV",
              "description": "Difference in average Hartree potentials between the semiconductor side and the water side at the interface."
            },
            "E_C_edge_minus_A_edge": {
              "type": "number",
              "units": "eV",
              "description": "CBM band edge position relative to the H2O/H2 level; equals (E_C_bulk_minus_H_semi_bulk) - (A_bulk_minus_H_sol_bulk) + (H_semi_edge_minus_H_sol_edge)."
            }
          }
        }
      },
      "description": "Computed CBM band edge positions relative to water H2O/H2 level for six photocatalyst semiconductors."
    }
  ],
  "notes": "The checker will verify that for each material the reported E_C_edge_minus_A_edge equals the algebraic combination of the three component fields (within a small numerical tolerance) and will then compare each final value to a hidden reference with an absolute tolerance of 0.2 eV. All six materials must be present."
}
```

## How you are scored
A hidden verifier reads your `results.json`. It performs two checks for each material:
1. **Internal consistency** – It verifies that the reported `E_C_edge_minus_A_edge` equals `E_C_bulk_minus_H_semi_bulk − A_bulk_minus_H_sol_bulk + H_semi_edge_minus_H_sol_edge` within a tight numerical tolerance. A failure here counts as an incorrect entry.
2. **Comparison to reference** – It compares your computed final value to a hidden reference (the paper’s reported result) using an absolute tolerance that accounts for the legitimate spread arising from different DFT implementations, pseudopotentials, and the irreproducible classical MD snapshots. The tolerance is chosen so that a correct re-run of the method with any reasonable open-source toolchain can meet it, while a random guess cannot.

Your score is the fraction of the six materials that pass both checks. All six entries must be present and valid.
