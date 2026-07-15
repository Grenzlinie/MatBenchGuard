# Monte Carlo simulations for electron backscattering and X-ray emission from layered and particulate samples

## Problem background
Electron backscattering and X-ray emission in heterogeneous materials depend strongly on specimen geometry and composition. Single-scattering Monte Carlo simulations are the standard tool for predicting these signals, which govern the contrast in backscattered-electron imaging and the quantitative composition analysis in scanning electron microscopes. This task addresses three practical cases: (a) the detectability of a thin vertical boron layer embedded in a steel matrix, (b) the effect of sphere diameter on backscattering and X-ray signals from a carbon particulate on a gold substrate, and (c) the use of X-ray intensity ratios to determine the thickness of a carbon thin film on gold without measuring the beam current. The computational goal is to reproduce the simulated backscattering coefficients, X-ray line intensities, and the derived contrast, K‑ratio, and R‑ratio data for these systems.

## Approach
The reproduction uses a single-scattering Monte Carlo model with Mott elastic cross‑sections, Bethe continuous energy loss, and Casnati ionization cross‑sections. The approach consists of simulating electron trajectories and collecting backscattered electrons as well as characteristic X‑ray counts for three sample configurations.

1.  **Vertical boron layer in steel:** A 10 nm vertical B layer is placed in an Fe‑0.8 wt% C matrix (1080 steel). A 10 nm diameter electron beam is scanned across the layer, and the backscattering coefficient η and the B Kα net intensity are recorded as a function of beam position for incident energies ranging from 1 to 20 keV. The image contrast is computed as C(%)=100×(ηmax−ηmin)/(ηmax+ηmin) from each line scan.

2.  **Carbon thin film on gold:** A pure carbon film of varying thickness (from zero to beyond the electron range) is deposited on a gold substrate. Electron trajectories are simulated at 4, 5, and 6 keV. The net intensities of C Kα and Au Mα lines are collected for each thickness, together with a simulation of a bulk graphite reference at the same energies. From these, the classic K‑ratio (Ifilm/Ibulk) and the proposed R‑ratio (IC Kα/(IC Kα+IAu Mα)) are computed as functions of film thickness.

3.  **Carbon spherical particulate on gold:** A spherical carbon particle (diameter 1–1000 nm) sits on a gold substrate. The beam is positioned at the top of the sphere, and 10 000 trajectories are followed for each diameter at incident energies from 1 to 20 keV. The backscattering coefficient η and the C Kα net intensity are recorded as functions of diameter and energy.

## Reproduction target
Execute the three sets of Monte Carlo simulations and produce the following six scored artifacts:

* `contrast_data_boron_layer.csv` — backscattered‑electron contrast (%) vs incident energy (keV) for the 10 nm boron layer, computed from the η line‑scans.
* `b_kalpha_line_scan.csv` — B Kα net intensity as a function of beam position (nm) for each incident energy.
* `eta_vs_diameter_particulate.csv` — backscattering coefficient η vs sphere diameter D (nm) for each incident energy for the C sphere on Au.
* `c_kalpha_vs_diameter_particulate.csv` — C Kα net intensity vs D (nm) for each incident energy for the C sphere on Au.
* `k_ratio_vs_thickness.csv` — K‑ratio (Ifilm/Ibulk graphite) vs film thickness (nm) at 4, 5, and 6 keV for the C film on Au.
* `r_ratio_vs_thickness.csv` — R‑ratio (IC Kα/(IC Kα+IAu Mα)) vs film thickness (nm) at 4, 5, and 6 keV for the C film on Au.

Data should follow the expected physical trends: contrast decreasing with energy, a distinct B Kα peak at the layer position, monotonic increase of K‑ and R‑ratios with thickness, and a diameter‑dependent behaviour of η and C Kα (rise to a maximum followed by decay) whose characteristic scale shifts with incident energy.

## Assets

- CASINO Monte Carlo simulation software: http://www.montecarlomodeling.mcgill.ca/
- Win X-Ray Monte Carlo program: http://www.montecarlomodeling.mcgill.ca/

## Workflow steps

### Step 1: Run all Monte Carlo simulations
- Role: process
- Action: Set up specimen geometries and material compositions, then run single-scattering Monte Carlo simulations (Mott elastic cross-sections, Bethe continuous energy loss, Casnati ionization cross-sections) to simulate electron trajectories for three cases. (a) Boron layer: a 10 nm vertical boron layer in an Fe-0.8 wt% C matrix, 10 nm beam diameter, 50 beam positions over a 100 nm line scan at incident energies 1,2,3,5,10,20 keV, 5000 trajectories per position; collect backscattering coefficient η and B Kα net intensity. (b) Carbon thin film: a carbon film of varying thickness (0 to >1000 nm) on a gold substrate, beam energies 4,5,6 keV, 10000 trajectories per condition, plus a bulk graphite reference simulation at the same energies; collect C Kα and Au Mα net intensities. (c) Carbon sphere: a spherical carbon particulate (diameters 1-1000 nm) on a gold substrate, beam incident at the top, 10000 trajectories, beam energies 1,2,5,10,20 keV; collect η, C Kα, and Au Mα net intensities.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Boron layer backscattered-electron contrast
- Role: scored
- Action: From the simulated η line-scan data for the boron layer, extract η_max and η_min for each incident energy and compute contrast C(%) = (η_max − η_min) / (η_max + η_min). Write a CSV file with columns E0_keV and contrast_percent.
- Output file: `/app/outputs/contrast_data_boron_layer.csv`
- Format: csv
- Contract: E0_keV (float, keV), contrast_percent (float, %)
- Scoring: scored by hidden verifier

### Step 3: Boron Kα line scan
- Role: scored
- Action: From the boron-layer simulation, extract the net intensity of the B Kα line as a function of beam position for each incident energy. Write a CSV with columns beam_position_nm, E0_keV, net_intensity.
- Output file: `/app/outputs/b_kalpha_line_scan.csv`
- Format: csv
- Contract: beam_position_nm (float, nm), E0_keV (float, keV), net_intensity (float)
- Scoring: scored by hidden verifier

### Step 4: Backscattering coefficient vs diameter for carbon particulate
- Role: scored
- Action: From the spherical-particulate simulation, extract the backscattering coefficient η for each sphere diameter D and incident energy. Write a CSV with columns E0_keV, D_nm, eta.
- Output file: `/app/outputs/eta_vs_diameter_particulate.csv`
- Format: csv
- Contract: E0_keV (float, keV), D_nm (float, nm), eta (float)
- Scoring: scored by hidden verifier

### Step 5: Carbon Kα intensity vs diameter for carbon particulate
- Role: scored
- Action: From the same simulation, extract the net intensity of the C Kα line for each diameter D and incident energy. Write a CSV with columns E0_keV, D_nm, net_intensity.
- Output file: `/app/outputs/c_kalpha_vs_diameter_particulate.csv`
- Format: csv
- Contract: E0_keV (float, keV), D_nm (float, nm), net_intensity (float)
- Scoring: scored by hidden verifier

### Step 6: K-ratio calibration curve for carbon film
- Role: scored (load-bearing)
- Action: Using the carbon-film thickness-series intensities and the bulk graphite reference intensity, compute the K-ratio = I_film / I_bulk_standard for each thickness and each beam energy (4,5,6 keV). Write a CSV with columns E0_keV, thickness_nm, K_ratio.
- Output file: `/app/outputs/k_ratio_vs_thickness.csv`
- Format: csv
- Contract: E0_keV (float, keV), thickness_nm (float, nm), K_ratio (float)
- Scoring: scored by hidden verifier

### Step 7: R-ratio calibration curve for carbon film
- Role: scored
- Action: From the same film intensities, compute the R-ratio = I_CKα / (I_CKα + I_AuMα) for each thickness and beam energy. Write a CSV with columns E0_keV, thickness_nm, R_ratio.
- Output file: `/app/outputs/r_ratio_vs_thickness.csv`
- Format: csv
- Contract: E0_keV (float, keV), thickness_nm (float, nm), R_ratio (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contrast_data_boron_layer.csv`
- `/app/outputs/b_kalpha_line_scan.csv`
- `/app/outputs/eta_vs_diameter_particulate.csv`
- `/app/outputs/c_kalpha_vs_diameter_particulate.csv`
- `/app/outputs/k_ratio_vs_thickness.csv`
- `/app/outputs/r_ratio_vs_thickness.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contrast_data_boron_layer.csv
- path: `/app/outputs/contrast_data_boron_layer.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Contrast of the backscattered-electron image for the 10 nm boron layer in steel as a function of incident energy.
- schema:
  - `type`: table
  - `required_columns`: `E0_keV`, `contrast_percent`
  - `units`:
    - `E0_keV`: keV
    - `contrast_percent`: %

### b_kalpha_line_scan.csv
- path: `/app/outputs/b_kalpha_line_scan.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Line-scan of B Kα net intensity across the boron layer for each incident energy.
- schema:
  - `type`: table
  - `required_columns`: `beam_position_nm`, `E0_keV`, `net_intensity`
  - `units`:
    - `beam_position_nm`: nm
    - `E0_keV`: keV
    - `net_intensity`: counts

### eta_vs_diameter_particulate.csv
- path: `/app/outputs/eta_vs_diameter_particulate.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Backscattering coefficient η as a function of sphere diameter for a carbon particle on gold at various incident energies.
- schema:
  - `type`: table
  - `required_columns`: `E0_keV`, `D_nm`, `eta`
  - `units`:
    - `E0_keV`: keV
    - `D_nm`: nm
    - `eta`: fraction

### c_kalpha_vs_diameter_particulate.csv
- path: `/app/outputs/c_kalpha_vs_diameter_particulate.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Net intensity of C Kα line as a function of sphere diameter for a carbon particle on gold at various incident energies.
- schema:
  - `type`: table
  - `required_columns`: `E0_keV`, `D_nm`, `net_intensity`
  - `units`:
    - `E0_keV`: keV
    - `D_nm`: nm
    - `net_intensity`: counts

### k_ratio_vs_thickness.csv
- path: `/app/outputs/k_ratio_vs_thickness.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: K-ratio (I_film / I_bulk_standard) of C Kα line for a carbon film on gold as a function of film thickness for energies 4, 5, and 6 keV.
- schema:
  - `type`: table
  - `required_columns`: `E0_keV`, `thickness_nm`, `K_ratio`
  - `units`:
    - `E0_keV`: keV
    - `thickness_nm`: nm
    - `K_ratio`: dimensionless

### r_ratio_vs_thickness.csv
- path: `/app/outputs/r_ratio_vs_thickness.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: R-ratio (I_CKα / (I_CKα + I_AuMα)) for a carbon film on gold as a function of film thickness for energies 4, 5, and 6 keV.
- schema:
  - `type`: table
  - `required_columns`: `E0_keV`, `thickness_nm`, `R_ratio`
  - `units`:
    - `E0_keV`: keV
    - `thickness_nm`: nm
    - `R_ratio`: dimensionless

Notes: All outputs are derived from single-scattering Monte Carlo simulations. The hidden checker will compare the reported values, trends, and structural relations (e.g., contrast ~30% at 20 keV, monotonic increase of R-ratio, peak location in line scan) to reference data extracted from the paper. No internet access is required during verification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contrast_data_boron_layer.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E0_keV",
          "contrast_percent"
        ],
        "units": {
          "E0_keV": "keV",
          "contrast_percent": "%"
        }
      },
      "description": "Contrast of the backscattered-electron image for the 10 nm boron layer in steel as a function of incident energy."
    },
    {
      "file": "b_kalpha_line_scan.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "beam_position_nm",
          "E0_keV",
          "net_intensity"
        ],
        "units": {
          "beam_position_nm": "nm",
          "E0_keV": "keV",
          "net_intensity": "counts"
        }
      },
      "description": "Line-scan of B Kα net intensity across the boron layer for each incident energy."
    },
    {
      "file": "eta_vs_diameter_particulate.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E0_keV",
          "D_nm",
          "eta"
        ],
        "units": {
          "E0_keV": "keV",
          "D_nm": "nm",
          "eta": "fraction"
        }
      },
      "description": "Backscattering coefficient η as a function of sphere diameter for a carbon particle on gold at various incident energies."
    },
    {
      "file": "c_kalpha_vs_diameter_particulate.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E0_keV",
          "D_nm",
          "net_intensity"
        ],
        "units": {
          "E0_keV": "keV",
          "D_nm": "nm",
          "net_intensity": "counts"
        }
      },
      "description": "Net intensity of C Kα line as a function of sphere diameter for a carbon particle on gold at various incident energies."
    },
    {
      "file": "k_ratio_vs_thickness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E0_keV",
          "thickness_nm",
          "K_ratio"
        ],
        "units": {
          "E0_keV": "keV",
          "thickness_nm": "nm",
          "K_ratio": "dimensionless"
        }
      },
      "description": "K-ratio (I_film / I_bulk_standard) of C Kα line for a carbon film on gold as a function of film thickness for energies 4, 5, and 6 keV."
    },
    {
      "file": "r_ratio_vs_thickness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E0_keV",
          "thickness_nm",
          "R_ratio"
        ],
        "units": {
          "E0_keV": "keV",
          "thickness_nm": "nm",
          "R_ratio": "dimensionless"
        }
      },
      "description": "R-ratio (I_CKα / (I_CKα + I_AuMα)) for a carbon film on gold as a function of film thickness for energies 4, 5, and 6 keV."
    }
  ],
  "notes": "All outputs are derived from single-scattering Monte Carlo simulations. The hidden checker will compare the reported values, trends, and structural relations (e.g., contrast ~30% at 20 keV, monotonic increase of R-ratio, peak location in line scan) to reference data extracted from the paper. No internet access is required during verification."
}
```

## How you are scored
A hidden verifier will check each of the six scored output files independently. It will compare the data you produce against reference values and trends derived from the original work, using appropriate tolerances that account for statistical noise and implementation differences. The verifier evaluates both structural properties (monotonicity, peak location, correct ordering between conditions) and numerical agreement with expected values. Each scored artifact contributes a weighted fraction to the final reward. Reporting a single number is not sufficient; every required table must be generated from the simulations as described.
