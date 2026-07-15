# MLP-MD Simulation of CaH₂ Hydrogenation via Surface Melting

## Problem background
Superhydrides with high hydrogen-to-metal (H/M) ratios are promising candidates for high-temperature superconductivity, but their synthesis requires extreme pressures and temperatures. The initial stages of hydrogenation — how a metal hydride absorbs hydrogen to form a superhydride — are not well understood. Calcium hydride (CaH2) is a simple ionic hydride whose further hydrogenation would yield the superhydride CaH4, yet whether and how this transformation proceeds is an open question. This task investigates the atomic-scale mechanism of CaH2 hydrogenation in contact with dense H2, aiming to clarify the role of surface melting and the thermodynamic factors that govern superhydride formation under pressure.

## Approach
The mechanism is probed using machine-learning potential molecular dynamics (MLP-MD). A deep neural network interatomic potential for the Ca–H system is first trained on density functional theory (DFT) reference data. Interface models are then built: CaH2 slabs with exposed (100) or (010) surfaces are brought into contact with high‑pressure H2, and bulk cells of CaH4 and CaH2+H2 mixtures are prepared. NPT MD simulations are run with the trained MLP under a matrix of pressures (10–50 GPa) and temperatures (1200 K and 1500 K). From these trajectories the H/M ratio is tracked over time, the local Ca‑sublattice ordering is analyzed with adaptive common neighbor analysis (a‑CNA), and the hydrogen atom environments are characterized by persistent homology diagrams. Separate bulk enthalpy simulations provide the data to compute pressure‑dependent reaction enthalpies.

## Reproduction target
Compute the following five scored artifacts, which together capture the key observables of the hydrogenation process:

1. **step_01_HM_vs_time.csv** – H/M ratio as a function of time for the CaH2(100)/H2 interface at 1500 K and 40 GPa.
2. **step_02_aCNA.csv** – fractions of hcp, fcc, and other Ca environments from the same trajectory and after quenching the final configuration to 300 K.
3. **step_03_persistence_diagram.json** – persistent homology ring features (birth‑death pairs) for H atoms near the interface (1500 K and 1200 K, 40 GPa) and for bulk CaH4 at 1500 K and 40 GPa.
4. **step_04_HM_vs_pressure.csv** – final H/M ratios after 1 ns for (100) and (010) surfaces at 1500 K and 1200 K, for pressures 10, 20, 30, 40, and 50 GPa.
5. **step_05_enthalpy_vs_pressure.csv** – pressure‑dependent enthalpy differences: ΔH_fus (CaH4 fusion) and ΔH_fus+ΔH_hyd (formation of liquid CaH4 from CaH2 + H2).

The assembled results must demonstrate, when evaluated by the hidden verifier, whether hydrogenation occurs, under which conditions, what structural intermediate forms, and how pressure influences the reaction thermodynamics.

## Assets

- DeePMD-kit: https://github.com/deepmodeling/deepmd-kit
- LAMMPS: https://www.lammps.org
- HomCloud: https://github.com/iobayashi/HomCloud
- Quantum ESPRESSO: https://www.quantum-espresso.org
- OVITO: https://www.ovito.org

## Workflow steps

### Step 1: Generate DFT training data for Ca-H system
- Role: process
- Action: Use a DFT code (e.g., Quantum ESPRESSO) to compute energies and forces for a diverse set of Ca-H configurations to build a reference dataset for MLP training.
- Evidence: `/app/outputs/dft_training_data.npz`

### Step 2: Train Ca-H machine-learning potential
- Role: process
- Action: Train a deep neural network potential for the Ca-H system using DeePMD-kit on the generated DFT dataset.
- Evidence: `/app/outputs/frozen_model.pb`

### Step 3: Build simulation cells
- Role: process
- Action: Construct interface simulation cells for CaH₂(100)/H₂, CaH₂(010)/H₂, and bulk cells for CaH₄ and CaH₂+H₂ at various pressures and compositions.
- Evidence: `/app/outputs/initial_configs.zip`

### Step 4: Run interface MLP-MD simulations
- Role: process
- Action: Perform NPT MLP-MD simulations for the CaH₂(100)/H₂ and CaH₂(010)/H₂ interfaces with the trained MLP. Run baseline: (100) at 1500 K, 40 GPa for ≥200 ps; additional trajectories: (100) at 1200 K, 40 GPa; and pressure scans at 10, 20, 30, 40, 50 GPa for both surfaces at 1500 K and 1200 K, each for 1 ns.
- Evidence: `/app/outputs/interface_md_logs.zip`

### Step 5: Run bulk MLP-MD simulations for enthalpy data
- Role: process
- Action: Perform short (100 ps) NPT simulations of bulk CaH₄ and bulk CaH₂+H₂ at several temperatures to obtain time-averaged enthalpies.
- Evidence: `/app/outputs/bulk_enthalpy_logs.zip`

### Step 6: Run bulk CaH₄ MD for reference persistent homology
- Role: process
- Action: Run an MLP-MD simulation of bulk CaH₄ at 1500 K, 40 GPa for a sufficiently long time to serve as reference for persistent homology comparison.
- Evidence: `/app/outputs/bulk_CaH4_trajectory.dcd`

### Step 7: Quench final hydrogenated configuration
- Role: process
- Action: Cool the final atomic configuration from the 1500 K CaH₂(100)/H₂ simulation to 300 K to reduce thermal noise and obtain a better estimate of the fcc Ca fraction.
- Evidence: `/app/outputs/quenched_config.xyz`

### Step 8: Extract H/M ratio time series
- Role: scored
- Action: Compute hydrogen-to-metal ratio (H/M) as a function of time from the CaH₂(100)/H₂ interface simulation at 1500 K, 40 GPa and write the time series.
- Output file: `/app/outputs/step_01_HM_vs_time.csv`
- Format: csv
- Contract: CSV with columns: time_ps (float), HM_ratio (float).
- Scoring: scored by hidden verifier

### Step 9: Perform a-CNA analysis on Ca sublattice
- Role: scored
- Action: Run adaptive common neighbor analysis on Ca atoms for the 1500 K, 40 GPa interface trajectory and for the quenched configuration. Output the time series of hcp, fcc, and others fractions.
- Output file: `/app/outputs/step_02_aCNA.csv`
- Format: csv
- Contract: CSV with columns: time_ps (float), hcp_frac (float), fcc_frac (float), others_frac (float).
- Scoring: scored by hidden verifier

### Step 10: Compute persistence diagrams
- Role: scored (load-bearing)
- Action: Calculate time-averaged persistence diagrams for H atoms near the interface (within 3 Å of Ca) using HomCloud for the 1500 K, 40 GPa and 1200 K, 40 GPa trajectories, and for bulk CaH₄ at 1500 K, 40 GPa. Output the coordinates of ring features.
- Output file: `/app/outputs/step_03_persistence_diagram.json`
- Format: json
- Contract: JSON object with keys: 'simulation_conditions': {T, P, surface}, 'persistence_pairs': list of [birth, death] for H atoms within 3 Å of Ca (time-averaged 25-160 ps), 'reference_bulk_CaH4': list of [birth, death] for bulk CaH₄ at same conditions.
- Scoring: scored by hidden verifier

### Step 11: Compile pressure-dependent H/M ratio
- Role: scored
- Action: Assemble the final H/M ratio after 1 ns from all pressure-scan interface simulations and produce a summary table.
- Output file: `/app/outputs/step_04_HM_vs_pressure.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), temperature_K (int), surface (string: '100' or '010'), HM_ratio (float).
- Scoring: scored by hidden verifier

### Step 12: Compute reaction enthalpies
- Role: scored
- Action: From the bulk enthalpy runs, extrapolate to 0 K and calculate ΔH_fus (CaH₄ fusion) and ΔH_fus+ΔH_hyd (formation of liquid CaH₄ from CaH₂ + H₂) as functions of pressure.
- Output file: `/app/outputs/step_05_enthalpy_vs_pressure.csv`
- Format: csv
- Contract: CSV with columns: pressure_GPa (float), delta_H_fus (float, eV/atom), delta_H_fus_plus_hyd (float, eV/atom).
- Scoring: scored by hidden verifier

### Step 13: Optional: DFT surface energy calculation
- Role: process
- Action: Perform DFT calculations of CaH₂(100) and (010) slabs in vacuum to compute surface energies, providing context for surface selectivity (not required for main scoring).
- Evidence: `/app/outputs/surface_energy_results.txt`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_HM_vs_time.csv`
- `/app/outputs/step_02_aCNA.csv`
- `/app/outputs/step_03_persistence_diagram.json`
- `/app/outputs/step_04_HM_vs_pressure.csv`
- `/app/outputs/step_05_enthalpy_vs_pressure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_HM_vs_time.csv
- path: `/app/outputs/step_01_HM_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Time evolution of the hydrogen-to-metal ratio during the CaH₂(100)/H₂ MLP-MD simulation at 1500 K and 40 GPa.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `HM_ratio`
  - `units`:
    - `time_ps`: picosecond
    - `HM_ratio`: dimensionless

### step_02_aCNA.csv
- path: `/app/outputs/step_02_aCNA.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Adaptive common neighbor analysis of the Ca sublattice during the same simulation; the quenched fcc fraction is derived from this time series or its tail.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `hcp_frac`, `fcc_frac`, `others_frac`
  - `units`:
    - `time_ps`: picosecond
    - `hcp_frac`: fraction
    - `fcc_frac`: fraction
    - `others_frac`: fraction

### step_03_persistence_diagram.json
- path: `/app/outputs/step_03_persistence_diagram.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Time-averaged persistence diagram ring features for the hydrogenating condition and reference bulk CaH₄.
- schema:
  - `type`: object
  - `required`: `simulation_conditions`, `persistence_pairs`, `reference_bulk_CaH4`
  - `items`:
    - `persistence_pairs`: [birth, death]

### step_04_HM_vs_pressure.csv
- path: `/app/outputs/step_04_HM_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Final H/M ratio after 1 ns for each pressure-scan condition.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `temperature_K`, `surface`, `HM_ratio`
  - `units`:
    - `pressure_GPa`: GPa
    - `temperature_K`: K
    - `surface`: categorical (100 or 010)
    - `HM_ratio`: dimensionless

### step_05_enthalpy_vs_pressure.csv
- path: `/app/outputs/step_05_enthalpy_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pressure-dependent fusion enthalpy of CaH₄ and formation enthalpy of liquid CaH₄ from CaH₂ + H₂.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `delta_H_fus`, `delta_H_fus_plus_hyd`
  - `units`:
    - `pressure_GPa`: GPa
    - `delta_H_fus`: eV/atom
    - `delta_H_fus_plus_hyd`: eV/atom

Notes: All scored outputs are compared against hidden reference thresholds or structural relations derived from the paper. Agent must execute the full pipeline (DFT, MLP training, MD) to produce correct artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_HM_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "HM_ratio"
        ],
        "units": {
          "time_ps": "picosecond",
          "HM_ratio": "dimensionless"
        }
      },
      "description": "Time evolution of the hydrogen-to-metal ratio during the CaH₂(100)/H₂ MLP-MD simulation at 1500 K and 40 GPa."
    },
    {
      "file": "step_02_aCNA.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "hcp_frac",
          "fcc_frac",
          "others_frac"
        ],
        "units": {
          "time_ps": "picosecond",
          "hcp_frac": "fraction",
          "fcc_frac": "fraction",
          "others_frac": "fraction"
        }
      },
      "description": "Adaptive common neighbor analysis of the Ca sublattice during the same simulation; the quenched fcc fraction is derived from this time series or its tail."
    },
    {
      "file": "step_03_persistence_diagram.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "simulation_conditions",
          "persistence_pairs",
          "reference_bulk_CaH4"
        ],
        "items": {
          "persistence_pairs": "[birth, death]"
        }
      },
      "description": "Time-averaged persistence diagram ring features for the hydrogenating condition and reference bulk CaH₄."
    },
    {
      "file": "step_04_HM_vs_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "temperature_K",
          "surface",
          "HM_ratio"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "temperature_K": "K",
          "surface": "categorical (100 or 010)",
          "HM_ratio": "dimensionless"
        }
      },
      "description": "Final H/M ratio after 1 ns for each pressure-scan condition."
    },
    {
      "file": "step_05_enthalpy_vs_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "delta_H_fus",
          "delta_H_fus_plus_hyd"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "delta_H_fus": "eV/atom",
          "delta_H_fus_plus_hyd": "eV/atom"
        }
      },
      "description": "Pressure-dependent fusion enthalpy of CaH₄ and formation enthalpy of liquid CaH₄ from CaH₂ + H₂."
    }
  ],
  "notes": "All scored outputs are compared against hidden reference thresholds or structural relations derived from the paper. Agent must execute the full pipeline (DFT, MLP training, MD) to produce correct artifacts."
}
```

## How you are scored
A hidden verifier independently scores each artifact against reference criteria derived from the paper’s reported findings. For example:
- The H/M time series is checked for reaching a sufficiently high value within a specific time window (threshold‑or‑better).
- The a‑CNA fractions are checked for attaining the expected fcc fraction after quenching.
- The persistence diagram ring features are compared to the reference ring features of bulk CaH4 (reference_match).
- The pressure‑scan H/M ratios are checked for monotonic trends and surface selectivity (threshold‑or‑better).
- The enthalpy differences are checked for the required relative ordering at high pressure (structural_audit).

Each artifact carries a weight, and the final reward is a weighted sum over the five scored outputs. Merely reporting numbers without genuinely executing the MLP‑MD pipeline will not satisfy the verifier’s criteria.
