# First-principles calculation of electron-phonon coupling and Tc in NbC under pressure

## Problem background
Niobium carbide (NbC) is a superconductor, but its critical temperature (Tc) is relatively low compared to what might be expected from simple models. First-principles calculations based on density functional theory (DFT) and density functional perturbation theory (DFPT) can compute the electron-phonon coupling constants and Tc, and can help understand the reasons for the modest Tc by analyzing the contributions from acoustic and optical phonons and the effects of pressure.

## Approach
The workflow uses open-source plane-wave DFT tools to compute the electronic structure and phonon spectra of rock-salt NbC at three volumes: the relaxed equilibrium volume V0, and compressed volumes 0.85V0 and 0.70V0 (corresponding to ~15% and ~30% compression). From the phonon frequencies and electron-phonon matrix elements, the isotropic Eliashberg spectral function α²F(ω) is constructed for each volume. The electron-phonon coupling constants are obtained by integrating α²F(ω)/ω over frequency ranges that separate acoustic (0–14 THz) and optical (above 14 THz) modes. Finally, the isotropic Eliashberg equations are solved with a fixed Coulomb pseudopotential μ* = 0.15 to obtain the superconducting critical temperature Tc for each volume. All steps are performed with standard solid-state pseudopotentials and a plane-wave DFT code.

## Reproduction target
Compute the electron-phonon coupling constants λ_ac (acoustic) and λ_op (optical) for the equilibrium volume V0. Also compute the superconducting critical temperature Tc at all three volumes: V0, 0.85V0, and 0.70V0. These quantities must be reported in the form of a JSON file containing the five values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (Nb, C): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Structure relaxation and equilibrium volume determination
- Role: process
- Action: Construct the rock-salt NbC unit cell. Perform variable-cell DFT relaxation to obtain the equilibrium lattice parameter and volume V0.
- Evidence: none

### Step 2: Self-consistent field calculations for three volumes
- Role: process
- Action: For the three volumes V0, 0.85V0, and 0.70V0, perform self-consistent DFT calculations to obtain ground-state charge densities and wavefunctions.
- Evidence: none

### Step 3: Phonon dispersion calculation
- Role: process
- Action: Using density-functional perturbation theory (DFPT), compute dynamical matrices on a fine q-point grid for each volume. Obtain phonon frequencies and eigenvectors.
- Evidence: none

### Step 4: Electron-phonon coupling and Eliashberg function calculation
- Role: process
- Action: Compute electron-phonon matrix elements, phonon linewidths, and the isotropic Eliashberg spectral function α²F(ω) for each volume.
- Evidence: none

### Step 5: Compute electron-phonon coupling constants and superconducting critical temperature
- Role: scored (load-bearing)
- Action: Integrate the computed α²F(ω) over frequency ranges 0–14 THz (acoustic) and above 14 THz (optical) using λ = 2 ∫ (α²F(ω)/ω) dω to obtain λ_ac and λ_op for V0. Solve the isotropic Eliashberg equations with Coulomb pseudopotential μ* = 0.15 using the α²F(ω) for each volume to obtain the superconducting critical temperatures Tc.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys V0_Tc (float, K), V0.85_Tc (float, K), V0.70_Tc (float, K), V0_lambda_ac (float, dimensionless), V0_lambda_op (float, dimensionless).
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
- target_policy: exact_match
- description: Electron-phonon coupling constants (acoustic and optical) at equilibrium volume V0, and superconducting critical temperatures Tc at three volumes (V0, 0.85V0, 0.70V0). The checker compares these values to hidden gold with tolerances.
- schema:
  - `type`: object
  - `required`: `V0_Tc`, `V0.85_Tc`, `V0.70_Tc`, `V0_lambda_ac`, `V0_lambda_op`
  - `properties`:
    - `V0_Tc`:
      - `type`: number
      - `unit`: K
    - `V0.85_Tc`:
      - `type`: number
      - `unit`: K
    - `V0.70_Tc`:
      - `type`: number
      - `unit`: K
    - `V0_lambda_ac`:
      - `type`: number
      - `unit`: dimensionless
    - `V0_lambda_op`:
      - `type`: number
      - `unit`: dimensionless

Notes: The task reproduces the electron-phonon coupling constants and Tc of NbC using first-principles DFT/DFPT. The agent must run the four process steps to obtain the Eliashberg functions, then compute the scored quantities. The scored artifact results.json contains all required numbers.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "V0_Tc",
          "V0.85_Tc",
          "V0.70_Tc",
          "V0_lambda_ac",
          "V0_lambda_op"
        ],
        "properties": {
          "V0_Tc": {
            "type": "number",
            "unit": "K"
          },
          "V0.85_Tc": {
            "type": "number",
            "unit": "K"
          },
          "V0.70_Tc": {
            "type": "number",
            "unit": "K"
          },
          "V0_lambda_ac": {
            "type": "number",
            "unit": "dimensionless"
          },
          "V0_lambda_op": {
            "type": "number",
            "unit": "dimensionless"
          }
        }
      },
      "description": "Electron-phonon coupling constants (acoustic and optical) at equilibrium volume V0, and superconducting critical temperatures Tc at three volumes (V0, 0.85V0, 0.70V0). The checker compares these values to hidden gold with tolerances."
    }
  ],
  "notes": "The task reproduces the electron-phonon coupling constants and Tc of NbC using first-principles DFT/DFPT. The agent must run the four process steps to obtain the Eliashberg functions, then compute the scored quantities. The scored artifact results.json contains all required numbers."
}
```

## How you are scored
After you complete the workflow and write the final output file, a hidden verifier independently checks each scored artifact. The verifier examines the reported quantities and compares them to hidden reference values using predefined tolerances. Each scored step contributes a weighted portion to the total reward; the final step with the electron-phonon coupling constants and Tc values carries the largest weight. Simply writing numbers that look plausible is not sufficient; the verifier expects values consistent with a correct execution of the computational protocol.
