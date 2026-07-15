# Electron-Phonon Superconducting Tc Estimation via McMillan-Allen-Dynes

## Problem background
Monolayer C3N is a two-dimensional honeycomb material composed of carbon and nitrogen atoms, with a semiconducting indirect band gap. It has attracted attention for potential applications in electronics and energy storage. Understanding whether charge doping or alkali-metal deposition can induce a superconducting state in this monolayer is of fundamental and practical interest. This work targets the estimation of the superconducting transition temperature via the phonon-mediated channel, quantifying the electron‑phonon coupling strength and the characteristic phonon energy under different structural and doping conditions.

## Approach
The approach uses first-principles density-functional theory (DFT) and density-functional perturbation theory (DFPT) to compute the electronic and phonon properties of monolayer C3N. From the DFPT-calculated dynamical matrices the Eliashberg spectral function is obtained, and its integration yields the total electron‑phonon coupling constant λ and the logarithmic average phonon frequency ω_log. Finally, the superconducting critical temperature Tc is evaluated with the isotropic McMillan–Allen–Dynes formula using a fixed retarded Coulomb pseudopotential μ*. Three distinct systems are compared: (1) electron‑doped C3N without biaxial strain, (2) electron‑doped C3N under 5% biaxial tensile strain, and (3) Li‑deposited C3N in the most stable adsorption configuration. The final result for each system is a triplet (λ, ω_log, Tc) that quantifies the superconducting propensity.

## Reproduction target
For each of three monolayer C3N conditions — (A) 0.2 e/cell electron doping at 0% biaxial strain, (B) 0.2 e/cell electron doping at 5% biaxial tensile strain, and (C) Li-deposited C3N in the most stable Li configuration — compute the following quantities: the total electron‑phonon coupling constant λ (dimensionless), the logarithmic average phonon frequency ω_log (in cm⁻¹), and the superconducting critical temperature Tc (in K). Report all nine numbers in a single JSON file following the format specified in the output contract.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- Norm‑conserving PBE pseudopotentials for C, N, Li: https://www.quantum-espresso.org/pseudopotentials/
- Crystal structure parameters for monolayer C3N: 10.1557/jmr.2017.299

## Workflow steps

### Step 1: Relax pristine monolayer C3N
- Role: process
- Action: Set up the monolayer C3N unit cell (honeycomb lattice) and perform DFT structural relaxation with appropriate vacuum to obtain the equilibrium geometry for a 2D system. This relaxed structure serves as the starting point for doping and strain.
- Evidence: `/app/outputs/relax_pristine.log`

### Step 2: Relax 0.2 e/cell electron‑doped C3N (0% strain)
- Role: process
- Action: Starting from the relaxed pristine structure, add 0.2 electrons per unit cell and relax the electron‑doped system under the same DFT settings. This provides the geometry for the unstrained electron‑doped case.
- Evidence: `/app/outputs/relax_doped_strain0.log`

### Step 3: Phonon and EPC calculation for 0.2 e/cell doped C3N (0% strain)
- Role: process
- Action: Compute the phonon dispersion and electron‑phonon coupling for the relaxed 0.2 e/cell doped structure. Evaluate the Eliashberg spectral function α²F(ω), then integrate to obtain the total electron‑phonon coupling constant λ and the logarithmic average phonon frequency ω_log.
- Evidence: `/app/outputs/epc_doped_strain0.log`

### Step 4: Relax 0.2 e/cell electron‑doped C3N under 5% biaxial tensile strain
- Role: process
- Action: Apply 5% biaxial tensile strain to the 0.2 e/cell electron‑doped structure and relax the geometry. This provides the strained doped configuration.
- Evidence: `/app/outputs/relax_doped_strain5.log`

### Step 5: Phonon and EPC calculation for strained 0.2 e/cell doped C3N
- Role: process
- Action: Compute the phonon dispersion and electron‑phonon coupling for the strained doped structure; extract λ and ω_log as in step s3.
- Evidence: `/app/outputs/epc_doped_strain5.log`

### Step 6: Relax Li‑deposited C3N configurations and identify most stable
- Role: process
- Action: Build three Li‑deposited monolayer C3N configurations: Li at the α site in‑plane (α_in), Li at α site out‑of‑plane (α_out), and Li at β site out‑of‑plane (β_out). Relax each using DFT. Identify the most stable configuration (expected to be Li@α_out) and retain its relaxed structure for EPC calculations.
- Evidence: `/app/outputs/relax_Li_configs.log`

### Step 7: Phonon and EPC calculation for most stable Li‑deposited C3N
- Role: process
- Action: Using the most stable Li‑deposited structure (Li@α_out), compute the phonon dispersion and electron‑phonon coupling; extract λ and ω_log.
- Evidence: `/app/outputs/epc_Li_deposited.log`

### Step 8: Assemble Tc results
- Role: scored (load-bearing)
- Action: For each of the three target systems — (1) 0.2 e/cell electron‑doped C3N (0% strain), (2) 0.2 e/cell electron‑doped C3N (5% biaxial tensile strain), (3) most stable Li‑deposited C3N — compute the superconducting critical temperature Tc using the isotropic McMillan‑Allen‑Dynes formula with a retarded Coulomb pseudopotential μ* = 0.112. Compile the total electron‑phonon coupling constant λ (dimensionless), the logarithmic average phonon frequency ω_log (in cm⁻¹), and Tc (in K) into a single JSON file.
- Output file: `/app/outputs/epc_results.json`
- Format: json
- Contract: JSON object with keys '0.2e_strain_0pct', '0.2e_strain_5pct', 'Li_deposited'. Each key maps to an object with fields: 'lambda' (float, dimensionless), 'omega_log_cm1' (float, cm⁻¹), 'Tc_K' (float, K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/epc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### epc_results.json
- path: `/app/outputs/epc_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled electron‑phonon coupling constant λ, logarithmic average phonon frequency ω_log, and superconducting Tc for the three configurations. These quantities are compared to the paper's reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `0.2e_strain_0pct`:
      - `type`: object
      - `required`: `lambda`, `omega_log_cm1`, `Tc_K`
    - `0.2e_strain_5pct`:
      - `type`: object
      - `required`: `lambda`, `omega_log_cm1`, `Tc_K`
    - `Li_deposited`:
      - `type`: object
      - `required`: `lambda`, `omega_log_cm1`, `Tc_K`
  - `units`:
    - `lambda`: dimensionless
    - `omega_log_cm1`: cm^-1
    - `Tc_K`: K

Notes: The agent must compute λ and ω_log from first‑principles DFT/DFPT before evaluating Tc. The checker performs a reference comparison (values within tolerance) and also verifies expected relative trends among the three systems.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "epc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "0.2e_strain_0pct": {
            "type": "object",
            "required": [
              "lambda",
              "omega_log_cm1",
              "Tc_K"
            ]
          },
          "0.2e_strain_5pct": {
            "type": "object",
            "required": [
              "lambda",
              "omega_log_cm1",
              "Tc_K"
            ]
          },
          "Li_deposited": {
            "type": "object",
            "required": [
              "lambda",
              "omega_log_cm1",
              "Tc_K"
            ]
          }
        },
        "units": {
          "lambda": "dimensionless",
          "omega_log_cm1": "cm^-1",
          "Tc_K": "K"
        }
      },
      "description": "Compiled electron‑phonon coupling constant λ, logarithmic average phonon frequency ω_log, and superconducting Tc for the three configurations. These quantities are compared to the paper's reported values with appropriate tolerances."
    }
  ],
  "notes": "The agent must compute λ and ω_log from first‑principles DFT/DFPT before evaluating Tc. The checker performs a reference comparison (values within tolerance) and also verifies expected relative trends among the three systems."
}
```

## How you are scored
A hidden verifier checks your submitted epc_results.json. It compares your computed λ, ω_log, and Tc for each of the three conditions against reference ranges derived from the published study and also verifies that the relative trends among the three systems are physically consistent. Each condition contributes equally to the final reward. Simply reporting numbers without executing the required DFT/DFPT workflow will not pass the verification.
