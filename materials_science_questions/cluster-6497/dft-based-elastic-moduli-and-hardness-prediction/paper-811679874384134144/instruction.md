# Superconductivity Prediction in fcc Boron under Pressure

## Problem background
High-pressure boron becomes superconducting at pressures above 160 GPa, with experimental critical temperatures reaching several kelvin. First-principles calculations have explored whether an electron-phonon mechanism can explain this behavior. The Hopfield parameter η quantifies the electron-phonon coupling strength, and the McMillan theory relates it to the superconducting transition temperature T_c. This task reproduces the computational predictions of η and T_c for face-centered cubic (fcc) boron at two lattice constants, as done in a first-principles study, to assess the electron-phonon picture.

## Approach
The reproduction uses density functional theory (DFT) with the all-electron full-potential linearized augmented plane-wave (LAPW) method to obtain the electronic structure of fcc boron. The key outputs are the total density of states at the Fermi energy, angular-momentum-resolved densities (s, p, d) inside the muffin-tin spheres, single-scatterer densities, and scattering phase shifts. These are fed into the Gaspari–Gyorffy (rigid-muffin-tin) formula to compute the Hopfield parameter η. The electron–phonon coupling constant is then λ = η / (M ⟨ω⟩²), where M is the boron atomic mass and ⟨ω⟩ is a root-mean-square phonon frequency. Finally, the McMillan equation with a Coulomb pseudopotential μ* converts λ to T_c. The workflow is executed at two lattice constants: a = 4.60 a.u. (compressed, ≈307 GPa) and a = 5.37 a.u. (equilibrium), using fixed parameters ⟨ω⟩ = 1250 K and μ* = 0.1.

## Reproduction target
Compute the Hopfield parameter η and superconducting transition temperature T_c for fcc boron at both the compressed (a = 4.60 a.u.) and equilibrium (a = 5.37 a.u.) lattice constants using the Gaspari–Gyorffy and McMillan formulas with ⟨ω⟩ = 1250 K and μ* = 0.1. The η and T_c for the compressed case must be consistent with the reference values from the original first‑principles prediction.

## Assets

- All-electron full-potential LAPW code (ELK or exciting): https://elk.sourceforge.net/
- Python with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: LAPW electronic structure calculations for fcc boron
- Role: process
- Action: Perform density functional theory (DFT) all-electron full-potential LAPW calculations for face-centered cubic (fcc) boron at two lattice constants: a = 4.60 a.u. (compressed, corresponding to P ≈ 307 GPa) and a = 5.37 a.u. (equilibrium). For each lattice constant, extract: the total density of states at the Fermi energy N(E_F), the angular-momentum-resolved DOS components N_s, N_p, N_d inside the muffin-tin spheres, the single-scatterer DOS N_s^(1), N_p^(1), N_d^(1), the scattering phase shifts δ_s, δ_p, δ_d, and the muffin-tin radius. Store the extracted data in structured JSON files as evidence.
- Evidence: `/app/outputs/lapw_data_compressed.json,lapw_data_equilibrium.json`

### Step 2: Compute Hopfield parameter and Tc for compressed fcc B
- Role: scored (load-bearing)
- Action: Read the LAPW data for a=4.60 a.u. from the evidence file. Compute the Hopfield parameter η using the Gaspari-Gyorffy formula. Then compute the electron-phonon coupling constant λ = η / (M * ⟨ω⟩^2) with the boron atomic mass M and root-mean-square phonon frequency ⟨ω⟩ = 1250 K. Employ the McMillan equation with Coulomb pseudopotential μ^* = 0.1 to obtain the superconducting transition temperature T_c. Write the resulting η and T_c to hopfield_and_tc_compressed.json.
- Output file: `/app/outputs/hopfield_and_tc_compressed.json`
- Format: json
- Contract: {"eta": float (eV/Å^2), "T_c": float (K)}
- Scoring: scored by hidden verifier

### Step 3: Compute Hopfield parameter and Tc for equilibrium fcc B
- Role: scored (load-bearing)
- Action: Read the LAPW data for a=5.37 a.u. from the evidence file. Compute the Hopfield parameter η as above, and the superconducting transition temperature T_c using the same McMillan parameters (⟨ω⟩=1250 K, μ^*=0.1). Write η and T_c to hopfield_and_tc_equilibrium.json.
- Output file: `/app/outputs/hopfield_and_tc_equilibrium.json`
- Format: json
- Contract: {"eta": float (eV/Å^2), "T_c": float (K)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hopfield_and_tc_compressed.json`
- `/app/outputs/hopfield_and_tc_equilibrium.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hopfield_and_tc_compressed.json
- path: `/app/outputs/hopfield_and_tc_compressed.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hopfield parameter η and superconducting transition temperature T_c for fcc boron at a=4.60 a.u. (compressed, P≈307 GPa), computed via Gaspari-Gyorffy and McMillan equations. This quantity is compared against the paper-reported reference to verify the electron-phonon coupling prediction.
- schema:
  - `type`: object
  - `required`: `eta`, `T_c`
  - `properties`:
    - `eta`:
      - `type`: number
      - `unit`: eV/Å^2
    - `T_c`:
      - `type`: number
      - `unit`: K

### hopfield_and_tc_equilibrium.json
- path: `/app/outputs/hopfield_and_tc_equilibrium.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hopfield parameter η and superconducting transition temperature T_c for fcc boron at the equilibrium lattice constant a=5.37 a.u., computed via the same protocol. Together with the compressed case, it confirms the pressure trend (higher η under compression).
- schema:
  - `type`: object
  - `required`: `eta`, `T_c`
  - `properties`:
    - `eta`:
      - `type`: number
      - `unit`: eV/Å^2
    - `T_c`:
      - `type`: number
      - `unit`: K

Notes: The agent must perform LAPW DFT calculations to obtain the necessary electronic structure inputs for the Gaspari-Gyorffy formula. The atomic mass of boron and the phonon frequency ⟨ω⟩=1250 K and μ^*=0.1 are provided in the instruction. The hidden checker will recompute η from the raw LAPW data (if submitted) and compare the reported η and T_c to the paper's reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hopfield_and_tc_compressed.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "eta",
          "T_c"
        ],
        "properties": {
          "eta": {
            "type": "number",
            "unit": "eV/Å^2"
          },
          "T_c": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Hopfield parameter η and superconducting transition temperature T_c for fcc boron at a=4.60 a.u. (compressed, P≈307 GPa), computed via Gaspari-Gyorffy and McMillan equations. This quantity is compared against the paper-reported reference to verify the electron-phonon coupling prediction."
    },
    {
      "file": "hopfield_and_tc_equilibrium.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "eta",
          "T_c"
        ],
        "properties": {
          "eta": {
            "type": "number",
            "unit": "eV/Å^2"
          },
          "T_c": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Hopfield parameter η and superconducting transition temperature T_c for fcc boron at the equilibrium lattice constant a=5.37 a.u., computed via the same protocol. Together with the compressed case, it confirms the pressure trend (higher η under compression)."
    }
  ],
  "notes": "The agent must perform LAPW DFT calculations to obtain the necessary electronic structure inputs for the Gaspari-Gyorffy formula. The atomic mass of boron and the phonon frequency ⟨ω⟩=1250 K and μ^*=0.1 are provided in the instruction. The hidden checker will recompute η from the raw LAPW data (if submitted) and compare the reported η and T_c to the paper's reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier automatically checks the output files. It may recompute the Hopfield parameter η from the intermediate LAPW data you provided (if submitted) and then compares your reported η and T_c for both lattice constants against the expected reference values, using appropriate tolerances. It also verifies the pressure trend (η compressed > η equilibrium). Each scored artifact contributes a share to the overall reward; the final reward is the weighted combination of these checks. Submitting the expected reference numbers without performing the required DFT calculations and post‑processing will not pass the checks.
