# Modal nonequilibrium Landauer prediction of thermal boundary conductance for epitaxial metal/sapphire interfaces

## Problem background
Thermal boundary conductance (TBC) governs heat transfer at solid/solid interfaces and is critical for thermal management in nanoscale electronic devices. Predicting TBC across metal/dielectric interfaces remains challenging: simple acoustic mismatch models often fail to capture the spectral details of phonon transport across the entire Brillouin zone. To investigate whether elastic phonon transport alone can explain measured TBC, a set of epitaxial metal/sapphire interfaces—Co/Al₂O₃, Al/Al₂O₃, and Ru/Al₂O₃—were fabricated and measured via time-domain thermoreflectance (TDTR). The experimental results were compared with theoretical predictions from the modal nonequilibrium Landauer method combined with the diffuse mismatch model and first-principles density functional theory (DFT) phonon densities of states. This task reproduces the theoretical TBC predictions for these three interfaces, allowing a direct comparison with independent experimental measurements.

## Approach
The core method is the modal nonequilibrium Landauer approach, which computes thermal boundary conductance from the perspective of phonon transmission across an interface. The spectral phonon transmission coefficient is determined using the diffuse mismatch model (DMM). In DMM, phonons are assumed to be completely diffuse at the interface and transmit according to the overlap of phonon density of states (DOS) on both sides, with no memory of their original direction or polarization. The required phonon densities of states for the metal films (Al, Co, Ru) and the c-plane sapphire substrate are obtained from first principles: density functional theory (DFT) calculations using the local density approximation (LDA) are performed to compute interatomic force constants; then phonon dispersions and the DOS (all branches, full Brillouin zone) are generated. Once the DOS is known, the Landauer formula with a local nonequilibrium correction is used to calculate the spectral heat flux as a function of temperature. Integrating over frequency yields the total TBC for each metal/sapphire interface. The method accounts only for elastic phonon transport (no inelastic scattering), so the resulting predictions test the hypothesis that elastic processes dominate the TBC for these epitaxial interfaces. The computed TBC versus temperature curves are then compared against experimental TDTR measurements to assess the predictive power of the elastic Landauer/DMM approach.

## Reproduction target
Produce a CSV file (`predicted_tbc.csv`) containing the predicted thermal boundary conductance (TBC) for Al/sapphire, Co/sapphire, and Ru/sapphire interfaces as a function of temperature, using the modal nonequilibrium Landauer method with DMM transmission and full-band DFT phonon densities of states. The TBC must be computed at least at the following temperature points: 80 K, 100 K, 150 K, 200 K, 250 K, 300 K, 350 K, 400 K, 450 K, and 500 K. The output must include columns for temperature (in K) and TBC (in MW/(m²·K)) for each of the three interfaces. The computation involves two mandatory stages: (1) DFT phonon calculations for bulk Al (FCC), Co (HCP), Ru (HCP), and c-plane sapphire (trigonal) using the LDA functional to obtain the phonon DOS, and (2) implementation of the Landauer method with DMM to compute the TBC curves. The final CSV will be evaluated against hidden experimental TDTR reference data; the predictions are not expected to match any single reported number but should capture the temperature dependence and relative magnitudes characteristic of the true physical system.

## Assets

- Crystal structures for Al (FCC), Co (HCP), Ru (HCP), and sapphire (trigonal Al2O3): https://materialsproject.org/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- phonopy: phonopy
- numpy, scipy: numpy scipy

## Workflow steps

### Step 1: DFT phonon density of states calculation
- Role: process
- Action: Perform DFT calculations with the LDA exchange-correlation functional to obtain phonon force constants for bulk Al (FCC), Co (HCP), Ru (HCP), and c-plane sapphire (trigonal). Use phonopy to compute full-band phonon dispersions and the phonon density of states (DOS) for each material. The computed DOS will be used as input to the Landauer TBC prediction in the next step.
- Evidence: `/app/outputs/dft_completion.txt`

### Step 2: Landauer thermal boundary conductance prediction
- Role: scored (load-bearing)
- Action: Implement the modal nonequilibrium Landauer method using the diffuse mismatch model (DMM) to compute spectral phonon transmission coefficients at the Al/sapphire, Co/sapphire, and Ru/sapphire interfaces, employing the phonon DOS obtained in the previous step. Compute the thermal boundary conductance (TBC) as a function of temperature from 80 K to 500 K at the following points: 80, 100, 150, 200, 250, 300, 350, 400, 450, 500 K. Write the predicted TBC values to predicted_tbc.csv.
- Output file: `/app/outputs/predicted_tbc.csv`
- Format: csv
- Contract: columns: temperature_K (float, unit K), Al_TBC_MW_m2K (float, unit MW/(m^2·K)), Co_TBC_MW_m2K (float, unit MW/(m^2·K)), Ru_TBC_MW_m2K (float, unit MW/(m^2·K)). The file must include at least the temperatures 80, 100, 150, 200, 250, 300, 350, 400, 450, 500 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_tbc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_tbc.csv
- path: `/app/outputs/predicted_tbc.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The predicted TBC values for the three metal/sapphire interfaces across the temperature range 80–500 K. The checker recomputes the mean absolute percentage error (MAPE) against hidden experimental TBC reference data from the paper and assigns a score based on MAPE thresholds.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `Al_TBC_MW_m2K`, `Co_TBC_MW_m2K`, `Ru_TBC_MW_m2K`
  - `units`:
    - `temperature_K`: K
    - `Al_TBC_MW_m2K`: MW/(m^2·K)
    - `Co_TBC_MW_m2K`: MW/(m^2·K)
    - `Ru_TBC_MW_m2K`: MW/(m^2·K)

Notes: The DFT phonon step is a required intermediate, but its outputs are not directly scored. Only the final TBC predictions are compared against experimental data. The solving agent must implement the Landauer method with DMM transmission; no precomputed DOS or TBC values are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_tbc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "Al_TBC_MW_m2K",
          "Co_TBC_MW_m2K",
          "Ru_TBC_MW_m2K"
        ],
        "units": {
          "temperature_K": "K",
          "Al_TBC_MW_m2K": "MW/(m^2·K)",
          "Co_TBC_MW_m2K": "MW/(m^2·K)",
          "Ru_TBC_MW_m2K": "MW/(m^2·K)"
        }
      },
      "description": "The predicted TBC values for the three metal/sapphire interfaces across the temperature range 80–500 K. The checker recomputes the mean absolute percentage error (MAPE) against hidden experimental TBC reference data from the paper and assigns a score based on MAPE thresholds."
    }
  ],
  "notes": "The DFT phonon step is a required intermediate, but its outputs are not directly scored. Only the final TBC predictions are compared against experimental data. The solving agent must implement the Landauer method with DMM transmission; no precomputed DOS or TBC values are provided."
}
```

## How you are scored
A hidden verifier will read your output file(s) and compare them against experimental reference measurements that are not visible to you. The primary score is based on the accuracy of your predicted TBC values relative to the hidden experimental data, computed as the mean absolute percentage error (MAPE) at the required temperature points; closer agreement yields a higher score. Small structural checks (e.g., monotonic temperature dependence, relative ordering at 300 K) may contribute a minor fraction of the total score. Your predicted TBC values must be the genuine result of the Landauer method using your DFT-derived densities of states; simply writing plausible numbers will not achieve a high score. The DFT step is a required intermediate but is not directly scored—only the final `predicted_tbc.csv` is evaluated. The verifier will independently assess your CSV file against the hidden gold values; there is no need for you to compute any self-evaluation metric.
