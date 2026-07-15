# DFT+U band gap predictions for kesterite photovoltaics using first-principles Hubbard parameters

## Problem background
Kesterite photovoltaic materials CZT (Cu₂ZnSnS₄) and CZGS (Cu₂ZnGeS₄) are promising for sustainable energy because of their earth-abundant elements and suitable optical properties. However, density functional theory (DFT) with the standard PBE functional predicts these materials to be near-metallic, severely underestimating the fundamental bandgap. More accurate methods such as hybrid functionals or self-consistent GW are computationally prohibitive for large simulation cells. The DFT+U approach can correct the bandgap provided the Hubbard U and Hund’s J parameters are determined from first principles rather than arbitrarily tuned. This task reproduces a first-principles workflow that computes these parameters via minimum‑tracking linear response and uses them to predict bandgaps and defect formation energies.

## Approach
The core idea is to apply Hubbard U corrections to all atomic subspaces that dominate the valence and conduction band edges—Cu 3d, S 3p, and Sn 5s (for CZTS) or Ge 4s (for CZGS)—instead of correcting only transition‑metal d‑states. First, bespoke norm‑conserving pseudopotentials are generated with the OPIUM code using the Rappe‑Rabe‑Kaxiras‑Joannopoulos algorithm. Then, using the ONETEP DFT code, minimum‑tracking linear‑response calculations are performed: spin‑resolved perturbations are applied to each target subspace, the linear‑response kernel is obtained, and the Hubbard U and Hund’s J parameters are regressed. With these ab‑initio parameters, DFT+U calculations are carried out on pristine unit cells using three different Hubbard‑corrected functionals: the simplified rotationally‑invariant Dudarev functional (PBE+U_eff), the extended Himmetoglu functional (PBE+U+J), and the flat‑plane‑based BLOR functional. Finally, a charge‑neutral Cu‑Zn anti‑site pair defect is introduced in a large supercell, and the frozen‑ion defect formation energy is obtained from total‑energy differences without geometry relaxation.

## Reproduction target
Compute the Hubbard U and Hund’s J parameters for Cu 3d, S 3p, and Sn 5s in CZTS, and for Cu 3d, S 3p, and Ge 4s in CZGS, using minimum‑tracking linear response. Then compute the fundamental bandgap of pristine CZTS and CZGS using the PBE+U_eff, PBE+U+J, and PBE+BLOR functionals. Finally, compute the frozen‑ion defect formation energy for the charge‑neutral Cu‑Zn anti‑site pair defect in a 1,728‑atom supercell. All results must be written to the specified CSV files according to the output contract.

## Assets

- ONETEP DFT code: https://github.com/ONETEP/onetep
- OPIUM pseudopotential generation code: https://opium.sourceforge.io
- Crystal structures of CZTS and CZGS: 10.1039/c9cp04280h

## Workflow steps

### Step 1: Generate norm-conserving pseudopotentials
- Role: process
- Action: Use OPIUM to generate norm-conserving pseudopotentials for Cu, Zn, Sn, Ge, S with the Rappe-Rabe-Kaxiras-Joannopoulos algorithm, a cutoff wavevector of 7.9 Ry^{1/2}, 10 Bessel functions, j-averaged scalar relativistic scheme, PBE functional, and partial core correction.
- Evidence: `/app/outputs/pseudopotential_generation.log`

### Step 2: Compute Hubbard U and Hund's J parameters
- Role: scored (load-bearing)
- Action: Using ONETEP and the generated pseudopotentials, perform minimum-tracking linear-response calculations for CZTS and CZGS. Apply spin-resolved perturbations to the Cu 3d, S 3p, Sn 5s (CZTS) and Ge 4s (CZGS) subspaces, compute the linear-response kernel, regress U and J, and output the values for each material-subspace combination.
- Output file: `/app/outputs/U_J_values.csv`
- Format: csv
- Contract: material,subspace,U,J
- Scoring: scored by hidden verifier

### Step 3: Compute band gaps of pristine kesterites
- Role: scored
- Action: Using ONETEP, the generated pseudopotentials, and the computed U/J parameters, perform DFT+U calculations on pristine CZTS and CZGS unit cells with the PBE+U_eff (Dudarev), PBE+U+J, and PBE+BLOR functionals; extract the fundamental band gap for each material-functional combination.
- Output file: `/app/outputs/bandgaps.csv`
- Format: csv
- Contract: material,functional,bandgap
- Scoring: scored by hidden verifier

### Step 4: Compute defect formation energy of Cu-Zn anti-site pair
- Role: scored
- Action: Construct a 1,728-atom supercell of pristine CZTS and CZGS, create the defect by swapping a neighboring Cu and Zn (no geometry relaxation), compute total energies for pristine and defective cells using ONETEP with PBE+U_eff, and output the frozen-ion defect formation energy as the energy difference.
- Output file: `/app/outputs/defect_formation_energies.csv`
- Format: csv
- Contract: material,formation_energy
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/U_J_values.csv`
- `/app/outputs/bandgaps.csv`
- `/app/outputs/defect_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### U_J_values.csv
- path: `/app/outputs/U_J_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Hubbard U and Hund's J parameters for Cu 3d, S 3p, Sn 5s (CZTS) and Ge 4s (CZGS) subspaces, computed via minimum-tracking linear response.
- schema:
  - `type`: table
  - `required_columns`: `material`, `subspace`, `U`, `J`
  - `units`:
    - `U`: eV
    - `J`: eV

### bandgaps.csv
- path: `/app/outputs/bandgaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fundamental band gaps of pristine CZTS and CZGS computed with PBE+U_eff, PBE+U+J, and PBE+BLOR functionals.
- schema:
  - `type`: table
  - `required_columns`: `material`, `functional`, `bandgap`
  - `units`:
    - `bandgap`: eV

### defect_formation_energies.csv
- path: `/app/outputs/defect_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Frozen-ion defect formation energy for the charge-neutral Cu-Zn anti-site pair in CZTS and CZGS.
- schema:
  - `type`: table
  - `required_columns`: `material`, `formation_energy`
  - `units`:
    - `formation_energy`: eV

Notes: All values are compared to hidden reference values from the paper within strict tolerances. The pseudopotential generation step is required for reproducibility but not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "U_J_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "subspace",
          "U",
          "J"
        ],
        "units": {
          "U": "eV",
          "J": "eV"
        }
      },
      "description": "Hubbard U and Hund's J parameters for Cu 3d, S 3p, Sn 5s (CZTS) and Ge 4s (CZGS) subspaces, computed via minimum-tracking linear response."
    },
    {
      "file": "bandgaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "functional",
          "bandgap"
        ],
        "units": {
          "bandgap": "eV"
        }
      },
      "description": "Fundamental band gaps of pristine CZTS and CZGS computed with PBE+U_eff, PBE+U+J, and PBE+BLOR functionals."
    },
    {
      "file": "defect_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "eV"
        }
      },
      "description": "Frozen-ion defect formation energy for the charge-neutral Cu-Zn anti-site pair in CZTS and CZGS."
    }
  ],
  "notes": "All values are compared to hidden reference values from the paper within strict tolerances. The pseudopotential generation step is required for reproducibility but not directly scored."
}
```

## How you are scored
A hidden verifier reads your three output CSV files and checks their structure. Each numerical entry—every Hubbard U, Hund’s J, bandgap, and formation energy—is compared to hidden reference values. You receive full credit when your computed value falls within a prescribed absolute tolerance of the reference; the reward degrades only when the deviation exceeds the tolerance (threshold‑or‑better scoring). Additionally, the verifier inspects the relative ordering of the bandgaps across the three functionals and expects a specific physical trend. The final score is a weighted average of the per‑entry rewards. Simply writing the known literature numbers without running the described calculations will not satisfy the task because the verifier’s hidden references are generated independently and the ordering check requires consistency that a genuine computation naturally produces.
