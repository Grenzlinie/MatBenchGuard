# Ab Initio MD Analysis of Short-Range Order in Co67B33 Metallic Glass

## Problem background
Co-based metallic glasses exhibit remarkable mechanical properties, including a very high elastic limit at room temperature that is known to decrease significantly upon heating. Understanding the atomic‑scale origin of this temperature dependence is critical for designing metallic glasses with improved high‑temperature performance. This task probes the topological short‑range order in a model Co₆₇B₃₃ glass using ab initio molecular dynamics (AIMD) simulations. The goal is to quantify how the local structure—including pair correlations, bond‑angle distributions, and dense‑packing motifs—evolves between a low reference temperature and an elevated temperature, thereby providing a basis to correlate structural changes with the reported mechanical response.

## Approach
Construct an amorphous Co₆₇B₃₃ atomic model with the experimentally reported composition and density. Using a density functional theory (DFT) code with PAW pseudopotentials and the PBE exchange‑correlation functional, perform a melt‑quench protocol to obtain a glassy configuration, followed by NVT production runs at 300 K and at a solver‑chosen higher temperature (≥600 K). From the saved trajectories, extract the partial pair distribution functions g(r) for Co–B and B–B pairs, the B–Co–B bond angle distribution, and Voronoi tessellation statistics to identify Frank–Kasper‑like polyhedra. The structural quantities obtained at the two temperatures are then contrasted to infer temperature‑induced changes in short‑range order.

## Reproduction target
Reproduce, via AIMD simulation, the temperature‑dependent topological short‑range order of amorphous Co₆₇B₃₃. Compute and submit three artifacts:
- **partial_pdfs.csv**: partial pair distribution functions for Co–B and B–B pairs at 300 K and at the solver‑selected high temperature;
- **bond_angle_dist.csv**: the B–Co–B bond angle distribution at both temperatures;
- **voronoi_fractions.json**: the fraction of Frank–Kasper‑like Voronoi polyhedra at both temperatures.
The checker will extract quantitative structural features from these curves (peak positions, relative amplitudes, fraction changes) and assess their agreement, including the relative changes between the two temperatures, against the paper’s reference values within prescribed tolerances.

## Assets

- Ab initio molecular dynamics package

## Workflow steps

### Step 1: AIMD simulation of Co67B33
- Role: process
- Action: Set up an amorphous Co67B33 atomic model with 125 Co and 61 B atoms at the experimental density of 7.9 g/cm³. Use a DFT code (e.g., Quantum ESPRESSO, CP2K, VASP) with PAW pseudopotentials and the PBE functional to perform a melt-quench protocol to obtain a glassy configuration, followed by NVT production runs at 300 K and at least one higher temperature (≥600 K, e.g., 1000 K or 1600 K). Save the atomic trajectories for subsequent analysis.
- Evidence: `/app/outputs/aimd_log.txt`

### Step 2: Compute partial PDFs
- Role: scored (load-bearing)
- Action: From the AIMD trajectory, compute the partial pair distribution functions g(r) for Co-B and B-B pairs at the two temperatures (300 K and the chosen higher temperature). Output the curves as a CSV file with columns: r (Å), Co_B_g_300K, B_B_g_300K, Co_B_g_highT, B_B_g_highT. Label the high-temperature columns with the actual temperature (e.g., Co_B_g_1000K).
- Output file: `/app/outputs/partial_pdfs.csv`
- Format: csv
- Contract: r (Å), Co_B_g_300K (dimensionless), B_B_g_300K (dimensionless), Co_B_g_highT (dimensionless), B_B_g_highT (dimensionless); highT temperature indicated in column name or metadata.
- Scoring: scored by hidden verifier

### Step 3: Compute B-Co-B bond angle distribution
- Role: scored (load-bearing)
- Action: From the same AIMD trajectory, compute the B-Co-B bond angle distribution (angle range 0–180°) at the two temperatures. Output a CSV file with columns: angle_degrees, probability_300K, probability_highT.
- Output file: `/app/outputs/bond_angle_dist.csv`
- Format: csv
- Contract: angle_degrees, probability_300K (dimensionless), probability_highT
- Scoring: scored by hidden verifier

### Step 4: Compute Frank-Kasper polyhedra fraction
- Role: scored (load-bearing)
- Action: Perform Voronoi tessellation on the atomic configurations at each temperature. Identify Frank-Kasper-like (densely packed) polyhedra (e.g., boron-centred bicapped square Archimedean antiprism) and compute their fraction relative to all polyhedra. Output a JSON file with keys Frank_Kasper_fraction_300K and Frank_Kasper_fraction_highT (floats between 0 and 1).
- Output file: `/app/outputs/voronoi_fractions.json`
- Format: json
- Contract: {"Frank_Kasper_fraction_300K": float, "Frank_Kasper_fraction_highT": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/partial_pdfs.csv`
- `/app/outputs/bond_angle_dist.csv`
- `/app/outputs/voronoi_fractions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### partial_pdfs.csv
- path: `/app/outputs/partial_pdfs.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Partial pair distribution functions g(r) for Co-B and B-B pairs at 300 K and a higher temperature chosen by the solver (≥600 K). The checker will detect local maxima in specified r windows and compare extracted peak positions to hidden paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `r`, `Co_B_g_300K`, `B_B_g_300K`, `Co_B_g_highT`, `B_B_g_highT`
  - `units`:
    - `r`: Å
    - `Co_B_g_300K`: dimensionless
    - `B_B_g_300K`: dimensionless
    - `Co_B_g_highT`: dimensionless
    - `B_B_g_highT`: dimensionless

### bond_angle_dist.csv
- path: `/app/outputs/bond_angle_dist.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: B-Co-B bond angle distribution at 300 K and the same higher temperature. The checker will identify the amplitude of the peak near 90° and verify that it decreases (broadens) with temperature.
- schema:
  - `type`: table
  - `required_columns`: `angle_degrees`, `probability_300K`, `probability_highT`
  - `units`:
    - `angle_degrees`: degrees
    - `probability_300K`: dimensionless
    - `probability_highT`: dimensionless

### voronoi_fractions.json
- path: `/app/outputs/voronoi_fractions.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fraction of Frank-Kasper-like Voronoi polyhedra at 300 K and the higher temperature. The checker will verify that fractions are between 0 and 1, that the high-temperature fraction is lower than 300 K, and that the values match hidden paper-reported fractions within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Frank_Kasper_fraction_300K`: float
    - `Frank_Kasper_fraction_highT`: float
  - `items`: object
  - `units`: object

Notes: The solver must choose the higher temperature (e.g., 1000 K or 1600 K) and clearly label columns/keys accordingly. The checker recomputes structural features from the raw CSV/JSON files and compares them to hidden gold values derived from the paper. No experimental XRD comparison or elastic limit discussion is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "partial_pdfs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "Co_B_g_300K",
          "B_B_g_300K",
          "Co_B_g_highT",
          "B_B_g_highT"
        ],
        "units": {
          "r": "Å",
          "Co_B_g_300K": "dimensionless",
          "B_B_g_300K": "dimensionless",
          "Co_B_g_highT": "dimensionless",
          "B_B_g_highT": "dimensionless"
        }
      },
      "description": "Partial pair distribution functions g(r) for Co-B and B-B pairs at 300 K and a higher temperature chosen by the solver (≥600 K). The checker will detect local maxima in specified r windows and compare extracted peak positions to hidden paper-reported values."
    },
    {
      "file": "bond_angle_dist.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_degrees",
          "probability_300K",
          "probability_highT"
        ],
        "units": {
          "angle_degrees": "degrees",
          "probability_300K": "dimensionless",
          "probability_highT": "dimensionless"
        }
      },
      "description": "B-Co-B bond angle distribution at 300 K and the same higher temperature. The checker will identify the amplitude of the peak near 90° and verify that it decreases (broadens) with temperature."
    },
    {
      "file": "voronoi_fractions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "Frank_Kasper_fraction_300K": "float",
          "Frank_Kasper_fraction_highT": "float"
        },
        "items": {},
        "units": {}
      },
      "description": "Fraction of Frank-Kasper-like Voronoi polyhedra at 300 K and the higher temperature. The checker will verify that fractions are between 0 and 1, that the high-temperature fraction is lower than 300 K, and that the values match hidden paper-reported fractions within tolerances."
    }
  ],
  "notes": "The solver must choose the higher temperature (e.g., 1000 K or 1600 K) and clearly label columns/keys accordingly. The checker recomputes structural features from the raw CSV/JSON files and compares them to hidden gold values derived from the paper. No experimental XRD comparison or elastic limit discussion is required."
}
```

## How you are scored
A hidden verifier independently reads your submitted files and recomputes structural metrics:
- For **partial PDFs**, it detects local maxima in specified r‑windows, extracts peak positions, and evaluates their broadening with temperature.
- For the **bond angle distribution**, it measures the amplitude of features near 90° and how they change between 300 K and the higher temperature.
- For the **Voronoi fractions**, it compares the reported fractions at each temperature and verifies that the high‑temperature fraction is lower than the 300 K one, within an absolute difference tolerance.

Each artifact is scored on a continuous scale from 0 to 1, and the final reward is a weighted sum:
- 40 % for the partial PDF features,
- 30 % for the bond angle trend,
- 30 % for the Voronoi fractions.

Simply reporting the paper’s numbers is insufficient; the verifier recomputes the features from your raw data and compares them to hidden reference values. No gold numbers or tolerances are provided to you.
