# Angular-dependent Interatomic Potential for Al–H: Property Computations

## Problem background
Hydrogen-induced degradation of aluminum alloys is a critical technological problem. Hydrogen absorption from the environment can lead to embrittlement, affecting mechanical properties. Accurate interatomic potentials are essential for atomistic simulations of these processes. However, existing potentials for the aluminum-hydrogen system have exhibited discrepancies with first-principles data, such as incorrect site preferences for hydrogen interstitial sites or insufficient testing across relevant properties. This work develops an angular-dependent potential (ADP) for the Al-H system that aims to reproduce a range of quantum-mechanical and experimental reference data, providing a tool for studying the effects of dissolved hydrogen on deformation and fracture of aluminum.

## Approach
The approach uses the angular-dependent potential (ADP) formalism, which extends the embedded-atom method (EAM) by adding non-central dipole and quadrupole terms. The total energy includes a pair energy, an embedding energy, and angular terms that penalize deviations from cubic symmetry. For the Al-H system, the pure Al part is described by the pre-existing EAM potential of Mishin et al. (1999). The hydrogen-hydrogen interactions and the Al-H cross-interaction are parameterized by closed-form functions whose optimal parameters are provided in the paper. No re-fitting is required; all needed parameters and functional forms are publicly available. The reproduction consists of implementing the ADP energy functional (pair, embedding, dipole, quadrupole) with these parameters, constructing the required crystal and defect structures, performing static energy minimizations to obtain equilibrium geometries and energies, and computing formation energies and bond lengths as defined by the thermodynamic relations given in the paper. For the hydrogen migration barrier, a nudged elastic band (NEB) calculation is performed between a tetrahedral and an octahedral interstitial site in aluminum. The results are collected into a single JSON file for evaluation.

## Reproduction target
Compute the following material properties using the ADP potential and collect them in the output JSON file:
- H₂ molecule: bond length and cohesive energy (eV/atom).
- Hydrogen crystals in simple cubic (SC), body-centered cubic (BCC), face-centered cubic (FCC), and hexagonal close-packed (HCP) structures: nearest-neighbor bond lengths and cohesive energies.
- Formation energies of selected aluminum hydrides: AlH₃ trigonal, AlH₂ fluorite, AlH zinc blende, and AlH rock salt (all in eV/atom).
- Dilute heats of solution of hydrogen at the tetrahedral (Td) and octahedral (Oh) interstitial sites in aluminum (eV).
- Migration barrier for a hydrogen atom moving from a tetrahedral to an octahedral site (eV).
- Formation energies of hydrogen‑vacancy pairs at tetrahedral and octahedral sites (eV).
All values must be written to `/app/outputs/predicted_properties.json` according to the output contract.

## Assets

- Al EAM potential (Mishin et al., 1999): http://www.ctcms.nist.gov/potentials/
- ADP potential files for hydrogen and Al–H cross interaction: http://www.ctcms.nist.gov/potentials/
- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://www.lammps.org/

## Workflow steps

### Step 1: Compute Al–H ADP properties and generate scored output
- Role: scored (load-bearing)
- Action: Using the ADP potential files from the NIST Interatomic Potentials Repository (pure H and Al–H cross interaction) and the published Al EAM potential, implement the full ADP energy functional (pair, embedding, dipole, quadrupole terms). Perform static energy minimizations on the required structures: H₂ dimer, SC, BCC, FCC, HCP hydrogen crystals; AlH₃ trigonal, AlH₂ fluorite, AlH zinc blende, AlH rock salt hydrides; Al with a single H at tetrahedral and octahedral interstitial sites; Al with an H‑vacancy pair at tetrahedral and octahedral sites. Compute formation energies and bond lengths as defined in the paper. For the migration barrier, run a nudged elastic band (NEB) calculation between a tetrahedral and an octahedral H site in Al. Collect all calculated quantities and write them to a JSON file with the exact keys listed in the output contract.
- Output file: `/app/outputs/predicted_properties.json`
- Format: json
- Contract: A JSON object with keys: 'H2_bond_length_angstrom' (float), 'H2_cohesive_eV_per_atom' (float), 'H_sc_bond_length_angstrom' (float), 'H_sc_cohesive_eV_per_atom' (float), 'H_bcc_bond_length_angstrom' (float), 'H_bcc_cohesive_eV_per_atom' (float), 'H_fcc_bond_length_angstrom' (float), 'H_fcc_cohesive_eV_per_atom' (float), 'H_hcp_bond_length_angstrom' (float), 'H_hcp_cohesive_eV_per_atom' (float), 'AlH3_trigonal_formation_eV_per_atom' (float), 'AlH2_fluorite_formation_eV_per_atom' (float), 'AlH_zincblende_formation_eV_per_atom' (float), 'AlH_rocksalt_formation_eV_per_atom' (float), 'H_Td_solution_eV' (float), 'H_Oh_solution_eV' (float), 'H_migration_barrier_eV' (float), 'H_Td_vacancy_formation_eV' (float), 'H_Oh_vacancy_formation_eV' (float). All values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_properties.json
- path: `/app/outputs/predicted_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All computed material properties from the ADP potential. The hidden verifier compares these values to the paper's reference data using tolerances and directional scoring.
- schema:
  - `type`: object
  - `required`: `H2_bond_length_angstrom`, `H2_cohesive_eV_per_atom`, `H_sc_bond_length_angstrom`, `H_sc_cohesive_eV_per_atom`, `H_bcc_bond_length_angstrom`, `H_bcc_cohesive_eV_per_atom`, `H_fcc_bond_length_angstrom`, `H_fcc_cohesive_eV_per_atom`, `H_hcp_bond_length_angstrom`, `H_hcp_cohesive_eV_per_atom`, `AlH3_trigonal_formation_eV_per_atom`, `AlH2_fluorite_formation_eV_per_atom`, `AlH_zincblende_formation_eV_per_atom`, `AlH_rocksalt_formation_eV_per_atom`, `H_Td_solution_eV`, `H_Oh_solution_eV`, `H_migration_barrier_eV`, `H_Td_vacancy_formation_eV`, `H_Oh_vacancy_formation_eV`
  - `properties`:
    - `H2_bond_length_angstrom`:
      - `type`: number
      - `unit`: Å
    - `H2_cohesive_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `H_sc_bond_length_angstrom`:
      - `type`: number
      - `unit`: Å
    - `H_sc_cohesive_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `H_bcc_bond_length_angstrom`:
      - `type`: number
      - `unit`: Å
    - `H_bcc_cohesive_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `H_fcc_bond_length_angstrom`:
      - `type`: number
      - `unit`: Å
    - `H_fcc_cohesive_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `H_hcp_bond_length_angstrom`:
      - `type`: number
      - `unit`: Å
    - `H_hcp_cohesive_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `AlH3_trigonal_formation_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `AlH2_fluorite_formation_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `AlH_zincblende_formation_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `AlH_rocksalt_formation_eV_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `H_Td_solution_eV`:
      - `type`: number
      - `unit`: eV
    - `H_Oh_solution_eV`:
      - `type`: number
      - `unit`: eV
    - `H_migration_barrier_eV`:
      - `type`: number
      - `unit`: eV
    - `H_Td_vacancy_formation_eV`:
      - `type`: number
      - `unit`: eV
    - `H_Oh_vacancy_formation_eV`:
      - `type`: number
      - `unit`: eV

Notes: The scored output is evaluated against the paper's reported results (hidden gold) with appropriate tolerances. No separate scoring of intermediate parameter files is performed; only the final property predictions are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/predicted_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "H2_bond_length_angstrom",
          "H2_cohesive_eV_per_atom",
          "H_sc_bond_length_angstrom",
          "H_sc_cohesive_eV_per_atom",
          "H_bcc_bond_length_angstrom",
          "H_bcc_cohesive_eV_per_atom",
          "H_fcc_bond_length_angstrom",
          "H_fcc_cohesive_eV_per_atom",
          "H_hcp_bond_length_angstrom",
          "H_hcp_cohesive_eV_per_atom",
          "AlH3_trigonal_formation_eV_per_atom",
          "AlH2_fluorite_formation_eV_per_atom",
          "AlH_zincblende_formation_eV_per_atom",
          "AlH_rocksalt_formation_eV_per_atom",
          "H_Td_solution_eV",
          "H_Oh_solution_eV",
          "H_migration_barrier_eV",
          "H_Td_vacancy_formation_eV",
          "H_Oh_vacancy_formation_eV"
        ],
        "properties": {
          "H2_bond_length_angstrom": {
            "type": "number",
            "unit": "Å"
          },
          "H2_cohesive_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "H_sc_bond_length_angstrom": {
            "type": "number",
            "unit": "Å"
          },
          "H_sc_cohesive_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "H_bcc_bond_length_angstrom": {
            "type": "number",
            "unit": "Å"
          },
          "H_bcc_cohesive_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "H_fcc_bond_length_angstrom": {
            "type": "number",
            "unit": "Å"
          },
          "H_fcc_cohesive_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "H_hcp_bond_length_angstrom": {
            "type": "number",
            "unit": "Å"
          },
          "H_hcp_cohesive_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "AlH3_trigonal_formation_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "AlH2_fluorite_formation_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "AlH_zincblende_formation_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "AlH_rocksalt_formation_eV_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "H_Td_solution_eV": {
            "type": "number",
            "unit": "eV"
          },
          "H_Oh_solution_eV": {
            "type": "number",
            "unit": "eV"
          },
          "H_migration_barrier_eV": {
            "type": "number",
            "unit": "eV"
          },
          "H_Td_vacancy_formation_eV": {
            "type": "number",
            "unit": "eV"
          },
          "H_Oh_vacancy_formation_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "All computed material properties from the ADP potential. The hidden verifier compares these values to the paper's reference data using tolerances and directional scoring."
    }
  ],
  "notes": "The scored output is evaluated against the paper's reported results (hidden gold) with appropriate tolerances. No separate scoring of intermediate parameter files is performed; only the final property predictions are scored."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/predicted_properties.json`. For each property, the verifier compares your computed value to a hidden reference value using tolerances and, where applicable, directional scoring (e.g., meeting or exceeding a target threshold earns full credit). The final reward is the fraction of properties that meet the acceptance criteria, equally weighted. Simply reporting the paper's numbers without performing the computations will fail because the tolerances are set to distinguish a genuine re-run from a trivial copy.
