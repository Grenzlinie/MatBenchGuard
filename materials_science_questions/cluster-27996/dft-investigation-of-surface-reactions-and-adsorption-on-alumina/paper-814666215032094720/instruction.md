# DFT and QM/MM Study of n-Octylphosphonic Acid Adsorption on Al and Al(OH)3 Surfaces

## Problem background
Aqueous aluminum-air batteries suffer from severe parasitic hydrogen evolution on the aluminum anode in alkaline electrolytes, which reduces available capacity and causes early cell failure. One strategy to suppress this unwanted side reaction is to introduce an organic additive that can anchor to the aluminum surface and to the intermediate discharge product Al(OH)₃, forming a protective film that blocks water from reaching the metal. n-Octylphosphonic acid (OPA) has been proposed as such an additive; its deprotonated form (R–PO₃²⁻) is thought to chemisorb on metallic Al and hydrogen-bond to Al(OH)₃. Understanding the adsorption geometry and interaction strengths is key to evaluating the additive's mechanism. This task aims to compute the equilibrium geometries and characteristic bond distances for OPA on two surfaces: Al(022) and Al(OH)₃(001).

## Approach
The approach uses first-principles and hybrid QM/MM simulations to obtain the optimized adsorption configurations. For the metallic Al surface, a periodic slab model of the Al(022) facet is built from bulk FCC aluminum, and the deprotonated OPA molecule is placed on it. A density functional theory (DFT) geometry optimization is performed with the GGA-PBE functional to minimize forces; the two Al–O bonds formed between the phosphate group and surface Al atoms are extracted. For the Al(OH)₃(001) surface, a slab is built from the gibbsite crystal structure. Because non-covalent interactions dominate, a quantum-mechanics/molecular-mechanics (QM/MM) scheme is employed: the OPA molecule and nearby surface groups are treated with DFT (PBE), while the rest of the surface and solvent environment are described by the Dreiding force field. After optimization, the shortest O···HO distance between an OPA oxygen and a surface hydroxyl hydrogen is identified. Both calculations capture the structural anchoring motifs that, in the original study, were linked to corrosion inhibition.

## Reproduction target
Carry out the following two independent calculations and report the results in the specified JSON files:

1. **DFT adsorption geometry on Al(022)**: Optimize the structure of a deprotonated OPA molecule on a periodic Al(022) slab. From the final optimized geometry, extract the two Al–O bond distances (in Å) and the atomic coordinates in XYZ format. Write the results to `dft_adsorption_geometry.json`.

2. **QM/MM hydrogen bond geometry on Al(OH)₃(001)**: Optimize the structure of OPA on a gibbsite Al(OH)₃(001) slab using the QM/MM protocol described. From the final optimized geometry, extract the shortest O···HO distance (in Å) and the atomic coordinates in XYZ format. Write the results to `qmmm_hbond_distance.json`.

The target is to produce physically meaningful adsorption geometries with bond distances consistent with the interaction type (chemisorption range for Al–O; hydrogen-bond range for O···HO).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- CP2K: https://www.cp2k.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Aluminum crystal structure (FCC): COD ID 9008463
- Gibbsite (Al(OH)3) crystal structure: COD ID 9004934
- n-Octylphosphonic acid SMILES

## Workflow steps

### Step 1: Prepare simulation cells and initial geometries
- Role: process
- Action: Build periodic slab models of Al(022) and Al(OH)3(001) surfaces from bulk crystal structures (FCC Al and gibbsite), add vacuum regions, and prepare initial guess geometries for OPA adsorption. Construct the deprotonated OPA molecule (R–PO3²⁻) from the SMILES string.
- Evidence: none

### Step 2: DFT chemisorption geometry on Al(022)
- Role: scored (load-bearing)
- Action: Perform DFT geometry optimization of deprotonated OPA on the Al(022) slab using the GGA-PBE functional. Extract the two Al–O bond distances and the final optimized coordinates.
- Output file: `/app/outputs/dft_adsorption_geometry.json`
- Format: json
- Contract: JSON object with keys: al_oxygen_distance_1 (float, Å), al_oxygen_distance_2 (float, Å), coordinates_xyz (string, XYZ coordinate block)
- Scoring: scored by hidden verifier

### Step 3: QM/MM hydrogen bond optimization on Al(OH)3(001)
- Role: scored (load-bearing)
- Action: Set up a QM/MM calculation where OPA is treated quantum mechanically (PBE) and the Al(OH)3 slab with the Dreiding force field. Perform geometry optimization and report the shortest O···HO distance and final coordinates.
- Output file: `/app/outputs/qmmm_hbond_distance.json`
- Format: json
- Contract: JSON object with keys: o_ho_distance (float, Å), coordinates_xyz (string, XYZ coordinate block)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_adsorption_geometry.json`
- `/app/outputs/qmmm_hbond_distance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_adsorption_geometry.json
- path: `/app/outputs/dft_adsorption_geometry.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized adsorption geometry on Al(022) showing bidentate Al–O bonds; checker compares Al–O distances to a hidden reference value within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `al_oxygen_distance_1`: float (Å)
    - `al_oxygen_distance_2`: float (Å)
    - `coordinates_xyz`: string

### qmmm_hbond_distance.json
- path: `/app/outputs/qmmm_hbond_distance.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: QM/MM optimized geometry on Al(OH)3(001) with the shortest O···HO hydrogen bond distance; checker compares the distance to a hidden reference value within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `o_ho_distance`: float (Å)
    - `coordinates_xyz`: string

Notes: The checker will recompute distances from the provided coordinates to verify the reported values. The target policy 'exact_match' is used because the bond distances are physical quantities whose correct values are determined by the computational procedure; a tolerance window is applied to absorb differences between open-source toolchains and the original calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_adsorption_geometry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "al_oxygen_distance_1": "float (Å)",
          "al_oxygen_distance_2": "float (Å)",
          "coordinates_xyz": "string"
        }
      },
      "description": "Optimized adsorption geometry on Al(022) showing bidentate Al–O bonds; checker compares Al–O distances to a hidden reference value within tolerance."
    },
    {
      "file": "qmmm_hbond_distance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "o_ho_distance": "float (Å)",
          "coordinates_xyz": "string"
        }
      },
      "description": "QM/MM optimized geometry on Al(OH)3(001) with the shortest O···HO hydrogen bond distance; checker compares the distance to a hidden reference value within tolerance."
    }
  ],
  "notes": "The checker will recompute distances from the provided coordinates to verify the reported values. The target policy 'exact_match' is used because the bond distances are physical quantities whose correct values are determined by the computational procedure; a tolerance window is applied to absorb differences between open-source toolchains and the original calculation."
}
```

## How you are scored
A hidden verifier will independently score each JSON artifact. For `dft_adsorption_geometry.json`, the checker reads the XYZ coordinates, recomputes the Al–O distances from the O atoms of the phosphate group to the nearest surface Al atoms, confirms that the distances fall in a plausible chemisorption range, and compares the exact distances to a hidden reference value within a tolerance that absorbs legitimate differences between open-source implementations and the original calculation. For `qmmm_hbond_distance.json`, the checker reads the XYZ coordinates, recomputes all O···HO distances between OPA oxygens and surface hydroxyl hydrogens, identifies the shortest distance, and compares it to a hidden reference within tolerance. Each artifact carries a separate weight in the final reward; submitting correct structural coordinates and bond distances, not merely a reported number, is required to pass. The reward ranges from 0 to 1, with partial credit awarded for partial agreements.
