# Orientational Order of Colloidal Dimers and Trimers on 2D Substrates

## Problem background
Colloidal particles confined to two-dimensional periodic substrates can organize into novel crystalline states. When the number of colloids exceeds the number of substrate minima, several colloids may be trapped in a single minimum, forming composite objects with internal rotational degrees of freedom—reminiscent of molecules. Understanding the resulting orientational ordering and the melting behavior of such "colloidal molecular crystals" is an open challenge in soft-matter physics. In this reproduction, you will investigate the orientational patterns of dimers (two colloids per minima) and trimers (three colloids per minima) on a square substrate via numerical simulations, and examine how the orientational order evolves as the temperature is raised.

## Approach
You will use Langevin dynamics simulations of Yukawa (screened Coulomb) colloids on a square substrate. The colloid–colloid interaction has screening length a0/2, and the substrate force is a sinusoidal potential of amplitude A=2.5 and period a0. The overdamped equation of motion is integrated numerically. Starting from a high-temperature disordered state, the system is cooled gradually to T=0 to obtain the ground-state configuration. You will perform these cooling runs for two fillings: Nc=2Nm (dimers) and Nc=3Nm (trimers). Additionally, you will run finite-temperature simulations for the dimer system at three temperatures expressed as fractions of the clean-system melting temperature Tm0 (which you must first estimate from a simulation without a substrate). From the final particle positions, you will compute the orientational order metrics: for dimers, the mean relative angle between neighboring dimers and its standard deviation; for trimers, the mean orientation angle between trimers in adjacent columns and its standard deviation. For the finite-temperature dimer runs, you will compute a scalar orientational order parameter (e.g., a nematic order parameter or average cosine of orientation deviation) at each temperature. All results are written to a single JSON file, `/app/outputs/dimer_ordering_results.json`, following the specified schema.

## Reproduction target
The objective is to computationally determine the orientational order of colloidal molecular crystals on a square substrate. Specifically:

- For the ground state (T=0), compute the mean relative angle (in degrees) and its standard deviation for neighboring dimers and for trimers in adjacent columns.
- For the dimer system, at three distinct temperatures (T/Tm0 = 0.25, 1.5, and 4.0, where Tm0 is determined from a separate simulation without a substrate), compute an orientational order parameter that quantifies the degree of orientational order.
- Record all these quantities in the required JSON file `/app/outputs/dimer_ordering_results.json` with the fields: `dimer_mean_relative_angle_degrees`, `dimer_relative_angle_std`, `trimer_mean_relative_angle_degrees_between_columns`, `trimer_relative_angle_std`, `dimer_order_parameter_lowT`, `dimer_order_parameter_intermediateT`, `dimer_order_parameter_highT`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Determine clean melting temperature Tm0
- Role: process
- Action: Run a Langevin dynamics simulation for Yukawa colloids without substrate (A=0) using the specified interaction parameters (screening length a0/2, charge Q=1). Start at high temperature and gradually cool, monitoring the onset of diffusion to estimate the melting temperature Tm0 of the clean system. Record the estimated value for later use.
- Evidence: `/app/outputs/tm0_estimate.txt`

### Step 2: Generate equilibrium configurations and trajectories
- Role: process
- Action: Implement the overdamped Langevin equation with Yukawa interactions and square substrate force (strength A=2.5, period a0). For fillings Nc=2Nm (dimer) and Nc=3Nm (trimer), begin at high temperature, cool gradually to T=0, and save the final particle positions. Additionally, for Nc=2Nm, perform three separate simulations at temperatures T/Tm0 = 0.25, 1.5, and 4.0 (using the Tm0 from step 1) and save the final positions or short trajectories.
- Evidence: none

### Step 3: Compute orientational order and melting metrics
- Role: scored (load-bearing)
- Action: From the T=0 dimer and trimer configurations, compute the orientational order: mean relative angle between neighboring dimer minima and its standard deviation; mean orientation angle between adjacent trimer columns and its standard deviation. For the finite-temperature dimer simulations, compute an orientational order parameter (e.g., a nematic order parameter or average cosine of dimer orientation deviation). Write all results to dimer_ordering_results.json.
- Output file: `/app/outputs/dimer_ordering_results.json`
- Format: json
- Contract: {"type":"object","required":["dimer_mean_relative_angle_degrees","dimer_relative_angle_std","trimer_mean_relative_angle_degrees_between_columns","trimer_relative_angle_std","dimer_order_parameter_lowT","dimer_order_parameter_intermediateT","dimer_order_parameter_highT"],"properties":{"dimer_mean_relative_angle_degrees":{"type":"number"},"dimer_relative_angle_std":{"type":"number"},"trimer_mean_relative_angle_degrees_between_columns":{"type":"number"},"trimer_relative_angle_std":{"type":"number"},"dimer_order_parameter_lowT":{"type":"number"},"dimer_order_parameter_intermediateT":{"type":"number"},"dimer_order_parameter_highT":{"type":"number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dimer_ordering_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dimer_ordering_results.json
- path: `/app/outputs/dimer_ordering_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Orientational order measures: mean angles and standard deviations for dimers/trimers at T=0, and dimer orientational order parameter at three temperatures (low, intermediate, high) to demonstrate two-stage melting.
- schema:
  - `type`: object
  - `required`: `dimer_mean_relative_angle_degrees`, `dimer_relative_angle_std`, `trimer_mean_relative_angle_degrees_between_columns`, `trimer_relative_angle_std`, `dimer_order_parameter_lowT`, `dimer_order_parameter_intermediateT`, `dimer_order_parameter_highT`
  - `properties`:
    - `dimer_mean_relative_angle_degrees`:
      - `type`: number
    - `dimer_relative_angle_std`:
      - `type`: number
    - `trimer_mean_relative_angle_degrees_between_columns`:
      - `type`: number
    - `trimer_relative_angle_std`:
      - `type`: number
    - `dimer_order_parameter_lowT`:
      - `type`: number
    - `dimer_order_parameter_intermediateT`:
      - `type`: number
    - `dimer_order_parameter_highT`:
      - `type`: number

Notes: The checker compares the reported mean angles to hidden reference values with appropriate tolerance, and verifies that dimer order parameters decrease monotonically with temperature and that the low-temperature value exceeds a structural threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dimer_ordering_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "dimer_mean_relative_angle_degrees",
          "dimer_relative_angle_std",
          "trimer_mean_relative_angle_degrees_between_columns",
          "trimer_relative_angle_std",
          "dimer_order_parameter_lowT",
          "dimer_order_parameter_intermediateT",
          "dimer_order_parameter_highT"
        ],
        "properties": {
          "dimer_mean_relative_angle_degrees": {
            "type": "number"
          },
          "dimer_relative_angle_std": {
            "type": "number"
          },
          "trimer_mean_relative_angle_degrees_between_columns": {
            "type": "number"
          },
          "trimer_relative_angle_std": {
            "type": "number"
          },
          "dimer_order_parameter_lowT": {
            "type": "number"
          },
          "dimer_order_parameter_intermediateT": {
            "type": "number"
          },
          "dimer_order_parameter_highT": {
            "type": "number"
          }
        }
      },
      "description": "Orientational order measures: mean angles and standard deviations for dimers/trimers at T=0, and dimer orientational order parameter at three temperatures (low, intermediate, high) to demonstrate two-stage melting."
    }
  ],
  "notes": "The checker compares the reported mean angles to hidden reference values with appropriate tolerance, and verifies that dimer order parameters decrease monotonically with temperature and that the low-temperature value exceeds a structural threshold."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/dimer_ordering_results.json` and compute a reward between 0 and 1. The verifier checks the reported orientational angles against physical expectations derived from the system's symmetry and compares the temperature-dependent order parameter values to ensure they satisfy a monotonic trend consistent with two-stage melting. The reward is higher when the quantities approach the expected values and trends produced by a correct implementation of the Langevin dynamics protocol. Simply reporting arbitrary or hand-guessed numbers will not receive credit; you must carry out the full computational workflow described above. The overall score combines the accuracy of the T=0 angles, the correctness of the order parameter trend, and the presence of all required fields in the JSON.
