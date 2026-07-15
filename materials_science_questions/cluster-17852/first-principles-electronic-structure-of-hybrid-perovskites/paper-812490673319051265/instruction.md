# Computing Defect Levels and Formation Energies in Orthorhombic CsPbBr3 using Hybrid DFT

## Problem background
Lead halide perovskites like CsPbBr₃ exhibit excellent optoelectronic performance, including high photoluminescence quantum yields and efficient charge transport, despite the presence of significant defect densities. This phenomenon, often called "defect tolerance", has been widely attributed to the Shallow Defect Hypothesis (SDH), which asserts that all energetically favorable native defects in these materials have only shallow levels and therefore cannot act as non-radiative recombination centers. However, growing experimental and theoretical evidence suggests that deep levels may in fact exist in metal halide perovskites, challenging the SDH. Resolving this question for CsPbBr₃ requires a comprehensive first‑principles investigation that determines the formation energies and thermodynamic charge‑state transition levels of all relevant native point defects and common impurities, across a range of chemical potential conditions. This task aims to perform such an investigation using hybrid density functional theory (DFT) with spin–orbit coupling (SOC), the same level of theory as the state‑of‑the‑art approach, and to produce the key quantitative results that decide whether deep defect levels appear in CsPbBr₃.

## Approach
The core method is a hybrid‑DFT defect calculation pipeline. The orthorhombic CsPbBr₃ crystal structure is obtained from a public database. First, a bulk electronic structure calculation is performed with the HSE hybrid functional (35% exact exchange, 0.1 Å⁻¹ screening) and SOC to reproduce the experimental band gap of CsPbBr₃ (~2.3 eV). Next, supercells are constructed for a series of native defects (vacancies, interstitials, antisites) and hydrogen impurities (interstitial and substitutional at each site) in all relevant charge states. Total energies of each defect supercell and of the pristine supercell are computed with identical HSE+SOC settings. Reference‑phase total energies (elemental Cs, Pb, Br and compounds such as CsBr, PbBr₂) are also evaluated to establish the chemical potential bounds corresponding to Pb‑rich and Br‑rich growth conditions, using either direct computation or publicly available Materials Project data. Defect formation energies are then calculated from these total energies using the standard supercell formalism, with the Freysoldt finite‑size correction applied to charged defects. From the formation energies, the charge‑neutrality Fermi level is determined under both Pb‑rich and Br‑rich chemical potentials, and the formation energies of the most abundant defects at that Fermi level are identified. Finally, thermodynamic charge‑state transition levels ε(q/q′) are derived from the formation energies evaluated at the valence‑band maximum, focusing on the defects that give rise to deep levels in the gap.

## Reproduction target
Produce two JSON files containing the primary numerical results of the defect study, computed strictly from the HSE+SOC total energies and the defect formation energy formalism described in the approach. The first file, `formation_energies_at_charge_neutrality.json`, reports the equilibrium Fermi level and the formation energies of the dominant defects at that Fermi level under Pb‑rich and Br‑rich chemical potential extremes. The second file, `defect_transition_levels.json`, lists the thermodynamic charge‑state transition levels for three key defects: the bromine interstitial (Brᵢ, −/₊ transition), the hydrogen interstitial (Hᵢ, −/₊ transition), and hydrogen substituting on bromine (H_Br, 0/₊ transition). All energies are expressed in eV and referenced to the valence‑band maximum. The required structure and keys of these files are fixed by the output contract, and the calculations must be internally consistent: the transition levels derivable from the formation energies at E_F=0 must agree with the transition levels reported directly.

## Assets

- CP2K (open-source DFT code with HSE+SOC capability): https://www.cp2k.org/
- SXDEFECTCORR (finite-size correction for charged defects): https://bitbucket.org/cfreysoldt/sxdefectcorr/
- Python packages (pymatgen, numpy, scipy): pip install pymatgen numpy scipy
- Orthorhombic CsPbBr3 crystal structure (CIF): https://next-gen.materialsproject.org/materials/mp-1087555?cif=true
- Materials Project database (reference phases for chemical potential bounds): https://materialsproject.org/

## Workflow steps

### Step 1: Bulk electronic structure and reference phase calculations
- Role: process
- Action: Obtain the orthorhombic CsPbBr3 crystal structure (Materials Project mp-1087555). Perform HSE+SOC DFT calculation with 35% exact-exchange mixing and screening parameter 0.1 Å⁻¹ to reproduce the experimental band gap of ~2.3 eV. Also compute total energies of reference phases (Cs, Pb, Br, CsBr, PbBr2, etc.) to determine chemical potential ranges for Pb-rich and Br-rich conditions.
- Evidence: `/app/outputs/bulk_reference.json`

### Step 2: Construction and DFT total energy calculations of defect supercells
- Role: process
- Action: Construct supercells for all enumerated native point defects (vacancies, interstitials, antisites) and hydrogen impurities (Hi, H_Br, H_Pb, H_Cs) in relevant charge states, and for the pristine supercell. Perform HSE+SOC DFT total energy calculations for each defect supercell and the pristine supercell. Record total energies E[X^q] and E[bulk].
- Evidence: `/app/outputs/defect_total_energies.json`

### Step 3: Compute defect formation energies at charge-neutrality
- Role: scored (load-bearing)
- Action: Using total energies from step2, chemical potentials from step1, and the Freysoldt finite-size correction (SXDEFECTCORR), compute defect formation energies E^f[X^q] as a function of Fermi level. Determine the equilibrium Fermi level E_F0 by solving charge neutrality. For the dominant defects in the defect hull at Pb-rich and Br-rich extremes, report their formation energies evaluated at E_F0. Write the results to formation_energies_at_charge_neutrality.json.
- Output file: `/app/outputs/formation_energies_at_charge_neutrality.json`
- Format: json
- Contract: {"Pb_rich": {"E_F0": <float>, "defects": [{"defect": "<string>", "formation_energy": <float>}, ...]}, "Br_rich": {"E_F0": <float>, "defects": [{"defect": "<string>", "formation_energy": <float>}, ...]}}
- Scoring: scored by hidden verifier

### Step 4: Compute thermodynamic charge-state transition levels
- Role: scored (load-bearing)
- Action: From the defect formation energies evaluated at E_F=0 (obtained during step3), compute the charge-state transition levels ε(q/q') using the formula ε = (E^f(q; E_F=0) - E^f(q'; E_F=0)) / (q' - q). Report the values for the key deep-level defects: Br_i (−/+), H_i (−/+), and H_Br (0/+). Write to defect_transition_levels.json.
- Output file: `/app/outputs/defect_transition_levels.json`
- Format: json
- Contract: {"Br_i_(-/+)": <float>, "H_i_(-/+)": <float>, "H_Br_(0/+)": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies_at_charge_neutrality.json`
- `/app/outputs/defect_transition_levels.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies_at_charge_neutrality.json
- path: `/app/outputs/formation_energies_at_charge_neutrality.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of the dominant defects at the charge-neutrality Fermi level under Pb-rich and Br-rich conditions, computed from HSE+SOC total energies and Freysoldt correction.
- schema:
  - `type`: object
  - `required`:
    - `Pb_rich`:
      - `type`: object
      - `required`:
        - `E_F0`: number (eV)
        - `defects`: array of objects with keys 'defect' (string) and 'formation_energy' (number, eV)
    - `Br_rich`:
      - `type`: object
      - `required`:
        - `E_F0`: number (eV)
        - `defects`: array of objects with keys 'defect' (string) and 'formation_energy' (number, eV)

### defect_transition_levels.json
- path: `/app/outputs/defect_transition_levels.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic charge-state transition levels for the deep-level defects Br interstitial, H interstitial, and H on Br site, referenced to the valence band maximum.
- schema:
  - `type`: object
  - `required`:
    - `Br_i_(-/+)`: number (eV)
    - `H_i_(-/+)`: number (eV)
    - `H_Br_(0/+)`: number (eV)

Notes: The hidden checker compares the submitted values to a hidden reference set (paper-reported results) with tolerances and checks internal consistency: transition levels must be consistent with the submitted formation energies at E_F=0 within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies_at_charge_neutrality.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Pb_rich": {
            "type": "object",
            "required": {
              "E_F0": "number (eV)",
              "defects": "array of objects with keys 'defect' (string) and 'formation_energy' (number, eV)"
            }
          },
          "Br_rich": {
            "type": "object",
            "required": {
              "E_F0": "number (eV)",
              "defects": "array of objects with keys 'defect' (string) and 'formation_energy' (number, eV)"
            }
          }
        }
      },
      "description": "Formation energies of the dominant defects at the charge-neutrality Fermi level under Pb-rich and Br-rich conditions, computed from HSE+SOC total energies and Freysoldt correction."
    },
    {
      "file": "defect_transition_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Br_i_(-/+)": "number (eV)",
          "H_i_(-/+)": "number (eV)",
          "H_Br_(0/+)": "number (eV)"
        }
      },
      "description": "Thermodynamic charge-state transition levels for the deep-level defects Br interstitial, H interstitial, and H on Br site, referenced to the valence band maximum."
    }
  ],
  "notes": "The hidden checker compares the submitted values to a hidden reference set (paper-reported results) with tolerances and checks internal consistency: transition levels must be consistent with the submitted formation energies at E_F=0 within a tolerance."
}
```

## How you are scored
A hidden verifier reads the two output JSON files and evaluates them against a set of reference values that were extracted from the original study. The verifier checks both the absolute numeric values and the internal consistency of the results. The formation energies and Fermi levels are scored by comparing with the reference values; the transition levels are scored independently, but the verifier also computes the transition levels from the reported formation energies at E_F=0 and verifies that they agree with the directly reported transition levels. Each artifact contributes a weighted share of the final score, with the transition levels and formation energies carrying substantial weight. The final reward reported in `/logs/verifier/reward.txt` is a single float between 0 and 1, with 1 representing a fully successful reproduction within the acceptable numerical spread. The verifier runs without network access and does not re‑execute any DFT calculation.
