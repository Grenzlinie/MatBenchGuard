# Computation of Activation Energies for Silicon Nucleophilic Substitution

## Problem background
Pentacoordinated silicon anions can undergo nucleophilic attack to form hexacoordinated intermediates, which are important in organosilicon chemistry. Understanding the energetics of these reactions—particularly the activation barriers for attack by a hydride ion and the relative stability of different pentacoordinated isomers—helps clarify ligand substitution mechanisms at silicon centers. This task focuses on computing the activation energies for the reaction of $\mathrm{SiH_3F_2^-}$ with a hydride ion ($\mathrm{H^-}$) and the energy difference between two isomers of the pentacoordinated anion using ab initio molecular orbital theory.

## Approach
We employ a two-stage computational protocol:
1. **Geometry optimization** of all species (reactants and transition states) at the restricted Hartree–Fock (RHF) level with the 6‑31++G** basis set. Diffuse and polarization functions are essential for anionic species.
2. **Single‑point energy calculations** at the second‑order Møller–Plesset (MP2) level using the same basis set on the optimized geometries.

The studied system is $\mathrm{SiH_3F_2^- + H^-}$. Two isomers of the pentacoordinated anion are considered: isomer **1** (both fluorine atoms apical) and isomer **2** (a structural isomer). For hydride attack, three transition states are located: **TS1** starting from isomer 1, and **TS2** and **TS3** starting from isomer 2. Activation barriers are computed as
$$\Delta E^\ddagger = E(\text{TS}) - E(\text{isomer}) - E(\mathrm{H^-})$$
and the isomer energy difference as $\Delta E_{2-1} = E(2) - E(1)$. All energies are obtained as total MP2/6‑31++G** single‑point energies (in hartree) and converted to kcal mol⁻¹ using $1~\text{hartree} = 627.509~\text{kcal mol}^{-1}$.
The workflow is implemented with an open‑source quantum chemistry package such as Psi4.

## Reproduction target
Reproduce the activation barriers (in kcal mol⁻¹) for hydride attack on the two isomers of $\mathrm{SiH_3F_2^-}$ leading to hexacoordinated dianions, and the energy difference between the two isomers, at the MP2/6‑31++G**//RHF/6‑31++G** level of theory, using an open‑source electronic structure code. The raw MP2 total energies (in hartree) for the reactants and transition states, together with the computed barriers and isomer energy difference, must be written to `/app/outputs/results.json` following the output schema described below. The checker will verify the internal consistency of the submitted energies and that the derived barriers satisfy a specific relative ordering, but the target numbers themselves are hidden.

## Assets

- Psi4: https://psicode.org/
- 6-31++G** basis set

## Workflow steps

### Step 1: Geometry optimization at RHF/6-31++G**
- Role: process
- Action: Construct initial molecular geometries for SiH₃F₂⁻ isomer 1 (both F apical), isomer 2 (structural isomer), and guessed transition states TS1 (from 1), TS2 and TS3 (from 2) for H⁻ attack. Perform RHF/6-31++G** geometry optimizations for all species. Use a saddle-point search algorithm for transition states and verify one imaginary frequency. Save the optimized Cartesian coordinates as XYZ files for subsequent energy calculations.
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 2: MP2 energy calculations and barrier determination
- Role: scored (load-bearing)
- Action: For each optimized geometry from step1 (isomer 1, isomer 2, TS1, TS2, TS3, and H⁻), perform a single-point MP2/6-31++G** calculation to obtain total energies in hartrees. Then compute activation barriers: barrier(TS) = (E_TS - E_corresponding_isomer - E_H⁻) * 627.509 kcal/mol. Compute isomer energy difference: ΔE = (E_isomer2 - E_isomer1) * 627.509. Report all energies and computed values in /app/outputs/results.json using the schema below.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'isomer_1_energy_mp2' (float, hartrees), 'isomer_2_energy_mp2' (float, hartrees), 'E_Hminus_mp2' (float, hartrees), 'TS1_energy_mp2' (float, hartrees), 'TS2_energy_mp2' (float, hartrees), 'TS3_energy_mp2' (float, hartrees), 'isomer_energy_difference_kcalmol' (float, kcal/mol), 'barrier_TS1_kcalmol' (float, kcal/mol), 'barrier_TS2_kcalmol' (float, kcal/mol), 'barrier_TS3_kcalmol' (float, kcal/mol), 'software_used' (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: MP2/6-31++G** single-point energies of reactants and transition states for (1) H⁻ attack on SiH₃F₂⁻, (2) F⁻ attack on SiH₃F₂⁻, and (3) H⁻ attack on SiH₂F₃⁻, together with all activation barriers and isomer energy differences.
- schema:
  - `type`: object
  - `required`: `isomer_1_energy_mp2`, `isomer_2_energy_mp2`, `E_Hminus_mp2`, `F_minus_energy_mp2`, `TS1_energy_mp2`, `TS2_energy_mp2`, `TS3_energy_mp2`, `TS4_energy_mp2`, `TS5_energy_mp2`, `TS6_energy_mp2`, `TS7_energy_mp2`, `TS8_energy_mp2`, `TS9_energy_mp2`, `isomer_energy_difference_kcalmol`, `isomer_7_8_energy_difference_kcalmol`, `barrier_TS1_kcalmol`, `barrier_TS2_kcalmol`, `barrier_TS3_kcalmol`, `barrier_TS4_kcalmol`, `barrier_TS5_kcalmol`, `barrier_TS6_kcalmol`, `barrier_TS7_kcalmol`, `barrier_TS8_kcalmol`, `barrier_TS9_kcalmol`, `software_used`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `isomer_1_energy_mp2`: hartrees
    - `isomer_2_energy_mp2`: hartrees
    - `E_Hminus_mp2`: hartrees
    - `F_minus_energy_mp2`: hartrees
    - `TS1_energy_mp2`: hartrees
    - `TS2_energy_mp2`: hartrees
    - `TS3_energy_mp2`: hartrees
    - `TS4_energy_mp2`: hartrees
    - `TS5_energy_mp2`: hartrees
    - `TS6_energy_mp2`: hartrees
    - `TS7_energy_mp2`: hartrees
    - `TS8_energy_mp2`: hartrees
    - `TS9_energy_mp2`: hartrees
    - `isomer_energy_difference_kcalmol`: kcal/mol
    - `isomer_7_8_energy_difference_kcalmol`: kcal/mol
    - `barrier_TS1_kcalmol`: kcal/mol
    - `barrier_TS2_kcalmol`: kcal/mol
    - `barrier_TS3_kcalmol`: kcal/mol
    - `barrier_TS4_kcalmol`: kcal/mol
    - `barrier_TS5_kcalmol`: kcal/mol
    - `barrier_TS6_kcalmol`: kcal/mol
    - `barrier_TS7_kcalmol`: kcal/mol
    - `barrier_TS8_kcalmol`: kcal/mol
    - `barrier_TS9_kcalmol`: kcal/mol
    - `software_used`: string

Notes: All three reaction systems are combined into one results.json to simplify the output contract and avoid needing multiple scored files. Hidden scoring weights are distributed across the systems inside the verifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "isomer_1_energy_mp2",
          "isomer_2_energy_mp2",
          "E_Hminus_mp2",
          "F_minus_energy_mp2",
          "TS1_energy_mp2",
          "TS2_energy_mp2",
          "TS3_energy_mp2",
          "TS4_energy_mp2",
          "TS5_energy_mp2",
          "TS6_energy_mp2",
          "TS7_energy_mp2",
          "TS8_energy_mp2",
          "TS9_energy_mp2",
          "isomer_energy_difference_kcalmol",
          "isomer_7_8_energy_difference_kcalmol",
          "barrier_TS1_kcalmol",
          "barrier_TS2_kcalmol",
          "barrier_TS3_kcalmol",
          "barrier_TS4_kcalmol",
          "barrier_TS5_kcalmol",
          "barrier_TS6_kcalmol",
          "barrier_TS7_kcalmol",
          "barrier_TS8_kcalmol",
          "barrier_TS9_kcalmol",
          "software_used"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "isomer_1_energy_mp2": "hartrees",
          "isomer_2_energy_mp2": "hartrees",
          "E_Hminus_mp2": "hartrees",
          "F_minus_energy_mp2": "hartrees",
          "TS1_energy_mp2": "hartrees",
          "TS2_energy_mp2": "hartrees",
          "TS3_energy_mp2": "hartrees",
          "TS4_energy_mp2": "hartrees",
          "TS5_energy_mp2": "hartrees",
          "TS6_energy_mp2": "hartrees",
          "TS7_energy_mp2": "hartrees",
          "TS8_energy_mp2": "hartrees",
          "TS9_energy_mp2": "hartrees",
          "isomer_energy_difference_kcalmol": "kcal/mol",
          "isomer_7_8_energy_difference_kcalmol": "kcal/mol",
          "barrier_TS1_kcalmol": "kcal/mol",
          "barrier_TS2_kcalmol": "kcal/mol",
          "barrier_TS3_kcalmol": "kcal/mol",
          "barrier_TS4_kcalmol": "kcal/mol",
          "barrier_TS5_kcalmol": "kcal/mol",
          "barrier_TS6_kcalmol": "kcal/mol",
          "barrier_TS7_kcalmol": "kcal/mol",
          "barrier_TS8_kcalmol": "kcal/mol",
          "barrier_TS9_kcalmol": "kcal/mol",
          "software_used": "string"
        }
      },
      "description": "MP2/6-31++G** single-point energies of reactants and transition states for (1) H⁻ attack on SiH₃F₂⁻, (2) F⁻ attack on SiH₃F₂⁻, and (3) H⁻ attack on SiH₂F₃⁻, together with all activation barriers and isomer energy differences."
    }
  ],
  "notes": "All three reaction systems are combined into one results.json to simplify the output contract and avoid needing multiple scored files. Hidden scoring weights are distributed across the systems inside the verifier."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that reads `/app/outputs/results.json`. The verifier recomputes the activation barriers and isomer energy difference from the raw MP2 energies you provide, and compares them against the expected physical values and the required trend among the barriers without revealing the target numbers. It also checks structural conformance (file format, presence of all required keys, correct units). A correct solution yields the proper barriers and isomer energy difference within a hidden tolerance, and meets the required ordering of barriers; full credit is awarded for meeting these criteria. The software tool reported in `software_used` must be a recognised open‑source quantum chemistry package.
