# Atomic-Scale Heterogeneity of a Multicomponent Bulk Metallic Glass: MD and EXAFS Analysis

## Problem background
Bulk metallic glasses (BMGs) can exhibit excellent glass forming ability (GFA), but the atomic-scale origin of GFA in multicomponent alloys remains an open question. In the Cu–Zr–Ag system, adding 10 at.% Ag to binary Cu50Zr50 dramatically improves GFA despite a positive heat of mixing for Cu–Ag, suggesting that chemical short- and medium-range order plays a decisive role. This work computationally investigates the atomic structure of Cu50Zr50, Cu45Zr45Ag10, and Cu40Zr40Ag20 metallic glasses to quantify the structural fingerprints—EXAFS spectral similarities, icosahedronlike cluster fractions, and Ag coordination—that underpin glass stability. Understanding these fingerprints could explain how minute Ag additions stabilize the liquid phase and enhance glass formation.

## Approach
The approach uses ab initio molecular dynamics (MD) simulations to generate glassy atomic configurations for three alloy compositions: Cu50Zr50, Cu45Zr45Ag10, and Cu40Zr40Ag20. Starting from known densities and a cubic box with periodic boundaries, each melt is quenched to room temperature, yielding structures that capture realistic short- and medium-range order. From these configurations, EXAFS k²χ(k) spectra are computed with FEFF8/9 for the Cu-K, Zr-K, and Ag-K absorption edges. A Voronoi tessellation analysis extracts the fractions of polyhedron types around each atomic species, with particular attention to Cu-centered icosahedronlike clusters (Voronoi index <0 2 8 1>). Additionally, the average number of Ag–Ag nearest neighbors is derived to assess whether Ag atoms tend to pair or form strings. By comparing the three compositions, one can isolate the effect of Ag addition on the local environments of Cu, Zr, and Ag, and quantify the structural heterogeneity that correlates with improved GFA.

## Reproduction target
Produce the atomic-scale structural analysis for Cu50Zr50, Cu45Zr45Ag10, and Cu40Zr40Ag20. Specifically:
1. Run MD simulations and save the final relaxed configurations.
2. Compute EXAFS spectra k²χ(k) for the Cu‑K, Zr‑K, and Ag‑K edges and store them as specified.
3. Perform Voronoi tessellation and output the polyhedron fractions for each center type (Cu, Zr, Ag).
4. Compute the average Ag–Ag coordination number for the two Ag‑containing alloys.
The artifacts should allow independent verification of these trends across the three compositions: (i) the Cu‑K EXAFS of Cu50Zr50 and Cu45Zr45Ag10 are nearly identical while their Zr‑K spectra differ noticeably; (ii) the fraction of Cu‑centered <0 2 8 1> icosahedronlike clusters is larger in Cu45Zr45Ag10 than in Cu50Zr50; (iii) the average Ag–Ag coordination number exceeds 1 for both Cu45Zr45Ag10 and Cu40Zr40Ag20, indicating Ag pairing/strings. Reproduce these relative trends, not any single absolute numerical value, through genuine MD simulation and analysis.

## Assets

- FEFF8/9 EXAFS calculation software: https://feffproject.org/feff/
- Open-source MD engine (CP2K or equivalent): https://www.cp2k.org/
- OVITO (or custom Voronoi code): https://www.ovito.org/
- Alloy mass densities from literature: 10.2320/matertrans.47.1922

## Workflow steps

### Step 1: MD simulation of glass formation
- Role: process
- Action: For each of the three compositions (Cu50Zr50, Cu45Zr45Ag10, Cu40Zr40Ag20), set up an MD simulation of approximately 250 atoms in a cubic box with periodic boundary conditions. Melt at 2500 K for 2000 steps (5 fs per step), quench to 300 K at a cooling rate of ~4×10¹³ K·s⁻¹, and relax. Use an open-source ab initio MD code (e.g., CP2K) or a validated classical potential. Save the final relaxed atomic configurations.
- Evidence: `/app/outputs/md_summary.txt`

### Step 2: Compute EXAFS spectra
- Role: scored (load-bearing)
- Action: From the final atomic configurations of step_0, calculate EXAFS k²χ(k) for the Cu K, Zr K, and Ag K edges using FEFF8/9. Generate spectra for each composition and edge, covering the k range ~2–12 Å⁻¹.
- Output file: `/app/outputs/step_01_exafs_data.json`
- Format: json
- Contract: JSON object with keys: Cu50Zr50_Cu_K, Cu50Zr50_Zr_K, Cu45Zr45Ag10_Cu_K, Cu45Zr45Ag10_Zr_K, Cu45Zr45Ag10_Ag_K, Cu40Zr40Ag20_Cu_K, Cu40Zr40Ag20_Zr_K, Cu40Zr40Ag20_Ag_K. Each value contains arrays 'k' (float, Å⁻¹) and 'chi' (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 3: Voronoi tessellation analysis
- Role: scored
- Action: Perform Voronoi tessellation on the final atomic configurations from step_0 to identify topological short-range order. For each composition and for each center type (Cu, Zr, Ag), compute the fraction of each Voronoi index among the polyhedra.
- Output file: `/app/outputs/step_02_voronoi_statistics.csv`
- Format: csv
- Contract: CSV with columns: composition (str, e.g., 'Cu50Zr50'), center_type (str, one of 'Cu','Zr','Ag'), voronoi_index (str, e.g., '<0 2 8 1>'), fraction (float between 0 and 1). List all center types and dominant indices per composition.
- Scoring: scored by hidden verifier

### Step 4: Ag–Ag coordination numbers
- Role: scored
- Action: From the Voronoi neighbor analysis, compute the average number of Ag nearest neighbors for each Ag atom (Ag–Ag coordination). Report the result for Cu45Zr45Ag10 and Cu40Zr40Ag20.
- Output file: `/app/outputs/step_03_ag_coordination.json`
- Format: json
- Contract: JSON object with keys 'Cu45Zr45Ag10' and 'Cu40Zr40Ag20'. Each value is a float representing the average Ag–Ag coordination number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_exafs_data.json`
- `/app/outputs/step_02_voronoi_statistics.csv`
- `/app/outputs/step_03_ag_coordination.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_exafs_data.json
- path: `/app/outputs/step_01_exafs_data.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: EXAFS spectra for the three alloys at the Cu-K, Zr-K, and Ag-K absorption edges. The checker will compute correlation coefficients and peak splitting indicators to verify the atomic-scale heterogeneity.
- schema:
  - `type`: object
  - `required`:
    - `Cu50Zr50_Cu_K`:
      - `k`: array of float
      - `chi`: array of float
    - `Cu50Zr50_Zr_K`:
      - `k`: array of float
      - `chi`: array of float
    - `Cu45Zr45Ag10_Cu_K`:
      - `k`: array of float
      - `chi`: array of float
    - `Cu45Zr45Ag10_Zr_K`:
      - `k`: array of float
      - `chi`: array of float
    - `Cu45Zr45Ag10_Ag_K`:
      - `k`: array of float
      - `chi`: array of float
    - `Cu40Zr40Ag20_Cu_K`:
      - `k`: array of float
      - `chi`: array of float
    - `Cu40Zr40Ag20_Zr_K`:
      - `k`: array of float
      - `chi`: array of float
    - `Cu40Zr40Ag20_Ag_K`:
      - `k`: array of float
      - `chi`: array of float

### step_02_voronoi_statistics.csv
- path: `/app/outputs/step_02_voronoi_statistics.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Voronoi polyhedra fractions for each composition and center type. The checker will verify that the fraction of Cu-centered <0 2 8 1> icosahedronlike clusters is higher in Cu45Zr45Ag10 than in Cu50Zr50.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `center_type`, `voronoi_index`, `fraction`
  - `units`:
    - `fraction`: none

### step_03_ag_coordination.json
- path: `/app/outputs/step_03_ag_coordination.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Average number of Ag nearest neighbors for each Ag atom. The checker will confirm that the average coordination number exceeds 1.0 for both alloys, demonstrating Ag pairing/strings.
- schema:
  - `type`: object
  - `required`:
    - `Cu45Zr45Ag10`: float
    - `Cu40Zr40Ag20`: float
  - `units`:
    - `Cu45Zr45Ag10`: dimensionless
    - `Cu40Zr40Ag20`: dimensionless

Notes: All outputs are produced from the MD-derived configurations. The checker recomputes metrics (e.g., correlations, trend comparisons, threshold checks) from these artifacts; hidden reference values and tolerances are applied to verify the paper's claims about selective replacement and atomic-scale heterogeneity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_exafs_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "Cu50Zr50_Cu_K": {
            "k": "array of float",
            "chi": "array of float"
          },
          "Cu50Zr50_Zr_K": {
            "k": "array of float",
            "chi": "array of float"
          },
          "Cu45Zr45Ag10_Cu_K": {
            "k": "array of float",
            "chi": "array of float"
          },
          "Cu45Zr45Ag10_Zr_K": {
            "k": "array of float",
            "chi": "array of float"
          },
          "Cu45Zr45Ag10_Ag_K": {
            "k": "array of float",
            "chi": "array of float"
          },
          "Cu40Zr40Ag20_Cu_K": {
            "k": "array of float",
            "chi": "array of float"
          },
          "Cu40Zr40Ag20_Zr_K": {
            "k": "array of float",
            "chi": "array of float"
          },
          "Cu40Zr40Ag20_Ag_K": {
            "k": "array of float",
            "chi": "array of float"
          }
        }
      },
      "description": "EXAFS spectra for the three alloys at the Cu-K, Zr-K, and Ag-K absorption edges. The checker will compute correlation coefficients and peak splitting indicators to verify the atomic-scale heterogeneity."
    },
    {
      "file": "step_02_voronoi_statistics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "center_type",
          "voronoi_index",
          "fraction"
        ],
        "units": {
          "fraction": "none"
        }
      },
      "description": "Voronoi polyhedra fractions for each composition and center type. The checker will verify that the fraction of Cu-centered <0 2 8 1> icosahedronlike clusters is higher in Cu45Zr45Ag10 than in Cu50Zr50."
    },
    {
      "file": "step_03_ag_coordination.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Cu45Zr45Ag10": "float",
          "Cu40Zr40Ag20": "float"
        },
        "units": {
          "Cu45Zr45Ag10": "dimensionless",
          "Cu40Zr40Ag20": "dimensionless"
        }
      },
      "description": "Average number of Ag nearest neighbors for each Ag atom. The checker will confirm that the average coordination number exceeds 1.0 for both alloys, demonstrating Ag pairing/strings."
    }
  ],
  "notes": "All outputs are produced from the MD-derived configurations. The checker recomputes metrics (e.g., correlations, trend comparisons, threshold checks) from these artifacts; hidden reference values and tolerances are applied to verify the paper's claims about selective replacement and atomic-scale heterogeneity."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. For the EXAFS data, it computes correlation coefficients between the spectra of different compositions and checks for characteristic spectral features (e.g., peak splitting). For the Voronoi statistics, it compares the fraction of the <0 2 8 1> icosahedronlike clusters across the three alloys. For the Ag coordination output, it verifies that the average number of Ag–Ag neighbors surpasses a threshold indicative of pairing. Each check is combined with appropriate tolerances to absorb legitimate run-to-run variation (different MD implementations, functional choices, or random seeds). The final reward is a weighted combination of these stage-level checks; simply reporting a number without executing the workflow will not satisfy the verifier. The computations you perform and the artifacts you submit must be internally consistent and exhibit the structural trends described in the target.
