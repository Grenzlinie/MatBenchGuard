# Lattice Thermal Conductivity of 2D Carbon Nitride Allotropes: DFT and Phonon BTE Reproduction

## Problem background
It is widely documented that lone-pair electrons in a material strengthen phonon anharmonicity and thereby suppress lattice thermal conductivity. However, recent computational investigations of two-dimensional carbon nitride allotropes have challenged this conventional understanding. The present investigation focuses on four two-dimensional systems: graphene, planar C₃N, penta-graphene, and penta-CN₂. The first two are planar hexagonal structures; the latter two are non-planar pentagonal structures. Substituting carbon with nitrogen in these frameworks introduces lone-pair electrons. The central question is how these lone-pair electrons affect the lattice thermal conductivity in each structural environment. The goal is to compute and compare the room-temperature lattice thermal conductivity (κ_L) and the optimized structural parameters for all four materials, thereby determining whether lone-pair electrons always reduce thermal transport or can, in specific geometries, enhance it.

## Approach
The computational protocol uses first-principles density functional theory (DFT) to relax the unit cells of graphene, planar C₃N, penta-graphene, and penta-CN₂. From the optimized geometries, harmonic and anharmonic (third-order) interatomic force constants are obtained via finite displacements or density-functional perturbation theory. These force constants are then input to the iterative solution of the linearized phonon Boltzmann transport equation, yielding the lattice thermal conductivity at 300 K. The same DFT parameters (pseudopotential quality, exchange-correlation functional, energy cutoffs) are applied consistently to enable a direct comparison. The conceptual framework is a systematic comparison of two structural topologies (planar hexagonal vs. pentagonal) each with and without nitrogen substitution. This isolates the role of lone-pair electrons on phonon scattering while holding the parent carbon framework constant. The required steps follow a standard multi-stage pipeline: geometry relaxation, harmonic force constants, anharmonic third-order force constants, Boltzmann transport solution, and structural-parameter extraction.

## Reproduction target
Produce two primary scored output files:

1. **thermal_conductivity_results.json** – contains the room-temperature (300 K) lattice thermal conductivity κ_L (in W m⁻¹ K⁻¹) for graphene, planar C₃N, penta-graphene, and penta-CN₂, computed via the iterative solution of the phonon Boltzmann transport equation.

2. **optimized_structures.json** – contains the relaxed lattice constant a, inter-layer distance h (where applicable), bond lengths l₁ and l₂, and bond angles θ₁ and θ₂ (where applicable) for each material, as defined in the paper's Table 1.

The target includes both the absolute numerical values and the relative ordering of κ_L between the two pentagonal materials and between the two planar materials. The computational procedure itself is the reproduction; the output artifacts are compared against a hidden reference.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- ShengBTE: https://www.shengbte.org/
- SSSP pseudopotential library (recommended) or equivalent PBE/PAW potentials: https://www.materialscloud.org/discover/sssp/
- Initial atomic structures (graphene, planar C3N, penta-graphene, penta-CN2)

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT structural relaxation for the unit cells of graphene, planar C3N, penta-graphene, and penta-CN2 to obtain optimized lattice constants and atomic positions.
- Evidence: `/app/outputs/relax_outputs.log`

### Step 2: Harmonic force constants
- Role: process
- Action: Compute harmonic interatomic force constants (IFCs) using density-functional perturbation theory (DFPT) or finite displacements, employing Quantum ESPRESSO + phonopy.
- Evidence: `/app/outputs/harmonic_ifc.dat`

### Step 3: Anharmonic third-order force constants
- Role: process
- Action: Calculate the anharmonic third‑order interatomic force constants using the finite displacement method (supercells) with the same DFT settings.
- Evidence: `/app/outputs/anharmonic_ifc.dat`

### Step 4: Solve phonon BTE and compute lattice thermal conductivity
- Role: scored (load-bearing)
- Action: Use ShengBTE (iterative method) to solve the linearized phonon Boltzmann transport equation at 300 K for the four materials and output the room‑temperature lattice thermal conductivity (κ_L) in a JSON file.
- Output file: `/app/outputs/thermal_conductivity_results.json`
- Format: json
- Contract: {"graphene": {"kappa_300K": float}, "planar_C3N": {"kappa_300K": float}, "penta_graphene": {"kappa_300K": float}, "penta_CN2": {"kappa_300K": float}}
- Scoring: scored by hidden verifier

### Step 5: Extract optimized structural parameters
- Role: scored
- Action: From the relaxed geometries of step 1, extract the lattice constant a, inter‑layer distance h, bond lengths l₁ and l₂, and bond angles θ₁ and θ₂ (where applicable) and save them in a JSON file.
- Output file: `/app/outputs/optimized_structures.json`
- Format: json
- Contract: {"graphene": {"a": float, "l1": float}, "planar_C3N": {"a": float, "l1": float, "l2": float}, "penta_graphene": {"a": float, "h": float, "l1": float, "l2": float, "theta1": float, "theta2": float}, "penta_CN2": {"a": float, "h": float, "l1": float, "l2": float, "theta1": float, "theta2": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_results.json`
- `/app/outputs/optimized_structures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_results.json
- path: `/app/outputs/thermal_conductivity_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Room‑temperature (300 K) lattice thermal conductivity for the four materials, obtained from the iterative solution of the phonon BTE. Units: W m⁻¹ K⁻¹.
- schema:
  - `type`: object
  - `required`:
    - `graphene`: object
    - `planar_C3N`: object
    - `penta_graphene`: object
    - `penta_CN2`: object
  - `properties`:
    - `graphene`:
      - `kappa_300K`: float
    - `planar_C3N`:
      - `kappa_300K`: float
    - `penta_graphene`:
      - `kappa_300K`: float
    - `penta_CN2`:
      - `kappa_300K`: float

### optimized_structures.json
- path: `/app/outputs/optimized_structures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constants and structural parameters extracted from the DFT ground‑state geometries.
- schema:
  - `type`: object
  - `required`:
    - `graphene`: object
    - `planar_C3N`: object
    - `penta_graphene`: object
    - `penta_CN2`: object
  - `properties`:
    - `graphene`:
      - `a`: float (lattice constant in Å)
      - `l1`: float (C–C bond length in Å)
    - `planar_C3N`:
      - `a`: float
      - `l1`: float (C–C bond length)
      - `l2`: float (C–N bond length)
    - `penta_graphene`:
      - `a`: float
      - `h`: float (inter‑layer distance in Å)
      - `l1`: float
      - `l2`: float
      - `theta1`: float (bond angle in degrees)
      - `theta2`: float
    - `penta_CN2`:
      - `a`: float
      - `h`: float
      - `l1`: float
      - `l2`: float
      - `theta1`: float
      - `theta2`: float

Notes: The checker compares the reported κ_L to the hidden gold within a 30% relative tolerance and verifies the correct ordering (penta‑CN₂ > penta‑graphene; planar C₃N < graphene). Structural parameters are checked within 2% of the paper‑reported values. Full credit requires both tolerance and trend conditions; partial credit may be awarded for correct trend alone.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "graphene": "object",
          "planar_C3N": "object",
          "penta_graphene": "object",
          "penta_CN2": "object"
        },
        "properties": {
          "graphene": {
            "kappa_300K": "float"
          },
          "planar_C3N": {
            "kappa_300K": "float"
          },
          "penta_graphene": {
            "kappa_300K": "float"
          },
          "penta_CN2": {
            "kappa_300K": "float"
          }
        }
      },
      "description": "Room‑temperature (300 K) lattice thermal conductivity for the four materials, obtained from the iterative solution of the phonon BTE. Units: W m⁻¹ K⁻¹."
    },
    {
      "file": "optimized_structures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "graphene": "object",
          "planar_C3N": "object",
          "penta_graphene": "object",
          "penta_CN2": "object"
        },
        "properties": {
          "graphene": {
            "a": "float (lattice constant in Å)",
            "l1": "float (C–C bond length in Å)"
          },
          "planar_C3N": {
            "a": "float",
            "l1": "float (C–C bond length)",
            "l2": "float (C–N bond length)"
          },
          "penta_graphene": {
            "a": "float",
            "h": "float (inter‑layer distance in Å)",
            "l1": "float",
            "l2": "float",
            "theta1": "float (bond angle in degrees)",
            "theta2": "float"
          },
          "penta_CN2": {
            "a": "float",
            "h": "float",
            "l1": "float",
            "l2": "float",
            "theta1": "float",
            "theta2": "float"
          }
        }
      },
      "description": "Optimized lattice constants and structural parameters extracted from the DFT ground‑state geometries."
    }
  ],
  "notes": "The checker compares the reported κ_L to the hidden gold within a 30% relative tolerance and verifies the correct ordering (penta‑CN₂ > penta‑graphene; planar C₃N < graphene). Structural parameters are checked within 2% of the paper‑reported values. Full credit requires both tolerance and trend conditions; partial credit may be awarded for correct trend alone."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact.

- For **thermal_conductivity_results.json**, the verifier checks the reported κ_L values against a hidden reference and verifies that the required relative ordering between the pentagonal pair and between the planar pair is correctly reproduced.
- For **optimized_structures.json**, the verifier checks the reported lattice parameters and bond geometries against expected values.

The two scores are combined into a final reward between 0 and 1. Partial credit may be awarded for correct trends even if individual values deviate somewhat. To earn full credit, the entire workflow must be executed to produce both artifacts; simply guessing or reporting numbers without performing the calculations is not sufficient.
