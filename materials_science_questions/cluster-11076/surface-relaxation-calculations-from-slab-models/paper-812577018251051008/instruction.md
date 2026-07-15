# DFT surface relaxation and half-metallicity of Heusler alloy Zr2VGa

## Problem background
Full-Heusler alloys of the form X2YZ are promising candidates for spintronic devices because they can be half-metallic ferromagnets: one spin channel behaves as a metal while the other is semiconducting at the Fermi level, enabling 100% spin polarization. Zr2VGa, with CuHg2Ti-type structure (space group F-43m), has attracted interest as a potential half-metallic ferromagnet. For practical spintronic applications in thin-film or multilayer form, it is essential to understand whether the half-metallic property survives at surfaces. This task addresses the electronic structure and magnetic properties of the (111), (001), and (110) surfaces of Zr2VGa.

## Approach
Spin-polarized density-functional theory (DFT) calculations are performed using the generalized gradient approximation (GGA-PBE) with an open-source plane-wave pseudopotential code. The equilibrium lattice constant is found by fitting total energies from a series of volume scans. At this constant, the bulk density of states is computed to extract the majority-spin band gap, total spin magnetic moment, and site-resolved atomic magnetic moments. Symmetric slab models with sufficient vacuum are built for all seven possible surface terminations of the (111), (001), and (110) planes; the atoms in the upper layers are relaxed while the bottom layers are fixed. The resulting interlayer relaxation displacements and atomic magnetic moments at the surface and subsurface layers are calculated, and the presence or absence of a half-metallic gap at each termination is evaluated.

## Reproduction target
Determine the equilibrium lattice constant of bulk Zr2VGa using an open-source DFT code. At that lattice constant, compute the majority-spin band gap at the Fermi level, the total spin magnetic moment per formula unit, and the site-resolved magnetic moments for Zr(1), Zr(2), V, and Ga. Build slab models for all seven surface terminations: Zr(1)-, Zr(2)-, V-, and Ga-terminated (111); Zr(1)V- and Zr(2)Ga-terminated (001); Zr(1)Zr(2)VGa-terminated (110). After relaxing the upper layers of each slab, extract the interlayer spacing displacements for the surface–subsurface atom pairs and the atomic magnetic moments at the surface and subsurface layers. For every termination, determine whether the half-metallic gap persists or is destroyed.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build bulk crystal structure
- Role: process
- Action: Construct the unit cell for bulk Zr2VGa in the CuHg2Ti-type structure (space group F-43m) with atomic positions Zr(1) (0,0,0), Zr(2) (0.25,0.25,0.25), V (0.5,0.5,0.5), Ga (0.75,0.75,0.75).
- Evidence: none

### Step 2: Determine equilibrium lattice parameter
- Role: process
- Action: Perform spin-polarized DFT-GGA energy-volume scans on the bulk Zr2VGa cell to locate the minimum total energy, determining the equilibrium lattice constant.
- Evidence: none

### Step 3: Compute bulk electronic and magnetic properties
- Role: scored
- Action: At the equilibrium lattice constant from step_02, run a self-consistent field calculation (spin-polarized) followed by a non-self-consistent density-of-states calculation. Extract the majority-spin band gap at the Fermi level, the total spin magnetic moment, and the atomic magnetic moments for Zr(1), Zr(2), V, and Ga. Save these values to bulk_properties.json.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: JSON object with keys: equilibrium_lattice_constant_A (float), bulk_band_gap_majority_eV (float), total_magnetic_moment_mu_B (float), atomic_magnetic_moments (object with keys Zr1, Zr2, V, Ga as floats).
- Scoring: scored by hidden verifier

### Step 4: Construct surface slab models
- Role: process
- Action: Build symmetric slab models for all seven surface terminations (Zr(1)-, Zr(2)-, V-, Ga-terminated (111); Zr(1)V- and Zr(2)Ga-terminated (001); Zr(1)Zr(2)VGa-terminated (110)). Use the equilibrium lattice constant from step_02, the layer counts specified in the paper (19 layers for (111), 13 for (001), 9 for (110)), and add at least 15 Å vacuum on both sides. Slab geometries must reflect the paper’s description of layer composition (one atom per layer for (111), two atoms per layer for (001), four atoms per layer for (110)).
- Evidence: none

### Step 5: Relax surfaces and compute relaxation/displacement and magnetic properties
- Role: scored (load-bearing)
- Action: For each slab from step_04, fix the bottom layers and relax the top four atomic layers using spin-polarized DFT. After relaxation, compute the interlayer spacing displacements (ΔZ in Å) for the surface–subsurface atom pairs specified in the paper’s Table 1, and the atomic magnetic moments (in μ_B) for surface and subsurface atoms as listed in Table 2. Verify that no spin channel displays a band gap at the Fermi level for any termination (i.e., half-metallicity is destroyed). Write all results, keyed by termination, to surface_results.json.
- Output file: `/app/outputs/surface_results.json`
- Format: json
- Contract: JSON object keyed by termination string (e.g., 'Zr1_ter_111', 'Zr2_ter_111', 'V_ter_111', 'Ga_ter_111', 'Zr1V_ter_001', 'Zr2Ga_ter_001', 'Zr1Zr2VGa_110'). Each value is an object with: relaxation_displacements_A (list of floats, interlayer displacement values as in Table 1), atomic_magnetic_moments_mu_B (list of floats for surface and subsurface atoms), half_metallic (boolean, must be false for all).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/surface_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bulk half-metallic properties of Zr2VGa: equilibrium lattice constant, majority-spin band gap, total and atomic magnetic moments. The hidden checker compares the numeric values to the paper’s reported results with tolerances that absorb code/functional differences (equilibrium lattice constant ±0.01 Å, band gap ±0.05 eV, total moment ±0.05 μ_B, atomic moments ±0.1 μ_B).
- schema:
  - `type`: object
  - `properties`:
    - `equilibrium_lattice_constant_A`:
      - `type`: number
    - `bulk_band_gap_majority_eV`:
      - `type`: number
    - `total_magnetic_moment_mu_B`:
      - `type`: number
    - `atomic_magnetic_moments`:
      - `type`: object
      - `properties`:
        - `Zr1`:
          - `type`: number
        - `Zr2`:
          - `type`: number
        - `V`:
          - `type`: number
        - `Ga`:
          - `type`: number

### surface_results.json
- path: `/app/outputs/surface_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Surface relaxation displacements and magnetic moments for all seven terminations, plus half-metallic destruction confirmation. The hidden checker compares relaxation_displacements_A elements to Table 1 within ±0.05 Å, atomic_magnetic_moments_mu_B list elements to Table 2 within ±0.1 μ_B, and verifies half_metallic is false for every termination.
- schema:
  - `type`: object
  - `additionalProperties`:
    - `type`: object
    - `properties`:
      - `relaxation_displacements_A`:
        - `type`: array
        - `items`:
          - `type`: number
      - `atomic_magnetic_moments_mu_B`:
        - `type`: array
        - `items`:
          - `type`: number
      - `half_metallic`:
        - `type`: boolean

Notes: The original paper used the proprietary WIEN2k code; the task is rescoped to open-source Quantum ESPRESSO with GGA-PBE pseudopotentials (e.g., SSSP efficiency set). Tolerances account for differences between FLAPW and plane-wave pseudopotential methods. All slab construction parameters (layer counts, vacuum) and relaxation details follow the paper's description. No hidden gold values or tolerances are disclosed in this public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "equilibrium_lattice_constant_A": {
            "type": "number"
          },
          "bulk_band_gap_majority_eV": {
            "type": "number"
          },
          "total_magnetic_moment_mu_B": {
            "type": "number"
          },
          "atomic_magnetic_moments": {
            "type": "object",
            "properties": {
              "Zr1": {
                "type": "number"
              },
              "Zr2": {
                "type": "number"
              },
              "V": {
                "type": "number"
              },
              "Ga": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Bulk half-metallic properties of Zr2VGa: equilibrium lattice constant, majority-spin band gap, total and atomic magnetic moments. The hidden checker compares the numeric values to the paper’s reported results with tolerances that absorb code/functional differences (equilibrium lattice constant ±0.01 Å, band gap ±0.05 eV, total moment ±0.05 μ_B, atomic moments ±0.1 μ_B)."
    },
    {
      "file": "surface_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "properties": {
            "relaxation_displacements_A": {
              "type": "array",
              "items": {
                "type": "number"
              }
            },
            "atomic_magnetic_moments_mu_B": {
              "type": "array",
              "items": {
                "type": "number"
              }
            },
            "half_metallic": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Surface relaxation displacements and magnetic moments for all seven terminations, plus half-metallic destruction confirmation. The hidden checker compares relaxation_displacements_A elements to Table 1 within ±0.05 Å, atomic_magnetic_moments_mu_B list elements to Table 2 within ±0.1 μ_B, and verifies half_metallic is false for every termination."
    }
  ],
  "notes": "The original paper used the proprietary WIEN2k code; the task is rescoped to open-source Quantum ESPRESSO with GGA-PBE pseudopotentials (e.g., SSSP efficiency set). Tolerances account for differences between FLAPW and plane-wave pseudopotential methods. All slab construction parameters (layer counts, vacuum) and relaxation details follow the paper's description. No hidden gold values or tolerances are disclosed in this public contract."
}
```

## How you are scored
A hidden verifier independently evaluates the two scored output files. It compares the equilibrium lattice constant, band gap, magnetic moments, relaxation displacements, and the presence/absence of a half-metallic gap at each termination against reference values and criteria. The comparisons use predefined tolerances that account for differences between the code used in the original study and the open-source code you employ. Each scored stage contributes a weighted sub-score, and the final reward is the weighted sum. The verifier does not require you to match specific tolerance values; you must only follow the output schema faithfully. Reporting numbers without executing the real DFT pipeline will not pass the verifier.
