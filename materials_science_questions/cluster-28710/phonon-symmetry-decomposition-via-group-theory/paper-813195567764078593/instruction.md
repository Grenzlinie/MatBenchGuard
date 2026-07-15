# Composition‑dependent A1‑TO phonon frequencies and lattice parameters of LiNb1−xTaxO3 mixed crystals

## Problem background
Lithium niobate (LiNbO₃) and lithium tantalate (LiTaO₃) are ferroelectric materials widely used in electro‑optic and acoustic devices. Their mixed crystals, LiNb₁₋ₓTaₓO₃, offer continuously tunable properties through the composition, but direct experimental data on the composition‑dependent structural parameters and vibrational frequencies are limited. First‑principles density functional theory can predict these quantities, providing a theoretical basis for non‑destructive composition determination via Raman spectroscopy. This task computes the lattice parameters and the zone‑center A₁‑TO phonon frequencies as a function of the Nb/Ta ratio.

## Approach
Total energy calculations are performed within the PW91 formulation of the generalized gradient approximation, using projector augmented wave (PAW) pseudopotentials. The rhombohedral R3c structure of LiNb₁₋ₓTaₓO₃ is modeled with 20‑atom supercells for five compositions (x = 0.00, 0.25, 0.50, 0.75, 1.00). All inequivalent Nb/Ta cation arrangements are enumerated for each mixed composition. For each configuration, the total energy is computed at several volumes, ionic positions are relaxed, and the energy‑volume data are fitted to the Murnaghan equation of state to extract equilibrium lattice parameters a and c. At the equilibrium geometries, the Γ‑point phonon frequencies are obtained with the frozen‑phonon (finite‑displacement) method, and the four A₁‑TO modes are identified by symmetry analysis of the eigenvectors. The final composition‑dependent values are obtained by averaging over all inequivalent cation arrangements. This workflow replaces the proprietary code used in the original study with the open‑source Quantum ESPRESSO package.

## Reproduction target
Produce the average rhombohedral lattice parameters a (Å), c (Å), unit‑cell volume (Å³), and the four A₁‑TO phonon frequencies TO₁, TO₂, TO₃, TO₄ (cm⁻¹) for the five compositions LiNb₁₋ₓTaₓO₃ with x = 0.00, 0.25, 0.50, 0.75, 1.00, using DFT with the PW91 functional and the frozen‑phonon approach. The reported values must represent the average over all inequivalent Nb/Ta cation configurations for each stoichiometry.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials (PW91) for Li, O, Nb, Ta: https://www.quantum-espresso.org/pseudopotentials/
- Crystal structures of LiNbO3 and LiTaO3 (R3c)

## Workflow steps

### Step 1: Build supercells for mixed crystal compositions
- Role: process
- Action: Construct rhombohedral 20‑atom supercells (2×1×1 repetition of the primitive R3c cell) for x = 0.00, 0.25, 0.50, 0.75, 1.00 and enumerate all inequivalent Nb/Ta cation arrangements. Use published crystallographic data for LiNbO₃ and LiTaO₃ as starting point.
- Evidence: `/app/outputs/configurations.txt`

### Step 2: DFT relaxation and Murnaghan equation‑of‑state fitting
- Role: process
- Action: For each supercell configuration, perform DFT total energy calculations at several volumes using PW91 GGA and PAW pseudopotentials. Relax ionic positions until residual forces drop below convergence threshold. Fit the total energy vs. volume data to the Murnaghan equation of state to obtain equilibrium lattice parameters a, c, and unit cell volume for each configuration.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 3: Frozen‑phonon calculation of Γ‑TO frequencies
- Role: process
- Action: At each equilibrium geometry, compute phonon frequencies at the Γ point using the frozen‑phonon (finite‑displacement) method. Identify the A1‑TO modes (TO1–TO4) by eigenvector analysis and symmetry classification.
- Evidence: `/app/outputs/phonon_log.txt`

### Step 4: Average over configurations and output final results
- Role: scored (load-bearing)
- Action: For each composition x, average the structural parameters (a, c, volume) and the four A1‑TO phonon frequencies (TO1, TO2, TO3, TO4) over all inequivalent cation configurations. Write the composition‑dependent averaged quantities to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of objects with keys: "x" (float, Nb fraction), "a" (float), "c" (float), "volume" (float), "TO1" (float), "TO2" (float), "TO3" (float), "TO4" (float). Example: {"x":0.0,"a":5.147,"c":13.72,"volume":312.5,"TO1":200,"TO2":242,"TO3":348,"TO4":577}
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
- description: Averaged lattice parameters (a, c in Å, volume in Å³) and Γ‑TO phonon frequencies (TO1–TO4 in cm⁻¹) for LiNb1−xTaxO3 at x = 0.00, 0.25, 0.50, 0.75, 1.00. Each entry corresponds to one composition.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `x`, `a`, `c`, `volume`, `TO1`, `TO2`, `TO3`, `TO4`
    - `properties`:
      - `x`:
        - `type`: number
      - `a`:
        - `type`: number
      - `c`:
        - `type`: number
      - `volume`:
        - `type`: number
      - `TO1`:
        - `type`: number
      - `TO2`:
        - `type`: number
      - `TO3`:
        - `type`: number
      - `TO4`:
        - `type`: number

Notes: Only the final averaged results are scored; the process steps produce evidence logs for auditing but are not directly rewarded.

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
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "x",
            "a",
            "c",
            "volume",
            "TO1",
            "TO2",
            "TO3",
            "TO4"
          ],
          "properties": {
            "x": {
              "type": "number"
            },
            "a": {
              "type": "number"
            },
            "c": {
              "type": "number"
            },
            "volume": {
              "type": "number"
            },
            "TO1": {
              "type": "number"
            },
            "TO2": {
              "type": "number"
            },
            "TO3": {
              "type": "number"
            },
            "TO4": {
              "type": "number"
            }
          }
        }
      },
      "description": "Averaged lattice parameters (a, c in Å, volume in Å³) and Γ‑TO phonon frequencies (TO1–TO4 in cm⁻¹) for LiNb1−xTaxO3 at x = 0.00, 0.25, 0.50, 0.75, 1.00. Each entry corresponds to one composition."
    }
  ],
  "notes": "Only the final averaged results are scored; the process steps produce evidence logs for auditing but are not directly rewarded."
}
```

## How you are scored
A hidden verifier evaluates each built artifact. The scored target is the final results.json: its lattice parameters and phonon frequencies are compared against independently determined reference values, and structural trends (monotonic changes with composition) are verified. The reward is a weighted combination of the agreement scores; simply reporting a known number without genuine computation yields a low score. All intermediate steps produce evidence logs that are monitored for consistency but do not contribute directly to the reward.
