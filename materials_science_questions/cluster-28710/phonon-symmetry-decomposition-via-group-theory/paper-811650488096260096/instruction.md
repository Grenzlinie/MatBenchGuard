# Multilayered Spherical Particle Modal Analysis and Group Theory Decomposition

## Problem background
Nuclear fuel for High Temperature Reactors (HTR) is encapsulated in sub-millimeter spherical particles composed of a fuel kernel coated with several protective layers: a porous pyrocarbon buffer, an inner dense pyrocarbon (IPyC), a silicon carbide (SiC) shell, and an outer dense pyrocarbon (OPyC). The SiC layer is the primary fission-product barrier; a crack in this layer would compromise containment. Non-destructive evaluation by laser ultrasonics detects embedded cracks through changes in the particle's vibration spectrum. The computational counterpart of this technique involves finite element modelling of the elastic eigenfrequencies of multilayered spheres and group-theoretical classification of the normal modes. This task reproduces the numerical determination of eigenfrequencies for both defect-free and cracked particles, and the decomposition of spheroidal (S) and torsional (T) modes into irreducible representations under the reduced symmetry introduced by a meridian crack.

## Approach
The work is divided into three independent computational stages.

**Finite element eigenfrequency analysis (defect-free).** A perfect multilayered spherical particle is modelled using three-dimensional linear elasticity. The geometry and material properties are defined as follows: the particle has an overall diameter of 1.00 mm, consisting of a ZrO₂ core (radius 312.5 μm), a porous pyrocarbon (PPyC) layer (thickness 84 μm), an inner dense pyrocarbon (IPyC) layer (29.5 μm), a SiC layer (37 μm), and an outer dense pyrocarbon (OPyC) layer (37 μm). Each material is isotropic and characterised by its Young's modulus E, density ρ, and Poisson's ratio ν:
  - ZrO₂: E = 200 GPa, ρ = 5900 kg/m³, ν = 0.25
  - PPyC: E = 7.5 GPa, ρ = 1050 kg/m³, ν = 0.30
  - IPyC: E = 15 GPa, ρ = 1900 kg/m³, ν = 0.30
  - SiC: E = 450 GPa, ρ = 3180 kg/m³, ν = 0.15
  - OPyC: E = 15 GPa, ρ = 1900 kg/m³, ν = 0.30
Ideal bonding between layers and a stress-free outer surface are assumed. The eigenproblem is solved with a finite element toolchain (Gmsh for mesh generation, CalculiX for the solve). Normal modes are identified as spheroidal (nS_L) or torsional (nT_L) from their displacement patterns, and the mean eigenfrequency of each multiplet is recorded. Because the absolute frequencies scale inversely with size, the results are also computed for a 1.20 mm particle by multiplying the 1.00 mm frequencies by 1.00/1.20.

**Cracked-particle eigenfrequency analysis.** A second finite element model introduces a crack in the SiC shell of the 1.00 mm particle. The crack is a 50 μm wide × 500 μm long slit lying in a meridian plane and filled with material having the properties of dense pyrocarbon (IPyC). The presence of the crack reduces the symmetry to the C₂v (2m) point group. After solving the eigenproblem, each mode is assigned to an irreducible representation (A₁, A₂, B₁, B₂) by inspecting the modal displacement field with respect to the symmetry operations of C₂v. The resulting eigenfrequencies and irrep labels are gathered for the multiplets 2S₁, 1S₂, 1S₃, 1S₄ and 1T₂.

**Group-theoretical decomposition.** Independently of any simulation, the splitting of the spheroidal (S_L) and torsional (T_L) representations, for L ≤ 2, is analytically reduced into irreducible representations of the C₂v point group. The character table of C₂v (identity E, C₂ rotation, and two mirror planes σ(zx) and σ(yz)) is used. The characters for a given mode type are: χ(E) = 2L+1; χ(C₂) = (−1)^{L}; and for reflection planes χ(σ) = +1 for spheroidal modes and −1 for torsional modes. The decomposition formula a_i = (1/g) Σ n_R χ_i(R) χ(R) (with g = 4, n_R = 1 for all classes) yields the spanning irreps for each original multiplet. The results are collected for S₀, S₁, S₂, T₁, and T₂.

## Reproduction target
Produce the following three scored artifacts:

1. **`defect_free_frequencies.csv`** – Eigenfrequencies (kHz) of the defect-free multilayered sphere for diameters 1.00 mm and 1.20 mm, with each row giving the spectroscopic mode label (e.g. 2S₁, 1T₂) and the mean multiplet frequency.

2. **`cracked_split_frequencies.csv`** – Eigenfrequencies (kHz) of the 1.00 mm particle containing a crack in the SiC shell. Each row reports the original multiplet label (2S₁, 1S₂, 1S₃, 1S₄, 1T₂), the C₂v irreducible representation (A₁, A₂, B₁, B₂) assigned to that split mode, and its frequency.

3. **`group_theory_decomposition.csv`** – The irreducible representation decomposition of the vibrational modes under C₂v symmetry. Each row corresponds to an original mode (S₀, S₁, S₂, T₁, T₂) and the spanning irreps as a space-separated sum (e.g. "2A₁+A₂+B₁+B₂").

## Assets

- Gmsh: http://gmsh.info/
- CalculiX: http://www.calculix.de/
- NumPy: numpy
- SymPy: sympy

## Workflow steps

### Step 1: Compute defect-free eigenfrequencies
- Role: scored (load-bearing)
- Action: Build a finite element mesh of a multilayered spherical particle using the layer thicknesses and material properties from the paper's Table 1 (diameter 1.00 mm). Solve the linear elastic eigenproblem for normal modes (spheroidal and torsional) and label each mode by its spectroscopic notation (nS_L, nT_L). Compute the mean eigenfrequency for each multiplet. Scale the resulting frequencies to a diameter 1.20 mm by multiplying by 1.00/1.20. Output both diameter sets in a CSV file.
- Output file: `/app/outputs/defect_free_frequencies.csv`
- Format: csv
- Contract: columns: diameter_mm (float), mode_label (string), frequency_kHz (float). One row per mode per diameter. Example: 1.00, 2S1, <computed_frequency_kHz>; 1.20, 2S1, <scaled_frequency_kHz>.
- Scoring: scored by hidden verifier

### Step 2: Compute cracked-particle eigenfrequencies
- Role: scored (load-bearing)
- Action: Construct a finite element model of the same particle (diameter 1.00 mm) but with a crack in the SiC shell: width 50 μm, length 500 μm, oriented along a meridian plane, filled with dense pyrocarbon. Solve the eigenproblem and assign each mode to an irreducible representation (A1, A2, B1, B2) of the C2v point group by inspecting modal symmetry. Output the eigenfrequencies of the split modes for multiplets 2S1, 1S2, 1S3, 1S4, 1T2.
- Output file: `/app/outputs/cracked_split_frequencies.csv`
- Format: csv
- Contract: columns: multiplet_label (string), irrep_label (string), frequency_kHz (float). One row per split mode. Example: 1S2, A1, <frequency_kHz>; 1S2, B2, <frequency_kHz>.
- Scoring: scored by hidden verifier

### Step 3: Group theory decomposition
- Role: scored
- Action: Using the character table of the 2m (C2v) point group, compute the decomposition of the spheroidal (S_L) and torsional (T_L) representations for L ≤ 2 into irreducible representations A1, A2, B1, B2. Determine the spanning irreps for each mode (S0, S1, S2, T1, T2) and output the result.
- Output file: `/app/outputs/group_theory_decomposition.csv`
- Format: csv
- Contract: columns: original_mode (string), spanning_irreps (string). One row per mode. Example: S0, A1. The spanning_irreps for other modes are provided as space-separated sums of irrep labels with their counts (e.g., "A1+B1+B2").
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_free_frequencies.csv`
- `/app/outputs/cracked_split_frequencies.csv`
- `/app/outputs/group_theory_decomposition.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_free_frequencies.csv
- path: `/app/outputs/defect_free_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Eigenfrequencies of a defect-free multilayered spherical particle for diameters 1.00 mm and 1.20 mm.
- schema:
  - `type`: table
  - `required_columns`: `diameter_mm`, `mode_label`, `frequency_kHz`
  - `units`:
    - `diameter_mm`: mm
    - `frequency_kHz`: kHz

### cracked_split_frequencies.csv
- path: `/app/outputs/cracked_split_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Eigenfrequencies of the cracked particle with irrep assignments.
- schema:
  - `type`: table
  - `required_columns`: `multiplet_label`, `irrep_label`, `frequency_kHz`
  - `units`:
    - `frequency_kHz`: kHz

### group_theory_decomposition.csv
- path: `/app/outputs/group_theory_decomposition.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Irreducible representation decomposition of S_L and T_L modes under C2v symmetry.
- schema:
  - `type`: table
  - `required_columns`: `original_mode`, `spanning_irreps`

Notes: All eigenfrequencies are in kHz. Mode labels follow spectroscopic notation. Irrep labels are A1, A2, B1, B2; spanning_irreps contains a space-separated list of irreps with counts (e.g. '2A1+A2+B1+B2').

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_free_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diameter_mm",
          "mode_label",
          "frequency_kHz"
        ],
        "units": {
          "diameter_mm": "mm",
          "frequency_kHz": "kHz"
        }
      },
      "description": "Eigenfrequencies of a defect-free multilayered spherical particle for diameters 1.00 mm and 1.20 mm."
    },
    {
      "file": "cracked_split_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "multiplet_label",
          "irrep_label",
          "frequency_kHz"
        ],
        "units": {
          "frequency_kHz": "kHz"
        }
      },
      "description": "Eigenfrequencies of the cracked particle with irrep assignments."
    },
    {
      "file": "group_theory_decomposition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "original_mode",
          "spanning_irreps"
        ]
      },
      "description": "Irreducible representation decomposition of S_L and T_L modes under C2v symmetry."
    }
  ],
  "notes": "All eigenfrequencies are in kHz. Mode labels follow spectroscopic notation. Irrep labels are A1, A2, B1, B2; spanning_irreps contains a space-separated list of irreps with counts (e.g. '2A1+A2+B1+B2')."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each output file. The frequencies in the defect-free and cracked-particle tables are compared to reference values; an appropriate numerical tolerance is applied to account for differences in mesh, solver, and floating-point arithmetic. The irrep assignments in the cracked-particle and group-theory files are checked for correctness. The total reward is a weighted sum of the per‑artifact scores, with the two frequency tables carrying the largest weight, followed by the group‑theory decomposition. Reporting a plausible value without actually running the required computations would not pass the verifier's checks.
