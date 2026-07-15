# Grain boundary density deficit predicts excess free volume in BCC-Fe: reproduce linear collapse and entropy equivalence

## Problem background
Grain boundaries (GBs) are two-dimensional crystal defects that profoundly influence material properties such as strength, diffusivity, and segregation. A long‑standing approach to characterising GB disorder is through the nearest‑neighbour coordination number, which counts broken bonds at the interface. However, coordination numbers alone ignore local variations in interatomic spacing and volumetric distortion, which also contribute to excess free volume, energy, and configurational disorder.

An alternative descriptor is a coarse‑grained atomic density field, obtained by applying a three‑dimensional Gaussian smearing to the atomic positions. This field naturally encodes both neighbour multiplicities (topology) and interatomic distances (spacing), potentially offering a more complete characterisation of the grain boundary state than discrete coordination counts. In this work, such a density field is used to analyse a comprehensive set of 408 distinct BCC‑Fe grain boundaries that have been generated and relaxed by molecular statics. The aim is to quantify how well the density deficit and the coordination deficit each describe the grain boundary excess free volume, energy, and configurational entropy, and whether a density‑based Shannon entropy compactly captures the same disorder information as a combination of shell‑descriptor entropies.

## Approach
The experimental pipeline consists of two stages. First, 408 BCC‑Fe grain‑boundary bicrystals are constructed using the published geometry definitions (tilt, twist, and mixed boundaries) and relaxed to their ground‑state configuration at 0 K via conjugate‑gradient energy minimisation with an appropriate Fe embedded‑atom method potential for iron. From each relaxed configuration, the grain boundary energy and the excess free volume per unit area are extracted.

Second, the atomic density field is computed for every relaxed configuration by Gaussian smearing with a fixed smearing radius (β = 2.4 r_Fe, where r_Fe = 1.26 Å). The grain boundary plane is located as the minimum of the planar‑averaged density profile. At this plane, the density deficit (1 − ρ^GB) and the coordination deficit (8 − Z₁^GB)/8 are evaluated within a narrow slab of thickness 0.2 Å, where the first‑neighbour coordination numbers Z₁ are obtained from a bulk‑referenced radial distribution function cutoff. Effective shell weights for the first and second coordination shells are derived from the local atomic volumes, separating the topological (count) and distance (spacing) contributions.

Two independent configurational Shannon entropies per unit area are then computed: one directly from the spatial distribution of the atomic density field across the grain boundary (S_ρ^GB), and the other as the half‑sum of the four shell‑descriptor entropies (Z₁, φ₁, Z₂, φ₂). All per‑boundary scalars are collected in a single table for subsequent statistical analysis.

## Reproduction target
Produce a CSV file `gb_properties.csv` with exactly 408 rows, one for each grain boundary, and the following columns:

- `gb_id` (string): boundary identifier
- `rho_deficit` (float, dimensionless): density deficit (1 − ρ^GB)
- `coord_deficit` (float, dimensionless): coordination deficit (8 − Z₁^GB)/8
- `delta_V` (float, Å³/Å²): excess free volume per unit area
- `gamma_GB` (float, J/m²): grain boundary energy
- `S_rho` (float): density‑based configurational entropy per unit area
- `S_sum_half` (float): half‑sum of the four shell‑descriptor entropies per unit area

The hidden verifier will use this file to assess two key relationships:
- The linearity (Pearson correlation) between the excess free volume `delta_V` and the density deficit `rho_deficit`.
- The equivalence between the two entropy measures, quantified by the slope and intercept of a linear regression of `S_rho` against `S_sum_half`.

Your computational workflow must include both the molecular statics relaxations and the subsequent post‑processing that yields the required scalars.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- EAM potential for BCC Fe: https://www.ctcms.nist.gov/potentials/
- Atomsk polycrystal generation tool: https://atomsk.univ-lille.fr
- Grain boundary definitions from Ratanaphan et al. (2015): 10.1016/j.actamat.2015.01.005

## Workflow steps

### Step 1: Generate and relax 408 BCC-Fe grain boundaries
- Role: process
- Action: Using the grain boundary definitions from Ratanaphan et al. (2015) (DOI: 10.1016/j.actamat.2015.01.005), construct bicrystal configurations for all 408 boundaries (tilt, twist, mixed) and perform molecular statics relaxation at 0 K using the LAMMPS code with an appropriate Fe embedded-atom method (EAM) potential. Compute per-boundary grain boundary energy γ^GB and excess free volume ΔV per unit area from the relaxed configurations. Save all relaxed atomic configurations in a structured format (e.g., LAMMPS data or dump files) for subsequent analysis.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Compute grain-boundary descriptors and configurational entropies
- Role: scored (load-bearing)
- Action: From the relaxed atomic configurations, compute the coarse-grained atomic density field using Gaussian smearing with smearing radius β=2.4·r_Fe (r_Fe=1.26 Å). Determine the GB-plane location as the planar-averaged density minimum, evaluate the density deficit (1−ρ^GB) within a slab of thickness w=0.2 Å. Compute per-atom first (Z₁) and second (Z₂) coordination numbers from bulk radial distribution function cutoffs. For each atom, compute the coarse-grained density ρₙ at its position using Eq. (2) with β=2.4·r_Fe and derive the effective shell weight φ₂ for the second shell: obtain the local Voronoi volume for the second coordination shell to compute an effective radius \tilde{R}_2, then evaluate φ₂ = (exp(-(R_I - \tilde{R}_2)^2/(2β^2)))/(β√(2π))^3. Using the relation ρₙ ≈ Z₁ φ₁ + Z₂ φ₂, solve for φ₁: φ₁ ≈ (ρₙ - Z₂ φ₂) / Z₁. Compute the GB-plane average coordination deficit (8−Z₁^GB)/8. Compute Shannon configurational excess entropies S_ρ^GB and S_sum_half = ½(S_{Z₁}+S_{φ₁}+S_{Z₂}+S_{φ₂}) per unit area following the paper's method. Assemble all per-GB scalars into a single CSV file gb_properties.csv with columns: gb_id (string), rho_deficit (float, dimensionless), coord_deficit (float, dimensionless), delta_V (float, Å³/Å²), gamma_GB (float, J/m²), S_rho (float, configurational entropy units), S_sum_half (float, same units). Exactly 408 rows, one per grain boundary.
- Output file: `/app/outputs/gb_properties.csv`
- Format: csv
- Contract: CSV with columns: gb_id (string), rho_deficit (float), coord_deficit (float), delta_V (float, Å³/Å²), gamma_GB (float, J/m²), S_rho (float), S_sum_half (float). 408 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gb_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gb_properties.csv
- path: `/app/outputs/gb_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-grain-boundary scalar properties: density deficit, coordination deficit, excess free volume, GB energy, and configurational entropies. The checker computes Pearson correlation between delta_V and rho_deficit, and linear regression between S_rho and S_sum_half, comparing against hidden thresholds.
- schema:
  - `type`: table
  - `required_columns`: `gb_id`, `rho_deficit`, `coord_deficit`, `delta_V`, `gamma_GB`, `S_rho`, `S_sum_half`
  - `row_count`: 408

Notes: The hidden checker performs T1 recompute: it reads gb_properties.csv, computes the Pearson correlation r between delta_V and rho_deficit, and the slope/intercept of S_rho vs. S_sum_half, then scores against hidden gold values derived from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gb_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "gb_id",
          "rho_deficit",
          "coord_deficit",
          "delta_V",
          "gamma_GB",
          "S_rho",
          "S_sum_half"
        ],
        "row_count": 408
      },
      "description": "Per-grain-boundary scalar properties: density deficit, coordination deficit, excess free volume, GB energy, and configurational entropies. The checker computes Pearson correlation between delta_V and rho_deficit, and linear regression between S_rho and S_sum_half, comparing against hidden thresholds."
    }
  ],
  "notes": "The hidden checker performs T1 recompute: it reads gb_properties.csv, computes the Pearson correlation r between delta_V and rho_deficit, and the slope/intercept of S_rho vs. S_sum_half, then scores against hidden gold values derived from the paper."
}
```

## How you are scored
A hidden verifier reads your submitted `gb_properties.csv` and performs the following checks:

1. **Structural integrity** (low weight): The file contains exactly 408 rows, all required columns are present, and the columns contain numeric values of the expected type.
2. **Free‑volume – density deficit relationship** (highest weight): The verifier computes the Pearson correlation *r* between the `delta_V` and `rho_deficit` columns. It compares *r* against a hidden reference threshold derived from the paper’s reported near‑perfect linear collapse. Correlation at or above the threshold earns full credit; lower correlations receive proportionally less credit. (Better‑than‑paper is never penalised.)
3. **Entropy equivalence** (high weight): The verifier fits a linear model `S_rho = a * S_sum_half + b`. It checks that the slope *a* falls within a hidden interval around unity and that the intercept *b* is small. A slope within the acceptable range and a small intercept earn full credit; deviations are scored progressively lower.

The final reward is a weighted sum of these components, all monotonic in the quality of the reproduced relationships. Reporting plausible numbers that happen to match the paper’s values is not sufficient — the verifier’s credit curve rewards genuine reproduction of the underlying physical trends. Your task is to faithfully execute the described computational protocol so that your output accurately reflects those trends.
