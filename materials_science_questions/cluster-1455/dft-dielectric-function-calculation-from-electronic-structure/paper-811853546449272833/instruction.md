# DFT Dielectric Response of Ta₂O₅ and Nb₂O₅ Polymorphs

## Problem background
High-κ dielectrics such as Ta₂O₅, Nb₂O₅, and their solid solutions are investigated for integrated circuit capacitors. Understanding the relative thermodynamic stability of the orthorhombic (β) and hexagonal (δ_A) polymorphs, and characterizing their dielectric permittivity, Born effective charges, and band gaps from first-principles density functional theory (DFT), is a central challenge.

## Approach
The approach is to model each phase with DFT using the local density approximation (LDA) and Vanderbilt ultrasoft pseudopotentials. Crystal structures are built for the orthorhombic β phase (from Ramprasad et al.) and the hexagonal δ_A phase (from Fukumoto and Miwa) of both Ta₂O₅ and Nb₂O₅, as well as a mixed β-NbTaO₅ phase. Geometry optimizations relax the structures to obtain total energies. Dielectric permittivity tensors (electronic plus ionic contributions), Born effective charge tensors, and LDA band gaps are computed via linear response and band structure calculations. The workflow compares the stability of the β and δ_A phases and the dielectric properties across the binary oxides and the mixed composition.

## Reproduction target
Recompute the total energy differences between the orthorhombic β phase and the hexagonal δ_A phase for Ta₂O₅ and Nb₂O₅. Compute the dielectric permittivity tensor components (ε_xx, ε_yy, ε_zz), the directionally averaged dielectric constant, the LDA band gap, and the average Born effective charges (for metal and oxygen ions) for the β and δ_A phases of both binary oxides and for the β phase of NbTaO₅. Determine whether the β phase is more stable than δ_A for both oxides, and whether the Nb₂O₅ phases have higher permittivity than their Ta₂O₅ counterparts.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Vanderbilt ultrasoft pseudopotentials for O, Nb, Ta: https://www.quantum-espresso.org/pseudopotentials
- Ramprasad et al. orthorhombic β-Ta2O5 structure: 10.1016/S0167-9317(03)00286-6
- Fukumoto and Miwa hexagonal δ_A structure: 10.1103/PhysRevB.55.11155

## Workflow steps

### Step 1: Crystal structure setup and DFT input generation
- Role: process
- Action: Construct initial atomic models for orthorhombic β and hexagonal δ_A phases of Ta2O5 and Nb2O5 using crystallographic data from Ramprasad et al. (orthorhombic) and Fukumoto and Miwa (hexagonal δ_A). Also construct the mixed β-NbTaO5 phase by randomly substituting half of the metal sites with Nb and Ta. Prepare Quantum ESPRESSO input files for LDA calculations with Vanderbilt ultrasoft pseudopotentials for each structure.
- Evidence: `/app/outputs/structures_archive`

### Step 2: DFT geometry optimization of crystalline phases
- Role: process
- Action: Use Quantum ESPRESSO pw.x to relax atomic positions and cell parameters for the five phases (β-Ta2O5, β-Nb2O5, δ_A-Ta2O5, δ_A-Nb2O5, β-NbTaO5) to obtain relaxed structures and total energies.
- Evidence: `/app/outputs/relax_outputs`

### Step 3: DFT linear response and band structure calculations
- Role: process
- Action: Use Quantum ESPRESSO ph.x to compute dielectric permittivity tensors (electronic + ionic contributions) and Born effective charge tensors for all atoms. Compute the LDA band gap via a pw.x band structure calculation for each relaxed phase.
- Evidence: `/app/outputs/dielectric_outputs`

### Step 4: Compile dielectric constants, band gaps, and stability energies
- Role: scored (load-bearing)
- Action: From the relaxed geometries and linear response outputs, extract total energy per formula unit (in Ry) for each phase; dielectric tensor components (ε_xx, ε_yy, ε_zz) and directionally averaged dielectric constant ε_avg = (ε_xx+ε_yy+ε_zz)/3; LDA band gap (eV); and average Born effective charges for metal (Ta/Nb) and oxygen ions. Compute energy differences ΔE = E(δ_A) − E(β) in eV per formula unit for Ta2O5 and Nb2O5. Write all results to /app/outputs/results.json following the output schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys 'beta_Ta2O5', 'deltaA_Ta2O5', 'beta_Nb2O5', 'deltaA_Nb2O5', 'beta_NbTaO5' each containing: energy_per_fu (number, Ry), epsilon_xx, epsilon_yy, epsilon_zz (numbers), epsilon_avg (number), band_gap (number, eV), metal_Born_charge_avg (number), oxygen_Born_charge_avg (number). Top-level keys: 'energy_diff_beta_vs_deltaA_Ta2O5' (number, eV/f.u.), 'energy_diff_beta_vs_deltaA_Nb2O5' (number, eV/f.u.).
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
- target_policy: reference_match
- description: All targeted quantities from the DFT workflow: total energies, dielectric tensor components, averaged permittivities, band gaps, Born effective charges, and energy differences between β and δ_A phases. The checker compares reported values to hidden paper-derived reference values and verifies that β is more stable than δ_A for both binary oxides and that Nb2O5 phases have higher permittivity than the corresponding Ta2O5 phases.
- schema:
  - `type`: object
  - `required`:
    - `beta_Ta2O5`:
      - `energy_per_fu`: number (Ry)
      - `epsilon_xx`: number
      - `epsilon_yy`: number
      - `epsilon_zz`: number
      - `epsilon_avg`: number
      - `band_gap`: number (eV)
      - `metal_Born_charge_avg`: number
      - `oxygen_Born_charge_avg`: number
    - `deltaA_Ta2O5`:
      - `energy_per_fu`: number (Ry)
      - `epsilon_xx`: number
      - `epsilon_yy`: number
      - `epsilon_zz`: number
      - `epsilon_avg`: number
      - `band_gap`: number (eV)
      - `metal_Born_charge_avg`: number
      - `oxygen_Born_charge_avg`: number
    - `beta_Nb2O5`:
      - `energy_per_fu`: number (Ry)
      - `epsilon_xx`: number
      - `epsilon_yy`: number
      - `epsilon_zz`: number
      - `epsilon_avg`: number
      - `band_gap`: number (eV)
      - `metal_Born_charge_avg`: number
      - `oxygen_Born_charge_avg`: number
    - `deltaA_Nb2O5`:
      - `energy_per_fu`: number (Ry)
      - `epsilon_xx`: number
      - `epsilon_yy`: number
      - `epsilon_zz`: number
      - `epsilon_avg`: number
      - `band_gap`: number (eV)
      - `metal_Born_charge_avg`: number
      - `oxygen_Born_charge_avg`: number
    - `beta_NbTaO5`:
      - `energy_per_fu`: number (Ry)
      - `epsilon_xx`: number
      - `epsilon_yy`: number
      - `epsilon_zz`: number
      - `epsilon_avg`: number
      - `band_gap`: number (eV)
      - `metal_Born_charge_avg`: number
      - `oxygen_Born_charge_avg`: number
    - `energy_diff_beta_vs_deltaA_Ta2O5`: number (eV/f.u.)
    - `energy_diff_beta_vs_deltaA_Nb2O5`: number (eV/f.u.)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The agent must execute all process steps (structure building, geometry optimization, linear response) to obtain the values compiled in this file. The target_policy is reference_match; the checker also performs structural audits for ordering. No gold values or tolerances are disclosed.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta_Ta2O5": {
            "energy_per_fu": "number (Ry)",
            "epsilon_xx": "number",
            "epsilon_yy": "number",
            "epsilon_zz": "number",
            "epsilon_avg": "number",
            "band_gap": "number (eV)",
            "metal_Born_charge_avg": "number",
            "oxygen_Born_charge_avg": "number"
          },
          "deltaA_Ta2O5": {
            "energy_per_fu": "number (Ry)",
            "epsilon_xx": "number",
            "epsilon_yy": "number",
            "epsilon_zz": "number",
            "epsilon_avg": "number",
            "band_gap": "number (eV)",
            "metal_Born_charge_avg": "number",
            "oxygen_Born_charge_avg": "number"
          },
          "beta_Nb2O5": {
            "energy_per_fu": "number (Ry)",
            "epsilon_xx": "number",
            "epsilon_yy": "number",
            "epsilon_zz": "number",
            "epsilon_avg": "number",
            "band_gap": "number (eV)",
            "metal_Born_charge_avg": "number",
            "oxygen_Born_charge_avg": "number"
          },
          "deltaA_Nb2O5": {
            "energy_per_fu": "number (Ry)",
            "epsilon_xx": "number",
            "epsilon_yy": "number",
            "epsilon_zz": "number",
            "epsilon_avg": "number",
            "band_gap": "number (eV)",
            "metal_Born_charge_avg": "number",
            "oxygen_Born_charge_avg": "number"
          },
          "beta_NbTaO5": {
            "energy_per_fu": "number (Ry)",
            "epsilon_xx": "number",
            "epsilon_yy": "number",
            "epsilon_zz": "number",
            "epsilon_avg": "number",
            "band_gap": "number (eV)",
            "metal_Born_charge_avg": "number",
            "oxygen_Born_charge_avg": "number"
          },
          "energy_diff_beta_vs_deltaA_Ta2O5": "number (eV/f.u.)",
          "energy_diff_beta_vs_deltaA_Nb2O5": "number (eV/f.u.)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "All targeted quantities from the DFT workflow: total energies, dielectric tensor components, averaged permittivities, band gaps, Born effective charges, and energy differences between β and δ_A phases. The checker compares reported values to hidden paper-derived reference values and verifies that β is more stable than δ_A for both binary oxides and that Nb2O5 phases have higher permittivity than the corresponding Ta2O5 phases."
    }
  ],
  "notes": "The agent must execute all process steps (structure building, geometry optimization, linear response) to obtain the values compiled in this file. The target_policy is reference_match; the checker also performs structural audits for ordering. No gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage’s artifact. For each scored artifact, the verifier compares your computed numerical values (or structural properties) against reference values derived from the original study using appropriate tolerances. The verifier also checks that the required structural ordering (β more stable than δ_A, and higher permittivity for Nb₂O₅ phases) is reproduced. The final reward is a weighted sum over the scored stages, with the main compilation of dielectric constants, band gaps, and energy differences carrying the largest weight. Reporting the expected numbers is not sufficient; you must actually run the DFT workflow and produce the artifacts through genuine computation.
