# FDTD Simulation of Al/SiO₂/AlOₓ/Al Nanodisc Array for LSPR Reflectance and Field Enhancement

## Problem background
This task investigates the optical response of a periodic array of Al/SiO₂/AlOₓ/Al nanodiscs, a metal–insulator–metal structure that can support localized surface plasmon resonances (LSPR). Understanding the electromagnetic behavior of such nanodisc arrays is central to explaining a reported phenomenon of light‑triggered selective repair of electrical breakdown paths in the oxide layer. The core question is: how is the electric field distributed inside the nanoscale oxide gap when the structure is illuminated with white light? Reproducing the electromagnetic simulation—specifically, computing the reflectance spectrum and the spatial map of the electric field intensity at a key visible wavelength—provides the quantitative optical field pattern that determines whether and where LSPR‑enhanced field effects occur. This task requires you to produce those two computed artifacts, which together capture the plasmonic signature of the nanodisc array.

## Approach
We model the nanodisc array as an infinite periodic arrangement of elliptical Al nanodiscs on a multilayer substrate (bottom Al / AlOₓ / SiO₂ / top Al / AlOₓ) using the finite‑difference time‑domain (FDTD) method. The geometry parameters are: nanodisc major axis 96 nm, minor axis 84 nm, sidewall angle 11° relative to the normal; layer thicknesses—bottom Al 100 nm, bottom AlOₓ 4 nm, SiO₂ 2 nm, top Al 33 nm, and top AlOₓ 2 nm; period 190 nm. The optical constants for Al, SiO₂, Al₂O₃ (an approximation for AlOₓ), and Si are taken from the Palik database. A plane‑wave source with a broad bandwidth (400–900 nm) illuminates the structure at an incidence angle of 35° measured from the normal. To approximate the unpolarized white‑light illumination used in experiments, the simulation is run separately for TE‑ and TM‑polarized excitation, and the results (reflectance and field intensity) are averaged. From the simulation output we will extract: (1) the far‑field reflected power versus wavelength to obtain the reflectance spectrum, and (2) at a wavelength of 550 nm, the steady‑state electric field intensity |E|² normalized to the incident field, sampled in a horizontal plane that cuts through the middle of the 2‑nm SiO₂ layer. The far‑field and near‑field data are then post‑processed into the required CSV files. The simulation itself can be performed with an open‑source FDTD solver (Meep) and does not require the proprietary solver originally used.

## Reproduction target
The target of this task is to compute, via FDTD simulation, the reflectance spectrum and the electric field intensity distribution for the described Al/SiO₂/AlOₓ/Al nanodisc array, and to write the results as CSV files that will be checked automatically. Specifically:
- Produce a reflectance spectrum covering 400–900 nm, saved to `/app/outputs/reflectance_spectrum.csv` with columns `wavelength_nm` (float, nm) and `reflectance` (float, dimensionless, normalized to incident power). The spectrum should contain at least 500 equally spaced rows.
- Produce a two‑dimensional map of the normalized electric field intensity |E|² inside the SiO₂ layer at a wavelength of 550 nm, saved to `/app/outputs/field_intensity_550nm.csv` with columns `x_nm` (float, nm), `y_nm` (float, nm), and `intensity` (float, dimensionless, |E|² normalized to the incident field). The grid must cover at least the nanodisc area (e.g., –120 nm to 120 nm in both x and y, with a spacing no larger than 2 nm).
These two artifacts are the scored outputs; the hidden verifier inspects them to confirm that the reflectance spectrum exhibits a plasmonic dip and that the field intensity map shows a characteristic spatial pattern of enhancement, consistent with the LSPR behavior expected for this structure. The simulation run log (`/app/outputs/simulation_log.txt`) is not scored but documents that the FDTD computation was executed.

## Assets

- Meep (open-source FDTD solver): https://github.com/NanoComp/meep
- Python with numpy and matplotlib: numpy matplotlib
- Palik optical constants (Al, SiO₂, Al₂O₃, Si): https://refractiveindex.info/

## Workflow steps

### Step 1: Run 3D FDTD simulation of Al/SiO₂/AlOₓ/Al nanodisc array
- Role: process
- Action: Set up a 3D FDTD simulation of the Al/SiO₂/AlOₓ/Al nanodisc array using the exact geometry from the paper (elliptical nanodisc with major axis 96 nm, minor axis 84 nm, period 190 nm; layer thicknesses: bottom Al 100 nm, bottom AlOₓ 4 nm, SiO₂ 2 nm, top Al 33 nm, top AlOₓ 2 nm; sidewall angle 11°). Use the Palik optical constants for all materials. Illuminate with a broad-band plane-wave source (400–900 nm) at 35° incidence, averaging TE and TM results to simulate unpolarized light. Record the full frequency- and spatial-domain field data needed to extract the reflectance spectrum and the 2D |E|² map at 550 nm in the middle of the SiO₂ layer.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Extract reflectance spectrum
- Role: scored
- Action: From the FDTD simulation output, extract the far-field reflected power versus wavelength and write the reflectance spectrum over 400–900 nm as a two-column CSV.
- Output file: `/app/outputs/reflectance_spectrum.csv`
- Format: csv
- Contract: Columns: wavelength_nm (float, nm), reflectance (float, dimensionless, normalized to incident power). At least 500 equally spaced rows covering 400–900 nm.
- Scoring: scored by hidden verifier

### Step 3: Extract field intensity map at 550 nm
- Role: scored (load-bearing)
- Action: From the FDTD simulation output, extract the steady-state electric field intensity |E|² (normalized to the incident field) in the plane cutting through the middle of the SiO₂ layer at wavelength 550 nm, and write as a three-column CSV grid.
- Output file: `/app/outputs/field_intensity_550nm.csv`
- Format: csv
- Contract: Columns: x_nm (float, nm), y_nm (float, nm), intensity (float, dimensionless, |E|² normalized to incident field). Grid covering at least the nanodisc area (e.g., -120 to 120 nm in x and y, with a spacing no larger than 2 nm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflectance_spectrum.csv`
- `/app/outputs/field_intensity_550nm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflectance_spectrum.csv
- path: `/app/outputs/reflectance_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Reflectance spectrum over 400–900 nm; structural audit checks LSPR dip position (within 600–650 nm) and depth (drop ≥0.3).
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectance`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectance`: dimensionless

### field_intensity_550nm.csv
- path: `/app/outputs/field_intensity_550nm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: 2D |E|² map at 550 nm; structural audit checks asymmetric enhancement (max intensity in top/bottom regions ≥60× minimum in central region, clear dark central band).
- schema:
  - `type`: table
  - `required_columns`: `x_nm`, `y_nm`, `intensity`
  - `units`:
    - `x_nm`: nm
    - `y_nm`: nm
    - `intensity`: dimensionless

Notes: The core FDTD simulation is the main computational reproduction; structural audits of derived properties from the two CSV artifacts verify the LSPR and field enhancement patterns quantitatively. No absolute values from the paper are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflectance_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectance"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectance": "dimensionless"
        }
      },
      "description": "Reflectance spectrum over 400–900 nm; structural audit checks LSPR dip position (within 600–650 nm) and depth (drop ≥0.3)."
    },
    {
      "file": "field_intensity_550nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_nm",
          "y_nm",
          "intensity"
        ],
        "units": {
          "x_nm": "nm",
          "y_nm": "nm",
          "intensity": "dimensionless"
        }
      },
      "description": "2D |E|² map at 550 nm; structural audit checks asymmetric enhancement (max intensity in top/bottom regions ≥60× minimum in central region, clear dark central band)."
    }
  ],
  "notes": "The core FDTD simulation is the main computational reproduction; structural audits of derived properties from the two CSV artifacts verify the LSPR and field enhancement patterns quantitatively. No absolute values from the paper are exposed."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact and combines the per‑stage scores (by weight) into a final reward between 0 and 1.

For `reflectance_spectrum.csv`, the checker will verify that the spectrum contains a reflectance minimum within the visible range and that the reflectance variation (peak‑to‑dip) is consistent with a plasmonic resonance. The check is structural: it does not require an exact reflectance value, but it expects a dip feature with sufficient contrast.

For `field_intensity_550nm.csv`, the checker will analyze the spatial distribution of |E|² to confirm the presence of substantial field intensification in certain zones and a depression in another, as expected from the LSPR effect in this asymmetric nanodisc geometry. The analysis uses predefined structural criteria and tolerances; it does not compare to a single numerical target value.

The verifier works solely from the CSV files you submit under `/app/outputs`; it does not re‑run the FDTD simulation. Passing the task therefore requires a physically correct simulation output that produces the expected spectral and spatial signatures, not a reproduction of the precise numbers from the original study.
