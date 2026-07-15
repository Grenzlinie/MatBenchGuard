# Magnetocrystalline Anisotropy Energy of Fe2AlB2 via DFT

## Problem background
Fe2AlB2 is a promising magnetocaloric material that could enable energy-efficient solid-state cooling. The magnetocaloric performance is strongly influenced by the magnetic anisotropy: the preferred orientation of the magnetization (the easy axis) and the energy cost to rotate it away (the magnetocrystalline anisotropy energy, MAE). Quantifying these properties is essential for designing applications. In this task, you will compute the MAE and the easy-axis orientation for the layered orthorhombic ferromagnet Fe2AlB2 using density-functional theory (DFT).

## Approach
The calculation follows the force-theorem approach to magnetocrystalline anisotropy within DFT. First, perform a scalar-relativistic self-consistent field (SCF) calculation to obtain the charge density for the relaxed Fe2AlB2 crystal structure. Then, keeping the scalar-relativistic potential fixed, carry out two non-self-consistent calculations that include spin-orbit coupling (SOC) with the magnetization oriented along the [001] direction (c-axis) and along the [100] direction (a-axis). The total occupied band energies from these two SOC runs are compared; the anisotropy energy K100 is defined as the energy difference E100 - E001. A negative K100 indicates that the a-axis is easier than the c-axis. The required inputs are the relaxed lattice parameters and atomic positions (provided) and any open-source DFT code that supports spin-orbit coupling.

## Reproduction target
Using an open-source DFT code with spin-orbit coupling, compute the magnetocrystalline anisotropy energy of ferromagnetic Fe2AlB2 with the relaxed crystal structure (a = 2.915 Å, b = 11.017 Å, c = 2.851 Å; Fe at (0, 0.3537, 0.5), Al at (0, 0, 0), B at (0, 0.2063, 0)). Produce two scored artifacts: (1) total_energies.json containing the total occupied band energies (eV per formula unit) for magnetization along [001] and [100]; (2) mae_report.txt stating the derived K100 value (in meV/f.u.) and the identified easy axis (a, b, or c).

## Assets

- Relaxed crystal structure of Fe2AlB2
- Experimental crystal structure of Fe2AlB2: 10.1107/S0108768191006063
- Open-source DFT code with spin-orbit coupling support (e.g., Quantum ESPRESSO, GPAW)

## Workflow steps

### Step 1: DFT total energies with SOC for [001] and [100]
- Role: scored (load-bearing)
- Action: Perform a scalar-relativistic self-consistent field (SCF) DFT calculation for the relaxed Fe2AlB2 crystal structure. Then run two non-self-consistent spin-orbit coupling calculations using the force theorem, with magnetization oriented along [001] and [100]. Extract the total occupied band energies for each direction and write them to total_energies.json.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: JSON object with keys 'E_001' and 'E_100' (numeric values in eV per formula unit).
- Scoring: scored by hidden verifier

### Step 2: MAE report and easy-axis identification
- Role: scored
- Action: Read total_energies.json, compute K100 = (E_100 - E_001) in meV/f.u. (1 eV = 1000 meV). Determine the easy axis: if K100 is negative, the a-axis ([100]) is easier than the c-axis ([001]). Write a summary to mae_report.txt stating the computed K100 value and the identified easy axis.
- Output file: `/app/outputs/mae_report.txt`
- Format: txt
- Contract: Text file containing exactly two lines: 'K100 = <value> meV/f.u.' and 'Easy axis = a' (or 'b' or 'c' as determined).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`
- `/app/outputs/mae_report.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Total occupied band energies for Fe2AlB2 with magnetization along [001] and [100], computed via DFT+SOC.
- schema:
  - `type`: object
  - `required`:
    - `E_001`: number (eV/f.u.)
    - `E_100`: number (eV/f.u.)

### mae_report.txt
- path: `/app/outputs/mae_report.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Summary of the computed magnetocrystalline anisotropy energy and easy-axis orientation.
- schema:
  - `type`: text
  - `required`: `line 1: K100 = <numeric> meV/f.u.`, `line 2: Easy axis = a, b, or c (whichever is determined)`

Notes: The scope focuses on the MAE calculation, which is the main quantitative claim of the paper. Co-equal results on Mn2AlB2 ground state, doping effects, and magnetoelastic effect require exchange-parameter calculations via linear-response and CPA/mean-field Tc estimation that are beyond the feasibility of a straightforward DFT reproduction with the current toolchain and would introduce additional uncertainty. They are omitted with this justification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "E_001": "number (eV/f.u.)",
          "E_100": "number (eV/f.u.)"
        }
      },
      "description": "Total occupied band energies for Fe2AlB2 with magnetization along [001] and [100], computed via DFT+SOC."
    },
    {
      "file": "mae_report.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": [
          "line 1: K100 = <numeric> meV/f.u.",
          "line 2: Easy axis = a, b, or c (whichever is determined)"
        ]
      },
      "description": "Summary of the computed magnetocrystalline anisotropy energy and easy-axis orientation."
    }
  ],
  "notes": "The scope focuses on the MAE calculation, which is the main quantitative claim of the paper. Co-equal results on Mn2AlB2 ground state, doping effects, and magnetoelastic effect require exchange-parameter calculations via linear-response and CPA/mean-field Tc estimation that are beyond the feasibility of a straightforward DFT reproduction with the current toolchain and would introduce additional uncertainty. They are omitted with this justification."
}
```

## How you are scored
A hidden verifier independently examines each output artifact. For total_energies.json, the verifier reads the energies, recomputes the anisotropy metric, and compares it to a hidden reference. For mae_report.txt, it checks that the reported K100 is numerically consistent with the energy file and that the easy-axis assignment is correct. The two stages carry weights that together determine the final reward, which ranges from 0 to 1. All comparisons use tolerances appropriate for DFT code-to-code variation, so a correctly executed reproduction is expected to receive full credit without needing to match any specific paper-reported absolute number.
