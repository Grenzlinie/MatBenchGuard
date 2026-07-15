# DFT-based estimation of equilibrium properties and band gaps for silver nitride phases

## Problem background
Silver nitride (Ag₃N) is a highly endothermic, explosive compound whose structural and electronic properties are poorly characterized experimentally. Density functional theory (DFT) can provide reliable predictions of these properties. In this work, we focus on the three structurally related Ag₃N phases: anti-ReO₃ (D0₉), CoAs₃ (D0₂), and RhF₃. The objective is to compute their equilibrium lattice parameters, cohesive energies, bulk moduli, pressure derivatives, and Kohn–Sham band gaps using first-principles calculations.

## Approach
The computational approach employs spin-polarized DFT with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation for exchange-correlation. The electron–ion interaction is treated with the projector augmented wave (PAW) method. For each crystal structure, the total energy is calculated as a function of the unit-cell volume while keeping the cell shape fixed and fully relaxing internal atomic positions. The resulting energy–volume data are fitted to the third-order Birch–Murnaghan equation of state to extract equilibrium properties. At the equilibrium geometry, a band structure and density of states calculation is performed to determine the Kohn–Sham band gap and its character (direct or indirect). The calculations are carried out using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and standard PAW pseudopotentials for Ag and N. Reference atomic energies for isolated Ag and N atoms are also required to compute the cohesive energy per atom.

## Reproduction target
Compute and report the equilibrium lattice constant (a, in Å), volume per atom (V₀, in Å³/atom), cohesive energy per atom (Ecoh, in eV/atom), bulk modulus (B₀, in GPa), its pressure derivative (B₀′), and the Kohn–Sham band gap (eV) together with its type (indirect or direct) for Ag₃N in the anti-ReO₃ (D0₉), CoAs₃ (D0₂), and RhF₃ crystal structures. All results must be written to the file `/app/outputs/ag3n_equilibrium_properties.json` according to the output contract. Additionally, the computed properties should reflect the close structural relationship among the three phases.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP PBE PAW pseudopotentials for Ag and N: https://www.materialscloud.org/discover/sssp/table/pbe
- Python scientific libraries (numpy, scipy, ase or pymatgen): numpy,scipy,ase

## Workflow steps

### Step 1: Compute reference atomic energies for Ag and N
- Role: process
- Action: Perform spin-polarized DFT calculations on isolated Ag and N atoms using the same computational parameters as the main volume scan (PBE functional, PAW pseudopotentials, plane-wave cutoff 600 eV). Store the total energies in a JSON file.
- Evidence: `/app/outputs/atomic_energies.json`

### Step 2: DFT total-energy volume scan for Agâ‚ƒN phases
- Role: process
- Action: For each of the three Agâ‚ƒN crystal structures (anti-ReOâ‚ƒ D0â‚‰, CoAsâ‚ƒ D0â‚‚, RhFâ‚ƒ), set up unit cells and perform spin-polarized DFT calculations at a set of volumes spanning approximately Â±10% around the expected equilibrium. At each volume, relax internal atomic positions until forces are <0.01 eV/Ã…. Use a Î“-centered 17Ã—17Ã—17 k-point mesh, plane-wave cutoff 600 eV, PBE functional with PAW pseudopotentials. Collect total energy and relaxed coordinates for each volume. Output raw data in a structured file.
- Evidence: `/app/outputs/volume_scan_data.json`

### Step 3: Equilibrium properties and band gaps for Agâ‚ƒN phases
- Role: scored (load-bearing)
- Action: From the energy-volume data and atomic reference energies, fit the third-order Birch-Murnaghan equation of state for each phase to obtain equilibrium atomic volume Vâ‚€ (Ã…Â³/atom), lattice constant(s), cohesive energy E_coh (eV/atom), bulk modulus Bâ‚€ (GPa), and its pressure derivative Bâ‚€â€². Then, at the equilibrium geometry, perform a band structure calculation and determine the Kohn-Sham band gap and whether it is direct or indirect. Compile all results into a single JSON file.
- Output file: `/app/outputs/ag3n_equilibrium_properties.json`
- Format: json
- Contract: {"phases": [{"name": "D0_9", "a": <float, Ã…>, "V0": <float, Ã…Â³/atom>, "Ecoh": <float, eV/atom>, "B0": <float, GPa>, "B0_prime": <float>, "band_gap": <float, eV>, "band_gap_type": "indirect"|"direct"}, {"name": "D0_2", ...}, {"name": "RhF3", ...}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ag3n_equilibrium_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ag3n_equilibrium_properties.json
- path: `/app/outputs/ag3n_equilibrium_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium properties and Kohnâ€“Sham band gaps for Agâ‚ƒN in D0â‚‰, D0â‚‚ and RhFâ‚ƒ structures, to be compared against reference values from the paper.
- schema:
  - `type`: object
  - `required`:
    - `phases`: array
  - `items`:
    - `name`: string
    - `a`: float, Angstrom
    - `V0`: float, AngstromÂ³/atom
    - `Ecoh`: float, eV/atom
    - `B0`: float, GPa
    - `B0_prime`: float, dimensionless
    - `band_gap`: float, eV
    - `band_gap_type`: string, one of 'indirect' or 'direct'
  - `units`: object

Notes: The hidden checker compares each phaseâ€™s reported values to the paperâ€™s published gold numbers with appropriate tolerances and also enforces a cross-phase consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ag3n_equilibrium_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "phases": "array"
        },
        "items": {
          "name": "string",
          "a": "float, Angstrom",
          "V0": "float, AngstromÂ³/atom",
          "Ecoh": "float, eV/atom",
          "B0": "float, GPa",
          "B0_prime": "float, dimensionless",
          "band_gap": "float, eV",
          "band_gap_type": "string, one of 'indirect' or 'direct'"
        },
        "units": {}
      },
      "description": "Equilibrium properties and Kohnâ€“Sham band gaps for Agâ‚ƒN in D0â‚‰, D0â‚‚ and RhFâ‚ƒ structures, to be compared against reference values from the paper."
    }
  ],
  "notes": "The hidden checker compares each phaseâ€™s reported values to the paperâ€™s published gold numbers with appropriate tolerances and also enforces a cross-phase consistency check."
}
```

## How you are scored
A hidden verifier will compare the values you report in `ag3n_equilibrium_properties.json` against independently established reference values. For each phase and each quantity, the verifier applies a tolerance; meeting or surpassing the reference threshold (in the physically correct direction) earns full credit, while larger deviations reduce the score. The verifier also checks cross-phase consistency: the properties of D0₂ and RhF₃ must lie within hidden limits of the D0₉ values. The overall reward is a weighted combination of the per-phase scores. Simply reporting numbers without actually executing the DFT volume scans and EOS fitting will not satisfy the verifier’s checks, which are designed to identify fabricated submissions. The reward is monotonic in quality: improving on the reference never lowers the score.
