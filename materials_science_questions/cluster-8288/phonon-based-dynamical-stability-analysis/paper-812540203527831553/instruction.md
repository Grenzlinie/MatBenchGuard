# First-principles investigation of structural, elastic, mechanical, and phonon properties of half-Heusler alloys AlNiAs and AlNiSb

## Problem background
Half-Heusler alloys with 18 valence electrons are promising candidates for thermoelectric applications. This work uses first-principles density functional theory to investigate the structural stability, electronic structure, elastic/mechanical behaviour, and lattice dynamics of two novel half-Heusler compounds AlNiAs and AlNiSb in the non-magnetic LiAlSi-type (C1_b) structure. The key quantities to be computed include the equilibrium lattice constant, bulk modulus and its pressure derivative, formation enthalpy, second-order elastic constants, polycrystalline mechanical moduli (Voigt–Reuss–Hill averages), density of states at the Fermi level, and zone-center optical phonon frequencies. Determining these properties from first principles provides insight into the stability, metallic/ductile character, and dynamic stability of these alloys.

## Approach
The approach employs plane-wave pseudopotential density functional theory with the PBE-GGA exchange-correlation functional, as implemented in the open-source Quantum ESPRESSO package. The crystal structure of the half-Heusler alloy is the LiAlSi type (space group F-43m), which can adopt three different atomic arrangements (Type I, Type II, Type III). Based on total energy comparisons, the non-magnetic Type-III configuration is the ground state and is used throughout. Structural properties are obtained by relaxing the unit cell, fitting the total energy versus volume data to the Birch–Murnaghan equation of state, and calculating the formation enthalpy from the elemental reference energies (fcc Al, fcc Ni, rhombohedral As, rhombohedral Sb). Elastic constants C11, C12, and C44 are determined through total energy-strain calculations, from which the Cauchy pressure and Zener anisotropy factor are derived. Polycrystalline mechanical moduli (bulk, shear, and Young’s moduli, Poisson’s ratio, and Pugh ratio) are computed under the Voigt, Reuss, and Hill averaging schemes. The total density of states at the Fermi level is extracted from a self-consistent electronic structure calculation followed by a non-self-consistent DOS run. Phonon frequencies at the Brillouin zone center are computed using density-functional perturbation theory (DFPT) and the optical zone-center modes are identified. All calculations are run with norm-conserving pseudopotentials of the Troullier–Martins type.

## Reproduction target
Reproduce the ground-state properties of AlNiAs and AlNiSb in the non-magnetic Type-III LiAlSi-type structure. Specifically, using Quantum ESPRESSO, compute the following quantities for both compounds and write them to the specified JSON files under /app/outputs:
- Equilibrium lattice constant (Å), bulk modulus B0 (GPa), pressure derivative B0', and formation enthalpy (eV/atom).
- Second-order elastic constants C11, C12, C44 (GPa), Cauchy pressure Cp = C12 − C44 (GPa), and Zener anisotropy A = 2 C44/(C11 − C12).
- Voigt, Reuss, and Hill averaged bulk modulus (B_V, B_R, B_H), shear modulus (G_V, G_R, G_H), Young’s modulus (E_V, E_R, E_H) in GPa, Poisson’s ratio (nu_V, nu_R, nu_H), and the Pugh ratio B_H/G_H.
- Total density of states at the Fermi level N(E_F) in states/eV.
- Zone-center optical phonon frequencies of the two triply degenerate modes T(1) (higher) and T(2) (lower) in cm⁻¹.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: DFT structural optimization and formation enthalpy
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO, perform structural relaxation for the Type‑III non‑magnetic phase of AlNiAs and AlNiSb. Fit total energy vs volume data to the Birch–Murnaghan equation of state to obtain equilibrium lattice constant a, bulk modulus B0, and pressure derivative B0'. Compute the formation enthalpy using the ground‑state energies of the compounds and elemental references (fcc Al, fcc Ni, rhombohedral As, rhombohedral Sb). Write all results to structural_properties.json.
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: JSON object with top-level keys 'AlNiAs' and 'AlNiSb'. Each value is an object with keys: 'a' (float, lattice constant in Å), 'B0' (float, bulk modulus in GPa), 'B0_prime' (float, pressure derivative), 'delta_H' (float, formation enthalpy in eV/atom).
- Scoring: scored by hidden verifier

### Step 2: Elastic constant calculation
- Role: scored
- Action: Using the relaxed structures from the previous step, apply the stress‑strain method in Quantum ESPRESSO to determine the second‑order elastic constants C11, C12, C44 for both compounds. Compute the Cauchy pressure Cp = C12 − C44 and the Zener anisotropy factor A = 2*C44/(C11 − C12). Write the results to elastic_constants.json.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with top-level keys 'AlNiAs' and 'AlNiSb'. Each value is an object with keys: 'C11', 'C12', 'C44' (float, in GPa), 'Cp' (float, Cauchy pressure, in GPa), 'A' (float, Zener anisotropy, dimensionless).
- Scoring: scored by hidden verifier

### Step 3: Mechanical properties (Voigt–Reuss–Hill)
- Role: scored
- Action: From the elastic constants obtained in the previous step, compute the polycrystalline elastic moduli using Voigt, Reuss, and Voigt–Reuss–Hill (Hill) averaging schemes. Specifically, calculate the bulk modulus B, shear modulus G, Young's modulus E, Poisson's ratio ν in all three approximations, and the Pugh ratio B_H/G_H. Write the full set of values to mechanical_properties.json.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: JSON object with top-level keys 'AlNiAs' and 'AlNiSb'. Each value is an object with keys: 'B_V', 'B_R', 'B_H', 'G_V', 'G_R', 'G_H', 'E_V', 'E_R', 'E_H' (float, in GPa), 'nu_V', 'nu_R', 'nu_H' (float, Poisson's ratio), 'BH_GH' (float, Pugh ratio).
- Scoring: scored by hidden verifier

### Step 4: Density of states at Fermi level
- Role: scored
- Action: Using the relaxed structures, perform a self‑consistent field (SCF) calculation followed by a non‑self‑consistent calculation to obtain the total density of states (DOS) for both compounds. Extract the DOS value at the Fermi energy N(E_F) and write it to dos_at_fermi.json.
- Output file: `/app/outputs/dos_at_fermi.json`
- Format: json
- Contract: JSON object with keys 'AlNiAs' and 'AlNiSb', each a float representing N(E_F) in states/eV.
- Scoring: scored by hidden verifier

### Step 5: Γ‑point phonon frequencies
- Role: scored
- Action: Using density‑functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO's ph.x, compute the optical phonon frequencies at the Brillouin zone center for both compounds. Identify the two triply degenerate optical modes T(1) (higher) and T(2) (lower) and write their frequencies to phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object with keys 'AlNiAs' and 'AlNiSb', each containing 'T1_freq' and 'T2_freq' (float, in cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/mechanical_properties.json`
- `/app/outputs/dos_at_fermi.json`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constant, bulk modulus, pressure derivative, and formation enthalpy for both compounds.
- schema:
  - `type`: object
  - `required`: `AlNiAs`, `AlNiSb`
  - `properties`:
    - `AlNiAs`:
      - `type`: object
      - `required`: `a`, `B0`, `B0_prime`, `delta_H`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Å
        - `B0`:
          - `type`: number
          - `unit`: GPa
        - `B0_prime`:
          - `type`: number
        - `delta_H`:
          - `type`: number
          - `unit`: eV/atom
    - `AlNiSb`:
      - `type`: object
      - `required`: `a`, `B0`, `B0_prime`, `delta_H`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Å
        - `B0`:
          - `type`: number
          - `unit`: GPa
        - `B0_prime`:
          - `type`: number
        - `delta_H`:
          - `type`: number
          - `unit`: eV/atom

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Second-order elastic constants C11, C12, C44, Cauchy pressure, and Zener anisotropy factor.
- schema:
  - `type`: object
  - `required`: `AlNiAs`, `AlNiSb`
  - `properties`:
    - `AlNiAs`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`, `Cp`, `A`
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `Cp`:
          - `type`: number
          - `unit`: GPa
        - `A`:
          - `type`: number
    - `AlNiSb`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`, `Cp`, `A`
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `Cp`:
          - `type`: number
          - `unit`: GPa
        - `A`:
          - `type`: number

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Voigt, Reuss, and Hill averaged bulk, shear, and Young's moduli, Poisson's ratios, and Pugh ratio.
- schema:
  - `type`: object
  - `required`: `AlNiAs`, `AlNiSb`
  - `properties`:
    - `AlNiAs`:
      - `type`: object
      - `required`: `B_V`, `B_R`, `B_H`, `G_V`, `G_R`, `G_H`, `E_V`, `E_R`, `E_H`, `nu_V`, `nu_R`, `nu_H`, `BH_GH`
      - `properties`:
        - `B_V`:
          - `type`: number
          - `unit`: GPa
        - `B_R`:
          - `type`: number
          - `unit`: GPa
        - `B_H`:
          - `type`: number
          - `unit`: GPa
        - `G_V`:
          - `type`: number
          - `unit`: GPa
        - `G_R`:
          - `type`: number
          - `unit`: GPa
        - `G_H`:
          - `type`: number
          - `unit`: GPa
        - `E_V`:
          - `type`: number
          - `unit`: GPa
        - `E_R`:
          - `type`: number
          - `unit`: GPa
        - `E_H`:
          - `type`: number
          - `unit`: GPa
        - `nu_V`:
          - `type`: number
        - `nu_R`:
          - `type`: number
        - `nu_H`:
          - `type`: number
        - `BH_GH`:
          - `type`: number
    - `AlNiSb`:
      - `type`: object
      - `required`: `B_V`, `B_R`, `B_H`, `G_V`, `G_R`, `G_H`, `E_V`, `E_R`, `E_H`, `nu_V`, `nu_R`, `nu_H`, `BH_GH`
      - `properties`:
        - `B_V`:
          - `type`: number
          - `unit`: GPa
        - `B_R`:
          - `type`: number
          - `unit`: GPa
        - `B_H`:
          - `type`: number
          - `unit`: GPa
        - `G_V`:
          - `type`: number
          - `unit`: GPa
        - `G_R`:
          - `type`: number
          - `unit`: GPa
        - `G_H`:
          - `type`: number
          - `unit`: GPa
        - `E_V`:
          - `type`: number
          - `unit`: GPa
        - `E_R`:
          - `type`: number
          - `unit`: GPa
        - `E_H`:
          - `type`: number
          - `unit`: GPa
        - `nu_V`:
          - `type`: number
        - `nu_R`:
          - `type`: number
        - `nu_H`:
          - `type`: number
        - `BH_GH`:
          - `type`: number

### dos_at_fermi.json
- path: `/app/outputs/dos_at_fermi.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total density of states at the Fermi level for both compounds.
- schema:
  - `type`: object
  - `required`: `AlNiAs`, `AlNiSb`
  - `properties`:
    - `AlNiAs`:
      - `type`: number
      - `unit`: states/eV
    - `AlNiSb`:
      - `type`: number
      - `unit`: states/eV

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zone-center optical phonon frequencies (T1 and T2) for both compounds.
- schema:
  - `type`: object
  - `required`: `AlNiAs`, `AlNiSb`
  - `properties`:
    - `AlNiAs`:
      - `type`: object
      - `required`: `T1_freq`, `T2_freq`
      - `properties`:
        - `T1_freq`:
          - `type`: number
          - `unit`: cm⁻¹
        - `T2_freq`:
          - `type`: number
          - `unit`: cm⁻¹
    - `AlNiSb`:
      - `type`: object
      - `required`: `T1_freq`, `T2_freq`
      - `properties`:
        - `T1_freq`:
          - `type`: number
          - `unit`: cm⁻¹
        - `T2_freq`:
          - `type`: number
          - `unit`: cm⁻¹

Notes: All outputs are scalar values computed from DFT simulations. The verifier will compare each reported value to the hidden gold derived from the paper, using component-specific tolerance windows (not disclosed). Only exact numerical matches within those tolerances are required; no directionality applies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "AlNiAs",
          "AlNiSb"
        ],
        "properties": {
          "AlNiAs": {
            "type": "object",
            "required": [
              "a",
              "B0",
              "B0_prime",
              "delta_H"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Å"
              },
              "B0": {
                "type": "number",
                "unit": "GPa"
              },
              "B0_prime": {
                "type": "number"
              },
              "delta_H": {
                "type": "number",
                "unit": "eV/atom"
              }
            }
          },
          "AlNiSb": {
            "type": "object",
            "required": [
              "a",
              "B0",
              "B0_prime",
              "delta_H"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Å"
              },
              "B0": {
                "type": "number",
                "unit": "GPa"
              },
              "B0_prime": {
                "type": "number"
              },
              "delta_H": {
                "type": "number",
                "unit": "eV/atom"
              }
            }
          }
        }
      },
      "description": "Equilibrium lattice constant, bulk modulus, pressure derivative, and formation enthalpy for both compounds."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "AlNiAs",
          "AlNiSb"
        ],
        "properties": {
          "AlNiAs": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44",
              "Cp",
              "A"
            ],
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "Cp": {
                "type": "number",
                "unit": "GPa"
              },
              "A": {
                "type": "number"
              }
            }
          },
          "AlNiSb": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44",
              "Cp",
              "A"
            ],
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "Cp": {
                "type": "number",
                "unit": "GPa"
              },
              "A": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Second-order elastic constants C11, C12, C44, Cauchy pressure, and Zener anisotropy factor."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "AlNiAs",
          "AlNiSb"
        ],
        "properties": {
          "AlNiAs": {
            "type": "object",
            "required": [
              "B_V",
              "B_R",
              "B_H",
              "G_V",
              "G_R",
              "G_H",
              "E_V",
              "E_R",
              "E_H",
              "nu_V",
              "nu_R",
              "nu_H",
              "BH_GH"
            ],
            "properties": {
              "B_V": {
                "type": "number",
                "unit": "GPa"
              },
              "B_R": {
                "type": "number",
                "unit": "GPa"
              },
              "B_H": {
                "type": "number",
                "unit": "GPa"
              },
              "G_V": {
                "type": "number",
                "unit": "GPa"
              },
              "G_R": {
                "type": "number",
                "unit": "GPa"
              },
              "G_H": {
                "type": "number",
                "unit": "GPa"
              },
              "E_V": {
                "type": "number",
                "unit": "GPa"
              },
              "E_R": {
                "type": "number",
                "unit": "GPa"
              },
              "E_H": {
                "type": "number",
                "unit": "GPa"
              },
              "nu_V": {
                "type": "number"
              },
              "nu_R": {
                "type": "number"
              },
              "nu_H": {
                "type": "number"
              },
              "BH_GH": {
                "type": "number"
              }
            }
          },
          "AlNiSb": {
            "type": "object",
            "required": [
              "B_V",
              "B_R",
              "B_H",
              "G_V",
              "G_R",
              "G_H",
              "E_V",
              "E_R",
              "E_H",
              "nu_V",
              "nu_R",
              "nu_H",
              "BH_GH"
            ],
            "properties": {
              "B_V": {
                "type": "number",
                "unit": "GPa"
              },
              "B_R": {
                "type": "number",
                "unit": "GPa"
              },
              "B_H": {
                "type": "number",
                "unit": "GPa"
              },
              "G_V": {
                "type": "number",
                "unit": "GPa"
              },
              "G_R": {
                "type": "number",
                "unit": "GPa"
              },
              "G_H": {
                "type": "number",
                "unit": "GPa"
              },
              "E_V": {
                "type": "number",
                "unit": "GPa"
              },
              "E_R": {
                "type": "number",
                "unit": "GPa"
              },
              "E_H": {
                "type": "number",
                "unit": "GPa"
              },
              "nu_V": {
                "type": "number"
              },
              "nu_R": {
                "type": "number"
              },
              "nu_H": {
                "type": "number"
              },
              "BH_GH": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Voigt, Reuss, and Hill averaged bulk, shear, and Young's moduli, Poisson's ratios, and Pugh ratio."
    },
    {
      "file": "dos_at_fermi.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "AlNiAs",
          "AlNiSb"
        ],
        "properties": {
          "AlNiAs": {
            "type": "number",
            "unit": "states/eV"
          },
          "AlNiSb": {
            "type": "number",
            "unit": "states/eV"
          }
        }
      },
      "description": "Total density of states at the Fermi level for both compounds."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "AlNiAs",
          "AlNiSb"
        ],
        "properties": {
          "AlNiAs": {
            "type": "object",
            "required": [
              "T1_freq",
              "T2_freq"
            ],
            "properties": {
              "T1_freq": {
                "type": "number",
                "unit": "cm⁻¹"
              },
              "T2_freq": {
                "type": "number",
                "unit": "cm⁻¹"
              }
            }
          },
          "AlNiSb": {
            "type": "object",
            "required": [
              "T1_freq",
              "T2_freq"
            ],
            "properties": {
              "T1_freq": {
                "type": "number",
                "unit": "cm⁻¹"
              },
              "T2_freq": {
                "type": "number",
                "unit": "cm⁻¹"
              }
            }
          }
        }
      },
      "description": "Zone-center optical phonon frequencies (T1 and T2) for both compounds."
    }
  ],
  "notes": "All outputs are scalar values computed from DFT simulations. The verifier will compare each reported value to the hidden gold derived from the paper, using component-specific tolerance windows (not disclosed). Only exact numerical matches within those tolerances are required; no directionality applies."
}
```

## How you are scored
A hidden verifier independently checks each of the five JSON output files. For each file, the verifier extracts the numerical values and compares them against hidden reference values that represent the correct result of the specified DFT workflow. The comparison uses tolerance windows that account for typical numerical spread between different DFT runs (code version, compilations, pseudopotential revision, and convergence settings). All required keys must be present; missing or incorrectly formatted files receive zero credit for that artifact. The final reward is a weighted sum of partial scores across the five outputs. Correct execution of all workflow steps is essential to produce values within the hidden tolerances.
