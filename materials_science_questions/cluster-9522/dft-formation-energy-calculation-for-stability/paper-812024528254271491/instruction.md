# DFT Formation Energy Calculation for Stability

## Problem background
Metal hydrides with high hydrogen-to-metal ratios are of interest for hydrogen storage applications. BaReH₉ is the prototype of a family of hydrides based on nine-fold coordinated transition-metal anions. It crystallises in a hexagonal structure where each Re is surrounded by a tricapped trigonal prism of H atoms, resulting in unusually short metal–H distances and a wide optical band gap. Understanding the origin of this stability is important for designing new high-hydrogen-content materials. Density functional theory (DFT) can quantify the electronic structure and assess whether a 3d analogue, such as a hypothetical (MnH₉)²⁻ salt, could be similarly stable. In this task you will compute the electronic structure and formation energies of both BaReH₉ and the hypothetical BaMnH₉ using DFT, providing essential quantitative data for such an assessment.

## Approach
Build first-principles models of BaReH₉ and BaMnH₉ using the all-electron linearized augmented plane-wave (LAPW) method within the local density approximation (LDA). For BaReH₉ fix the experimental lattice parameters (a = 5.287 Å, c = 9.323 Å) while relaxing the fractional coordinates of the hydrogen atoms. For BaMnH₉, scale the lattice parameters using covalent radius differences to a = 5.067 Å, c = 8.883 Å and relax the H positions analogously. Then compute reference total energies of the elemental solids (Ba, Re, Mn) and the H₂ molecule, applying a +5 mRy/atom energy correction to Mn to account for the α‑Mn ground state. Using the relaxed structures, run self-consistent field calculations to obtain the total energies, band structures, and densities of states. From these, extract for each compound the direct band gap at the Brillouin-zone centre (Γ) and the formation energy ΔE per formula unit relative to the elements, expressed in kJ per mol H₂.

## Reproduction target
Produce two JSON files containing the computed properties:
- For BaReH₉: the LDA direct band gap at Γ (eV) and the formation energy (kJ mol⁻¹ H₂).
- For hypothetical BaMnH₉: the same two quantities.
The formation energy is defined as ΔE = [E(compound) – E(Ba) – E(Re/Mn) – (9/2) E(H₂)] / 4.5, using the energies of the elemental reference phases computed in the same LDA setup.

## Assets

- Elk all-electron LAPW code: https://elk.sourceforge.io/
- Crystal structures of BaReH9 and BaMnH9

## Workflow steps

### Step 1: Relax H positions in BaReH9
- Role: process
- Action: Perform structural relaxation of H atomic coordinates in BaReH9 using LDA, keeping the experimental lattice parameters (a=5.287 Å, c=9.323 Å) fixed.
- Evidence: `/app/outputs/BaReH9_relaxed_structure.txt`

### Step 2: Relax H positions in BaMnH9
- Role: process
- Action: Perform structural relaxation of H coordinates in hypothetical BaMnH9 within LDA using estimated lattice parameters a=5.067 Å, c=8.883 Å and the same Wyckoff positions as BaReH9 (Mn on 2c site).
- Evidence: `/app/outputs/BaMnH9_relaxed_structure.txt`

### Step 3: Compute reference total energies
- Role: process
- Action: Compute total energies of the elemental reference phases using the same LDA functional: Ba metal, Re metal, Mn metal (with a +5 mRy/atom correction to approximate α‑Mn ground state), and an isolated H₂ molecule in a large supercell.
- Evidence: `/app/outputs/reference_energies.dat`

### Step 4: BaReH9 electronic structure and formation energy
- Role: scored (load-bearing)
- Action: Using the relaxed BaReH9 structure, perform a self-consistent DFT calculation to obtain the total energy and band structure; extract the direct band gap at the Γ point and compute the formation energy ΔE = [E(BaReH9) – E(Ba) – E(Re) – 9/2 E(H₂)] / 4.5, expressed in kJ per mol of H₂.
- Output file: `/app/outputs/BaReH9_results.json`
- Format: json
- Contract: {"band_gap_eV": float, "formation_energy_kJ_per_mol_H2": float}
- Scoring: scored by hidden verifier

### Step 5: BaMnH9 electronic structure and formation energy
- Role: scored (load-bearing)
- Action: Using the relaxed BaMnH9 structure, perform analogous self-consistent DFT calculations, extract the direct band gap at Γ, and compute the formation energy with the reference energies from step_03.
- Output file: `/app/outputs/BaMnH9_results.json`
- Format: json
- Contract: {"band_gap_eV": float, "formation_energy_kJ_per_mol_H2": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/BaReH9_results.json`
- `/app/outputs/BaMnH9_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### BaReH9_results.json
- path: `/app/outputs/BaReH9_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed LDA direct band gap at Γ (eV) and formation energy (kJ/mol H₂) for BaReH9.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number
    - `formation_energy_kJ_per_mol_H2`: number

### BaMnH9_results.json
- path: `/app/outputs/BaMnH9_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed LDA band gap at Γ (eV) and formation energy (kJ/mol H₂) for hypothetical BaMnH9.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number
    - `formation_energy_kJ_per_mol_H2`: number

Notes: The checker will compare these values to hidden paper-reported reference values with absolute tolerances (±0.2 eV for band gaps, ±20 kJ/mol H₂ for formation energies).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "BaReH9_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number",
          "formation_energy_kJ_per_mol_H2": "number"
        }
      },
      "description": "Computed LDA direct band gap at Γ (eV) and formation energy (kJ/mol H₂) for BaReH9."
    },
    {
      "file": "BaMnH9_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number",
          "formation_energy_kJ_per_mol_H2": "number"
        }
      },
      "description": "Computed LDA band gap at Γ (eV) and formation energy (kJ/mol H₂) for hypothetical BaMnH9."
    }
  ],
  "notes": "The checker will compare these values to hidden paper-reported reference values with absolute tolerances (±0.2 eV for band gaps, ±20 kJ/mol H₂ for formation energies)."
}
```

## How you are scored
A hidden verifier reads your BaReH9_results.json and BaMnH9_results.json files. It extracts the four reported numbers: the band gap and formation energy for each compound. Each number is compared to a pre‑determined reference value (the paper’s own LDA result) using an absolute tolerance. The fraction of numbers that lie within tolerance determines your reward (0.0–1.0). The tolerances are set wide enough to absorb legitimate differences between LAPW implementations but narrow enough that a guess without performing the calculations will almost certainly fail. Reporting the paper’s values is not sufficient—you must actually run the DFT workflow to obtain self‑consistent values.
