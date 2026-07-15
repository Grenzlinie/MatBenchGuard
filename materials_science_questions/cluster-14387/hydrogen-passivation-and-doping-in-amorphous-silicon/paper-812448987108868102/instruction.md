# Adatom dangling bond surface states in Si(111) DAS model

## Problem background
The Si(111) surface reconstructs into a 7×7 superstructure whose atomic arrangement is given by the dimer–adatom–stacking‑fault (DAS) model. This model features adatoms, rest atoms, corner holes, and dimers, and gives rise to dangling‑bond states on the adatoms. Understanding the electronic structure of these surface states—their number, energy width, and spatial localization—is essential for interpreting photoemission and scanning‑tunneling spectroscopy experiments. First‑principles methods can predict these properties directly from the atomic coordinates, without empirical parameters.

## Approach
We use density‑functional theory (DFT) in the local‑density approximation (Ceperley–Alder functional) with a norm‑conserving pseudopotential for silicon. The calculation is performed in a repeated‑slab geometry. The slab contains 16 Si layers and adatom layers on both surfaces, following the DAS model. A plane‑wave basis set is employed, with the kinetic‑energy cutoff chosen to balance accuracy and computational cost; higher‑energy plane waves are included perturbationally. A single special k‑point that permits group‑theory reduction is used for Brillouin‑zone integration. From the self‑consistent calculation we obtain the one‑electron energies and wavefunctions. Post‑processing then identifies which bands lie in the bulk band gap and analyses the spatial character of the lowest‑energy surface state among those bands.

## Reproduction target
Run the described DFT calculation for the Si(111) 7×7 DAS model and extract the following from the output: (i) the number of surface‑state bands that fall within the bulk band gap, (ii) the total energy width spanned by those bands, and (iii) for the lowest‑energy band in that group, the adatom site (among the four types labelled A(F)c, A(F)m, A(U)c, A(U)m) on which the wavefunction has the largest amplitude. Write the results to `electronic_structure_results.json` according to the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving pseudopotential for Si (Bachelet–Hamann–Schlüter type): https://pseudodojo.org/ or SSSP library
- Atomic coordinates for Si(111) 7×7 DAS slab model

## Workflow steps

### Step 1: DFT calculation for Si(111) 7×7 DAS slab
- Role: process
- Action: Construct the Si(111) 7×7 DAS slab model (16 Si layers, adatom layers on both surfaces, repeated slab geometry). Run a plane‑wave DFT calculation with Quantum ESPRESSO using the LDA (Ceperley–Alder functional) and a norm‑conserving Si pseudopotential. Set plane‑wave cutoffs to 2.3 aB⁻¹ for wavefunctions, 3.1 aB⁻¹ for electron density; treat waves above 1.48 aB⁻¹ perturbationally. Use a single special k‑point for Brillouin‑zone integration that allows group‑theory splitting. Save one‑electron energies and wavefunction coefficients.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 2: Extract surface‑state band properties
- Role: scored (load-bearing)
- Action: From the DFT output, identify the bands at the special k‑point that lie within the bulk band gap (region a). Count the number of such bands; determine the energy width they cover. For the state with the lowest energy in this group, examine the wavefunction amplitude on the four types of adatom sites (A(F)c, A(F)m, A(U)c, A(U)m) and record the site with the largest amplitude. Write the results to electronic_structure_results.json.
- Output file: `/app/outputs/electronic_structure_results.json`
- Format: json
- Contract: {"number_of_surface_state_bands_in_gap": int, "energy_width_of_region_a": float (eV), "lowest_energy_state_adatom_site": string, "lowest_energy_band_index": int, "band_energies_at_special_kpoint": [float], "surface_state_band_indices": [int]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_structure_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_structure_results.json
- path: `/app/outputs/electronic_structure_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the extracted number of surface-state bands in the gap, their energy width, the adatom site of the lowest-energy state, the band index of that state, the full list of band energies at the special k‑point, and the indices of the surface-state bands.
- schema:
  - `type`: object
  - `required`:
    - `number_of_surface_state_bands_in_gap`: integer
    - `energy_width_of_region_a`: float (eV)
    - `lowest_energy_state_adatom_site`: string
    - `lowest_energy_band_index`: integer
    - `band_energies_at_special_kpoint`: array of floats (eV)
    - `surface_state_band_indices`: array of integers

Notes: The reference values (number of bands = 24, energy width ≈ 0.4 eV, lowest site = ‘A(F)c’) are hidden; the checker compares the agent's computed values to these gold numbers with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "number_of_surface_state_bands_in_gap": "integer",
          "energy_width_of_region_a": "float (eV)",
          "lowest_energy_state_adatom_site": "string",
          "lowest_energy_band_index": "integer",
          "band_energies_at_special_kpoint": "array of floats (eV)",
          "surface_state_band_indices": "array of integers"
        }
      },
      "description": "Contains the extracted number of surface-state bands in the gap, their energy width, the adatom site of the lowest-energy state, the band index of that state, the full list of band energies at the special k‑point, and the indices of the surface-state bands."
    }
  ],
  "notes": "The reference values (number of bands = 24, energy width ≈ 0.4 eV, lowest site = ‘A(F)c’) are hidden; the checker compares the agent's computed values to these gold numbers with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads `electronic_structure_results.json` and independently checks the quantities you report. The verifier scores each workflow stage's artifact, and the stage scores are combined by weight into the final reward. Reporting accurate numbers is necessary but not sufficient; you must demonstrate that you obtained them by executing the full computational pipeline. The verifier compares your output to reference values derived from the original study, but no reference values or tolerances are disclosed to you.
