# Spinodal Scaling and Dynamics in the 2D 8-state Potts Model

## Problem background
First-order phase transitions can exhibit metastable states where a system lingers in a phase that is not the globally stable one before eventually nucleating the stable phase. For finite-size systems, the boundaries of these metastable regions—called spinodal points—depend on system size. Understanding how the spinodal temperature approaches the transition temperature as the system grows is key to revealing the structure of the free-energy barrier. This work investigates the 2D q-state Potts model (q=8) on a square lattice, which undergoes a first-order transition between a paramagnetic and a ferromagnetic phase. By probing the density of states and performing finite-size scaling of the free-energy landscape, one can extract critical scaling exponents that characterize the barrier's shape. Additionally, comparing the equilibrium spinodal points with the size-dependent crossover observed in nucleation dynamics tests whether equilibrium metastability governs the finite-size effects in the relaxation process.

## Approach
The reproduction follows a two-pronged computational approach: equilibrium analysis and dynamic relaxation.

**Equilibrium part**: Use the Wang-Landau algorithm to compute the density of states g(E) for the 2D q=8 Potts model on L×L lattices (periodic boundary conditions) for sizes L = 32, 64, 128, 256, 512. From g(E), derive the microcanonical inverse temperature β(E) = ∂ln g(E)/∂E and the free energy F(β_c; E) = E − β_c^{-1} ln g(E) at the known transition inverse temperature β_c = ln(1+√8). Locate the spinodal points—the extremal points of β(E)—for both the ferromagnetic and paramagnetic branches. Fit the power-law relation |β_spi − β_c| ∝ L^{-1/ν} to obtain the exponent ν. Then perform a finite-size data collapse of β(E) and F(β_c; E) by scaling the energy axis and the free energy axis to extract the exponents d_E and d_F that describe the finite-size scaling of the internal energy and free-energy barrier at the bistable point.

**Dynamics part**: Initialize the system in a fully ordered ferromagnetic state, equilibrate at β_c, then quench to a set of lower inverse temperatures β (e.g., 1.30–1.34). Simulate the time evolution using the Metropolis algorithm for L=256 (optionally larger) and record the order parameter m(t). Average over many independent runs (e.g., 64 samples). From the averaged m(t) curves, determine the characteristic relaxation time τ_0.4 defined as the time when the order parameter crosses 0.4. Finally, identify the temperature β_deviation at which τ_0.4 starts to deviate from the large-system behavior and compare it with the equilibrium spinodal temperature β_spi_f(L=256) obtained in the equilibrium analysis; the absolute difference between them quantifies the agreement.

## Reproduction target
Compute and report the following quantities:

- The finite-size scaling exponent ν from the L-dependence of the spinodal temperatures. Report the fitted value and its error.
- The finite-size scaling exponents d_E and d_F characterizing the free-energy landscape at β_c. Provide the best estimates and their errors.
- A table of characteristic relaxation times τ_0.4 as a function of β for L=256 (and optionally larger L).
- The value of β_deviation where the dynamics first shows a finite-size effect for L=256 and the absolute difference from the corresponding equilibrium ferromagnetic spinodal temperature β_spi_f.

## Assets

- NumPy: numpy
- SciPy: scipy
- Wang-Landau algorithm
- Metropolis algorithm

## Workflow steps

### Step 1: Wang-Landau sampling
- Role: process
- Action: Implement parallel Wang-Landau sampling for the 2D q=8 Potts model on square lattices with periodic boundaries for system sizes L=32,64,128,256,512. Compute the density of states g(E) for each L. Save the g(E) arrays to disk for later analysis.
- Evidence: `/app/outputs/wl_run.log`

### Step 2: Spinodal scaling analysis
- Role: scored (load-bearing)
- Action: From the density of states g(E) for each L, compute microcanonical inverse temperature β(E)=∂ln g(E)/∂E. Identify the spinodal points (extremal points of β(E)) for the ferromagnetic and paramagnetic branches. Fit |β_spi−β_c| versus L to obtain exponent ν, where β_c=ln(1+√8). Write the spinodal data and fitted ν to step01_spinodal_scaling.json.
- Output file: `/app/outputs/step01_spinodal_scaling.json`
- Format: json
- Contract: {"L": "list of integers", "beta_spi_f": "list of floats", "beta_spi_p": "list of floats", "beta_c": 1.3424, "fitted_nu": "float", "fitted_nu_err": "float"}
- Scoring: scored by hidden verifier

### Step 3: Free-energy landscape finite-size scaling
- Role: scored (load-bearing)
- Action: For each L, compute the free energy F(β_c;E)=E−β_c^{-1} ln g(E). Perform data collapse of β(E) and F(β_c;E) by trying values of d_E and d_F until the curves for L≥256 collapse onto single master curves when plotted against scaled variables. Report the estimated best-fit exponents and their errors in step02_landscape_exponents.json.
- Output file: `/app/outputs/step02_landscape_exponents.json`
- Format: json
- Contract: {"d_E": "float", "d_E_err": "float", "d_F": "float", "d_F_err": "float"}
- Scoring: scored by hidden verifier

### Step 4: Metropolis dynamics simulation
- Role: process
- Action: Initialize the 2D 8-state Potts model in a fully ordered ferromagnetic state and equilibrate at β_c for 1000 MC steps. Then quench the system to a range of lower inverse temperatures β (e.g., 1.30–1.34) and simulate Metropolis dynamics for L=256 (and optionally L=512). Record the time series of the order parameter m(t) after quench. Average over many independent runs (e.g., 64 samples for L=256).
- Evidence: `/app/outputs/dynamics_log.txt`

### Step 5: Extract relaxation times
- Role: scored
- Action: From the time series of m(t) for each β and L, determine the time τ_0.4 at which the average order parameter crosses 0.4 (after the initial plateau). Write a CSV file with columns L, beta, tau_0.4 for at least L=256.
- Output file: `/app/outputs/step03_dynamics_tau.csv`
- Format: csv
- Contract: CSV with columns: L (int), beta (float), tau_0.4 (float). At least one row for L=256 and several β values.
- Scoring: scored by hidden verifier

### Step 6: Dynamics-spinodal agreement
- Role: scored (load-bearing)
- Action: Using the tau_0.4 data from step03 and the equilibrium spinodal β_spi_f for L=256 from step01, identify the temperature at which the relaxation time τ_0.4 starts to deviate from the large-system behavior (e.g., where it becomes faster than the extrapolated large-L trend). Report this crossover temperature as beta_deviation and compute the absolute difference from the equilibrium spinodal temperature. Write step04_dynamics_agreement.json.
- Output file: `/app/outputs/step04_dynamics_agreement.json`
- Format: json
- Contract: {"L_dynamics": 256, "beta_deviation": "float", "beta_spi_f": "float", "difference": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step01_spinodal_scaling.json`
- `/app/outputs/step02_landscape_exponents.json`
- `/app/outputs/step03_dynamics_tau.csv`
- `/app/outputs/step04_dynamics_agreement.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step01_spinodal_scaling.json
- path: `/app/outputs/step01_spinodal_scaling.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Spinodal scaling data and fitted exponent ν; compared to the paper's ν=1.4(1) with a hidden tolerance.
- schema:
  - `type`: object
  - `required`: `L`, `beta_spi_f`, `beta_spi_p`, `beta_c`, `fitted_nu`, `fitted_nu_err`
  - `properties`:
    - `L`:
      - `type`: array
      - `items`:
        - `type`: integer
    - `beta_spi_f`:
      - `type`: array
      - `items`:
        - `type`: number
    - `beta_spi_p`:
      - `type`: array
      - `items`:
        - `type`: number
    - `beta_c`:
      - `type`: number
    - `fitted_nu`:
      - `type`: number
    - `fitted_nu_err`:
      - `type`: number

### step02_landscape_exponents.json
- path: `/app/outputs/step02_landscape_exponents.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Finite-size scaling exponents d_E and d_F; compared to the paper's d_E=1.2(1) and d_F=0.5(1) with hidden tolerances.
- schema:
  - `type`: object
  - `required`: `d_E`, `d_E_err`, `d_F`, `d_F_err`
  - `properties`:
    - `d_E`:
      - `type`: number
    - `d_E_err`:
      - `type`: number
    - `d_F`:
      - `type`: number
    - `d_F_err`:
      - `type`: number

### step03_dynamics_tau.csv
- path: `/app/outputs/step03_dynamics_tau.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Characteristic relaxation time τ_0.4; structural audit verifies column types, presence of L=256 rows, and monotonic decrease of τ_0.4 with decreasing beta.
- schema:
  - `type`: table
  - `required_columns`: `L`, `beta`, `tau_0.4`
  - `columns`:
    - `L`:
      - `type`: integer
    - `beta`:
      - `type`: number
    - `tau_0.4`:
      - `type`: number

### step04_dynamics_agreement.json
- path: `/app/outputs/step04_dynamics_agreement.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Agreement check between dynamical crossover and equilibrium spinodal; threshold requires |beta_deviation - beta_spi_f| < 0.02.
- schema:
  - `type`: object
  - `required`: `L_dynamics`, `beta_deviation`, `beta_spi_f`, `difference`
  - `properties`:
    - `L_dynamics`:
      - `type`: integer
    - `beta_deviation`:
      - `type`: number
    - `beta_spi_f`:
      - `type`: number
    - `difference`:
      - `type`: number

Notes: All scored artifacts are derived from the same Wang-Landau and Metropolis simulations. Hidden gold values and tolerances are based on the paper's reported results. The structural audit on step03 checks column format and monotonicity of τ_0.4 versus beta.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step01_spinodal_scaling.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "L",
          "beta_spi_f",
          "beta_spi_p",
          "beta_c",
          "fitted_nu",
          "fitted_nu_err"
        ],
        "properties": {
          "L": {
            "type": "array",
            "items": {
              "type": "integer"
            }
          },
          "beta_spi_f": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "beta_spi_p": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "beta_c": {
            "type": "number"
          },
          "fitted_nu": {
            "type": "number"
          },
          "fitted_nu_err": {
            "type": "number"
          }
        }
      },
      "description": "Spinodal scaling data and fitted exponent ν; compared to the paper's ν=1.4(1) with a hidden tolerance."
    },
    {
      "file": "step02_landscape_exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "d_E",
          "d_E_err",
          "d_F",
          "d_F_err"
        ],
        "properties": {
          "d_E": {
            "type": "number"
          },
          "d_E_err": {
            "type": "number"
          },
          "d_F": {
            "type": "number"
          },
          "d_F_err": {
            "type": "number"
          }
        }
      },
      "description": "Finite-size scaling exponents d_E and d_F; compared to the paper's d_E=1.2(1) and d_F=0.5(1) with hidden tolerances."
    },
    {
      "file": "step03_dynamics_tau.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "beta",
          "tau_0.4"
        ],
        "columns": {
          "L": {
            "type": "integer"
          },
          "beta": {
            "type": "number"
          },
          "tau_0.4": {
            "type": "number"
          }
        }
      },
      "description": "Characteristic relaxation time τ_0.4; structural audit verifies column types, presence of L=256 rows, and monotonic decrease of τ_0.4 with decreasing beta."
    },
    {
      "file": "step04_dynamics_agreement.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "L_dynamics",
          "beta_deviation",
          "beta_spi_f",
          "difference"
        ],
        "properties": {
          "L_dynamics": {
            "type": "integer"
          },
          "beta_deviation": {
            "type": "number"
          },
          "beta_spi_f": {
            "type": "number"
          },
          "difference": {
            "type": "number"
          }
        }
      },
      "description": "Agreement check between dynamical crossover and equilibrium spinodal; threshold requires |beta_deviation - beta_spi_f| < 0.02."
    }
  ],
  "notes": "All scored artifacts are derived from the same Wang-Landau and Metropolis simulations. Hidden gold values and tolerances are based on the paper's reported results. The structural audit on step03 checks column format and monotonicity of τ_0.4 versus beta."
}
```

## How you are scored
A hidden verifier evaluates your four submitted artifacts independently. For step01_spinodal_scaling.json, the checker compares your reported ν against a reference (the paper's value) with a pre-set tolerance; a reasonable fit to the spinodal data is expected. For step02_landscape_exponents.json, your d_E and d_F are compared to reference values under tolerances. For step03_dynamics_tau.csv, the checker audits the table's structure, verifies the presence of L=256 rows, and checks that τ_0.4 decreases monotonically as β moves away from β_c. For step04_dynamics_agreement.json, the checker compares |β_deviation − β_spi_f| against a threshold; meeting or exceeding the threshold/tolerance requirement earns full credit for that part. The total reward is a weighted sum of these stage scores. Reporting numbers alone is not sufficient; the intermediate steps (Wang-Landau sampling and Metropolis dynamics) must be genuinely executed, as the existence of the scored artifacts depends on them.
