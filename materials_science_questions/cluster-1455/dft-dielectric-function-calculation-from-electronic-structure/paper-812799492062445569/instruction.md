# Compute band gaps, elastic constants, and optical properties of orthorhombic halide perovskites using DFT

## Problem background
Orthorhombic methylammonium lead halides (MAPbX₃ with X = I, Br, Cl) are promising absorber materials for high-efficiency perovskite solar cells. To optimize such devices, it is essential to understand their opto‑electronic and mechanical properties — band gaps, elastic stability, optical absorption, dielectric response — and the role of the organic MA⁺ cation. Density Functional Theory (DFT) can predict these properties systematically, enabling a comparative study across the halide series. This task sets out to compute these key quantities using a standardized DFT protocol, providing a basis for evaluating the materials' suitability for photovoltaic applications.

## Approach
The approach is to perform plane‑wave DFT calculations within Quantum ESPRESSO using the Perdew–Burke–Ernzerhof (PBE) generalized‑gradient approximation and ultrasoft pseudopotentials. Crystal structures of the three orthorhombic Pnma compounds are obtained from public crystallographic databases. After relaxing atomic positions and cell parameters, the workflow computes: (1) the full elastic stiffness tensor and directional Young's moduli to assess mechanical stability and anisotropy; (2) self‑consistent electronic structure and band gaps at the Γ point; (3) projected density of states to quantify the contribution of the MA⁺ cation near the band edges; (4) the frequency‑dependent dielectric tensor for the (0 0 1) polarization direction, from which both the optical absorption coefficient and the real/imaginary dielectric functions are extracted. The same protocol is applied to MAPbI₃, MAPbBr₃, and MAPbCl₃, allowing the investigation of trends across the halide series.

## Reproduction target
The objective is to produce the five scored artifacts described in the Workflow steps:
- `elastic_constants.json` containing the elastic stiffness constants and Young's moduli (in GPa) for each compound, verifying orthorhombic stability criteria.
- `band_gaps.json` reporting the direct band gap (in eV) at the Γ point for each compound.
- `pdos_MA_analysis.json` giving the MA‑p peak energy (eV) and its relative DOS contribution at the valence‑band maximum and conduction‑band minimum.
- `absorption_coefficient.csv` providing the optical absorption coefficient (cm⁻¹) for (0 0 1) polarization over the energy range 0–6 eV with a step size ≤ 0.05 eV.
- `dielectric_constant.csv` providing the real (ε₁) and imaginary (ε₂) parts of the dielectric function for the same polarization and energy grid.

These artifacts collectively capture the key DFT‑derived properties that determine the materials' opto‑electronic and mechanical performance.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Orthorhombic MAPbX3 crystal structures: https://www.crystallography.net/cod/
- SSSP PBE ultrasoft pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- pymatgen (optional): https://pypi.org/project/pymatgen/

## Workflow steps

### Step 1: Geometry optimization of orthorhombic unit cells
- Role: process
- Action: Relax the crystal structures (atomic positions and cell parameters) of MAPbI3, MAPbBr3, and MAPbCl3 in the orthorhombic Pnma phase using GGA-PBE with ultrasoft pseudopotentials. Use appropriate plane-wave cutoffs and k-point meshes for convergence.
- Evidence: none

### Step 2: Elastic constants and Young’s moduli
- Role: scored (load-bearing)
- Action: Compute the full elastic stiffness tensor for each relaxed compound. Derive the Young’s moduli Ex, Ey, Ez and verify that the orthorhombic mechanical stability criteria are satisfied.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"MAPbI3": {"c11": float, "c22": float, "c33": float, "c44": float, "c55": float, "c66": float, "c12": float, "c13": float, "c23": float, "Ex": float, "Ey": float, "Ez": float}, "MAPbBr3": {...}, "MAPbCl3": {...}} (units: GPa)
- Scoring: scored by hidden verifier

### Step 3: Self-consistent field calculation
- Role: process
- Action: Run ground-state SCF calculations for each optimized structure to obtain the self-consistent charge density and Kohn-Sham wavefunctions at the PBE level. Use the same pseudopotentials, k-point meshes, and convergence thresholds.
- Evidence: none

### Step 4: Electronic band gaps
- Role: scored
- Action: Perform a non-self-consistent band structure calculation along a high-symmetry k‑path for each compound using the SCF charge density. Extract the fundamental band gap at the Γ point.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"MAPbI3": float (eV), "MAPbBr3": float (eV), "MAPbCl3": float (eV)}
- Scoring: scored by hidden verifier

### Step 5: Partial density of states and MA+ analysis
- Role: scored (load-bearing)
- Action: Compute projected density of states (PDOS) using the SCF wavefunctions and atomic orbital projections. Identify the energy position of the MA‑p peak and evaluate the relative contribution of MA‑p states at the valence band maximum and conduction band minimum.
- Output file: `/app/outputs/pdos_MA_analysis.json`
- Format: json
- Contract: {"MAPbI3": {"MA_p_peak_energy_eV": float, "dos_at_VBM_relative": float, "dos_at_CBM_relative": float}, "MAPbBr3": {...}, "MAPbCl3": {...}} (dos_at_VBM_relative and dos_at_CBM_relative are ratios of MA‑p DOS to total DOS)
- Scoring: scored by hidden verifier

### Step 6: Optical absorption coefficient
- Role: scored (load-bearing)
- Action: Run an optical response calculation (e.g., using epsilon.x) to obtain the frequency‑dependent macroscopic dielectric tensor. Extract the absorption coefficient α(ω) for the (0 0 1) polarization direction for all three compounds. The agent may perform a single optics run and extract both this artifact and the dielectric constant artifact.
- Output file: `/app/outputs/absorption_coefficient.csv`
- Format: csv
- Contract: Columns: energy_eV (numeric, eV), alpha_MAPbI3 (numeric, cm⁻¹), alpha_MAPbBr3 (numeric, cm⁻¹), alpha_MAPbCl3 (numeric, cm⁻¹). Energy range at least 0–6 eV with step ≤ 0.05 eV.
- Scoring: scored by hidden verifier

### Step 7: Optical dielectric constant
- Role: scored (load-bearing)
- Action: From the same optical response calculation as for absorption, extract the real (ε₁) and imaginary (ε₂) parts of the dielectric function for the (0 0 1) polarization direction. Write them to a CSV.
- Output file: `/app/outputs/dielectric_constant.csv`
- Format: csv
- Contract: Columns: energy_eV (eV), eps1_MAPbI3 (unitless), eps2_MAPbI3 (unitless), eps1_MAPbBr3 (unitless), eps2_MAPbBr3 (unitless), eps1_MAPbCl3 (unitless), eps2_MAPbCl3 (unitless). Energy range 0–6 eV, step ≤ 0.05 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/pdos_MA_analysis.json`
- `/app/outputs/absorption_coefficient.csv`
- `/app/outputs/dielectric_constant.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic stiffness tensor constants and directional Young’s moduli for the three orthorhombic perovskite compounds. All values in GPa.
- schema:
  - `type`: object
  - `required`: `MAPbI3`, `MAPbBr3`, `MAPbCl3`
  - `properties`:
    - `MAPbI3`:
      - `type`: object
      - `required`: `c11`, `c22`, `c33`, `c44`, `c55`, `c66`, `c12`, `c13`, `c23`, `Ex`, `Ey`, `Ez`
      - `units`: GPa
    - `MAPbBr3`:
      - `type`: object
      - `required`: `c11`, `c22`, `c33`, `c44`, `c55`, `c66`, `c12`, `c13`, `c23`, `Ex`, `Ey`, `Ez`
      - `units`: GPa
    - `MAPbCl3`:
      - `type`: object
      - `required`: `c11`, `c22`, `c33`, `c44`, `c55`, `c66`, `c12`, `c13`, `c23`, `Ex`, `Ey`, `Ez`
      - `units`: GPa

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gap at Γ point for each compound (eV).
- schema:
  - `type`: object
  - `required`: `MAPbI3`, `MAPbBr3`, `MAPbCl3`
  - `properties`:
    - `MAPbI3`:
      - `type`: number
      - `unit`: eV
    - `MAPbBr3`:
      - `type`: number
      - `unit`: eV
    - `MAPbCl3`:
      - `type`: number
      - `unit`: eV

### pdos_MA_analysis.json
- path: `/app/outputs/pdos_MA_analysis.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Quantitative PDOS evidence for the electronic inertness of the organic cation: MA‑p peak position (eV) and relative DOS contributions at the valence and conduction band edges (ratio of MA‑p DOS to total DOS).
- schema:
  - `type`: object
  - `required`: `MAPbI3`, `MAPbBr3`, `MAPbCl3`
  - `properties`:
    - `MAPbI3`:
      - `type`: object
      - `required`: `MA_p_peak_energy_eV`, `dos_at_VBM_relative`, `dos_at_CBM_relative`
      - `properties`:
        - `MA_p_peak_energy_eV`:
          - `type`: number
          - `unit`: eV
        - `dos_at_VBM_relative`:
          - `type`: number
          - `unit`: ratio
        - `dos_at_CBM_relative`:
          - `type`: number
          - `unit`: ratio
    - `MAPbBr3`:
      - `type`: object
      - `required`: `MA_p_peak_energy_eV`, `dos_at_VBM_relative`, `dos_at_CBM_relative`
      - `properties`:
        - `MA_p_peak_energy_eV`:
          - `type`: number
          - `unit`: eV
        - `dos_at_VBM_relative`:
          - `type`: number
          - `unit`: ratio
        - `dos_at_CBM_relative`:
          - `type`: number
          - `unit`: ratio
    - `MAPbCl3`:
      - `type`: object
      - `required`: `MA_p_peak_energy_eV`, `dos_at_VBM_relative`, `dos_at_CBM_relative`
      - `properties`:
        - `MA_p_peak_energy_eV`:
          - `type`: number
          - `unit`: eV
        - `dos_at_VBM_relative`:
          - `type`: number
          - `unit`: ratio
        - `dos_at_CBM_relative`:
          - `type`: number
          - `unit`: ratio

### absorption_coefficient.csv
- path: `/app/outputs/absorption_coefficient.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Optical absorption coefficient spectra for (0 0 1) polarization, covering at least 0–6 eV in steps ≤ 0.05 eV.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `alpha_MAPbI3`, `alpha_MAPbBr3`, `alpha_MAPbCl3`
  - `units`:
    - `energy_eV`: eV
    - `alpha_MAPbI3`: cm⁻¹
    - `alpha_MAPbBr3`: cm⁻¹
    - `alpha_MAPbCl3`: cm⁻¹

### dielectric_constant.csv
- path: `/app/outputs/dielectric_constant.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Real (ε₁) and imaginary (ε₂) parts of the dielectric function for (0 0 1) polarization, same energy grid as absorption.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `eps1_MAPbI3`, `eps2_MAPbI3`, `eps1_MAPbBr3`, `eps2_MAPbBr3`, `eps1_MAPbCl3`, `eps2_MAPbCl3`
  - `units`:
    - `energy_eV`: eV
    - `eps1_MAPbI3`: unitless
    - `eps2_MAPbI3`: unitless
    - `eps1_MAPbBr3`: unitless
    - `eps2_MAPbBr3`: unitless
    - `eps1_MAPbCl3`: unitless
    - `eps2_MAPbCl3`: unitless

Notes: The task requires open-source Quantum ESPRESSO with PBE ultrasoft pseudopotentials, CIF structures from public databases, and reproduces the paper's DFT workflow. Scoring uses generous tolerances and trend checks to account for code/functional differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "MAPbI3",
          "MAPbBr3",
          "MAPbCl3"
        ],
        "properties": {
          "MAPbI3": {
            "type": "object",
            "required": [
              "c11",
              "c22",
              "c33",
              "c44",
              "c55",
              "c66",
              "c12",
              "c13",
              "c23",
              "Ex",
              "Ey",
              "Ez"
            ],
            "units": "GPa"
          },
          "MAPbBr3": {
            "type": "object",
            "required": [
              "c11",
              "c22",
              "c33",
              "c44",
              "c55",
              "c66",
              "c12",
              "c13",
              "c23",
              "Ex",
              "Ey",
              "Ez"
            ],
            "units": "GPa"
          },
          "MAPbCl3": {
            "type": "object",
            "required": [
              "c11",
              "c22",
              "c33",
              "c44",
              "c55",
              "c66",
              "c12",
              "c13",
              "c23",
              "Ex",
              "Ey",
              "Ez"
            ],
            "units": "GPa"
          }
        }
      },
      "description": "Elastic stiffness tensor constants and directional Young’s moduli for the three orthorhombic perovskite compounds. All values in GPa."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "MAPbI3",
          "MAPbBr3",
          "MAPbCl3"
        ],
        "properties": {
          "MAPbI3": {
            "type": "number",
            "unit": "eV"
          },
          "MAPbBr3": {
            "type": "number",
            "unit": "eV"
          },
          "MAPbCl3": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Direct band gap at Γ point for each compound (eV)."
    },
    {
      "file": "pdos_MA_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "MAPbI3",
          "MAPbBr3",
          "MAPbCl3"
        ],
        "properties": {
          "MAPbI3": {
            "type": "object",
            "required": [
              "MA_p_peak_energy_eV",
              "dos_at_VBM_relative",
              "dos_at_CBM_relative"
            ],
            "properties": {
              "MA_p_peak_energy_eV": {
                "type": "number",
                "unit": "eV"
              },
              "dos_at_VBM_relative": {
                "type": "number",
                "unit": "ratio"
              },
              "dos_at_CBM_relative": {
                "type": "number",
                "unit": "ratio"
              }
            }
          },
          "MAPbBr3": {
            "type": "object",
            "required": [
              "MA_p_peak_energy_eV",
              "dos_at_VBM_relative",
              "dos_at_CBM_relative"
            ],
            "properties": {
              "MA_p_peak_energy_eV": {
                "type": "number",
                "unit": "eV"
              },
              "dos_at_VBM_relative": {
                "type": "number",
                "unit": "ratio"
              },
              "dos_at_CBM_relative": {
                "type": "number",
                "unit": "ratio"
              }
            }
          },
          "MAPbCl3": {
            "type": "object",
            "required": [
              "MA_p_peak_energy_eV",
              "dos_at_VBM_relative",
              "dos_at_CBM_relative"
            ],
            "properties": {
              "MA_p_peak_energy_eV": {
                "type": "number",
                "unit": "eV"
              },
              "dos_at_VBM_relative": {
                "type": "number",
                "unit": "ratio"
              },
              "dos_at_CBM_relative": {
                "type": "number",
                "unit": "ratio"
              }
            }
          }
        }
      },
      "description": "Quantitative PDOS evidence for the electronic inertness of the organic cation: MA‑p peak position (eV) and relative DOS contributions at the valence and conduction band edges (ratio of MA‑p DOS to total DOS)."
    },
    {
      "file": "absorption_coefficient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "alpha_MAPbI3",
          "alpha_MAPbBr3",
          "alpha_MAPbCl3"
        ],
        "units": {
          "energy_eV": "eV",
          "alpha_MAPbI3": "cm⁻¹",
          "alpha_MAPbBr3": "cm⁻¹",
          "alpha_MAPbCl3": "cm⁻¹"
        }
      },
      "description": "Optical absorption coefficient spectra for (0 0 1) polarization, covering at least 0–6 eV in steps ≤ 0.05 eV."
    },
    {
      "file": "dielectric_constant.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "eps1_MAPbI3",
          "eps2_MAPbI3",
          "eps1_MAPbBr3",
          "eps2_MAPbBr3",
          "eps1_MAPbCl3",
          "eps2_MAPbCl3"
        ],
        "units": {
          "energy_eV": "eV",
          "eps1_MAPbI3": "unitless",
          "eps2_MAPbI3": "unitless",
          "eps1_MAPbBr3": "unitless",
          "eps2_MAPbBr3": "unitless",
          "eps1_MAPbCl3": "unitless",
          "eps2_MAPbCl3": "unitless"
        }
      },
      "description": "Real (ε₁) and imaginary (ε₂) parts of the dielectric function for (0 0 1) polarization, same energy grid as absorption."
    }
  ],
  "notes": "The task requires open-source Quantum ESPRESSO with PBE ultrasoft pseudopotentials, CIF structures from public databases, and reproduces the paper's DFT workflow. Scoring uses generous tolerances and trend checks to account for code/functional differences."
}
```

## How you are scored
Each of the five output files is independently evaluated by a hidden verifier. For the JSON artifacts (elastic constants, band gaps, PDOS analysis), the verifier compares your reported quantities to independently established reference benchmarks, applying generous tolerances that account for differences in computational codes, functionals, and pseudopotentials. For the CSV spectra (absorption coefficient and dielectric constant), the verifier validates the format and the required energy coverage, and checks that key spectral features agree with expected physical ranges. The final score is a weighted combination of the per‑artifact rewards. Simply submitting known literature values without performing the actual DFT calculations will not satisfy the verifier; the checking logic is designed to reward genuine computation.
