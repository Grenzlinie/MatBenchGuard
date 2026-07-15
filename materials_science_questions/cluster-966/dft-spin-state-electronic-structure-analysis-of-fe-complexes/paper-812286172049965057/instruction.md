# Zeeman selection-rule calculation of resonance fluorescence polarization

## Problem background
The phenomenon of resonant fluorescence in atomic vapors can be affected by weak magnetic fields, leading to partial polarization of the emitted light. This task addresses the theoretical calculation of the polarization degree for two atomic species—sodium (Na D₂ line) and mercury (Hg resonance line)—when the vapor is excited by light polarized parallel to the magnetic field and the fluorescence is observed perpendicular to the field. Using the Zeeman splitting scheme and electric-dipole selection rules, one can enumerate the allowed absorption and emission transitions and, from them, deduce the expected polarization. The goal is to compute the polarization degree for both systems, thereby demonstrating the quantitative difference in their behavior without relying on experimental measurements.

## Approach
Use the known Zeeman sublevels of the relevant atomic states: for Na D₂ (transition 1S → 2p₁), the ground state splits into m = ±1/2, and the excited state 2p₁ into m = ±1/2, ±3/2; for Hg (1S → 2p₂), the ground state has m = 0 and the excited state 2p₂ splits into m = 0, ±1. Under excitation light with its electric vector parallel to the magnetic field H, only Δm = 0 absorption transitions are allowed. After absorption, the excited atoms return to the ground state via all Δm = 0, ±1 emission transitions, subject to the selection rules. For transverse observation (perpendicular to H), Δm = 0 emission is polarized parallel to H, while Δm = ±1 emission is polarized perpendicular to H. Assuming equal a priori weights for each possible emission path, compute the total intensities of the parallel and perpendicular components. The degree of polarization is defined as P = (I∥ − I⊥) / (I∥ + I⊥). Apply this procedure to both atomic lines, counting the transitions that arise from the sublevels populated under the given excitation conditions.

## Reproduction target
Compute, using the Zeeman selection rules and the equal-weight assumption, the polarization degrees for the Na D₂ line and the Hg resonance line under the specified excitation and observation geometry (E ∥ H, observation ⊥ H). Output a single JSON file containing the two numeric values: one for Na D₂ and one for Hg. The computation must be performed from first principles—no external data or fitted parameters—and the result written to the specified output file.

## Assets
No external assets are required. The entire computation is self-contained and based solely on the Zeeman sublevel structure and selection rules described in the approach section. No datasets, pre-trained models, or special tools are needed beyond standard numerical computing libraries.

## Workflow steps

### Step 1: Compute polarization degrees
- Role: scored (load-bearing)
- Action: Implement the Zeeman selection-rule calculation for the Na D₂ (1S→2p₁) and Hg (1S→2p₂) resonance lines under excitation light polarized parallel to the magnetic field (E ∥ H) and observation perpendicular to H. Enumerate Zeeman sublevels and allowed absorption/emission transitions, assign parallel/perpendicular polarization based on Δm, assume equal a priori weights for emission pathways, compute intensities I_parallel and I_perpendicular, and calculate the polarization degree P = (I_parallel - I_perpendicular) / (I_parallel + I_perpendicular). Write the two resulting polarization values to a JSON file.
- Output file: `/app/outputs/polarization_results.json`
- Format: json
- Contract: {"Na_D2_polarization": float, "Hg_resonance_polarization": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polarization_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polarization_results.json
- path: `/app/outputs/polarization_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Polarization degrees for Na D₂ and Hg resonance lines computed from Zeeman selection rules.
- schema:
  - `type`: object
  - `required`:
    - `Na_D2_polarization`: float
    - `Hg_resonance_polarization`: float

Notes: Both polarization degrees are derived from the Zeeman splitting of the relevant atomic levels and the electric-dipole selection rules (Δm = 0, ±1) under the specified experimental geometry. The Hg resonance line involves a single allowed transition and thus yields a different polarization than the Na D₂ line.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polarization_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Na_D2_polarization": "float",
          "Hg_resonance_polarization": "float"
        }
      },
      "description": "Polarization degrees for Na D₂ and Hg resonance lines computed from Zeeman selection rules."
    }
  ],
  "notes": "Both polarization degrees are derived from the Zeeman splitting of the relevant atomic levels and the electric-dipole selection rules (Δm = 0, ±1) under the specified experimental geometry. The Hg resonance line involves a single allowed transition and thus yields a different polarization than the Na D₂ line."
}
```

## How you are scored
A hidden verifier will independently recompute the two polarization values using the same physical model. The verifier reads your submitted JSON file, extracts the Na_D2_polarization and Hg_resonance_polarization entries, and compares them against the checker's own computed values. Credit is awarded based on the closeness of your computed results to those expected values; the verifier does not rely on any thresholds reported here. Simply reporting a number without performing the correct computation will not receive full credit, because the verifier's criteria are based on the underlying physics, not on matching a publicly known reference. Your implementation must faithfully enumerate the allowed transitions and apply the polarization formula.
