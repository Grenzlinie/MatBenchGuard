# Pentadiamond property reproduction via DFT

## Problem background
Pentadiamond is a proposed three-dimensional carbon allotrope composed entirely of carbon atoms forming a network of pentagonal rings. The structure incorporates both sp² and sp³ hybridized carbon atoms and crystallizes in the cubic space group Fm-3m. This material is of interest because its unusual pentagonal bonding network may lead to exceptional mechanical properties and a semiconducting electronic character. The task is to reproduce, from first principles, the fundamental mechanical (elastic constants and derived moduli), electronic (band gap and carrier effective masses), and vibrational (dynamical stability) properties of pentadiamond by performing density functional theory calculations on the specified crystal structure.

## Approach
The reproduction uses density functional theory (DFT) with the generalized gradient approximation (PBE functional) and a suitable pseudopotential to describe carbon atoms. The workflow consists of: (i) constructing the initial unit cell from the reported lattice parameter and atomic fractional coordinates; (ii) fully relaxing the cell geometry and atomic positions; (iii) calculating the phonon dispersion to verify the absence of imaginary modes; (iv) computing the electronic band structure and extracting the indirect band gap and carrier effective masses at the band edges; (v) computing the three independent elastic stiffness constants (c11, c12, c44) via finite differences of the total energy under small strain distortions; and (vi) post-processing the elastic constants to obtain orientation-averaged bulk modulus, Young's modulus, shear modulus, and Poisson's ratio, and compiling all results into a single JSON file.

## Reproduction target
Using DFT, compute the equilibrium geometry of pentadiamond, then determine the following quantities and write them to `properties.json`: the elastic stiffness constants c11, c12, and c44 (in GPa); the orientation-averaged bulk modulus, Young's modulus, shear modulus, and Poisson's ratio; the indirect band gap (eV) and its type; the electron effective masses at the conduction band minimum and hole effective masses at the valence band maximum (in units of the free electron mass m_e); and a confirmation of dynamical stability (boolean) together with the maximum imaginary phonon frequency (cm⁻¹). The final answer is a single JSON file containing these values, derived from your own DFT calculations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Carbon PBE pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Structure setup
- Role: process
- Action: Prepare the initial pentadiamond crystal structure: cubic lattice, space group Fm-3m (No. 225), with lattice parameter approximately 9.195 Å. The fractional atomic coordinates are: C1 (0.250, 0.250, 0.250), C2 (0.152, 0.152, 0.152), C3 (0.198, 0.198, 0.000). Write the input files needed for the following DFT calculations.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform DFT structural relaxation of the pentadiamond unit cell using the PBE functional and a suitable carbon pseudopotential. Relax atomic positions and lattice parameter until forces fall below a convergence threshold. Save the relaxed structure and total energy.
- Evidence: `/app/outputs/relax.log`

### Step 3: Phonon dispersion calculation
- Role: process
- Action: Using the relaxed structure, compute phonon dispersion and density of states via density functional perturbation theory (DFPT). Check for the presence of any imaginary modes.
- Evidence: `/app/outputs/phonon.log`

### Step 4: Electronic structure calculation
- Role: process
- Action: Calculate the electronic band structure and density of states for the relaxed structure, using a suitable high-symmetry k-point path. From the band structure extract the indirect band gap (valence band maximum at L, conduction band minimum at X) and the carrier effective masses at those band edges by parabolic fitting.
- Evidence: `/app/outputs/bands.dat`

### Step 5: Elastic constant calculation
- Role: process
- Action: Compute the three independent elastic stiffness constants c11, c12, c44 for the cubic pentadiamond using finite differences of the total energy under small applied strain distortions.
- Evidence: `/app/outputs/elastic_constants.dat`

### Step 6: Compute and report all properties
- Role: scored (load-bearing)
- Action: From the DFT outputs obtained in steps S2–S5, derive the following quantities and write them to the JSON output file: bulk modulus B = (c11 + 2*c12)/3; the elastic compliances; the orientation-averaged Young's modulus and shear modulus using the standard cubic formulae; a representative Poisson's ratio; the indirect band gap and its type; electron and hole effective masses; and dynamical stability (absence of imaginary modes, with the maximum imaginary frequency). Store all results in the specified properties.json.
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: Object with keys: c11 (float, GPa), c12 (float, GPa), c44 (float, GPa), bulk_modulus (float, GPa), young_modulus (float, GPa), shear_modulus (float, GPa), poisson_ratio (float), band_gap (float, eV), band_gap_type (string, "indirect"), electron_eff_mass_1 (float, m_e), electron_eff_mass_2 (float, m_e), hole_eff_mass_1 (float, m_e), hole_eff_mass_2 (float, m_e), phonon_stable (boolean), max_imaginary_frequency (float, cm⁻¹, 0 if none).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate JSON file containing all reproduced properties (elastic constants, derived moduli, Poisson's ratio, band gap, effective masses, phonon stability). The checker compares each scalar field to hidden reference values from the paper.
- schema:
  - `type`: object
  - `required`:
    - `c11`: number (GPa)
    - `c12`: number (GPa)
    - `c44`: number (GPa)
    - `bulk_modulus`: number (GPa)
    - `young_modulus`: number (GPa)
    - `shear_modulus`: number (GPa)
    - `poisson_ratio`: number
    - `band_gap`: number (eV)
    - `band_gap_type`: string
    - `electron_eff_mass_1`: number (m_e)
    - `electron_eff_mass_2`: number (m_e)
    - `hole_eff_mass_1`: number (m_e)
    - `hole_eff_mass_2`: number (m_e)
    - `phonon_stable`: boolean
    - `max_imaginary_frequency`: number (cm⁻¹)
  - `units`:
    - `c11`: GPa
    - `c12`: GPa
    - `c44`: GPa
    - `bulk_modulus`: GPa
    - `young_modulus`: GPa
    - `shear_modulus`: GPa
    - `band_gap`: eV
    - `electron_eff_mass_1`: m_e
    - `electron_eff_mass_2`: m_e
    - `hole_eff_mass_1`: m_e
    - `hole_eff_mass_2`: m_e
    - `max_imaginary_frequency`: cm⁻¹

Notes: The verifier performs a result-level comparison (T0) of each field against toleranced paper-reported values. The solving agent must genuinely run DFT to produce these numbers; the dependency on all prior process steps makes the task load-bearing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c11": "number (GPa)",
          "c12": "number (GPa)",
          "c44": "number (GPa)",
          "bulk_modulus": "number (GPa)",
          "young_modulus": "number (GPa)",
          "shear_modulus": "number (GPa)",
          "poisson_ratio": "number",
          "band_gap": "number (eV)",
          "band_gap_type": "string",
          "electron_eff_mass_1": "number (m_e)",
          "electron_eff_mass_2": "number (m_e)",
          "hole_eff_mass_1": "number (m_e)",
          "hole_eff_mass_2": "number (m_e)",
          "phonon_stable": "boolean",
          "max_imaginary_frequency": "number (cm⁻¹)"
        },
        "units": {
          "c11": "GPa",
          "c12": "GPa",
          "c44": "GPa",
          "bulk_modulus": "GPa",
          "young_modulus": "GPa",
          "shear_modulus": "GPa",
          "band_gap": "eV",
          "electron_eff_mass_1": "m_e",
          "electron_eff_mass_2": "m_e",
          "hole_eff_mass_1": "m_e",
          "hole_eff_mass_2": "m_e",
          "max_imaginary_frequency": "cm⁻¹"
        }
      },
      "description": "Aggregate JSON file containing all reproduced properties (elastic constants, derived moduli, Poisson's ratio, band gap, effective masses, phonon stability). The checker compares each scalar field to hidden reference values from the paper."
    }
  ],
  "notes": "The verifier performs a result-level comparison (T0) of each field against toleranced paper-reported values. The solving agent must genuinely run DFT to produce these numbers; the dependency on all prior process steps makes the task load-bearing."
}
```

## How you are scored
A hidden verifier will read your `properties.json` and compare each reported quantity against expected reference values within defined tolerances. Each field contributes to the total score according to a preset weight; large deviations reduce the score. The verifier does not re-run any DFT calculations; it performs a result-level comparison of the submitted numbers against the reference. You are not required to match values from any external publication; the reward reflects how closely your computed results agree with the reference properties determined by the same methodology.
