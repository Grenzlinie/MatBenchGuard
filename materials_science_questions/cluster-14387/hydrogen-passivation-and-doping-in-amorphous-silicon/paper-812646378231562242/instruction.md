# Field-dependent activation enthalpy for Si–Si bond breakage in SiO₂

## Problem background
Time‑dependent dielectric breakdown (TDDB) in thin SiO₂ films is a critical reliability concern for VLSI circuits. A proposed molecular mechanism involves an oxygen vacancy defect that creates a weakly bonded Si–Si pair. When an electric field is applied across the oxide, the vacancy dipole interacts with the local field, potentially lowering the energy barrier for bond rupture. Understanding how the activation enthalpy for Si–Si bond breakage depends on field and temperature is essential for predicting device lifetimes under low‑field operating conditions. This task computes the model predictions that underlie that thermochemical picture.

## Approach
The central idea is that the applied oxide field $E_{\text{ox}}$ is enhanced at a vacancy site by a local Lorentz field $E_{\text{loc}} = \frac{3+\chi}{3}E_{\text{ox}}$, where $\chi$ is the electric susceptibility. The oxygen vacancy possesses a permanent dipole moment $p$ arising from the asymmetric SiO₃ environment, which can align with the local field and lower the activation enthalpy $\Delta H$. An induced polarizability term $\alpha$ also contributes a quadratic field energy, but its magnitude relative to the linear dipole term must be quantified. The Clausius–Mossotti relation provides $\alpha$ from the dielectric constant and the volume density of dipoles. The activation enthalpy is then $\Delta H = (\Delta H)_0 - p \cdot E_{\text{loc}}$, ignoring the quadratic term. From this, the field acceleration parameter $\gamma$ (the logarithmic derivative of the reaction rate with respect to field) can be expressed as $\gamma = p \cdot E_{\text{loc}} / (k_{\text{B}} T\, E_{\text{ox}})$.

The task implements these relations to compute the key model quantities: the molecular polarizability, the relative size of the quadratic and linear energy terms at a representative high field, the activation enthalpy at a set of oxide fields, and the field acceleration parameter at several temperatures. No data fitting or external experimental data are used; all constants are taken directly from the paper's model description.

## Reproduction target
Compute the following deterministic quantities from the stated formulas and constants:

1. Molecular polarizability $\alpha$ (in e·cm²/V) via the Clausius–Mossotti relation.
2. The ratio $\frac{1}{2}\alpha E_{\text{loc}}^2 / (p \cdot E_{\text{loc}})$ at $E_{\text{ox}} = 10$ MV/cm, indicating the relative importance of the induced dipole term.
3. Activation enthalpy $\Delta H$ for $E_{\text{ox}} = 0, 2, 4, 6, 8, 10$ MV/cm, and the slope of $\Delta H$ versus $E_{\text{ox}}$.
4. Field acceleration parameter $\gamma$ (in cm/MV) at $T = 300, 400, 500$ K.

Collect all results in a single JSON file (`results.json`) following the schema given in the workflow step. The verifier will independently recompute every quantity and compare them to your reported values.

## Assets
The computation requires only a standard Python environment with `numpy`. Install it via pip (e.g., `python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy`). No external datasets, pre‑trained models, or proprietary tools are needed; all physical constants are provided in the workflow step.

## Workflow steps

### Step 1: Model computation
- Role: scored (load-bearing)
- Action: Implement the Lorentz local field relation (Eloc = ((3+χ)/3) Eox with χ=2.9), the permanent dipole moment p = 3(z*e)(1.2 Å) assuming z*=1, the Clausius–Mossotti molecular polarizability α = [3(εr−1)ε0]/[(εr+2)Nv] with εr=3.9, ε0=5.52e5 eV/(V cm), Nv=2.3e22 cm⁻³, the field‑dependent activation enthalpy ΔH = (ΔH)₀ − p·Eloc with (ΔH)₀=1.15 eV, and the field acceleration parameter γ = p·Eloc/(kBT·Eox). Compute α, the ratio (½α·Eloc²)/(p·Eloc) at Eox=10 MV/cm, ΔH for Eox=0,2,4,6,8,10 MV/cm, and γ at T=300,400,500 K. Write all results into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "alpha": "float (e cm²/V)",
  "quadratic_to_linear_ratio": "float (dimensionless)",
  "activation_enthalpy_slope": "float (eV per MV/cm)",
  "activation_enthalpy_data": [
    {"E_ox": "float (MV/cm)", "E_loc": "float (MV/cm)", "delta_H": "float (eV)"}
  ],
  "field_acceleration_data": [
    {"T": "float (K)", "gamma": "float (cm/MV)"}
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: All deterministic model quantities: polarizability, quadratic‑to‑linear energy ratio, activation enthalpy versus oxide field, and field acceleration parameter versus temperature.
- schema:
  - `type`: object
  - `required`:
    - `alpha`: float (e cm²/V)
    - `quadratic_to_linear_ratio`: float (dimensionless)
    - `activation_enthalpy_slope`: float (eV per MV/cm)
    - `activation_enthalpy_data`: array of {E_ox: float (MV/cm), E_loc: float (MV/cm), delta_H: float (eV)}
    - `field_acceleration_data`: array of {T: float (K), gamma: float (cm/MV)}

Notes: The scorer recomputes every quantity from the same public formulas and constants and compares the agent's reported values to the checker's recomputed values with a hidden tolerance appropriate for floating‑point reproducibility.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha": "float (e cm²/V)",
          "quadratic_to_linear_ratio": "float (dimensionless)",
          "activation_enthalpy_slope": "float (eV per MV/cm)",
          "activation_enthalpy_data": "array of {E_ox: float (MV/cm), E_loc: float (MV/cm), delta_H: float (eV)}",
          "field_acceleration_data": "array of {T: float (K), gamma: float (cm/MV)}"
        }
      },
      "description": "All deterministic model quantities: polarizability, quadratic‑to‑linear energy ratio, activation enthalpy versus oxide field, and field acceleration parameter versus temperature."
    }
  ],
  "notes": "The scorer recomputes every quantity from the same public formulas and constants and compares the agent's reported values to the checker's recomputed values with a hidden tolerance appropriate for floating‑point reproducibility."
}
```

## How you are scored
A hidden verifier will read your `results.json` and recompute every numerical field using the same formulas and constants. It compares your reported values to the recomputed values, using tolerances that account for floating‑point reproducibility. The verifier also checks that the activation enthalpy data are consistent with a linear field dependence. Each scored field contributes to the final reward, which is a weighted sum (in [0,1]). Simply reporting numbers that look plausible is not sufficient; the verifier's comparison is against a genuine recomputation, not a predetermined published value.
