## Problem background

The elemental actinide metals exhibit anomalous properties due to the partial localization of 5f electrons. Standard density functional theory (LDA) fails to describe the late actinides. The Disordered Local Moment (DLM) picture within the local spin density approximation combined with the coherent potential approximation (LSDA+CPA) can capture correlation effects beyond LDA without requiring explicit long‑range magnetic ordering, yielding accurate equilibrium volumes, bulk moduli, and electronic density of states.

## Approach

In this task you will use first-principles LSDA+CPA DLM calculations to determine the equilibrium properties of the actinide series and the density of states for δ‑Pu. The workflow consists of:
1. Performing self-consistent total energy calculations for each actinide (Th through Bk) in the fcc structure over a range of volumes, using an open‑source KKR or LMTO‑based code with CPA capability. For Pu, the DLM (disordered local moment) configuration is used.
2. Fitting the total energy vs. volume data to an equation of state (e.g., Birch‑Murnaghan) to extract the equilibrium Wigner‑Seitz radius and bulk modulus for each element.
3. Using the self-consistent potential from the Pu calculation at the equilibrium volume to compute the electronic density of states (DOS) as a function of energy.

The final outputs are two CSV files: one table with the equilibrium Wigner‑Seitz radii (Bohr) and bulk moduli (GPa) for all elements, and a second file with the DOS for δ‑Pu (energy in eV relative to Fermi level, DOS in states/eV/atom).

## Reproduction target

Compute the equilibrium Wigner‑Seitz radius (Bohr) and bulk modulus (GPa) for the fcc phase of the elements Th, Pa, U, Np, Pu, Am, Cm, and Bk using LSDA+CPA DLM calculations. Additionally, compute the density of states (DOS) for δ‑Pu at its equilibrium volume. The two CSV artifacts are the scored outputs; the verifier will compare your computed values against reference DLM results and check the structural features of the DOS.

## Assets

- **SPR‑KKR package** (or any open‑source KKR/LMTO code with CPA capability). Access: https://www.ebert.cup.uni-muenchen.de/SPRKKR/ . This code is required for the DFT+CPA calculations.

## Workflow steps

### Step 0: DFT total energy calculations for fcc actinides
- Role: process
- Action: Perform self‑consistent LSDA+CPA calculations for each actinide (Th, Pa, U, Np, Pu, Am, Cm, Bk) in the fcc crystal structure, for a set of volumes spanning roughly ±10% around the expected equilibrium, using an open‑source KKR or LMTO‑based code with CPA capability (e.g., SPR‑KKR). For Pu, the DLM (disordered local moment) setup must be used. Record total energies and self‑consistent potentials for each volume.
- Evidence: `/app/outputs/total_energies.txt`

### Step 1: Extract equilibrium Wigner‑Seitz radius and bulk modulus (load‑bearing)
- Role: scored (load‑bearing)
- Action: For each actinide, fit the total energy vs. volume data from Step 0 to an equation of state (e.g., Birch‑Murnaghan) and extract the equilibrium Wigner‑Seitz radius (in Bohr) and bulk modulus (in GPa). Compile the results into a CSV file.
- Output file: `/app/outputs/actinide_volumes_bulk_moduli.csv`
- Format: csv
- Contract: CSV with columns: `element` (string), `rws_bohr` (float, Wigner‑Seitz radius in Bohr), `bulk_modulus_gpa` (float, bulk modulus in GPa). One row per element (Th, Pa, U, Np, Pu, Am, Cm, Bk).
- Scoring: scored by hidden verifier

### Step 2: Compute density of states for δ‑Pu
- Role: scored
- Action: Using the self‑consistent potential from the Pu DFT calculation at the equilibrium volume (from Step 0), compute the electronic density of states (DOS) as a function of energy. Output a two‑column CSV of energy (eV) relative to the Fermi level and DOS (states/eV/atom).
- Output file: `/app/outputs/delta_plutonium_dos.csv`
- Format: csv
- Contract: CSV with columns: `energy_eV` (float, energy relative to Fermi level in eV), `dos_states_per_eV_atom` (float, density of states in states/eV/atom).
- Scoring: scored by hidden verifier

## Output files

The following artifact files must be written to `/app/outputs`:
- `actinide_volumes_bulk_moduli.csv`
- `delta_plutonium_dos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### actinide_volumes_bulk_moduli.csv
- path: `/app/outputs/actinide_volumes_bulk_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium Wigner-Seitz radii and bulk moduli for the fcc actinide series from LSDA+CPA DLM calculations.
- schema:
  - `type`: table
  - `required_columns`: `element`, `rws_bohr`, `bulk_modulus_gpa`
  - `units`: object

### delta_plutonium_dos.csv
- path: `/app/outputs/delta_plutonium_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Density of states for δ-Pu at equilibrium volume, computed from the self-consistent DLM calculation.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `dos_states_per_eV_atom`
  - `units`: object

Notes: The verifier checks radii and bulk moduli against reference values with tolerances, and verifies DOS structural features (peak positions, bandwidth).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "actinide_volumes_bulk_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "rws_bohr",
          "bulk_modulus_gpa"
        ],
        "units": {}
      },
      "description": "Equilibrium Wigner-Seitz radii and bulk moduli for the fcc actinide series from LSDA+CPA DLM calculations."
    },
    {
      "file": "delta_plutonium_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "dos_states_per_eV_atom"
        ],
        "units": {}
      },
      "description": "Density of states for δ-Pu at equilibrium volume, computed from the self-consistent DLM calculation."
    }
  ],
  "notes": "The verifier checks radii and bulk moduli against reference values with tolerances, and verifies DOS structural features (peak positions, bandwidth)."
}
```

## How you are scored

A hidden verifier will independently inspect each scored artifact. The Wigner‑Seitz radii and bulk moduli are compared against reference LSDA+CPA DLM results with appropriate tolerances; the overall trend (volume increase at Pu, decrease for heavier elements) is also checked. The DOS is verified by its structural features: the positions of the main peaks relative to the Fermi level and the total bandwidth, without requiring exact intensity matching. The combined score from these checks forms your final reward.
