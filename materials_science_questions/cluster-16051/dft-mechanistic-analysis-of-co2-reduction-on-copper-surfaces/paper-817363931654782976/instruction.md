# DFT Calculations of HOMO-LUMO Gaps and Free Energies of CO2 Reduction on Donor-Acceptor Cu Porphyrins

## Problem background
Molecular copper porphyrin catalysts with donor‑acceptor modifications have been explored for electrochemical CO2 reduction to CH4, a demanding multi‑electron conversion. Density functional theory (DFT) can provide insight into how such structural modifications affect the electronic structure and reaction energetics, offering a computational rationalization of catalytic trends. This task reproduces the DFT component of such an investigation, computing the HOMO–LUMO gap and the Gibbs free energy change for the key *CO → *CHO step on two related copper porphyrin molecules: one substituted with amino donor groups (CuTAPP) and an unsubstituted reference (CuTPP).

## Approach
The study is based on first‑principles DFT. Three‑dimensional molecular models are built for the two catalyst molecules and their surface intermediates (*CO and *CHO bound to the Cu centre), together with gas‑phase H2 and H2O. Geometry optimizations and harmonic frequency analyses are carried out at the B3LYP/6‑31G(d) level using the LANL2DZ effective core potential for Cu, employing the ORCA quantum chemistry package. From the converged electronic structures the HOMO–LUMO gaps are extracted. The Gibbs free energy profile for the elementary step *CO + H⁺ + e⁻ → *CHO is reconstructed via the computational hydrogen electrode (CHE) model, using the electronic energies, zero‑point energies (ZPE), and vibrational entropies obtained from the frequency calculations. The procedure yields a HOMO–LUMO gap and a reaction free energy for each catalyst, allowing a comparison of their predicted properties.

## Reproduction target
Produce the HOMO–LUMO gap (in eV) for both CuTAPP and CuTPP, and compute the Gibbs free energy change (in eV) for the *CO → *CHO step on each catalyst at standard conditions (298.15 K, pH 0). The required deliverables are a CSV file with the two gaps and a JSON file containing the per‑species energy components (electronic energy, ZPE, vibrational entropy, temperature) needed to recompute the reaction free energy. The verifier will independently assess these outputs against a hidden reference derived from the same level of theory.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de
- Initial molecular geometries (XYZ)

## Workflow steps

### Step 1: Build initial molecular structures
- Role: process
- Action: Generate or load the starting three-dimensional geometries for CuTAPP and CuTPP, and construct initial coordinates for the *CO and *CHO adsorbates bound to the Cu center. Also prepare gas-phase H2 and H2O. The agent may use bundled XYZ files or chemical libraries.
- Evidence: none

### Step 2: DFT geometry optimization and frequency calculation
- Role: process
- Action: For every species (CuTAPP, CuTPP, *CO@CuTAPP, *CO@CuTPP, *CHO@CuTAPP, *CHO@CuTPP, H2, H2O) perform DFT geometry optimization followed by a harmonic frequency analysis at the B3LYP/6-31G(d) level with LANL2DZ effective core potential on Cu, using ORCA. This provides relaxed geometries, total energies, vibrational frequencies, and Kohn-Sham orbital energies.
- Evidence: none

### Step 3: Extract HOMO-LUMO gaps
- Role: scored
- Action: From the converged ORCA output of CuTAPP and CuTPP, read the highest occupied and lowest unoccupied molecular orbital energies and compute the HOMO-LUMO gap in eV. Write the gaps to /app/outputs/step_01_homo_lumo_gaps.csv.
- Output file: `/app/outputs/step_01_homo_lumo_gaps.csv`
- Format: csv
- Contract: Columns: molecule (str), gap (eV). Two rows: CuTAPP and CuTPP.
- Scoring: scored by hidden verifier

### Step 4: Collect species energies for free energy reconstruction
- Role: scored (load-bearing)
- Action: Parse the ORCA output files to retrieve for each species the total electronic energy (E_el), zero-point energy (ZPE), and vibrational entropy corrections. Save the data as a structured JSON document to /app/outputs/step_02_species_energies.json.
- Output file: `/app/outputs/step_02_species_energies.json`
- Format: json
- Contract: Object with keys: species (list of str), E_total (list of float, eV), ZPE (list of float, eV), S_vib (list of float, eV/K), T (float, K). Must contain all species: CuTAPP, CuTPP, *CO@CuTAPP, *CO@CuTPP, *CHO@CuTAPP, *CHO@CuTPP, H2, H2O.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_homo_lumo_gaps.csv`
- `/app/outputs/step_02_species_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_homo_lumo_gaps.csv
- path: `/app/outputs/step_01_homo_lumo_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed HOMO-LUMO gaps for CuTAPP and CuTPP. The checker compares these against reference values within tolerance and verifies the gap ordering.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `gap`
  - `units`:
    - `gap`: eV

### step_02_species_energies.json
- path: `/app/outputs/step_02_species_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Energy components for all reaction species. The checker recomputes the Gibbs free energy change for the *CO→*CHO step using the computational hydrogen electrode model and compares to reference values within tolerance, also verifying the free energy ordering.
- schema:
  - `type`: object
  - `required`:
    - `species`: array of string
    - `E_total`: array of number (eV)
    - `ZPE`: array of number (eV)
    - `S_vib`: array of number (eV/K)
    - `T`: number (K)
  - `units`:
    - `E_total`: eV
    - `ZPE`: eV
    - `S_vib`: eV/K
    - `T`: K

Notes: All experimental characterizations (synthesis, spectroscopy, electrochemistry) are wet-lab and omitted. The electron density difference analysis is qualitative and not scored. The DFT workflow must be run by the agent; the task provides initial XYZ geometries as a convenience.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_homo_lumo_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "gap"
        ],
        "units": {
          "gap": "eV"
        }
      },
      "description": "Computed HOMO-LUMO gaps for CuTAPP and CuTPP. The checker compares these against reference values within tolerance and verifies the gap ordering."
    },
    {
      "file": "step_02_species_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "species": "array of string",
          "E_total": "array of number (eV)",
          "ZPE": "array of number (eV)",
          "S_vib": "array of number (eV/K)",
          "T": "number (K)"
        },
        "units": {
          "E_total": "eV",
          "ZPE": "eV",
          "S_vib": "eV/K",
          "T": "K"
        }
      },
      "description": "Energy components for all reaction species. The checker recomputes the Gibbs free energy change for the *CO→*CHO step using the computational hydrogen electrode model and compares to reference values within tolerance, also verifying the free energy ordering."
    }
  ],
  "notes": "All experimental characterizations (synthesis, spectroscopy, electrochemistry) are wet-lab and omitted. The electron density difference analysis is qualitative and not scored. The DFT workflow must be run by the agent; the task provides initial XYZ geometries as a convenience."
}
```

## How you are scored
A hidden verifier scores each workflow stage independently. For the HOMO–LUMO gaps, it checks your submitted values against a hidden reference with an appropriate tolerance. For the free energy reconstruction, the verifier recomputes the *CO → *CHO Gibbs free energy change from your submitted energy components using the CHE model and compares the result to a hidden reference. Additional structural properties, such as the relative ordering of computed energies between the two catalysts, may also be verified. The final reward is a weighted sum of these per‑stage scores. Simply reporting arbitrary numbers will not yield a high score; the artifacts must be internally consistent with a correct DFT simulation.
