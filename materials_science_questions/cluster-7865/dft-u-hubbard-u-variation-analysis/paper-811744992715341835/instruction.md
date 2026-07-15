# DFT+U Hubbard U Variation Analysis for Co-Phthalocyanine

## Problem background
Co-phthalocyanine (CoPc) is a prototypical molecular magnet with a rich electronic structure that arises from the interplay of the central Co atom and the surrounding organic ligand. Because the Co 3d states are strongly correlated, standard density functional theory (DFT) often fails to give an accurate description of the molecule's geometry, magnetic moment, and valence electronic spectrum. The DFT+U approach offers a computationally tractable way to include on-site correlation effects by adding a Hubbard U correction to the Co 3d orbitals. This task investigates whether the GGA+U method can reproduce the key structural, electronic, and magnetic properties of an isolated CoPc molecule that are known from experiment and high-level hybrid-functional calculations. The quantities to be determined are the relaxed molecule's bond lengths and angles, the HOMO-LUMO gap, the total and Co-site magnetic moments, and the position of the prominent Co 3d features in the projected density of states.

## Approach
We use first-principles density functional theory within the spin-polarized generalized gradient approximation (GGA), augmented by an on-site Hubbard U correction applied to the Co 3d orbitals (Dudarev formalism). The isolated CoPc molecule is simulated in a large periodic cubic cell to suppress spurious interactions between periodic images. The workflow proceeds in two stages: first, a geometry relaxation is performed to obtain the ground-state atomic positions; second, a self-consistent electronic-structure calculation yields the total and atom-projected density of states as well as the magnetic moments. From the optimized geometry the relevant bond lengths and angles are extracted, and from the electronic structure the HOMO-LUMO gap, the magnetic moments, and the Co 3d projected density of states (PDOS) over an energy window near the Fermi level are obtained. The computed quantities are intended to be compared with experimental data and with results from the hybrid functional B3LYP, which serves as a higher-level reference for the electronic structure.

## Reproduction target
The goal is to compute, from the GGA+U calculation alone, the following quantities for the CoPc molecule:
- The optimized bond lengths (Co–N1, N1–C1, C1–N2, C1–C2, C–H) and angles (C1–N1–C1', N2–C1–N1, N1–C1–C2) as defined in the workflow steps.
- The HOMO-LUMO electronic gap.
- The total magnetic moment of the molecule and the magnetic moment on the Co atom.
- The energy positions of the dominant Co 3d peaks in the projected density of states over the energy range from -5 eV to +2 eV relative to the Fermi level.
All of these must be extracted from the single DFT+U run described in the workflow and written to the specified output files. No external pre-computed values or fitted data may be used.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: DFT+U Calculation
- Role: process
- Action: Run spin-polarized GGA+U calculation for an isolated CoPc molecule using Dudarev's approach with U=6 eV applied to Co 3d orbitals. Use a plane-wave cutoff of 500 eV, simulation cell 21 Å × 21 Å × 21 Å, Gamma-point sampling. Perform geometry relaxation to obtain optimized atomic positions, then compute total and projected density of states (DOS) and magnetic moments.
- Evidence: `/app/outputs/geometry.cif`

### Step 2: Structural Parameter Extraction
- Role: scored (load-bearing)
- Action: From the optimized geometry, extract the following bond lengths (in Å): Co–N1, N1–C1, C1–N2, C1–C2, C–H; and the following bond angles (in degrees): θ(C1–N1–C1′), θ(N2–C1–N1), θ(N1–C1–C2).
- Output file: `/app/outputs/step_01_structure.json`
- Format: json
- Contract: { "R_Co_N1": number, "R_N1_C1": number, "R_C1_N2": number, "R_C1_C2": number, "R_C_H": number, "theta_C1_N1_C1p": number, "theta_N2_C1_N1": number, "theta_N1_C1_C2": number }
- Scoring: scored by hidden verifier

### Step 3: Electronic and Magnetic Properties Extraction
- Role: scored (load-bearing)
- Action: Extract the HOMO-LUMO gap and the total and Co site magnetic moments from the calculation.
- Output file: `/app/outputs/step_02_properties.json`
- Format: json
- Contract: { "HOMO_LUMO_gap": number, "total_magnetic_moment": number, "Co_magnetic_moment": number }
- Scoring: scored by hidden verifier

### Step 4: Co-d PDOS Extraction
- Role: scored (load-bearing)
- Action: Extract the Co 3d projected density of states (PDOS) in the energy window from -5 eV to +2 eV relative to the Fermi level (E_F). Ensure the energy grid is sufficiently fine to resolve peaks.
- Output file: `/app/outputs/step_03_pdos_co.csv`
- Format: csv
- Contract: Columns: energy_eV (float), pdos_co_3d (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structure.json`
- `/app/outputs/step_02_properties.json`
- `/app/outputs/step_03_pdos_co.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structure.json
- path: `/app/outputs/step_01_structure.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bond lengths and angles from the optimized CoPc geometry, compared to hidden reference values with tolerances.
- schema:
  - `type`: object
  - `required`: `R_Co_N1`, `R_N1_C1`, `R_C1_N2`, `R_C1_C2`, `R_C_H`, `theta_C1_N1_C1p`, `theta_N2_C1_N1`, `theta_N1_C1_C2`
  - `units`:
    - `R_Co_N1`: Å
    - `R_N1_C1`: Å
    - `R_C1_N2`: Å
    - `R_C1_C2`: Å
    - `R_C_H`: Å
    - `theta_C1_N1_C1p`: degree
    - `theta_N2_C1_N1`: degree
    - `theta_N1_C1_C2`: degree

### step_02_properties.json
- path: `/app/outputs/step_02_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: HOMO-LUMO gap and magnetic moments from the GGA+U calculation, compared to hidden reference values with tolerances.
- schema:
  - `type`: object
  - `required`: `HOMO_LUMO_gap`, `total_magnetic_moment`, `Co_magnetic_moment`
  - `units`:
    - `HOMO_LUMO_gap`: eV
    - `total_magnetic_moment`: μB
    - `Co_magnetic_moment`: μB

### step_03_pdos_co.csv
- path: `/app/outputs/step_03_pdos_co.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Co 3d projected density of states; peak positions are computed from the data and compared to hidden reference peaks with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `pdos_co_3d`
  - `units`:
    - `energy_eV`: eV
    - `pdos_co_3d`: arbitrary

Notes: All quantities are compared to the paper-reported values with predefined tolerances. The PDOS file is required to contain the energy grid and corresponding Co-d projected DOS; the checker will identify local maxima and compare their positions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "R_Co_N1",
          "R_N1_C1",
          "R_C1_N2",
          "R_C1_C2",
          "R_C_H",
          "theta_C1_N1_C1p",
          "theta_N2_C1_N1",
          "theta_N1_C1_C2"
        ],
        "units": {
          "R_Co_N1": "Å",
          "R_N1_C1": "Å",
          "R_C1_N2": "Å",
          "R_C1_C2": "Å",
          "R_C_H": "Å",
          "theta_C1_N1_C1p": "degree",
          "theta_N2_C1_N1": "degree",
          "theta_N1_C1_C2": "degree"
        }
      },
      "description": "Bond lengths and angles from the optimized CoPc geometry, compared to hidden reference values with tolerances."
    },
    {
      "file": "step_02_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "HOMO_LUMO_gap",
          "total_magnetic_moment",
          "Co_magnetic_moment"
        ],
        "units": {
          "HOMO_LUMO_gap": "eV",
          "total_magnetic_moment": "μB",
          "Co_magnetic_moment": "μB"
        }
      },
      "description": "HOMO-LUMO gap and magnetic moments from the GGA+U calculation, compared to hidden reference values with tolerances."
    },
    {
      "file": "step_03_pdos_co.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "pdos_co_3d"
        ],
        "units": {
          "energy_eV": "eV",
          "pdos_co_3d": "arbitrary"
        }
      },
      "description": "Co 3d projected density of states; peak positions are computed from the data and compared to hidden reference peaks with tolerance."
    }
  ],
  "notes": "All quantities are compared to the paper-reported values with predefined tolerances. The PDOS file is required to contain the energy grid and corresponding Co-d projected DOS; the checker will identify local maxima and compare their positions."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each output file. The verifier compares your reported structural parameters, HOMO-LUMO gap, magnetic moments, and Co‑d PDOS peaks against reference values derived from the published experimental and theoretical benchmarks. Each scored artifact contributes a portion of the final reward; the contributions are weighted so that the main physical quantities carry the largest share. To pass, the computed numbers must agree with the reference within appropriate tolerances that account for the legitimate spread of a re‑run with a different DFT implementation. Simply hard‑coding the expected answer is not sufficient: the verifier expects consistent, physically plausible results that could only come from a genuine execution of the DFT+U workflow.
