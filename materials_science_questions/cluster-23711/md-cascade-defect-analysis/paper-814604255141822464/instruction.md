# 1D Rate-Theory Calculation of Interstitial-Starvation Width in SiC

## Problem background
Silicon carbide (SiC) is a candidate material for nuclear applications, but it is susceptible to radiation-induced amorphization (RIA). Grain boundaries (GBs) influence RIA through two competing effects: they act as sinks that remove defects (improving resistance), but they can also enhance amorphization locally via **interstitial starvation**. This occurs when highly mobile interstitials are preferentially absorbed by GBs, leaving behind an excess of less mobile vacancies. A one-dimensional rate-theory model (reaction-diffusion) predicts the vacancy accumulation near GBs and defines the spatial extent of the zone where amorphization is promoted. This task reproduces that calculation to determine how far from a GB the excess energy profile is above specific threshold values that indicate enhanced amorphization risk.

## Approach
A 1D rate-theory model tracks four defect species (Si interstitial, Si vacancy, C interstitial, C vacancy) along the width of a single grain bounded by two GBs. Each species n obeys a diffusion-reaction equation:

- diffusion term: D_n * d²c_n/dx²
- generation: G_n = Γ * η * α_n, where Γ = 6.48×10⁻⁴ dpa/s (dose rate), η = 0.8 (intracascade recombination fraction), and α_n is the generation fraction for species n.
- recombination: R * c_i(x) * c_v(x), where the reaction rate R depends on the Frenkel pair type.

Parameter values (from ab initio studies) are:
- Si interstitial diffusivity D = 2.08×10⁻¹⁴ cm²/s, migration barrier E_m = 0.83 eV; Si vacancy D = 2.70×10⁻³⁶ cm²/s, E_m = 2.40 eV; C interstitial D = 1.09×10⁻¹² cm²/s, E_m = 0.60 eV; C vacancy D = 2.47×10⁻⁵³ cm²/s, E_m = 3.66 eV.
- Generation fractions: α_{Si_I}=0.075, α_{Si_V}=0.925, α_{C_I}=0.435, α_{C_V}=0.565.
- For Si Frenkel pairs, the recombination barrier E_r = 0.03 eV is much smaller than the interstitial migration barrier, so the reaction is barrierless: R = 4π r_c (D_i + D_v) with r_c = 0.63 nm.
- For C Frenkel pairs, the interstitial migration barrier (0.60 eV) is comparable to or smaller than the recombination barrier (E_r = 0.90 eV), so R = 4π r_c (D_i + D_v) * exp((E_m^fast - E_r)/k_B T), with r_c = 0.21 nm and E_m^fast = 0.60 eV.

The system is at temperature T = 100 °C (≈373 K). The grain size is 1 μm; the two GBs are at x = 0 and x = 1000 nm. Defect concentrations are set to zero at the GBs throughout the simulation, and initial (t=0) concentrations are zero everywhere. Irradiation runs for 1040 s (dose 0.675 dpa). The steady-state defect concentrations are solved numerically.

From the steady-state solution, compute the excess energy per atom: ΔE(x) = Σ ΔE_n * c_n(x), where ΔE_n are the formation energies: ΔE_{Si_I}=8.745 eV, ΔE_{Si_V}=4.966 eV, ΔE_{C_I}=6.953 eV, ΔE_{C_V}=4.193 eV (energy gain per introduced defect). The resulting spatial profile ΔE(x) shows a peak near the GBs and decays toward the grain interior. Regions where ΔE exceeds the critical energy for amorphization are predicted to amorphize. From the profile, determine the distance from the grain boundary at which ΔE first falls below 0.6 eV/atom (the amorphization threshold) and below 0.3 eV/atom (half of that threshold).

## Reproduction target
Produce two scored outputs:

1. A CSV file (`excess_energy_profile.csv`) containing the steady-state excess energy profile ΔE(x) for x from 0 to 1000 nm (at least 100 uniformly spaced points). Columns: `x_nm` (position from one GB in nm), `DeltaE_eV_per_atom` (excess energy per atom in eV/atom).

2. A JSON file (`distances.json`) containing the distances from the grain boundary at which ΔE first drops below the two thresholds. Because the profile is symmetric, report the distance from the left boundary (x=0) where the profile falls below 0.6 eV/atom (the amorphization threshold) and below 0.3 eV/atom (the half-threshold). The JSON object should be: {"distance_to_amorphization_nm": <float>, "distance_to_half_amorphization_nm": <float>}.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Solve rate-theory equations and compute excess energy profile
- Role: scored (load-bearing)
- Action: Implement a steady-state 1D reaction-diffusion solver for four defect species (Si and C interstitials and vacancies) with generation rate G = Γ·η·αₙ (Γ=6.48×10⁻⁴ dpa/s, η=0.8) and recombination rates as described in the problem statement (barrierless for Si pairs, exponential barrier for C pairs). Use the provided defect diffusivities, reaction barriers, and formation energies. Set grain size 1 μm, temperature 100 °C, irradiation time 1040 s (0.675 dpa). Boundary conditions: defect concentrations = 0 at grain boundaries (x=0 and x=1000 nm); initial concentrations zero. Compute the steady-state excess energy per atom profile ΔE(x) = Σ ΔEₓ·cₓ(x) and write to excess_energy_profile.csv with columns x_nm and DeltaE_eV_per_atom, at least 100 uniformly spaced points over 0–1000 nm.
- Output file: `/app/outputs/excess_energy_profile.csv`
- Format: csv
- Contract: CSV with columns: x_nm (float, position from GB in nm, range 0–1000), DeltaE_eV_per_atom (float, excess energy). At least 100 uniformly spaced points.
- Scoring: scored by hidden verifier

### Step 2: Extract distances to amorphization thresholds
- Role: scored
- Action: From excess_energy_profile.csv, determine the distances from the grain boundary at which ΔE first drops below 0.6 eV/atom (amorphization threshold) and 0.3 eV/atom (half-threshold). Output these two distances in a JSON file.
- Output file: `/app/outputs/distances.json`
- Format: json
- Contract: JSON object: {"distance_to_amorphization_nm": <float>, "distance_to_half_amorphization_nm": <float>}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/excess_energy_profile.csv`
- `/app/outputs/distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### excess_energy_profile.csv
- path: `/app/outputs/excess_energy_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spatial profile of excess energy per atom computed from the 1D rate-theory model. Checker verifies column types, coverage, peak near boundaries, and that the profile can be used to extract threshold distances.
- schema:
  - `type`: table
  - `required_columns`: `x_nm`, `DeltaE_eV_per_atom`
  - `units`:
    - `x_nm`: nm
    - `DeltaE_eV_per_atom`: eV/atom

### distances.json
- path: `/app/outputs/distances.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Distances from grain boundary where ΔE reaches the amorphization threshold (0.6 eV/atom) and half-threshold (0.3 eV/atom). Checker recomputes these from the submitted profile and compares with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `distance_to_amorphization_nm`: float
    - `distance_to_half_amorphization_nm`: float
  - `units`:
    - `distance_to_amorphization_nm`: nm
    - `distance_to_half_amorphization_nm`: nm

Notes: The checker recomputes the distances from the excess energy profile and compares them to the paper-reported gold values (hidden) with a tolerance that accounts for numerical solver spread. The profile itself is verified for structural correctness before distances are extracted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "excess_energy_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_nm",
          "DeltaE_eV_per_atom"
        ],
        "units": {
          "x_nm": "nm",
          "DeltaE_eV_per_atom": "eV/atom"
        }
      },
      "description": "Spatial profile of excess energy per atom computed from the 1D rate-theory model. Checker verifies column types, coverage, peak near boundaries, and that the profile can be used to extract threshold distances."
    },
    {
      "file": "distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "distance_to_amorphization_nm": "float",
          "distance_to_half_amorphization_nm": "float"
        },
        "units": {
          "distance_to_amorphization_nm": "nm",
          "distance_to_half_amorphization_nm": "nm"
        }
      },
      "description": "Distances from grain boundary where ΔE reaches the amorphization threshold (0.6 eV/atom) and half-threshold (0.3 eV/atom). Checker recomputes these from the submitted profile and compares with tolerances."
    }
  ],
  "notes": "The checker recomputes the distances from the excess energy profile and compares them to the paper-reported gold values (hidden) with a tolerance that accounts for numerical solver spread. The profile itself is verified for structural correctness before distances are extracted."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines the two output files:

- **Profile structural audit**: The verifier checks that `excess_energy_profile.csv` has the correct columns, covers the full 0–1000 nm range with at least 100 uniformly spaced points, and shows the expected qualitative behaviour (ΔE highest at the grain boundaries and decaying toward the grain interior).
- **Threshold distance recomputation**: The verifier reads your profile, interpolates to find the first x from the boundary where ΔE drops below 0.6 eV/atom and 0.3 eV/atom, and compares these distances against benchmark values derived from the scientific literature. A tolerance is applied to account for differences in numerical solvers and discretisation.
- **Distances.json consistency**: The verifier also reads your `distances.json` and verifies that the reported distances match those recomputed from your own profile to within numerical precision.

The final reward (a float between 0 and 1) is a weighted combination of the profile structural correctness and the agreement of the threshold distances. Accurate distances carry the largest weight. Simply reporting numbers—without a valid underlying profile that produces them—does not score well.
