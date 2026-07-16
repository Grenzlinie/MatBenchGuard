# Heat flow simulation and nucleation estimation in laser-annealed silicon films

## Problem background
Pulsed XeCl excimer laser irradiation of thin hydrogenated amorphous silicon (a-Si:H) films on quartz induces rapid melting and subsequent solidification. Depending on laser energy and film thickness, the film may solidify into a polycrystalline state via interface-controlled growth, or into an amorphous state via homogeneous solidification. The transition is governed by the temperature distribution in the molten silicon, in particular the temperature gradient at the Si/quartz interface at the onset of solidification. The paper whose computational sub-result we reproduce reports that a temperature gradient below a critical threshold drives homogeneous amorphization, while larger gradients maintain a moving liquid/solid interface and yield crystallization. Additionally, thickness-dependent amorphization data show that films thinner than about 18 nm amorphize fully, films around 24 nm show mixed crystalline and amorphous phases, and films of 36 nm are predominantly crystalline, enabling an estimation of the minimum crystalline nucleation density and nucleation rate under these rapid solidification conditions.

This task isolates the numerical heat-flow simulation and the derived nucleation estimates that support those claims. The required inputs (film thicknesses, amorphization threshold laser energies, and standard thermal/optical properties of silicon and quartz) are all publicly available and will be provided in the instruction. The output quantities—melt duration, temperature gradient, and nucleation density and rate—are to be computed and saved to the specified output files.

## Approach
The core computational work is a one-dimensional heat-flow simulation of pulsed laser melting. The model considers a thin a-Si film on a thick quartz substrate, heated by a laser pulse with a known temporal shape (30 ns FWHM Gaussian) and incident energy density. The material properties (density, specific heat, thermal conductivity, latent heat of fusion, melting point, reflectivity) are taken from standard literature values provided in a table.

You will implement a numerical solver (e.g., explicit finite differences) for the 1D heat equation, tracking the temperature profile over time. From the simulation, for each given film thickness and its corresponding amorphization threshold energy, determine:
- The melt duration, defined as the time interval during which the entire film depth exceeds the melting temperature.
- The temperature gradient in the liquid silicon at the Si/quartz interface at the moment when solidification begins (when the interface temperature drops to the melting point and the interface starts to move).

In the second stage, you will use the reported experimental observation that complete amorphization occurs for films ≤18 nm, mixed phases appear at 24 nm, and 36 nm films are predominantly crystalline. Assuming spherical crystalline grains whose growth is bounded by film thickness, and that the 36 nm film is fully crystallized, compute a minimum nucleation density (one grain per thickness-limited volume). Then, using an upper-bound solidification time of 5 ns (the experimental detection limit), estimate the minimum nucleation rate. These geometric and kinetic estimates yield the nucleation density and nucleation rate, which you will write as a JSON object.

All numerical methods are left to you to choose and implement with appropriate convergence and stability safeguards.

## Reproduction target
Reproduce the computational components that support the reported temperature gradient threshold and the nucleation estimates. Specifically:

1. Simulate pulsed-laser melting for a-Si films of thickness 12, 24, and 36 nm on quartz, using the amorphization threshold laser energies provided in the instruction. Compute the melt duration (ns) and the temperature gradient (K/cm) in liquid silicon at the Si/quartz interface just before solidification. Write the results to `step_01_simulation_results.csv` following the required schema.

2. Using the thickness-dependent amorphization pattern (full amorphization ≤18 nm, mixed at 24 nm, crystalline at 36 nm) and the assumption that spherical grains fill the film thickness in the fully crystallized 36 nm case, compute the minimum crystalline nucleation density (m⁻³). Then, taking the solidification completion time as ≤5 ns, compute the minimum nucleation rate (m⁻³ s⁻¹). Write these two numbers to `step_02_nucleation_results.json`.

The outputs must be placed in `/app/outputs/` as specified in the workflow steps. The simulation results and the nucleation estimates together form the reproduction target.

## Assets

- Standard thermal and optical properties of amorphous/crystalline silicon and quartz (density, specific heat, thermal conductivity, latent heat, melting point, reflectivity)

## Workflow steps

### Step 1: Heat-flow numerical simulation
- Role: scored
- Action: Solve the 1D heat equation numerically (finite difference method) for a pulsed-laser melting scenario. Use the provided film thicknesses (12, 24, 36 nm), amorphization threshold laser energies (given in instruction), and the standard thermal properties of silicon and quartz (provided in instruction). Assume initial temperature 300 K, a 30 ns FWHM Gaussian laser pulse shape, and appropriate boundary conditions. Extract the melt duration and the temperature gradient in liquid silicon at the Si/quartz interface at the onset of solidification. Write results to step_01_simulation_results.csv.
- Output file: `/app/outputs/step_01_simulation_results.csv`
- Format: csv
- Contract: Columns: film_thickness_nm (int), amorphization_threshold_mJ_per_cm2 (float), melt_duration_ns (float), temperature_gradient_K_per_cm (float).
- Scoring: scored by hidden verifier

### Step 2: Crystalline nucleation density and rate estimation
- Role: scored (load-bearing)
- Action: Using the film-thickness dependence of amorphization (full amorphization for films <=18 nm, mixed at 24 nm, fully crystalline at 36 nm), estimate the minimum crystalline nucleation density by assuming spherical grains with diameter limited by film thickness and that the 36 nm film was completely crystallized. Then, using the detection-limited solidification time (<5 ns), compute the minimum nucleation rate. Write estimates to step_02_nucleation_results.json.
- Output file: `/app/outputs/step_02_nucleation_results.json`
- Format: json
- Contract: Object with keys: nucleation_density_m3 (float, units m^-3), nucleation_rate_m3_s1 (float, units m^-3 s^-1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_simulation_results.csv`
- `/app/outputs/step_02_nucleation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_simulation_results.csv
- path: `/app/outputs/step_01_simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulation results for melt duration and temperature gradient at the Si/quartz interface for three film thicknesses.
- schema:
  - `type`: table
  - `required_columns`: `film_thickness_nm`, `amorphization_threshold_mJ_per_cm2`, `melt_duration_ns`, `temperature_gradient_K_per_cm`
  - `units`:
    - `film_thickness_nm`: nm
    - `amorphization_threshold_mJ_per_cm2`: mJ/cm²
    - `melt_duration_ns`: ns
    - `temperature_gradient_K_per_cm`: K/cm

### step_02_nucleation_results.json
- path: `/app/outputs/step_02_nucleation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Estimated minimum crystalline nucleation density and nucleation rate.
- schema:
  - `type`: object
  - `required`: `nucleation_density_m3`, `nucleation_rate_m3_s1`
  - `items`:
    - `nucleation_density_m3`: float (unit: m^-3)
    - `nucleation_rate_m3_s1`: float (unit: m^-3 s^-1)

Notes: All values are to be compared against hidden paper-reported reference values with relative tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "film_thickness_nm",
          "amorphization_threshold_mJ_per_cm2",
          "melt_duration_ns",
          "temperature_gradient_K_per_cm"
        ],
        "units": {
          "film_thickness_nm": "nm",
          "amorphization_threshold_mJ_per_cm2": "mJ/cm²",
          "melt_duration_ns": "ns",
          "temperature_gradient_K_per_cm": "K/cm"
        }
      },
      "description": "Simulation results for melt duration and temperature gradient at the Si/quartz interface for three film thicknesses."
    },
    {
      "file": "step_02_nucleation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "nucleation_density_m3",
          "nucleation_rate_m3_s1"
        ],
        "items": {
          "nucleation_density_m3": "float (unit: m^-3)",
          "nucleation_rate_m3_s1": "float (unit: m^-3 s^-1)"
        }
      },
      "description": "Estimated minimum crystalline nucleation density and nucleation rate."
    }
  ],
  "notes": "All values are to be compared against hidden paper-reported reference values with relative tolerances."
}
```

## How you are scored
A hidden verifier will independently check your output artifacts. Each scored step (`step_01_simulation_results.csv` and `step_02_nucleation_results.json`) is compared against reference values derived from the source work, using appropriate tolerances that account for legitimate differences in numerical implementation. The reward is a weighted combination: the simulation outputs (melt duration and temperature gradient) carry substantial weight, and the nucleation estimates (density and rate) also contribute. Simply reporting the paper's numbers without executing the simulation and the estimation procedure is not sufficient; the verifier expects the computed quantities to be consistent with the input conditions and the described method. There is no partial credit for intermediate files that are not part of the output contract. Your solution should produce both scored artifacts in the specified formats.
