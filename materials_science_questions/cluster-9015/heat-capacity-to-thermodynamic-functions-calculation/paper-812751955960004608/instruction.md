# Band gap temperature dependence calculation for silicon

## Problem background
The forbidden band gap energy (E_g) of a nondegenerate semiconductor decreases with increasing temperature. Understanding this dependence is essential for device design and fundamental physics. Empirical formulas exist, but a rigorous statistical thermodynamic derivation that yields a closed-form expression with meaningful entropy and heat capacity contributions is challenging. This task addresses a theoretical framework that treats the thermal generation of electron-hole pairs as a chemical reaction, leading to a new equation for the band gap change: ΔE_g = A T − B T ln T, where A and B are constants derivable from the partition functions of the charge carriers and the constrained valence band electrons. The goal is to implement this derivation for silicon using provided microscopic parameters and standard physical constants, compute the coefficients A and B, and evaluate ΔE_g at several temperatures.

## Approach
The central idea is to model the excitation of an electron from the valence band edge to the conduction band as the reaction e_∘ → e⁻ + e⁺, where e⁻ is a free electron, e⁺ is a hole, and e_∘ is a valence band edge electron. The standard Gibbs energy change of this reaction equals the band gap energy. Standard-state Gibbs energies for each species are obtained from their translational partition functions: free electrons and holes are treated as ideal boltzons with a volume V and an effective mass geometric mean ⟨m⟩; the valence band edge electrons are assumed to move in a much smaller restricted volume λV. Combining these partition functions yields a general expression for ΔE_g as a function of temperature that contains a constant, a term linear in T, and a term −B T ln T. From this expression, the coefficients A and B can be calculated for any semiconductor given its λ, ⟨m⟩/m₀, and molar volume V. The derivation for silicon uses λ = 1.5×10⁻⁴, ⟨m⟩/m₀ = 1.2, V = 12.05 cm³/mol together with the Boltzmann constant k, Planck constant h, electron rest mass m₀, and Avogadro’s number N_A. After obtaining A and B numerically (in eV/K), ΔE_g is evaluated at the four target temperatures.

## Reproduction target
Implement the statistical thermodynamic derivation to obtain the theoretical coefficients A and B (in eV/K) for silicon in the equation ΔE_g = A T − B T ln T. Then compute ΔE_g (in eV) at T = 100, 200, 300, and 400 K. Output all results into the JSON file specified in the output contract. No experimental data or material parameters beyond those listed are required.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Derive and compute band gap temperature dependence
- Role: scored (load-bearing)
- Action: Implement the statistical thermodynamic derivation for the band gap energy change ΔE_g(T) in silicon. Use the partition function expressions for electrons (q_-), holes (q_+), and valence band edge electrons (q_v) to obtain the general form ΔE_g = A T - B T ln T. Apply the given parameters: λ = 1.5×10⁻⁴, ⟨m⟩/m₀ = 1.2, molar volume V = 12.05 cm³/mol, and standard physical constants (Boltzmann constant k, Planck constant h, electron rest mass m₀, Avogadro's number N_A). Simplify numerically to find the coefficients A and B (in eV/K). Then evaluate ΔE_g at temperatures T = 100, 200, 300, 400 K. Write all results into a JSON file as specified in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"A": float (eV/K), "B": float (eV/K), "DeltaEg_100K": float (eV), "DeltaEg_200K": float (eV), "DeltaEg_300K": float (eV), "DeltaEg_400K": float (eV)}
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
- target_policy: reference_match
- description: Derived coefficients A and B for ΔE_g = A T - B T ln T, and the resulting ΔE_g at 100, 200, 300, 400 K for silicon.
- schema:
  - `type`: object
  - `required`:
    - `A`: float (eV/K)
    - `B`: float (eV/K)
    - `DeltaEg_100K`: float (eV)
    - `DeltaEg_200K`: float (eV)
    - `DeltaEg_300K`: float (eV)
    - `DeltaEg_400K`: float (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `A`: eV/K
    - `B`: eV/K
    - `DeltaEg_100K`: eV
    - `DeltaEg_200K`: eV
    - `DeltaEg_300K`: eV
    - `DeltaEg_400K`: eV

Notes: The agent must compute A and B from first principles using the provided parameters. The checker compares each reported value to the paper's Eq. (18) gold values with appropriate tolerance, and may check internal consistency.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "A": "float (eV/K)",
          "B": "float (eV/K)",
          "DeltaEg_100K": "float (eV)",
          "DeltaEg_200K": "float (eV)",
          "DeltaEg_300K": "float (eV)",
          "DeltaEg_400K": "float (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "A": "eV/K",
          "B": "eV/K",
          "DeltaEg_100K": "eV",
          "DeltaEg_200K": "eV",
          "DeltaEg_300K": "eV",
          "DeltaEg_400K": "eV"
        }
      },
      "description": "Derived coefficients A and B for ΔE_g = A T - B T ln T, and the resulting ΔE_g at 100, 200, 300, 400 K for silicon."
    }
  ],
  "notes": "The agent must compute A and B from first principles using the provided parameters. The checker compares each reported value to the paper's Eq. (18) gold values with appropriate tolerance, and may check internal consistency."
}
```

## How you are scored
A hidden verifier will independently score the `results.json` file. It compares your submitted A and B against theoretically expected reference values, and your ΔE_g at each temperature against the values predicted by the reference form of the equation. All comparisons use tolerances that account for legitimate numerical differences from independent computation. The verifier may also recompute ΔE_g from your own A and B to check internal consistency. Each scored quantity contributes to the final reward.
