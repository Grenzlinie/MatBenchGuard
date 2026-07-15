# Monte Carlo Electron Transport and Energy Deposition in Thin FEP Films

## Problem background
The paper investigates functionally gradient proton exchange membranes (PEMs) fabricated by electron beam (EB) irradiation with heterogeneous energy deposition. The energy deposition profile (depth‑dose) within thin fluorinated (FEP) films determines the radical density and subsequent grafting gradient, making it critical to understand how electron energy is deposited as a function of depth. This task focuses on reproducing the Monte Carlo simulated depth‑dose profiles for soft (150–190 keV) and ultra‑low (40–110 keV) electron beams in FEP films, and the electron transmission behavior through a 25 µm film, to provide the quantitative basis for selecting irradiation energies that yield desired through‑thickness grafting distributions.

## Approach
Use a general-purpose open‑source Monte Carlo electron/photon transport code (e.g., EGS5, Geant4, PENELOPE) to simulate electron penetration and energy deposition in multilayer planar geometries representative of two commercial EB accelerators. The simulation models consist of a thin metallic window, a nitrogen atmosphere, and the FEP sample. For the soft‑EB geometry (CURETRON® model) the window is titanium; for the ultra‑low EB geometry (EB‑ENGINE® model) the window is beryllium. Electron beams with accelerating voltages of 150, 160, 170, 180, 190 keV (soft) and 40, 60, 110 keV (ultra‑low) are simulated using at least 5000 primary electrons each. The per‑electron energy deposited as a function of depth in the FEP is recorded, and a second set of simulations with a 25 µm FEP layer determines the fraction of electrons transmitted through the film.

## Reproduction target
Compute and output the following two artifacts:

1. `depth_dose_profiles.csv` – Depth‑dose profiles D(z) (energy deposited per incident electron) for each of the nine accelerating voltages in the corresponding accelerator geometry. The profiles are evaluated at depth intervals of 10 µm from the FEP surface to 300 µm.
2. `transmission_fractions.json` – The fraction of primary electrons that exit the downstream face of a 25 µm FEP film for the 40 keV, 60 keV, and 110 keV beams.

The results will be checked against physically motivated structural properties (monotonicity, depth ordering, near‑surface deposition, and transmission thresholds) derived from the original paper’s findings. No absolute numeric match to paper values is required; the verification is based on consistent physical trends.

## Assets

- Monte Carlo electron transport code (EGS5, Geant4, PENELOPE, or equivalent)

## Workflow steps

### Step 1: Simulate depth-dose profiles for soft and ultra-low EB
- Role: scored (load-bearing)
- Action: Set up the Monte Carlo simulation geometry for the CURETRON (soft EB) and EB-ENGINE (ultra-low EB) multilayer stacks. Run electron transport for the specified accelerating voltages: 150,160,170,180,190 keV (CURETRON) and 40,60,110 keV (EB-ENGINE). Use at least 5000 primary electrons per simulation. Extract the per-electron energy deposition as a function of depth in the FEP layer from the surface to 300 μm at 10 μm intervals. Save the depth-dose data.
- Output file: `/app/outputs/depth_dose_profiles.csv`
- Format: csv
- Contract: CSV file with columns: voltage_keV (integer), depth_um (float, depth from FEP surface in μm), dose_per_electron (float, deposited energy per primary electron, in keV or MeV). Depth steps: 0,10,20,…,300 μm. Required voltages: 150,160,170,180,190 (CURETRON geometry) and 40,60,110 (EB-ENGINE geometry).
- Scoring: scored by hidden verifier

### Step 2: Simulate electron transmission through 25 µm FEP film
- Role: scored
- Action: Using the EB-ENGINE geometry with the FEP thickness set to 25 μm (instead of 300 μm), run simulations for 40, 60, and 110 keV primary electrons (at least 5000 each). Compute the fraction of primary electrons that exit the FEP at the transmit face (transmitted fraction). Output the results.
- Output file: `/app/outputs/transmission_fractions.json`
- Format: json
- Contract: JSON object with string keys "40", "60", "110" and floating-point values representing the fraction of primary electrons transmitted through the 25 μm FEP film (range 0.0–1.0). Example: {"40": 0.002, "60": 0.23, "110": 0.89}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/depth_dose_profiles.csv`
- `/app/outputs/transmission_fractions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### depth_dose_profiles.csv
- path: `/app/outputs/depth_dose_profiles.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Per-electron depth-dose profiles for soft EB (150-190 keV) and ultra-low EB (40-110 keV) at 10 μm depth intervals in FEP. Checked by structural properties: monotonic decrease with depth for soft EB, energy-dependent shift, near-surface peak for ultra-low EB, and consistent units.
- schema:
  - `type`: table
  - `required_columns`: `voltage_keV`, `depth_um`, `dose_per_electron`
  - `units`:
    - `voltage_keV`: keV
    - `depth_um`: μm
    - `dose_per_electron`: keV or MeV per primary electron

### transmission_fractions.json
- path: `/app/outputs/transmission_fractions.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Transmitted electron fractions through 25 μm FEP for 40, 60, and 110 keV. Checked against threshold ranges: 40 keV fraction < 0.05, 60 keV fraction between 0.05 and 0.5 inclusive, 110 keV fraction > 0.5.
- schema:
  - `type`: object
  - `required`: `40`, `60`, `110`
  - `items`:
    - `40`: float (0-1)
    - `60`: float (0-1)
    - `110`: float (0-1)

Notes: The checker validates structural trends and threshold constraints, not exact numeric matches to paper values. No absolute gold numbers are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "depth_dose_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "voltage_keV",
          "depth_um",
          "dose_per_electron"
        ],
        "units": {
          "voltage_keV": "keV",
          "depth_um": "μm",
          "dose_per_electron": "keV or MeV per primary electron"
        }
      },
      "description": "Per-electron depth-dose profiles for soft EB (150-190 keV) and ultra-low EB (40-110 keV) at 10 μm depth intervals in FEP. Checked by structural properties: monotonic decrease with depth for soft EB, energy-dependent shift, near-surface peak for ultra-low EB, and consistent units."
    },
    {
      "file": "transmission_fractions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "40",
          "60",
          "110"
        ],
        "items": {
          "40": "float (0-1)",
          "60": "float (0-1)",
          "110": "float (0-1)"
        }
      },
      "description": "Transmitted electron fractions through 25 μm FEP for 40, 60, and 110 keV. Checked against threshold ranges: 40 keV fraction < 0.05, 60 keV fraction between 0.05 and 0.5 inclusive, 110 keV fraction > 0.5."
    }
  ],
  "notes": "The checker validates structural trends and threshold constraints, not exact numeric matches to paper values. No absolute gold numbers are required."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that reads the two output files and checks them against a hidden rubric. The verifier does NOT re‑run the Monte Carlo simulation; it validates the structure and content of the submitted files, and compares the reported values to the expected physical trends and quantitative thresholds derived from the paper. Each stage is weighted, and the final reward is a continuous score between 0 and 1. Reporting a number you found in a paper or guesswork without performing the simulations will not pass the hidden checks. You must run the described simulations and produce the required output files through honest computational work.
