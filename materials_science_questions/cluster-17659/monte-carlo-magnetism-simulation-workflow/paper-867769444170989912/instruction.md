# Metastable Bulk Glass Para-Hydrogen Superfluidity from Path Integral Monte Carlo

## Problem background
Molecular para‑hydrogen (p‑H₂) is a spinless boson and is predicted to become superfluid at low temperature, but it crystallizes at 13.8 K before any superfluid transition can occur. It has been proposed that a metastable non‑crystalline (glass/liquid‑like) phase of bulk p‑H₂ might exhibit superfluidity if crystallization is frustrated. This task investigates that possibility by computing via Path Integral Monte Carlo the superfluid and condensate properties of an amorphous p‑H₂ system at a temperature of 1 K and number density ρ = 0.0234 Å⁻³.

## Approach
The approach uses Path Integral Monte Carlo (PIMC) with a specially designed two‑stage equilibration protocol to prepare a metastable amorphous configuration. First, a fictitious system of particles having the mass of p‑H₂ but interacting via the shallower Aziz ⁴He–⁴He pair potential is equilibrated to frustrate crystallization; then the true Silvera–Goldman p‑H₂ potential is switched on and the system is re‑equilibrated using collective centre‑of‑mass moves of the polymers. Bosonic permutation sampling is performed with the Worm Algorithm and the thermal density matrix is represented with a high‑order Chin action. After equilibration at the target temperature, the one‑body density matrix and the winding number are computed to extract the condensate fraction n₀ and the superfluid fraction ρₛ/ρ.

## Reproduction target
Implement the two‑stage PIMC equilibration protocol described in the Approach and, after equilibration at T = 1 K and number density ρ = 0.0234 Å⁻³, compute the superfluid fraction ρₛ/ρ (from the winding number estimator) and the condensate fraction n₀ (from the plateau of the one‑body density matrix at large separation). Write the results as a JSON object with keys 'superfluid_fraction' and 'condensate_fraction' to /app/outputs/superfluid_results.json.

## Assets

- Silvera‑Goldman p‑H₂ pair potential: 10.1063/1.436229
- Aziz He–He pair potential: 10.1080/00268978700101491

## Workflow steps

### Step 1: PIMC simulation and superfluid measurement
- Role: scored (load-bearing)
- Action: Implement and execute a Path Integral Monte Carlo simulation for N=130 p‑H₂ molecules in a non‑commensurate cubic simulation box at number density ρ=0.0234 Å⁻³. Use the Silvera‑Goldman pair potential for the physical interaction. Follow a two‑stage equilibration protocol: (i) equilibrate a fictitious system of particles with the mass of p‑H₂ but interacting via the Aziz ⁴He–⁴He pair potential to frustrate crystallization, (ii) switch to the Silvera‑Goldman potential and re‑equilibrate using collective centre‑of‑mass moves of the polymers. Employ a high‑order Chin action and the Worm Algorithm for bosonic permutation sampling. After equilibration at T=1 K, compute the one‑body density matrix to extract the condensate fraction n₀ from its plateau at large r, and estimate the superfluid fraction ρ_s/ρ from the winding number estimator. Write the results to /app/outputs/superfluid_results.json.
- Output file: `/app/outputs/superfluid_results.json`
- Format: json
- Contract: JSON object with keys 'superfluid_fraction' (float, unitless) and 'condensate_fraction' (float, unitless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/superfluid_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### superfluid_results.json
- path: `/app/outputs/superfluid_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Superfluid fraction and condensate fraction of the metastable bulk glass p‑H₂ system at T=1 K.
- schema:
  - `type`: object
  - `required`:
    - `superfluid_fraction`: float
    - `condensate_fraction`: float

Notes: The two fractions are compared to hidden gold values derived from the paper within tolerances that account for implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "superfluid_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "superfluid_fraction": "float",
          "condensate_fraction": "float"
        }
      },
      "description": "Superfluid fraction and condensate fraction of the metastable bulk glass p‑H₂ system at T=1 K."
    }
  ],
  "notes": "The two fractions are compared to hidden gold values derived from the paper within tolerances that account for implementation differences."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that reads `/app/outputs/superfluid_results.json` and compares the reported 'superfluid_fraction' and 'condensate_fraction' to hidden reference values within tolerances that account for legitimate implementation differences. Both values must be within their respective tolerance for full credit. The reward is a single float between 0 and 1.
