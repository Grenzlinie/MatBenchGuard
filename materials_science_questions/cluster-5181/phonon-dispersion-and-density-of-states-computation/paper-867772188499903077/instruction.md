# First‑principles spin‑phonon coupling for V(IV) molecular qubits

## Problem background
Spin-phonon coupling limits the coherence times of molecular spin qubits by enabling energy exchange between a spin and lattice vibrations. A first-principles understanding of how normal modes modulate the Zeeman interaction (g-tensor) in vanadium(IV) complexes can guide chemical design. This work combines periodic DFT phonon calculations with high-level electronic structure methods to compute mode-resolved spin-phonon coupling coefficients and an average coupling magnitude for four compounds, and investigates the correlation with the chemical structure (ligand field, coordination geometry).

## Approach
The conceptual approach has three main stages. (1) Periodic DFT (PBE functional with rVV10 van der Waals correction) is used to optimize crystal structures and compute Γ‑point phonon frequencies and normal‑mode eigenvectors via finite‑difference Hessian diagonalization. (2) For the central molecule in each crystal, the g‑tensor is calculated at equilibrium and at six displaced geometries (±0.0050, ±0.0075, ±0.0150 Å) per molecular Cartesian coordinate using CASSCF+NEVPT2 (active space: one electron in five 3d orbitals; basis: def2‑TZVP for V/O/S, def2‑SVP for C/H). (3) Each g‑tensor component is fitted versus displacement to a second‑order polynomial to extract the linear Cartesian derivative (∂g/∂X)₀, which is then projected onto the phonon normal modes to obtain mode‑resolved spin‑phonon coupling coefficients. The average molecular spin‑phonon coupling |∂g| is defined as the sum of absolute values of all Cartesian derivatives. The same workflow is applied to four vanadium(IV) molecular crystals that differ in coordination (penta‑coordinated vanadyl vs. hexa‑coordinated) and ligand donor atoms (oxygen vs. sulfur).

## Reproduction target
For each of the four molecular crystals — [PPh₄]₂[VO(cat)₂] (compound 1), [PPh₄]₂[V(cat)₃] (compound 2), [PPh₄]₂[VO(dmit)₂] (compound 3), [PPh₄]₂[V(dmit)₃] (compound 4) — compute the equilibrium g‑tensor components (gx, gy, gz) and the average molecular spin‑phonon coupling |∂g| using the above workflow. Report these quantities along with the list of Γ‑point optical phonon frequencies (cm⁻¹) and the corresponding mode‑coupling norms (sum_{jr}|∂gjr/∂qα|²) in separate JSON files, one per compound. The target is to obtain the computed g‑tensor and |∂g| values for each compound. In addition, a structural check across the four compounds verifies that the relative ordering of the computed |∂g| values is consistent with the paper’s calculated trend.

## Assets

- CP2K (Quickstep module): https://www.cp2k.org/
- ORCA: https://orcaforum.kofo.mpg.de/
- Crystal structure of [PPh₄]₂[VO(cat)₂]: 10.1021/acs.inorgchem.6b02722
- Crystal structure of [PPh₄]₂[V(cat)₃]: 10.1021/ja047340c
- Crystal structure of [PPh₄]₂[VO(dmit)₂]: 10.1021/jacs.6b05580
- Crystal structure of [PPh₄]₂[V(dmit)₃]: 10.1021/jacs.6b05580

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Obtain the four CIF files (resources) and verify the asymmetric unit and space group. Convert to a format suitable for periodic DFT (e.g., CP2K input).
- Evidence: `/app/outputs/input_coords.log`

### Step 2: Periodic DFT geometry optimization
- Role: process
- Action: For each compound, perform a variable‑cell geometry relaxation of the crystal unit cell using CP2K (PBE functional with rVV10 van der Waals correction) until forces and stresses are tightly converged. Save the relaxed cell parameters and atomic coordinates.
- Evidence: `/app/outputs/geo_opt_structures.tar.gz`

### Step 3: Γ‑point phonon calculation
- Role: process
- Action: For each relaxed structure, compute the finite‑difference Hessian at Γ by displacing inequivalent atoms by ±0.01 Å. Symmetrize the Hessian (average with its transpose) and enforce the acoustic sum rule. Diagonalize the mass‑weighted Hessian to obtain phonon frequencies ω_α and eigenvectors L. Save all frequencies and eigenvectors.
- Evidence: `/app/outputs/phonon_results.tar.gz`

### Step 4: Extract molecular geometries
- Role: process
- Action: From each optimized crystal cell, isolate the central vanadium complex (the dianion). Determine its atomic Cartesian coordinates and masses; they will be used for the high‑level CASSCF calculations.
- Evidence: `/app/outputs/molecular_coords.json`

### Step 5: CASSCF+NEVPT2 g‑tensor scans
- Role: process
- Action: For each compound, run ORCA CASSCF+NEVPT2 (active space: one electron in five 3d orbitals; basis: def2‑TZVP for V, O, S; def2‑SVP for C, H) at the equilibrium molecular geometry and at each of the six displaced geometries (±0.0050, ±0.0075, ±0.0150 Å) for every molecular Cartesian degree of freedom (3M coordinates). Record all nine g‑tensor components at every geometry.
- Evidence: `/app/outputs/g_tensor_raw.tar.gz`

### Step 6: Fit Cartesian derivatives
- Role: process
- Action: For each compound and each Cartesian coordinate i, fit the g‑tensor components versus displacement to a second‑order polynomial y = b x² + a x + c. Extract the linear coefficient a as the Cartesian derivative (∂gjr/∂Xi)₀. Collect all derivatives into a matrix.
- Evidence: `/app/outputs/cartesian_derivatives.json`

### Step 7: Compute spin‑phonon coupling for compound 1
- Role: scored (load-bearing)
- Action: For compound 1 ([VO(cat)₂]²⁻), project the Cartesian derivatives onto the crystal normal modes using mass‑weighted eigenvectors L and phonon frequencies ω_α from step 03, through the projection formula that involves ℏ, ω_α, m_i and L. Compute the average spin‑phonon coupling |∂g| = Σ_{l,v,j,r} |(∂gjr/∂Xlv)₀|. Also record the equilibrium g‑tensor (gx,gy,gz), the list of Γ‑point optical phonon frequencies (cm⁻¹), and the corresponding list of mode coupling norms (sum_{jr}|∂gjr/∂qα|²). Write the results to /app/outputs/compound_1_results.json.
- Output file: `/app/outputs/compound_1_results.json`
- Format: json
- Contract: {"gx": float, "gy": float, "gz": float, "avg_dg": float, "phonon_freqs": [float, ...], "mode_couplings": [float, ...]}
- Scoring: scored by hidden verifier

### Step 8: Compute spin‑phonon coupling for compound 2
- Role: scored (load-bearing)
- Action: For compound 2 ([V(cat)₃]²⁻), perform the same projection and computation as step 07, writing results to /app/outputs/compound_2_results.json.
- Output file: `/app/outputs/compound_2_results.json`
- Format: json
- Contract: {"gx": float, "gy": float, "gz": float, "avg_dg": float, "phonon_freqs": [float, ...], "mode_couplings": [float, ...]}
- Scoring: scored by hidden verifier

### Step 9: Compute spin‑phonon coupling for compound 3
- Role: scored (load-bearing)
- Action: For compound 3 ([VO(dmit)₂]²⁻), perform the same projection and computation as step 07, writing results to /app/outputs/compound_3_results.json.
- Output file: `/app/outputs/compound_3_results.json`
- Format: json
- Contract: {"gx": float, "gy": float, "gz": float, "avg_dg": float, "phonon_freqs": [float, ...], "mode_couplings": [float, ...]}
- Scoring: scored by hidden verifier

### Step 10: Compute spin‑phonon coupling for compound 4
- Role: scored (load-bearing)
- Action: For compound 4 ([V(dmit)₃]²⁻), perform the same projection and computation as step 07, writing results to /app/outputs/compound_4_results.json.
- Output file: `/app/outputs/compound_4_results.json`
- Format: json
- Contract: {"gx": float, "gy": float, "gz": float, "avg_dg": float, "phonon_freqs": [float, ...], "mode_couplings": [float, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/compound_1_results.json`
- `/app/outputs/compound_2_results.json`
- `/app/outputs/compound_3_results.json`
- `/app/outputs/compound_4_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### compound_1_results.json
- path: `/app/outputs/compound_1_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate spin‑phonon coupling results for compound 1 [VO(cat)₂]²⁻.
- schema:
  - `type`: object
  - `required`:
    - `gx`: float
    - `gy`: float
    - `gz`: float
    - `avg_dg`: float
    - `phonon_freqs`: array of float
    - `mode_couplings`: array of float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `phonon_freqs`: cm⁻¹
    - `mode_couplings`: sum_{jr}|∂gjr/∂qα|² (unitless)

### compound_2_results.json
- path: `/app/outputs/compound_2_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate spin‑phonon coupling results for compound 2 [V(cat)₃]²⁻.
- schema:
  - `type`: object
  - `required`:
    - `gx`: float
    - `gy`: float
    - `gz`: float
    - `avg_dg`: float
    - `phonon_freqs`: array of float
    - `mode_couplings`: array of float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `phonon_freqs`: cm⁻¹
    - `mode_couplings`: sum_{jr}|∂gjr/∂qα|² (unitless)

### compound_3_results.json
- path: `/app/outputs/compound_3_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate spin‑phonon coupling results for compound 3 [VO(dmit)₂]²⁻.
- schema:
  - `type`: object
  - `required`:
    - `gx`: float
    - `gy`: float
    - `gz`: float
    - `avg_dg`: float
    - `phonon_freqs`: array of float
    - `mode_couplings`: array of float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `phonon_freqs`: cm⁻¹
    - `mode_couplings`: sum_{jr}|∂gjr/∂qα|² (unitless)

### compound_4_results.json
- path: `/app/outputs/compound_4_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate spin‑phonon coupling results for compound 4 [V(dmit)₃]²⁻.
- schema:
  - `type`: object
  - `required`:
    - `gx`: float
    - `gy`: float
    - `gz`: float
    - `avg_dg`: float
    - `phonon_freqs`: array of float
    - `mode_couplings`: array of float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `phonon_freqs`: cm⁻¹
    - `mode_couplings`: sum_{jr}|∂gjr/∂qα|² (unitless)

Notes: All four JSON files must be present. The checker will compare gx,gy,gz and avg_dg against paper‑reported reference values with appropriate tolerances, and will verify the relative ordering of avg_dg (2 > 4 > 1 > 3).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "compound_1_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gx": "float",
          "gy": "float",
          "gz": "float",
          "avg_dg": "float",
          "phonon_freqs": "array of float",
          "mode_couplings": "array of float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "phonon_freqs": "cm⁻¹",
          "mode_couplings": "sum_{jr}|∂gjr/∂qα|² (unitless)"
        }
      },
      "description": "Aggregate spin‑phonon coupling results for compound 1 [VO(cat)₂]²⁻."
    },
    {
      "file": "compound_2_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gx": "float",
          "gy": "float",
          "gz": "float",
          "avg_dg": "float",
          "phonon_freqs": "array of float",
          "mode_couplings": "array of float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "phonon_freqs": "cm⁻¹",
          "mode_couplings": "sum_{jr}|∂gjr/∂qα|² (unitless)"
        }
      },
      "description": "Aggregate spin‑phonon coupling results for compound 2 [V(cat)₃]²⁻."
    },
    {
      "file": "compound_3_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gx": "float",
          "gy": "float",
          "gz": "float",
          "avg_dg": "float",
          "phonon_freqs": "array of float",
          "mode_couplings": "array of float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "phonon_freqs": "cm⁻¹",
          "mode_couplings": "sum_{jr}|∂gjr/∂qα|² (unitless)"
        }
      },
      "description": "Aggregate spin‑phonon coupling results for compound 3 [VO(dmit)₂]²⁻."
    },
    {
      "file": "compound_4_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gx": "float",
          "gy": "float",
          "gz": "float",
          "avg_dg": "float",
          "phonon_freqs": "array of float",
          "mode_couplings": "array of float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "phonon_freqs": "cm⁻¹",
          "mode_couplings": "sum_{jr}|∂gjr/∂qα|² (unitless)"
        }
      },
      "description": "Aggregate spin‑phonon coupling results for compound 4 [V(dmit)₃]²⁻."
    }
  ],
  "notes": "All four JSON files must be present. The checker will compare gx,gy,gz and avg_dg against paper‑reported reference values with appropriate tolerances, and will verify the relative ordering of avg_dg (2 > 4 > 1 > 3)."
}
```

## How you are scored
A hidden verifier checks each of the four JSON files. For each compound it compares the reported gx, gy, gz to the paper‑reported computed values using a fixed tolerance (±0.005); it compares |∂g| using a relative tolerance of 10 %; it also verifies that the ordering of |∂g| across the four compounds matches the paper‑reported ordering. The phonon frequencies and mode couplings are validated for shape (list of strictly positive frequencies, matching number of optical modes, non‑negative couplings). Each check contributes a weighted score, and the overall reward is the combined score. Reporting numbers is not sufficient — you must produce the artifacts as described in the workflow.
