# DFT electronic structure and orbital-resolved DOS of CuAlS2

## Problem background
Ternary chalcopyrite semiconductors with formula $A^I B^{III} C^{VI}_2$ are important for nonlinear optics and photovoltaics due to their wide band gaps and high nonlinear coefficients. First-principles calculations based on density functional theory (DFT) can predict electronic band structures, density of states (DOS), and optical constants such as the dielectric function and refractive index. For CuAlS₂, a representative member, the band edges and the orbital composition of the valence and conduction bands determine the optical response. This task requires you to produce DFT-derived electronic and optical properties for CuAlS₂ and submit the computed quantities as plain-text and CSV outputs.

## Approach
Use the open‑source plane‑wave pseudopotential code Quantum ESPRESSO with the GGA‑PBE exchange‑correlation functional. Starting from the experimental crystal structure (chalcopyrite, space group I‑42d, a=5.3336 Å, c=10.4440 Å), run a non‑spin‑polarized self‑consistent field (SCF) calculation with appropriate pseudopotentials for Cu, Al, and S. From the SCF eigenvalues and wavefunctions, extract the direct band gap at the Γ point. Then compute the total DOS and orbital‑projected DOS (Cu s, p, d; Al s, p, d; S s, p) using a Gaussian smearing. Calculate the real and imaginary parts of the dielectric function in the independent‑particle approximation, and finally obtain the zero‑energy refractive index from $n=\sqrt{\varepsilon_1(0)}$. All outputs are to be written as files under `/app/outputs` according to the step specifications below.

## Reproduction target
Produce the following five artifacts for CuAlS₂:

1.  A text file containing the direct band gap at Γ (eV) without any scissor operator.
2.  A CSV file of the total density of states (energy in eV, total DOS in states/eV) covering the energy range –20 eV to +15 eV relative to the valence band maximum.
3.  A CSV file of the orbital‑projected DOS (energy, Cu_s, Cu_p, Cu_d, Al_s, Al_p, Al_d, S_s, S_p) over the same energy range.
4.  A CSV file of the dielectric function (energy, ε₁, ε₂) over 0–20 eV.
5.  A text file containing the refractive index $n(0)=\sqrt{\varepsilon_1(0)}$.

The checker will verify that the band gap and refractive index fall within a reasonable range of independently obtained values and that the DOS and dielectric function satisfy specific orbital‑composition and shape criteria.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- Standard solid-state pseudopotentials (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT SCF calculation for CuAlS2
- Role: process
- Action: Run a non-spin-polarized DFT self-consistent field calculation for CuAlS2 in the chalcopyrite structure (space group I-42d, experimental lattice constants a=5.3336 Å, c=10.4440 Å) using Quantum ESPRESSO with GGA-PBE functional and appropriate pseudopotentials. Use a converged k-point grid and plane-wave cutoff to obtain accurate Kohn–Sham eigenvalues, wavefunctions, and charge density. This step produces the electronic structure required for all downstream analyses.
- Evidence: `/app/outputs/scf.log`

### Step 2: Extract direct band gap at Γ
- Role: scored
- Action: From the DFT eigenvalues determine the top of the valence band and bottom of the conduction band at the Γ point; compute the direct band gap in eV and write the value as a single float to the output file.
- Output file: `/app/outputs/band_gap_CuAlS2.txt`
- Format: txt
- Contract: Single float number in eV.
- Scoring: scored by hidden verifier

### Step 3: Total density of states (DOS)
- Role: scored
- Action: Compute the total density of states from the electronic eigenvalues using a Gaussian smearing of 0.25 eV, covering an energy range from -20 to 15 eV relative to the valence band maximum. Write a CSV with columns: energy (eV), total DOS (states/eV).
- Output file: `/app/outputs/dos_total_CuAlS2.csv`
- Format: csv
- Contract: CSV with columns: energy (numeric), total_DOS (numeric). Rows ordered by increasing energy.
- Scoring: scored by hidden verifier

### Step 4: Orbital-projected density of states (PDOS)
- Role: scored (load-bearing)
- Action: Compute the projected density of states onto atomic orbitals for Cu (s, p, d), Al (s, p, d), and S (s, p) using the same energy range and smearing. Write a CSV with columns: energy, Cu_s, Cu_p, Cu_d, Al_s, Al_p, Al_d, S_s, S_p (all in states/eV).
- Output file: `/app/outputs/dos_partial_CuAlS2.csv`
- Format: csv
- Contract: CSV with columns: energy (numeric), Cu_s (numeric), Cu_p (numeric), Cu_d (numeric), Al_s (numeric), Al_p (numeric), Al_d (numeric), S_s (numeric), S_p (numeric).
- Scoring: scored by hidden verifier

### Step 5: Dielectric function
- Role: scored
- Action: Compute the real (ε1) and imaginary (ε2) parts of the dielectric function using the independent-particle approximation from the DFT wavefunctions and energies, with an energy range from 0 to 20 eV and a suitable broadening. Write a CSV with columns: energy (eV), epsilon1, epsilon2.
- Output file: `/app/outputs/dielectric_function_CuAlS2.csv`
- Format: csv
- Contract: CSV with columns: energy (numeric), epsilon1 (numeric), epsilon2 (numeric).
- Scoring: scored by hidden verifier

### Step 6: Refractive index at zero energy
- Role: scored
- Action: Extract the zero-energy (ω → 0) refractive index n from the low-energy limit of the real dielectric function: n = sqrt(ε1(0)). Write the value as a single float to the output file.
- Output file: `/app/outputs/refractive_index_CuAlS2.txt`
- Format: txt
- Contract: Single float: refractive index n.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_CuAlS2.txt`
- `/app/outputs/dos_total_CuAlS2.csv`
- `/app/outputs/dos_partial_CuAlS2.csv`
- `/app/outputs/dielectric_function_CuAlS2.csv`
- `/app/outputs/refractive_index_CuAlS2.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_CuAlS2.txt
- path: `/app/outputs/band_gap_CuAlS2.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed direct band gap without scissor operator.
- schema:
  - `type`: text
  - `description`: Single float value representing the direct band gap at Γ in eV.

### dos_total_CuAlS2.csv
- path: `/app/outputs/dos_total_CuAlS2.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total density of states for CuAlS2.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_DOS`
  - `units`:
    - `energy`: eV
    - `total_DOS`: states/eV

### dos_partial_CuAlS2.csv
- path: `/app/outputs/dos_partial_CuAlS2.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Orbital-projected DOS for CuAlS2.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `Cu_s`, `Cu_p`, `Cu_d`, `Al_s`, `Al_p`, `Al_d`, `S_s`, `S_p`
  - `units`:
    - `energy`: eV
    - `Cu_s`: states/eV
    - `Cu_p`: states/eV
    - `Cu_d`: states/eV
    - `Al_s`: states/eV
    - `Al_p`: states/eV
    - `Al_d`: states/eV
    - `S_s`: states/eV
    - `S_p`: states/eV

### dielectric_function_CuAlS2.csv
- path: `/app/outputs/dielectric_function_CuAlS2.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Real and imaginary parts of the dielectric function.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `epsilon1`, `epsilon2`
  - `units`:
    - `energy`: eV
    - `epsilon1`: dimensionless
    - `epsilon2`: dimensionless

### refractive_index_CuAlS2.txt
- path: `/app/outputs/refractive_index_CuAlS2.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Refractive index from low-energy limit of ε1.
- schema:
  - `type`: text
  - `description`: Single float value: refractive index n(ω→0).

Notes: All energy values are relative to the valence band maximum. Band gap and refractive index are compared to the paper's values; DOS and dielectric function are verified structurally by integrating over specified energy windows to confirm orbital composition and peak positions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_CuAlS2.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single float value representing the direct band gap at Γ in eV."
      },
      "description": "Computed direct band gap without scissor operator."
    },
    {
      "file": "dos_total_CuAlS2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_DOS"
        ],
        "units": {
          "energy": "eV",
          "total_DOS": "states/eV"
        }
      },
      "description": "Total density of states for CuAlS2."
    },
    {
      "file": "dos_partial_CuAlS2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "Cu_s",
          "Cu_p",
          "Cu_d",
          "Al_s",
          "Al_p",
          "Al_d",
          "S_s",
          "S_p"
        ],
        "units": {
          "energy": "eV",
          "Cu_s": "states/eV",
          "Cu_p": "states/eV",
          "Cu_d": "states/eV",
          "Al_s": "states/eV",
          "Al_p": "states/eV",
          "Al_d": "states/eV",
          "S_s": "states/eV",
          "S_p": "states/eV"
        }
      },
      "description": "Orbital-projected DOS for CuAlS2."
    },
    {
      "file": "dielectric_function_CuAlS2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
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
      "description": "Real and imaginary parts of the dielectric function."
    },
    {
      "file": "refractive_index_CuAlS2.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single float value: refractive index n(ω→0)."
      },
      "description": "Refractive index from low-energy limit of ε1."
    }
  ],
  "notes": "All energy values are relative to the valence band maximum. Band gap and refractive index are compared to the paper's values; DOS and dielectric function are verified structurally by integrating over specified energy windows to confirm orbital composition and peak positions."
}
```

## How you are scored
Each of the five scored files is evaluated independently by a hidden verifier. The band gap and refractive index are compared against reference values within tolerances that account for differences between DFT codes. The total and partial DOS files are audited for structural correctness: for example, the conduction band (3.5–10.5 eV) must be dominated by Cu and Al s and p states, the upper valence band (–2 to 0 eV) by Cu d states split into e and t₂ components, and the deep band near –15 eV by Al d states. The dielectric function is checked for smoothness and plausible peak positions. Each check contributes a portion of the total reward (a float between 0 and 1). Reporting only the final numbers without genuinely performing the DFT workflow is unlikely to pass the structural audits.
