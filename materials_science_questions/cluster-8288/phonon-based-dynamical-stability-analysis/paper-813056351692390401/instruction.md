# Layer-Dependent Properties of MoS2 Nanosheets from DFT Calculations

## Problem background
Layered transition metal dichalcogenide MoS2 exhibits layer-number-dependent properties critical for nanoelectronics and catalysis. This work investigates how surface, cleaving, binding, and van der Waals energies, electronic band structure (especially the band gap of the 2H polytype), and optical properties (dielectric function, refractive index, absorption, reflectivity) vary with the number of layers for three polytypes (1T', 2H, 3R) using hybrid-functional DFT. The goal is to quantify the convergence of these properties from monolayer to bulk, providing physically meaningful asymptotic limits.

## Approach
Use density functional theory (DFT) with the HSE06 hybrid functional and Grimme-D3 van der Waals correction to calculate total energies, electronic band structures, and optical response functions. Start from bulk MoS2 and free atoms to obtain reference energies, then construct (001) slab models with vacuum spacing for each polytype across a range of layer numbers (from monolayer to a thick limit representing bulk). For each slab, compute the total energy, band gap (for 2H), and optical quantities (static dielectric constant, refractive index at zero and high frequency, absorption coefficient and reflectivity at characteristic peaks). From the total energies, derive surface energy as the difference between slab and equivalent bulk energy divided by twice surface area, cleaving energy as the energy required to separate a monolayer from an N-layer slab per area, binding energy per formula unit from atomic reference energies, and the van der Waals energy contribution. Fit each layer-number series with the model y = A - B * exp(-N / C) to extract asymptotic bulk values and report the fitting coefficients A, B, C. The workflow should be implemented with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and publicly available pseudopotentials.

## Reproduction target
Produce a single JSON file `results.json` containing: (1) for each polytype (1T', 2H, 3R), the asymptotic surface energy (J/m²), cleaving energy (J/m²), binding energy per MoS2 molecule (eV), and van der Waals energy contribution (J/m²) obtained from exponential fits to layer-number series; (2) a table of the direct band gap (eV) of 2H-MoS2 as a function of layer number N from 1 up to a thick limit; (3) for each polytype and for six optical quantities (static dielectric constant ε₁(0), static refractive index n(0), high-frequency dielectric constant ε₁(∞), high-frequency refractive index n(∞), absorption coefficient at the characteristic peak, and reflectivity at that peak), the three fitted parameters [A, B, C] of the model y = A - B * exp(-N / C). All quantities must be computed from the DFT pipeline described in the workflow steps, not looked up or guessed.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBEsol or PBE) for Mo and S: https://www.materialscloud.org/discover/sssp/table/precision
- Python 3 with numpy, scipy, matplotlib: python3.10+

## Workflow steps

### Step 1: Bulk reference DFT calculations
- Role: process
- Action: Perform DFT geometry optimization and electronic structure calculation for bulk MoS2 in 1T', 2H, and 3R phases using HSE06 hybrid functional with Grimme-D3 dispersion correction, using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO). Extract optimized lattice constants, total energy per formula unit, and electronic band gap for 2H.
- Evidence: none

### Step 2: Atomic reference energies
- Role: process
- Action: Calculate total energies of isolated Mo and S atoms using the same DFT settings (HSE06, same pseudopotentials, cubic cell with appropriate lattice constant) to obtain E_Mo and E_S reference energies.
- Evidence: none

### Step 3: Generate nanosheet slab models
- Role: process
- Action: Using the optimized bulk structures, cleave (001) slabs with vacuum spacing (approx. 20 Å) to create supercell models for layer numbers N = 1,2,3,4,5,6,7,8,10,12,15,20 for each polytype (1T', 2H, 3R). Assign initial lattice parameters and atomic coordinates.
- Evidence: none

### Step 4: DFT optimization and electronic structure of nanosheets
- Role: process
- Action: Perform full geometry optimization of all slab models with HSE06 + DFT-D. For each converged slab, compute total energy E_slab(N), and extract electronic band structure and band gap (direct/indirect character and value). Record the band gap vs layer number for the 2H phase.
- Evidence: none

### Step 5: Optical properties calculation
- Role: process
- Action: Using the optimized wavefunctions and electronic structure, compute the frequency-dependent dielectric function (real and imaginary parts), refractive index, absorption coefficient, and reflectivity for all nanosheet models. Extract static dielectric constant ε1(0), static refractive index n(0), high-frequency dielectric constant ε1(∞), high-frequency refractive index n(∞), and the absorption/reflectivity values at the characteristic peaks (~185 nm for 1T'/2H, ~220 nm for 3R).
- Evidence: none

### Step 6: Energy analysis, optical fitting, and final results
- Role: scored (load-bearing)
- Action: From the collected total energies and reference energies: compute surface energy E_surf(N) = [E_slab(N) - n*E_bulk]/(2S), cleaving energy E_cleav(N) = [E_{N-1} + E_1 - E_N]/S, binding energy per molecule E_bind(N) = [n*E_Mo + 2n*E_S - E_slab(N)]/(3n), and van der Waals energy contribution for each phase and layer. Fit exponential convergence functions to the layer-number series to obtain asymptotic bulk values. Export the 2H band gap values as a table. For optical quantities (ε1(0), n(0), ε1(∞), n(∞), absorption coefficient, reflectivity) fit exponential equations of the form A - B*exp(-layer/C) and report the fitted coefficients A, B, C. Write all computed quantities into a single JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "energies": {
    "1T'": { "surface_energy_asymptote_J_per_m2": "number", "cleaving_energy_asymptote_J_per_m2": "number", "binding_energy_asymptote_eV": "number", "vdw_energy_asymptote_J_per_m2": "number" },
    "2H": { "surface_energy_asymptote_J_per_m2": "number", "cleaving_energy_asymptote_J_per_m2": "number", "binding_energy_asymptote_eV": "number", "vdw_energy_asymptote_J_per_m2": "number" },
    "3R": { "surface_energy_asymptote_J_per_m2": "number", "cleaving_energy_asymptote_J_per_m2": "number", "binding_energy_asymptote_eV": "number", "vdw_energy_asymptote_J_per_m2": "number" }
  },
  "bandgap_2H": [
    { "layer": "int", "bandgap_eV": "number" }
  ],
  "optical": {
    "1T'": { "eps1_0_fit_coeffs": ["number", "number", "number"], "n_0_fit_coeffs": ["number", "number", "number"], "eps1_inf_fit_coeffs": ["number", "number", "number"], "n_inf_fit_coeffs": ["number", "number", "number"], "absorption_fit_coeffs": ["number", "number", "number"], "reflectivity_fit_coeffs": ["number", "number", "number"] },
    "2H": { "eps1_0_fit_coeffs": ["number", "number", "number"], "n_0_fit_coeffs": ["number", "number", "number"], "eps1_inf_fit_coeffs": ["number", "number", "number"], "n_inf_fit_coeffs": ["number", "number", "number"], "absorption_fit_coeffs": ["number", "number", "number"], "reflectivity_fit_coeffs": ["number", "number", "number"] },
    "3R": { "eps1_0_fit_coeffs": ["number", "number", "number"], "n_0_fit_coeffs": ["number", "number", "number"], "eps1_inf_fit_coeffs": ["number", "number", "number"], "n_inf_fit_coeffs": ["number", "number", "number"], "absorption_fit_coeffs": ["number", "number", "number"], "reflectivity_fit_coeffs": ["number", "number", "number"] }
  }
}
Note: fitting coefficients correspond to A, B, C in y = A - B*exp(-x/C).
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
- description: Aggregated layer-dependent properties and asymptotic values for all three polytypes, including energies, 2H band gap, and optical fitting coefficients. The checker compares each numerical value against paper-reported gold values with tolerances.
- schema:
  - `type`: object
  - `required`: `energies`, `bandgap_2H`, `optical`
  - `properties`:
    - `energies`:
      - `type`: object
      - `properties`:
        - `1T'`:
          - `type`: object
          - `properties`:
            - `surface_energy_asymptote_J_per_m2`:
              - `type`: number
            - `cleaving_energy_asymptote_J_per_m2`:
              - `type`: number
            - `binding_energy_asymptote_eV`:
              - `type`: number
            - `vdw_energy_asymptote_J_per_m2`:
              - `type`: number
        - `2H`:
          - `type`: object
          - `properties`:
            - `surface_energy_asymptote_J_per_m2`:
              - `type`: number
            - `cleaving_energy_asymptote_J_per_m2`:
              - `type`: number
            - `binding_energy_asymptote_eV`:
              - `type`: number
            - `vdw_energy_asymptote_J_per_m2`:
              - `type`: number
        - `3R`:
          - `type`: object
          - `properties`:
            - `surface_energy_asymptote_J_per_m2`:
              - `type`: number
            - `cleaving_energy_asymptote_J_per_m2`:
              - `type`: number
            - `binding_energy_asymptote_eV`:
              - `type`: number
            - `vdw_energy_asymptote_J_per_m2`:
              - `type`: number
    - `bandgap_2H`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `layer`:
            - `type`: integer
          - `bandgap_eV`:
            - `type`: number
    - `optical`:
      - `type`: object
      - `properties`:
        - `1T'`:
          - `type`: object
          - `properties`:
            - `eps1_0_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `n_0_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `eps1_inf_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `n_inf_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `absorption_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `reflectivity_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
        - `2H`:
          - `type`: object
          - `properties`:
            - `eps1_0_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `n_0_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `eps1_inf_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `n_inf_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `absorption_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `reflectivity_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
        - `3R`:
          - `type`: object
          - `properties`:
            - `eps1_0_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `n_0_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `eps1_inf_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `n_inf_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `absorption_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3
            - `reflectivity_fit_coeffs`:
              - `type`: array
              - `items`:
                - `type`: number
              - `minItems`: 3
              - `maxItems`: 3

Notes: All quantities are derived from DFT calculations and fitted to exponential forms. Values must be reported in the specified units. The checker uses hidden paper-reported asymptotic values for comparison.

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
          "energies",
          "bandgap_2H",
          "optical"
        ],
        "properties": {
          "energies": {
            "type": "object",
            "properties": {
              "1T'": {
                "type": "object",
                "properties": {
                  "surface_energy_asymptote_J_per_m2": {
                    "type": "number"
                  },
                  "cleaving_energy_asymptote_J_per_m2": {
                    "type": "number"
                  },
                  "binding_energy_asymptote_eV": {
                    "type": "number"
                  },
                  "vdw_energy_asymptote_J_per_m2": {
                    "type": "number"
                  }
                }
              },
              "2H": {
                "type": "object",
                "properties": {
                  "surface_energy_asymptote_J_per_m2": {
                    "type": "number"
                  },
                  "cleaving_energy_asymptote_J_per_m2": {
                    "type": "number"
                  },
                  "binding_energy_asymptote_eV": {
                    "type": "number"
                  },
                  "vdw_energy_asymptote_J_per_m2": {
                    "type": "number"
                  }
                }
              },
              "3R": {
                "type": "object",
                "properties": {
                  "surface_energy_asymptote_J_per_m2": {
                    "type": "number"
                  },
                  "cleaving_energy_asymptote_J_per_m2": {
                    "type": "number"
                  },
                  "binding_energy_asymptote_eV": {
                    "type": "number"
                  },
                  "vdw_energy_asymptote_J_per_m2": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "bandgap_2H": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "layer": {
                  "type": "integer"
                },
                "bandgap_eV": {
                  "type": "number"
                }
              }
            }
          },
          "optical": {
            "type": "object",
            "properties": {
              "1T'": {
                "type": "object",
                "properties": {
                  "eps1_0_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "n_0_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "eps1_inf_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "n_inf_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "absorption_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "reflectivity_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  }
                }
              },
              "2H": {
                "type": "object",
                "properties": {
                  "eps1_0_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "n_0_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "eps1_inf_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "n_inf_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "absorption_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "reflectivity_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  }
                }
              },
              "3R": {
                "type": "object",
                "properties": {
                  "eps1_0_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "n_0_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "eps1_inf_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "n_inf_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "absorption_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  },
                  "reflectivity_fit_coeffs": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "minItems": 3,
                    "maxItems": 3
                  }
                }
              }
            }
          }
        }
      },
      "description": "Aggregated layer-dependent properties and asymptotic values for all three polytypes, including energies, 2H band gap, and optical fitting coefficients. The checker compares each numerical value against paper-reported gold values with tolerances."
    }
  ],
  "notes": "All quantities are derived from DFT calculations and fitted to exponential forms. Values must be reported in the specified units. The checker uses hidden paper-reported asymptotic values for comparison."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares every numerical value (asymptotic energies, band gap entries, and optical fitting coefficients) against hidden reference values derived from the original study. The comparison uses tolerances appropriate for the toolchain and methodological spread, so a correct re-implementation scores highly even if numbers differ slightly from the original. In addition, the verifier checks structural constraints, such as that the 2H band gap decreases monotonically with increasing layer number. Each scored field contributes to a final reward in [0,1]; the exact weights and tolerances are not disclosed. Reporting the correct physical trends and well-converged values from a genuine DFT re-run yields a high score.
