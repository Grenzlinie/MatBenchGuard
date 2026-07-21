# DFT adsorption energies of I3- on CZTS and CZTSSe surfaces

## Problem background
In dye-sensitized solar cells (DSSCs), the counter electrode (CE) catalyzes the reduction of triiodide (I₃⁻) to iodide (I⁻) to regenerate the sensitizer. Platinum is an excellent CE material, but its scarcity drives the search for earth-abundant alternatives. Cu₂ZnSnS₄ (CZTS) and its selenized derivative CZTSSe are promising Pt‑free counter‑electrode materials. Experimental studies have shown that selenization of CZTS to CZTSSe significantly improves the power conversion efficiency of DSSCs, but the atomic‑scale origin of this enhancement is not fully understood. Density functional theory (DFT) can probe the interaction between the I₃⁻ molecule and the catalyst surface, providing insight into which metal sites are most active and how substitution of sulfur by selenium modifies the catalytic activity. This task computes the adsorption energies and bond lengths of I₃⁻ on CZTS and CZTSSe surfaces to investigate the role of different surface metal sites in the enhanced performance.

## Approach
The investigation is carried out via periodic DFT slab calculations. Begin by constructing slab models of the wurtzite CZTS(002) surface and the corresponding selenized surface, where Se atoms partially replace S to form CZTSSe. The clean surfaces are relaxed with DFT geometry optimization. Next, an I₃⁻ molecule is placed on three distinct adsorption sites — atop Zn, Cu, and Sn atoms — for each surface. For each configuration, the total energy of the slab+adsorbate system, the isolated slab energy, and the isolated I₃⁻ energy are calculated. The adsorption energy is computed as E_b = E_total − (E_surface + E_I₃⁻), and the I₁–I₂ bond length is extracted from the relaxed adsorbate geometry. By collecting these quantities for all six combinations (two surfaces × three sites), one can analyse how the adsorption strength and bond activation change with selenization and which sites are most affected.

## Reproduction target
Produce a CSV file named adsorption_results.csv containing the computed adsorption energies (eV) and I₁–I₂ bond lengths (Å) for I₃⁻ adsorbed on the Zn, Cu, and Sn sites of CZTS and CZTSSe. The file must have the columns: system (CZTS or CZTSSe), site (Zn, Cu, or Sn), adsorption_energy_eV (float), I1_I2_bond_length_A (float), with exactly one row per combination. The hidden verifier will compare the relative trends among these values (the magnitude of energy changes upon selenization for different sites, and the bond length variations) against reference behaviour to evaluate the quality of the reproduction.

## Assets

- Open-source periodic DFT code (e.g., Quantum ESPRESSO, CP2K, or equivalent): https://www.quantum-espresso.org/
- Wurtzite Cu2ZnSnS4 crystal structure: https://materialsproject.org

## Workflow steps

### Step 1: Surface model construction and relaxation
- Role: process
- Action: Construct periodic slab models of wurtzite CZTS(002) and its selenized derivative CZTSSe (with Se partially substituting S). Perform DFT geometry optimization to relax the atomic positions of each clean surface.
- Evidence: `/app/outputs/relaxed_surface_geometries.json`

### Step 2: Compute I3- adsorption energies and I1-I2 bond lengths
- Role: scored (load-bearing)
- Action: For both relaxed surfaces (CZTS and CZTSSe), place an I3- molecule on the Zn, Cu, and Sn adsorption sites. For each configuration, compute the total energy of the system (E_total), the energy of the clean surface (E_surface), and the energy of the isolated I3- molecule (E_I3-). Calculate the adsorption energy as E_total - (E_surface + E_I3-) and extract the I1-I2 bond length. Write the results to adsorption_results.csv.
- Output file: `/app/outputs/adsorption_results.csv`
- Format: csv
- Contract: CSV with columns: system (string, one of 'CZTS' or 'CZTSSe'), site (string, one of 'Zn', 'Cu', 'Sn'), adsorption_energy_eV (float), I1_I2_bond_length_A (float). One row per combination.
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
- description: CSV file containing the computed adsorption energies (eV) and I1–I2 bond lengths (Å) for I3- on Zn, Cu, and Sn sites of CZTS and CZTSSe surfaces. The checker compares relative trends (e.g., Zn-site adsorption energy more negative in CZTSSe than in CZTS, Cu/Sn changes smaller, and bond length elongation on Zn) against hidden reference values derived from the paper’s DFT data.
- schema:
  - `type`: table
  - `file_format`: csv
  - `required_columns`: `system`, `site`, `adsorption_energy_eV`, `I1_I2_bond_length_A`
  - `units`:
    - `adsorption_energy_eV`: eV
    - `I1_I2_bond_length_A`: Angstrom

Notes: The task is scoped to the separable DFT adsorption energy calculations. The companion quantities (atomic/bond populations, DOS, EDD) are not required as they are explanatory details. The agent may use any open-source periodic DFT code and must construct the CZTS and CZTSSe slab models from public structure data.

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
        "file_format": "csv",
        "required_columns": [
          "system",
          "site",
          "adsorption_energy_eV",
          "I1_I2_bond_length_A"
        ],
        "units": {
          "adsorption_energy_eV": "eV",
          "I1_I2_bond_length_A": "Angstrom"
        }
      },
      "description": "CSV file containing the computed adsorption energies (eV) and I1–I2 bond lengths (Å) for I3- on Zn, Cu, and Sn sites of CZTS and CZTSSe surfaces. The checker compares relative trends (e.g., Zn-site adsorption energy more negative in CZTSSe than in CZTS, Cu/Sn changes smaller, and bond length elongation on Zn) against hidden reference values derived from the paper’s DFT data."
    }
  ],
  "notes": "The task is scoped to the separable DFT adsorption energy calculations. The companion quantities (atomic/bond populations, DOS, EDD) are not required as they are explanatory details. The agent may use any open-source periodic DFT code and must construct the CZTS and CZTSSe slab models from public structure data."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the scored output files. For this task, the verifier inspects adsorption_results.csv. It checks whether the computed adsorption energies and bond lengths show the correct relative ordering and magnitude of change upon selenization, as derived from the paper’s reported DFT data. Exact numerical agreement is not required; tolerances account for typical DFT functional and pseudopotential spread. Each scored artifact is assigned a weight, and the final reward (a float between 0 and 1) is the weighted sum of the scores. Simply reporting plausible numbers is not enough; the verifier cross‑checks that the trends are physically consistent with the published results.
