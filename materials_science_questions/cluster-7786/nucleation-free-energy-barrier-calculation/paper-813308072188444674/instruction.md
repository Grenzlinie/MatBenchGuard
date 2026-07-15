# Nucleation and Growth Simulator for Phase-Change Material Grain Size

## Problem background
Phase-change memory (PCM) devices use materials like Ge2Sb2Te5 (GST) that can switch between amorphous and crystalline states with a large resistance contrast. The crystalline state is composed of many polycrystalline grains, and the distribution of grain sizes directly affects intermediate resistance levels, multi-level cell operation, and long-term device reliability. Understanding how these grains nucleate and grow under different thermal histories is critical for engineering PCM technology. Classical nucleation theory (CNT) provides a quantitative framework to model the formation and evolution of crystalline nuclei, and when implemented in a voxelized numerical simulator, it can predict grain size distributions resulting from various annealing protocols. This task focuses on reproducing such a simulator and using it to predict the median grain area in GST films annealed at three different temperature ramp rates, providing a computational test of the underlying nucleation and growth physics.

## Approach
The method is a voxelized classical nucleation theory simulator. It models a thin GST film as a 3‑D grid of voxels, each capable of supporting sub‑critical nuclei populations or growing into a crystalline grain. The free energy of a nucleus is described by a spherical‑cap model that incorporates the temperature‑dependent bulk free energy difference between amorphous and crystalline phases (Hoffmann model). At each voxel, rate equations track the stochastic addition and removal of monomers to nuclei, with jump rates tied to the local viscosity. The viscosity itself follows an Arrhenius law below the glass transition temperature and a Vogel–Fulcher–Tammann equation above it, making crystallization kinetics highly temperature‑sensitive. Once a nucleus exceeds the critical size, it propagates as a growth front through neighboring voxels with a velocity derived consistently from the rate equations. Heterogeneous nucleation (with a contact angle θ = 90°) is permitted at GST‑capping‑layer interfaces, while homogeneous nucleation (θ = 180°) occurs in the bulk. The simulation is performed at three constant heating rates—380, 7.5, and 0.17 °C/min—using a 204×204×43 grid with 5 nm × 5 nm × 2.5 nm voxels and the physical parameters specified in the workflow step. Multiple independent runs per rate (each with a different random seed) capture the stochastic nature of nucleation. After each run, the grain ID maps are analyzed to compute the distribution of grain areas; the median grain area (the area such that half of the total crystalline area is covered by larger grains) is extracted and averaged across runs for each ramp rate.

## Reproduction target
Implement the CNT simulator as described in Step 1 and run it for all three ramp rates (380, 7.5, 0.17 °C/min), performing at least five independent simulations per rate with different random seeds. From the resulting grain‑ID maps, compute the median grain area for each run and then average these medians per ramp rate. Write the three average median grain areas (in nm²) to a JSON file named median_grain_areas.json with keys exactly "380", "7.5", and "0.17". The goal is to produce realistic grain size estimates that can be compared against experimental measurements, thereby demonstrating that the simulator correctly captures the dependence of grain size on ramp rate.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Simulate nucleation and growth at three ramp rates
- Role: process
- Action: Implement a voxelized classical nucleation theory simulator for GST crystallization as described in the method: use a spherical-cap free energy model with Hoffmann Δg, rate equations for sub-critical nuclei with per-voxel histograms, growth-front propagation, and heterogeneous/homogeneous nucleation. Use the provided physical parameters (monomer volume 2.9e-28 m³, enthalpy of fusion 6.1e8 J/m³, melting temperature 900 K (627 °C), surface energy 0.060 J/m², activation energy 2.3 eV, glass transition 155 °C, viscosity at Tg 1.65e8 Pa·s, fragility 24.25, Vogel-Fulcher temperature 120 °C, nearest-neighbor distance 0.299 nm). Run simulations on a 204×204×43 grid of 5 nm × 5 nm × 2.5 nm voxels with heterogeneous nucleation (θ=90°) at GST–interface voxels and homogeneous nucleation (θ=180°) in bulk, for three constant ramp rates (380, 7.5, 0.17 °C/min). For each ramp rate, run at least five independent simulations with different random seeds. Save the resulting 3D grain ID maps or per-voxel crystallinity data to disk for later analysis.
- Evidence: `/app/outputs/grain_maps.npz`

### Step 2: Compute average median grain area
- Role: scored (load-bearing)
- Action: From the saved grain ID maps for each ramp rate and each random seed, compute the distribution of grain areas (count of voxels per grain × voxel area). For each run, determine the median grain area by finding the area at which 50% of the total crystalline area is covered by larger grains. Average these medians across the runs for each ramp rate, and write a JSON file containing the three average median areas.
- Output file: `/app/outputs/median_grain_areas.json`
- Format: json
- Contract: A JSON object with exactly three keys: "380", "7.5", "0.17". Each value is a floating-point number representing the average median grain area in nm².
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/median_grain_areas.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### median_grain_areas.json
- path: `/app/outputs/median_grain_areas.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Average median grain area for three temperature ramp rates, computed from stochastic nucleation-and-growth simulations. The hidden checker compares these against paper-reported experimental values (TEM) using relative error thresholds.
- schema:
  - `type`: object
  - `required`: `380`, `7.5`, `0.17`
  - `properties`:
    - `380`:
      - `type`: number
      - `units`: nm²
    - `7.5`:
      - `type`: number
      - `units`: nm²
    - `0.17`:
      - `type`: number
      - `units`: nm²

Notes: The simulation uses the physical parameters, geometry, and nucleation model described in the steps; no additional calibration or parameter fitting is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "median_grain_areas.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "380",
          "7.5",
          "0.17"
        ],
        "properties": {
          "380": {
            "type": "number",
            "units": "nm²"
          },
          "7.5": {
            "type": "number",
            "units": "nm²"
          },
          "0.17": {
            "type": "number",
            "units": "nm²"
          }
        }
      },
      "description": "Average median grain area for three temperature ramp rates, computed from stochastic nucleation-and-growth simulations. The hidden checker compares these against paper-reported experimental values (TEM) using relative error thresholds."
    }
  ],
  "notes": "The simulation uses the physical parameters, geometry, and nucleation model described in the steps; no additional calibration or parameter fitting is required."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the median_grain_areas.json file. For each of the three ramp rates, the verifier compares the average median grain area you report to a hidden reference value derived from experimental TEM measurements of GST films annealed under the same conditions. The comparison uses a relative error metric, and the score for each rate is based on how close your value is to the reference. The final reward is the arithmetic mean of the three individual scores. You must not hardcode or guess the reference values; the only way to achieve a high score is to faithfully implement the simulator and run the requested simulations to produce genuine, physics‑based outputs.
