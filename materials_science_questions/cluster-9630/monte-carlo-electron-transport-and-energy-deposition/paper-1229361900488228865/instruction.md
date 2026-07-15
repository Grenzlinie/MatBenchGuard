# Monte Carlo simulation of bremsstrahlung photon escape and photoneutron yield optimization

## Problem background
A low-cost neutron source is valuable for irradiation experiments, material testing, and neutron-based techniques. One approach uses an electron accelerator to generate bremsstrahlung photons in a metal converter, which then produce photoneutrons in a secondary target via (γ,n) reactions. The key design trade-offs are the thickness of the photon converter and the thickness of the neutron-producing layer. A converter that is too thin produces few photons, while one that is too thick reabsorbs many of them before they can escape. Similarly, the neutron target must be thick enough to stop the photons and create neutrons, but too thick a layer will self-shield and reduce the usable forward neutron flux. Here, the converter material is tantalum, and the neutron target is erbium deuteride (ErD3), a low-threshold photoneutron material. The electron beam has an energy of 10 MeV. The quantity to compute is the combination of tantalum and ErD3 thicknesses that maximizes the escaping photon fluence and the resulting directional photoneutron yield, and to determine the overall neutron yield per source electron.

## Approach
Use an open-source Monte Carlo particle transport code (Geant4) to simulate the processes. The geometry comprises a planar 10 MeV electron source, a cylindrical tantalum disk of radius 2.0 cm, and a cylindrical ErD3 target of radius 10.0 cm. Tally regions are placed in vacuum before and after each component to count particles. The workflow is split into two main simulation campaigns followed by analysis:

1. **Photon converter scan:** Vary the tantalum thickness from 0.1 mm to 10 mm, record the number of photons created inside the tantalum and the track-length estimate of photon fluence in the downstream vacuum. From these data, determine the Ta thickness that maximizes the escaping photon fluence.

2. **Photoneutron target scan:** Using the optimal Ta thickness found above, simulate the full system (Ta + ErD3) and also a configuration without any Ta. For each, vary the ErD3 thickness from 1 cm to 20 cm. Record the total number of photoneutrons produced and the number that exit the rear face of the ErD3 (directional yield).

All simulations use 1 × 10⁸ primary electrons. ErD3 is modeled with a density of 3.8 g/cm³ (50% packing fraction). The analysis produces three tables: escaped photon fluence versus Ta thickness, photoneutron yield metrics versus ErD3 thickness for both configurations, and a summary text file with the optimal thicknesses and yields.

## Reproduction target
Using the described simulation steps, compute and write to the output files the following:

*   The tantalum thickness that maximizes the photon track-length fluence in the vacuum region immediately behind the converter.
*   The total and directional photoneutron yields per source electron as functions of ErD3 thickness, for both the `with_Ta` and `without_Ta` configurations.
*   From these data, extract and report:
    *   the optimal Ta thickness for escaping photons,
    *   the overall neutron yield per source electron (maximum total neutrons without Ta),
    *   the directional neutron yield per source electron (maximum directional neutrons without Ta), and
    *   the ErD3 thickness that gives that maximum directional yield.

## Assets

- Geant4: https://geant4.web.cern.ch/download/
- Python 3: python3

## Workflow steps

### Step 1: Run Geant4 simulations for Ta-only converter thickness scan
- Role: process
- Action: Using Geant4, simulate a planar 10 MeV electron beam incident on a tantalum disk of radius 2.0 cm between two vacuum tally cells. Run separate simulations for Ta thicknesses: 0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0 mm, each with 1e8 primary histories. For each thickness, record the number of electrons transmitted to the downstream vacuum cell, the total number of photons produced inside the Ta layer, and the track-length estimate of photon fluence in the downstream vacuum cell. Consolidate results into a single CSV file.
- Evidence: `/app/outputs/ta_raw_tallies.csv`

### Step 2: Compute escaped photon fluence and optimal Ta thickness
- Role: scored (load-bearing)
- Action: Read ta_raw_tallies.csv and compute the escaped photon track-length fluence per source electron (units 1/cm^2) and the total photons produced. Output a CSV with columns: Ta_thickness_mm, photon_fluence_1percm2, total_photons_produced.
- Output file: `/app/outputs/photon_fluence_vs_Ta.csv`
- Format: csv
- Contract: Ta_thickness_mm (float), photon_fluence_1percm2 (float), total_photons_produced (float)
- Scoring: scored by hidden verifier

### Step 3: Simulate ErD3 targets with and without optimized Ta converter
- Role: process
- Action: From photon_fluence_vs_Ta.csv, determine the Ta thickness corresponding to the maximum photon_fluence_1percm2 (optimal Ta thickness). Using Geant4, simulate the same electron beam incident on: (a) a cylinder of erbium deuteride (ErD3) of radius 10.0 cm, density 3.8 g/cm^3 (50% packing fraction), without any Ta layer; (b) the same but with the optimal Ta foil placed immediately upstream. For each configuration, vary the ErD3 thickness over [1, 2, 5, 8, 10, 12, 15, 20] cm. Run 1e8 histories per case. Record the total number of photoneutrons generated and the number of photoneutrons crossing the rear plane (directional yield). Consolidate all results into one CSV file.
- Evidence: `/app/outputs/erd3_raw_results.csv`

### Step 4: Compute photoneutron yield vs ErD3 thickness
- Role: scored (load-bearing)
- Action: Read erd3_raw_results.csv and compute for each ErD3 thickness and configuration the total neutrons per source electron and the directional neutrons per source electron. Output a CSV with columns: ErD3_thickness_cm, configuration, total_neutrons_per_source_electron, directional_neutrons_per_source_electron.
- Output file: `/app/outputs/neutron_yield_vs_ErD3.csv`
- Format: csv
- Contract: ErD3_thickness_cm (float), configuration (string, one of: with_Ta, without_Ta), total_neutrons_per_source_electron (float), directional_neutrons_per_source_electron (float)
- Scoring: scored by hidden verifier

### Step 5: Generate summary of key findings
- Role: scored
- Action: From photon_fluence_vs_Ta.csv, extract the optimal Ta thickness (the Ta_thickness_mm value corresponding to the maximum photon_fluence_1percm2). From neutron_yield_vs_ErD3.csv, compute the overall neutron yield per source electron (the maximum total_neutrons_per_source_electron across all ErD3 thicknesses for the without_Ta configuration), the directional neutron yield per source electron (the maximum directional_neutrons_per_source_electron for without_Ta), and the ErD3 thickness that gives that maximum directional yield. Write these four values to summary_results.txt, each on a separate line in 'key: value' format.
- Output file: `/app/outputs/summary_results.txt`
- Format: txt
- Contract: Lines: optimal_Ta_thickness_mm: <float>, overall_neutrons_per_source_electron: <float>, directional_neutrons_per_source_electron: <float>, optimal_ErD3_thickness_for_directional_cm: <float>
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/photon_fluence_vs_Ta.csv`
- `/app/outputs/neutron_yield_vs_ErD3.csv`
- `/app/outputs/summary_results.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### photon_fluence_vs_Ta.csv
- path: `/app/outputs/photon_fluence_vs_Ta.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Escaped photon fluence and internal photon production as functions of tantalum thickness. The checker verifies that photon_fluence_1percm2 has a single maximum within 0.5 mm of 1.5 mm and total_photons_produced increases monotonically.
- schema:
  - `type`: table
  - `required_columns`: `Ta_thickness_mm`, `photon_fluence_1percm2`, `total_photons_produced`
  - `units`:
    - `Ta_thickness_mm`: mm
    - `photon_fluence_1percm2`: 1/cm^2
    - `total_photons_produced`: count

### neutron_yield_vs_ErD3.csv
- path: `/app/outputs/neutron_yield_vs_ErD3.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Photoneutron yield curves for both configurations (with and without Ta). The checker verifies that total_neutrons_per_source_electron increases monotonically with ErD3 thickness, directional_neutrons_per_source_electron has a maximum near 12 cm (±3 cm), and the without_Ta configuration yields comparable total neutrons to the with_Ta one (within a factor of 2).
- schema:
  - `type`: table
  - `required_columns`: `ErD3_thickness_cm`, `configuration`, `total_neutrons_per_source_electron`, `directional_neutrons_per_source_electron`
  - `units`:
    - `ErD3_thickness_cm`: cm
    - `total_neutrons_per_source_electron`: neutrons/electron
    - `directional_neutrons_per_source_electron`: neutrons/electron

### summary_results.txt
- path: `/app/outputs/summary_results.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Summarized key results. The checker verifies that optimal_Ta_thickness_mm is within [1.0, 2.0], overall_neutrons_per_source_electron within [1e-5, 1e-3], directional_neutrons_per_source_electron within [1e-7, 1e-5], and optimal_ErD3_thickness_for_directional_cm within [8, 16].
- schema:
  - `type`: text
  - `pattern`: optimal_Ta_thickness_mm: <float>
overall_neutrons_per_source_electron: <float>
directional_neutrons_per_source_electron: <float>
optimal_ErD3_thickness_for_directional_cm: <float>

Notes: The scored outputs capture the three headline quantities: optimal tantalum thickness for maximum escaping photon fluence, photoneutron yield vs ErD3 thickness, and summary metrics. Tolerances are generous to accommodate differences between Geant4 and MCNP physics lists.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "photon_fluence_vs_Ta.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ta_thickness_mm",
          "photon_fluence_1percm2",
          "total_photons_produced"
        ],
        "units": {
          "Ta_thickness_mm": "mm",
          "photon_fluence_1percm2": "1/cm^2",
          "total_photons_produced": "count"
        }
      },
      "description": "Escaped photon fluence and internal photon production as functions of tantalum thickness. The checker verifies that photon_fluence_1percm2 has a single maximum within 0.5 mm of 1.5 mm and total_photons_produced increases monotonically."
    },
    {
      "file": "neutron_yield_vs_ErD3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ErD3_thickness_cm",
          "configuration",
          "total_neutrons_per_source_electron",
          "directional_neutrons_per_source_electron"
        ],
        "units": {
          "ErD3_thickness_cm": "cm",
          "total_neutrons_per_source_electron": "neutrons/electron",
          "directional_neutrons_per_source_electron": "neutrons/electron"
        }
      },
      "description": "Photoneutron yield curves for both configurations (with and without Ta). The checker verifies that total_neutrons_per_source_electron increases monotonically with ErD3 thickness, directional_neutrons_per_source_electron has a maximum near 12 cm (±3 cm), and the without_Ta configuration yields comparable total neutrons to the with_Ta one (within a factor of 2)."
    },
    {
      "file": "summary_results.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "pattern": "optimal_Ta_thickness_mm: <float>\noverall_neutrons_per_source_electron: <float>\ndirectional_neutrons_per_source_electron: <float>\noptimal_ErD3_thickness_for_directional_cm: <float>"
      },
      "description": "Summarized key results. The checker verifies that optimal_Ta_thickness_mm is within [1.0, 2.0], overall_neutrons_per_source_electron within [1e-5, 1e-3], directional_neutrons_per_source_electron within [1e-7, 1e-5], and optimal_ErD3_thickness_for_directional_cm within [8, 16]."
    }
  ],
  "notes": "The scored outputs capture the three headline quantities: optimal tantalum thickness for maximum escaping photon fluence, photoneutron yield vs ErD3 thickness, and summary metrics. Tolerances are generous to accommodate differences between Geant4 and MCNP physics lists."
}
```

## How you are scored
A hidden verifier checks each scored output file independently. For `photon_fluence_vs_Ta.csv` it verifies that the photon fluence data exhibits a single maximum at a reasonable Ta thickness and that the total photon production increases monotonically with thickness. For `neutron_yield_vs_ErD3.csv` it verifies that total neutron yield increases monotonically with ErD3 thickness, that the directional yield curve shows a peak, and that the yields with and without Ta are comparable within a generous tolerance. For `summary_results.txt` it compares the four extracted numbers against hidden acceptable ranges derived from the paper's known results, with tolerances set to account for code and physics-list differences between Geant4 and the original tool. The final reward is a weighted combination of the partial scores from each artifact; simply reporting numbers without running the simulations will not satisfy the verifier.
