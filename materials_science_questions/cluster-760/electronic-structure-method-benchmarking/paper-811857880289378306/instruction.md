# Conformer energies, rotational barriers, and enthalpy of formation of cumene hydroperoxide via DFT

## Problem background
Cumene hydroperoxide (PhCMe2OOH) is an important intermediate in hydrocarbon oxidation and polymerization. Experimental determination of its gas-phase enthalpy of formation is challenging due to the molecule’s instability and rapid conformational interconversion. Computational approaches using density functional theory (DFT) offer a viable route to obtain thermodynamic data. This task focuses on reproducing the conformer analysis, internal rotational barriers, and the enthalpy of formation of cumene hydroperoxide via DFT calculations and an isodesmic reaction scheme.

## Approach
The workflow uses the B3LYP exchange-correlation functional in combination with two basis sets (6‑31G(d,p) and 6‑311+G(3df,2p)). The procedure involves:

- Conformational search to locate the seven distinct stable conformers (ignoring methyl rotations).
- Geometry optimizations and harmonic vibrational frequency calculations at the B3LYP/6‑31G(d,p) level.
- Application of zero‑point vibrational energy and thermal corrections (scale factor for frequencies, free‑rotator model for low‑frequency torsional modes).
- Single‑point energy calculations at the larger basis set B3LYP/6‑311+G(3df,2p) on the optimized geometries.
- Calculation of identical quantities for ten reference species that appear in the isodesmic reactions.
- Construction of three isodesmic reactions that conserve the number and type of chemical bonds, thereby reducing systematic errors in the computed reaction enthalpies.
- Derivation of per‑conformer enthalpies of formation ΔfH(298 K) from the isodesmic reaction enthalpies and known experimental formation enthalpies of the reference compounds.
- Evaluation of relative conformer energies (ΔE), Boltzmann populations at 298 K, and the ensemble‑averaged ΔfH(298 K) of cumene hydroperoxide.
- Relaxed potential energy scans to determine the barriers to internal rotation about the C(4)–C(5), C(4)–O(2), O(2)–O(1), and C(3)–C(4) bonds.

All computations are performed with an open‑source quantum chemistry package (ORCA recommended). Reference thermochemical data are retrieved from public databases.

## Reproduction target
For the seven distinct conformers of cumene hydroperoxide (A‑I, A‑II, B‑I, B‑II, B‑III, C, D), compute:
- relative electronic energies ΔE (kcal mol⁻¹) including zero‑point and thermal corrections at both B3LYP/6‑31G(d,p) and B3LYP/6‑311+G(3df,2p) levels,
- Boltzmann populations at 298 K,
- per‑conformer enthalpies of formation ΔfH(298 K) via the isodesmic reaction scheme, averaged over the three reactions.

Also compute the barrier heights (kcal mol⁻¹) for internal rotation about the C(4)–C(5), C(4)–O(2), O(2)–O(1), and C(3)–C(4) bonds. Finally, report the Boltzmann‑weighted ensemble enthalpy of formation ΔfH(298 K) of cumene hydroperoxide.

## Assets

- ORCA quantum chemistry package (version 5.0 or later): https://orcaforum.kofo.mpg.de/
- Experimental enthalpies of formation for reference compounds: https://webbook.nist.gov/chemistry/
- Molecular builder (optional): openbabel

## Workflow steps

### Step 1: Intramolecular rotational barriers from DFT scans
- Role: scored
- Action: Perform relaxed potential energy scans at B3LYP/6-31G(d,p) for rotations about the C(4)–C(5), C(4)–O(2), O(2)–O(1), and C(3)–C(4) bonds of cumene hydroperoxide. Extract the highest barrier for the A→B transformation and the methyl group rotation barrier. Report the barrier heights in kcal mol⁻¹.
- Output file: `/app/outputs/barrier_heights.csv`
- Format: csv
- Contract: columns: rotation (string, description of the bond scanned, e.g., 'C4-C5', 'C4-O2', 'O2-O1', 'C3-C4'), barrier_height (float, kcal/mol).
- Scoring: scored by hidden verifier

### Step 2: Conformer geometry optimization and frequency analysis
- Role: process
- Action: Identify the seven distinct conformers A-I, A-II, B-I, B-II, B-III, C, D of cumene hydroperoxide through conformational sampling. Perform full geometry optimization and harmonic vibrational frequency calculation at B3LYP/6-31G(d,p) for each conformer. Verify that all structures correspond to minima (no imaginary frequencies).
- Evidence: `/app/outputs/conformer_structures.xyz`

### Step 3: Zero-point vibrational energy and thermal corrections
- Role: process
- Action: Apply the scale factor 0.9806 to the harmonic frequencies to obtain zero-point vibrational energy (ZPVE). Use the free-rotator model for low-frequency torsional modes (frequency < 250 cm⁻¹) to compute the thermal enthalpy correction at 298 K (0.296 kcal/mol per mode).
- Evidence: none

### Step 4: Single-point energies at larger basis set
- Role: process
- Action: Using the optimized geometries from step_02, perform single-point total electronic energy calculations at the B3LYP/6-311+G(3df,2p) level for all seven conformers.
- Evidence: none

### Step 5: Reference molecule calculations for isodesmic reactions
- Role: process
- Action: For each reference species (CH4, Me2CHOOH, PhCH3, Bu^tOH, C6H6, PhOH, HOOH, H2O, Bu^tOOH, MeOOH), perform geometry optimization, frequency calculation, and single-point energy calculations at B3LYP/6-31G(d,p) and B3LYP/6-311+G(3df,2p). Apply the same zero-point and thermal corrections as in step_03. Compute the enthalpy of each isodesmic reaction (IDRs 1–3).
- Evidence: `/app/outputs/reference_energies.json`

### Step 6: Conformer relative energies, populations, and per-conformer enthalpies
- Role: scored (load-bearing)
- Action: Using the total electronic energies (both basis sets) and the zero-point/temperature corrections for each conformer, compute the relative energy ΔE (kcal mol⁻¹) referenced to conformer A. Construct a Boltzmann distribution at T=298 K from the ΔE values to obtain the room-temperature populations. Using the reference molecule energies and the known experimental gas-phase enthalpies of formation (as reported in the paper’s Table 3), compute the per-conformer enthalpy of formation ΔfH(298 K) via isodesmic reactions (1)–(3) and average over the three reactions. Write all values to conformer_energies_populations.csv.
- Output file: `/app/outputs/conformer_energies_populations.csv`
- Format: csv
- Contract: columns: conformer (string, one of A-I, A-II, B-I, B-II, B-III, C, D), deltaE_631Gdp (float, kcal/mol), deltaE_6311PlusG3df2p (float, kcal/mol), Boltzmann_population (float, dimensionless), deltaH_formation (float, kcal/mol).
- Scoring: scored by hidden verifier

### Step 7: Ensemble-weighted enthalpy of formation
- Role: scored
- Action: Weight the per-conformer ΔfH values by the Boltzmann population of each conformer to obtain the overall gas-phase enthalpy of formation ΔfH(298 K) of cumene hydroperoxide. Write the single value to ensemble_enthalpy.txt.
- Output file: `/app/outputs/ensemble_enthalpy.txt`
- Format: txt
- Contract: a single float value (kcal mol⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barrier_heights.csv`
- `/app/outputs/conformer_energies_populations.csv`
- `/app/outputs/ensemble_enthalpy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barrier_heights.csv
- path: `/app/outputs/barrier_heights.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Extracted intramolecular rotational barrier heights. The checker compares the reported results to hidden reference values with a defined tolerance.
- schema:
  - `type`: table
  - `required_columns`: `rotation`, `barrier_height`
  - `units`:
    - `barrier_height`: kcal/mol

### conformer_energies_populations.csv
- path: `/app/outputs/conformer_energies_populations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-conformer relative energies (ΔE) at two basis sets, Boltzmann populations at 298 K, and average enthalpies of formation from isodesmic reactions. The checker compares each value to hidden reference values within defined tolerances.
- schema:
  - `type`: table
  - `required_columns`: `conformer`, `deltaE_631Gdp`, `deltaE_6311PlusG3df2p`, `Boltzmann_population`, `deltaH_formation`
  - `units`:
    - `deltaE_631Gdp`: kcal/mol
    - `deltaE_6311PlusG3df2p`: kcal/mol
    - `Boltzmann_population`: dimensionless
    - `deltaH_formation`: kcal/mol

### ensemble_enthalpy.txt
- path: `/app/outputs/ensemble_enthalpy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Boltzmann-weighted gas-phase enthalpy of formation ΔfH(298 K) of cumene hydroperoxide. The checker compares the single number to the hidden reference value.
- schema:
  - `type`: text
  - `units`: kcal/mol

Notes: All scored artifacts are compared against hidden reference values obtained from the original paper. The agent must compute them from scratch using the described DFT workflow; no pre-computed values are provided. The load-bearing step_06 ensures that upstream process steps (geometry optimization, frequency calculations, single-point energies, reference molecule calculations) are genuinely executed because the final populations and enthalpies depend on these intermediate energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barrier_heights.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rotation",
          "barrier_height"
        ],
        "units": {
          "barrier_height": "kcal/mol"
        }
      },
      "description": "Extracted intramolecular rotational barrier heights. The checker compares the reported results to hidden reference values with a defined tolerance."
    },
    {
      "file": "conformer_energies_populations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "conformer",
          "deltaE_631Gdp",
          "deltaE_6311PlusG3df2p",
          "Boltzmann_population",
          "deltaH_formation"
        ],
        "units": {
          "deltaE_631Gdp": "kcal/mol",
          "deltaE_6311PlusG3df2p": "kcal/mol",
          "Boltzmann_population": "dimensionless",
          "deltaH_formation": "kcal/mol"
        }
      },
      "description": "Per-conformer relative energies (ΔE) at two basis sets, Boltzmann populations at 298 K, and average enthalpies of formation from isodesmic reactions. The checker compares each value to hidden reference values within defined tolerances."
    },
    {
      "file": "ensemble_enthalpy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "kcal/mol"
      },
      "description": "Boltzmann-weighted gas-phase enthalpy of formation ΔfH(298 K) of cumene hydroperoxide. The checker compares the single number to the hidden reference value."
    }
  ],
  "notes": "All scored artifacts are compared against hidden reference values obtained from the original paper. The agent must compute them from scratch using the described DFT workflow; no pre-computed values are provided. The load-bearing step_06 ensures that upstream process steps (geometry optimization, frequency calculations, single-point energies, reference molecule calculations) are genuinely executed because the final populations and enthalpies depend on these intermediate energies."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that examines each scored artifact (barrier_heights.csv, conformer_energies_populations.csv, ensemble_enthalpy.txt). The verifier compares your reported numerical results against hidden expected values, applying tolerances appropriate for the method. Each artifact contributes a weighted portion to the total reward, with the ensemble enthalpy and per‑conformer relative energies/populations receiving the largest weights. The verifier does not re‑run any computations; it checks the final answers. However, the workflow steps are mandatory — you must genuinely perform the geometry optimizations, frequency calculations, single‑point energies, and reference molecule calculations, as the hidden checker may inspect intermediate evidence. Reporting numbers that fall within the expected tolerances earns full credit; results outside the tolerances may receive partial credit if they show the correct qualitative trends (e.g., correct ordering of conformer stabilities).
