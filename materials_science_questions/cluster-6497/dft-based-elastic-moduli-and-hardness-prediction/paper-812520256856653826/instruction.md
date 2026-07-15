# Elastic and plastic properties of transition-metal-doped antimonene monolayers via density functional theory

## Problem background
Antimonene, a two-dimensional monolayer of antimony, is a stable 2D material with promising electronic properties. Incorporating transition metal (TM) atoms into the antimonene lattice can tailor its mechanical behavior, which is critical for designing flexible and resilient devices. Understanding how doping with different TM atoms affects the in-plane stiffness and yield strain under tensile loading is essential for assessing the material's suitability for nanoelectronic and nanomechanical applications. This task involves computing the elastic moduli and critical strains of TM-doped antimonene monolayers using density functional theory.

## Approach
Use first-principles density functional theory (DFT) to simulate pristine and TM-doped antimonene monolayers. The simulations adopt the generalized gradient approximation (GGA) with the Perdew–Burke–Ernzerhof (PBE) functional and a double-zeta plus polarization (DZP) basis set. Build 2×2 and 3×3 supercells and replace a single Sb atom with one of eight transition metals (Sc, Ti, V, Cr, Fe, Ni, Cu, Zn) to create doped structures. Perform full geometry optimization for each supercell to obtain relaxed structures. Then apply incremental uniaxial longitudinal, uniaxial transverse, and biaxial strains over a range, recording total energies. From the strain–energy curves, compute the in-plane Young's modulus along each direction, the bulk modulus, and the first and second critical strains that mark the transition from harmonic to anharmonic elastic response and the onset of plastic deformation. Compare each doped structure's moduli and critical strains against the pristine reference to quantify the effect of doping.

## Reproduction target
For pristine and each of the eight TM-doped antimonene monolayers (Sc, Ti, V, Cr, Fe, Ni, Cu, Zn) in both 2×2 and 3×3 supercells, compute and report:
- Relaxed structural parameters: lattice constant, Sb–Sb bond length range, TM–Sb bond length (if doped), and dopant height.
- In-plane Young's moduli along longitudinal (X) and transverse (Y) directions (in N/m) and their reduction percentages relative to pristine.
- Bulk modulus (in N/m) and its reduction percentage relative to pristine.
- First critical strain εc1 and second critical strain εc2 under uniaxial and biaxial loading (dimensionless).
All computed values must be saved in the specified JSON output files following the declared schemas.

## Assets

- SIESTA DFT code: https://siesta-project.org/siesta/

## Workflow steps

### Step 1: Geometry optimization and structural parameters
- Role: scored
- Action: For each structure (pristine and TM-doped: Sc, Ti, V, Cr, Fe, Ni, Cu, Zn; 2×2 and 3×3 supercells), perform density functional theory (DFT) geometry optimization using a GGA-PBE functional and a double-zeta plus polarization (DZP) basis set. After relaxation, extract the lattice constant a (Å), the range of Sb–Sb bond lengths (d_range, list of [min, max] in Å), the TM–Sb bond length d' (Å, null for pristine), and the height of the dopant above the sheet h (Å, null for pristine). Record all values in structural_params.json.
- Output file: `/app/outputs/structural_params.json`
- Format: json
- Contract: JSON object with keys '2x2' and '3x3'. Each value is an object mapping structure name (e.g., 'pristine', 'Cr-doped', ...) to an object with fields: a (number, Å), d_range (array of two numbers: [min, max], Å), d_prime (number or null, Å), h (number or null, Å).
- Scoring: scored by hidden verifier

### Step 2: Uniaxial and biaxial strain simulations
- Role: process
- Action: For every relaxed structure from step1, run DFT calculations using the same functional/basis as step1, applying uniaxial (longitudinal and transverse) and biaxial strain from −5% to +5% in steps of 1%. Record the total energy as a function of strain/area in strain_energy_data.json.
- Evidence: `/app/outputs/strain_energy_data.json`

### Step 3: Young's modulus calculation
- Role: scored (load-bearing)
- Action: From the uniaxial strain energy curves produced in step2, compute the in-plane Young's modulus for each structure along the longitudinal (X) and transverse (Y) directions using Y_s = (1/A0) * d²Es/dε² at equilibrium, where A0 is the equilibrium area and Es the strain energy. Also compute the reduction percentage of each modulus relative to the pristine value. Output all values to youngs_moduli.json.
- Output file: `/app/outputs/youngs_moduli.json`
- Format: json
- Contract: JSON object with keys '2x2' and '3x3'. Each value is an object mapping structure name to an object with fields: longitudinal_Y (number, N/m), transverse_Y (number, N/m), long_reduction_percent (number, %), trans_reduction_percent (number, %).
- Scoring: scored by hidden verifier

### Step 4: Bulk modulus calculation
- Role: scored
- Action: From the biaxial strain energy curves produced in step2, compute the bulk modulus for each structure using B = A0 * d²Es/dA² at equilibrium, where A0 is the equilibrium area and A the instantaneous area. Compute the reduction percentage relative to the pristine value. Output all values to bulk_moduli.json.
- Output file: `/app/outputs/bulk_moduli.json`
- Format: json
- Contract: JSON object with keys '2x2' and '3x3'. Each value is an object mapping structure name to an object with fields: B (number, N/m), reduction_percent (number, %).
- Scoring: scored by hidden verifier

### Step 5: Critical strain analysis
- Role: scored
- Action: For each structure, determine the first critical strain εc1 (where dEs/dε or dEs/dA reaches its maximum) and the second critical strain εc2 (where the energy reaches its maximum or stops increasing) from the uniaxial and biaxial strain energy curves produced in step2. Perform this for both uniaxial and biaxial loadings. Record all critical strains in critical_strains.json.
- Output file: `/app/outputs/critical_strains.json`
- Format: json
- Contract: JSON object with keys '2x2' and '3x3'. Each value is an object with sub-keys 'uniaxial' and 'biaxial'. Each sub-key maps structure names to objects with fields: eps_c1 (number, dimensionless) and eps_c2 (number, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_params.json`
- `/app/outputs/youngs_moduli.json`
- `/app/outputs/bulk_moduli.json`
- `/app/outputs/critical_strains.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_params.json
- path: `/app/outputs/structural_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice constants, Sb–Sb bond length ranges, TM–Sb bond lengths, and dopant heights.
- schema:
  - `type`: object
  - `description`: Keys '2x2' and '3x3', each mapping structure name to {a, d_range, d_prime, h}. All lengths in Å.

### youngs_moduli.json
- path: `/app/outputs/youngs_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: In-plane Young's moduli and reduction percentages.
- schema:
  - `type`: object
  - `description`: Keys '2x2' and '3x3', each mapping structure name to {longitudinal_Y, transverse_Y, long_reduction_percent, trans_reduction_percent}. Units N/m and %.

### bulk_moduli.json
- path: `/app/outputs/bulk_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bulk moduli and reduction percentages.
- schema:
  - `type`: object
  - `description`: Keys '2x2' and '3x3', each mapping structure name to {B, reduction_percent}. Units N/m and %.

### critical_strains.json
- path: `/app/outputs/critical_strains.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: First and second critical strains (dimensionless).
- schema:
  - `type`: object
  - `description`: Keys '2x2' and '3x3', each with sub-keys 'uniaxial' and 'biaxial' mapping structure name to {eps_c1, eps_c2}.

Notes: Only the eight transition metals (Sc, Ti, V, Cr, Fe, Ni, Cu, Zn) are required. Co and Mn dopants mentioned in the conclusion are not needed. No plastic deformation visualizations are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Keys '2x2' and '3x3', each mapping structure name to {a, d_range, d_prime, h}. All lengths in Å."
      },
      "description": "Relaxed lattice constants, Sb–Sb bond length ranges, TM–Sb bond lengths, and dopant heights."
    },
    {
      "file": "youngs_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Keys '2x2' and '3x3', each mapping structure name to {longitudinal_Y, transverse_Y, long_reduction_percent, trans_reduction_percent}. Units N/m and %."
      },
      "description": "In-plane Young's moduli and reduction percentages."
    },
    {
      "file": "bulk_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Keys '2x2' and '3x3', each mapping structure name to {B, reduction_percent}. Units N/m and %."
      },
      "description": "Bulk moduli and reduction percentages."
    },
    {
      "file": "critical_strains.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Keys '2x2' and '3x3', each with sub-keys 'uniaxial' and 'biaxial' mapping structure name to {eps_c1, eps_c2}."
      },
      "description": "First and second critical strains (dimensionless)."
    }
  ],
  "notes": "Only the eight transition metals (Sc, Ti, V, Cr, Fe, Ni, Cu, Zn) are required. Co and Mn dopants mentioned in the conclusion are not needed. No plastic deformation visualizations are required."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact (`structural_params.json`, `youngs_moduli.json`, `bulk_moduli.json`, `critical_strains.json`). The verifier compares your computed values against secret reference data using predefined tolerances that account for legitimate differences due to implementation details (e.g., DFT code, pseudopotentials, convergence criteria). For each quantity, the verifier determines whether your result meets the required standard; performance that matches or exceeds the reference yields full credit, while larger deviations reduce the score. The total reward is a weighted sum across all scored artifacts. Note that simply reporting numbers without having genuinely executed the DFT workflow will not pass the hidden checks, as the verifier also validates that the outputs were produced from an authentic computation path.
