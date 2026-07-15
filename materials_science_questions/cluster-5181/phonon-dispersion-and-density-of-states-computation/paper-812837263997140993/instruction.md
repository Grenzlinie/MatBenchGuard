# Lattice Dynamics and Thermal Diffuse Scattering of a Layered Silicate with Competing Instabilities

## Problem background
Bi2SiO5 is a layered silicate that exhibits ferroelectricity near room temperature, with a Curie temperature of approximately 663 K. The ferroelectric transition is believed to involve competing structural instabilities at different points in the Brillouin zone, driven by the dynamics of the silicate tetrahedral chains and the bismuth oxide layers. Understanding these competing instabilities requires knowledge of the phonon dispersion relations, especially the softening of optical phonon modes at the zone-center (Γ) and at the zone-boundary points Y and S. This task focuses on the computational reproduction of the lattice dynamics of Bi2SiO5 in its ferroelectric phase using density functional perturbation theory (DFPT).

## Approach
The computational approach uses planewave density functional theory (DFT) combined with density functional perturbation theory (DFPT) to compute phonon frequencies and polarization vectors. The workflow involves:
- Building or obtaining the crystal structure of Bi2SiO5 in the ferroelectric Cc phase (lattice parameters a=15.577 Å, b=5.623 Å, c=5.474 Å, β=90.002°).
- Performing a self-consistent DFT calculation and then a DFPT phonon calculation on a q-point grid that includes the high-symmetry points Γ, Y (1,0,0), and S (0.5,0.5,0) in the Brillouin zone of the paraelectric reference structure.
- From the computed phonon frequencies and eigenvectors, calculating the one-phonon thermal diffuse scattering (TDS) intensity at selected reciprocal-space points using the standard formula I ∝ (1/ω) coth(ħω/2kBT) |F(Q)|^2, where ω is the phonon frequency, Q the scattering vector, and F(Q) the structure factor (combination of atomic scattering factors and phonon eigenvectors). The TDS intensities are to be evaluated at T=300 K for two points: the Y point at (0, -1, 3) and the S point at (-4.5, -4.5, 0).

## Reproduction target
Reproduce the computational part of the study: using an open-source planewave DFT code (e.g., Quantum ESPRESSO) with norm-conserving pseudopotentials, perform a DFPT calculation for Bi2SiO5 in the ferroelectric Cc phase. Compute the lowest optical phonon energies (in meV) at the Γ, Y, and S points. Then, from the DFPT results, compute the one-phonon TDS intensity at the Y and S points at 300 K. The required deliverables are:
- A JSON file with phonon energies at Γ, Y, S.
- A CSV file with the TDS intensities at Y and S, annotated by point and temperature.
The hidden verifier will independently judge the quality of the submitted artifacts based on a set of hidden criteria that reflect the physical expectations from the original study.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials (Bi, Si, O): http://pseudopotentials.quantum-espresso.org/legacy_tables/sssp/
- Bi2SiO5 crystal structure (ferroelectric phase)

## Workflow steps

### Step 1: DFPT phonon calculation
- Role: process
- Action: Perform a density functional perturbation theory calculation for Bi2SiO5 in the ferroelectric Cc phase using Quantum ESPRESSO with norm-conserving pseudopotentials. Compute phonon frequencies and polarization vectors at Gamma, Y (1,0,0), and S (0.5,0.5,0) points of the paraelectric Brillouin zone.
- Evidence: `/app/outputs/phonon_output.log`

### Step 2: Extract phonon energies at Gamma, Y, S
- Role: scored
- Action: From the DFPT output, extract the lowest optical phonon energies in meV at Gamma, Y, and S points.
- Output file: `/app/outputs/step_01_phonon_energies.json`
- Format: json
- Contract: {"gamma": <float>, "y": <float>, "s": <float>}
- Scoring: scored by hidden verifier

### Step 3: Compute TDS intensity at Y and S points
- Role: scored (load-bearing)
- Action: Using the phonon frequencies and polarization vectors from DFPT, compute the one-phonon thermal diffuse scattering intensity at the Y and S points at 300 K according to the standard one-phonon formula (intensity proportional to 1/ω coth(ħω/2kBT) times squared atomic scattering factors).
- Output file: `/app/outputs/step_02_tds_intensity.csv`
- Format: csv
- Contract: point,temperature_K,tds_intensity
Y,300,<float>
S,300,<float>
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_energies.json`
- `/app/outputs/step_02_tds_intensity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_energies.json
- path: `/app/outputs/step_01_phonon_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lowest optical phonon energies at Gamma, Y, and S points.
- schema:
  - `type`: object
  - `required`:
    - `gamma`: float (meV)
    - `y`: float (meV)
    - `s`: float (meV)
  - `description`: Lowest optical phonon energies at Gamma, Y, S.

### step_02_tds_intensity.csv
- path: `/app/outputs/step_02_tds_intensity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: One-phonon TDS intensity at Y and S points at 300 K. The checker will verify the rows are present and the intensities are positive, with a hidden structural condition.
- schema:
  - `type`: table
  - `required_columns`: `point`, `temperature_K`, `tds_intensity`
  - `columns_schema`:
    - `point`: string (Y or S)
    - `temperature_K`: integer (300)
    - `tds_intensity`: float >0
  - `description`: One-phonon TDS intensity at Y and S points at 300 K.

Notes: TDS intensity values are in arbitrary units.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma": "float (meV)",
          "y": "float (meV)",
          "s": "float (meV)"
        },
        "description": "Lowest optical phonon energies at Gamma, Y, S."
      },
      "description": "Lowest optical phonon energies at Gamma, Y, and S points."
    },
    {
      "file": "step_02_tds_intensity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "point",
          "temperature_K",
          "tds_intensity"
        ],
        "columns_schema": {
          "point": "string (Y or S)",
          "temperature_K": "integer (300)",
          "tds_intensity": "float >0"
        },
        "description": "One-phonon TDS intensity at Y and S points at 300 K."
      },
      "description": "One-phonon TDS intensity at Y and S points at 300 K. The checker will verify the rows are present and the intensities are positive, with a hidden structural condition."
    }
  ],
  "notes": "TDS intensity values are in arbitrary units."
}
```

## How you are scored
Your submission will be scored by a hidden automated verifier. The verifier will read your output files and apply two checks:
- For `step_01_phonon_energies.json`: it will verify that the file contains valid positive numbers for gamma, y, and s, and will compare these energies against reference values within a tolerance that accounts for differences in DFT setup and pseudopotentials. Meeting or exceeding the accuracy threshold yields a portion of the total reward.
- For `step_02_tds_intensity.csv`: it will verify that the CSV has the correct columns and contains two positive rows for Y and S at 300 K. It will then evaluate whether the computed intensities are physically reasonable and satisfy a hidden structural condition that captures the main result of the paper.
The total reward is the sum of the weighted scores from both steps; successfully reproducing both parts will yield the maximum reward.
