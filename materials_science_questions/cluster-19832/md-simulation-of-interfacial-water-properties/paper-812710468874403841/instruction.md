# Water-Methanol Interface Surface Excess Thermodynamics from MD Simulation

## Problem background
Understanding the thermodynamic properties of liquid-vapor interfaces in associating fluid mixtures is important for many chemical and biological processes. Water-methanol mixtures are a model system where methanol acts as a simple surfactant, affecting surface tension and interfacial structure. Molecular dynamics simulations using empirical force fields can provide detailed information on surface excess quantities that are difficult to measure experimentally. This task reproduces such a simulation study for the water-methanol system across a range of compositions.

## Approach
The core idea is to simulate a liquid slab of water-methanol mixtures with explicit liquid-vapor interfaces using classical molecular dynamics. The TIP4P water model and TIPS methanol model are used to represent molecular interactions. For each composition, a rectangular simulation cell contains a slab of liquid surrounded by vapor, and the simulation is performed at constant temperature (NVT ensemble). From the generated trajectories, density and energy profiles across the interface are computed. The Gibbs dividing surface is defined by the condition that the total excess mass vanishes, and surface tension is obtained from the integral of the difference between the normal and tangential pressure components. Surface excess energy is then derived from the energy density profiles, and surface excess entropy follows from the relation *s*<sup>s</sup> = (*u*<sup>s</sup> – γ)/T. By comparing mixture results with pure component values, the mixing excess of surface excess energy and entropy can be determined. The key comparison is the deviation of these mixing excesses from zero, which indicates whether the interface is thermodynamically enriched or depleted relative to an ideal mixture.

## Reproduction target
Run molecular dynamics simulations for the nine compositions specified in the simulation step (methanol mole fractions *x*<sub>M</sub> = 0, 0.045, 0.089, 0.195, 0.275, 0.320, 0.468, 0.747, 1.0) and compute for each: surface tension γ, surface excess energy *u*<sup>s</sup>, surface excess entropy *s*<sup>s</sup>, mixing excess of *u*<sup>s</sup> (Δ*u*<sup>s</sup>), and mixing excess of *s*<sup>s</sup> (Δ*s*<sup>s</sup>). Report all results in the CSV file `/app/outputs/surface_excess_properties.csv` with the required columns. The primary target is to determine whether Δ*u*<sup>s</sup> and Δ*s*<sup>s</sup> for compositions with *x*<sub>M</sub> ≤ 0.3 are significantly different from zero, and whether they follow a consistent trend as a function of composition.

## Assets

- TIP4P water force field (Jorgensen et al., 1983): included in standard MD force field libraries (GROMACS, LAMMPS, OpenMM)
- TIPS methanol force field (Jorgensen, 1981): 10.1021/ja00415a004
- Open-source molecular dynamics package (GROMACS, LAMMPS, or OpenMM): https://www.gromacs.org / https://lammps.sandia.gov / https://openmm.org

## Workflow steps

### Step 1: Run molecular dynamics simulations
- Role: process
- Action: For nine compositions (methanol/water molecule counts from Table I: 0/1000, 50/950, 100/900, 200/800, 250/750, 300/700, 500/500, 750/250, 1000/0), set up a rectangular liquid slab with Lx=Ly as given in Table I and Lz=120 Å. Use TIP4P water and TIPS methanol potentials. Perform NVT MD at 300 K with a 0.5 fs timestep, Ewald summation for electrostatics, and a 14 Å short-range cutoff. Equilibrate for 20,000 steps, then collect trajectories of 100,000–175,000 steps. Save trajectory information for post-analysis.
- Evidence: `/app/outputs/trajectory_files.txt`

### Step 2: Compute surface excess properties
- Role: scored (load-bearing)
- Action: From the generated trajectories, compute mass density profiles and potential energy density profiles for each composition. Determine bulk liquid densities and locate the Gibbs dividing surface using the zero total excess mass condition. Calculate surface tension γ via the virial route (integral of P_N - P_T). Obtain surface excess energy u^s = (U - u^l V^l - u^g V^g)/A. Compute surface excess entropy s^s = (u^s - γ)/T at T = 300 K. For pure water and pure methanol endpoints, obtain u^s and s^s references. Calculate mixing excesses Δu^s(x_M) = u^s(mixture) – [x_M·u^s(pure methanol) + (1–x_M)·u^s(pure water)] and analogously Δs^s. Additionally, compute the methanol mole fraction in the outermost surface layer (vapor side, e.g., the 10‑90 layer) as outermost_x_M and include it in the output. Write all per-composition results to surface_excess_properties.csv.
- Output file: `/app/outputs/surface_excess_properties.csv`
- Format: csv
- Contract: CSV with header: x_M, gamma (mN/m), u_s (kJ/m^2), s_s (kJ/(m^2*K)), Delta_u_s (kJ/m^2), Delta_s_s (kJ/(m^2*K)), outermost_x_M. One row per composition. All numeric values as floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_excess_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_excess_properties.csv
- path: `/app/outputs/surface_excess_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Per-composition surface tension, surface excess energy, surface excess entropy, mixing excesses, and the methanol mole fraction in the outermost surface layer. The main verification is that for rows with x_M <= 0.3, both Delta_u_s and Delta_s_s are negative, and that for all rows with x_M > 0, outermost_x_M is high (>= 0.8), indicating surface saturation. The checker will additionally compare values to hidden reference tolerances.
- schema:
  - `type`: table
  - `required_columns`: `x_M`, `gamma (mN/m)`, `u_s (kJ/m^2)`, `s_s (kJ/(m^2*K))`, `Delta_u_s (kJ/m^2)`, `Delta_s_s (kJ/(m^2*K))`, `outermost_x_M`
  - `units`:
    - `x_M`: dimensionless mole fraction
    - `gamma (mN/m)`: mN/m
    - `u_s (kJ/m^2)`: kJ/m^2
    - `s_s (kJ/(m^2*K))`: kJ/(m^2*K)
    - `Delta_u_s (kJ/m^2)`: kJ/m^2
    - `Delta_s_s (kJ/(m^2*K))`: kJ/(m^2*K)
    - `outermost_x_M`: dimensionless mole fraction

Notes: The scored artifact must contain exactly one row for each of the nine compositions listed in the simulation step. The hidden checker will evaluate sign compliance for x_M <= 0.3, outer layer composition saturation, and perform accuracy checks against hidden reference values digitized from the paper's figures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_excess_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_M",
          "gamma (mN/m)",
          "u_s (kJ/m^2)",
          "s_s (kJ/(m^2*K))",
          "Delta_u_s (kJ/m^2)",
          "Delta_s_s (kJ/(m^2*K))",
          "outermost_x_M"
        ],
        "units": {
          "x_M": "dimensionless mole fraction",
          "gamma (mN/m)": "mN/m",
          "u_s (kJ/m^2)": "kJ/m^2",
          "s_s (kJ/(m^2*K))": "kJ/(m^2*K)",
          "Delta_u_s (kJ/m^2)": "kJ/m^2",
          "Delta_s_s (kJ/(m^2*K))": "kJ/(m^2*K)",
          "outermost_x_M": "dimensionless mole fraction"
        }
      },
      "description": "Per-composition surface tension, surface excess energy, surface excess entropy, mixing excesses, and the methanol mole fraction in the outermost surface layer. The main verification is that for rows with x_M <= 0.3, both Delta_u_s and Delta_s_s are negative, and that for all rows with x_M > 0, outermost_x_M is high (>= 0.8), indicating surface saturation. The checker will additionally compare values to hidden reference tolerances."
    }
  ],
  "notes": "The scored artifact must contain exactly one row for each of the nine compositions listed in the simulation step. The hidden checker will evaluate sign compliance for x_M <= 0.3, outer layer composition saturation, and perform accuracy checks against hidden reference values digitized from the paper's figures."
}
```

## How you are scored
A hidden verifier will read your CSV and evaluate it against reference values derived from independent computation. The scoring has two main components: (1) Accuracy of the reported quantities (γ, *u*<sup>s</sup>, *s*<sup>s</sup>, Δ*u*<sup>s</sup>, Δ*s*<sup>s</sup>) relative to reference tolerances; (2) Internal consistency, e.g., whether *s*<sup>s</sup> satisfies the thermodynamic relation *s*<sup>s</sup> = (*u*<sup>s</sup> – γ)/T within a small tolerance. For compositions with *x*<sub>M</sub> ≤ 0.3, the verifier also tests whether the mixing excesses are statistically distinguishable from zero, given expected simulation uncertainties. The final reward is a weighted sum of these checks. Simply returning the numbers from the original publication without actually running the simulation will not pass, because the verifier tolerances and consistency checks require physically plausible, self‑consistent values produced by a realistic MD workflow.
