# Radical chain‑reaction of terminal‑unsaturated organic molecules on water‑saturated Si(100)-(2×1) — styrene case study

## Problem background
Functionalisation of semiconductor surfaces with organic molecules is important for molecular electronics and sensors.  
On hydrogen‑terminated Si(100)-(2×1), terminal unsaturated molecules can undergo radical chain‑reactions that form ordered nanostructures.  
When the silicon surface is water‑saturated, it carries both –H and –OH terminating groups; a key question is how the –OH groups affect chain propagation.  
While H‑abstraction from Si–H has been widely studied, the role of –OH is less clear: it might block propagation, or it might serve as a medium for radical transfer.

This task investigates the radical chain‑reaction of **styrene** on a water‑saturated Si(100)-(2×1) surface by computing adsorption energies and H‑/OH‑abstraction energy barriers using density functional theory (DFT).

## Approach
The water‑saturated Si(100)-(2×1) surface is modelled as a periodic slab with six Si layers and two Si‑Si dimer rows, terminated by –OH and –H groups in a **zigzag pattern**.  
A surface dangling bond is introduced by removing one hydrogen atom.  
The radical chain reaction of styrene is studied in two stages:
1. barrierless adsorption of styrene onto the dangling bond,
2. subsequent H‑atom or OH‑group abstraction from neighbouring surface groups by the β‑carbon radical of the adsorbed styrene.

Transition states for H‑abstraction from –OH groups along three directions (intradimer **r1**, interdimer **r2**, cross‑dimer‑row **r3**) and for direct interdimer OH‑abstraction (**r2‑OH**) are located and their energy barriers computed.

All calculations are performed with an open‑source DFT package (e.g. Quantum ESPRESSO or CP2K) using the Perdew–Burke–Ernzerhof (PBE) functional and Grimme D2 dispersion correction.

## Slab construction (crystallographic data and atomic coordinates)
You must build a slab model that reproduces the water‑saturated Si(100)-(2×1) surface with the zigzag OH/H pattern.

- Bulk silicon lattice constant: `a0 = 5.431 Å`.
- Surface primitive cell (1×1): `a_surf = a0 / √2 ≈ 3.84 Å`.
- Supercell for the (2×1) reconstructed surface with two dimer rows:
  - Lattice vector **a** = (3.84, 0, 0) Å  (along the dimer bond direction).
  - Lattice vector **b** = (0, 7.68, 0) Å  (across two dimer rows).
  - Lattice vector **c** = (0, 0, 25.0) Å  (vacuum layer of ~15 Å after slab).
- Number of Si layers: 6. The bottom 2 layers (and the passivating H atoms beneath them, if present) must be kept fixed during relaxation; all other atoms may relax.
- Dimer geometry: The topmost Si atoms form symmetric Si–Si dimers with bond length **2.30 Å**. The dimers are arranged in rows along the **a** direction; the distance between two neighbouring dimers along a row is 3.84 Å.
- Zigzag OH/H termination: Starting from the bare relaxed Si(100)-(2×1) surface, terminate the two surface Si atoms of each dimer with one –H and one –OH group in an alternating pattern that forms a zigzag arrangement.  
  In the 2‑row supercell (4 surface Si atoms), the following pattern can be used (indices can be assigned arbitrarily but must be consistent):
  - Dimer‑row 1: Si_1 → OH, Si_2 → H.
  - Dimer‑row 2: Si_3 → H, Si_4 → OH.
  Adjust the alternation so that OH and H alternate along both the dimer‑row direction and across rows.  
  Bond lengths: `d(Si–H) ≈ 1.48 Å`, `d(Si–O) ≈ 1.65 Å`, `d(O–H) ≈ 0.97 Å`. Si–O–H angle ≈ 110°.
- Dangling bond: Remove one terminal H atom from a Si–H group at a chosen position, leaving a Si radical centre. Ensure that the resulting configuration resembles the “zigzag pattern with a single dangling bond” shown in the reference figure (Figure 1, left panel in the literature).

*You may use a structure‑building tool (e.g. ASE, pymatgen or the DFT package’s own builder) and the parameters above to generate the initial slab. The exact internal coordinates can be obtained by relaxing the structure; the values given here are sufficient to set up the model.*

## DFT calculation parameters
- Functional: Perdew–Burke–Ernzerhof (PBE).
- Dispersion correction: Grimme D2 (DFT‑D2).
- Plane‑wave cut‑off (if using Quantum ESPRESSO): `ecutwfc = 40 Ry`, `ecutrho = 320 Ry`. For CP2K use the equivalent DZVP‑MOLOPT‑SR‑GTH basis set.
- Pseudopotentials: Use standard, well‑tested pseudopotentials (e.g. SSSP PBE precision 1.1 for Si, C, H, O) or Goedecker‑Teter‑Hutter (GTH) pseudopotentials with corresponding GTH basis sets.
- k‑point grid: 2×2×1 Monkhorst–Pack mesh for the supercell.
- Spin: Unrestricted (open‑shell systems).
- Geometry convergence: Forces < 0.03 eV/Å, energy convergence < 1e‑5 eV.
- Transition‑state search: Use the climbing‑image nudged elastic band (CI‑NEB) method or the dimer method, as implemented in the chosen code. Verify true transition states by a single imaginary frequency.

## Reproduction target
Using the slab model and DFT settings described above, perform the following for **styrene** on the zigzag‑patterned water‑saturated Si(100)-(2×1) slab with a surface dangling bond:
- (a) compute the adsorption energy of styrene (positive value of released energy, in eV);
- (b) compute the energy barriers for H‑abstraction from a surface –OH group along the intradimer (r1), interdimer (r2), and cross‑dimer‑row (r3) directions;
- (c) compute the energy barrier for direct –OH abstraction along the interdimer direction.

Collect all results in the CSV file `/app/outputs/barriers.csv` with columns `step`, `molecule`, `energy_value`, `energy_type` as specified in the output contract. A hidden verifier will audit the structural consistency of the results.

## Assets
- Open‑source DFT package (e.g. Quantum ESPRESSO or CP2K): https://www.quantum‑espresso.org or https://www.cp2k.org
- PBE functional and Grimme D2 dispersion correction (included in the package).

## Workflow steps

### Step 1: Build and optimise the Si(100)-(2×1) slab with zigzag OH/H termination and a dangling bond
- Role: process
- Action: Construct the periodic slab according to the crystallographic data given above. Relax all atomic positions (except the fixed bottom layers) using DFT with the PBE+D2 settings. Ensure the geometry converges to the forces threshold.

### Step 2: Compute adsorption energy and H‑abstraction/OH‑abstraction barriers for styrene
- Role: scored (load‑bearing)
- Action: Using the optimised slab, perform DFT (PBE+D2) to:
  - (a) place a styrene molecule near the surface dangling bond and perform a full relaxation; record the energy difference between the relaxed adsorbed state and the separated slab + styrene as the **adsorption energy** (positive released energy).
  - (b) locate the transition states for H‑abstraction from a surface –OH group along the intradimer (r1), interdimer (r2), and cross‑dimer‑row (r3) directions.
  - (c) locate the transition state for direct –OH abstraction along the interdimer direction.
- Output file: `/app/outputs/barriers.csv`
- Format: csv
- Contract: CSV with columns: `step` (text: `adsorption`, `r1_Habstraction`, `r2_Habstraction`, `r3_Habstraction`, `r2_OHabstraction`), `molecule` (text: always `styrene`), `energy_value` (float, in eV), `energy_type` (text: `adsorption` or `barrier`).
- Scoring: scored by hidden verifier

## Output files
Write all scored artefacts under `/app/outputs`:
- `/app/outputs/barriers.csv`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers.csv
- path: `/app/outputs/barriers.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Activation barriers and adsorption energy for styrene on water‑saturated Si(100)-(2×1) zigzag surface. Contains only the five required rows: adsorption, r1_Habstraction, r2_Habstraction, r3_Habstraction, r2_OHabstraction.
- schema:
  - `type`: table
  - `required_columns`: `step`, `molecule`, `energy_value`, `energy_type`
  - `units`:
    - `energy_value`: eV

## Self‑check before finishing (optional, not scored)
A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "molecule",
          "energy_value",
          "energy_type"
        ],
        "units": {
          "energy_value": "eV"
        }
      },
      "description": "Activation barriers and adsorption energy for styrene on water‑saturated Si(100)-(2×1) zigzag surface. Contains only the five required rows: adsorption, r1_Habstraction, r2_Habstraction, r3_Habstraction, r2_OHabstraction."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads `/app/outputs/barriers.csv` and performs a structural audit that checks certain qualitative relationships among the energy values (such as relative orderings) and whether the adsorption energy falls within a plausible range. The exact rules are not disclosed. It returns a reward of 1.0 if all conditions are satisfied, 0.0 otherwise. Reporting numbers from the paper without real DFT calculations will not pass.