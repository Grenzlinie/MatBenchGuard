# DFT computation of phonon properties for SrAl2H2 and SrAlSiH

## Problem background
Solid‑state aluminum hydrides are investigated as potential hydrogen‑storage materials. Understanding the nature of Al–H bonding is central to controlling their stability and decomposition. The polyanionic hydrides SrAl2H2 and SrAlSiH contain Al–H units embedded in a two‑dimensional layer, with Al bonded to either further Al atoms or to Si. Their vibrational spectra provide direct signatures of bond strengths and anharmonicities. This task requires computing from first principles the equilibrium crystal structures, the optical phonon frequencies at the Brillouin zone centre, and the anharmonic shift of the Al–H stretching mode in SrAlSiH, thereby quantifying the lattice dynamics and the degree of anharmonicity of the Al–H bond.

## Approach
The computational approach employs density functional theory (DFT) with a plane‑wave basis and GGA‑PBE exchange‑correlation functional, using an open‑source code such as Quantum ESPRESSO. The workflow proceeds in three stages:

1. **Structure relaxation:** Starting from the experimentally reported lattice parameters and atomic coordinates, both unit cells (SrAl2H2 in space group P‑3m1 and SrAlSiH in P3m1) are fully relaxed until pressure and forces vanish. This yields the theoretical equilibrium lattice constants and internal positions.

2. **Γ‑point phonons:** For each compound a 3×3×3 supercell is built from the relaxed cell. After a re‑optimisation of internal degrees of freedom (using Γ‑point sampling for SrAlSiH and a 2×2×2 Monkhorst–Pack grid for metallic SrAl2H2), the direct (finite‑displacement) method is applied: every atom is displaced by ±0.01 Å along the Cartesian axes, Hellmann–Feynman forces are collected, and the force‑constant matrix is constructed. Diagonalising the dynamical matrix at the Γ point gives the optical phonon frequencies.

3. **Anharmonicity of the Al–H stretch:** For SrAlSiH, the H atom is displaced stepwise along the Al–H bond direction (the crystallographic z‑axis). DFT total energies are computed at each displacement, and the curve is fitted to a fourth‑order polynomial U = a x² – b x³ + c x⁴. Solving the one‑dimensional Schrödinger equation for this potential yields the ground state energy E0 and the first two excited states E1, E2. From these the fundamental frequency ω1 = (E1‑E0)/ħ, the first overtone ω2 = (E2‑E0)/ħ, and the anharmonic shift Δ = 2ω1 – ω2 are derived.

## Reproduction target
Produce the following three scored artifacts:

- **geometry_relaxation.json** – the DFT‑relaxed lattice parameters a, c and the fractional z‑coordinates of Al, H (and Si for SrAlSiH) for both compounds.
- **gamma_frequencies.json** – the optical phonon frequencies (cm⁻¹) at the Γ point for SrAl2H2 and SrAlSiH, labelled according to the mode‑type assignments specified in the output schema.
- **anharmonicity.json** – the fitted potential energies E0, E1, E2 (eV), the fundamental and overtone frequencies ω1, ω2 (cm⁻¹), and the anharmonic shift Δ = 2ω1 – ω2 (cm⁻¹) for the Al–H stretching mode in SrAlSiH.

All outputs must conform to the exact JSON schemas detailed in the output contract.

## Assets

- Quantum ESPRESSO (or other plane-wave DFT code): https://www.quantum-espresso.org
- GGA (PBE) ultrasoft pseudopotentials: https://www.materialscloud.org/discover/sssp/
- Python 3 with NumPy and SciPy: python3, numpy, scipy

## Workflow steps

### Step 1: Structure relaxation
- Role: scored
- Action: Perform DFT geometry optimization for the unit cells of SrAl2H2 (space group P-3m1) and SrAlSiH (P3m1), starting from the experimental lattice parameters and atomic coordinates given in the literature. Relax both lattice constants and internal coordinates to zero pressure and zero force. Report the final equilibrium lattice parameters a, c and the fractional z-coordinates of Al, H (and Si for SrAlSiH).
- Output file: `/app/outputs/geometry_relaxation.json`
- Format: json
- Contract: JSON object with keys "SrAl2H2" and "SrAlSiH". SrAl2H2 fields: a (float, Å), c (float, Å), Al_z (float, fractional), H_z (float, fractional). SrAlSiH fields: a (float, Å), c (float, Å), Al_z (float, fractional), Si_z (float, fractional), H_z (float, fractional).
- Scoring: scored by hidden verifier

### Step 2: Gamma-point phonon frequencies
- Role: scored (load-bearing)
- Action: Build a 3×3×3 supercell from the relaxed unit cell of each compound. Re-optimize internal coordinates (Γ‑point sampling for SrAlSiH, 2×2×2 k‑mesh for SrAl2H2). Apply the direct method: displace each atom by ±0.01 Å along Cartesian directions, compute Hellmann-Feynman forces, construct the force‑constant matrix, and diagonalize the dynamical matrix at the Γ point. Extract all optical phonon frequencies.
- Output file: `/app/outputs/gamma_frequencies.json`
- Format: json
- Contract: JSON object with keys "SrAl2H2" and "SrAlSiH". SrAl2H2 fields: E_Sr, A_Sr, A_outofplane_stretch, E_inplane_stretch, E_AlH_bend1, E_AlH_bend2, A_AlH_stretch1, A_AlH_stretch2 (all float, cm⁻¹). SrAlSiH fields: E_Sr, A_Sr, A_outofplane_stretch, E_inplane_stretch, E_AlH_bend, A_AlH_stretch (all float, cm⁻¹).
- Scoring: scored by hidden verifier

### Step 3: Al–H stretching anharmonicity
- Role: scored
- Action: Using the relaxed SrAlSiH unit cell, displace the H atom along the Al–H bond direction (z-axis) in small steps. Compute DFT total energies at each displacement, fit a polynomial U = a x² – b x³ + c x⁴, solve the one-dimensional Schrödinger equation to obtain ground state energy E0, first excited state E1, and second excited state E2. From these calculate ω1 = (E1-E0)/ħ, ω2 = (E2-E0)/ħ, and the anharmonic shift Δ = 2ω1 – ω2.
- Output file: `/app/outputs/anharmonicity.json`
- Format: json
- Contract: JSON object with key "SrAlSiH". Value is an object with fields: E0 (float, eV), E1 (float, eV), E2 (float, eV), omega1 (float, cm⁻¹), omega2 (float, cm⁻¹), Delta (float, cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometry_relaxation.json`
- `/app/outputs/gamma_frequencies.json`
- `/app/outputs/anharmonicity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometry_relaxation.json
- path: `/app/outputs/geometry_relaxation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final relaxed DFT lattice constants and internal atomic coordinates for both compounds.
- schema:
  - `type`: object
  - `required`: `SrAl2H2`, `SrAlSiH`
  - `properties`:
    - `SrAl2H2`:
      - `type`: object
      - `required`: `a`, `c`, `Al_z`, `H_z`
      - `properties`:
        - `a`: number (Å)
        - `c`: number (Å)
        - `Al_z`: number (fractional)
        - `H_z`: number (fractional)
    - `SrAlSiH`:
      - `type`: object
      - `required`: `a`, `c`, `Al_z`, `Si_z`, `H_z`
      - `properties`:
        - `a`: number (Å)
        - `c`: number (Å)
        - `Al_z`: number (fractional)
        - `Si_z`: number (fractional)
        - `H_z`: number (fractional)

### gamma_frequencies.json
- path: `/app/outputs/gamma_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Γ‑point optical phonon frequencies obtained from the direct method.
- schema:
  - `type`: object
  - `required`: `SrAl2H2`, `SrAlSiH`
  - `properties`:
    - `SrAl2H2`:
      - `type`: object
      - `required`: `E_Sr`, `A_Sr`, `A_outofplane_stretch`, `E_inplane_stretch`, `E_AlH_bend1`, `E_AlH_bend2`, `A_AlH_stretch1`, `A_AlH_stretch2`
      - `units`: cm⁻¹
    - `SrAlSiH`:
      - `type`: object
      - `required`: `E_Sr`, `A_Sr`, `A_outofplane_stretch`, `E_inplane_stretch`, `E_AlH_bend`, `A_AlH_stretch`
      - `units`: cm⁻¹

### anharmonicity.json
- path: `/app/outputs/anharmonicity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Anharmonicity results for the Al–H stretching mode in SrAlSiH.
- schema:
  - `type`: object
  - `required`: `SrAlSiH`
  - `properties`:
    - `SrAlSiH`:
      - `type`: object
      - `required`: `E0`, `E1`, `E2`, `omega1`, `omega2`, `Delta`
      - `units`:
        - `E0`: eV
        - `E1`: eV
        - `E2`: eV
        - `omega1`: cm⁻¹
        - `omega2`: cm⁻¹
        - `Delta`: cm⁻¹

Notes: All outputs are compared against the published DFT results as reference values. Tolerances account for typical code‑to‑code variation in plane‑wave DFT.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometry_relaxation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "SrAl2H2",
          "SrAlSiH"
        ],
        "properties": {
          "SrAl2H2": {
            "type": "object",
            "required": [
              "a",
              "c",
              "Al_z",
              "H_z"
            ],
            "properties": {
              "a": "number (Å)",
              "c": "number (Å)",
              "Al_z": "number (fractional)",
              "H_z": "number (fractional)"
            }
          },
          "SrAlSiH": {
            "type": "object",
            "required": [
              "a",
              "c",
              "Al_z",
              "Si_z",
              "H_z"
            ],
            "properties": {
              "a": "number (Å)",
              "c": "number (Å)",
              "Al_z": "number (fractional)",
              "Si_z": "number (fractional)",
              "H_z": "number (fractional)"
            }
          }
        }
      },
      "description": "Final relaxed DFT lattice constants and internal atomic coordinates for both compounds."
    },
    {
      "file": "gamma_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "SrAl2H2",
          "SrAlSiH"
        ],
        "properties": {
          "SrAl2H2": {
            "type": "object",
            "required": [
              "E_Sr",
              "A_Sr",
              "A_outofplane_stretch",
              "E_inplane_stretch",
              "E_AlH_bend1",
              "E_AlH_bend2",
              "A_AlH_stretch1",
              "A_AlH_stretch2"
            ],
            "units": "cm⁻¹"
          },
          "SrAlSiH": {
            "type": "object",
            "required": [
              "E_Sr",
              "A_Sr",
              "A_outofplane_stretch",
              "E_inplane_stretch",
              "E_AlH_bend",
              "A_AlH_stretch"
            ],
            "units": "cm⁻¹"
          }
        }
      },
      "description": "Γ‑point optical phonon frequencies obtained from the direct method."
    },
    {
      "file": "anharmonicity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "SrAlSiH"
        ],
        "properties": {
          "SrAlSiH": {
            "type": "object",
            "required": [
              "E0",
              "E1",
              "E2",
              "omega1",
              "omega2",
              "Delta"
            ],
            "units": {
              "E0": "eV",
              "E1": "eV",
              "E2": "eV",
              "omega1": "cm⁻¹",
              "omega2": "cm⁻¹",
              "Delta": "cm⁻¹"
            }
          }
        }
      },
      "description": "Anharmonicity results for the Al–H stretching mode in SrAlSiH."
    }
  ],
  "notes": "All outputs are compared against the published DFT results as reference values. Tolerances account for typical code‑to‑code variation in plane‑wave DFT."
}
```

## How you are scored
A hidden verifier independently checks each of the three JSON artifacts against reference DFT results. The comparison uses tolerances that account for typical code‑to‑code variations in plane‑wave pseudopotential calculations. Each stage is awarded a score reflecting how closely the computed values match the reference, and the three scores are combined with predetermined weights to form the final task reward. You must execute the entire workflow honestly; simply inserting published target numbers will not pass the verifier's hidden checks, which audit internal consistency and tolerances that a trivial copy cannot satisfy.
