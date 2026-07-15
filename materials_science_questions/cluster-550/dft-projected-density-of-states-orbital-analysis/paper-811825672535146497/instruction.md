# DFT electronic structure and magnetic properties of Sr3NiPtO6

## Problem background
The compound Sr3NiPtO6 is a geometrically frustrated insulator that does not exhibit long-range magnetic order down to 1.8 K, a behavior that has been interpreted as a possible spin-liquid ground state. Understanding the electronic structure and magnetic interactions — specifically the Ni magnetic moment, the size of the insulating gap, and the nature of the coupling between Ni ions — is essential for explaining this anomalous magnetic behavior.

## Approach
The core approach is first-principles electronic structure calculations using the all-electron full-potential linearized augmented plane wave (FPLAPW) method within the generalized gradient approximation (GGA). The same crystal structure (lattice parameters and atomic positions) is used for all calculations. The workflow proceeds as follows: (1) a non‑magnetic GGA calculation to establish a baseline; (2) a spin‑polarized ferromagnetic GGA calculation to obtain the total magnetic moment, the Ni spin moment, the insulating gap in the down‑spin channel, and the total energy; (3) an antiferromagnetic GGA calculation with alternating Ni spins along the chain to extract the energy difference between the ferromagnetic and antiferromagnetic configurations; (4) a ferromagnetic GGA calculation with spin‑orbit coupling (SOC) to obtain the orbital magnetic moment on Ni. All calculations can be performed with the open‑source ELK code (or any equivalent all‑electron LAPW code).

## Reproduction target
Compute, via all-electron DFT within GGA, the following quantities for Sr3NiPtO6: (i) the total magnetic moment per formula unit in the ferromagnetic state; (ii) the energy difference between the ferromagnetic and antiferromagnetic (intra‑chain) configurations; (iii) the orbital magnetic moment on Ni induced by spin‑orbit coupling; and (iv) the insulating band gap in the down‑spin channel. Report these results as three JSON files (ferromagnetic_results.json, antiferromagnetic_results.json, soc_results.json) with the exact keys described in the workflow steps below.

## Assets

- Crystal structure of Sr3NiPtO6: 10.1021/cm9810939
- ELK (all-electron full-potential LAPW code): https://elk.sourceforge.net

## Workflow steps

### Step 1: Non-magnetic GGA calculation
- Role: process
- Action: Perform a non-magnetic GGA electronic structure calculation for Sr3NiPtO6 using the public crystal structure. This step provides a metallic baseline and initial wavefunctions for subsequent spin-polarized runs.
- Evidence: `/app/outputs/nm_evidence.txt`

### Step 2: Ferromagnetic GGA results
- Role: scored (load-bearing)
- Action: Run a spin-polarized ferromagnetic GGA calculation. After convergence, extract the total magnetic moment per formula unit (in μB), the Ni spin magnetic moment (μB), the down‑spin channel band gap (eV), and the total energy (eV). Write these values to ferromagnetic_results.json.
- Output file: `/app/outputs/ferromagnetic_results.json`
- Format: json
- Contract: JSON object with required keys: total_magnetic_moment_per_fu (number, μB), Ni_spin_moment (number, μB), band_gap_down_spin (number, eV), total_energy (number, eV).
- Scoring: scored by hidden verifier

### Step 3: Antiferromagnetic GGA results
- Role: scored
- Action: Set up an antiferromagnetic configuration with alternating Ni spins along the chain. Run a GGA calculation for this configuration. After convergence, compute the energy difference ΔE = E_FM − E_AFM (in meV per formula unit). Write the result to antiferromagnetic_results.json.
- Output file: `/app/outputs/antiferromagnetic_results.json`
- Format: json
- Contract: JSON object with required key: energy_difference_FM_minus_AFM (number, meV/f.u.). May optionally include Ni_spin_moment_AFM (number, μB).
- Scoring: scored by hidden verifier

### Step 4: Spin-orbit coupling (SOC) results
- Role: scored (load-bearing)
- Action: Perform a ferromagnetic GGA calculation including spin-orbit coupling (SOC) as a perturbation starting from scalar-relativistic wavefunctions. After convergence, extract the orbital magnetic moment on Ni (in μB). Write the value to soc_results.json.
- Output file: `/app/outputs/soc_results.json`
- Format: json
- Contract: JSON object with required key: Ni_orbital_moment (number, μB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ferromagnetic_results.json`
- `/app/outputs/antiferromagnetic_results.json`
- `/app/outputs/soc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ferromagnetic_results.json
- path: `/app/outputs/ferromagnetic_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact from the ferromagnetic DFT run. Values are compared to the paper's reference within domain-appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `total_magnetic_moment_per_fu`: number (μB)
    - `Ni_spin_moment`: number (μB)
    - `band_gap_down_spin`: number (eV)
    - `total_energy`: number (eV)

### antiferromagnetic_results.json
- path: `/app/outputs/antiferromagnetic_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy difference between ferromagnetic and antiferromagnetic configurations. Compared to the paper's reference.
- schema:
  - `type`: object
  - `required`:
    - `energy_difference_FM_minus_AFM`: number (meV/f.u.)

### soc_results.json
- path: `/app/outputs/soc_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ni orbital magnetic moment from SOC calculation. Compared to the paper's reference.
- schema:
  - `type`: object
  - `required`:
    - `Ni_orbital_moment`: number (μB)

Notes: All outputs are compared to the paper's published numeric results using reference_match policy. Tolerances are hidden. The non-magnetic step evidence is not scored; the task is graded on honest execution of the full workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ferromagnetic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "total_magnetic_moment_per_fu": "number (μB)",
          "Ni_spin_moment": "number (μB)",
          "band_gap_down_spin": "number (eV)",
          "total_energy": "number (eV)"
        }
      },
      "description": "Scored artifact from the ferromagnetic DFT run. Values are compared to the paper's reference within domain-appropriate tolerances."
    },
    {
      "file": "antiferromagnetic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "energy_difference_FM_minus_AFM": "number (meV/f.u.)"
        }
      },
      "description": "Energy difference between ferromagnetic and antiferromagnetic configurations. Compared to the paper's reference."
    },
    {
      "file": "soc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Ni_orbital_moment": "number (μB)"
        }
      },
      "description": "Ni orbital magnetic moment from SOC calculation. Compared to the paper's reference."
    }
  ],
  "notes": "All outputs are compared to the paper's published numeric results using reference_match policy. Tolerances are hidden. The non-magnetic step evidence is not scored; the task is graded on honest execution of the full workflow."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. Each of the three scored output files (ferromagnetic_results.json, antiferromagnetic_results.json, soc_results.json) is independently checked against a reference (hidden gold) using appropriate tolerances. The verifier aggregates the scores from all scored stages into a final reward between 0 and 1. No gold values or tolerances are provided to you. Simply reproducing the format is not enough; the computed physical quantities must lie within the expected range of the reference to earn high credit. The non‑magnetic evidence file (nm_evidence.txt) is required as proof that the prerequisite non‑magnetic calculation was performed, but it is not itself scored.
