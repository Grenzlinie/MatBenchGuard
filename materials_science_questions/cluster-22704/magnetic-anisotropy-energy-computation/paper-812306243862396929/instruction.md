# Magnetic Anisotropy Energy Computation for Fe-Co Multilayers on MgO(001)

## Problem background
Magnetic tunnel junctions (MTJs) with perpendicular magnetic anisotropy (PMA) are crucial for spintronic devices. Identifying multilayer thin films with large PMA is challenging because the magnetocrystalline anisotropy (MA) energy is highly sensitive to the atomic-layer stacking at interfaces. This task addresses the atomic-layer stacking dependence of the MA energy in Co-Fe bilayer multilayer thin films on MgO(001), as well as the modification of the MA energy by an external electric field. The goal is to compute, from first principles, the MA energy and the electric-field-induced MA modification for specific atomic-layer configurations, providing insight into how interfacial atomic arrangements control the magnetic anisotropy.

## Approach
The reproduction uses first-principles density functional theory (DFT) calculations within the full-potential linearized augmented plane-wave (FLAPW) method. Slab models consisting of six Fe/Co atomic layers on a four-layer MgO(001) substrate are constructed. Atomic positions are relaxed along the film normal. Spin-polarized total energies are computed with spin-orbit coupling (SOC) included via second variation for magnetization aligned in-plane ([100]) and out-of-plane ([001]). The MA energy per unit area is taken as the total energy difference MAE = E[100] - E[001]. For the electric-field effect, an external electric field of ±0.25 V/Å is applied in the vacuum region and the MAE is recomputed; the average slope η^MA = (MAE(+0.25 V/Å) - MAE(-0.25 V/Å)) / 0.5 provides the electric-field-induced MA modification. The required tool is an open-source FLAPW DFT code (e.g., FLEUR).

## Reproduction target
The objective is to produce two scored CSV files as described in the Workflow steps:

1. `ma_energies.csv`: compute the magnetic anisotropy energy (MA_energy_meV_per_unit_area) for the configurations:
   - FFFFFF/ (6 Fe layers)
   - CCCCCC/ (6 Co layers)
   - CCCCFF/ (4 Co surface layers, 2 Fe layers at the interface)

2. `efield_modification.csv`: for the CCCCFF/ configuration, compute the electric-field-induced MA modification η^MA (eta_MA_meV_per_V_per_Angstrom) using the ±0.25 V/Å field protocol.

These quantities must be computed via the workflow; simply reporting numbers without performing the calculations is insufficient.

## Assets

- FLEUR – FLAPW DFT code: https://www.flapw.de

## Workflow steps

### Step 1: Build slab models for three target configurations
- Role: process
- Action: Construct atomic slab structures for the three configurations: FFFFFF/ (6 Fe layers on 4 MgO layers), CCCCCC/ (6 Co layers on 4 MgO layers), and CCCCFF/ (4 surface Co layers, 2 Fe layers at interface on 4 MgO layers). Use bcc stacking for metal layers, rocksalt MgO(001) substrate, and place interfacial metal atoms atop O atoms. Set in-plane lattice constant to that of calculated bulk MgO.
- Evidence: `/app/outputs/slab_models.tar.gz`

### Step 2: Relax atomic positions
- Role: process
- Action: Perform DFT force calculations using the FLAPW code to relax atomic positions along the film normal for each slab, obtaining equilibrium structures.
- Evidence: `/app/outputs/relaxed_structures.tar.gz`

### Step 3: Compute MA energies for three configurations
- Role: scored (load-bearing)
- Action: For each relaxed slab, carry out spin-polarized DFT calculations with spin-orbit coupling (second-variational SOC) to obtain total energies for magnetization along in-plane [100] and out-of-plane [001] directions. Compute MAE = E[100] - E[001] in meV/unit-area and record values.
- Output file: `/app/outputs/ma_energies.csv`
- Format: csv
- Contract: configuration: string, MA_energy_meV_per_unit_area: float
- Scoring: scored by hidden verifier

### Step 4: Compute E-field-induced MA modification for CCCCFF/
- Role: scored
- Action: For the relaxed CCCCFF/ slab, apply an external electric field of ±0.25 V/Å in the vacuum region, recompute total energies with SOC for [100] and [001] directions, and calculate η^MA = (MAE(0.25 V/Å) - MAE(-0.25 V/Å)) / 0.5.
- Output file: `/app/outputs/efield_modification.csv`
- Format: csv
- Contract: configuration: string, eta_MA_meV_per_V_per_Angstrom: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ma_energies.csv`
- `/app/outputs/efield_modification.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ma_energies.csv
- path: `/app/outputs/ma_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed magnetic anisotropy energy (MAE) for three atomic-layer configurations: FFFFFF/, CCCCCC/, and CCCCFF/. The checker verifies the reported MAE values against hidden paper-derived reference values with tolerance, and additionally checks that the signs and ordering satisfy structural constraints (FF>0, CC<0, CCFF>0 and >CC).
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `MA_energy_meV_per_unit_area`
  - `units`:
    - `MA_energy_meV_per_unit_area`: meV/unit-area

### efield_modification.csv
- path: `/app/outputs/efield_modification.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed electric-field-induced MA modification, η^MA, for the CCCCFF/ configuration. The checker verifies the value against a hidden paper-derived reference with tolerance, and checks that η^MA is positive and consistent with a single-Fe-layer dominated mechanism.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `eta_MA_meV_per_V_per_Angstrom`
  - `units`:
    - `eta_MA_meV_per_V_per_Angstrom`: (meV/unit-area)/(V/Å)

Notes: The hidden checker uses paper-derived reference MAE values for the three configurations (tolerance 0.5 meV/unit-area) and a reference η^MA value (tolerance ~0.2 meV·V⁻¹·Å⁻¹). Structural checks: FFFFFF/ MAE > 0, CCCCCC/ MAE < 0, CCCCFF/ MAE > 0 and greater than CCCCCC/, η^MA positive.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ma_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "MA_energy_meV_per_unit_area"
        ],
        "units": {
          "MA_energy_meV_per_unit_area": "meV/unit-area"
        }
      },
      "description": "Computed magnetic anisotropy energy (MAE) for three atomic-layer configurations: FFFFFF/, CCCCCC/, and CCCCFF/. The checker verifies the reported MAE values against hidden paper-derived reference values with tolerance, and additionally checks that the signs and ordering satisfy structural constraints (FF>0, CC<0, CCFF>0 and >CC)."
    },
    {
      "file": "efield_modification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "eta_MA_meV_per_V_per_Angstrom"
        ],
        "units": {
          "eta_MA_meV_per_V_per_Angstrom": "(meV/unit-area)/(V/Å)"
        }
      },
      "description": "Computed electric-field-induced MA modification, η^MA, for the CCCCFF/ configuration. The checker verifies the value against a hidden paper-derived reference with tolerance, and checks that η^MA is positive and consistent with a single-Fe-layer dominated mechanism."
    }
  ],
  "notes": "The hidden checker uses paper-derived reference MAE values for the three configurations (tolerance 0.5 meV/unit-area) and a reference η^MA value (tolerance ~0.2 meV·V⁻¹·Å⁻¹). Structural checks: FFFFFF/ MAE > 0, CCCCCC/ MAE < 0, CCCCFF/ MAE > 0 and greater than CCCCCC/, η^MA positive."
}
```

## How you are scored
Each scored artifact (`ma_energies.csv` and `efield_modification.csv`) is evaluated by a hidden verifier. The verifier compares the reported values to hidden reference targets (with an appropriate tolerance) and checks that the MA energies satisfy fundamental physical consistency criteria (e.g., sign and relative ordering) expected for this system. The final reward is the sum of weighted scores from the individual output stages, normalized to the interval [0, 1]. The verifier is designed to reward an honest reproduction of the computational workflow; merely guessing or copying the paper's numbers is not sufficient.
