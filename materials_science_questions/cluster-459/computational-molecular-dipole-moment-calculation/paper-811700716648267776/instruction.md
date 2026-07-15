# Computational Study of Vibrational Dipole Moments for a Diatomic Ion

## Problem background
Cold molecular ions such as XH⁺ are promising for quantum information, precision measurement, and controlled reaction studies. Their large rotational constants and, for many metal‑hydride ions, zero metal nuclear spin make them advantageous for laser cooling and state preparation. To estimate the timescales for cooling and the achievable measurement precision, one needs accurate vibrational permanent dipole moments (PDM_v), transition dipole moments (TDM_{v-v'}), and spontaneous emission rates (A_v). This task computes these quantities from first principles for a representative ion.

## Approach
The computational strategy consists of two parts: electronic structure and vibrational analysis. First, the ground‑state potential energy curve E(R) and electric dipole moment function μ(R) are obtained from ab initio calculations at the CASPT2 level with the spin‑free DKH3 relativistic Hamiltonian and ANO‑RCC basis sets, on a grid of internuclear distances R. Second, the radial vibrational Schrödinger equation for J=0 is solved numerically using the Numerov method to yield all bound vibrational wavefunctions and energies. From these wavefunctions and μ(R), permanent dipole moments (PDM_v) are computed by numerical integration, transition dipole moments (TDM_{v-v'}) are evaluated among the lowest vibrational states, and spontaneous emission rates (Einstein A coefficients) are derived from the TDMs and energy differences. The target system is MgH⁺.

## Reproduction target
For the diatomic ion ²⁴MgH⁺, produce the following outputs by executing the full CASPT2/Numerov protocol:

- Spectroscopic constants: equilibrium bond length Rₑ (Å), harmonic vibrational frequency ωₑ (cm⁻¹), rotational constant Bₑ (cm⁻¹), vibration–rotation coupling constant αₑ (cm⁻¹), and electronic dissociation energy Dₑ (eV).
- Vibrational permanent dipole moments (PDM_v) and energies for all bound vibrational levels.
- Transition dipole moments (TDM_{v-v'}) between the five lowest vibrational states.
- Spontaneous emission rates (A_v) for the four lowest excited vibrational levels.

All quantities must be derived from the raw electronic structure data (potential energy and dipole moment curves) and written to the JSON files specified in the workflow steps.

## Assets

- OpenMolcas quantum chemistry package: https://gitlab.com/Molcas/OpenMolcas
- ANO-RCC basis sets for Mg and H: https://www.basissetexchange.org/
- Python scientific stack (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: CASPT2 potential energy and dipole moment calculation
- Role: process
- Action: Run a CASSCF(2,2) calculation followed by CASPT2 with the DKH3 Hamiltonian and ANO-RCC basis sets for Mg and H. Compute the electronic ground-state energy and dipole moment (density expectation value) on a grid of internuclear distances R = 1.5 au to 50.0 au (in steps of 0.1 au or similar). Write the resulting PEC E(R) and dipole function μ(R) to a CSV evidence file.
- Evidence: `/app/outputs/pe_and_dipole_curve.csv`

### Step 2: Numerov solution of vibrational Schrödinger equation
- Role: process
- Action: Using the PEC E(R) from the previous step, solve the radial Schrödinger equation for J=0 with the Numerov method. Obtain all bound vibrational wavefunctions ψ_v(R), energies E_v, and rotational constants B_v. Use a dense integration grid (e.g., 1000 points on R=1.5–15 au) for accurate permanent dipole moments. Save the vibrational energies, rotational constants, and squared wavefunction grid values to an evidence file.
- Evidence: `/app/outputs/vibrational_data.npy`

### Step 3: Spectroscopic constants
- Role: scored
- Action: From the computed PEC E(R), extract the equilibrium bond length R_e (Å), harmonic vibrational frequency ω_e (cm⁻¹), rotational constant B_e (cm⁻¹), vibration–rotation coupling constant α_e (cm⁻¹), and electronic dissociation energy D_e (eV). Write these to spectroscopic_constants.json.
- Output file: `/app/outputs/spectroscopic_constants.json`
- Format: json
- Contract: {"R_e": float, "omega_e": float, "B_e": float, "alpha_e": float, "D_e": float}
- Scoring: scored by hidden verifier

### Step 4: Vibrational permanent dipole moments
- Role: scored (load-bearing)
- Action: For every bound vibrational level v, compute the permanent dipole moment PDM_v = ∫ μ(R) |ψ_v(R)|² R² dR / ∫ |ψ_v(R)|² R² dR using Simpson quadrature over the grid. Report the vibrational energy E_v (cm⁻¹), rotational constant B_v (cm⁻¹), and PDM (Debye) for each level. Write the results as an array in pdms.json.
- Output file: `/app/outputs/pdms.json`
- Format: json
- Contract: [{"v": int, "energy": float, "B_v": float, "pdm": float}]
- Scoring: scored by hidden verifier

### Step 5: Vibrational transition dipole moments
- Role: scored
- Action: Using a fine integration grid (e.g., 1500 points on R=1.5–8.0 au), evaluate transition dipole moments TDM_{v-v'} = |∫ μ(R) ψ_{v'}^*(R) ψ_v(R) R² dR| / (√∫|ψ_{v'}|² R² dR · √∫|ψ_v|² R² dR) for v, v' = 0..4 (all combinations). Report the non-zero values (or all pairs) in tdms.json, each with fields v, v_prime, and tdm in Debye.
- Output file: `/app/outputs/tdms.json`
- Format: json
- Contract: [{"v": int, "v_prime": int, "tdm": float}]
- Scoring: scored by hidden verifier

### Step 6: Spontaneous emission rates
- Role: scored
- Action: From the transition dipole moments and vibrational energy differences ΔE = E_v - E_{v'}, compute the Einstein A coefficient for v = 1..4 (J=0 → J'=1) as A_v = (16π³/(3ε₀h⁴c³)) Σ_{v'=0}^{v-1} (ΔE)³ |TDM_{v-v'}|². Report the rates in s⁻¹ in sers.json as an array of objects with v and ser.
- Output file: `/app/outputs/sers.json`
- Format: json
- Contract: [{"v": int, "ser": float}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spectroscopic_constants.json`
- `/app/outputs/pdms.json`
- `/app/outputs/tdms.json`
- `/app/outputs/sers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spectroscopic_constants.json
- path: `/app/outputs/spectroscopic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spectroscopic constants derived from the CASPT2 potential energy curve.
- schema:
  - `type`: object
  - `required`:
    - `R_e`: float (Å)
    - `omega_e`: float (cm⁻¹)
    - `B_e`: float (cm⁻¹)
    - `alpha_e`: float (cm⁻¹)
    - `D_e`: float (eV)

### pdms.json
- path: `/app/outputs/pdms.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Permanent dipole moments and energies for all bound vibrational states.
- schema:
  - `type`: array
  - `items`:
    - `v`: int
    - `energy`: float (cm⁻¹)
    - `B_v`: float (cm⁻¹)
    - `pdm`: float (Debye)

### tdms.json
- path: `/app/outputs/tdms.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Transition dipole moments between the five lowest vibrational states.
- schema:
  - `type`: array
  - `items`:
    - `v`: int
    - `v_prime`: int
    - `tdm`: float (Debye)

### sers.json
- path: `/app/outputs/sers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spontaneous emission rates for the four lowest vibrational excited states.
- schema:
  - `type`: array
  - `items`:
    - `v`: int
    - `ser`: float (s⁻¹)

Notes: All scored quantities are compared against the paper's reported values for MgH⁺ within appropriate tolerances. The agent must produce computed aggregates from the CASPT2 workflow, not read precomputed numbers. Spectroscopic constants require the units as specified; dipole moments in Debye; rates in s⁻¹.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spectroscopic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R_e": "float (Å)",
          "omega_e": "float (cm⁻¹)",
          "B_e": "float (cm⁻¹)",
          "alpha_e": "float (cm⁻¹)",
          "D_e": "float (eV)"
        }
      },
      "description": "Spectroscopic constants derived from the CASPT2 potential energy curve."
    },
    {
      "file": "pdms.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "v": "int",
          "energy": "float (cm⁻¹)",
          "B_v": "float (cm⁻¹)",
          "pdm": "float (Debye)"
        }
      },
      "description": "Permanent dipole moments and energies for all bound vibrational states."
    },
    {
      "file": "tdms.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "v": "int",
          "v_prime": "int",
          "tdm": "float (Debye)"
        }
      },
      "description": "Transition dipole moments between the five lowest vibrational states."
    },
    {
      "file": "sers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "v": "int",
          "ser": "float (s⁻¹)"
        }
      },
      "description": "Spontaneous emission rates for the four lowest vibrational excited states."
    }
  ],
  "notes": "All scored quantities are compared against the paper's reported values for MgH⁺ within appropriate tolerances. The agent must produce computed aggregates from the CASPT2 workflow, not read precomputed numbers. Spectroscopic constants require the units as specified; dipole moments in Debye; rates in s⁻¹."
}
```

## How you are scored
Your work is evaluated by an automated verifier that loads each output artifact and compares your computed numeric quantities to reference values derived from independent high‑level calculations. No single number determines the score; the verifier examines each field of the scored JSON files. The overall reward is a weighted combination:

- Spectroscopic constants: 40% of the final score.
- Permanent dipole moments (PDMs): 30%.
- Transition dipole moments (TDMs): 20%.
- Spontaneous emission rates (SERs): 10%.

Simply reporting reference numbers without performing the CASPT2/Numerov pipeline will not satisfy the requirements; the verifier expects results consistent with a genuine execution of the computational protocol.
