# Stability and Mechanical Properties of Pentagonal BxNy Monolayers via DFT and Phonon Calculations

## Problem background
Pentagonal two-dimensional materials analogous to penta-graphene are of interest for their structural stability and mechanical/electronic properties. This task investigates pentagonal boron nitride (BₓNᵧ) monolayers, focusing on two candidate structures: B₂N₄-I and B₃N₃-I. The goal is to determine their dynamical stability via phonon calculations, characterize their mechanical response under uniaxial and biaxial tensile strain, and for the semiconducting B₃N₃-I, to explore how the band gap evolves with strain and whether a direct-to-indirect band gap transition occurs. The results are relevant for nanomechanical and optoelectronic applications.

## Approach
The approach uses density functional theory (DFT) with the PBE functional to model the monolayers. The workflow begins by building the two pentagonal unit cells (B₂N₄-I and B₃N₃-I) according to the pentagonal lattice with boron and nitrogen atoms occupying sp² and sp³ sites. Full geometry optimization relaxes atomic positions and lattice parameters. Phonon frequencies are then computed using the finite displacement method to assess dynamical stability. To evaluate mechanical properties, tensile strain increments are applied along the biaxial, x-axial, and y-axial directions while computing stress tensors; stress-strain curves yield the 2D Young’s modulus, intrinsic strength, and fracture strain. For B₃N₃-I, electronic band structures are calculated at equilibrium and at several strain levels to track the band gap and detect any direct-to-indirect transition. All computations are performed with open-source tools (Quantum ESPRESSO and Phonopy) using publicly available pseudopotentials.

## Reproduction target
Reproduce the dynamical stability, mechanical properties, and band gap behavior of pentagonal B₂N₄-I and B₃N₃-I by executing the workflow and submitting the required JSON files. The key outcomes to provide are:
- Optimized lattice parameters and total energies for both structures (structures_optimized.json).
- Dynamical stability verdicts and minimum phonon frequencies (phonon_stability.json).
- 2D Young’s moduli, intrinsic strengths, and fracture strains for both structures, and for B₃N₃-I additionally the band gap at zero strain and the critical uniaxial strain at which a direct-to-indirect band gap transition occurs (mechanical_and_band_gap.json).
All submitted values must be derived from your own DFT and phonon calculations; simply quoting numbers from the literature is not sufficient.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Phonopy: https://phonopy.github.io/phonopy/install.html
- PBE pseudopotentials for B and N: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct initial structures
- Role: process
- Action: Build initial unit cells for the two stable pentagonal BxNy configurations (B2N4-I and B3N3-I) following the pentagonal lattice description with boron and nitrogen atoms placed on sp2 and sp3 sites.
- Evidence: `/app/outputs/initial_structures.xyz`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform full geometry optimization for B2N4-I and B3N3-I using Quantum ESPRESSO with the PBE functional to relax atomic positions and lattice parameters until the forces and total energy are converged.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 3: Optimized structures and energies
- Role: scored (load-bearing)
- Action: Save the relaxed lattice vectors, fractional atomic coordinates with element labels, and total energy per unit cell for B2N4-I and B3N3-I.
- Output file: `/app/outputs/structures_optimized.json`
- Format: json
- Contract: JSON object with keys 'B2N4-I' and 'B3N3-I', each an object containing: 'lattice_vectors' (3x3 array of floats in Å), 'atomic_positions' (list of objects with keys 'element' (string), 'x' (float), 'y' (float), 'z' (float) in fractional coordinates), 'total_energy' (float in eV).
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion calculation
- Role: process
- Action: Compute phonon frequencies for the two relaxed structures using the finite displacement method (Phonopy) based on DFT forces, employing a supercell and a suitable q-point grid.
- Evidence: `/app/outputs/phonon_dispersion.pdf`

### Step 5: Phonon stability assessment
- Role: scored (load-bearing)
- Action: From the phonon dispersion, determine whether each structure is dynamically stable (no soft modes with imaginary frequencies beyond a small numerical tolerance) and record the minimum phonon frequency.
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: JSON object with keys 'B2N4-I' and 'B3N3-I', each containing: 'dynamically_stable' (boolean), 'min_phonon_frequency' (float in cm⁻¹).
- Scoring: scored by hidden verifier

### Step 6: Strain simulations and band structures
- Role: process
- Action: Apply uniaxial tensile strain along the X and Y directions and biaxial strain to both relaxed structures, performing DFT calculations at multiple strain increments to obtain stress tensors. For B3N3-I, also compute the electronic band structure at equilibrium and under several uniaxial strains up to fracture.
- Evidence: `/app/outputs/strain_data.tar.gz`

### Step 7: Mechanical and electronic properties
- Role: scored (load-bearing)
- Action: From the stress-strain curves, compute the 2D Young's modulus (N/m), intrinsic strength (GPa), and fracture strain (decimal) for each loading direction. For B3N3-I, determine the band gap (eV) at zero strain and the tensile strain at which the gap transitions from direct to indirect.
- Output file: `/app/outputs/mechanical_and_band_gap.json`
- Format: json
- Contract: JSON object with keys 'B2N4-I' and 'B3N3-I'. Each contains 'Young_modulus_2D' object with keys 'biaxial','x_axial','y_axial' (float, N/m), 'intrinsic_strength' object with same keys (float, GPa), 'fracture_strain' object with same keys (float, decimal). For 'B3N3-I' additionally include 'band_gap_zero_strain' (float, eV) and 'direct_indirect_transition_strain' (float, decimal).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structures_optimized.json`
- `/app/outputs/phonon_stability.json`
- `/app/outputs/mechanical_and_band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structures_optimized.json
- path: `/app/outputs/structures_optimized.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized geometries and total energies of B2N4-I and B3N3-I, compared to paper-reported reference values within tolerances.
- schema:
  - `type`: object
  - `required`: `B2N4-I`, `B3N3-I`
  - `properties`:
    - `B2N4-I`:
      - `type`: object
      - `required`: `lattice_vectors`, `atomic_positions`, `total_energy`
      - `lattice_vectors`: 3x3 array of floats (Å)
      - `atomic_positions`: list of objects with element (string) and x,y,z (float) in fractional coordinates
      - `total_energy`: float (eV)
    - `B3N3-I`:
      - `type`: object
      - `required`: `lattice_vectors`, `atomic_positions`, `total_energy`
      - `lattice_vectors`: 3x3 array of floats (Å)
      - `atomic_positions`: list of objects with element (string) and x,y,z (float) in fractional coordinates
      - `total_energy`: float (eV)

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Dynamical stability verdict and minimum phonon frequency; stability requires true and frequency > -0.5 cm⁻¹.
- schema:
  - `type`: object
  - `required`: `B2N4-I`, `B3N3-I`
  - `properties`:
    - `B2N4-I`:
      - `type`: object
      - `required`: `dynamically_stable`, `min_phonon_frequency`
      - `dynamically_stable`: boolean (true if no soft modes)
      - `min_phonon_frequency`: float (cm⁻¹, must be > -0.5 cm⁻¹)
    - `B3N3-I`:
      - `type`: object
      - `required`: `dynamically_stable`, `min_phonon_frequency`
      - `dynamically_stable`: boolean
      - `min_phonon_frequency`: float (cm⁻¹)

### mechanical_and_band_gap.json
- path: `/app/outputs/mechanical_and_band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mechanical properties and band gap evolution; compared to paper-reported values within tolerances.
- schema:
  - `type`: object
  - `required`: `B2N4-I`, `B3N3-I`
  - `B2N4-I`:
    - `type`: object
    - `required`: `Young_modulus_2D`, `intrinsic_strength`, `fracture_strain`
    - `Young_modulus_2D`: object with biaxial, x_axial, y_axial (float N/m)
    - `intrinsic_strength`: object with biaxial, x_axial, y_axial (float GPa)
    - `fracture_strain`: object with biaxial, x_axial, y_axial (float, decimal)
  - `B3N3-I`:
    - `type`: object
    - `required`: `Young_modulus_2D`, `intrinsic_strength`, `fracture_strain`, `band_gap_zero_strain`, `direct_indirect_transition_strain`
    - `Young_modulus_2D`: object (as above)
    - `intrinsic_strength`: object (as above)
    - `fracture_strain`: object (as above)
    - `band_gap_zero_strain`: float (eV)
    - `direct_indirect_transition_strain`: float (decimal, critical uniaxial strain)

Notes: The checker will compare lattice constants, bond lengths, and total energy from structures_optimized.json to paper reference values within tolerances. For phonon_stability.json, it checks that dynamically_stable is true and min_phonon_frequency > -0.5 cm⁻¹. For mechanical_and_band_gap.json, 2D Young's moduli, intrinsic strengths, fracture strains, and band gaps are compared within tolerances; the direct-to-indirect transition strain must lie between 4% and 6%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structures_optimized.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "B2N4-I",
          "B3N3-I"
        ],
        "properties": {
          "B2N4-I": {
            "type": "object",
            "required": [
              "lattice_vectors",
              "atomic_positions",
              "total_energy"
            ],
            "lattice_vectors": "3x3 array of floats (Å)",
            "atomic_positions": "list of objects with element (string) and x,y,z (float) in fractional coordinates",
            "total_energy": "float (eV)"
          },
          "B3N3-I": {
            "type": "object",
            "required": [
              "lattice_vectors",
              "atomic_positions",
              "total_energy"
            ],
            "lattice_vectors": "3x3 array of floats (Å)",
            "atomic_positions": "list of objects with element (string) and x,y,z (float) in fractional coordinates",
            "total_energy": "float (eV)"
          }
        }
      },
      "description": "Optimized geometries and total energies of B2N4-I and B3N3-I, compared to paper-reported reference values within tolerances."
    },
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "B2N4-I",
          "B3N3-I"
        ],
        "properties": {
          "B2N4-I": {
            "type": "object",
            "required": [
              "dynamically_stable",
              "min_phonon_frequency"
            ],
            "dynamically_stable": "boolean (true if no soft modes)",
            "min_phonon_frequency": "float (cm⁻¹, must be > -0.5 cm⁻¹)"
          },
          "B3N3-I": {
            "type": "object",
            "required": [
              "dynamically_stable",
              "min_phonon_frequency"
            ],
            "dynamically_stable": "boolean",
            "min_phonon_frequency": "float (cm⁻¹)"
          }
        }
      },
      "description": "Dynamical stability verdict and minimum phonon frequency; stability requires true and frequency > -0.5 cm⁻¹."
    },
    {
      "file": "mechanical_and_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "B2N4-I",
          "B3N3-I"
        ],
        "B2N4-I": {
          "type": "object",
          "required": [
            "Young_modulus_2D",
            "intrinsic_strength",
            "fracture_strain"
          ],
          "Young_modulus_2D": "object with biaxial, x_axial, y_axial (float N/m)",
          "intrinsic_strength": "object with biaxial, x_axial, y_axial (float GPa)",
          "fracture_strain": "object with biaxial, x_axial, y_axial (float, decimal)"
        },
        "B3N3-I": {
          "type": "object",
          "required": [
            "Young_modulus_2D",
            "intrinsic_strength",
            "fracture_strain",
            "band_gap_zero_strain",
            "direct_indirect_transition_strain"
          ],
          "Young_modulus_2D": "object (as above)",
          "intrinsic_strength": "object (as above)",
          "fracture_strain": "object (as above)",
          "band_gap_zero_strain": "float (eV)",
          "direct_indirect_transition_strain": "float (decimal, critical uniaxial strain)"
        }
      },
      "description": "Mechanical properties and band gap evolution; compared to paper-reported values within tolerances."
    }
  ],
  "notes": "The checker will compare lattice constants, bond lengths, and total energy from structures_optimized.json to paper reference values within tolerances. For phonon_stability.json, it checks that dynamically_stable is true and min_phonon_frequency > -0.5 cm⁻¹. For mechanical_and_band_gap.json, 2D Young's moduli, intrinsic strengths, fracture strains, and band gaps are compared within tolerances; the direct-to-indirect transition strain must lie between 4% and 6%."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted output files. Each load-bearing artifact (structures_optimized.json, phonon_stability.json, mechanical_and_band_gap.json) is scored separately against hidden reference criteria. The verifier checks that the geometries and energies are consistent with a correct DFT optimization, that the phonon analysis correctly identifies dynamical stability, and that the extracted mechanical properties and band gap values are physically reasonable and lie within expected tolerances derived from the method. The final reward is a weighted combination of these per-artifact scores. Providing only the paper's reported numbers is insufficient; you must actually execute the computational workflow and generate the artifacts from your own calculations.
