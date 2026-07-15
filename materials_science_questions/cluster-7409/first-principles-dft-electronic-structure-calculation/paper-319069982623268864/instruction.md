# First-principles CPA-DFT electronic structure of doped α-Al2O3

## Problem background
The electronic properties of \(\alpha\)-Al\(_2\)O\(_3\) (corundum) can be modified by substituting aluminium atoms with transition metal or post‑transition metal cations, and by introducing vacancies on both sublattices. Understanding how such doping and non‑stoichiometry change the total density of states near the Fermi level is key for designing oxide‑based electronic devices. This computational study investigates the electronic structure of pure \(\alpha\)-Al\(_2\)O\(_3\) and a series of doped compositions using first‑principles density‑functional theory within the Coherent Potential Approximation (CPA). You will compute the total density of states for twelve defined compositions and determine for each whether the spectrum is metallic or insulating; for insulating systems you must extract the band‑gap width.

## Approach
An open‑source CPA‑capable DFT code (for example AKAI‑KKR) is employed to model substitutional disorder on the mean‑field level. Starting from the known corundum crystal structure of \(\alpha\)-Al\(_2\)O\(_3\), you prepare input configurations that define the desired dopant concentrations and vacancy fractions using the CPA. For each composition a self‑consistent field calculation is run to converge the charge density, and the total density of states is then computed on a sufficiently fine energy mesh. Pure \(\alpha\)-Al\(_2\)O\(_3\) serves as the reference. From the resulting DOS you locate the Fermi level: if the DOS is finite there the system is metallic; otherwise you identify the valence‑band maximum and the conduction‑band minimum and report their energy difference as the band gap.

## Reproduction target
Deliver two scored output files under `/app/outputs`:

1. **`total_dos_all_compositions.dat` (TSV)** – Contains the total DOS for each of the twelve compositions listed below. Each composition’s data block is preceded by a header line `# composition: <name>` and has columns: composition, energy_in_eV (eV), total_dos (states/eV).

2. **`band_gap_summary.csv` (CSV)** – Two columns: composition and band_gap. For insulating compositions give the band gap in eV as a float; for metallic compositions use the string `'metallic'`.

The twelve compositions that must be present:
- pure α‑Al\(_2\)O\(_3\)
- Al\(_{1.94}\)Zr\(_{0.06}\)O\(_3\)
- Al\(_{1.94}\)Nb\(_{0.06}\)O\(_3\)
- Al\(_{1.94}\)Mo\(_{0.06}\)O\(_3\)
- Al\(_{1.94}\)O\(_3\) (Al vacancy)
- Al\(_{1.97}\)Ga\(_{0.03}\)O\(_3\)
- Al\(_{1.96}\)Zr\(_{0.03}\)O\(_3\)
- Al\(_{1.95}\)Nb\(_{0.03}\)O\(_3\)
- Al\(_{1.94}\)Mo\(_{0.03}\)O\(_3\)
- Al\(_{1.97}\)Ga\(_{0.03}\)O\(_{2.97}\)
- Al\(_{1.96}\)Zr\(_{0.03}\)O\(_{2.97}\)
- Al\(_{1.91}\)Nb\(_{0.03}\)Sn\(_{0.06}\)O\(_{2.97}\)

## Assets

- Crystal structure of α-Al2O3 (corundum)
- AKAI-KKR (MACHIKANEYAMA) CPA-DFT code: https://kkr.issp.u-tokyo.ac.jp/
- Atomic potentials/pseudopotentials for Al, O, Zr, Nb, Mo, Ga, Sn

## Workflow steps

### Step 1: Prepare CPA-DFT input files
- Role: process
- Action: Set up the corundum crystal structure of α-Al2O3 and create CPA input configurations for all twelve studied compositions: pure α-Al2O3, Al1.94Zr0.06O3, Al1.94Nb0.06O3, Al1.94Mo0.06O3, Al1.94O3 (Al vacancy), Al1.97Ga0.03O3, Al1.96Zr0.03O3, Al1.95Nb0.03O3, Al1.94Mo0.03O3, Al1.97Ga0.03O2.97, Al1.96Zr0.03O2.97, Al1.91Nb0.03Sn0.06O2.97. Each input must define the substitutional disorder via CPA appropriate for the chosen DFT code.
- Evidence: `/app/outputs/input_files.tar.gz`

### Step 2: Run CPA-DFT self-consistent field calculations
- Role: process
- Action: Using an open-source CPA-capable DFT code (e.g., AKAI-KKR), perform self-consistent field electronic structure calculations for each composition from step_01. Converge the charge density and compute the total density of states (DOS) for each system. The pure α-Al2O3 calculation serves as the reference.
- Evidence: `/app/outputs/scf_logs.tar.gz`

### Step 3: Compile total DOS file
- Role: scored (load-bearing)
- Action: Collect the computed total DOS for each composition from the SCF runs and assemble them into a single TSV file. Each composition's data must be preceded by a header line '# composition: <name>'. The file must contain all twelve compositions with a fine energy grid that resolves band edges.
- Output file: `/app/outputs/total_dos_all_compositions.dat`
- Format: tsv
- Contract: TSV with columns: composition (string), energy_in_eV (float), total_dos (float). Sections separated by '# composition: <name>' lines.
- Scoring: scored by hidden verifier

### Step 4: Compile band gap summary
- Role: scored
- Action: From the computed DOS in total_dos_all_compositions.dat, determine for each composition whether it is metallic (finite DOS at the Fermi level) or insulating. If insulating, calculate the band gap in eV as the energy difference between the valence band maximum and conduction band minimum. Write a CSV with columns composition and band_gap, using the string 'metallic' for metallic compositions.
- Output file: `/app/outputs/band_gap_summary.csv`
- Format: csv
- Contract: CSV with two columns: composition (string), band_gap (float or the string 'metallic'). One row per composition (12 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_dos_all_compositions.dat`
- `/app/outputs/band_gap_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_dos_all_compositions.dat
- path: `/app/outputs/total_dos_all_compositions.dat`
- format: tsv
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for each of the twelve α-Al2O3-based compositions. The checker recomputes band gaps and metallicity from this file.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `energy_in_eV`, `total_dos`
  - `units`:
    - `energy_in_eV`: eV
    - `total_dos`: states/eV

### band_gap_summary.csv
- path: `/app/outputs/band_gap_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Summary of band gaps (eV) or metallicity for each composition. Compared against the paper's reference band gaps with hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `band_gap`
  - `units`:
    - `band_gap`: eV or 'metallic'

Notes: The checker recomputes the electronic character and band gaps from the raw DOS file to ensure consistency. The band_gap_summary is also checked for agreement with the recomputed values. Gold band gaps are paper-reported values and are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_dos_all_compositions.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "energy_in_eV",
          "total_dos"
        ],
        "units": {
          "energy_in_eV": "eV",
          "total_dos": "states/eV"
        }
      },
      "description": "Total density of states for each of the twelve α-Al2O3-based compositions. The checker recomputes band gaps and metallicity from this file."
    },
    {
      "file": "band_gap_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "band_gap"
        ],
        "units": {
          "band_gap": "eV or 'metallic'"
        }
      },
      "description": "Summary of band gaps (eV) or metallicity for each composition. Compared against the paper's reference band gaps with hidden tolerance."
    }
  ],
  "notes": "The checker recomputes the electronic character and band gaps from the raw DOS file to ensure consistency. The band_gap_summary is also checked for agreement with the recomputed values. Gold band gaps are paper-reported values and are hidden."
}
```

## How you are scored
A hidden verifier independently reads your `total_dos_all_compositions.dat` file and applies the same procedure – locating the Fermi level from the DOS and determining whether each composition is metallic or insulating, together with the band gap when applicable. It compares these derived quantities against hidden reference values with an appropriate tolerance. The verifier also checks that your `band_gap_summary.csv` is fully consistent with the DOS‑derived results. The final reward is a weighted combination of the correctness of the metallicity assignments and the agreement of the band gaps, with the DOS file providing the evidence base for the recomputation. Reporting numbers without the underlying computed DOS will not satisfy the scoring criteria.
