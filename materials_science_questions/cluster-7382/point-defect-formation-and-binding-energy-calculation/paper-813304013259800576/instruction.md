# Formation and migration energies of point defects in silicon using range-separated random-phase approximation

## Problem background
The random-phase approximation (RPA) is a many-body method for the exchange-correlation energy of density functional theory that correctly captures van der Waals interactions and yields improved band gaps. However, RPA calculations are computationally very demanding, limiting their application to small systems. A range-separation technique has been proposed that splits the Coulomb interaction into a short-range part (treated within a local density approximation) and a long-range part (evaluated explicitly with RPA), drastically reducing the computational cost while preserving accuracy. This technique is applied to compute atomization energies of a set of crystals, the van der Waals binding in hexagonal boron nitride (h-BN), and the formation and migration energies of point defects (self-interstitials and vacancies) in silicon. The defect calculations in large supercells are particularly important because standard density functional approximations suffer from the band gap problem and yield unreliable formation and migration energies. Obtaining accurate defect energetics with an affordable RPA scheme can help resolve the long-standing experimental controversy about self-diffusion mechanisms in silicon.

## Approach
The method is based on a range-separated RPA correlation energy. The Coulomb potential is divided into short-range and long-range parts using a complementary error-function split controlled by a cutoff radius r_c. The total RPA correlation energy is expressed as the sum of three contributions: (i) the RPA correlation energy density of the homogeneous electron gas (jellium) under the full Coulomb interaction, (ii) subtracted by the correlation energy density of jellium under the long-range-only interaction, both evaluated with the local electronic density, and (iii) the explicitly computed long-range RPA correlation energy using the Kohn-Sham wavefunctions and eigenvalues.

To implement this, you must first parametrize the jellium long-range RPA correlation energy density by numerically integrating the RPA response equations for the homogeneous electron gas with the long-range Coulomb interaction over a dense grid of densities and cutoff radii r_c, and fitting a Padé approximant to obtain a functional ε_c^{LR-RPA,jellium}(n, r_c).

For real systems, perform standard density functional theory (LDA or PBE) calculations to obtain ground-state charge densities, Kohn-Sham orbitals, and eigenvalues for the bulk crystals, isolated atoms, and for hexagonal BN as a function of interlayer spacing. Compute the explicit long-range RPA correlation from these wavefunctions for each cutoff radius. Then use the fitted jellium functional and the explicit long-range RPA energy to compute the total RPA correlation energy via the three-term formula.

Atomization energies are obtained as the difference between the total energy of the bulk crystal (per atom) and the isolated atom. For h-BN, map the total energy versus interlayer spacing and fit to extract the equilibrium spacing d_0 and the out-of-plane elastic constant C_33.

For silicon defects, construct supercells (16, 64, 216 atoms) with a self-interstitial in the split<110> and hexagonal configurations, and with a vacancy. Relax atomic positions using LDA forces (the vacancy requires a manual Jahn-Teller distortion relaxation). For the 64-atom supercell, compute minimum-energy paths for the migration pathways split<110> → hex and hex → hex using a climbing-image nudged elastic band method (or equivalent) with LDA forces. Finally, compute the RPA correlation energies for the perfect and defect supercells, and evaluate formation energies as E^f = E(defect) − E(bulk) + Σ ν_i μ_i with μ_Si from bulk silicon. Extract migration barriers as the energy difference along the path.

## Reproduction target
Your goal is to compute and report the following quantities using the range-separated RPA scheme:

1. Atomization energies (eV/atom) of the bulk crystals Al, Si, β-SiC, diamond, w-AlN, and c-BN, for cutoff radii r_c = 0.5, 1.0, 2.0 bohr and for the full RPA limit (r_c → 0). Write these to `step_01_atomization_energies.json`.

2. The equilibrium interlayer spacing d_0 (bohr) and elastic constant C_33 (GPa) of hexagonal boron nitride for cutoff radii r_c = 1.0, 2.0, 4.0 bohr and for the full RPA limit. Write these to `step_02_hBN_interlayer.csv` as one row per r_c.

3. Formation energies (eV) of the silicon self-interstitial in the split<110> configuration, the self-interstitial in the hexagonal configuration, and the single vacancy, computed in 16-atom, 64-atom, and 216-atom supercells. Additionally, for the 64-atom supercell, report the migration barriers (eV) for the split<110> → hex path, the hex → hex path, and the vacancy migration path. Write these to `step_03_defect_energies.json`.

## Assets

- ABINIT: https://www.abinit.org
- Quantum ESPRESSO: https://www.quantum-espresso.org
- Pseudopotentials (PSlibrary or equivalent): https://www.quantum-espresso.org/pseudopotentials
- Crystal structures (Si, Al, β-SiC, diamond, w-AlN, c-BN, h-BN lattice parameters)

## Workflow steps

### Step 1: Parametrization of jellium LR-RPA correlation energy functional
- Role: process
- Action: Numerically integrate the RPA correlation energy for the homogeneous electron gas (jellium) with the long-range Coulomb interaction (erfc split) for a dense grid of densities and cutoff radii r_c. Fit a Padé approximant to obtain ε_c^{LR-RPA,jellium}(n, r_c).
- Evidence: `/app/outputs/s00_jellium_fit.log`

### Step 2: DFT calculations for bulk crystals and isolated atoms
- Role: process
- Action: Perform DFT (LDA or PBE) self-consistent calculations for the bulk crystals Al, Si, β-SiC, diamond, w-AlN, c-BN and for the corresponding isolated atoms (Al, Si, C, N, B) using converged plane-wave cutoffs and k-point grids. Save Kohn-Sham wavefunctions, eigenvalues, and densities.
- Evidence: none

### Step 3: Atomization energies via range-separated RPA
- Role: scored
- Action: For each crystal and atom, compute the total range-separated RPA correlation energy using the fitted jellium functional and the explicit LR-RPA correlation energy evaluated from the DFT wavefunctions. Obtain total atomization energy as E_bulk - E_atom (including kinetic and exchange contributions). Evaluate for cutoff radii r_c = 0.5, 1.0, 2.0 bohr and for the full RPA limit.
- Output file: `/app/outputs/step_01_atomization_energies.json`
- Format: json
- Contract: { "type": "array", "items": { "type": "object", "properties": { "crystal": {"type": "string"}, "rc": {"type": "number"}, "E_atomization_RPA": {"type": "number", "unit": "eV/atom"} }, "required": ["crystal", "rc", "E_atomization_RPA"] } }
- Scoring: scored by hidden verifier

### Step 4: DFT calculations for h-BN interlayer configurations
- Role: process
- Action: Perform DFT (LDA/PBE) total energy calculations for hexagonal BN with a series of interlayer spacings (c/2 from ~3.0 to ~5.5 bohr) to map the energy vs spacing curve. Save wavefunctions and densities.
- Evidence: none

### Step 5: h-BN interlayer spacing and elastic constant from range-separated RPA
- Role: scored
- Action: Compute the total range-separated RPA energy for each spacing using the same method and functional. Fit the total energy vs spacing to extract the equilibrium interlayer spacing d_0 and the elastic constant C_33. Use cutoff radii r_c = 1.0, 2.0, 4.0 bohr and the full-RPA limit.
- Output file: `/app/outputs/step_02_hBN_interlayer.csv`
- Format: csv
- Contract: CSV with columns: r_c (bohr), d_0 (bohr), C_33 (GPa). One row per r_c value tested.
- Scoring: scored by hidden verifier

### Step 6: DFT calculations for silicon defect supercells
- Role: process
- Action: Perform DFT (LDA) calculations for the perfect silicon supercell (16, 64, 216 atoms) and for defect supercells containing a silicon self-interstitial in split<110> and hexagonal configurations, and a vacancy. For the 64-atom supercell, compute minimum-energy paths using climbing-image nudged elastic band method (or equivalent) for the migration paths split<110> → hex and hex → hex with LDA forces. Relax atomic positions using LDA; for the vacancy, apply a manual Jahn-Teller distortion relaxation as described in the paper.
- Evidence: none

### Step 7: Defect formation and migration energies
- Role: scored (load-bearing)
- Action: Compute the range-separated RPA correlation energies for perfect and defect supercells. Calculate formation energies as E^f = E(defect) - E(bulk) + Σ ν_i μ_i, using μ_Si from bulk silicon. For migration, extract the barrier as the energy difference along the path. Report formation energies for Si_split<110>, Si_hex, and V_Si in each supercell size, and migration barriers for the split→hex and hex→hex paths in the 64-atom cell.
- Output file: `/app/outputs/step_03_defect_energies.json`
- Format: json
- Contract: { "type": "array", "items": { "type": "object", "properties": { "supercell_size": {"type": "integer"}, "defect": {"type": "string", "enum": ["Si_split⟨110⟩", "Si_hex", "V_Si"]}, "formation_energy": {"type": "number", "unit": "eV"}, "migration_barrier": {"type": "number", "unit": "eV", "optional": true} }, "required": ["supercell_size", "defect", "formation_energy"] } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_atomization_energies.json`
- `/app/outputs/step_02_hBN_interlayer.csv`
- `/app/outputs/step_03_defect_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_atomization_energies.json
- path: `/app/outputs/step_01_atomization_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Atomization energies of Al, Si, β-SiC, diamond, w-AlN, c-BN for cutoff radii 0.5, 1.0, 2.0 bohr and the full-RPA limit.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `crystal`:
        - `type`: string
      - `rc`:
        - `type`: number
      - `E_atomization_RPA`:
        - `type`: number
        - `unit`: eV/atom
    - `required`: `crystal`, `rc`, `E_atomization_RPA`

### step_02_hBN_interlayer.csv
- path: `/app/outputs/step_02_hBN_interlayer.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium interlayer spacing d_0 and elastic constant C_33 of hexagonal BN for cutoff radii 1.0, 2.0, 4.0 bohr and the full-RPA limit.
- schema:
  - `type`: table
  - `required_columns`: `r_c`, `d_0`, `C_33`
  - `units`:
    - `r_c`: bohr
    - `d_0`: bohr
    - `C_33`: GPa

### step_03_defect_energies.json
- path: `/app/outputs/step_03_defect_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of silicon self-interstitial (split and hex) and vacancy in 16-, 64-, and 216-atom supercells, and migration barriers for interstitials and vacancy in the 64-atom cell.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `supercell_size`:
        - `type`: integer
      - `defect`:
        - `type`: string
        - `enum`: `Si_split⟨110⟩`, `Si_hex`, `V_Si`
      - `formation_energy`:
        - `type`: number
        - `unit`: eV
      - `migration_barrier`:
        - `type`: number
        - `unit`: eV
        - `optional`: True
    - `required`: `supercell_size`, `defect`, `formation_energy`

Notes: All values correspond to the range-separated RPA scheme with a cutoff radius of 1.0 bohr (or full RPA where indicated). The checker compares against paper-reported reference values using appropriate tolerances; directional scoring ensures that meeting or beating the reference earns full credit, with credit decreasing only for worse performance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_atomization_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "crystal": {
              "type": "string"
            },
            "rc": {
              "type": "number"
            },
            "E_atomization_RPA": {
              "type": "number",
              "unit": "eV/atom"
            }
          },
          "required": [
            "crystal",
            "rc",
            "E_atomization_RPA"
          ]
        }
      },
      "description": "Atomization energies of Al, Si, β-SiC, diamond, w-AlN, c-BN for cutoff radii 0.5, 1.0, 2.0 bohr and the full-RPA limit."
    },
    {
      "file": "step_02_hBN_interlayer.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_c",
          "d_0",
          "C_33"
        ],
        "units": {
          "r_c": "bohr",
          "d_0": "bohr",
          "C_33": "GPa"
        }
      },
      "description": "Equilibrium interlayer spacing d_0 and elastic constant C_33 of hexagonal BN for cutoff radii 1.0, 2.0, 4.0 bohr and the full-RPA limit."
    },
    {
      "file": "step_03_defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "supercell_size": {
              "type": "integer"
            },
            "defect": {
              "type": "string",
              "enum": [
                "Si_split⟨110⟩",
                "Si_hex",
                "V_Si"
              ]
            },
            "formation_energy": {
              "type": "number",
              "unit": "eV"
            },
            "migration_barrier": {
              "type": "number",
              "unit": "eV",
              "optional": true
            }
          },
          "required": [
            "supercell_size",
            "defect",
            "formation_energy"
          ]
        }
      },
      "description": "Formation energies of silicon self-interstitial (split and hex) and vacancy in 16-, 64-, and 216-atom supercells, and migration barriers for interstitials and vacancy in the 64-atom cell."
    }
  ],
  "notes": "All values correspond to the range-separated RPA scheme with a cutoff radius of 1.0 bohr (or full RPA where indicated). The checker compares against paper-reported reference values using appropriate tolerances; directional scoring ensures that meeting or beating the reference earns full credit, with credit decreasing only for worse performance."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact after your run finishes. For each step, the verifier reads your output file, extracts the reported quantities, and compares them against reference values that are not disclosed to you. The comparison uses appropriate tolerances to decide a per-step score, and these scores are combined (with the main defect energies step carrying the largest weight) into an overall reward between 0.0 and 1.0. The verifier does not provide the reference numbers; you must obtain the correct values by performing the computational workflow faithfully.
