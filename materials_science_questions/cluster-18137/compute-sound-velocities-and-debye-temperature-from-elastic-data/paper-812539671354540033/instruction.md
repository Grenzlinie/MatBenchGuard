# Modal Nonequilibrium Landauer Thermal Boundary Conductance Prediction

## Problem background
Thermal boundary conductance (TBC) across solid/solid interfaces is critical for thermal management in nanoscale devices. Predicting TBC from first principles is challenging because it depends on detailed phonon spectra and interfacial transmission mechanisms. The modal nonequilibrium Landauer method, combined with phonon densities of states (DOS) from density functional theory (DFT) and a diffuse mismatch model (DMM) for phonon transmission, is a candidate approach to compute TBC without adjustable parameters. This task evaluates the ability of that modeling framework to reproduce temperature-dependent TBC across epitaxial metal/sapphire interfaces — specifically Al/sapphire, Co/sapphire, and Ru/sapphire — by comparing the computed TBC against experimental measurements.

## Approach
The modeling strategy consists of two stages. First, use DFT to compute the full-band phonon density of states for the bulk materials: Al (fcc), Co (hcp), Ru (hcp), and c-plane sapphire (Al₂O₃). Second, for each metal/sapphire interface, compute the spectral phonon transmission coefficient from the DOS via the diffuse mismatch model, then obtain the temperature-dependent TBC using the modal nonequilibrium Landauer formalism, which incorporates a local-temperature correction for nonequilibrium near the interface. The Landauer expression integrates over frequency and phonon branches; the DMM transmission coefficient is determined by the relative phonon DOS of the two sides, assuming diffuse scattering at the interface. The calculations are performed for temperatures from 80 K to 500 K. The DFT stage can be carried out with any open-source plane-wave code and suitable pseudopotentials; the TBC calculation can be implemented in Python using standard numerical libraries.

## Reproduction target
Produce a CSV file named `TBC_vs_temperature.csv` containing the predicted thermal boundary conductance for the three interfaces. The file must have exactly three columns: `temperature` (float, in K), `interface` (string: one of `Al_sapphire`, `Co_sapphire`, `Ru_sapphire`), and `TBC` (float, in MW m⁻² K⁻¹). Include rows for each interface at the following temperatures: 80, 100, 150, 200, 250, 300, 350, 400, 450, and 500 K. The TBC values must be derived from the DFT-computed phonon DOS and the modal nonequilibrium Landauer/DMM approach described in the workflow steps.

## Assets

- Crystal structures of Al (fcc), Co (hcp), Ru (hcp), and Al2O3 (corundum) from Materials Project: https://materialsproject.org/
- SSSP efficiency library pseudopotentials (LDA): https://www.materialscloud.org/discover/sssp/
- Quantum ESPRESSO (pw.x and ph.x): https://www.quantum-espresso.org/
- Phonopy: phonopy
- Python scientific libraries (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: DFT Phonon DOS Calculation
- Role: process
- Action: Compute the full-band phonon density of states (DOS) and dispersion for bulk Al (fcc), Co (hcp), Ru (hcp), and c-plane sapphire (Al2O3) using density functional theory. Use Quantum ESPRESSO (pw.x, ph.x) with the local-density approximation (LDA) and SSSP efficiency pseudopotentials. Post-process with Phonopy to obtain the total phonon DOS versus frequency for each material.
- Evidence: `/app/outputs/dos_data.npz`

### Step 2: Modal Nonequilibrium Landauer TBC Calculation
- Role: scored (load-bearing)
- Action: Implement the modal nonequilibrium Landauer method with a local temperature correction. For each interface (Al/sapphire, Co/sapphire, Ru/sapphire), compute the spectral phonon transmission coefficient using the diffuse mismatch model (DMM) based on the DFT-computed phonon DOS from step_01. Using the Landauer formalism, calculate the temperature-dependent thermal boundary conductance (TBC) for temperatures 80, 100, 150, 200, 250, 300, 350, 400, 450, 500 K.
- Output file: `/app/outputs/TBC_vs_temperature.csv`
- Format: csv
- Contract: columns: temperature (float, K), interface (string, one of Al_sapphire, Co_sapphire, Ru_sapphire), TBC (float, MW/m²K). Rows for each interface at each temperature: 80,100,150,200,250,300,350,400,450,500 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/TBC_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### TBC_vs_temperature.csv
- path: `/app/outputs/TBC_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted thermal boundary conductance (TBC) as a function of temperature for three metal/sapphire interfaces.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `interface`, `TBC`
  - `units`:
    - `temperature`: K
    - `TBC`: MW/m²K

Notes: The checker compares against hidden paper-reported experimental TBC values using mean absolute error (MAE) with a tolerance. Full credit is awarded if MAE ≤ specified threshold; reward decays for larger errors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "TBC_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "interface",
          "TBC"
        ],
        "units": {
          "temperature": "K",
          "TBC": "MW/m²K"
        }
      },
      "description": "Predicted thermal boundary conductance (TBC) as a function of temperature for three metal/sapphire interfaces."
    }
  ],
  "notes": "The checker compares against hidden paper-reported experimental TBC values using mean absolute error (MAE) with a tolerance. Full credit is awarded if MAE ≤ specified threshold; reward decays for larger errors."
}
```

## How you are scored
A hidden verifier compares the TBC values in your submitted CSV against a set of hidden experimental reference data (measured TBC for the same interfaces and temperatures). It calculates the mean absolute error (MAE) between your predictions and the hidden references. The final reward is a number between 0 and 1: full credit (1.0) is awarded when the MAE is at or below a predetermined threshold; for MAE larger than the threshold the reward decreases linearly, reaching zero at twice the threshold. The exact threshold and the reference data are not disclosed. Formatting errors (missing columns, incorrect interface names, extra or missing rows) result in a low or zero score. You must produce the CSV exactly as specified in the output contract.
