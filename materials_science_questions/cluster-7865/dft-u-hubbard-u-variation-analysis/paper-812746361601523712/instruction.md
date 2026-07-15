# DFT+U Calculation of Structural and Magnetic Properties of Intermetallic Compounds

## Problem background
Rare-earth intermetallic compounds exhibit a range of functional properties useful in applications such as magnets and actuators. Reliable prediction of their structural and magnetic behavior requires computational methods that can capture strong electron correlations. Standard density functional theory (DFT) approximations fail for the localized 4f electrons of lanthanide ions. The DFT+U (LSDA+U) method adds an on-site Hubbard U correction to improve the description of these correlated states. This task applies LSDA+U to two ternary intermetallic compounds, Yb3Pd2Sn2 and Eu3Pd2Sn2, to compute their equilibrium lattice parameters, bulk modulus, magnetic moments, and—for the Eu-based compound—the relative energies of different collinear magnetic configurations in order to identify the magnetic ground state.

## Approach
The calculations use the full-potential linearized augmented plane wave (FP-LAPW) method as implemented in the WIEN2k code. LSDA+U is employed with an effective Hubbard U of 6.66 eV for Yb²⁺ (using the around mean field (AMF) double-counting correction) and 5.96 eV for Eu²⁺ (using the self-interaction correction (SIC) double-counting correction). Structural optimization is performed in three stages: first, total energy is computed for a series of volumes and fitted to the Murnaghan equation of state to obtain the equilibrium volume V, bulk modulus B, and its pressure derivative B′. Second, the b/a ratio is scanned at fixed c/a and volume to find its optimal value. Third, the c/a ratio is scanned at fixed b/a and volume. The equilibrium lattice constants a, b, c are derived from V and the optimized ratios. At the optimized structure, a self-consistent field (SCF) calculation yields the total magnetic moment of the unit cell and the atomic magnetic moments on each lanthanide site. For Eu3Pd2Sn2, three collinear magnetic configurations are constructed—one ferromagnetic (FM) and two antiferromagnetic (AFM1, AFM2). For each configuration, a volume optimization is performed to obtain the minimum total energy, allowing identification of the magnetic ground state. All results are compiled into a single JSON file.

## Reproduction target
Produce the file /app/outputs/results.json containing the following quantities for Yb3Pd2Sn2 and Eu3Pd2Sn2, computed with LSDA+U using the specified U_eff and double-counting choices: equilibrium unit-cell volume V (nm³), lattice constants a, b, c (nm), cell-shape ratios c/a and b/a (dimensionless), bulk modulus B (GPa) and its pressure derivative B′ (dimensionless), total magnetic moment of the unit cell (µB), and a list of atomic magnetic moments (µB) for the Yb or Eu sites in the order they appear in the provided crystal structure data. For Eu3Pd2Sn2 additionally: the magnetic ground state (a string that is one of "FM", "AFM1", or "AFM2") and the minimum total energies (in Ry) for the FM, AFM1, and AFM2 configurations. For Yb3Pd2Sn2, set the magnetic ground state and energy fields to null.

## Assets

- WIEN2k: https://www.wien2k.at
- Crystal structure data (space group Pbcm, atomic coordinates) for Yb3Pd2Sn2 and Eu3Pd2Sn2

## Workflow steps

### Step 1: LSDA+U structural optimization for both compounds
- Role: process
- Action: For Yb3Pd2Sn2 with U_eff = 6.66 eV and Eu3Pd2Sn2 with U_eff = 5.96 eV, perform total-energy calculations while varying volume and fit the Murnaghan equation of state to obtain the equilibrium volume V, bulk modulus B, and pressure derivative B_prime. At the equilibrium volume, scan the b/a ratio at fixed c/a, and scan the c/a ratio at fixed b/a, to determine the optimal cell shape ratios. Derive the equilibrium lattice parameters a, b, c from V and the optimized ratios.
- Evidence: `/app/outputs/optimization.log`

### Step 2: SCF calculation of magnetic moments
- Role: process
- Action: At the equilibrium geometries from step 1, run self-consistent field LSDA+U calculations for both compounds to obtain the total magnetic moment of the unit cell and atomic magnetic moments on all Yb/Eu sites.
- Evidence: `/app/outputs/scf_mag.log`

### Step 3: Magnetic ground state energy comparison for Eu3Pd2Sn2
- Role: process
- Action: For Eu3Pd2Sn2, construct collinear ferromagnetic (FM) and two antiferromagnetic (AFM1, AFM2) configurations as described in the paper. For each configuration, perform a volume optimization via Murnaghan EOS fitting using LSDA+U to obtain the minimum energy.
- Evidence: `/app/outputs/mag_config_energy.log`

### Step 4: Compile and report all results
- Role: scored (load-bearing)
- Action: Gather from the previous steps: equilibrium V, a, b, c, c_over_a, b_over_a, B, B_prime, total_magnetic_moment and atomic_magnetic_moments for Yb3Pd2Sn2 and Eu3Pd2Sn2; for Eu3Pd2Sn2 also the magnetic ground state and the FM, AFM1, AFM2 energies. Write them into results.json with the schema below.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with top-level keys "Yb3Pd2Sn2" and "Eu3Pd2Sn2". Each contains: V (float, nm³), a (float, nm), b (float, nm), c (float, nm), c_over_a (float), b_over_a (float), B (float, GPa), B_prime (float), total_magnetic_moment (float, μB), atomic_magnetic_moments (list of floats, μB, in order of Yb/Eu sites from the crystal data). For Eu3Pd2Sn2 additionally: magnetic_ground_state (string, one of "FM", "AFM1", "AFM2"), FM_energy (float, Ry), AFM1_energy (float, Ry), AFM2_energy (float, Ry). For Yb3Pd2Sn2, magnetic_ground_state, FM_energy, AFM1_energy, AFM2_energy are null.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: LSDA+U structural, magnetic properties and magnetic ground state for Re3Pd2Sn2 compounds.
- schema:
  - `type`: object
  - `required`:
    - `Yb3Pd2Sn2`:
      - `type`: object
      - `required`: `V`, `a`, `b`, `c`, `c_over_a`, `b_over_a`, `B`, `B_prime`, `total_magnetic_moment`, `atomic_magnetic_moments`, `magnetic_ground_state`, `FM_energy`, `AFM1_energy`, `AFM2_energy`
      - `units`:
        - `V`: nm^3
        - `a`: nm
        - `b`: nm
        - `c`: nm
        - `c_over_a`: dimensionless
        - `b_over_a`: dimensionless
        - `B`: GPa
        - `B_prime`: dimensionless
        - `total_magnetic_moment`: mu_B
        - `atomic_magnetic_moments`: list of floats (mu_B)
        - `magnetic_ground_state`: string|null
        - `FM_energy`: Ry|null
        - `AFM1_energy`: Ry|null
        - `AFM2_energy`: Ry|null
    - `Eu3Pd2Sn2`:
      - `type`: object
      - `required`: `V`, `a`, `b`, `c`, `c_over_a`, `b_over_a`, `B`, `B_prime`, `total_magnetic_moment`, `atomic_magnetic_moments`, `magnetic_ground_state`, `FM_energy`, `AFM1_energy`, `AFM2_energy`
      - `units`:
        - `V`: nm^3
        - `a`: nm
        - `b`: nm
        - `c`: nm
        - `c_over_a`: dimensionless
        - `b_over_a`: dimensionless
        - `B`: GPa
        - `B_prime`: dimensionless
        - `total_magnetic_moment`: mu_B
        - `atomic_magnetic_moments`: list of floats (mu_B)
        - `magnetic_ground_state`: string (one of FM, AFM1, AFM2)
        - `FM_energy`: Ry
        - `AFM1_energy`: Ry
        - `AFM2_energy`: Ry

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Yb3Pd2Sn2": {
            "type": "object",
            "required": [
              "V",
              "a",
              "b",
              "c",
              "c_over_a",
              "b_over_a",
              "B",
              "B_prime",
              "total_magnetic_moment",
              "atomic_magnetic_moments",
              "magnetic_ground_state",
              "FM_energy",
              "AFM1_energy",
              "AFM2_energy"
            ],
            "units": {
              "V": "nm^3",
              "a": "nm",
              "b": "nm",
              "c": "nm",
              "c_over_a": "dimensionless",
              "b_over_a": "dimensionless",
              "B": "GPa",
              "B_prime": "dimensionless",
              "total_magnetic_moment": "mu_B",
              "atomic_magnetic_moments": "list of floats (mu_B)",
              "magnetic_ground_state": "string|null",
              "FM_energy": "Ry|null",
              "AFM1_energy": "Ry|null",
              "AFM2_energy": "Ry|null"
            }
          },
          "Eu3Pd2Sn2": {
            "type": "object",
            "required": [
              "V",
              "a",
              "b",
              "c",
              "c_over_a",
              "b_over_a",
              "B",
              "B_prime",
              "total_magnetic_moment",
              "atomic_magnetic_moments",
              "magnetic_ground_state",
              "FM_energy",
              "AFM1_energy",
              "AFM2_energy"
            ],
            "units": {
              "V": "nm^3",
              "a": "nm",
              "b": "nm",
              "c": "nm",
              "c_over_a": "dimensionless",
              "b_over_a": "dimensionless",
              "B": "GPa",
              "B_prime": "dimensionless",
              "total_magnetic_moment": "mu_B",
              "atomic_magnetic_moments": "list of floats (mu_B)",
              "magnetic_ground_state": "string (one of FM, AFM1, AFM2)",
              "FM_energy": "Ry",
              "AFM1_energy": "Ry",
              "AFM2_energy": "Ry"
            }
          }
        }
      },
      "description": "LSDA+U structural, magnetic properties and magnetic ground state for Re3Pd2Sn2 compounds."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your /app/outputs/results.json and evaluate each required quantity. The verifier compares your reported structural parameters and magnetic moments to reference values (tolerances account for legitimate spread between different DFT implementations). It checks that for Eu3Pd2Sn2 the ferromagnetic energy is lower than both antiferromagnetic energies, confirming FM as the ground state. It also verifies internal consistency: V ≈ (c/a)*(b/a)*a³. The final reward is a weighted combination of scores over all scored quantities; you must genuinely execute the workflow steps—merely copying numbers will not suffice.
