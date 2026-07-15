# Reproduction of Molecular Dipole Moment and Key Bond Topological Properties from Multipole Refinement of High-Resolution X-ray Data

## Problem background
The molecule N-o-vanillylidene-L-histidine (OVHIS) crystallizes as a double zwitterion: both carboxyl and phenol groups are deprotonated while the imine and imidazole nitrogen atoms are protonated. This creates a highly polarized structure in which four oxygen atoms carrying substantial negative charge lie on one side of the molecule and the positively charged imidazole ring lies on the opposite side. High-resolution, low-temperature single-crystal X-ray diffraction data have been collected for this compound. A multipole refinement of the experimental electron density allows direct calculation of the molecular dipole moment and a topological analysis of covalent and intermolecular bonding according to Bader's QTAIM. Reproducing these results requires obtaining the public diffraction data, performing a Hansen–Coppens multipole refinement, computing the dipole moment, and extracting QTAIM bond-critical-point properties for selected covalent and hydrogen bonds.

## Approach
Obtain the high-resolution X‑ray diffraction data (CCDC 764272) and perform a Hansen–Coppens multipole refinement with the open‑source XD2006 suite. The refinement models non‑hydrogen atoms up to the octupolar level and hydrogen atoms with axially symmetric quadrupoles, applying appropriate κ‑parameter constraints for chemically equivalent hydrogen atoms. From the refined electron density, compute the magnitude of the molecular dipole moment using the electrostatic property module. Use the same density for a QTAIM topological analysis with XDPROP (or an equivalent tool) to locate all bond critical points and evaluate the electron density (ρ), its Laplacian (∇²ρ), and the kinetic (G), potential (V), and total (H) energy densities at each point. Focus on two strong intermolecular charge‑assisted N–H···O hydrogen bonds and one representative covalent imine bond.

## Reproduction target
You must produce three outputs:

1. **R1 residual** – the final R1 of the aspherical atom refinement for reflections with I>3σ(I), written as a single floating‑point number to /app/outputs/step_00_refinement_R1.txt.
2. **Molecular dipole moment** – the magnitude (in Debye) computed from the refined multipole model, written as a single number to /app/outputs/step_01_dipole_moment.txt.
3. **Key bond topological parameters** – a JSON file at /app/outputs/step_02_topological_properties.json containing the QTAIM descriptors (rho, nabla2, G, V, H) for the bonds **N3-H3N...O2**, **N2-H2N...O4**, and **N1-C8**. The JSON must have exactly the structure: `{ "N3-H3N...O2": {"rho": ..., "nabla2": ..., "G": ..., "V": ..., "H": ...}, "N2-H2N...O4": {...}, "N1-C8": {...} }` with numeric values.

## Assets

- OVHIS high-resolution X-ray diffraction data (CCDC 764272): https://www.ccdc.cam.ac.uk/structures/search?accession=764272
- XD2006 multipole refinement program suite: https://xd.chem.uconn.edu/

## Workflow steps

### Step 1: Multipole Refinement (R1 quality)
- Role: scored
- Action: Obtain the high-resolution X-ray diffraction data for OVHIS from CCDC 764272 and perform a Hansen–Coppens multipole refinement using XD2006. Treat non‑hydrogen atoms at the octupolar level, hydrogen atoms with axially symmetric quadrupoles, and apply the H‑atom κ‑parameter grouping constraints described in the paper. Refine the model and write the final R1 value (for reflections with I>3σ(I)) to the output file.
- Output file: `/app/outputs/step_00_refinement_R1.txt`
- Format: txt
- Contract: A single floating-point number, e.g., 0.0116.
- Scoring: scored by hidden verifier

### Step 2: Molecular Dipole Moment
- Role: scored (load-bearing)
- Action: From the refined multipole electron density model, compute the molecular dipole moment magnitude (in Debye) using the electrostatic property module of XD2006 (or an equivalent open‑source tool). Write the value to the output file.
- Output file: `/app/outputs/step_01_dipole_moment.txt`
- Format: txt
- Contract: A single floating-point number representing the dipole moment in Debye.
- Scoring: scored by hidden verifier

### Step 3: QTAIM Topological Analysis
- Role: process
- Action: Perform a Bader QTAIM topological analysis on the experimental electron density using XDPROP (part of XD2006) or an equivalent program. Locate all bond critical points and compute the electron density ρ, its Laplacian ∇²ρ, and the kinetic (G), potential (V), and total (H) energy densities for every covalent and intermolecular bond.
- Evidence: `/app/outputs/qtaim_full_output.txt`

### Step 4: Key Bond Topological Parameters
- Role: scored (load-bearing)
- Action: From the QTAIM analysis, extract the topological parameters for these three bonds: N3-H3N...O2, N2-H2N...O4, and N1-C8. Write a JSON file with the bond identifiers as keys and an object containing rho (e/Å³), nabla2 (e/Å⁵), G, V, H (kJ mol⁻¹ per a.u. volume) as values.
- Output file: `/app/outputs/step_02_topological_properties.json`
- Format: json
- Contract: { "N3-H3N...O2": {"rho": <float>, "nabla2": <float>, "G": <float>, "V": <float>, "H": <float>}, "N2-H2N...O4": {...}, "N1-C8": {...} }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_00_refinement_R1.txt`
- `/app/outputs/step_01_dipole_moment.txt`
- `/app/outputs/step_02_topological_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_00_refinement_R1.txt
- path: `/app/outputs/step_00_refinement_R1.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The R1 residual of the aspherical atom refinement against I>3σ(I) reflections. A lower value is better.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the R1 residual.
  - `unit`: dimensionless

### step_01_dipole_moment.txt
- path: `/app/outputs/step_01_dipole_moment.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Magnitude of the molecular dipole moment computed from the experimental charge density.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the dipole moment magnitude.
  - `unit`: Debye

### step_02_topological_properties.json
- path: `/app/outputs/step_02_topological_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: QTAIM topological parameters for two strong charge‑assisted hydrogen bonds and one covalent imine bond.
- schema:
  - `type`: object
  - `required`: `N3-H3N...O2`, `N2-H2N...O4`, `N1-C8`
  - `additionalProperties`: False
  - `properties`:
    - `N3-H3N...O2`:
      - `type`: object
      - `required`: `rho`, `nabla2`, `G`, `V`, `H`
      - `properties`:
        - `rho`:
          - `type`: number
          - `unit`: e/Å³
        - `nabla2`:
          - `type`: number
          - `unit`: e/Å⁵
        - `G`:
          - `type`: number
          - `unit`: kJ mol⁻¹ per a.u. volume
        - `V`:
          - `type`: number
          - `unit`: kJ mol⁻¹ per a.u. volume
        - `H`:
          - `type`: number
          - `unit`: kJ mol⁻¹ per a.u. volume
    - `N2-H2N...O4`:
      - `$ref`: #/properties/N3-H3N...O2
    - `N1-C8`:
      - `$ref`: #/properties/N3-H3N...O2

Notes: The refinement R1 quality check ensures the underlying charge‑density model is properly reproduced, which is essential for the dipole moment and topological properties that follow. The checker compares the dipole moment and topological parameters to hidden paper‑reported values within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_00_refinement_R1.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the R1 residual.",
        "unit": "dimensionless"
      },
      "description": "The R1 residual of the aspherical atom refinement against I>3σ(I) reflections. A lower value is better."
    },
    {
      "file": "step_01_dipole_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the dipole moment magnitude.",
        "unit": "Debye"
      },
      "description": "Magnitude of the molecular dipole moment computed from the experimental charge density."
    },
    {
      "file": "step_02_topological_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "N3-H3N...O2",
          "N2-H2N...O4",
          "N1-C8"
        ],
        "additionalProperties": false,
        "properties": {
          "N3-H3N...O2": {
            "type": "object",
            "required": [
              "rho",
              "nabla2",
              "G",
              "V",
              "H"
            ],
            "properties": {
              "rho": {
                "type": "number",
                "unit": "e/Å³"
              },
              "nabla2": {
                "type": "number",
                "unit": "e/Å⁵"
              },
              "G": {
                "type": "number",
                "unit": "kJ mol⁻¹ per a.u. volume"
              },
              "V": {
                "type": "number",
                "unit": "kJ mol⁻¹ per a.u. volume"
              },
              "H": {
                "type": "number",
                "unit": "kJ mol⁻¹ per a.u. volume"
              }
            }
          },
          "N2-H2N...O4": {
            "$ref": "#/properties/N3-H3N...O2"
          },
          "N1-C8": {
            "$ref": "#/properties/N3-H3N...O2"
          }
        }
      },
      "description": "QTAIM topological parameters for two strong charge‑assisted hydrogen bonds and one covalent imine bond."
    }
  ],
  "notes": "The refinement R1 quality check ensures the underlying charge‑density model is properly reproduced, which is essential for the dipole moment and topological properties that follow. The checker compares the dipole moment and topological parameters to hidden paper‑reported values within appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores each of the three outputs. The R1 factor is checked against a required maximum quality threshold. The dipole moment is compared against an expected reference value and must lie within an allowed tolerance band. The JSON file is validated for correct schema (required keys, numeric types) and each topological parameter is compared against reference values, again within tolerances that account for legitimate methodological differences. The overall reward is a weighted combination of the individual scores, with the dipole moment and QTAIM parameters carrying the main weight.
