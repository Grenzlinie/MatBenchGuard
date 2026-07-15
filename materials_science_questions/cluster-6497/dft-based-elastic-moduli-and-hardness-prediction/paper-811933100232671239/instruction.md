# DFT-based structural, elastic, and electronic property prediction for cubic CaZrO3

## Problem background
Calcium zirconate (CaZrO₃) is a perovskite ceramic with high melting point, chemical stability, and ionic conductivity, making it attractive for capacitors, sensors, refractory applications, and gate dielectrics. Its cubic phase is stable at high temperature. First-principles prediction of its ground-state structural parameters, elastic constants, and electronic band gap provides fundamental data to guide materials design and compare with experiments. This task reproduces those predictions using density functional theory (DFT).

## Approach
The calculations use plane-wave pseudopotential DFT within the generalized gradient approximation (GGA‑PBE). The open‑source code Quantum ESPRESSO is employed with ultrasoft pseudopotentials for Ca, Zr, and O. The workflow proceeds in three stages: (1) total‑energy calculations for the cubic perovskite unit cell at a set of volumes, followed by fitting the energy–volume data to the Murnaghan equation of state to extract equilibrium properties (lattice constant, bulk modulus, etc.); (2) applying small strains to the equilibrium lattice and computing the stress tensor to obtain the independent single‑crystal elastic constants c₁₁, c₁₂, c₄₄, from which polycrystalline moduli (bulk, shear, Young) are derived via Voigt–Reuss–Hill averaging; (3) computing the Kohn–Sham band structure and density of states for the equilibrium structure to determine the fundamental band gap and its nature (direct or indirect). Each stage builds on the previous one and the final numerical values are written to designated JSON output files.

## Reproduction target
Produce the following quantities for cubic CaZrO₃: (i) equilibrium lattice constant, volume per formula unit, cohesive energy, bulk modulus and its pressure derivative from Murnaghan equation‑of‑state fitting; (ii) single‑crystal elastic constants c₁₁, c₁₂, c₄₄ and the derived polycrystalline bulk, shear and Young’s moduli; (iii) the fundamental electronic band gap value and whether it is direct or indirect. All values must be obtained from DFT calculations as described in the workflow steps and reflect the computational parameters you choose within the specified theoretical framework.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Ca, Zr, O from QE pseudopotential library: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT total-energy vs volume calculations
- Role: process
- Action: Perform DFT total-energy calculations for cubic CaZrO3 at a range of volumes using GGA-PBE with ultrasoft pseudopotentials. Record total energy for each volume.
- Evidence: `/app/outputs/e_v_data.csv`

### Step 2: Murnaghan EoS fitting and ground-state properties
- Role: scored (load-bearing)
- Action: Fit total energy vs volume data to the Murnaghan equation of state. Extract equilibrium lattice constant a (Å), equilibrium volume per formula unit V0 (Å³), cohesive energy E_coh (eV), bulk modulus B (GPa), and its pressure derivative B'.
- Output file: `/app/outputs/step01_eos_properties.json`
- Format: json
- Contract: { "a_angstrom": float, "V0_angstrom3_per_fu": float, "E_coh_eV": float, "B_GPa": float, "B_prime": float }
- Scoring: scored by hidden verifier

### Step 3: Strain-stress DFT calculations for elastic constants
- Role: process
- Action: Apply small strains to the equilibrium cubic lattice and compute the resulting stress tensor using DFT with the same pseudopotential and cutoff settings. Extract the three independent elastic constants c11, c12, c44.
- Evidence: none

### Step 4: Elastic constants and polycrystalline moduli
- Role: scored
- Action: From the single-crystal elastic constants c11, c12, c44, compute the polycrystalline bulk modulus B_el (GPa), shear modulus G (GPa) via Voigt-Reuss-Hill averaging, and Young's modulus E (GPa). Report all quantities.
- Output file: `/app/outputs/step02_elastic_moduli.json`
- Format: json
- Contract: { "c11_GPa": float, "c12_GPa": float, "c44_GPa": float, "B_el_GPa": float, "G_GPa": float, "E_GPa": float }
- Scoring: scored by hidden verifier

### Step 5: Electronic band structure and DOS calculation
- Role: process
- Action: Using the equilibrium structure, compute the Kohn-Sham band structure along high-symmetry lines and the total/partial density of states with a dense k-point grid. Determine the fundamental band gap and its nature.
- Evidence: none

### Step 6: Band gap extraction
- Role: scored
- Action: From the computed band structure, identify the valence band maximum and conduction band minimum. Extract the fundamental band gap value (eV) and whether it is direct or indirect.
- Output file: `/app/outputs/step03_band_gap.json`
- Format: json
- Contract: { "band_gap_eV": float, "band_gap_type": string }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step01_eos_properties.json`
- `/app/outputs/step02_elastic_moduli.json`
- `/app/outputs/step03_band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step01_eos_properties.json
- path: `/app/outputs/step01_eos_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium structural and equation-of-state parameters from Murnaghan fit, compared to hidden paper-reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `a_angstrom`: float
    - `V0_angstrom3_per_fu`: float
    - `E_coh_eV`: float
    - `B_GPa`: float
    - `B_prime`: float
  - `units`:
    - `a_angstrom`: Å
    - `V0_angstrom3_per_fu`: Å³
    - `E_coh_eV`: eV
    - `B_GPa`: GPa
    - `B_prime`: dimensionless

### step02_elastic_moduli.json
- path: `/app/outputs/step02_elastic_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single-crystal elastic constants and derived polycrystalline moduli, compared to hidden paper-reported values with relative tolerance and internal consistency check.
- schema:
  - `type`: object
  - `required`:
    - `c11_GPa`: float
    - `c12_GPa`: float
    - `c44_GPa`: float
    - `B_el_GPa`: float
    - `G_GPa`: float
    - `E_GPa`: float
  - `units`:
    - `c11_GPa`: GPa
    - `c12_GPa`: GPa
    - `c44_GPa`: GPa
    - `B_el_GPa`: GPa
    - `G_GPa`: GPa
    - `E_GPa`: GPa

### step03_band_gap.json
- path: `/app/outputs/step03_band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fundamental band gap value and type (direct/indirect), compared to hidden paper-reported value and exact string for gap type with tight tolerance.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: float
    - `band_gap_type`: string
  - `units`:
    - `band_gap_eV`: eV

Notes: The single-crystal elastic constants and band gap are derived from DFT strain-stress and band structure calculations, respectively. These are computation-dependent quantities; the hidden checker compares to paper values with tolerances that absorb legitimate toolchain spread. The charge density and bonding analysis (Fig. 3) is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step01_eos_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "a_angstrom": "float",
          "V0_angstrom3_per_fu": "float",
          "E_coh_eV": "float",
          "B_GPa": "float",
          "B_prime": "float"
        },
        "units": {
          "a_angstrom": "Å",
          "V0_angstrom3_per_fu": "Å³",
          "E_coh_eV": "eV",
          "B_GPa": "GPa",
          "B_prime": "dimensionless"
        }
      },
      "description": "Equilibrium structural and equation-of-state parameters from Murnaghan fit, compared to hidden paper-reported values with appropriate tolerances."
    },
    {
      "file": "step02_elastic_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c11_GPa": "float",
          "c12_GPa": "float",
          "c44_GPa": "float",
          "B_el_GPa": "float",
          "G_GPa": "float",
          "E_GPa": "float"
        },
        "units": {
          "c11_GPa": "GPa",
          "c12_GPa": "GPa",
          "c44_GPa": "GPa",
          "B_el_GPa": "GPa",
          "G_GPa": "GPa",
          "E_GPa": "GPa"
        }
      },
      "description": "Single-crystal elastic constants and derived polycrystalline moduli, compared to hidden paper-reported values with relative tolerance and internal consistency check."
    },
    {
      "file": "step03_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "float",
          "band_gap_type": "string"
        },
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Fundamental band gap value and type (direct/indirect), compared to hidden paper-reported value and exact string for gap type with tight tolerance."
    }
  ],
  "notes": "The single-crystal elastic constants and band gap are derived from DFT strain-stress and band structure calculations, respectively. These are computation-dependent quantities; the hidden checker compares to paper values with tolerances that absorb legitimate toolchain spread. The charge density and bonding analysis (Fig. 3) is not required."
}
```

## How you are scored
A hidden verifier scores each workflow artifact independently by comparing your submitted values to the paper’s reported reference results, using appropriate tolerances that account for the spread of independent DFT re‑runs with different implementations. The artifacts `step01_eos_properties.json`, `step02_elastic_moduli.json`, and `step03_band_gap.json` each carry a weight, and the final reward is the weighted sum of those scores. Your job is to perform a faithful DFT reproduction; reporting numbers without the underlying calculation will not receive credit.
