# Extracting Free Energy Diagrams for ORR on Pt-Nx-C from Published DFT Results

## Problem background
Single-atom catalysts (SACs) supported on nitrogen-doped carbon exhibit promising activity for the oxygen reduction reaction (ORR). The number of nitrogen atoms directly coordinating the metal center (M-Nx-C) can influence the electronic structure and catalytic properties. The paper by Fan et al. (J. Mater. Sci. Technol., 2021) used platinum on N-doped graphene (Pt-Nx-C, x = 1,2,3,4) as a model system and computed the free energy landscapes of the ORR through the associative mechanism via DFT. The key quantity of interest is the free energy barrier of the rate-determining step, which can be read directly from the published free energy diagrams in Figure 6 of the paper.

## Approach
The strategy is to obtain the free energies of the ORR intermediates (*OOH, *O, *OH) on the four Pt‑Nx‑C sites from the paper’s Figure 6. The figure displays the free energy profiles for each model with the clean slab + O2(g) set as the reference (G = 0 eV). All values already include zero-point energy, entropy, and water solvation corrections as described in the paper. By reading the free energy of each intermediate from the diagram you can construct the table required for the reproduction target.

## Reproduction target
Read the free energy values of the clean reference and the adsorbates *OOH, *O, *OH (in eV) for the four Pt‑Nx‑C models (Pt-N1-C, Pt-N2-C, Pt-N3-C, Pt-N4-C) from Figure 6 of the paper. Output them in the specified CSV format. These values represent the free energy relative to the clean slab + O2(g) = 0 eV.

## Assets

- Paper: “The modulating effect of N coordination on single-atom catalysts researched by Pt‑Nx‑C model through both experimental study and DFT simulation” (provided in the environment)
- Figure 6 (image provided in the environment) showing the ORR free energy diagrams for Pt-N1-C, Pt-N2-C, Pt-N3-C, Pt-N4-C.

## Workflow steps

### Step 1: Extract free energies from Figure 6
- Role: scored (load-bearing)
- Action: Open Figure 6 of the paper. Locate the free energy diagram for each model (Pt‑N1‑C, Pt‑N2‑C, Pt‑N3‑C, Pt‑N4‑C). Read the free energy value (y‑axis) of the states: clean slab + O₂(g) (always 0.0 eV), *OOH, *O, and *OH. Record the values to one decimal place in eV.
- Output file: `/app/outputs/free_energy_diagram.csv`
- Format: csv
- Contract: model (string): Pt-N1-C, Pt-N2-C, Pt-N3-C, Pt-N4-C; intermediate (string): clean, OOH, O, OH; free_energy (float): free energy in eV relative to clean slab + O2(g), set to 0.0 for clean.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_diagram.csv
- path: `/app/outputs/free_energy_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Free energy of each ORR intermediate relative to clean slab + O2(g) for Pt-Nx-C models with x=1,2,3,4.
- schema:
  - `type`: table
  - `required_columns`: `model`, `intermediate`, `free_energy`
  - `units`:
    - `free_energy`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "intermediate",
          "free_energy"
        ],
        "units": {
          "free_energy": "eV"
        }
      },
      "description": "Free energy of each ORR intermediate relative to clean slab + O2(g) for Pt-Nx-C models with x=1,2,3,4."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will inspect the submitted CSV file `free_energy_diagram.csv`. It compares the reported free energies of each intermediate to a set of reference values and checks that the largest free‑energy increase (the rate‑limiting barrier) follows a physically meaningful trend with respect to the Pt‑N coordination number. The reward is a weighted combination of these quantitative and qualitative checks. Submitting numbers that match the reference alone is not sufficient; the verifier evaluates the internal consistency and the correctness of the derived trend.