# Point defect formation and effective formation volumes in B2-FeAl

## Problem background
Intermetallic compounds like B2-FeAl are candidates for high-temperature structural applications. Understanding point defects is crucial because they control high-temperature creep and diffusion. Pressure-dependent experiments offer insights into defect formation volumes, but in ordered compounds multiple defect types must appear simultaneously to maintain composition. As a result, the effective formation volume measured in a pressure experiment is not simply the local relaxation volume of a single defect—it depends on the concentrations and relaxation volumes of all relevant defects. This task addresses the computation of local relaxation volumes and effective formation volumes for the four key point defects (Fe vacancy, Al vacancy, Fe antisite, Al antisite) in B2-FeAl at stoichiometric and off-stoichiometric compositions.

## Approach
The reproduction uses a two-stage computational pipeline.

**Stage 1 – DFT supercell calculations.** A 32‑atom supercell of B2-FeAl serves as the reference. Four defective supercells are constructed by introducing a single Fe vacancy, Al vacancy, Fe antisite, or Al antisite. For each supercell, DFT calculations are performed at several fixed volumes with full atomic relaxation. Total energies as a function of volume are fitted to a universal binding curve to extract the equilibrium volume and total energy at mechanical equilibrium. From these, the defect formation energy ε_i and the local relaxation volume ΔV_i are obtained for each defect type.

**Stage 2 – Grandcanonical analysis.** Using the ε_i and ΔV_i values (formation entropies are set to zero), the generalized grandcanonical equations are solved self‑consistently for the four defect types to determine the chemical potentials and equilibrium defect concentrations at T = 1300 K for both stoichiometric FeAl and Fe0.52Al0.48. Finally, the effective formation volumes Ω̄_i are obtained by numerically evaluating the pressure derivative Ω̄_i = –k_B T ∂ ln c_i / ∂ p. All quantities are expressed in units of the mean atomic volume Ω₀.

The choice of the DFT code (e.g., Quantum ESPRESSO, ABINIT, CP2K), pseudopotentials, k‑point mesh, energy cut‑offs, and volume scan range is left to you, as long as the resulting ΔV_i and Ω̄_i are physically consistent with a 32‑atom supercell approach. The critical output is the final JSON file.

## Reproduction target
Produce the file `/app/outputs/defect_properties.json` containing the local relaxation volumes ΔV_i and the effective formation volumes Ω̄_i for Fe vacancy, Al vacancy, Fe antisite, and Al antisite at both stoichiometric FeAl and Fe0.52Al0.48 at T = 1300 K. All values must be given in units of the mean atomic volume Ω₀ and structured according to the output contract below.

## Assets

- B2-FeAl crystal structure (CsCl prototype, Pm-3m, lattice parameter ~2.89 Å, 2 atoms per conventional cell)
- Pseudopotentials for Fe and Al (SSSP PBEsol efficiency library or equivalent): https://www.materialscloud.org/discover/sssp/table/efficiency
- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, ABINIT): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: DFT supercell calculation of defect formation energies and local relaxation volumes
- Role: process
- Action: For perfect B2-FeAl and four defective 32‑atom supercells (Fe vacancy, Al vacancy, Fe antisite, Al antisite): perform DFT calculations at several volumes. For each configuration, relax atomic positions at fixed volume, then determine the equilibrium volume and total energy by fitting a universal binding curve to the volume‑dependent total energies. Compute defect formation energy ε_i = E_defect − E_perfect at mechanical equilibrium, and local relaxation volume ΔV_i = V_defect_eq − V_perfect_eq.
- Evidence: `/app/outputs/energy_volume_data.json`

### Step 2: Grandcanonical calculation of effective formation volumes
- Role: scored (load-bearing)
- Action: Using ε_i and ΔV_i from the DFT step, set formation entropies to zero. Solve the generalized grandcanonical equations (self‑consistent determination of chemical potentials and equilibrium defect concentrations) for the four defect types at stoichiometric FeAl and at Fe0.52Al0.48, T = 1300 K. Numerically compute effective formation volumes Ω̄_i = −k_B T ∂ ln c_i / ∂ p. Report all ΔV_i and Ω̄_i in units of the mean atomic volume Ω₀.
- Output file: `/app/outputs/defect_properties.json`
- Format: json
- Contract: {"stoichiometric": {"Fe_vacancy": {"Delta_V": float, "effective_Omega": float}, "Al_vacancy": {"Delta_V": float, "effective_Omega": float}, "Fe_antisite": {"Delta_V": float, "effective_Omega": float}, "Al_antisite": {"Delta_V": float, "effective_Omega": float}}, "off_stoichiometric": {"Fe_vacancy": {"Delta_V": float, "effective_Omega": float}, "Al_vacancy": {"Delta_V": float, "effective_Omega": float}, "Fe_antisite": {"Delta_V": float, "effective_Omega": float}, "Al_antisite": {"Delta_V": float, "effective_Omega": float}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_properties.json
- path: `/app/outputs/defect_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing local relaxation volumes ΔV and effective formation volumes Ω̄ for all four defect types at stoichiometric and off‑stoichiometric FeAl at 1300 K, expressed in units of the mean atomic volume Ω₀.
- schema:
  - `type`: object
  - `required`: `stoichiometric`, `off_stoichiometric`
  - `properties`:
    - `stoichiometric`:
      - `type`: object
      - `properties`:
        - `Fe_vacancy`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number
        - `Al_vacancy`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number
        - `Fe_antisite`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number
        - `Al_antisite`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number
    - `off_stoichiometric`:
      - `type`: object
      - `properties`:
        - `Fe_vacancy`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number
        - `Al_vacancy`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number
        - `Fe_antisite`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number
        - `Al_antisite`:
          - `type`: object
          - `properties`:
            - `Delta_V`: number
            - `effective_Omega`: number

Notes: The DFT step (process) must produce energy‑volume data; the scored step loads that data and implements the grandcanonical equations. The agent chooses the DFT code, pseudopotentials, k‑mesh, volume scans, and convergence settings, as long as the final ΔV and Ω̄ values are numerically consistent with the paper within the (hidden) tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "stoichiometric",
          "off_stoichiometric"
        ],
        "properties": {
          "stoichiometric": {
            "type": "object",
            "properties": {
              "Fe_vacancy": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              },
              "Al_vacancy": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              },
              "Fe_antisite": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              },
              "Al_antisite": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              }
            }
          },
          "off_stoichiometric": {
            "type": "object",
            "properties": {
              "Fe_vacancy": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              },
              "Al_vacancy": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              },
              "Fe_antisite": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              },
              "Al_antisite": {
                "type": "object",
                "properties": {
                  "Delta_V": "number",
                  "effective_Omega": "number"
                }
              }
            }
          }
        }
      },
      "description": "JSON file containing local relaxation volumes ΔV and effective formation volumes Ω̄ for all four defect types at stoichiometric and off‑stoichiometric FeAl at 1300 K, expressed in units of the mean atomic volume Ω₀."
    }
  ],
  "notes": "The DFT step (process) must produce energy‑volume data; the scored step loads that data and implements the grandcanonical equations. The agent chooses the DFT code, pseudopotentials, k‑mesh, volume scans, and convergence settings, as long as the final ΔV and Ω̄ values are numerically consistent with the paper within the (hidden) tolerance."
}
```

## How you are scored
A hidden verifier compares the values you write in `defect_properties.json` to reference values derived from the original study (not visible to you). The verifier checks all 16 numbers — ΔV_i and Ω̄_i for the four defect types at two compositions — and computes a score based on accuracy, with built‑in tolerance to absorb legitimate differences arising from DFT implementation choices (pseudopotentials, code, convergence settings).

Additionally, the verifier enforces that the signs of the local relaxation volumes ΔV_i are physically correct for each defect: negative for Fe vacancy, Al vacancy, and Fe antisite; positive for Al antisite. An incorrect sign may result in a score of zero.

The process‑step evidence file `energy_volume_data.json` is not directly scored but must be generated to demonstrate that the DFT calculations were executed. Your score comes entirely from the correctness of the values reported in `defect_properties.json` according to the output contract.
