# First-principles electronic and magnetic properties of Sr2BB'O5 brownmillerites

## Problem background
Brownmillerite oxides ABO₂.₅ exhibit tunable structural, electronic, and magnetic properties that make them promising for spintronics and redox applications. This task investigates the series Sr₂BB'O₅ (B = Fe, Co, Ni; B' = Co, Ni, Mn), which has two transition metals at the B-site. The goal is to determine the thermodynamic and dynamic stability, electronic structure, and magnetic interactions of these compounds using first‑principles DFT+U calculations. The key open questions are: Which compositions are stable in the brownmillerite structure? What are their electronic (insulator vs half‑metal) and magnetic ground states, and what are the signs and strengths of the magnetic exchange couplings?

## Approach
The computational approach uses density functional theory with the GGA‑PBE functional and a Hubbard U correction (U=4 eV) on the 3d states of the transition metals, implemented via an open‑source plane‑wave code with PAW pseudopotentials. The workflow systematically explores the energy landscape: for each of the six Sr₂BB'O₅ compounds, total energies are computed for all combinations of four structural space groups (Icmm, Ibm2, Pnma, Pbcm), two B‑site cation orderings (along the [100] and [010] crystal directions), and four magnetic configurations (ferromagnetic FM, A‑type antiferromagnetic A‑AFM, C‑type C‑AFM, and G‑type G‑AFM). The configuration with the lowest total energy is taken as the candidate ground state. Formation energies are then calculated by subtracting the total energies of the reference binary oxides (SrO, FeO, CoO, NiO, MnO) computed with the same DFT settings. For compounds with negative formation energies (thermodynamically stable), phonon spectra are calculated using finite‑displacement forces and Phonopy to check for imaginary modes, which would indicate dynamic instability. For the dynamically stable compounds, electronic density of states and band structure are computed to classify them as insulator or half‑metal and to extract the band gap. Finally, the energies of the different magnetic configurations for the ground‑state structures are mapped onto a Heisenberg model to derive the magnetic exchange constants J between the transition‑metal ions.

## Reproduction target
By performing the DFT+U calculations as described, produce the following results for the Sr₂BB'O₅ series:
- The ground‑state space group, B‑site ordering direction, magnetic order, and formation energy (in meV per formula unit) for each compound.
- For thermodynamically stable compounds, a determination of dynamical stability (absence of imaginary phonon modes).
- For dynamically stable compounds, the magnetic ordering pattern, electronic type (insulator or half‑metal), and band gap (in eV).
- The magnetic exchange constants (in meV) for the stable compounds, obtained from the Heisenberg model fit.

All outputs must follow the exact file formats described in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- ASE (Atomic Simulation Environment): https://wiki.fysik.dtu.dk/ase/
- Pseudopotentials for Quantum ESPRESSO: https://www.quantum-espresso.org/pseudopotentials
- Crystal structure information for Sr2BB'O5 and reference oxides

## Workflow steps

### Step 1: DFT total-energy survey for all Sr2BB'O5 configurations
- Role: process
- Action: Perform DFT calculations (GGA-PBE+U with U=4 eV on the 3d transition-metal atoms) for all six Sr2BB'O5 compounds (B = Fe, Co, Ni; B' = Co, Ni, Mn) across four structural space groups (Icmm, Ibm2, Pnma, Pbcm), two B-site ordering directions ([100] and [010]), and four magnetic configurations (FM, A-AFM, C-AFM, G-AFM). Relax structures and collect total energies.
- Evidence: `/app/outputs/dft_survey_energies.txt`

### Step 2: DFT calculations for reference binary oxides
- Role: process
- Action: Compute the total energies of SrO, FeO, CoO, NiO, and MnO using the same DFT settings (PBE+U, U=4 eV on 3d elements) and pseudopotentials as in step 1. These energies serve as references for formation energy calculations.
- Evidence: `/app/outputs/binary_oxide_energies.txt`

### Step 3: Ground-state assignment and formation energies
- Role: scored (load-bearing)
- Action: For each Sr2BB'O5 compound, select the configuration with the lowest DFT total energy as the ground state. Compute formation energies E_form = E(compound) - sum of reference oxide energies. Output a CSV file listing compound, space group, B-site ordering axis, magnetic order, and formation energy (meV per formula unit).
- Output file: `/app/outputs/step_02_ground_states.csv`
- Format: csv
- Contract: compound (str), space_group (one of Icmm,Ibm2,Pnma,Pbcm), b_site_ordering (100 or 010), magnetic_order (FM,A-AFM,C-AFM,G-AFM), formation_energy_meV_per_fu (float)
- Scoring: scored by hidden verifier

### Step 4: Phonon stability analysis
- Role: scored
- Action: For each compound with a negative formation energy (thermodynamically stable), compute phonon dispersion using finite-displacement forces from DFT (Phonopy) and check for imaginary modes. Output a text file indicating for each such compound whether it is dynamically stable (true/false).
- Output file: `/app/outputs/step_03_phonon_stability.txt`
- Format: txt
- Contract: One line per compound: `compound:dynamically_stable` where `dynamically_stable` is true or false.
- Scoring: scored by hidden verifier

### Step 5: Electronic structure of stable compounds
- Role: scored
- Action: For the two dynamically stable compounds Sr2FeCoO5 and Sr2NiMnO5, compute density of states and band structure using the same DFT settings. Determine magnetic ordering type, electronic type (insulator or half-metal), and the band gap (eV). Output a CSV file with compound, magnetic_ordering, electronic_type, bandgap_eV.
- Output file: `/app/outputs/step_04_electronic_summary.csv`
- Format: csv
- Contract: compound (str), magnetic_ordering (G-AFM or A-AFM), electronic_type (insulator or half-metal), bandgap_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Heisenberg exchange constants
- Role: scored
- Action: For Sr2FeCoO5 and Sr2NiMnO5, extract the total energies of the four magnetic configurations (FM, A-AFM, C-AFM, G-AFM) for the ground-state structural arrangement. Fit these energies to the Heisenberg model equations to obtain the magnetic exchange constants J for each compound. Output a CSV with compound, interaction, and value in meV.
- Output file: `/app/outputs/step_05_exchange_constants.csv`
- Format: csv
- Contract: compound (str), interaction (str), value_meV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_ground_states.csv`
- `/app/outputs/step_03_phonon_stability.txt`
- `/app/outputs/step_04_electronic_summary.csv`
- `/app/outputs/step_05_exchange_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_ground_states.csv
- path: `/app/outputs/step_02_ground_states.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ground-state structural, magnetic, and formation energy data for all six Sr2BB'O5 compounds. The checker compares space group, B-site ordering, magnetic order exactly; formation energy sign must match paper (negative/positive).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `space_group`, `b_site_ordering`, `magnetic_order`, `formation_energy_meV_per_fu`
  - `units`:
    - `formation_energy_meV_per_fu`: meV

### step_03_phonon_stability.txt
- path: `/app/outputs/step_03_phonon_stability.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Dynamical stability verdict for thermodynamically stable compounds. Exact match against paper-verified list of dynamically stable systems is required.
- schema:
  - `type`: text
  - `pattern`: One line per compound: compound:dynamically_stable (true/false)

### step_04_electronic_summary.csv
- path: `/app/outputs/step_04_electronic_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electronic structure summary for the two dynamically stable compounds. The checker verifies magnetic ordering and electronic type exactly; bandgap is compared within a tolerance relative to paper values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `magnetic_ordering`, `electronic_type`, `bandgap_eV`
  - `units`:
    - `bandgap_eV`: eV

### step_05_exchange_constants.csv
- path: `/app/outputs/step_05_exchange_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Heisenberg exchange constants for Sr2FeCoO5 and Sr2NiMnO5. The checker compares sign and approximate magnitude (tolerances absorb cross-code differences) against paper-reported J values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `interaction`, `value_meV`
  - `units`:
    - `value_meV`: meV

Notes: All scored artifacts are compared against paper-reported values with appropriate tolerances and sign checks to account for cross-code (Quantum ESPRESSO vs VASP) reproduction differences. Structural/magnetic assignments and dynamical stability require exact match; bandgap and exchange constants use tolerant comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_ground_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "space_group",
          "b_site_ordering",
          "magnetic_order",
          "formation_energy_meV_per_fu"
        ],
        "units": {
          "formation_energy_meV_per_fu": "meV"
        }
      },
      "description": "Ground-state structural, magnetic, and formation energy data for all six Sr2BB'O5 compounds. The checker compares space group, B-site ordering, magnetic order exactly; formation energy sign must match paper (negative/positive)."
    },
    {
      "file": "step_03_phonon_stability.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "pattern": "One line per compound: compound:dynamically_stable (true/false)"
      },
      "description": "Dynamical stability verdict for thermodynamically stable compounds. Exact match against paper-verified list of dynamically stable systems is required."
    },
    {
      "file": "step_04_electronic_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "magnetic_ordering",
          "electronic_type",
          "bandgap_eV"
        ],
        "units": {
          "bandgap_eV": "eV"
        }
      },
      "description": "Electronic structure summary for the two dynamically stable compounds. The checker verifies magnetic ordering and electronic type exactly; bandgap is compared within a tolerance relative to paper values."
    },
    {
      "file": "step_05_exchange_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "interaction",
          "value_meV"
        ],
        "units": {
          "value_meV": "meV"
        }
      },
      "description": "Heisenberg exchange constants for Sr2FeCoO5 and Sr2NiMnO5. The checker compares sign and approximate magnitude (tolerances absorb cross-code differences) against paper-reported J values."
    }
  ],
  "notes": "All scored artifacts are compared against paper-reported values with appropriate tolerances and sign checks to account for cross-code (Quantum ESPRESSO vs VASP) reproduction differences. Structural/magnetic assignments and dynamical stability require exact match; bandgap and exchange constants use tolerant comparison."
}
```

## How you are scored
Your submission will be evaluated by a hidden automatic verifier. The verifier independently checks each of the four scored output files (ground states, phonon stability, electronic summary, exchange constants) against reference results derived from the published study, allowing tolerances that reflect the expected spread between different DFT implementations. Each scored artifact is weighted equally in the final reward (0–1). Simply copying numbers from the literature will not pass – the verifier expects the artifacts to be internally consistent with an actual computation conducted with the specified DFT setup. Make sure all required output files are present and correctly formatted.
