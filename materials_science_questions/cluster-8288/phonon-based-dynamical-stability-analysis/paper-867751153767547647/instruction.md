# First-Principles Lattice Thermal Conductivity of Monolayer Ga2O3

## Problem background
Monolayer Ga₂O₃ is a recently discovered two-dimensional semiconductor forming a quintuple‑layer O‑Ga‑O‑Ga‑O stacking. Its wide band gap and high carrier mobility make it promising for optoelectronics and power electronics. Reliable thermal management of such devices requires a thorough understanding of the material’s heat transport properties. In this task, we compute the lattice thermal conductivity of the Ga₂O₃ monolayer from first principles and analyse how different phonon branches contribute to heat conduction.

## Approach
We follow a standard DFT+phonon Boltzmann transport equation (BTE) workflow. Starting from the crystal geometry, the monolayer is structurally relaxed using DFT with the PBE exchange‑correlation functional. Harmonic interatomic force constants are then obtained from DFT supercell calculations employing the SCAN meta‑GGA functional, and anharmonic third‑order force constants are extracted from the same supercell using PBE forces. With the harmonic and anharmonic force constants, the iterative phonon BTE is solved to obtain the in‑plane lattice thermal conductivity κ<sub>L</sub> at 300 K. From the same simulation we also derive the Debye temperature (from the maximum acoustic frequency), the thermal sheet conductance using an effective thickness, and a representative phonon mean free path by fitting the cumulative κ<sub>L</sub> vs. mean free path. Finally, the mode‑resolved output is grouped into acoustic branches (ZA, TA, LA) and optical branches, with the two lowest optical branches identified as quasi‑acoustic modes (Q1, Q2); per‑branch contributions are summed to obtain branch‑level κ<sub>L</sub> and percentage contributions at 300 K.

## Reproduction target
Produce the following computed quantities for monolayer Ga₂O₃ at 300 K, all from the same DFT+phonon BTE pipeline:

- In‑plane lattice thermal conductivity κ<sub>L</sub> (W m⁻¹ K⁻¹) → results.json
- Thermal sheet conductance (nW K⁻¹) using an effective thickness of 7.57 Å → results.json
- Debye temperature (K) → results.json
- Representative phonon mean free path (nm) → results.json
- Per‑branch κ<sub>L</sub> contributions for ZA, TA, LA, Q1 (lowest quasi‑acoustic), Q2 (second lowest quasi‑acoustic), and the remaining optical branches, together with their percentage contributions → branch_contributions_300K.csv
- Derived fractions: optical contribution (Q1+Q2+other_optical)/total, and quasi‑acoustic contribution (Q1+Q2)/total → results.json.

All results must be self‑consistent: the sum of the branch contributions must equal the reported total κ<sub>L</sub>.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- ShengBTE: https://www.shengbte.org/
- PBE pseudopotentials (SSSP efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- SCAN pseudopotentials (PseudoDojo): https://pseudodojo.org/
- Ga2O3 monolayer crystal structure description

## Workflow steps

### Step 1: Structure optimization
- Role: process
- Action: Relax the Ga2O3 monolayer structure using density functional theory with the PBE functional, a plane-wave cutoff of 600 eV, a 13×13×1 k‑mesh, and a vacuum spacing >20 Å. Converge forces below 1e‑4 eV/Å.
- Evidence: `/app/outputs/relax.log`

### Step 2: Harmonic phonon calculation
- Role: process
- Action: Compute harmonic interatomic force constants on a 5×5×1 supercell using the SCAN meta-GGA functional and the Gamma point. Use Phonopy to obtain the second-order force constants file.
- Evidence: `/app/outputs/harmonic_ifc.dat`

### Step 3: Anharmonic IFC calculation
- Role: process
- Action: Compute third-order interatomic force constants on the same 5×5×1 supercell using DFT forces (PBE functional, Gamma point) and the thirdorder.py script. Include interactions up to the 8th nearest neighbour.
- Evidence: `/app/outputs/anharmonic_ifc.dat`

### Step 4: Solve phonon BTE and compute summary properties
- Role: scored (load-bearing)
- Action: Run ShengBTE on a 151×151×1 q‑grid at T=300 K using the iterative solution. From the output, extract the in-plane lattice thermal conductivity κ_L, compute the 2D thermal sheet conductance (effective thickness 7.57 Å), the Debye temperature from the maximum acoustic frequency, and fit the cumulative κ_L vs mean free path to obtain the representative MFP l_0. Write all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: object with keys: kappa_L_300K_W_mK (number), kappa_2D_sheet_conductance_nW_K (number), Debye_temperature_K (number), representative_MFP_nm (number), optical_contribution_fraction (number), quasi_acoustic_contribution_fraction (number), ZA_contribution (number), TA_contribution (number), LA_contribution (number), Q1_contribution (number), Q2_contribution (number), other_optical_contribution (number)
- Scoring: scored by hidden verifier

### Step 5: Compute branch-resolved contributions
- Role: scored
- Action: From the mode-resolved output of ShengBTE, group phonon branches into ZA, TA, LA, Q1 (lowest quasi-acoustic), Q2 (second lowest quasi-acoustic), and remaining optical branches. Sum the modal contributions to obtain per-branch κ_L and percentage contributions at 300 K. Write branch_contributions_300K.csv.
- Output file: `/app/outputs/branch_contributions_300K.csv`
- Format: csv
- Contract: columns: branch (string), contribution_kappa_W_mK (float), percentage (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/branch_contributions_300K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity, Debye temperature, representative MFP, and branch-summarised contributions for the monolayer.
- schema:
  - `type`: object
  - `properties`:
    - `kappa_L_300K_W_mK`:
      - `type`: number
      - `unit`: W m^-1 K^-1
    - `kappa_2D_sheet_conductance_nW_K`:
      - `type`: number
      - `unit`: nW K^-1
    - `Debye_temperature_K`:
      - `type`: number
      - `unit`: K
    - `representative_MFP_nm`:
      - `type`: number
      - `unit`: nm
    - `optical_contribution_fraction`:
      - `type`: number
      - `unit`: unitless
    - `quasi_acoustic_contribution_fraction`:
      - `type`: number
      - `unit`: unitless
    - `ZA_contribution`:
      - `type`: number
      - `unit`: W m^-1 K^-1
    - `TA_contribution`:
      - `type`: number
      - `unit`: W m^-1 K^-1
    - `LA_contribution`:
      - `type`: number
      - `unit`: W m^-1 K^-1
    - `Q1_contribution`:
      - `type`: number
      - `unit`: W m^-1 K^-1
    - `Q2_contribution`:
      - `type`: number
      - `unit`: W m^-1 K^-1
    - `other_optical_contribution`:
      - `type`: number
      - `unit`: W m^-1 K^-1
  - `required`: `kappa_L_300K_W_mK`, `kappa_2D_sheet_conductance_nW_K`, `Debye_temperature_K`, `representative_MFP_nm`, `optical_contribution_fraction`, `quasi_acoustic_contribution_fraction`, `ZA_contribution`, `TA_contribution`, `LA_contribution`, `Q1_contribution`, `Q2_contribution`, `other_optical_contribution`

### branch_contributions_300K.csv
- path: `/app/outputs/branch_contributions_300K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-branch thermal conductivity and percentage at 300 K. Branch values: ZA, TA, LA, Q1, Q2, other_optical.
- schema:
  - `type`: table
  - `required_columns`: `branch`, `contribution_kappa_W_mK`, `percentage`
  - `units`:
    - `contribution_kappa_W_mK`: W m^-1 K^-1
    - `percentage`: %

Notes: All results are obtained from a DFT+phonon BTE pipeline using open-source tools. The effective thickness 7.57 Å must be used for 2D sheet conductance. The Debye temperature is calculated from the maximum acoustic frequency. The representative MFP l_0 is obtained by fitting cumulative κ_L vs MFP with the single-parametric function given in the task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "kappa_L_300K_W_mK": {
            "type": "number",
            "unit": "W m^-1 K^-1"
          },
          "kappa_2D_sheet_conductance_nW_K": {
            "type": "number",
            "unit": "nW K^-1"
          },
          "Debye_temperature_K": {
            "type": "number",
            "unit": "K"
          },
          "representative_MFP_nm": {
            "type": "number",
            "unit": "nm"
          },
          "optical_contribution_fraction": {
            "type": "number",
            "unit": "unitless"
          },
          "quasi_acoustic_contribution_fraction": {
            "type": "number",
            "unit": "unitless"
          },
          "ZA_contribution": {
            "type": "number",
            "unit": "W m^-1 K^-1"
          },
          "TA_contribution": {
            "type": "number",
            "unit": "W m^-1 K^-1"
          },
          "LA_contribution": {
            "type": "number",
            "unit": "W m^-1 K^-1"
          },
          "Q1_contribution": {
            "type": "number",
            "unit": "W m^-1 K^-1"
          },
          "Q2_contribution": {
            "type": "number",
            "unit": "W m^-1 K^-1"
          },
          "other_optical_contribution": {
            "type": "number",
            "unit": "W m^-1 K^-1"
          }
        },
        "required": [
          "kappa_L_300K_W_mK",
          "kappa_2D_sheet_conductance_nW_K",
          "Debye_temperature_K",
          "representative_MFP_nm",
          "optical_contribution_fraction",
          "quasi_acoustic_contribution_fraction",
          "ZA_contribution",
          "TA_contribution",
          "LA_contribution",
          "Q1_contribution",
          "Q2_contribution",
          "other_optical_contribution"
        ]
      },
      "description": "Thermal conductivity, Debye temperature, representative MFP, and branch-summarised contributions for the monolayer."
    },
    {
      "file": "branch_contributions_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "branch",
          "contribution_kappa_W_mK",
          "percentage"
        ],
        "units": {
          "contribution_kappa_W_mK": "W m^-1 K^-1",
          "percentage": "%"
        }
      },
      "description": "Per-branch thermal conductivity and percentage at 300 K. Branch values: ZA, TA, LA, Q1, Q2, other_optical."
    }
  ],
  "notes": "All results are obtained from a DFT+phonon BTE pipeline using open-source tools. The effective thickness 7.57 Å must be used for 2D sheet conductance. The Debye temperature is calculated from the maximum acoustic frequency. The representative MFP l_0 is obtained by fitting cumulative κ_L vs MFP with the single-parametric function given in the task."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. Each output artifact (results.json and branch_contributions_300K.csv) is scored independently against reference values with tolerances appropriate for an independent re‑implementation using different DFT codes. The verifier also checks internal consistency, such as whether the branch contributions sum to the reported total κ<sub>L</sub> to within a tight margin. The final reward is a weighted combination of the per‑artifact scores. Submitting expected values without genuinely executing the computational workflow will not pass these consistency checks.
