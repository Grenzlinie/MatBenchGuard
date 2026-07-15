# Superconducting parameters from first-principles for BaM2P2 (M=Ni,Rh,Ir)

## Problem background
The ternary phosphides BaM2P2 (M = Ni, Rh, Ir) crystallize in the ThCr2Si2-type body-centered tetragonal structure and are known to exhibit superconductivity. First-principles density functional theory (DFT) calculations of the electronic structure, phonon spectrum, and electron-phonon coupling provide the key quantities that describe a phonon-mediated pairing mechanism: the electronic density of states at the Fermi level N(EF), the Eliashberg spectral function α²F(ω), and the derived superconducting parameters — the coupling constant λ, logarithmically averaged phonon frequency ω_ln, critical temperature Tc (within the Allen–Dynes formalism), and electronic specific heat coefficient γ. This task reproduces those quantities for the three compounds from first principles to test the theoretical description of their superconducting state.

## Approach
The work employs plane-wave pseudopotential DFT in the generalized gradient approximation (PBE). Starting from experimentally reported crystal structures (provided as text files), a structural relaxation is performed to obtain the equilibrium lattice parameters and internal coordinates. A self-consistent field (SCF) calculation yields the total and partial density of states, from which the total N(EF) is extracted. Density-functional perturbation theory is then used to compute phonon frequencies across a suitable q‑point mesh, and the electron-phonon matrix elements are evaluated to construct the Eliashberg spectral function α²F(ω). From α²F(ω) and N(EF) the average electron-phonon coupling λ, the logarithmic average frequency ω_ln, the Allen–Dynes critical temperature Tc (with Coulomb pseudopotential μ* = 0.13), and the electronic specific heat coefficient γ are obtained via standard BCS relations. The entire workflow is applied identically to BaNi2P2, BaRh2P2, and BaIr2P2, allowing comparison of the electron-phonon coupling strength and the resulting superconducting temperatures across the series.

## Reproduction target
For each of the three compounds (BaNi2P2, BaRh2P2, BaIr2P2), produce a JSON file containing the total density of states at the Fermi level N(EF) (in states/eV per unit cell) and the Eliashberg spectral function α²F(ω) as an array of [frequency (meV), dimensionless α²F] pairs. The files must follow the schema: `{"N_EF": <float>, "alpha2F": [[freq_meV, value], ...]}`. The derived superconducting parameters (λ, ω_ln, Tc, γ) are not to be submitted; instead, a hidden verifier will recompute them from the submitted N(EF) and α²F(ω) data. The goal is to provide raw data that, upon integration, reproduces the superconducting quantities computed in the original study, including the correct relative ordering of λ and Tc among the three materials.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- BaNi2P2 experimental crystal structure (ThCr2Si2-type, I4/mmm)
- BaRh2P2 experimental crystal structure
- BaIr2P2 experimental crystal structure

## Workflow steps

### Step 1: DFT and electron-phonon calculations for all three compounds
- Role: process
- Action: For each compound (BaNi2P2, BaRh2P2, BaIr2P2), using Quantum ESPRESSO or an equivalent open-source DFT code, perform: (1) structural relaxation of the initial ThCr2Si2-type cell; (2) a self-consistent field (SCF) calculation to obtain the electronic density of states and the total N(EF); (3) a phonon calculation on a suitable q-point grid; (4) electron-phonon coupling calculation to produce the Eliashberg spectral function α²F(ω). Save all intermediate outputs (SCF data, phonon frequencies, α²F raw data) so that the extraction steps below can read them.
- Evidence: `/app/outputs/dft_logs_and_checkpoints`

### Step 2: Extract BaNi2P2 results
- Role: scored (load-bearing)
- Action: From the outputs of the dft_e3 step for BaNi2P2, extract the total N(EF) (in states/eV per unit cell) and the Eliashberg spectral function α²F(ω) as a list of [frequency_meV, value] pairs. Write these into BaNi2P2_results.json following the schema.
- Output file: `/app/outputs/BaNi2P2_results.json`
- Format: json
- Contract: {"N_EF": number (states/eV/cell total), "alpha2F": [[frequency_meV, dimensionless_alpha2F], ...] }
- Scoring: scored by hidden verifier

### Step 3: Extract BaRh2P2 results
- Role: scored (load-bearing)
- Action: From the outputs of the dft_e3 step for BaRh2P2, extract N(EF) and α²F(ω) and write to BaRh2P2_results.json.
- Output file: `/app/outputs/BaRh2P2_results.json`
- Format: json
- Contract: {"N_EF": number (states/eV/cell total), "alpha2F": [[frequency_meV, dimensionless_alpha2F], ...] }
- Scoring: scored by hidden verifier

### Step 4: Extract BaIr2P2 results
- Role: scored (load-bearing)
- Action: From the outputs of the dft_e3 step for BaIr2P2, extract N(EF) and α²F(ω) and write to BaIr2P2_results.json.
- Output file: `/app/outputs/BaIr2P2_results.json`
- Format: json
- Contract: {"N_EF": number (states/eV/cell total), "alpha2F": [[frequency_meV, dimensionless_alpha2F], ...] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/BaNi2P2_results.json`
- `/app/outputs/BaRh2P2_results.json`
- `/app/outputs/BaIr2P2_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### BaNi2P2_results.json
- path: `/app/outputs/BaNi2P2_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw data for BaNi2P2: total density of states at Fermi level and Eliashberg spectral function.
- schema:
  - `type`: object
  - `required`:
    - `N_EF`: number (states/eV/cell total)
    - `alpha2F`: array of [frequency_meV, dimensionless_alpha2F] pairs

### BaRh2P2_results.json
- path: `/app/outputs/BaRh2P2_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw data for BaRh2P2: total density of states at Fermi level and Eliashberg spectral function.
- schema:
  - `type`: object
  - `required`:
    - `N_EF`: number (states/eV/cell total)
    - `alpha2F`: array of [frequency_meV, dimensionless_alpha2F] pairs

### BaIr2P2_results.json
- path: `/app/outputs/BaIr2P2_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw data for BaIr2P2: total density of states at Fermi level and Eliashberg spectral function.
- schema:
  - `type`: object
  - `required`:
    - `N_EF`: number (states/eV/cell total)
    - `alpha2F`: array of [frequency_meV, dimensionless_alpha2F] pairs

Notes: For each compound the checker will recompute λ, ωln, Allen‑Dynes Tc (μ*=0.13), and γ from the submitted α²F(ω) and N(EF) and compare these derived quantities to the paper‑reported values. The solver must produce the raw spectral function and density of states; the derived superconducting parameters are not required to be submitted explicitly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "BaNi2P2_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "N_EF": "number (states/eV/cell total)",
          "alpha2F": "array of [frequency_meV, dimensionless_alpha2F] pairs"
        }
      },
      "description": "Raw data for BaNi2P2: total density of states at Fermi level and Eliashberg spectral function."
    },
    {
      "file": "BaRh2P2_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "N_EF": "number (states/eV/cell total)",
          "alpha2F": "array of [frequency_meV, dimensionless_alpha2F] pairs"
        }
      },
      "description": "Raw data for BaRh2P2: total density of states at Fermi level and Eliashberg spectral function."
    },
    {
      "file": "BaIr2P2_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "N_EF": "number (states/eV/cell total)",
          "alpha2F": "array of [frequency_meV, dimensionless_alpha2F] pairs"
        }
      },
      "description": "Raw data for BaIr2P2: total density of states at Fermi level and Eliashberg spectral function."
    }
  ],
  "notes": "For each compound the checker will recompute λ, ωln, Allen‑Dynes Tc (μ*=0.13), and γ from the submitted α²F(ω) and N(EF) and compare these derived quantities to the paper‑reported values. The solver must produce the raw spectral function and density of states; the derived superconducting parameters are not required to be submitted explicitly."
}
```

## How you are scored
A hidden verifier independently processes each scored artifact. It reads the submitted N(EF) and α²F(ω) for each compound and computes λ, ω_ln, Tc (Allen–Dynes formula with μ* = 0.13), and γ. These recomputed values are compared on a per‑compound basis to reference values derived from the published study, using tolerances appropriate for DFT‑based electron‑phonon calculations. An additional structural check verifies that the relative ordering of λ and Tc across the three compounds matches the correct physical trend. The final reward is a weighted sum over these checks: the predicted Tc contributes 40%, the coupling constant λ and logarithmic frequency ω_ln contribute 20% each, the electronic specific heat coefficient γ contributes 20%, and the ordering verification contributes 10%. Submitting only the final derived numbers without the raw spectral data is not sufficient; all required JSON files must be present and well‑formed.
