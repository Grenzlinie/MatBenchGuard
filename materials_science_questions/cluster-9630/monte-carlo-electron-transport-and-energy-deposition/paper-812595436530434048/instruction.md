# Monte Carlo Electron Transport in Insulating Solids with 1D Electrostatic Charging

## Problem background
In scanning electron microscopy (SEM) and related microanalytical techniques, insulating specimens accumulate trapped charge under the electron beam, generating an internal electric field that modifies electron trajectories and degrades imaging and analysis. Understanding how this charging affects electron transport is therefore important for interpreting SEM and microanalysis data. This task couples a single-scattering Monte Carlo electron transport model (Mott elastic cross sections, continuous slowing-down approximation) with a simple one-dimensional electrostatic model of a uniform trapped-charge layer (parameters: surface electric field Emax and trapping depth Zmax). The goal is to quantify the influence of charging on the electron range, backscattered fraction, and depth-dependent energy deposition in the specimen.

## Approach
The reproduction uses a Monte Carlo simulation of electron transport in Al2O3 at 20 keV, based on a single-scattering model with Mott elastic cross sections and the Bethe continuous-slowing-down approximation for energy loss. The effect of trapped charge is modelled by a one-dimensional uniform charge layer, which produces a depth-dependent electric field. In the uncharged case, the field is zero; in the charged case, the field magnitude at the surface is Emax and the layer extends to depth Zmax. The trapping depth Zmax is first determined from a simulation without any electric field. Then a series of simulations for several Emax values is performed, and the backscattered coefficient (fraction of incident electrons backscattered with energy above 50 eV) and depth-resolved histograms of total energy loss, Bethe stopping-power loss, and electric energy loss are extracted. The required material properties (Al2O3 density, composition, stopping power) and the physical models are obtained from standard public databases and the open-source CASINO Monte Carlo code.

## Reproduction target
Compute the backscattered coefficient as a function of the surface electric field Emax for the values 0, 1e7, 2e7, 5e7, and 1e8 V/m, and compute depth-resolved energy loss distributions (total loss, Bethe loss, electric loss) for the uncharged case (Emax = 0) and the charged case (Emax = 1e8 V/m), for Al2O3 at 20 keV, using a Monte Carlo simulation with Mott elastic cross sections, continuous slowing-down approximation, and a 1D uniform trapped-charge electrostatic model. At least 10,000 primary electrons must be simulated per Emax value. The depth histograms must use bins of 10 nm from 0 to 500 nm.

## Assets

- CASINO Monte Carlo simulation code: https://www.gel.usherbrooke.ca/casino/
- NIST ESTAR stopping power database: https://physics.nist.gov/PhysRefData/Star/Text/ESTAR.html
- Mott elastic scattering cross sections: https://physics.nist.gov/PhysRefData/Elastic/
- Al2O3 material composition and density

## Workflow steps

### Step 1: Determine trapping depth Zmax from uncharged simulation
- Role: process
- Action: Run a Monte Carlo simulation for Al2O3 at 20 keV without any electric field. From the simulated electron trajectories, compute a representative depth (e.g., the depth that contains 99% of total energy deposition) and set Zmax to this value; it will be used in subsequent charged simulations.
- Evidence: `/app/outputs/zmax_value.txt`

### Step 2: Compute backscattered coefficient for varying Emax
- Role: scored (load-bearing)
- Action: Using Zmax from the uncharged simulation, run charged Monte Carlo simulations for Al2O3 at 20 keV with the 1D uniform trapped-charge electrostatic model for Emax values 0, 1e7, 2e7, 5e7, 1e8 V/m. Use a sufficient number of primary electrons (at least 10,000 per Emax). For each Emax, compute the backscattered coefficient as the fraction of incident electrons that emerge with kinetic energy > 50 eV. Record the results as a CSV file.
- Output file: `/app/outputs/backscattered_coefficient.csv`
- Format: csv
- Contract: Columns: [Emax, backscattered_coefficient]. Emax: numeric, V/m; backscattered_coefficient: numeric, dimensionless fraction.
- Scoring: scored by hidden verifier

### Step 3: Generate depth-resolved energy loss distributions
- Role: scored
- Action: From the simulations for the uncharged case (Emax=0) and the charged case (Emax=1e8 V/m), extract depth-binned histograms of total energy loss, Bethe stopping power loss, and electric energy loss per incident electron. Use depth bins from 0 to 500 nm with a 10 nm bin size (bins represented by their center depths). Write the results as a JSON file.
- Output file: `/app/outputs/depth_distributions.json`
- Format: json
- Contract: { "uncharged": { "depth_bins": [...], "total_loss": [...], "bethe_loss": [...], "electric_loss": [...] }, "charged": { "depth_bins": [...], "total_loss": [...], "bethe_loss": [...], "electric_loss": [...] } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/backscattered_coefficient.csv`
- `/app/outputs/depth_distributions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### backscattered_coefficient.csv
- path: `/app/outputs/backscattered_coefficient.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Backscattered coefficient as a function of surface electric field Emax for five values: 0, 1e7, 2e7, 5e7, 1e8 V/m.
- schema:
  - `type`: table
  - `required_columns`: `Emax`, `backscattered_coefficient`
  - `units`:
    - `Emax`: V/m
    - `backscattered_coefficient`: dimensionless fraction

### depth_distributions.json
- path: `/app/outputs/depth_distributions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Depth-resolved energy loss distributions for the uncharged (Emax=0) and charged (Emax=1e8 V/m) cases, binned from 0 to 500 nm with 10 nm bins.
- schema:
  - `type`: object
  - `required`:
    - `uncharged`:
      - `depth_bins`: array of floats (nm, bin centers)
      - `total_loss`: array of floats (eV/electron)
      - `bethe_loss`: array of floats (eV/electron)
      - `electric_loss`: array of floats (eV/electron)
    - `charged`:
      - `depth_bins`: array of floats (nm, bin centers)
      - `total_loss`: array of floats (eV/electron)
      - `bethe_loss`: array of floats (eV/electron)
      - `electric_loss`: array of floats (eV/electron)

Notes: Hidden reference values are derived from digitized figures in the original paper. Tolerances accommodate Monte Carlo statistical noise and implementation-dependent variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "backscattered_coefficient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Emax",
          "backscattered_coefficient"
        ],
        "units": {
          "Emax": "V/m",
          "backscattered_coefficient": "dimensionless fraction"
        }
      },
      "description": "Backscattered coefficient as a function of surface electric field Emax for five values: 0, 1e7, 2e7, 5e7, 1e8 V/m."
    },
    {
      "file": "depth_distributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "uncharged": {
            "depth_bins": "array of floats (nm, bin centers)",
            "total_loss": "array of floats (eV/electron)",
            "bethe_loss": "array of floats (eV/electron)",
            "electric_loss": "array of floats (eV/electron)"
          },
          "charged": {
            "depth_bins": "array of floats (nm, bin centers)",
            "total_loss": "array of floats (eV/electron)",
            "bethe_loss": "array of floats (eV/electron)",
            "electric_loss": "array of floats (eV/electron)"
          }
        }
      },
      "description": "Depth-resolved energy loss distributions for the uncharged (Emax=0) and charged (Emax=1e8 V/m) cases, binned from 0 to 500 nm with 10 nm bins."
    }
  ],
  "notes": "Hidden reference values are derived from digitized figures in the original paper. Tolerances accommodate Monte Carlo statistical noise and implementation-dependent variations."
}
```

## How you are scored
A hidden verifier independently checks each of the two scored artifacts: the backscattered coefficient CSV file and the depth distribution JSON file. It first validates that the files conform to the required format and schema (column names, data types, array lengths). Then it compares the numerical contents to hidden reference values derived from the original study’s results, using tolerances that accommodate Monte Carlo statistical noise and implementation differences. The final reward is a weighted sum of the scores from both artifacts, with the backscattered coefficient carrying a higher weight than the depth distributions. Simply reporting plausible numbers is not sufficient; you must execute the full simulation pipeline as described to obtain results that agree with the reference data.
