# Resonant Raman B_k Displacement and State-Selective Enhancement Computation

## Problem background
The Raman spectra of polycyclic aromatic hydrocarbons (PAHs) of D2h symmetry show a characteristic D-band of totally symmetric vibrations near 1200–1400 cm⁻¹. The relative intensities of the sub-bands within this region can change markedly when the excitation laser wavelength is tuned. According to Albrecht's A-term theory of resonance Raman scattering, the activity of each vibration is controlled by dimensionless displacement parameters B_k, which measure the geometric distortion of the molecule upon electronic excitation. Two dipole-allowed excited states, labelled L_a and B_a, lie at accessible energies for large PAHs, and their different excited-state geometries are expected to selectively enhance different subsets of D-band modes. In addition, very low-frequency in-plane vibrations exist that correspond to whole-molecule acoustic-like motions; their frequencies should depend on the size of the PAH. The task is to compute the B_k displacement parameters for three D2h PAHs of increasing size and to analyse the resulting pattern of D-band enhancement and the low-frequency mode frequencies.

## Approach
The computation follows the Albrecht A-term formalism using quantum chemical calculations. For each molecule (C60H22, C78H26, C114H34), the ground-state equilibrium geometry, harmonic vibrational frequencies, and mass-weighted normal modes are first obtained. Excited-state equilibrium geometries are then optimised for the L_a and B_a electronic states. Dimensionless displacement parameters B_k are computed for every totally symmetric mode k using the projection formula B_k = (ω_k/ħ)^{1/2} [(x_g – x_e) M^{1/2} L_k], where ω_k is the mode frequency, x_g and x_e are the ground- and excited-state Cartesian coordinate vectors, M is the diagonal mass matrix, and L_k is the mass-weighted normal coordinate vector. The D-band region (1200–1400 cm⁻¹) is split into low- and high-frequency subgroups by the median frequency within each molecule. The mean B_k values for the L_a and B_a states are computed for each subgroup to reveal the state‑selective enhancement pattern. In parallel, the lowest-frequency in-plane longitudinal and transversal normal modes (the acoustic-like whole-molecule expansion/contraction motions) are identified for each molecule.

## Reproduction target
Produce B_k tables (c60_bk_tables.json, c78_bk_tables.json, c114_bk_tables.json) listing for every totally symmetric mode its frequency and the B_k values for the L_a and B_a excited states. From these tables, extract the D-band modes (1200–1400 cm⁻¹), split them into low- and high‑frequency subgroups using the median frequency, and report the mean B_La and B_Ba for each subgroup in trend_summary.json. Additionally, identify the lowest-frequency in-plane longitudinal and transversal modes for each molecule and write their frequencies to low_freq_modes.json. The final data set should make the state‑selective D‑band enhancement pattern and the size‑dependent trend of the acoustic-mode frequencies directly readable.

## Assets

- C60H22 (D2h) molecular structure: 15562123
- C78H26 (D2h) molecular structure: 15562286
- C114H34 (D2h) molecular structure: 15562373
- Open-source quantum chemistry package (e.g., Psi4, ORCA, PySCF): psi4/orca/pyscf

## Workflow steps

### Step 1: Ground-state geometry optimization and vibrational analysis
- Role: process
- Action: For C60, C78, C114, generate initial 3D molecular geometries, perform ground-state geometry optimization, and compute harmonic vibrational frequencies and mass-weighted normal modes. Save relevant log/checkpoint files as evidence.
- Evidence: `/app/outputs/ground_state_calc.log`

### Step 2: Excited-state geometry optimization for L_a and B_a
- Role: process
- Action: For each molecule, optimize the geometry of the L_a (1 B_3u) and B_a (2 B_3u) excited states using a suitable excited-state method (e.g., TD-DFT, CIS). Save equilibrium Cartesian coordinates. Save relevant log/checkpoint files as evidence.
- Evidence: `/app/outputs/excited_state_calc.log`

### Step 3: Compute B_k parameters for C60
- Role: scored (load-bearing)
- Action: Using the ground-state normal modes/frequencies and excited-state geometries for L_a and B_a, compute the dimensionless displacement parameters B_k for all totally symmetric modes of C60 following the projection formula B_k = (ω_k/ħ)^{1/2} [ (x_g - x_e) M^{1/2} L_k ], and write the results.
- Output file: `/app/outputs/c60_bk_tables.json`
- Format: json
- Contract: JSON list of objects; each object has keys: mode_id (integer), frequency_cm1 (float), B_La (float), B_Ba (float).
- Scoring: scored by hidden verifier

### Step 4: Compute B_k parameters for C78
- Role: scored (load-bearing)
- Action: Same as for C60, for C78.
- Output file: `/app/outputs/c78_bk_tables.json`
- Format: json
- Contract: Same schema as c60_bk_tables.json.
- Scoring: scored by hidden verifier

### Step 5: Compute B_k parameters for C114
- Role: scored (load-bearing)
- Action: Same as for C60, for C114.
- Output file: `/app/outputs/c114_bk_tables.json`
- Format: json
- Contract: Same schema as c60_bk_tables.json.
- Scoring: scored by hidden verifier

### Step 6: Summarize state-selective enhancement trend
- Role: scored
- Action: For each molecule, extract D-region modes (1200–1400 cm⁻¹), split by median frequency into low and high subgroups, compute mean B_La and mean B_Ba for each subgroup, and report them along with the lists of frequencies.
- Output file: `/app/outputs/trend_summary.json`
- Format: json
- Contract: JSON object with keys 'c60', 'c78', 'c114'. Each value is an object with keys: low_subgroup (list of floats, frequencies in cm⁻¹), high_subgroup (list of floats), mean_B_La_low (float), mean_B_Ba_low (float), mean_B_La_high (float), mean_B_Ba_high (float).
- Scoring: scored by hidden verifier

### Step 7: Identify low-frequency acoustic-like modes
- Role: scored (load-bearing)
- Action: For each molecule, locate the lowest-frequency in-plane longitudinal and transversal normal modes (whole-molecule expansion/contraction) and report their frequencies.
- Output file: `/app/outputs/low_freq_modes.json`
- Format: json
- Contract: JSON object with keys 'c60', 'c78', 'c114'. Each value is an object with keys: longitudinal_freq_cm1 (float), transversal_freq_cm1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/c60_bk_tables.json`
- `/app/outputs/c78_bk_tables.json`
- `/app/outputs/c114_bk_tables.json`
- `/app/outputs/trend_summary.json`
- `/app/outputs/low_freq_modes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### c60_bk_tables.json
- path: `/app/outputs/c60_bk_tables.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: B_k displacement parameters for C60; raw data used by the checker to recompute the state-selective enhancement trend.
- schema:
  - `type`: array
  - `required`:
  - `items`:
    - `type`: object
    - `required`: `mode_id`, `frequency_cm1`, `B_La`, `B_Ba`
    - `properties`:
      - `mode_id`:
        - `type`: integer
      - `frequency_cm1`:
        - `type`: number
      - `B_La`:
        - `type`: number
      - `B_Ba`:
        - `type`: number

### c78_bk_tables.json
- path: `/app/outputs/c78_bk_tables.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: B_k displacement parameters for C78.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `mode_id`, `frequency_cm1`, `B_La`, `B_Ba`
    - `properties`:
      - `mode_id`:
        - `type`: integer
      - `frequency_cm1`:
        - `type`: number
      - `B_La`:
        - `type`: number
      - `B_Ba`:
        - `type`: number

### c114_bk_tables.json
- path: `/app/outputs/c114_bk_tables.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: B_k displacement parameters for C114.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `mode_id`, `frequency_cm1`, `B_La`, `B_Ba`
    - `properties`:
      - `mode_id`:
        - `type`: integer
      - `frequency_cm1`:
        - `type`: number
      - `B_La`:
        - `type`: number
      - `B_Ba`:
        - `type`: number

### trend_summary.json
- path: `/app/outputs/trend_summary.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent-computed trend summary; checker recomputes from B_k tables and validates consistency.
- schema:
  - `type`: object
  - `required`: `c60`, `c78`, `c114`
  - `properties`:
    - `c60`:
      - `type`: object
      - `required`: `low_subgroup`, `high_subgroup`, `mean_B_La_low`, `mean_B_Ba_low`, `mean_B_La_high`, `mean_B_Ba_high`
      - `properties`:
        - `low_subgroup`:
          - `type`: array
          - `items`:
            - `type`: number
        - `high_subgroup`:
          - `type`: array
          - `items`:
            - `type`: number
        - `mean_B_La_low`:
          - `type`: number
        - `mean_B_Ba_low`:
          - `type`: number
        - `mean_B_La_high`:
          - `type`: number
        - `mean_B_Ba_high`:
          - `type`: number
    - `c78`:
      - `type`: object
      - `required`: `low_subgroup`, `high_subgroup`, `mean_B_La_low`, `mean_B_Ba_low`, `mean_B_La_high`, `mean_B_Ba_high`
      - `properties`:
        - `low_subgroup`:
          - `type`: array
          - `items`:
            - `type`: number
        - `high_subgroup`:
          - `type`: array
          - `items`:
            - `type`: number
        - `mean_B_La_low`:
          - `type`: number
        - `mean_B_Ba_low`:
          - `type`: number
        - `mean_B_La_high`:
          - `type`: number
        - `mean_B_Ba_high`:
          - `type`: number
    - `c114`:
      - `type`: object
      - `required`: `low_subgroup`, `high_subgroup`, `mean_B_La_low`, `mean_B_Ba_low`, `mean_B_La_high`, `mean_B_Ba_high`
      - `properties`:
        - `low_subgroup`:
          - `type`: array
          - `items`:
            - `type`: number
        - `high_subgroup`:
          - `type`: array
          - `items`:
            - `type`: number
        - `mean_B_La_low`:
          - `type`: number
        - `mean_B_Ba_low`:
          - `type`: number
        - `mean_B_La_high`:
          - `type`: number
        - `mean_B_Ba_high`:
          - `type`: number

### low_freq_modes.json
- path: `/app/outputs/low_freq_modes.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Frequencies of the lowest in-plane longitudinal and transversal modes for each PAH; checker verifies size-dependent ordering.
- schema:
  - `type`: object
  - `required`: `c60`, `c78`, `c114`
  - `properties`:
    - `c60`:
      - `type`: object
      - `required`: `longitudinal_freq_cm1`, `transversal_freq_cm1`
      - `properties`:
        - `longitudinal_freq_cm1`:
          - `type`: number
        - `transversal_freq_cm1`:
          - `type`: number
    - `c78`:
      - `type`: object
      - `required`: `longitudinal_freq_cm1`, `transversal_freq_cm1`
      - `properties`:
        - `longitudinal_freq_cm1`:
          - `type`: number
        - `transversal_freq_cm1`:
          - `type`: number
    - `c114`:
      - `type`: object
      - `required`: `longitudinal_freq_cm1`, `transversal_freq_cm1`
      - `properties`:
        - `longitudinal_freq_cm1`:
          - `type`: number
        - `transversal_freq_cm1`:
          - `type`: number

Notes: All scored artifacts are in JSON format. The checker will use the B_k tables to recompute the state-selective trend and cross-check the trend_summary. Low-frequency modes are checked for decreasing frequency order with increasing molecular size (C60 > C78 > C114).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "c60_bk_tables.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "required": [],
        "items": {
          "type": "object",
          "required": [
            "mode_id",
            "frequency_cm1",
            "B_La",
            "B_Ba"
          ],
          "properties": {
            "mode_id": {
              "type": "integer"
            },
            "frequency_cm1": {
              "type": "number"
            },
            "B_La": {
              "type": "number"
            },
            "B_Ba": {
              "type": "number"
            }
          }
        }
      },
      "description": "B_k displacement parameters for C60; raw data used by the checker to recompute the state-selective enhancement trend."
    },
    {
      "file": "c78_bk_tables.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "mode_id",
            "frequency_cm1",
            "B_La",
            "B_Ba"
          ],
          "properties": {
            "mode_id": {
              "type": "integer"
            },
            "frequency_cm1": {
              "type": "number"
            },
            "B_La": {
              "type": "number"
            },
            "B_Ba": {
              "type": "number"
            }
          }
        }
      },
      "description": "B_k displacement parameters for C78."
    },
    {
      "file": "c114_bk_tables.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "mode_id",
            "frequency_cm1",
            "B_La",
            "B_Ba"
          ],
          "properties": {
            "mode_id": {
              "type": "integer"
            },
            "frequency_cm1": {
              "type": "number"
            },
            "B_La": {
              "type": "number"
            },
            "B_Ba": {
              "type": "number"
            }
          }
        }
      },
      "description": "B_k displacement parameters for C114."
    },
    {
      "file": "trend_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "c60",
          "c78",
          "c114"
        ],
        "properties": {
          "c60": {
            "type": "object",
            "required": [
              "low_subgroup",
              "high_subgroup",
              "mean_B_La_low",
              "mean_B_Ba_low",
              "mean_B_La_high",
              "mean_B_Ba_high"
            ],
            "properties": {
              "low_subgroup": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "high_subgroup": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "mean_B_La_low": {
                "type": "number"
              },
              "mean_B_Ba_low": {
                "type": "number"
              },
              "mean_B_La_high": {
                "type": "number"
              },
              "mean_B_Ba_high": {
                "type": "number"
              }
            }
          },
          "c78": {
            "type": "object",
            "required": [
              "low_subgroup",
              "high_subgroup",
              "mean_B_La_low",
              "mean_B_Ba_low",
              "mean_B_La_high",
              "mean_B_Ba_high"
            ],
            "properties": {
              "low_subgroup": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "high_subgroup": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "mean_B_La_low": {
                "type": "number"
              },
              "mean_B_Ba_low": {
                "type": "number"
              },
              "mean_B_La_high": {
                "type": "number"
              },
              "mean_B_Ba_high": {
                "type": "number"
              }
            }
          },
          "c114": {
            "type": "object",
            "required": [
              "low_subgroup",
              "high_subgroup",
              "mean_B_La_low",
              "mean_B_Ba_low",
              "mean_B_La_high",
              "mean_B_Ba_high"
            ],
            "properties": {
              "low_subgroup": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "high_subgroup": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "mean_B_La_low": {
                "type": "number"
              },
              "mean_B_Ba_low": {
                "type": "number"
              },
              "mean_B_La_high": {
                "type": "number"
              },
              "mean_B_Ba_high": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Agent-computed trend summary; checker recomputes from B_k tables and validates consistency."
    },
    {
      "file": "low_freq_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "c60",
          "c78",
          "c114"
        ],
        "properties": {
          "c60": {
            "type": "object",
            "required": [
              "longitudinal_freq_cm1",
              "transversal_freq_cm1"
            ],
            "properties": {
              "longitudinal_freq_cm1": {
                "type": "number"
              },
              "transversal_freq_cm1": {
                "type": "number"
              }
            }
          },
          "c78": {
            "type": "object",
            "required": [
              "longitudinal_freq_cm1",
              "transversal_freq_cm1"
            ],
            "properties": {
              "longitudinal_freq_cm1": {
                "type": "number"
              },
              "transversal_freq_cm1": {
                "type": "number"
              }
            }
          },
          "c114": {
            "type": "object",
            "required": [
              "longitudinal_freq_cm1",
              "transversal_freq_cm1"
            ],
            "properties": {
              "longitudinal_freq_cm1": {
                "type": "number"
              },
              "transversal_freq_cm1": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Frequencies of the lowest in-plane longitudinal and transversal modes for each PAH; checker verifies size-dependent ordering."
    }
  ],
  "notes": "All scored artifacts are in JSON format. The checker will use the B_k tables to recompute the state-selective trend and cross-check the trend_summary. Low-frequency modes are checked for decreasing frequency order with increasing molecular size (C60 > C78 > C114)."
}
```

## How you are scored
A hidden verifier independently inspects your submitted output files. For the state‑selective enhancement trend, the verifier reads your B_k tables, recomputes the means for the low‑ and high‑frequency D‑band subgroups, and checks that the resulting pattern is internally consistent with your trend_summary.json. For the low‑frequency modes, the verifier reads low_freq_modes.json and verifies that the longitudinal and transversal frequencies follow the expected ordering with molecular size. Because calculations with different quantum‑chemical methods, basis sets, or functionals may yield different absolute values of B_k and frequencies, the verification focuses on the qualitative trend rather than on exact numerical agreement. The final reward is a weighted combination of the outcomes of all scored steps; submitting only a pre-written answer without the required computational artifacts will not pass the verification.
