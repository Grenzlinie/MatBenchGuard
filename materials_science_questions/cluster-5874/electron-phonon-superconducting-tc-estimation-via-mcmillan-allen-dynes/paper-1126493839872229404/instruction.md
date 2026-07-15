# Self-consistent one-loop LW slave-rotor study of Hubbard model spin liquid

## Problem background
The Hubbard model on a triangular lattice is a fundamental model for strongly correlated electrons and may host a U(1) quantum spin liquid (QSL) phase with a spinon Fermi surface. Recent measurements on quasi‑2D materials such as 1T‑TaS₂ and 1T‑TaSe₂ report anomalous low‑temperature specific heat and impurity‑induced resonant features that are thought to be signatures of such a spin liquid. Understanding this physics requires going beyond mean‑field treatments to capture gauge fluctuations and the interplay between spinon and chargon degrees of freedom. The present task builds a self‑consistent Luttinger–Ward framework combined with a slave‑rotor decomposition to compute the electron specific heat, the impurity spectral function, and the spinon thermal conductivity — quantities that are central to identifying and characterising a U(1) quantum spin liquid.

## Approach
The starting point is the Hubbard Hamiltonian, where the electron operator is rewritten as a product of a spinon (fermion) and a chargon (boson) through a U(1) slave‑rotor decomposition. The kinetic hopping term becomes a four‑field interaction. A Luttinger–Ward functional is constructed at the one‑loop level, including Hartree–Fock, self‑interaction (RPA‑type), and binding diagrams. Functional derivatives of this functional yield self‑consistent Dyson equations for the spinon and chargon Green’s functions, together with the constraints on the Lagrange multipliers that enforce the mean charge and angular momentum. The effective kinetic interactions (T_self, T_bind) derived from the two‑particle diagrams are then used to reconstruct the physical electron bound‑state Green’s function via a Bethe–Salpeter equation that binds spinon and chargon on the same lattice site. For the impurity problem, the same functional approach is extended: a magnetic impurity hybridizes with the spin liquid, and the coupled spinon/chargon Green’s functions are solved within a first‑order self‑consistent Born approximation; the impurity electron Green’s function then receives an additional binding correction. Matsubara results are analytically continued to real frequencies (using IR basis and Nevanlinna or equivalent) to obtain spectral functions. The specific heat is computed from the temperature‑dependent internal energy of the electron bound state, and the thermal conductivity is obtained from the spinon energy current‑current correlation function.

## Reproduction target
Implement the self‑consistent one‑loop Luttinger–Ward slave‑rotor solution for the triangular‑lattice Hubbard model with hopping t = 0.0913935 eV and Hubbard U = 0.775 eV, and compute the following quantities:

1. The electronic specific heat divided by temperature, C_V/T, as a function of T². Produce this curve using the temperature‑dependent electron Green’s function, sampling at least 10 temperatures in the range 1–20 K.

2. The impurity electron spectral function A_d(ω) for an impurity coupled to the host with hybridization V = 0.2 eV and on‑site Coulomb repulsion U_imp = 3 eV. Solve the impurity self‑consistent equations and compute the impurity electron Green’s function including the binding interaction; output the real‑frequency spectral function on a grid that covers −2.0 eV to 2.0 eV with at least 200 points.

3. The spinon thermal conductivity κ_f as a function of temperature. Compute the DC conductivity from the spinon energy current‑current correlation function at the lowest bosonic Matsubara frequency and derive κ_f. Report results for at least 8 temperatures in the range 5–50 K.

All three outputs must be written as CSV files under /app/outputs according to the schema specified in the output contract. The computed curves should reflect the physics of the one‑loop Luttinger–Ward slave‑rotor treatment, including the effects of gauge fluctuations beyond mean‑field theory.

## Assets

- Python scientific computing stack (NumPy, SciPy, Matplotlib): numpy scipy matplotlib
- Intermediate Representation (IR) basis library (sparse-ir): https://github.com/SpM-lab/sparse-ir
- Nevanlinna analytic continuation library: https://github.com/ShinaokaGroup/Nevanlinna

## Workflow steps

### Step 1: Self-consistent one-loop LW slave-rotor solution
- Role: process
- Action: Implement the self-consistent solution of the one-loop Luttinger-Ward equations together with slave-rotor constraints for the Hubbard model on a triangular lattice with parameters t=0.0913935 eV, U=0.775 eV. Use an appropriate Matsubara grid and convergence criterion to obtain spinon and chargon Green's functions, self-energies, effective interactions T_{f,self}, T_{X,self}, T_bind, and Lagrange multipliers μ, λ, h.
- Evidence: `/app/outputs/host_convergence_log.txt`

### Step 2: Electron bound-state Green's function via BSE
- Role: process
- Action: Using the spinon and chargon Green's functions and the binding interaction T_bind from the previous step, solve the real-space Bethe-Salpeter equation to construct the physical electron Green's function G_c in Matsubara frequency.
- Evidence: `/app/outputs/electron_green_function.h5`

### Step 3: Analytic continuation to real frequencies
- Role: process
- Action: Perform analytic continuation (e.g., using Nevanlinna or equivalent method) of spinon, chargon, and electron Green's functions to real frequencies, obtaining spectral functions and density of states.
- Evidence: `/app/outputs/spectral_data.h5`

### Step 4: Impurity coupled equations solution
- Role: process
- Action: Using the local host spinon and chargon Green's functions (r=0) and T_bind, solve the self-consistent first-order Born approximation equations (with V=0.2 eV, U_imp=3 eV) to obtain impurity spinon and chargon Green's functions and effective parameters. Compute the impurity electron Green's function G_d including the T_bind correction.
- Evidence: `/app/outputs/impurity_solution.h5`

### Step 5: Specific heat calculation
- Role: scored (load-bearing)
- Action: From the temperature-dependent electron Green's function G_c (Matsubara), compute the electron internal energy and numerically differentiate to obtain C_V/T as a function of T^2. Sample at least 10 temperatures in the low-temperature regime (e.g., 1 K to 20 K).
- Output file: `/app/outputs/step_01_specific_heat.csv`
- Format: csv
- Contract: T (numeric, K), CV_T (numeric, arbitrary units)
- Scoring: scored by hidden verifier

### Step 6: Impurity electron spectral function
- Role: scored
- Action: Using the impurity electron Green's function G_d (real frequency) from the impurity solution, compute the spectral function A_d(ω) = -(1/π) Im G_d(ω). Output at least 200 points covering -2.0 eV to 2.0 eV.
- Output file: `/app/outputs/step_02_impurity_spectral.csv`
- Format: csv
- Contract: omega (numeric, eV), A_d (numeric, states/eV)
- Scoring: scored by hidden verifier

### Step 7: Spinon thermal conductivity
- Role: scored
- Action: Compute the spinon energy current-current correlation function Π_f(q→0,ω) from the spinon Green's function and T_{f,self}. Extract the DC conductivity using the lowest Matsubara frequency and derive the spinon thermal conductivity κ_f for a range of temperatures (e.g., 5 K to 50 K). Output at least 8 points.
- Output file: `/app/outputs/step_03_thermal_conductivity.csv`
- Format: csv
- Contract: T (numeric, K), kappa_f (numeric, arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_specific_heat.csv`
- `/app/outputs/step_02_impurity_spectral.csv`
- `/app/outputs/step_03_thermal_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_specific_heat.csv
- path: `/app/outputs/step_01_specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic specific heat divided by temperature (C_V/T) as a function of T^2, expected to show a low-temperature upturn consistent with experimental data.
- schema:
  - `type`: table
  - `required_columns`: `T`, `CV_T`
  - `units`:
    - `T`: K
    - `CV_T`: arbitrary units

### step_02_impurity_spectral.csv
- path: `/app/outputs/step_02_impurity_spectral.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Impurity electron spectral function A_d(ω) displaying resonant peaks near the Mott gap edges.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `A_d`
  - `units`:
    - `omega`: eV
    - `A_d`: states/eV

### step_03_thermal_conductivity.csv
- path: `/app/outputs/step_03_thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spinon thermal conductivity κ_f as a function of temperature, approximately following a T^{-2} scaling.
- schema:
  - `type`: table
  - `required_columns`: `T`, `kappa_f`
  - `units`:
    - `T`: K
    - `kappa_f`: arbitrary units

Notes: All scored artifacts are produced by computing relevant quantities from the self-consistently determined Green's functions and effective interactions. The checker will compare the specific heat curve to a hidden experimental reference (RMSE-based), verify the structural properties of the impurity spectral peaks (position and height), and confirm the approximate -2 slope of the log–log thermal conductivity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "CV_T"
        ],
        "units": {
          "T": "K",
          "CV_T": "arbitrary units"
        }
      },
      "description": "Electronic specific heat divided by temperature (C_V/T) as a function of T^2, expected to show a low-temperature upturn consistent with experimental data."
    },
    {
      "file": "step_02_impurity_spectral.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "A_d"
        ],
        "units": {
          "omega": "eV",
          "A_d": "states/eV"
        }
      },
      "description": "Impurity electron spectral function A_d(ω) displaying resonant peaks near the Mott gap edges."
    },
    {
      "file": "step_03_thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "kappa_f"
        ],
        "units": {
          "T": "K",
          "kappa_f": "arbitrary units"
        }
      },
      "description": "Spinon thermal conductivity κ_f as a function of temperature, approximately following a T^{-2} scaling."
    }
  ],
  "notes": "All scored artifacts are produced by computing relevant quantities from the self-consistently determined Green's functions and effective interactions. The checker will compare the specific heat curve to a hidden experimental reference (RMSE-based), verify the structural properties of the impurity spectral peaks (position and height), and confirm the approximate -2 slope of the log–log thermal conductivity."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that checks each output artifact against reference data and expected structural properties. The verification does not rely on matching a single published number; instead it examines whether your computed curves capture the relevant physical trends:

- For specific heat: the verifier compares the C_V/T vs T² curve to digitized experimental reference data, assessing the overall shape and the presence of a characteristic low‑temperature feature.
- For the impurity spectral function: the verifier inspects the energies, peak heights, and widths of the main spectral features relative to the Mott gap to ensure they are consistent with the expected resonant behaviour.
- For thermal conductivity: the verifier examines the temperature dependence (log‑log slope) of κ_f to verify the approximate power‑law scaling.

The scores from the three tasks are combined into a single final reward. Simply reporting numbers from a paper is not sufficient; the verifier scores the actual data contained in the submitted CSV files.
