## Problem background
NiTi shape memory alloys are widely used in medical and engineering applications, but their production is hampered by the presence of brittle Ni2Ti4Ox oxide inclusions. These oxides degrade mechanical properties and formability. The formation mechanism of Ni2Ti4Ox is not well understood; it is hypothesized that as-cast NiTi2 segregation acts as a precursor and that oxygen uptake during heat treatment stabilizes the oxide phase. First-principles calculations can reveal the thermodynamic driving force by computing formation enthalpies.

## Approach
Use plane-wave density functional theory (DFT) with the generalized gradient approximation of Perdew–Burke–Ernzerhof (GGA-PBE). Build 1×1×1 supercells of cubic NiTi2 and Ni2Ti4Ox (x = 0.25, 0.5, 0.75, 1) with the Ti2Ni-type structure (space group Fd-3m). Insert oxygen atoms at the tetrahedral interstitial sites to achieve the required stoichiometry. Also prepare reference structures for the elemental ground states: face-centered cubic (fcc) Ni, hexagonal close-packed (hcp) Ti, and the O2 molecule.

Compute the total energies of all compounds and elemental references using an open-source DFT code (e.g., Quantum ESPRESSO). Use a plane-wave cutoff energy of 380 eV and a total-energy convergence criterion of at least 5×10⁻⁷ eV/atom. Perform full geometry optimization to obtain relaxed total energies.

Derive the formation enthalpy per formula unit from the DFT total energies. For a compound with total energy E_compound and the elemental reference energies E_i (per atom), the formation enthalpy ΔH per mole of atoms is

  ΔH (eV/atom) = (E_compound − Σ_i N_i E_i) / N_total

and then convert to kJ/mol (1 eV/atom = 96.485 kJ/mol). For NiTi2 the supercell contains 32 Ni + 64 Ti = 96 atoms; for Ni2Ti4Ox it contains 32 Ni, 64 Ti, and 16x O atoms. The formation enthalpy formulas are:

  NiTi2:            ΔH = (E_NiTi2 − 32 E_Ni − 64 E_Ti) / 96
  Ni2Ti4Ox:         ΔH = (E_Ni2Ti4Ox − 32 E_Ni − 64 E_Ti − 16x E_O) / (96 + 16x)

where E_O is the total energy of an isolated oxygen atom (obtained from the O2 molecule calculation, taking half the dimer energy).

## Reproduction target
Compute the formation enthalpies (in kJ/mol) of cubic NiTi2 and Ni2Ti4Ox (x = 0.25, 0.5, 0.75, 1). The results must exhibit a monotonic trend in formation enthalpy as oxygen content varies (the direction of the trend will be evaluated).

## Assets
- **Quantum ESPRESSO** (or equivalent open-source DFT code with GGA-PBE support) – tool; available from https://www.quantum-espresso.org .
- **Crystal structure data for Ti2Ni-type (Fd-3m)** – public literature data; the structure is described by Mueller & Knott (1963) and can be obtained from the Inorganic Crystal Structure Database (ICSD) or the Crystallography Open Database (COD).

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct 1×1×1 supercells of cubic NiTi2 and Ni2Ti4Ox with x = 0.25, 0.5, 0.75, 1 in the Fd-3m space group. Place oxygen atoms at the tetrahedral interstitial sites to satisfy the occupancy for each composition. Prepare reference structures for elemental Ni (fcc), Ti (hcp), and O (O₂ molecule) in their standard states.
- Evidence: none

### Step 2: DFT total energy calculations
- Role: process
- Action: Perform geometry optimization and total energy calculations for all constructed supercells and the three elemental references using the GGA-PBE functional. Use a plane-wave cutoff energy of 380 eV and a total-energy convergence of at least 5×10⁻⁷ eV/atom. Record the relaxed total energies.
- Evidence: `/app/outputs/dft_total_energies.json`

### Step 3: Formation enthalpy derivation
- Role: scored (load-bearing)
- Action: From the DFT total energies obtained in Step 2, apply the formation enthalpy formulas to compute the formation enthalpy in kJ/mol for NiTi2 and for each Ni2Ti4Ox composition (x = 0.25, 0.5, 0.75, 1). Write the results to a CSV file.
- Output file: `/app/outputs/formation_enthalpies.csv`
- Format: csv
- Contract: The CSV must have a header row with columns `compound`, `num_O`, `formation_enthalpy_kJ_per_mol`. Rows must correspond to the five compounds: `NiTi2` (num_O=0), `Ni2Ti4O0.25` (num_O=4), `Ni2Ti4O0.5` (num_O=8), `Ni2Ti4O0.75` (num_O=12), `Ni2Ti4O1` (num_O=16). The formation enthalpy column must contain numerical values in kJ/mol.
- Scoring: scored by hidden verifier

## Output files
The following files must be placed under `/app/outputs/`:
- `dft_total_energies.json` (evidence of DFT calculations)
- `formation_enthalpies.csv` (scored artifact)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_enthalpies.csv
- path: `/app/outputs/formation_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation enthalpies in kJ/mol for NiTi2 and Ni2Ti4Ox (x=0.25,0.5,0.75,1). The verifier checks the reported values against reference data within a tolerance and verifies the monotonic trend with oxygen content.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `num_O`, `formation_enthalpy_kJ_per_mol`
  - `units`:
    - `formation_enthalpy_kJ_per_mol`: kJ/mol

Notes: The verifier will also check the monotonic trend between formation enthalpy and oxygen content. Structural metadata (compound name, oxygen count) must match the prescribed rows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "num_O",
          "formation_enthalpy_kJ_per_mol"
        ],
        "units": {
          "formation_enthalpy_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Formation enthalpies in kJ/mol for NiTi2 and Ni2Ti4Ox (x=0.25,0.5,0.75,1). The verifier checks the reported values against reference data within a tolerance and verifies the monotonic trend with oxygen content."
    }
  ],
  "notes": "The verifier will also check the monotonic trend between formation enthalpy and oxygen content. Structural metadata (compound name, oxygen count) must match the prescribed rows."
}
```

## How you are scored
A hidden verifier reads your `formation_enthalpies.csv` and compares the reported formation enthalpies against reference values within a tolerance. It also checks that the formation enthalpy follows a strict monotonic trend with oxygen content (from x=0 to x=1). Each of these checks contributes to a combined weighted score (floating point between 0 and 1). Simply reporting the paper's numbers without performing the underlying DFT workflow is not sufficient – the verifier will detect attempts to bypass the computation.
