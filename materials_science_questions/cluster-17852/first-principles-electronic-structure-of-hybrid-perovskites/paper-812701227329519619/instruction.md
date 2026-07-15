# DFT Formation Energies and Band Gaps of Cubic CsPbX3 Perovskites

## Problem background
All-inorganic cesium lead halide (CsPbX3) perovskite nanocrystals have emerged as promising light-absorbing materials for hybrid organic solar cells. A key challenge is to select a halide composition that balances thermodynamic stability with favorable charge carrier mobility. Density functional theory (DFT) calculations are employed to evaluate the relative stability and electronic properties of the cubic perovskite compositions CsPbI3, CsPbBr1.5I1.5, and CsPbBr3. This task involves computing the formation energies and direct band gaps (with and without spin-orbit coupling) of these three materials using an open-source DFT framework, following the theoretical approach presented in the literature.

## Approach
The stability and electronic structure of the three cubic perovskite systems are investigated using DFT. Starting from the published experimental lattice parameters and space group, crystal structures are built, including a 2×2×2 supercell for the mixed-halide compound to model a 1:1 Br:I ratio. Geometry optimization is performed at the PBE (Perdew-Burke-Ernzerhof) generalized gradient approximation level to obtain relaxed total energies and equilibrium geometries. Subsequently, formation energies are derived by comparing the total energy of each perovskite to the energies of the elemental references. The electronic band structure is computed with the TB-mBJ (Tran-Blaha modified Becke-Johnson) meta-GGA potential, including spin-orbit coupling (SOC) due to the heavy lead atom. The direct band gap at the R-point is extracted for each compound with and without SOC. The workflow uses open-source DFT software (e.g., Quantum ESPRESSO) and standard publicly available pseudopotentials, replacing any proprietary code with an equivalent open implementation.

## Reproduction target
Produce a JSON file (`dft_results.json`) that reports, for each of the three compositions (CsPbI3, CsPbBr1.5I1.5, CsPbBr3), the formation energy in eV, the direct band gap without spin-orbit coupling in eV, and the direct band gap with spin-orbit coupling in eV. The formation energies should reflect the relative thermodynamic stability among the three perovskites as obtained from the DFT optimizations. The band gaps are the fundamental electronic gaps at the R-point derived from the TB‑mBJ+SOC band structure calculations. All results must originate from a self-contained DFT workflow executed by the solving agent.

## Assets

- Crystal structure parameters for CsPbI3, CsPbBr3, CsPbBr1.5I1.5
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Standard PAW pseudopotentials: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Build input structures for cubic perovskites: CsPbI3 (a=6.348 Å, Pm-3m, 1 formula unit), CsPbBr3 (a=5.868 Å, Pm-3m), and CsPbBr1.5I1.5 using a 2×2×2 supercell with a=6.07 Å, 8 Cs, 8 Pb, 12 Br, 12 I atoms, arranged with cubic symmetry.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Geometry optimization with PBE
- Role: process
- Action: Perform variable-cell relaxation (or fixed experimental cell with ionic relaxation) for each structure using the PBE exchange-correlation functional. Obtain total energies and relaxed lattice parameters/positions.
- Evidence: `/app/outputs/optimization_results.log`

### Step 3: Formation energies and band gaps with TB-mBJ+SOC
- Role: scored (load-bearing)
- Action: From the optimized structures, compute formation energies (using elemental reference energies), and perform band structure calculations with the TB-mBJ meta-GGA functional including spin-orbit coupling. Extract the direct band gap at the R-point both with and without SOC for each compound.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"CsPbI3": {"formation_energy(eV)": <number>, "bandgap_noSOC(eV)": <number>, "bandgap_withSOC(eV)": <number>}, "CsPbBr1.5I1.5": {...}, "CsPbBr3": {...}}
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
- target_policy: reference_match
- description: JSON file containing the computed formation energies and band gaps (with and without spin-orbit coupling) for the three perovskite compositions. Used for scoring against hidden reference values and ordering checks.
- schema:
  - `type`: object
  - `required`: `CsPbI3`, `CsPbBr1.5I1.5`, `CsPbBr3`
  - `properties`:
    - `CsPbI3`:
      - `type`: object
      - `required`: `formation_energy(eV)`, `bandgap_noSOC(eV)`, `bandgap_withSOC(eV)`
      - `properties`:
        - `formation_energy(eV)`:
          - `type`: number
        - `bandgap_noSOC(eV)`:
          - `type`: number
        - `bandgap_withSOC(eV)`:
          - `type`: number
    - `CsPbBr1.5I1.5`:
      - `type`: object
      - `required`: `formation_energy(eV)`, `bandgap_noSOC(eV)`, `bandgap_withSOC(eV)`
      - `properties`:
        - `formation_energy(eV)`:
          - `type`: number
        - `bandgap_noSOC(eV)`:
          - `type`: number
        - `bandgap_withSOC(eV)`:
          - `type`: number
    - `CsPbBr3`:
      - `type`: object
      - `required`: `formation_energy(eV)`, `bandgap_noSOC(eV)`, `bandgap_withSOC(eV)`
      - `properties`:
        - `formation_energy(eV)`:
          - `type`: number
        - `bandgap_noSOC(eV)`:
          - `type`: number
        - `bandgap_withSOC(eV)`:
          - `type`: number

Notes: The checker will compare each reported field to hidden reference values (paper-reported) within appropriate tolerances, and verify formation energy ordering: E(CsPbBr3) < E(CsPbBr1.5I1.5) < E(CsPbI3).

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CsPbI3",
          "CsPbBr1.5I1.5",
          "CsPbBr3"
        ],
        "properties": {
          "CsPbI3": {
            "type": "object",
            "required": [
              "formation_energy(eV)",
              "bandgap_noSOC(eV)",
              "bandgap_withSOC(eV)"
            ],
            "properties": {
              "formation_energy(eV)": {
                "type": "number"
              },
              "bandgap_noSOC(eV)": {
                "type": "number"
              },
              "bandgap_withSOC(eV)": {
                "type": "number"
              }
            }
          },
          "CsPbBr1.5I1.5": {
            "type": "object",
            "required": [
              "formation_energy(eV)",
              "bandgap_noSOC(eV)",
              "bandgap_withSOC(eV)"
            ],
            "properties": {
              "formation_energy(eV)": {
                "type": "number"
              },
              "bandgap_noSOC(eV)": {
                "type": "number"
              },
              "bandgap_withSOC(eV)": {
                "type": "number"
              }
            }
          },
          "CsPbBr3": {
            "type": "object",
            "required": [
              "formation_energy(eV)",
              "bandgap_noSOC(eV)",
              "bandgap_withSOC(eV)"
            ],
            "properties": {
              "formation_energy(eV)": {
                "type": "number"
              },
              "bandgap_noSOC(eV)": {
                "type": "number"
              },
              "bandgap_withSOC(eV)": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "JSON file containing the computed formation energies and band gaps (with and without spin-orbit coupling) for the three perovskite compositions. Used for scoring against hidden reference values and ordering checks."
    }
  ],
  "notes": "The checker will compare each reported field to hidden reference values (paper-reported) within appropriate tolerances, and verify formation energy ordering: E(CsPbBr3) < E(CsPbBr1.5I1.5) < E(CsPbI3)."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage’s artifact. The formation energy stage is evaluated based on whether the relative ordering of the computed formation energies among the three compositions agrees with the expected thermodynamic stability trend (i.e., the relative ordering of stability). The band gap stage is evaluated by comparing each reported band gap value (both without and with spin‑orbit coupling) to hidden reference values derived from the literature; the comparison accommodates the expected spread between different DFT implementations at the same level of theory. The final reward is a weighted combination of the scores from the formation energy ordering and the band gap matches, with the band gaps carrying the major weight. Reporting numbers that deviate significantly from the expected physical trends or falling outside typical code-to-code variability will reduce the reward.
