# Critical Temperature, Secondary Exponent and Field Phase Boundaries of Antiferro Quadrupole Models on the Diamond Lattice

## Problem background
In strongly correlated electron systems, orbital degrees of freedom can give rise to quadrupole orders. This work investigates antiferro quadrupole models on a diamond lattice, motivated by Pr-based 1‑2‑20 compounds. Two classical effective models are considered: a plane‑rotor (XY) model with Z₃ single‑site anisotropy, and a two‑component φ⁴ model with amplitude fluctuations and a third‑order anisotropy term. At zero magnetic field, the system orders at finite temperature. A magnetic field couples through a quadratic Zeeman term and produces a rich competition among collinear, canted, and mixed antiferro‑quadrupole phases. The goal is to compute the critical temperature, determine the universality class, measure the critical exponent of a secondary (parasitic ferro) order parameter, and locate the field‑induced phase boundaries.

## Approach
The problem is tackled with classical Monte Carlo simulations on a diamond lattice with antiferro nearest‑neighbour interactions. For the plane‑rotor model at anisotropy c=3.0, a combination of Metropolis single‑spin flips, Wolff cluster updates, and global C₃ rotations is used to equilibrate the system at several temperatures across system sizes L=8,16,32,64,128. From the recorded time series, Binder ratios and correlation‑length ratios of the primary staggered order parameter are computed to locate the zero‑field critical temperature and to test universality by comparing the crossing values with those of known classes. The same simulation data yield a secondary (ferro) order parameter; its scaling exponent is extracted via finite‑size analysis. For the φ⁴ model (a=−5, b=10, c=0.5, J=1) with a quadratic Zeeman field h≥0, simulations are run at temperature T=0.8 and a range of h values for sizes L=16,32,64. Binder ratios for the two staggered order‑parameter components are computed to determine the transition fields among phases I, II, III and to find the tetracritical point where they meet.

## Reproduction target
1. Plane‑rotor model (c=3.0): Compute the zero‑field critical temperature Tc and determine the universality class from the Binder‑ratio crossing value and the correlation‑length‑ratio crossing value. Write the three numbers to zero_field_criticality.json.
2. From the same simulations, extract the critical exponent β′ of the parasitic ferro quadrupole order parameter. Write it to secondary_exponent_beta_prime.json.
3. φ⁴ model (c=0.5) under a field h≥0: At T=0.8, locate the phase boundary field h_II_III (transition between phases II and III), the boundary h_I_II (transition between phases I and II), and the h‑coordinate of the tetracritical point where all three ordered phases meet. Write these three h‑values to phase_boundaries_T0_8.json.

## Assets

- Python interpreter: python
- NumPy: numpy
- SciPy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Plane-rotor MC simulation at c=3.0
- Role: process
- Action: Implement and run classical Monte Carlo simulations for the plane-rotor model with parameters c=3.0, J=1 on a diamond lattice for system sizes L=8, 16, 32, 64, 128. Use a combination of Metropolis single-spin flips, Wolff cluster updates, and global C3 rotations. Record time series of energy, order parameter components, and Fourier-transformed correlation matrices at each temperature step.
- Evidence: `/app/outputs/simulation_log_c3.txt`

### Step 2: Zero-field critical temperature and universality
- Role: scored (load-bearing)
- Action: From the simulation data, compute the Binder ratio and correlation length ratio for the primary staggered order parameter as functions of temperature and system size. Determine the critical temperature Tc from the crossing point of the curves, and extract the Binder ratio crossing value and the correlation length ratio crossing value. Write the results to zero_field_criticality.json.
- Output file: `/app/outputs/zero_field_criticality.json`
- Format: json
- Contract: {"Tc": float, "Binder_crossing_value": float, "xi_over_L_crossing_value": float}
- Scoring: scored by hidden verifier

### Step 3: Secondary order parameter critical exponent β′
- Role: scored
- Action: From the same simulation data, extract the secondary (ferro) order parameter squared as a function of temperature. Perform a finite-size scaling analysis to determine the critical exponent β′ of the parasitic ferro quadrupole order. Report the exponent in secondary_exponent_beta_prime.json.
- Output file: `/app/outputs/secondary_exponent_beta_prime.json`
- Format: json
- Contract: {"beta_prime": float}
- Scoring: scored by hidden verifier

### Step 4: φ⁴ model MC simulation under magnetic field
- Role: process
- Action: Implement and run Monte Carlo simulations for the two-component φ⁴ model (with amplitude fluctuations) with a=-5, b=10, J=1, anisotropy c=0.5, and quadratic Zeeman coupling term for h≥0. Perform simulations at temperatures including T=0.8 and for a range of h values, for system sizes L=16, 32, 64. Record staggered order parameter moments and Binder ratios for the u and v components.
- Evidence: `/app/outputs/simulation_log_phi4_field.txt`

### Step 5: Phase boundaries at T=0.8 and tetracritical point
- Role: scored
- Action: From the field simulation data, compute Binder ratios for the u and v staggered order parameters. Determine the phase boundaries between phases II/III (h_II_III) and I/II (h_I_II) at temperature T=0.8, and locate the tetracritical point. Write the three h-values to phase_boundaries_T0_8.json.
- Output file: `/app/outputs/phase_boundaries_T0_8.json`
- Format: json
- Contract: {"h_II_III": float, "h_I_II": float, "h_tetracritical": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zero_field_criticality.json`
- `/app/outputs/secondary_exponent_beta_prime.json`
- `/app/outputs/phase_boundaries_T0_8.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zero_field_criticality.json
- path: `/app/outputs/zero_field_criticality.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical temperature, Binder crossing value, and correlation length ratio crossing value for the plane-rotor model at c=3.0. Checked against hidden paper gold with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Tc`: float
    - `Binder_crossing_value`: float
    - `xi_over_L_crossing_value`: float

### secondary_exponent_beta_prime.json
- path: `/app/outputs/secondary_exponent_beta_prime.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical exponent β′ of the parasitic ferro quadrupole order parameter. Checked against hidden paper gold with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `beta_prime`: float

### phase_boundaries_T0_8.json
- path: `/app/outputs/phase_boundaries_T0_8.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phase boundary fields at T=0.8 and tetracritical point for the φ⁴ model with c=0.5. Checked against hidden paper gold with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `h_II_III`: float
    - `h_I_II`: float
    - `h_tetracritical`: float

Notes: All scored artifacts are validated by result-level comparison against paper-reported values with appropriate tolerances. The process steps must produce simulation records that the analysis steps consume, enforced by the load-bearing step requiring genuine simulation output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zero_field_criticality.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc": "float",
          "Binder_crossing_value": "float",
          "xi_over_L_crossing_value": "float"
        }
      },
      "description": "Critical temperature, Binder crossing value, and correlation length ratio crossing value for the plane-rotor model at c=3.0. Checked against hidden paper gold with tolerance."
    },
    {
      "file": "secondary_exponent_beta_prime.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "beta_prime": "float"
        }
      },
      "description": "Critical exponent β′ of the parasitic ferro quadrupole order parameter. Checked against hidden paper gold with tolerance."
    },
    {
      "file": "phase_boundaries_T0_8.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "h_II_III": "float",
          "h_I_II": "float",
          "h_tetracritical": "float"
        }
      },
      "description": "Phase boundary fields at T=0.8 and tetracritical point for the φ⁴ model with c=0.5. Checked against hidden paper gold with tolerance."
    }
  ],
  "notes": "All scored artifacts are validated by result-level comparison against paper-reported values with appropriate tolerances. The process steps must produce simulation records that the analysis steps consume, enforced by the load-bearing step requiring genuine simulation output."
}
```

## How you are scored
A hidden verifier reads each of your JSON artifacts and compares the values to hidden reference targets. The five scored quantities (Tc, Binder‑crossing value, ξ/L‑crossing value, β′, h_II_III, h_I_II, and h_tetracritical) are combined with weights to produce a final reward in [0,1]. The verifier does not inspect your code; it only checks the final numbers. Because the Monte Carlo procedure is stochastic and implementation‑dependent, the tolerances are set to accommodate legitimate run‑to‑run spread while rejecting random guesses. To earn full credit you must implement the simulations faithfully and extract the required quantities from your own simulation data; simply reporting the paper’s published numbers without running the computations will not pass.
