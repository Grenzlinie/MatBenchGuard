# Compute reduced Fermi energies for In(As,P) mixed crystals

## Problem background
For III‑V semiconductor mixed crystals, the position of the Fermi level relative to the conduction band edge is a critical quantity for understanding carrier statistics and band structure. At high temperatures the material becomes intrinsic, and the differential thermovoltage φ in this regime can be described by a two‑band Seebeck equation. This equation links the measurable thermovoltage to the reduced Fermi energy η = (ζ−E_L)/kT, the bandgap ΔE, the electron‑to‑hole mobility ratio b, and the scattering mechanism. The task reproduces the calculation of η for three compositions of In(As_y P_{1−y}) at 666 K, using experimentally determined intrinsic thermovoltage and Hall coefficient together with known optical bandgaps and a fixed mobility ratio.

## Approach
The intrinsic Seebeck equation for a two‑band semiconductor with a known scattering mechanism relates the thermovoltage φ to the reduced Fermi energy η. For acoustic‑phonon scattering (τ ∝ E^{−1/2}) the thermal‑scattering transport function A(η) is expressed as the ratio of Fermi‑Dirac integrals: A(η) = F₁(η) / F₀(η). The equation becomes a one‑dimensional nonlinear equation in η once the temperature T, bandgap ΔE, mobility ratio b, and the measured φ are inserted. The bandgap for each composition y is obtained from a linear interpolation between the well‑established bandgaps of InAs and InP. The Hall coefficient R is provided as a consistency check of the intrinsic regime but does not enter the equation directly. For each composition the workflow computes ΔE, sets up the Seebeck equation, and solves it numerically using Fermi‑Dirac integral evaluations and a root‑finding method (e.g., SciPy’s fsolve).

## Reproduction target
Compute the reduced Fermi energy η = (ζ−E_L)/kT for the three In(As_y P_{1−y}) compositions with y = 0.85, 0.80, and 0.60 at T = 666 K. Use the provided intrinsic thermovoltage φ (μV/°C) and Hall coefficient R (cm³/(A s)) for each composition (listed in the workflow step), the mobility ratio b = 70, and compute the bandgap ΔE from the linear relation ΔE(y) = 1.34 − 0.98·y eV. Solve the intrinsic two‑band Seebeck equation for the acoustic‑phonon scattering case and output the three η values as a JSON object with keys 'y_0.85', 'y_0.8', 'y_0.6'. The values are dimensionless.

## Assets

- SciPy: scipy

## Workflow steps

### Step 1: Compute reduced Fermi energies
- Role: scored (load-bearing)
- Action: For each composition (y = 0.85, 0.80, 0.60):
1. Compute the bandgap ΔE = 1.34 − 0.98·y (eV) from the linear relation between InAs and InP optical bandgaps.
2. Use the corresponding intrinsic thermovoltage φ (μV/°C) and Hall coefficient R (cm³/A·s) at 666 K: y=0.85 → φ=−295, R=−28; y=0.80 → φ=−356, R=−39; y=0.60 → φ=−475, R=−150.
3. Set mobility ratio b = 70 and temperature T = 666 K.
4. For each y, solve the intrinsic two-band Seebeck equation
     φ = (k/e) * { -[b/(b+1)] * [A(η) – η] + [1/(b+1)] * [A(η+ΔE/(kT)) – (η+ΔE/(kT))] }
   for the reduced Fermi energy η = (ζ−E_L)/kT, where k/e = 86.1733 μV/K and A is the transport function for acoustic-phonon scattering (τ ∝ E^{−1/2}), given by
     A(η) = F_1(η) / F_0(η)
   with F_j(η) = ∫_0^∞ x^{j+1/2} / (1 + exp(x−η)) dx (the Fermi-Dirac integrals). Use numerical integration and a root-finding method (e.g., SciPy's fsolve).
5. Write the three values to /app/outputs/reduced_fermi_energies.json as a JSON object with keys 'y_0.85', 'y_0.8', 'y_0.6' mapping to the computed η (dimensionless).
- Output file: `/app/outputs/reduced_fermi_energies.json`
- Format: json
- Contract: {"y_0.85": float, "y_0.8": float, "y_0.6": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reduced_fermi_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reduced_fermi_energies.json
- path: `/app/outputs/reduced_fermi_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reduced Fermi energies (ζ−E_L)/kT for the three In(As_y P_1−y) compositions (y=0.85, 0.80, 0.60) computed from the intrinsic Seebeck equation at T=666 K.
- schema:
  - `type`: object
  - `required`:
    - `y_0.85`: float
    - `y_0.8`: float
    - `y_0.6`: float

Notes: Values are dimensionless. The solving agent must compute them from provided inputs and the known transport integral; the output contract does not prescribe numeric results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reduced_fermi_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "y_0.85": "float",
          "y_0.8": "float",
          "y_0.6": "float"
        }
      },
      "description": "Reduced Fermi energies (ζ−E_L)/kT for the three In(As_y P_1−y) compositions (y=0.85, 0.80, 0.60) computed from the intrinsic Seebeck equation at T=666 K."
    }
  ],
  "notes": "Values are dimensionless. The solving agent must compute them from provided inputs and the known transport integral; the output contract does not prescribe numeric results."
}
```

## How you are scored
A hidden verifier reads your file /app/outputs/reduced_fermi_energies.json and compares each computed η value to a hidden gold standard using an absolute tolerance. The verifier is deterministic and does not know which implementation you used. Full credit (all three values within tolerance) earns the maximum reward; each correct value contributes equally, so partial credit is possible. The verifier does not disclose the tolerance or the gold values. Your code must produce the JSON file exactly as specified, with the correct keys and numeric values.
