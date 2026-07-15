# DFT Stabilization Energy Calculation for AFePO4NO3 (A = Li, Na, K, NH4)

## Problem background
The development of new cathode materials for alkali-ion batteries relies heavily on computational screening to identify stable, high-capacity phases. Mixed polyanionic compounds — where two different oxyanions coexist in the same crystal lattice — are of particular interest because they offer structural flexibility and can tune the insertion voltage. This task focuses on a class of phosphatonitrates with the general formula AFePO4NO3 (A = Li, Na, K, NH4), which are derived from the mineral bonshtedtite (Na3FePO4CO3) by replacing the carbonate group with nitrate and adjusting the monovalent cation. Density functional theory (DFT) can predict whether these hypothetical phases are thermodynamically stable relative to the simple reactants ANO3 and FePO4, and can also compute the fully relaxed crystal structures. Your goal is to reproduce those predicted stabilization energies and the corresponding lattice parameters.

## Approach
The approach uses first-principles plane-wave DFT as implemented in Quantum ESPRESSO. The computational strategy is to start from the known bonshtedtite structure, substitute the CO3 group with NO3 and replace the monovalent cation to generate the four AFePO4NO3 candidate structures. Reference phases ANO3 (LiNO3, NaNO3, KNO3, NH4NO3) and FePO4 are also prepared. All systems are treated within the generalized gradient approximation (PBE) and with spin-polarized calculations that impose an antiferromagnetic ordering on the iron magnetic moments. Variable-cell geometry optimizations are performed for each compound. The total electronic energy of each fully relaxed structure is collected. Stabilization energy ΔE_s is then evaluated from the reaction AFePO4NO3 → ANO3 + FePO4, i.e., ΔE_s = E(AFePO4NO3) – E(ANO3) – E(FePO4), converted to kJ/mol. In addition, the final lattice parameters (a, b, c, α, β, γ, and volume) are extracted from the relaxed unit cells. The comparison being made is the relative stability of the four phosphatonitrates against their constituent reactants, and the structural details of the lowest-energy configurations.

## Reproduction target
Your task is to compute, for each of the four AFePO4NO3 compositions (A = Li, Na, K, NH4):
- the stabilization energy ΔE_s (in kJ/mol) defined by the reaction ANO3 + FePO4 → AFePO4NO3, and
- the relaxed lattice parameters (a, b, c, α, β, γ, and unit-cell volume) of the product phase.
To make the result verifiable, you must report not only the final ΔE_s values but also the raw total energies of every compound involved (the four AFePO4NO3 products plus the four ANO3 references and FePO4) as well as the structural parameters. All these quantities must be assembled in a single JSON file. The hidden checker will recompute ΔE_s from the total energies you provide and compare both the recomputed stabilization energies and the reported lattice parameters to a set of reference values derived from the original study. The overall score is a weighted combination of how well your computed ΔE_s values and lattice parameters match those references.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bonshtedtite structure (Na3FePO4CO3): ICSD #77053
- Reference structures of ANO3 and FePO4 (must use the following exact polymorphs and unit cells as used in the original DFT study):
  - LiNO3: trigonal (R-3c), a = 5.97 Å, c = 9.38 Å
  - NaNO3: trigonal (R-3c), a = 5.07 Å, c = 16.82 Å
  - KNO3: orthorhombic (Pnma), a = 5.42 Å, b = 9.19 Å, c = 6.45 Å
  - NH4NO3: orthorhombic (Pnma), a = 7.66 Å, b = 5.75 Å, c = 5.75 Å
  - FePO4: quartz-type trigonal (P3121), a = 5.033 Å, c = 11.247 Å
  (Obtain CIF files from ICSD or from the literature; the checker expects these specific structures.)

## Workflow steps

### Step 1: Prepare initial crystal structures
- Role: process
- Action: Generate starting structures for AFePO4NO3 (A = Li, Na, K, NH4) by modifying the bonshtedtite structure (Na3FePO4CO3): replace the CO3 group with NO3 and substitute the monovalent cation site. Prepare the reference phases ANO3 (Li, Na, K, NH4) and FePO4 using the exact polymorphs and unit-cell parameters listed in the Assets section; set up antiferromagnetic Fe ordering where applicable.
- Evidence: `/app/outputs/prepared_structures.tar.gz`

### Step 2: Run DFT geometry optimizations and total-energy calculations
- Role: process
- Action: Using Quantum Espresso (pw.x) with PBE exchange-correlation, UltraSoft pseudopotentials (non-linear core corrected), spin-polarized calculation with antiferromagnetic ordering for Fe, and variable-cell BFGS relaxation without symmetry constraints. Fixed parameters: wavefunction cutoff 544 eV, charge density cutoff 5.4 keV, Monkhorst-Pack k-point grid with a density of 0.216 Å⁻¹. Perform separate relaxations for the four AFePO4NO3 products, the four ANO3 references, and FePO4. Record the converged total energy and fully relaxed lattice parameters for each.
- Evidence: `/app/outputs/dft_output_logs.tar.gz`

### Step 3: Aggregate DFT results into dft_results.json
- Role: scored (load-bearing)
- Action: Extract converged total energies (eV) and relaxed lattice parameters (a,b,c,alpha,beta,gamma, V, crystal system) from the DFT output files. Compute ΔE_s (kJ/mol) for each A using the formula ΔE_s = [E(AFePO4NO3) - E(ANO3) - E(FePO4)] × 96.485. Assemble all values into /app/outputs/dft_results.json following the output contract schema.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: JSON object with top-level keys "references" (object mapping each cation symbol and "FePO4" to {"total_energy_eV": float}) and "compounds" (array of objects, each with keys: A (string), total_energy_eV (float), delta_E_kJmol (float), crystal_system (string), a (float, Å), b (float, Å), c (float, Å), alpha (float, °), beta (float, °), gamma (float, °), V (float, Å³)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains the total energies of all computed phases (AFePO4NO3, ANO3, FePO4) and the relaxed lattice parameters. The checker will recompute the stabilization energy ΔE_s for each A from the total energies using the reaction stoichiometry and compare the recomputed values and lattice parameters to the paper's reference.
- schema:
  - `type`: object
  - `required`: `references`, `compounds`
  - `properties`:
    - `references`:
      - `type`: object
      - `additionalProperties`:
        - `type`: object
        - `required`: `total_energy_eV`
        - `properties`:
          - `total_energy_eV`:
            - `type`: number
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `A`, `total_energy_eV`, `delta_E_kJmol`, `crystal_system`, `a`, `b`, `c`, `alpha`, `beta`, `gamma`, `V`
        - `properties`:
          - `A`:
            - `type`: string
          - `total_energy_eV`:
            - `type`: number
          - `delta_E_kJmol`:
            - `type`: number
          - `crystal_system`:
            - `type`: string
          - `a`:
            - `type`: number
          - `b`:
            - `type`: number
          - `c`:
            - `type`: number
          - `alpha`:
            - `type`: number
          - `beta`:
            - `type`: number
          - `gamma`:
            - `type`: number
          - `V`:
            - `type`: number

Notes: The checker recomputes ΔE_s from the provided total energies using the formula ΔE_s = [E(AFePO4NO3) - E(ANO3) - E(FePO4)] × 96.485 kJ/(mol·eV). The agent must ensure that total energies correspond to fully converged variable-cell relaxations under the specified DFT settings. Lattice parameters are compared separately.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "references",
          "compounds"
        ],
        "properties": {
          "references": {
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "required": [
                "total_energy_eV"
              ],
              "properties": {
                "total_energy_eV": {
                  "type": "number"
                }
              }
            }
          },
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "A",
                "total_energy_eV",
                "delta_E_kJmol",
                "crystal_system",
                "a",
                "b",
                "c",
                "alpha",
                "beta",
                "gamma",
                "V"
              ],
              "properties": {
                "A": {
                  "type": "string"
                },
                "total_energy_eV": {
                  "type": "number"
                },
                "delta_E_kJmol": {
                  "type": "number"
                },
                "crystal_system": {
                  "type": "string"
                },
                "a": {
                  "type": "number"
                },
                "b": {
                  "type": "number"
                },
                "c": {
                  "type": "number"
                },
                "alpha": {
                  "type": "number"
                },
                "beta": {
                  "type": "number"
                },
                "gamma": {
                  "type": "number"
                },
                "V": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Contains the total energies of all computed phases (AFePO4NO3, ANO3, FePO4) and the relaxed lattice parameters. The checker will recompute the stabilization energy ΔE_s for each A from the total energies using the reaction stoichiometry and compare the recomputed values and lattice parameters to the paper's reference."
    }
  ],
  "notes": "The checker recomputes ΔE_s from the provided total energies using the formula ΔE_s = [E(AFePO4NO3) - E(ANO3) - E(FePO4)] × 96.485 kJ/(mol·eV). The agent must ensure that total energies correspond to fully converged variable-cell relaxations under the specified DFT settings. Lattice parameters are compared separately."
}
```

## How you are scored
A hidden verifier inspects your submitted dft_results.json. It extracts the total energies and recomputes the stabilization energy ΔE_s for each cation using the formula ΔE_s = [E(AFePO4NO3) – E(ANO3) – E(FePO4)] × 96.485 kJ/(mol·eV). These recomputed values, along with your reported lattice parameters (a, b, c, α, β, γ, V), are compared to a set of reference results that the verifier holds. The comparison accounts for the expected spread in a full DFT re-run (different compiler, library, subtle algorithmic differences, etc.) by using generous tolerances. The final reward is a weighted average: approximately 60 % of the score comes from the accuracy of the stabilization energies, and 40 % from the accuracy of the lattice parameters. Importantly, simply reporting the reference numbers without a genuine DFT calculation will not yield a high score, because the verifier recomputes from your raw total energies and checks internal consistency; a fabricated or guessed set of energies will likely fail the checks.
