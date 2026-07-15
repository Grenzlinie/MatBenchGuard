# Two-Dimensional Borophene Mechanical and Superconducting Properties Calculation

## Problem background
Bilayer δ6 borophene (BL-δ6) is a two-dimensional boron allotrope formed by AB‑stacked δ6 monolayers with covalent interlayer bonds. Due to its strong directional σ‑bonds and delocalised metallic bonding, this material is predicted to exhibit exceptional in‑plane mechanical stiffness and phonon‑mediated superconductivity. Understanding its elastic constants and superconducting critical temperature (Tc), and how these are affected by applied tensile strain, is key to evaluating its potential for nanoscale applications. This reproduction task computes the independent in‑plane elastic constants, the derived Young’s moduli, and the anisotropic superconducting critical temperature of BL‑δ6 at zero strain and under 13% uniaxial tensile strain along the a‑axis.

## Approach
The workflow uses first-principles density functional theory (DFT) and many-body electron‑phonon coupling calculations:

1. **Structure optimisation** – Optimise the atomic geometry of BL‑δ6 to obtain equilibrium lattice constants and atomic positions.
2. **Elastic properties** – Apply small strain distortions and fit the resulting strain‑energy curves to extract the four independent in‑plane elastic constants (C11, C22, C12, C44). From these, derive the in‑plane Young’s moduli Ya and Yb.
3. **Electronic structure and Wannier interpolation** – Compute the DFT band structure and generate maximally localised Wannier functions (Wannier90) that faithfully interpolate the electronic states near the Fermi level, providing the necessary input for the electron‑phonon coupling stage.
4. **Phonons and electron‑phonon coupling** – Calculate the phonon dispersion using density‑functional perturbation theory (DFPT) and compute the electron‑phonon coupling matrix elements with the EPW code. From these, obtain the Eliashberg spectral function α²F(ω) and the total electron‑phonon coupling parameter.
5. **Anisotropic superconducting Tc** – Solve the fully anisotropic Migdal‑Eliashberg equations to obtain the momentum‑dependent superconducting gap and the critical temperature for both the unstrained system and the system under 13% uniaxial tensile strain along the a‑axis. The strain‑dependent pathway requires repeating the electronic structure, Wannier interpolation, phonon, and coupling calculations on the strained geometry.

## Reproduction target
The objective is to compute and report the following quantities for BL‑δ6:

- The four independent in‑plane elastic constants C11, C22, C12, C44 (in N/m) and the derived Young’s moduli Ya and Yb (in N/m), obtained from DFT strain‑energy fitting.
- The anisotropic Migdal‑Eliashberg critical temperature Tc for the unstrained structure (in K).
- The anisotropic Migdal‑Eliashberg critical temperature Tc for the structure under 13% uniaxial tensile strain along the a‑axis (in K).

All values must be computed using the described DFT + Wannier90 + EPW pipeline and saved to the specified JSON output files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: http://www.wannier.org/
- Electron-Phonon Wannier (EPW): https://epw-code.org/

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: Optimize the atomic structure of BL-δ6 (AB-stacked δ6 monolayers with initial lattice constants a=3.243 Å, b=2.883 Å) using density-functional theory to obtain equilibrium lattice constants and atomic positions.
- Evidence: none

### Step 2: Elastic constants calculation
- Role: scored
- Action: Compute the four independent in-plane elastic constants C11, C22, C12, C44 by fitting strain-energy curves from DFT calculations with applied strain distortions. Derive the in-plane Young’s moduli Ya and Yb. Write the results to elastic_constants.json.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"C11": float (N/m), "C22": float, "C12": float, "C44": float, "Ya": float, "Yb": float}
- Scoring: scored by hidden verifier

### Step 3: Electronic structure and Wannier interpolation
- Role: process
- Action: Perform a DFT band structure calculation on the relaxed BL-δ6 and generate maximally localized Wannier functions (Wannier90) to interpolate the electronic states, producing the necessary input for EPW.
- Evidence: none

### Step 4: Phonon dispersion and electron-phonon coupling
- Role: process
- Action: Compute the phonon dispersion and electron-phonon coupling matrix elements using density-functional perturbation theory (DFPT) and EPW, obtaining the Eliashberg spectral function α2F(ω) and total EPC parameter λ.
- Evidence: none

### Step 5: Anisotropic Tc at zero strain
- Role: scored (load-bearing)
- Action: Solve the fully anisotropic Migdal-Eliashberg equations using EPW to obtain the momentum-dependent superconducting gap and the critical temperature Tc of unstrained BL-δ6. Write the result to tc_zero_strain.json.
- Output file: `/app/outputs/tc_zero_strain.json`
- Format: json
- Contract: {"Tc_anisotropic_ME": float (K)}
- Scoring: scored by hidden verifier

### Step 6: Strain-dependent electronic and phonon calculations
- Role: process
- Action: Generate a BL-δ6 structure under 13% uniaxial tensile strain along the a-axis, relax internal coordinates, then compute electronic structure, Wannier interpolation, phonon dispersion, and electron-phonon coupling for the strained system, preparing all necessary inputs for the Tc calculation.
- Evidence: none

### Step 7: Anisotropic Tc at 13% strain
- Role: scored (load-bearing)
- Action: Solve the anisotropic Migdal-Eliashberg equations for the 13% strained structure to obtain the critical temperature. Write the result to tc_thirteen_strain.json.
- Output file: `/app/outputs/tc_thirteen_strain.json`
- Format: json
- Contract: {"Tc_anisotropic_ME": float (K)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/tc_zero_strain.json`
- `/app/outputs/tc_thirteen_strain.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed elastic constants and Young's moduli; compared to the paper-reported reference values with a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `C11`: number
    - `C22`: number
    - `C12`: number
    - `C44`: number
    - `Ya`: number
    - `Yb`: number
  - `units`:
    - `C11`: N/m
    - `C22`: N/m
    - `C12`: N/m
    - `C44`: N/m
    - `Ya`: N/m
    - `Yb`: N/m

### tc_zero_strain.json
- path: `/app/outputs/tc_zero_strain.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Anisotropic Migdal-Eliashberg Tc at zero strain; compared to the paper-reported value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Tc_anisotropic_ME`: number
  - `units`:
    - `Tc_anisotropic_ME`: K

### tc_thirteen_strain.json
- path: `/app/outputs/tc_thirteen_strain.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Anisotropic Tc under 13% tensile strain along a; compared to the paper-reported value and monotonic increase with strain is verified.
- schema:
  - `type`: object
  - `required`:
    - `Tc_anisotropic_ME`: number
  - `units`:
    - `Tc_anisotropic_ME`: K

Notes: All scored outputs are JSON files containing the computed physical quantities. The hidden checker will compare these values against the paper's reported results, using appropriate tolerances to account for implementation differences. The checker will also verify that Tc increases under tensile strain, consistent with the paper's conclusion.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "number",
          "C22": "number",
          "C12": "number",
          "C44": "number",
          "Ya": "number",
          "Yb": "number"
        },
        "units": {
          "C11": "N/m",
          "C22": "N/m",
          "C12": "N/m",
          "C44": "N/m",
          "Ya": "N/m",
          "Yb": "N/m"
        }
      },
      "description": "Computed elastic constants and Young's moduli; compared to the paper-reported reference values with a tolerance."
    },
    {
      "file": "tc_zero_strain.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc_anisotropic_ME": "number"
        },
        "units": {
          "Tc_anisotropic_ME": "K"
        }
      },
      "description": "Anisotropic Migdal-Eliashberg Tc at zero strain; compared to the paper-reported value within a tolerance."
    },
    {
      "file": "tc_thirteen_strain.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc_anisotropic_ME": "number"
        },
        "units": {
          "Tc_anisotropic_ME": "K"
        }
      },
      "description": "Anisotropic Tc under 13% tensile strain along a; compared to the paper-reported value and monotonic increase with strain is verified."
    }
  ],
  "notes": "All scored outputs are JSON files containing the computed physical quantities. The hidden checker will compare these values against the paper's reported results, using appropriate tolerances to account for implementation differences. The checker will also verify that Tc increases under tensile strain, consistent with the paper's conclusion."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden verifier. The verifier compares the computed elastic constants, Young’s moduli, and the two critical temperature values to reference results using appropriate tolerances. For the strain‑dependent Tc, the verifier also checks that the critical temperature at 13% tensile strain is larger than the zero‑strain value, consistent with the expected physical trend. The final reward is a weighted combination of the scores from the three scored artifacts. Simply reporting a number without having executed the DFT and electron‑phonon pipeline is not sufficient.
