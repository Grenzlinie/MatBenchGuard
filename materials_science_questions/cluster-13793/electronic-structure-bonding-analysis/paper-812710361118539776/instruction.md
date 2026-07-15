# DFT-based bonding analysis of amino acid adsorption on clay mineral

## Problem background
Amino acids adsorb onto clay mineral surfaces in soils, influencing the fate of organic nitrogen and the cycling of biomolecules. Understanding the interaction mechanism – whether through electrostatic forces, cation exchange, or hydrophilic effects – requires quantifying the binding strength and the electronic structure at the interface. This task investigates the adsorption of four amino acids (glycine, serine, glutamate, arginine) on pure calcium-montmorillonite in an aqueous environment using density functional theory. The goal is to compute adsorption energies, charge distributions on the terminal carboxyl and amino groups, and the orbital contributions at the valence band edge, in order to identify the dominant orbital coupling that drives the adsorption process.

## Approach
The computational approach constructs a slab model of a pure Ca-montmorillonite supercell and separately places each of the four amino acids with four water molecules near the surface, separated by a vacuum gap. For each system, a DFT geometry optimization is performed using the GGA-PBE exchange-correlation functional and a plane-wave/PAW or equivalent basis set to obtain the relaxed structures. Total energies, Mulliken charges, and the partial density of states (PDOS) are computed from the final geometries. The adsorption energy is derived as the difference between the total energy of the combined Ca-montmorillonite + amino acid + water system and the isolated subsystems. The Mulliken charges on the terminal -COO⁻(H) and -NH₃⁺ groups are extracted for the shorter contact-time regime (< 10 ps equivalent). Analysis of the PDOS reveals which orbital character dominates the top of the valence band, allowing the principal adsorption driver to be deduced.

## Reproduction target
You must produce three scored artifacts:

1. `adsorption_energies.json`: a JSON object with the computed adsorption energies (kJ/mol) for glycine, serine, glutamate, and arginine on pure Ca-montmorillonite, using the formula E_ads = E(Ca-Mt+AA+H₂O) – E(Ca-Mt) – E(AA+H₂O).
2. `mulliken_charges.json`: a JSON array of objects, each containing the amino acid name ("Glycine", "Serine", "Glutamate", "Arginine") and the Mulliken charges (elementary charge units) of its -COO⁻(H) and -NH₃⁺ groups, taken from the <10 ps equivalent contact-time regime.
3. `vb_dominance.txt`: a plain-text file stating the orbital character that dominates the top of the valence band, and explicitly concluding which orbital coupling is the principal adsorption driver based on the computed PDOS data.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, ASE with GPAW): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Build initial atomic models of Ca-montmorillonite and amino acid + water systems
- Role: process
- Action: Construct a 2×1×1 supercell of Ca-montmorillonite (Ca[Al₄][Si₈O₂₀](OH)₄) using lattice parameters a=4.80-5.00 Å, b=8.30-8.70 Å, c=13.90-14.50 Å, α=β=γ=90°. Place each amino acid (glycine, serine, glutamate, arginine) and four water molecules near the surface with a ~16 Å vacuum gap. Generate initial Cartesian coordinates for all four Ca-Mt+AA+H₂O systems.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: Run DFT geometry optimization and electronic structure calculations
- Role: process
- Action: For each Ca-Mt+AA+H₂O system, perform DFT geometry optimization using GGA-PBE, a DNP-like basis or equivalent PAW, and a 3×3×3 k-point mesh. Converge to energy < 1e-5 eV/atom. Compute total energies, Mulliken charges, and partial density of states (PDOS) for the final structures.
- Evidence: `/app/outputs/dft_convergence.log`

### Step 3: Compute and output adsorption energies
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute adsorption energies as E_ads = E(Ca-Mt+AA+H₂O) – E(Ca-Mt) – E(AA+H₂O). Report values for glycine, serine, glutamate, and arginine on pure Ca-Mt.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {"type":"object","properties":{"Glycine":{"type":"number","unit":"kJ/mol"},"Serine":{"type":"number","unit":"kJ/mol"},"Glutamate":{"type":"number","unit":"kJ/mol"},"Arginine":{"type":"number","unit":"kJ/mol"}},"required":["Glycine","Serine","Glutamate","Arginine"]}
- Scoring: scored by hidden verifier

### Step 4: Compute and output Mulliken charges of terminal groups
- Role: scored
- Action: From the DFT output, extract Mulliken charges for the carboxyl (-COO⁻(H)) and amino (-NH₃⁺) groups of each amino acid. Report the <10 ps equivalent values (the shorter contact time regime).
- Output file: `/app/outputs/mulliken_charges.json`
- Format: json
- Contract: {"type":"array","items":{"type":"object","properties":{"amino_acid":{"type":"string"},"COO_charge":{"type":"number"},"NH3_charge":{"type":"number"}},"required":["amino_acid","COO_charge","NH3_charge"]}}
- Scoring: scored by hidden verifier

### Step 5: Determine valence band top orbital dominance
- Role: scored
- Action: From the computed PDOS, identify the orbital character that dominates the valence band maximum. Write a statement describing the dominant orbital and concluding which orbital coupling is the principal adsorption driver based on this analysis.
- Output file: `/app/outputs/vb_dominance.txt`
- Format: txt
- Contract: A plain-text statement with no specific format, but must contain the key phrases asserting the dominant orbital identity and its role as the main adsorption driver.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`
- `/app/outputs/mulliken_charges.json`
- `/app/outputs/vb_dominance.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed adsorption energies for glycine, serine, glutamate, and arginine on pure Ca-montmorillonite in kJ/mol.
- schema:
  - `type`: object
  - `properties`:
    - `Glycine`:
      - `type`: number
      - `unit`: kJ/mol
    - `Serine`:
      - `type`: number
      - `unit`: kJ/mol
    - `Glutamate`:
      - `type`: number
      - `unit`: kJ/mol
    - `Arginine`:
      - `type`: number
      - `unit`: kJ/mol
  - `required`: `Glycine`, `Serine`, `Glutamate`, `Arginine`

### mulliken_charges.json
- path: `/app/outputs/mulliken_charges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mulliken charges for terminal -COO⁻(H) and -NH₃⁺ groups of each amino acid, in elementary charge units.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `amino_acid`:
        - `type`: string
      - `COO_charge`:
        - `type`: number
      - `NH3_charge`:
        - `type`: number
    - `required`: `amino_acid`, `COO_charge`, `NH3_charge`

### vb_dominance.txt
- path: `/app/outputs/vb_dominance.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: A text statement identifying the dominant orbital character at the valence band maximum and the derived principal adsorption driver.
- schema:
  - `type`: text

Notes: Adsorption energies and Mulliken charges are compared to reference values from the original study within specified tolerances. The valence band dominance statement is checked for correctness of the conclusion.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "Glycine": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "Serine": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "Glutamate": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "Arginine": {
            "type": "number",
            "unit": "kJ/mol"
          }
        },
        "required": [
          "Glycine",
          "Serine",
          "Glutamate",
          "Arginine"
        ]
      },
      "description": "Computed adsorption energies for glycine, serine, glutamate, and arginine on pure Ca-montmorillonite in kJ/mol."
    },
    {
      "file": "mulliken_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "amino_acid": {
              "type": "string"
            },
            "COO_charge": {
              "type": "number"
            },
            "NH3_charge": {
              "type": "number"
            }
          },
          "required": [
            "amino_acid",
            "COO_charge",
            "NH3_charge"
          ]
        }
      },
      "description": "Mulliken charges for terminal -COO⁻(H) and -NH₃⁺ groups of each amino acid, in elementary charge units."
    },
    {
      "file": "vb_dominance.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "A text statement identifying the dominant orbital character at the valence band maximum and the derived principal adsorption driver."
    }
  ],
  "notes": "Adsorption energies and Mulliken charges are compared to reference values from the original study within specified tolerances. The valence band dominance statement is checked for correctness of the conclusion."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each output file. The computed adsorption energies and Mulliken charges are compared against reference values derived from independent calculations, with tolerances that accommodate differences in DFT implementation. The valence band dominance statement is validated to ensure it correctly identifies the dominant orbital character and draws the appropriate conclusion about the main adsorption driver. The final score is a weighted combination of these checks; merely writing numbers without executing the DFT workflow will not result in a passing score.
