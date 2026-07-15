# Steady-state μTEG performance simulation with load resistance sweep

## Problem background
Nanostructured PbTe–SrTe alloys are promising for high-temperature thermoelectric generation. This work models a micro-thermoelectric generator (μTEG) consisting of a single p–n leg pair with temperature-dependent material properties, and investigates how load resistance R_L and thermoelement geometry (rectangular vs. trapezoidal) affect the conversion efficiency and output power at a fixed temperature difference ΔT = 560 K.

## Approach
The approach uses finite-element modeling of coupled electrical and thermal transport, accounting for temperature-dependent material properties (Seebeck coefficient, electrical resistivity, thermal conductivity) described by polynomial fits. The μTEG consists of a single p-n thermocouple pair electrically in series and thermally in parallel. Two thermoelement geometries are considered: a rectangular prism (120 μm × 120 μm × 300 μm) and a trapezoidal prism (length 300 μm, lower width 40 μm, upper width 200 μm, thickness 120 μm, inclination angle 72°). The simulation solves the steady-state heat and charge transport equations under fixed temperatures: cold side at 300 K and hot side at 860 K (ΔT = 560 K). An external load resistance R_L is connected, and by varying R_L across a range we can compute the conversion efficiency η (ratio of output electrical power to heat absorbed at the hot side) and the output power P_out. This procedure is repeated for two material compositions (4 mol% SrTe and 2 mol% SrTe) combined with both geometries, giving four distinct cases. The output is a dense sweep of η and P_out versus R_L for each case, from which the maximum values can be identified.

## Reproduction target
Produce a single CSV file, /app/outputs/sweep_data.csv, containing the computed efficiency (%) and output power (mW) for every simulated load resistance value R_L (Ω) in a sweep that covers at least 0.1–1.2 Ω with sufficient resolution to locate the maxima. This sweep must be performed independently for all four combinations of material (4% SrTe, 2% SrTe) and geometry (rectangular, trapezoidal). The file must follow the output contract schema exactly. The hidden verifier will parse this file, extract the maximum η and maximum P_out for each combination, and compare them to held-out reference benchmarks. Producing a valid, well-resolved sweep is the goal; merely reporting the paper's numbers without running the simulation will not yield a correct sweep and will not satisfy the verification.

## Assets

- FEniCS (finite element framework): https://fenicsproject.org

## Workflow steps

### Step 1: FEM simulation and efficiency/power sweep at ΔT = 560 K
- Role: scored
- Action: Build a 3D finite-element model of a single-pair μTEG (p‑n leg) with temperature-dependent Seebeck coefficient, electrical resistivity, and thermal conductivity given by the polynomial fits in the paper. Implement both geometries: rectangular (120 μm × 120 μm × 300 μm) and trapezoidal (length 300 μm, lower width 40 μm, upper width 200 μm, thickness 120 μm, inclination angle 72°). Set cold-side temperature Tc = 300 K, hot-side Th = 860 K (ΔT = 560 K). Solve the coupled heat‑charge transport PDEs for a fine range of load resistances RL (cover at least 0.1–1.2 Ω at a resolution sufficient to locate maxima). Record the computed efficiency η (%) and output power Pout (mW) for every simulated RL. Run for all four material‑geometry combinations: 4 mol% SrTe and 2 mol% SrTe, each with rectangular and trapezoidal shape. Output a single CSV file containing every simulated point.
- Output file: `/app/outputs/sweep_data.csv`
- Format: csv
- Contract: CSV with columns: material (str, one of '4% SrTe' or '2% SrTe'), geometry (str, one of 'rectangular' or 'trapezoidal'), RL (float, Ω), eta (float, %), Pout (float, mW). Each row is one simulated load resistance value for one combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sweep_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sweep_data.csv
- path: `/app/outputs/sweep_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Full sweep of efficiency and output power vs. load resistance for four combinations (material × geometry) at ΔT = 560 K. The checker will extract the maximum η and maximum Pout for each combination and compare to the paper’s reported values.
- schema:
  - `type`: table
  - `required_columns`: `material`, `geometry`, `RL`, `eta`, `Pout`
  - `units`:
    - `RL`: Ω
    - `eta`: %
    - `Pout`: mW

Notes: The simulation must use the material property polynomials exactly as given in the paper (Table 1) and must cover a load resistance range dense enough to resolve the maxima. No external dataset is required; the workflow is entirely compute-driven.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sweep_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "geometry",
          "RL",
          "eta",
          "Pout"
        ],
        "units": {
          "RL": "Ω",
          "eta": "%",
          "Pout": "mW"
        }
      },
      "description": "Full sweep of efficiency and output power vs. load resistance for four combinations (material × geometry) at ΔT = 560 K. The checker will extract the maximum η and maximum Pout for each combination and compare to the paper’s reported values."
    }
  ],
  "notes": "The simulation must use the material property polynomials exactly as given in the paper (Table 1) and must cover a load resistance range dense enough to resolve the maxima. No external dataset is required; the workflow is entirely compute-driven."
}
```

## How you are scored
The hidden verifier will read your sweep_data.csv and independently compute the maximum efficiency and maximum output power for each of the four material–geometry combinations. It compares these values to held-out reference benchmarks using predetermined tolerances (not disclosed here). Your reward is the fraction of the four combinations for which both the maximum efficiency and the maximum output power fall within the required tolerance. Purely reporting the paper's numbers without performing the simulation will not produce a valid sweep and will fail this check.
