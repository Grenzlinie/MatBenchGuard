# Compute Thermoelectric Figure of Merit in Topological Insulator Nanowires

## Problem background
Topological insulator nanowires made of Bi₂Te₃, Sb₂Te₃, and Bi₂Se₃ attract interest for thermoelectric energy conversion. When these materials are fabricated as nanowires, the large surface-to-volume ratio means that both a three-dimensional semiconducting bulk channel and two-dimensional topological surface states contribute to charge and heat transport. As the nanowire diameter is reduced from tens of microns down to nanometers, the surface contribution grows, and the two channels — each with its own dependence on the Fermi level — compete, potentially reshaping the total Seebeck coefficient, electrical and thermal conductivities, and the overall thermoelectric figure of merit ZT = S²σT/(κ_el + κ_ph). Understanding how the total ZT depends on diameter, and how the optimal Fermi level shifts, is essential for designing nanostructured thermoelectrics. This task computes these transport properties to determine the diameter‑dependent ZT and its optimal point for each material.

## Approach
The task implements a semiclassical Boltzmann transport model under constant relaxation-time approximation for a cylindrical topological insulator nanowire. Two parallel, non-interacting channels are considered: a three‑dimensional bulk channel modelled by a two‑band parabolic semiconductor (valence and conduction band separated by a band gap), and a two‑dimensional surface channel with a Dirac‑like dispersion that includes a curvature‑correcting effective mass and a finite‑size gap that scales inversely with diameter. Both channels’ transport coefficients (Seebeck coefficient S, electrical conductivity σ, electronic thermal conductivity κ_el, and figure of merit ZT) are computed as functions of the Fermi level E_F (measured from the bulk valence‑band edge) at T = 300 K, for each of the three materials Bi₂Te₃, Sb₂Te₃, and Bi₂Se₃. The material‑specific parameters (band gaps, effective masses, Fermi velocities, Dirac‑point offsets, and phonon thermal conductivities) are taken from the literature and will be given. The surface channel is evaluated both in a gapless (infinite‑diameter) limit and for a diameter of 10 nm. The total nanowire transport properties are then obtained by combining the bulk and surface contributions via parallel‑channel formulas that account for the surface‑to‑volume ratio s/v = 4/d and for the bulk phonon thermal conductivity, yielding total S, σ, κ, and ZT for a range of diameters. At each diameter the optimal Fermi level and the corresponding maximum ZT are identified.

## Reproduction target
Produce three scored CSV artifacts:
1. `/app/outputs/bulk_ZT_vs_EF.csv` – the bulk thermoelectric figure of merit ZT_b as a function of Fermi level E_F (in meV) for Bi₂Te₃, Sb₂Te₃, and Bi₂Se₃, scanned from –400 meV to +600 meV with a step of at most 1 meV.
2. `/app/outputs/surface_ZT_vs_EF.csv` – the surface ZT_s for the same three materials and the same Fermi‑level range, for two diameter cases: the gapless limit (labelled as `inf`) and d = 10 nm.
3. `/app/outputs/nanowire_ZT_opt.csv` – for each material and for the diameters 10, 50, 100, 500, 1000, and 10000 nm, report the maximum total ZT (ZT_opt) and the Fermi level at which it occurs (EF_opt_meV).
All calculations are carried out at 300 K.

## Assets

- NumPy: https://numpy.org/
- SciPy: https://scipy.org/

## Workflow steps

### Step 1: Compute bulk thermoelectric coefficients
- Role: scored
- Action: Implement the two-band parabolic band model and semiclassical Boltzmann transport under constant relaxation time for Bi2Te3, Sb2Te3, Bi2Se3 using given literature parameters (band gaps, effective masses, etc.). Compute the Seebeck coefficient, electrical conductivity, electronic thermal conductivity, and ZT_b as functions of Fermi level at 300 K over the range -400 to +600 meV with step ≤1 meV. Output a CSV file.
- Output file: `/app/outputs/bulk_ZT_vs_EF.csv`
- Format: csv
- Contract: Columns: material (string, one of Bi2Te3,Sb2Te3,Bi2Se3), EF_meV (float), ZT_b (float).
- Scoring: scored by hidden verifier

### Step 2: Compute surface thermoelectric coefficients
- Role: scored
- Action: Implement the Dirac-like surface dispersion with curvature and diameter-dependent gap (ΔE_s = 4 ħ v_F / d) using given surface parameters (Fermi velocity v_F, effective mass m*, Dirac point offsets ΔE_DP). Compute surface Seebeck coefficient, electrical conductivity, electronic thermal conductivity, and ZT_s as functions of Fermi level at 300 K for two cases: gapless (ΔE_s ≈ 0, labeled as diameter 'inf') and d=10 nm. Use the same Fermi level range and step. Output a CSV file.
- Output file: `/app/outputs/surface_ZT_vs_EF.csv`
- Format: csv
- Contract: Columns: material (string), diameter_nm (string, either 'inf' or '10'), EF_meV (float), ZT_s (float).
- Scoring: scored by hidden verifier

### Step 3: Compute total nanowire ZT and extract optima
- Role: scored (load-bearing)
- Action: Using the bulk and surface transport coefficients from previous steps, combine them via parallel-channel formulas accounting for surface-to-volume ratio s/v = 4/d and bulk phonon thermal conductivity κ_ph. For each material and for diameters d in {10, 50, 100, 500, 1000, 10000} nm, compute total ZT as a function of E_F and determine the maximum ZT (ZT_opt) and corresponding optimal Fermi level E_F_opt within the scanned range. Output a CSV file.
- Output file: `/app/outputs/nanowire_ZT_opt.csv`
- Format: csv
- Contract: Columns: material (string), diameter_nm (int), ZT_opt (float), EF_opt_meV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_ZT_vs_EF.csv`
- `/app/outputs/surface_ZT_vs_EF.csv`
- `/app/outputs/nanowire_ZT_opt.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_ZT_vs_EF.csv
- path: `/app/outputs/bulk_ZT_vs_EF.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Bulk ZT vs Fermi level for each material.
- schema:
  - `type`: table
  - `required_columns`: `material`, `EF_meV`, `ZT_b`

### surface_ZT_vs_EF.csv
- path: `/app/outputs/surface_ZT_vs_EF.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface ZT vs Fermi level for each material and diameter case.
- schema:
  - `type`: table
  - `required_columns`: `material`, `diameter_nm`, `EF_meV`, `ZT_s`

### nanowire_ZT_opt.csv
- path: `/app/outputs/nanowire_ZT_opt.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Optimal total nanowire ZT and corresponding Fermi level for each diameter and material.
- schema:
  - `type`: table
  - `required_columns`: `material`, `diameter_nm`, `ZT_opt`, `EF_opt_meV`

Notes: The hidden checker will extract the maximum ZT and corresponding Fermi levels from each CSV, compare against hidden paper-reported values with tolerances, and verify that ZT_opt at d=10 nm is less than ZT_opt at d=10 μm for each material (structural trend check).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_ZT_vs_EF.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "EF_meV",
          "ZT_b"
        ]
      },
      "description": "Bulk ZT vs Fermi level for each material."
    },
    {
      "file": "surface_ZT_vs_EF.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "diameter_nm",
          "EF_meV",
          "ZT_s"
        ]
      },
      "description": "Surface ZT vs Fermi level for each material and diameter case."
    },
    {
      "file": "nanowire_ZT_opt.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "diameter_nm",
          "ZT_opt",
          "EF_opt_meV"
        ]
      },
      "description": "Optimal total nanowire ZT and corresponding Fermi level for each diameter and material."
    }
  ],
  "notes": "The hidden checker will extract the maximum ZT and corresponding Fermi levels from each CSV, compare against hidden paper-reported values with tolerances, and verify that ZT_opt at d=10 nm is less than ZT_opt at d=10 μm for each material (structural trend check)."
}
```

## How you are scored
Your submission is scored by a hidden verifier that performs several checks.
- From your bulk and surface CSV files, the verifier extracts the maximum ZT and its corresponding Fermi level for each material (and for each surface diameter case) and compares them to concealed reference values with appropriate tolerances.
- From your nanowire_ZT_opt.csv, the verifier reads ZT_opt and EF_opt at each listed diameter and compares them to hidden reference data.
- Additionally, the verifier checks a mandatory structural trend: for every material, the optimal ZT at d = 10 nm must be lower than the optimal ZT at d = 10 µm.
Each scored artifact contributes a share of the final reward; the verifier combines the checks into a score between 0 and 1. Reporting the paper’s published numbers without performing the actual computation will not satisfy the verifier’s checks, because the tolerances and the structural test require a self-consistent, physics‑based model.
