# DFT Analysis of Defect State Energies and Hydrogen Bond Dynamics at a Doped Hematite-Water Interface

## Problem background
Zn-doped hematite (α-Fe₂O₃) is a promising photoanode for the oxygen evolution reaction (OER). Doping introduces excess hole carriers whose electronic properties at the aqueous interface determine catalytic performance. Understanding the energy, localization, and dynamics of the hole defect state, as well as the interfacial hydrogen bonding, is crucial for linking doping to lowered overpotentials. This task requires computing, via hybrid DFT and ab initio molecular dynamics, the defect state energy within the band gap, the band gap itself, the electrochemical alignment of the defect state, and the hydrogen bond survival times at the doped hematite–water interface.

## Approach
The system is a Zn-doped hematite (0001) slab in contact with water. First, a slab model is built and relaxed in vacuum using PBE0 with 12% exact exchange. Then a water layer is added and the interface is set up with a double dehydrogenation on the Zn-proximal surface. Ab initio molecular dynamics (AIMD) is run with a 0.5 fs time step at 300 K using two consecutive DFT protocols: approximately 35.7 ps with PBE+D3 and approximately 14.3 ps with PBE+U+D3 (U=4.3 eV on Fe 3d). Atomic coordinates are saved every 200 fs. For each saved snapshot, the doubly dehydrogenated surface is rehydrogenated and a PBE0(0.12) single-point calculation is performed. The lowest unoccupied α‑spin eigenvalue is taken as the defect state energy, and the valence band maximum (VBM) and conduction band minimum (CBM) are extracted, giving the DS energy relative to VBM and the VBM–CBM gap. These values are collected into a time series. Summary statistics are computed for the two trajectory segments separately. The VBM is aligned to the electrochemical scale using the plane-averaged electrostatic potential and a literature protocol for semiconductor–water interfaces at the point-of-zero-charge, yielding the defect state level vs RHE. Finally, hydrogen bonds in the full trajectory are identified by a geometric criterion (O···O < 3.5 Å, O···H–O angle > 135°). Survival probabilities are computed for intrasurface, surface‑donating, and surface‑accepting bonds on both the fully protonated and the doubly deprotonated surfaces, then fitted to exponentials to obtain characteristic decay times and R².

## Reproduction target
Compute and report the following quantities:

1. **Defect state energy and band gap time series**: For every snapshot (one per 200 fs), the DS energy above VBM and the VBM–CBM gap, written to `ds_energies.csv`.
2. **Segment-wise summary statistics**: Mean and standard deviation of the DS energy and band gap for the PBE+D3 segment (first ~35.7 ps) and the PBE+U+D3 segment (last ~14.3 ps), written to `ds_summary.csv`.
3. **Electrochemical alignment**: VBM and average defect state energy on the RHE scale, along with the offset from the O₂/H₂O redox potential, written to `ds_alignment.json`.
4. **Hydrogen bond survival times**: Characteristic decay times τ and fit quality R² for intrasurface, surface‑donating, and surface‑accepting hydrogen bonds on both the fully protonated and the doubly deprotonated surfaces, written to `hbond_survival.csv`.

## Assets

- CP2K: https://www.cp2k.org/
- Goedecker-Teter-Hunter pseudopotentials: CP2K
- DZVP basis set: CP2K
- Hematite crystal structure (α-Fe2O3): any public crystallographic database (ICSD, Materials Project, COD)
- Python with numpy, pandas: python>=3.9, numpy, pandas

## Workflow steps

### Step 1: Prepare Zn-doped hematite (0001) slab model
- Role: process
- Action: Build a six-layer hematite (0001) slab with antiferromagnetic ordering from the bulk crystal structure. Substitute one subsurface Fe with Zn (~2% doping). Fully hydroxylate both surfaces. Relax the slab in vacuum using PBE0 with 12% exact exchange in CP2K. Output the relaxed structure.
- Evidence: `/app/outputs/slab_relaxed.xyz`

### Step 2: Set up hematite/water interface
- Role: process
- Action: Add 56 water molecules to the relaxed slab in a cell with ~19 Å water layer. Remove two hydrogen atoms from the Zn-proximal surface (double dehydrogenation) to model catalytic conditions. Prepare an initial random water configuration.
- Evidence: `/app/outputs/interface.xyz`

### Step 3: Run ab initio molecular dynamics of the interface
- Role: process
- Action: Perform NVT AIMD at 300 K with a Nosé–Hoover thermostat and 0.5 fs time step. Run two consecutive segments: approximately 35.7 ps with PBE+D3, then approximately 14.3 ps with PBE+U+D3 (U=4.3 eV on Fe 3d). Save atomic coordinates every 200 fs (total >50 ps).
- Evidence: `/app/outputs/aimd_trajectory.xyz`

### Step 4: Compute defect state energies and band gaps from snapshots
- Role: scored (load-bearing)
- Action: For each saved snapshot, rehydrogenate the doubly dehydrogenated surface, then perform a PBE0(0.12) single-point calculation. Extract the lowest unoccupied α-spin eigenvalue (defect state energy) and the valence band maximum (VBM) and conduction band minimum (CBM). Compute the DS energy relative to VBM and the VBM–CBM gap. Write the full time series to ds_energies.csv.
- Output file: `/app/outputs/ds_energies.csv`
- Format: csv
- Contract: Columns: time_ps (float), ds_energy_above_vbm_eV (float), vbm_cbm_gap_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Summary statistics of defect state energies
- Role: scored
- Action: From the computed DS energies, calculate the mean and standard deviation of ds_energy_above_vbm_eV and vbm_cbm_gap_eV for the PBE+D3 segment (first 35.7 ps) and the PBE+U+D3 segment (last 14.3 ps). Write the result to ds_summary.csv.
- Output file: `/app/outputs/ds_summary.csv`
- Format: csv
- Contract: Columns: segment (string: 'PBE+D3' or 'PBE+U+D3'), mean_ds_energy_eV (float), std_ds_energy_eV (float), mean_vbm_cbm_gap_eV (float), std_vbm_cbm_gap_eV (float).
- Scoring: scored by hidden verifier

### Step 6: Electrochemical level alignment of the defect state
- Role: scored
- Action: Align the VBM to the electrochemical scale using the plane-averaged electrostatic potential from snapshots and a literature protocol for semiconductor–water interfaces at pH equal to the point-of-zero-charge. Compute the average defect state level vs RHE. Output the aligned VBM, DS level, and offset from the O₂/H₂O redox potential.
- Output file: `/app/outputs/ds_alignment.json`
- Format: json
- Contract: Keys: vbm_vs_rhe_eV (float), ds_mean_vs_rhe_eV (float), ds_std_vs_rhe_eV (float), offset_from_oer_eV (float).
- Scoring: scored by hidden verifier

### Step 7: Analyze hydrogen bonding dynamics
- Role: scored
- Action: From the full AIMD trajectory, identify hydrogen bonds using the geometric criterion (O···O < 3.5 Å, O···H–O angle > 135°). Compute survival probabilities for intrasurface, surface-donating, and surface-accepting bonds on the fully protonated and doubly deprotonated surfaces. Fit exponential decays to obtain characteristic times τ and R². Write results to hbond_survival.csv.
- Output file: `/app/outputs/hbond_survival.csv`
- Format: csv
- Contract: Columns: surface_type (string: 'fully_protonated' or 'doubly_deprotonated'), bond_type (string: 'intrasurface', 'surface_donating', 'surface_accepting'), tau_ps (float), r_squared (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ds_energies.csv`
- `/app/outputs/ds_summary.csv`
- `/app/outputs/ds_alignment.json`
- `/app/outputs/hbond_survival.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ds_energies.csv
- path: `/app/outputs/ds_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time series of defect state energy above VBM and VBM-CBM gap for each snapshot. Checker will compute segment-wise means and standard deviations and compare to hidden paper reference values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `ds_energy_above_vbm_eV`, `vbm_cbm_gap_eV`
  - `units`:
    - `time_ps`: picoseconds
    - `ds_energy_above_vbm_eV`: eV
    - `vbm_cbm_gap_eV`: eV

### ds_summary.csv
- path: `/app/outputs/ds_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Segment-wise summary statistics of defect state energy and band gap. Checker compares directly to hidden reference values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `segment`, `mean_ds_energy_eV`, `std_ds_energy_eV`, `mean_vbm_cbm_gap_eV`, `std_vbm_cbm_gap_eV`
  - `units`:
    - `mean_ds_energy_eV`: eV
    - `std_ds_energy_eV`: eV
    - `mean_vbm_cbm_gap_eV`: eV
    - `std_vbm_cbm_gap_eV`: eV

### ds_alignment.json
- path: `/app/outputs/ds_alignment.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aligned VBM and defect state energy on the electrochemical scale. Checker compares values to hidden paper reference with tolerance.
- schema:
  - `type`: object
  - `required`: `vbm_vs_rhe_eV`, `ds_mean_vs_rhe_eV`, `ds_std_vs_rhe_eV`, `offset_from_oer_eV`
  - `units`:
    - `vbm_vs_rhe_eV`: eV
    - `ds_mean_vs_rhe_eV`: eV
    - `ds_std_vs_rhe_eV`: eV
    - `offset_from_oer_eV`: eV

### hbond_survival.csv
- path: `/app/outputs/hbond_survival.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Hydrogen bond survival times and exponential fit R² for different surface and bond types. Checker verifies that R² exceeds a threshold and that tau values are within tolerance of hidden paper reference.
- schema:
  - `type`: table
  - `required_columns`: `surface_type`, `bond_type`, `tau_ps`, `r_squared`
  - `units`:
    - `tau_ps`: picoseconds
    - `r_squared`: unitless

Notes: The primary verification is recomputation of summary statistics from ds_energies.csv and comparison to reference values; ds_summary.csv is a convenience artifact that may also be checked directly. Alignment values are checked against paper-derived references. Hydrogen bond survival R² must meet a minimum threshold (fits of sufficient quality), and tau values are compared within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ds_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "ds_energy_above_vbm_eV",
          "vbm_cbm_gap_eV"
        ],
        "units": {
          "time_ps": "picoseconds",
          "ds_energy_above_vbm_eV": "eV",
          "vbm_cbm_gap_eV": "eV"
        }
      },
      "description": "Time series of defect state energy above VBM and VBM-CBM gap for each snapshot. Checker will compute segment-wise means and standard deviations and compare to hidden paper reference values with tolerance."
    },
    {
      "file": "ds_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "segment",
          "mean_ds_energy_eV",
          "std_ds_energy_eV",
          "mean_vbm_cbm_gap_eV",
          "std_vbm_cbm_gap_eV"
        ],
        "units": {
          "mean_ds_energy_eV": "eV",
          "std_ds_energy_eV": "eV",
          "mean_vbm_cbm_gap_eV": "eV",
          "std_vbm_cbm_gap_eV": "eV"
        }
      },
      "description": "Segment-wise summary statistics of defect state energy and band gap. Checker compares directly to hidden reference values with tolerance."
    },
    {
      "file": "ds_alignment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "vbm_vs_rhe_eV",
          "ds_mean_vs_rhe_eV",
          "ds_std_vs_rhe_eV",
          "offset_from_oer_eV"
        ],
        "units": {
          "vbm_vs_rhe_eV": "eV",
          "ds_mean_vs_rhe_eV": "eV",
          "ds_std_vs_rhe_eV": "eV",
          "offset_from_oer_eV": "eV"
        }
      },
      "description": "Aligned VBM and defect state energy on the electrochemical scale. Checker compares values to hidden paper reference with tolerance."
    },
    {
      "file": "hbond_survival.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface_type",
          "bond_type",
          "tau_ps",
          "r_squared"
        ],
        "units": {
          "tau_ps": "picoseconds",
          "r_squared": "unitless"
        }
      },
      "description": "Hydrogen bond survival times and exponential fit R² for different surface and bond types. Checker verifies that R² exceeds a threshold and that tau values are within tolerance of hidden paper reference."
    }
  ],
  "notes": "The primary verification is recomputation of summary statistics from ds_energies.csv and comparison to reference values; ds_summary.csv is a convenience artifact that may also be checked directly. Alignment values are checked against paper-derived references. Hydrogen bond survival R² must meet a minimum threshold (fits of sufficient quality), and tau values are compared within tolerance."
}
```

## How you are scored
A hidden verifier will independently examine each of your submitted output files. For the DS energy and band gap data, the verifier will recompute the segment-wise means and standard deviations from your `ds_energies.csv` and compare them to hidden reference values (derived from the original study). The `ds_summary.csv` file will be checked directly against the same references. The alignment results in `ds_alignment.json` will be compared to reference aligned energies. For `hbond_survival.csv`, the verifier will verify that the exponential fits are of acceptable quality (R² exceeding a threshold) and that the reported characteristic times are within tolerance of the reference values. A structural check will also confirm that the number of snapshots per segment is correct. Each scored artifact contributes a weight to the final reward; reporting numbers without executing the computational workflow will not pass the verifier's checks.
