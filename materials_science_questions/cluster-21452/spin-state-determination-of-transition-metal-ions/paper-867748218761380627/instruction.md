# Spin State Splitting of LaCoO3 from CASSCF/MRCI Active Space Calculations

## Problem background
LaCoO3 is a cobalt oxide perovskite that exhibits a spin-state transition at about 90 K, switching from a non-magnetic insulating phase at low temperature to a paramagnetic phase above the transition. The low-temperature electronic structure involves a subtle competition between ligand-field splitting, exchange interactions, and charge-transfer fluctuations between Co 3d and O 2p orbitals. Standard density-functional approaches have difficulty capturing the strong local correlations in this material. Quantum chemical wavefunction methods — specifically complete-active-space self-consistent-field (CASSCF) followed by multireference configuration interaction (MRCI) — can treat both the multireference character and dynamic correlation explicitly, but the result depends sensitively on which orbitals are included in the active space and which electrons are correlated. This task computes the low-spin (LS) to high-spin (HS) energy splitting on an embedded CoO6 cluster at four successive levels of theory that differ in their active orbital space and correlation treatment, thereby mapping out how the splitting depends on these choices.

## Approach
An isolated CoO6 octahedron is cut from the cubic perovskite lattice (Co–O distance 1.92 Å) and embedded in an array of point charges that approximate the crystalline Madelung potential of LaCoO3. All-electron Gaussian basis sets (triple-zeta quality) are used for Co, O, and the embedding La point charges. The electronic structure is solved with four successive wavefunction-based methods:

1. **CASSCF(6,5)** — a state-averaged CASSCF with 6 active electrons distributed over the 5 Co 3d orbitals (the minimal d-only active space).
2. **CASSCF(6,7)** — the active space is enlarged to 7 orbitals by adding the two ligand O 2p e_g symmetry-adapted combinations, which have the strongest overlap with the Co 3d e_g orbitals.
3. **MRCI-7** — internally contracted MRCI with single and double excitations starting from the CASSCF(6,7) reference, correlating the Co 3d and O 2p e_g electrons (valence correlation).
4. **MRCI-11** — the correlation treatment is further extended to also include single and double excitations from the Co 3s and 3p semi-core orbitals (as well as Co 3d, 4s, 4p and the O 2p e_g orbitals), capturing semi-core correlation effects.

At each level the absolute energies (in hartree) of the LS (^1A_g) and HS (^5T_2g) states are computed, and the splitting E(HS) – E(LS) is evaluated in eV. The four splittings together show the cumulative effect of expanding the active space and the correlation treatment on the spin-state ordering.

## Reproduction target
Construct the embedded CoO6 cluster, run the four calculations (two CASSCF and two MRCI) using an open-source quantum chemistry package (PySCF or ORCA), and report the four LS–HS energy splittings in a single JSON file with keys `cas5_splitting_eV`, `cas7_splitting_eV`, `mrci7_splitting_eV`, and `mrci11_splitting_eV`. Each value is E(HS) – E(LS) in eV: a positive value means the HS state is lower in energy, a negative value means the LS state is lower.

## Assets

- Crystal structure of LaCoO3 (Co-O bond length): 10.1103/PhysRevB.66.094408
- All-electron Gaussian basis sets for Co, O, La: https://www.basissetexchange.org/
- Open-source quantum chemistry code (PySCF or ORCA): https://pyscf.org/

## Workflow steps

### Step 1: Construct embedded CoO6 cluster
- Role: process
- Action: Build a CoO6 octahedron with Co–O distance 1.92 Å. Surround it with point charges that mimic the crystalline environment of cubic LaCoO3. Output the cluster geometry and embedding potential.
- Evidence: `/app/outputs/cluster_setup.json`

### Step 2: CASSCF with cas‑5 active space
- Role: process
- Action: Perform a state‑averaged CASSCF(6,5) calculation on the embedded CoO6 cluster to obtain absolute energies of the LS (^1A_g) and HS (^5T_2g) states. Write the two energies (in hartree) to cas5_energies.txt.
- Evidence: `/app/outputs/cas5_energies.txt`

### Step 3: CASSCF with cas‑7 active space
- Role: process
- Action: Perform a state‑averaged CASSCF calculation with an expanded active space: 6 electrons in 7 orbitals (5 Co 3d + 2 O 2p e_g combinations). Obtain LS and HS absolute energies and write them to cas7_energies.txt.
- Evidence: `/app/outputs/cas7_energies.txt`

### Step 4: MRCI-7 correlating Co 3d and O 2p e_g electrons
- Role: process
- Action: Starting from the cas‑7 reference, perform internally contracted MRCI including all single and double excitations from the Co 3d and O 2p e_g orbitals. Write the corrected LS and HS absolute energies to mrci7_energies.txt.
- Evidence: `/app/outputs/mrci7_energies.txt`

### Step 5: MRCI-11 including Co 3s,3p semi‑core correlations
- Role: process
- Action: Extend the MRCI correlation treatment to also include single and double excitations involving the Co 3s and 3p semi‑core electrons (as well as Co 3d,4s,4p and O 2p e_g). Compute LS and HS absolute energies and write to mrci11_energies.txt.
- Evidence: `/app/outputs/mrci11_energies.txt`

### Step 6: Compute and report LS‑HS energy splittings
- Role: scored (load-bearing)
- Action: Read the absolute energies of LS and HS states from the four evidence files, calculate E(HS) – E(LS) in eV for each level, and write the four splittings to spin_state_splittings.json.
- Output file: `/app/outputs/spin_state_splittings.json`
- Format: json
- Contract: {"cas5_splitting_eV": <float>, "cas7_splitting_eV": <float>, "mrci7_splitting_eV": <float>, "mrci11_splitting_eV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_state_splittings.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_state_splittings.json
- path: `/app/outputs/spin_state_splittings.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The four HS–LS energy splittings computed at successive levels of theory. Positive values indicate HS lower in energy; negative values indicate LS lower.
- schema:
  - `type`: object
  - `required`:
    - `cas5_splitting_eV`: float
    - `cas7_splitting_eV`: float
    - `mrci7_splitting_eV`: float
    - `mrci11_splitting_eV`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `cas5_splitting_eV`: eV
    - `cas7_splitting_eV`: eV
    - `mrci7_splitting_eV`: eV
    - `mrci11_splitting_eV`: eV

Notes: The scoring will compare each splitting to reference values from the paper with appropriate tolerances and check that the MRCI-11 splitting has the correct sign (LS ground state).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_state_splittings.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cas5_splitting_eV": "float",
          "cas7_splitting_eV": "float",
          "mrci7_splitting_eV": "float",
          "mrci11_splitting_eV": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "cas5_splitting_eV": "eV",
          "cas7_splitting_eV": "eV",
          "mrci7_splitting_eV": "eV",
          "mrci11_splitting_eV": "eV"
        }
      },
      "description": "The four HS–LS energy splittings computed at successive levels of theory. Positive values indicate HS lower in energy; negative values indicate LS lower."
    }
  ],
  "notes": "The scoring will compare each splitting to reference values from the paper with appropriate tolerances and check that the MRCI-11 splitting has the correct sign (LS ground state)."
}
```

## How you are scored
A hidden verifier reads your `spin_state_splittings.json` and compares each of the four splittings against independently established reference values using predefined tolerances. Each of the four splittings carries equal weight toward the final reward (0.0 to 1.0). The reward is monotonic: better agreement with the reference values yields a higher score, and the final reward is the weighted sum across the four splittings. Simply reporting published numbers without executing the computations is neither necessary nor sufficient — the verifier expects results that arise from a genuine execution of the prescribed computational workflow.
