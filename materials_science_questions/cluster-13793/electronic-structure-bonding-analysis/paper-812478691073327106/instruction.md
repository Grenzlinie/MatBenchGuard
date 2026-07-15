# Activation Free Energies for Bond Formation and Dissociation in Na-Ga and Ga Melts

## Problem background
The formation and dissociation of molecular bonds in molten environments influence the mechanisms of crystal growth, especially when additives or the solvent itself act as catalysts. In Na-flux gallium nitride (GaN) growth, carbon additives enhance growth, and for low-temperature graphene synthesis, molten gallium catalyses methane decomposition. Quantifying the activation free energies for bond formation and dissociation of N-N, C-C, and C-H bonds in sodium-gallium (Na-Ga) and pure gallium (Ga) melts is essential for understanding the catalytic role of gallium and for optimising growth processes. These energies are difficult to measure directly, so first-principles computation is a valuable tool.

## Approach
We use a first-principles molecular dynamics (FPMD) approach combined with the blue-moon ensemble method for rare events. In this method, a chosen interatomic distance (the reaction coordinate) is constrained to a series of values, and constrained MD simulations are performed at each distance. The mean force required to maintain the constraint is recorded as a function of distance. Integrating these mean forces yields the free energy profile along the chosen bond coordinate. From the profile, the activation free energy for bond dissociation (Ed) is the energy difference between a local maximum and the preceding local minimum, while the formation activation energy (Ef) is the barrier from the separated/free state (zero energy) to that local maximum. Atomistic models are built for: (i) a Na-Ga melt (Na:Ga ~4:1, ~54 atoms) with two nitrogen atoms for N-N bond breaking; (ii) a Na-Ga melt with two carbon atoms for C-C; (iii) a Na-Ga melt with a CH unit for C-H; and (iv) a pure Ga melt (~53 Ga atoms) with a methane molecule for C-H dissociation. All systems are modelled in periodic cubic cells at the appropriate temperature (1073 K for Na-Ga melts, 373 K for Ga melt) using density functional theory (DFT) with the PBE exchange-correlation functional and norm-conserving/ultrasoft pseudopotentials. Free energy profiles are then computed for each bond–melt combination, from which Ef and Ed are extracted.

## Reproduction target
Compute and report the activation free energies for formation (Ef) and dissociation (Ed) for the following four systems:
1. N–N bond in Na–Ga melt at 1073 K.
2. C–C bond in Na–Ga melt at 1073 K.
3. C–H bond (from a CH unit) in Na–Ga melt at 1073 K.
4. C–H bond (from CH₄) in a Ga melt at 373 K.
All energies must be reported in electronvolts (eV) as positive numbers. Write the results to a JSON file, activation_energies.json, following the exact schema given in the output contract.

## Assets

- DFT-MD software (Quantum ESPRESSO or CP2K): https://www.quantum-espresso.org/
- Pseudopotential library (SSSP): http://materialscloud.org/sssp/
- Ga melt density reference: 10.1007/BF00912547

## Workflow steps

### Step 1: Prepare simulation cells
- Role: process
- Action: Construct initial atomic coordinates for Na-Ga melt (Na:Ga ≈ 4:1, ~54 atoms) systems: with two N atoms (N-N bond study), two C atoms (C-C study), one CH unit (C-H study), and a Ga melt (~53 Ga atoms + CH4 molecule) system. Use cubic boxes with periodic boundary conditions. Cell sizes: ~12.6 Å for Na-Ga melt, ~10.1 Å for Ga melt at 373 K. Save coordinate files for all systems.
- Evidence: none

### Step 2: Constrained MD simulations
- Role: process
- Action: For each system (N-N, C-C, C-H in Na-Ga melt; C-H in Ga melt), run first-principles molecular dynamics in NVT ensemble with blue-moon method. Constrain the target interatomic distance at multiple values covering the reaction coordinate (e.g., 1.0–3.5 Å). Record mean constraint forces at each distance. Use PBE functional, appropriate pseudopotentials, single k-point, and reasonable cutoff. Run MD for sufficient time to obtain converged mean forces. (For C-H in Ga melt, temperature is 373 K; others at 1073 K.)
- Evidence: none

### Step 3: Extract activation free energies and write output
- Role: scored (load-bearing)
- Action: Integrate mean force vs distance data to obtain free energy profiles for each bond-melt system. Identify stable bond lengths, local maxima/minima, and extract formation activation energy (Ef) and dissociation activation energy (Ed) for: N-N in Na-Ga melt, C-C in Na-Ga melt, C-H (CH) in Na-Ga melt, and C-H (CH4) in Ga melt at 373 K. Compile results into activation_energies.json.
- Output file: `/app/outputs/activation_energies.json`
- Format: json
- Contract: JSON object with keys: "N-N_NaGa_Ef", "N-N_NaGa_Ed", "C-C_NaGa_Ef", "C-C_NaGa_Ed", "C-H_CH_NaGa_Ef", "C-H_CH_NaGa_Ed", "C-H_CH4_Ga_Ef", "C-H_CH4_Ga_Ed". All values are positive floats (eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.json
- path: `/app/outputs/activation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Activation free energies for bond formation (Ef) and dissociation (Ed) of N-N, C-C, C-H(CH) in Na-Ga melt and C-H(CH4) in Ga melt. The four dissociation energies (Ed) are scored; formation energies must be positive.
- schema:
  - `type`: object
  - `required`: `N-N_NaGa_Ef`, `N-N_NaGa_Ed`, `C-C_NaGa_Ef`, `C-C_NaGa_Ed`, `C-H_CH_NaGa_Ef`, `C-H_CH_NaGa_Ed`, `C-H_CH4_Ga_Ef`, `C-H_CH4_Ga_Ed`
  - `properties`:
    - `N-N_NaGa_Ef`:
      - `type`: number
    - `N-N_NaGa_Ed`:
      - `type`: number
    - `C-C_NaGa_Ef`:
      - `type`: number
    - `C-C_NaGa_Ed`:
      - `type`: number
    - `C-H_CH_NaGa_Ef`:
      - `type`: number
    - `C-H_CH_NaGa_Ed`:
      - `type`: number
    - `C-H_CH4_Ga_Ef`:
      - `type`: number
    - `C-H_CH4_Ga_Ed`:
      - `type`: number
  - `units`: eV

Notes: Scoring is based on the four dissociation activation energies (Ed) compared to reference values within an absolute tolerance. Formation energies (Ef) must be positive but are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "N-N_NaGa_Ef",
          "N-N_NaGa_Ed",
          "C-C_NaGa_Ef",
          "C-C_NaGa_Ed",
          "C-H_CH_NaGa_Ef",
          "C-H_CH_NaGa_Ed",
          "C-H_CH4_Ga_Ef",
          "C-H_CH4_Ga_Ed"
        ],
        "properties": {
          "N-N_NaGa_Ef": {
            "type": "number"
          },
          "N-N_NaGa_Ed": {
            "type": "number"
          },
          "C-C_NaGa_Ef": {
            "type": "number"
          },
          "C-C_NaGa_Ed": {
            "type": "number"
          },
          "C-H_CH_NaGa_Ef": {
            "type": "number"
          },
          "C-H_CH_NaGa_Ed": {
            "type": "number"
          },
          "C-H_CH4_Ga_Ef": {
            "type": "number"
          },
          "C-H_CH4_Ga_Ed": {
            "type": "number"
          }
        },
        "units": "eV"
      },
      "description": "Activation free energies for bond formation (Ef) and dissociation (Ed) of N-N, C-C, C-H(CH) in Na-Ga melt and C-H(CH4) in Ga melt. The four dissociation energies (Ed) are scored; formation energies must be positive."
    }
  ],
  "notes": "Scoring is based on the four dissociation activation energies (Ed) compared to reference values within an absolute tolerance. Formation energies (Ef) must be positive but are not scored."
}
```

## How you are scored
Your submitted activation_energies.json is read by a hidden verifier. The verifier compares each of the four dissociation activation energies (the Ed fields) to a hidden reference value, using a pre-defined absolute tolerance that accounts for typical differences between independent DFT implementations. Your reward is the fraction of the four Ed values that fall within the tolerance (a number between 0 and 1). The formation energies (Ef fields) are checked for positivity but are not directly scored. All required fields must be present; partial or missing fields result in a lower reward. Do not attempt to reverse-engineer the reference values or tolerance; concentrate on executing the described first-principles workflow accurately.
