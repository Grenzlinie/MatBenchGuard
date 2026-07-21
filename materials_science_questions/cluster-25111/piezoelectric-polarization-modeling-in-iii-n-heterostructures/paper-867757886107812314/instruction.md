# Strain-induced quantum dot electroelastic and electronic structure computation

## Problem background
Strain‑induced quantum dots formed by an InP island on an In₀.₂Ga₀.₈As quantum well exhibit deep piezoelectric potential minima that influence carrier localization and optical properties. Understanding the detailed electronic structure and photoluminescence spectrum of such systems requires three‑dimensional electroelastic modeling followed by multiband k·p calculation of confined states.

## Approach
Build the three‑dimensional geometry of the InP island (with {001}, {101}, {111} facets) on an In₀.₂Ga₀.₈As quantum well located 8.25 nm below the island. Using the provided material parameters (elastic constants, piezoelectric coefficients, band gaps, deformation potentials, etc.), solve the coupled electroelastic equations (continuum elasticity with linear piezoelectric coupling) via a finite‑element method with tetrahedral second‑order elements. Extract the strain tensor, piezoelectric potential, and deformation potentials. Construct the total single‑particle potential (band offset + deformation potential + piezoelectric potential) in the quantum well midplane. Discretise the eight‑band k·p Hamiltonian (strain‑free part plus strain‑dependent part) on a finite‑difference grid and diagonalise it with an implicitly restarted Lanczos method to obtain confined electron and hole eigenstates and eigenenergies. From the eigenenergies compute the density of states (total and optically active DP‑localized only) and, using the electric dipole approximation, the continuous‑wave photoluminescence spectrum with a Gaussian inhomogeneous broadening of 6 meV.

## Reproduction target
Produce the depths of the hole piezoelectric potential (PEP) minima, the hole deformation‑potential (DP) minimum, the electron DP minimum, and the electron PEP minima, all in meV relative to strain‑free quantum well band edges. Compute the total density of states (DOS) and the DOS of only the optically active (DP‑localized) states as a function of energy. Compute the continuous‑wave photoluminescence spectrum (energy in eV vs. intensity). Output these three results in the exact JSON and CSV files specified in the workflow steps.

## Assets

- Material parameters (elastic, piezoelectric, and k·p)

## Workflow steps

### Step 1: Electroelastic simulation
- Role: process
- Action: Construct the 3D geometry of the InP island with facets {001}, {101}, {111} on an In0.2Ga0.8As quantum well located 8.25 nm below the island. Solve the coupled electroelastic equations (continuum elasticity with piezoelectric coupling, linear constitutive relation) using a finite-element method with tetrahedral second-order elements and the material parameters provided. Obtain the full strain tensor, piezoelectric potential, and deformation potentials.
- Evidence: `/app/outputs/electroelastic_log.txt`

### Step 2: Potential minima depths
- Role: scored (load-bearing)
- Action: Extract the local extrema of the electron and hole potentials in the quantum well midplane from the computed fields. Report, relative to the strain-free band edges, the depths of the hole piezoelectric potential (PEP) minima, the hole deformation-potential (DP) minimum, the electron DP minimum, and the electron PEP minima, in meV.
- Output file: `/app/outputs/step_02_potential_minima.json`
- Format: json
- Contract: {"hole_PEP": number (meV), "hole_DP": number (meV), "electron_DP": number (meV), "electron_PEP": number (meV)}
- Scoring: scored by hidden verifier

### Step 3: Eight-band k·p electronic structure calculation
- Role: process
- Action: Discretize the eight-band k·p Hamiltonian (strain-free part plus strain-dependent part including deformation potentials and piezoelectric potential) on a finite-difference grid. Diagonalize using an implicitly restarted Lanczos method to obtain confined electron and hole eigenstates and eigenenergies.
- Evidence: `/app/outputs/kdotp_log.txt`

### Step 4: Density of states
- Role: scored (load-bearing)
- Action: Using the eigenenergies from step03, compute the total density of states (DOS) and the DOS of only the optically active (DP-localized) states. Output a CSV with energy in meV, total DOS, and DP-only DOS.
- Output file: `/app/outputs/step_04_dos.csv`
- Format: csv
- Contract: energy(meV),DOS_total,DOS_DP_only
- Scoring: scored by hidden verifier

### Step 5: Photoluminescence spectrum
- Role: scored (load-bearing)
- Action: Compute interband radiative transition rates using the electric dipole approximation and the eigenstates from step03. Convolve with a Gaussian broadening of 6 meV and sum over all transitions to obtain the continuous-wave photoluminescence spectrum. Output a CSV with energy in eV and intensity.
- Output file: `/app/outputs/step_05_pl_spectrum.csv`
- Format: csv
- Contract: energy(eV),intensity
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_potential_minima.json`
- `/app/outputs/step_04_dos.csv`
- `/app/outputs/step_05_pl_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_potential_minima.json
- path: `/app/outputs/step_02_potential_minima.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Depths of the hole piezoelectric potential minima, hole deformation-potential minimum, electron deformation-potential minimum, and electron piezoelectric potential minima, all in meV relative to strain-free QW band edges.
- schema:
  - `type`: object
  - `required`:
    - `hole_PEP`: number (meV)
    - `hole_DP`: number (meV)
    - `electron_DP`: number (meV)
    - `electron_PEP`: number (meV)

### step_04_dos.csv
- path: `/app/outputs/step_04_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Density of states of the SIQD system: total DOS and the DOS of optically active (DP-localized) states only, as a function of energy.
- schema:
  - `type`: table
  - `required_columns`: `energy(meV)`, `DOS_total`, `DOS_DP_only`

### step_05_pl_spectrum.csv
- path: `/app/outputs/step_05_pl_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulated continuous-wave photoluminescence spectrum of the SIQD ensemble.
- schema:
  - `type`: table
  - `required_columns`: `energy(eV)`, `intensity`

Notes: The hidden checker will compare the reported minima depths to the paper's hidden reference values with appropriate tolerances, and will examine the DOS and PL spectrum data for expected peak positions and relative ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_potential_minima.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "hole_PEP": "number (meV)",
          "hole_DP": "number (meV)",
          "electron_DP": "number (meV)",
          "electron_PEP": "number (meV)"
        }
      },
      "description": "Depths of the hole piezoelectric potential minima, hole deformation-potential minimum, electron deformation-potential minimum, and electron piezoelectric potential minima, all in meV relative to strain-free QW band edges."
    },
    {
      "file": "step_04_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy(meV)",
          "DOS_total",
          "DOS_DP_only"
        ]
      },
      "description": "Density of states of the SIQD system: total DOS and the DOS of optically active (DP-localized) states only, as a function of energy."
    },
    {
      "file": "step_05_pl_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy(eV)",
          "intensity"
        ]
      },
      "description": "Simulated continuous-wave photoluminescence spectrum of the SIQD ensemble."
    }
  ],
  "notes": "The hidden checker will compare the reported minima depths to the paper's hidden reference values with appropriate tolerances, and will examine the DOS and PL spectrum data for expected peak positions and relative ordering."
}
```

## How you are scored
A hidden verifier independently examines each output artifact. It compares the reported minima depths to a known correct reference (with an appropriate tolerance). It verifies that the DOS data exhibits the expected peak structure and that the photoluminescence spectrum shows characteristic peaks with correct energy ordering and relative intensities. The final score is a weighted combination of these checks across the three scored outputs.
