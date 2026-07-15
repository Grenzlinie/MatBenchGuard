# DFT investigation of Rb doping effects on structural, electronic, optical, and thermoelectric properties of KCl

## Problem background
The problem is to determine the effect of substituting half the K atoms with Rb in KCl, forming the K0.5Rb0.5Cl alloy, on its structural, electronic, optical, and thermoelectric properties. The work applies density functional theory (DFT) within the generalized gradient approximation (GGA-PBE) using the full-potential linearized augmented plane-wave method (FP-LAPW). By comparing pure KCl and the doped alloy, the study addresses changes in the equilibrium lattice constant, bulk modulus, pressure derivative, direct band gap, static dielectric constant, refractive index, extinction coefficient peak, Seebeck coefficient, and electrical conductivity. Your task is to independently compute these properties for both materials and report them in a structured format, thereby reproducing the computational findings.

## Approach
The computational approach employs first-principles DFT calculations to treat the two systems: pure KCl in the Fm3m (NaCl-type) structure, and the K0.5Rb0.5Cl alloy modeled by a 2×2×2 supercell where four K atoms are replaced by Rb, resulting in Fd3m symmetry. All calculations use the FP-LAPW method with the GGA-PBE exchange-correlation functional.

The properties are derived in a sequence of stages:
1. **Equation of state:** total energies are computed over a range of volumes for each compound, and the Birch-Murnaghan equation of state is fitted to obtain the equilibrium lattice constant a0, bulk modulus B, and its pressure derivative B'.
2. **Electronic structure:** a self-consistent field calculation yields the ground-state charge density and Kohn-Sham eigenvalues. A non-self-consistent band structure along high-symmetry lines is then computed, from which the direct band gap at Γ is extracted.
3. **Optical response:** the complex dielectric function ε(ω) = ε1(ω) + i ε2(ω) is calculated using the Kohn-Sham eigenvalues and momentum matrix elements, covering photon energies up to 13.5 eV. From ε(ω), the static dielectric constant ε1(0), refractive index n(0), the main peaks in ε1 and ε2, and the extinction coefficient k(ω) peak are derived.
4. **Thermoelectric transport:** the Seebeck coefficient and electrical conductivity are obtained from the band energies via semi-classical Boltzmann transport theory (using the BoltzTraP2 code) over the temperature range 50-800 K; values are extracted at 50 K and 800 K.

At each stage the results for pure KCl and the K0.5Rb0.5Cl alloy are compared to isolate the changes induced by Rb doping.

## Reproduction target
Produce the following quantities for both KCl and K0.5Rb0.5Cl:
- From Birch-Murnaghan EOS fit: equilibrium lattice constant a0 (in Å), bulk modulus B (in GPa), and pressure derivative B'.
- Direct band gap Eg (in eV) at the Γ point, and confirm that the gap is direct (VBM and CBM both at Γ).
- Optical properties extracted from the dielectric function up to 13.5 eV: static dielectric constant ε1(0), refractive index n(0), the energy and value of the first ε1 peak, the energies and values of the two main ε2 peaks, and the energy and value of the extinction coefficient k peak.
- Thermoelectric transport coefficients: Seebeck coefficient S (in μV/K) and electrical conductivity σ (in Ω⁻¹ cm⁻¹) at 50 K and 800 K.

Additionally, compare the Seebeck coefficients of KCl and the alloy at 50 K and at 800 K, and note the relative ordering (which material has the larger value).

All results must be written to the specified JSON files under `/app/outputs`.

## Assets

- FP-LAPW DFT code (Elk, exciting, or ABINIT): http://elk.sourceforge.net/
- BoltzTraP2: https://gitlab.com/sousaw/BoltzTraP2
- Python with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Supercell generation and total-energy scan for equation of state
- Role: process
- Action: Construct 2×2×2 supercells for KCl (Fm3m) and K0.5Rb0.5Cl (Fd3m) with Rb substitution. Using an FP-LAPW code with GGA-PBE, perform total-energy calculations at multiple volumes around the expected equilibrium for each compound. Output the calculated energies vs volume.
- Evidence: `/app/outputs/eos_energies.csv`

### Step 2: Equation-of-state fitting and structural properties
- Role: scored
- Action: Fit the total-energy vs volume data to the Birch-Murnaghan equation of state. Extract equilibrium lattice constant a0, bulk modulus B, and pressure derivative B' for both KCl and K0.5Rb0.5Cl. Write the results.
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: JSON object with keys 'KCl' and 'K0.5Rb0.5Cl', each an object with 'a0' (float, Å), 'B' (float, GPa), 'Bprime' (float).
- Scoring: scored by hidden verifier

### Step 3: Self-consistent field (SCF) calculation
- Role: process
- Action: Using the equilibrium lattice constants, perform self-consistent DFT calculation for KCl and K0.5Rb0.5Cl to obtain the ground-state charge density and Kohn-Sham eigenvalues on a suitable k-mesh. Record convergence evidence.
- Evidence: `/app/outputs/scf_converged.log`

### Step 4: Band structure and direct band gap
- Role: scored
- Action: Compute non-self-consistent band structure along high-symmetry paths for both compounds. Determine the direct band gap (VBM and CBM at Γ). Write the band gap values and gap nature.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: JSON object with keys 'KCl' (float), 'K0.5Rb0.5Cl' (float), and 'nature' (string, expected 'direct').
- Scoring: scored by hidden verifier

### Step 5: Optical dielectric function and derived constants
- Role: scored (load-bearing)
- Action: From Kohn-Sham eigenvalues and momentum matrix elements, compute the complex dielectric function ε(ω) up to 13.5 eV. Derive static dielectric constant ε1(0), refractive index n(0), ε1 peak, two main ε2 peaks, and the peak of extinction coefficient k with its energy. Write all values.
- Output file: `/app/outputs/optical_properties.json`
- Format: json
- Contract: JSON object with keys 'KCl' and 'K0.5Rb0.5Cl'. Each contains: 'epsilon1_0' (float), 'n_0' (float), 'epsilon1_peak' (object with 'energy' (float, eV) and 'value' (float)), 'epsilon2_peaks' (list of two objects, each with 'energy' (float) and 'value' (float)), 'k_peak' (object with 'energy' (float, eV) and 'value' (float)).
- Scoring: scored by hidden verifier

### Step 6: Thermoelectric transport coefficients
- Role: scored
- Action: Compute the Seebeck coefficient and electrical conductivity as functions of temperature using semi-classical Boltzmann theory (BoltzTraP2) based on the SCF band energies. Extract values at 50 K and 800 K for both compounds. Write the results.
- Output file: `/app/outputs/thermoelectric_properties.json`
- Format: json
- Contract: JSON object with keys 'KCl' and 'K0.5Rb0.5Cl'. Each contains: 'Seebeck_50K' (float, μV/K), 'Seebeck_800K' (float), 'conductivity_50K' (float, Ω⁻¹ cm⁻¹), 'conductivity_800K' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.json`
- `/app/outputs/band_gap.json`
- `/app/outputs/optical_properties.json`
- `/app/outputs/thermoelectric_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted equilibrium lattice constant, bulk modulus and pressure derivative from Birch-Murnaghan EOS.
- schema:
  - `type`: object
  - `required`: `KCl`, `K0.5Rb0.5Cl`
  - `properties`:
    - `KCl`:
      - `type`: object
      - `required`: `a0`, `B`, `Bprime`
      - `properties`:
        - `a0`:
          - `type`: number
          - `units`: Å
        - `B`:
          - `type`: number
          - `units`: GPa
        - `Bprime`:
          - `type`: number
    - `K0.5Rb0.5Cl`:
      - `type`: object
      - `required`: `a0`, `B`, `Bprime`
      - `properties`:
        - `a0`:
          - `type`: number
          - `units`: Å
        - `B`:
          - `type`: number
          - `units`: GPa
        - `Bprime`:
          - `type`: number

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Direct band gap values and nature (must be 'direct') for both compounds.
- schema:
  - `type`: object
  - `required`: `KCl`, `K0.5Rb0.5Cl`, `nature`
  - `properties`:
    - `KCl`:
      - `type`: number
      - `units`: eV
    - `K0.5Rb0.5Cl`:
      - `type`: number
      - `units`: eV
    - `nature`:
      - `type`: string
      - `enum`: `direct`

### optical_properties.json
- path: `/app/outputs/optical_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static dielectric constant, refractive index, peaks in ε1 and ε2, and extinction coefficient peak derived from the complex dielectric function.
- schema:
  - `type`: object
  - `required`: `KCl`, `K0.5Rb0.5Cl`
  - `properties`:
    - `KCl`:
      - `type`: object
      - `required`: `epsilon1_0`, `n_0`, `epsilon1_peak`, `epsilon2_peaks`, `k_peak`
      - `properties`:
        - `epsilon1_0`:
          - `type`: number
        - `n_0`:
          - `type`: number
        - `epsilon1_peak`:
          - `type`: object
          - `required`: `energy`, `value`
          - `properties`:
            - `energy`:
              - `type`: number
              - `units`: eV
            - `value`:
              - `type`: number
        - `epsilon2_peaks`:
          - `type`: array
          - `minItems`: 2
          - `maxItems`: 2
          - `items`:
            - `type`: object
            - `required`: `energy`, `value`
            - `properties`:
              - `energy`:
                - `type`: number
                - `units`: eV
              - `value`:
                - `type`: number
        - `k_peak`:
          - `type`: object
          - `required`: `energy`, `value`
          - `properties`:
            - `energy`:
              - `type`: number
              - `units`: eV
            - `value`:
              - `type`: number
    - `K0.5Rb0.5Cl`:
      - `type`: object
      - `required`: `epsilon1_0`, `n_0`, `epsilon1_peak`, `epsilon2_peaks`, `k_peak`
      - `properties`:
        - `epsilon1_0`:
          - `type`: number
        - `n_0`:
          - `type`: number
        - `epsilon1_peak`:
          - `type`: object
          - `required`: `energy`, `value`
          - `properties`:
            - `energy`:
              - `type`: number
              - `units`: eV
            - `value`:
              - `type`: number
        - `epsilon2_peaks`:
          - `type`: array
          - `minItems`: 2
          - `maxItems`: 2
          - `items`:
            - `type`: object
            - `required`: `energy`, `value`
            - `properties`:
              - `energy`:
                - `type`: number
                - `units`: eV
              - `value`:
                - `type`: number
        - `k_peak`:
          - `type`: object
          - `required`: `energy`, `value`
          - `properties`:
            - `energy`:
              - `type`: number
              - `units`: eV
            - `value`:
              - `type`: number

### thermoelectric_properties.json
- path: `/app/outputs/thermoelectric_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Seebeck coefficient and electrical conductivity at 50 K and 800 K from Boltzmann transport.
- schema:
  - `type`: object
  - `required`: `KCl`, `K0.5Rb0.5Cl`
  - `properties`:
    - `KCl`:
      - `type`: object
      - `required`: `Seebeck_50K`, `Seebeck_800K`, `conductivity_50K`, `conductivity_800K`
      - `properties`:
        - `Seebeck_50K`:
          - `type`: number
          - `units`: μV/K
        - `Seebeck_800K`:
          - `type`: number
          - `units`: μV/K
        - `conductivity_50K`:
          - `type`: number
          - `units`: Ω⁻¹ cm⁻¹
        - `conductivity_800K`:
          - `type`: number
          - `units`: Ω⁻¹ cm⁻¹
    - `K0.5Rb0.5Cl`:
      - `type`: object
      - `required`: `Seebeck_50K`, `Seebeck_800K`, `conductivity_50K`, `conductivity_800K`
      - `properties`:
        - `Seebeck_50K`:
          - `type`: number
          - `units`: μV/K
        - `Seebeck_800K`:
          - `type`: number
          - `units`: μV/K
        - `conductivity_50K`:
          - `type`: number
          - `units`: Ω⁻¹ cm⁻¹
        - `conductivity_800K`:
          - `type`: number
          - `units`: Ω⁻¹ cm⁻¹

Notes: All numerical quantities are compared to the paper's reported values using tolerances appropriate for code/functional differences. Nature of band gap must be 'direct'. The relative ordering of Seebeck coefficients between KCl and alloy at the two temperatures is also verified structurally.

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
          "KCl",
          "K0.5Rb0.5Cl"
        ],
        "properties": {
          "KCl": {
            "type": "object",
            "required": [
              "a0",
              "B",
              "Bprime"
            ],
            "properties": {
              "a0": {
                "type": "number",
                "units": "Å"
              },
              "B": {
                "type": "number",
                "units": "GPa"
              },
              "Bprime": {
                "type": "number"
              }
            }
          },
          "K0.5Rb0.5Cl": {
            "type": "object",
            "required": [
              "a0",
              "B",
              "Bprime"
            ],
            "properties": {
              "a0": {
                "type": "number",
                "units": "Å"
              },
              "B": {
                "type": "number",
                "units": "GPa"
              },
              "Bprime": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Fitted equilibrium lattice constant, bulk modulus and pressure derivative from Birch-Murnaghan EOS."
    },
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "KCl",
          "K0.5Rb0.5Cl",
          "nature"
        ],
        "properties": {
          "KCl": {
            "type": "number",
            "units": "eV"
          },
          "K0.5Rb0.5Cl": {
            "type": "number",
            "units": "eV"
          },
          "nature": {
            "type": "string",
            "enum": [
              "direct"
            ]
          }
        }
      },
      "description": "Direct band gap values and nature (must be 'direct') for both compounds."
    },
    {
      "file": "optical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "KCl",
          "K0.5Rb0.5Cl"
        ],
        "properties": {
          "KCl": {
            "type": "object",
            "required": [
              "epsilon1_0",
              "n_0",
              "epsilon1_peak",
              "epsilon2_peaks",
              "k_peak"
            ],
            "properties": {
              "epsilon1_0": {
                "type": "number"
              },
              "n_0": {
                "type": "number"
              },
              "epsilon1_peak": {
                "type": "object",
                "required": [
                  "energy",
                  "value"
                ],
                "properties": {
                  "energy": {
                    "type": "number",
                    "units": "eV"
                  },
                  "value": {
                    "type": "number"
                  }
                }
              },
              "epsilon2_peaks": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                  "type": "object",
                  "required": [
                    "energy",
                    "value"
                  ],
                  "properties": {
                    "energy": {
                      "type": "number",
                      "units": "eV"
                    },
                    "value": {
                      "type": "number"
                    }
                  }
                }
              },
              "k_peak": {
                "type": "object",
                "required": [
                  "energy",
                  "value"
                ],
                "properties": {
                  "energy": {
                    "type": "number",
                    "units": "eV"
                  },
                  "value": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "K0.5Rb0.5Cl": {
            "type": "object",
            "required": [
              "epsilon1_0",
              "n_0",
              "epsilon1_peak",
              "epsilon2_peaks",
              "k_peak"
            ],
            "properties": {
              "epsilon1_0": {
                "type": "number"
              },
              "n_0": {
                "type": "number"
              },
              "epsilon1_peak": {
                "type": "object",
                "required": [
                  "energy",
                  "value"
                ],
                "properties": {
                  "energy": {
                    "type": "number",
                    "units": "eV"
                  },
                  "value": {
                    "type": "number"
                  }
                }
              },
              "epsilon2_peaks": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                  "type": "object",
                  "required": [
                    "energy",
                    "value"
                  ],
                  "properties": {
                    "energy": {
                      "type": "number",
                      "units": "eV"
                    },
                    "value": {
                      "type": "number"
                    }
                  }
                }
              },
              "k_peak": {
                "type": "object",
                "required": [
                  "energy",
                  "value"
                ],
                "properties": {
                  "energy": {
                    "type": "number",
                    "units": "eV"
                  },
                  "value": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Static dielectric constant, refractive index, peaks in ε1 and ε2, and extinction coefficient peak derived from the complex dielectric function."
    },
    {
      "file": "thermoelectric_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "KCl",
          "K0.5Rb0.5Cl"
        ],
        "properties": {
          "KCl": {
            "type": "object",
            "required": [
              "Seebeck_50K",
              "Seebeck_800K",
              "conductivity_50K",
              "conductivity_800K"
            ],
            "properties": {
              "Seebeck_50K": {
                "type": "number",
                "units": "μV/K"
              },
              "Seebeck_800K": {
                "type": "number",
                "units": "μV/K"
              },
              "conductivity_50K": {
                "type": "number",
                "units": "Ω⁻¹ cm⁻¹"
              },
              "conductivity_800K": {
                "type": "number",
                "units": "Ω⁻¹ cm⁻¹"
              }
            }
          },
          "K0.5Rb0.5Cl": {
            "type": "object",
            "required": [
              "Seebeck_50K",
              "Seebeck_800K",
              "conductivity_50K",
              "conductivity_800K"
            ],
            "properties": {
              "Seebeck_50K": {
                "type": "number",
                "units": "μV/K"
              },
              "Seebeck_800K": {
                "type": "number",
                "units": "μV/K"
              },
              "conductivity_50K": {
                "type": "number",
                "units": "Ω⁻¹ cm⁻¹"
              },
              "conductivity_800K": {
                "type": "number",
                "units": "Ω⁻¹ cm⁻¹"
              }
            }
          }
        }
      },
      "description": "Seebeck coefficient and electrical conductivity at 50 K and 800 K from Boltzmann transport."
    }
  ],
  "notes": "All numerical quantities are compared to the paper's reported values using tolerances appropriate for code/functional differences. Nature of band gap must be 'direct'. The relative ordering of Seebeck coefficients between KCl and alloy at the two temperatures is also verified structurally."
}
```

## How you are scored
Your work is scored by an automated hidden verifier that compares the submitted JSON files against reference values derived from the original study. Each scored artifact (`structural_properties.json`, `band_gap.json`, `optical_properties.json`, `thermoelectric_properties.json`) is checked independently; the verifier examines the numeric quantities with generous tolerances that absorb legitimate differences between DFT codes and basis sets. The band gap must be reported as `"nature": "direct"`. The Seebeck coefficient ordering between KCl and the alloy at the two specified temperatures is also verified. The final score is a weighted combination of the individual checks. Submitting the expected numbers without performing the required calculations is not sufficient to guarantee a passing score, as the verifier also verifies structural consistency across artifacts.
