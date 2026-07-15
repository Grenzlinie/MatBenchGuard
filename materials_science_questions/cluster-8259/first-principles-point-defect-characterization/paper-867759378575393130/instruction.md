# Structural and electronic properties of Stone-Wales defective antimonene nanotubes from first principles

## Problem background
Antimonene, a two-dimensional monolayer of antimony, can form one-dimensional nanotubes with distinct electronic properties. Stone-Wales (SW) defects — created by rotating a central Sb–Sb bond by 90°, converting four adjacent hexagons into a 5-7-7-5 ring pattern — are topological defects expected to alter the structural stability and electronic structure of these nanotubes. Understanding how SW defects affect bond-length distributions, formation energies, and band gaps is essential for designing nanoelectronic devices based on antimonene nanotubes. This reproduction task addresses the computation of structural geometries and electronic properties of six antimonene nanotube configurations: pristine zigzag (ZbNT) and armchair (ASbNT) nanotubes, and two distinct Stone-Wales defective variants for each chirality (SW1-ZbNT, SW2-ZbNT, SW1-ASbNT, SW2-ASbNT).

## Approach
The computational approach is based on first-principles density functional theory (DFT) using the generalized gradient approximation of Perdew–Burke–Ernzerhof (PBE). The workflow proceeds as follows:
1. **Model Construction** – Using the Atomic Simulation Environment (ASE), build atomic coordinates for the six antimonene nanotubes. The ideal zigzag and armchair nanotubes have specified diameters and supercell lengths. Stone-Wales defects are introduced by selecting a central Sb–Sb bond and rotating it by 90°, which produces the characteristic 5-7-7-5 topology. Two orientations are considered for each chirality, corresponding to whether the rotated bond is oriented approximately perpendicular or oblique relative to the tube axis.
2. **Geometry Optimization** – Perform full relaxation of each structure with Quantum ESPRESSO (pw.x) and PBE pseudopotentials from the SSSP efficiency library. The relaxation converges forces and total energy to tight criteria, yielding equilibrium bond lengths, total energies, and the final tube dimensions.
3. **Band Structure Calculation** – For each relaxed geometry, carry out a static DFT calculation to obtain the electronic band structure along a high-symmetry k‑path. The band gap is extracted as the energy difference between the valence band maximum (VBM) and conduction band minimum (CBM).
4. **Data Compilation** – From the relaxed geometries, measure the minimum and maximum Sb–Sb bond distances (d_Sb‑Sb). For defective structures, compute the orientation angle of the central rotated bond relative to the axial direction. Calculate formation energies as Ef = Edefect_total − Eperfect_total. Gather all results (including diameter, tube length, bond-length ranges, orientation angles, formation energies, and band gaps) for each of the six configurations.

## Reproduction target
Produce a single JSON file, antimonene_sw_data.json, containing, for each of the six nanotube configurations, the following computed properties:
• name (string identifying the configuration)
• diameter_ang (Å)
• tube_length_ang (Å)
• d_Sb_Sb_min_ang (Å) – minimum Sb–Sb bond distance
• d_Sb_Sb_max_ang (Å) – maximum Sb–Sb bond distance
• orientation_angle_deg (degrees; 0 for pristine nanotubes)
• formation_energy_eV (eV; 0 for pristine nanotubes)
• band_gap_eV (eV)
All numerical fields must be reported to three decimal places. The output serves as the sole scored artifact; a hidden verifier will compare your computed numbers against reference values and assess the internal consistency of the results. No intermediate files need to be submitted for scoring, but they document your workflow.

## Assets

- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/
- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build initial atomic models
- Role: process
- Action: Construct atomic coordinates for the six nanotube systems: pristine zigzag (ZbNT), pristine armchair (ASbNT), and their two Stone-Wales defective variants each (SW1-ZbNT, SW2-ZbNT, SW1-ASbNT, SW2-ASbNT). Use ASE to create ideal nanotubes with appropriate diameters (~17.742 Å for zigzag, ~15.579 Å for armchair) and supercell lengths (~19.031 Å and ~14.420 Å). For defective structures, rotate a central Sb–Sb bond by 90° to introduce the Stone-Wales (5-7-7-5) defect.
- Evidence: `/app/outputs/initial_structures.tar.gz`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform full geometry relaxation for all six structures using Quantum ESPRESSO (pw.x) with the PBE functional and SSSP efficiency pseudopotentials for Sb. Converge forces and total energy to tight criteria. Save relaxed coordinates and total energies.
- Evidence: `/app/outputs/relaxation_logs.tar.gz`

### Step 3: DFT band structure calculation
- Role: process
- Action: For each optimized structure, perform a static DFT calculation on the relaxed coordinates to compute the band structure along an appropriate high-symmetry k‑path. Extract the band gap (difference between VBM and CBM) for each system.
- Evidence: `/app/outputs/band_data.tar.gz`

### Step 4: Compile structural and electronic data
- Role: scored (load-bearing)
- Action: From the relaxed geometries, measure the minimum and maximum Sb–Sb bond distances for each structure. For SW-defective structures, compute the orientation angle of the central rotated bond relative to the tube axis. Calculate formation energies as E_defect_total - E_perfect_total. Insert all values (name, diameter, tube length, bond-length range, orientation angle, formation energy, band gap) into a single JSON file.
- Output file: `/app/outputs/antimonene_sw_data.json`
- Format: json
- Contract: JSON object with key 'structures' whose value is an array of 6 objects, each with: name (str), diameter_ang (float), tube_length_ang (float), d_Sb_Sb_min_ang (float), d_Sb_Sb_max_ang (float), orientation_angle_deg (float, 0 for perfect), formation_energy_eV (float, 0 for perfect), band_gap_eV (float). All numeric fields reported to 3 decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/antimonene_sw_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### antimonene_sw_data.json
- path: `/app/outputs/antimonene_sw_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the reproduced structural and electronic parameters for the six antimonene nanotube configurations. The checker compares each numeric field to hidden paper reference values within tolerances and verifies trend constraints (formation energy ordering, band gap reduction).
- schema:
  - `type`: object
  - `required`:
    - `structures`: array of 6 structure objects
  - `items`:
    - `name`: string
    - `diameter_ang`: float (Å)
    - `tube_length_ang`: float (Å)
    - `d_Sb_Sb_min_ang`: float (Å)
    - `d_Sb_Sb_max_ang`: float (Å)
    - `orientation_angle_deg`: float (degrees, 0 for pristine)
    - `formation_energy_eV`: float (eV, 0 for pristine)
    - `band_gap_eV`: float (eV)

Notes: All numeric fields must be reported to three decimal places. Orientation angle and formation energy are zero for pristine nanotubes. The checker validates structure completeness, numeric precision, and consistency with expected physical trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "antimonene_sw_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "structures": "array of 6 structure objects"
        },
        "items": {
          "name": "string",
          "diameter_ang": "float (Å)",
          "tube_length_ang": "float (Å)",
          "d_Sb_Sb_min_ang": "float (Å)",
          "d_Sb_Sb_max_ang": "float (Å)",
          "orientation_angle_deg": "float (degrees, 0 for pristine)",
          "formation_energy_eV": "float (eV, 0 for pristine)",
          "band_gap_eV": "float (eV)"
        }
      },
      "description": "Scored artifact containing the reproduced structural and electronic parameters for the six antimonene nanotube configurations. The checker compares each numeric field to hidden paper reference values within tolerances and verifies trend constraints (formation energy ordering, band gap reduction)."
    }
  ],
  "notes": "All numeric fields must be reported to three decimal places. Orientation angle and formation energy are zero for pristine nanotubes. The checker validates structure completeness, numeric precision, and consistency with expected physical trends."
}
```

## How you are scored
A hidden verifier reads the antimonene_sw_data.json file. It checks that:
- The file contains exactly six structure entries with the required fields.
- Each numeric field (diameter, tube length, bond-length min/max, orientation angle, formation energy, band gap) falls within an expected range relative to reference values.
- Key physical trends are satisfied, such as the relative ordering of formation energies among the two defective orientations for each chirality, and the shift in band gap between pristine and defective nanotubes.
The verifier assigns a weighted score; band gap and formation energy values carry higher weight because they directly reflect the electronic and energetic impact of the Stone-Wales defects. Reporting paper-derived numbers without executing the DFT pipeline will not receive full credit because the verifier also validates the internal consistency and trend relationships.
