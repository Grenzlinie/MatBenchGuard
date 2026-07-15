# Superconducting Tc Estimation of FCC Metallic Hydrogen via First-Principles Electron-Phonon Calculations

## Problem background
Metallic hydrogen has long been predicted to become a high-temperature superconductor when compressed into a monoatomic phase, but the exact magnitude of the superconducting critical temperature (Tc) remains an open theoretical question that depends on the detailed electron-phonon coupling. First-principles calculations can provide quantitative estimates of Tc by directly computing the lattice dynamics and electron-phonon spectral function. This task investigates the superconducting properties of the simple face-centered cubic (FCC) phase of metallic hydrogen at a fixed density corresponding to a Wigner–Seitz radius r_s = 1, using density-functional theory and linear-response calculations.

## Approach
The calculation proceeds through four stages. First, a self-consistent Kohn–Sham DFT calculation is performed for FCC monoatomic hydrogen at r_s = 1, employing a suitable exchange-correlation functional (e.g., the local density approximation) and a standard hydrogen pseudopotential. Second, density-functional perturbation theory (DFPT) is used to obtain the phonon dispersion and eigenvectors. Third, the electron-phonon matrix elements are evaluated and the isotropic Eliashberg spectral function α²F(ω) is constructed on a fine frequency grid. Finally, the Eliashberg equations are solved to yield the superconducting critical temperature Tc; as a simpler alternative, the McMillan–Allen–Dynes formula may be applied with a Coulomb pseudopotential μ* = 0.1. All necessary tools and pseudopotentials are publicly available.

## Reproduction target
Produce the Eliashberg spectral function α²F(ω) for FCC monoatomic hydrogen at Wigner–Seitz radius r_s = 1 and derive the superconducting critical temperature Tc from it. Output the spectral function as a two-column CSV file and the Tc value in Kelvin as a plain text file. The results will be compared against a hidden reference computed from the same underlying theory.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Hydrogen pseudopotential (e.g., H.pz-rrkjus.UPF): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT self-consistent field calculation for FCC metallic hydrogen at r_s=1
- Role: process
- Action: Perform a self-consistent Kohn-Sham DFT calculation for face-centered cubic (FCC) monoatomic hydrogen at a Wigner-Seitz radius r_s=1. Use a suitable exchange-correlation functional (e.g., LDA) and the hydrogen pseudopotential. Obtain the ground-state electron density and Kohn-Sham orbitals required for linear-response.
- Evidence: none

### Step 2: Phonon dispersion calculation for FCC metallic hydrogen at r_s=1
- Role: process
- Action: Using density-functional perturbation theory (DFPT) as implemented in the DFT code, compute the dynamical matrix on a q-point grid and obtain phonon frequencies and eigenvectors. Interpolate to produce the phonon dispersion for FCC hydrogen at r_s=1.
- Evidence: none

### Step 3: Compute Eliashberg spectral function α²F(ω) and output CSV
- Role: scored (load-bearing)
- Action: From the phonon frequencies, eigenvectors, and electron wavefunctions, calculate the electron-phonon matrix elements and the isotropic Eliashberg function α²F(ω) on a fine frequency grid. Output the data as a two-column CSV.
- Output file: `/app/outputs/step_02_alpha2F.csv`
- Format: csv
- Contract: Two-column CSV with header 'frequency (meV)', 'alpha2F'. Frequency column contains positive values in meV; alpha2F column is dimensionless. At least 200 data points covering the full phonon frequency range (0 to ~400 meV).
- Scoring: scored by hidden verifier

### Step 4: Compute superconducting critical temperature Tc
- Role: scored
- Action: Using the α²F(ω) function from the previous step, solve the isotropic Eliashberg equations or apply the McMillan-Allen-Dynes formula to evaluate the superconducting critical temperature Tc with a Coulomb pseudopotential μ*=0.1. Output the Tc value in Kelvin.
- Output file: `/app/outputs/step_03_Tc.txt`
- Format: txt
- Contract: A single line containing the Tc value in Kelvin (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_alpha2F.csv`
- `/app/outputs/step_03_Tc.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_alpha2F.csv
- path: `/app/outputs/step_02_alpha2F.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The Eliashberg spectral function α²F(ω) for FCC metallic hydrogen at r_s=1. The checker will numerically integrate this function to obtain the electron-phonon coupling constant λ, the logarithmic average frequency ω_log, and the resulting Tc via the McMillan-Allen-Dynes formula.
- schema:
  - `type`: table
  - `required_columns`: `frequency (meV)`, `alpha2F`
  - `units`:
    - `frequency (meV)`: meV
    - `alpha2F`: dimensionless

### step_03_Tc.txt
- path: `/app/outputs/step_03_Tc.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: The agent's reported Tc value. The checker compares this value directly to the paper's reported Tc (hidden) within a tolerance band, as a secondary check in addition to the recomputed Tc from the α²F data.
- schema:
  - `type`: text
  - `description`: Single line with the superconducting critical temperature in Kelvin, computed from the submitted α²F using the McMillan-Allen-Dynes formula with μ*=0.1.

Notes: Primary scoring is based on the Tc recomputed by the checker from the submitted α²F, with sanity checks on λ. The agent's directly submitted Tc is also compared as a supporting reference. The lattice stability calculations of the original paper are excluded per the task scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_alpha2F.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency (meV)",
          "alpha2F"
        ],
        "units": {
          "frequency (meV)": "meV",
          "alpha2F": "dimensionless"
        }
      },
      "description": "The Eliashberg spectral function α²F(ω) for FCC metallic hydrogen at r_s=1. The checker will numerically integrate this function to obtain the electron-phonon coupling constant λ, the logarithmic average frequency ω_log, and the resulting Tc via the McMillan-Allen-Dynes formula."
    },
    {
      "file": "step_03_Tc.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line with the superconducting critical temperature in Kelvin, computed from the submitted α²F using the McMillan-Allen-Dynes formula with μ*=0.1."
      },
      "description": "The agent's reported Tc value. The checker compares this value directly to the paper's reported Tc (hidden) within a tolerance band, as a secondary check in addition to the recomputed Tc from the α²F data."
    }
  ],
  "notes": "Primary scoring is based on the Tc recomputed by the checker from the submitted α²F, with sanity checks on λ. The agent's directly submitted Tc is also compared as a supporting reference. The lattice stability calculations of the original paper are excluded per the task scope."
}
```

## How you are scored
A hidden verifier will independently inspect each scored artifact. It will numerically integrate your α²F(ω) data to recompute Tc and the electron-phonon coupling constant λ, then compare both the recomputed Tc and your directly reported Tc to a hidden reference derived from the paper's methodology. Additional consistency checks on the shape and integral properties of α²F(ω) may be applied. The final reward is a weighted sum of these evaluations; delivering physically plausible, self-consistent results is necessary to earn full credit.
