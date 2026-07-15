# Anharmonic phonon frequency renormalization and electron-phonon coupling in MgB2

## Problem background
MgB2 exhibits superconductivity near 40 K. First-principles calculations and neutron scattering measurements indicate that the E2g in-plane boron phonon near the zone centre is strongly anharmonic. This anharmonicity has been linked to significant frequency renormalization and nonlinear electron–phonon coupling, and it is believed to play a key role in explaining both the high transition temperature and the reduced boron isotope effect. Resolving the size of these effects from first principles is therefore an important test for the understanding of the pairing mechanism in this material.

## Approach
The reproduction isolates the E2g zone‑centre phonon and its interaction with the electronic structure using density‑functional theory (DFT) and subsequent post‑processing.

1. **Crystal structure and frozen‑phonon mapping** – The hexagonal MgB2 unit cell is relaxed within the generalised gradient approximation. Starting from the relaxed structure, total energies are computed as a function of the displacement amplitude *u* along the E2g in‑plane boron eigenmode (boron atoms move in opposite in‑plane directions while Mg remains stationary). This yields a discrete *E(u)* curve.

2. **Anharmonic potential and vibrational frequencies** – The computed *E(u)* data (after subtracting the minimum) are fitted to the form *E(u) = A₂ u² + A₄ u⁴*, giving the quadratic and quartic coefficients *A₂* and *A₄*. The harmonic frequency *ω_H* follows directly from *A₂* and the effective mass of the mode. The self‑consistent harmonic (Hartree‑Fock) frequency *ω_sch* is obtained by solving the coupled equations involving the expectation value ⟨u²⟩. The exact quantum frequency is found by numerically solving the one‑dimensional Schrödinger equation for the potential *A₂ u² + A₄ u⁴* and taking the ground‑to‑first‑excited‑state gap.

3. **Electron–phonon coupling constants** – From Kohn–Sham eigenvalues of the undistorted and frozen‑phonon distorted structures, the Fermi‑surface averaged deformation potential Δ(u) is computed as a function of *u*. Fitting Δ(u) extracts the linear (*B₂′*) and quartic (*B₄′*) electron–phonon coupling coefficients.

4. **λ, Tc, and isotope effect** – Using the anharmonic oscillator eigenstates and the coupling coefficients, the total electron–phonon coupling constant λ is evaluated for the two boron isotope masses *M_B = 10* and *M_B = 11* via the appropriate transition‑matrix formula. The superconducting transition temperature *Tc* for each isotope is then estimated with the McMillan expression and a Coulomb pseudopotential μ* = 0.15, and the boron isotope effect exponent α is computed from the logarithmic derivative −d ln Tc / d ln M_B.

All steps use the open‑source plane‑wave code Quantum ESPRESSO, publicly available GGA pseudopotentials, and standard Python numerical libraries (numpy, scipy).

## Reproduction target
Produce a JSON file `results.json` that contains the following quantities computed from the DFT and post‑processing pipeline described above:

- `harmonic_frequency_meV` – harmonic frequency *ω_H* (meV)
- `sch_frequency_meV` – self‑consistent harmonic frequency *ω_sch* (meV)
- `quantum_frequency_meV` – exact quantum frequency *ω*(E2g) (meV)
- `ratio_A4_A2_sq` – anharmonicity ratio *A₄ / A₂²*
- `lambda_B10` – electron–phonon coupling constant λ for isotope mass *M_B = 10*
- `lambda_B11` – electron–phonon coupling constant λ for isotope mass *M_B = 11*
- `Tc_B10_K` – superconducting transition temperature for *M_B = 10* (K)
- `Tc_B11_K` – superconducting transition temperature for *M_B = 11* (K)
- `isotope_effect_alpha` – boron isotope effect exponent α

All values must be self‑consistently derived from the DFT calculations and the subsequent numerical post‑processing. The workflow uses the standard hexagonal MgB₂ crystal structure (space group P6/mmm), the specified GGA pseudopotentials, and a converged plane‑wave basis.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA pseudopotentials for Mg and B (PSLibrary): https://www.quantum-espresso.org/pseudopotentials/pslibrary
- Python with numpy and scipy: pip install numpy scipy
- MgB2 crystal structure (hexagonal, space group P6/mmm)

## Workflow steps

### Step 1: DFT geometry relaxation of MgB2
- Role: process
- Action: Using Quantum ESPRESSO, relax the lattice parameters and atomic positions of MgB2 within the generalized gradient approximation (GGA) with a sufficiently converged plane-wave cutoff and k-point grid. The initial structure is the standard hexagonal cell.
- Evidence: `/app/outputs/relax.log`

### Step 2: Frozen-phonon energy calculations for E2g mode
- Role: process
- Action: For the relaxed structure, compute total energies as a function of displacement u along the E2g in-plane boron eigenmode (boron atoms move oppositely along x or y, Mg stationary) over a range of displacement amplitudes. Use the same DFT settings as in the relaxation.
- Evidence: `/app/outputs/e2g_energy_vs_u.csv`

### Step 3: Fit anharmonic potential to E(u) data
- Role: process
- Action: Fit the computed E(u) data (subtracting the minimum energy) to the anharmonic form E(u) = A2*u^2 + A4*u^4 to extract the quadratic coefficient A2 and quartic coefficient A4. Calculate the anharmonicity ratio A4/A2^2.
- Evidence: `/app/outputs/fit_results.json`

### Step 4: Compute harmonic frequency
- Role: process
- Action: From A2 and the effective mass M of the E2g mode (M = m_B/2, where m_B is the boron atomic mass), compute the harmonic frequency ω_H = sqrt(A2/M).
- Evidence: none

### Step 5: Solve self-consistent harmonic approximation
- Role: process
- Action: Solve the self-consistent harmonic (Hartree-Fock decoupling) equations using the quartic potential. Compute ⟨u²⟩ = ħ/(2Mω_sch) and ω_sch² = (A2 + 3 A4 ⟨u²⟩) / M iteratively to obtain the anharmonically renormalized frequency ω_sch.
- Evidence: none

### Step 6: Exact quantum solution of the anharmonic oscillator
- Role: process
- Action: Numerically solve the one-dimensional Schrödinger equation with the potential E(u)=A2*u^2+A4*u^4 to obtain the energy difference between the ground and first excited state. Report this as the exact quantum frequency ω(E2g).
- Evidence: none

### Step 7: Compute Fermi-surface averaged deformation potential and EP coupling constants
- Role: process
- Action: From Kohn-Sham eigenvalues of the undistorted and E2g-distorted structures (obtained during the frozen-phonon calculations), compute the Fermi-surface averaged deformation potential Δ(u) as a function of displacement. Fit the displacement dependence to extract the linear (B2′) and quartic (B4′) electron-phonon coupling coefficients.
- Evidence: `/app/outputs/deformation_potential.csv`

### Step 8: Calculate electron-phonon coupling λ, Tc, and isotope effect
- Role: process
- Action: Using the anharmonic oscillator eigenstates and the EP coupling constants, evaluate the total electron-phonon coupling constant λ for boron masses M_B=10 and M_B=11 via the formula λ = N(E_F)*[B2′* Σ|⟨n|Q|0⟩|²/(E_n−E₀) + B4′* Σ|⟨n|Q²|0⟩|²/(E_n−E₀)]. Use the McMillan expression for Tc with μ*=0.15 to obtain Tc for each mass, and compute the boron isotope effect exponent α = −d ln Tc / d ln M_B.
- Evidence: none

### Step 9: Write final results
- Role: scored (load-bearing)
- Action: Collect all computed quantities: harmonic frequency (meV), self-consistent harmonic frequency (meV), exact quantum frequency (meV), ratio A4/A2^2, electron-phonon coupling λ for B-10 and B-11, superconducting Tc for B-10 and B-11 (K), and boron isotope effect exponent α. Save them as a JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys: harmonic_frequency_meV (float), sch_frequency_meV (float), quantum_frequency_meV (float), ratio_A4_A2_sq (float), lambda_B10 (float), lambda_B11 (float), Tc_B10_K (float), Tc_B11_K (float), isotope_effect_alpha (float).
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
- description: JSON file containing the final reproduced quantities: harmonic frequency, self-consistent harmonic frequency, exact quantum frequency, anharmonicity ratio, electron-phonon coupling λ for B-10 and B-11, superconducting Tc for B-10 and B-11, and boron isotope effect α.
- schema:
  - `type`: object
  - `required`: `harmonic_frequency_meV`, `sch_frequency_meV`, `quantum_frequency_meV`, `ratio_A4_A2_sq`, `lambda_B10`, `lambda_B11`, `Tc_B10_K`, `Tc_B11_K`, `isotope_effect_alpha`
  - `properties`:
    - `harmonic_frequency_meV`:
      - `type`: number
      - `unit`: meV
    - `sch_frequency_meV`:
      - `type`: number
      - `unit`: meV
    - `quantum_frequency_meV`:
      - `type`: number
      - `unit`: meV
    - `ratio_A4_A2_sq`:
      - `type`: number
    - `lambda_B10`:
      - `type`: number
    - `lambda_B11`:
      - `type`: number
    - `Tc_B10_K`:
      - `type`: number
      - `unit`: K
    - `Tc_B11_K`:
      - `type`: number
      - `unit`: K
    - `isotope_effect_alpha`:
      - `type`: number

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
          "harmonic_frequency_meV",
          "sch_frequency_meV",
          "quantum_frequency_meV",
          "ratio_A4_A2_sq",
          "lambda_B10",
          "lambda_B11",
          "Tc_B10_K",
          "Tc_B11_K",
          "isotope_effect_alpha"
        ],
        "properties": {
          "harmonic_frequency_meV": {
            "type": "number",
            "unit": "meV"
          },
          "sch_frequency_meV": {
            "type": "number",
            "unit": "meV"
          },
          "quantum_frequency_meV": {
            "type": "number",
            "unit": "meV"
          },
          "ratio_A4_A2_sq": {
            "type": "number"
          },
          "lambda_B10": {
            "type": "number"
          },
          "lambda_B11": {
            "type": "number"
          },
          "Tc_B10_K": {
            "type": "number",
            "unit": "K"
          },
          "Tc_B11_K": {
            "type": "number",
            "unit": "K"
          },
          "isotope_effect_alpha": {
            "type": "number"
          }
        }
      },
      "description": "JSON file containing the final reproduced quantities: harmonic frequency, self-consistent harmonic frequency, exact quantum frequency, anharmonicity ratio, electron-phonon coupling λ for B-10 and B-11, superconducting Tc for B-10 and B-11, and boron isotope effect α."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `results.json` and independently scores each of the nine numeric entries. For each quantity the verifier compares your reported value to a reference value obtained from independent evaluation, applying tolerances that reflect the expected spread of a converged DFT plus post‑processing pipeline. The overall reward is a weighted sum of the individual scores, rescaled to the interval [0, 1]. A high score requires that the computed values lie within the physically justified tolerance windows for each quantity; simply reporting an arbitrary number, even if close to a textbook value, is insufficient if that value is not a faithful result of the described workflow.
