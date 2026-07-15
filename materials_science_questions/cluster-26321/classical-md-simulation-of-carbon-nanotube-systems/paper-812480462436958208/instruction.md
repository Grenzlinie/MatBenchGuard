# Reproduce DFT release barriers and spectral signatures of a drug-nanotube inclusion complex

## Problem background
Cisplatin is a widely used anticancer drug, but its systemic toxicity limits clinical dosage. Carbon nanotubes (CNTs) are promising drug delivery vehicles that can encapsulate cisplatin and release it in a controlled manner inside the body. This task reproduces a computational study of cisplatin (cDDP) release from an oxidized carbon nanotube inclusion complex (cDDP@CNTox) using density functional theory (DFT). The work quantifies the kinetic barrier, thermodynamics, and spectroscopic signatures (Raman and ¹H NMR) of the release process. Your goal is to compute the gas-phase release energy profile, the associated activation thermodynamics, dispersion-corrected energy barriers, Raman G/D intensity ratios at several points along the release path, and the ¹H NMR chemical shifts for cisplatin NH₃ protons at those points.

## Approach
The investigation proceeds in two stages. First, a semi-rigid scan simulates the drug release: starting from the published equilibrium geometry of the cDDP@CNTox inclusion complex, the cisplatin molecule is translated outward in 0.5 Å steps (28 steps total, covering 0–14 Å) while the surrounding nanotube atoms (72 carbon and 12 hydrogen atoms) are kept frozen; the remaining atoms are optimized at each step using DFT at the B3LYP/LANL2DZ/6-31G level. The total energy relative to the equilibrium complex gives an energy profile along the release coordinate. In the second stage, the scan geometries are used for additional calculations: (a) harmonic vibrational frequency calculations at selected scan points (7, 11, 15, 28) to obtain enthalpy, entropic term (TΔS), and Gibbs free energy of release; (b) single-point energy evaluations on the geometry corresponding to the barrier (scan point 7) with dispersion-corrected functionals (B3LYP-D3 and M06-2X) and augmented basis sets; (c) Raman spectra (B3LYP/LANL2DZ/6-31G) for the free oxidized nanotube, the inclusion complex, and selected release intermediates, extracting the G‑band and D‑band frequencies and their intensity ratio; and (d) ¹H NMR chemical shifts (GIAO method, IEFPCM‑water solvent) for the cisplatin NH₃ protons in free cisplatin, the inclusion complex, and the same set of release geometries. All results are to be organized into a CSV file for the energy profile and a JSON file aggregating the thermodynamic, barrier, spectroscopic, and NMR quantities.

## Reproduction target
Produce two scored output files.

1. `/app/outputs/energy_profile.csv` – a two‑column CSV with the gas‑phase relative energy of the drug release scan at B3LYP/LANL2DZ/6-31G. Columns: `scan_step` (integer 1–28, corresponding to the 0.5 Å displacement steps) and `relative_energy_kcal_per_mol` (float, energy referenced to the equilibrium inclusion complex, in kcal mol⁻¹).

2. `/app/outputs/results.json` – a JSON object containing all other reproduction targets, with the following keys:
   - `gas_phase_barrier` (float, kcal mol⁻¹): the energy barrier from the B3LYP/LANL2DZ/6-31G scan.
   - `aqueous_barrier` (float, kcal mol⁻¹): the barrier with IEFPCM‑water solvation at the same level.
   - `activation_enthalpy`, `TdS`, `activation_free_energy` (each float, kcal mol⁻¹): activation thermodynamics from harmonic frequency calculations at scan point 7 (B3LYP/LANL2DZ/6-31G, gas phase, 1 atm, 298.15 K).
   - `b3lyp_d3_barrier`, `m06x_6_31g_barrier`, `m06x_631g_d_barrier` (each float, kcal mol⁻¹): dispersion‑corrected single‑point barriers at scan point 7 using the functionals/basis sets B3LYP-D3/LANL2DZ/6-31G(d,p), M06‑2X/LANL2DZ/6‑31G, and M06‑2X/LANL2DZ/6‑31G(d,p) respectively.
   - `Raman_data` (array of objects): each object contains `structure` (string: `"CNTox"`, `"cDDP@CNTox"`, `"CNTox⇒cDDP(7)"`, `"CNTox⇒cDDP(15)"`, or `"CNTox⇒cDDP(28)"`), `G_freq` (float, cm⁻¹), `D_freq` (float, cm⁻¹), and `G_D_ratio` (float).
   - `NMR_data` (array of objects): each object contains `structure` (string: `"free cDDP"`, `"cDDP@CNTox"`, `"CNTox⇒cDDP(7)"`, `"CNTox⇒cDDP(11)"`, `"CNTox⇒cDDP(15)"`, or `"CNTox⇒cDDP(28)"`), `proton_label` (string, label for the NH₃ proton, e.g., Ha, Hc, …), and `chemical_shift` (float, ppm, referenced to TMS).

All energy/enthalpy/entropy values must be reported in kcal mol⁻¹, frequencies in cm⁻¹, and NMR shifts in ppm.

## Assets

- cDDP@CNTox inclusion complex geometry (from De Souza et al., RSC Adv. 2017): 10.1039/C7RA00181K
- Open-source DFT package (e.g., ORCA, NWChem, PySCF) supporting B3LYP, B3LYP-D3, M06-2X and LANL2DZ/6-31G basis sets

## Workflow steps

### Step 1: Semi-rigid scan and energy profile
- Role: scored (load-bearing)
- Action: Retrieve the published cDDP@CNTox geometry from the supplementary material of De Souza et al., RSC Adv. 2017, 7, 13212–13222. Perform a semi-rigid scan at the B3LYP/LANL2DZ/6-31G level, translating the cisplatin molecule out of the nanotube cavity in 0.5 Å increments over 28 steps (0 to 14 Å displacement). Freeze the 72 carbon and 12 hydrogen atoms indicated in the paper; optimize the remaining atoms at each step. Compute the gas-phase total energy relative to the equilibrium inclusion complex and write a two-column CSV file.
- Output file: `/app/outputs/energy_profile.csv`
- Format: csv
- Contract: CSV with columns: scan_step (integer 1–28), relative_energy_kcal_per_mol (float). Energies are referenced to the equilibrium inclusion complex in kcal/mol.
- Scoring: scored by hidden verifier

### Step 2: Thermodynamic, single-point, Raman, and NMR analysis
- Role: scored
- Action: Using the scan geometries generated in step 01, perform the following calculations. (a) Harmonic vibrational frequency calculations at B3LYP/LANL2DZ/6-31G for scan points 7, 11, 15, and 28 to obtain ΔH, TΔS, and ΔG of release in the gas phase (1 atm, 298.15 K). (b) Single-point energy calculations on scan point 7 at B3LYP-D3/LANL2DZ/6-31G(d,p), M06-2X/LANL2DZ/6-31G, and M06-2X/LANL2DZ/6-31G(d,p) to obtain dispersion-corrected barriers. (c) Raman spectra (B3LYP/LANL2DZ/6-31G) for free CNTox, the cDDP@CNTox inclusion complex, and scan geometries 7, 15, 28; extract the G-band and D-band frequencies and the G/D intensity ratio. (d) 1H NMR chemical shifts (GIAO, IEFPCM-water) for cisplatin NH3 protons in free cDDP, the inclusion complex, and scan geometries 7, 11, 15, 28. Assemble all quantities into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: gas_phase_barrier (float), aqueous_barrier (float), activation_enthalpy (float), TdS (float), activation_free_energy (float), b3lyp_d3_barrier (float), m06x_6_31g_barrier (float), m06x_631g_d_barrier (float), Raman_data (array of {structure:str, G_freq:float, D_freq:float, G_D_ratio:float}), NMR_data (array of {structure:str, proton_label:str, chemical_shift:float}). All energy/enthalpy/entropy values in kcal/mol, frequencies in cm⁻¹, shifts in ppm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_profile.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_profile.csv
- path: `/app/outputs/energy_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Two-column CSV file with the gas-phase relative energy versus scan step number. The checker recomputes the profile error and verifies structural features such as peak location and energy decrease after the barrier.
- schema:
  - `type`: table
  - `required_columns`: `scan_step`, `relative_energy_kcal_per_mol`
  - `units`:
    - `relative_energy_kcal_per_mol`: kcal/mol

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing all reproduction targets: energy barriers, activation thermodynamics, dispersion-corrected barriers, Raman G/D ratios, and 1H NMR chemical shifts. The checker compares each numeric value against the paper's reference within specified tolerances and verifies cross-artifact consistency.
- schema:
  - `type`: object
  - `required`:
    - `gas_phase_barrier`: float (kcal/mol)
    - `aqueous_barrier`: float (kcal/mol)
    - `activation_enthalpy`: float (kcal/mol)
    - `TdS`: float (kcal/mol)
    - `activation_free_energy`: float (kcal/mol)
    - `b3lyp_d3_barrier`: float (kcal/mol)
    - `m06x_6_31g_barrier`: float (kcal/mol)
    - `m06x_631g_d_barrier`: float (kcal/mol)
    - `Raman_data`: array of objects [{structure: str, G_freq: float (cm^-1), D_freq: float (cm^-1), G_D_ratio: float}]
    - `NMR_data`: array of objects [{structure: str, proton_label: str, chemical_shift: float (ppm)}]

Notes: The semi-rigid scan must use the published geometry and the specified atom constraints. For the results.json, the structures to include are: for Raman – free CNTox, cDDP@CNTox, CNTox⇒cDDP(7), CNTox⇒cDDP(15), CNTox⇒cDDP(28); for NMR – free cDDP, cDDP@CNTox, CNTox⇒cDDP(7), CNTox⇒cDDP(11), CNTox⇒cDDP(15), CNTox⇒cDDP(28). The cisplatin NH3 proton labels are as used in the paper. All quantities must be in the specified units.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "scan_step",
          "relative_energy_kcal_per_mol"
        ],
        "units": {
          "relative_energy_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Two-column CSV file with the gas-phase relative energy versus scan step number. The checker recomputes the profile error and verifies structural features such as peak location and energy decrease after the barrier."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gas_phase_barrier": "float (kcal/mol)",
          "aqueous_barrier": "float (kcal/mol)",
          "activation_enthalpy": "float (kcal/mol)",
          "TdS": "float (kcal/mol)",
          "activation_free_energy": "float (kcal/mol)",
          "b3lyp_d3_barrier": "float (kcal/mol)",
          "m06x_6_31g_barrier": "float (kcal/mol)",
          "m06x_631g_d_barrier": "float (kcal/mol)",
          "Raman_data": "array of objects [{structure: str, G_freq: float (cm^-1), D_freq: float (cm^-1), G_D_ratio: float}]",
          "NMR_data": "array of objects [{structure: str, proton_label: str, chemical_shift: float (ppm)}]"
        }
      },
      "description": "JSON file containing all reproduction targets: energy barriers, activation thermodynamics, dispersion-corrected barriers, Raman G/D ratios, and 1H NMR chemical shifts. The checker compares each numeric value against the paper's reference within specified tolerances and verifies cross-artifact consistency."
    }
  ],
  "notes": "The semi-rigid scan must use the published geometry and the specified atom constraints. For the results.json, the structures to include are: for Raman – free CNTox, cDDP@CNTox, CNTox⇒cDDP(7), CNTox⇒cDDP(15), CNTox⇒cDDP(28); for NMR – free cDDP, cDDP@CNTox, CNTox⇒cDDP(7), CNTox⇒cDDP(11), CNTox⇒cDDP(15), CNTox⇒cDDP(28). The cisplatin NH3 proton labels are as used in the paper. All quantities must be in the specified units."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage’s output artifact. The verifier reads your submitted `energy_profile.csv` and `results.json` and compares the quantities against a hidden reference, applying appropriate tolerances and checking structural trends. For the energy profile, it verifies that the profile exhibits a barrier at the correct scan step and that later steps become exergonic; it may also recompute aggregate metrics. For the thermodynamic, single‑point, Raman, and NMR data in `results.json`, the verifier compares each value to the reference and checks expected trends such as the sign of the activation free energy, the increase in the G/D ratio after drug release, and the convergence of ¹H NMR shifts to free‑cisplatin values. The final reward (0–1) is a weighted combination of per‑artifact scores. Simply reporting numbers is not sufficient; you must execute the computational workflow and produce the two output files as described.
