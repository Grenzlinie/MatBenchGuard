# DFT Calculation of Intrinsic Activation Free Energies for CO Addition in SSZ-13 Zeolite

## Problem background
SSZ-13 (zeolite with the chabazite, CHA, framework topology) catalyzes the carbonylation of dimethyl ether (DME) to methyl acetate. The reaction is thought to proceed via a rate-determining step: nucleophilic attack of CO on a surface methoxy group bound to a Brønsted acid site. The CHA structure contains four crystallographically distinct oxygen sites that can host the methoxy group, and the activation barrier for CO addition may depend on which oxygen atom the methoxy is attached to. Understanding the role of methoxy location is central to explaining the observed catalytic activity. This task asks you to compute the intrinsic activation free energies at each of the four O sites from first principles.

## Approach
The reproduction uses periodic density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional augmented by Grimme D3(BJ) dispersion corrections. You will construct a 2×2×2 supercell of the CHA framework (288 atoms) starting from the public primitive cell, substitute one aluminum atom at the unique T site to obtain Si/Al ≈ 95, and add a charge-balancing proton to create a Brønsted acid site. Then, for each of the four distinct O sites (O1, O2, O3, O4), you will place a methoxy group (–CH₃) on that oxygen (removing the proton) and co-adsorb a CO molecule. The transition state for CO addition is located with the climbing-image nudged elastic band (CI-NEB) method followed by dimer refinement. Harmonic vibrational analysis provides zero-point energies and thermodynamic corrections at a temperature of 165 °C and a pressure of 1 bar. The intrinsic activation free energy ΔG_A = G_TS − G_reactant is extracted for each site. The final result is a set of four ΔG_A values that reveal which O sites yield lower barriers.

## Reproduction target
Compute the intrinsic activation free energy ΔG_A (kJ mol⁻¹) for the CO-addition step at each of the four crystallographically distinct oxygen sites (O1, O2, O3, O4) in SSZ-13. The calculation conditions are: PBE-D3(BJ) functional, plane‑wave cutoff 400 eV, Γ‑point sampling, supercell with Si/Al = 95. The free energies are evaluated at T = 165 °C and p = 1 bar. Output the four values in the order [O1, O2, O3, O4] as a JSON file named activation_barriers.json with the key "intrinsic_activation_free_energies".

## Assets

- CHA zeolite framework structure (CIF): https://www.iza-structure.org/databases/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV ultrasoft pseudopotentials: http://www.physics.rutgers.edu/gbrv/

## Workflow steps

### Step 1: Build CHA supercell and prepare methoxy configurations
- Role: process
- Action: From the CHA primitive cell (IZA), construct a 2×2×2 supercell (288 atoms). Substitute one Al atom at the crystallographic T site, add a charge‑balancing H to the nearest O to form a Brønsted acid site (Si/Al=95). For each of the four distinct O sites (O1, O2, O3, O4), generate a structure with a methoxy group (–CH3) placed on that O atom (the proton removed) and a CO molecule co‑adsorbed in a reasonable starting geometry. Save the four starting configurations for the transition‑state searches.
- Evidence: `/app/outputs/supercell_setup.log`

### Step 2: Compute intrinsic activation free energies at O1, O2, O3, O4
- Role: scored (load-bearing)
- Action: For each O site, perform periodic DFT (PBE‑D3(BJ) functional, plane‑wave cutoff 400 eV, Γ‑point sampling) to: (i) optimize the reactant (methoxy + CO), (ii) locate the CO‑addition transition state via climbing‑image nudged elastic band followed by dimer refinement, (iii) confirm the TS with one imaginary vibrational mode, (iv) compute harmonic frequencies to obtain zero‑point energies, thermal corrections, and free energies at 165 °C and 1 bar. Extract the intrinsic activation free energy ΔG_A = G_TS – G_reactant in kJ mol⁻¹ and write the four values into a JSON array.
- Output file: `/app/outputs/activation_barriers.json`
- Format: json
- Contract: {"intrinsic_activation_free_energies": [0.0, 0.0, 0.0, 0.0]} (example format; real values are produced by the DFT workflow).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_barriers.json
- path: `/app/outputs/activation_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Intrinsic activation free energy barriers for CO addition to surface methoxy at the four crystallographically distinct O sites in SSZ-13 (CHA).
- schema:
  - `type`: object
  - `required`: `intrinsic_activation_free_energies`
  - `properties`:
    - `intrinsic_activation_free_energies`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 4
      - `maxItems`: 4
      - `unit`: kJ mol^-1
      - `description`: Ordered list of ΔG_A for O1, O2, O3, O4, respectively.

Notes: The hidden checker reads activation_barriers.json, extracts the array, and compares each value to the paper‑reported reference with tolerances. It also verifies the ordering trend (O1 and O2 barriers must be lower than O3 and O4).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "intrinsic_activation_free_energies"
        ],
        "properties": {
          "intrinsic_activation_free_energies": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 4,
            "maxItems": 4,
            "unit": "kJ mol^-1",
            "description": "Ordered list of ΔG_A for O1, O2, O3, O4, respectively."
          }
        }
      },
      "description": "Intrinsic activation free energy barriers for CO addition to surface methoxy at the four crystallographically distinct O sites in SSZ-13 (CHA)."
    }
  ],
  "notes": "The hidden checker reads activation_barriers.json, extracts the array, and compares each value to the paper‑reported reference with tolerances. It also verifies the ordering trend (O1 and O2 barriers must be lower than O3 and O4)."
}
```

## How you are scored
The hidden verifier reads your activation_barriers.json and compares the reported activation free energies to a confidential reference. Your score reflects how closely your DFT-calculated values agree with the expected pattern; the verifier may additionally check that the relative ordering of the four activation barriers satisfies a structural constraint derived from theoretical analysis. It is not enough to simply copy a published number—your DFT workflow must genuinely produce the results you report.
