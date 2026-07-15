# Free Energy Profiles of S-Nitrosothiol Approach to Copper Sites in MOF-143 via Umbrella Sampling

## Problem background
Nitric oxide (NO) is a gaseous signalling molecule with therapeutic applications, but its high reactivity makes controlled delivery challenging. Chemically storing NO as S-nitrosothiols (RSNOs) and using copper-based metal-organic frameworks (MOFs) as catalysts allows sustained release. A key step in the catalytic cycle is the approach of an RSNO species to a copper site, which may be influenced by the size and chemical structure of the RSNO. This work investigates the free-energy barriers for RSNO approach to copper sites in MOF-143, a copper paddle-wheel MOF with extended BTB linkers, using classical molecular dynamics and umbrella sampling. Understanding how the molecular structure of biologically compatible RSNOs (cysteine and glutathione derivatives) modulates these barriers can inform the design of NO delivery systems with tunable release rates.

## Approach
The computational protocol consists of: (1) building the MOF-143 crystal structure; (2) computing partial charges for the MOF cluster and the RSNO molecules (CysNO and GSNO) with density functional theory (B3LYP/6-311G(d,p) for main group atoms, LANL2DZ for Cu) using the CHELPG scheme; (3) assembling solvated simulation cells (MOF-143 + ethanol + one or two RSNOs) and assigning a modified Dreiding force field with custom Lennard-Jones parameters for Cu–RSNO interactions; (4) running umbrella sampling simulations along the Cu–S distance reaction coordinate for three scenarios: a single RSNO approaching a reduced Cu(I) site (1RSNO), a second RSNO approaching the same copper site (2RSNO), and a second RSNO approaching an adjacent copper site (RSNO2); (5) reconstructing the free-energy profiles (PMFs) using the weighted histogram analysis method (WHAM); (6) extracting barrier heights from the PMFs for comparison across scenarios and RSNO species.

## Reproduction target
Produce free-energy profiles (PMFs) as a function of Cu–S distance for the approach of CysNO and GSNO to copper sites in MOF-143 under three conditions: 1RSNO, 2RSNO, and RSNO2. From the PMF data, compute the barrier height (max PMF minus min PMF) for each 2RSNO combination, and for 1RSNO and RSNO2 report 0.0 kcal/mol if the maximum fluctuation is ≤2 kcal/mol or the fluctuation otherwise. The PMF data and derived barriers should allow verification of how the size and structure of RSNOs influence the approach barriers and whether the MOF environment imposes different barriers depending on the scenario.

## Assets

- MOF-143 crystal structure (CIF file): CSD entry from Furukawa et al., Inorg. Chem. 2011, 50, 9147-9152; CCDC deposition number not explicitly given, but the structure is available from the Cambridge Structural Database or the Yaghi group.
- Dreiding force field parameters: gromacs
- Custom Lennard-Jones parameters for Cu(I)–RSNO interactions: The non‑bonded interactions between copper(I) and the atoms of the S‑nitrosothiol moiety are parameterized using the following Lennard‑Jones coefficients (A in kJ mol⁻¹ nm¹², B in kJ mol⁻¹ nm⁶):
  Cu–CH₃: A = 3.5E-04, B = 3.1E-01
  Cu–S: A = 4.9E-07, B = 1.7E-02
  Cu–N: A = 3.2E-05, B = 1.1E-01
  Cu–O: A = 2.1E-09, B = 5.2E-01
  Additionally, for copper–ethanol interactions:
  Cu–CH₂: A = 1.0E-04, B = 1.9E-01
  Cu–O: A = 1.5E-09, B = 1.6E-04
  Cu–H: A = 1.5E-06, B = 1.7E-02
- GROMACS: https://www.gromacs.org/
- WHAM analysis tool: gromacs
- Open-source DFT code for partial charges: https://www.orcasoftware.de/
- Python 3: python3

## Workflow steps

### Step 1: Compute MOF-143 partial charges
- Role: process
- Action: Build a representative cluster of MOF-143 from the crystal structure. Use DFT at the B3LYP level with a mixed basis set (LANL2DZ for Cu, 6-311G(d,p) for O, C, H) to compute CHELPG charges for all atoms. Also compute charges for the Cu(I)-reduced cluster with Na+ counterions to confirm the charge reduction at copper. Store the partial charges for use in the force field.
- Evidence: `/app/outputs/mof143_charges.txt`

### Step 2: Compute RSNO partial charges
- Role: process
- Action: For CysNO and GSNO, perform gas-phase DFT optimization at B3LYP/6-311G(d,p) and compute CHELPG charges. Save the charges for each atom.
- Evidence: `/app/outputs/cysno_charges.txt, gsno_charges.txt`

### Step 3: Prepare simulation systems
- Role: process
- Action: Assemble periodic simulation cells containing MOF-143, 200 ethanol molecules, and the appropriate RSNO molecules for the scenarios: (i) one CysNO approaching Cu(I), (ii) one GSNO approaching Cu(I), (iii) two CysNO (second approaches same Cu), (iv) two GSNO (second approaches same Cu), (v) two CysNO (second approaches adjacent Cu), (vi) two GSNO (second approaches adjacent Cu). Assign Dreiding force field parameters, the custom Cu-RSNO LJ parameters, and the partial charges from steps 1 and 2. Create GROMACS topology and coordinate files.
- Evidence: `/app/outputs/system_descriptions.txt`

### Step 4: Run umbrella sampling MD simulations
- Role: process
- Action: For each of the six systems, perform umbrella sampling along the Cu–S distance reaction coordinate (1.8 to 7.0 Å, 17 windows, force constant 35000 kcal mol⁻¹ nm⁻²). Equilibrate each window for 30 ns and run a 60 ns production NPT ensemble at 300 K and 1 bar, using a 0.5 fs time step, SPME electrostatics, 9 Å real-space cutoff, and 12 Å van der Waals cutoff. Save trajectories and umbrella windows for WHAM analysis.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 5: Compute free-energy profiles via WHAM
- Role: scored (load-bearing)
- Action: Apply the weighted histogram analysis method (WHAM) to the umbrella sampling data to obtain the free-energy profile (PMF) as a function of Cu–S distance for each scenario (1RSNO, 2RSNO, RSNO2) and each RSNO (CysNO, GSNO). Write the combined data to pmf_data.csv.
- Output file: `/app/outputs/pmf_data.csv`
- Format: csv
- Contract: Columns: scenario (string: 1RSNO, 2RSNO, RSNO2), RSNO (string: CysNO, GSNO), r_CuS (float, Angstrom), PMF (float, kcal/mol).
- Scoring: scored by hidden verifier

### Step 6: Extract barrier heights from PMFs
- Role: scored
- Action: From pmf_data.csv, compute the barrier height for each 2RSNO scenario as max(PMF) minus min(PMF) within the sampled range. For 1RSNO and RSNO2, report 0.0 if the maximum fluctuation is ≤2 kcal/mol; otherwise report the fluctuation. Write the results to barriers.csv.
- Output file: `/app/outputs/barriers.csv`
- Format: csv
- Contract: Columns: scenario (string), RSNO (string), barrier_height (float, kcal/mol; 0.0 indicates negligible barrier).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pmf_data.csv`
- `/app/outputs/barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pmf_data.csv
- path: `/app/outputs/pmf_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Free-energy profiles (PMFs) for RSNO approach to copper sites in MOF-143. The checker will verify the shape (e.g., monotonic rise after minimum), trends (2GSNO barrier < 2CysNO barrier), and that 1RSNO/RSNO2 profiles are barrierless within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `scenario`, `RSNO`, `r_CuS`, `PMF`
  - `units`:
    - `r_CuS`: Angstrom
    - `PMF`: kcal/mol
  - `notes`: scenario must be exactly one of 1RSNO, 2RSNO, RSNO2; RSNO must be CysNO or GSNO.

### barriers.csv
- path: `/app/outputs/barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Derived barrier heights from the PMF data. The checker will recompute barriers from pmf_data.csv and compare the 2RSNO barriers against paper-reported approximate values (±2.0 kcal/mol tolerance), and verify that 1RSNO and RSNO2 barriers are ≤2.0 kcal/mol.
- schema:
  - `type`: table
  - `required_columns`: `scenario`, `RSNO`, `barrier_height`
  - `units`:
    - `barrier_height`: kcal/mol
  - `notes`: barrier_height = 0.0 for negligible barriers.

Notes: All energies in kcal/mol, distances in Angstrom. The scored PMF data and barriers must be derived from the umbrella sampling simulations; fabricating these values will be detected by the checker's structural and trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pmf_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "scenario",
          "RSNO",
          "r_CuS",
          "PMF"
        ],
        "units": {
          "r_CuS": "Angstrom",
          "PMF": "kcal/mol"
        },
        "notes": "scenario must be exactly one of 1RSNO, 2RSNO, RSNO2; RSNO must be CysNO or GSNO."
      },
      "description": "Free-energy profiles (PMFs) for RSNO approach to copper sites in MOF-143. The checker will verify the shape (e.g., monotonic rise after minimum), trends (2GSNO barrier < 2CysNO barrier), and that 1RSNO/RSNO2 profiles are barrierless within tolerance."
    },
    {
      "file": "barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "scenario",
          "RSNO",
          "barrier_height"
        ],
        "units": {
          "barrier_height": "kcal/mol"
        },
        "notes": "barrier_height = 0.0 for negligible barriers."
      },
      "description": "Derived barrier heights from the PMF data. The checker will recompute barriers from pmf_data.csv and compare the 2RSNO barriers against paper-reported approximate values (±2.0 kcal/mol tolerance), and verify that 1RSNO and RSNO2 barriers are ≤2.0 kcal/mol."
    }
  ],
  "notes": "All energies in kcal/mol, distances in Angstrom. The scored PMF data and barriers must be derived from the umbrella sampling simulations; fabricating these values will be detected by the checker's structural and trend checks."
}
```

## How you are scored
A hidden verifier reads pmf_data.csv and barriers.csv. It recomputes the 2RSNO barrier heights directly from the PMF data and compares them against hidden expected values, and checks that the 1RSNO and RSNO2 barriers are consistent with no significant obstacle to approach. The verifier also validates the structural shape of the PMFs (e.g., monotonic rise after a minimum, absence of spurious oscillations). Scoring tolerances account for run-to-run differences from different implementations and seeds. A correctly executed reproduction that yields physically reasonable PMFs and barrier values matching the expected trends will receive a high score.
