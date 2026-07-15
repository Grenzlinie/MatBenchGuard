# Thermal Expansivity and Mode Grüneisen Parameters of Ice Ih via Quasiharmonic Approximation

## Problem background
Water ice Ih is known to exhibit anomalous volumetric behavior at low temperatures. Understanding the origin of this behavior is important for the physics of tetrahedrally coordinated solids and amorphous ices. The underlying mechanism is thought to involve the frequency dependence of intermolecular vibrational modes. This task computes the thermal expansivity and mode-resolved Grüneisen parameters of ice Ih using a classical water model and the quasiharmonic approximation, in order to probe the contribution of different frequency bands.

## Approach
The method follows the quasiharmonic approximation: a static potential energy surface is expanded around the minimum-energy configuration to obtain harmonic vibrational frequencies. The quantum vibrational free energy is then evaluated as a function of temperature and volume. By minimizing the Gibbs free energy at a given pressure, the equilibrium volume and thermal expansivity are obtained. Mode Grüneisen parameters are derived from the volume dependence of the individual frequencies. The TIP4P/2005 water model is used to describe the intermolecular interactions. The workflow proceeds from generating a proton-disordered ice Ih unit cell, through volume-dependent normal mode calculations, to the final thermodynamic and spectral analyses.

## Reproduction target
Compute the thermal expansivity α(T) for ice Ih at an external pressure of 0.1 MPa over the temperature range 0–100 K in steps of 5 K, and save the table to alpha_vs_T.csv. Compute the frequency-resolved contribution of each normal mode, γ_j C_j, at T = 30 K, binned into 10 cm⁻¹ intervals from 0 to 200 cm⁻¹, and save to gamma_C_vs_freq.csv. Also compute the total γ C_V at T = 30 K and save to total_gamma_CV.csv. All calculations must use the TIP4P/2005 water model and the quasiharmonic approximation, without fitting to any pre-existing results.

## Assets

- TIP4P/2005 water model: 10.1063/1.2037275

## Workflow steps

### Step 1: Generate ice Ih structure
- Role: process
- Action: Create a proton-disordered hexagonal ice Ih unit cell (space group P6₃/mmc, 8 water molecules) satisfying the Bernal–Fowler ice rules. This structure is the starting configuration for all subsequent calculations.
- Evidence: `/app/outputs/iceIh_structure.xyz`

### Step 2: Quasiharmonic normal mode calculations
- Role: process
- Action: For a set of volumes spanning the expected equilibrium volume, energy-minimize the ice Ih structure using the TIP4P/2005 potential, compute the Hessian matrix, and diagonalize to obtain normal mode frequencies ω_j(V) and potential energy U_q(V) for each volume.
- Evidence: `/app/outputs/modes_data.npz`

### Step 3: Compute thermal expansivity α(T)
- Role: scored (load-bearing)
- Action: From the stored ω_j(V) and U_q(V), compute the quantum vibrational free energy A(T,V) for temperatures from 0 to 100 K (step 5 K). At each temperature, minimize the Gibbs free energy G(T,p)=A+pV with p=0.1 MPa to find the equilibrium volume V₀(T). Calculate the thermal expansivity α(T) = (1/V₀) dV₀/dT via finite differences. Output the table to alpha_vs_T.csv.
- Output file: `/app/outputs/alpha_vs_T.csv`
- Format: csv
- Contract: CSV with columns: T (K), alpha (K⁻¹). T from 0 to 100 K in steps of 5 K.
- Scoring: scored by hidden verifier

### Step 4: Mode Grüneisen parameter frequency analysis
- Role: scored (load-bearing)
- Action: From ω_j at two nearby volumes, compute mode Grüneisen parameters γ_j = −∂ ln ω_j / ∂ ln V using central finite differences. Compute mode heat capacities C_j at T=30 K via the quantum harmonic oscillator formula. Bin modes by frequency in 10 cm⁻¹ bins (range 0–200 cm⁻¹) and compute the average γ_j C_j per bin. Save the binned results to gamma_C_vs_freq.csv.
- Output file: `/app/outputs/gamma_C_vs_freq.csv`
- Format: csv
- Contract: CSV with columns: low_freq (cm⁻¹), high_freq (cm⁻¹), gamma_C (J mol⁻¹ K⁻¹). Bins of width 10 cm⁻¹ from 0 to 200 cm⁻¹.
- Scoring: scored by hidden verifier

### Step 5: Total γ C_V at 30 K
- Role: scored
- Action: Sum the mode products γ_j C_j over all modes to obtain the total γ C_V at T=30 K. Output the value to total_gamma_CV.csv.
- Output file: `/app/outputs/total_gamma_CV.csv`
- Format: csv
- Contract: CSV with columns: T (K), gamma_CV (J mol⁻¹ K⁻¹). Contains a single row for T=30 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha_vs_T.csv`
- `/app/outputs/gamma_C_vs_freq.csv`
- `/app/outputs/total_gamma_CV.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_vs_T.csv
- path: `/app/outputs/alpha_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Thermal expansivity α(T) for ice Ih at 0.1 MPa, with T from 0 to 100 K in 5 K steps.
- schema:
  - `type`: table
  - `required_columns`: `T`, `alpha`
  - `units`:
    - `T`: K
    - `alpha`: K⁻¹

### gamma_C_vs_freq.csv
- path: `/app/outputs/gamma_C_vs_freq.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Frequency‑binned (10 cm⁻¹ bins, 0–200 cm⁻¹) average γ_j C_j at T=30 K for ice Ih.
- schema:
  - `type`: table
  - `required_columns`: `low_freq`, `high_freq`, `gamma_C`
  - `units`:
    - `low_freq`: cm⁻¹
    - `high_freq`: cm⁻¹
    - `gamma_C`: J mol⁻¹ K⁻¹

### total_gamma_CV.csv
- path: `/app/outputs/total_gamma_CV.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total γ C_V at T=30 K for ice Ih (single row).
- schema:
  - `type`: table
  - `required_columns`: `T`, `gamma_CV`
  - `units`:
    - `T`: K
    - `gamma_CV`: J mol⁻¹ K⁻¹

Notes: All outputs must be computed using the TIP4P/2005 water model within the quasiharmonic approximation, without fitting to the paper's reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "alpha"
        ],
        "units": {
          "T": "K",
          "alpha": "K⁻¹"
        }
      },
      "description": "Thermal expansivity α(T) for ice Ih at 0.1 MPa, with T from 0 to 100 K in 5 K steps."
    },
    {
      "file": "gamma_C_vs_freq.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "low_freq",
          "high_freq",
          "gamma_C"
        ],
        "units": {
          "low_freq": "cm⁻¹",
          "high_freq": "cm⁻¹",
          "gamma_C": "J mol⁻¹ K⁻¹"
        }
      },
      "description": "Frequency‑binned (10 cm⁻¹ bins, 0–200 cm⁻¹) average γ_j C_j at T=30 K for ice Ih."
    },
    {
      "file": "total_gamma_CV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "gamma_CV"
        ],
        "units": {
          "T": "K",
          "gamma_CV": "J mol⁻¹ K⁻¹"
        }
      },
      "description": "Total γ C_V at T=30 K for ice Ih (single row)."
    }
  ],
  "notes": "All outputs must be computed using the TIP4P/2005 water model within the quasiharmonic approximation, without fitting to the paper's reported values."
}
```

## How you are scored
A hidden verifier inspects the three scored output files. For alpha_vs_T.csv, it evaluates whether the computed thermal expansivity across the temperature range matches the expected physical behavior (e.g., trends and characteristic temperatures) determined from unrelated experiments. For gamma_C_vs_freq.csv, it checks that the frequency-resolved contribution of the Grüneisen parameter times heat capacity follows the correct physical pattern across bins. For total_gamma_CV.csv, it compares the reported total to a hidden reference value. Each check yields a partial reward, and the final reward is a weighted combination. The verifier tolerates small numerical differences that arise from legitimate variations in implementation, basis, and numerical method, as long as the physical conclusions agree.
