# Classical Nucleation Theory Critical Size Calculation

## Problem background
In nuclear physics, phase transitions in hot nuclear matter can lead to liquid-gas coexistence and droplet formation, analogous to classical nucleation in a supersaturated vapor. When an excited blob of nuclear matter expands to subnuclear densities in the metastable region, droplets may form. The free energy change associated with forming a droplet of a given radius determines the stability of the vapor phase and the critical size above which droplets grow. Fisher's droplet model provides a framework to compute this free energy as a function of droplet radius, and the resulting critical radius reflects the conditions for phase separation. This task computes the free energy landscape and extracts critical radii for a nucleonic vapor at a temperature T = 10 MeV for several supersaturation ratios.

## Approach
The free energy change ΔG upon forming a spherical droplet of radius r is modeled with three contributions: a surface term proportional to r², a bulk condensation term proportional to r³ and the logarithm of the supersaturation ratio S, and an entropy correction due to the closed surface. The model uses fixed parameters: surface tension σ, nuclear liquid density n, temperature T, and a critical exponent τ. The task evaluates ΔG(r) at four supersaturation ratios S = 1, 2, 3, 4. For S > 1, the ΔG curve exhibits a maximum at the critical radius r*, which is the smallest droplet size that can grow spontaneously. For S = 1, there is no driving force for condensation and ΔG increases monotonically. By numerically locating the maximum of ΔG(r) for each S > 1, the critical radii are determined.

## Reproduction target
Compute the free energy change ΔG as a function of droplet radius r using Fisher's droplet model at T = 10 MeV for supersaturation ratios S = 1, 2, 3, 4. Evaluate r on a sufficiently fine grid to capture the peaks. For S = 2, 3, 4, determine the critical radius r* as the r that maximizes ΔG. For S = 1, confirm that ΔG increases monotonically with r (no local maximum). Output the full ΔG(r) data for all S in delta_g_vs_r.csv and the extracted critical radii for S = 2, 3, 4 in critical_radii.json.

## Assets

- Python 3 with NumPy and SciPy: numpy, scipy

## Workflow steps

### Step 1: Compute radius parameter r0
- Role: process
- Action: Calculate the radius constant r0 from the liquid droplet number density n = 0.15 fm^{-3} using the relation r0 = (3/(4πn))^(1/3). This value enters the logarithmic term of the free energy formula.
- Evidence: `/app/outputs/r0.txt`

### Step 2: Compute free energy landscapes
- Role: scored (load-bearing)
- Action: For each supersaturation ratio S in {1, 2, 3, 4}, compute the free energy change ΔG as a function of droplet radius r using Fisher's droplet model: ΔG = 4πσ r² − (4/3)π n T ln(S) r³ + 3 T τ ln(r/r0). Use σ = 1 MeV·fm⁻², n = 0.15 fm⁻³, T = 10 MeV, τ = 2.2. Evaluate r over a range covering the expected critical radii (from near 0 to 10 fm) with sufficient resolution to identify the peak. Export the data as a CSV file.
- Output file: `/app/outputs/delta_g_vs_r.csv`
- Format: csv
- Contract: Columns: r (float, fm), S (int), delta_G (float, MeV)
- Scoring: scored by hidden verifier

### Step 3: Extract critical radii
- Role: scored
- Action: From the computed ΔG(r) curves, determine the critical radius r* for S=2, 3, and 4. The critical radius is the value of r at which ΔG is maximum. For S=1, there is no local maximum; indicate that no critical radius exists. Output the results as a JSON file.
- Output file: `/app/outputs/critical_radii.json`
- Format: json
- Contract: Keys: 'S2', 'S3', 'S4' mapping to floats (units: fm). Example: {'S2': 2.6, 'S3': 2.0, 'S4': 1.8} (values are illustrative).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_g_vs_r.csv`
- `/app/outputs/critical_radii.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_g_vs_r.csv
- path: `/app/outputs/delta_g_vs_r.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Free energy change ΔG as a function of radius r for each saturation ratio S. The checker recomputes the critical radii from this data and compares to the hidden paper gold.
- schema:
  - `type`: table
  - `required_columns`: `r`, `S`, `delta_G`
  - `units`:
    - `r`: fm
    - `delta_G`: MeV

### critical_radii.json
- path: `/app/outputs/critical_radii.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The agent's extracted critical radii for S=2,3,4. The checker compares these directly to the paper-reported gold values with a tolerance.
- schema:
  - `type`: object
  - `required`: `S2`, `S3`, `S4`
  - `items`:
    - `type`: number
    - `units`: fm

Notes: All input parameters are explicitly given; the agent must implement Fisher's formula and choose an appropriate numerical method for peak finding. No external datasets are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_g_vs_r.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "S",
          "delta_G"
        ],
        "units": {
          "r": "fm",
          "delta_G": "MeV"
        }
      },
      "description": "Free energy change ΔG as a function of radius r for each saturation ratio S. The checker recomputes the critical radii from this data and compares to the hidden paper gold."
    },
    {
      "file": "critical_radii.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "S2",
          "S3",
          "S4"
        ],
        "items": {
          "type": "number",
          "units": "fm"
        }
      },
      "description": "The agent's extracted critical radii for S=2,3,4. The checker compares these directly to the paper-reported gold values with a tolerance."
    }
  ],
  "notes": "All input parameters are explicitly given; the agent must implement Fisher's formula and choose an appropriate numerical method for peak finding. No external datasets are required."
}
```

## How you are scored
A hidden verifier will score your submission in two stages, each carrying part of the total reward. First, it will read your delta_g_vs_r.csv and independently identify the maximum ΔG for S = 2, 3, 4, then compare the corresponding r values to a reference derived from the original study. For S = 1, it will check that ΔG is strictly increasing with r. Second, it will read your critical_radii.json and compare the reported r* values directly to the same hidden reference. The checks are combined into a final reward; a high reward requires accurate critical radii that are consistent with the reference within an acceptable margin. The scoring does not depend on quoting specific numerical targets—it verifies that the results you compute match the physical expectation.
