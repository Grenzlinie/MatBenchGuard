# Formation Energy and Optical Gap Calculations for Doped ZnO from First Principles

## Problem background
Transparent conducting oxides (TCOs) such as zinc oxide (ZnO) are critical for optoelectronic applications including photovoltaic electrodes. Doping ZnO with group‑III elements (e.g., Al, Ga) is a standard strategy to improve both electrical conductivity and optical transparency. Understanding how co‑doping with Al and Ga together affects thermodynamic stability (formation energies under different growth conditions) and optical performance (optical band gap) compared with the pure and mono‑doped cases is essential for guiding the design of improved transparent electrode materials. First‑principles density functional theory (DFT) provides a direct route to compute these quantities.

## Approach
Use first‑principles plane‑wave DFT with the PBE exchange‑correlation functional for geometry optimizations and total energy calculations, and a hybrid functional (e.g., HSE06 with standard mixing) for optical gaps. Build 64‑atom supercells of wurtzite ZnO with substitutional doping at 3.125% concentration: one Zn replaced by Al (AZO), one by Ga (GZO), both simultaneously (AGZO), and a pure reference. Relax structures until forces and energies are well converged. Compute chemical potentials for Zn, O, Al, Ga from reference phases (bulk Zn, O₂ molecule, Al₂O₃, Ga₂O₃, ZnO) under two limiting chemical environments — Zn‑rich and O‑rich — as required to define formation energies. Then evaluate formation energies for each doped system via the defect formation energy expression involving total energies and chemical potentials. For the doped supercells, perform a single‑point hybrid calculation on the relaxed geometry; extract the optical band gap from the band structure as the energy separation between the valence band maximum and the Fermi level inside the conduction band (Burstein–Moss shift). The goal is to compare the formation energies and optical gaps across all systems and conditions to reveal the relative stability and optical transparency trends.

## Reproduction target
Produce two CSV files:
- results.csv with columns system, condition, formation_energy (eV) for pure ZnO and the three doped systems under both Zn‑rich and O‑rich conditions.
- optical_gap.csv with columns system, optical_gap (eV) for the three doped systems.
The formation energies must be computed from the relaxed total energies and chemical potentials as described. The optical gaps must be derived from hybrid‑functional band structures. The CSV files will be evaluated by a hidden verifier.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency) for Zn, O, Al, Ga: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structures for wurtzite ZnO, hcp Zn, O2 molecule, Al2O3, Ga2O3

## Workflow steps

### Step 1: Reference total-energy calculations for chemical potentials
- Role: process
- Action: Using the selected DFT code and pseudopotentials, compute the total energies of hexagonal bulk Zn (per atom), O2 molecule (total energy), Al2O3 (per formula unit), Ga2O3 (per formula unit), and wurtzite ZnO (per formula unit). Use GGA-PBE functional and convergence criteria comparable to the paper.
- Evidence: `/app/outputs/reference_total_energies.txt`

### Step 2: Geometry optimization of pure and doped/co-doped ZnO supercells
- Role: process
- Action: Construct 64-atom supercells (4x2x2) for: (a) pure ZnO, (b) Al-doped ZnO (one Zn replaced by Al → Al0.0312Zn0.9688O), (c) Ga-doped ZnO (one Zn replaced by Ga → Ga0.0312Zn0.9688O), (d) Al/Ga co-doped ZnO (two Zn atoms replaced by one Al and one Ga → Al0.0312Zn0.9376Ga0.0312O). Perform structural relaxation using GGA-PBE with force convergence < 0.01 eV/Å and energy convergence < 1e-5 eV per atom. Record the final total energy of each relaxed supercell.
- Evidence: `/app/outputs/relaxations.log`

### Step 3: Compute formation energies and write results.csv
- Role: scored (load-bearing)
- Action: From the relaxed total energies and the reference chemical potentials, determine μ_Zn and μ_O under Zn-rich and O-rich conditions as described: (Zn-rich) μ_Zn = energy per atom of bulk Zn, μ_O = μ_ZnO - μ_Zn; (O-rich) μ_O = ½ E(O2), μ_Zn = μ_ZnO - μ_O. Then compute μ_Al = (E(Al2O3) - 3μ_O)/2 and μ_Ga = (E(Ga2O3) - 3μ_O)/2. For each system, calculate ΔE_form = E_defect - E_pure + n_Zn μ_Zn - n_Al μ_Al - n_Ga μ_Ga (n_Zn = number of Zn atoms removed, etc.). Write the results to /app/outputs/results.csv with columns: system, condition, formation_energy (eV).
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: system (string), condition (string: Zn-rich or O-rich), formation_energy (float, eV)
- Scoring: scored by hidden verifier

### Step 4: Compute optical band gaps and write optical_gap.csv
- Role: scored
- Action: Using the relaxed structures from step 1, perform single-point HSE06 (or a comparable hybrid functional with standard mixing, e.g., α=0.25) calculations for the three doped supercells (Al-doped, Ga-doped, Al/Ga co-doped). From the resulting electronic band structure, determine the optical band gap as the energy difference between the valence band maximum and the Fermi level inside the conduction band (Burstein-Moss shift). Write the results to /app/outputs/optical_gap.csv with columns: system, optical_gap (eV).
- Output file: `/app/outputs/optical_gap.csv`
- Format: csv
- Contract: system (string), optical_gap (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`
- `/app/outputs/optical_gap.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies of pure ZnO, Al-doped ZnO, Ga-doped ZnO, and Al/Ga co-doped ZnO under Zn-rich and O-rich conditions.
- schema:
  - `type`: table
  - `required_columns`: `system`, `condition`, `formation_energy`
  - `units`:
    - `formation_energy`: eV

### optical_gap.csv
- path: `/app/outputs/optical_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optical band gaps of Al-doped ZnO, Ga-doped ZnO, and Al/Ga co-doped ZnO.
- schema:
  - `type`: table
  - `required_columns`: `system`, `optical_gap`
  - `units`:
    - `optical_gap`: eV

Notes: Formation energies and optical band gaps are compared to paper-reported values with tolerances. Ranking of formation energies under O-rich (AGZO < AZO < GZO) and optical gaps (AGZO > AZO > GZO) is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "condition",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "eV"
        }
      },
      "description": "Formation energies of pure ZnO, Al-doped ZnO, Ga-doped ZnO, and Al/Ga co-doped ZnO under Zn-rich and O-rich conditions."
    },
    {
      "file": "optical_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "optical_gap"
        ],
        "units": {
          "optical_gap": "eV"
        }
      },
      "description": "Optical band gaps of Al-doped ZnO, Ga-doped ZnO, and Al/Ga co-doped ZnO."
    }
  ],
  "notes": "Formation energies and optical band gaps are compared to paper-reported values with tolerances. Ranking of formation energies under O-rich (AGZO < AZO < GZO) and optical gaps (AGZO > AZO > GZO) is also verified."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the two CSV files under /app/outputs. It checks that the files conform to the specified schema and that the reported formation energies and optical gaps are physically reasonable and consistent with the expected ordering among systems and conditions. The verifier assigns a weighted score: results.csv carries 60% of the total weight, optical_gap.csv 40%. The score reflects how closely your computed values match the reference data. The exact tolerances and reference values are not disclosed. Submitting plausible but incorrect numbers that violate the known physical trends (e.g., incorrect stability ordering) will result in a low score. The hidden verifier operates independently; simply reporting the expected values without performing the DFT calculations cannot succeed because the checks include trend and tolerance criteria that reflect the actual computational workflow.
