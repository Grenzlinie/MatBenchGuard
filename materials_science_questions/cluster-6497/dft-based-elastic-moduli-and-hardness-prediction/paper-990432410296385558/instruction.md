# Mechanical properties and anisotropic superconducting transition of bilayer δ₆ borophene from first principles

## Problem background
Two-dimensional materials that combine metallic conductivity with covalent bonding can host phonon-mediated superconductivity and exceptional mechanical stiffness. Bilayer δ₆ borophene (BL‑δ₆) is a recently proposed polymorph consisting of two AB‑stacked δ₆ monolayers interlinked by covalent bonds. First‑principles calculations predict that the coexistence of directional σ‑bonds and delocalized multicenter bonds in this structure yields large in‑plane stiffness and a conventional superconducting transition mediated by electron–phonon coupling. The task is to reproduce the computed mechanical constants and the anisotropic superconducting critical temperature (Tc) of BL‑δ₆ for both the equilibrium geometry and under tensile strain.

## Approach
The reproduction follows a first‑principles density‑functional‑theory (DFT) workflow. The equilibrium structure of BL‑δ₆ is built from published lattice parameters and relaxed by variable‑cell DFT. In‑plane elastic constants are obtained via stress‑strain relations under small lattice distortions, and Young’s moduli are derived from them. Electronic structure calculations and Wannier interpolation provide a compact Hamiltonian for electron–phonon coupling (EPC). Phonon dispersions are computed with density‑functional perturbation theory. Finally, the anisotropic Migdal–Eliashberg equations are solved using the EPW code to obtain the momentum‑resolved superconducting gap and Tc. The pipeline is executed twice: once for the relaxed unstrained configuration and once for a configuration where the armchair lattice constant is increased by 13% (with internal coordinates relaxed). All calculations use open‑source plane‑wave codes (Quantum ESPRESSO, Wannier90, EPW) and a standard boron pseudopotential.

## Reproduction target
Produce three JSON artifact files:

- **elastic_constants.json** – four independent in‑plane elastic constants C11, C22, C12, C44 (units N/m).
- **young_moduli.json** – in‑plane Young’s moduli Ya (armchair direction) and Yb (zigzag direction) in N/m.
- **superconducting_tc.json** – anisotropic superconducting critical temperatures Tc_unstrained and Tc_strained_13_percent (units K) for the unstrained BL‑δ₆ and for 13% tensile strain along the armchair direction.

All quantities must be computed from the DFT+EPW pipeline; they must not be copied from any external source. The agent’s own code produces these numbers from scratch.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- EPW: https://epw-code.org/
- Wannier90: https://wannier.org/
- Boron pseudopotential (PSLibrary PAW): PSLibrary

## Workflow steps

### Step 1: Build initial BL-δ₆ structure
- Role: process
- Action: Construct the unit cell of bilayer δ₆ borophene (space group Pmmm) with lattice constants a=3.243 Å, b=2.883 Å and three inequivalent boron atoms B1, B2, B3 at positions corresponding to AB stacking of two δ₆ monolayers with interlayer covalent bonds.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: DFT geometry relaxation of BL-δ₆
- Role: process
- Action: Perform variable-cell relaxation of the BL-δ₆ unit cell using Quantum ESPRESSO to obtain the equilibrium lattice constants and atomic positions.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 3: Compute elastic constants (C₁₁, C₂₂, C₁₂, C₄₄)
- Role: scored
- Action: Using the relaxed BL-δ₆ structure, calculate the four independent in‑plane elastic constants by applying small lattice distortions and computing the stress via DFT. Extract the Voigt-notation stiffness coefficients in 2D units of N/m.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {'C11': float, 'C22': float, 'C12': float, 'C44': float}
- Scoring: scored by hidden verifier

### Step 4: Derive in‑plane Young’s moduli (Y_a, Y_b)
- Role: scored
- Action: From the elastic constants obtained in step03 and the lattice constants, compute the in‑plane Young’s moduli along the a (armchair) and b (zigzag) directions using the orthorhombic 2D formulas.
- Output file: `/app/outputs/young_moduli.json`
- Format: json
- Contract: {'Ya': float, 'Yb': float}
- Scoring: scored by hidden verifier

### Step 5: Electronic band structure and Wannier interpolation (unstrained)
- Role: process
- Action: Perform a self-consistent DFT calculation on the relaxed unstrained structure, compute the band structure, and use Wannier90 to obtain maximally localized Wannier functions for the relevant bands, generating a Wannier‑interpolated Hamiltonian.
- Evidence: `/app/outputs/wannier_unstrained.chk`

### Step 6: Phonon dispersion calculation (unstrained)
- Role: process
- Action: Compute the full phonon dispersion and density of states for the relaxed unstrained structure using density‑functional perturbation theory (DFPT) in Quantum ESPRESSO.
- Evidence: `/app/outputs/phonons_unstrained.matdyn`

### Step 7: Anisotropic electron‑phonon coupling and T_c (unstrained)
- Role: process
- Action: Using EPW, compute the electron‑phonon coupling matrix elements on dense k‑ and q‑grids, solve the fully anisotropic Migdal‑Eliashberg equations, and extract the superconducting critical temperature T_c for the unstrained BL-δ₆.
- Evidence: `/app/outputs/tc_unstrained.json`

### Step 8: Apply 13% tensile strain and relax strained geometry
- Role: process
- Action: Starting from the relaxed unstrained unit cell, increase lattice constant a by 13% (keep b fixed) and perform constrained relaxation of atomic positions at this fixed in‑plane strain.
- Evidence: `/app/outputs/strained_structure.xyz`

### Step 9: Electronic band structure and Wannier interpolation (strained 13%)
- Role: process
- Action: Repeat the DFT self‑consistent calculation and Wannierization on the 13%‑strained structure to obtain the electronic Hamiltonian for this configuration.
- Evidence: `/app/outputs/wannier_strained.chk`

### Step 10: Phonon dispersion calculation (strained 13%)
- Role: process
- Action: Compute the phonon dispersion for the 13%‑strained structure using DFPT.
- Evidence: `/app/outputs/phonons_strained.matdyn`

### Step 11: Anisotropic electron‑phonon coupling and T_c (strained 13%)
- Role: process
- Action: Using EPW on the strained electronic and phonon data, solve the anisotropic Eliashberg equations and extract the superconducting T_c for the 13%‑strained configuration.
- Evidence: `/app/outputs/tc_strained.json`

### Step 12: Collect superconducting T_c results
- Role: scored (load-bearing)
- Action: Read the T_c values from the evidence files of steps 07 and 11 and write a final JSON file containing both the unstrained and 13%‑strained anisotropic critical temperatures.
- Output file: `/app/outputs/superconducting_tc.json`
- Format: json
- Contract: {'Tc_unstrained': float, 'Tc_strained_13_percent': float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/young_moduli.json`
- `/app/outputs/superconducting_tc.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed four independent in‑plane elastic constants of BL‑δ₆ (2D stiffness coefficients).
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (N/m)
    - `C22`: float (N/m)
    - `C12`: float (N/m)
    - `C44`: float (N/m)

### young_moduli.json
- path: `/app/outputs/young_moduli.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Derived in‑plane Young’s moduli along a (armchair) and b (zigzag) directions.
- schema:
  - `type`: object
  - `required`:
    - `Ya`: float (N/m)
    - `Yb`: float (N/m)

### superconducting_tc.json
- path: `/app/outputs/superconducting_tc.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Anisotropic superconducting critical temperatures for unstrained BL‑δ₆ and for 13% tensile strain along the a direction.
- schema:
  - `type`: object
  - `required`:
    - `Tc_unstrained`: float (K)
    - `Tc_strained_13_percent`: float (K)

Notes: The checker compares the reported values against hidden reference numbers with tolerances appropriate for DFT method spread. Young's modulus Ya is also verified to exceed the graphene reference (346.1 N/m) as a structural check.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float (N/m)",
          "C22": "float (N/m)",
          "C12": "float (N/m)",
          "C44": "float (N/m)"
        }
      },
      "description": "Computed four independent in‑plane elastic constants of BL‑δ₆ (2D stiffness coefficients)."
    },
    {
      "file": "young_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Ya": "float (N/m)",
          "Yb": "float (N/m)"
        }
      },
      "description": "Derived in‑plane Young’s moduli along a (armchair) and b (zigzag) directions."
    },
    {
      "file": "superconducting_tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc_unstrained": "float (K)",
          "Tc_strained_13_percent": "float (K)"
        }
      },
      "description": "Anisotropic superconducting critical temperatures for unstrained BL‑δ₆ and for 13% tensile strain along the a direction."
    }
  ],
  "notes": "The checker compares the reported values against hidden reference numbers with tolerances appropriate for DFT method spread. Young's modulus Ya is also verified to exceed the graphene reference (346.1 N/m) as a structural check."
}
```

## How you are scored
A hidden verifier independently scores each of the three output files. For each artifact, the verifier reads the required numerical fields and compares them against a hidden reference derived from the original publication, using tolerances appropriate to the method. The final reward is a weighted sum of the per‑artifact scores. The agent must execute the full computational pipeline to generate these values; writing numbers without producing the intermediate workflow evidence (structures, checkpoints, etc.) will not satisfy the verifier. The hidden checks may also verify that certain structural relations hold (e.g., mechanical stability conditions) as secondary confirmation.
