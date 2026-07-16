# Vinet EOS Fitting for a High‑Pressure Organic Crystal Phase

## Problem background
Coronene (C24H12) is a polycyclic aromatic hydrocarbon whose high‑pressure structural behavior is relevant to understanding carbon storage in the Earth's mantle and to modeling compressed organic molecules. At ambient conditions coronene adopts a low‑symmetry crystal structure, and under pressure it transforms to a high‑pressure monoclinic phase. Characterizing the compressibility of this high‑pressure phase is typically done by fitting an equation of state to measured pressure–volume data. The Vinet equation of state is widely used for solids under compression; its two key material parameters are the zero‑pressure bulk modulus K0 and its pressure derivative K0′. Determining these parameters from experimental data requires a non‑linear least‑squares regression that accounts for the coupling between K0, K0′ and the zero‑pressure volume.

## Approach
The Vinet equation of state relates pressure P and unit‑cell volume V through three parameters: the zero‑pressure volume V0, the zero‑pressure bulk modulus K0, and its pressure derivative K0′. The equation is:

P(V) = 3 K0 ( (1 - x) / x² ) exp( (3/2) (K0′ - 1) (1 - x) )

where x = (V / V0)^(1/3). Given the measured (P, V) data, all three parameters are estimated simultaneously by non‑linear least squares — typically by minimizing the sum of squared residuals between the computed pressures and the observed pressures. The fitting can be performed with standard optimization libraries (e.g., the Levenberg‑Marquardt algorithm). The two physically meaningful parameters are K0 (the bulk modulus at zero pressure, in GPa) and K0′, which quantifies the pressure dependence of the bulk modulus.

## Reproduction target
Using the provided pressure–volume data for the high‑pressure coronene phase, perform a non‑linear least‑squares fit of the Vinet equation of state and extract the optimal values of K0 (in GPa) and K0′. Write these two numbers to the output file `/app/outputs/eos_fit_results.json` in the specified JSON format.

## Assets

- Pressure‑volume data of coronene phase II

## Workflow steps

### Step 1: Vinet EOS fitting
- Role: scored (load-bearing)
- Action: Read the provided pressure‑volume data from the bundled CSV file, fit the Vinet equation of state using non‑linear least‑squares regression, and output the best‑fit values of the zero‑pressure bulk modulus K0 (GPa) and its pressure derivative K0′.
- Output file: `/app/outputs/eos_fit_results.json`
- Format: json
- Contract: {"type": "object", "required": ["K0_GPa", "K0_prime"], "properties": {"K0_GPa": {"type": "number", "units": "GPa"}, "K0_prime": {"type": "number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_fit_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_fit_results.json
- path: `/app/outputs/eos_fit_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted zero‑pressure bulk modulus (K0 in GPa) and pressure derivative (K0′, dimensionless) from the Vinet equation of state applied to the provided pressure‑volume data.
- schema:
  - `type`: object
  - `required`: `K0_GPa`, `K0_prime`
  - `properties`:
    - `K0_GPa`:
      - `type`: number
      - `units`: GPa
    - `K0_prime`:
      - `type`: number

Notes: The earlier experimental stages (2D XRD image integration, unit‑cell refinement) are omitted because raw diffraction images are not publicly available in machine‑readable form and require proprietary software. Only the final computational EOS fitting step with published table data is reproduced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_fit_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "K0_GPa",
          "K0_prime"
        ],
        "properties": {
          "K0_GPa": {
            "type": "number",
            "units": "GPa"
          },
          "K0_prime": {
            "type": "number"
          }
        }
      },
      "description": "Fitted zero‑pressure bulk modulus (K0 in GPa) and pressure derivative (K0′, dimensionless) from the Vinet equation of state applied to the provided pressure‑volume data."
    }
  ],
  "notes": "The earlier experimental stages (2D XRD image integration, unit‑cell refinement) are omitted because raw diffraction images are not publicly available in machine‑readable form and require proprietary software. Only the final computational EOS fitting step with published table data is reproduced."
}
```

## How you are scored
Your submitted `eos_fit_results.json` will be evaluated by a hidden verifier. The verifier will independently fit the Vinet equation of state to the same input data using a reference non‑linear least‑squares procedure and will compare your reported K0_GPa and K0_prime against the expected values (derived from that reference fit). The comparison uses an absolute tolerance that accounts for minor numerical differences between independent fitting implementations. The closer your numbers are to the reference, the higher your score — with full credit for a match within tolerance. The score from this stage contributes to your overall task reward.
