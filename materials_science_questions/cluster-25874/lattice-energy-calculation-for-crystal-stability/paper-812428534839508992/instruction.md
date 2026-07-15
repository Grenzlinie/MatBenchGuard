# Partial Charge and Madelung Energy Calculation for MIL-50 Open-Framework Gallium Phosphate

## Problem background
MIL-50 is an open-framework gallium phosphate (GaPO) with 18-ring and 6-ring channels, composed of hexameric Ga3P3 building units. The channels contain 1,6-diaminohexane, water molecules, and rubidium cations. Single-crystal XRD reveals a framework in space group Cmc2₁, but the water sites exhibit fractional occupancy, suggesting disordered water within the 18-ring pores. Double-quantum ³¹P NMR hints that one phosphorus site (P3) may be split into two distinct environments, while other phosphorus sites appear unsplit. This raises the question: does the water sublattice possess a periodic lower-symmetry pattern that breaks the effective point-group symmetry of the crystal in a way that induces a detectable charge asymmetry only on the P3 site? The computational target is to resolve the water topology, optimize the hydrogen positions, and compute the partial charges and Madelung energy to determine whether such a charge split emerges.

## Approach
We use the non‑empirical PACHA (Partial Atomic Charges via Hard‑Sphere Approximation) model to assign partial charges at each geometry and to evaluate the Madelung lattice energy. The overall approach combines four elements:

1. **Structural model construction** – Transform the published CIF of MIL-50 from the C‑centered cell to a primitive cell (pmc2₁ setting) and apply symmetry masks to the water oxygen sites (O1W, O3W, O4W, O5W) that originally had fractional occupancy. The masks restrict the symmetry operations applied to each water sublattice, eliminating unrealistically short O···O contacts and achieving full occupancy while preserving stoichiometric neutrality.

2. **Hydrogen placement** – Missing hydrogen atoms on water molecules, hydroxyl groups, and ammonium groups are added using standard bond lengths (O‑H 0.97 Å, N‑H 1.05 Å) and idealized bond angles (H‑O‑H 105°, tetrahedral around N). Adjustable dihedral angles define the degrees of freedom for the subsequent optimization.

3. **Geometry optimization** – The hydrogen positions are refined by a downhill simplex minimization of the Madelung lattice energy, computed at each iteration using the PACHA charge model. The atomic parameters for the PACHA method (electronegativities and 1s/2s/3p/5s orbital radii for H, C, N, O, F, P, Ga, Rb) are provided in the workflow description.

4. **Analysis** – The final optimized geometry is used to compute (i) the final Madelung lattice energy and (ii) the PACHA partial charges of all phosphorus atoms. The phosphorus charges are grouped by crystallographic site (P1–P5) and their symmetry‑related copies in the primitive cell. The charge values reveal whether the P3 site experiences a detectable asymmetry compared to the other phosphorus sites, thereby testing the influence of the water sublattice symmetry.

## Reproduction target
Produce the following two artifacts from the fully optimized primitive‑cell geometry:

- **Madelung energy** ( `madelung_energy.txt` ) — a single floating‑point number representing the final Madelung lattice energy in kJ/mol, obtained after hydrogen optimization with the PACHA model.
- **Phosphorus partial charges** ( `phosphorus_charges.json` ) — a JSON object mapping each phosphorus site label (P1, P2, P3, P4, P5) to an array of partial charge values for all symmetry‑related copies in the pmc2₁ cell (P1–P4 have four copies; P5 has two copies). The arrays should allow an assessment of whether the P3 site shows a charge split while the other phosphorus sites remain essentially uniform.

The hidden verifier will automatically evaluate these outputs; the task is to run the full computational pipeline and report the numbers that the procedure yields – no external lookup or paper‑matching is required.

## Assets

- MIL-50 Single-Crystal CIF File: https://pubs.acs.org/doi/suppl/10.1021/ja029072b

## Workflow steps

### Step 1: Build initial structural model and optimize hydrogen positions with PACHA Madelung minimization
- Role: process
- Action: Construct the primitive unit cell from the published CIF, apply symmetry masks to water oxygen sites (O1W, O3W, O4W, O5W) to achieve full occupancy, add missing hydrogen atoms to water, hydroxyl, and ammonium groups using standard bond lengths and angles, and perform a simplex minimization of the Madelung lattice energy using the non‑empirical PACHA partial charge model. Save the final optimized geometry as a CIF file.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 2: Report final Madelung energy
- Role: scored (load-bearing)
- Action: Extract the Madelung lattice energy from the final optimized structure and write it to madelung_energy.txt as a single floating‑point number in kJ/mol.
- Output file: `/app/outputs/madelung_energy.txt`
- Format: txt
- Contract: A single floating-point number representing the final Madelung lattice energy in kJ/mol.
- Scoring: scored by hidden verifier

### Step 3: Report phosphorus partial charges
- Role: scored
- Action: Compute the PACHA partial charges for all phosphorus atoms from the final optimized structure and write them to phosphorus_charges.json as a JSON object mapping each P-site label (P1, P2, P3, P4, P5) to an array of partial charge values for all symmetry‑related copies (4 values for P1–P4, 2 for P5).
- Output file: `/app/outputs/phosphorus_charges.json`
- Format: json
- Contract: JSON object mapping P-site label to an array of partial charge values (e.g., 'P1': [0.534, 0.534, 0.534, 0.534], ...).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/madelung_energy.txt`
- `/app/outputs/phosphorus_charges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### madelung_energy.txt
- path: `/app/outputs/madelung_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Final Madelung lattice energy computed via the PACHA method after hydrogen optimization.
- schema:
  - `type`: text
  - `description`: A single floating-point number in kJ/mol

### phosphorus_charges.json
- path: `/app/outputs/phosphorus_charges.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Partial charges of phosphorus atoms showing the symmetry lowering of the P3 site.
- schema:
  - `type`: object
  - `description`: JSON object with top-level keys P1, P2, P3, P4, P5; each value is an array of partial charge floats (number of entries matches site multiplicity in the pmc2_1 cell).

Notes: All outputs are produced from the final optimized primitive-cell geometry. The Madelung energy is checked against a hidden paper reference with tolerance; the phosphorus charges are verified for the expected P3 charge asymmetry and uniformity of other P sites.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "madelung_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number in kJ/mol"
      },
      "description": "Final Madelung lattice energy computed via the PACHA method after hydrogen optimization."
    },
    {
      "file": "phosphorus_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "description": "JSON object with top-level keys P1, P2, P3, P4, P5; each value is an array of partial charge floats (number of entries matches site multiplicity in the pmc2_1 cell)."
      },
      "description": "Partial charges of phosphorus atoms showing the symmetry lowering of the P3 site."
    }
  ],
  "notes": "All outputs are produced from the final optimized primitive-cell geometry. The Madelung energy is checked against a hidden paper reference with tolerance; the phosphorus charges are verified for the expected P3 charge asymmetry and uniformity of other P sites."
}
```

## How you are scored
A hidden verifier independently scores each scored workflow stage.

- The **Madelung energy** is checked for consistency with the PACHA method; the verifier compares your computed value against a reference that reflects a correct execution of the hydrogen‑optimization protocol.
- The **phosphorus partial charges** are audited for structural properties: the verifier examines whether the P3 site entries exhibit a clear charge asymmetry and whether all other P‑sites (P1, P2, P4, P5) show a high degree of internal uniformity across their symmetry copies.

Each stage carries a fraction of the total score, and the final reward is a weighted combination. The scoring is designed so that an honest implementation of the described method produces a high score; simply writing guessed numbers is unlikely to satisfy the structural audit. Do **not** attempt to hardcode expected values – run the pipeline and report what it produces.
