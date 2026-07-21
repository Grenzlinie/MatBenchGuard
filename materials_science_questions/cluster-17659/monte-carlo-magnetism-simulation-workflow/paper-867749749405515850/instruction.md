# Binary Bose Mixture PIMC Chemical Potential and Contact

## Problem background
Binary mixtures of ultracold bosons can undergo a miscible-immiscible phase transition driven by the interspecies interaction strength. At zero temperature, mean-field theory predicts a paramagnetic state for interspecies coupling below a critical value and a ferromagnetic state above it. Finite-temperature perturbative theories (Hartree-Fock and Popov) suggest that thermal fluctuations may induce a ferromagnetic transition even when the coupling is below the zero-temperature threshold. The validity of these predictions near the critical region has not been established by exact numerical simulations. This task aims to compute, with path-integral Monte Carlo, the chemical potentials and free energy of a repulsive two-component Bose mixture as functions of polarization and temperature, and to determine whether the mixture remains paramagnetic or exhibits phase separation.

## Approach
We use a canonical path-integral Monte Carlo (PIMC) method based on the worm algorithm in continuous space. The simulation is extended to include configurations with one additional particle, enabling the chemical potential to be extracted from the relative occupation times of the N and N+1 sectors. The free energy is obtained from the pressure (estimated via the virial) and the chemical potentials. The implementation is validated first on an ideal Bose gas, where the PIMC chemical potential is compared with exact finite-N recursion formulas, and then on a single-component hard-sphere Bose gas, where the result is compared with Hartree-Fock predictions. The validated code is then applied to a two-component mixture with hard-sphere interactions. For the polarization scan, the simulation runs at a fixed temperature and density, varying the relative particle numbers. For the balanced mixture, the interspecies contact parameter C12 is determined from the short-range behavior of the pair correlation function between the two species. All simulations are performed in Python using standard numerical libraries.

## Reproduction target
Implement the PIMC worm algorithm for a binary Bose mixture and produce four output files:
- `validation_ideal_gas.csv`: Chemical potential of an ideal Bose gas at T = 1.5 T_c^0 for several particle numbers, compared with the exact finite-N recursion result.
- `validation_interacting_gas.csv`: Chemical potential of a single-component hard-sphere Bose gas with gas parameter na^3 = 10^-6 at temperatures T/T_c^0 = 0.5, 0.8, 1.0, alongside the Hartree-Fock prediction.
- `chemical_potentials.csv`: For a mixture with total N = 128 particles, gas parameter na^3 = 10^-4, temperature T = 0.794 T_c^0, and interspecies coupling g12/g = 0.93, compute the component chemical potentials µ1, µ2 and the free energy per particle F/N at six polarizations: p = 0, 0.1, 0.2, 0.3, 0.4, 0.5.
- `balanced_mixture.csv`: For a balanced (p = 0) mixture with na^3 = 10^-6 and g12/g = 0.93, simulate for particle numbers N = 128, 256, 384, 512 and extrapolate to the thermodynamic limit. Report the extrapolated chemical potential and interspecies contact parameter C12 at temperatures T/T_c^0 = 0.5, 0.8, 1.0.

## Assets

- Python 3: https://www.python.org/
- NumPy: https://numpy.org/
- SciPy: https://scipy.org/
- Matplotlib: https://matplotlib.org/

## Workflow steps

### Step 1: Validate PIMC algorithm on ideal Bose gas
- Role: scored
- Action: Implement the canonical PIMC worm algorithm with sector-changing moves (Extend/Shorten Worm, Add/Remove Worm, Add/Remove Ring Polymer) for a single component. Run simulations for an ideal Bose gas at T=1.5 T_c^0 for several particle numbers N (e.g., 32, 64, 128, 256). Record the chemical potential µ(N,T) estimated via the sector occupation time ratio. Compare with the exact finite-N result computed from the recursion formula.
- Output file: `/app/outputs/validation_ideal_gas.csv`
- Format: csv
- Contract: N (int), mu_PIMC (float, units of k_B T), mu_exact (float, same units)
- Scoring: scored by hidden verifier

### Step 2: Validate PIMC on single-component interacting Bose gas
- Role: scored
- Action: Extend the validated algorithm to include hard-sphere interactions via the pair-product approximation. Simulate a single-component gas with gas parameter na^3=10^-6 for temperatures T/T_c^0 = 0.5, 0.8, 1.0. Extract the chemical potential and report it alongside the Hartree-Fock prediction for comparison.
- Output file: `/app/outputs/validation_interacting_gas.csv`
- Format: csv
- Contract: T_over_Tc0 (float), mu_PIMC (float, units of k_B T_c^0), mu_expected_HF (float, same units)
- Scoring: scored by hidden verifier

### Step 3: Binary mixture: chemical potentials and free energy vs polarization
- Role: scored (load-bearing)
- Action: Generalize the algorithm to two components with intraspecies coupling g and interspecies coupling g12/g=0.93. Simulate a mixture of N=128 total particles at temperature T=0.794 T_c^0 and gas parameter na^3=10^-4, using hard-sphere potentials. For polarizations p=0,0.1,0.2,0.3,0.4,0.5, extract the component chemical potentials µ1, µ2 via sector occupation times and compute the free energy per particle F/N from the thermodynamic relation F = -PV + µ1 N1 + µ2 N2 (pressure from a virial estimator or equivalent).
- Output file: `/app/outputs/chemical_potentials.csv`
- Format: csv
- Contract: polarization (float), mu1 (float, units of k_B T_c^0), mu2 (float, same units), free_energy_per_particle (float, same units)
- Scoring: scored by hidden verifier

### Step 4: Balanced mixture: chemical potential and contact vs temperature
- Role: scored
- Action: Using the validated binary-mixture code, simulate a balanced (p=0) mixture at density na^3=10^-6 and coupling g12/g=0.93. Perform simulations for several particle numbers N (e.g., 128, 256, 384, 512) at each temperature T/T_c^0 = 0.5, 0.8, 1.0. Estimate the chemical potential µ and the interspecies contact parameter C12 for each N, then extrapolate to the thermodynamic limit (e.g., linear fit in 1/N). Report the extrapolated values.
- Output file: `/app/outputs/balanced_mixture.csv`
- Format: csv
- Contract: T_over_Tc0 (float), chemical_potential (float, units of k_B T_c^0), interspecies_contact_C12 (float, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/validation_ideal_gas.csv`
- `/app/outputs/validation_interacting_gas.csv`
- `/app/outputs/chemical_potentials.csv`
- `/app/outputs/balanced_mixture.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### validation_ideal_gas.csv
- path: `/app/outputs/validation_ideal_gas.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ideal-gas validation: the checker recomputes mu_exact and verifies mu_PIMC matches within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `N`, `mu_PIMC`, `mu_exact`
  - `units`:
    - `N`: integer
    - `mu_PIMC`: k_B T
    - `mu_exact`: k_B T

### validation_interacting_gas.csv
- path: `/app/outputs/validation_interacting_gas.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Interacting-gas validation: the checker compares mu_PIMC to the Hartree-Fock expectation.
- schema:
  - `type`: table
  - `required_columns`: `T_over_Tc0`, `mu_PIMC`, `mu_expected_HF`
  - `units`:
    - `T_over_Tc0`: dimensionless
    - `mu_PIMC`: k_B T_c^0
    - `mu_expected_HF`: k_B T_c^0

### chemical_potentials.csv
- path: `/app/outputs/chemical_potentials.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Mixture polarization scan. The checker verifies mu1 > mu2 for all p>0, fits free_energy_per_particle vs p^2 to extract the magnetic susceptibility chi, and compares chi to the zero-temperature mean-field value 2/(g-g12) within 20% tolerance.
- schema:
  - `type`: table
  - `required_columns`: `polarization`, `mu1`, `mu2`, `free_energy_per_particle`
  - `units`:
    - `polarization`: dimensionless
    - `mu1`: k_B T_c^0
    - `mu2`: k_B T_c^0
    - `free_energy_per_particle`: k_B T_c^0

### balanced_mixture.csv
- path: `/app/outputs/balanced_mixture.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Balanced mixture: the checker compares the chemical potential and interspecies contact to hidden reference values derived from the paper's Figures 5 and 6.
- schema:
  - `type`: table
  - `required_columns`: `T_over_Tc0`, `chemical_potential`, `interspecies_contact_C12`
  - `units`:
    - `T_over_Tc0`: dimensionless
    - `chemical_potential`: k_B T_c^0
    - `interspecies_contact_C12`: dimensionless

Notes: All outputs are produced by PIMC simulations. The checker will recompute metrics or compare to hidden references; the public instruction does not contain gold values or tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "validation_ideal_gas.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "mu_PIMC",
          "mu_exact"
        ],
        "units": {
          "N": "integer",
          "mu_PIMC": "k_B T",
          "mu_exact": "k_B T"
        }
      },
      "description": "Ideal-gas validation: the checker recomputes mu_exact and verifies mu_PIMC matches within tolerance."
    },
    {
      "file": "validation_interacting_gas.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_over_Tc0",
          "mu_PIMC",
          "mu_expected_HF"
        ],
        "units": {
          "T_over_Tc0": "dimensionless",
          "mu_PIMC": "k_B T_c^0",
          "mu_expected_HF": "k_B T_c^0"
        }
      },
      "description": "Interacting-gas validation: the checker compares mu_PIMC to the Hartree-Fock expectation."
    },
    {
      "file": "chemical_potentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "polarization",
          "mu1",
          "mu2",
          "free_energy_per_particle"
        ],
        "units": {
          "polarization": "dimensionless",
          "mu1": "k_B T_c^0",
          "mu2": "k_B T_c^0",
          "free_energy_per_particle": "k_B T_c^0"
        }
      },
      "description": "Mixture polarization scan. The checker verifies mu1 > mu2 for all p>0, fits free_energy_per_particle vs p^2 to extract the magnetic susceptibility chi, and compares chi to the zero-temperature mean-field value 2/(g-g12) within 20% tolerance."
    },
    {
      "file": "balanced_mixture.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_over_Tc0",
          "chemical_potential",
          "interspecies_contact_C12"
        ],
        "units": {
          "T_over_Tc0": "dimensionless",
          "chemical_potential": "k_B T_c^0",
          "interspecies_contact_C12": "dimensionless"
        }
      },
      "description": "Balanced mixture: the checker compares the chemical potential and interspecies contact to hidden reference values derived from the paper's Figures 5 and 6."
    }
  ],
  "notes": "All outputs are produced by PIMC simulations. The checker will recompute metrics or compare to hidden references; the public instruction does not contain gold values or tolerances."
}
```

## How you are scored
A hidden verifier independently scores each output artifact. For the ideal-gas validation, it recomputes the exact chemical potential from the recursion formulas and checks that your PIMC values agree within a small tolerance. For the interacting-gas validation, it checks that your PIMC chemical potential is consistent with the Hartree-Fock prediction. For the mixture polarization scan, it performs two checks: (a) it verifies that the majority chemical potential is strictly larger than the minority for all nonzero polarizations (structural condition), and (b) it fits the free energy per particle as a function of the squared polarization, extracts the magnetic susceptibility, and compares it to the zero-temperature mean-field prediction. For the balanced mixture, it compares your reported chemical potential and interspecies contact parameter at each temperature to reference values. The final reward is a weighted sum of the scores from all four steps, with the polarization scan carrying the highest weight. Simply copying literature values is not sufficient; the verifier expects results consistent with a genuine PIMC simulation that satisfies the structural and quantitative comparisons.
