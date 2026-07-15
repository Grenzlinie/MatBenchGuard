# DFT Band Gap and Structural Properties of Zinc-Blende Nitrides and Alloys

## Problem background
BTlGaN quaternary alloys are being investigated as materials for infrared optoelectronic devices. A key open question is whether a composition can achieve lattice matching to GaN while tuning the band gap into the infrared. At the same time, the reliability of density functional theory (DFT) for predicting structural and electronic properties of these alloys is best established by first benchmarking against the known binary compounds GaN, BN, and TlN. This task evaluates those predictions by computing several structural, electronic, and optical quantities with an open‑source DFT code.

## Approach
The workflow employs the full‑potential linearized augmented plane wave (FP‑LAPW) method, implemented in the open‑source code **exciting**. Structural properties (equilibrium lattice constants and bulk moduli) are obtained from total‑energy vs. volume calculations with the GGA‑WC functional, fitted with the Murnaghan equation of state. Electronic band structures are then computed using the TB‑mBJ exchange potential, which gives accurate band gaps. From the band structure, direct and indirect band gaps are extracted. For the quaternary alloy, a 32‑atom supercell of zinc‑blende GaN is constructed and atoms substituted to reach the target composition, followed by atomic‑position relaxation with GGA‑WC. The relaxed geometry is used to compute the band structure and the real part of the dielectric function. The static dielectric constant is read at zero frequency, and the static refractive index is obtained as its square root. The final required numbers are collected into a JSON file for verification.

## Reproduction target
You must compute and report the following quantities in a single JSON file `/app/outputs/results.json`:

- For each zinc‑blende binary compound **GaN**, **BN**, and **TlN**:
  - equilibrium lattice constant a₀ (Å) and bulk modulus B₀ (GPa)
  - direct band gap at Γ (E_Γ–Γ, eV) and indirect band gap Γ–X (E_Γ–X, eV)
- For the quaternary alloy with composition **B₀.₁₂₅Tl₀.₁₈₇Ga₀.₆₈₈N**:
  - equilibrium lattice constant a₀ (Å)
  - direct band gap at Γ (E_Γ–Γ, eV)
  - static dielectric constant ε₁(0)
  - static refractive index n(0)

The exact JSON schema is given in the Output contract below.

## Assets

- exciting (FP-LAPW DFT code): https://exciting-code.org/

## Workflow steps

### Step 1: Binary structural benchmark (GaN, BN, TlN)
- Role: process
- Action: For zinc-blende GaN, BN, and TlN, perform DFT total energy calculations with the GGA-WC functional at a series of unit cell volumes. Fit the energy–volume data with the Murnaghan equation of state to obtain equilibrium lattice constant a0 and bulk modulus B0. Save the energy–volume data as evidence.
- Evidence: `/app/outputs/energy_volume_data.json`

### Step 2: Binary electronic benchmark (GaN, BN, TlN)
- Role: process
- Action: Using the equilibrium structures from step 1, compute the electronic band structure with the TB-mBJ exchange potential. Extract the direct band gap at Γ (E_Γ–Γ) and the indirect gap at Γ–X (E_Γ–X) for each compound. Save the band structure data as evidence.
- Evidence: `/app/outputs/band_data.json`

### Step 3: Alloy supercell construction and relaxation
- Role: process
- Action: Build a 32-atom supercell (2×2×2) of zinc-blende GaN. Substitute atoms to reach the composition B₀.₁₂₅Tl₀.₁₈₇Ga₀.₆₈₈N. Relax atomic positions using GGA-WC to obtain the equilibrium lattice constant. Save the optimized geometry as evidence.
- Evidence: `/app/outputs/alloy_optimized_structure.json`

### Step 4: Alloy band structure calculation
- Role: process
- Action: Compute the electronic band structure of the relaxed alloy supercell with TB-mBJ. Extract the direct band gap at Γ (E_Γ–Γ). Save the band structure data as evidence.
- Evidence: `/app/outputs/alloy_band_data.json`

### Step 5: Alloy optical properties calculation
- Role: process
- Action: Using the electronic structure from step 4, compute the real part of the dielectric function ε₁(ω) with TB-mBJ. Extract the static dielectric constant ε₁(0) and compute the static refractive index n(0) = √(ε₁(0)). Save the optical data as evidence.
- Evidence: `/app/outputs/optical_data.json`

### Step 6: Compile final reproduction results
- Role: scored (load-bearing)
- Action: Gather all required quantities from the previous steps and write them to results.json. Binary compounds: a₀ (Å), B₀ (GPa), E_Γ–Γ (eV), E_Γ–X (eV). Quaternary alloy: a₀ (Å), E_Γ–Γ (eV), ε₁(0), n(0).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: binary_compounds: list of objects with keys: compound (string), a0_Angstrom (float), B0_GPa (float), E_gamma_gamma_eV (float), E_gamma_X_eV (float); quaternary: object with keys: a0_Angstrom (float), E_gamma_gamma_eV (float), eps1_0 (float), n0 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed scalar quantities for the binary benchmark compounds (GaN, BN, TlN) and the quaternary B₀.₁₂₅Tl₀.₁₈₇Ga₀.₆₈₈N alloy. Values are compared against hidden paper-reported references with tolerances.
- schema:
  - `type`: object
  - `required`: `binary_compounds`, `quaternary`
  - `properties`:
    - `binary_compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `compound`, `a0_Angstrom`, `B0_GPa`, `E_gamma_gamma_eV`, `E_gamma_X_eV`
        - `properties`:
          - `compound`:
            - `type`: string
          - `a0_Angstrom`:
            - `type`: number
          - `B0_GPa`:
            - `type`: number
          - `E_gamma_gamma_eV`:
            - `type`: number
          - `E_gamma_X_eV`:
            - `type`: number
    - `quaternary`:
      - `type`: object
      - `required`: `a0_Angstrom`, `E_gamma_gamma_eV`, `eps1_0`, `n0`
      - `properties`:
        - `a0_Angstrom`:
          - `type`: number
        - `E_gamma_gamma_eV`:
          - `type`: number
        - `eps1_0`:
          - `type`: number
        - `n0`:
          - `type`: number

Notes: The binaries must include GaN, BN, and TlN. The quaternary is the lattice-matched composition specified in the action. All values are to be computed from the DFT calculations described in the process steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "binary_compounds",
          "quaternary"
        ],
        "properties": {
          "binary_compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "compound",
                "a0_Angstrom",
                "B0_GPa",
                "E_gamma_gamma_eV",
                "E_gamma_X_eV"
              ],
              "properties": {
                "compound": {
                  "type": "string"
                },
                "a0_Angstrom": {
                  "type": "number"
                },
                "B0_GPa": {
                  "type": "number"
                },
                "E_gamma_gamma_eV": {
                  "type": "number"
                },
                "E_gamma_X_eV": {
                  "type": "number"
                }
              }
            }
          },
          "quaternary": {
            "type": "object",
            "required": [
              "a0_Angstrom",
              "E_gamma_gamma_eV",
              "eps1_0",
              "n0"
            ],
            "properties": {
              "a0_Angstrom": {
                "type": "number"
              },
              "E_gamma_gamma_eV": {
                "type": "number"
              },
              "eps1_0": {
                "type": "number"
              },
              "n0": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Computed scalar quantities for the binary benchmark compounds (GaN, BN, TlN) and the quaternary B₀.₁₂₅Tl₀.₁₈₇Ga₀.₆₈₈N alloy. Values are compared against hidden paper-reported references with tolerances."
    }
  ],
  "notes": "The binaries must include GaN, BN, and TlN. The quaternary is the lattice-matched composition specified in the action. All values are to be computed from the DFT calculations described in the process steps."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json`. It extracts each reported quantity and compares it against a hidden reference value. Each quantity is scored individually; the verifier uses tolerances that account for the expected spread between different DFT implementations. The overall reward is a weighted combination of these per‑quantity scores. The verifier may also check that the intermediate evidence files exist and are consistent with the final numbers, but the primary scoring comes from `results.json`.
