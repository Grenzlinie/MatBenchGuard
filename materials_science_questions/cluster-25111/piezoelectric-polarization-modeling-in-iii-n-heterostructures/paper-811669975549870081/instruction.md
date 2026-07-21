# Strain-induced PL shift and piezoelectric coefficient estimation in InGaN/GaN MQWs

## Problem background
In wurtzite III-nitride heterostructures, built‑in spontaneous and piezoelectric polarization fields create large internal electric fields in quantum wells, producing a quantum‑confined Stark effect (QCSE) that can dramatically shift optical transition energies relative to flat‑band conditions. The piezoelectric polarization of coherently strained (In,Ga)N on GaN is a key quantity governing QCSE magnitude and, consequently, the emission wavelength and efficiency of light‑emitting devices. By applying an external biaxial tensile strain, the piezoelectric contribution can be probed independently of the spontaneous polarization because the spontaneous contribution is unchanged by strain. Experimentally, photoluminescence (PL) measurements on (In,Ga)N/GaN multiple quantum wells (MQWs) with different indium contents reveal strain‑induced shifts that can be red or blue depending on the indium fraction. A computational model using the quasi‑cubic deformation potential theory and a linear piezoelectric polarization model, with material constants linearly interpolated from published GaN and InN values, predicts the net PL shift as a competition between a bandgap red‑shift (from deformation potentials) and a blue‑shift (from reduced QCSE). Your task is to implement this computational pipeline to calculate the strain‑dependent PL shifts and to estimate corrected piezoelectric polarization coefficients from the computed shifts and the experimentally observed shifts.

## Approach
The computational approach proceeds as follows. For each of the three indium contents (0.025, 0.085, 0.119), all material parameters (lattice constants, elastic constants C13 and C33, deformation potentials a_g and d5, spontaneous polarization P_SP, and piezoelectric coefficients e31 and e33) are linearly interpolated between the values for GaN and InN using the known literature data. The strain state of the well and barrier under an applied biaxial tensile strain ε is determined using the in‑plane lattice constants of strained and unstrained material and the elastic constants, taking into account a small pre‑strain of the GaN buffer (+0.03%). The resulting in‑plane and out‑of‑plane strain components are decomposed into hydrostatic and uniaxial components. The bandgap change for the well and for the barrier is computed using the quasi‑cubic approximation with the deformation potentials. The total polarization in each layer is the sum of the spontaneous polarization and the piezoelectric polarization (the latter derived from the strain components and the piezoelectric coefficients using the linear piezoelectric model). From the discontinuity of the total polarization across the well/barrier interface, the change in the electric field inside the well is obtained. Using the interface‑localized‑wavefunction approximation, the corresponding change in the QCSE energy is estimated as the product of the field change and the well width (4.2 nm). The net PL shift is then the combination of the bandgap changes and the QCSE shift. Finally, using the experimentally observed PL shifts at the maximum applied strain (a red‑shift of 3 meV for In 0.025 and blue‑shifts of 3 meV and 6 meV for In 0.085 and 0.119, respectively) together with your computed shifts, you will estimate the linear and cubic terms of the piezoelectric polarization discontinuity between GaN and (In,Ga)N.

## Reproduction target
Produce two scored artifacts:
1. A CSV file `pl_shifts.csv` containing the net PL energy shift (in meV) as a function of applied biaxial strain for each of the three indium compositions. The file must include at least the strain values 0, 2×10⁻⁴, 4×10⁻⁴, 6×10⁻⁴, and 8×10⁻⁴ for each composition.
2. A JSON file `corrected_coefficients.json` with keys `linear_delta_PPZ1` and `cubic_delta_PPZ3` giving the estimated linear and cubic piezoelectric polarization discontinuity coefficients (in C/m²).

The goal is to correctly implement the physical model described in the Approach section and to obtain shifts that are consistent with the model's predictions, and to derive polarization coefficients that are internally consistent with your computed shifts and the provided experimental observations.

## Assets

- Piezoelectric and spontaneous polarization constants of GaN and InN (Bernardini et al., Phys. Rev. B 56, R10024, 1997): 10.1103/PhysRevB.56.R10024
- Elastic constants and deformation potentials of GaN and InN (Kim et al., Phys. Rev. B 53, 16310, 1996): 10.1103/PhysRevB.53.16310
- Lattice constants of GaN and InN (Porowski, J. Cryst. Growth 189/190, 153, 1998): 10.1016/S0022-0248(98)00244-9

## Workflow steps

### Step 1: Interpolate material parameters
- Role: process
- Action: Linearly interpolate all material constants (lattice constants a0, elastic constants C13 and C33, deformation potentials a_g and d5, spontaneous polarization P_SP, piezoelectric coefficients e31 and e33) between the values for GaN and InN for each In content (0.025, 0.085, 0.119).
- Evidence: `/app/outputs/material_constants.json`

### Step 2: Compute strain-induced PL energy shifts
- Role: scored (load-bearing)
- Action: For each In content and for applied biaxial tensile strain ε from 0 to 8×10⁻⁴ (at least steps 0, 2×10⁻⁴, 4×10⁻⁴, 6×10⁻⁴, 8×10⁻⁴), compute the net PL energy shift in meV. Determine in-plane and out-of-plane strain components for wells and barriers using the lattice constants and a GaN buffer pre-strain of +0.03%. Convert strains to hydrostatic and uniaxial components, then compute bandgap changes ΔE_g for well and barrier via the quasi-cubic approximation. Compute total polarization (spontaneous + piezoelectric) using the linear piezoelectric polarization model. From the polarization discontinuity at the well/barrier interface, obtain the change in electric field in the well (using static dielectric constant of the well material), estimate the QCSE energy shift as ΔE_w × d_w (well width 4.2 nm), and combine with the bandgap changes to get the net PL shift. Use the interface-localized-wavefunction approximation.
- Output file: `/app/outputs/pl_shifts.csv`
- Format: csv
- Contract: CSV with columns: In_content (float, one of 0.025, 0.085, 0.119), strain (float, applied biaxial strain), PL_shift_meV (float, net PL energy shift in meV).
- Scoring: scored by hidden verifier

### Step 3: Estimate corrected piezoelectric polarization coefficients
- Role: scored
- Action: Using the experimentally observed PL shifts (red-shift of 3 meV for In content 0.025, blue-shifts of 3 meV and 6 meV for 0.085 and 0.119, respectively, all at the maximum applied strain ε = 8×10⁻⁴) together with your computed PL shifts from the previous step, estimate (a) the linear piezoelectric polarization discontinuity coefficient ΔP_PZ^(1) (in C/m²) assuming only a linear term, and (b) the cubic coefficient ΔP_PZ^(3) (in C/m²) assuming the predicted linear term (ΔP_PZ^(1) = -0.6 C/m²) is correct. Report both values.
- Output file: `/app/outputs/corrected_coefficients.json`
- Format: json
- Contract: JSON object with keys: linear_delta_PPZ1 (float, C/m²), cubic_delta_PPZ3 (float, C/m²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pl_shifts.csv`
- `/app/outputs/corrected_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pl_shifts.csv
- path: `/app/outputs/pl_shifts.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Strain-dependent PL energy shift for the three InGaN/GaN MQW samples. The checker recomputes expected shifts from bundled material constants and compares the agent's values with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `In_content`, `strain`, `PL_shift_meV`
  - `units`: object

### corrected_coefficients.json
- path: `/app/outputs/corrected_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Estimated linear and cubic piezoelectric polarization discontinuity coefficients. The checker compares the agent's reported values to the paper's hidden gold values within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `linear_delta_PPZ1`: number
    - `cubic_delta_PPZ3`: number
  - `units`:
    - `linear_delta_PPZ1`: C/m²
    - `cubic_delta_PPZ3`: C/m²

Notes: The workflow uses only publicly reported material constants from the cited literature. The experimentally observed PL shifts are provided as fixed inputs. The computed PL shifts must reproduce the correct trend (blue-shift increasing with In content) and magnitudes consistent with the paper's reported calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pl_shifts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "In_content",
          "strain",
          "PL_shift_meV"
        ],
        "units": {}
      },
      "description": "Strain-dependent PL energy shift for the three InGaN/GaN MQW samples. The checker recomputes expected shifts from bundled material constants and compares the agent's values with an appropriate tolerance."
    },
    {
      "file": "corrected_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "linear_delta_PPZ1": "number",
          "cubic_delta_PPZ3": "number"
        },
        "units": {
          "linear_delta_PPZ1": "C/m²",
          "cubic_delta_PPZ3": "C/m²"
        }
      },
      "description": "Estimated linear and cubic piezoelectric polarization discontinuity coefficients. The checker compares the agent's reported values to the paper's hidden gold values within tolerance."
    }
  ],
  "notes": "The workflow uses only publicly reported material constants from the cited literature. The experimentally observed PL shifts are provided as fixed inputs. The computed PL shifts must reproduce the correct trend (blue-shift increasing with In content) and magnitudes consistent with the paper's reported calculations."
}
```

## How you are scored
A hidden verifier independently evaluates each of your output files. For `pl_shifts.csv`, the verifier recomputes the expected PL shifts using the same equations and the same material constants (which are bundled inside the verifier) and compares your values against the recomputed references using a tolerance that accounts for implementation differences; additionally, the verifier checks that your shifts follow the expected trends (blue‑shift magnitude increasing with indium content and with applied strain). For `corrected_coefficients.json`, the verifier compares your submitted coefficients to reference values derived from the paper and also verifies that the coefficients are consistent with your own `pl_shifts.csv` values. The rewards from both checks are combined into an overall score between 0 and 1.
