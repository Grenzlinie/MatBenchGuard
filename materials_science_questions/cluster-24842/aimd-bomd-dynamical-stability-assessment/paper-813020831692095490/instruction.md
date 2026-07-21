# DFT-MD and Metadynamics of a Palladium-Chromium Hemichelate Complex

## Problem background
This task addresses the dynamical behaviour of a palladium–chromium hemichelate complex composed of a (η³-2-methylallyl)Pd cation bonded to a (η⁶-indenyl)tricarbonylchromium anion. The complex is known to be highly fluxional in solution, but the relative rates and coupling between its intramolecular motions are not fully characterised. Three motions are of primary interest: (i) slippage of the indenyl ligand between η¹ and η³ coordination to Pd, (ii) rotation of the Cr(CO)₃ tripod about the arene–metal axis, and (iii) rotation of the 2‑methylallyl ligand. The goal is to quantify the free energy barriers for these processes and to characterise the short‑timescale dynamics of the η¹ isomer.

## Approach
The approach uses density functional theory molecular dynamics (DFT‑MD) and well‑tempered metadynamics (MTD) simulations performed with the CP2K package. All simulations employ the PBE‑D3 functional, GTH pseudopotentials, a TZV2P basis set, and a 323 K NVT ensemble. First, unbiased 100 ps DFT‑MD runs are performed for the η¹‑3b₁ isomer (starting from its X‑ray structure) and the syn η³‑3b₁ isomer (starting from an optimised geometry). These trajectories are analysed to extract collective variables (CVs) that track key geometrical changes, including the rocking motion of the CO ligands and the η³→η¹ conversion. Second, three two‑dimensional metadynamics simulations are launched from a pre‑equilibrated snapshot to accelerate rare events: one sampling the CVs for indenyl slippage, one for slippage plus Cr(CO)₃ rotation, and one for slippage plus 2‑methylallyl rotation. Free energy surfaces are computed from the accumulated hills, and minimum‑energy‑path analyses yield the relevant free energy barriers.

## Reproduction target
The task is to produce the following scored artifacts under /app/outputs:

- **free_energy_barriers.json**: three free energy barriers (kcal mol⁻¹) extracted from the metadynamics runs — indenyl slippage, Cr(CO)₃ rotation, and 2‑methylallyl rotation.
- **eta1_3b1_CV5_timeseries.csv**: time series of CV5 = d(Pd‑C22) − d(Pd‑C21) over the 100 ps unbiased MD of η¹‑3b₁, capturing the carbonyl rocking motion.
- **eta1_3b1_md_summary.json**: average CV1–CV6 values from that trajectory and a boolean indicating whether a full Cr(CO)₃ rotation occurred.
- **eta3_3b1_md_summary.json**: conversion time and average CV1 before/after the spontaneous η³→η¹ transformation observed in the unbiased MD of syn η³‑3b₁.

All quantities are to be computed directly from the simulations; the task is complete when each artifact is written.

## Assets

- CP2K: https://www.cp2k.org
- X-ray structure of eta1-3b1 (CCDC CEWNUP): https://www.ccdc.cam.ac.uk/structures/search?Identifier=CEWNUP

## Workflow steps

### Step 1: Prepare initial structures
- Role: process
- Action: Obtain the CIF file for CCDC CEWNUP X-ray structure of eta1-3b1, convert to CP2K coordinate format. Build a starting geometry for syn eta3-3b1 by modifying the eta1 structure to an eta3 indenyl coordination and perform a short DFT geometry optimization with CP2K (PBE-D3/GTH). Save the optimized geometry as optimized_eta3_3b1.xyz.
- Evidence: `/app/outputs/optimized_eta3_3b1.xyz`

### Step 2: Run unbiased DFT-MD of eta1-3b1 (MD2)
- Role: process
- Action: Run a 100 ps unbiased ab initio molecular dynamics (DFT-MD) simulation of eta1-3b1 at 323 K using CP2K with PBE-D3 functional, TZV2P basis set, GTH pseudopotentials, 0.5 fs time step, cubic box of 18.5 Angstrom, NVT ensemble, starting from the CEWNUP structure. Save the full trajectory as eta1_3b1_trajectory.xyz.
- Evidence: `/app/outputs/eta1_3b1_trajectory.xyz`

### Step 3: Extract CV5 time series from eta1-3b1 MD
- Role: scored
- Action: From eta1_3b1_trajectory.xyz, compute CV5 = d(Pd-C22) - d(Pd-C21) at every saved time step and write eta1_3b1_CV5_timeseries.csv.
- Output file: `/app/outputs/eta1_3b1_CV5_timeseries.csv`
- Format: csv
- Contract: time_ps: float, CV5_angstrom: float
- Scoring: scored by hidden verifier

### Step 4: Compute summary from eta1-3b1 MD
- Role: scored
- Action: From eta1_3b1_trajectory.xyz, compute the time-averaged values of CV1–CV6 over the full 100 ps and determine whether a full Cr(CO)3 rotation occurred (full_cr_rotation_observed, boolean). Write the results to eta1_3b1_md_summary.json.
- Output file: `/app/outputs/eta1_3b1_md_summary.json`
- Format: json
- Contract: {"average_CV1": float, "average_CV2": float, "average_CV3": float, "average_CV4": float, "average_CV5": float, "average_CV6": float, "full_cr_rotation_observed": bool}
- Scoring: scored by hidden verifier

### Step 5: Run unbiased DFT-MD of syn eta3-3b1 (MD3)
- Role: process
- Action: Run a 100 ps unbiased DFT-MD simulation of syn eta3-3b1 at 323 K with the same CP2K settings as for eta1-3b1, starting from the optimized geometry optimized_eta3_3b1.xyz. Save the trajectory as eta3_3b1_trajectory.xyz.
- Evidence: `/app/outputs/eta3_3b1_trajectory.xyz`

### Step 6: Analyze eta3-3b1 MD conversion
- Role: scored
- Action: From eta3_3b1_trajectory.xyz, determine the simulation time at which CV1 = d(Pd-C11)-d(Pd-C14) becomes persistently negative (conversion_time_ps). Compute the average CV1 before and after this time. Write the results to eta3_3b1_md_summary.json.
- Output file: `/app/outputs/eta3_3b1_md_summary.json`
- Format: json
- Contract: {"conversion_time_ps": float, "average_CV1_before": float, "average_CV1_after": float}
- Scoring: scored by hidden verifier

### Step 7: Extract pre-equilibration snapshot
- Role: process
- Action: From eta1_3b1_trajectory.xyz, extract the atomic configuration at time 30 ps. Save as equil_30ps.xyz. This will be the starting point for all metadynamics simulations.
- Evidence: `/app/outputs/equil_30ps.xyz`

### Step 8: Metadynamics MTD1: indenyl slippage
- Role: process
- Action: Run a well-tempered metadynamics simulation with CP2K using active collective variables CV1 and CV2. Use Gaussian hills of height 0.5 kcal/mol added every 80 fs, widths 0.05 Angstrom (CV1) and 0.1 (CV2). Start from equil_30ps.xyz. Simulate until convergence (e.g., 12,500 hills, ~500 ps). Output the free energy surface data as fes_mtd1.dat.
- Evidence: `/app/outputs/fes_mtd1.dat`

### Step 9: Metadynamics MTD2: slippage + Cr rotation
- Role: process
- Action: Run a well-tempered metadynamics simulation with active CV1 and CV4. Use the same hill parameters as MTD1; width for CV4 is 2.5 degrees. Start from equil_30ps.xyz, simulate 12,500 hills. Output fes_mtd2.dat.
- Evidence: `/app/outputs/fes_mtd2.dat`

### Step 10: Metadynamics MTD3: slippage + allyl rotation
- Role: process
- Action: Run a well-tempered metadynamics simulation with active CV1 and CV6. Hill width for CV6 is 3.75 degrees. Simulate 12,500 hills. Output fes_mtd3.dat.
- Evidence: `/app/outputs/fes_mtd3.dat`

### Step 11: Extract free energy barriers
- Role: scored (load-bearing)
- Action: From the free energy surfaces fes_mtd1.dat, fes_mtd2.dat, fes_mtd3.dat, compute the minimum free energy paths and extract the free energy barriers (in kcal/mol) for: indenyl ring slippage (eta1->eta3 from MTD1), Cr(CO)3 rotation (highest barrier in MTD2), and 2-methylallyl rotation (coupled pathway from MTD3). Write the three barriers to free_energy_barriers.json.
- Output file: `/app/outputs/free_energy_barriers.json`
- Format: json
- Contract: {"indenyl_slippage_deltaG_kcal_mol": float, "cr_co3_rotation_deltaG_kcal_mol": float, "allyl_rotation_deltaG_kcal_mol": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eta1_3b1_CV5_timeseries.csv`
- `/app/outputs/eta1_3b1_md_summary.json`
- `/app/outputs/eta3_3b1_md_summary.json`
- `/app/outputs/free_energy_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eta1_3b1_CV5_timeseries.csv
- path: `/app/outputs/eta1_3b1_CV5_timeseries.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of CV5 = d(Pd-C22)-d(Pd-C21) over the 100 ps unbiased DFT-MD of eta1-3b1. Checker will recompute average and oscillation amplitude and compare against paper reference.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `CV5_angstrom`
  - `units`:
    - `time_ps`: ps
    - `CV5_angstrom`: angstrom

### eta1_3b1_md_summary.json
- path: `/app/outputs/eta1_3b1_md_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Summary of averaged collective variables and whether full Cr(CO)3 rotation occurred during the eta1-3b1 MD simulation.
- schema:
  - `type`: object
  - `required`: `average_CV1`, `average_CV2`, `average_CV3`, `average_CV4`, `average_CV5`, `average_CV6`, `full_cr_rotation_observed`
  - `properties`:
    - `average_CV1`:
      - `type`: float
      - `unit`: angstrom
    - `average_CV2`:
      - `type`: float
      - `unit`: none
    - `average_CV3`:
      - `type`: float
      - `unit`: angstrom
    - `average_CV4`:
      - `type`: float
      - `unit`: degree
    - `average_CV5`:
      - `type`: float
      - `unit`: angstrom
    - `average_CV6`:
      - `type`: float
      - `unit`: degree
    - `full_cr_rotation_observed`:
      - `type`: boolean

### eta3_3b1_md_summary.json
- path: `/app/outputs/eta3_3b1_md_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Summary of the eta3->eta1 conversion observed in the MD simulation of syn eta3-3b1.
- schema:
  - `type`: object
  - `required`: `conversion_time_ps`, `average_CV1_before`, `average_CV1_after`
  - `properties`:
    - `conversion_time_ps`:
      - `type`: float
      - `unit`: ps
    - `average_CV1_before`:
      - `type`: float
      - `unit`: angstrom
    - `average_CV1_after`:
      - `type`: float
      - `unit`: angstrom

### free_energy_barriers.json
- path: `/app/outputs/free_energy_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Free energy barriers extracted from the metadynamics simulations.
- schema:
  - `type`: object
  - `required`: `indenyl_slippage_deltaG_kcal_mol`, `cr_co3_rotation_deltaG_kcal_mol`, `allyl_rotation_deltaG_kcal_mol`
  - `properties`:
    - `indenyl_slippage_deltaG_kcal_mol`:
      - `type`: float
      - `unit`: kcal/mol
    - `cr_co3_rotation_deltaG_kcal_mol`:
      - `type`: float
      - `unit`: kcal/mol
    - `allyl_rotation_deltaG_kcal_mol`:
      - `type`: float
      - `unit`: kcal/mol

Notes: All output files must be placed under /app/outputs. The hidden checker compares the agent's reported numbers to paper reference values using tolerances appropriate for the method (e.g., ±2 kcal/mol for free energy barriers).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eta1_3b1_CV5_timeseries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "CV5_angstrom"
        ],
        "units": {
          "time_ps": "ps",
          "CV5_angstrom": "angstrom"
        }
      },
      "description": "Time series of CV5 = d(Pd-C22)-d(Pd-C21) over the 100 ps unbiased DFT-MD of eta1-3b1. Checker will recompute average and oscillation amplitude and compare against paper reference."
    },
    {
      "file": "eta1_3b1_md_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "average_CV1",
          "average_CV2",
          "average_CV3",
          "average_CV4",
          "average_CV5",
          "average_CV6",
          "full_cr_rotation_observed"
        ],
        "properties": {
          "average_CV1": {
            "type": "float",
            "unit": "angstrom"
          },
          "average_CV2": {
            "type": "float",
            "unit": "none"
          },
          "average_CV3": {
            "type": "float",
            "unit": "angstrom"
          },
          "average_CV4": {
            "type": "float",
            "unit": "degree"
          },
          "average_CV5": {
            "type": "float",
            "unit": "angstrom"
          },
          "average_CV6": {
            "type": "float",
            "unit": "degree"
          },
          "full_cr_rotation_observed": {
            "type": "boolean"
          }
        }
      },
      "description": "Summary of averaged collective variables and whether full Cr(CO)3 rotation occurred during the eta1-3b1 MD simulation."
    },
    {
      "file": "eta3_3b1_md_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "conversion_time_ps",
          "average_CV1_before",
          "average_CV1_after"
        ],
        "properties": {
          "conversion_time_ps": {
            "type": "float",
            "unit": "ps"
          },
          "average_CV1_before": {
            "type": "float",
            "unit": "angstrom"
          },
          "average_CV1_after": {
            "type": "float",
            "unit": "angstrom"
          }
        }
      },
      "description": "Summary of the eta3->eta1 conversion observed in the MD simulation of syn eta3-3b1."
    },
    {
      "file": "free_energy_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "indenyl_slippage_deltaG_kcal_mol",
          "cr_co3_rotation_deltaG_kcal_mol",
          "allyl_rotation_deltaG_kcal_mol"
        ],
        "properties": {
          "indenyl_slippage_deltaG_kcal_mol": {
            "type": "float",
            "unit": "kcal/mol"
          },
          "cr_co3_rotation_deltaG_kcal_mol": {
            "type": "float",
            "unit": "kcal/mol"
          },
          "allyl_rotation_deltaG_kcal_mol": {
            "type": "float",
            "unit": "kcal/mol"
          }
        }
      },
      "description": "Free energy barriers extracted from the metadynamics simulations."
    }
  ],
  "notes": "All output files must be placed under /app/outputs. The hidden checker compares the agent's reported numbers to paper reference values using tolerances appropriate for the method (e.g., ±2 kcal/mol for free energy barriers)."
}
```

## How you are scored
A hidden verifier scores each ‘scored’ workflow stage independently. The verifier reads the output files you write and compares the quantities you report against reference values using appropriate tolerances. The per‑stage scores are then combined into a single final reward. The reward reflects the accuracy of your computed results, not merely the presence of the files. Presenting numbers without actually running the simulations will not yield a passing score.
