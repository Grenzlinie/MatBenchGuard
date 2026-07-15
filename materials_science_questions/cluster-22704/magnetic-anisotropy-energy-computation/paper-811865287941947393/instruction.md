# Magnetic Anisotropy and Magnetization of Metallophthalocyanine Molecules from First Principles Calculations

## Problem background
Metallophthalocyanine (MPc) molecules are promising building blocks for molecular magnets and spintronic devices. The magnetic anisotropy energy and the spin and orbital magnetic moments depend critically on the choice of transition metal center. First-principles density functional theory (DFT) can predict these properties for isolated MPc molecules, guiding the search for systems with large magnetic anisotropy and stable magnetization. This task asks you to compute the spin magnetic moment, orbital magnetic moment, and magnetic anisotropy energy of isolated MnPc, FePc, CoPc, and NiPc molecules using DFT with spin–orbit coupling.

## Approach
You will use the full-potential linearized augmented plane wave (FLAPW) method with the GGA-PBE functional. Spin–orbit coupling (SOC) is included second-variationally in the self-consistent cycle. The magnetic anisotropy energy (MAE) is obtained by comparing the total energies (or via the torque method) for two magnetization directions: perpendicular to the molecular plane and in-plane. The total spin magnetic moment is extracted from the spin density, and the orbital magnetic moment is obtained from the SOC-corrected wavefunctions. The calculations are performed for isolated molecules in a large supercell that minimizes intermolecular interactions. Before the production runs, the molecular geometry is relaxed to determine the equilibrium metal–nitrogen distances.

## Reproduction target
Run self-consistent DFT+SOC calculations for MnPc, FePc, CoPc, and NiPc. Report the computed spin magnetic moment Ms (μB), orbital magnetic moment ML (μB), and magnetic anisotropy energy EMAE (meV) for each system in a single CSV file named magnetic_properties.csv. The EMAE sign convention must follow: positive values correspond to an easy axis perpendicular to the molecular plane.

## Assets

- FLAPW code (e.g. exciting, Elk): https://exciting-code.org/

## Workflow steps

### Step 1: Geometry construction and optimization
- Role: process
- Action: Construct the initial molecular geometries for MPc (M = Mn, Fe, Co, Ni) with square‑planar coordination using standard bond lengths. Set up a slab model with large vacuum (lateral cell a = 20 Å) and perform DFT geometry optimization to obtain the equilibrium metal–nitrogen distances for each molecule.
- Evidence: `/app/outputs/optimized_geometries.log`

### Step 2: Self-consistent DFT+SOC calculations and extraction of magnetic quantities
- Role: process
- Action: For each optimized MPc molecule, perform self‑consistent DFT calculations with spin–orbit coupling (SOC) included second variationally, using the FLAPW method and the GGA‑PBE functional. Use the torque approach (or total energy differences for two magnetization directions: perpendicular and in‑plane) to obtain the magnetic anisotropy energy (MAE). Extract the total spin magnetic moment from the spin density, and the orbital magnetic moment from the SOC‑corrected wavefunctions. Record the final equilibrium total energies for the two magnetization orientations.
- Evidence: `/app/outputs/dft_runs.log`

### Step 3: Compile magnetic properties table
- Role: scored (load-bearing)
- Action: Aggregate the final Ms, ML, and EMAE values for MnPc, FePc, CoPc, and NiPc from the completed DFT runs into a single CSV file. Ensure MAE sign follows the convention (positive = easy axis perpendicular to molecular plane).
- Output file: `/app/outputs/magnetic_properties.csv`
- Format: csv
- Contract: Columns: system (str), Ms (float, μ_B), ML (float, μ_B), EMAE (float, meV). One row per system.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_properties.csv
- path: `/app/outputs/magnetic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed magnetic properties of isolated MPc molecules: spin magnetic moment, orbital magnetic moment, and magnetic anisotropy energy.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Ms`, `ML`, `EMAE`
  - `units`:
    - `Ms`: mu_B
    - `ML`: mu_B
    - `EMAE`: meV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Ms",
          "ML",
          "EMAE"
        ],
        "units": {
          "Ms": "mu_B",
          "ML": "mu_B",
          "EMAE": "meV"
        }
      },
      "description": "Computed magnetic properties of isolated MPc molecules: spin magnetic moment, orbital magnetic moment, and magnetic anisotropy energy."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier scores your submission. The magnetic_properties.csv file is the primary scored artifact: the verifier compares your reported Ms, ML, and EMAE values against reference values with appropriate tolerances and checks that the sign of EMAE is physically consistent. The process evidence logs (optimized_geometries.log and dft_runs.log) are inspected to confirm that the required DFT workflow was genuinely executed. Each part of the workflow contributes a weighted portion to the overall reward. Simply outputting expected numbers without running the computational pipeline will not yield a passing score.
