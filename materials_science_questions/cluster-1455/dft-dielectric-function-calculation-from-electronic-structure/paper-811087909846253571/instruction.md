# DFT structural, electronic, and optical properties of BTlGaN quaternary alloys

## Problem background
BTlGaN quaternary alloys are investigated as candidate semiconductor materials for infrared optoelectronic devices such as laser diodes and LEDs. A key challenge is to mitigate the lattice mismatch between high Tl-content GaN layers and a GaN substrate while achieving narrow band gaps suitable for infrared emission. Incorporating small amounts of boron is proposed to compensate the lattice strain. This task reproduces the first-principles density functional theory (DFT) study that predicts the structural, electronic, and optical properties of zinc-blende B_xTl_yGa_{1-x-y}N alloys lattice matched to GaN.

## Approach
All computations are performed with an open‑source all‑electron full‑potential linearized augmented plane wave (FP‑LAPW) code such as Elk. The exchange‑correlation functional for structural properties is the Wu–Cohen generalized gradient approximation (GGA‑WC); for electronic and optical properties, the Tran–Blaha modified Becke–Johnson (TB‑mBJ) potential and the Perdew–Burke–Ernzerhof (GGA‑PBE) functional are used. The workflow covers: (1) building zinc‑blende unit cells for the binary compounds GaN, BN, and TlN, and 32‑atom supercells for quaternary B_xTl_yGa_{1‑x‑y}N alloys; (2) structural relaxation and equation‑of‑state fitting to obtain equilibrium lattice constants and bulk moduli; (3) band‑structure calculations for binary and quaternary systems to extract direct and indirect band gaps; and (4) computation of the complex dielectric function ε(ω)=ε1(ω)+iε2(ω) from momentum matrix elements, followed by Kramers–Kronig transformation to obtain the real part.

## Reproduction target
Use an open‑source FP‑LAPW code to compute four sets of quantities:
1. Equilibrium lattice constants (a0) and bulk moduli (B0) for zinc‑blende GaN, BN, and TlN, obtained from GGA‑WC total‑energy vs. volume curves fitted with the Murnaghan equation of state.
2. Direct Γ–Γ and indirect Γ–X band gaps for the same three binaries, computed with both GGA‑PBE and TB‑mBJ functionals.
3. Direct Γ–Γ band gap for zinc‑blende B_xTl_yGa_{1‑x‑y}N alloys using TB‑mBJ, for composition (x=0.125, y=0.187) and at least one other composition.
4. The complex dielectric function ε1(ω) and ε2(ω) for the quaternary alloys with y=0.187 and x = 0, 0.062, 0.125, 0.187. The static dielectric constant (ε1 at zero energy) and its trend with x should be derived from the submitted data.
All results must be written to the specified output CSV files under /app/outputs.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.io/
- Elk atomic data / pseudopotentials: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Build initial crystal structures
- Role: process
- Action: Generate zinc-blende unit cells for GaN, BN, TlN and 32-atom supercells for B_xTl_yGa_{1-x-y}N with compositions (0.125,0.187) and at least one other.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Binary structural relaxation and EOS
- Role: scored
- Action: Perform DFT structural relaxation with GGA-WC, compute total energy vs. volume, fit Murnaghan equation of state, and extract equilibrium a0 and B0 for GaN, BN, TlN.
- Output file: `/app/outputs/binary_structural.csv`
- Format: csv
- Contract: Columns: compound (GaN, BN, TlN), a0 (Angstrom), B0 (GPa). One row per compound.
- Scoring: scored by hidden verifier

### Step 3: Binary band gaps
- Role: scored
- Action: Compute band structures using GGA-PBE and TB-mBJ for the relaxed binary structures; extract direct Γ-Γ and indirect Γ-X gaps.
- Output file: `/app/outputs/binary_bandgaps.csv`
- Format: csv
- Contract: Columns: compound, gap_type (direct/indirect), GGA_PBE_gap (eV), TB_mBJ_gap (eV). One row per gap type.
- Scoring: scored by hidden verifier

### Step 4: Relax quaternary alloy supercells
- Role: process
- Action: Perform DFT structural relaxation with GGA-WC on the B_xTl_yGa_{1-x-y}N 32-atom supercells to obtain equilibrium lattice constants for the chosen compositions.
- Evidence: `/app/outputs/quaternary_a0.csv`

### Step 5: Quaternary direct band gaps
- Role: scored (load-bearing)
- Action: Compute the band structure for the relaxed quaternary supercells using TB-mBJ, and extract the direct Γ-Γ band gap for at least two compositions, including x=0.125, y=0.187.
- Output file: `/app/outputs/quaternary_bandgap.csv`
- Format: csv
- Contract: Columns: x (B fraction), y (Tl fraction), direct_gap (eV). One row per composition.
- Scoring: scored by hidden verifier

### Step 6: Density of states analysis
- Role: process
- Action: Compute total and partial density of states (TDOS, PDOS) for the prototype composition B0.187Tl0.187Ga0.626N using TB-mBJ.
- Evidence: `/app/outputs/dos_B0.187Tl0.187Ga0.626N.csv`

### Step 7: Dielectric function of quaternary alloys
- Role: scored
- Action: Compute the complex dielectric function (ε1, ε2) from momentum matrix elements and Kramers-Kronig transformation for y=0.187 and x=0, 0.062, 0.125, 0.187 using TB-mBJ; output data for photon energies 0-30 eV.
- Output file: `/app/outputs/optical_dielectric_function.csv`
- Format: csv
- Contract: Columns: x, energy (eV), epsilon1, epsilon2. Rows cover the energy range 0-30 eV for each x=0,0.062,0.125,0.187.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binary_structural.csv`
- `/app/outputs/binary_bandgaps.csv`
- `/app/outputs/quaternary_bandgap.csv`
- `/app/outputs/optical_dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binary_structural.csv
- path: `/app/outputs/binary_structural.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constants and bulk moduli for zinc-blende GaN, BN, TlN, to be compared with paper Table 1 values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a0`, `B0`
  - `units`:
    - `a0`: Angstrom
    - `B0`: GPa

### binary_bandgaps.csv
- path: `/app/outputs/binary_bandgaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct and indirect band gaps for binary GaN, BN, TlN using GGA-PBE and TB-mBJ, compared to paper Table 2 values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `gap_type`, `GGA_PBE_gap`, `TB_mBJ_gap`
  - `units`:
    - `GGA_PBE_gap`: eV
    - `TB_mBJ_gap`: eV

### quaternary_bandgap.csv
- path: `/app/outputs/quaternary_bandgap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct Γ-Γ band gaps of BxTlyGa1-x-yN alloys for at least two compositions, compared to paper Figure 3 extracted values.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `direct_gap`
  - `units`:
    - `direct_gap`: eV

### optical_dielectric_function.csv
- path: `/app/outputs/optical_dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Real and imaginary parts of the dielectric function for y=0.187 and x=0,0.062,0.125,0.187; checker will verify that the static dielectric constant (average ε1 over 0–0.5 eV) increases with B composition x, and inspect ε2 peak positions qualitatively.
- schema:
  - `type`: table
  - `required_columns`: `x`, `energy`, `epsilon1`, `epsilon2`
  - `units`:
    - `energy`: eV
    - `epsilon1`: dimensionless
    - `epsilon2`: dimensionless

Notes: The agent must use an open-source FP-LAPW code (e.g., Elk). No fixed numerical parameters are mandated; convergence is the agent's responsibility. The checker compares computed values to paper‑reported gold within domain‑appropriate tolerances and verifies optical trends. Gold values and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binary_structural.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a0",
          "B0"
        ],
        "units": {
          "a0": "Angstrom",
          "B0": "GPa"
        }
      },
      "description": "Equilibrium lattice constants and bulk moduli for zinc-blende GaN, BN, TlN, to be compared with paper Table 1 values within tolerances."
    },
    {
      "file": "binary_bandgaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "gap_type",
          "GGA_PBE_gap",
          "TB_mBJ_gap"
        ],
        "units": {
          "GGA_PBE_gap": "eV",
          "TB_mBJ_gap": "eV"
        }
      },
      "description": "Direct and indirect band gaps for binary GaN, BN, TlN using GGA-PBE and TB-mBJ, compared to paper Table 2 values."
    },
    {
      "file": "quaternary_bandgap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "direct_gap"
        ],
        "units": {
          "direct_gap": "eV"
        }
      },
      "description": "Direct Γ-Γ band gaps of BxTlyGa1-x-yN alloys for at least two compositions, compared to paper Figure 3 extracted values."
    },
    {
      "file": "optical_dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "energy",
          "epsilon1",
          "epsilon2"
        ],
        "units": {
          "energy": "eV",
          "epsilon1": "dimensionless",
          "epsilon2": "dimensionless"
        }
      },
      "description": "Real and imaginary parts of the dielectric function for y=0.187 and x=0,0.062,0.125,0.187; checker will verify that the static dielectric constant (average ε1 over 0–0.5 eV) increases with B composition x, and inspect ε2 peak positions qualitatively."
    }
  ],
  "notes": "The agent must use an open-source FP-LAPW code (e.g., Elk). No fixed numerical parameters are mandated; convergence is the agent's responsibility. The checker compares computed values to paper‑reported gold within domain‑appropriate tolerances and verifies optical trends. Gold values and tolerances are hidden."
}
```

## How you are scored
Your submission consists of the four scored artifacts listed in the Workflow steps. A hidden verifier reads each artifact and independently checks the computed quantities against expected reference values. Verification methods include:
- Comparing reported lattice constants and bulk moduli to reference values.
- Comparing reported TB‑mBJ band gaps to reference values.
- Comparing reported quaternary direct band gaps to reference values.
- For the dielectric function, computing the static dielectric constant (average ε1 over 0–0.5 eV) from your data and verifying that it increases with increasing boron concentration x; the verifier also inspects the position and shape of ε2 peaks.
Each stage is weighted, and the final reward is a weighted combination of the stage scores. The verifier uses tolerances appropriate for a legitimate re‑run of the computational workflow. Simply reporting the correct numbers without performing the actual DFT calculations will not suffice, because the verifier performs independent checks on your raw outputs.
