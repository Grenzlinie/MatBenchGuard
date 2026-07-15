# Compute Phonon-Induced Spin Dephasing Time of NV- Center in Diamond from First Principles

## Problem background
The negatively charged nitrogen‑vacancy (NV−) center in diamond is a leading solid‑state spin qubit. Its coherence time T2 is a critical figure of merit for quantum information processing. At low temperatures, where population relaxation (T1) is very long, dephasing induced by interactions with lattice vibrations — pure dephasing — is expected to set an upper bound on the achievable T2. Understanding this phonon‑induced pure dephasing from first principles is therefore essential for predicting and improving qubit performance.

## Approach
We compute the pure dephasing time using a first‑principles workflow that combines constrained density functional theory (cDFT), harmonic lattice dynamics, and a second‑order cumulant expansion. The spin Hamiltonian includes zero‑field splitting (ZFS) and hyperfine interaction (HFI) terms. The key idea is that thermal lattice vibrations modulate these spin‑Hamiltonian parameters, causing energy‑level fluctuations. To capture this, the workflow first obtains the ground‑state electronic structure of an NV− center in a diamond supercell via spin‑polarized cDFT, from which the ZFS tensor and HFI tensor are computed. Next, finite‑displacement gradients of these tensors with respect to every atomic coordinate are evaluated. In parallel, harmonic phonon eigenmodes and frequencies are obtained from DFT force constants (using an open‑source phonon package). Combining phonon‑mode displacements with the spin‑Hamiltonian gradients yields the time‑dependent energy‑difference fluctuation δE(t). The thermal autocorrelation function C(t)=⟨δE(t)δE(0)⟩_T is built using harmonic‑phonon statistics and Bose‑Einstein occupations. From C(t) one extracts the mean‑square fluctuation Δ²=C(0) and the correlation time τ_c, which then yield the pure dephasing function D(t)=exp[−g(t)] and the pure dephasing time 1/Γ[pure] within the second‑order cumulant (Gaussian) approximation. The entire pipeline runs with open‑source DFT codes (e.g., Quantum ESPRESSO) that provide the necessary wavefunctions and force constants; the required post‑processing formulas for ZFS and HFI are standard magnetic dipole–dipole and hyperfine expressions.

## Reproduction target
Compute the pure dephasing time 1/Γ[pure] (in seconds) of a single NV− center in diamond at temperatures **10 K** and **70 K** using the full first‑principles pipeline: constrained DFT ground state, finite‑difference gradients of the ZFS and HFI tensors, harmonic phonon calculation, construction of the energy‑fluctuation autocorrelation, and extraction of the dephasing time via the second‑order cumulant expansion. Report the computed values in a machine‑readable JSON file at `/app/outputs/dephasing_times.json`.

## Assets

- Diamond crystal structure (CIF): https://next-gen.materialsproject.org/materials/mp-66
- phonopy: https://phonopy.github.io/phonopy/
- Quantum ESPRESSO or equivalent DFT code with constrained DFT capability: https://www.quantum-espresso.org/
- Python scientific packages (numpy, scipy): https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Ground-state constrained DFT calculation
- Role: process
- Action: Build a 3×3×2 diamond supercell containing a single NV− center (215 atoms). Perform a spin-polarized constrained DFT calculation (triplet state) using the PBE functional and a plane-wave code to obtain the ground-state Kohn–Sham wavefunction, and compute the zero-field splitting (ZFS) tensor D and hyperfine interaction (HFI) tensor A_hfi for the equilibrium geometry.
- Evidence: none

### Step 2: Finite-difference gradient evaluation
- Role: process
- Action: For each atom and each Cartesian direction, displace the atom by ±1e-3 Å from its equilibrium position, recompute the ground state, and form central-difference gradients ∇_a D and ∇_a A_hfi for all atoms.
- Evidence: none

### Step 3: Harmonic phonon calculation
- Role: process
- Action: Using DFT force constants (from finite-displacement or density-functional perturbation theory), compute harmonic phonon eigenmodes and frequencies with the phonopy package on an 8×8×3 q-point grid (244 irreducible q-points).
- Evidence: none

### Step 4: Energy-fluctuation autocorrelation and cumulant expansion
- Role: process
- Action: Construct the time-dependent energy-difference fluctuation δE(t) by contracting phonon-mode displacements with the pre-computed ZFS and HFI gradients, following the spin-phonon expansion. For temperatures 10 K and 70 K, compute the thermal autocorrelation function C(t)=⟨δE(t)δE(0)⟩_T using harmonic phonon statistics and Bose-Einstein occupations. From C(t) extract the mean-square fluctuation Δ²=C(0) and the correlation time τ_c, then obtain the pure dephasing time 1/Γ[pure] within the second-order cumulant (Gaussian) approximation.
- Evidence: none

### Step 5: Report pure dephasing times
- Role: scored (load-bearing)
- Action: Write the computed pure dephasing time 1/Γ[pure] (in seconds) for temperatures 10 K and 70 K to a JSON file.
- Output file: `/app/outputs/dephasing_times.json`
- Format: json
- Contract: A JSON object with keys '10' and '70' mapping to positive numbers (seconds). Example: {"10": 1.0, "70": 1.0}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dephasing_times.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dephasing_times.json
- path: `/app/outputs/dephasing_times.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Pure dephasing time 1/Γ[pure] (seconds) at 10 K and 70 K.
- schema:
  - `type`: object
  - `required`: `10`, `70`
  - `properties`:
    - `10`:
      - `type`: number
      - `description`: Pure dephasing time (seconds) at 10 K
    - `70`:
      - `type`: number
      - `description`: Pure dephasing time (seconds) at 70 K
  - `additionalProperties`: False

Notes: The checker compares both values against hidden paper-derived golds with a factor-of-10 tolerance. Both values must be finite positive numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dephasing_times.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "10",
          "70"
        ],
        "properties": {
          "10": {
            "type": "number",
            "description": "Pure dephasing time (seconds) at 10 K"
          },
          "70": {
            "type": "number",
            "description": "Pure dephasing time (seconds) at 70 K"
          }
        },
        "additionalProperties": false
      },
      "description": "Pure dephasing time 1/Γ[pure] (seconds) at 10 K and 70 K."
    }
  ],
  "notes": "The checker compares both values against hidden paper-derived golds with a factor-of-10 tolerance. Both values must be finite positive numbers."
}
```

## How you are scored
A hidden verifier inspects the artifacts you write under `/app/outputs`. Each scored workflow step carries a share of the total reward. The main scored artifact is `dephasing_times.json`; the verifier reads the pure dephasing times you report for 10 K and 70 K and compares them to a hidden reference. Because independent implementations can differ (different DFT codes, basis sets, convergence settings), the comparison uses a tolerance band that accepts correct reproductions while rejecting random guesses. The verifier does **not** simply check for equality with a single number. Additional smaller checks may validate the presence and format of intermediate evidence. Reporting plausible‑looking numbers without real execution will not earn full credit.
