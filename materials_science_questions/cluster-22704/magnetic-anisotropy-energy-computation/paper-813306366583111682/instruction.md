# Magnetic Anisotropy Energy of Co and Co-Pt Chains on Pt(111)

## Problem background
The ability to control magnetic properties with an electric field is a central goal of spintronics, where large magnetic anisotropy energy (MAE) can stabilize nanomagnets against thermal fluctuations. Atomic chains on heavy-metal substrates such as Pt(111) are attractive systems because of their strong spin-orbit coupling and reduced dimensionality. In this task you will investigate how atomic relaxation and an externally applied perpendicular electric field affect the MAE and the easy-axis orientation of pure Co chains and mixed Co-Pt chains deposited on a Pt(111) surface.

## Approach
You will reproduce the key first-principles results using density functional theory (DFT) with spin-orbit coupling, substituting the proprietary VASP code with the open-source Quantum ESPRESSO. The calculations use the local spin-density approximation (LSDA) and the reference lattice constant of bulk Pt (3.91 Å). A six-layer Pt(111) slab is built; pure Co chains are placed in a 4×1 supercell and mixed Co-Pt chains in a 4×2 supercell, oriented along the [10-1] direction. After ionic relaxation, non-collinear total energies are computed for several magnetization directions (θ, φ). The MAE is defined as the energy of the hardest axis minus that of the easiest axis. For the relaxed pure Co chain, SOC-DFT calculations are repeated under a perpendicular external electric field (dipole correction) at a set of field values between -1.0 and +1.0 V/Å. The final step aggregates all MAE values and easy-axis angles into a structured JSON file.

## Reproduction target
You must compute and report, in a single JSON file, the MAE (in meV) and the easy-axis polar and azimuthal angles (in degrees) for the following conditions: (1) pure Co chain, unrelaxed and relaxed; (2) mixed Co-Pt chain, unrelaxed and relaxed; and (3) the relaxed pure Co chain under external electric fields of -1.0, -0.5, 0.0, +0.5, and +1.0 V/Å. Your submission should satisfy these physical trends: (a) for both chain types the MAE in the relaxed geometry must be larger than in the unrelaxed geometry; (b) for the pure Co chain the MAE must increase monotonically as the electric field becomes more negative (directed outward from the surface); and (c) the relaxed easy-axis orientation should be qualitatively out-of-plane (θ near 0°).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency pseudopotentials (Co, Pt): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build Pt(111) slab
- Role: process
- Action: Construct a six-layer Pt(111) slab using the LDA-optimized bulk lattice constant of 3.91 Å. Include a vacuum region in the supercell.
- Evidence: `/app/outputs/slab_geometry.txt`

### Step 2: Setup chain geometries
- Role: process
- Action: Place a pure Co linear chain in a 4×1 supercell and a mixed Co-Pt linear chain in a 4×2 supercell on the Pt(111) surface. Follow the in-plane chain direction [10-1] and set the initial vertical height of the chain atoms to 2.25 Å.
- Evidence: `/app/outputs/chain_setup.txt`

### Step 3: Relax geometries
- Role: process
- Action: Perform ionic relaxation for both chain systems using DFT (LDA) until forces on all atoms are below 5 meV/Å. Retain the unrelaxed initial geometries for later calculations.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 4: SOC-DFT calculations for pure Co chain
- Role: process
- Action: Run self-consistent spin-orbit coupled DFT calculations for the pure Co chain using both unrelaxed and relaxed geometries. Compute total energies for at least two magnetization directions: out-of-plane (θ=0°) and in-plane (θ=90°, φ=0°). Additionally, for the relaxed geometry, perform calculations under external electric fields of -1.0, -0.5, 0.0, 0.5, 1.0 V/Å for the same magnetization directions.
- Evidence: `/app/outputs/co_chain_energies.txt`

### Step 5: SOC-DFT calculations for mixed Co-Pt chain
- Role: process
- Action: Run self-consistent spin-orbit coupled DFT calculations for the mixed Co-Pt chain using both unrelaxed and relaxed geometries. Compute total energies for three magnetization directions: out-of-plane (θ=0°, φ=0°), in-plane along y (θ=90°, φ=90°), and in-plane along x (θ=90°, φ=0°).
- Evidence: `/app/outputs/copt_chain_energies.txt`

### Step 6: Compute MAE and easy axis
- Role: scored (load-bearing)
- Action: From the total energies obtained in previous steps, compute the magnetic anisotropy energy (MAE) as E_hard - E_easy for each system and condition. Determine the easy axis (θ, φ) as the magnetization direction with the lowest energy. Compile all results into a single JSON file.
- Output file: `/app/outputs/magnetic_anisotropy_results.json`
- Format: json
- Contract: Array of objects, each with fields: system (string, values 'pure_Co' or 'Co_Pt'), geometry_state (string, 'unrelaxed' or 'relaxed'), electric_field (number, V/Å, 0 for zero-field; only for 'pure_Co' relaxed), MAE (number, meV), easy_theta (number, degrees, 0-90), easy_phi (number, degrees, 0-360).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_anisotropy_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_anisotropy_results.json
- path: `/app/outputs/magnetic_anisotropy_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Magnetic anisotropy energy and easy-axis orientation for pure Co and Co-Pt chains on Pt(111) under different geometries and external electric fields.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `geometry_state`, `electric_field`, `MAE`, `easy_theta`, `easy_phi`
    - `properties`:
      - `system`:
        - `type`: string
        - `enum`: `pure_Co`, `Co_Pt`
      - `geometry_state`:
        - `type`: string
        - `enum`: `unrelaxed`, `relaxed`
      - `electric_field`:
        - `type`: number
        - `description`: Applied electric field in V/Å; 0 for zero-field.
      - `MAE`:
        - `type`: number
        - `description`: Magnetic anisotropy energy in meV.
      - `easy_theta`:
        - `type`: number
        - `minimum`: 0
        - `maximum`: 90
        - `description`: Polar angle of easy axis in degrees.
      - `easy_phi`:
        - `type`: number
        - `minimum`: 0
        - `maximum`: 360
        - `description`: Azimuthal angle of easy axis in degrees.

Notes: The verifier performs a T3 structural audit: it checks that relaxed MAE > unrelaxed MAE for both chain types (by at least 0.1 meV), that the MAE for the pure Co chain under electric field increases monotonically as the field becomes more negative (at most one deviation allowed), and that the easy-axis orientation is qualitatively correct (out-of-plane for the relaxed systems).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_anisotropy_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "geometry_state",
            "electric_field",
            "MAE",
            "easy_theta",
            "easy_phi"
          ],
          "properties": {
            "system": {
              "type": "string",
              "enum": [
                "pure_Co",
                "Co_Pt"
              ]
            },
            "geometry_state": {
              "type": "string",
              "enum": [
                "unrelaxed",
                "relaxed"
              ]
            },
            "electric_field": {
              "type": "number",
              "description": "Applied electric field in V/Å; 0 for zero-field."
            },
            "MAE": {
              "type": "number",
              "description": "Magnetic anisotropy energy in meV."
            },
            "easy_theta": {
              "type": "number",
              "minimum": 0,
              "maximum": 90,
              "description": "Polar angle of easy axis in degrees."
            },
            "easy_phi": {
              "type": "number",
              "minimum": 0,
              "maximum": 360,
              "description": "Azimuthal angle of easy axis in degrees."
            }
          }
        }
      },
      "description": "Magnetic anisotropy energy and easy-axis orientation for pure Co and Co-Pt chains on Pt(111) under different geometries and external electric fields."
    }
  ],
  "notes": "The verifier performs a T3 structural audit: it checks that relaxed MAE > unrelaxed MAE for both chain types (by at least 0.1 meV), that the MAE for the pure Co chain under electric field increases monotonically as the field becomes more negative (at most one deviation allowed), and that the easy-axis orientation is qualitatively correct (out-of-plane for the relaxed systems)."
}
```

## How you are scored
A hidden verifier reads your `magnetic_anisotropy_results.json` and scores it automatically. The scoring has two components: a primary structural audit that checks the required trends—relaxation increases MAE, monotonic field dependence, and the correct easy-axis orientation—and a secondary absolute-value comparison against hidden reference data within appropriate tolerances. The structural checks carry the most weight; producing numerically accurate values that violate the expected trends will lead to a low score. You must produce the JSON file exactly as specified in the output contract; the verifier will reject any submission that does not conform to the schema.
