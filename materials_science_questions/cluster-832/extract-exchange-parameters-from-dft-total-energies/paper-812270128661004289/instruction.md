# Compute Heisenberg-model D/Tp ratios for amorphous and crystalline Gd-based alloys

## Problem background
In Gd-based metallic alloys, the spin-wave stiffness constant \(D\) and the paramagnetic Curie temperature \(T_{\mathrm{p}}\) are observed to be linearly related. For amorphous materials, the ratio \(D/T_{\mathrm{p}}\) is typically lower than that of crystalline counterparts with similar composition. A nearest-neighbor Heisenberg model that incorporates fluctuations in the exchange interaction due to structural disorder can give a prediction for \(D/T_{\mathrm{p}}\) based on the average and variance of the nearest-neighbour distance. The model yields an expression that depends on the atomic spin \(S\), Boltzmann's constant \(k_\mathrm{B}\), the magnetic coordination number \(z\), the mean distance \(r_0\), and, for amorphous systems, the rms distance fluctuation \(\Delta r\) and the exchange-fluctuation amplitude \(\Delta J/J_0\).

This task asks you to compute the \(D/T_{\mathrm{p}}\) ratios predicted by this model for three specific alloys, using parameters from public literature, and to inspect whether the computed values reflect the expected effect of structural disorder.

## Approach
You will implement the analytic expression for \(D/T_{\mathrm{p}}\) that follows from the nearest-neighbour Heisenberg model. For a crystalline material, where disorder is absent, the fluctuation correction vanishes and only the bare first term contributes. For an amorphous material, the full expression includes a correction factor that reduces the ratio relative to the disorder-free value.

You will evaluate the expression for three cases using the parameters detailed in the workflow step:
- an amorphous Gd-based alloy with specified values of \(z\), \(r_0\), \(\Delta r\), and \(\Delta J/J_0\) taken from the literature for amorphous GdFe₂;
- crystalline GdAl₂ (disorder-free, with its own \(z\) and \(r_0\));
- crystalline Gd (disorder-free, with its own \(z\) and \(r_0\)).

In all cases you use the same spin value \(S = 7/2\) and the same \(k_\mathrm{B}\). There is no data fitting or training; the computation is a direct evaluation of the formula for the three parameter sets. You will write the three resulting numbers into a JSON file as specified in the workflow step.

## Reproduction target
Produce a JSON file containing three \(D/T_{\mathrm{p}}\) ratios (in \(\mathrm{meV\,\mathring{A}^2\,K^{-1}}\)) for the amorphous alloy, crystalline GdAl₂, and crystalline Gd, computed from the model and the supplied parameters. The amorphous ratio must be strictly smaller than both crystalline ratios, reflecting the disorder-induced reduction in spin-wave stiffness predicted by the model. The hidden verifier will compare your computed values against expected references and will also verify the structural ordering between the three cases.

## Assets
No external assets are required for this task. All necessary constants (\(k_\mathrm{B}\), \(S\)) and the structural parameters (\(z\), \(r_0\), \(\Delta r\), \(\Delta J/J_0\) for the three cases) are provided directly in the workflow step below. There are no datasets, model weights, or other files to download.

## Workflow steps

### Step 1: Compute D/Tp for amorphous and crystalline cases
- Role: scored
- Action: Implement the formula D/Tp = k_B * r0^2 / [2*(S+1)] * [1 - 2*z*(Δr/r0)*(ΔJ/J0)] when disorder is present, and the disorder-free term (the first factor alone) for crystalline cases. Use S=3.5, k_B=8.617333262e-5 meV/K, and the following per-case parameters: (1) amorphous: z=6, r0=3.47 Å, Δr=0.37 Å, ΔJ/J0=0.25; (2) crystalline GdAl2: z=4, r0=3.422 Å, Δr=0, ΔJ/J0=0; (3) crystalline Gd: z=12, r0=3.573 Å, Δr=0, ΔJ/J0=0. Compute the three values and write them as a JSON object to the output file.
- Output file: `/app/outputs/computed_D_over_Tp.json`
- Format: json
- Contract: {"amorphous": <number>, "crystalline_GdAl2": <number>, "crystalline_Gd": <number>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_D_over_Tp.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_D_over_Tp.json
- path: `/app/outputs/computed_D_over_Tp.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Three D/Tp ratios computed from the Heisenberg model. The checker validates each value against a hidden reference within an absolute tolerance and also verifies that the amorphous value is strictly less than both crystalline values.
- schema:
  - `type`: object
  - `required`: `amorphous`, `crystalline_GdAl2`, `crystalline_Gd`
  - `properties`:
    - `amorphous`:
      - `type`: number
      - `unit`: meV·Å^2·K^{-1}
    - `crystalline_GdAl2`:
      - `type`: number
      - `unit`: meV·Å^2·K^{-1}
    - `crystalline_Gd`:
      - `type`: number
      - `unit`: meV·Å^2·K^{-1}

Notes: The structural parameters for the amorphous case (z, r0, Δr) are taken from Cargill (AIP Conf. Proc. 18, 631, 1974) for amorphous GdFe2 and are provided in the problem statement; no external download is required. Crystalline parameters are from standard structural data. All values are public.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_D_over_Tp.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "amorphous",
          "crystalline_GdAl2",
          "crystalline_Gd"
        ],
        "properties": {
          "amorphous": {
            "type": "number",
            "unit": "meV·Å^2·K^{-1}"
          },
          "crystalline_GdAl2": {
            "type": "number",
            "unit": "meV·Å^2·K^{-1}"
          },
          "crystalline_Gd": {
            "type": "number",
            "unit": "meV·Å^2·K^{-1}"
          }
        }
      },
      "description": "Three D/Tp ratios computed from the Heisenberg model. The checker validates each value against a hidden reference within an absolute tolerance and also verifies that the amorphous value is strictly less than both crystalline values."
    }
  ],
  "notes": "The structural parameters for the amorphous case (z, r0, Δr) are taken from Cargill (AIP Conf. Proc. 18, 631, 1974) for amorphous GdFe2 and are provided in the problem statement; no external download is required. Crystalline parameters are from standard structural data. All values are public."
}
```

## How you are scored
A hidden verifier reads your output file `computed_D_over_Tp.json`. It first confirms that the file is valid JSON and contains the three required keys: `amorphous`, `crystalline_GdAl2`, and `crystalline_Gd`. Each numeric value is then compared against a reference value (which you do not have) using an appropriate tolerance. The verifier also checks that the amorphous ratio is strictly smaller than both crystalline ratios. Your final reward (a float between 0 and 1) is the weighted sum of these checks. Reporting the paper's numbers is not sufficient; the verifier independently evaluates the correctness of your computed results.
