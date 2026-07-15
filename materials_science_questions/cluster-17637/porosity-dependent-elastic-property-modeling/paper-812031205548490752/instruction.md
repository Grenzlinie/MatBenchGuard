# Compute Elastic Moduli of Mesoporous Silica Spheres from Measured Lamb Mode Frequencies

## Problem background
Mesoporous silica spheres (MSMSPs) are attractive for applications in bioimaging, drug delivery, and phononics, where their nanomechanical and elastic properties govern performance. The elastic moduli – bulk modulus B and shear modulus G – can be determined from hypersonic vibrations excited by a pump-probe laser. By measuring the frequency f0 of the lowest-energy radial Lamb mode of an isolated sphere, together with its diameter D and density ρ, the longitudinal and transverse sound velocities sL and sT can be extracted under the assumption of a constant Poisson ratio ν = 0.17. From the velocities and density the moduli B and G follow. For bare (unfilled) porous spheres, the theoretical bulk modulus can also be predicted from the porosity using the Hashin–Shtrikman model with known solid silica moduli. This task asks you to compute these quantities for a set of five nickel-filled MSMSP samples and two bare porous sphere samples from given parameters.

## Approach
We use the classical Lamb theory for the free radial vibration of an isotropic elastic sphere. For a fixed Poisson ratio ν = 0.17, the solution of the characteristic equation gives dimensionless wavenumbers kL = 2.4 and kT = 3.8. The measured Lamb mode frequency f0 then yields the sound velocities:

  sL = (π f0 D) / kL,
  sT = (π f0 D) / kT.

From the velocities and the single-sphere density ρ, the elastic moduli are obtained via the standard relations for an isotropic solid:

  G = ρ · sT²,
  B = ρ · sL² – (4/3)·G.

For the two bare porous sphere samples, the theoretical bulk modulus Bp is computed using the Hashin–Shtrikman formula,

  Bp = (1 – p)·B0 / (1 + p·(3·B0/(4·G0))),

where p is the porosity (volume fraction), B0 = 36.9 GPa and G0 = 31.0 GPa are the bulk and shear moduli of solid (non‑porous) fused silica.

The required per-sample parameters (D, ρ, f0, porosity) are listed in the table below. Your task is to apply the above formulas to each sample and output the computed sL, sT, B, G, and (for the bare spheres) Bp in a CSV file.

Sample parameters (input data):

| sample | D (nm) | porosity (% vol.) | ρ (g/cm³) | f0 (GHz) |
|--------|--------|-------------------|------------|----------|
| 1A     | 1050   | 57                | 1.05       | 3.53     |
| 1B     | 1050   | 57                | 1.25       | 3.35     |
| 1C     | 1050   | 57                | 2.15       | 3.28     |
| Bare 1050 nm | 1050 | 57                | 0.90       | 3.68     |
| 2A     | 620    | 54                | 1.10       | 6.24     |
| 2B     | 620    | 54                | 1.41       | 6.01     |
| Bare 620 nm  | 620  | 54                | 0.95       | 6.35     |

*Note: The bare sphere rows are used ONLY for the theoretical Bp calculation. Leave the velocity and modulus columns empty for those rows.*

## Reproduction target
Produce a CSV file `/app/outputs/elastic_moduli.csv` that contains one row for each of the seven samples (five Ni‑filled and two bare). For each Ni‑filled sample, compute and report the longitudinal sound velocity sL (km/s), transverse sound velocity sT (km/s), bulk modulus B (GPa), and shear modulus G (GPa) using the formulas and input parameters above. For the two bare porous sphere samples, compute and report only the theoretical bulk modulus Bp (GPa) in the `theoretical_Bp_GPa` column; leave the velocity, B, and G columns empty for these rows.

## Assets
No external datasets, models, or tools are required. All necessary input parameters are provided in the Approach section above. You may implement the computations using any standard programming language or script (e.g., Python, Bash, etc.) within the sandbox environment.

## Workflow steps

### Step 1: Compute elastic moduli from given parameters
- Role: scored
- Action: Compute longitudinal and transverse sound velocities (sL, sT) and bulk and shear moduli (B, G) for the five Ni-filled MSMSP samples using the given sphere diameter D, single-sphere density rho, and measured lowest symmetric radial Lamb mode frequency f0, under the assumption of Poisson ratio ν=0.17 which fixes the dimensionless wavenumbers kL=2.4 and kT=3.8. For the two bare porous sphere samples, compute the theoretical bulk modulus Bp using the Hashin-Shtrikman formula with solid silica moduli B0=36.9 GPa, G0=31.0 GPa and porosity p. Output one CSV row per sample (5 Ni-filled + 2 bare) with all computed values.
- Output file: `/app/outputs/elastic_moduli.csv`
- Format: csv
- Contract: Columns: sample (str), D_nm (float), rho_gcm3 (float), f0_GHz (float), sL_kms (float), sT_kms (float), B_GPa (float), G_GPa (float), theoretical_Bp_GPa (float, empty for Ni-filled rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli.csv
- path: `/app/outputs/elastic_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Agent-computed elastic moduli for the seven MSMSP samples. The checker recomputes the values from the provided input parameters and compares to hidden paper-reported gold values with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `D_nm`, `rho_gcm3`, `f0_GHz`, `sL_kms`, `sT_kms`, `B_GPa`, `G_GPa`, `theoretical_Bp_GPa`
  - `description`: Each row provides the computed elastic properties for one sample. For Ni-filled samples, the theoretical_Bp_GPa column is left empty.

Notes: The task is compute-driven; the required parameters (D, rho, f0, porosity) are extracted from the paper's Table 1 and will be provided inline in instruction.md. No external datasets or pre-built artifacts are needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "D_nm",
          "rho_gcm3",
          "f0_GHz",
          "sL_kms",
          "sT_kms",
          "B_GPa",
          "G_GPa",
          "theoretical_Bp_GPa"
        ],
        "description": "Each row provides the computed elastic properties for one sample. For Ni-filled samples, the theoretical_Bp_GPa column is left empty."
      },
      "description": "Agent-computed elastic moduli for the seven MSMSP samples. The checker recomputes the values from the provided input parameters and compares to hidden paper-reported gold values with a tolerance."
    }
  ],
  "notes": "The task is compute-driven; the required parameters (D, rho, f0, porosity) are extracted from the paper's Table 1 and will be provided inline in instruction.md. No external datasets or pre-built artifacts are needed."
}
```

## How you are scored
A hidden verifier will independently recompute the sound velocities and moduli from the same input parameters and compare your reported values against independently determined reference values. The verifier accepts a small relative tolerance (not disclosed) to account for legitimate numerical differences. For each sample, each computed field that matches within tolerance counts toward the final score. The overall score is the fraction of correct fields over all expected fields, yielding a value between 0 and 1. Reporting numbers without actually performing the calculations will not score well because the verifier expects values that are consistent with the formulas and input data.
