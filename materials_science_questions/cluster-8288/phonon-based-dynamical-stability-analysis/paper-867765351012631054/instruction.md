# Phonon-based dynamical stability analysis of borophene sheets

## Problem background
Borophene, a two‑dimensional boron sheet, has been synthesized and predicted in several structural phases. Two candidate phases, denoted β (Pmmn8, 8 atoms per unit cell) and γ (Pmmn2, 2 atoms per unit cell), are of interest as building blocks for nanoelectronics. Determining their relative thermodynamic and mechanical stability is a prerequisite for understanding which form is most likely to appear freestanding. Stability can be assessed by computing the binding energy per atom (thermodynamic stability) and the phonon dispersion (mechanical stability). The goal is to calculate these quantities from first‑principles and use them to compare the two phases.

## Approach
The workflow employs density functional theory (DFT) with the SIESTA code and the Perdew‑Burke‑Ernzerhof (GGA‑PBE) functional, a double‑ζ basis set, and a norm‑conserving Troullier‑Martins pseudopotential for boron. First, the atomic positions and lattice vectors of both the β and γ sheets are relaxed to obtain equilibrium geometries and total energies. The binding energy per atom is then computed as E_B = –(E_cell – n*E_atom)/n, where E_cell is the total energy of the relaxed unit cell, E_atom is the energy of an isolated boron atom obtained with the same setup, and n is the number of atoms in the cell. Next, phonon calculations are performed using the finite‑displacement method implemented in Phonopy, with rotational‑symmetry enforcement on the force constants. The phonon frequencies are evaluated along the high‑symmetry directions Γ–X and Γ–Y, with particular attention to the out‑of‑plane acoustic (ZA) branch. All computations are carried out with open‑source tools and publicly available structural data.

## Reproduction target
Compute and output the binding energy per atom (in eV/atom) for both the β (Pmmn8) and γ (Pmmn2) borophene sheets. Then, for each sheet, compute the phonon dispersion and extract the frequencies at the high‑symmetry points Γ (0,0,0), X (0.5,0,0), Y (0,0.5,0) and the midpoint M (0.25,0,0) along Γ–X. All frequencies must be non‑negative (real) to indicate mechanical stability. The low‑frequency behavior of the ZA branch along Γ–X is a key discriminant between the two phases. The required outputs are three JSON files: binding_energies.json, phonon_dispersion_beta.json, phonon_dispersion_gamma.json, with the formats specified in the steps below.

## Assets

- SIESTA: https://departments.icmab.es/leem/siesta/
- Phonopy: phonopy
- Boron norm‑conserving Troullier‑Martins pseudopotential: https://departments.icmab.es/leem/siesta/Databases/Pseudopotentials/periodictable-gga-abinit.html
- β (Pmmn8) borophene structure: 10.1103/PhysRevLett.112.085502
- γ (Pmmn2) borophene structure: 10.1126/science.aad1080

## Workflow steps

### Step 1: Geometry optimization of β and γ borophene sheets
- Role: process
- Action: Perform DFT geometry relaxation for both β (Pmmn8) and γ (Pmmn2) freestanding sheets using SIESTA with GGA‑PBE functional, double‑ζ basis, and norm‑conserving B pseudopotential. Relax atomic positions and lattice vectors to obtain equilibrium structures. Record total energies per unit cell.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Calculate binding energies
- Role: scored (load-bearing)
- Action: Using the total energies of the relaxed unit cells and the energy of an isolated B atom computed with the same SIESTA setup, compute the binding energy per atom E_B = –(E_cell – n*E_atom)/n for both sheets. Write a JSON file with the two values.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"beta_binding_energy": <float in eV/atom>, "gamma_binding_energy": <float in eV/atom>}
- Scoring: scored by hidden verifier

### Step 3: Compute phonon dispersion for β sheet
- Role: scored (load-bearing)
- Action: Using the relaxed β structure, perform phonon calculations with the finite‑displacement method via Phonopy and SIESTA force computations. Enforce rotational symmetry on the force constants. Extract phonon frequencies at high‑symmetry points Γ, X, Y and the midpoint M (halfway between Γ and X). Write frequencies into a JSON file.
- Output file: `/app/outputs/phonon_dispersion_beta.json`
- Format: json
- Contract: {"Gamma": [<list of floats>], "X": [<list of floats>], "Y": [<list of floats>], "M": [<list of floats>]}
- Scoring: scored by hidden verifier

### Step 4: Compute phonon dispersion for γ sheet
- Role: scored (load-bearing)
- Action: Using the relaxed γ structure, perform phonon calculation with Phonopy and SIESTA, enforcing rotational symmetry. Extract frequencies at Γ, X, Y, and the midpoint M along Γ–X. Write to a JSON file.
- Output file: `/app/outputs/phonon_dispersion_gamma.json`
- Format: json
- Contract: {"Gamma": [<list of floats>], "X": [<list of floats>], "Y": [<list of floats>], "M": [<list of floats>]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`
- `/app/outputs/phonon_dispersion_beta.json`
- `/app/outputs/phonon_dispersion_gamma.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Binding energies per atom for β and γ borophene sheets. Checked against paper‑reported values with tolerance; also verifies β > γ.
- schema:
  - `type`: object
  - `required`:
    - `beta_binding_energy`: float
    - `gamma_binding_energy`: float
  - `units`:
    - `beta_binding_energy`: eV/atom
    - `gamma_binding_energy`: eV/atom

### phonon_dispersion_beta.json
- path: `/app/outputs/phonon_dispersion_beta.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon frequencies at high‑symmetry points for β. Audited: all frequencies non‑negative; no deep low‑frequency valley in ZA branch.
- schema:
  - `type`: object
  - `required`:
    - `Gamma`: array of numbers
    - `X`: array of numbers
    - `Y`: array of numbers
    - `M`: array of numbers
  - `units`:
    - `array values`: cm^-1

### phonon_dispersion_gamma.json
- path: `/app/outputs/phonon_dispersion_gamma.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon frequencies at high‑symmetry points for γ. Audited: all frequencies non‑negative; ZA branch shows a low‑frequency valley at M (< ~30 cm⁻¹ and lower than at Γ).
- schema:
  - `type`: object
  - `required`:
    - `Gamma`: array of numbers
    - `X`: array of numbers
    - `Y`: array of numbers
    - `M`: array of numbers
  - `units`:
    - `array values`: cm^-1

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta_binding_energy": "float",
          "gamma_binding_energy": "float"
        },
        "units": {
          "beta_binding_energy": "eV/atom",
          "gamma_binding_energy": "eV/atom"
        }
      },
      "description": "Binding energies per atom for β and γ borophene sheets. Checked against paper‑reported values with tolerance; also verifies β > γ."
    },
    {
      "file": "phonon_dispersion_beta.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Gamma": "array of numbers",
          "X": "array of numbers",
          "Y": "array of numbers",
          "M": "array of numbers"
        },
        "units": {
          "array values": "cm^-1"
        }
      },
      "description": "Phonon frequencies at high‑symmetry points for β. Audited: all frequencies non‑negative; no deep low‑frequency valley in ZA branch."
    },
    {
      "file": "phonon_dispersion_gamma.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Gamma": "array of numbers",
          "X": "array of numbers",
          "Y": "array of numbers",
          "M": "array of numbers"
        },
        "units": {
          "array values": "cm^-1"
        }
      },
      "description": "Phonon frequencies at high‑symmetry points for γ. Audited: all frequencies non‑negative; ZA branch shows a low‑frequency valley at M (< ~30 cm⁻¹ and lower than at Γ)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects each of your output files independently. It checks the binding energies for physical consistency and compares the phonon frequencies against expected structural patterns (all modes non‑negative, the shape of the ZA branch) and reference ranges. The reward is a weighted combination of the scores from the three scored artifacts. Simply reporting numbers without actually running the DFT and phonon computations will produce artifacts that fail the checks. The verifier allows for reasonable run‑to‑run spread, so your goal is to faithfully follow the workflow and produce accurate, physically meaningful results.
