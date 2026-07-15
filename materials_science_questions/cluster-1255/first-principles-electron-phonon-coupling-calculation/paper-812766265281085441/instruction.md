# First-principles electron-phonon coupling in doped alkali-metal hydrides

## Problem background
Alkali‑metal hydrides (LiH, NaH, KH) are wide‑gap insulators at ambient pressure. Substitutional doping with alkaline‑earth elements (Be, Mg, Ca) introduces extra electrons that can metalize the system, raising the possibility of phonon‑mediated superconductivity without requiring external pressure. This computational study uses first‑principles density functional theory (DFT) and density functional perturbation theory (DFPT) within the virtual crystal approximation (VCA) to model the doped alloys, compute the electron‑phonon coupling constant λ, the superconducting critical temperature Tc, and the electronic density of states at the Fermi level N(EF) as a function of doping. The key open question is whether the resulting λ and Tc values can be large enough for observable superconductivity, and how the electronic structure evolves with doping.

## Approach
The alloys are represented by a primitive rocksalt (B1) unit cell and treated with the Perdew‑Burke‑Ernzerhof (PBE) exchange‑correlation functional. Norm‑conserving pseudopotentials are used, and the substitutional disorder is handled by the virtual‑crystal approximation: a pseudopotential is generated for a virtual atom with a fractional nuclear charge at each doping concentration. Structural optimisations include zero‑point energy (ZPE) corrections obtained within the quasiharmonic approximation, giving equilibrium lattice parameters. Self‑consistent DFT calculations then yield the electronic band structure and N(EF). Phonon frequencies and eigenvectors are computed on a dense q‑mesh using DFPT, Fourier‑interpolated to produce the phonon density of states and dispersion, and combined with screened electron‑phonon matrix elements to obtain the Eliashberg spectral function α²F(ω). The average electron‑phonon coupling constant λ is obtained from the spectral function, and the isotropic Eliashberg gap equations are solved with a Coulomb pseudopotential μ* = 0.1 to estimate Tc.

## Reproduction target
Your task is to carry out the complete VCA‑DFT/DFPT workflow for three alloy systems: Li1−xBexH, Na1−xMgxH, and K1−xCaxH. You must produce two scored output files:

1. **N_EF_vs_doping.csv**: For each alloy system, compute the electronic density of states at the Fermi level N(EF) (units: states/eV/atom/spin) at several doping concentrations, including the undoped case and at least two doped levels up to the maximum stable doping (0.05, 0.20, and 0.45 for LiBeH, NaMgH, and KCaH, respectively). Arrange the rows for each system in order of increasing doping x.

2. **lambda_Tc_results.json**: For the three alloys at their maximum stable doping (Li0.95Be0.05H, Na0.8Mg0.2H, K0.55Ca0.45H), compute the electron‑phonon coupling constant λ and the superconducting critical temperature Tc (in Kelvin, using μ* = 0.1). Report them as a JSON object with keys 'LiBeH', 'NaMgH', 'KCaH', each containing 'lambda' (float) and 'Tc' (float).

## Assets

- Quantum ESPRESSO (DFT/DFPT code): https://www.quantum-espresso.org/
- EPW (Electron-Phonon Wannier): https://epw-code.org/
- PBE norm-conserving pseudopotentials for H, Li, Be, Na, Mg, K, Ca: https://materialscloud.org/sssp/

## Workflow steps

### Step 1: Prepare VCA pseudopotentials
- Role: process
- Action: Generate Virtual Crystal Approximation (VCA) pseudopotentials for Li/Be, Na/Mg, and K/Ca virtual atoms at the required doping concentrations using norm-conserving pseudopotentials from a public library. The pseudopotentials must be suitable for the DFT code (e.g., Quantum ESPRESSO).
- Evidence: `/app/outputs/vca_pseudo_generation.log`

### Step 2: ZPE-corrected structural optimization
- Role: process
- Action: For each alloy system (Li1-xBexH, Na1-xMgxH, K1-xCaxH) at multiple doping levels (including the target maximum doping and at least two lower levels), perform structural optimization including zero-point energy (ZPE) corrections within the quasiharmonic approximation. Obtain optimized lattice parameters for each composition.
- Evidence: `/app/outputs/zpe_optimized_structures.txt`

### Step 3: Compute N(E_F) vs doping
- Role: scored
- Action: Using the ZPE-optimized structures, run self-consistent DFT calculations and compute the electronic density of states at the Fermi level, N(E_F), for each doping level. Write the results to a CSV file with columns: system, doping_x, N_EF (in states/eV/atom/spin). Ensure the rows for each system are in order of increasing doping.
- Output file: `/app/outputs/N_EF_vs_doping.csv`
- Format: csv
- Contract: CSV with columns: system (e.g. 'LiBeH'), doping_x (float), N_EF (float, units: states/eV/atom/spin). Minimum rows per system: LiBeH at doping levels up to x=0.05; NaMgH up to x=0.20; KCaH up to x=0.45, each including the undoped case and at least two doped levels.
- Scoring: scored by hidden verifier

### Step 4: Phonon and e-ph coupling calculations
- Role: process
- Action: For the three alloys at their maximum stable doping (Li0.95Be0.05H, Na0.8Mg0.2H, K0.55Ca0.45H), compute phonon frequencies and eigenvectors on a sufficiently dense q-mesh using DFPT, then Fourier-interpolate to obtain the phonon density of states and dispersion. Compute the screened electron-phonon matrix elements and evaluate phonon linewidths γ(qj) and the isotropic Eliashberg spectral function α²F(ω).
- Evidence: `/app/outputs/eliasberg_function.log`

### Step 5: Compute λ and Tc
- Role: scored (load-bearing)
- Action: From the Eliashberg spectral function, compute the average electron-phonon coupling constant λ using λ = 2 ∫ (α²F(ω)/ω) dω. Solve the isotropic Eliashberg gap equations with Coulomb pseudopotential μ* = 0.1 to obtain the superconducting critical temperature Tc (in K) for each of the three alloys. Output the results in a JSON file with keys: 'LiBeH', 'NaMgH', 'KCaH', each an object with keys 'lambda' (float) and 'Tc' (float).
- Output file: `/app/outputs/lambda_Tc_results.json`
- Format: json
- Contract: A JSON object with keys: 'LiBeH', 'NaMgH', 'KCaH'. Each value is an object with keys 'lambda' (float) and 'Tc' (float, in K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/N_EF_vs_doping.csv`
- `/app/outputs/lambda_Tc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### N_EF_vs_doping.csv
- path: `/app/outputs/N_EF_vs_doping.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electronic density of states at the Fermi level as a function of alkaline-earth doping for LiBeH, NaMgH, and KCaH alloys. The rows for each system must be in order of increasing doping.
- schema:
  - `type`: table
  - `required_columns`: `system`, `doping_x`, `N_EF`
  - `units`:
    - `N_EF`: states/eV/atom/spin

### lambda_Tc_results.json
- path: `/app/outputs/lambda_Tc_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electron-phonon coupling constant λ and superconducting critical temperature Tc (μ* = 0.1) for the three alloys at maximum stable doping.
- schema:
  - `type`: object
  - `required`:
    - `LiBeH`: object with lambda and Tc
    - `NaMgH`: object with lambda and Tc
    - `KCaH`: object with lambda and Tc
  - `items`:
    - `lambda`: float
    - `Tc`: float (K)

Notes: The agent must perform all calculations from first principles using an open-source DFT/DFPT code (e.g., Quantum ESPRESSO + EPW). The Eliashberg equations must be solved with Coulomb pseudopotential μ* = 0.1. No external/pre-computed data beyond pseudopotentials is allowed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "N_EF_vs_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "doping_x",
          "N_EF"
        ],
        "units": {
          "N_EF": "states/eV/atom/spin"
        }
      },
      "description": "Electronic density of states at the Fermi level as a function of alkaline-earth doping for LiBeH, NaMgH, and KCaH alloys. The rows for each system must be in order of increasing doping."
    },
    {
      "file": "lambda_Tc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LiBeH": "object with lambda and Tc",
          "NaMgH": "object with lambda and Tc",
          "KCaH": "object with lambda and Tc"
        },
        "items": {
          "lambda": "float",
          "Tc": "float (K)"
        }
      },
      "description": "Electron-phonon coupling constant λ and superconducting critical temperature Tc (μ* = 0.1) for the three alloys at maximum stable doping."
    }
  ],
  "notes": "The agent must perform all calculations from first principles using an open-source DFT/DFPT code (e.g., Quantum ESPRESSO + EPW). The Eliashberg equations must be solved with Coulomb pseudopotential μ* = 0.1. No external/pre-computed data beyond pseudopotentials is allowed."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact after your run completes. The verifier checks the N_EF_vs_doping.csv file to ensure that for every alloy system the reported N(EF) increases monotonically with doping concentration — confirming the metalization trend. The lambda_Tc_results.json file is compared to a hidden reference: the verifier checks that your reported λ and Tc values are within generous tolerances that account for the expected spread between different DFT/DFPT implementations (e.g., different basis sets, pseudopotential schemes, and convergence parameters). Both checks contribute to a final reward score between 0 and 1; simply reporting the paper’s numbers without performing the calculations will not pass.
