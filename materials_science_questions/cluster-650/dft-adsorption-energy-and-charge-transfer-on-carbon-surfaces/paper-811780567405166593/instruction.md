# DFT adsorption energies and magnetic moments of IVA-group atoms on graphene

## Problem background
Graphene's exceptional electronic properties can be modified by adsorbing foreign atoms, but the strength of interaction and the resulting structural and magnetic changes vary strongly with the adsorbate species. Group‑IVA atoms span a wide range of atomic sizes and bonding character, from the covalent, light carbon atom to the heavy, metallic lead atom, making them an ideal series for probing from strong chemisorption to weak physisorption on graphene. The computational target is to determine, using spin‑polarised density‑functional theory, how the adsorption energy, the graphene distortion, the adsorbate–carbon bond length, and the induced magnetic moment depend on the atom type and on the adsorption site.

## Approach
Use spin‑polarised DFT within the generalised gradient approximation (Perdew‑Burke‑Ernzerhof functional) and the projector‑augmented‑wave method to treat core electrons. Build a 4×4 graphene supercell with adequate vacuum and place each IVA atom (C, Si, Ge, Sn, Pb) in three high‑symmetry adsorption positions: top (above a carbon atom), bridge (above a C–C bond midpoint), and hollow (above the hexagon centre). For every adsorbate–site combination, relax the geometry until forces fall below a tight tolerance. Compute the total energies of isolated graphene and of each isolated atom in separate reference cells to allow the adsorption energy to be obtained from the relaxed adsorbate+graphene total energies. Extract the magnetic moment of the supercell, the vertical distortion of the graphene layer, and the distance from the adsorbate to its nearest carbon neighbour. The final task is to collect these quantities for all 15 systems into a single table.

## Reproduction target
Compute the adsorption energy (in eV), the graphene height distortion (in Å), the adsorbate–carbon nearest‑neighbour distance (in Å), and the total magnetic moment (in μ_B) for every combination of adsorbate atom (C, Si, Ge, Sn, Pb) and adsorption site (top = T, bridge = B, hollow = H). Collect the 15 rows of these four quantities together in a single CSV file.

## Assets

- Open-source DFT code supporting PAW-PBE (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE PAW pseudopotentials for C, Si, Ge, Sn, Pb: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Generate initial adsorption configurations
- Role: process
- Action: Build a 4x4 graphene supercell (in-plane lattice constant 9.88 Å, 15 Å vacuum). For each IVA group atom (C, Si, Ge, Sn, Pb) and for each adsorption site (top, bridge, hollow), place the atom initially at a height of 2.0 Å above the plane. Produce 15 input structures.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: Compute reference energies (isolated graphene and atoms)
- Role: process
- Action: Perform spin-polarised DFT-GGA-PBE calculations: (a) isolated graphene supercell to obtain E_g; (b) each isolated IVA atom in a 15 Å cubic cell (Γ-point sampling) to obtain E_a for C, Si, Ge, Sn, Pb. Use the same PAW pseudopotentials and an appropriate plane-wave cutoff.
- Evidence: `/app/outputs/reference_energies.csv`

### Step 3: DFT relaxations of adsorbate+graphene systems
- Role: process
- Action: For each of the 15 initial structures, run a spin-polarised DFT-GGA-PBE structural optimisation. Extract from each relaxed run the total energy E_ag, total magnetic moment M, the maximum z-range of graphene C atoms Δh, and the distance from the adsorbate to its nearest C atom d_ac. Use a convergent k-point mesh and force convergence.
- Evidence: `/app/outputs/relaxation_raw_data.csv`

### Step 4: Compute adsorption energies and compile final table
- Role: scored (load-bearing)
- Action: For each system, compute the adsorption energy E_ad = E_ag - (E_a + E_g) using the reference energies. Collect the atom, site, E_ad, Δh, d_ac, and M into a single CSV with 15 rows.
- Output file: `/app/outputs/adsorption_results.csv`
- Format: csv
- Contract: Columns: atom (C, Si, Ge, Sn, Pb), site (T, B, H), E_ad (float, eV), Δh (float, Å), d_ac (float, Å), M (float, μ_B). 15 rows total.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.csv
- path: `/app/outputs/adsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final adsorption energies, structural parameters, and magnetic moment for each IVA atom (C, Si, Ge, Sn, Pb) at top (T), bridge (B), and hollow (H) sites, reproducing the numerical values of Table I.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `site`, `E_ad`, `Δh`, `d_ac`, `M`
  - `units`:
    - `E_ad`: eV
    - `Δh`: Å
    - `d_ac`: Å
    - `M`: μ_B

Notes: The agent must run the full DFT workflow using an open-source code (e.g., Quantum ESPRESSO). The electronic structure analysis (DOS, charge density) shown in the paper is not scored because no numerical targets are provided. The hollow-site stability test is not required for the main scoring target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom",
          "site",
          "E_ad",
          "Δh",
          "d_ac",
          "M"
        ],
        "units": {
          "E_ad": "eV",
          "Δh": "Å",
          "d_ac": "Å",
          "M": "μ_B"
        }
      },
      "description": "Final adsorption energies, structural parameters, and magnetic moment for each IVA atom (C, Si, Ge, Sn, Pb) at top (T), bridge (B), and hollow (H) sites, reproducing the numerical values of Table I."
    }
  ],
  "notes": "The agent must run the full DFT workflow using an open-source code (e.g., Quantum ESPRESSO). The electronic structure analysis (DOS, charge density) shown in the paper is not scored because no numerical targets are provided. The hollow-site stability test is not required for the main scoring target."
}
```

## How you are scored
The hidden verifier reads your final CSV and compares each entry to a hidden reference derived from the original study, applying predefined acceptance tolerances on the numerical values and verifying the relative ordering of adsorption energies among the three sites for each atom. The reward is a single number in [0, 1]; higher agreement earns a higher score. Reporting the expected table without actually executing the DFT workflow will not satisfy the acceptance criteria, because the verifier checks the values against reference results that were obtained under a specific computational protocol.
