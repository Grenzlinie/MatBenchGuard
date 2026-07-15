# Electron transport and dose prediction in a thin foil

## Problem background
A reflex triode accelerates electrons onto a thin anode foil to produce X-rays. The radiation dose per electron depends on the foil thickness and the electron energy; an optimum thickness exists that maximizes the dose. Understanding this dependence is crucial for scaling predictions from measured currents and voltages. Fully resolved particle-in-cell simulations that model realistic electron angles are computationally demanding, raising the question of whether a simpler model — where electrons are normally incident and reflect inside the foil — can capture the essential dose trends for a range of conditions. This task investigates that question by implementing a simple Monte Carlo model and mapping out the resulting dose per electron as a function of foil thickness and incident electron energy.

## Approach
The approach implements a Monte Carlo simulation of electron-photon transport in a tantalum foil (Z=73, density 16.69 g/cm³). Monoenergetic electrons are injected normally into the foil. As they traverse the material, they lose energy continuously according to the Bethe stopping power formula and scatter elastically from nuclei using a screened Rutherford cross section. Bremsstrahlung photons are generated and their energy deposition is tracked. To mimic the reflex triode geometry, electrons reaching the front surface (other than the injection face) are reflected and continue moving until all their energy is deposited. By running this simulation for many foil thicknesses at a fixed electron energy, and for many incident energies at a fixed thickness, we compute the total energy deposited per incident electron, which is proportional to the X-ray dose. This simple model captures the essential physics without the complexity of a full particle-in-cell code.

## Reproduction target
Produce a dataset that quantifies the energy deposited per incident electron as a function of foil thickness and incident electron energy. Specifically:
- At a fixed electron energy of 1 MeV, simulate foil thicknesses from 0.1 µm to 10 µm and record the total energy deposited per electron.
- From these results, determine the thickness that maximizes the dose per electron at 1 MeV — the optimum thickness.
- Then, at that optimum thickness, simulate electron energies from 0.5 MeV to 2 MeV and record the dose per electron.
Write the complete dataset to a CSV file with columns for foil thickness, energy, and dose per electron. Also write the optimum thickness to a plain text file. The target is to obtain the functional relationship between thickness, energy, and dose, and to identify the optimum thickness at 1 MeV.

## Assets

- Open-source Monte Carlo electron-photon transport code (e.g., Geant4, EGSnrc, or custom implementation): https://geant4.web.cern.ch/
- NIST ESTAR stopping power data (optional): https://physics.nist.gov/PhysRefData/Star/Text/ESTAR.html

## Workflow steps

### Step 1: Monte Carlo simulation of electron transport and dose
- Role: scored (load-bearing)
- Action: Implement and run a Monte Carlo electron-photon transport simulation for a tantalum foil (Z=73, density 16.69 g/cm³) with normally-incident monoenergetic electrons. Use Bethe stopping power and screened Rutherford elastic scattering. Electrons that reach the front surface (except the incident face) are reflected and continue until all energy is lost. At a fixed voltage of 1 MV, simulate foil thicknesses from 0.1 µm to 10 µm (at least 20 points) and compute the total energy deposited per incident electron (dose per electron). From the results, identify the optimum thickness that maximises the dose per electron at 1 MV. Then, at that optimum thickness, simulate voltages from 0.5 MV to 2 MV (at least 5 points). Write all simulation results to dose_vs_thickness.csv with columns: foil_thickness_um, voltage_MV, dose_per_electron_MeV.
- Output file: `/app/outputs/dose_vs_thickness.csv`
- Format: csv
- Contract: columns: foil_thickness_um (float, µm), voltage_MV (float, MV), dose_per_electron_MeV (float, MeV). Each row represents a single simulation point.
- Scoring: scored by hidden verifier

### Step 2: Optimum thickness extraction
- Role: scored
- Action: Read dose_vs_thickness.csv, locate rows where voltage_MV == 1.0, find the foil_thickness_um corresponding to the maximum dose_per_electron_MeV. Write that optimum thickness (as a single floating-point number) to optimum_thickness.txt.
- Output file: `/app/outputs/optimum_thickness.txt`
- Format: txt
- Contract: A single floating-point number followed by a newline.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dose_vs_thickness.csv`
- `/app/outputs/optimum_thickness.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dose_vs_thickness.csv
- path: `/app/outputs/dose_vs_thickness.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated dose per electron at 1 MV for various foil thicknesses, and at the optimum thickness for various voltages. Compared to hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `foil_thickness_um`, `voltage_MV`, `dose_per_electron_MeV`
  - `units`:
    - `foil_thickness_um`: µm
    - `voltage_MV`: MV
    - `dose_per_electron_MeV`: MeV

### optimum_thickness.txt
- path: `/app/outputs/optimum_thickness.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimum foil thickness in microns at 1 MV. The checker compares this to the paper-derived optimum with an absolute tolerance.
- schema:
  - `type`: text
  - `required`:

Notes: The simulation must use Bethe stopping power and screened Rutherford elastic scattering for tantalum. The checker will compare dose values to hidden reference data obtained from a correct implementation of the same simple reflex model, applying a relative tolerance on dose and an absolute tolerance on optimum thickness. Trends (dose maximum, monotonic voltage dependence) are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dose_vs_thickness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "foil_thickness_um",
          "voltage_MV",
          "dose_per_electron_MeV"
        ],
        "units": {
          "foil_thickness_um": "µm",
          "voltage_MV": "MV",
          "dose_per_electron_MeV": "MeV"
        }
      },
      "description": "Simulated dose per electron at 1 MV for various foil thicknesses, and at the optimum thickness for various voltages. Compared to hidden reference values within tolerance."
    },
    {
      "file": "optimum_thickness.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": []
      },
      "description": "Optimum foil thickness in microns at 1 MV. The checker compares this to the paper-derived optimum with an absolute tolerance."
    }
  ],
  "notes": "The simulation must use Bethe stopping power and screened Rutherford elastic scattering for tantalum. The checker will compare dose values to hidden reference data obtained from a correct implementation of the same simple reflex model, applying a relative tolerance on dose and an absolute tolerance on optimum thickness. Trends (dose maximum, monotonic voltage dependence) are also verified."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that compares your output artifacts against reference data. For the dose dataset, the verifier checks both the qualitative trends (dose should rise to a maximum then decrease with thickness; dose should decrease monotonically with increasing energy) and the quantitative values within an acceptable tolerance that accounts for implementation differences. For the optimum thickness, the verifier compares your reported value to a hidden reference. The final reward is a combination of the scores from both artifacts. Note that the verifier knows the expected physics; simply copying numbers from a prior or hard-coding a plausible curve will not succeed if the underlying relationships are not physically realistic.
