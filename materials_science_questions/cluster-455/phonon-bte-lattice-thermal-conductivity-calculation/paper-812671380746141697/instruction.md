# Laser heating simulation of magnetite-graphene nanocomposite substrates

## Problem background
Hyperthermia treatment uses localized heating to destroy cancer cells, often enhanced by nanoparticles that absorb laser energy and convert it to heat. This task investigates the thermal response of magnetite-graphene nanocomposite substrates under a moving laser beam. The aim is to compute the transient temperature distribution for substrates of varying compositions, to understand which materials can maintain temperatures within a therapeutic window. The physical model couples 3D transient heat conduction in a thin square substrate with 1D laser penetration that depends on temperature, simulating a circularly moving laser spot.

## Approach
The problem is solved numerically using the finite-element method. A substrate of dimensions 10 mm × 10 mm × 1 mm is modeled. The heat equation is coupled with a 1D penetration model for the laser beam (which moves in a circular path of radius 0.02 m with angular velocity 10 rad/s and total input power 50 W). The absorption coefficient decreases linearly with temperature as described in the problem statement. Material properties (density, specific heat, and isotropic thermal conductivity) are provided for seven substrates: pure magnetite (Fe), pure graphene (G), and five hybrid compositions (F25G75, F45G55, F65G35, F75G25, F85G15), where the number indicates the weight percentage of magnetite. For each substrate, the transient simulation is run from t = 0 s to t = 1 s. The required outputs are the global minimum and maximum temperatures at four specific times, extracted from the simulation results.

## Reproduction target
Produce a CSV file `temperature_results.csv` containing the minimum and maximum temperatures (in Kelvin) for each of the seven substrates at the four time points (0.08, 0.46, 0.86, and 1.0 seconds). The file must have exactly 28 rows (7 substrates × 4 times). Additionally, determine the relative ordering of the substrates by their maximum temperature at t = 1.0 s (list them from highest to lowest). A hidden verifier will check both the temperature values and the ordering against reference data.

## Assets

- FEniCS (or equivalent open-source FEM library): https://fenicsproject.org/download/
- NumPy/SciPy: numpy scipy
- Python 3: https://www.python.org/

## Workflow steps

### Step 1: Run coupled heat-transfer FEM simulation
- Role: process
- Action: Implement the 3D transient heat conduction equation coupled with 1D laser penetration and temperature-dependent absorption coefficient for each of the seven substrate compositions (Fe, F25G75, F45G55, F65G35, F75G25, F85G15, G). Use the geometry (10×10×1 mm), material properties (density, specific heat, isotropic thermal conductivity), moving circular laser source (radius 0.02 m, angular velocity 10 rad/s, total power 50 W), and absorption model from the problem specification. Run the simulation from t=0 to t=1 s for each substrate. Record a completion log.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Extract min/max temperatures and save results
- Role: scored (load-bearing)
- Action: From the completed simulation, extract the global minimum and maximum temperature values at times t=0.08, 0.46, 0.86, and 1.0 s for each of the seven substrates. Write a CSV with columns: Substrate (string), Time (float, seconds), MinTemp (float, Kelvin), MaxTemp (float, Kelvin). There must be exactly 28 rows (7 substrates × 4 times).
- Output file: `/app/outputs/temperature_results.csv`
- Format: csv
- Contract: Substrate: one of 'Fe','F25G75','F45G55','F65G35','F75G25','F85G15','G'; Time: one of 0.08,0.46,0.86,1.0; MinTemp: float in K; MaxTemp: float in K. 28 rows total.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_results.csv
- path: `/app/outputs/temperature_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the simulated minimum and maximum temperatures for all substrates and time steps. The checker compares each value to hidden reference values with tolerances and also verifies the relative ordering of MaxTemp at t=1.0 s across substrates.
- schema:
  - `type`: table
  - `required_columns`: `Substrate`, `Time`, `MinTemp`, `MaxTemp`
  - `units`:
    - `MinTemp`: K
    - `MaxTemp`: K

Notes: All required fields and units are listed. The checker uses absolute tolerances and a structural ordering check; tolerances are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Substrate",
          "Time",
          "MinTemp",
          "MaxTemp"
        ],
        "units": {
          "MinTemp": "K",
          "MaxTemp": "K"
        }
      },
      "description": "Scored artifact containing the simulated minimum and maximum temperatures for all substrates and time steps. The checker compares each value to hidden reference values with tolerances and also verifies the relative ordering of MaxTemp at t=1.0 s across substrates."
    }
  ],
  "notes": "All required fields and units are listed. The checker uses absolute tolerances and a structural ordering check; tolerances are not disclosed to the agent."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage. For the main scored artifact (`temperature_results.csv`), the checker will compare your reported minimum and maximum temperatures to reference values (derived from the same physical model, with generous tolerances to account for solver and discretization differences). It will also verify that the ordering of substrates by MaxTemp at 1.0 s matches the expected ordering. The final reward is a weighted combination of the value-proximity score and the ordering score. Reporting the correct numbers is not sufficient; they must be produced by a genuine simulation run as described in the workflow steps.
