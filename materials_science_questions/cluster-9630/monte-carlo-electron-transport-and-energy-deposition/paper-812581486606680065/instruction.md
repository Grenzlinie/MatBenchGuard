# Monte Carlo Simulation of Electronuclear vs Photonuclear Mo-99 Production Yields

## Problem background
The medical isotope 99mTc, used in about 85% of nuclear medicine diagnostic procedures, is obtained from its parent 99Mo. Accelerator-based production of 99Mo via photonuclear (γ,n) reactions on 100Mo is a promising approach that avoids highly enriched uranium. In the one-stage irradiation scheme, the 100Mo target itself acts as the bremsstrahlung converter, so the direct electron beam may also cause electronuclear (e⁻,e'⁻n) reactions that produce additional 99Mo. The relative importance of this electronuclear channel compared to the photonuclear one is not well established for the electron beam energies (30–50 MeV) commonly used for radioisotope production. Monte Carlo simulations can quantify the two production channels and determine under which target conditions the electronuclear contribution becomes significant.

## Approach
Use the GEANT4 simulation toolkit (version 10.6.p1 or compatible) to model a cylindrical 100Mo target (radius 3.85 mm, density 10.22 g/cm³) irradiated by a monoenergetic electron pencil beam. The photonuclear channel is described by the LEND (Low Energy Nuclear Data) model, which relies on evaluated ENDF/B-VII.1 data, while the electronuclear channel is modeled through the equivalent photon approximation (EPA). Two main target configurations are studied: a thick (20 mm) target and a thin (1 mm) target, each bombarded at five beam energies (30, 35, 40, 45, 50 MeV). For each configuration, the photonuclear and electronuclear 99Mo yields per primary electron are recorded in depth bins (1 mm bins for the thick target; 0.1 mm bins for the thin target). The thick-target yields are then integrated over the full target length to obtain total yields per energy. Additionally, at the single beam energy of 40 MeV, targets of varying thickness (0.1, 0.5, 1, 2, 5, 10, 20 mm) are simulated to compute the fraction of the total yield that originates from electronuclear reactions.

## Reproduction target
Produce the following four CSV files by executing the GEANT4 simulations and the subsequent analysis steps:

1. Depth-resolved photonuclear and electronuclear 99Mo yields (per primary electron) for the 20 mm thick target at beam energies 30, 35, 40, 45, and 50 MeV, with 1 mm depth bins.
2. Depth-resolved yields for the 1 mm thin target at the same five energies, with 0.1 mm depth bins.
3. Volume-integrated total yields for the 20 mm target at each beam energy, together with the total electronuclear-to-photonuclear ratio.
4. For the 40 MeV beam only, the total photonuclear and electronuclear yields and the electronuclear fraction (electronuclear / (electronuclear + photonuclear)) as a function of target thickness (0.1, 0.5, 1, 2, 5, 10, 20 mm).

All files must follow the exact column schemas and units described in the workflow steps and output contract.

## Assets

- GEANT4 simulation toolkit: https://geant4.web.cern.ch/

## Workflow steps

### Step 1: Thick target Monte Carlo simulation
- Role: scored (load-bearing)
- Action: Simulate a 20 mm thick cylindrical 100Mo target (radius 3.85 mm, density 10.22 g/cm³) irradiated by a monoenergetic electron pencil beam at energies 30, 35, 40, 45, 50 MeV. Use GEANT4 with LEND photonuclear and EPA electronuclear models. Record the photonuclear and electronuclear 99Mo yields per primary electron in 1 mm depth bins (0–1 mm, 1–2 mm, ..., 19–20 mm).
- Output file: `/app/outputs/thick_target_depth_yields.csv`
- Format: csv
- Contract: energy_MeV (float), depth_mm (float, bin start, e.g., 0, 1, ..., 19), photonuclear_yield_per_e (float), electronuclear_yield_per_e (float), ratio (float, electronuclear/photonuclear if photonuclear>0, else 0)
- Scoring: scored by hidden verifier

### Step 2: Thin target Monte Carlo simulation
- Role: scored (load-bearing)
- Action: Simulate a 1 mm thick 100Mo target (same radius and density) for the same five energies. Record yields in 0.1 mm depth bins (0-0.1 mm, ..., 0.9-1.0 mm). Use the same GEANT4 physics configuration.
- Output file: `/app/outputs/thin_target_depth_yields.csv`
- Format: csv
- Contract: energy_MeV (float), depth_mm (float, bin start, e.g., 0, 0.1, ..., 0.9), photonuclear_yield_per_e (float), electronuclear_yield_per_e (float), ratio (float)
- Scoring: scored by hidden verifier

### Step 3: Compute thick target integrated yields
- Role: scored
- Action: From the thick_target_depth_yields.csv, integrate over the full 20 mm thickness (sum bins) to obtain the total photonuclear and electronuclear yields per primary electron for each energy. Compute the total ratio.
- Output file: `/app/outputs/thick_target_total_yields.csv`
- Format: csv
- Contract: energy_MeV (float), total_photonuclear_yield_per_e (float), total_electronuclear_yield_per_e (float), ratio_total (float)
- Scoring: scored by hidden verifier

### Step 4: Fraction of electronuclear yield vs target thickness at 40 MeV
- Role: scored (load-bearing)
- Action: Simulate 100Mo targets of thicknesses 0.1, 0.5, 1, 2, 5, 10, 20 mm (same radius and density) irradiated by a 40 MeV electron beam. For each thickness, record the total photonuclear and electronuclear yields per primary electron. Compute the fraction of electronuclear yield (electronuclear / (electronuclear + photonuclear)).
- Output file: `/app/outputs/fraction_vs_thickness.csv`
- Format: csv
- Contract: thickness_mm (float), total_photonuclear_yield_per_e (float), total_electronuclear_yield_per_e (float), fraction_electronuclear (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thick_target_depth_yields.csv`
- `/app/outputs/thin_target_depth_yields.csv`
- `/app/outputs/thick_target_total_yields.csv`
- `/app/outputs/fraction_vs_thickness.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thick_target_depth_yields.csv
- path: `/app/outputs/thick_target_depth_yields.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Depth-resolved 99Mo yields for the thick 20 mm target at five beam energies. Used to verify monotonic decrease of electronuclear yield, buildup of photonuclear yield, and ratio thresholds in first and later bins.
- schema:
  - `type`: table
  - `required_columns`: `energy_MeV`, `depth_mm`, `photonuclear_yield_per_e`, `electronuclear_yield_per_e`, `ratio`
  - `units`:
    - `energy_MeV`: MeV
    - `depth_mm`: mm
    - `photonuclear_yield_per_e`: per primary electron
    - `electronuclear_yield_per_e`: per primary electron
    - `ratio`: dimensionless

### thin_target_depth_yields.csv
- path: `/app/outputs/thin_target_depth_yields.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Depth-resolved 99Mo yields for the thin 1 mm target at five beam energies. Used to verify ratio ~0.2 at 1 mm depth and linear trends.
- schema:
  - `type`: table
  - `required_columns`: `energy_MeV`, `depth_mm`, `photonuclear_yield_per_e`, `electronuclear_yield_per_e`, `ratio`
  - `units`:
    - `energy_MeV`: MeV
    - `depth_mm`: mm
    - `photonuclear_yield_per_e`: per primary electron
    - `electronuclear_yield_per_e`: per primary electron
    - `ratio`: dimensionless

### thick_target_total_yields.csv
- path: `/app/outputs/thick_target_total_yields.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Volume-integrated yields over the entire 20 mm target. The total ratio is compared to ~0.01 with thresholds.
- schema:
  - `type`: table
  - `required_columns`: `energy_MeV`, `total_photonuclear_yield_per_e`, `total_electronuclear_yield_per_e`, `ratio_total`
  - `units`:
    - `energy_MeV`: MeV
    - `total_photonuclear_yield_per_e`: per primary electron
    - `total_electronuclear_yield_per_e`: per primary electron
    - `ratio_total`: dimensionless

### fraction_vs_thickness.csv
- path: `/app/outputs/fraction_vs_thickness.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total yields and electronuclear fraction for thicknesses 0.1–20 mm at 40 MeV. Key thresholds: at 1 mm fraction ~0.20, at 0.1 mm >0.65.
- schema:
  - `type`: table
  - `required_columns`: `thickness_mm`, `total_photonuclear_yield_per_e`, `total_electronuclear_yield_per_e`, `fraction_electronuclear`
  - `units`:
    - `thickness_mm`: mm
    - `total_photonuclear_yield_per_e`: per primary electron
    - `total_electronuclear_yield_per_e`: per primary electron
    - `fraction_electronuclear`: dimensionless

Notes: All yields are reported per primary electron. Depth bins for thick target are 1 mm wide; for thin target 0.1 mm wide. The checker performs structural audits on the depth profiles and threshold comparisons on ratios and fractions. Tolerances are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thick_target_depth_yields.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_MeV",
          "depth_mm",
          "photonuclear_yield_per_e",
          "electronuclear_yield_per_e",
          "ratio"
        ],
        "units": {
          "energy_MeV": "MeV",
          "depth_mm": "mm",
          "photonuclear_yield_per_e": "per primary electron",
          "electronuclear_yield_per_e": "per primary electron",
          "ratio": "dimensionless"
        }
      },
      "description": "Depth-resolved 99Mo yields for the thick 20 mm target at five beam energies. Used to verify monotonic decrease of electronuclear yield, buildup of photonuclear yield, and ratio thresholds in first and later bins."
    },
    {
      "file": "thin_target_depth_yields.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_MeV",
          "depth_mm",
          "photonuclear_yield_per_e",
          "electronuclear_yield_per_e",
          "ratio"
        ],
        "units": {
          "energy_MeV": "MeV",
          "depth_mm": "mm",
          "photonuclear_yield_per_e": "per primary electron",
          "electronuclear_yield_per_e": "per primary electron",
          "ratio": "dimensionless"
        }
      },
      "description": "Depth-resolved 99Mo yields for the thin 1 mm target at five beam energies. Used to verify ratio ~0.2 at 1 mm depth and linear trends."
    },
    {
      "file": "thick_target_total_yields.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_MeV",
          "total_photonuclear_yield_per_e",
          "total_electronuclear_yield_per_e",
          "ratio_total"
        ],
        "units": {
          "energy_MeV": "MeV",
          "total_photonuclear_yield_per_e": "per primary electron",
          "total_electronuclear_yield_per_e": "per primary electron",
          "ratio_total": "dimensionless"
        }
      },
      "description": "Volume-integrated yields over the entire 20 mm target. The total ratio is compared to ~0.01 with thresholds."
    },
    {
      "file": "fraction_vs_thickness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_mm",
          "total_photonuclear_yield_per_e",
          "total_electronuclear_yield_per_e",
          "fraction_electronuclear"
        ],
        "units": {
          "thickness_mm": "mm",
          "total_photonuclear_yield_per_e": "per primary electron",
          "total_electronuclear_yield_per_e": "per primary electron",
          "fraction_electronuclear": "dimensionless"
        }
      },
      "description": "Total yields and electronuclear fraction for thicknesses 0.1–20 mm at 40 MeV. Key thresholds: at 1 mm fraction ~0.20, at 0.1 mm >0.65."
    }
  ],
  "notes": "All yields are reported per primary electron. Depth bins for thick target are 1 mm wide; for thin target 0.1 mm wide. The checker performs structural audits on the depth profiles and threshold comparisons on ratios and fractions. Tolerances are not disclosed."
}
```

## How you are scored
A hidden automated verifier will load each of the CSV files you write to `/app/outputs`. It first checks that every required column is present and of the expected type. It then evaluates the correctness of the reported yields, ratios, and fractions by comparing them to independently determined reference values and by examining the structural properties of the depth profiles—for example, whether the electronuclear yield decreases monotonically with depth, whether the photonuclear yield exhibits the expected buildup, and whether certain ratios lie within predetermined bounds. The final reward is a weighted sum over the scored artifacts, with the thick-target depth yields, thin-target depth yields, and the fraction‑vs‑thickness result carrying the largest weight. Simply reporting numbers without having executed the Monte Carlo workflow will not receive credit.
