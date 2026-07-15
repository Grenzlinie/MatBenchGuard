# DFT Confirmation of Metallic and Nonmagnetic Behavior in ZrFe0.63Sb

## Problem background
Ternary equiatomic antimonides such as ZrFe1-xSb crystallize in the TiNiSi structure type and exhibit a range of electronic properties depending on composition and valence electron count. The electronic structure of ZrFe1-xSb is of interest because the iron site exhibits partial occupancy (x ≈ 0.32–0.37 under synthesis conditions). Ab initio calculations can reveal whether this material is metallic or insulating and whether it possesses a net magnetic moment, which are key to understanding its bonding and potential applications.

## Approach
Use density functional theory (DFT) as implemented in Quantum ESPRESSO to perform spin-polarized electronic structure calculations on a structural model of ZrFe0.63Sb. The experimental crystal structure (orthorhombic, space group Pnma, Z=4) is used as input. The partial occupancy of the Fe site is handled by a supercell approach or a virtual crystal approximation. A self-consistent field (SCF) calculation is followed by a non-self-consistent calculation to obtain the density of states. The key quantities extracted are the density of states at the Fermi level (in states/eV/unit cell) and the total magnetic moment (in μB). These together determine the metallic versus insulating character and the magnetic ground state.

## Reproduction target
Compute the total density of states at the Fermi level and the total magnetic moment for the structural model of ZrFe0.63Sb. Output both values as a JSON file named electronic_properties.json with keys `dos_at_fermi` (float) and `total_magnetic_moment` (float). The produced numbers will be assessed against hidden criteria that distinguish metallic from insulating behavior and magnetic from nonmagnetic ground states. The task does not require reproducing any specific table or figure from a publication; it is a standalone computational evaluation of the compound's electronic properties.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency library): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Construct crystal structure model for ZrFe0.63Sb
- Role: process
- Action: Build a structural model for ZrFe0.63Sb using the experimental lattice parameters a=682.7 pm, b=417.9 pm, c=739.9 pm, space group Pnma (no. 62), Z=4. Place atoms on Wyckoff position 4c (y=0.25): Zr at x=0.0006, z=0.7920; Fe at x=0.1557, z=0.4254 with partial occupancy 0.63; Sb at x=0.2776, z=0.0929. Handle the Fe partial occupancy via a supercell approach or virtual crystal approximation. Prepare a spin-polarized Quantum ESPRESSO input file suitable for the chosen occupancy treatment, using the SSSP pseudopotentials.
- Evidence: `/app/outputs/step1_structure.log`

### Step 2: Perform DFT electronic structure calculation and output scored properties
- Role: scored (load-bearing)
- Action: Run a spin-polarized self-consistent field (SCF) calculation followed by a non-self-consistent calculation to obtain the density of states (DOS). Extract the DOS at the Fermi level in states/eV/unit cell and the total magnetic moment in μB. Write both values as a JSON object with keys 'dos_at_fermi' (float) and 'total_magnetic_moment' (float) to the file electronic_properties.json.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: {"dos_at_fermi": float, "total_magnetic_moment": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The DFT-calculated electronic properties that indicate metallic behaviour (finite DOS at Fermi level) and nonmagnetic ground state for ZrFe0.63Sb.
- schema:
  - `type`: object
  - `required`: `dos_at_fermi`, `total_magnetic_moment`
  - `properties`:
    - `dos_at_fermi`:
      - `type`: number
      - `description`: Density of states at the Fermi level in states/eV/unit cell
    - `total_magnetic_moment`:
      - `type`: number
      - `description`: Total magnetic moment in μB

Notes: The DFT calculation should use a well-converged k-point grid and appropriate pseudopotentials. The agent may choose the supercell size or virtual crystal approximation to model the partial Fe occupancy. No specific exchange-correlation functional is mandated; standard PBE is acceptable.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "dos_at_fermi",
          "total_magnetic_moment"
        ],
        "properties": {
          "dos_at_fermi": {
            "type": "number",
            "description": "Density of states at the Fermi level in states/eV/unit cell"
          },
          "total_magnetic_moment": {
            "type": "number",
            "description": "Total magnetic moment in μB"
          }
        }
      },
      "description": "The DFT-calculated electronic properties that indicate metallic behaviour (finite DOS at Fermi level) and nonmagnetic ground state for ZrFe0.63Sb."
    }
  ],
  "notes": "The DFT calculation should use a well-converged k-point grid and appropriate pseudopotentials. The agent may choose the supercell size or virtual crystal approximation to model the partial Fe occupancy. No specific exchange-correlation functional is mandated; standard PBE is acceptable."
}
```

## How you are scored
A hidden verifier reads your `electronic_properties.json` and checks the values against thresholds that correspond to the type of electronic structure (metallic vs insulating) and magnetic character (magnetic vs nonmagnetic). Full credit is awarded if both checks pass; otherwise, no credit is given. The verifier does not award partial credit for intermediate files. The exact thresholds are not disclosed, but a correct computation using a well-converged DFT setup with appropriate pseudopotentials and k-point sampling should pass.
