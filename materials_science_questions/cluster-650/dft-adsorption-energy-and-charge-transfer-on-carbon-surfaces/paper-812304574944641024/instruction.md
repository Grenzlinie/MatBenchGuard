# Hydrocarbon Adsorption Energy Calculation on MgO (100) Surface

## Problem background
Predicting adsorption equilibria from the physical properties of adsorbent and adsorbate is a fundamental challenge in surface science. For non‑polar molecules on ionic surfaces, the adsorption energy arises from dispersive, inductive, and repulsive interactions that can be modelled with a force‑field approach. This task addresses the calculation of standard adsorption energies for hydrocarbons on the (100) face of magnesia (MgO) using such a model. The objective is to compute adsorption energies from first principles and to analyse the relative contributions of the different energy terms, providing a computational test of the theory against experimental heats of adsorption.

## Approach
The calculation follows an additive scheme in which each adsorbate molecule is divided into energy centres (segments such as CH₃, CH₂, or aromatic rings). For each centre, the total potential energy at a distance z from the surface is the sum of three contributions: (i) a dispersive attraction expressed as a sum over inverse powers of distance (inverse sixth, eighth, and tenth powers) with constants derived from polarizabilities and diamagnetic susceptibilities; (ii) an inductive attraction from the mean square electrostatic field of the ionic lattice; and (iii) an exponential repulsion term. The geometric lattice sums are evaluated over a finite set of surface ions and corrected for the bulk by integration, then fitted to simple functional forms of z. The repulsion constant is determined from the equilibrium condition that the first derivative of the total potential with respect to z vanishes at the equilibrium distance. Per‑segment energies are then assembled into whole‑molecule adsorption energies at zero coverage. A lateral interaction correction is applied to convert them to standard coverage θ = 0.5. The contributions of the individual energy terms are obtained by decomposing the total attractive energy.

## Reproduction target
Produce two JSON artifacts in `/app/outputs`:

1. `step_07_adsorption_energies.json` — a JSON object containing the standard adsorption energies (in kcal/mol) at coverage θ = 0.5 on the MgO (100) face for **n‑hexane**, **n‑heptane**, **n‑octane**, **benzene**, and **toluene**.

2. `step_08_energy_contributions.json` — a JSON object containing the overall integer percentage contributions (relative to the total attractive forces) of the **first dispersion term**, **second dispersion term**, **third dispersion term**, **induction term**, and **repulsion term**, as described in the output contract.

## Assets

- Python 3 scientific stack: numpy, scipy

## Workflow steps

### Step 1: Lattice Sums for MgO (100) Surface
- Role: process
- Action: Construct the MgO (100) surface lattice (lattice constant d=2.1 Å). Compute lattice sums for dispersion terms (f_D1, f_D2, f_D3) and repulsion term (f_R') over a range of distances z above the plane. Fit the computed sums to power-law forms for dispersion and exponential form for repulsion.
- Evidence: none

### Step 2: Dispersion Constants for Adsorbate Segments
- Role: process
- Action: Using the polarizabilities and susceptibilities of Mg²⁺ and O²⁻ ions (α_Mg=0.11e-24, α_O=1.69e-24 cc; χ_Mg=-6.7e-30, χ_O=-10e-30 cc) and of adsorbate segments (CH₃, CH₂, benzene, toluene), calculate dispersion constants C_i1, C_i2, C_i3 via Kirkwood-type formulas.
- Evidence: none

### Step 3: Induction Potential Parameters
- Role: process
- Action: Evaluate the electrostatic induction term for the (100) face of MgO using the Lennard-Jones–Dent expression, deriving the exponential form Φ_iI = -A_i e^{-a z} with A_i and a determined from lattice constant, ionic charges, and segment polarizabilities.
- Evidence: none

### Step 4: Repulsion Constant from Equilibrium
- Role: process
- Action: For each segment type, use the equilibrium condition dΦ/dz=0 at the equilibrium distance z0 (sum of van der Waals radius and d/2=1.05 Å) to solve for the repulsion constant B', with exponential repulsion constant ρ=0.31 Å, employing the dispersion and induction terms from previous steps.
- Evidence: none

### Step 5: Per-Segment Energies and Energy Term Fractions
- Role: process
- Action: Evaluate the total adsorption potential at z0 for each segment type and ion (Mg²⁺, O²⁻), recording the separate contributions: first (C6), second (C8), third (C10) dispersion terms, induction energy, and exponential repulsion energy. Compute each term's percentage of the total attractive energy (dispersion + induction).
- Evidence: none

### Step 6: Whole-Molecule Adsorption Energies at θ=0.5
- Role: scored (load-bearing)
- Action: Apply the additive segment scheme to sum per-segment energies into total zero-coverage energies for n-hexane, n-heptane, n-octane, benzene, and toluene. Correct to standard coverage θ=0.5 using the lateral interaction correction Φ^0 = Φ_0 - N C r_{θ=0.5}^{-6}. Output the five standard adsorption energies in kcal/mol as a JSON object.
- Output file: `/app/outputs/step_07_adsorption_energies.json`
- Format: json
- Contract: JSON object with keys "n-hexane", "n-heptane", "n-octane", "benzene", "toluene", each a numeric value in kcal/mol.
- Scoring: scored by hidden verifier

### Step 7: Energy Term Contributions on MgO
- Role: scored
- Action: From the per-segment energy decomposition obtained earlier, compute the overall percentages (to nearest integer) of the first, second, third dispersion terms, induction term, and repulsion term relative to the total attractive energy. Output the five percentages as a JSON object.
- Output file: `/app/outputs/step_08_energy_contributions.json`
- Format: json
- Contract: JSON object with keys "C6_pct", "C8_pct", "C10_pct", "induction_pct", "repulsion_pct", each an integer (percent).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_07_adsorption_energies.json`
- `/app/outputs/step_08_energy_contributions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_07_adsorption_energies.json
- path: `/app/outputs/step_07_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Standard adsorption energies at half coverage on MgO (100).
- schema:
  - `type`: object
  - `required`:
    - `n-hexane`: number (kcal/mol)
    - `n-heptane`: number (kcal/mol)
    - `n-octane`: number (kcal/mol)
    - `benzene`: number (kcal/mol)
    - `toluene`: number (kcal/mol)

### step_08_energy_contributions.json
- path: `/app/outputs/step_08_energy_contributions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Percentage contributions of energy terms to total attractive forces on MgO.
- schema:
  - `type`: object
  - `required`:
    - `C6_pct`: integer (percent)
    - `C8_pct`: integer (percent)
    - `C10_pct`: integer (percent)
    - `induction_pct`: integer (percent)
    - `repulsion_pct`: integer (percent)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_07_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "n-hexane": "number (kcal/mol)",
          "n-heptane": "number (kcal/mol)",
          "n-octane": "number (kcal/mol)",
          "benzene": "number (kcal/mol)",
          "toluene": "number (kcal/mol)"
        }
      },
      "description": "Standard adsorption energies at half coverage on MgO (100)."
    },
    {
      "file": "step_08_energy_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C6_pct": "integer (percent)",
          "C8_pct": "integer (percent)",
          "C10_pct": "integer (percent)",
          "induction_pct": "integer (percent)",
          "repulsion_pct": "integer (percent)"
        }
      },
      "description": "Percentage contributions of energy terms to total attractive forces on MgO."
    }
  ],
  "notes": ""
}
```

## How you are scored
After the agent submits the two output files, a hidden verifier compares the reported energies against reference values derived from the published theoretical model and checks that the reported percentages fall within the expected ranges. The final reward (a float between 0 and 1) is a weighted combination of the scores for the two artifacts: the adsorption energies contribute the majority of the weight, while the energy‑term percentages contribute the remainder. The scoring rewards reproduction fidelity: values closer to the hidden references yield higher scores; large deviations reduce the score proportionally. The agent must execute the full computational pipeline accurately; simply guessing or reporting approximate values will not achieve a high score.
