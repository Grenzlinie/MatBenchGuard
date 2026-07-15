# Extended Hückel Binding Energies of Adsorbates on Graphite Surfaces

## Problem background
The oxidation of carbon materials such as graphite is promoted by the presence of alkali metals like potassium, dramatically increasing the sticking probability of molecular oxygen even at very low alkali coverages. The mechanism of this promotion remains debated — whether it involves direct chemical interaction between potassium and O₂, or merely an electronic modification of the graphite surface. Understanding the binding energetics of potassium, dioxygen, and their coadsorbed complexes on graphite is essential for elucidating the elementary steps of the catalyzed oxidation. This task reproduces the theoretical component of a study that used extended Hückel tight-binding calculations to compute binding energies for individual and coadsorbed species on perfect and defective graphite surfaces, providing insights into the relative stabilization afforded by potassium coadsorption versus surface defects.

## Approach
The calculations are performed within the extended Hückel tight-binding method. The graphite surface is modelled by a two-layer slab with a C–C bond length of 142 pm and an interlayer distance of 335 pm. The perfect surface unit cell contains 36 carbon atoms (18 per layer). For defect calculations, larger cells are used to isolate the vacancy; for an in‑plane vacancy a surface layer of 24 carbon atoms is sufficient, with the vacancy created by removing at least two adjacent carbon atoms to accommodate the adsorbate at a C–O distance of 175 pm without artificial strain.

Binding energies are computed as  
E_b = E(bare slab) + E(free adsorbate) − E(adsorbate+slab),  
where a positive value indicates exothermic adsorption.  
The atomic parameters (Coulomb integrals H_ii and Slater exponents ζ) to be used are:
- Carbon:  2s −21.4 eV, ζ = 1.625;  2p −11.4 eV, ζ = 1.625.
- Oxygen:  2s −32.3 eV, ζ = 2.275;  2p −14.8 eV, ζ = 2.275.
- Potassium: 4s −10.49 eV, ζ = 1.20; 4p −7.37 eV, ζ = 1.20  
  (these K parameters were obtained by charge iteration).
The reference energies for the free species are E(K) = −4.34 eV and E(O₂) = −249.681 eV.  
The extended Hückel calculation can be performed using the open‑source package YAeHMOP or by a self‑implementation of the method employing these parameters.

## Reproduction target
Compute and save to a CSV file the binding energies (in eV) for the following six adsorption configurations, each named by the identifier given in parentheses:

1. Potassium atom at the 6‑fold hollow site (C site) on a perfect graphite surface, with C–K = 303 pm  (K_perfect_Csite).
2. O₂ bent end‑on on a perfect surface at the A (on‑top) site, with C–O = 175 pm and the surface–O–O angle γ = 135°  (O2_perfect_Aendon_135).
3. O₂ side‑on above a coadsorbed potassium atom (K1 site), with K–O = 270 pm and the O–O bond parallel to the surface  (O2_K1_sideon).
4. O₂ end‑on in a large vacancy (at least two missing C atoms), with the O₂ approaching in the surface plane at a C–O distance of 175 pm  (O2_defect_inplane_endon).
5. O₂ side‑on in the same large vacancy, also with a C–O distance of 175 pm  (O2_defect_inplane_sideon).
6. Potassium atom on a rim carbon adjacent to a single‑atom vacancy, with C–K = 303 pm  (K_defect_rim).

The CSV file must be written to `/app/outputs/binding_energies.csv` and contain exactly two columns: `configuration` (string) and `binding_energy_eV` (float), with one row per configuration. The reference energies for the bare slab and free adsorbates are given in the Approach section; use them consistently.

## Assets

- Extended Hückel implementation: YAeHMOP

## Workflow steps

### Step 1: Model setup and EH parameters
- Role: process
- Action: Build a two-layer graphite slab model (C-C bond length 142 pm, interlayer distance 335 pm) and set up an extended Hückel tight-binding code (or configure YAeHMOP) with the atomic parameters for C, O, and K as provided in the instructions. Unit cell for the perfect surface contains 36 carbon atoms. For defect calculations, larger cells (e.g., 24 carbon surface layer) will be constructed later as needed.
- Evidence: none

### Step 2: Compute binding energies for selected configurations
- Role: scored (load-bearing)
- Action: Compute the binding energy E_b = E(bare surface) + E(free adsorbate) - E(adsorbate+surface) for the following configurations using the extended Hückel method: (1) K at the 6-fold hollow site (C site, C-K = 303 pm) on a perfect surface; (2) O2 bent end-on on a perfect surface A site (C-O = 175 pm, surface-O-O angle 135°); (3) O2 side-on above a coadsorbed K atom (K1 site, K-O = 270 pm); (4) O2 end-on in a large vacancy (at least two missing C atoms, in-plane C-O distance 175 pm); (5) O2 side-on in the same vacancy; (6) K on a rim carbon adjacent to a single vacancy (C-K = 303 pm). Use the same reference energies for free K, O2, and O as in the provided parameters. Write results to a CSV file.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: configuration: string, binding_energy_eV: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed binding energies for the specified adsorption configurations on graphite; used to verify the paper's reported energies and the relative ordering K1 > defect > perfect surface.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `binding_energy_eV`
  - `units`:
    - `binding_energy_eV`: eV
  - `description`: Each row identifies a configuration and its computed binding energy in eV.

Notes: Configurations are identified by strings: K_perfect_Csite, O2_perfect_Aendon_135, O2_K1_sideon, O2_defect_inplane_endon, O2_defect_inplane_sideon, K_defect_rim. The hidden checker compares each value to the paper's gold with tolerances and checks the ordering trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "binding_energy_eV"
        ],
        "units": {
          "binding_energy_eV": "eV"
        },
        "description": "Each row identifies a configuration and its computed binding energy in eV."
      },
      "description": "Computed binding energies for the specified adsorption configurations on graphite; used to verify the paper's reported energies and the relative ordering K1 > defect > perfect surface."
    }
  ],
  "notes": "Configurations are identified by strings: K_perfect_Csite, O2_perfect_Aendon_135, O2_K1_sideon, O2_defect_inplane_endon, O2_defect_inplane_sideon, K_defect_rim. The hidden checker compares each value to the paper's gold with tolerances and checks the ordering trend."
}
```

## How you are scored
A hidden automatic verifier will read your `binding_energies.csv` and independently score your submission. It compares each binding energy you report against expected reference values (derived from the original theoretical study) using tolerances that account for differences in k‑point sampling, numerical integration, and other implementation details. In addition, the verifier checks that the relative ordering of the binding energies among the potassium‑covered, defective, and perfect surface configurations follows a consistent physical pattern. The final reward is a weighted combination of these numeric matches and the trend check, yielding a score between 0 and 1. Reporting the values is not enough – you must genuinely perform the extended Hückel computation for each configuration.
