# DFT investigation of charge-density-wave instability and superconductivity in 1T-TaSe2

## Problem background
Charge-density-wave (CDW) instabilities in layered transition-metal dichalcogenides, such as 1T-TaSe₂, are central to understanding the interplay between electrons and the lattice. First-principles calculations based on density-functional theory (DFT) can capture the sequence of structural transformations seen in these materials, predict how the CDW distortion evolves under pressure, and assess the possibility of electron-phonon-mediated superconductivity when the distortion is suppressed. This task reproduces the computational investigation of these phenomena using DFT and density-functional perturbation theory (DFPT).

## Approach
The overall workflow is built around plane-wave DFT with the local-density approximation (LDA) and ultrasoft pseudopotentials, as implemented in Quantum ESPRESSO. Starting from the high-temperature 1T crystal structure, a full relaxation is performed to obtain the equilibrium lattice and atomic positions. Phonon dispersions are then computed using DFPT on the relaxed cell; any unstable (imaginary-frequency) modes are identified and characterized. To investigate the commensurate CDW (CCDW) phase, in-plane √13×√13 supercells are constructed for two stacking variants—triclinic and hexagonal—and relaxed. The resulting geometries and total energies are compared against the undistorted 1T reference to extract structural parameters and stabilization energies. The effect of pressure is simulated by repeating the phonon and total-energy calculations at several compressed volumes for the CCDW supercell; this yields the critical pressure at which the CDW distortion disappears and the 1T structure becomes dynamically stable. Finally, for the undistorted 1T phase at two representative high pressures, the electron-phonon coupling constant λ, characteristic phonon frequencies (logarithmic average ω_log and arithmetic average ω_ave), electronic density of states at the Fermi level N(0), and the superconducting transition temperature Tc (using the Allen-Dynes formula with a Coulomb pseudopotential μ*=0.14) are computed.

## Reproduction target
This task aims to compute, from first principles, the following quantities:
- At ambient pressure: the wave vector q (in reciprocal lattice units) and the value of the strongest imaginary phonon frequency of the relaxed 1T structure, measured in cm⁻¹ (negative).
- For the commensurate CDW phase: the in-plane lattice parameter a, the out-of-plane lattice parameter c, the fractional changes δd₁ and δd₂ of specific Ta-Ta distances relative to the undistorted 1T structure (in percent), and the stabilization energy ΔE relative to the 1T phase (in mRy per formula unit) — all reported separately for triclinic and hexagonal stacking.
- The hydrostatic pressure (in GPa) at which the CDW distortion vanishes and the 1T structure becomes dynamically stable.
- For the undistorted 1T structure at 45 GPa and 60 GPa: the electronic density of states at the Fermi level N(0) (states/Ry/spin), the logarithmic average phonon frequency ω_log (meV), the arithmetic average phonon frequency ω_ave (meV), the electron-phonon coupling constant λ, and the superconducting Tc (K) from the Allen-Dynes formula with μ*=0.14.

## Assets

- Quantum ESPRESSO (PWSCF) package: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Ta and Se (LDA, Perdew-Zunger, with nonlinear core correction for Se): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Relaxation of undistorted 1T structure
- Role: process
- Action: Perform DFT structural relaxation of the 1T-TaSe2 unit cell (Se-Ta-Se trilayer, trigonal) using the LDA functional and ultrasoft pseudopotentials (with nonlinear core correction for Se). Optimize lattice parameters and internal atomic positions to obtain the equilibrium ground-state structure.
- Evidence: `/app/outputs/relax_1t_output.log`

### Step 2: Phonon instability of 1T at ambient pressure
- Role: scored (load-bearing)
- Action: Using the relaxed 1T structure, compute the phonon dispersion with density-functional perturbation theory. Identify the unstable acoustic branch along Γ–M involving in-plane Ta displacements. Locate the q-point (among the sampled grid) that has the largest imaginary frequency and is closest in in-plane projection to the incommensurate CDW ordering vector (≈0.278 b1 + b3/3). Determine the critical electronic smearing width at which the instability first appears. Write the result to phonon_instability.json.
- Output file: `/app/outputs/phonon_instability.json`
- Format: json
- Contract: {
  "pressure_0GPa": {
    "q_minimum": [float, float, float] (reciprocal lattice units),
    "q_label": "string (e.g., nearest to ICDW ordering vector)",
    "imaginary_frequency": float (in cm⁻¹, negative value indicating instability),
    "critical_smearing_width": float (Ry, σ value at which instability first appears)
  }
}
- Scoring: scored by hidden verifier

### Step 3: CCDW supercell relaxation
- Role: process
- Action: Construct √13×√13 in-plane supercells of the commensurate CDW phase. Build two stacking variants: triclinic (offset between clusters in adjacent trilayers) and hexagonal (cluster centres aligned vertically). For each stacking, perform DFT relaxation using the same computational setup, starting from small atomic displacements toward star-of-David clusters. Optimize atomic positions and out-of-plane lattice constants (keep in-plane supercell fixed). Save the relaxed coordinates and total energies.
- Evidence: `/app/outputs/ccdw_relax.log`

### Step 4: CCDW structural parameters
- Role: scored
- Action: From the relaxed triclinic and hexagonal CCDW structures, extract: lattice parameters a and c (in Å), fractional change δd1 and δd2 of Ta–Ta distances relative to the undistorted 1T structure (in percent), and stabilization energy ΔE (in mRy per formula unit) for each stacking variant. Write the values to ccdw_structural_params.json.
- Output file: `/app/outputs/ccdw_structural_params.json`
- Format: json
- Contract: {
  "triclinic": {
    "a": float (Å), "c": float (Å), "delta_d1": float (%), "delta_d2": float (%), "delta_E_mRy_per_fu": float
  },
  "hexagonal": {
    "a": float (Å), "c": float (Å), "delta_d1": float (%), "delta_d2": float (%), "delta_E_mRy_per_fu": float
  }
}
- Scoring: scored by hidden verifier

### Step 5: High-pressure properties and superconductivity
- Role: scored (load-bearing)
- Action: Perform DFT total-energy and relaxation calculations for the CCDW supercell at several hydrostatic pressures to track the CDW amplitude. Determine the pressure at which the distortion vanishes (the undistorted 1T structure becomes dynamically stable). Additionally, for the undistorted 1T structure at 45 GPa and 60 GPa, compute: electronic density of states at the Fermi level N(0) (states/Ry/spin), electron-phonon coupling constant λ, logarithmic average phonon frequency ω_log (meV), average phonon frequency ω_ave (meV), and superconducting Tc (K) using the Allen-Dynes formula with μ*=0.14. Write all quantities to high_pressure_properties.json.
- Output file: `/app/outputs/high_pressure_properties.json`
- Format: json
- Contract: {
  "cdw_disappearance_pressure_GPa": float,
  "pressures": [
    {
      "P_GPa": float,
      "N0_states_per_Ry_spin": float,
      "hbar_omega_log_meV": float,
      "hbar_omega_ave_meV": float,
      "lambda": float,
      "Tc_K": float
    }
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_instability.json`
- `/app/outputs/ccdw_structural_params.json`
- `/app/outputs/high_pressure_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_instability.json
- path: `/app/outputs/phonon_instability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phonon instability at ambient pressure: q-point of largest imaginary frequency near ICDW vector, frequency, and critical smearing.
- schema:
  - `type`: object
  - `required`: `pressure_0GPa`
  - `items`:
    - `pressure_0GPa`:
      - `type`: object
      - `required`: `q_minimum`, `q_label`, `imaginary_frequency`, `critical_smearing_width`
      - `properties`:
        - `q_minimum`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 3
          - `maxItems`: 3
          - `description`: reciprocal lattice units
        - `q_label`:
          - `type`: string
        - `imaginary_frequency`:
          - `type`: number
          - `description`: cm⁻¹, negative value
        - `critical_smearing_width`:
          - `type`: number
          - `description`: Ry

### ccdw_structural_params.json
- path: `/app/outputs/ccdw_structural_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Structural parameters of the commensurate CDW phase for triclinic and hexagonal stacking.
- schema:
  - `type`: object
  - `required`: `triclinic`, `hexagonal`
  - `items`:
    - `triclinic`:
      - `type`: object
      - `required`: `a`, `c`, `delta_d1`, `delta_d2`, `delta_E_mRy_per_fu`
      - `properties`:
        - `a`:
          - `type`: number
          - `description`: Å
        - `c`:
          - `type`: number
          - `description`: Å
        - `delta_d1`:
          - `type`: number
          - `description`: %
        - `delta_d2`:
          - `type`: number
          - `description`: %
        - `delta_E_mRy_per_fu`:
          - `type`: number
          - `description`: mRy per formula unit
    - `hexagonal`:
      - `type`: object
      - `required`: `a`, `c`, `delta_d1`, `delta_d2`, `delta_E_mRy_per_fu`
      - `properties`:
        - `a`:
          - `type`: number
          - `description`: Å
        - `c`:
          - `type`: number
          - `description`: Å
        - `delta_d1`:
          - `type`: number
          - `description`: %
        - `delta_d2`:
          - `type`: number
          - `description`: %
        - `delta_E_mRy_per_fu`:
          - `type`: number
          - `description`: mRy per formula unit

### high_pressure_properties.json
- path: `/app/outputs/high_pressure_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: High-pressure CDW suppression pressure and superconducting properties at 45 and 60 GPa.
- schema:
  - `type`: object
  - `required`: `cdw_disappearance_pressure_GPa`, `pressures`
  - `items`:
    - `cdw_disappearance_pressure_GPa`:
      - `type`: number
      - `description`: GPa
    - `pressures`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `P_GPa`, `N0_states_per_Ry_spin`, `hbar_omega_log_meV`, `hbar_omega_ave_meV`, `lambda`, `Tc_K`
        - `properties`:
          - `P_GPa`:
            - `type`: number
            - `description`: GPa
          - `N0_states_per_Ry_spin`:
            - `type`: number
            - `description`: states/Ry/spin
          - `hbar_omega_log_meV`:
            - `type`: number
            - `description`: meV
          - `hbar_omega_ave_meV`:
            - `type`: number
            - `description`: meV
          - `lambda`:
            - `type`: number
          - `Tc_K`:
            - `type`: number
            - `description`: K
      - `minItems`: 2

Notes: All scored outputs are compared to paper-reported values with appropriate tolerances (structural parameters within 5%, ΔE within 0.5 mRy, phonon instability q-vector within 0.01 reciprocal lattice units and frequency magnitude within 20%, λ within 10%, Tc within 20%, CDW disappearance pressure within ±5 GPa). The checker reads the JSON files and verifies shape and values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_instability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "pressure_0GPa"
        ],
        "items": {
          "pressure_0GPa": {
            "type": "object",
            "required": [
              "q_minimum",
              "q_label",
              "imaginary_frequency",
              "critical_smearing_width"
            ],
            "properties": {
              "q_minimum": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 3,
                "maxItems": 3,
                "description": "reciprocal lattice units"
              },
              "q_label": {
                "type": "string"
              },
              "imaginary_frequency": {
                "type": "number",
                "description": "cm⁻¹, negative value"
              },
              "critical_smearing_width": {
                "type": "number",
                "description": "Ry"
              }
            }
          }
        }
      },
      "description": "Phonon instability at ambient pressure: q-point of largest imaginary frequency near ICDW vector, frequency, and critical smearing."
    },
    {
      "file": "ccdw_structural_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "triclinic",
          "hexagonal"
        ],
        "items": {
          "triclinic": {
            "type": "object",
            "required": [
              "a",
              "c",
              "delta_d1",
              "delta_d2",
              "delta_E_mRy_per_fu"
            ],
            "properties": {
              "a": {
                "type": "number",
                "description": "Å"
              },
              "c": {
                "type": "number",
                "description": "Å"
              },
              "delta_d1": {
                "type": "number",
                "description": "%"
              },
              "delta_d2": {
                "type": "number",
                "description": "%"
              },
              "delta_E_mRy_per_fu": {
                "type": "number",
                "description": "mRy per formula unit"
              }
            }
          },
          "hexagonal": {
            "type": "object",
            "required": [
              "a",
              "c",
              "delta_d1",
              "delta_d2",
              "delta_E_mRy_per_fu"
            ],
            "properties": {
              "a": {
                "type": "number",
                "description": "Å"
              },
              "c": {
                "type": "number",
                "description": "Å"
              },
              "delta_d1": {
                "type": "number",
                "description": "%"
              },
              "delta_d2": {
                "type": "number",
                "description": "%"
              },
              "delta_E_mRy_per_fu": {
                "type": "number",
                "description": "mRy per formula unit"
              }
            }
          }
        }
      },
      "description": "Structural parameters of the commensurate CDW phase for triclinic and hexagonal stacking."
    },
    {
      "file": "high_pressure_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "cdw_disappearance_pressure_GPa",
          "pressures"
        ],
        "items": {
          "cdw_disappearance_pressure_GPa": {
            "type": "number",
            "description": "GPa"
          },
          "pressures": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "P_GPa",
                "N0_states_per_Ry_spin",
                "hbar_omega_log_meV",
                "hbar_omega_ave_meV",
                "lambda",
                "Tc_K"
              ],
              "properties": {
                "P_GPa": {
                  "type": "number",
                  "description": "GPa"
                },
                "N0_states_per_Ry_spin": {
                  "type": "number",
                  "description": "states/Ry/spin"
                },
                "hbar_omega_log_meV": {
                  "type": "number",
                  "description": "meV"
                },
                "hbar_omega_ave_meV": {
                  "type": "number",
                  "description": "meV"
                },
                "lambda": {
                  "type": "number"
                },
                "Tc_K": {
                  "type": "number",
                  "description": "K"
                }
              }
            },
            "minItems": 2
          }
        }
      },
      "description": "High-pressure CDW suppression pressure and superconducting properties at 45 and 60 GPa."
    }
  ],
  "notes": "All scored outputs are compared to paper-reported values with appropriate tolerances (structural parameters within 5%, ΔE within 0.5 mRy, phonon instability q-vector within 0.01 reciprocal lattice units and frequency magnitude within 20%, λ within 10%, Tc within 20%, CDW disappearance pressure within ±5 GPa). The checker reads the JSON files and verifies shape and values."
}
```

## How you are scored
A hidden verifier independently compares each of your submitted output JSON files (phonon_instability.json, ccdw_structural_params.json, high_pressure_properties.json) against reference values. Each scored step contributes a weighted share to the final reward, with the load-bearing stages carrying the largest weights. The verifier checks whether your computed values fall within appropriate, undisclosed tolerances; meeting or exceeding the reference threshold earns full credit for that quantity, and the reward degrades monotonically as the deviation grows. The exact weighting and tolerance bands are hidden, so you should aim for an accurate reproduction using the prescribed computational protocol.
