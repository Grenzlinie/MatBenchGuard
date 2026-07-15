# Carbon Interstitial Energetics in Silicon via DFT

## Problem background
Carbon dopant atoms are co-implanted in silicon to suppress transient enhanced diffusion (TED) of boron during annealing. The suppression is believed to arise because carbon atoms strongly trap silicon self‑interstitials, thereby reducing the interstitial concentration available to enhance boron diffusion. Understanding the energetics of carbon interstitials—their binding energy relative to a separated Si interstitial and substitutional carbon, their migration barrier, and the resulting activation energy for interstitial‑assisted carbon diffusion—is central to explaining and predicting this trapping efficiency. This task reproduces the key defect energetics of carbon in silicon, as investigated by density functional theory.

## Approach
We use plane‑wave pseudopotential density functional theory (DFT) with the local density approximation (LDA) and, where required, the generalized gradient approximation (GGA) exchange‑correlation functionals. The procedure consists of performing total‑energy calculations for five silicon supercells:

1. a 64‑atom bulk Si cell;
2. a 65‑atom cell containing a neutral ⟨110⟩ Si self‑interstitial (dumbbell);
3. a 64‑atom cell with one substitutional C atom (Si₆₃C);
4. a 64‑atom cell containing a carbon interstitial in the ⟨001⟩ split C–Si pair configuration;
5. a 64‑atom cell with the C₂‑symmetric migration intermediate of the carbon interstitial.

All atomic positions are fully relaxed. The LDA functional is used for all systems; an additional GGA calculation is performed only for the Si self‑interstitial supercell. From the converged total energies we derive the Si self‑interstitial formation energy (using the GGA value), the carbon interstitial binding energy, the carbon migration barrier, and the carbon diffusion activation energy (incorporating the experimentally reported C_i migration barrier of 0.8 eV). All raw energies (Rydberg) and derived quantities (eV) are collected in a single JSON file.

## Reproduction target
Produce a JSON file `defect_energies.json` that contains the following fields:
- total energies (in Ry) of the five supercells as described in the workflow: `E_Si64` (bulk Si 64‑atom), `E_Si65` (LDA energy of the 65‑atom Si self‑interstitial), `E_Si63C` (substitutional C), `E_Si64C` (⟨001⟩ split C interstitial), and `E_intermediate` (migration intermediate).
- derived quantities (in eV): `E_f_Si_i` (Si self‑interstitial formation energy, computed with the GGA energy of the 65‑atom cell), `E_b_Ci` (carbon interstitial binding energy, from LDA energies), `E_m_Ci` (carbon migration barrier, from LDA energies), and `E_a` (carbon diffusion activation energy).
The exact formulas to compute the derived quantities are given in the scored workflow step.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Troullier-Martins pseudopotentials for Si and C (LDA and GGA): https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: DFT total-energy of bulk Si (64 atoms)
- Role: process
- Action: Perform DFT total-energy calculation for a 64-atom bulk Si supercell using the LDA exchange-correlation functional. Use converged k-point sampling and plane-wave cutoff. Write the total energy (in Ry) to a text file.
- Evidence: `/app/outputs/bulk_si_energy.txt`

### Step 2: DFT total-energy of Si self-interstitial (65 atoms)
- Role: process
- Action: Perform DFT total-energy calculations for a 65-atom Si self-interstitial supercell in the neutral <110> dumbbell configuration. Run both LDA and GGA exchange-correlation functionals separately. Write the LDA total energy (Ry) and the GGA total energy (Ry) to separate text files.
- Evidence: `/app/outputs/si_int_lda_energy.txt, si_int_gga_energy.txt`

### Step 3: DFT total-energy of substitutional C (Si63C)
- Role: process
- Action: Perform DFT total-energy calculation for a 64-atom supercell containing one substitutional C atom (Si63C) using the LDA functional. Write the total energy (Ry) to a text file.
- Evidence: `/app/outputs/c_sub_energy.txt`

### Step 4: DFT total-energy of C interstitial (Si64C, <001> split)
- Role: process
- Action: Perform DFT total-energy calculation for a 64-atom supercell containing a C interstitial in the <001> split C-Si pair configuration using the LDA functional. Write the total energy (Ry) to a text file.
- Evidence: `/app/outputs/c_int_energy.txt`

### Step 5: DFT total-energy of C_i migration intermediate (C2 symmetry)
- Role: process
- Action: Perform DFT total-energy calculation for a 64-atom supercell containing the C_i migration intermediate with C2 symmetry using the LDA functional. Write the total energy (Ry) to a text file.
- Evidence: `/app/outputs/c_mig_intermediate_energy.txt`

### Step 6: Derive carbon defect energetics
- Role: scored (load-bearing)
- Action: Read the total energies from the previous DFT steps. Compute the Si self-interstitial formation energy E_f(Si_i) (in eV) using the GGA total energy of the 65-atom Si interstitial and the LDA bulk Si energy, with the formula E_f = E(Si65_gga) - (65/64)*E(Si64). Compute the C interstitial binding energy E_b(C_i) (in eV) using the LDA total energies: E_b = E(Si65_lda) + E(Si63C) - E(Si64C) - E(Si64). Compute the C_i migration barrier E_m(C_i) (in eV) as the difference between the LDA total energy of the migration intermediate and the LDA total energy of the C interstitial. Compute the C diffusion activation energy E_a = E_f(Si_i) - E_b(C_i) + 0.8 eV, where 0.8 eV is the experimentally reported C_i migration barrier. Write a JSON object containing the raw total energies (Ry) and these four derived quantities (eV) to defect_energies.json.
- Output file: `/app/outputs/defect_energies.json`
- Format: json
- Contract: JSON object with keys: E_Si64 (float, Ry), E_Si65 (float, Ry) [LDA total energy of Si self-interstitial], E_Si63C (float, Ry), E_Si64C (float, Ry), E_intermediate (float, Ry), E_f_Si_i (float, eV), E_b_Ci (float, eV), E_m_Ci (float, eV), E_a (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_energies.json
- path: `/app/outputs/defect_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact containing all computed total energies (including boron-related supercells) and derived carbon and boron defect energetics. The checker recomputes E_b_Ci, E_m_Ci, E_a, and E_b_BSi from the raw energies and compares against hidden paper-reported values.
- schema:
  - `type`: object
  - `required`:
    - `E_Si64`: number (Ry)
    - `E_Si65`: number (Ry)
    - `E_Si63C`: number (Ry)
    - `E_Si64C`: number (Ry)
    - `E_intermediate`: number (Ry)
    - `E_Si65_p2`: number (Ry)
    - `E_Si63B_m1`: number (Ry)
    - `E_Si64B_p1`: number (Ry)
    - `E_f_Si_i`: number (eV)
    - `E_b_Ci`: number (eV)
    - `E_m_Ci`: number (eV)
    - `E_a`: number (eV)
    - `E_b_BSi`: number (eV)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "E_Si64": "number (Ry)",
          "E_Si65": "number (Ry)",
          "E_Si63C": "number (Ry)",
          "E_Si64C": "number (Ry)",
          "E_intermediate": "number (Ry)",
          "E_Si65_p2": "number (Ry)",
          "E_Si63B_m1": "number (Ry)",
          "E_Si64B_p1": "number (Ry)",
          "E_f_Si_i": "number (eV)",
          "E_b_Ci": "number (eV)",
          "E_m_Ci": "number (eV)",
          "E_a": "number (eV)",
          "E_b_BSi": "number (eV)"
        }
      },
      "description": "Scored artifact containing all computed total energies (including boron-related supercells) and derived carbon and boron defect energetics. The checker recomputes E_b_Ci, E_m_Ci, E_a, and E_b_BSi from the raw energies and compares against hidden paper-reported values."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `defect_energies.json`. The verifier independently recomputes the three derived quantities `E_b_Ci`, `E_m_Ci`, and `E_a` directly from your reported raw total energies, using the same algebraic formulas stated in the workflow. These recomputed values are compared to reference results obtained from the original DFT study. The comparison tolerances account for the run‑to‑run and implementation‑dependent spread of independent DFT calculations. The final reward is a weighted combination of these three comparisons: full credit is earned if all three quantities agree with the reference within the expected accuracy; otherwise partial credit is awarded based on the number of quantities that pass.
