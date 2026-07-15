# Chemomechanical Lithiation Model for Si@SiO2 Core-Shell Nanoparticles

## Problem background
Lithiation of silicon nanoparticles in lithium-ion battery anodes causes large volume expansion (~300%) and can lead to particle fracture, pulverization, and capacity fading. A thin surface oxide layer (SiO₂) grown on the Si nanoparticle can provide mechanical confinement that limits expansion, but it also restricts the extent of lithiation, potentially leaving a portion of the Si unlithiated. Understanding the trade-off between mechanical stability and capacity utilization is critical for designing high-performance Si-based composite anodes. This task investigates the chemo-mechanical coupling in a single spherical Si nanoparticle (30 nm diameter) covered by an amorphous SiO₂ shell of tunable thickness. The goal is to compute, from a physics-based model, the fraction of the Si core that remains unlithiated and the tensile hoop stress generated at the outer surface of the oxide layer as functions of the oxide thickness, for two different critical hydrostatic pressure thresholds that govern when lithiation arrests.

## Approach
The problem is treated with a coupled continuum diffusion-mechanics model for a spherically symmetric geometry. Lithium transport in the Si core is described by a nonlinear diffusion equation in which the effective diffusivity depends on both the local lithium concentration and the local hydrostatic pressure via an exponential relation, with a cap to maintain numerical stability. The mechanical response of the Si, the fully lithiated LiₓSi phase, and the SiO₂ shell is taken as elastic-perfectly plastic, using Young’s moduli, Poisson’s ratios, and yield stresses that are constant for each phase and interpolated linearly for partially lithiated Si. Lithiation-induced volumetric expansion is introduced as a composition-dependent chemical strain (expansion coefficients for Si and SiO₂). A key feature is the self‑limiting lithiation mechanism: when the hydrostatic compressive stress exceeds a prescribed critical threshold, further lithiation is assumed to stop. The model is run for a series of oxide shell thicknesses (1–10 nm) and for two critical pressure values (2.5 GPa and 4.0 GPa). For each combination, the simulation is advanced until lithiation arrests, and the volume fraction of unlithiated Si (Vᵘ/V₀) and the tensile hoop stress at the outermost surface of the oxide layer are recorded. The agent must implement a numerical solver (using any open‑source tool/library) that couples diffusion and mechanics within this framework and produces the final results as a CSV file.

## Reproduction target
Implement the coupled chemo-mechanical model described above for a 30 nm Si nanoparticle with an outer SiO₂ shell. Use the specified material parameters and the nonlinear diffusion law. For each oxide thickness t₀ = 1, 2, …, 10 nm, and for each critical hydrostatic pressure threshold σp^crit = 2.5 GPa and 4.0 GPa, run the simulation until lithiation arrests and extract: (i) the fraction of unlithiated Si (volume of unlithiated Si / initial Si volume), and (ii) the tensile hoop stress (in GPa) at the outermost surface of the oxide layer. Save all results in a single CSV file named `chemomechanical_results.csv`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Run chemomechanical simulations
- Role: scored (load-bearing)
- Action: Implement the coupled chemo-mechanical model for lithiation of a spherical Si nanoparticle (30 nm diameter) with an outer SiO₂ shell. Use the specified material parameters (Si: E=160 GPa, ν=0.24, σy=5 GPa; fully lithiated Si: E=40 GPa, ν=0.22, σy=1 GPa; SiOₓ: E=90 GPa, ν=0.17, σy=5 GPa; expansion coefficients β_Si=0.447, β_SiOₓ=0.3), nonlinear diffusivity D = D₀ exp[–σpΩ/(RT)(3.9c – 1/(1–c))] capped at 10⁴D₀, and critical hydrostatic pressure thresholds σp^crit = 2.5 and 4.0 GPa above which lithiation stops. For each oxide thickness t₀ = 1,2,…,10 nm and each critical pressure, compute the volume fraction of unlithiated Si (Vᵘ/V₀) and the tensile hoop stress at the outer surface of the oxide layer when lithiation arrests. Write all results to chemomechanical_results.csv.
- Output file: `/app/outputs/chemomechanical_results.csv`
- Format: csv
- Contract: columns: oxide_thickness_nm (float), critical_pressure_GPa (float), fraction_unlithiated (float, 0–1), hoop_stress_GPa (float). Rows: one per (t₀, σp^crit) combination, covering t₀=1..10 nm and σp^crit=2.5,4.0 GPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chemomechanical_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chemomechanical_results.csv
- path: `/app/outputs/chemomechanical_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the computed unlithiated Si fraction and tensile hoop stress at the oxide surface for each oxide thickness and critical pressure condition.
- schema:
  - `type`: table
  - `required_columns`: `oxide_thickness_nm`, `critical_pressure_GPa`, `fraction_unlithiated`, `hoop_stress_GPa`
  - `units`:
    - `oxide_thickness_nm`: nm
    - `critical_pressure_GPa`: GPa
    - `fraction_unlithiated`: dimensionless
    - `hoop_stress_GPa`: GPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chemomechanical_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "oxide_thickness_nm",
          "critical_pressure_GPa",
          "fraction_unlithiated",
          "hoop_stress_GPa"
        ],
        "units": {
          "oxide_thickness_nm": "nm",
          "critical_pressure_GPa": "GPa",
          "fraction_unlithiated": "dimensionless",
          "hoop_stress_GPa": "GPa"
        }
      },
      "description": "CSV containing the computed unlithiated Si fraction and tensile hoop stress at the oxide surface for each oxide thickness and critical pressure condition."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your `chemomechanical_results.csv`, extract the computed values at several specific oxide thicknesses for each critical pressure, and compare them to a hidden set of reference values. The comparison uses tolerances that account for numerical differences across implementations. The verifier also checks that the fraction of unlithiated Si increases monotonically with oxide thickness and that the hoop stress decreases monotonically with oxide thickness. Your reward is proportional to the fraction of check points that fall within tolerance and that satisfy the monotonicity conditions. Simply reporting a number (even the correct one) without actually running the simulation is not rewarded; the verifier expects the output of a genuine numerical computation.
