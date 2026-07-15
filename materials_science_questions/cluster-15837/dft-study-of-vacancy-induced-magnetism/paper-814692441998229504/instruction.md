# DFT study of vacancy-induced magnetism in graphene/h-BN bilayer

## Problem background
Two-dimensional heterostructures composed of graphene and hexagonal boron nitride (h-BN) offer tunable electronic properties through interlayer interactions and sublattice-symmetry breaking. Introducing point defects—vacancies, substitutional dopants, or their combinations—can further modify the electronic structure and give rise to localized magnetic moments. Understanding how specific defect configurations influence magnetism and spin-dependent conduction is important for designing half-metallic materials for spintronics. This task investigates four defect configurations in a graphene/h-BN bilayer: a boron vacancy in the h-BN layer, a carbon vacancy in the graphene layer, and two combined substitution+vacancy cases (carbon substituting a boron site plus a carbon vacancy, and carbon substituting a nitrogen site plus a carbon vacancy). The goal is to compute the induced total magnetic moments, the band gaps for majority and minority spin channels, and the spin polarization at the Fermi level for each system, and thereby assess whether the configurations exhibit half-metallic or asymmetric semiconducting character.

## Approach
Density functional theory (DFT) calculations with spin polarization are used to model the graphene/h-BN bilayer in a periodic supercell containing one of the four defect configurations. Starting from the known pristine structures, atomic models are first constructed and the geometry is optimized by minimizing forces, including van der Waals corrections to capture interlayer cohesion and a dipole correction to eliminate spurious fields from the slab geometry. After relaxation, self-consistent field calculations are performed to obtain the electronic ground state and total magnetic moment. Subsequently, band structure and density-of-states calculations yield the band gaps for majority and minority spin channels and the spin polarization P(Ef) at the Fermi level. The procedure employs an open-source plane-wave DFT code with standard pseudopotentials for B, C, and N atoms (for example from the SSSP library) and the local density approximation (LDA) for exchange-correlation, consistent with established practice for these layered heterostructures. The central comparison is between the four defect configurations to reveal how each type of defect modifies the magnetic and electronic properties relative to one another.

## Reproduction target
For each of the four defect configurations—B15N16/C32 (B vacancy), B16N16/C31 (C vacancy), B15CN16/C31 (combination of C substitution at B site and C vacancy), and B16N15C/C31 (combination of C substitution at N site and C vacancy)—compute and report the following quantities: total magnetic moment (in μB), band gap for majority spin (in eV), band gap for minority spin (in eV), and spin polarization P(Ef) at the Fermi level (as a percentage). Write these results into a JSON file following the specified schema. The computed values should establish whether the B15CN16/C31 configuration exhibits near 100% spin polarization (half-metallic character) and whether the B16N15C/C31 configuration is an asymmetric semiconductor with both spin gap channels open and the majority-spin gap smaller than the minority-spin gap.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Model construction and input preparation
- Role: process
- Action: Construct 4x4 supercells for the four defect configurations (B15N16/C32, B16N16/C31, B15CN16/C31, B16N15C/C31) in the graphene/h-BN bilayer. Prepare Quantum ESPRESSO input files with appropriate pseudopotentials and parameters.
- Evidence: `/app/outputs/supercells.tar.gz`

### Step 2: Spin-polarized DFT relaxation and electronic structure calculations
- Role: process
- Action: For each defect configuration, run spin-polarized DFT using Quantum ESPRESSO with appropriate functional, van der Waals correction, and dipole correction. Perform structural relaxation, then self-consistent calculation, followed by band structure and density of states calculations to obtain the required properties.
- Evidence: `/app/outputs/dft_outputs.tar.gz`

### Step 3: Extract magnetic and electronic results
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract the total magnetic moment (μB), band gaps for majority and minority spin (eV), and spin polarization P(Ef) (%) for each configuration. Write a JSON file containing an array of objects with the specified schema.
- Output file: `/app/outputs/magnetic_and_electronic_results.json`
- Format: json
- Contract: Array of objects, each with fields: configuration (string), total_magnetic_moment_muB (float), majority_band_gap_eV (float), minority_band_gap_eV (float), spin_polarization_percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_and_electronic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_and_electronic_results.json
- path: `/app/outputs/magnetic_and_electronic_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Array of objects for the four defect configurations, each containing the computed total magnetic moment, majority/minority spin band gaps, and spin polarization.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `configuration`, `total_magnetic_moment_muB`, `majority_band_gap_eV`, `minority_band_gap_eV`, `spin_polarization_percent`
    - `properties`:
      - `configuration`:
        - `type`: string
        - `description`: Defect configuration label, e.g. B15N16/C32, B16N16/C31, B15CN16/C31, B16N15C/C31
      - `total_magnetic_moment_muB`:
        - `type`: number
        - `description`: Total magnetic moment in μB
      - `majority_band_gap_eV`:
        - `type`: number
        - `description`: Band gap for majority spin in eV
      - `minority_band_gap_eV`:
        - `type`: number
        - `description`: Band gap for minority spin in eV
      - `spin_polarization_percent`:
        - `type`: number
        - `description`: Spin polarization at Fermi level P(Ef) in percent

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_and_electronic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "configuration",
            "total_magnetic_moment_muB",
            "majority_band_gap_eV",
            "minority_band_gap_eV",
            "spin_polarization_percent"
          ],
          "properties": {
            "configuration": {
              "type": "string",
              "description": "Defect configuration label, e.g. B15N16/C32, B16N16/C31, B15CN16/C31, B16N15C/C31"
            },
            "total_magnetic_moment_muB": {
              "type": "number",
              "description": "Total magnetic moment in μB"
            },
            "majority_band_gap_eV": {
              "type": "number",
              "description": "Band gap for majority spin in eV"
            },
            "minority_band_gap_eV": {
              "type": "number",
              "description": "Band gap for minority spin in eV"
            },
            "spin_polarization_percent": {
              "type": "number",
              "description": "Spin polarization at Fermi level P(Ef) in percent"
            }
          }
        }
      },
      "description": "Array of objects for the four defect configurations, each containing the computed total magnetic moment, majority/minority spin band gaps, and spin polarization."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier checks the final JSON output and — where applicable — inspects the intermediate process evidence (supercell archives, DFT raw outputs) for completeness. The primary scoring comes from your reported magnetic moments, band gaps, and spin polarization. For each configuration, the verifier compares the computed total magnetic moment to a reference value obtained from independent DFT calculations using the same exchange-correlation functional, within tolerances that account for differences between DFT codes and pseudopotentials (honest, well-converged calculations pass; grossly wrong results do not). Additionally, two structural conditions are enforced: for B15CN16/C31 the spin polarization must exceed a predetermined threshold consistent with half-metallicity; for B16N15C/C31 both band gaps must be positive and the majority band gap must be strictly smaller than the minority band gap. The reward is a weighted sum: each magnetic moment contributes to the score, the half-metallic and asymmetric-semiconductor checks provide additional weight, and the overall JSON schema compliance carries a small verification weight. You do not need to match any reference value exactly — meeting the physical trends and staying within tolerance is sufficient.
