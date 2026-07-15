# FCC Metallic Hydrogen Stability and Superconductivity from Ab Initio Density-Functional Theory

## Problem background
Metallic hydrogen is a high-pressure phase predicted to exhibit high-temperature superconductivity and unusual lattice stability. At sufficient pressure, molecular hydrogen is expected to dissociate into a monoatomic metallic phase that can adopt simple crystal structures such as face-centred cubic (FCC). A central question is at what density (Wigner-Seitz radius r_s) the FCC structure becomes dynamically stable—that is, all its phonon frequencies are real—and what superconducting critical temperature T_c it can reach near that stability boundary. Nonperturbative density-functional calculations can provide quantitative answers to both questions, and the present task reproduces these key predictions.

## Approach
We study monoatomic metallic hydrogen in the FCC crystal structure using density-functional theory (DFT) and density-functional perturbation theory (DFPT) within the plane-wave pseudopotential formalism. The workflow starts by constructing primitive FCC cells with one hydrogen atom and varying the lattice constant to cover a range of Wigner-Seitz radii r_s. For each r_s, a self-consistent DFT calculation yields the ground-state charge density, followed by DFPT phonon calculations on a q-point grid to obtain the phonon frequencies. A phonon mode with an imaginary frequency signals dynamical instability; the stability threshold is the smallest r_s for which all phonon modes at all q-points are real. Separately, at a fixed density of r_s = 1.0, we compute the electron-phonon coupling strength λ and the Eliashberg spectral function α²F(ω) using the same DFPT machinery. From these we numerically solve the Eliashberg equations to obtain the superconducting critical temperature T_c. The calculations are performed with Quantum ESPRESSO, an open-source DFT code, using a publicly available hydrogen pseudopotential.

## Reproduction target
We aim to determine two quantitative results: (1) the Wigner-Seitz radius r_s (dimensionless) at which FCC metallic hydrogen becomes dynamically stable, i.e., the threshold below which all phonon modes are real, and (2) the superconducting critical temperature T_c (in Kelvin) of FCC metallic hydrogen at r_s = 1.0. Both results are obtained by executing the DFT/DFPT pipeline described below and writing the values to the designated output files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Hydrogen pseudopotential (norm-conserving or ultrasoft): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate FCC crystal structures for a range of Wigner-Seitz radii
- Role: process
- Action: Create DFT input files for the FCC structure of monoatomic metallic hydrogen. The primitive cell contains one hydrogen atom. Define the lattice constant a (in Bohr) from the Wigner-Seitz radius r_s using a = (16π/3)^{1/3} * r_s * a_B, with a_B = 1 Bohr. Prepare a set of r_s values covering the expected stability threshold (e.g., from 0.9 to 1.3).
- Evidence: `/app/outputs/fcc_structures.txt`

### Step 2: Self-consistent DFT calculations
- Role: process
- Action: For each r_s, run a self-consistent DFT calculation (pw.x) to obtain the ground-state charge density and Kohn-Sham wavefunctions. Use an appropriate k-point mesh and plane-wave energy cutoff.
- Evidence: `/app/outputs/scf_logs.zip`

### Step 3: Phonon dispersion calculations
- Role: process
- Action: For each r_s, run density-functional perturbation theory (ph.x) on a q-point grid covering the Brillouin zone to compute phonon frequencies. The phonon frequencies determine dynamical stability (real = stable, imaginary = unstable).
- Evidence: `/app/outputs/phonon_dispersion_plots.zip`

### Step 4: Determine FCC dynamical stability threshold
- Role: scored (load-bearing)
- Action: Analyze the computed phonon frequencies across all r_s values. Identify the smallest r_s for which all phonon modes at all q-points are real (no imaginary frequencies). Write this threshold r_s to the output file.
- Output file: `/app/outputs/rs_stability.txt`
- Format: txt
- Contract: First line: a floating-point number (e.g., 1.05). No units; r_s is defined relative to the Bohr radius.
- Scoring: scored by hidden verifier

### Step 5: Electron-phonon coupling calculation
- Role: process
- Action: For the specific case r_s = 1.0, run electron-phonon coupling calculations using ph.x with the electron_phonon option, then use q2r.x, matdyn.x, and lambda.x to obtain the Eliashberg spectral function α²F(ω) and the electron-phonon coupling constant λ.
- Evidence: `/app/outputs/elph_outputs.zip`

### Step 6: Compute superconducting critical temperature
- Role: scored (load-bearing)
- Action: Using the computed α²F(ω) and λ, solve the Eliashberg equations numerically to obtain the superconducting critical temperature T_c. Output the value in Kelvin.
- Output file: `/app/outputs/tc_value.txt`
- Format: txt
- Contract: First line: a floating-point number representing T_c in Kelvin (e.g., 600).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rs_stability.txt`
- `/app/outputs/tc_value.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rs_stability.txt
- path: `/app/outputs/rs_stability.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The Wigner-Seitz radius r_s at which FCC metallic hydrogen becomes dynamically stable (all phonon modes real). Compared to a hidden reference value with a tolerance; credit decays as the difference increases.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: dimensionless (r_s)

### tc_value.txt
- path: `/app/outputs/tc_value.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Superconducting critical temperature T_c (in Kelvin) for FCC hydrogen at r_s=1.0. Compared to a hidden reference value with a tolerance; credit decays as the difference increases.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: Kelvin

Notes: The agent must run full DFT and DFPT calculations using Quantum ESPRESSO (open-source) and a publicly available hydrogen pseudopotential. The scored artifacts are derived from the raw simulation outputs; the checker compares the reported values to the paper's results with generous tolerances to account for code/pseudopotential differences. No paper identity or gold values are revealed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rs_stability.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "dimensionless (r_s)"
        }
      },
      "description": "The Wigner-Seitz radius r_s at which FCC metallic hydrogen becomes dynamically stable (all phonon modes real). Compared to a hidden reference value with a tolerance; credit decays as the difference increases."
    },
    {
      "file": "tc_value.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "Kelvin"
        }
      },
      "description": "Superconducting critical temperature T_c (in Kelvin) for FCC hydrogen at r_s=1.0. Compared to a hidden reference value with a tolerance; credit decays as the difference increases."
    }
  ],
  "notes": "The agent must run full DFT and DFPT calculations using Quantum ESPRESSO (open-source) and a publicly available hydrogen pseudopotential. The scored artifacts are derived from the raw simulation outputs; the checker compares the reported values to the paper's results with generous tolerances to account for code/pseudopotential differences. No paper identity or gold values are revealed to the agent."
}
```

## How you are scored
A hidden verifier will evaluate your output files independently. It reads the numeric value from `/app/outputs/rs_stability.txt` and compares it to a reference value with a tolerance that accounts for legitimate differences between DFT implementations. Similarly, it reads the numeric value from `/app/outputs/tc_value.txt` and compares it to a reference T_c with a tolerance. In both cases, the score is awarded based on how close your computed number is to the reference; the reward decreases as the difference increases. The combined score from these two checks determines your overall task reward.
