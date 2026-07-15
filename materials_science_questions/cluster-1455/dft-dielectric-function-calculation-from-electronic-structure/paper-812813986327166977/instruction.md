# DFT Band Gaps and Dielectric Function Features for Double Perovskite Oxides

## Problem background
Double perovskite oxides of the form Pb2ScMO6 (M = Sb, Ta) are of interest for optoelectronic devices because their electronic and optical properties can be tuned by composition. Their band gaps, orbital contributions to the density of states, and frequency-dependent dielectric response are key to understanding their semiconducting or insulating character. First-principles density functional theory (DFT) can predict the direct band gap, the onset of optical absorption (ε₂ threshold), and the position of the dominant ε₂ peak, which together characterise the material's potential for light-emitting, photovoltaic, or transparent-conductor applications. This task targets those quantities for the two compounds using two exchange-correlation functionals (GGA and mBJ), providing a test of the reproducibility of such computational predictions.

## Approach
The computational approach uses plane‑wave DFT with the GGA and modified Becke‑Johnson (mBJ) exchange‑correlation functionals. For each compound (Pb2ScSbO6 and Pb2ScTaO6), self‑consistent field (SCF) calculations are performed on the cubic Fm‑3m unit cell with the reported lattice constants and internal oxygen parameter u. From the SCF wavefunctions, the band structure is computed along a high‑symmetry path that includes the X point, and the direct band gap at X is extracted. The frequency‑dependent complex dielectric function ε(ω) is obtained via the momentum matrix element approach and a Kramers‑Kronig transformation; the imaginary part ε₂(ω) is analysed to determine the absorption onset (energy where ε₂ first becomes non‑zero) and the photon energy of the dominant (global maximum) peak. The entire workflow can be executed with an open‑source DFT code capable of GGA, mBJ, and optical response post‑processing (e.g., Quantum ESPRESSO with the epsilon.x utility). All required inputs—crystal structures, atomic positions, and pseudopotential families—are specified in the workflow steps.

## Reproduction target
For Pb2ScSbO6 and Pb2ScTaO6, compute the direct band gap (eV) at the X point using both the GGA and the mBJ functional. Compute the imaginary dielectric function ε₂(ω) for each compound–functional combination, and from it determine the absorption onset (the photon energy at which ε₂ first becomes non‑zero) and the photon energy of the dominant ε₂ peak. Report these twelve quantities in three JSON files: `band_gaps.json`, `epsilon2_onset.json`, and `epsilon2_peak.json`, using the exact keys and units defined in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Precision pseudopotentials: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT electronic structure calculation
- Role: process
- Action: Set up and run self-consistent field (SCF) calculations for Pb2ScSbO6 and Pb2ScTaO6 using GGA and mBJ functionals. Use the provided cubic Fm-3m structures (Sb: a=8.1866 Å, u=0.2551; Ta: a=8.1967 Å, u=0.2556) and atomic positions: Pb (0.25,0.25,0.25), Sc (0.5,0.5,0.5), M (0,0,0), O (u,0,0). Converge charge density and wavefunctions with a suitable k‑mesh and plane‑wave cutoff.
- Evidence: `/app/outputs/scf_output.tar`

### Step 2: Band gap extraction
- Role: scored (load-bearing)
- Action: From the SCF results compute the band structure along a high‑symmetry path that includes the X point, and determine the direct band gap at the X point for each compound and functional. Write the values to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON object with keys: Pb2ScSbO6_GGA_bandgap, Pb2ScSbO6_mBJ_bandgap, Pb2ScTaO6_GGA_bandgap, Pb2ScTaO6_mBJ_bandgap. All values are floats (electron volts).
- Scoring: scored by hidden verifier

### Step 3: Dielectric function calculation
- Role: process
- Action: Using the wavefunctions from the SCF calculations, compute the frequency‑dependent complex dielectric function ε(ω) for each compound and functional via the momentum matrix element approach and Kramers‑Kronig transformation (e.g., with epsilon.x post‑processing). Produce the imaginary part ε₂(ω) on a fine energy grid.
- Evidence: `/app/outputs/epsilon2_data.tar`

### Step 4: Epsilon2 onset extraction
- Role: scored
- Action: Analyze the ε₂(ω) data for each compound and functional, identify the photon energy (eV) at which ε₂ first becomes nonzero (absorption onset), and record the results in epsilon2_onset.json.
- Output file: `/app/outputs/epsilon2_onset.json`
- Format: json
- Contract: JSON object with keys: Pb2ScSbO6_GGA_onset, Pb2ScSbO6_mBJ_onset, Pb2ScTaO6_GGA_onset, Pb2ScTaO6_mBJ_onset. All values are floats (electron volts).
- Scoring: scored by hidden verifier

### Step 5: Epsilon2 peak extraction
- Role: scored (load-bearing)
- Action: From the ε₂(ω) data determine the photon energy of the dominant (global maximum) peak for each compound and functional. Write the results to epsilon2_peak.json.
- Output file: `/app/outputs/epsilon2_peak.json`
- Format: json
- Contract: JSON object with keys: Pb2ScSbO6_GGA_peak, Pb2ScSbO6_mBJ_peak, Pb2ScTaO6_GGA_peak, Pb2ScTaO6_mBJ_peak. All values are floats (electron volts).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/epsilon2_onset.json`
- `/app/outputs/epsilon2_peak.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Direct band gap values (eV) at the X point for the two double perovskite oxides computed with GGA and mBJ functionals.
- schema:
  - `type`: object
  - `required`: `Pb2ScSbO6_GGA_bandgap`, `Pb2ScSbO6_mBJ_bandgap`, `Pb2ScTaO6_GGA_bandgap`, `Pb2ScTaO6_mBJ_bandgap`
  - `properties`:
    - `Pb2ScSbO6_GGA_bandgap`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScSbO6_mBJ_bandgap`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScTaO6_GGA_bandgap`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScTaO6_mBJ_bandgap`:
      - `type`: number
      - `unit`: eV

### epsilon2_onset.json
- path: `/app/outputs/epsilon2_onset.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Photon energy (eV) at which ε₂(ω) first becomes nonzero (absorption onset) for each compound and functional.
- schema:
  - `type`: object
  - `required`: `Pb2ScSbO6_GGA_onset`, `Pb2ScSbO6_mBJ_onset`, `Pb2ScTaO6_GGA_onset`, `Pb2ScTaO6_mBJ_onset`
  - `properties`:
    - `Pb2ScSbO6_GGA_onset`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScSbO6_mBJ_onset`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScTaO6_GGA_onset`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScTaO6_mBJ_onset`:
      - `type`: number
      - `unit`: eV

### epsilon2_peak.json
- path: `/app/outputs/epsilon2_peak.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Photon energy (eV) of the dominant global maximum peak in ε₂(ω) for each compound and functional.
- schema:
  - `type`: object
  - `required`: `Pb2ScSbO6_GGA_peak`, `Pb2ScSbO6_mBJ_peak`, `Pb2ScTaO6_GGA_peak`, `Pb2ScTaO6_mBJ_peak`
  - `properties`:
    - `Pb2ScSbO6_GGA_peak`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScSbO6_mBJ_peak`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScTaO6_GGA_peak`:
      - `type`: number
      - `unit`: eV
    - `Pb2ScTaO6_mBJ_peak`:
      - `type`: number
      - `unit`: eV

Notes: The checker compares these values to hidden reference numbers (paper‑reported) within tolerances that accommodate legitimate differences arising from DFT code and pseudopotential choices. No structural optimization is required; the provided lattice constants and atomic positions must be used directly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Pb2ScSbO6_GGA_bandgap",
          "Pb2ScSbO6_mBJ_bandgap",
          "Pb2ScTaO6_GGA_bandgap",
          "Pb2ScTaO6_mBJ_bandgap"
        ],
        "properties": {
          "Pb2ScSbO6_GGA_bandgap": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScSbO6_mBJ_bandgap": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScTaO6_GGA_bandgap": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScTaO6_mBJ_bandgap": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Direct band gap values (eV) at the X point for the two double perovskite oxides computed with GGA and mBJ functionals."
    },
    {
      "file": "epsilon2_onset.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Pb2ScSbO6_GGA_onset",
          "Pb2ScSbO6_mBJ_onset",
          "Pb2ScTaO6_GGA_onset",
          "Pb2ScTaO6_mBJ_onset"
        ],
        "properties": {
          "Pb2ScSbO6_GGA_onset": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScSbO6_mBJ_onset": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScTaO6_GGA_onset": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScTaO6_mBJ_onset": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Photon energy (eV) at which ε₂(ω) first becomes nonzero (absorption onset) for each compound and functional."
    },
    {
      "file": "epsilon2_peak.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Pb2ScSbO6_GGA_peak",
          "Pb2ScSbO6_mBJ_peak",
          "Pb2ScTaO6_GGA_peak",
          "Pb2ScTaO6_mBJ_peak"
        ],
        "properties": {
          "Pb2ScSbO6_GGA_peak": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScSbO6_mBJ_peak": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScTaO6_GGA_peak": {
            "type": "number",
            "unit": "eV"
          },
          "Pb2ScTaO6_mBJ_peak": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Photon energy (eV) of the dominant global maximum peak in ε₂(ω) for each compound and functional."
    }
  ],
  "notes": "The checker compares these values to hidden reference numbers (paper‑reported) within tolerances that accommodate legitimate differences arising from DFT code and pseudopotential choices. No structural optimization is required; the provided lattice constants and atomic positions must be used directly."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact. It reads `band_gaps.json`, `epsilon2_onset.json`, and `epsilon2_peak.json` and compares the reported values against hidden reference numbers obtained from the original paper. Comparisons use tolerances that allow for legitimate differences arising from DFT code, pseudopotential choices, and convergence settings. Reporting the paper's numbers without actually running the DFT workflow is not sufficient; the verifier expects values that are genuinely computed from a valid self‑consistent procedure. The reward is a weighted combination of the band‑gap accuracy, the ε₂ onset accuracy, and the ε₂ peak accuracy, with the largest weight assigned to the band gaps. The exact weights and tolerances are not revealed, but the verifier rewards honest computational reproduction.
