# First-principles computational study of toxic gas adsorption on doped BC3 sheets

## Problem background
Toxic gas molecules such as HCN, NO, NO2, and NH3 are common air pollutants. Two-dimensional BC3 sheets doped with transition metals (Mo, Si, Pt) have been proposed as sensitive gas detectors and spintronic materials because adsorbed gases may systematically modify the electronic structure and magnetic properties. This task uses first-principles density functional theory (DFT) to compute the adsorption stability, charge transfer, and magnetic moments for these gas/dopant combinations, and to determine which substrates give optimal sensing performance.

## Approach
The approach uses spin-polarized DFT calculations with an open-source plane-wave code (Quantum ESPRESSO) and standard PBE pseudopotentials. A 2×2 supercell of BC3 containing 16 B and 16 C atoms is built with a vacuum layer. A single boron vacancy is created and a dopant atom (Mo, Si, or Pt) is substituted into the vacancy; the three doped sheets are relaxed. Then, for each of the four gas molecules (HCN, NO, NO2, NH3), the molecule is placed near the dopant in its most favorable orientation, the whole system is relaxed, and three properties are extracted: adsorption energy Eads = E(gas) + E(substrate) - E(complex), the total magnetic moment of the complex, and the net Bader charge transferred to the gas molecule (positive means the gas gains electrons). The workflow produces a CSV file with the results for all 12 gas/substrate combinations.

## Reproduction target
Produce a CSV file, `/app/outputs/adsorption_results.csv`, with 12 rows (one per gas/substrate pair) and the columns: substrate (string: Mo-BC3, Si-BC3, Pt-BC3), gas (string: HCN, NO, NO2, NH3), Eads (float, eV), magnetic_moment (float, μB), delta_q (float, |e|). Your computed values will be compared against a hidden reference using tolerances and additional structural/trend checks (for example, certain adsorption energies must be higher than others for a given substrate).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (SSSP or GBRV library): https://www.materialscloud.org/discover/sssp/
- Bader charge analysis code (Henkelman group): https://theory.cm.utexas.edu/henkelman/code/bader/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Relax doped BC3 supercells
- Role: process
- Action: Construct a 2×2 supercell of BC3 (16 B, 16 C) with a 16 Å vacuum layer. Create a single boron vacancy and substitute Mo, Si, and Pt individually at this vacancy to obtain Mo-BC3, Si-BC3, and Pt-BC3. Perform spin-polarized DFT relaxation for each doped sheet using an appropriate k-point grid and plane-wave energy cutoff. Save the optimized geometries for use in the gas adsorption step.
- Evidence: `/app/outputs/doped_geometries.json`

### Step 2: Gas adsorption simulations and property extraction
- Role: scored (load-bearing)
- Action: For each gas molecule (HCN, NO, NO2, NH3) and each substrate (Mo-BC3, Si-BC3, Pt-BC3), place the molecule in its most favorable orientation near the dopant atom, relax the whole system with spin-polarized DFT, and compute: (1) adsorption energy Eads = E(gas) + E(substrate) - E(complex), (2) total magnetic moment of the relaxed complex, (3) net Bader charge transfer to the gas molecule (positive means gain). Write all 12 results to adsorption_results.csv.
- Output file: `/app/outputs/adsorption_results.csv`
- Format: csv
- Contract: CSV with columns: substrate (string: Mo-BC3, Si-BC3, Pt-BC3), gas (string: HCN, NO, NO2, NH3), Eads (float, eV), magnetic_moment (float, μB), delta_q (float, |e|).
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
- description: Computed adsorption energies, total magnetic moments, and Bader charge transfers for HCN, NO, NO2, NH3 on Mo-BC3, Si-BC3, and Pt-BC3. Each row corresponds to one gas/substrate pair.
- schema:
  - `type`: table
  - `required_columns`: `substrate`, `gas`, `Eads`, `magnetic_moment`, `delta_q`
  - `units`:
    - `Eads`: eV
    - `magnetic_moment`: μB
    - `delta_q`: |e|

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
          "substrate",
          "gas",
          "Eads",
          "magnetic_moment",
          "delta_q"
        ],
        "units": {
          "Eads": "eV",
          "magnetic_moment": "μB",
          "delta_q": "|e|"
        }
      },
      "description": "Computed adsorption energies, total magnetic moments, and Bader charge transfers for HCN, NO, NO2, NH3 on Mo-BC3, Si-BC3, and Pt-BC3. Each row corresponds to one gas/substrate pair."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/adsorption_results.csv` and evaluates the reported quantities. Numeric values (adsorption energy, magnetic moment, charge transfer) are compared to a hidden reference using appropriate tolerances. In addition, relative orderings (e.g., one gas must have a larger adsorption energy than another on the same substrate) are checked. The final reward is a weighted fraction of correct value matches and satisfied trend checks. Simply reporting a number is not sufficient; the verifier expects the CSV to contain results derived from a genuine DFT calculation, and the scoring tolerances are set to allow for differences between DFT codes and implementation choices while still being strict enough to require a physically correct result.
