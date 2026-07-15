# Geometry optimization and electronic structure analysis of BaCoO3

## Problem background
BaCoO3 is a pseudo-perovskite that crystallizes in an hexagonal structure with chains of face-sharing CoO6 octahedra. Its magnetotransport properties are of interest, but the underlying conduction mechanism—whether dominated by direct Co–Co σ interactions or by Co–O hybridization—has been debated. Clarifying this requires determining the optimal oxygen position within the unit cell and analyzing the resulting electronic structure for different geometries. This task investigates that question by computing the equilibrium oxygen coordinate and comparing key electronic features for the relaxed structure and a reference geometry.

## Approach
The investigation uses an all-electron full-potential linearized augmented plane wave (FP-LAPW) method, implemented in the open-source Elk code. The workflow first performs a geometry optimization of the oxygen atoms in ferromagnetic BaCoO3 (space group P6_3mc, fixed spin moment of 2 μB per cell) using the GGA-PBE functional. From the optimized oxygen Wyckoff parameter x, two geometries are constructed: the relaxed ground state and a non-optimized structure with x = 0.1450. Self-consistent field calculations are carried out for both geometries at higher numerical precision. Band structures are generated along high-symmetry paths, including the chain direction Γ–A, to measure the dispersion of the d_{x²−y²} band and to assess whether each geometry is half‑metallic or metallic. Additionally, differential charge densities are computed (crystal density minus a superposition of isolated ionic densities) to locate and compare the peak electron accumulation in the lobes between oxygen ligands around a Co ion. These quantities allow an analysis of the relative importance of Co–O interactions versus direct Co–Co interactions.

## Reproduction target
From the geometry optimization, extract the optimized oxygen position parameter x and write it to optimized_x.txt. Using the self-consistent eigenvalues, compute the bandwidth of the d_{x²−y²} band along Γ–A for the optimized geometry, and determine whether the optimized geometry exhibits half‑metallicity (a spin gap at the Fermi level in one spin channel) and whether the x=0.1450 geometry is metallic (no gap in either spin). Report these electronic structure metrics in band_analysis.json. Finally, for both geometries, compute the peak positive value of the differential charge density in the lobes between oxygen ligands around a Co ion, and record the results in density_peaks.json.

## Assets

- Elk all-electron full-potential linearized augmented plane wave (FP-LAPW) code: https://elk.sourceforge.io/
- Initial crystal structure of BaCoO3

## Workflow steps

### Step 1: Geometry optimization of oxygen position
- Role: process
- Action: Set up the initial BaCoO3 structure with lattice parameters a=5.645 Å, c=4.752 Å, space group P6₃mc. Perform a ferromagnetic fixed-spin-moment calculation (total moment 2 μB/cell) using the GGA-PBE functional, and relax the oxygen position x by minimizing forces and total energy. Record the final x and residual forces.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Extract optimized oxygen position x
- Role: scored
- Action: From the geometry optimization output, extract the converged oxygen x parameter and write it to a plain text file.
- Output file: `/app/outputs/optimized_x.txt`
- Format: txt
- Contract: single float, e.g., 0.1284
- Scoring: scored by hidden verifier

### Step 3: SCF calculation for optimized geometry
- Role: process
- Action: Using the optimized geometry from step_02, perform a self-consistent field calculation with higher numerical precision (converged charge density, wavefunctions, eigenvalues).
- Evidence: `/app/outputs/scf_optimized.log`

### Step 4: SCF calculation for x=0.1450 geometry
- Role: process
- Action: Set up the structure with oxygen x=0.1450 (all other parameters identical). Perform the same high-quality SCF calculation and retain the converged charge density and eigenvalues.
- Evidence: `/app/outputs/scf_x1450.log`

### Step 5: Band structure analysis for both geometries
- Role: scored (load-bearing)
- Action: Using the eigenvalues from step_03 and step_04, compute the band structure along the high-symmetry path including the chain direction Γ-A. Identify the d_{x²−y²} band and measure its bandwidth (energy spread) along Γ-A for the optimized geometry. Determine whether the optimized geometry is half-metallic (a spin gap at the Fermi level in one channel) and whether the x=0.1450 geometry is metallic (no gap in either spin). Write the results to a JSON file.
- Output file: `/app/outputs/band_analysis.json`
- Format: json
- Contract: object with fields: optimized_bandwidth_dx2y2 (float, eV), optimized_half_metallic (boolean), x1450_metallic (boolean)
- Scoring: scored by hidden verifier

### Step 6: Differential charge density analysis
- Role: scored
- Action: For both the optimized and x=0.1450 geometries, compute the self-consistent crystal charge density and subtract a superposition of isolated ionic densities (Co⁴⁺, O²⁻, Ba²⁺). From the resulting differential density maps, determine the peak positive density in the lobes between oxygen ligands around a Co ion. Write the peak values (in e/Å³) to a JSON file.
- Output file: `/app/outputs/density_peaks.json`
- Format: json
- Contract: object with fields: optimized_peak_density (float, e/Å³), x1450_peak_density (float, e/Å³)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_x.txt`
- `/app/outputs/band_analysis.json`
- `/app/outputs/density_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_x.txt
- path: `/app/outputs/optimized_x.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimized oxygen position parameter x from geometry relaxation.
- schema:
  - `type`: text
  - `required`:
    - `value`: float

### band_analysis.json
- path: `/app/outputs/band_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Electronic structure metrics: bandwidth of d_{x²−y²} band, half-metallicity of optimized geometry, and metallicity of x=0.1450 geometry.
- schema:
  - `type`: object
  - `required`:
    - `optimized_bandwidth_dx2y2`: float (eV)
    - `optimized_half_metallic`: boolean
    - `x1450_metallic`: boolean

### density_peaks.json
- path: `/app/outputs/density_peaks.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Peak differential electron density in the lobes between oxygen ligands for both geometries.
- schema:
  - `type`: object
  - `required`:
    - `optimized_peak_density`: float (e/Å³)
    - `x1450_peak_density`: float (e/Å³)

Notes: All output files are written to /app/outputs. Scoring compares extracted values to hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_x.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "value": "float"
        }
      },
      "description": "Optimized oxygen position parameter x from geometry relaxation."
    },
    {
      "file": "band_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "optimized_bandwidth_dx2y2": "float (eV)",
          "optimized_half_metallic": "boolean",
          "x1450_metallic": "boolean"
        }
      },
      "description": "Electronic structure metrics: bandwidth of d_{x²−y²} band, half-metallicity of optimized geometry, and metallicity of x=0.1450 geometry."
    },
    {
      "file": "density_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "optimized_peak_density": "float (e/Å³)",
          "x1450_peak_density": "float (e/Å³)"
        }
      },
      "description": "Peak differential electron density in the lobes between oxygen ligands for both geometries."
    }
  ],
  "notes": "All output files are written to /app/outputs. Scoring compares extracted values to hidden reference values with appropriate tolerances."
}
```

## How you are scored
After you submit all required artifacts, a hidden verification procedure will independently examine the contents of optimized_x.txt, band_analysis.json, and density_peaks.json. The verifier compares your reported numerical values, boolean flags, and derived quantities to reference benchmarks using pre‑set tolerances and structural checks appropriate for the underlying physics. Each scored artifact contributes a pre‑determined share of the total reward. Only the final output files are evaluated; intermediate process logs are not scored but must exist to document that the required calculations were performed.
