# Landauer-DMM thermal boundary conductance prediction for epitaxial metal/sapphire interfaces

## Problem background
Efficient thermal management of nanoscale devices requires understanding heat transfer across solid/solid interfaces. Thermal boundary conductance (TBC) quantifies this interfacial heat flow and is critical for predicting device temperatures. However, experimental TBC often deviates from predictions by simple acoustic mismatch models because the full phonon density of states (DOS) and dispersion over the entire Brillouin zone govern interfacial phonon transport. This work focuses on epitaxial metal/sapphire interfaces (Al, Co, Ru on c‑plane sapphire), where the interface is well‑defined and elastic phonon transmission is expected to dominate the TBC. The goal is to predict the temperature‑dependent TBC for these three interfaces using a first‑principles‑based Landauer approach and compare with experimental reference data to assess the predictive power of the method.

## Approach
The reproduction proceeds in two stages:
1. **First‑principles phonon calculations.** Perform density functional theory (DFT) calculations for bulk Al (fcc), Co (hcp), Ru (hcp), and c‑plane sapphire (corundum) using a plane‑wave code with the local density approximation (LDA). Compute harmonic force constants (via finite displacements or density‑functional perturbation theory) and post‑process with Phonopy to obtain the full‑band phonon dispersion and phonon density of states for each material. These phonon DOS are the essential input for the TBC computation.
2. **Modal nonequilibrium Landauer TBC prediction.** Implement the modal nonequilibrium Landauer method, which extends the standard Landauer formalism with a local‑temperature correction to account for nonequilibrium phonon populations near the interface. Apply the diffuse mismatch model (DMM) to compute the frequency‑dependent phonon transmission coefficient at the interface using the phonon DOS of the two materials. Then integrate over frequency and temperature to obtain the thermal boundary conductance. Compute the TBC for Al/sapphire, Co/sapphire, and Ru/sapphire at five temperatures: 100, 200, 300, 400, and 500 K.

## Reproduction target
Compute the thermal boundary conductance (in MW m⁻² K⁻¹) for the three metal/sapphire interfaces at the five specified temperatures using the methodology above. Output the results in a CSV file with columns: `interface` (one of `Al_sapphire`, `Co_sapphire`, `Ru_sapphire`), `temperature_K` (100, 200, 300, 400, 500), and `TBC_MW_m2_K` (floating point). The quality of the prediction will be assessed by the hidden verifier.

## Assets

- Crystal structures of Al, Co, Ru, and c-plane sapphire: https://materialsproject.org/ (Al: mp-134, Co: mp-54, Ru: mp-32, sapphire: mp-1143)
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Standard solid-state pseudopotentials (SSSP): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: DFT phonon DOS and dispersion calculation
- Role: process
- Action: Perform first-principles density functional theory (DFT) calculations for Al (fcc), Co (hcp), Ru (hcp), and c-plane sapphire (corundum) using an open-source plane-wave DFT code with the local density approximation (LDA). Compute harmonic force constants (via finite displacements or density-functional perturbation theory) and post-process with Phonopy to obtain full-band phonon dispersions and the phonon density of states (DOS) for each material.
- Evidence: `/app/outputs/phonon_dos.json`

### Step 2: Modal nonequilibrium Landauer TBC prediction
- Role: scored (load-bearing)
- Action: Implement the modal nonequilibrium Landauer method as described in the reference paper, using the DFT-computed phonon densities of states for Al, Co, Ru, and sapphire. Apply the diffuse mismatch model (DMM) to obtain spectral phonon transmission coefficients. Compute the temperature-dependent thermal boundary conductance (TBC) for the Al/sapphire, Co/sapphire, and Ru/sapphire interfaces at temperatures 100, 200, 300, 400, and 500 K. Write the results to a CSV file.
- Output file: `/app/outputs/tbc_output.csv`
- Format: csv
- Contract: CSV with columns: interface (string, one of Al_sapphire, Co_sapphire, Ru_sapphire), temperature_K (integer), TBC_MW_m2_K (floating point).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tbc_output.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tbc_output.csv
- path: `/app/outputs/tbc_output.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed thermal boundary conductance values for Al/sapphire, Co/sapphire, and Ru/sapphire interfaces at temperatures 100, 200, 300, 400, and 500 K.
- schema:
  - `type`: table
  - `required_columns`: `interface`, `temperature_K`, `TBC_MW_m2_K`
  - `units`:
    - `TBC_MW_m2_K`: MW m^{-2} K^{-1}

Notes: The hidden checker compares the agent's reported TBC values against reference experimental data with a tolerance, and also verifies that Co/sapphire has the highest TBC among the three interfaces.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tbc_output.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "interface",
          "temperature_K",
          "TBC_MW_m2_K"
        ],
        "units": {
          "TBC_MW_m2_K": "MW m^{-2} K^{-1}"
        }
      },
      "description": "Computed thermal boundary conductance values for Al/sapphire, Co/sapphire, and Ru/sapphire interfaces at temperatures 100, 200, 300, 400, and 500 K."
    }
  ],
  "notes": "The hidden checker compares the agent's reported TBC values against reference experimental data with a tolerance, and also verifies that Co/sapphire has the highest TBC among the three interfaces."
}
```

## How you are scored
A hidden verifier will read your output file and compare each reported TBC value against a hidden reference dataset derived from the original experimental measurements for the same interfaces and temperatures. Credit is awarded based on how closely your values match the references, using a tolerance that accounts for typical computational and methodological variations (the exact tolerance is not disclosed). In addition, a structural check verifies that the relative ordering of TBC values across interfaces is consistent with the experimental data. The final reward is a weighted combination of all comparisons; reporting numbers without performing the computational workflow will not yield a passing score.
