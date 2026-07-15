# First-principles magnetotransport protocol for narrow-gap semiconductors

## Problem background
The narrow-gap semiconductor ZrTe5 exhibits unusual magnetotransport properties: a resistivity peak as a function of temperature, nonlinear Hall resistivity that can reverse sign, and non-saturating magnetoresistance at elevated temperatures. The physical origin of these anomalies has been debated, with proposed mechanisms including topological phase transitions and multi-carrier effects. In this task we implement a first-principles computational protocol that combines density functional theory (DFT) and semiclassical Boltzmann transport in the relaxation-time approximation to compute the temperature- and magnetic-field-dependent resistivity and Hall resistivity of ZrTe5. The goal is to reproduce these hallmark transport curves for three fixed doping levels and thereby examine whether the multi-carrier picture and Fermi surface geometry can account for the observations without invoking topology or correlations.

## Approach
The workflow consists of an ab initio electronic structure calculation to obtain the band structure of ZrTe5, followed by the construction of a tight-binding Hamiltonian using maximally-localized Wannier functions. From this Hamiltonian we compute the electronic density of states (DOS) for the conduction and valence bands. The temperature-dependent chemical potential is then determined by solving the charge neutrality condition for fixed net carrier concentrations (n0 = -3.0e18, 1.0e18, 3.0e18 cm⁻³) — i.e., demanding that the difference between the electron and hole concentrations, each obtained by integrating the DOS with the Fermi–Dirac distribution, equals n0 at every temperature.

Parallelly, we compute the band-resolved magnetoconductivity per relaxation time, σ_n(Bτ)/τ_n, on a dense grid of chemical potential and temperature, using the semiclassical Boltzmann transport equation in the presence of a magnetic field. The total resistivity times relaxation time, ρ(Bτ, μ, T)τ, is obtained by inverting the sum of the band conductivities. Interpolating this precomputed grid at the self-consistent chemical potential μ(T) yields ρτ as a function of temperature and Bτ for each doping.

To convert ρτ to absolute resistivity, we model the relaxation time τ(T) using a Bloch–Grüneisen formula with the parameters ρ0=1.06, α=11, n=2, and the Debye temperature ΘR=600 K, and we enforce a carrier-type ratio τ_h(T) = 5 τ_e(T). Combining τ(T) with the interpolated ρτ gives the full longitudinal and Hall resistivity tensors as functions of temperature (35–275 K) and magnetic field (0–9 T). The final outputs are the zero-field resistivity anomaly, the Hall resistivity with its nonlinear and sign-change features, and the field-dependent magnetoresistance.

## Reproduction target
Produce the following four datasets for the narrow-gap semiconductor ZrTe5, covering the temperature range 35–275 K and magnetic fields 0–9 T at the three fixed doping levels n0 = -3.0e18, 1.0e18, 3.0e18 cm⁻³:
1. Temperature-dependent chemical potential: μ(T) for each doping level.
2. Zero-field resistivity: ρ(T) ≡ ρ(B=0, T) for each doping level, showing the characteristic anomaly.
3. Hall resistivity: ρ_yx(B,T) for each doping level, at field steps of 0.5 T and temperature steps of 10 K, revealing the nonlinear field dependence and any sign reversal in electron-doped cases.
4. Magnetoresistance: MR(B,T) = [ρ_xx(B,T) – ρ_xx(0,T)] / ρ_xx(0,T) for each doping level, over the same B,T grid, exhibiting non-saturating behavior at high temperatures.
All outputs must be written as CSV files according to the schemas specified in the output contract.

## Assets

- ZrTe5 crystal structure: https://materialsproject.org/materials/mp-541688
- Quantum ESPRESSO: https://www.quantum-espresso.org
- Wannier90: https://github.com/wannier-developers/wannier90
- WannierTools: https://github.com/wannier-tools/wanniertools
- BoltzTraP2: https://gitlab.com/sousaw/BoltzTraP2

## Workflow steps

### Step 1: DFT band structure and tight-binding Hamiltonian construction
- Role: process
- Action: Perform a first-principles DFT calculation on the ZrTe5 crystal structure using an open-source code (e.g., Quantum ESPRESSO) to obtain the band structure. Then construct a maximally-localized Wannier tight-binding model via Wannier90 that reproduces the DFT bands.
- Evidence: `/app/outputs/wannier_hr.dat`

### Step 2: Density of states computation
- Role: process
- Action: Compute the density of states (DOS) for conduction and valence bands from the tight-binding Hamiltonian using a dense k-mesh, preparing for chemical potential determination.
- Evidence: `/app/outputs/dos_data.npy`

### Step 3: Temperature-dependent chemical potential μ(T)
- Role: scored
- Action: For the specified net doping levels n0 = -3.0e18, 1.0e18, 3.0e18 cm⁻³, solve the charge neutrality condition using the computed DOS and the Fermi-Dirac distribution to obtain μ(T) in the temperature range 35–275 K.
- Output file: `/app/outputs/step_01_mu_T.csv`
- Format: csv
- Contract: CSV columns: temperature (K), mu_n0=-3e18 (eV), mu_n0=1e18 (eV), mu_n0=3e18 (eV)
- Scoring: scored by hidden verifier

### Step 4: Magnetoconductivity per relaxation time grid
- Role: process
- Action: Using the tight-binding Hamiltonian and the semiclassical Boltzmann transport equation, compute the band-resolved magnetoconductivity per relaxation time σ_n(Bτ)/τ_n on a dense grid of chemical potential μ and temperature T. Then form the total resistivity times relaxation time ρ(Bτ, μ, T)τ = [∑_n σ_n(Bτ)/τ_n]⁻¹.
- Evidence: `/app/outputs/rho_tau_grid.hdf5`

### Step 5: Interpolation of ρτ for fixed doping
- Role: process
- Action: For each fixed n0, interpolate the precomputed ρ(Bτ, μ, T)τ grid at the self-consistent chemical potential μ(T) from step_01 to obtain ρ(Bτ, μ(T), T)τ as a function of temperature and Bτ.
- Evidence: `/app/outputs/interpolated_rho_tau.csv`

### Step 6: Relaxation time τ(T) from Bloch-Grüneisen model
- Role: process
- Action: Compute the temperature-dependent relaxation time τ(T) using the Bloch–Grüneisen formula with the parameters ρ0=1.06, α=11, n=2, Θ_R=600, and the proportionality τ(T) ∝ 1/ρ_sc(T). Apply the carrier-type ratio τ_h(T) = 5 τ_e(T) as used in the paper.
- Evidence: `/app/outputs/tau_T.csv`

### Step 7: Absolute magnetoresistivity combination
- Role: process
- Action: Combine the interpolated resistivity-per-relaxation-time with τ(T) to obtain absolute resistivity tensors (longitudinal and Hall resistivities) as functions of B, T, and doping, on a grid B ∈ [0, 9] T and T ∈ [35, 275] K.
- Evidence: `/app/outputs/full_transport_tensor.hdf5`

### Step 8: Zero-field resistivity anomaly
- Role: scored (load-bearing)
- Action: Extract the zero-field resistivity ρ(B=0, T) for the three doping levels from the absolute resistivity data, and write to CSV.
- Output file: `/app/outputs/step_02_resistivity_zero_field.csv`
- Format: csv
- Contract: CSV columns: temperature (K), rho_n0=-3e18 (μΩ·cm), rho_n0=1e18 (μΩ·cm), rho_n0=3e18 (μΩ·cm)
- Scoring: scored by hidden verifier

### Step 9: Hall resistivity curves
- Role: scored
- Action: Extract the Hall resistivity ρ_yx(B,T) for the three doping levels across B ∈ [0,9] T (0.5 T steps) and T ∈ [35,275] K (10 K steps) from the absolute resistivity data, and write to CSV.
- Output file: `/app/outputs/step_03_hall_resistivity.csv`
- Format: csv
- Contract: CSV columns: B (T), temperature (K), rho_yx_n0=-3e18 (μΩ·cm), rho_yx_n0=1e18 (μΩ·cm), rho_yx_n0=3e18 (μΩ·cm)
- Scoring: scored by hidden verifier

### Step 10: Magnetoresistance curves
- Role: scored
- Action: Compute the magnetoresistance MR(B,T) = [ρ_xx(B,T) – ρ_xx(0,T)] / ρ_xx(0,T) for the three doping levels over the same B,T grid, and write to CSV.
- Output file: `/app/outputs/step_04_magnetoresistance.csv`
- Format: csv
- Contract: CSV columns: B (T), temperature (K), MR_n0=-3e18 (dimensionless), MR_n0=1e18 (dimensionless), MR_n0=3e18 (dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mu_T.csv`
- `/app/outputs/step_02_resistivity_zero_field.csv`
- `/app/outputs/step_03_hall_resistivity.csv`
- `/app/outputs/step_04_magnetoresistance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mu_T.csv
- path: `/app/outputs/step_01_mu_T.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature-dependent chemical potential for three fixed doping levels. The structural auditor verifies the trend (decrease toward mid‑gap) and that the curves for different doping levels are ordered correctly with respect to peak shifts.
- schema:
  - `type`: table
  - `required_columns`: `temperature (K)`, `mu_n0=-3e18 (eV)`, `mu_n0=1e18 (eV)`, `mu_n0=3e18 (eV)`
  - `units`:
    - `temperature (K)`: K
    - `mu_n0=-3e18 (eV)`: eV
    - `mu_n0=1e18 (eV)`: eV
    - `mu_n0=3e18 (eV)`: eV

### step_02_resistivity_zero_field.csv
- path: `/app/outputs/step_02_resistivity_zero_field.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Zero‑field resistivity curves showing the characteristic anomaly. Scoring checks that a peak exists for each doping level and that the peak temperature T_P matches the hidden reference (within ±10 K after spline interpolation).
- schema:
  - `type`: table
  - `required_columns`: `temperature (K)`, `rho_n0=-3e18 (μΩ·cm)`, `rho_n0=1e18 (μΩ·cm)`, `rho_n0=3e18 (μΩ·cm)`
  - `units`:
    - `temperature (K)`: K
    - `rho_n0=-3e18 (μΩ·cm)`: μΩ·cm
    - `rho_n0=1e18 (μΩ·cm)`: μΩ·cm
    - `rho_n0=3e18 (μΩ·cm)`: μΩ·cm

### step_03_hall_resistivity.csv
- path: `/app/outputs/step_03_hall_resistivity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Field‑dependent Hall resistivity at multiple temperatures and doping levels. Scoring verifies that the electron‑doped curves (n0 = 1e18, 3e18) exhibit a sign reversal (zero crossing in ρ_yx) at intermediate temperatures (50–200 K), as demanded by the structural checker.
- schema:
  - `type`: table
  - `required_columns`: `B (T)`, `temperature (K)`, `rho_yx_n0=-3e18 (μΩ·cm)`, `rho_yx_n0=1e18 (μΩ·cm)`, `rho_yx_n0=3e18 (μΩ·cm)`
  - `units`:
    - `B (T)`: T
    - `temperature (K)`: K
    - `rho_yx_n0=-3e18 (μΩ·cm)`: μΩ·cm
    - `rho_yx_n0=1e18 (μΩ·cm)`: μΩ·cm
    - `rho_yx_n0=3e18 (μΩ·cm)`: μΩ·cm

### step_04_magnetoresistance.csv
- path: `/app/outputs/step_04_magnetoresistance.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetoresistance MR(B,T) = (ρ_xx(B) – ρ_xx(0))/ρ_xx(0). Scoring checks that at 275 K the MR is monotonically increasing with B and does not saturate (slope at 9 T exceeds a hidden threshold scaled by zero‑field resistivity).
- schema:
  - `type`: table
  - `required_columns`: `B (T)`, `temperature (K)`, `MR_n0=-3e18 (dimensionless)`, `MR_n0=1e18 (dimensionless)`, `MR_n0=3e18 (dimensionless)`
  - `units`:
    - `B (T)`: T
    - `temperature (K)`: K
    - `MR_n0=-3e18 (dimensionless)`: dimensionless
    - `MR_n0=1e18 (dimensionless)`: dimensionless
    - `MR_n0=3e18 (dimensionless)`: dimensionless

Notes: All scored artifacts undergo structural verification (T3) against hidden reference curves digitized from the paper’s figures. The checkers extract peak positions, zero crossings, and monotonicity trends rather than exact pointwise equality.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mu_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature (K)",
          "mu_n0=-3e18 (eV)",
          "mu_n0=1e18 (eV)",
          "mu_n0=3e18 (eV)"
        ],
        "units": {
          "temperature (K)": "K",
          "mu_n0=-3e18 (eV)": "eV",
          "mu_n0=1e18 (eV)": "eV",
          "mu_n0=3e18 (eV)": "eV"
        }
      },
      "description": "Temperature-dependent chemical potential for three fixed doping levels. The structural auditor verifies the trend (decrease toward mid‑gap) and that the curves for different doping levels are ordered correctly with respect to peak shifts."
    },
    {
      "file": "step_02_resistivity_zero_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature (K)",
          "rho_n0=-3e18 (μΩ·cm)",
          "rho_n0=1e18 (μΩ·cm)",
          "rho_n0=3e18 (μΩ·cm)"
        ],
        "units": {
          "temperature (K)": "K",
          "rho_n0=-3e18 (μΩ·cm)": "μΩ·cm",
          "rho_n0=1e18 (μΩ·cm)": "μΩ·cm",
          "rho_n0=3e18 (μΩ·cm)": "μΩ·cm"
        }
      },
      "description": "Zero‑field resistivity curves showing the characteristic anomaly. Scoring checks that a peak exists for each doping level and that the peak temperature T_P matches the hidden reference (within ±10 K after spline interpolation)."
    },
    {
      "file": "step_03_hall_resistivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "B (T)",
          "temperature (K)",
          "rho_yx_n0=-3e18 (μΩ·cm)",
          "rho_yx_n0=1e18 (μΩ·cm)",
          "rho_yx_n0=3e18 (μΩ·cm)"
        ],
        "units": {
          "B (T)": "T",
          "temperature (K)": "K",
          "rho_yx_n0=-3e18 (μΩ·cm)": "μΩ·cm",
          "rho_yx_n0=1e18 (μΩ·cm)": "μΩ·cm",
          "rho_yx_n0=3e18 (μΩ·cm)": "μΩ·cm"
        }
      },
      "description": "Field‑dependent Hall resistivity at multiple temperatures and doping levels. Scoring verifies that the electron‑doped curves (n0 = 1e18, 3e18) exhibit a sign reversal (zero crossing in ρ_yx) at intermediate temperatures (50–200 K), as demanded by the structural checker."
    },
    {
      "file": "step_04_magnetoresistance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "B (T)",
          "temperature (K)",
          "MR_n0=-3e18 (dimensionless)",
          "MR_n0=1e18 (dimensionless)",
          "MR_n0=3e18 (dimensionless)"
        ],
        "units": {
          "B (T)": "T",
          "temperature (K)": "K",
          "MR_n0=-3e18 (dimensionless)": "dimensionless",
          "MR_n0=1e18 (dimensionless)": "dimensionless",
          "MR_n0=3e18 (dimensionless)": "dimensionless"
        }
      },
      "description": "Magnetoresistance MR(B,T) = (ρ_xx(B) – ρ_xx(0))/ρ_xx(0). Scoring checks that at 275 K the MR is monotonically increasing with B and does not saturate (slope at 9 T exceeds a hidden threshold scaled by zero‑field resistivity)."
    }
  ],
  "notes": "All scored artifacts undergo structural verification (T3) against hidden reference curves digitized from the paper’s figures. The checkers extract peak positions, zero crossings, and monotonicity trends rather than exact pointwise equality."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the scored CSV artifacts. The verifier does not check point-by-point numerical equality; instead it extracts physically meaningful, structural features from your data and compares them against hidden reference characteristics. For the zero-field resistivity, the verifier locates the peak temperature for each doping and checks whether those peaks appear in the expected range. For the Hall resistivity, it verifies that the electron-doped curves exhibit a sign reversal (zero crossing) at intermediate temperatures. For the magnetoresistance, it confirms that the curves at the highest temperature are monotonically increasing with field and do not saturate. Each scored stage contributes a weighted fraction to the final reward, with the zero-field resistivity (load-bearing) carrying the largest weight. Reporting the paper's numeric values without executing the pipeline cannot produce the required curve shapes and structural features, and will not pass the verifier.
