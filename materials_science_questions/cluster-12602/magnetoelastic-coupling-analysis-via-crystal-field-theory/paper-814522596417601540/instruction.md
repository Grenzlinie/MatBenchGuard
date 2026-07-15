# Band Jahn-Teller Effect and DOS Peak Splitting in CoFe₁₊ₓTi₁₋ₓAl via KKR-CPA-LDA

## Problem background
Heusler alloys CoFeTiAl and CoFeFeAl represent two limiting electronic and magnetic states: a nonmagnetic semiconductor and a high‑spin‑polarised ferrimagnetic metal, respectively. The isostructural alloy series CoFe₁₊ₓTi₁₋ₓAl (x = 0 → 1) offers a continuous path to follow the evolution of structure, magnetism, and electronic properties from one limit to the other. A central question is whether the series exhibits a sharp simultaneous change in equilibrium lattice parameter (ELP) and magnetization near a critical composition, and whether such a change can be linked to a band Jahn‑Teller effect — specifically, the splitting or merging of Co and Fe(4b) density‑of‑states peaks in the spin‑down channel near the Fermi level. This task reproduces the spin‑polarised KKR‑CPA‑LDA calculations that provide the computational evidence for this mechanism.

## Approach
The calculations use the Korringa‑Kohn‑Rostoker method with the coherent potential approximation and the local density approximation (KKR‑CPA‑LDA), available in the public Akai code. The crystal structure is the quaternary Heusler (LiMgPdSn‑type) arrangement: Co at 4a (0,0,0), Fe at 4b (½,½,½), Ti at 4c (¼,¼,¼), Al at 4d (¾,¾,¾). For off‑stoichiometric compositions the extra Fe atoms are assumed to randomly occupy the vacant Ti sites, a disorder treated with CPA.

The workflow consists of two main stages. First, for each composition x a series of total‑energy calculations is performed as a function of the lattice constant; the resulting energy‑volume data are fitted to an equation of state to obtain the equilibrium lattice parameter. At the equilibrium lattice parameter a self‑consistent spin‑polarised calculation yields the total magnetic moment per formula unit and the basic electronic density of states. Second, for two compositions (x ≈ 0.64 and 0.66), additional non‑self‑consistent calculations are carried out at both the equilibrium and at perturbed lattice parameters (contracted and expanded) to isolate the effect of lattice strain on the electronic structure. From these runs the atom‑projected partial density of states for Co and Fe at the 4b site are extracted for the spin‑down channel, enabling the analysis of peak splitting or merging.

## Reproduction target
You must produce two scored artefacts that together capture the composition‑dependent lattice parameter, magnetism, and the electronic structure signature of the band‑Jahn–Teller mechanism:

1. **results_table.csv** — a comma‑separated file with header `x, ELP, magnetization`. `x` is the Fe substitution level (0–1), `ELP` the equilibrium lattice parameter in Å, and `magnetization` the total magnetic moment per formula unit in μ<sub>B</sub>. At minimum, include rows for the compositions x = 0, 0.1, 0.2, …, 1.0, plus the refined grid values 0.62, 0.64, 0.66, 0.68.

2. **dos_critical.json** — a JSON object containing the spin‑down, atom‑projected density of states for Co and Fe at the 4b site under four specific (x, lattice‑parameter) conditions:
   - `x64_eq`: x = 0.64 at its equilibrium lattice parameter (5.71 Å).
   - `x64_exp`: x = 0.64 at the expanded lattice parameter 5.74 Å.
   - `x66_eq`: x = 0.66 at its equilibrium lattice parameter (5.74 Å).
   - `x66_cont`: x = 0.66 at the contracted lattice parameter 5.71 Å.
   For each condition, provide arrays of [energy (eV relative to the Fermi level), DOS (states/eV/atom)] covering at least the energy window [-2, 2] eV for `Co_spin_down` and `Fe4b_spin_down`.

These artefacts are the raw output of the calculations; the hidden verifier will compare them against reference data and structural expectations.

## Assets

- Akai KKR-CPA-LDA code: http://sham.phys.sci.osaka-u.ac.jp/kkr

## Workflow steps

### Step 1: Set up KKR-CPA input configurations
- Role: process
- Action: Generate input files for the LiMgPdSn-type Heusler structure for all required compositions (X = 0, 0.1, …, 1.0 and refined grid near 0.65). Define CPA for randomly occupying Fe on vacant Ti sites.
- Evidence: `/app/outputs/setup.log`

### Step 2: Total energy vs lattice parameter scans
- Role: process
- Action: For each composition, run spin-polarised KKR-CPA total-energy calculations over a range of lattice parameters sufficient to locate the minimum energy.
- Evidence: `/app/outputs/energy_scan.log`

### Step 3: Determine equilibrium lattice parameters
- Role: process
- Action: Fit the total energy vs volume/lattice parameter data (e.g., Murnaghan equation of state) for each composition; extract the equilibrium lattice parameter (ELP).
- Evidence: `/app/outputs/elp_fit.log`

### Step 4: Compute magnetisation and electronic structure at equilibrium lattice
- Role: process
- Action: Run self-consistent spin-polarised KKR-CPA calculations at the determined ELP for every composition. Obtain total magnetic moment per formula unit, atomic magnetic moments, and total density of states.
- Evidence: `/app/outputs/scf.log`

### Step 5: Produce ELP and magnetisation results table
- Role: scored (load-bearing)
- Action: Compile the equilibrium lattice parameter (in Å) and total magnetic moment per formula unit (in μB) for all compositions into a CSV file. Include at minimum the values for X = 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.8, 0.9, 1.0.
- Output file: `/app/outputs/results_table.csv`
- Format: csv
- Contract: CSV with header: x (float between 0 and 1), ELP (float, Å), magnetization (float, μB). One row per composition.
- Scoring: scored by hidden verifier

### Step 6: Compute non-equilibrium DOS for critical compositions
- Role: process
- Action: Run KKR-CPA calculations for X = 0.64 and X = 0.66 at both the equilibrium lattice parameters (5.71 Å for X=0.64, 5.74 Å for X=0.66) and at the perturbed lattice parameters (X=0.64 expanded to 5.74 Å, X=0.66 contracted to 5.71 Å). Extract the atom-projected partial density of states for Co and Fe atoms at the 4b site in the spin-down channel.
- Evidence: `/app/outputs/dos_calc.log`

### Step 7: Produce DOS critical JSON
- Role: scored
- Action: Format the spin-down atom-projected DOS of Co and Fe(4b) for the four required cases into a JSON file. Each case is an object with 'Co_spin_down' and 'Fe4b_spin_down' arrays of [energy, DOS] pairs (energy in eV, DOS in states/eV/atom) covering at least [-2, 2] eV relative to the Fermi level.
- Output file: `/app/outputs/dos_critical.json`
- Format: json
- Contract: JSON object with keys 'x64_eq', 'x64_exp', 'x66_eq', 'x66_cont'. Each value is an object with keys 'Co_spin_down' and 'Fe4b_spin_down'. Each such value is a 2D array of [energy, DOS] pairs.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_table.csv`
- `/app/outputs/dos_critical.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_table.csv
- path: `/app/outputs/results_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice parameter and total magnetic moment per formula unit for CoFe₁₊ₓTi₁₋ₓAl across the composition range. The checker compares against paper-reported values and verifies the discontinuity near x≈0.65.
- schema:
  - `type`: table
  - `required_columns`: `x`, `ELP`, `magnetization`
  - `units`:
    - `ELP`: Å
    - `magnetization`: μB

### dos_critical.json
- path: `/app/outputs/dos_critical.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Spin-down atom-projected DOS for Co and Fe(4b) at four critical composition/lattice-parameter combinations. The checker audits peak splitting patterns to confirm the band Jahn–Teller mechanism.
- schema:
  - `type`: object
  - `required`: `x64_eq`, `x64_exp`, `x66_eq`, `x66_cont`
  - `properties`:
    - `x64_eq`:
      - `type`: object
      - `properties`:
        - `Co_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number
        - `Fe4b_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number
    - `x64_exp`:
      - `type`: object
      - `properties`:
        - `Co_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number
        - `Fe4b_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number
    - `x66_eq`:
      - `type`: object
      - `properties`:
        - `Co_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number
        - `Fe4b_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number
    - `x66_cont`:
      - `type`: object
      - `properties`:
        - `Co_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number
        - `Fe4b_spin_down`:
          - `type`: array
          - `items`:
            - `type`: array
            - `items`:
              - `type`: number

Notes: The paper's B2-disorder verification calculations are omitted as they are not required for the main band Jahn–Teller claim. The KKR-CPA-LDA code must be compiled from public source; the solving agent is responsible for obtaining and compiling it.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "ELP",
          "magnetization"
        ],
        "units": {
          "ELP": "Å",
          "magnetization": "μB"
        }
      },
      "description": "Equilibrium lattice parameter and total magnetic moment per formula unit for CoFe₁₊ₓTi₁₋ₓAl across the composition range. The checker compares against paper-reported values and verifies the discontinuity near x≈0.65."
    },
    {
      "file": "dos_critical.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "x64_eq",
          "x64_exp",
          "x66_eq",
          "x66_cont"
        ],
        "properties": {
          "x64_eq": {
            "type": "object",
            "properties": {
              "Co_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              },
              "Fe4b_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "x64_exp": {
            "type": "object",
            "properties": {
              "Co_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              },
              "Fe4b_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "x66_eq": {
            "type": "object",
            "properties": {
              "Co_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              },
              "Fe4b_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "x66_cont": {
            "type": "object",
            "properties": {
              "Co_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              },
              "Fe4b_spin_down": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Spin-down atom-projected DOS for Co and Fe(4b) at four critical composition/lattice-parameter combinations. The checker audits peak splitting patterns to confirm the band Jahn–Teller mechanism."
    }
  ],
  "notes": "The paper's B2-disorder verification calculations are omitted as they are not required for the main band Jahn–Teller claim. The KKR-CPA-LDA code must be compiled from public source; the solving agent is responsible for obtaining and compiling it."
}
```

## How you are scored
An automated hidden verifier will evaluate each scored artefact independently.

- For **results_table.csv**, the verifier compares your computed ELP and magnetization values for each composition against hidden reference data, computing root‑mean‑square deviations for both quantities. It also checks for a sharp discontinuity near the critical composition by verifying that the difference between the x ≈ 0.66 and x ≈ 0.64 values exceeds a hidden threshold.
- For **dos_critical.json**, the verifier performs a structural audit: it locates peaks in the spin‑down DOS of Co and Fe(4b) within an energy window near the Fermi level and checks that the `x64_eq` and `x66_eq` cases show the expected splitting/merging pattern characteristic of the band‑Jahn–Teller mechanism, and that the perturbed‑lattice cases (`x64_exp`, `x66_cont`) show the inverse behavior.

The final reward is a weighted combination of the scores from the two artefacts (the table carries the larger weight). Simply reporting the paper’s numbers is not sufficient — the verifier uses tolerances and structural criteria that require a genuine, self‑consistent first‑principles calculation.
