# First-Principles Mechanical, Dynamical, and Thermodynamic Properties of Ordered Fe-Pt Alloys

## Problem background
Density functional theory (DFT) is used to investigate the mechanical, dynamical, and thermodynamic properties of ordered bimetallic Fe-Pt alloys (Fe₃Pt, FePt, FePt₃) in four crystal structures. Understanding elastic constants, phonon stability, and thermal behavior is crucial for the design of magnetic storage and spintronic devices. This reproduction task asks you to compute these properties from first principles, following a well-defined protocol with open-source tools.

## Approach
The reproduction uses spin-polarised DFT calculations within the generalised gradient approximation (GGA-PBE) to relax the crystal structures. From the relaxed structures, monocrystalline elastic constants are computed using the stress–strain method. Polycrystalline moduli (bulk, shear, Young’s modulus, Poisson ratio, Pugh ratio) are derived via Voigt–Reuss–Hill averaging, and mechanical stability is checked against the Born criteria for the appropriate crystal symmetry. Phonon dispersion and density of states are calculated using the finite-displacement method. From the phonon data, the minimum frequency across the Brillouin zone is extracted to assess dynamical stability, and the Debye temperature and isochoric heat capacity at 300 K are computed from the phonon density of states. The workflow is designed to be implemented with open-source codes (Quantum ESPRESSO for DFT forces and stress, Phonopy for phonons) using standard pseudopotentials.

## Reproduction target
For each of the four ordered Fe-Pt phases — cubic Pm-3m Fe₃Pt, tetragonal I4/mmm Fe₃Pt, tetragonal P4/mmm FePt, and cubic Pm-3m FePt₃ — produce the three scored JSON artifacts described in the workflow steps:

* `elastic_constants_and_moduli.json` — containing the single-crystal elastic constants and the derived polycrystalline moduli, together with the outcome of the Born mechanical stability checks.
* `dynamical_stability.json` — reporting the minimum phonon frequency (in THz) across high-symmetry directions and the dynamical stability verdict.
* `thermodynamic_properties.json` — containing the Debye temperature and isochoric heat capacity at 300 K.

All calculations must be performed with the open-source toolchain (Quantum ESPRESSO + Phonopy) using the structural parameters and computational settings detailed in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP pseudopotentials (PBE, efficiency): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare initial crystal structures
- Role: process
- Action: Construct the four ordered Fe-Pt crystal structures: cubic Pm-3m Fe₃Pt, tetragonal I4/mmm Fe₃Pt, tetragonal P4/mmm FePt, and cubic Pm-3m FePt₃ using the lattice parameters and atomic positions specified in the task background. Generate the input files required for DFT geometry relaxation.
- Evidence: `/app/outputs/input_structures.tar.gz`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform spin-polarized DFT structure relaxation for each phase using GGA-PBE exchange-correlation, ultrasoft pseudopotentials from SSSP, a plane-wave cutoff of 350 eV, and appropriate Monkhorst–Pack k-point grids. Allow cell shape and volume to change until force and energy convergence thresholds are met. Save the final relaxed structures and total energies.
- Evidence: `/app/outputs/relaxed_structures.tar.gz`

### Step 3: Elastic constant calculation via stress-strain
- Role: process
- Action: Using the relaxed structures, apply small homogeneous strains (maximum amplitude 0.003) and compute the resulting stress tensors via DFT. Extract the independent monocrystalline elastic constants C11, C12, C44 (and for tetragonal phases also C33, C13, C66) from the linear stress–strain relation. Save the raw elastic constants to an intermediate file.
- Evidence: `/app/outputs/raw_elastic_constants.json`

### Step 4: Elastic constants and polycrystalline moduli analysis
- Role: scored (load-bearing)
- Action: From the raw elastic constants, compute polycrystalline moduli (bulk modulus B, shear modulus G, Young’s modulus E, Poisson ratio ν, Pugh ratio G/B) using Voigt–Reuss–Hill averaging for each phase. Check the Born mechanical stability criteria for cubic and tetragonal symmetries. Write all results to the scored artifact.
- Output file: `/app/outputs/elastic_constants_and_moduli.json`
- Format: json
- Contract: JSON object: top-level keys are structure names 'Pm-3m-Fe3Pt', 'I4/mmm-Fe3Pt', 'P4/mmm-FePt', 'Pm-3m-FePt3'. Each value is an object with numeric fields: C11, C12, C44 (and for tetragonal phases also C33, C13, C66) in GPa; bulk_modulus_B, shear_modulus_G, young_modulus_E, poisson_ratio_nu, G_B_ratio (all floats); and boolean born_stable.
- Scoring: scored by hidden verifier

### Step 5: Phonon dispersion and density of states calculation
- Role: process
- Action: Using the relaxed structures, perform finite-displacement phonon calculations (e.g., via Phonopy) with DFT forces. Generate phonon dispersion curves along high-symmetry lines and the total phonon density of states for all four phases. Save the force constants and phonon frequencies as intermediate files.
- Evidence: `/app/outputs/phonon_output.tar.gz`

### Step 6: Dynamical stability verification
- Role: scored (load-bearing)
- Action: From the phonon dispersion data, extract the minimum phonon frequency (in THz) across all high-symmetry paths for each phase. Determine dynamical stability (true if the minimum frequency is non-negative, false otherwise). Write the results to the scored artifact.
- Output file: `/app/outputs/dynamical_stability.json`
- Format: json
- Contract: JSON object: keys are structure names. Each value is an object with min_phonon_frequency_THz (float, can be negative) and dynamically_stable (boolean).
- Scoring: scored by hidden verifier

### Step 7: Thermodynamic property computation
- Role: scored (load-bearing)
- Action: From the phonon density of states, compute the Debye temperature (using the standard definition) and the isochoric heat capacity Cv at 300 K for each phase. Write the values to the scored artifact.
- Output file: `/app/outputs/thermodynamic_properties.json`
- Format: json
- Contract: JSON object: keys are structure names. Each value is an object with Debye_temperature_K (float) and heat_capacity_Cv_at_300K (float, in cal/(cell·K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants_and_moduli.json`
- `/app/outputs/dynamical_stability.json`
- `/app/outputs/thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants_and_moduli.json
- path: `/app/outputs/elastic_constants_and_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed monocrystalline elastic constants, derived polycrystalline moduli, and mechanical stability verdicts for the four Fe-Pt alloys.
- schema:
  - `type`: object
  - `description`: Top-level keys are structure names 'Pm-3m-Fe3Pt', 'I4/mmm-Fe3Pt', 'P4/mmm-FePt', 'Pm-3m-FePt3'. Each value is an object containing elastic constants and moduli.
  - `required_keys`: `Pm-3m-Fe3Pt`, `I4/mmm-Fe3Pt`, `P4/mmm-FePt`, `Pm-3m-FePt3`
  - `field_spec`:
    - `Pm-3m-Fe3Pt`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`, `bulk_modulus_B`, `shear_modulus_G`, `young_modulus_E`, `poisson_ratio_nu`, `G_B_ratio`, `born_stable`
      - `fields`:
        - `C11`:
          - `type`: float
          - `unit`: GPa
        - `C12`:
          - `type`: float
          - `unit`: GPa
        - `C44`:
          - `type`: float
          - `unit`: GPa
        - `bulk_modulus_B`:
          - `type`: float
          - `unit`: GPa
        - `shear_modulus_G`:
          - `type`: float
          - `unit`: GPa
        - `young_modulus_E`:
          - `type`: float
          - `unit`: GPa
        - `poisson_ratio_nu`:
          - `type`: float
        - `G_B_ratio`:
          - `type`: float
        - `born_stable`:
          - `type`: boolean
    - `I4/mmm-Fe3Pt`:
      - `type`: object
      - `required`: `C11`, `C12`, `C13`, `C33`, `C44`, `C66`, `bulk_modulus_B`, `shear_modulus_G`, `young_modulus_E`, `poisson_ratio_nu`, `G_B_ratio`, `born_stable`
      - `fields`:
        - `C11`:
          - `type`: float
          - `unit`: GPa
        - `C12`:
          - `type`: float
          - `unit`: GPa
        - `C13`:
          - `type`: float
          - `unit`: GPa
        - `C33`:
          - `type`: float
          - `unit`: GPa
        - `C44`:
          - `type`: float
          - `unit`: GPa
        - `C66`:
          - `type`: float
          - `unit`: GPa
        - `bulk_modulus_B`:
          - `type`: float
          - `unit`: GPa
        - `shear_modulus_G`:
          - `type`: float
          - `unit`: GPa
        - `young_modulus_E`:
          - `type`: float
          - `unit`: GPa
        - `poisson_ratio_nu`:
          - `type`: float
        - `G_B_ratio`:
          - `type`: float
        - `born_stable`:
          - `type`: boolean
    - `P4/mmm-FePt`:
      - `type`: object
      - `required`: `C11`, `C12`, `C13`, `C33`, `C44`, `C66`, `bulk_modulus_B`, `shear_modulus_G`, `young_modulus_E`, `poisson_ratio_nu`, `G_B_ratio`, `born_stable`
      - `fields`:
        - `C11`:
          - `type`: float
          - `unit`: GPa
        - `C12`:
          - `type`: float
          - `unit`: GPa
        - `C13`:
          - `type`: float
          - `unit`: GPa
        - `C33`:
          - `type`: float
          - `unit`: GPa
        - `C44`:
          - `type`: float
          - `unit`: GPa
        - `C66`:
          - `type`: float
          - `unit`: GPa
        - `bulk_modulus_B`:
          - `type`: float
          - `unit`: GPa
        - `shear_modulus_G`:
          - `type`: float
          - `unit`: GPa
        - `young_modulus_E`:
          - `type`: float
          - `unit`: GPa
        - `poisson_ratio_nu`:
          - `type`: float
        - `G_B_ratio`:
          - `type`: float
        - `born_stable`:
          - `type`: boolean
    - `Pm-3m-FePt3`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`, `bulk_modulus_B`, `shear_modulus_G`, `young_modulus_E`, `poisson_ratio_nu`, `G_B_ratio`, `born_stable`
      - `fields`:
        - `C11`:
          - `type`: float
          - `unit`: GPa
        - `C12`:
          - `type`: float
          - `unit`: GPa
        - `C44`:
          - `type`: float
          - `unit`: GPa
        - `bulk_modulus_B`:
          - `type`: float
          - `unit`: GPa
        - `shear_modulus_G`:
          - `type`: float
          - `unit`: GPa
        - `young_modulus_E`:
          - `type`: float
          - `unit`: GPa
        - `poisson_ratio_nu`:
          - `type`: float
        - `G_B_ratio`:
          - `type`: float
        - `born_stable`:
          - `type`: boolean

### dynamical_stability.json
- path: `/app/outputs/dynamical_stability.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Minimum phonon frequency across the Brillouin zone and the dynamical stability verdict for each phase.
- schema:
  - `type`: object
  - `description`: Keys are structure names; each value is an object with min_phonon_frequency_THz (float, negative for instability) and dynamically_stable (boolean).
  - `required_keys`: `Pm-3m-Fe3Pt`, `I4/mmm-Fe3Pt`, `P4/mmm-FePt`, `Pm-3m-FePt3`
  - `field_spec`:
    - `*`:
      - `type`: object
      - `required`: `min_phonon_frequency_THz`, `dynamically_stable`
      - `fields`:
        - `min_phonon_frequency_THz`:
          - `type`: float
          - `unit`: THz
        - `dynamically_stable`:
          - `type`: boolean

### thermodynamic_properties.json
- path: `/app/outputs/thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Debye temperature and isochoric heat capacity at 300 K derived from the phonon density of states.
- schema:
  - `type`: object
  - `description`: Keys are structure names; each value is an object with Debye temperature and isochoric heat capacity at 300 K.
  - `required_keys`: `Pm-3m-Fe3Pt`, `I4/mmm-Fe3Pt`, `P4/mmm-FePt`, `Pm-3m-FePt3`
  - `field_spec`:
    - `*`:
      - `type`: object
      - `required`: `Debye_temperature_K`, `heat_capacity_Cv_at_300K`
      - `fields`:
        - `Debye_temperature_K`:
          - `type`: float
          - `unit`: K
        - `heat_capacity_Cv_at_300K`:
          - `type`: float
          - `unit`: cal/(cell·K)

Notes: All three scored artifacts are load-bearing: the elastic constants and moduli, the dynamical stability check, and the thermodynamic quantities must be produced from the DFT and phonon workflows. The checker compares them against the paper's reported values using tolerances appropriate for a re-run with an open-source toolchain.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants_and_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Top-level keys are structure names 'Pm-3m-Fe3Pt', 'I4/mmm-Fe3Pt', 'P4/mmm-FePt', 'Pm-3m-FePt3'. Each value is an object containing elastic constants and moduli.",
        "required_keys": [
          "Pm-3m-Fe3Pt",
          "I4/mmm-Fe3Pt",
          "P4/mmm-FePt",
          "Pm-3m-FePt3"
        ],
        "field_spec": {
          "Pm-3m-Fe3Pt": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44",
              "bulk_modulus_B",
              "shear_modulus_G",
              "young_modulus_E",
              "poisson_ratio_nu",
              "G_B_ratio",
              "born_stable"
            ],
            "fields": {
              "C11": {
                "type": "float",
                "unit": "GPa"
              },
              "C12": {
                "type": "float",
                "unit": "GPa"
              },
              "C44": {
                "type": "float",
                "unit": "GPa"
              },
              "bulk_modulus_B": {
                "type": "float",
                "unit": "GPa"
              },
              "shear_modulus_G": {
                "type": "float",
                "unit": "GPa"
              },
              "young_modulus_E": {
                "type": "float",
                "unit": "GPa"
              },
              "poisson_ratio_nu": {
                "type": "float"
              },
              "G_B_ratio": {
                "type": "float"
              },
              "born_stable": {
                "type": "boolean"
              }
            }
          },
          "I4/mmm-Fe3Pt": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C13",
              "C33",
              "C44",
              "C66",
              "bulk_modulus_B",
              "shear_modulus_G",
              "young_modulus_E",
              "poisson_ratio_nu",
              "G_B_ratio",
              "born_stable"
            ],
            "fields": {
              "C11": {
                "type": "float",
                "unit": "GPa"
              },
              "C12": {
                "type": "float",
                "unit": "GPa"
              },
              "C13": {
                "type": "float",
                "unit": "GPa"
              },
              "C33": {
                "type": "float",
                "unit": "GPa"
              },
              "C44": {
                "type": "float",
                "unit": "GPa"
              },
              "C66": {
                "type": "float",
                "unit": "GPa"
              },
              "bulk_modulus_B": {
                "type": "float",
                "unit": "GPa"
              },
              "shear_modulus_G": {
                "type": "float",
                "unit": "GPa"
              },
              "young_modulus_E": {
                "type": "float",
                "unit": "GPa"
              },
              "poisson_ratio_nu": {
                "type": "float"
              },
              "G_B_ratio": {
                "type": "float"
              },
              "born_stable": {
                "type": "boolean"
              }
            }
          },
          "P4/mmm-FePt": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C13",
              "C33",
              "C44",
              "C66",
              "bulk_modulus_B",
              "shear_modulus_G",
              "young_modulus_E",
              "poisson_ratio_nu",
              "G_B_ratio",
              "born_stable"
            ],
            "fields": {
              "C11": {
                "type": "float",
                "unit": "GPa"
              },
              "C12": {
                "type": "float",
                "unit": "GPa"
              },
              "C13": {
                "type": "float",
                "unit": "GPa"
              },
              "C33": {
                "type": "float",
                "unit": "GPa"
              },
              "C44": {
                "type": "float",
                "unit": "GPa"
              },
              "C66": {
                "type": "float",
                "unit": "GPa"
              },
              "bulk_modulus_B": {
                "type": "float",
                "unit": "GPa"
              },
              "shear_modulus_G": {
                "type": "float",
                "unit": "GPa"
              },
              "young_modulus_E": {
                "type": "float",
                "unit": "GPa"
              },
              "poisson_ratio_nu": {
                "type": "float"
              },
              "G_B_ratio": {
                "type": "float"
              },
              "born_stable": {
                "type": "boolean"
              }
            }
          },
          "Pm-3m-FePt3": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44",
              "bulk_modulus_B",
              "shear_modulus_G",
              "young_modulus_E",
              "poisson_ratio_nu",
              "G_B_ratio",
              "born_stable"
            ],
            "fields": {
              "C11": {
                "type": "float",
                "unit": "GPa"
              },
              "C12": {
                "type": "float",
                "unit": "GPa"
              },
              "C44": {
                "type": "float",
                "unit": "GPa"
              },
              "bulk_modulus_B": {
                "type": "float",
                "unit": "GPa"
              },
              "shear_modulus_G": {
                "type": "float",
                "unit": "GPa"
              },
              "young_modulus_E": {
                "type": "float",
                "unit": "GPa"
              },
              "poisson_ratio_nu": {
                "type": "float"
              },
              "G_B_ratio": {
                "type": "float"
              },
              "born_stable": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "Computed monocrystalline elastic constants, derived polycrystalline moduli, and mechanical stability verdicts for the four Fe-Pt alloys."
    },
    {
      "file": "dynamical_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Keys are structure names; each value is an object with min_phonon_frequency_THz (float, negative for instability) and dynamically_stable (boolean).",
        "required_keys": [
          "Pm-3m-Fe3Pt",
          "I4/mmm-Fe3Pt",
          "P4/mmm-FePt",
          "Pm-3m-FePt3"
        ],
        "field_spec": {
          "*": {
            "type": "object",
            "required": [
              "min_phonon_frequency_THz",
              "dynamically_stable"
            ],
            "fields": {
              "min_phonon_frequency_THz": {
                "type": "float",
                "unit": "THz"
              },
              "dynamically_stable": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "Minimum phonon frequency across the Brillouin zone and the dynamical stability verdict for each phase."
    },
    {
      "file": "thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "Keys are structure names; each value is an object with Debye temperature and isochoric heat capacity at 300 K.",
        "required_keys": [
          "Pm-3m-Fe3Pt",
          "I4/mmm-Fe3Pt",
          "P4/mmm-FePt",
          "Pm-3m-FePt3"
        ],
        "field_spec": {
          "*": {
            "type": "object",
            "required": [
              "Debye_temperature_K",
              "heat_capacity_Cv_at_300K"
            ],
            "fields": {
              "Debye_temperature_K": {
                "type": "float",
                "unit": "K"
              },
              "heat_capacity_Cv_at_300K": {
                "type": "float",
                "unit": "cal/(cell·K)"
              }
            }
          }
        }
      },
      "description": "Debye temperature and isochoric heat capacity at 300 K derived from the phonon density of states."
    }
  ],
  "notes": "All three scored artifacts are load-bearing: the elastic constants and moduli, the dynamical stability check, and the thermodynamic quantities must be produced from the DFT and phonon workflows. The checker compares them against the paper's reported values using tolerances appropriate for a re-run with an open-source toolchain."
}
```

## How you are scored
Each of the three scored artifacts is independently evaluated by a hidden verifier. The verifier compares your computed elastic constants and polycrystalline moduli to reference values, within tolerances that account for legitimate toolchain differences. It checks that the Born stability conditions are correctly applied. For dynamical stability, the verifier assesses whether the reported minimum phonon frequency leads to the correct stability classification. The thermodynamic values (Debye temperature and heat capacity) are compared against expected ranges. The final reward is a weighted sum across the three artifacts. The verifier may also check for internal consistency (e.g., agreement between elastic‑constant‑derived and phonon‑derived Debye temperature) to ensure the workflow was genuinely executed. Reporting a number without running the full DFT and phonon pipeline will not yield a competitive score.
