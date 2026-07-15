# Photocatalytic Water Splitting Band Edge Assessment

## Problem background
Photocatalytic water splitting is a promising route for renewable hydrogen production. Two-dimensional semiconductors offer large surface areas and short carrier migration distances that can improve charge separation compared with bulk materials. Janus MoSSe, a monolayer where one chalcogenide surface is S and the other is Se, is a candidate photocatalyst. Its performance may be enhanced by forming van der Waals heterostructures with nitride monolayers GaN or AlN. The key questions are whether such MoSSe/GaN and MoSSe/AlN heterostructures exhibit a type-II band alignment that separates photogenerated electrons and holes, band edge positions that straddle the water redox potentials, high carrier mobilities, interfacial charge transfer that creates a built-in electric field, and strong optical absorption. This task reproduces the first-principles assessment of these properties to evaluate the potential of these heterostructures as efficient water-splitting photocatalysts.

## Approach
The reproduction uses density functional theory (DFT) with the generalized gradient approximation (Perdew–Burke–Ernzerhof, PBE) for structural relaxation and the Heyd–Scuseria–Ernzerhof (HSE06) hybrid functional for accurate electronic and optical properties. Honeycomb monolayers of MoSSe, GaN, and AlN are constructed using their known lattice constants, then optimized. The MoSSe/XN (X=Ga,Al) heterostructures are built in the most stable stacking configuration and fully relaxed. The workflow computes: (1) relaxed geometries (lattice constants, interlayer distances, formation energies); (2) projected band structures at the HSE06 level to determine band gaps and band edge positions relative to vacuum; (3) carrier mobilities using the two-dimensional Bardeen–Shockley method: effective masses are extracted from band structures, deformation potentials and elastic moduli are obtained from uniaxial strain calculations, and mobilities for electrons and holes along armchair and zigzag directions are evaluated at 300 K; (4) interfacial charge redistribution via charge density difference, total transferred charge, and plane-averaged electrostatic potential drop; (5) optical absorption spectra from the frequency-dependent dielectric function. All final quantities are assembled into a single structured JSON report.

## Reproduction target
Produce a JSON file at `/app/outputs/results.json` containing two top-level keys, `mo_sse_gaN` and `mo_sse_alN`. For each heterostructure the JSON must report: the relaxed lattice constant (Å), the interface distance (Å), the formation energy (meV/Å²), the HSE06 band gap (eV), the conduction band minimum and valence band maximum energies relative to the vacuum level (eV), a list of carrier mobilities (each entry specifying the transport direction, carrier type electron/hole, effective mass, deformation potential, elastic modulus, and mobility in cm²·V⁻¹·s⁻¹), the total transferred charge (|e|), the potential drop across the interface (eV), and a list of optical absorption peaks (each giving wavelength in nm and absorption coefficient in cm⁻¹). All numeric values should be computed through the workflow steps executed on the MoSSe/XN heterostructures; the goal is to obtain a self-consistent set of structural, electronic, transport, interfacial, and optical properties.

## Assets

- Quantum ESPRESSO (or compatible open-source DFT code): https://www.quantum-espresso.org/
- Pseudopotentials for Mo, S, Se, Ga, Al, N (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization of monolayers and heterostructures
- Role: process
- Action: Build honeycomb models for MoSSe, GaN, and AlN monolayers using known lattice constants (MoSSe ~3.228 Å, GaN ~3.255 Å, AlN ~3.127 Å). Perform geometry optimization of each monolayer. Construct MoSSe/GaN and MoSSe/AlN vdW heterostructures with the most stable stacking (σ6) and fully relax atomic positions and cell parameters. Record relaxed lattice constants, bond lengths, interface distances, and formation energies.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: HSE06 band structure and band edge alignment
- Role: process
- Action: Using the relaxed heterostructure geometries, perform HSE06 calculations to obtain projected band structures and the energies of the conduction band minimum (CBM) and valence band maximum (VBM) relative to the vacuum level. Determine band gaps and band offsets. Verify that the CBM is above the H⁺/H₂ reduction potential (−4.44 eV) and the VBM is below the O₂/H₂O oxidation potential (−5.67 eV) at pH 0.
- Evidence: `/app/outputs/band_structure.log`

### Step 3: Carrier mobility via Bardeen–Shockley method
- Role: process
- Action: Extract effective masses for electrons and holes along armchair and zigzag directions from band structures. Apply uniaxial strain to compute deformation potential constants by tracking CBM/VBM shifts, and determine elastic modulus from strain-energy curves. Use the 2D Bardeen–Shockley formula at T=300 K to calculate carrier mobilities for electrons and holes in both transport directions.
- Evidence: `/app/outputs/mobility_data.log`

### Step 4: Interfacial charge transfer and built-in electric field
- Role: process
- Action: Compute charge density difference between heterostructure and isolated monolayers. Integrate to obtain total transferred charge. Calculate plane-averaged electrostatic potential across the interface and extract the potential drop.
- Evidence: `/app/outputs/charge_transfer.log`

### Step 5: Optical absorption spectrum
- Role: process
- Action: Compute frequency-dependent dielectric function from DFT, then calculate absorption coefficient spectrum. Identify the peak wavelengths and their corresponding absorption coefficients in the UV and visible regions.
- Evidence: `/app/outputs/absorption_spectrum.dat`

### Step 6: Collect final quantitative results
- Role: scored (load-bearing)
- Action: Gather all computed quantities from the previous steps and write them into a single JSON file at /app/outputs/results.json. The JSON must contain two top-level keys 'mo_sse_gaN' and 'mo_sse_alN', each holding structural, electronic, transport, interfacial, and optical data as specified in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"mo_sse_gaN": {"lattice_constant_A": <float>, "interface_distance_A": <float>, "formation_energy_meV_per_Ang2": <float>, "band_gap_eV": <float>, "cbm_vs_vacuum_eV": <float>, "vbm_vs_vacuum_eV": <float>, "carrier_mobilities": [{"direction": "<string>", "carrier_type": "<string>", "effective_mass": <float>, "deformation_potential_eV": <float>, "elastic_modulus_N_per_m": <float>, "mobility_cm2_V_s": <float>}, ...], "charge_transfer_e": <float>, "potential_drop_eV": <float>, "optical_absorption_peaks": [{"wavelength_nm": <float>, "absorption_coefficient_cm1": <float>}, ...]}, "mo_sse_alN": { ... same structure ... }}
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
- description: JSON file containing all reproduced structural, electronic, transport, interfacial, and optical properties for MoSSe/GaN and MoSSe/AlN vdW heterostructures.
- schema:
  - `type`: object
  - `required`: `mo_sse_gaN`, `mo_sse_alN`
  - `properties`:
    - `mo_sse_gaN`:
      - `type`: object
      - `required`: `lattice_constant_A`, `interface_distance_A`, `formation_energy_meV_per_Ang2`, `band_gap_eV`, `cbm_vs_vacuum_eV`, `vbm_vs_vacuum_eV`, `carrier_mobilities`, `charge_transfer_e`, `potential_drop_eV`, `optical_absorption_peaks`
      - `properties`:
        - `lattice_constant_A`:
          - `type`: number
        - `interface_distance_A`:
          - `type`: number
        - `formation_energy_meV_per_Ang2`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number
        - `cbm_vs_vacuum_eV`:
          - `type`: number
        - `vbm_vs_vacuum_eV`:
          - `type`: number
        - `carrier_mobilities`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `direction`, `carrier_type`, `effective_mass`, `deformation_potential_eV`, `elastic_modulus_N_per_m`, `mobility_cm2_V_s`
            - `properties`:
              - `direction`:
                - `type`: string
              - `carrier_type`:
                - `type`: string
                - `enum`: `electron`, `hole`
              - `effective_mass`:
                - `type`: number
              - `deformation_potential_eV`:
                - `type`: number
              - `elastic_modulus_N_per_m`:
                - `type`: number
              - `mobility_cm2_V_s`:
                - `type`: number
        - `charge_transfer_e`:
          - `type`: number
        - `potential_drop_eV`:
          - `type`: number
        - `optical_absorption_peaks`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `wavelength_nm`, `absorption_coefficient_cm1`
            - `properties`:
              - `wavelength_nm`:
                - `type`: number
              - `absorption_coefficient_cm1`:
                - `type`: number
    - `mo_sse_alN`:
      - `type`: object
      - `required`: `lattice_constant_A`, `interface_distance_A`, `formation_energy_meV_per_Ang2`, `band_gap_eV`, `cbm_vs_vacuum_eV`, `vbm_vs_vacuum_eV`, `carrier_mobilities`, `charge_transfer_e`, `potential_drop_eV`, `optical_absorption_peaks`
      - `properties`:
        - `lattice_constant_A`:
          - `type`: number
        - `interface_distance_A`:
          - `type`: number
        - `formation_energy_meV_per_Ang2`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number
        - `cbm_vs_vacuum_eV`:
          - `type`: number
        - `vbm_vs_vacuum_eV`:
          - `type`: number
        - `carrier_mobilities`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `direction`, `carrier_type`, `effective_mass`, `deformation_potential_eV`, `elastic_modulus_N_per_m`, `mobility_cm2_V_s`
            - `properties`:
              - `direction`:
                - `type`: string
              - `carrier_type`:
                - `type`: string
                - `enum`: `electron`, `hole`
              - `effective_mass`:
                - `type`: number
              - `deformation_potential_eV`:
                - `type`: number
              - `elastic_modulus_N_per_m`:
                - `type`: number
              - `mobility_cm2_V_s`:
                - `type`: number
        - `charge_transfer_e`:
          - `type`: number
        - `potential_drop_eV`:
          - `type`: number
        - `optical_absorption_peaks`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `wavelength_nm`, `absorption_coefficient_cm1`
            - `properties`:
              - `wavelength_nm`:
                - `type`: number
              - `absorption_coefficient_cm1`:
                - `type`: number

Notes: The checker will compare each numeric quantity in results.json to the paper's reported values using tolerances appropriate for the domain (e.g., structural parameters ±0.01 Å, electronic energies ±0.1 eV, mobilities ±20%, charge transfer ±0.01 |e|, absorption peaks ±5%). Directional metrics (e.g., mobility where higher is better) that exceed the paper's value are considered full credit.

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
          "mo_sse_gaN",
          "mo_sse_alN"
        ],
        "properties": {
          "mo_sse_gaN": {
            "type": "object",
            "required": [
              "lattice_constant_A",
              "interface_distance_A",
              "formation_energy_meV_per_Ang2",
              "band_gap_eV",
              "cbm_vs_vacuum_eV",
              "vbm_vs_vacuum_eV",
              "carrier_mobilities",
              "charge_transfer_e",
              "potential_drop_eV",
              "optical_absorption_peaks"
            ],
            "properties": {
              "lattice_constant_A": {
                "type": "number"
              },
              "interface_distance_A": {
                "type": "number"
              },
              "formation_energy_meV_per_Ang2": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              },
              "cbm_vs_vacuum_eV": {
                "type": "number"
              },
              "vbm_vs_vacuum_eV": {
                "type": "number"
              },
              "carrier_mobilities": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "direction",
                    "carrier_type",
                    "effective_mass",
                    "deformation_potential_eV",
                    "elastic_modulus_N_per_m",
                    "mobility_cm2_V_s"
                  ],
                  "properties": {
                    "direction": {
                      "type": "string"
                    },
                    "carrier_type": {
                      "type": "string",
                      "enum": [
                        "electron",
                        "hole"
                      ]
                    },
                    "effective_mass": {
                      "type": "number"
                    },
                    "deformation_potential_eV": {
                      "type": "number"
                    },
                    "elastic_modulus_N_per_m": {
                      "type": "number"
                    },
                    "mobility_cm2_V_s": {
                      "type": "number"
                    }
                  }
                }
              },
              "charge_transfer_e": {
                "type": "number"
              },
              "potential_drop_eV": {
                "type": "number"
              },
              "optical_absorption_peaks": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "wavelength_nm",
                    "absorption_coefficient_cm1"
                  ],
                  "properties": {
                    "wavelength_nm": {
                      "type": "number"
                    },
                    "absorption_coefficient_cm1": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "mo_sse_alN": {
            "type": "object",
            "required": [
              "lattice_constant_A",
              "interface_distance_A",
              "formation_energy_meV_per_Ang2",
              "band_gap_eV",
              "cbm_vs_vacuum_eV",
              "vbm_vs_vacuum_eV",
              "carrier_mobilities",
              "charge_transfer_e",
              "potential_drop_eV",
              "optical_absorption_peaks"
            ],
            "properties": {
              "lattice_constant_A": {
                "type": "number"
              },
              "interface_distance_A": {
                "type": "number"
              },
              "formation_energy_meV_per_Ang2": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              },
              "cbm_vs_vacuum_eV": {
                "type": "number"
              },
              "vbm_vs_vacuum_eV": {
                "type": "number"
              },
              "carrier_mobilities": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "direction",
                    "carrier_type",
                    "effective_mass",
                    "deformation_potential_eV",
                    "elastic_modulus_N_per_m",
                    "mobility_cm2_V_s"
                  ],
                  "properties": {
                    "direction": {
                      "type": "string"
                    },
                    "carrier_type": {
                      "type": "string",
                      "enum": [
                        "electron",
                        "hole"
                      ]
                    },
                    "effective_mass": {
                      "type": "number"
                    },
                    "deformation_potential_eV": {
                      "type": "number"
                    },
                    "elastic_modulus_N_per_m": {
                      "type": "number"
                    },
                    "mobility_cm2_V_s": {
                      "type": "number"
                    }
                  }
                }
              },
              "charge_transfer_e": {
                "type": "number"
              },
              "potential_drop_eV": {
                "type": "number"
              },
              "optical_absorption_peaks": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "wavelength_nm",
                    "absorption_coefficient_cm1"
                  ],
                  "properties": {
                    "wavelength_nm": {
                      "type": "number"
                    },
                    "absorption_coefficient_cm1": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "JSON file containing all reproduced structural, electronic, transport, interfacial, and optical properties for MoSSe/GaN and MoSSe/AlN vdW heterostructures."
    }
  ],
  "notes": "The checker will compare each numeric quantity in results.json to the paper's reported values using tolerances appropriate for the domain (e.g., structural parameters ±0.01 Å, electronic energies ±0.1 eV, mobilities ±20%, charge transfer ±0.01 |e|, absorption peaks ±5%). Directional metrics (e.g., mobility where higher is better) that exceed the paper's value are considered full credit."
}
```

## How you are scored
A hidden verifier will evaluate each workflow stage's output independently. The verifier reads the evidence files from the process steps and the final `results.json`. It compares the reported quantities against expected reference values obtained from the original study using tolerances appropriate for DFT reproduction (e.g., tight tolerances for structural parameters, moderate tolerances for method‑sensitive quantities such as band gaps and mobilities). Directional metrics (where larger is better) that meet or exceed the reference receive full credit. The overall score is a weighted combination of the scores from all stages, with the main claims (band alignment, carrier mobilities, optical absorption peaks) carrying the largest weight. Simply writing plausible numbers without executing the calculations will not yield a high score.
