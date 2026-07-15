# DFT adsorption of IVA-group atoms on graphene

## Problem background
Understanding how individual atoms adsorb on graphene is fundamental for tailoring its electronic structure and magnetic properties. This task investigates the adsorption of group‑IVA atoms (C, Si, Ge, Sn, Pb) on graphene using first‑principles density functional theory. The key quantities of interest are the adsorption energy, the structural distortion of the graphene sheet, the adsorbate–carbon bond length, and the total magnetic moment induced by the adsorbate at three high‑symmetry surface sites.

## Approach
Spin‑polarized DFT calculations with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional are used to relax the adsorbate+graphene system and compute total energies. A 4×4 supercell of graphene with a vacuum slab is employed to isolate the adsorbate. Three adsorption sites are considered: top, bridge, and hollow. Reference energies for isolated graphene and isolated atoms are obtained with equivalent computational parameters. The adsorption energy is computed as the difference between the total energy of the combined system and the sum of the isolated components.

## Reproduction target
For each of the five group‑IVA atoms (C, Si, Ge, Sn, Pb) adsorbed on graphene at the top, bridge, and hollow sites, compute the adsorption energy E_ad (eV), graphene height distortion Δh (Å), adsorbate–carbon bond length d_ac (Å), and total magnetic moment M (μB) using the protocol described in the workflow steps. Produce a single CSV file, adsorption_results.csv, containing these 15 rows of data.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency Pseudopotential Library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python packages (numpy, ase, pymatgen): numpy ase pymatgen

## Workflow steps

### Step 1: Build graphene supercell and initial adsorbate configurations
- Role: process
- Action: Construct a 4×4×1 graphene supercell (in-plane lattice constant 9.88 Å, vacuum 15 Å). Generate initial structures for each adsorbate (C, Si, Ge, Sn, Pb) at top (T), bridge (B), and hollow (H) sites with an initial vertical distance of 2.0 Å. Save the structures as Quantum ESPRESSO input files.
- Evidence: none

### Step 2: Reference calculation – isolated graphene
- Role: process
- Action: Perform a spin-polarized DFT-PBE calculation on the pristine graphene supercell. Extract the total energy E_g.
- Evidence: none

### Step 3: Reference calculation – isolated atoms
- Role: process
- Action: For each atom (C, Si, Ge, Sn, Pb), perform a spin-polarized DFT-PBE calculation on an isolated atom in a 15 Å cubic cell using Γ‑point sampling. Extract the total energy E_a for each species.
- Evidence: none

### Step 4: Geometry optimization of adsorbate+graphene systems
- Role: process
- Action: For each of the 15 adsorbate/site combinations, perform a spin-polarized DFT-PBE geometry relaxation (force convergence < 0.02 eV/Å) using the same computational parameters as for graphene. Extract the total energy E_ag, relaxed atomic coordinates, and total magnetic moment M.
- Evidence: none

### Step 5: Extract properties and compute final table
- Role: scored (load-bearing)
- Action: From the relaxed geometries, compute the adsorption energy E_ad = E_ag - (E_a + E_g), the height distortion Δh = z_max - z_min of graphene carbon atoms, and the adsorbate–carbon bond length d_ac (distance to nearest carbon). Collect the magnetic moment M from the DFT output. Write all results into adsorption_results.csv with columns: atom, site, E_ad, delta_h, d_ac, M.
- Output file: `/app/outputs/adsorption_results.csv`
- Format: csv
- Contract: CSV with columns: atom (string), site (string), E_ad (float, eV), delta_h (float, Å), d_ac (float, Å), M (float, μB). 15 rows, one per adsorbate/site combination.
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
- description: Computed adsorption energies, structural distortions, bond lengths, and magnetic moments for all 15 adsorbate/site configurations.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `site`, `E_ad`, `delta_h`, `d_ac`, `M`
  - `units`:
    - `E_ad`: eV
    - `delta_h`: Å
    - `d_ac`: Å
    - `M`: μB
  - `nrows`: 15

Notes: The checker will compare each value to hidden gold from the paper's Table I using absolute tolerances that account for systematic differences between VASP (used in the paper) and Quantum ESPRESSO (open-source replacement).

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
          "delta_h",
          "d_ac",
          "M"
        ],
        "units": {
          "E_ad": "eV",
          "delta_h": "Å",
          "d_ac": "Å",
          "M": "μB"
        },
        "nrows": 15
      },
      "description": "Computed adsorption energies, structural distortions, bond lengths, and magnetic moments for all 15 adsorbate/site configurations."
    }
  ],
  "notes": "The checker will compare each value to hidden gold from the paper's Table I using absolute tolerances that account for systematic differences between VASP (used in the paper) and Quantum ESPRESSO (open-source replacement)."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads your adsorption_results.csv. For each of the 15 configurations, the verifier checks whether your computed values for E_ad, Δh, d_ac, and M fall within predetermined tolerances of a hidden reference set. Your score is the fraction of configurations that pass all four checks, so it is essential that your calculations faithfully follow the prescribed DFT protocol and geometry optimization.
