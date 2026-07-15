# DFT Calculation of Lattice Parameters and Formation Energies for Cubic TiAlMoN Compositions

## Problem background
Alloying Ti-Al-N hard coatings with molybdenum can modify their structural and energetic properties, potentially enhancing high-temperature performance. First-principles DFT calculations are used to evaluate the structural stability of cubic Ti<sub>1-x-y</sub>Al<sub>x</sub>Mo<sub>y</sub>N solid solutions. Understanding how lattice parameters and formation energies evolve with Mo content is essential for assessing phase stability and designing improved coatings.

## Approach
Density functional theory (DFT) calculations with the generalized gradient approximation (GGA-PBE) are employed to study four cubic TiAlMoN compositions. 2×2×2 supercells (64 atoms) are generated for each composition using the Alloy-Theoretic Automated Toolkit (ATAT) or an equivalent method. Geometry optimizations (cell relaxation and ionic relaxation) are performed with an open-source plane-wave DFT code (Quantum ESPRESSO) and appropriate pseudopotentials (SSSP PBE efficiency). Formation energies are referenced to elemental phases: Ti-hcp, Al-fcc, Mo-bcc, and the N₂ molecule.

## Reproduction target
Produce a JSON file containing, for each of the four compositions (Ti<sub>0.5</sub>Al<sub>0.5</sub>N, Ti<sub>0.50</sub>Al<sub>0.47</sub>Mo<sub>0.03</sub>N, Ti<sub>0.50</sub>Al<sub>0.44</sub>Mo<sub>0.06</sub>N, Ti<sub>0.50</sub>Al<sub>0.37</sub>Mo<sub>0.13</sub>N), the Mo fraction on the metal sublattice, the equilibrium lattice parameter (in Å), and the formation energy (in eV/atom). The results must be written to `/app/outputs/dft_results.json` with the structure defined in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Alloy-Theoretic Automated Toolkit (ATAT): https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/

## Workflow steps

### Step 1: Supercell construction and DFT calculations
- Role: process
- Action: Generate 2x2x2 supercells (64 atoms) for four cubic TiAlMoN compositions (Ti0.5Al0.5N, Ti0.50Al0.47Mo0.03N, Ti0.50Al0.44Mo0.06N, Ti0.50Al0.37Mo0.13N) and for elemental reference phases (Ti-hcp, Al-fcc, Mo-bcc, N₂ molecule) using ATAT or an equivalent supercell approach. Perform geometry optimization (cell relaxation and ionic relaxation) for each structure with Quantum ESPRESSO (GGA-PBE, SSSP pseudopotentials) to obtain total energies and optimized lattice parameters.
- Evidence: `/app/outputs/dft_logs.tar.gz`

### Step 2: Compute formation energies and lattice parameters
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute the formation energy (eV/atom) for each TiAlMoN composition as E_form = (E_total - sum_i n_i * mu_i) / N_total, where mu_i are the total energies of the elemental references (Ti-hcp, Al-fcc, Mo-bcc, N₂). Extract the cubic lattice parameter (a in Å) from the optimized structures. Write a JSON file containing the four compositions, their Mo fraction, lattice parameter, and formation energy.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"compositions": [{"label": "string", "y": float, "lattice_parameter_angstrom": float, "formation_energy_eV_per_atom": float}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the computed lattice parameters and formation energies for four cubic TiAlMoN compositions. The checker compares each value to hidden reference data with appropriate tolerances and verifies the expected monotonic trend of increasing lattice parameter with Mo content.
- schema:
  - `type`: object
  - `required`:
    - `compositions`: array of objects, each with keys: label (string, composition label), y (float, Mo fraction on metal sublattice), lattice_parameter_angstrom (float, Å), formation_energy_eV_per_atom (float, eV/atom)
  - `items`:
    - `label`: string
    - `y`: float
    - `lattice_parameter_angstrom`: float
    - `formation_energy_eV_per_atom`: float

Notes: The verifier will compare the reported lattice parameters and formation energies to hidden gold values and verify the trend that lattice parameter increases with Mo content. No specific tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "compositions": "array of objects, each with keys: label (string, composition label), y (float, Mo fraction on metal sublattice), lattice_parameter_angstrom (float, Å), formation_energy_eV_per_atom (float, eV/atom)"
        },
        "items": {
          "label": "string",
          "y": "float",
          "lattice_parameter_angstrom": "float",
          "formation_energy_eV_per_atom": "float"
        }
      },
      "description": "JSON file containing the computed lattice parameters and formation energies for four cubic TiAlMoN compositions. The checker compares each value to hidden reference data with appropriate tolerances and verifies the expected monotonic trend of increasing lattice parameter with Mo content."
    }
  ],
  "notes": "The verifier will compare the reported lattice parameters and formation energies to hidden gold values and verify the trend that lattice parameter increases with Mo content. No specific tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted `dft_results.json`. It compares each composition’s lattice parameter and formation energy against hidden reference values. Additionally, it checks that the computed lattice parameters satisfy a required monotonic trend across the series. Your final reward is a weighted combination of these checks; simply reporting the paper’s numbers is not sufficient because the verifier uses hidden tolerances and internal checks that require genuine calculations.
