# Substitutional phosphorus in MoSe₂ monolayer: defect identification and acceptor levels via DFT and STEM simulations

## Problem background
Tuning the conductivity of two-dimensional transition metal dichalcogenides by doping is critical for device applications. Substituting selenium with group‑V elements is a candidate approach, but the resulting defect energy levels and the ability to identify dopants via high‑resolution imaging need theoretical investigation. This task addresses the electronic and imaging signatures of phosphorus and other group‑V dopants in monolayer MoSe₂ through density functional theory calculations and simulated annular dark‑field scanning transmission electron microscopy images.

## Approach
The approach combines two computational methods. First, density functional theory using the PBE exchange–correlation functional with plane‑wave basis is employed to model 4×4 MoSe₂ supercells containing different impurities: substitutional phosphorus (P_Se), nitrogen (N_Se), arsenic (As_Se) at selenium sites, a selenium vacancy (V_Se), and the pristine monolayer. Structural relaxations are performed and the electronic band structure is computed. From the band structure, the energy positions of the defect‑induced impurity bands relative to the host valence band maximum are determined for the three group‑V dopants. Second, multislice ADF‑STEM image simulations are carried out for the relaxed P_Se and V_Se supercells using microscope parameters matching the experimental setup: accelerating voltage 200 kV, convergence semi‑angle 21.4 mrad, and ADF detector inner semi‑angle 53 mrad. From the simulated images, the ratio of the intensity at the defect column to that at a neighbouring Mo column is extracted to quantify the contrast signature of each defect.

## Reproduction target
The goal is to compute, via the workflow described, the following quantities and write them to the specified output files: the ratio of the defect‑column intensity to the neighbouring Mo‑column intensity in simulated ADF‑STEM images for the P_Se and V_Se defects, and the defect level energies (eV above the valence band maximum) for N, P, and As substitutional dopants in MoSe₂. The computed values should reflect the physics captured by the PBE functional and the multislice simulation with the given parameters.

## Assets

- MoSe₂ monolayer crystal structure (2H phase): https://next-gen.materialsproject.org/materials/mp-1634?chemsys=Mo-Se
- PBE pseudopotentials for Mo, Se, P, N, As (SSSP library): https://www.materialscloud.org/discover/sssp
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- STEM simulation code (QSTEM or Dr. Probe): http://qstem.org

## Workflow steps

### Step 1: DFT relaxations and electronic structure of MoSe₂ defect supercells
- Role: process
- Action: Perform structural relaxation and electronic structure calculation (PBE functional) for 4×4 MoSe₂ supercells containing: a substitutional P at Se site (P_Se), a Se vacancy (V_Se), substitutional N at Se (N_Se), substitutional As at Se (As_Se), and the undoped host. Produce relaxed atomic coordinates and raw band structure data for subsequent analysis.
- Evidence: none

### Step 2: QSTEM simulation of ADF-STEM intensity ratios
- Role: scored (load-bearing)
- Action: Using the relaxed atomic coordinates from the relaxation step for the P_Se and V_Se defect supercells, run multislice ADF-STEM image simulations (200 kV, convergence semi-angle 21.4 mrad, ADF detector inner semi-angle 53 mrad). Compute the ratio of the defect‑site intensity to the neighbouring Mo‑site intensity for each defect. Write the two ratios to a JSON file.
- Output file: `/app/outputs/step_01_qstem_results.json`
- Format: json
- Contract: {"P_Se_intensity_ratio": float, "V_Se_intensity_ratio": float}
- Scoring: scored by hidden verifier

### Step 3: Extract defect level energies for group-V dopants
- Role: scored
- Action: From the DFT electronic structure outputs of the relaxation step (the relaxed N_Se, P_Se, and As_Se supercells), determine the defect level energies (impurity band positions) relative to the valence band maximum. Report the three energies (in eV) in a JSON file.
- Output file: `/app/outputs/step_02_dft_results.json`
- Format: json
- Contract: {"N_defect_level_above_VBM_eV": float, "P_defect_level_above_VBM_eV": float, "As_defect_level_above_VBM_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_qstem_results.json`
- `/app/outputs/step_02_dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_qstem_results.json
- path: `/app/outputs/step_01_qstem_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: ADF-STEM intensity ratios (defect‑site intensity divided by Mo‑site intensity) for the P_Se and V_Se defects.
- schema:
  - `type`: object
  - `required`:
    - `P_Se_intensity_ratio`: float
    - `V_Se_intensity_ratio`: float

### step_02_dft_results.json
- path: `/app/outputs/step_02_dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Acceptor defect level energies (above VBM) for N, P, and As substitutional dopants in MoSe₂.
- schema:
  - `type`: object
  - `required`:
    - `N_defect_level_above_VBM_eV`: float
    - `P_defect_level_above_VBM_eV`: float
    - `As_defect_level_above_VBM_eV`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_qstem_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "P_Se_intensity_ratio": "float",
          "V_Se_intensity_ratio": "float"
        }
      },
      "description": "ADF-STEM intensity ratios (defect‑site intensity divided by Mo‑site intensity) for the P_Se and V_Se defects."
    },
    {
      "file": "step_02_dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "N_defect_level_above_VBM_eV": "float",
          "P_defect_level_above_VBM_eV": "float",
          "As_defect_level_above_VBM_eV": "float"
        }
      },
      "description": "Acceptor defect level energies (above VBM) for N, P, and As substitutional dopants in MoSe₂."
    }
  ],
  "notes": ""
}
```

## How you are scored
Each required output file is inspected by a hidden verifier that compares your reported values against reference results derived from the paper’s findings, using tolerances appropriate for the computational methods. The verifier computes a partial reward for each artifact, and the total reward (a number between 0 and 1) is a weighted sum across the artifacts. The scoring rewards accurate reproduction of the physical quantities and the expected relative trends (e.g., the ordering of defect levels among different dopants). Simply reporting numbers without executing the required computations will not yield a correct result, as the verifier checks consistency with the expected outcome of the prescribed workflow.
