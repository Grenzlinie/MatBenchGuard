# Substitutional segregation enthalpies of trivalent dopants in an Al2O3 Σ13 grain boundary

## Problem background
In α-Al₂O₃, oversized trivalent isovalent dopants (e.g., Y, La) strongly segregate to grain boundaries, suppressing grain-boundary diffusion and reducing tensile creep rates by orders of magnitude. The driving force for this segregation is believed to be the elastic strain energy associated with the size mismatch between the dopant and the host Al³⁺ ion. Characterizing the free volume near grain boundaries and computing the segregation enthalpies for various dopants and site types is essential to quantify this relationship and to design effective doping strategies for enhanced creep resistance. This task computes the zero-temperature relaxed substitutional segregation enthalpies for four trivalent cations (Fe³⁺, Yb³⁺, Eu³⁺, La³⁺) at three distinct types of Al sites within a Σ13 [0001] tilt grain boundary.

## Approach
We use atomistic simulations with empirical pair potentials and the shell model to describe interatomic interactions in Al₂O₃ and the dopant oxides. The short-range interactions are modeled by Born–Mayer repulsive and van der Waals attractive terms, with long-range Coulomb forces treated by Ewald summation. The host Al₂O₃ is described with parameters from Catlow et al., while dopant–oxygen interactions are taken from Bush et al. A Σ13 coincidence-site lattice boundary with a [0001] rotation axis is constructed and relaxed to its ground-state configuration using conjugate-gradient energy minimization. The free volume at the grain boundary is quantified by constructing Voronoi polyhedra around cation sites, measuring the average distance to the nearest oxygen faces relative to the bulk value (d/db). Three specific substitutional sites with distinct d/db values (1.067, 1.018, 0.9813) are identified as representative large, intermediate, and small sites. For each dopant and each site type, the substitutional segregation enthalpy ΔH is computed as the difference in relaxed energies: ΔH = E_doped_gb + E_bulk_pure − E_pure_gb − E_doped_bulk, where all energies are obtained from the relaxed supercell calculations. Bulk reference energies for pure Al₂O₃ and each dopant substituting Al are also computed. This allows an investigation of how ΔH depends on ionic radius mismatch (Δr) and site size.

## Reproduction target
Compute the relaxed substitutional segregation enthalpies ΔH (in eV) for Fe³⁺, Yb³⁺, Eu³⁺, and La³⁺ substituting Al³⁺ at the three grain-boundary site types (type 1: d/db=1.067, type 2: d/db=1.018, type 3: d/db=0.9813) of a relaxed Σ13 [0001] tilt boundary in α-Al₂O₃. Produce a CSV file with columns dopant, site_type, and dH. Additionally, verify that for the largest site type (type 1) ΔH scales with (Δr)² for the four dopants, and that for the smallest site type (type 3) ΔH is positive for the oversized dopants (Yb³⁺, Eu³⁺, La³⁺). These trends are to be verified by the scoring mechanism, not reported in the CSV.

## Assets

- GULP (General Utility Lattice Program): http://gulp.curtin.edu.au/download.html
- Empirical pair potential parameters for α-Al₂O₃ (Catlow et al.): 10.1103/PhysRevB.25.1006
- Empirical pair potential parameters for M₂O₃ dopants (Bush et al.): 10.1039/JM9940400831
- Ionic radii of trivalent cations (Shannon)
- Crystal structure of α-Al₂O₃ (corundum)

## Workflow steps

### Step 1: Construct Σ13 [0001] tilt grain boundary supercell
- Role: process
- Action: Build the initial atomic configuration of a Σ13 coincidence‑site lattice boundary with [0001] rotation axis, rotation angle 27.80°, supercell dimensions 1×1×4, containing two grain boundaries and 3120 ions, periodic in three dimensions.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: Relax the pure Σ13 boundary structure
- Role: process
- Action: Minimise the total energy of the pure Al₂O₃ supercell using the Catlow et al. pair potentials and shell model with Ewald summation, via conjugate‑gradient relaxation until forces are minimised, keeping in‑plane dimensions fixed. The relaxed core positions define the reference boundary structure.
- Evidence: `/app/outputs/relaxed_boundary.xyz`

### Step 3: Identify substitutional site types by Voronoi analysis
- Role: process
- Action: Perform a Voronoi polyhedron construction on the cation (Al³⁺) positions from the relaxed pure‑boundary coordinates. For each substitutional site compute the average distance to the six nearest oxygen faces relative to the bulk distance d/db. Identify three distinct Al sites whose relative radii match 1.067, 1.018, and 0.9813 (site types 1,2,3). Output the indices/coordinates of these sites.
- Evidence: `/app/outputs/site_indices.txt`

### Step 4: Compute segregation enthalpies and output CSV
- Role: scored (load-bearing)
- Action: For each of the four trivalent dopants (Fe³⁺, Yb³⁺, Eu³⁺, La³⁺) and each of the three identified site types, compute the relaxed substitutional segregation enthalpy ΔH = E_doped_gb + E_bulk_pure - E_pure_gb - E_doped_bulk. Use dopant‑oxygen interaction parameters from Bush et al., and compute the required bulk reference energies (perfect bulk Al₂O₃ and each dopant substituting Al in bulk) with the same potentials. Perform ionic relaxation for each doped configuration. Output a CSV file with columns: dopant, site_type, dH.
- Output file: `/app/outputs/segregation_enthalpies.csv`
- Format: csv
- Contract: dopant (string), site_type (int 1,2,3), dH (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/segregation_enthalpies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### segregation_enthalpies.csv
- path: `/app/outputs/segregation_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relaxed substitutional segregation enthalpy ΔH for each dopant (Fe,Yb,Eu,La) at three site types (1‑largest, 2‑intermediate, 3‑smallest) in the Σ13 boundary. The checked scoring includes value‑level comparison to reference, a linear trend of ΔH vs (Δr)² for site_type=1, and the sign condition ΔH > ‑0.1 eV for oversized dopants at site_type=3.
- schema:
  - `type`: table
  - `required_columns`: `dopant`, `site_type`, `dH`
  - `units`:
    - `dH`: eV

Notes: The checker will compare each ΔH value to known reference data (within tolerance), perform a linear regression of ΔH on (Δr)² for site_type=1 points and verify a negative slope with R²>0.95, and check that for site_type=3 the enthalpy for Yb, Eu, La is > −0.1 eV. The ionic radii for (Δr)² calculation are taken from the provided Shannon table.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "segregation_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dopant",
          "site_type",
          "dH"
        ],
        "units": {
          "dH": "eV"
        }
      },
      "description": "Relaxed substitutional segregation enthalpy ΔH for each dopant (Fe,Yb,Eu,La) at three site types (1‑largest, 2‑intermediate, 3‑smallest) in the Σ13 boundary. The checked scoring includes value‑level comparison to reference, a linear trend of ΔH vs (Δr)² for site_type=1, and the sign condition ΔH > ‑0.1 eV for oversized dopants at site_type=3."
    }
  ],
  "notes": "The checker will compare each ΔH value to known reference data (within tolerance), perform a linear regression of ΔH on (Δr)² for site_type=1 points and verify a negative slope with R²>0.95, and check that for site_type=3 the enthalpy for Yb, Eu, La is > −0.1 eV. The ionic radii for (Δr)² calculation are taken from the provided Shannon table."
}
```

## How you are scored
Your submission is judged by a hidden verifier that reads `/app/outputs/segregation_enthalpies.csv`. The verifier performs the following checks, each contributing a portion of the total reward:
- Individual value match: each ΔH in the CSV is compared to reference values within a tolerance. A value that is too far from the reference degrades the score.
- Linear trend: for site_type=1, the verifier computes a linear regression of ΔH against (Δr)² using the provided Shannon ionic radii. It checks that the slope is negative and the coefficient of determination (R²) exceeds a high threshold.
- Sign condition: for site_type=3, the verifier checks that ΔH is positive for Yb, Eu, and La.
The exact tolerance and thresholds are hidden. The reward is a weighted combination of these checks; simply reporting approximate numbers is not sufficient — the values must be produced by a genuine atomistic simulation workflow as described in the preceding steps.
