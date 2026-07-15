# NEB-based Lithium Ion Migration Barrier Computation

## Problem background
Olivine LiFePO4 is a cathode material for lithium-ion batteries whose lithium ions diffuse through one-dimensional channels along the [010] direction. Li/Fe anti-site exchange defects, where a Li ion occupies a Fe site and a Fe ion occupies a Li site, can form during synthesis and block these channels. The energetic stability of different anti-site configurations (corner-shared vs. edge-shared) in stoichiometric LiFePO4 and in lithium-deficient compositions, as well as the activation barriers for recombination of such defects, are critical to understanding whether these defects can be removed by electrochemical or thermal processes. This task reproduces the first-principles calculations of defect formation energies and recombination barriers that underlie such engineering strategies.

## Approach
The computational approach uses spin-polarized density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation (GGA) and a Hubbard U correction (GGA+U) on Fe (U = 4.3 eV, J = 1.0 eV). Starting from the orthorhombic olivine LiFePO4 crystal structure (space group Pnma), a 1×2×2 supercell (112 atoms, 16 formula units) is built. Three types of point defects are introduced combinatorially: one Li vacancy at the M1 (Li) site, one Fe anti-site at M1, and one Li anti-site at an M2 (Fe) site, yielding 45 unique configurations. Total energies are computed for each defect configuration and for the pristine stoichiometric and Li-deficient defect-free supercells. Formation energies of the two most stable configurations (corner-shared and edge-shared) in both stoichiometric and Li-deficient conditions are obtained relative to the appropriate defect-free references. For the lowest-energy corner-shared configuration, the recombination pathway (Li migrates to the vacant M1, then Fe migrates to M2) is studied using the nudged-elastic-band (NEB) method, both with and without the addition of one excess electron (modeled as a homogeneous background charge), to extract the activation barriers.

## Reproduction target
Your task is to compute and report the following quantities using an open-source DFT code (e.g., Quantum ESPRESSO) and the NEB method:

1. Defect formation energies (in eV) for the corner-shared and edge-shared Li/Fe anti-site configurations in stoichiometric LiFePO4 and in Li-deficient LiFePO4 (one Li vacancy per supercell), along with the total energies of the corresponding defect-free supercells. The results must be written to /app/outputs/defect_formation_energies.json according to the output contract.

2. NEB activation barriers (in eV) for the recombination of the corner-shared defect without and with one excess electron, including the discretized energy profiles along the reaction coordinate. The results must be written to /app/outputs/neb_barriers.json according to the output contract.

The expected physical trends (e.g., relative ordering of formation energies and barriers) should naturally emerge from the calculations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- CASM: https://github.com/prisms-center/CASMcode
- LiFePO4 crystal structure (olivine): Materials Project mp-19017 or ICSD 172537
- Pseudopotentials for Li, Fe, P, O (PBE): Standard PBE projector-augmented wave (PAW) or ultrasoft pseudopotentials from the Quantum ESPRESSO library.

## Workflow steps

### Step 1: Enumerate Li/Fe anti-site defect configurations with a Li vacancy
- Role: process
- Action: Using the olivine LiFePO4 crystal structure and CASM (or manual enumeration), generate all 45 unique supercell configurations containing one Li vacancy at M1, one Fe anti-site at M1, and one Li anti-site at M2 within a 1×2×2 supercell (112 atoms, 16 formula units). Output the list of generated structures, e.g., as defect_configurations.json.
- Evidence: `/app/outputs/defect_configurations.json`

### Step 2: Run DFT total-energy calculations for all configurations
- Role: process
- Action: Perform spin-polarized GGA+U (PBE, U=4.3 eV, J=1.0 eV on Fe) total-energy calculations on every defect configuration, the stoichiometric defect-free supercell, and the Li-deficient defect-free supercell using Quantum ESPRESSO. Record the relaxed total energy for each configuration in a structured file (total_energies.json).
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Compute and report defect formation energies
- Role: scored
- Action: From the DFT total energies, compute the defect formation energies of the two most stable anti-site configurations (corner-shared and edge-shared) in stoichiometric and Li-deficient LiFePO4 relative to the appropriate defect-free references. Write the results to defect_formation_energies.json.
- Output file: `/app/outputs/defect_formation_energies.json`
- Format: json
- Contract: JSON object with keys: stoichiometric_corner_energy_eV (float), stoichiometric_edge_energy_eV (float), li_deficient_corner_energy_eV (float), li_deficient_edge_energy_eV (float), stoichiometric_defect_free_energy_eV (float), li_deficient_defect_free_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 4: Run NEB calculations for the corner-shared defect recombination path
- Role: process
- Action: Take the lowest-energy corner-shared defect configuration from step 2, construct initial and final states for the recombination pathway, and perform nudged-elastic-band (NEB) calculations without and with one excess electron (simulated by a homogeneous background charge) using the same DFT settings. Record the raw NEB profiles (neb_raw.json).
- Evidence: `/app/outputs/neb_raw.json`

### Step 5: Report NEB activation barriers
- Role: scored (load-bearing)
- Action: Extract the minimum-energy path and activation barriers from the NEB calculations, and write neb_barriers.json containing the barriers and the discretized energy profiles.
- Output file: `/app/outputs/neb_barriers.json`
- Format: json
- Contract: JSON object with keys: barrier_without_electron_eV (float), barrier_with_electron_eV (float), reaction_coordinates (list of floats 0-1), energy_profile_without_electron_eV (list of floats), energy_profile_with_electron_eV (list of floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_formation_energies.json`
- `/app/outputs/neb_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_formation_energies.json
- path: `/app/outputs/defect_formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Defect formation energies for the corner-shared and edge-shared Li/Fe anti-site configurations in stoichiometric and Li-deficient LiFePO4, along with reference defect-free total energies.
- schema:
  - `type`: object
  - `required`:
    - `stoichiometric_corner_energy_eV`: float
    - `stoichiometric_edge_energy_eV`: float
    - `li_deficient_corner_energy_eV`: float
    - `li_deficient_edge_energy_eV`: float
    - `stoichiometric_defect_free_energy_eV`: float
    - `li_deficient_defect_free_energy_eV`: float

### neb_barriers.json
- path: `/app/outputs/neb_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: NEB activation barriers for recombination without and with an extra electron, plus the discretized energy profiles along the reaction coordinate.
- schema:
  - `type`: object
  - `required`:
    - `barrier_without_electron_eV`: float
    - `barrier_with_electron_eV`: float
    - `reaction_coordinates`: list of floats 0-1
    - `energy_profile_without_electron_eV`: list of floats
    - `energy_profile_with_electron_eV`: list of floats

Notes: Formation energies and NEB barriers are compared to the paper's reported values with appropriate tolerances. Trend checks (Li-deficient energies lower than stoichiometric; NEB barrier with electron lower than without) are also applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "stoichiometric_corner_energy_eV": "float",
          "stoichiometric_edge_energy_eV": "float",
          "li_deficient_corner_energy_eV": "float",
          "li_deficient_edge_energy_eV": "float",
          "stoichiometric_defect_free_energy_eV": "float",
          "li_deficient_defect_free_energy_eV": "float"
        }
      },
      "description": "Defect formation energies for the corner-shared and edge-shared Li/Fe anti-site configurations in stoichiometric and Li-deficient LiFePO4, along with reference defect-free total energies."
    },
    {
      "file": "neb_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "barrier_without_electron_eV": "float",
          "barrier_with_electron_eV": "float",
          "reaction_coordinates": "list of floats 0-1",
          "energy_profile_without_electron_eV": "list of floats",
          "energy_profile_with_electron_eV": "list of floats"
        }
      },
      "description": "NEB activation barriers for recombination without and with an extra electron, plus the discretized energy profiles along the reaction coordinate."
    }
  ],
  "notes": "Formation energies and NEB barriers are compared to the paper's reported values with appropriate tolerances. Trend checks (Li-deficient energies lower than stoichiometric; NEB barrier with electron lower than without) are also applied."
}
```

## How you are scored
A hidden verifier will read your JSON output files and compare the reported formation energies and NEB barriers to a reference that accounts for the paper’s published values and for systematic differences between DFT codes and pseudopotentials. The verifier will also check that the results obey certain expected physical trends, such as Li-deficient formation energies being lower than stoichiometric ones and the NEB barrier being reduced when an excess electron is present. Each of the two scored artifacts carries a weight; the final reward is a weighted combination of their individual scores. Submitting the paper’s numbers without genuinely performing the calculations is not sufficient—the verifier evaluates the quality of your computed results against the hidden reference.
