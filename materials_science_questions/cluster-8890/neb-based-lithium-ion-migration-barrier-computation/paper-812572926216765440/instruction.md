# Li+ Migration Barrier in Li2TiSiO5 via NEB Computation

## Problem background
Lithium-ion batteries require anode materials with low voltage and high capacity. Li2TiSiO5 is a titanium-based anode that offers a promising balance of working potential and theoretical capacity. Understanding how lithium ions migrate through its crystal lattice is essential for rationalising rate performance. First-principles calculations, such as density functional theory (DFT) combined with the nudged elastic band (NEB) method, can map three‑dimensional migration pathways and compute the associated energy barriers. Reproducing these computational results helps validate the predicted lithium ion transport mechanism and establishes the role of different interstitial sites in the migration process.

## Approach
Use DFT with the Perdew–Burke–Ernzerhof (PBE) functional to model lithium ion diffusion in Li2TiSiO5. Begin with the primitive crystal structure (space group P4/nmm) and build a 1a × 1b × 2c supercell. Analyse the supercell to identify possible interstitial lithium sites; two key sites are the crystallographic 2b and 4d Wyckoff positions. Construct initial and final configurations for a lithium ion migrating from a 2b site to a neighbouring 4d site and then to an adjacent 2b site. Perform climbing‑image nudged elastic band (CI‑NEB) calculations to converge the minimum‑energy path and obtain the energy profile. Extract the maximum energy barrier along the path (in eV) and the sequence of sites traversed. The workflow must use an open‑source DFT code (e.g., Quantum ESPRESSO) with a suitable pseudopotential set and appropriate numerical convergence. The final output is a single CSV file reporting the barrier and the migration path.

## Reproduction target
Compute the lithium ion migration energy barrier for the path that connects the 2b and 4d interstitial sites in the 1a × 1b × 2c supercell of Li2TiSiO5, using DFT with the PBE functional and CI‑NEB. Report the maximum energy barrier (barrier_eV, in eV) along the whole path and the site‑sequence description (migration_path) in the file `li_migration_barriers.csv`.

## Assets

- Li2TiSiO5 crystal structure (CIF): https://next-gen.materialsproject.org/materials/mp-1108195
- Quantum ESPRESSO: quantum-espresso
- Atomic Simulation Environment (ASE): ase
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare supercell and identify NEB endpoints
- Role: process
- Action: Construct a 1a×1b×2c supercell of Li2TiSiO5 from the primitive cell. Identify the inequivalent interstitial sites 2b and 4d. Create initial and final configurations for Li migration along the 2b→4d→2b path.
- Evidence: `/app/outputs/supercell_endpoints.pdb`

### Step 2: Compute Li+ migration barrier and path
- Role: scored (load-bearing)
- Action: Run climbing-image nudged elastic band (CI-NEB) calculations using DFT with the PBE functional, an open-source code (e.g., Quantum ESPRESSO) and a suitable pseudopotential set. Use the supercell and endpoints from the previous step. Extract the maximum energy barrier (in eV) along the path and the migration path site sequence. Write results to li_migration_barriers.csv.
- Output file: `/app/outputs/li_migration_barriers.csv`
- Format: csv
- Contract: barrier_eV (float), migration_path (string, e.g., '2b→4d→2b')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/li_migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### li_migration_barriers.csv
- path: `/app/outputs/li_migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed Li+ migration energy barrier (maximum barrier along the NEB path) and the site sequence. Scoring uses the barrier value with a tolerance and requires the migration_path to contain '2b→4d→2b'.
- schema:
  - `type`: table
  - `required_columns`: `barrier_eV`, `migration_path`
  - `units`:
    - `barrier_eV`: eV

Notes: The NEB calculation must be performed on the 1a×1b×2c supercell using a PBE-based DFT setup. The reported barrier is the maximum energy barrier along the computed path.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "li_migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "barrier_eV",
          "migration_path"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Computed Li+ migration energy barrier (maximum barrier along the NEB path) and the site sequence. Scoring uses the barrier value with a tolerance and requires the migration_path to contain '2b→4d→2b'."
    }
  ],
  "notes": "The NEB calculation must be performed on the 1a×1b×2c supercell using a PBE-based DFT setup. The reported barrier is the maximum energy barrier along the computed path."
}
```

## How you are scored
A hidden verifier reads your `li_migration_barriers.csv` file. It checks two properties: (1) that the `migration_path` string contains the expected sequence of interstitial sites determined by the crystal structure; (2) that the `barrier_eV` value is sufficiently close to a reference obtained from high‑accuracy calculations, with a tolerance that accounts for typical variability among different DFT implementations and pseudopotentials. The scoring uses a threshold‑or‑better policy: you earn full credit if your barrier meets the closeness requirement and the path string is correct; otherwise partial credit is awarded when only one criterion is satisfied. The overall reward is a weighted combination of the scores from all workflow stages. There is no need to reproduce a specific literature value; the verifier's reference is hidden.
