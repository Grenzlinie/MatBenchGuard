# DFT calculation of Sr3P4O13 electronic and optical properties

## Problem background
The solid-state compound Sr3P4O13 is a layered phosphate built from SrO7 polyhedra and P4O13 chains. Its electronic structure and optical response are of interest for potential applications as a transparent material. First-principles density functional theory (DFT) calculations can characterize the band structure, density of states, dielectric function, and refractive index, providing insight into the bonding nature and predicting key material properties. This task asks you to compute these quantities from the crystal structure using DFT.

## Approach
The calculation uses plane-wave DFT with the local density approximation (LDA) functional and norm-conserving pseudopotentials. The workflow consists of a self-consistent field (SCF) calculation, a non-self-consistent band structure and density-of-states calculation (total and atom-projected), and a linear optical response calculation to obtain the dielectric tensor. From these results, the direct band gap, the static dielectric constant, the principal static refractive indices, and the projected densities of states are extracted. An open-source DFT code (e.g., Quantum ESPRESSO) is used as the computational engine.

## Crystal structure of Sr3P4O13

The crystal structure of Sr3P4O13 is triclinic, space group P-1 (No. 2). The lattice parameters are:
- a = 7.2755 Å
- b = 7.7260 Å
- c = 10.1935 Å
- α = 102.28°
- β = 103.46°
- γ = 94.35°

The unit cell contains 2 formula units (Z=2). Fractional atomic coordinates (from single-crystal X-ray diffraction) are given below. Use these positions for the DFT calculation.

```
Sr1   0.24861  0.98443  0.24312
Sr2   0.29161  0.78097 -0.13614
Sr3   0.21542  1.22782  0.62632
P1    0.3627   0.5397   0.1418
P2    0.3287   0.8092   0.5129
P3    0.1746   1.1909  -0.0214
P4   -0.1374   0.5373  -0.3474
O1    0.3366   1.1000   0.0466
O2    0.1551   0.8966   0.4551
O3    0.1187   1.1196  -0.1786
O4    0.2633   0.3985   0.0004
O5    0.3975   0.8718   0.6670
O6    0.3691   0.7179   0.1096
O7    0.4742   0.8186   0.4300
O8    0.0657   0.5124  -0.3173
O9    0.2542   0.5980   0.4867
O10   0.0100   1.1924   0.0439
O11  -0.1812   0.7178  -0.3636
O12   0.2092   0.5323   0.2303
O13   0.5450   0.4899   0.2125
```

## Reproduction target
Using the provided crystal structure (unit cell parameters and fractional atomic coordinates) of Sr3P4O13, perform plane-wave DFT calculations with the LDA functional and norm-conserving pseudopotentials. Compute and report:
- the direct band gap (in eV),
- the static dielectric constant ε(0),
- the three static refractive index components n_x, n_y, n_z,
- and a CSV table of the total density of states and the projected densities of states for O-2p, P-3p, and Sr-5s as a function of energy.
All outputs must be deposited under /app/outputs as specified in the workflow steps below.

## Assets

- Quantum ESPRESSO or equivalent open-source DFT package: https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Sr, P, O: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Run DFT calculation on Sr3P4O13
- Role: process
- Action: Using the provided crystal structure (unit cell parameters and fractional coordinates), set up and run a plane-wave DFT calculation with LDA functional and norm-conserving pseudopotentials. Perform self-consistent field (SCF) calculation, followed by non-self-consistent band structure and density of states (total and atom-projected) calculations, and compute the dielectric function (real and imaginary parts). The chosen code must output the Kohn-Sham eigenvalues, total and partial DOS, and optical dielectric tensor.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: Compute direct band gap
- Role: scored
- Action: From the DFT band structure, determine the direct band gap (in eV) at the Γ point (or the smallest direct gap if not at Γ) and write the value to the output file.
- Output file: `/app/outputs/step_01_band_gap.txt`
- Format: txt
- Contract: One floating-point number.
- Scoring: scored by hidden verifier

### Step 3: Compute static dielectric constant
- Role: scored
- Action: Extract the static (ω→0) real part of the dielectric function, ε(0) ≡ ε1(0), and write the value (scalar, averaged over polarization directions if the code provides components) to the output file.
- Output file: `/app/outputs/step_02_dielectric_constant.txt`
- Format: txt
- Contract: One floating-point number.
- Scoring: scored by hidden verifier

### Step 4: Compute static refractive index components
- Role: scored
- Action: From the dielectric tensor components ε_xx(0), ε_yy(0), ε_zz(0), compute the principal refractive indices n_x = √ε_xx, n_y = √ε_yy, n_z = √ε_zz at ω=0, and write them as three space-separated floats.
- Output file: `/app/outputs/step_03_refractive_index.txt`
- Format: txt
- Contract: Three space-separated floats.
- Scoring: scored by hidden verifier

### Step 5: Extract density of states table
- Role: scored (load-bearing)
- Action: From the DFT total and partial density of states output, produce a CSV table with columns: Energy(eV), TotalDOS, O_p, P_p, Sr_s. The energy range should cover the valence and low conduction bands (e.g., from -6 eV to +6 eV relative to the Fermi level). O_p corresponds to oxygen 2p projected DOS, P_p to phosphorus 3p, and Sr_s to strontium 5s (summed over all atoms).
- Output file: `/app/outputs/step_04_dos_data.csv`
- Format: csv
- Contract: CSV with header: Energy(eV),TotalDOS,O_p,P_p,Sr_s.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gap.txt`
- `/app/outputs/step_02_dielectric_constant.txt`
- `/app/outputs/step_03_refractive_index.txt`
- `/app/outputs/step_04_dos_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gap.txt
- path: `/app/outputs/step_01_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Direct band gap of Sr3P4O13 calculated by DFT.
- schema:
  - `type`: text
  - `description`: one floating-point number in eV

### step_02_dielectric_constant.txt
- path: `/app/outputs/step_02_dielectric_constant.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Static dielectric constant ε(0) of Sr3P4O13.
- schema:
  - `type`: text
  - `description`: one floating-point number (static dielectric constant)

### step_03_refractive_index.txt
- path: `/app/outputs/step_03_refractive_index.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Static refractive index components of Sr3P4O13.
- schema:
  - `type`: text
  - `description`: three space-separated floats: nx ny nz

### step_04_dos_data.csv
- path: `/app/outputs/step_04_dos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total and projected DOS; used to verify that O-2p and P-3p dominate valence bands, and Sr-5s dominates conduction band bottom.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `TotalDOS`, `O_p`, `P_p`, `Sr_s`

Notes: The DFT run is the central computational reproduction. Scalar outputs are compared to reference values with appropriate tolerances. The DOS step is load-bearing: a structurally correct DOS requires a completed DFT calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "one floating-point number in eV"
      },
      "description": "Direct band gap of Sr3P4O13 calculated by DFT."
    },
    {
      "file": "step_02_dielectric_constant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "one floating-point number (static dielectric constant)"
      },
      "description": "Static dielectric constant ε(0) of Sr3P4O13."
    },
    {
      "file": "step_03_refractive_index.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "three space-separated floats: nx ny nz"
      },
      "description": "Static refractive index components of Sr3P4O13."
    },
    {
      "file": "step_04_dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "TotalDOS",
          "O_p",
          "P_p",
          "Sr_s"
        ]
      },
      "description": "Total and projected DOS; used to verify that O-2p and P-3p dominate valence bands, and Sr-5s dominates conduction band bottom."
    }
  ],
  "notes": "The DFT run is the central computational reproduction. Scalar outputs are compared to reference values with appropriate tolerances. The DOS step is load-bearing: a structurally correct DOS requires a completed DFT calculation."
}
```

## How you are scored
A hidden verifier will independently examine each scored output file. For the scalar quantities (band gap, dielectric constant, and refractive indices), your computed values are compared to hidden reference values derived from the scientific literature, with tolerances that account for differences in DFT implementation and pseudopotentials. For the density-of-states CSV, the verifier performs a structural audit: it checks that O-2p and P-3p states dominate the occupied valence region, and that Sr-5s states dominate the bottom of the conduction band, confirming that a genuine DFT calculation was performed. The final reward combines the scores from all four outputs.
