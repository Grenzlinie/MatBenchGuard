# DFT calculation of band gaps and optical constants of orthorhombic L‑threonine crystal

## Problem background
Amino acid crystals are increasingly studied for bio-organic optoelectronic devices because many of them behave as wide-band-gap semiconductors with good transparency in the visible region. A predictive understanding of their structural, electronic, and optical properties is therefore important for technological development. This work concentrates on anhydrous orthorhombic L‑threonine crystals—a polar amino acid in its zwitterionic form—and aims to characterize the crystal's electronic band structure and optical response using first‑principles density‑functional theory. The task is to compute the band gap character and values, the static dielectric constant, and the refractive index for this crystal and to report them in a verifiable format.

## Approach
The computational study employs density‑functional theory (DFT) with two exchange‑correlation functionals: the local‑density approximation (LDA) and the Perdew–Burke–Ernzerhof generalized‑gradient approximation augmented with the Tkatchenko–Scheffler dispersion correction (GGA+TS). Norm‑conserving pseudopotentials and a plane‑wave basis set are used throughout. The workflow proceeds in four stages: (1) Geometry optimization: starting from the published experimental crystal structure, the unit cell of orthorhombic L‑threonine is relaxed separately for the LDA and GGA+TS functionals. (2) Electronic structure: Kohn‑Sham band structures and partial densities of states are computed for each optimized geometry, from which the band gap type (direct or indirect) and the gap value(s) in eV are extracted. (3) Optical properties: The complex dielectric function and the refractive index are calculated within the independent‑particle approximation for light polarized along the [001] crystal direction, separately for the LDA and GGA+TS functionals. (4) Data compilation: The static (zero‑frequency) dielectric constant ε₁(0) and the refractive index n(0) are collected, and all results are written to the required JSON files. The agent may use any open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) and publicly available norm‑conserving pseudopotentials.

## Reproduction target
For both the LDA and GGA+TS functionals, determine the electronic band gap: whether it is direct or indirect, and the associated gap value(s) in eV. For light polarized along the [001] direction, compute the static dielectric constant ε₁(0) and the refractive index n(0). Report these quantities in two JSON files, `band_gaps.json` and `optical_constants.json`, following the schemas shown in the respective workflow steps. The correctness of the reported numbers will be assessed against reference values derived from the original study.

## Assets

- Experimental crystal structure of anhydrous orthorhombic L‑threonine (Janczak et al. 1997): 10.1107/S0108270197007525
- Quantum ESPRESSO DFT package: https://www.quantum-espresso.org
- Norm‑conserving pseudopotentials (SG15 or PSlibrary): http://pseudopotentials.quantum-espresso.org

## Workflow steps

### Step 1: LDA geometry optimization
- Role: process
- Action: Optimize the crystal structure of anhydrous orthorhombic L‑threonine using DFT with the LDA exchange‑correlation functional, starting from the experimental structure (Janczak et al. 1997).
- Evidence: `/app/outputs/lda_opt.log`

### Step 2: GGA+TS geometry optimization
- Role: process
- Action: Optimize the crystal structure using DFT with the GGA‑PBE functional including Tkatchenko‑Scheffler dispersion correction (GGA+TS).
- Evidence: `/app/outputs/gga_opt.log`

### Step 3: LDA electronic structure calculation
- Role: process
- Action: Compute the Kohn‑Sham band structure and partial density of states for the LDA‑optimized geometry. Determine the band gap type (direct/indirect) and value(s).
- Evidence: `/app/outputs/lda_bands.dat`

### Step 4: GGA+TS electronic structure calculation
- Role: process
- Action: Compute the Kohn‑Sham band structure and partial density of states for the GGA+TS‑optimized geometry. Determine the band gap type and value(s).
- Evidence: `/app/outputs/gga_bands.dat`

### Step 5: Compile band gap results
- Role: scored (load-bearing)
- Action: Collect the band gap type and value(s) from the LDA and GGA+TS electronic structure runs and write band_gaps.json according to the output schema.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"GGA_TS": {"gap_type": "direct", "direct_gap": number}, "LDA": {"gap_type": "indirect", "indirect_gaps": [number, ...]}} with numeric values in eV
- Scoring: scored by hidden verifier

### Step 6: LDA optical properties calculation
- Role: process
- Action: Compute the complex dielectric function є(ω) and refractive index n(ω) from the LDA wavefunctions. Extract the static values є1(0) and n(0) for light polarized along [001].
- Evidence: `/app/outputs/lda_optical.dat`

### Step 7: GGA+TS optical properties calculation
- Role: process
- Action: Compute the complex dielectric function and refractive index from the GGA+TS wavefunctions. Extract the static values є1(0) and n(0) for light polarized along [001].
- Evidence: `/app/outputs/gga_optical.dat`

### Step 8: Compile optical constants
- Role: scored (load-bearing)
- Action: Write optical_constants.json containing the static dielectric constant є1(0) and refractive index n(0) for both LDA and GGA+TS functionals.
- Output file: `/app/outputs/optical_constants.json`
- Format: json
- Contract: {"GGA_TS": {"epsilon1_0": number, "refractive_index_0": number}, "LDA": {"epsilon1_0": number, "refractive_index_0": number}} with dimensionless values
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/optical_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gap type and values (eV) computed with LDA and GGA+TS functionals.
- schema:
  - `type`: object
  - `required`:
    - `GGA_TS`:
      - `gap_type`: one of [direct, indirect]
      - `direct_gap`: number (eV) present only if gap_type=direct
      - `indirect_gaps`: list of numbers (eV) present only if gap_type=indirect
    - `LDA`:
      - `gap_type`: one of [direct, indirect]
      - `direct_gap`: number (eV) present only if gap_type=direct
      - `indirect_gaps`: list of numbers (eV) present only if gap_type=indirect

### optical_constants.json
- path: `/app/outputs/optical_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static dielectric constant and refractive index at zero frequency for light polarized along [001], from LDA and GGA+TS functionals.
- schema:
  - `type`: object
  - `required`:
    - `GGA_TS`:
      - `epsilon1_0`: number (dimensionless)
      - `refractive_index_0`: number (dimensionless)
    - `LDA`:
      - `epsilon1_0`: number (dimensionless)
      - `refractive_index_0`: number (dimensionless)

Notes: All values are dimensionless. Band gap type (direct/indirect) must match exactly; numeric tolerances are applied by the hidden checker. The agent may use any open‑source DFT code (e.g., Quantum ESPRESSO) with norm‑conserving pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GGA_TS": {
            "gap_type": "one of [direct, indirect]",
            "direct_gap": "number (eV) present only if gap_type=direct",
            "indirect_gaps": "list of numbers (eV) present only if gap_type=indirect"
          },
          "LDA": {
            "gap_type": "one of [direct, indirect]",
            "direct_gap": "number (eV) present only if gap_type=direct",
            "indirect_gaps": "list of numbers (eV) present only if gap_type=indirect"
          }
        }
      },
      "description": "Band gap type and values (eV) computed with LDA and GGA+TS functionals."
    },
    {
      "file": "optical_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GGA_TS": {
            "epsilon1_0": "number (dimensionless)",
            "refractive_index_0": "number (dimensionless)"
          },
          "LDA": {
            "epsilon1_0": "number (dimensionless)",
            "refractive_index_0": "number (dimensionless)"
          }
        }
      },
      "description": "Static dielectric constant and refractive index at zero frequency for light polarized along [001], from LDA and GGA+TS functionals."
    }
  ],
  "notes": "All values are dimensionless. Band gap type (direct/indirect) must match exactly; numeric tolerances are applied by the hidden checker. The agent may use any open‑source DFT code (e.g., Quantum ESPRESSO) with norm‑conserving pseudopotentials."
}
```

## How you are scored
A hidden verifier reads your submitted artifact files (`band_gaps.json` and `optical_constants.json`). For each stage it compares the quantities you computed—band gap type, band gap values (eV), static dielectric constant, and refractive index—to reference values that were extracted from the published work. Agreement is evaluated with pre‑defined tolerances; the band gap type must be identified exactly (direct/indirect). The final reward is a weighted combination of the per‑stage scores, so faithfully executing the complete DFT pipeline (geometry optimization, band structure, and optical calculations) is essential for a high score.
