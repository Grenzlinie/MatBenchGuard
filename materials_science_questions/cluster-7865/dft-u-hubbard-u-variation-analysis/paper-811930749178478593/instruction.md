# First-Principles Calculation of Structural and Electronic Properties of Plutonium Intermetallic Compounds

## Problem background
Plutonium intermetallic compounds Pu3M and PuM3 (M = Ga, In, Sn, Ge) are model systems for understanding the factors that stabilise Pu-based alloys, especially delta-phase stabilisers. First-principles density-functional-theory (DFT) calculations can reveal how electronic structure, hybridisation, and thermodynamic properties such as formation heat depend on composition and on the choice of alloying element.

## Approach
The workflow uses all-electron full-potential linearised augmented-plane-wave (FPLAPW) calculations with the PBE96 generalised-gradient approximation (GGA), including spin-orbit coupling and spin polarisation. For each pure element (Pu, Ga, In, Sn, Ge) and each AuCu3-type compound (Pu3Ga, Pu3In, Pu3Sn, PuIn3, PuSn3, PuGe3), initial crystal structures are generated from known experimental space groups and lattice constants. A series of total-energy calculations at different volumes is performed; the equilibrium lattice constant and bulk modulus are obtained by fitting the energy-volume data to Murnaghan's equation of state. Self-consistent electronic structure calculations at the equilibrium volumes then yield partial densities of states (DOS) projected onto s, p, d, and f orbitals for both spin channels. From the partial DOS of the Pu3M compounds, we extract the energy gap that separates localised M s states from the bottom of the valence band. Finally, formation heats are computed as the difference between the total energy of each compound and the stoichiometrically weighted sum of the pure-element total energies.

## Reproduction target
Produce three CSV files under `/app/outputs`:
1. `lattice_parameters.csv` – columns: `compound`, `a_calc` (Å), `B0_calc` (GPa). One row for each of the 11 systems: Pu, Ga, In, Sn, Ge, Pu3Ga, Pu3In, Pu3Sn, PuIn3, PuSn3, PuGe3.
2. `gap_widths.csv` – columns: `compound`, `gap_width` (eV). One row for each of the three Pu3M compounds: Pu3In, Pu3Ga, Pu3Sn. If no gap is present, set `gap_width` to 0.
3. `formation_heats.csv` – columns: `compound`, `formation_heat` (eV). One row for each of the six compounds: Pu3In, Pu3Ga, Pu3Sn, PuIn3, PuSn3, PuGe3.
All values are obtained by following the workflow steps below.

## Assets

- Elk FPLAPW code: https://elk.sourceforge.net/
- Experimental crystal structures of elements and compounds

## Workflow steps

### Step 1: Generate initial crystal structures
- Role: process
- Action: Create input crystal structure files for DFT for all pure elements (Pu, Ga, In, Sn, Ge) and the six intermetallic compounds (Pu3Ga, Pu3In, Pu3Sn, PuIn3, PuSn3, PuGe3) using the experimental space groups and lattice parameters specified in the instructions.
- Evidence: none

### Step 2: Equilibrium structure optimization
- Role: scored
- Action: For each system, perform total-energy DFT calculations at several volumes using the FPLAPW method with GGA (PBE96) including spin-orbit coupling and spin polarization. Fit the total-energy vs volume data to Murnaghan's equation of state to obtain the equilibrium lattice constant a and bulk modulus B0.
- Output file: `/app/outputs/lattice_parameters.csv`
- Format: csv
- Contract: CSV with columns: compound (string), a_calc (float, Angstrom), B0_calc (float, GPa). Compounds: Pu, Ga, In, Sn, Ge, Pu3Ga, Pu3In, Pu3Sn, PuIn3, PuSn3, PuGe3.
- Scoring: scored by hidden verifier

### Step 3: Electronic structure and DOS calculation
- Role: process
- Action: At the equilibrium volumes obtained in step 02, perform self-consistent FPLAPW calculations for the six compounds and compute partial density of states (DOS) projected onto s, p, d, f orbitals for both spin channels.
- Evidence: `/app/outputs/dos_calculations.log`

### Step 4: Gap width extraction from DOS
- Role: scored (load-bearing)
- Action: From the partial DOS computed in step 03, identify the energy gap that separates the localized M s states from the bottom of the valence band in Pu3M compounds (Pu3In, Pu3Ga, Pu3Sn). Measure the gap width in eV; if no such gap is present for a compound, set the gap width to 0.
- Output file: `/app/outputs/gap_widths.csv`
- Format: csv
- Contract: CSV with columns: compound (string), gap_width (float, eV). Compounds: Pu3In, Pu3Ga, Pu3Sn.
- Scoring: scored by hidden verifier

### Step 5: Formation heat calculation
- Role: scored
- Action: Using the equilibrium total energies of the compounds and pure elements obtained in step 02, compute the formation heats according to: E^f(Pu3M) = E(Pu3M) - 0.75*E(Pu) - 0.25*E(M) and E^f(PuM3) = E(PuM3) - 0.25*E(Pu) - 0.75*E(M). Report the formation heat in eV.
- Output file: `/app/outputs/formation_heats.csv`
- Format: csv
- Contract: CSV with columns: compound (string), formation_heat (float, eV). Compounds: Pu3In, Pu3Ga, Pu3Sn, PuIn3, PuSn3, PuGe3.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.csv`
- `/app/outputs/gap_widths.csv`
- `/app/outputs/formation_heats.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.csv
- path: `/app/outputs/lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimised lattice constants and bulk moduli for Pu, Ga, In, Sn, Ge, Pu3Ga, Pu3In, Pu3Sn, PuIn3, PuSn3, PuGe3.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a_calc`, `B0_calc`
  - `units`:
    - `a_calc`: Angstrom
    - `B0_calc`: GPa

### gap_widths.csv
- path: `/app/outputs/gap_widths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Gap widths for Pu3In, Pu3Ga, Pu3Sn.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `gap_width`
  - `units`:
    - `gap_width`: eV

### formation_heats.csv
- path: `/app/outputs/formation_heats.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation heats of Pu3In, Pu3Ga, Pu3Sn, PuIn3, PuSn3, PuGe3.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `formation_heat`
  - `units`:
    - `formation_heat`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a_calc",
          "B0_calc"
        ],
        "units": {
          "a_calc": "Angstrom",
          "B0_calc": "GPa"
        }
      },
      "description": "Optimised lattice constants and bulk moduli for Pu, Ga, In, Sn, Ge, Pu3Ga, Pu3In, Pu3Sn, PuIn3, PuSn3, PuGe3."
    },
    {
      "file": "gap_widths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "gap_width"
        ],
        "units": {
          "gap_width": "eV"
        }
      },
      "description": "Gap widths for Pu3In, Pu3Ga, Pu3Sn."
    },
    {
      "file": "formation_heats.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "formation_heat"
        ],
        "units": {
          "formation_heat": "eV"
        }
      },
      "description": "Formation heats of Pu3In, Pu3Ga, Pu3Sn, PuIn3, PuSn3, PuGe3."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads each CSV file and compares every numeric value to a hidden reference. The reward is the fraction of values across all three files that fall within the verifier's predetermined tolerances. Qualitative features of the density of states are not scored.
