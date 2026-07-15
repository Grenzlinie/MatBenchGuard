# Magnetocrystalline Anisotropy in (Fe1-xCox)2B Alloys

## Problem background
Magnetocrystalline anisotropy (MCA) in (Fe1-xCox)2B alloys exhibits multiple spin reorientation transitions as the cobalt concentration changes, making the system a compelling rare-earth-free permanent magnet candidate. Understanding the electronic origin of the nonmonotonic concentration dependence of the MCA energy \(K\) is key to rational material optimization.

## Approach
The task reproduces first-principles density functional theory (DFT) calculations to compute the magnetocrystalline anisotropy energy \(K\) as a function of cobalt concentration \(x\) and tetragonal strain. The alloy structures are built in the body-centered tetragonal I4/mcm (space group 140) using linear interpolation between the experimental zero-temperature lattice parameters of the two endpoint compounds, Fe2B and Co2B. Random substitutional disorder is approximated, for example via virtual crystal approximation or special quasirandom structures. For each composition, spin-polarized DFT self-consistent field calculations are performed with the generalized gradient approximation (PBE functional) and a dense k-point mesh, omitting spin-orbit coupling (SOC). The resulting charge density is then fixed, and SOC is added perturbatively to compute \(K\) as the single-particle energy difference between magnetization oriented along the crystallographic \(c\) axis and along the in-plane directions. The same procedure is applied to the \(x=0.3\) composition under volume-conserving tetragonal distortions to assess the strain dependence of \(K\). All calculations are executed with the open-source Quantum ESPRESSO code and standard PBE pseudopotentials.

## Reproduction target
Perform DFT calculations for (Fe1-xCox)2B at cobalt fractions \(x = 0.0, 0.3, 0.5, 0.8, 1.0\), and produce the resulting magnetocrystalline anisotropy energy \(K\) (in meV per formula unit) for each composition. Additionally, at \(x = 0.3\), apply volume-conserving tetragonal strains that change the \(c/a\) ratio by –3%, 0%, and +3%, and compute the corresponding \(K\) values. The final deliverables are two CSV files containing the concentration-dependent and strain-dependent data, which will be evaluated by a hidden verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP library): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate alloy crystal structures
- Role: process
- Action: For each Co concentration x in {0.0, 0.3, 0.5, 0.8, 1.0}, linearly interpolate the experimental lattice parameters a, c and internal coordinate u between the end compounds Fe2B and Co2B to construct structural models of (Fe1-xCox)2B in the I4/mcm structure. Approximate random disorder, for example using virtual crystal approximation or special quasirandom structures.
- Evidence: none

### Step 2: Self-consistent DFT calculations without spin-orbit coupling
- Role: process
- Action: For each alloy structure, perform a spin-polarized DFT self-consistent field calculation using the GGA (PBE) functional and a dense Monkhorst-Pack k-point mesh to obtain the ground-state charge density and magnetization. Do not include spin-orbit coupling in this stage.
- Evidence: none

### Step 3: Compute magnetocrystalline anisotropy energy K(x)
- Role: scored (load-bearing)
- Action: For each Co concentration, using the charge density from the previous step as a fixed starting point, compute the magnetocrystalline anisotropy energy K as the single-particle energy difference between magnetization along [100] (or [010]) and along [001] directions, including spin-orbit coupling perturbatively.
- Output file: `/app/outputs/K_vs_x.csv`
- Format: csv
- Contract: columns: x (float, cobalt fraction), K_meV_per_fu (float, MCA energy in meV/f.u.)
- Scoring: scored by hidden verifier

### Step 4: Compute K vs. tetragonal strain at x=0.3
- Role: scored
- Action: For x=0.3, apply volume-conserving tetragonal distortions to vary the c/a ratio by -3%, 0%, +3% (three structures). For each distortion, recompute the SCF charge density without spin-orbit coupling, then compute K as in the previous step.
- Output file: `/app/outputs/K_vs_strain_x03.csv`
- Format: csv
- Contract: columns: c_over_a (float, tetragonal ratio), K_meV_per_fu (float, MCA energy in meV/f.u.)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/K_vs_x.csv`
- `/app/outputs/K_vs_strain_x03.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### K_vs_x.csv
- path: `/app/outputs/K_vs_x.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetocrystalline anisotropy energy as a function of cobalt concentration for the five specified compositions.
- schema:
  - `type`: table
  - `required_columns`: `x`, `K_meV_per_fu`
  - `units`:
    - `x`: cobalt fraction (dimensionless)
    - `K_meV_per_fu`: meV per formula unit

### K_vs_strain_x03.csv
- path: `/app/outputs/K_vs_strain_x03.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetocrystalline anisotropy energy as a function of tetragonal strain at x=0.3.
- schema:
  - `type`: table
  - `required_columns`: `c_over_a`, `K_meV_per_fu`
  - `units`:
    - `c_over_a`: tetragonal ratio (dimensionless)
    - `K_meV_per_fu`: meV per formula unit

Notes: The checker verifies relative trends (ordering, monotonicity) rather than absolute values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "K_vs_x.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "K_meV_per_fu"
        ],
        "units": {
          "x": "cobalt fraction (dimensionless)",
          "K_meV_per_fu": "meV per formula unit"
        }
      },
      "description": "Magnetocrystalline anisotropy energy as a function of cobalt concentration for the five specified compositions."
    },
    {
      "file": "K_vs_strain_x03.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "c_over_a",
          "K_meV_per_fu"
        ],
        "units": {
          "c_over_a": "tetragonal ratio (dimensionless)",
          "K_meV_per_fu": "meV per formula unit"
        }
      },
      "description": "Magnetocrystalline anisotropy energy as a function of tetragonal strain at x=0.3."
    }
  ],
  "notes": "The checker verifies relative trends (ordering, monotonicity) rather than absolute values."
}
```

## How you are scored
A hidden verifier independently examines each submitted CSV file against expected structural trends — relative ordering between compositions, monotonicity of the strain response, and shape of the concentration dependence. No single absolute target value is prescribed; instead, the reward is based on whether the computed quantities obey the correct qualitative relationships that reflect the underlying physics. Each scored artifact carries a weight, and the final overall reward is a combination of the per‑artifact scores.
