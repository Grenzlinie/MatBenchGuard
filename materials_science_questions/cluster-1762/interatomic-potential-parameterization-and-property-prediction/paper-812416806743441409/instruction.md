# Harmonic Lattice Dynamics of Solid N2 with Ab Initio Intermolecular Potential

## Problem background
Solid nitrogen crystallizes into ordered α and γ phases at low temperature. The intermolecular forces between N2 molecules determine the crystal structure, cohesive energy, and lattice vibrational frequencies. An ab initio derived pair potential can be tested without fitting to crystal data by performing harmonic lattice dynamics calculations and comparing the computed properties (lattice constants, cohesion energy, Γ‑point phonon frequencies) against experimental measurements. This task asks you to compute these properties for both phases using the harmonic approximation and two variants of the site‑site potential.

## Approach
The intermolecular interaction is modeled as a site–site potential with three types of contributions: electrostatic point charges placed along the molecular axis, an exponential overlap repulsion, and a C/r⁶ dispersion term, each with force‑center positions that may differ between contributions. Two parameter sets, labeled potential A and potential B, are provided. For each potential, you will construct the α‑N2 and γ‑N2 crystal lattices according to their space groups (Pa3 and P4₂/mnm, respectively) and molecular orientations. Perform lattice energy minimization with respect to the free lattice constant(s) at zero temperature and pressure for α‑N2, and at 4 kbar for γ‑N2, by summing pair interactions over a neighbour list of sufficient radius. Then solve the harmonic dynamical matrix at the Brillouin‑zone center (Γ point) to obtain phonon mode frequencies, and compute the cohesive energy per molecule for the α phase. The results will be compared to experimental measurements that serve as the hidden reference.

## Reproduction target
Compute the equilibrium lattice constant a for α‑N2 (Å), the cohesion energy per molecule for α‑N2 (kJ/mol), and the Γ‑point phonon frequencies (cm⁻¹) for the modes Eg, Tg1, Tg2, Au, Tu1, Eu, Tu2 for both potentials A and B. For γ‑N2 at 4 kbar, compute the lattice constants a and c (Å) and the Γ‑point phonon frequencies for modes Eg, B1g, A2g, Eu, B1u for both potentials. Write all computed quantities into /app/outputs/reproduction_results.json following the schema defined in the output contract. The hidden verifier will compare your values to experimental reference data.

## Assets

- Intermolecular potential parameters for N2 (Table I of the paper)
- Crystal structures of α-N2 and γ-N2
- Scientific Python libraries: numpy, scipy

## Workflow steps

### Step 1: Implement intermolecular potential and crystal builder
- Role: process
- Action: Implement the site–site intermolecular potential for potentials A and B using the provided parameters (charges, overlap exp-6, dispersion C/r⁶). Create functions to build the α-N2 and γ-N2 crystal lattices with the correct space group symmetries and molecular orientations. Establish a neighbour list for lattice energy sums.
- Evidence: `/app/outputs/potential_implementation.log`

### Step 2: Perform harmonic lattice dynamics calculations
- Role: process
- Action: For α-N2 and γ-N2 with both potentials A and B, minimize the lattice energy with respect to the lattice constants (a for α; a and c for γ) at the specified temperature and pressure. Construct and diagonalize the dynamical matrix at the Γ point to obtain phonon frequencies. Compute the cohesion energy for α-N2 as the lattice energy per molecule.
- Evidence: `/app/outputs/minimization_details.log`

### Step 3: Write harmonic results to JSON
- Role: scored (load-bearing)
- Action: Collect the computed lattice constants, cohesion energy, and Γ‑point phonon frequencies for α-N2 and γ-N2 under potentials A and B, and write them to reproduction_results.json following the output contract schema.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: A JSON object with top‑level keys 'alpha_N2_harmonic' and 'gamma_N2_harmonic'. Each phase object contains 'potential_A' and 'potential_B' sub-objects. Each potential object contains: 'lattice_constant_a_angstrom' (float), for gamma also 'lattice_constant_c_angstrom' (float), 'cohesion_energy_kJ_per_mol' (float, only for alpha), and 'phonon_frequencies_cm-1' (object mapping mode labels to floats). Mode labels for alpha: ['Eg','Tg1','Tg2','Au','Tu1','Eu','Tu2']; for gamma: ['Eg','B1g','A2g','Eu','B1u'].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Contains the harmonic lattice constants, cohesion energy for α-N2, and Γ‑point phonon frequencies for both crystal phases and both potentials. The checker compares each quantity to hidden experimental reference values with predefined tolerances, scoring on a threshold-or-better basis.
- schema:
  - `type`: object
  - `required`:
    - `alpha_N2_harmonic`: object
    - `gamma_N2_harmonic`: object
  - `items`:
    - `potential_A`: object
    - `potential_B`: object
  - `required_columns`:
  - `units`:
    - `lattice_constant_a_angstrom`: angstrom
    - `lattice_constant_c_angstrom`: angstrom
    - `cohesion_energy_kJ_per_mol`: kJ/mol
    - `phonon_frequencies_cm-1.mode`: cm⁻¹

Notes: The reference values used for scoring are the experimental lattice constants, cohesion energy, and phonon frequencies for the α and γ phases of solid N₂, taken from the literature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "alpha_N2_harmonic": "object",
          "gamma_N2_harmonic": "object"
        },
        "items": {
          "potential_A": "object",
          "potential_B": "object"
        },
        "required_columns": [],
        "units": {
          "lattice_constant_a_angstrom": "angstrom",
          "lattice_constant_c_angstrom": "angstrom",
          "cohesion_energy_kJ_per_mol": "kJ/mol",
          "phonon_frequencies_cm-1.mode": "cm⁻¹"
        }
      },
      "description": "Contains the harmonic lattice constants, cohesion energy for α-N2, and Γ‑point phonon frequencies for both crystal phases and both potentials. The checker compares each quantity to hidden experimental reference values with predefined tolerances, scoring on a threshold-or-better basis."
    }
  ],
  "notes": "The reference values used for scoring are the experimental lattice constants, cohesion energy, and phonon frequencies for the α and γ phases of solid N₂, taken from the literature."
}
```

## How you are scored
A hidden verifier independently evaluates each scored workflow artifact. It compares your reported lattice constants, cohesion energy, and phonon frequencies against experimental reference values (hidden gold) using predefined tolerances that are not disclosed to you. The scoring policy is threshold_or_better: achieving or surpassing the level of agreement with experiment that the harmonic model can deliver earns full credit; less accurate results incur a penalty. The verifier combines the weighted scores of the scored artifacts into the final reward. Simply copying numbers from an external source will not guarantee a perfect score because the tolerances are hidden and the verification depends on the values you actually compute.
