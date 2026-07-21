# DFT Binding Energies and Vibrational Frequencies of NO on Iridium Surfaces

## Problem background
Understanding how nitric oxide (NO) adsorbs and decomposes on metal surfaces is central to designing catalysts for pollution control. The reactivity and selectivity of a catalyst depend on the surface structure and the adsorption sites it offers. Density functional theory (DFT) can predict binding energies and vibrational frequencies of NO on specific surface sites, providing insight into the adsorption modes (atop, bridge) and supporting experimental spectroscopy. This task aims to compute these properties for NO on three iridium surfaces to quantify the structure–property relationships.

## Approach
Use an open-source plane-wave DFT code (e.g., Quantum ESPRESSO, GPAW) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and appropriate pseudopotentials. Build slab models for Ir(210), Ir(110), and Ir(311) from the fcc bulk structure, with sufficient vacuum and frozen bottom layers. Place NO in atop and bridge adsorption sites. Optimize each structure fully and then compute the harmonic N–O stretching frequency. Calculate the binding energy as the energy difference between the NO+slab system, the bare slab, and the gas‑phase NO reference. The workflow repeats this for all six site/surface combinations.

## Reproduction target
Produce a JSON file (`dft_results.json`) containing the binding energy (eV, positive for exothermic adsorption) and the harmonic N–O stretching frequency (cm⁻¹) for NO adsorbed on each of the following surfaces and sites: Ir(210) atop, Ir(210) bridge, Ir(110) atop, Ir(110) bridge, Ir(311) atop, and Ir(311) bridge. The values must come from your DFT calculations with the PBE functional; the exact setup (slab thickness, k‑point sampling, cutoff energy) is chosen by you, as long as it is physically reasonable and yields converged properties.

## Assets

- Quantum ESPRESSO or other open-source plane-wave DFT code: https://www.quantum-espresso.org/
- FCC Ir crystal structure: https://next-gen.materialsproject.org/materials/mp-126
- Pseudopotentials for Ir, N, and O: typically included with Quantum ESPRESSO (e.g., Ir.pbe-...UPF, N.pbe-...UPF, O.pbe-...UPF)

## Workflow steps

### Step 1: DFT Calculations of NO on Ir Surfaces
- Role: scored (load-bearing)
- Action: Perform DFT calculations using the PBE exchange-correlation functional and appropriate pseudopotentials to compute the binding energy (eV) and harmonic N–O stretching frequency (cm⁻¹) for NO adsorbed on Ir(210), Ir(110), and Ir(311) surfaces. Consider the atop and bridge adsorption sites for each surface as described in the methodological model (slab geometries, vacuum, fixed bottom layers). Compute binding energy as E(NO) + E(slab) – E(NO+slab). Report the results in dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {
  "Ir210_atop": {"binding_energy_eV": number, "frequency_cm-1": number},
  "Ir210_bridge": {"binding_energy_eV": number, "frequency_cm-1": number},
  "Ir110_atop": {"binding_energy_eV": number, "frequency_cm-1": number},
  "Ir110_bridge": {"binding_energy_eV": number, "frequency_cm-1": number},
  "Ir311_atop": {"binding_energy_eV": number, "frequency_cm-1": number},
  "Ir311_bridge": {"binding_energy_eV": number, "frequency_cm-1": number}
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed binding energies and N-O stretching frequencies for NO on the specified Ir surface sites.
- schema:
  - `type`: object
  - `required`: `Ir210_atop`, `Ir210_bridge`, `Ir110_atop`, `Ir110_bridge`, `Ir311_atop`, `Ir311_bridge`
  - `properties`:
    - `Ir210_atop`:
      - `type`: object
      - `required`: `binding_energy_eV`, `frequency_cm-1`
      - `properties`:
        - `binding_energy_eV`:
          - `type`: number
        - `frequency_cm-1`:
          - `type`: number
    - `Ir210_bridge`:
      - `type`: object
      - `required`: `binding_energy_eV`, `frequency_cm-1`
      - `properties`:
        - `binding_energy_eV`:
          - `type`: number
        - `frequency_cm-1`:
          - `type`: number
    - `Ir110_atop`:
      - `type`: object
      - `required`: `binding_energy_eV`, `frequency_cm-1`
      - `properties`:
        - `binding_energy_eV`:
          - `type`: number
        - `frequency_cm-1`:
          - `type`: number
    - `Ir110_bridge`:
      - `type`: object
      - `required`: `binding_energy_eV`, `frequency_cm-1`
      - `properties`:
        - `binding_energy_eV`:
          - `type`: number
        - `frequency_cm-1`:
          - `type`: number
    - `Ir311_atop`:
      - `type`: object
      - `required`: `binding_energy_eV`, `frequency_cm-1`
      - `properties`:
        - `binding_energy_eV`:
          - `type`: number
        - `frequency_cm-1`:
          - `type`: number
    - `Ir311_bridge`:
      - `type`: object
      - `required`: `binding_energy_eV`, `frequency_cm-1`
      - `properties`:
        - `binding_energy_eV`:
          - `type`: number
        - `frequency_cm-1`:
          - `type`: number

Notes: The checker compares each reported value against a hidden reference with generous tolerances and verifies structural ordering (e.g., atop vs bridge energy/frequency trends).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Ir210_atop",
          "Ir210_bridge",
          "Ir110_atop",
          "Ir110_bridge",
          "Ir311_atop",
          "Ir311_bridge"
        ],
        "properties": {
          "Ir210_atop": {
            "type": "object",
            "required": [
              "binding_energy_eV",
              "frequency_cm-1"
            ],
            "properties": {
              "binding_energy_eV": {
                "type": "number"
              },
              "frequency_cm-1": {
                "type": "number"
              }
            }
          },
          "Ir210_bridge": {
            "type": "object",
            "required": [
              "binding_energy_eV",
              "frequency_cm-1"
            ],
            "properties": {
              "binding_energy_eV": {
                "type": "number"
              },
              "frequency_cm-1": {
                "type": "number"
              }
            }
          },
          "Ir110_atop": {
            "type": "object",
            "required": [
              "binding_energy_eV",
              "frequency_cm-1"
            ],
            "properties": {
              "binding_energy_eV": {
                "type": "number"
              },
              "frequency_cm-1": {
                "type": "number"
              }
            }
          },
          "Ir110_bridge": {
            "type": "object",
            "required": [
              "binding_energy_eV",
              "frequency_cm-1"
            ],
            "properties": {
              "binding_energy_eV": {
                "type": "number"
              },
              "frequency_cm-1": {
                "type": "number"
              }
            }
          },
          "Ir311_atop": {
            "type": "object",
            "required": [
              "binding_energy_eV",
              "frequency_cm-1"
            ],
            "properties": {
              "binding_energy_eV": {
                "type": "number"
              },
              "frequency_cm-1": {
                "type": "number"
              }
            }
          },
          "Ir311_bridge": {
            "type": "object",
            "required": [
              "binding_energy_eV",
              "frequency_cm-1"
            ],
            "properties": {
              "binding_energy_eV": {
                "type": "number"
              },
              "frequency_cm-1": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "DFT-computed binding energies and N-O stretching frequencies for NO on the specified Ir surface sites."
    }
  ],
  "notes": "The checker compares each reported value against a hidden reference with generous tolerances and verifies structural ordering (e.g., atop vs bridge energy/frequency trends)."
}
```

## How you are scored
A hidden verifier independently checks your `dft_results.json`. It compares your binding energies and frequencies to reference values with generous tolerances that account for differences between DFT codes and pseudopotentials. It also verifies physically expected structural relationships – for example, the relative ordering of binding energies between atop and bridge sites on each surface, and the relative ordering of vibrational frequencies. Full credit is given when all comparisons are within tolerance and all structural checks pass; otherwise a partial score proportional to the number of satisfied checks is awarded. Reporting a value without running a genuine DFT calculation will not pass these checks.
