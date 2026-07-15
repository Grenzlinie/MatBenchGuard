# DFT formation energies and multislice STEM simulations of point defect complexes in beta-Ga2O3

## Problem background
Point defect complexes in the ultra-wide band gap semiconductor β‑Ga₂O₃ critically influence its electronic and optical properties. The material’s performance in devices such as power electronics and transparent conductors can be severely degraded by deep-level defects. Understanding the atomic-scale structure and electronic behaviour of these defects is essential for controlling doping and for advancing β‑Ga₂O₃ technology. A particular divacancy–interstitial complex, 2V_Ga1–Ga_i, has been proposed to act as a compensating acceptor. This reproduction task focuses on computationally validating the energetic ordering, charge-state transition levels, and characteristic HAADF‑STEM intensity signatures of this complex using density functional theory and image simulations.

## Approach
The reproduction proceeds in two computational stages. First, hybrid density functional theory (DFT) calculations are performed with the HSE06 functional (32% exact exchange) for bulk β‑Ga₂O₃ and for the 2V_Ga1–Ga_i defect complexes at the i_c and i_b interstitial sites using a 160‑atom supercell. Total energies are obtained for relevant charge states, and relaxed defect structures are generated. From these, formation energies are computed as a function of the Fermi level using chemical potentials for oxygen and gallium, and thermodynamic charge-state transition levels (e.g., ε(-/-2) or ε(-2/-3)) are extracted. Second, multislice HAADF‑STEM image simulations are carried out using the relaxed defect structures. The simulation models a 25 nm thick crystal along the [010] projection with microscope parameters C_s3 = 0.002 mm, C_s5 = 1.0 mm, convergence half‑angle 20.0 mrad, and an acceleration voltage of 300 kV. Line profiles of the HAADF intensity are extracted across Ga₁ columns adjacent to interstitial positions for both defect‑free and defect‑containing configurations, enabling a quantitative comparison of column intensities.

## Reproduction target
You must produce three scored output files from the described workflow:
- `formation_energies.json` – formation energies of the 2V_Ga1–Ga_i complexes (i_c and i_b sites) for the computed charge states, including the chemical potentials (μ_O, μ_Ga).
- `transition_levels.json` – extracted thermodynamic charge-state transition levels (eV above the valence band maximum) for these complexes.
- `simulated_intensity_profiles.csv` – CSV file with columns `distance_nm`, `intensity_defect_free`, `intensity_with_defect`, representing line profiles of HAADF intensity across Ga₁ columns adjacent to interstitial sites in the simulated images.
Your task is to compute these quantities by faithfully executing the DFT and multislice simulations. The verifier will subsequently assess the results against expected physical trends and magnitudes without providing you the reference values.

## Assets

- β-Ga2O3 crystal structure (CIF): https://materialsproject.org/materials/mp-342/
- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org/
- HSE06 pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Multislice simulation code (Dr. Probe or equivalent): https://www.er-c.org/barthel/drprobe/

## Workflow steps

### Step 1: DFT defect calculation
- Role: process
- Action: Perform hybrid functional DFT calculations (HSE06, 160-atom supercell) for bulk β-Ga2O3 and for 2V-Ga1–Ga_i defect complexes at ic and ib interstitial sites. Compute total energies for relevant charge states and obtain relaxed defect structures.
- Evidence: `/app/outputs/dft_raw_energies.pkl`

### Step 2: Formation energies
- Role: scored (load-bearing)
- Action: From the DFT total energies and chemical potentials, compute the formation energies of 2V_Ga1–Ga_i (ic and ib) complexes as a function of Fermi level and write formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON object: {"system": string, "charge_states": [int], "formation_energies": {"<site>_<charge>": {"mu_O": float, "mu_Ga": float, "energy_eV": float}, ...}, "data_source": string, where <site> is "ic" or "ib" and <charge> is the integer charge state (e.g., "ic_0", "ib_-2")}
- Scoring: scored by hidden verifier

### Step 3: Charge-state transition levels
- Role: scored (load-bearing)
- Action: For each defect complex (ic and ib), determine the thermodynamic charge-state transition level (e.g., ε(-/-2) or ε(-2/-3)) in eV above VBM and write transition_levels.json as a JSON array of objects.
- Output file: `/app/outputs/transition_levels.json`
- Format: json
- Contract: JSON array of objects, each with: {"defect": string, "transition": string, "level_eV": float, "method": string}
- Scoring: scored by hidden verifier

### Step 4: Multislice HAADF-STEM intensity profiles
- Role: scored (load-bearing)
- Action: Run multislice simulation code (Dr. Probe or equivalent) using the relaxed defect structures from the DFT step. Simulate HAADF-STEM images for a 25 nm thick crystal along [010] projection with microscope parameters C_s3=0.002 mm, C_s5=1.0 mm, convergence half-angle 20.0 mrad, 300 kV. Produce line profiles of HAADF intensity across Ga1 columns adjacent to interstitials for defect-free and defect-containing configurations, and write simulated_intensity_profiles.csv.
- Output file: `/app/outputs/simulated_intensity_profiles.csv`
- Format: csv
- Contract: CSV columns: distance_nm (float), intensity_defect_free (float), intensity_with_defect (float). Header required.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/transition_levels.json`
- `/app/outputs/simulated_intensity_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies of 2V_Ga1–Ga_i complexes at i_c and i_b sites, enabling verification of energetic ordering.
- schema:
  - `type`: object
  - `required`:
    - `system`: string
    - `charge_states`: array of integers
    - `formation_energies`: object with keys of the form <site>_<charge> (e.g., 'ic_0', 'ib_-2'), each value an object with mu_O (float, eV), mu_Ga (float, eV), energy_eV (float)
    - `data_source`: string

### transition_levels.json
- path: `/app/outputs/transition_levels.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic charge-state transition levels for the defect complexes (ic and ib), to be compared against the paper-reported deep acceptor range.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`:
      - `defect`: string (e.g., '2V_Ga1–Ga_i^c')
      - `transition`: string (e.g., '-/2-')
      - `level_eV`: float (eV above VBM)
      - `method`: string

### simulated_intensity_profiles.csv
- path: `/app/outputs/simulated_intensity_profiles.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Line profiles of HAADF intensity across Ga1 columns, showing at least 15% reduction in intensity adjacent to interstitials relative to defect-free.
- schema:
  - `type`: table
  - `required_columns`: `distance_nm`, `intensity_defect_free`, `intensity_with_defect`
  - `units`:
    - `distance_nm`: nanometers
    - `intensity_defect_free`: arbitrary intensity
    - `intensity_with_defect`: arbitrary intensity

Notes: All scored artifacts are produced by the agent's computational workflow. DFT and multislice steps must be executed; the process step output (relaxed structures) is required. The checker re-derives the ordering, transition level range, and intensity reduction from these artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "system": "string",
          "charge_states": "array of integers",
          "formation_energies": "object with keys of the form <site>_<charge> (e.g., 'ic_0', 'ib_-2'), each value an object with mu_O (float, eV), mu_Ga (float, eV), energy_eV (float)",
          "data_source": "string"
        }
      },
      "description": "Formation energies of 2V_Ga1–Ga_i complexes at i_c and i_b sites, enabling verification of energetic ordering."
    },
    {
      "file": "transition_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": {
            "defect": "string (e.g., '2V_Ga1–Ga_i^c')",
            "transition": "string (e.g., '-/2-')",
            "level_eV": "float (eV above VBM)",
            "method": "string"
          }
        }
      },
      "description": "Thermodynamic charge-state transition levels for the defect complexes (ic and ib), to be compared against the paper-reported deep acceptor range."
    },
    {
      "file": "simulated_intensity_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_nm",
          "intensity_defect_free",
          "intensity_with_defect"
        ],
        "units": {
          "distance_nm": "nanometers",
          "intensity_defect_free": "arbitrary intensity",
          "intensity_with_defect": "arbitrary intensity"
        }
      },
      "description": "Line profiles of HAADF intensity across Ga1 columns, showing at least 15% reduction in intensity adjacent to interstitials relative to defect-free."
    }
  ],
  "notes": "All scored artifacts are produced by the agent's computational workflow. DFT and multislice steps must be executed; the process step output (relaxed structures) is required. The checker re-derives the ordering, transition level range, and intensity reduction from these artifacts."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three scored output files you submit. The verifier checks your computed results for consistency with the underlying physics and literature expectations—for example, whether the formation energies exhibit the correct relative ordering, whether the transition levels fall within a plausible energy window, and whether the simulated intensity profiles show the characteristic signature of the divacancy–interstitial complex. Each artifact contributes a proportional share to your final reward (total 1.0). Fabricating numbers or attempting to guess the paper’s reported values will not yield a high score; only a genuine computational reproduction that follows the stated approach can satisfy the verifier.
