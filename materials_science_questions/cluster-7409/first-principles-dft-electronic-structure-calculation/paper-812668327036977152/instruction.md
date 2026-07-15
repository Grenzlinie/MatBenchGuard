# DFT+U calculation of local lattice relaxation, magnetic moment and defect formation energies of Gd-substituted CeO₂

## Problem background
Gd-doped CeO₂ is a technologically important material for solid oxide fuel cells, catalysis, and oxygen storage. The interplay between Gd substitutions and oxygen vacancies determines the material's electronic structure, ionic conductivity, and defect chemistry. Understanding whether a single Gd substitution induces hole states, how it affects local lattice relaxation and spin polarization, and how Gd atoms interact with oxygen vacancies to form stable dopant-defect complexes is essential for optimizing material performance. This task computes the structural, magnetic, and energetic consequences of Gd doping in CeO₂ using first-principles DFT+U calculations.

## Approach
The approach employs spin-polarized DFT+U calculations with the PBE functional and a Hubbard U correction on the 4f electrons of Ce and Gd. Three dopant configurations are compared within a 2×2×2 CeO₂ supercell: (i) a single Gd substitution for Ce (Ce₃₁GdO₆₄), (ii) a Gd–oxygen vacancy pair with the vacancy at the nearest-neighbor position (Ce₃₁GdO₆₃), and (iii) a Gd-V_O-Gd cluster with two Gd atoms both at nearest-neighbor sites to the same oxygen vacancy (Ce₃₀Gd₂O₆₃). For each configuration, the total energy, relaxed geometry, total magnetic moment, and electronic structure (Fermi level position) are obtained. Reference bulk formation energies of CeO₂, Ce₂O₃, and Gd₂O₃ are also computed with the same functional. These allow chemical potentials to be determined under O-rich and O-poor conditions, from which the formation energies of the three defect configurations are derived using the standard supercell approach. The relative stability of the three configurations is assessed by comparing their formation energies across the two oxygen chemical potential regimes.

## Reproduction target
For the single Gd substitution (Ce₃₁GdO₆₄), compute: the average outward displacement of the eight nearest oxygen atoms and twelve nearest cerium atoms relative to the pristine supercell; the total magnetic moment of the supercell; and whether the Fermi level lies inside the band gap. For all three defect configurations (Gd, Gd-V_O, Gd-V_O-Gd), compute their formation energies under O-rich (Δμ_O = 0) and O-poor (CeO₂ in equilibrium with Ce₂O₃) conditions. Finally, determine the most thermodynamically stable configuration among the three under each set of conditions. All results are recorded in `/app/outputs/results.json` according to the specified schema.

## Assets

- DFT code (VASP or Quantum ESPRESSO): https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials for Ce, O, Gd: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax pristine CeO₂ supercell
- Role: process
- Action: Construct a 2×2×2 CeO₂ supercell (96 atoms) from the fluorite structure with lattice constant 5.49 Å. Perform a spin-polarized DFT+U relaxation using PBE functional, U_eff=5 eV on Ce 4f, plane-wave cutoff 500 eV, and 2×2×2 k-point mesh. Obtain the relaxed atomic positions and total energy.
- Evidence: none

### Step 2: Relax single Gd substitution Ce₃₁GdO₆₄
- Role: process
- Action: Substitute one Ce atom in the 2×2×2 supercell with a Gd atom to form Ce₃₁GdO₆₄. Relax the structure using the same DFT+U settings (PBE, U_eff=5 eV on both Ce and Gd 4f, cutoff 500 eV, 2×2×2 k-points). After relaxation, extract the total energy, total magnetic moment, and determine from the electronic structure whether the Fermi level lies inside the band gap. Record atomic positions.
- Evidence: none

### Step 3: Relax Gd-V_O and Gd-V_O-Gd defect complexes
- Role: process
- Action: Construct and relax the Gd–oxygen vacancy pair (V_O at 1NN to Gd, Ce₃₁GdO₆₃) and the Gd-V_O-Gd cluster (two Gd atoms both at 1NN to the same V_O, Ce₃₀Gd₂O₆₃) with identical DFT+U settings. Obtain the total energies E(Gd-V_O) and E(Gd-V_O-Gd).
- Evidence: none

### Step 4: Compute reference bulk formation energies of CeO₂, Ce₂O₃, Gd₂O₃
- Role: process
- Action: Using the same DFT+U functional, compute total energies of bulk cubic CeO₂, hexagonal Ce₂O₃, and C-type Gd₂O₃. From these and elemental reference energies derive chemical potentials μ_O, μ_Ce, μ_Gd under O-rich (Δμ_O=0) and O-poor conditions following the constraints: Δμ_Ce + 2Δμ_O = E_f(CeO₂), 2Δμ_Ce + 3Δμ_O = E_f(Ce₂O₃), and 2Δμ_Gd + 3Δμ_O = E_f(Gd₂O₃).
- Evidence: none

### Step 5: Compile and write scored results
- Role: scored (load-bearing)
- Action: Using the outputs of steps 01–04, compute: (i) average displacement of the eight nearest O and twelve nearest Ce in Ce₃₁GdO₆₄ relative to pristine CeO₂; (ii) total magnetic moment of Ce₃₁GdO₆₄; (iii) a boolean `fermi_level_in_gap` determined from the relaxed single‑Gd supercell; (iv) formation energies of Gd, Gd-V_O, and Gd-V_O-Gd under O-rich and O-poor conditions using the standard formula ΔE_f = E(defect) + Σ n_i μ_i − E(CeO₂) with the chemical potentials from step 04. Write all results into `results.json`.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "single_gd_O_displacement": <float, Å>,
  "single_gd_Ce_displacement": <float, Å>,
  "single_gd_magnetic_moment": <float, μ_B>,
  "fermi_level_in_gap": <bool>,
  "formation_energies": {
    "O-rich": { "Gd": <float, eV>, "Gd_V_O": <float, eV>, "Gd_V_O_Gd": <float, eV> },
    "O-poor": { "Gd": <float, eV>, "Gd_V_O": <float, eV>, "Gd_V_O_Gd": <float, eV> }
  },
  "ordering": <string> // e.g. "Gd-V_O-Gd is most stable under O-rich and O-poor"
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains all scored physical quantities: atomic displacements, magnetic moment, Fermi level position, formation energies under two oxygen chemical potential conditions, and the stability ordering of defect complexes.
- schema:
  - `type`: object
  - `required`:
    - `single_gd_O_displacement`: float (Å)
    - `single_gd_Ce_displacement`: float (Å)
    - `single_gd_magnetic_moment`: float (μ_B)
    - `fermi_level_in_gap`: boolean
    - `formation_energies`:
      - `type`: object
      - `properties`:
        - `O-rich`:
          - `Gd`: float (eV)
          - `Gd_V_O`: float (eV)
          - `Gd_V_O_Gd`: float (eV)
        - `O-poor`:
          - `Gd`: float (eV)
          - `Gd_V_O`: float (eV)
          - `Gd_V_O_Gd`: float (eV)
    - `ordering`: string

Notes: The hidden checker compares each numeric value to the paper-reported gold with appropriate tolerances and verifies that the ordering declares Gd-V_O-Gd as the most stable configuration under both O-rich and O-poor conditions. The form of the results.json must exactly match the declared schema.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "single_gd_O_displacement": "float (Å)",
          "single_gd_Ce_displacement": "float (Å)",
          "single_gd_magnetic_moment": "float (μ_B)",
          "fermi_level_in_gap": "boolean",
          "formation_energies": {
            "type": "object",
            "properties": {
              "O-rich": {
                "Gd": "float (eV)",
                "Gd_V_O": "float (eV)",
                "Gd_V_O_Gd": "float (eV)"
              },
              "O-poor": {
                "Gd": "float (eV)",
                "Gd_V_O": "float (eV)",
                "Gd_V_O_Gd": "float (eV)"
              }
            }
          },
          "ordering": "string"
        }
      },
      "description": "Contains all scored physical quantities: atomic displacements, magnetic moment, Fermi level position, formation energies under two oxygen chemical potential conditions, and the stability ordering of defect complexes."
    }
  ],
  "notes": "The hidden checker compares each numeric value to the paper-reported gold with appropriate tolerances and verifies that the ordering declares Gd-V_O-Gd as the most stable configuration under both O-rich and O-poor conditions. The form of the results.json must exactly match the declared schema."
}
```

## How you are scored
A hidden verifier reads your `results.json` file and independently checks each reported quantity against the expected physical values. The verifier scores the displacements, magnetic moment, Fermi-level location, and formation energies, and verifies that the declared stability ordering is correct under both O-rich and O-poor conditions. Each correctly computed quantity contributes to the final reward; incorrect or missing entries are penalized. The verifier does not re-run the DFT calculations but compares your results to a hidden reference obtained from the protocol defined in the workflow steps. To receive full credit, you must faithfully execute all process steps and compile the scored artifact from your own computed data.
