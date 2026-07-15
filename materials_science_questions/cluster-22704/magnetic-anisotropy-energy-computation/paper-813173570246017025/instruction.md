# First-principles Calculation of Magnetocrystalline Anisotropy in FePd

## Problem background
The CuAu(I)-type FePd ordered alloy exhibits strong uniaxial magnetocrystalline anisotropy, making it a candidate for magnetic recording media. Understanding and predicting the easy magnetization direction and the magnitude of the anisotropy constant (K_uniaxial) from first principles is important for rational materials design. In this task, we compute the magnetocrystalline anisotropy energy of FePd using a full-potential linear augmented plane wave (FLAPW) method with spin-orbit coupling, reproducing the crucial electronic-structure calculations that determine the magnetic easy axis and quantify the uniaxial anisotropy constant.

## Approach
We employ density-functional theory with the PBE generalized-gradient approximation, using a full-potential linear augmented plane wave (FLAPW) method. Spin-orbit coupling is introduced as a second-order perturbation. The tetragonal CuAu(I) unit cell (a=3.89 Å, c=3.68 Å) with Fe at (0,0,0) and (0.5,0.5,0) and Pd at (0,0.5,0.5) and (0.5,0,0.5) is constructed. Three independent self-consistent total-energy calculations are performed for different magnetization directions: (0,0,1) — along the c-axis; (1,1,a/c) — 45° from c; and (1,1,0) — 90° from c, with the orbital quantization axis fixed along the c-axis. The energy differences between these calculations quantify the magnetocrystalline anisotropy. The uniaxial anisotropy constant K_uniaxial is obtained from the energy increment at 45° divided by the unit cell volume, using appropriate unit conversions.

## Reproduction target
Your goal is to produce a results.json file containing the converged total energies for each magnetization direction, identify the easy axis (lowest energy), compute the energy differences ΔE_45 and ΔE_90 relative to that axis, and derive the uniaxial anisotropy constant K_uniaxial. The output file must be written to /app/outputs/results.json and follow the prescribed schema: energy_case_A, energy_case_B, energy_case_C, delta_E_45, delta_E_90, K_uniaxial (units as specified). The calculation must use the provided structure, functional, and spin-orbit treatment, with adequate k-point sampling and convergence that reflect the physics of the problem.

## Assets

- Open-source full-potential LAPW code (e.g., exciting, Elk): https://exciting-code.org/

## Workflow steps

### Step 1: Prepare crystal structure and FLAPW input files
- Role: process
- Action: Set up the tetragonal CuAu(I) FePd unit cell with experimental lattice constants a=3.89 Å, c=3.68 Å and atomic positions: Fe at (0,0,0) and (0.5,0.5,0); Pd at (0,0.5,0.5) and (0.5,0,0.5). Choose appropriate augmentation-sphere radii and convergence parameters. Prepare input files for a full-potential LAPW code with PBE-GGA exchange-correlation and settings for spin-orbit coupling as a second-order perturbation.
- Evidence: `/app/outputs/input_parameters.txt`

### Step 2: Run self-consistent FLAPW+SOC calculations for three magnetization directions
- Role: process
- Action: Perform three independent self-consistent total-energy calculations with magnetization directions: (0,0,1) – along c-axis (case A), (1,1,a/c) – 45° from c-axis (case B), and (1,1,0) – 90° from c-axis (case C). Use a Brillouin-zone sampling of 2048 k-points and convergence threshold appropriate to the physics. Keep the orbital quantization axis along the c-axis. Record the converged total energy for each orientation.
- Evidence: `/app/outputs/scf_energies.log`

### Step 3: Compile total energies and compute magnetocrystalline anisotropy energy and K_uniaxial
- Role: scored (load-bearing)
- Action: Read the total energies from the previous step, identify the easy axis (lowest total energy), compute the energy differences ΔE_45 = E(B) - E(A) and ΔE_90 = E(C) - E(A), and derive the uniaxial anisotropy constant K_uniaxial = ΔE_45 / (a²c) using appropriate unit conversions (1 Ry = 2.1798741×10⁻¹⁸ J, 1 Å = 1×10⁻¹⁰ m). Write all values to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "energy_case_A": "float (Ry/cell)",
  "energy_case_B": "float (Ry/cell)",
  "energy_case_C": "float (Ry/cell)",
  "delta_E_45": "float (Ry/cell)",
  "delta_E_90": "float (Ry/cell)",
  "K_uniaxial": "float (MJ/m^3)"
}
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
- description: JSON file containing the total energies for the three magnetization directions, the corresponding energy differences, and the derived uniaxial anisotropy constant. The checker will recompute K_uniaxial from delta_E_45 and the known unit cell volume and compare all quantities to the paper's expected values within appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `energy_case_A`, `energy_case_B`, `energy_case_C`, `delta_E_45`, `delta_E_90`, `K_uniaxial`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `energy_case_A`: Ry/cell
    - `energy_case_B`: Ry/cell
    - `energy_case_C`: Ry/cell
    - `delta_E_45`: Ry/cell
    - `delta_E_90`: Ry/cell
    - `K_uniaxial`: MJ/m^3

Notes: The agent must produce total energies from three FLAPW+SOC calculations. The checker compares the agent's quantities to reference values; units must be exactly as declared. The easy axis (lowest energy) must be along the c-axis (energy_case_A minimum).

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
          "energy_case_A",
          "energy_case_B",
          "energy_case_C",
          "delta_E_45",
          "delta_E_90",
          "K_uniaxial"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "energy_case_A": "Ry/cell",
          "energy_case_B": "Ry/cell",
          "energy_case_C": "Ry/cell",
          "delta_E_45": "Ry/cell",
          "delta_E_90": "Ry/cell",
          "K_uniaxial": "MJ/m^3"
        }
      },
      "description": "JSON file containing the total energies for the three magnetization directions, the corresponding energy differences, and the derived uniaxial anisotropy constant. The checker will recompute K_uniaxial from delta_E_45 and the known unit cell volume and compare all quantities to the paper's expected values within appropriate tolerances."
    }
  ],
  "notes": "The agent must produce total energies from three FLAPW+SOC calculations. The checker compares the agent's quantities to reference values; units must be exactly as declared. The easy axis (lowest energy) must be along the c-axis (energy_case_A minimum)."
}
```

## How you are scored
A hidden verifier will check your results.json. It will verify that the lowest total energy corresponds to the magnetization along the c-axis. It will recompute K_uniaxial from your reported delta_E_45 and the known unit cell volume. It will compare your delta_E_45 and delta_E_90 values to target reference results, and compare your K_uniaxial to the expected anisotropy constant, using tolerances that account for code and convergence differences. The verifier will combine these checks into a single reward score between 0 and 1. Correctly identifying the easy axis and reproducing the anisotropy constant within tolerance will earn full credit; partial matches receive proportional credit.
