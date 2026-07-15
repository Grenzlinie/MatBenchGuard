# Platinum Phase Stability via Z Methodology

## Problem background
Predicting phase stability of crystalline materials under high pressure is a fundamental challenge in materials science and geophysics. A material can adopt multiple crystal structures, and the most stable one may change with pressure and temperature, leading to a phase diagram with melting curves and solid-solid transitions. This task focuses on platinum (Pt), where body-centered cubic (fcc) and a hexagonal structure known as 9R (or α-Sm) are energetically competitive. The open question is: at different pressures, which of these two phases melts at a higher temperature, and which solid phase is the most stable when a liquid is solidified under given pressure–temperature conditions?

## Approach
We use the Z methodology, which consists of two complementary ab initio molecular dynamics (AIMD) techniques. The direct Z method computes melting curves: for a fixed density, sequences of isochoric AIMD runs are performed at increasing energies, covering the solid, superheated solid, and liquid regimes. The melting point is bracketed by the highest temperature at which the system remains solid and the lowest at which it becomes liquid, and is taken as the midpoint. The inverse Z method locates solid-solid phase boundaries: a liquid configuration is prepared at a given density, supercooled to a temperature substantially below the estimated melting point, and then evolved in the NVT ensemble until solidification occurs. The final crystal structure is identified by comparing radial distribution functions or X-ray diffraction patterns. The phase that solidifies is the most stable solid at that pressure and temperature. Both methods are implemented with an open-source AIMD code (e.g., Quantum ESPRESSO) and public pseudopotentials. The workflow will apply these methods to fcc and 9R platinum, computing their melting curves and determining the solidification outcome at selected pressure–temperature points.

## Reproduction target
1. Compute the melting curves of fcc and 9R platinum at pressures of 0, 50, and 100 GPa using the direct Z method. For each phase and pressure, bracket the melting temperature and record it.
2. Determine the most stable solid phase at three distinct (P,T) conditions via the inverse Z method: (20 GPa, 2500 K), (40 GPa, 2500 K), and (100 GPa, 3000 K). For each condition, prepare the liquid, supercool, run NVT AIMD until solidification, and identify whether the final crystal structure is fcc or hexagonal/9R.
3. Write the results to two CSV files: melting_curves.csv with columns pressure_GPa, phase, melting_temperature_K; and inverse_z_results.csv with columns pressure_GPa, temperature_K, solid_phase.
These outputs are scored; the exact expected numbers are not provided—you must compute them from the defined methodology.

## Assets

- Quantum ESPRESSO (open-source AIMD code): https://www.quantum-espresso.org/download
- Pseudopotentials for Pt (SSSP or PSLibrary): https://www.quantum-espresso.org/pseudopotentials
- Crystal structures for fcc and 9R Pt

## Workflow steps

### Step 1: Compute melting curves of fcc and 9R Pt via direct Z method
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO, carry out direct Z isochore sequences for fcc and 9R Pt at densities corresponding to 0, 50, and 100 GPa. For each structure and density, follow the direct Z protocol: AIMD runs in the solid, superheated solid, and liquid regimes, bracketing the melting point. Compute the melting temperature as the midpoint between the highest solid temperature and lowest liquid temperature. Write the resulting melting temperatures for each phase and pressure to the output file.
- Output file: `/app/outputs/melting_curves.csv`
- Format: csv
- Contract: pressure_GPa: float, phase: string, melting_temperature_K: float
- Scoring: scored by hidden verifier

### Step 2: Determine most stable solid phase via inverse Z solidification
- Role: scored (load-bearing)
- Action: For each of the three (P,T) conditions: (20 GPa, 2500 K), (40 GPa, 2500 K), (100 GPa, 3000 K), perform inverse Z solidification. Prepare a liquid Pt configuration at the appropriate density, supercool to a temperature within 0.55–0.85 times the estimated melting temperature, then run NVT AIMD (Nosé–Hoover thermostat, 1 fs timestep) until solidification occurs (up to 20 ps). Identify the final crystal structure using radial distribution function or X-ray diffraction pattern analysis (distinguish fcc from hexagonal/9R). Record the identified solid phase.
- Output file: `/app/outputs/inverse_z_results.csv`
- Format: csv
- Contract: pressure_GPa: float, temperature_K: float, solid_phase: string
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/melting_curves.csv`
- `/app/outputs/inverse_z_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### melting_curves.csv
- path: `/app/outputs/melting_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Melting temperatures of fcc and 9R platinum at 0, 50, and 100 GPa computed via the direct Z method.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `phase`, `melting_temperature_K`
  - `units`:
    - `pressure_GPa`: GPa
    - `melting_temperature_K`: K

### inverse_z_results.csv
- path: `/app/outputs/inverse_z_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Most stable solid phase identified via inverse Z solidification at three (P,T) conditions.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `temperature_K`, `solid_phase`
  - `units`:
    - `pressure_GPa`: GPa
    - `temperature_K`: K

Notes: The direct Z method requires running multiple AIMD simulations to bracket the melting point. The inverse Z method requires liquid preparation, supercooling, and an NVT solidification run. The agent may use Quantum ESPRESSO or another open-source AIMD code with appropriate pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "melting_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "phase",
          "melting_temperature_K"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "melting_temperature_K": "K"
        }
      },
      "description": "Melting temperatures of fcc and 9R platinum at 0, 50, and 100 GPa computed via the direct Z method."
    },
    {
      "file": "inverse_z_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "temperature_K",
          "solid_phase"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "temperature_K": "K"
        }
      },
      "description": "Most stable solid phase identified via inverse Z solidification at three (P,T) conditions."
    }
  ],
  "notes": "The direct Z method requires running multiple AIMD simulations to bracket the melting point. The inverse Z method requires liquid preparation, supercooling, and an NVT solidification run. The agent may use Quantum ESPRESSO or another open-source AIMD code with appropriate pseudopotentials."
}
```

## How you are scored
A hidden verifier will independently evaluate each of your two output files. For melting_curves.csv, the verifier compares your melting temperatures against a hidden reference for each pressure and phase, checking both the absolute values within an allowed tolerance and the overall trend between the two phases across pressures. For inverse_z_results.csv, the verifier checks whether the identified solid phase at each of the three (P,T) points matches the correct most stable phase. The two stages are combined by weight to yield a final reward between 0 and 1. Reporting a number without genuinely running the required simulations will likely fail because the verifier expects numbers that can only emerge from the full AIMD protocol.
