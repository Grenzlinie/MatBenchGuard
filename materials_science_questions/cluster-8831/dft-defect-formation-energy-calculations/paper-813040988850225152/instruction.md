# DFT Formation Energy and Thermochromic Property Calculations for Substitutionally Doped VO2

## Problem background
Vanadium dioxide (VO2) is a thermochromic material that undergoes a metal–insulator transition from a high-temperature rutile (R) phase to a low-temperature monoclinic (M1) phase at approximately 340 K. This property makes it attractive for smart windows, but practical application requires reducing the transition temperature (Tc) to near room temperature. Elemental doping is a common strategy to lower Tc. This task investigates, through density functional theory, the doping of VO2 with group VA elements (P, As, Bi) at three possible sites: the octahedral interstitial site, a vanadium-substitutional site, and an oxygen-substitutional site. The goal is to determine how these dopants affect formation energies, electronic band gaps (Eg2), and the phase transition temperature, and thereby to identify which dopant most effectively reduces Tc while being energetically feasible to incorporate.

## Approach
The calculations use spin-unpolarized plane-wave density functional theory with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and an on-site Hubbard U correction applied to vanadium d states to describe strong electron correlations. Chemical potentials for O, V, P, As, and Bi are obtained from first-principles total-energy calculations on an O2 molecule and bulk elemental phases. Supercells containing 96 atoms are constructed for both the rutile and monoclinic phases of VO2. For each dopant (P, As, Bi) one foreign atom is introduced at each of the three sites, and the atomic positions and lattice parameters are relaxed to obtain total energies. 

From the relaxed total energies and the computed chemical potentials, formation energies are evaluated under two growth conditions (oxygen-rich and vanadium-rich) using formulas that account for the number of atoms added or removed and the corresponding elemental reference energies. Formation Helmholtz free energies are computed directly from the total energies and the elemental reference energies. Band gaps (Eg2) are extracted from the electronic structure of the relaxed monoclinic phase. Finally, the phase transition temperature Tc for each doped system is estimated from the total-energy difference between the rutile and monoclinic phases, taking the known Tc of pure VO2 (340 K) as a reference and approximating the enthalpy change by the Helmholtz free-energy difference at 0 K. The pure VO2 system is treated as the reference baseline throughout.

## Reproduction target
Produce two JSON files that contain the computed quantities for pure VO2 and for all nine M-doped configurations (M = P, As, Bi; doping sites: interstitial, V-substitutional, O-substitutional) in both crystal phases.

- `formation_energies.json`: an array of objects, each containing the system label, phase ("R" or "M1"), the total energy, the formation Helmholtz free energy, and the formation energies under oxygen-rich and vanadium-rich conditions (where formation energies are null for the pure system).
- `properties.json`: an array of objects for the doped monoclinic (M1) systems and the pure M1 reference, each containing the system label, the band gap Eg2 (in eV), and the estimated phase transition temperature Tc (in K).

The numeric values and the relative trends among dopants and doping sites constitute the reproduction target.

## Assets

- VO2 crystal structures (rutile and monoclinic)
- Plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PAW/US pseudopotentials for V, O, P, As, Bi: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Reference chemical potentials
- Role: process
- Action: Perform DFT total-energy calculations for an O2 molecule, bulk vanadium, and bulk phosphorus, arsenic, and bismuth. Extract total energies and derive chemical potentials mu_O, mu_V, mu_P, mu_As, mu_Bi following the paper's definitions (mu_O = E(O2)/2, mu_V and mu_M from bulk energies per atom).
- Evidence: `/app/outputs/chemical_potentials.json`

### Step 2: Supercell geometry optimization and total energies
- Role: process
- Action: Build 2x2x2 supercells for monoclinic VO2 and 2x2x4 primitive-cell supercells for rutile VO2 (both 96 atoms). Create all doped configurations: M@i, M@V, M@O for each M = P, As, Bi. Relax atomic positions and lattice parameters using spin-unpolarized DFT with PBE+U (U=3.5 eV on V d), a plane-wave cutoff of 600 eV, and a 4x4x4 k-point mesh. Record total energy of each relaxed system.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Band gap calculation (M1 phase)
- Role: process
- Action: For each relaxed monoclinic (M1) supercell (pure VO2 and all M-doped systems), compute band structure and extract the band gap Eg2 (energy between highest occupied and lowest unoccupied states, ignoring in-gap defect states). Use non-spin-polarized DFT with the same functional settings.
- Evidence: `/app/outputs/band_gaps_raw.json`

### Step 4: Formation energy analysis
- Role: scored (load-bearing)
- Action: From the total energies (step 2) and chemical potentials (step 1), compute defect formation energies under O-rich and V-rich growth conditions, and formation Helmholtz free energies. Collect all values into a single JSON file.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: Each object: system (string, e.g. 'P@O'), phase (string, 'R' or 'M1'), total_energy (float, eV), formation_helmholtz (float, eV), formation_O_rich (float or null for pure), formation_V_rich (float or null for pure).
- Scoring: scored by hidden verifier

### Step 5: Properties (Eg2 and Tc)
- Role: scored
- Action: Combine Eg2 values from step 3 with total energies from step 2 for the M1 phase. Compute phase transition temperature Tc for each doped M1 system using Tc = 340 K * (DeltaH / DeltaH0) where DeltaH is approximated by total-energy difference between R and M1 phases. Include the pure M1 reference (Tc = 340 K, Eg2 from step 3).
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: Each object: system (string), Eg2 (float, eV), Tc (float, K). Only doped M1 systems and pure M1 reference.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies and Helmholtz free energies for all doped configurations and pure VO2 in both phases.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `phase`, `total_energy`, `formation_helmholtz`, `formation_O_rich`, `formation_V_rich`
    - `properties`:
      - `system`:
        - `type`: string
      - `phase`:
        - `type`: string
        - `enum`: `R`, `M1`
      - `total_energy`:
        - `type`: number
        - `units`: eV
      - `formation_helmholtz`:
        - `type`: number
        - `units`: eV
      - `formation_O_rich`:
        - `type`: `number`, `null`
        - `units`: eV
      - `formation_V_rich`:
        - `type`: `number`, `null`
        - `units`: eV
    - `additionalProperties`: False

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Band gaps Eg2 and phase transition temperatures Tc for M1-phase doped systems and pure VO2.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `Eg2`, `Tc`
    - `properties`:
      - `system`:
        - `type`: string
      - `Eg2`:
        - `type`: number
        - `units`: eV
      - `Tc`:
        - `type`: number
        - `units`: K
    - `additionalProperties`: False

Notes: The checker will verify structural trends (ordering of formation energies, negativity of formation Helmholtz free energies, band gap reduction, and Tc ordering) with tolerance-based numeric comparisons against hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "phase",
            "total_energy",
            "formation_helmholtz",
            "formation_O_rich",
            "formation_V_rich"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "phase": {
              "type": "string",
              "enum": [
                "R",
                "M1"
              ]
            },
            "total_energy": {
              "type": "number",
              "units": "eV"
            },
            "formation_helmholtz": {
              "type": "number",
              "units": "eV"
            },
            "formation_O_rich": {
              "type": [
                "number",
                "null"
              ],
              "units": "eV"
            },
            "formation_V_rich": {
              "type": [
                "number",
                "null"
              ],
              "units": "eV"
            }
          },
          "additionalProperties": false
        }
      },
      "description": "Formation energies and Helmholtz free energies for all doped configurations and pure VO2 in both phases."
    },
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "Eg2",
            "Tc"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "Eg2": {
              "type": "number",
              "units": "eV"
            },
            "Tc": {
              "type": "number",
              "units": "K"
            }
          },
          "additionalProperties": false
        }
      },
      "description": "Band gaps Eg2 and phase transition temperatures Tc for M1-phase doped systems and pure VO2."
    }
  ],
  "notes": "The checker will verify structural trends (ordering of formation energies, negativity of formation Helmholtz free energies, band gap reduction, and Tc ordering) with tolerance-based numeric comparisons against hidden reference values."
}
```

## How you are scored
A hidden automated verifier inspects the submitted `formation_energies.json` and `properties.json`. It checks that the reported values satisfy a set of expected structural relationships (such as ordering of formation energies among doping sites, sign of formation Helmholtz free energies, relative band-gap magnitudes, and Tc ordering) and compares the numeric values against an internal reference. The verifier combines these checks into a single reward score between 0 and 1. The workflow steps themselves are not individually scored; the reward depends entirely on the two output files. The verifier does not require you to match any specific paper or code; it evaluates the submission on its own terms.
