# DFT cluster model for clean corundum surface relaxation and CO chemisorption

## Problem background
Understanding the relaxation of the clean α‑Al₂O₃(0001) surface and its interaction with small probe molecules such as CO is important for catalysis and surface science. Small cluster models terminated with saturators have been proposed as computationally efficient alternatives to periodic slab calculations. The central question is whether such a cluster can capture the quantitative structural relaxation, electronic changes, and chemisorption energetics and vibrational signatures that larger‑scale methods predict. This task evaluates that model by requiring computation of specific surface relaxation and CO adsorption properties.

## Approach
The experiment constructs a stoichiometric Al₈O₁₂ cluster from the corundum bulk structure by extracting the (0001)‑terminated slab fragment. Dangling bonds are passivated with fractional‑charge pseudo‑hydrogen saturators: H′ (Z=1.5) on Al and H″ (Z=0.5) on O, while the three H″ on O_II are replaced with ordinary hydrogen to maintain charge neutrality. Density functional theory with a generalized gradient approximation (GGA) is used to optimize the clean surface; only the topmost surface Al and O atoms (not directly bonded to saturators) are relaxed. From the relaxed clean cluster the following quantities are obtained: the inward displacement of the surface Al atom, the first‑to‑second layer spacing, the Al–O bond length, the surface relaxation energy (difference between relaxed and unrelaxed total energies), and the shift of the lowest unoccupied molecular orbital (LUMO). Then CO is adsorbed atop the surface Al site in a C‑down orientation. The positions of CO, the surface Al, and the neighbouring surface O atoms are re‑optimized, and basis set superposition error (BSSE) corrected adsorption enthalpy, the C–O bond length, and the harmonic C–O stretching frequency are computed. All calculations are performed with a GGA functional (e.g., BP or PBE) and appropriate basis sets for the atoms involved.

## Reproduction target
Your task is to produce and report: (1) the relaxed atomic coordinates of the clean Al₈O₁₂ cluster (clean_relaxed.xyz), (2) a JSON file (clean_energies.json) containing the total energies and LUMO energies of the unrelaxed and relaxed cluster together with the surface area used for energy‑density conversion, (3) the optimized geometry of CO adsorbed C‑down on the same cluster (co_adsorbed_C_down.xyz), and (4) a JSON file (adsorption_results.json) with the BSSE‑corrected adsorption enthalpy, C–O bond length, and C–O stretching frequency. All results originate from DFT geometry optimisations; no pre‑existing input files beyond the crystal structure data are needed. The computations must be carried out using a GGA functional and the basis‑set strategy described in the instructions.

## Assets

- CP2K (open-source DFT code): https://www.cp2k.org/
- Bulk α-Al2O3 crystal structure parameters
- Pseudopotentials and basis sets for CP2K: GTH-PBE pseudopotentials + DZVP-MOLOPT basis sets (included with CP2K)

## Workflow steps

### Step 1: Build saturated Al8O12 cluster model
- Role: process
- Action: Construct the stoichiometric Al8O12 cluster from the bulk corundum structure by extracting the (0001)-terminated slab fragment. Attach pseudo-hydrogen saturators H' (Z=1.5) to Al dangling bonds and H'' (Z=0.5) to O dangling bonds, then replace the three H'' on O_II atoms with ordinary hydrogen (Z=1). Write the initial unrelaxed geometry to unrelaxed.xyz.
- Evidence: `/app/outputs/unrelaxed.xyz`

### Step 2: Clean surface relaxation and geometry
- Role: scored (load-bearing)
- Action: Using DFT with a GGA functional (e.g., BP or PBE) and a triple-zeta basis for Al/O, double-zeta for H, relax the positions of the surface atoms Al_I and O_I (those not directly bonded to saturators) while keeping saturator positions fixed. Output the final relaxed geometry.
- Output file: `/app/outputs/clean_relaxed.xyz`
- Format: other
- Contract: Standard XYZ format: number of atoms on first line, comment line, then lines with element symbol and x y z coordinates in Angstrom.
- Scoring: scored by hidden verifier

### Step 3: Clean surface electronic energies
- Role: scored
- Action: Perform single-point calculations on the unrelaxed and relaxed clean clusters to obtain total energies and LUMO energies. Write a JSON file containing these values and the fixed surface area used for energy density conversion.
- Output file: `/app/outputs/clean_energies.json`
- Format: json
- Contract: {"unrelaxed_total_energy": "float (Hartree)", "relaxed_total_energy": "float (Hartree)", "unrelaxed_LUMO_energy": "float (eV)", "relaxed_LUMO_energy": "float (eV)", "surface_area_A2": 19.55}
- Scoring: scored by hidden verifier

### Step 4: CO adsorption geometry optimization
- Role: scored (load-bearing)
- Action: Starting from the relaxed clean cluster, place a CO molecule above the Al_I surface atom in a C-down orientation. Perform a geometry optimization of the CO molecule, Al_I, and O_I atoms. Include basis set superposition error (BSSE) correction using ghost-fragment calculations. Output the final geometry.
- Output file: `/app/outputs/co_adsorbed_C_down.xyz`
- Format: other
- Contract: Standard XYZ format.
- Scoring: scored by hidden verifier

### Step 5: CO adsorption properties report
- Role: scored
- Action: Compute the BSSE-corrected adsorption enthalpy, C-O bond length, and harmonic C-O stretching frequency from the optimized CO-adsorbed cluster. Write these quantities to a JSON file.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: {"adsorption_enthalpy_kcal_per_mol": "float (with BSSE correction)", "C_O_bond_length_A": "float", "C_O_stretching_frequency_cm-1": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/clean_relaxed.xyz`
- `/app/outputs/clean_energies.json`
- `/app/outputs/co_adsorbed_C_down.xyz`
- `/app/outputs/adsorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### clean_relaxed.xyz
- path: `/app/outputs/clean_relaxed.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Relaxed geometry of the clean Al8O12 cluster. Used to verify surface relaxation displacements and bond lengths.
- schema:
  - `type`: text
  - `description`: XYZ format with atom symbols and coordinates. The checker will parse lines and compute structural parameters.

### clean_energies.json
- path: `/app/outputs/clean_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy values from single-point calculations. The checker recomputes relaxation energy and LUMO destabilization.
- schema:
  - `type`: object
  - `required`:
    - `unrelaxed_total_energy`: float (Hartree)
    - `relaxed_total_energy`: float (Hartree)
    - `unrelaxed_LUMO_energy`: float (eV)
    - `relaxed_LUMO_energy`: float (eV)
    - `surface_area_A2`: float (Å²)

### co_adsorbed_C_down.xyz
- path: `/app/outputs/co_adsorbed_C_down.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Optimized geometry of CO adsorbed C-down on the cluster.
- schema:
  - `type`: text
  - `description`: XYZ format of CO-adsorbed cluster. Used to verify the C-O bond length and geometry.

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reported adsorption properties: enthalpy, bond length, and vibrational frequency. Checker compares these to reference values.
- schema:
  - `type`: object
  - `required`:
    - `adsorption_enthalpy_kcal_per_mol`: float
    - `C_O_bond_length_A`: float
    - `C_O_stretching_frequency_cm-1`: float

Notes: The checker will recompute structural parameters (displacements, d spacing, bond lengths) from the XYZ geometry files using known bulk reference positions. Energies and LUMO shift are recomputed from clean_energies.json. Adsorption properties are compared against reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "clean_relaxed.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ format with atom symbols and coordinates. The checker will parse lines and compute structural parameters."
      },
      "description": "Relaxed geometry of the clean Al8O12 cluster. Used to verify surface relaxation displacements and bond lengths."
    },
    {
      "file": "clean_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "unrelaxed_total_energy": "float (Hartree)",
          "relaxed_total_energy": "float (Hartree)",
          "unrelaxed_LUMO_energy": "float (eV)",
          "relaxed_LUMO_energy": "float (eV)",
          "surface_area_A2": "float (Å²)"
        }
      },
      "description": "Energy values from single-point calculations. The checker recomputes relaxation energy and LUMO destabilization."
    },
    {
      "file": "co_adsorbed_C_down.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ format of CO-adsorbed cluster. Used to verify the C-O bond length and geometry."
      },
      "description": "Optimized geometry of CO adsorbed C-down on the cluster."
    },
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "adsorption_enthalpy_kcal_per_mol": "float",
          "C_O_bond_length_A": "float",
          "C_O_stretching_frequency_cm-1": "float"
        }
      },
      "description": "Reported adsorption properties: enthalpy, bond length, and vibrational frequency. Checker compares these to reference values."
    }
  ],
  "notes": "The checker will recompute structural parameters (displacements, d spacing, bond lengths) from the XYZ geometry files using known bulk reference positions. Energies and LUMO shift are recomputed from clean_energies.json. Adsorption properties are compared against reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact. It extracts structural parameters (Al_I displacement, interlayer spacing d, Al_I–O_I bond length) from clean_relaxed.xyz, recomputes the relaxation energy and LUMO shift from clean_energies.json, and reads the adsorption enthalpy, C–O bond length, and C–O stretching frequency from adsorption_results.json. Each quantity is compared against a hidden reference, with credit given only when the computed values lie within tolerances that account for legitimate differences in computational setup. The final reward is a weighted combination of the clean‑surface and CO‑adsorption stages: the adsorption properties carry the larger share. Reporting a number without the correct underlying geometry or energy data yields no credit; fidelity to the described protocol is essential.
