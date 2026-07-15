# Formation Energy and Decomposition Energy of Fe2CrSi from DFT Calculations

## Problem background
The Heusler compound Fe2CrSi has been predicted to be a half-metallic ferromagnet, but thin-film experiments indicate that upon heating it decomposes into Fe3Si and Cr3Si. Density functional theory (DFT) calculations can assess the thermodynamic driving force of this decomposition by computing formation energies of the relevant phases and the reaction energy of the decomposition reaction.

## Approach
The reproduction uses the full-potential linearized augmented plane-wave (FLAPW) method with the Perdew-Burke-Ernzerhof (PBE) functional, as implemented in the open-source elk code. Total energies are calculated for the crystalline compounds Fe2CrSi (in both the L2_1 and A15 structures), Fe3Si (D0_3 structure), and Cr3Si (A15 structure), as well as for the elemental bulk references bcc Fe, bcc Cr, and diamond Si. From these total energies, formation energies per formula unit are derived, and the energy change per formula unit for the decomposition reaction 3 Fe2CrSi → 2 Fe3Si + Cr3Si is computed.

## Reproduction target
Compute, in eV per formula unit, the formation energies of Fe2CrSi in the L2_1 and A15 structures, Fe3Si in the D0_3 structure, and Cr3Si in the A15 structure. Then compute the decomposition reaction energy per formula unit for 3 Fe2CrSi → 2 Fe3Si + Cr3Si, using the lower-energy polymorph of Fe2CrSi. Report all five numeric results in the scored output file step_01_formation_energies.json as specified in the Output Contract.

## Assets

- elk (FLAPW DFT code): https://elk.sourceforge.net

## Workflow steps

### Step 1: Calculate elemental reference total energies
- Role: process
- Action: Run DFT total energy calculations using the FLAPW method (elk code) with the PBE functional for bcc Fe, bcc Cr, and diamond Si. Store the total energies for later use.
- Evidence: `/app/outputs/reference_energies.json`

### Step 2: Calculate compound total energies
- Role: process
- Action: Run DFT calculations for Fe2CrSi in the L21 structure (a=5.679 Å), Fe2CrSi in the A15 structure (a=4.545 Å), Fe3Si in the D03 structure (a=5.654 Å), and Cr3Si in the A15 structure (a=4.560 Å) using the same DFT method.
- Evidence: `/app/outputs/compound_energies.json`

### Step 3: Compute formation energies and decomposition reaction energy
- Role: scored (load-bearing)
- Action: From the total energies obtained in steps 1 and 2, compute the formation energy per formula unit for each compound as E_formation = E_total - sum of elemental reference energies. For Fe2CrSi, report both the L21 and A15 values. Then compute the decomposition reaction energy per formula unit for 3Fe2CrSi → 2Fe3Si + Cr3Si as E_reaction = (2*E_Fe3Si + E_Cr3Si) - 3*E_Fe2CrSi, using the lower of the two Fe2CrSi formation energies as the reactant energy. Write the results to step_01_formation_energies.json.
- Output file: `/app/outputs/step_01_formation_energies.json`
- Format: json
- Contract: {"Fe2CrSi_L21": <formation energy in eV/f.u.>, "Fe2CrSi_A15": <formation energy in eV/f.u.>, "Fe3Si": <formation energy in eV/f.u.>, "Cr3Si": <formation energy in eV/f.u.>, "reaction_energy_per_fu": <reaction energy in eV/f.u.>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.json
- path: `/app/outputs/step_01_formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the formation energies of the four studied crystalline phases and the decomposition reaction energy, derived from DFT total energies. The checker compares these values against the paper-reported hidden gold within a hidden tolerance.
- schema:
  - `type`: object
  - `required`: `Fe2CrSi_L21`, `Fe2CrSi_A15`, `Fe3Si`, `Cr3Si`, `reaction_energy_per_fu`
  - `properties`:
    - `Fe2CrSi_L21`:
      - `type`: number
      - `units`: eV per formula unit
    - `Fe2CrSi_A15`:
      - `type`: number
      - `units`: eV per formula unit
    - `Fe3Si`:
      - `type`: number
      - `units`: eV per formula unit
    - `Cr3Si`:
      - `type`: number
      - `units`: eV per formula unit
    - `reaction_energy_per_fu`:
      - `type`: number
      - `units`: eV per formula unit

Notes: The reaction energy must be positive. The agent must compute the formation energies from their own DFT total energies; the checker will compare against the paper's reported values. Internal consistency is checked by recomputing the reaction energy from the submitted formation energies using the lower Fe2CrSi value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Fe2CrSi_L21",
          "Fe2CrSi_A15",
          "Fe3Si",
          "Cr3Si",
          "reaction_energy_per_fu"
        ],
        "properties": {
          "Fe2CrSi_L21": {
            "type": "number",
            "units": "eV per formula unit"
          },
          "Fe2CrSi_A15": {
            "type": "number",
            "units": "eV per formula unit"
          },
          "Fe3Si": {
            "type": "number",
            "units": "eV per formula unit"
          },
          "Cr3Si": {
            "type": "number",
            "units": "eV per formula unit"
          },
          "reaction_energy_per_fu": {
            "type": "number",
            "units": "eV per formula unit"
          }
        }
      },
      "description": "Contains the formation energies of the four studied crystalline phases and the decomposition reaction energy, derived from DFT total energies. The checker compares these values against the paper-reported hidden gold within a hidden tolerance."
    }
  ],
  "notes": "The reaction energy must be positive. The agent must compute the formation energies from their own DFT total energies; the checker will compare against the paper's reported values. Internal consistency is checked by recomputing the reaction energy from the submitted formation energies using the lower Fe2CrSi value."
}
```

## How you are scored
A hidden verifier reads your output file and computes a reward. It confirms all required keys are present and numeric, recomputes the reaction energy from your reported formation energies to check internal consistency, and compares your formation energies and reaction energy against reference values. The reward reflects how well your computed values agree. Simply reporting known literature values without running the DFT workflow will not satisfy the scoring.
