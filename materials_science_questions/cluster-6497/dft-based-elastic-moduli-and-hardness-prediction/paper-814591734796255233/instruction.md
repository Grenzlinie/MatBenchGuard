# DFT and QMC study of bulk modulus and lattice stability in superhard boron carbon nitride

## Problem background
Cubic boron nitride (c-BN) is a superhard material valued for its high-temperature chemical stability when machining ferrous alloys, but its hardness is roughly half that of diamond. Doping c-BN with carbon to form cubic BC₂N (c-BC₂N) has been proposed as a route to increase hardness, yet experimental measurements of the bulk modulus of c-BC₂N vary widely, with some reports placing it below that of c-BN. Previous density functional theory (DFT) studies have predicted that c-BC₂N should possess a higher bulk modulus than c-BN, but these predictions may be affected by the choice of exchange-correlation functional and by the neglect of phonon effects. This task uses accurate quantum Monte Carlo (QMC) and phonon calculations to compute the zero-point-corrected bulk modulus of c-BN and c-BC₂N and to determine their relative ordering, while also accounting for lattice instabilities at high pressure.

## Approach
The bulk modulus is obtained by fitting an equation of state (EoS) to the total energy versus volume data of each material. First, density functional theory (DFT) calculations with the PBE functional generate trial wavefunctions and total energies at a set of volumes for both the zinc-blende c-BN structure and the most stable cubic c-BC₂N configuration. Diffusion Monte Carlo (DMC) with the T-move scheme and a finite-size correction is then used to compute more accurate total energies at each volume. In parallel, phonon frequencies and zero-point vibrational free energies are computed within the quasiharmonic approximation over the same volume range; volumes where the phonon spectrum develops imaginary frequencies (indicating lattice instability) are excluded from the subsequent fitting. The DMC total energies are corrected by adding the zero-point free energy, and the resulting energy-volume points are fitted to the Vinet equation of state with the pressure derivative B₀′ fixed to 4.0. This yields the zero-point-corrected equilibrium volume V₀ and bulk modulus B₀ at 0 K for each material, from which the ordering can be determined.

## Reproduction target
Produce a JSON file `/app/outputs/results.json` containing the zero-point-corrected equilibrium volume V₀ (in Bohr³) and bulk modulus B₀ (in GPa) for c-BN and for c-BC₂N, computed from the DMC energy-volume data corrected by zero-point phonon free energies and fitted to the Vinet equation of state with B₀′ = 4.0. The file must also report the ordering of the bulk moduli: whether c-BC₂N or c-BN has the higher B₀.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org
- CASINO (QMC code): https://www.casinoqmc.net
- Trail-Needs norm-conserving pseudopotentials for B, C, N: http://www.tcm.phy.cam.ac.uk/~mdt26/pseudopotentials.html
- Crystal structure for c-BN (zinc-blende): mp-1029
- Crystal structure for c-BC2N (most stable cubic configuration from Sun et al.): mp-566645

## Workflow steps

### Step 1: DFT total energy calculations for c-BN and c-BC2N
- Role: process
- Action: Using Quantum ESPRESSO with PBE functional and norm-conserving Trail-Needs pseudopotentials, perform self-consistent total energy calculations for zinc-blende c-BN and the most stable cubic c-BC2N configuration at a set of volumes to generate energy-volume curves. Provide Kohn-Sham wavefunctions for subsequent DMC.
- Evidence: `/app/outputs/dft_energies.csv`

### Step 2: DMC total energy calculations
- Role: process
- Action: Using CASINO, convert DFT wavefunctions to spline basis, set up Slater-Jastrow trial wavefunctions, and run diffusion Monte Carlo (DMC) at each volume with the T-move scheme and MPC finite-size correction. Collect DMC total energies and statistical errors for c-BN and c-BC2N.
- Evidence: `/app/outputs/dmc_energies.csv`

### Step 3: Phonon and zero-point energy calculations
- Role: process
- Action: Using Quantum ESPRESSO with density functional perturbation theory under the quasiharmonic approximation, compute phonon frequencies and zero-point vibrational free energies as a function of volume for both materials. Identify any volumes with negative phonon frequencies and exclude them from later fitting. Collect zero-point energy corrections per volume.
- Evidence: `/app/outputs/phonon_free_energies.csv`

### Step 4: Equation-of-state fitting and final bulk modulus extraction
- Role: scored (load-bearing)
- Action: For each material, add the zero-point phonon free energy at 0 K from step2 to the DMC total energies from step1, then fit the corrected energy-volume points to the Vinet equation of state with the pressure derivative B0' fixed to 4.0, excluding any unstable volumes identified in step2. Extract the zero-point-corrected equilibrium volume V0 and bulk modulus B0. Report the values and the ordering in a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: BN_B0 (float, GPa), BN_V0 (float, Bohr^3), BC2N_B0 (float, GPa), BC2N_V0 (float, Bohr^3), ordering (string, 'BC2N_higher' if BC2N_B0 > BN_B0 else 'BN_higher')
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
- description: Zero-point-corrected equilibrium volume and bulk modulus for c-BN and c-BC2N computed from DMC energy-volume data and phonon free energies by Vinet EoS fitting (B0'=4.0). The ordering field indicates which material has the higher bulk modulus.
- schema:
  - `type`: object
  - `required`: `BN_B0`, `BC2N_B0`, `BN_V0`, `BC2N_V0`, `ordering`
  - `properties`:
    - `BN_B0`:
      - `type`: number
      - `unit`: GPa
    - `BC2N_B0`:
      - `type`: number
      - `unit`: GPa
    - `BN_V0`:
      - `type`: number
      - `unit`: Bohr^3
    - `BC2N_V0`:
      - `type`: number
      - `unit`: Bohr^3
    - `ordering`:
      - `type`: string
      - `enum`: `BC2N_higher`, `BN_higher`

Notes: The hidden checker compares the reported values to the paper's DMC/0K results with appropriate tolerances and verifies the ordering. Process artifacts (dft_energies.csv, dmc_energies.csv, phonon_free_energies.csv) are not directly scored but must be produced to obtain the final result.

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
        "required": [
          "BN_B0",
          "BC2N_B0",
          "BN_V0",
          "BC2N_V0",
          "ordering"
        ],
        "properties": {
          "BN_B0": {
            "type": "number",
            "unit": "GPa"
          },
          "BC2N_B0": {
            "type": "number",
            "unit": "GPa"
          },
          "BN_V0": {
            "type": "number",
            "unit": "Bohr^3"
          },
          "BC2N_V0": {
            "type": "number",
            "unit": "Bohr^3"
          },
          "ordering": {
            "type": "string",
            "enum": [
              "BC2N_higher",
              "BN_higher"
            ]
          }
        }
      },
      "description": "Zero-point-corrected equilibrium volume and bulk modulus for c-BN and c-BC2N computed from DMC energy-volume data and phonon free energies by Vinet EoS fitting (B0'=4.0). The ordering field indicates which material has the higher bulk modulus."
    }
  ],
  "notes": "The hidden checker compares the reported values to the paper's DMC/0K results with appropriate tolerances and verifies the ordering. Process artifacts (dft_energies.csv, dmc_energies.csv, phonon_free_energies.csv) are not directly scored but must be produced to obtain the final result."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and independently evaluates the reported BN_B₀ and BC₂N_B₀ against internal reference values with pre-set tolerances that account for statistical and systematic errors in the computational pipeline. The verifier also checks the ordering field. Full credit requires that both bulk moduli lie within tolerance and the ordering is correct; partial credit is possible if only some conditions are met. The scoring does not rely on exact agreement with any single published digit but on whether the results fall within the expected range for a correctly executed re-run of the described workflow.
