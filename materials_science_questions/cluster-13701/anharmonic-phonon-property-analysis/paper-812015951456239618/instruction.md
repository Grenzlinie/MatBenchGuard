# Computational Analysis of d-Wave Pairing and Pseudogap from a Vibrational Bond-Coupling Model

## Problem background
High-temperature superconductivity (HTS) in cuprates involves a d-wave pairing mechanism, a pseudogap, and an anomalous doping-dependent oxygen isotope shift. The fluctuating Cu-O-Cu bond model (FBM) postulates that nonlinear (quadratic) coupling between planar oxygen vibrations and the Cu-Cu hopping integral drives pairing and can also produce a static d-wave charge-density wave (dCDW). This task reproduces the model’s computational predictions: the doping-dependent superconducting transition temperature T_c, the corresponding oxygen isotope shift exponent α, the magnitude of the dCDW gap χ_Q, and the vibrational amplitude modulation ratio √⟨u²⟩/√⟨x²⟩. Solving these quantities from the model Hamiltonian provides a quantitative test of whether the proposed microscopic mechanism captures the salient experimental features.

## Approach
Implement the FBM Hamiltonian with the given parameters (nearest-neighbor hopping t = 0.25 eV, further hoppings t′ = –0.06 eV, t″ = 0.0325 eV, pairing coupling K = 0.48 eV, anharmonic vibrator frequencies ω_a = 0.05 eV and ω_h = 0.015 eV, energy cutoff = 1.6 eV). Solve the linearized gap equation using a fast Fourier transform method to obtain the superconducting transition temperature T_c as a function of doping for oxygen-16 (mass 16) and oxygen-18 (mass 18). From these T_c values derive the isotope exponent α(p) = –d ln T_c / d ln M by finite difference. Separately, with a reduced coupling K = 0.23 eV, minimize the free energy of a one-dimensional d-wave CDW to determine the gap amplitude χ_Q. Finally, using the formula that relates the r.m.s. quadrupolar amplitude to χ_Q and the model parameters (mode degeneracy n = 3, spin degeneracy n_s = 2, K, ω_a), compute the vibrational amplitude ratio √⟨u²⟩/√⟨x²⟩.

## Reproduction target
Produce the following scored artifacts in the /app/outputs directory:

- **Tc_alpha_vs_doping.csv**: a CSV with columns doping_p (unitless), Tc_K (Kelvin, for oxygen-16), and isotope_shift_alpha (unitless). The rows should sample a range of dopings that covers underdoped, optimal, and overdoped regimes.
- **dCDW_gap_meV.txt**: a text file containing a single floating-point number, the dCDW gap χ_Q in meV.
- **amplitude_ratio.txt**: a text file containing a single floating-point number, the vibrational amplitude ratio √⟨u²⟩/√⟨x²⟩.

The Tc/α curve and the two dCDW scalars together constitute the full reproduction target.

## Assets

- Python scientific stack (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Solve FBM gap equation for Tc(p) with O-16 and O-18
- Role: process
- Action: Implement the FBM pairing propagator and linearized gap equation. For a set of doping points covering underdoped to overdoped, solve for Tc using a fast Fourier transform method (or equivalent iterative solver) for oxygen-16 and oxygen-18 masses. Store the resulting Tc arrays for the next step.
- Evidence: none

### Step 2: Compute isotope shift and output Tc(p) and alpha(p)
- Role: scored (load-bearing)
- Action: Using the Tc arrays from step1, compute the isotope shift exponent alpha(p) = -d ln Tc / d ln M (via finite difference). Write a CSV file with columns: doping_p, Tc_K, isotope_shift_alpha. The Tc values are for O-16.
- Output file: `/app/outputs/Tc_alpha_vs_doping.csv`
- Format: csv
- Contract: columns: doping_p (float), Tc_K (float), isotope_shift_alpha (float); rows for a representative set of dopings (e.g., 10-15 points).
- Scoring: scored by hidden verifier

### Step 3: Calculate dCDW gap and output chi_Q
- Role: scored
- Action: Using the FBM parameters with K=0.23 eV, minimize the free energy of the one-dimensional d-wave CDW state to obtain the amplitude chi_Q. Write chi_Q in meV to a text file.
- Output file: `/app/outputs/dCDW_gap_meV.txt`
- Format: txt
- Contract: Single float (line) representing chi_Q in meV.
- Scoring: scored by hidden verifier

### Step 4: Output vibrational amplitude ratio
- Role: scored
- Action: From the computed chi_Q (in eV) and the model parameters (n=3, n_s=2, K=0.23 eV, omega_a=0.05 eV), calculate the vibrational amplitude ratio sqrt(<u^2>)/sqrt(<x^2>) using the explicit formula: ratio = sqrt(2 * n_s * chi_Q^2 / (n * K * omega_a)). Write the ratio to a text file.
- Output file: `/app/outputs/amplitude_ratio.txt`
- Format: txt
- Contract: Single float (line) representing the ratio sqrt(<u^2>)/sqrt(<x^2>).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Tc_alpha_vs_doping.csv`
- `/app/outputs/dCDW_gap_meV.txt`
- `/app/outputs/amplitude_ratio.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Tc_alpha_vs_doping.csv
- path: `/app/outputs/Tc_alpha_vs_doping.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Doping-dependent superconducting transition temperature and oxygen isotope shift exponent.
- schema:
  - `type`: table
  - `required_columns`: `doping_p`, `Tc_K`, `isotope_shift_alpha`
  - `units`:
    - `doping_p`: unitless
    - `Tc_K`: Kelvin
    - `isotope_shift_alpha`: unitless

### dCDW_gap_meV.txt
- path: `/app/outputs/dCDW_gap_meV.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Magnitude of the d-wave CDW gap from free-energy minimization.
- schema:
  - `type`: text
  - `value`: float
  - `unit`: meV

### amplitude_ratio.txt
- path: `/app/outputs/amplitude_ratio.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Ratio of the r.m.s. dCDW quadrupolar amplitude to the zero-point vibrational amplitude.
- schema:
  - `type`: text
  - `value`: float
  - `unit`: unitless

Notes: This task reproduces key predictions of a microscopic model for high-Tc superconductivity. The Tc and isotope shift curves should exhibit a hump and a dip near optimal doping, respectively. The dCDW gap and amplitude ratio are scalar values consistent with the model parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Tc_alpha_vs_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping_p",
          "Tc_K",
          "isotope_shift_alpha"
        ],
        "units": {
          "doping_p": "unitless",
          "Tc_K": "Kelvin",
          "isotope_shift_alpha": "unitless"
        }
      },
      "description": "Doping-dependent superconducting transition temperature and oxygen isotope shift exponent."
    },
    {
      "file": "dCDW_gap_meV.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "value": "float",
        "unit": "meV"
      },
      "description": "Magnitude of the d-wave CDW gap from free-energy minimization."
    },
    {
      "file": "amplitude_ratio.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "value": "float",
        "unit": "unitless"
      },
      "description": "Ratio of the r.m.s. dCDW quadrupolar amplitude to the zero-point vibrational amplitude."
    }
  ],
  "notes": "This task reproduces key predictions of a microscopic model for high-Tc superconductivity. The Tc and isotope shift curves should exhibit a hump and a dip near optimal doping, respectively. The dCDW gap and amplitude ratio are scalar values consistent with the model parameters."
}
```

## How you are scored
A hidden verifier inspects each output artifact independently and combines the scores by weight to produce a total reward in [0,1].

- The Tc/α curve (file Tc_alpha_vs_doping.csv) is weighted 0.6. The verifier compares the doping dependence of T_c and α to reference expectations (the presence of a T_c hump and an α dip near optimal doping, reasonable magnitudes, and a physically sound doping range).
- The dCDW gap (dCDW_gap_meV.txt) and the amplitude ratio (amplitude_ratio.txt) each carry 0.2 (total 0.4). The verifier checks that the submitted scalar values fall within physically plausible ranges for the given model parameters.

Scoring is not based on exactly matching any single number; it rewards a faithful numerical solution of the FBM equations that captures the essential doping trends and yields dCDW parameters consistent with the model.
