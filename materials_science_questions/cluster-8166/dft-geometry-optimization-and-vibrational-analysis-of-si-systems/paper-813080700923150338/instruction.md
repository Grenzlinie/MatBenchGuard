# Chemisorption Binding Energies from Empirical Potential Molecular Dynamics

## Problem background
Understanding the initial stages of diamond film growth on silicon via chemical vapor deposition (CVD) requires knowledge of how small hydrocarbon molecules such as acetylene (C₂H₂) and the methyl radical (CH₃) chemisorb onto the clean Si(001)−(2×1) dimerized surface. This task investigates the binding energies and preferred chemisorption configurations of these molecules using the extended Brenner (XB) empirical potential. The XB potential enables large-scale molecular dynamics simulations to efficiently identify candidate chemisorption sites and compute binding energies, complementing more computationally expensive ab initio methods.

## Approach
The method uses classical molecular dynamics (MD) and geometry optimization with the extended Brenner (XB) potential, a multi‑particle interatomic potential for C‑H‑Si systems. A slab model of the Si(001)−(2×1) surface is constructed with periodic boundary conditions. C₂H₂ and CH₃ molecules are incident on the surface with translational energies in the range 0.20–1.0 eV, rotationally and vibrationally cold, and with random starting points, aiming points, and orientations. Many MD trajectories are simulated to explore the configurational space and identify likely chemisorption sites. For each observed (and several hypothesized) site, an initial atomic configuration is prepared, and a full geometry relaxation is performed using the XB potential until the forces are equilibrated. Binding energies are then computed as the difference E_bind = E_slab+adsorbate − E_clean_slab − E_isolated_molecule. The key comparison is between the binding energies of the different adsorption configurations: for C₂H₂, the dimer bridge site (intact and broken dimer) and three cross‑dimer sites (denoted R, A, D); for CH₃, the dangling‑bond sites (one or two adsorbates) and a second‑layer site.

## Reproduction target
Compute and report the binding energies (in eV) for the following chemisorption configurations on Si(001)−(2×1) as predicted by the extended Brenner potential:

- C₂H₂ at the dimer bridge site with intact dimer
- C₂H₂ at the dimer bridge site with broken dimer
- C₂H₂ at cross‑dimer site R
- C₂H₂ at cross‑dimer site A
- C₂H₂ at cross‑dimer site D
- CH₃ at a single surface dangling bond
- CH₃ at both ends of one surface dimer (two CH₃)
- CH₃ at a second‑layer silicon site between the dimer rows

Each binding energy must be obtained from a full geometry optimization using the XB potential (after relaxing the adsorbate and the top substrate layers) and written to the output file `/app/outputs/binding_energies.json` with the exact keys specified in the output contract.

## Assets

- Extended Brenner (XB) potential parameters for C-H-Si systems: https://doi.org/10.1016/0039-6028(96)00587-0
- LAMMPS molecular dynamics package: https://lammps.sandia.gov

## Workflow steps

### Step 1: Slab construction
- Role: process
- Action: Construct a Si(001)-(2x1) slab model of 128 atoms, 8 layers deep, with two-dimensional periodic boundary conditions. Fix the bottom two layers, define a thermal buffer layer (layers 3-4) with velocity rescaling, and allow the top layers and adsorbates to move freely.
- Evidence: `/app/outputs/slab_model.log`

### Step 2: MD simulations of chemisorption events
- Role: process
- Action: Run molecular dynamics simulations using the extended Brenner (XB) potential. Simulate C2H2 and CH3 molecules incident on the slab with translational energies between 0.20 and 1.0 eV, rotationally and vibrationally cold, using random starting points, aiming points, and orientations. Record trajectories.
- Evidence: `/app/outputs/md_trajectories.log`

### Step 3: Site identification and initial geometry preparation
- Role: process
- Action: Analyze the MD trajectories to identify observed chemisorption sites. Prepare initial atomic configurations for geometry optimization of all reported di-sigma sites for C2H2 (bridge intact dimer, bridge broken dimer, cross-dimer R, cross-dimer A, cross-dimer D) and for CH3 (dangling bond one, dangling bond two, second-layer site). For sites not observed in the MD, manually place the molecule in a plausible starting geometry.
- Evidence: `/app/outputs/site_configurations.txt`

### Step 4: Geometry optimization and binding energy calculation
- Role: scored (load-bearing)
- Action: For each identified configuration, perform geometry optimization using the XB potential until forces are equilibrated, then compute the total energy. Calculate the binding energy as E_bind = E_slab+adsorbate - E_clean_slab - E_isolated_molecule. Write all binding energies (in eV) to binding_energies.json.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: JSON object with keys: 'C2H2_bridge_intact', 'C2H2_bridge_broken', 'C2H2_crossdimer_R', 'C2H2_crossdimer_A', 'C2H2_crossdimer_D', 'CH3_dangling_bond_one', 'CH3_dangling_bond_two', 'CH3_second_layer'; each a float in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Binding energies computed by the agent for the XB potential chemisorption configurations. The checker compares each value to the paper's reported XB binding energies within a hidden tolerance.
- schema:
  - `type`: object
  - `required`: `C2H2_bridge_intact`, `C2H2_bridge_broken`, `C2H2_crossdimer_R`, `C2H2_crossdimer_A`, `C2H2_crossdimer_D`, `CH3_dangling_bond_one`, `CH3_dangling_bond_two`, `CH3_second_layer`
  - `properties`:
    - `C2H2_bridge_intact`:
      - `type`: number
      - `unit`: eV
    - `C2H2_bridge_broken`:
      - `type`: number
      - `unit`: eV
    - `C2H2_crossdimer_R`:
      - `type`: number
      - `unit`: eV
    - `C2H2_crossdimer_A`:
      - `type`: number
      - `unit`: eV
    - `C2H2_crossdimer_D`:
      - `type`: number
      - `unit`: eV
    - `CH3_dangling_bond_one`:
      - `type`: number
      - `unit`: eV
    - `CH3_dangling_bond_two`:
      - `type`: number
      - `unit`: eV
    - `CH3_second_layer`:
      - `type`: number
      - `unit`: eV
  - `units`:
    - `each_value`: eV

Notes: Only the XB potential results are scored; ab-initio reference calculations are excluded from this task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "C2H2_bridge_intact",
          "C2H2_bridge_broken",
          "C2H2_crossdimer_R",
          "C2H2_crossdimer_A",
          "C2H2_crossdimer_D",
          "CH3_dangling_bond_one",
          "CH3_dangling_bond_two",
          "CH3_second_layer"
        ],
        "properties": {
          "C2H2_bridge_intact": {
            "type": "number",
            "unit": "eV"
          },
          "C2H2_bridge_broken": {
            "type": "number",
            "unit": "eV"
          },
          "C2H2_crossdimer_R": {
            "type": "number",
            "unit": "eV"
          },
          "C2H2_crossdimer_A": {
            "type": "number",
            "unit": "eV"
          },
          "C2H2_crossdimer_D": {
            "type": "number",
            "unit": "eV"
          },
          "CH3_dangling_bond_one": {
            "type": "number",
            "unit": "eV"
          },
          "CH3_dangling_bond_two": {
            "type": "number",
            "unit": "eV"
          },
          "CH3_second_layer": {
            "type": "number",
            "unit": "eV"
          }
        },
        "units": {
          "each_value": "eV"
        }
      },
      "description": "Binding energies computed by the agent for the XB potential chemisorption configurations. The checker compares each value to the paper's reported XB binding energies within a hidden tolerance."
    }
  ],
  "notes": "Only the XB potential results are scored; ab-initio reference calculations are excluded from this task."
}
```

## How you are scored
A hidden automated verifier will read your `/app/outputs/binding_energies.json` and compare each computed binding energy to a hidden reference value. Credit is awarded based on how close each value is to the reference, within an undisclosed tolerance. To receive full credit you must faithfully execute the complete workflow — slab construction, MD exploration, site identification, geometry optimization with the XB potential, and binding energy calculation — because the verifier only checks the final numbers; simply reporting approximate or copied values will not pass the check. The verifier also validates that the output file exists, contains all required keys, and that the values are numerically plausible.
