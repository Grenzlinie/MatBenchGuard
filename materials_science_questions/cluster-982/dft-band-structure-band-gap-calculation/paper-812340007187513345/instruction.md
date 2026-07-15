# DFT Band Structure and Bulk Properties of Pyrite-type Disulphides

## Problem background
The pyrite-type disulphides (MS₂, M = Mn, Fe, Co, Ni, Cu, Zn) exhibit a wide range of electronic and magnetic behaviours, including semiconducting, metallic, and insulating phases. First-principles density-functional theory (DFT) calculations can predict the electronic structure, band gaps, and bulk thermodynamic properties such as equilibrium volume and bulk modulus. These predictions are essential for understanding mineral physics and materials design. This task aims to compute these quantities for the pyrite family using a plane-wave DFT method.

## Approach
The reproduction employs plane-wave density-functional theory within the local density approximation (LDA) as implemented in the open-source code Quantum ESPRESSO. Three computational campaigns are carried out:

- **FeS₂ band structure**: A self-consistent field (SCF) calculation at the experimental volume is followed by a non-self-consistent band structure calculation along the high-symmetry path Γ–X–M–Γ–R–X to extract the direct band gap at the Γ point.
- **FeS₂ equation of state**: Seven SCF calculations at scaled volumes around the experimental volume provide total energy vs. volume data. The Murnaghan equation of state is fitted to these data to obtain the equilibrium volume, total energy at equilibrium, and bulk modulus.
- **MS₂ series d-band centres**: For every compound from MnS₂ to ZnS₂, an SCF calculation is performed at the experimental volume, and the projected density of states onto the metal d states is obtained. From the PDOS, the d-band centre (first moment) relative to the Fermi level is computed and recorded.

## Reproduction target
Produce the following using the LDA plane-wave DFT workflow described above:

- **step_07_bandgap.txt**: The direct band gap of FeS₂ at its experimental volume (a single float in eV).
- **step_06_eos_properties.json**: A JSON object with keys `V0` (equilibrium volume in a.u.³), `E0` (total energy in Ry), and `B0` (bulk modulus in Mbar) obtained from a Murnaghan equation-of-state fit to FeS₂ total energies at seven volumes.
- **step_09_series_dband_positions.csv**: A two-column CSV file (`compound`, `d_band_center`) giving the metal d-band centre (eV) relative to the Fermi level for MnS₂, FeS₂, CoS₂, NiS₂, CuS₂, and ZnS₂.

## Assets

- Quantum ESPRESSO (plane-wave DFT code with LDA support): https://www.quantum-espresso.org/download
- LDA pseudopotentials for transition metals (Mn,Fe,Co,Ni,Cu,Zn) and sulphur: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structures of pyrite-type MS₂ (MnS₂–ZnS₂): ICSD #202206 (FeS₂ pyrite); other MS₂ entries from ICSD or literature
- Python packages for equation-of-state fitting: numpy, scipy

## Workflow steps

### Step 1: Prepare crystal structure input files
- Role: process
- Action: For each MS₂ compound (MnS₂ to ZnS₂), obtain the experimental crystal structure (space group Pa-3, lattice constant, and internal atomic coordinates) from the literature or ICSD. For FeS₂, also generate a set of 7 scaled unit-cell volumes spanning approximately ±5% around the experimental volume. Generate Quantum ESPRESSO SCF input files using the chosen LDA pseudopotentials and a converged k-point mesh.
- Evidence: `/app/outputs/step_01_input_files_log.txt`

### Step 2: Run DFT SCF and band structure calculation for FeS₂ at experimental volume
- Role: process
- Action: Run a self-consistent field (SCF) calculation for FeS₂ at its experimental volume using plane-wave DFT with LDA. Then perform a non-self-consistent band structure calculation along the high-symmetry path Γ–X–M–Γ–R–X to obtain Kohn-Sham eigenvalues.
- Evidence: none

### Step 3: Extract direct band gap of FeS₂
- Role: scored (load-bearing)
- Action: From the band structure output of step 2, identify the valence band maximum (VBM) and conduction band minimum (CBM) at the Γ point. Compute the direct band gap (E_g = CBM – VBM) in eV and write this single float value to `step_07_bandgap.txt`.
- Output file: `/app/outputs/step_07_bandgap.txt`
- Format: txt
- Contract: A single float value in eV.
- Scoring: scored by hidden verifier

### Step 4: Run DFT SCF calculations for FeS₂ at multiple volumes
- Role: process
- Action: For each of the 7 scaled volumes prepared in step 1, run a DFT SCF calculation for FeS₂ to obtain the total energy at that volume. Use the same pseudopotentials and convergence thresholds as in step 2.
- Evidence: `/app/outputs/step_04_energy_log.txt`

### Step 5: Fit Murnaghan equation of state and extract bulk properties
- Role: scored (load-bearing)
- Action: Fit the Murnaghan equation of state to the total energy vs volume data from step 4. Extract the equilibrium volume V0 (atomic units³), the minimum total energy E0 (Rydberg), and the bulk modulus B0 (Mbar). Write these as a JSON object with keys 'V0', 'E0', 'B0' to `step_06_eos_properties.json`.
- Output file: `/app/outputs/step_06_eos_properties.json`
- Format: json
- Contract: {"V0": float (a.u.^3), "E0": float (Ry), "B0": float (Mbar)}
- Scoring: scored by hidden verifier

### Step 6: Run DFT SCF calculations for the MS₂ series (MnS₂–ZnS₂)
- Role: process
- Action: For each of the six disulphides MnS₂, FeS₂, CoS₂, NiS₂, CuS₂, ZnS₂, run a DFT SCF calculation at the respective experimental volumes using the same LDA functional and pseudopotentials. Use the SCF output to obtain the projected density of states (PDOS) on the metal d states.
- Evidence: `/app/outputs/step_06_pdos_log.txt`

### Step 7: Extract metal d-band centres across the series
- Role: scored (load-bearing)
- Action: From the SCF outputs of step 6, compute the angular-momentum-resolved local density of states projected onto the metal d states. Calculate the d-band centre (first moment) relative to the Fermi energy: ε_d = ∫ E·g_d(E) dE / ∫ g_d(E) dE over the valence band. Write a CSV file with columns 'compound' and 'd_band_center' (in eV) for the six compounds to `step_09_series_dband_positions.csv`.
- Output file: `/app/outputs/step_09_series_dband_positions.csv`
- Format: csv
- Contract: Columns: compound (str), d_band_center (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_07_bandgap.txt`
- `/app/outputs/step_06_eos_properties.json`
- `/app/outputs/step_09_series_dband_positions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_07_bandgap.txt
- path: `/app/outputs/step_07_bandgap.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The direct band gap of FeS₂ calculated at the experimental volume.
- schema:
  - `type`: text
  - `description`: A single float value representing the direct band gap of FeS₂ in eV.

### step_06_eos_properties.json
- path: `/app/outputs/step_06_eos_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium unit-cell volume, total valence-electron energy, and bulk modulus of FeS₂ from a Murnaghan equation of state fit.
- schema:
  - `type`: object
  - `required`:
    - `V0`: float (a.u.³)
    - `E0`: float (Ry)
    - `B0`: float (Mbar)

### step_09_series_dband_positions.csv
- path: `/app/outputs/step_09_series_dband_positions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Metal d-band centre positions across the pyrite-type disulphide series, verifying the reported trend of the d-band moving to higher binding energies.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `d_band_center`
  - `description`: Metal d-band centre (eV) relative to the Fermi level for each compound MnS₂–ZnS₂.

Notes: The workflow replaces the original LMTO-ASA method with plane-wave DFT (Quantum ESPRESSO). Scored quantities may differ slightly from the paper due to different basis sets and pseudopotentials; checker tolerances absorb these systematic shifts. The d-band centres are scored by their relative ordering, not by absolute values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_07_bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single float value representing the direct band gap of FeS₂ in eV."
      },
      "description": "The direct band gap of FeS₂ calculated at the experimental volume."
    },
    {
      "file": "step_06_eos_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V0": "float (a.u.³)",
          "E0": "float (Ry)",
          "B0": "float (Mbar)"
        }
      },
      "description": "Equilibrium unit-cell volume, total valence-electron energy, and bulk modulus of FeS₂ from a Murnaghan equation of state fit."
    },
    {
      "file": "step_09_series_dband_positions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "d_band_center"
        ],
        "description": "Metal d-band centre (eV) relative to the Fermi level for each compound MnS₂–ZnS₂."
      },
      "description": "Metal d-band centre positions across the pyrite-type disulphide series, verifying the reported trend of the d-band moving to higher binding energies."
    }
  ],
  "notes": "The workflow replaces the original LMTO-ASA method with plane-wave DFT (Quantum ESPRESSO). Scored quantities may differ slightly from the paper due to different basis sets and pseudopotentials; checker tolerances absorb these systematic shifts. The d-band centres are scored by their relative ordering, not by absolute values."
}
```

## How you are scored
A hidden verifier inspects the artifacts you write to `/app/outputs`. Each scored file is evaluated independently:

- The band gap in `step_07_bandgap.txt` is compared to a reference value using a tolerance that accounts for systematic differences between plane-wave and the original LMTO-ASA calculations. Meeting or exceeding the threshold earns full credit.
- The EOS properties in `step_06_eos_properties.json` are compared to reference values with per-property tolerances; staying within those tolerances earns full credit.
- The d-band centre CSV `step_09_series_dband_positions.csv` is scored by a structural audit: the verifier checks the relative ordering of the d-band centres across the series, not the exact numerical values.

The final reward is a weighted sum of the three stage scores, with the band gap and EOS properties contributing the largest shares. Running the prescribed calculations and generating the evidence artifacts is required; reporting numbers without executing the DFT workflow will not satisfy the task.
