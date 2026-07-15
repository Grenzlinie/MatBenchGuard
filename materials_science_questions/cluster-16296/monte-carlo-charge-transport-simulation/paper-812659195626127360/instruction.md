# Ballistic I-V Modeling of Double-Barrier Resonant Tunneling Diodes with Doped Wells

## Problem background
Double-barrier resonant tunneling diodes (DBRTDs) exhibit negative differential resistance and are promising for high-frequency oscillators. Current-voltage (I–V) characteristics are often modeled using a ballistic transport framework that assumes transverse momentum conservation. However, experimental I–V curves frequently show higher valley currents than predicted, pointing to scattering processes. To isolate the contribution of elastic scattering from band-bending effects, devices with intentional well doping (n-type, p-type, and undoped) have been fabricated. The ballistic model can be extended to include band bending due to ionized impurities by solving Poisson's equation self-consistently. The predicted I–V parameters from this model serve as a baseline: they account for band bending but not for scattering. The present task is to compute these predicted parameters for different doping profiles, which sheds light on the role of elastic scattering when compared with experimental measurements.

## Approach
Implement a one-dimensional ballistic transport model for the DBRTD. The device structure consists of a 60 Å Al0.3Ga0.7As barrier, a 50 Å GaAs well, and a 40 Å Al0.3Ga0.7As barrier, with buffer/spacer layers. Three well doping profiles are considered: (i) n-type: a 16.7 Å region in the well center doped with Si at 1.0×10^18 cm^−3; (ii) undoped: no intentional doping; (iii) p-type: a 16.7 Å region in the well center doped with Be at 1.0×10^18 cm^−3. For each profile, at a temperature of 77 K and a Fermi energy of 0.056 eV above the conduction band, the conduction band profile is obtained by solving Poisson's equation self-consistently under applied bias. The transmission coefficient for the double-barrier structure is then computed using a transfer matrix method. The current density is calculated by integrating the transmission over the electron supply function as a function of bias. From the resulting I–V curve, the peak and valley positions (mV), peak and valley current densities (A/cm^2), and the peak-to-valley ratio are extracted. The entire simulation is implemented from scratch using Python with numpy and scipy. The compensated doping case is not required for the scored output.

## Reproduction target
Produce a CSV file, `predicted_iv_parameters.csv`, with one row for each of the three well doping conditions: `n-type`, `undoped`, `p-type`. The columns are: `well_doping` (string), `peak_pos_mV` (float, mV), `valley_pos_mV` (float, mV), `peak_current_Acm2` (float, A/cm^2), `valley_current_Acm2` (float, A/cm^2), `peak_to_valley_ratio` (float). These values must correspond to the ballistic model predictions with band bending under positive bias on the top contact. The peak positions across the three doping types must satisfy the relative ordering n-type < undoped < p-type, which arises from the band-bending effects of ionized impurities. Your computed parameters will be evaluated against a hidden reference standard and the structural ordering.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute predicted I-V parameters
- Role: scored (load-bearing)
- Action: Implement a ballistic transport model for a double-barrier resonant tunneling diode. Device structure: 60 Å Al0.3Ga0.7As barrier, 50 Å GaAs well with doping profiles (n-type: 16.7 Å of 1.0×10^18 cm^−3 Si centered; undoped: no intentional doping; p-type: 16.7 Å of 1.0×10^18 cm^−3 Be centered), 40 Å Al0.3Ga0.7As barrier, plus buffer/spacer layers. Assume Fermi energy 0.056 eV above conduction band and temperature 77 K. Solve Poisson's equation self-consistently to obtain conduction band profile under bias. Compute the transmission coefficient using a transfer matrix method. Integrate over the electron supply function to obtain current density vs. voltage. Extract peak position (mV), valley position (mV), peak current density (A/cm^2), valley current density (A/cm^2), and peak-to-valley ratio for n-type, undoped, and p-type doping profiles. Write the results to predicted_iv_parameters.csv.
- Output file: `/app/outputs/predicted_iv_parameters.csv`
- Format: csv
- Contract: Columns: well_doping (string, one of 'n-type','undoped','p-type'), peak_pos_mV (float), valley_pos_mV (float), peak_current_Acm2 (float), valley_current_Acm2 (float), peak_to_valley_ratio (float). One row per doping case.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_iv_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_iv_parameters.csv
- path: `/app/outputs/predicted_iv_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted I-V parameters from ballistic transport model for each well doping profile.
- schema:
  - `type`: table
  - `required_columns`: `well_doping`, `peak_pos_mV`, `valley_pos_mV`, `peak_current_Acm2`, `valley_current_Acm2`, `peak_to_valley_ratio`
  - `units`:
    - `peak_pos_mV`: mV
    - `valley_pos_mV`: mV
    - `peak_current_Acm2`: A/cm^2
    - `valley_current_Acm2`: A/cm^2
    - `peak_to_valley_ratio`: dimensionless
  - `column_types`:
    - `well_doping`: string
    - `peak_pos_mV`: float
    - `valley_pos_mV`: float
    - `peak_current_Acm2`: float
    - `valley_current_Acm2`: float
    - `peak_to_valley_ratio`: float

Notes: The agent must implement the entire simulation from scratch; no precomputed artifacts are provided. Parameters (layer thicknesses, doping profiles, Fermi energy, temperature) are specified in the step action. The compensated doping case is excluded from the scored target because it was not tabulated in the paper's predicted results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_iv_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "well_doping",
          "peak_pos_mV",
          "valley_pos_mV",
          "peak_current_Acm2",
          "valley_current_Acm2",
          "peak_to_valley_ratio"
        ],
        "units": {
          "peak_pos_mV": "mV",
          "valley_pos_mV": "mV",
          "peak_current_Acm2": "A/cm^2",
          "valley_current_Acm2": "A/cm^2",
          "peak_to_valley_ratio": "dimensionless"
        },
        "column_types": {
          "well_doping": "string",
          "peak_pos_mV": "float",
          "valley_pos_mV": "float",
          "peak_current_Acm2": "float",
          "valley_current_Acm2": "float",
          "peak_to_valley_ratio": "float"
        }
      },
      "description": "Predicted I-V parameters from ballistic transport model for each well doping profile."
    }
  ],
  "notes": "The agent must implement the entire simulation from scratch; no precomputed artifacts are provided. Parameters (layer thicknesses, doping profiles, Fermi energy, temperature) are specified in the step action. The compensated doping case is excluded from the scored target because it was not tabulated in the paper's predicted results."
}
```

## How you are scored
A hidden verifier will read your `predicted_iv_parameters.csv` and compare each entry against a reference set of predicted values (derived from the ballistic model described in the literature). Voltage values are compared with an absolute tolerance, current densities with a relative tolerance, and the peak-to-valley ratio is also checked. Additionally, the verifier confirms that the monotonic ordering of peak positions (n-type < undoped < p-type) holds. The reward is a weighted combination of these checks, with full credit only when all values lie within tolerance and the ordering is correct. Reporting numbers without implementing the model is not sufficient; the verifier expects results that are consistent with a correct implementation of the described physical model.
