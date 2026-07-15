# DFT Study of Hydroxyl Coadsorption and the Water Formation Intermediate on Pt(111)

## Problem background
The low-temperature water formation reaction on platinum proceeds through a surface intermediate whose chemical identity has been debated. Experimental STM and vibrational spectroscopy indicate ordered overlayers with characteristic periodicities, but the stoichiometry and structure remain uncertain. This reproduction investigates the nature of those ordered phases using periodic density functional theory (DFT) calculations, focusing on the coadsorption of OH and H and the energetic preference between competing structural models.

## Approach
The approach uses plane-wave DFT calculations to model the Pt(111) surface within a √3×√3-R30° unit cell. A three-layer slab, frozen metal atoms, and a DFT-calculated lattice constant are employed. The workflow first constructs a high-coverage 2/3 ML OH reference phase. Then, starting from that reference, one additional hydrogen atom is placed at several plausible surface sites and full geometry relaxations are performed. Two competing local minima emerge: one where the added H remains on a bare Pt site (a simple OH+H coadsorption) and one where the added H converts one OH into H₂O, forming a mixed OH+H₂O network. The relative stability of these two geometries is quantified by the total energy difference. In addition, a finite-difference vibrational analysis of the mixed OH+H₂O phase is performed to obtain the normal-mode frequencies of key stretching, bending, and adsorbate–metal modes. These frequencies serve as an independent fingerprint of the surface species.

## Reproduction target
Compute the total energy difference ΔE between the OH+H coadsorption phase (structure (b)) and the mixed OH+H₂O phase (structure (c)) on Pt(111) in the √3×√3-R30° unit cell. Additionally, compute the vibrational frequencies of the mixed OH+H₂O phase for the following normal modes: OH stretch, three OH bending modes, Pt–OH stretch, and two translational modes (parallel and perpendicular to the surface). Report ΔE (in eV) and the set of frequencies (in cm⁻¹) with corresponding assignments.

## Assets

- Plane-wave DFT code supporting PW91 functional: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Pt, O, H (PW91): https://www.materialscloud.org/discover/sssp/table
- Pt bulk lattice constant

## Workflow steps

### Step 1: Prepare Pt(111) slab and 2/3 ML OH reference phase
- Role: process
- Action: Construct a three-layer Pt(111) slab with a √3×√3-R30° unit cell using a lattice constant of 3.9711 Å. Freeze the metal atoms. Place two OH groups per cell at top sites in a zigzag configuration to form the high-coverage OH network. Optimize the geometry with plane-wave DFT using the PW91 GGA functional and ultrasoft pseudopotentials, with a plane-wave kinetic energy cutoff of 300 eV, a 5×5×1 k‑point mesh, Fermi smearing of 0.1 eV, and vacuum >11 Å. Save the optimized geometry as the pure 2/3 ML OH phase.
- Evidence: `/app/outputs/oh_sqrt3_optimized.xyz`

### Step 2: OH+H coadsorption and structure search
- Role: process
- Action: Starting from the optimized 2/3 ML OH phase, add one H atom at each of the nine plausible adsorption sites suggested in the paper (e.g., top sites on bare Pt, bridging positions near OH). Perform full geometry relaxation for each initial placement using the same DFT settings. From the converged structures, identify the two distinct minima: structure (b) where the added H remains on a top site of the Pt not bound to OH, and structure (c) where the H is incorporated into the OH network, converting one OH into H2O (mixed OH+H2O phase). Save the optimized geometries of both minima.
- Evidence: `/app/outputs/structure_b.xyz, structure_c.xyz`

### Step 3: Compute ΔE between structures (b) and (c)
- Role: scored (load-bearing)
- Action: Extract the total energies of structure (b) and structure (c) from the DFT output. Compute ΔE = E(b) – E(c). Write a JSON file containing both absolute energies and the energy difference.
- Output file: `/app/outputs/step_01_energies.json`
- Format: json
- Contract: {"structure_b_total_energy": float (eV), "structure_c_total_energy": float (eV), "delta_E": float (eV)}
- Scoring: scored by hidden verifier

### Step 4: Vibrational analysis of mixed OH+H2O phase (c)
- Role: process
- Action: Take the optimized geometry of structure (c). Perform a numerical finite-difference vibrational calculation: displace each relevant atom by ±δ (e.g., 0.01 Å), compute forces, and construct the dynamical matrix. Diagonalize to obtain normal-mode frequencies. Include only the atoms of the adsorbed species (OH and H2O fragments); keep the Pt slab fixed. Use the same DFT parameters as before.
- Evidence: `/app/outputs/vibrations_raw.log`

### Step 5: Report key vibrational frequencies
- Role: scored (load-bearing)
- Action: From the computed spectrum, identify the normal modes corresponding to: OH stretch (ν(OH)), three OH bending modes (δ1–δ3), Pt–OH stretch (ν(Pt–OH)), and two translational modes (T∥ and T⊥). Report the frequency (cm⁻¹) and an assignment for each. Write the results as a JSON array.
- Output file: `/app/outputs/step_02_vibrations.json`
- Format: json
- Contract: [{"mode": "ν(OH)", "frequency": float, "assignment": "OH stretch"}, {"mode": "δ1(OH)", "frequency": float, "assignment": "bending mode 1"}, {"mode": "δ2(OH)", "frequency": float, "assignment": "bending mode 2"}, {"mode": "δ3(OH)", "frequency": float, "assignment": "bending mode 3"}, {"mode": "ν(Pt–OH)", "frequency": float, "assignment": "Pt-OH stretch"}, {"mode": "T∥(Pt–OH)", "frequency": float, "assignment": "translational parallel"}, {"mode": "T⊥(Pt–OH)", "frequency": float, "assignment": "translational perpendicular"}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energies.json`
- `/app/outputs/step_02_vibrations.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energies.json
- path: `/app/outputs/step_01_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energies of the coadsorbed OH+H structure (b) and the mixed OH+H2O structure (c) and their energy difference ΔE = E(b) – E(c). The key quantity is delta_E.
- schema:
  - `type`: object
  - `required`:
    - `structure_b_total_energy`: float (eV)
    - `structure_c_total_energy`: float (eV)
    - `delta_E`: float (eV)
  - `units`:
    - `structure_b_total_energy`: eV
    - `structure_c_total_energy`: eV
    - `delta_E`: eV

### step_02_vibrations.json
- path: `/app/outputs/step_02_vibrations.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Vibrational frequencies and mode assignments for the mixed OH+H2O phase. The reported modes must include the OH stretch, three bends, Pt-OH stretch, and two translational modes as listed.
- schema:
  - `type`: array
  - `items`:
    - `mode`: string
    - `frequency`: float (cm⁻¹)
    - `assignment`: string
  - `required_modes`: `ν(OH)`, `δ1(OH)`, `δ2(OH)`, `δ3(OH)`, `ν(Pt–OH)`, `T∥(Pt–OH)`, `T⊥(Pt–OH)`

Notes: The submitted delta_E and vibrational frequencies are compared to the experimental/calculated reference values from the paper within appropriate tolerances to account for differences in DFT implementation and pseudopotential choice.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "structure_b_total_energy": "float (eV)",
          "structure_c_total_energy": "float (eV)",
          "delta_E": "float (eV)"
        },
        "units": {
          "structure_b_total_energy": "eV",
          "structure_c_total_energy": "eV",
          "delta_E": "eV"
        }
      },
      "description": "Total energies of the coadsorbed OH+H structure (b) and the mixed OH+H2O structure (c) and their energy difference ΔE = E(b) – E(c). The key quantity is delta_E."
    },
    {
      "file": "step_02_vibrations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "mode": "string",
          "frequency": "float (cm⁻¹)",
          "assignment": "string"
        },
        "required_modes": [
          "ν(OH)",
          "δ1(OH)",
          "δ2(OH)",
          "δ3(OH)",
          "ν(Pt–OH)",
          "T∥(Pt–OH)",
          "T⊥(Pt–OH)"
        ]
      },
      "description": "Vibrational frequencies and mode assignments for the mixed OH+H2O phase. The reported modes must include the OH stretch, three bends, Pt-OH stretch, and two translational modes as listed."
    }
  ],
  "notes": "The submitted delta_E and vibrational frequencies are compared to the experimental/calculated reference values from the paper within appropriate tolerances to account for differences in DFT implementation and pseudopotential choice."
}
```

## How you are scored
A hidden verifier independently inspects the submitted JSON artifacts. For the energy difference step, the reported ΔE is compared to a hidden reference using an absolute tolerance; for the vibrational frequencies step, each reported mode frequency is compared to a hidden reference using a relative tolerance. Full credit is awarded if all values fall within the specified tolerances; partial credit is given for each correctly matched mode. The verifier does not recompute the DFT calculations – it relies on the numbers you submit in the output files.
