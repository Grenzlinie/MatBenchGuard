# Extracting effective tunneling mass from DFT imaginary band structure

## Problem background
Future dynamic random-access memory (DRAM) scaling requires metal-insulator-metal (MIM) capacitors with high permittivity dielectrics, low leakage current and small physical thickness. As fabrication improves and defect densities decrease, the ultimate leakage limit is set by intrinsic direct tunneling, which depends on the dielectric thickness, the electrode/dielectric barrier, and the effective electron tunneling mass (m_tunnel) in the dielectric. This task focuses on computing the effective tunneling mass for two candidate high-k materials: rutile TiO2 (r-TiO2) and SrTiO3 (STO), including Sr-rich variants. The m_tunnel parameter is extracted from first-principles calculations of the imaginary band structure, providing a critical input for scaling projections.

## Approach
The effective tunneling mass is obtained by computing the complex band structure of bulk crystals using density-functional theory. For each material and crystallographic orientation, the imaginary wavenumber κ(E) in the band gap is calculated with the Quantum ESPRESSO package using ultra-soft pseudopotentials at the PBE level and a plane-wave cutoff of 540 eV. The conduction band minimum (CBM) is identified and the imaginary bands are scaled to match experimental band gaps. At a fixed energy below the CBM corresponding to the trap depth observed in real films (1.3 eV for r-TiO2, 0.9 eV for STO and Sr-rich variants), the effective tunneling mass is extracted via the parabolic approximation m_tunnel = ħ²κ² / [2(E_CBM − E)]. The resulting m_tunnel values are then compared across different orientations and stoichiometries to assess their impact on tunneling leakage.

## Reproduction target
Compute the effective tunneling mass at the specified trap depth for every material/orientation combination listed in the workflow (r-TiO2 (110), (001), (100), (101); stoichiometric SrTiO3 (110), (001), (111); and Sr-rich Sr₂TiO₄ (001) and Sr₀.₆₂Ti₀.₃₈O₄ (001)). Report all values in a single JSON array stored at /app/outputs/computed_mtunnel.json. Each entry must contain the material, orientation, stoichiometry, the energy below CBM used, and the computed m_tunnel in units of free electron mass.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE USPP pseudopotentials for Ti, Sr, O: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of rutile TiO2 (ICSD 9161 or equivalent): ICSD 9161
- Crystal structure of cubic SrTiO3 (ICSD 23082 or equivalent): ICSD 23082
- Crystal structures of Sr2TiO4 and Sr0.62Ti0.38O4: 10.1149/1.3257917

## Workflow steps

### Step 1: DFT complex band structure calculations
- Role: process
- Action: For each material/orientation: r-TiO2 (110), (001), (100), (101); SrTiO3 (110), (001), (111); Sr2TiO4 (001); Sr0.62Ti0.38O4 (001), set up the bulk crystal structure using appropriate lattice parameters, select PBE USPP pseudopotentials, and use a plane-wave energy cutoff of 540 eV. Run Quantum ESPRESSO to compute the complex band structure (imaginary bands) in the band gap along the relevant direction. Extract the imaginary wavenumber κ as a function of energy below the conduction band minimum.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: Extract effective tunneling mass and produce scored output
- Role: scored (load-bearing)
- Action: For each material/orientation, at the energy below the conduction band minimum corresponding to the trap depth (use the values: 1.3 eV for r-TiO2, 0.9 eV for all SrTiO3 and Sr-rich variants), take the imaginary wavenumber κ from the complex band data and compute the effective tunneling mass using the parabolic approximation formula m_tunnel = ħ²κ² / [2(E_CBM - E)], expressed in units of free electron mass m_e. Assemble all DFT-extracted values into a JSON array.
- Output file: `/app/outputs/computed_mtunnel.json`
- Format: json
- Contract: JSON array of objects, each with string fields: material, orientation, stoichiometry, and numeric fields: energy_below_CBM (float, eV), m_tunnel (float, units of m_e).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_mtunnel.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_mtunnel.json
- path: `/app/outputs/computed_mtunnel.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Effective tunneling mass values computed from DFT imaginary bands at the specified trap depth energies.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `orientation`, `stoichiometry`, `energy_below_CBM`, `m_tunnel`
    - `properties`:
      - `material`:
        - `type`: string
      - `orientation`:
        - `type`: string
      - `stoichiometry`:
        - `type`: string
      - `energy_below_CBM`:
        - `type`: number
        - `units`: eV
      - `m_tunnel`:
        - `type`: number
        - `units`: m_e

Notes: The DFT calculations require substantial CPU/GPU resources; the agent is expected to acquire necessary compute outside the sandbox and bring the final artifact back.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_mtunnel.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "orientation",
            "stoichiometry",
            "energy_below_CBM",
            "m_tunnel"
          ],
          "properties": {
            "material": {
              "type": "string"
            },
            "orientation": {
              "type": "string"
            },
            "stoichiometry": {
              "type": "string"
            },
            "energy_below_CBM": {
              "type": "number",
              "units": "eV"
            },
            "m_tunnel": {
              "type": "number",
              "units": "m_e"
            }
          }
        }
      },
      "description": "Effective tunneling mass values computed from DFT imaginary bands at the specified trap depth energies."
    }
  ],
  "notes": "The DFT calculations require substantial CPU/GPU resources; the agent is expected to acquire necessary compute outside the sandbox and bring the final artifact back."
}
```

## How you are scored
Your submission is evaluated entirely by a hidden verifier. The verifier reads the scored artifact computed_mtunnel.json and checks each reported effective tunneling mass against hidden reference values and expected relative trends between different materials, orientations and stoichiometries. For example, certain orientations are expected to yield higher m_tunnel than others. You must obtain these values by genuinely running the DFT workflow; reporting a number without executing the steps will not satisfy the hidden checks. The final reward is a weighted combination of the results from this scored step.
