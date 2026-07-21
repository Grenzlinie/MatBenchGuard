# Pressure-induced B1→B2 phase transition in uranium sulfide using TBIPM

## Problem background
Uranium sulfide (US) crystallizes in the rock-salt (B1) structure at ambient conditions and is expected to undergo a pressure-induced structural phase transition to the CsCl-type (B2) structure at high pressure. Computing the transition pressure and the associated volume collapse is important for understanding the high-pressure behavior of actinide monochalcogenides. In this task you will reproduce the B1→B2 phase transition pressure and volume collapse at 0 K using a three-body interaction potential model (TBIPM).

## Approach
The TBIPM expresses the total cohesive energy of the crystal as a sum of long-range Coulomb interactions, three-body interactions, a Hafemeister–Flygare type short‑range overlap repulsion extended to second‑neighbour ions, and van der Waals contributions. With the supplied model parameters (ionic radii r_i=0.80 Å, r_j=1.24 Å, near‑neighbour distance r_o=5.488 Å, bulk modulus B_T=105 GPa, potential parameters b=2.5066×10⁻¹² erg, p=0.365 Å, f(r)=−0.0169), you will compute the equilibrium cohesive energies of the B1 (NaCl‑type) and B2 (CsCl‑type) phases by minimizing the static lattice energy with respect to structural parameters. Using the unit‑cell volumes V_B1 = 2.00 r³ and V_B2 = 1.54 r³ with r = 5.488 Å, construct the Gibbs free energy (at 0 K it equals enthalpy) as a function of pressure, G(P)=U+PV. The phase transition pressure P_t is the pressure where ΔG(P)=G_B1(P)−G_B2(P) crosses zero. At that pressure, a third‑order Birch–Murnaghan equation of state with the given bulk modulus is used to obtain the volumes of each phase, from which the volume collapse is computed as [V_B1(P_t)−V_B2(P_t)]/V_B1(0)×100 %.

## Reproduction target
Compute the B1→B2 structural phase transition pressure (in GPa) and the associated volume collapse (in percent) for US at 0 K using the TBIPM with the supplied parameters. Output these two numbers to the file `/app/outputs/final_results.json` with fields `transition_pressure_gpa` and `volume_collapse_percent`.

## Assets
No external datasets or pre‑trained models are needed. All required physical constants and model parameters are provided in the approach and workflow steps above. The TBIPM functional form must be implemented from its description; standard Python scientific packages (e.g., numpy, scipy) are sufficient.

## Workflow steps

### Step 1: Compute cohesive energies of B1 and B2 phases using TBIPM
- Role: process
- Action: Implement the three-body interaction potential model (TBIPM) for US with the provided parameters. Compute the static lattice energy for the NaCl-type (B1) and CsCl-type (B2) structures, minimizing with respect to structural parameters to obtain equilibrium cohesive energies U_B1 and U_B2.
- Evidence: `/app/outputs/cohesive_energies.txt`

### Step 2: Compute transition pressure and volume collapse
- Role: scored (load-bearing)
- Action: Using the equilibrium cohesive energies, construct enthalpy functions G_B1(P) = U_B1 + P V_B1 and G_B2(P) = U_B2 + P V_B2, with unit-cell volumes V_B1=2.00 r^3, V_B2=1.54 r^3 (r = 5.488 Å). Find the pressure P_t where ΔG(P) = 0. Then, using a third-order Birch–Murnaghan equation of state with bulk modulus B_T, compute the volume of each phase at P_t and calculate the volume collapse as [V_B1(P_t)−V_B2(P_t)]/V_B1(0)×100. Write the transition pressure (GPa) and volume collapse (percentage) to a JSON file.
- Output file: `/app/outputs/final_results.json`
- Format: json
- Contract: {"transition_pressure_gpa": "float (GPa)", "volume_collapse_percent": "float (%)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_results.json
- path: `/app/outputs/final_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the computed B1→B2 transition pressure and associated volume collapse for US at 0 K.
- schema:
  - `type`: object
  - `required`:
    - `transition_pressure_gpa`: float (GPa)
    - `volume_collapse_percent`: float (%)

Notes: The checker compares transition_pressure_gpa and volume_collapse_percent against hidden reference values. It applies tolerances of ±5 GPa for pressure and ±0.5 percentage points for volume collapse.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "transition_pressure_gpa": "float (GPa)",
          "volume_collapse_percent": "float (%)"
        }
      },
      "description": "Scored artifact containing the computed B1→B2 transition pressure and associated volume collapse for US at 0 K."
    }
  ],
  "notes": "The checker compares transition_pressure_gpa and volume_collapse_percent against hidden reference values. It applies tolerances of ±5 GPa for pressure and ±0.5 percentage points for volume collapse."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/final_results.json` and compare the computed transition pressure and volume collapse to the expected results. You must implement the full TBIPM and the procedure described in the workflow steps; simply writing down the correct numbers without executing the computational pipeline will receive low scores because the verifier may also perform sanity checks on intermediate evidence. Each scored stage contributes to the overall reward.
