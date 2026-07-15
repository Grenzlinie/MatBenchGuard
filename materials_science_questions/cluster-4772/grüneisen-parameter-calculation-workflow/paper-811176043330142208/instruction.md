# Effective phonon spectra and thermal properties of ScF3

## Problem background
Scandium fluoride (ScF$_3$) is an empty perovskite that exhibits strong negative thermal expansion (NTE) over a wide temperature range. Simple quasiharmonic calculations give contradictory results for its lattice parameter and thermal expansion, and the role of anharmonicity in determining the material's thermal properties is not yet settled. This task addresses the open problem of whether ab initio calculations that incorporate temperature-dependent anharmonic effects can quantitatively describe the lattice parameter, thermal conductivity, and Grüneisen parameter of ScF$_3$ from low to high temperatures—without relying on empirical adjustments.

## Approach
The core idea is to compute temperature-dependent effective interatomic force constants (IFCs) via a self-consistent loop that couples density functional theory (DFT) with a quantum harmonic model of the atomic displacements. Starting from a harmonic phonon reference, the loop iterates the following for each target temperature: (i) build a quantum covariance matrix from the current phonon spectrum; (ii) generate random supercell displacement configurations from that Gaussian distribution; (iii) compute DFT forces for each configuration; (iv) fit second- and third-order IFCs by least-squares regression of the forces; (v) update the phonon spectrum from the new second-order IFCs; (vi) estimate the internal pressure from the DFT forces and a quasiharmonic kinetic term, then adjust the lattice parameter until the total pressure vanishes. Electronic thermal excitations are included via Fermi-Dirac occupation smearing. After convergence, the temperature-dependent IFCs and lattice parameters are obtained.

Using these IFCs, the lattice thermal conductivity is solved via the full phonon Boltzmann transport equation. Mode Grüneisen parameters are computed from the third-order IFCs, and the weighted Grüneisen parameter is evaluated as a function of temperature. The protocol avoids phenomenological parameters and relies solely on the first-principles inputs: the crystal structure and open-source DFT/PBEsol calculations.

## Reproduction target
Produce three scored CSV files under `/app/outputs`:

- `lattice_parameter_vs_temperature.csv` – the equilibrium lattice parameter (in Å) at T = 0, 300, 600, 900, 1200, 1500 K, obtained from the fully self-consistent anharmonic protocol.
- `thermal_conductivity_vs_temperature.csv` – the lattice thermal conductivity (in W/mK) at T = 300, 600, 900, 1200, 1500 K.
- `weighted_gruneisen_parameter_vs_temperature.csv` – the weighted Grüneisen parameter (dimensionless) at T = 0, 300, 600, 900, 1200, 1500 K.

Each file must follow the exact column layout and temperature points specified in the workflow steps. The goal is to reproduce the temperature evolution of these quantities as predicted by the anharmonic first-principles method described below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- ShengBTE: https://www.shengbte.org
- PBEsol pseudopotentials for Sc and F: https://www.materialscloud.org/discover/sssp/#!/efficiency
- Phonopy: https://phonopy.github.io/phonopy/
- thirdorder.py: https://github.com/thirdorder/thirdorder
- Cubic ScF3 primitive cell

## Workflow steps

### Step 1: Harmonic phonon reference calculation
- Role: process
- Action: Compute the harmonic phonon frequencies and eigenvectors for a 4×4×4 supercell of cubic ScF3 using DFT with the PBEsol exchange‑correlation functional and small‑displacement finite differences. This provides the initial phonon spectrum needed to start the self‑consistent loop.
- Evidence: `/app/outputs/harmonic_phonon_frequencies.json`

### Step 2: Self‑consistent anharmonic IFC fitting and lattice parameter optimization
- Role: scored (load-bearing)
- Action: For each target temperature (0, 300, 600, 900, 1200, 1500 K) perform the iterative temperature‑dependent effective phonon protocol: (a) compute the quantum covariance matrix Σ from the current phonon spectrum at the Γ point of a 4×4×4 supercell; (b) generate random atomic displacement configurations from a multidimensional Gaussian with covariance Σ; (c) run DFT to obtain forces for each configuration; (d) fit effective second‑ and third‑order interatomic force constants (third‑order cutoff 5 Å) via least‑squares regression; (e) update the phonon spectrum from the fitted second‑order IFCs; (f) compute the mean DFT pressure and the quasiharmonic kinetic‑energy derivative, and update the lattice parameter until the total external pressure vanishes. Include electronic thermal excitations through Fermi‑Dirac occupations in DFT. Iterate until self‑consistency is reached. Record the converged lattice parameter a(T).
- Output file: `/app/outputs/lattice_parameter_vs_temperature.csv`
- Format: csv
- Contract: columns: temperature_K (integer), lattice_parameter_A (float). Rows for T = 0, 300, 600, 900, 1200, 1500 K.
- Scoring: scored by hidden verifier

### Step 3: Calculation of thermal conductivity
- Role: scored
- Action: Using the temperature‑dependent effective second‑ and third‑order IFCs obtained from the self‑consistent loop, solve the full phonon Boltzmann transport equation on a well‑converged q‑point grid to obtain the lattice thermal conductivity κ(T) at T = 300, 600, 900, 1200, 1500 K.
- Output file: `/app/outputs/thermal_conductivity_vs_temperature.csv`
- Format: csv
- Contract: columns: temperature_K (integer), thermal_conductivity_W_mK (float). Rows for T = 300, 600, 900, 1200, 1500 K.
- Scoring: scored by hidden verifier

### Step 4: Weighted Grüneisen parameter analysis
- Role: scored
- Action: From the same IFCs and phonon frequencies, compute mode‑dependent Grüneisen parameters and evaluate the weighted Grüneisen parameter γ(T) for T = 0, 300, 600, 900, 1200, 1500 K.
- Output file: `/app/outputs/weighted_gruneisen_parameter_vs_temperature.csv`
- Format: csv
- Contract: columns: temperature_K (integer), weighted_gruneisen_parameter (float). Rows for T = 0, 300, 600, 900, 1200, 1500 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameter_vs_temperature.csv`
- `/app/outputs/thermal_conductivity_vs_temperature.csv`
- `/app/outputs/weighted_gruneisen_parameter_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameter_vs_temperature.csv
- path: `/app/outputs/lattice_parameter_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: ScF3 lattice parameter computed from the self‑consistent anharmonic protocol; compared to experimental reference with tolerance
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `lattice_parameter_A`
  - `units`:
    - `temperature_K`: K
    - `lattice_parameter_A`: Å

### thermal_conductivity_vs_temperature.csv
- path: `/app/outputs/thermal_conductivity_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Lattice thermal conductivity predicted from temperature‑dependent IFCs; verified for trend, scaling exponent, and magnitude
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `thermal_conductivity_W_mK`
  - `units`:
    - `temperature_K`: K
    - `thermal_conductivity_W_mK`: W/mK

### weighted_gruneisen_parameter_vs_temperature.csv
- path: `/app/outputs/weighted_gruneisen_parameter_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Weighted Grüneisen parameter showing sign and trend, including suppression of negative thermal expansion near 1100 K
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `weighted_gruneisen_parameter`
  - `units`:
    - `temperature_K`: K
    - `weighted_gruneisen_parameter`: dimensionless

Notes: All scored artifacts are produced by re-running the computational protocol. The checker compares lattice parameter to experimental data, verifies thermal conductivity trend and exponent, and checks Grüneisen sign change and zero crossing. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameter_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "lattice_parameter_A"
        ],
        "units": {
          "temperature_K": "K",
          "lattice_parameter_A": "Å"
        }
      },
      "description": "ScF3 lattice parameter computed from the self‑consistent anharmonic protocol; compared to experimental reference with tolerance"
    },
    {
      "file": "thermal_conductivity_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "thermal_conductivity_W_mK"
        ],
        "units": {
          "temperature_K": "K",
          "thermal_conductivity_W_mK": "W/mK"
        }
      },
      "description": "Lattice thermal conductivity predicted from temperature‑dependent IFCs; verified for trend, scaling exponent, and magnitude"
    },
    {
      "file": "weighted_gruneisen_parameter_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "weighted_gruneisen_parameter"
        ],
        "units": {
          "temperature_K": "K",
          "weighted_gruneisen_parameter": "dimensionless"
        }
      },
      "description": "Weighted Grüneisen parameter showing sign and trend, including suppression of negative thermal expansion near 1100 K"
    }
  ],
  "notes": "All scored artifacts are produced by re-running the computational protocol. The checker compares lattice parameter to experimental data, verifies thermal conductivity trend and exponent, and checks Grüneisen sign change and zero crossing. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden automatic verifier evaluates each of the three output artifacts independently. The lattice parameter values are compared against an experimental reference with a tolerance that rewards agreement, without penalizing small implementation-dependent deviations. The thermal conductivity is checked for its temperature trend (monotonic decrease, approximate power-law form) and for physically reasonable magnitudes. The weighted Grüneisen parameter is examined for its sign at low and high temperatures, its overall temperature dependence, and a key feature of its behavior. The three checks are combined with predefined weights into a final reward between 0 and 1. The scoring is fully automatic and deterministic; no manual inspection is performed.
