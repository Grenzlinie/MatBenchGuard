# Oxygen vacancy A1 defect level in LaAlO3 via hybrid DFT

## Problem background
In high‑k gate oxide materials such as LaAlO₃, oxygen vacancies can create defect states that trap charge and cause threshold voltage instabilities in transistors. Knowing the energy position of these states relative to the conduction band minimum is essential for evaluating device reliability. This task aims to compute the energy of the neutral oxygen vacancy’s singly degenerate A₁ gap state in cubic LaAlO₃ using a bandgap‑correcting hybrid density functional method.

## Approach
Use density functional theory (DFT) with a hybrid exchange‑correlation functional (e.g., HSE06 or a screened‑exchange equivalent) to study the electronic structure of the neutral oxygen vacancy in cubic LaAlO₃. First, determine the conduction band minimum (CBM) of pristine LaAlO₃ as an energy reference from a bulk calculation. Then, construct a supercell (40–80 atoms) with one neutral oxygen vacancy, relax the atomic positions, and perform a single‑point hybrid‑functional calculation. Compute the projected density of states to locate the singly‑degenerate A₁ symmetry gap state. By aligning the electrostatic potentials or core levels, determine the energy of this defect state relative to the bulk CBM and report the difference.

## Reproduction target
Produce the energy (in eV) of the singly‑degenerate A₁ gap state arising from the neutral oxygen vacancy in cubic LaAlO₃, referenced to the conduction band minimum. The value, obtained from a hybrid functional calculation on a relaxed supercell with proper potential alignment, must be written as a single floating‑point number to vacancy_A1_state_energy.txt. A positive value indicates the state lies below the CBM.

## Assets

- Cubic LaAlO3 crystal structure
- Quantum ESPRESSO or equivalent open-source DFT code: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE) or equivalent: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk LaAlO3 reference calculation
- Role: process
- Action: Perform DFT calculations on cubic LaAlO3 using GGA-PBE to obtain the conduction band minimum (CBM) energy. Use a supercell consistent with the defect calculations.
- Evidence: `/app/outputs/bulk_cbm.txt`

### Step 2: Oxygen vacancy supercell relaxation
- Role: process
- Action: Construct a supercell (40–80 atoms) of cubic LaAlO3 containing a single neutral oxygen vacancy. Relax atomic positions using GGA-PBE with ultra-soft or PAW pseudopotentials, keeping supercell volume fixed.
- Evidence: `/app/outputs/V0_relaxed.xyz`

### Step 3: Vacancy A1 gap state energy
- Role: scored (load-bearing)
- Action: Perform a single-point DFT calculation on the relaxed neutral oxygen vacancy supercell using a hybrid functional (e.g., HSE06). Compute the projected density of states to identify the singly-degenerate A1 symmetry gap state (occupied, localized on adjacent Al ions). Determine its energy eigenvalue relative to the bulk CBM using a consistent potential alignment (e.g., core-level alignment or average electrostatic potential). Report the energy difference (positive value = below CBM) in eV.
- Output file: `/app/outputs/vacancy_A1_state_energy.txt`
- Format: txt
- Contract: A single floating-point number (eV). Positive value means below CBM.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_A1_state_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_A1_state_energy.txt
- path: `/app/outputs/vacancy_A1_state_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energy of the A1 defect state below the conduction band minimum of LaAlO3.
- schema:
  - `type`: text
  - `description`: Numeric value in eV

Notes: Tolerances account for differences in pseudopotentials, functional implementation, and potential alignment method. The agent must implement its own alignment procedure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_A1_state_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Numeric value in eV"
      },
      "description": "Energy of the A1 defect state below the conduction band minimum of LaAlO3."
    }
  ],
  "notes": "Tolerances account for differences in pseudopotentials, functional implementation, and potential alignment method. The agent must implement its own alignment procedure."
}
```

## How you are scored
A hidden verifier independently checks the artifacts you produce. The bulk CBM reference and vacancy relaxation are process steps that are required but carry no direct score. The main reward comes from the energy value in vacancy_A1_state_energy.txt: the verifier compares it to a hidden reference expected for a correctly executed reproduction. Full credit is awarded when your reported value falls within the expected tolerance; larger discrepancies receive partial credit, and unrelated values receive zero. The final score is a weighted combination, with the load‑bearing A₁ state energy carrying the dominant weight. Simply reporting paper‑known numbers without executing the required calculations will not satisfy the process requirements.
