# Piezoelectric superlattice shear horizontal wave dispersion and effective constants

## Problem background
Superlattices composed of alternating piezoelectric layers (e.g., CdS and ZnO, hexagonal 6mm symmetry) can support shear horizontal (SH) acoustic waves that couple to the electric field. This coupling leads to novel dispersion features and surface modes (Bleustein‑Gulyaev waves) that have no elastic-only analogue. Understanding the bulk band structure and surface wave existence is important for acoustic devices. This task reproduces the computation of bulk SH wave band edges, surface wave phase velocities, and long-wavelength effective constants for a CdS–ZnO piezoelectric superlattice.

## Approach
The core method is a transfer matrix formalism for SH waves. The layers are hexagonal 6mm crystals with their c-axis along x₃, the superlattice normal along x₁, and propagation along x₂. The governing equations couple the transverse displacement U₃ to the electric potential φ. With harmonic time dependence and a Bloch wave ansatz, the fields in each layer are expressed in terms of four unknown coefficients. Applying elastic and electric boundary conditions at the interfaces links the coefficients in successive cells via a 4×4 transfer matrix T. Bulk waves propagate when the eigenvalues of T have unit magnitude; band edges are located by scanning frequency ω for a given reduced wavenumber k∥D. Surface waves correspond to eigenvalues with a positive imaginary part (decaying into the bulk), with the surface dispersion solved from determinantal conditions appropriate to metallized or non-metallized electrical boundaries. In the long-wavelength limit, the superlattice behaves as an effective homogeneous medium whose constants are obtained by averaging appropriate combinations of the constituent material parameters, accounting for the layer thickness fractions. The provided material constants (CdS and ZnO) are sufficient to implement this scheme without any external data.

## Reproduction target
Compute and output the following: (1) Bulk band edges: for a CdS–ZnO superlattice with equal layer thicknesses, produce the lower and upper frequencies of the first two SH bulk bands as functions of reduced wavenumber k∥D ∈ [0, π] (dimensionless frequencies Ω = ω·D/(2π·C_t(CdS)), where C_t(CdS) = √(C₄₄(CdS)/ρ(CdS))). (2) Surface wave phase velocities: for the same superlattice, compute the phase velocity (in units of C_t(CdS)) of Bleustein–Gulyaev waves below the lowest bulk band at selected k∥D = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0] for a CdS top layer under non‑metallized and metallized boundary conditions, and for a ZnO top layer under metallized conditions. (3) Effective medium constants: in the long-wavelength limit (equal layer thicknesses, volume fraction x=0.5), determine the effective elastic constant C₄₄^eff (10^10 N/m²), piezoelectric constant e₁₅^eff (C/m²), and dielectric constant ε₁₁^eff (10⁻¹¹ F/m).

## Assets

- CdS and ZnO material parameters

## Workflow steps

### Step 1: Compute bulk SH wave band edges
- Role: scored (load-bearing)
- Action: Implement the transfer matrix T for shear horizontal (SH) waves in a piezoelectric superlattice composed of hexagonal 6mm crystals, with c-axis along x₃, superlattice normal along x₁, and propagation along x₂. Use the provided material parameters of CdS and ZnO and assume equal layer thicknesses (h = h'). Compute the bulk band edges for the first two bands: for a range of reduced wavenumber k∥D from 0 to π (at least 100 evenly spaced points), scan frequency ω to find the boundaries where bulk waves propagate (i.e., |cos(k₁D)| ≤ 1). Record the lower and upper band edges as dimensionless frequencies Ω = ω·D / (2π·C_t(CdS)), where C_t(CdS) = √(C₄₄(CdS)/ρ(CdS)).
- Output file: `/app/outputs/bulk_band_edges.csv`
- Format: csv
- Contract: Columns: k_parallel_D (float), band1_lower (float, dimensionless Ω), band1_upper (float, dimensionless Ω), band2_lower (float, dimensionless Ω), band2_upper (float, dimensionless Ω).
- Scoring: scored by hidden verifier

### Step 2: Compute surface wave phase velocities
- Role: scored (load-bearing)
- Action: Using the same transfer matrix and superlattice parameters, compute the eigenvectors corresponding to eigenvalues with a positive imaginary part (decaying into the bulk). Solve the surface wave dispersion relations: for a CdS top layer compute surface wave frequencies below the lowest bulk band for both non-metallized (3×3 determinant) and metallized (2×2 determinant) boundary conditions; for a ZnO top layer compute only the metallized case (the non-metallized case is too close to the bulk band to distinguish). Evaluate at the selected k∥D values [0.1, 0.5, 1.0, 2.0, 5.0, 10.0] and convert frequencies to phase velocities in units of C_t(CdS) = √(C₄₄(CdS)/ρ(CdS)). If a mode does not exist at a given k∥D, leave the corresponding entry as NaN.
- Output file: `/app/outputs/surface_phase_velocities.csv`
- Format: csv
- Contract: Columns: k_parallel_D (float), velocity_CdS_nonmetal (float), velocity_CdS_metal (float), velocity_ZnO_metal (float). Use NaN when a mode does not exist.
- Scoring: scored by hidden verifier

### Step 3: Compute effective medium constants
- Role: scored
- Action: Using the material parameters of CdS and ZnO (Table 1) and equal layer thickness fraction x = 0.5, compute the long-wavelength effective constants from the averaging rules for orthorhombic 2mm symmetry with normal along x₁, specialized to 6mm (C55 = C44, ε22 = ε11).  
1. Elastic constant: C₄₄^eff is the thickness-weighted arithmetic average: C₄₄^eff = x · C₄₄(CdS) + (1−x) · C₄₄(ZnO).  
2. Piezoelectric and dielectric constants: For each material, compute 𝒟' = C₄₄·ε₁₁ + (e₁₅)². Then compute the thickness-weighted averages of the three combinations:  
   A = < e₁₅ / 𝒟' > = x·e₁₅(CdS)/𝒟'(CdS) + (1−x)·e₁₅(ZnO)/𝒟'(ZnO),  
   B = < ε₁₁ / 𝒟' > = x·ε₁₁(CdS)/𝒟'(CdS) + (1−x)·ε₁₁(ZnO)/𝒟'(ZnO),  
   C = < C₄₄ / 𝒟' > = x·C₄₄(CdS)/𝒟'(CdS) + (1−x)·C₄₄(ZnO)/𝒟'(ZnO).  
   Obtain the effective 𝒟'^eff = C₄₄^eff / C, then e₁₅^eff = A · 𝒟'^eff, ε₁₁^eff = B · 𝒟'^eff.  
All units: C₄₄ in 10^10 N/m², e₁₅ in C/m², ε₁₁ in 10⁻¹¹ F/m. Output the results in a JSON file.
- Output file: `/app/outputs/effective_constants.json`
- Format: json
- Contract: JSON object with keys: "C44_eff" (float, unit 10^10 N/m²), "e15_eff" (float, unit C/m²), "epsilon11_eff" (float, unit 10⁻¹¹ F/m).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_band_edges.csv`
- `/app/outputs/surface_phase_velocities.csv`
- `/app/outputs/effective_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_band_edges.csv
- path: `/app/outputs/bulk_band_edges.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Bulk band-edge frequencies for the first two SH bands; the hidden checker will recompute the transfer matrix and compare the band edges within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `k_parallel_D`, `band1_lower`, `band1_upper`, `band2_lower`, `band2_upper`
  - `units`:
    - `k_parallel_D`: dimensionless
    - `band1_lower`: dimensionless (Ω)
    - `band1_upper`: dimensionless (Ω)
    - `band2_lower`: dimensionless (Ω)
    - `band2_upper`: dimensionless (Ω)

### surface_phase_velocities.csv
- path: `/app/outputs/surface_phase_velocities.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface wave phase velocities for selected k∥D values; the hidden checker will recompute the surface wave conditions and compare velocities within a relative tolerance. NaN entries are allowed when a mode does not exist.
- schema:
  - `type`: table
  - `required_columns`: `k_parallel_D`, `velocity_CdS_nonmetal`, `velocity_CdS_metal`, `velocity_ZnO_metal`
  - `units`:
    - `k_parallel_D`: dimensionless
    - `velocity_CdS_nonmetal`: v / C_t(CdS) (dimensionless)
    - `velocity_CdS_metal`: v / C_t(CdS) (dimensionless)
    - `velocity_ZnO_metal`: v / C_t(CdS) (dimensionless)

### effective_constants.json
- path: `/app/outputs/effective_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Effective medium constants; the hidden checker will compute the expected values from the material parameters and compare them with an absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `C44_eff`: float (unit 10^10 N/m²)
    - `e15_eff`: float (unit C/m²)
    - `epsilon11_eff`: float (unit 10⁻¹¹ F/m)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_band_edges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_parallel_D",
          "band1_lower",
          "band1_upper",
          "band2_lower",
          "band2_upper"
        ],
        "units": {
          "k_parallel_D": "dimensionless",
          "band1_lower": "dimensionless (Ω)",
          "band1_upper": "dimensionless (Ω)",
          "band2_lower": "dimensionless (Ω)",
          "band2_upper": "dimensionless (Ω)"
        }
      },
      "description": "Bulk band-edge frequencies for the first two SH bands; the hidden checker will recompute the transfer matrix and compare the band edges within a relative tolerance."
    },
    {
      "file": "surface_phase_velocities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_parallel_D",
          "velocity_CdS_nonmetal",
          "velocity_CdS_metal",
          "velocity_ZnO_metal"
        ],
        "units": {
          "k_parallel_D": "dimensionless",
          "velocity_CdS_nonmetal": "v / C_t(CdS) (dimensionless)",
          "velocity_CdS_metal": "v / C_t(CdS) (dimensionless)",
          "velocity_ZnO_metal": "v / C_t(CdS) (dimensionless)"
        }
      },
      "description": "Surface wave phase velocities for selected k∥D values; the hidden checker will recompute the surface wave conditions and compare velocities within a relative tolerance. NaN entries are allowed when a mode does not exist."
    },
    {
      "file": "effective_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C44_eff": "float (unit 10^10 N/m²)",
          "e15_eff": "float (unit C/m²)",
          "epsilon11_eff": "float (unit 10⁻¹¹ F/m)"
        }
      },
      "description": "Effective medium constants; the hidden checker will compute the expected values from the material parameters and compare them with an absolute tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently recomputes the bulk band edges and surface wave velocities from your submitted CSVs using an independent implementation of the transfer‑matrix procedure and compares them to reference values within a preset tolerance (smaller error receives higher credit). The effective constants are compared against the expected values derived from the same material parameters. The final reward is a weighted sum of the scores for each of the three scored outputs; the bulk band edges and surface velocities carry the majority of the weight, while the effective constants contribute a smaller portion. Simply copying numbers from a paper is insufficient—the verifier checks that the submitted numbers are the result of a genuine computation.
