# GaAs Valley Phononic Crystal Bandgap Calculation and Edge State Verification

## Problem background
Valley phononic crystals (VPnCs) exploit the quantum valley Hall effect to realise topologically protected transport of elastic waves, enabling robust edge modes with suppressed backscattering. In continuous elastic media like GaAs, achieving complete phononic bandgaps for multiple symmetry modes simultaneously at ultra‑high frequencies (GHz) is challenging due to high modal density. This task addresses the design of a monolithic GaAs‑based VPnC whose unit cell contains a large fixed triangular hole and three small rotatable triangular holes arranged on a triangular lattice. By breaking mirror symmetry through rotation of the small holes, the crystal is expected to open complete bandgaps for both z‑symmetric (S) and z‑antisymmetric (A) elastic modes, each centred around a Dirac degeneracy near the K point of the Brillouin zone. The central computational task is to compute the phononic band structure, extract the Dirac degeneracy frequencies and the resulting bandgap edges, and then verify the existence of valley‑protected edge states in a supercell with domain walls. Reproducing these numerical results tests whether the proposed geometry reliably yields the claimed multiple complete bandgaps and topological edge transport.

## Approach
The approach is based on the finite‑element method (FEM) solving the three‑dimensional elastic wave equation in GaAs, treated as a linear anisotropic elastic medium with cubic symmetry. Two configurations of the primitive cell are studied: the mirror‑symmetric configuration with zero rotation (α = 0°) and the mirror‑symmetry‑broken configuration (α = 4°, Type‑A). For each configuration, Bloch periodic boundary conditions are applied and eigenfrequencies are computed along high‑symmetry paths in the irreducible Brillouin zone. For α = 0°, the degeneracies of the S‑mode and A‑mode Dirac points near the K point are identified. For α = 4°, the eigenmodes are classified by parity of the out‑of‑plane displacement into S and A modes, and the lower and upper edges of the complete bandgaps are extracted. In a second stage, a supercell containing an AB interface (between Type‑A and Type‑B unit cells, with Type‑B having α = −4°) is constructed, and the projected band structure is computed as a function of the wave‑vector component along the interface. The presence of edge‑state branches inside the previously identified bandgaps is determined by mode localisation and dispersion characteristics. The entire workflow can be implemented with any open‑source FEM solver capable of handling 3D elastic eigenproblems with Bloch‑Floquet boundary conditions.

## Reproduction target
The reproduction target has two scored stages. First, compute the unit cell band structure and produce a JSON file containing the two Dirac degeneracy frequencies for α = 0° (in GHz) and the complete bandgap lower and upper edges for the S and A modes for α = 4° (also in GHz). Second, compute the projected band structure of the supercell waveguide and write a CSV file with the dispersion data (`kx`, `frequency`, `mode_index`, and optionally `interface_type`) that captures the edge‑state branches inside the S‑mode and A‑mode bandgaps. The success of the reproduction is judged by the accuracy of the extracted bandgap edges against hidden reference values and by the presence of edge‑state modes with opposite group velocities in each bandgap, as verified by a hidden checker. No external data are required; all geometry and material parameters are provided in the workflow steps.

## Assets

- Open‑source finite‑element solver for elastic wave eigenfrequency analysis (e.g., FEniCS, FreeFEM, Elmer): fenics or freefem or elmer

## Workflow steps

### Step 1: Unit cell band structure and bandgap determination
- Role: scored
- Action: Build the 3D GaAs phononic crystal primitive cell with the given geometry (`a = 730 nm`, `h = 200 nm`, `l_L = 535 nm`, `l_S = 240 nm`, `CD = 260 nm`) and material parameters (`ρ = 5360 kg/m³`, `C₁₁ = 118.8 GPa`, `C₁₂ = 53.8 GPa`, `C₄₄ = 59.4 GPa`). Apply Bloch periodic boundary conditions. Compute the eigenfrequencies along the high‑symmetry path `Γ‑K‑M‑Γ` of the hexagonal Brillouin zone for two configurations: rotation `α = 0°` and `α = 4°` (Type‑A). The primitive unit cell is a rhombus with lattice vectors `a₁ = (a, 0, 0)` and `a₂ = (a/2, √3·a/2, 0)`; the reciprocal‑lattice vectors are `b₁ = (2π/a, 2π/(√3·a), 0)` and `b₂ = (0, 4π/(√3·a), 0)`. The path consists of the following segments (coordinates in the basis `(b₁, b₂)`): `Γ → K (0,0,0 → 2/3, 1/3, 0)`, `K → M (2/3, 1/3, 0 → 1/2, 0, 0)`, `M → Γ (1/2, 0, 0 → 0,0,0)`. Use a uniform sampling of at least 30 points per segment to obtain a smooth dispersion.  
  For `α = 0°`, identify the two Dirac degeneracy frequencies near the K point. For `α = 4°`, separate the modes into z‑symmetric (S) and z‑antisymmetric (A) classes based on the parity of the out‑of‑plane displacement component; extract the complete phononic bandgap lower/upper edges for the S and A mode pairs.
- Output file: `/app/outputs/summary_dirac_bandgaps.json`
- Format: json
- Contract: object with keys: `"dirac_frequencies_0deg"` (array of two numbers in GHz — first element: S‑mode Dirac frequency, second element: A‑mode Dirac frequency), `"bandgap_S_mode"` (array `[lower, upper]` in GHz), `"bandgap_A_mode"` (array `[lower, upper]` in GHz).
- Scoring: scored by hidden verifier

### Step 2: Supercell waveguide edge state dispersion
- Role: scored (load‑bearing)
- Action: Construct a supercell containing one Type‑A (`α = 4°`) and one Type‑B (`α = −4°`) unit cell to form two domain walls (AB and BA interfaces). Use the same material and geometric parameters. Apply periodic Bloch boundary conditions along the interface direction (`x`) and scan the wavevector component `kx` over the interval `[‑0.5, 0.5]` in units of `2π/a`, using at least 200 uniformly spaced points. Solve the eigenproblem to obtain the projected phononic band structure. Identify edge state branches localised at the interfaces within the S and A bandgap regions and record their dispersion.
- Output file: `/app/outputs/supercell_dispersion.csv`
- Format: csv
- Contract: table with columns: `"kx"` (dimensionless, in units of `2π/a`), `"frequency"` (GHz), `"mode_index"` (integer); optionally `"interface_type"` (`"AB"` or `"BA"`).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/summary_dirac_bandgaps.json`
- `/app/outputs/supercell_dispersion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### summary_dirac_bandgaps.json
- path: `/app/outputs/summary_dirac_bandgaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted Dirac degeneracy frequencies for α = 0° and complete bandgap edges for S and A modes for α = 4°. The checker compares the reported values against the hidden reference values within a tolerance. The array `dirac_frequencies_0deg` must contain the frequencies in the order [S‑mode Dirac, A‑mode Dirac].
- schema:
  - `type`: object
  - `required`: `dirac_frequencies_0deg`, `bandgap_S_mode`, `bandgap_A_mode`
  - `properties`:
    - `dirac_frequencies_0deg`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 2
      - `maxItems`: 2
      - `units`: GHz
      - `description`: First element is the z‑symmetric (S) mode Dirac frequency, second element the z‑antisymmetric (A) mode Dirac frequency.
    - `bandgap_S_mode`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 2
      - `maxItems`: 2
      - `units`: GHz
    - `bandgap_A_mode`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 2
      - `maxItems`: 2
      - `units`: GHz

### supercell_dispersion.csv
- path: `/app/outputs/supercell_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Projected band structure of the supercell with AB/BA domain walls. The checker verifies that within each bandgap frequency range (S and A) there exist edge state branches with opposite group velocities, consistent with valley-protected transport.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `frequency`, `mode_index`
  - `optional_columns`: `interface_type`
  - `units`:
    - `kx`: `2π/a`
    - `frequency`: GHz

Notes: The Berry curvature stage and full Z‑shaped waveguide simulation are omitted from the minimal reproduction because they are computationally expensive and the core claim is verified by the bandgap and edge state dispersion.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "summary_dirac_bandgaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "dirac_frequencies_0deg",
          "bandgap_S_mode",
          "bandgap_A_mode"
        ],
        "properties": {
          "dirac_frequencies_0deg": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 2,
            "maxItems": 2,
            "units": "GHz",
            "description": "First element: S-mode Dirac frequency, second element: A-mode Dirac frequency."
          },
          "bandgap_S_mode": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 2,
            "maxItems": 2,
            "units": "GHz"
          },
          "bandgap_A_mode": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 2,
            "maxItems": 2,
            "units": "GHz"
          }
        }
      },
      "description": "Extracted Dirac degeneracy frequencies for α=0° and complete bandgap edges for S and A modes for α=4°. The checker compares the reported values against the hidden reference values within a tolerance."
    },
    {
      "file": "supercell_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "frequency",
          "mode_index"
        ],
        "optional_columns": [
          "interface_type"
        ],
        "units": {
          "kx": "2π/a",
          "frequency": "GHz"
        }
      },
      "description": "Projected band structure of the supercell with AB/BA domain walls. The checker verifies that within each bandgap frequency range (S and A) there exist edge state branches with opposite group velocities, consistent with valley-protected transport."
    }
  ],
  "notes": "The Berry curvature stage and full Z‑shaped waveguide simulation are omitted from the minimal reproduction because they are computationally expensive and the core claim is verified by the bandgap and edge state dispersion."
}
```

## How you are scored
A hidden verifier automatically scores each workflow stage’s artifact and combines the two stage rewards with predetermined weights. For the unit cell results (`summary_dirac_bandgaps.json`), the verifier compares the reported Dirac frequencies and bandgap edges to a hidden reference; the comparison tolerates small deviations expected from different FEM implementations and meshing choices, but unphysical or largely incorrect values will yield little or no reward. For the supercell dispersion (`supercell_dispersion.csv`), the verifier performs a structural audit: it checks that within each bandgap frequency range there exist edge‑state branches with opposite group velocities, consistent with valley‑protected transport, and that the data format matches the required schema. The agent must execute the full finite‑element workflow and submit the resulting numerical artifacts.