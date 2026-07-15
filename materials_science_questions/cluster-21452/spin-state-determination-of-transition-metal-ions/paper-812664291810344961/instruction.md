# Reproducing MgF2 Bulk and Co2+ Spin State via Hybrid DFT

## Problem background
Magnesium fluoride (MgF2) is a wide‑band‑gap rutile-structured crystal used in optics and laser systems. Doping with Co2+ ions introduces impurity levels that can modify its optical and magnetic properties. A reliable first‑principles description requires: (i) accurately predicting the band gap, lattice parameters, elastic constants, and phonon frequencies of pure MgF2, and (ii) determining whether the Co2+ dopant assumes a high‑spin or low‑spin state and locating its impurity levels relative to the host band edges. This task addresses both challenges.

## Approach
We carry out periodic hybrid density‑functional theory (DFT) calculations using a PBE‑based hybrid functional with the fraction of exact (Hartree‑Fock) exchange set to ~0.45 (PBEh45), which has been found to give a good balance between band‑gap accuracy and structural/mechanical properties. For the pristine MgF2 primitive cell we relax the geometry, compute the band gap, elastic coefficients, and Γ‑point phonon frequencies. For the Co‑doped system we construct a 2×2×2 supercell (96 atoms) with one Mg replaced by Co, and perform spin‑polarized calculations for both high‑spin (total spin projection Sz=3/2) and low‑spin (Sz=1/2) initial configurations. Comparing total energies reveals the thermodynamically stable spin state; projected density‑of‑states analysis locates the Co 3d minority‑spin levels within the gap.

## Reproduction target
Using an open‑source periodic DFT code that supports hybrid functionals with tunable exact‑exchange fraction, perform the following and write the results to the specified JSON files:

1. For pure MgF2 (rutile, space group P42/mnm, 6‑atom primitive cell), after geometry relaxation, output: band gap (eV), lattice parameters a, c and internal u, bulk modulus B and elastic coefficients c11, c12, c13, c33, c44, c66 (GPa), IR‑active transverse‑optical and longitudinal‑optical phonon frequencies (cm⁻¹, in the order b1u, eu, a2u, eu, b1u, eu for TO and eu, eu, eu, a2u for LO), and Raman‑active phonon frequencies (cm⁻¹, in the order b1g, eg, a1g, b2g).

2. For the Co‑doped 2×2×2 supercell, after spin‑polarized relaxation of both high‑spin and low‑spin configurations, output: total energies (Ha) for each spin state, the energy difference ΔE = E(LS) – E(HS) (eV, positive means HS is more stable), the magnetic moment of Co in the high‑spin state (μB), and the energies (eV) of the Co 3d minority‑spin peaks above the valence band maximum.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotentials library: https://www.materialscloud.org/discover/sssp/
- MgF2 rutile crystal structure: 10.17188/1195289
- Python packages for data processing: pip install numpy scipy matplotlib

## Workflow steps

### Step 1: Pure MgF2 DFT calculations
- Role: process
- Action: Set up and run DFT calculations for a primitive cell of MgF2 (rutile, space group P4_2/mnm, 6 atoms) using a hybrid functional with exx_fraction=0.45 (or equivalent PBEh45). Perform geometry relaxation to obtain lattice parameters a, c, u; compute the band gap; compute elastic coefficients; and compute phonon frequencies at the Gamma-point (IR-active and Raman-active modes). Use standard pseudopotentials from a public library.
- Evidence: `/app/outputs/pure_MgF2_raw_outputs.tar.gz`

### Step 2: Extract pure MgF2 properties
- Role: scored
- Action: From the raw DFT outputs of step s01, extract the following quantities and write them into a JSON file: band gap (eV), lattice parameters a, c (Angstrom), internal parameter u, bulk modulus B (GPa), elastic coefficients c11, c12, c13, c33, c44, c66 (GPa), IR-active transverse and longitudinal phonon frequencies (list of frequencies for the modes in the order of Table 4: b1u (TO), eu (TO), a2u (TO), eu (TO), b1u (TO), eu (TO) for TO; eu (LO), eu (LO), eu (LO), a2u (LO) for LO), and Raman-active phonon frequencies (list for b1g, eg, a1g, b2g as in Table 5). Write this object to step_02_pure_MgF2_properties.json.
- Output file: `/app/outputs/step_02_pure_MgF2_properties.json`
- Format: json
- Contract: {"band_gap_eV": float, "lattice_parameters": {"a_Ang": float, "c_Ang": float, "u": float}, "elastic_properties": {"B_GPa": float, "c11_GPa": float, "c12_GPa": float, "c13_GPa": float, "c33_GPa": float, "c44_GPa": float, "c66_GPa": float}, "IR_phonon_frequencies_cm-1": {"TO": [float, float, float, float, float, float], "LO": [float, float, float, float]}, "Raman_phonon_frequencies_cm-1": [float, float, float, float]}
- Scoring: scored by hidden verifier

### Step 3: Co-doped MgF2 supercell calculations
- Role: process
- Action: Build a 96-atom supercell (2x2x2 extension of the primitive cell) of MgF2 with one Mg replaced by Co. Perform spin-polarized DFT calculations with exx_fraction=0.45 for both high-spin (Sz=3/2) and low-spin (Sz=1/2) initial spin configurations. For each: relax geometry, compute total energy, magnetic moment on Co, and projected density of states (DOS).
- Evidence: `/app/outputs/co_doped_MgF2_raw_outputs.tar.gz`

### Step 4: Extract Co-doped MgF2 properties
- Role: scored (load-bearing)
- Action: From the raw DFT outputs of step s03, extract the total energies (Ha) for high-spin and low-spin configurations, the energy difference ΔE = E(LS) − E(HS) (eV, positive means HS more stable), the magnetic moment of Co in the HS state (μB), and the energy positions (eV) of the Co 3d minority-spin peaks above the valence band maximum (e.g., for the HS state the first peak around 2.2 eV). Write these values to step_04_Co_doped_properties.json.
- Output file: `/app/outputs/step_04_Co_doped_properties.json`
- Format: json
- Contract: {"high_spin_total_energy_Ha": float, "low_spin_total_energy_Ha": float, "delta_E_eV": float, "magnetic_moment_HS_mu_B": float, "Co_3d_minority_peak_positions_eV": [float, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_pure_MgF2_properties.json`
- `/app/outputs/step_04_Co_doped_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_pure_MgF2_properties.json
- path: `/app/outputs/step_02_pure_MgF2_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed properties of pure MgF2: band gap, lattice parameters, elastic constants, and Gamma-point phonon frequencies. The checker compares each value to the hidden paper reference with per-field tolerances.
- schema:
  - `type`: object
  - `required`: `band_gap_eV`, `lattice_parameters`, `elastic_properties`, `IR_phonon_frequencies_cm-1`, `Raman_phonon_frequencies_cm-1`
  - `properties`:
    - `band_gap_eV`:
      - `type`: number
      - `description`: Band gap in eV
    - `lattice_parameters`:
      - `type`: object
      - `required`: `a_Ang`, `c_Ang`, `u`
      - `properties`:
        - `a_Ang`:
          - `type`: number
          - `description`: Lattice parameter a in Angstrom
        - `c_Ang`:
          - `type`: number
          - `description`: Lattice parameter c in Angstrom
        - `u`:
          - `type`: number
          - `description`: Internal fluorine parameter
    - `elastic_properties`:
      - `type`: object
      - `required`: `B_GPa`, `c11_GPa`, `c12_GPa`, `c13_GPa`, `c33_GPa`, `c44_GPa`, `c66_GPa`
      - `properties`:
        - `B_GPa`:
          - `type`: number
        - `c11_GPa`:
          - `type`: number
        - `c12_GPa`:
          - `type`: number
        - `c13_GPa`:
          - `type`: number
        - `c33_GPa`:
          - `type`: number
        - `c44_GPa`:
          - `type`: number
        - `c66_GPa`:
          - `type`: number
    - `IR_phonon_frequencies_cm-1`:
      - `type`: object
      - `required`: `TO`, `LO`
      - `properties`:
        - `TO`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 6
          - `maxItems`: 6
          - `description`: Transverse optical phonon frequencies in order: b1u, eu, a2u, eu, b1u, eu
        - `LO`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 4
          - `maxItems`: 4
          - `description`: Longitudinal optical phonon frequencies in order: eu, eu, eu, a2u
    - `Raman_phonon_frequencies_cm-1`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 4
      - `maxItems`: 4
      - `description`: Raman-active phonon frequencies in order: b1g, eg, a1g, b2g

### step_04_Co_doped_properties.json
- path: `/app/outputs/step_04_Co_doped_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Spin-state and electronic structure results for Co-doped MgF2: total energies of HS and LS states, energy difference, magnetic moment, and Co 3d minority-spin peak positions. The checker verifies HS stability and compares values to hidden paper references with tolerances.
- schema:
  - `type`: object
  - `required`: `high_spin_total_energy_Ha`, `low_spin_total_energy_Ha`, `delta_E_eV`, `magnetic_moment_HS_mu_B`, `Co_3d_minority_peak_positions_eV`
  - `properties`:
    - `high_spin_total_energy_Ha`:
      - `type`: number
      - `description`: Total energy of high-spin configuration in Hartree
    - `low_spin_total_energy_Ha`:
      - `type`: number
      - `description`: Total energy of low-spin configuration in Hartree
    - `delta_E_eV`:
      - `type`: number
      - `description`: E(LS) - E(HS) in eV; positive means HS is more stable
    - `magnetic_moment_HS_mu_B`:
      - `type`: number
      - `description`: Magnetic moment of Co in the HS state in Bohr magnetons
    - `Co_3d_minority_peak_positions_eV`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Energies of Co 3d minority-spin peaks above the valence band maximum in eV

Notes: The scores for pure MgF2 properties are awarded per-field based on closeness to the paper-reported PBEh45 values, using tolerances that account for the expected spread from a different DFT code and pseudopotentials. For Co-doped results, the checker verifies that delta_E > 0 (indicating high-spin is more stable) and compares the absolute values to the paper's gold with allocated tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_pure_MgF2_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_eV",
          "lattice_parameters",
          "elastic_properties",
          "IR_phonon_frequencies_cm-1",
          "Raman_phonon_frequencies_cm-1"
        ],
        "properties": {
          "band_gap_eV": {
            "type": "number",
            "description": "Band gap in eV"
          },
          "lattice_parameters": {
            "type": "object",
            "required": [
              "a_Ang",
              "c_Ang",
              "u"
            ],
            "properties": {
              "a_Ang": {
                "type": "number",
                "description": "Lattice parameter a in Angstrom"
              },
              "c_Ang": {
                "type": "number",
                "description": "Lattice parameter c in Angstrom"
              },
              "u": {
                "type": "number",
                "description": "Internal fluorine parameter"
              }
            }
          },
          "elastic_properties": {
            "type": "object",
            "required": [
              "B_GPa",
              "c11_GPa",
              "c12_GPa",
              "c13_GPa",
              "c33_GPa",
              "c44_GPa",
              "c66_GPa"
            ],
            "properties": {
              "B_GPa": {
                "type": "number"
              },
              "c11_GPa": {
                "type": "number"
              },
              "c12_GPa": {
                "type": "number"
              },
              "c13_GPa": {
                "type": "number"
              },
              "c33_GPa": {
                "type": "number"
              },
              "c44_GPa": {
                "type": "number"
              },
              "c66_GPa": {
                "type": "number"
              }
            }
          },
          "IR_phonon_frequencies_cm-1": {
            "type": "object",
            "required": [
              "TO",
              "LO"
            ],
            "properties": {
              "TO": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 6,
                "maxItems": 6,
                "description": "Transverse optical phonon frequencies in order: b1u, eu, a2u, eu, b1u, eu"
              },
              "LO": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 4,
                "maxItems": 4,
                "description": "Longitudinal optical phonon frequencies in order: eu, eu, eu, a2u"
              }
            }
          },
          "Raman_phonon_frequencies_cm-1": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 4,
            "maxItems": 4,
            "description": "Raman-active phonon frequencies in order: b1g, eg, a1g, b2g"
          }
        }
      },
      "description": "Computed properties of pure MgF2: band gap, lattice parameters, elastic constants, and Gamma-point phonon frequencies. The checker compares each value to the hidden paper reference with per-field tolerances."
    },
    {
      "file": "step_04_Co_doped_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "high_spin_total_energy_Ha",
          "low_spin_total_energy_Ha",
          "delta_E_eV",
          "magnetic_moment_HS_mu_B",
          "Co_3d_minority_peak_positions_eV"
        ],
        "properties": {
          "high_spin_total_energy_Ha": {
            "type": "number",
            "description": "Total energy of high-spin configuration in Hartree"
          },
          "low_spin_total_energy_Ha": {
            "type": "number",
            "description": "Total energy of low-spin configuration in Hartree"
          },
          "delta_E_eV": {
            "type": "number",
            "description": "E(LS) - E(HS) in eV; positive means HS is more stable"
          },
          "magnetic_moment_HS_mu_B": {
            "type": "number",
            "description": "Magnetic moment of Co in the HS state in Bohr magnetons"
          },
          "Co_3d_minority_peak_positions_eV": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Energies of Co 3d minority-spin peaks above the valence band maximum in eV"
          }
        }
      },
      "description": "Spin-state and electronic structure results for Co-doped MgF2: total energies of HS and LS states, energy difference, magnetic moment, and Co 3d minority-spin peak positions. The checker verifies HS stability and compares values to hidden paper references with tolerances."
    }
  ],
  "notes": "The scores for pure MgF2 properties are awarded per-field based on closeness to the paper-reported PBEh45 values, using tolerances that account for the expected spread from a different DFT code and pseudopotentials. For Co-doped results, the checker verifies that delta_E > 0 (indicating high-spin is more stable) and compares the absolute values to the paper's gold with allocated tolerances."
}
```

## How you are scored
A hidden verifier will read the two JSON files you produce and compare each reported quantity to the correct reference values using per‑field tolerances. Each field that falls within its tolerance earns partial credit; the overall reward is the fraction of fields that pass. The pure‑MgF2 and Co‑doped properties are weighted approximately equally, with a slight emphasis on the Co‑doped results because they carry the main scientific claim. The verifier does not expect you to report any specific paper’s numbers — it compares your computed values to the correct underlying quantities. You must genuinely run the calculations; reporting numbers you did not compute will be penalised only in the sense that your submitted artifact will not match the reference.
