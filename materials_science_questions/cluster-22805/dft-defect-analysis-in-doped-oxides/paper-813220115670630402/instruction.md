# Reproduce electronic-to-nuclear stopping power ratios for fluorapatites using SRIM

## Problem background
Apatite-type materials with the general formula A<sup>I</sup><sub>4</sub>A<sup>II</sup><sub>6</sub>(BO<sub>4</sub>)<sub>6</sub>(OH,F,Cl)<sub>2</sub> can incorporate a wide variety of cations and anions, making them candidates for nuclear waste immobilization. Their radiation tolerance depends on chemical composition: energetic ions cause atomic displacements (nuclear stopping) that can lead to amorphization, while ionization from electronic energy loss can promote defect annealing. The electronic-to-nuclear stopping power ratio (ENSP) is a key parameter that correlates with radiation stability. This task asks you to reproduce the ENSP for several fluorapatite compositions by running stopping-range simulations, which provides a quantitative link between composition and radiation tolerance without requiring experimental irradiation or microscopy.

## Approach
You will use the publicly available SRIM software (version 2008 or later) to simulate 1 MeV Kr²⁺ ions incident on each fluorapatite target. For each composition, define the target density using known crystallographic data (lattice parameters and atomic positions from databases like ICSD or the literature) or estimate it from the formula mass and typical apatite densities. Set the displacement energy to 50 eV for all atoms, as is common practice for these materials. Run SRIM to obtain depth-resolved electronic stopping power (Sₑ) and nuclear stopping power (Sₙ) and extract the representative values. Compute the ratio ENSP = Sₑ/Sₙ for each composition and write the results to a CSV file with the required columns and row order, as detailed in the workflow step.

## Reproduction target
Produce the file `/app/outputs/ensp_computed.csv` containing, for the four fluorapatite compositions in the order Ca<sub>10</sub>(VO<sub>4</sub>)<sub>6</sub>F<sub>2</sub>, Ca<sub>10</sub>(P<sub>0.5</sub>V<sub>0.5</sub>O<sub>4</sub>)<sub>6</sub>F<sub>2</sub>, Ca<sub>10</sub>(PO<sub>4</sub>)<sub>6</sub>F<sub>2</sub>, and Pb<sub>4</sub>Ca<sub>6</sub>(VO<sub>4</sub>)<sub>6</sub>F<sub>2</sub>, the electronic stopping power Sₑ (eV/nm), nuclear stopping power Sₙ (eV/nm), and ENSP (dimensionless). The hidden verifier will compare your computed ENSP values to reference values and will also check that the relative ordering of ENSP across the four compositions follows the expected monotonic trend driven by the chemical substitutions (phosphate vs. vanadate at the B-site and calcium vs. lead at the A-site).

## Assets

- SRIM (Stopping and Range of Ions in Matter): https://www.srim.org/
- Crystallographic data for fluorapatite compositions

## Workflow steps

### Step 1: SRIM simulation and ENSP calculation
- Role: scored
- Action: Use SRIM (version 2008 or later) to simulate 1 MeV Kr²⁺ ions incident on each of the four fluorapatite targets: Ca₁₀(VO₄)₆F₂, Ca₁₀(P₀.₅V₀.₅O₄)₆F₂, Ca₁₀(PO₄)₆F₂, and Pb₄Ca₆(VO₄)₆F₂. For each target, set the density using known crystallographic data (or estimate from lattice parameters), and use a displacement energy of 50 eV for all atoms. From the SRIM output, extract the electronic stopping power (Se) and nuclear stopping power (Sn) in eV/nm, compute ENSP = Se/Sn, and write the results to ensp_computed.csv with the four rows in the order: Ca10VO4_6F2, Ca10P0.5V0.5O4_6F2, Ca10PO4_6F2, Pb4Ca6VO4_6F2.
- Output file: `/app/outputs/ensp_computed.csv`
- Format: csv
- Contract: CSV with header: composition, Se_eVnm, Sn_eVnm, ENSP. Exactly four rows in the given order. All numeric fields are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ensp_computed.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ensp_computed.csv
- path: `/app/outputs/ensp_computed.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed electronic stopping power (Se), nuclear stopping power (Sn), and their ratio (ENSP) for the four fluorapatite compositions under 1 MeV Kr²⁺ irradiation.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `Se_eVnm`, `Sn_eVnm`, `ENSP`
  - `units`:
    - `Se_eVnm`: eV/nm
    - `Sn_eVnm`: eV/nm
    - `ENSP`: dimensionless
  - `description`: Four rows for Ca10VO4_6F2, Ca10P0.5V0.5O4_6F2, Ca10PO4_6F2, Pb4Ca6VO4_6F2 in that order.

Notes: The checker will verify that ENSP values match the paper's reported gold within a tolerance and that the ordering Ca10PO4_6F2 > Ca10P0.5V0.5O4_6F2 > Ca10VO4_6F2 > Pb4Ca6VO4_6F2 is satisfied. The agent must write exactly four rows in the specified order.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ensp_computed.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "Se_eVnm",
          "Sn_eVnm",
          "ENSP"
        ],
        "units": {
          "Se_eVnm": "eV/nm",
          "Sn_eVnm": "eV/nm",
          "ENSP": "dimensionless"
        },
        "description": "Four rows for Ca10VO4_6F2, Ca10P0.5V0.5O4_6F2, Ca10PO4_6F2, Pb4Ca6VO4_6F2 in that order."
      },
      "description": "Computed electronic stopping power (Se), nuclear stopping power (Sn), and their ratio (ENSP) for the four fluorapatite compositions under 1 MeV Kr²⁺ irradiation."
    }
  ],
  "notes": "The checker will verify that ENSP values match the paper's reported gold within a tolerance and that the ordering Ca10PO4_6F2 > Ca10P0.5V0.5O4_6F2 > Ca10VO4_6F2 > Pb4Ca6VO4_6F2 is satisfied. The agent must write exactly four rows in the specified order."
}
```

## How you are scored
A hidden verifier reads your `ensp_computed.csv` and scores it in two parts: (i) how accurately the ENSP values match reference values within a tolerance, and (ii) whether the ordering of the four ENSP values satisfies the predefined monotonic relationship (e.g., the values should be consistent with the known effects of phosphate-for-vanadate and calcium-for-lead substitutions). The two parts are weighted, and the final reward is the weighted sum, ranging from 0 to 1. Simply reporting a number or re-ordering the rows will not be enough – you must correctly execute the SRIM simulations to obtain the right stopping powers.
