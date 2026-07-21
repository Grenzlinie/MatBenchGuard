# Tight-binding model of compressed black phosphorus node-line semimetal

## Problem background
Black phosphorus (BP) is a layered semiconductor with an orthorhombic structure. Under moderate hydrostatic pressure, the lattice is compressed, altering the electronic structure. First-principles calculations and tight-binding model analysis suggest that compressed BP may host a three-dimensional topological node-line semimetal state when spin-orbit coupling is neglected. In this exotic state, a closed loop of band crossings (a node line) is predicted to appear near the Fermi energy, protected by time-reversal and inversion symmetry. This task reproduces the tight-binding model calculations that test for the existence of the node line and associated topological surface states.

## Approach
A four-band tight-binding model, with hopping parameters extracted from the literature, captures the low-energy electronic structure of compressed BP. The model includes four phosphorus atoms per unit cell and intra-layer as well as inter-layer hopping terms. The momentum-space Hamiltonian is constructed and diagonalized to obtain the bulk band structure and to locate zero-gap crossing points in the T–Z–Γ plane (the node line). The topological character of the (100) surface is probed by computing the Berry phase along the direction normal to the surface for a grid of in-plane momenta, using the discretized F-matrix method. To examine surface states, a finite slab with an 80-layer beard-type termination is constructed and its Hamiltonian diagonalized in the surface Brillouin zone.

## Reproduction target
Compute the bulk band structure along high-symmetry paths and on a dense grid in the T–Z–Γ plane to identify band inversions and the closed node line. Compute the Berry phase for the zigzag-terminated (100) surface as a function of in-plane momentum (k₂,k₃). Compute the surface band structure for an 80-layer slab with beard-type (100) termination.

## Model definition

### Lattice and reciprocal vectors
The compressed orthorhombic BP lattice parameters are:
- a = 4.34 Å
- b = 5.50 Å
- c = 10.49 Å

The primitive lattice vectors are:
- a₁ = (a, 0, 0)
- a₂ = (0, b, 0)
- a₃ = (0, 0, c)

Corresponding reciprocal lattice vectors:
- b₁ = (2π/a, 0, 0)
- b₂ = (0, 2π/b, 0)
- b₃ = (0, 0, 2π/c)

A wave vector k = (k₁, k₂, k₃) in fractional coordinates corresponds to Cartesian components (k₁·b₁ + k₂·b₂ + k₃·b₃). In the momentum-space Hamiltonian, phases are expressed in terms of the dot products k·aᵢ = 2π kᵢ (since aᵢ are orthogonal, aᵢ·bⱼ = 2π δ_ij).

### Tight-binding parameters
The on-site energy and hopping integrals are (all in eV):
- ε = -1.1112
- t₁∥ = -1.3298
- t₂∥ = 4.2265
- t₃∥ = -0.3605
- t₄∥ = -0.1621
- t₁⊥ = 0.5558
- t₂⊥ = 0.2303

### Momentum-space Hamiltonian
The 4×4 Hamiltonian in the basis of the four phosphorus atoms in the unit cell is constructed as follows:

Define H(k) = ε·I + M(k), where M(k) is a Hermitian matrix with zero diagonal. The upper triangular elements are given below; the lower triangle is filled by Hermitian conjugation.

Using the fractional k-coordinates (k₁, k₂, k₃) and phases φᵢ = 2π kᵢ:

h₁₂ = t₁∥ (1 + exp(-i φ₂)) + t₃∥ (exp(-i φ₁) + exp(-i (φ₁+φ₂)))

h₁₃ = t₄∥ (1 + exp(-i φ₂) + exp(-i φ₁) + exp(-i (φ₁+φ₂))) + t₂⊥ (exp(-i φ₃) + exp(-i (φ₁+φ₃)))

h₁₄ = t₂∥ exp(-i (φ₁+φ₂)) + t₁⊥ (exp(-i (φ₁+φ₃)) + exp(-i (φ₁+φ₂+φ₃)))

h₂₃ = t₂∥ + t₁⊥ (exp(-i φ₃) + exp(i (φ₂ - φ₃)))

h₂₄ = h₁₃

h₃₄ = h₁₂

The full matrix is:
H(k) = ε I +
[ 0      h₁₂     h₁₃   h₁₄  ]
[ h₁₂*   0       h₂₃   h₂₄  ]
[ h₁₃*   h₂₃*    0     h₃₄  ]
[ h₁₄*   h₂₄*    h₃₄*  0    ]

All hᵢⱼ are complex; the star denotes complex conjugation.

The high-symmetry points in fractional coordinates for the band-structure path are:
- Γ = (0, 0, 0)
- Z  = (0, 0, 0.5)
- T  = (0.5, 0.0, 0.5)

## Assets
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Bulk band structure and node line
- Role: scored (load-bearing)
- Action: Construct the 4×4 tight-binding Hamiltonian H(k) as defined above. Diagonalize on a dense grid in the T–Z–Γ plane (k₂ = 0 plane) and along the high-symmetry path Γ → Z → T (with dense intermediate points) to obtain eigenvalues. Identify the closed node line where the two central bands cross near the Fermi level; you may use a bisection or root-finding method in the polar coordinates around Z in the k₁-k₃ plane (with k₂ = 0).
- Output file: `/app/outputs/bulk_band_structure.json`
- Format: json
- Contract: {"kpath": [{"label": "string", "k": [float,float,float]}, ...], "eigenvalues": [[float,float,float,float], ...], "node_line_points": [[float,float,float], ...]}
- Scoring: scored by hidden verifier

### Step 2: Berry phase for zigzag termination
- Role: scored
- Action: For the zigzag-terminated (100) surface, compute the Berry phase along the k₁ momentum direction for a grid of in-plane momenta (k₂,k₃) covering the projected node line. Use the discretized F-matrix method with a sufficiently fine k₁ mesh (e.g., 30 to 50 points across the 1D BZ) to obtain the Berry phase modulo 2π, normalized to units of π. The occupied bands are the two lowest eigenstates of H(k₁, k₂, k₃) at each (k₂,k₃).
- Output file: `/app/outputs/berry_phase_zigzag.json`
- Format: json
- Contract: {"k_parallel": [[float,float], ...], "berry_phase": [float, ...]}
- Scoring: scored by hidden verifier

### Step 3: Beard-type (100) surface states
- Role: scored
- Action: Construct the tight-binding Hamiltonian for an 80-layer slab of the beard-terminated (100) surface. Use the model definition of Eq. (1) and the lattice with 80 layers along the surface-normal direction, applying the same hopping parameters but with a finite slab in the k₁ direction. Diagonalize the slab Hamiltonian for a set of surface momenta (k₂,k₃) on a path that passes through the projected node ring (e.g., a line along k₂ with k₃ = 0.5) to obtain all slab eigenvalues.
- Output file: `/app/outputs/surface_band_beard.json`
- Format: json
- Contract: {"k_path": [[float,float], ...], "eigenvalues": [[float, ...], ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_band_structure.json`
- `/app/outputs/berry_phase_zigzag.json`
- `/app/outputs/surface_band_beard.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_band_structure.json
- path: `/app/outputs/bulk_band_structure.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Bulk tight-binding band structure and identified node line points.
- schema:
  - `type`: object
  - `required`:
    - `kpath`: array of objects, each with 'label' (string) and 'k' (array of 3 floats, fractional coordinates)
    - `eigenvalues`: array of arrays, each inner array of 4 floats representing the 4 band energies in eV
    - `node_line_points`: array of arrays of 3 floats, fractional coordinates of the closed node line
  - `items`: object
  - `required_columns`:
  - `units`:
    - `eigenvalues`: eV
    - `k`: dimensionless (fractional)
    - `node_line_points`: dimensionless (fractional)

### berry_phase_zigzag.json
- path: `/app/outputs/berry_phase_zigzag.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Berry phase computed for the zigzag termination as a function of in-plane momentum.
- schema:
  - `type`: object
  - `required`:
    - `k_parallel`: array of arrays of 2 floats (k2, k3) in fractional coordinates
    - `berry_phase`: array of floats, Berry phase in units of π
  - `items`: object
  - `required_columns`:
  - `units`:
    - `k_parallel`: dimensionless (fractional)
    - `berry_phase`: unit of π

### surface_band_beard.json
- path: `/app/outputs/surface_band_beard.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Surface band structure of the beard-terminated (100) slab.
- schema:
  - `type`: object
  - `required`:
    - `k_path`: array of arrays of 2 floats, surface BZ k-point coordinates
    - `eigenvalues`: array of arrays, each inner array containing the slab band eigenvalues in eV
  - `items`: object
  - `required_columns`:
  - `units`:
    - `k_path`: dimensionless (surface BZ coordinates)
    - `eigenvalues`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "kpath": "array of objects, each with 'label' (string) and 'k' (array of 3 floats, fractional coordinates)",
          "eigenvalues": "array of arrays, each inner array of 4 floats representing the 4 band energies in eV",
          "node_line_points": "array of arrays of 3 floats, fractional coordinates of the closed node line"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "eigenvalues": "eV",
          "k": "dimensionless (fractional)",
          "node_line_points": "dimensionless (fractional)"
        }
      },
      "description": "Bulk tight-binding band structure and identified node line points."
    },
    {
      "file": "berry_phase_zigzag.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "k_parallel": "array of arrays of 2 floats (k2, k3) in fractional coordinates",
          "berry_phase": "array of floats, Berry phase in units of π"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "k_parallel": "dimensionless (fractional)",
          "berry_phase": "unit of π"
        }
      },
      "description": "Berry phase computed for the zigzag termination as a function of in-plane momentum."
    },
    {
      "file": "surface_band_beard.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "k_path": "array of arrays of 2 floats, surface BZ k-point coordinates",
          "eigenvalues": "array of arrays, each inner array containing the slab band eigenvalues in eV"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "k_path": "dimensionless (surface BZ coordinates)",
          "eigenvalues": "eV"
        }
      },
      "description": "Surface band structure of the beard-terminated (100) slab."
    }
  ]
}
```

## How you are scored
A hidden verifier inspects each of the three output files. It recomputes key structural and quantitative features from your raw JSON artifacts and compares these against a hidden reference derived from the paper. Each stage is scored independently, and the final reward is the weighted sum of these scores. Reporting a plausible final number is not sufficient; the submitted raw data must pass the structural and quantitative checks applied by the verifier.