# DFT Adsorption of H2S and SO2 on h-YN Monolayer

## Problem background
Sulfur-containing gases (H2S and SO2) are toxic pollutants released from industrial activities and natural processes. Two-dimensional (2D) materials offer high surface-to-volume ratios and tunable electronic properties for gas scavenging and sensing. The hexagonal yttrium nitride (h-YN) monolayer is a recently predicted semiconductor with promising carrier mobility. Its interaction with sulfur-containing gases in the presence of environmental oxygen is unknown. This task investigates the adsorption of H2S and SO2 on pristine h-YN and on an O2-preadsorbed h-YN substrate using first-principles density functional theory (DFT). The key quantities to compute are the adsorption energies and the resulting band gaps, which determine the potential for gas capture and sensing.

## Approach
Use plane-wave DFT with the GGA-PBE exchange-correlation functional and Grimme's DFT-D2 dispersion correction. Model the h-YN monolayer in a supercell with a vacuum region. First, relax the pristine h-YN monolayer to obtain its total energy and band structure (extract the indirect band gap). Next, compute reference energies for isolated H2S, SO2, and O2 molecules. Then, for each gas molecule (H2S and SO2), scan multiple adsorption sites (Y-top, N-top, bridge, hollow) and molecular orientations on the pristine h-YN; fully relax each configuration to locate the minimum-energy structure and record total energies and band gaps. Repeat the same adsorption site scan for an O2 molecule on pristine h-YN to obtain the O2-preadsorbed structure and its band gap. Finally, using the relaxed O2-h-YN slab as substrate, scan adsorption of H2S and SO2 again and relax to find the minimum-energy configurations. Compute the adsorption energies from the total energies using standard subtractions. Collect all band gaps and compile the results into a JSON file.

## Reproduction target
Produce a single JSON file (/app/outputs/results.json) containing:
- Adsorption energies (E_ads) for H2S on pristine h-YN, SO2 on pristine h-YN, O2 on pristine h-YN, H2S on O2-preadsorbed h-YN, and SO2 on O2-preadsorbed h-YN (all in eV).
- Band gaps (indirect) for pristine h-YN, H2S adsorbed on pristine h-YN, SO2 adsorbed on pristine h-YN, O2-preadsorbed h-YN, H2S adsorbed on O2-h-YN, and SO2 adsorbed on O2-h-YN (all in eV).
- Total DFT energies (in eV) of all relevant systems (for optional internal consistency), including the isolated gas-phase molecules.
The adsorption energies must be computed from the total energies using the standard formula: E_ads = E(system) − E(substrate) − E(gas). The target is to reproduce these quantities as determined by DFT at the PBE-D2 level.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW PBE pseudopotentials (Y, N, S, H, O): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Gas-phase energy calculations
- Role: process
- Action: Using Quantum ESPRESSO with PBE functional and DFT-D2 dispersion correction, calculate the total energy of isolated H2S, SO2, and O2 molecules in sufficiently large vacuum boxes, with convergence settings consistent with the surface calculations.
- Evidence: `/app/outputs/gas_phase_energies.log`

### Step 2: Pristine h-YN optimization and band gap
- Role: process
- Action: Relax the h-YN monolayer supercell (lattice constant 3.767 Å) using PBE-D2 and compute the band structure to extract the indirect band gap. Record the total energy E(h-YN).
- Evidence: `/app/outputs/pristine_hyn_relax.log`

### Step 3: SCG adsorption on pristine h-YN
- Role: process
- Action: For H2S and SO2 separately, scan multiple adsorption sites (Y-top, N-top, bridge, hollow) and molecular orientations; fully relax the geometries to locate minimum-energy configurations. Record total energies E(H2S@h-YN) and E(SO2@h-YN) and compute the band gaps of these minimum-energy systems.
- Evidence: `/app/outputs/scg_on_pristine.log`

### Step 4: O2 adsorption on pristine h-YN
- Role: process
- Action: Place O2 over h-YN, scan binding sites and orientations (parallel/perpendicular); fully relax to find the minimum-energy configuration (note O2 dissociates). Record total energy E(O2-h-YN) and compute its band gap.
- Evidence: `/app/outputs/o2_on_hyn.log`

### Step 5: SCG adsorption on O2-h-YN
- Role: process
- Action: Using the relaxed O2-h-YN structure as substrate, scan sites and orientations for H2S and SO2; fully relax to find minimum-energy configurations. Record total energies E(H2S@O2-h-YN) and E(SO2@O2-h-YN) and compute their band gaps.
- Evidence: `/app/outputs/scg_on_o2hyn.log`

### Step 6: Compile scored quantities
- Role: scored (load-bearing)
- Action: From the computed total energies, calculate adsorption energies: E_ads(SCG) = E(SCG@h-YN) - E(h-YN) - E(SCG); E_ads(O2) = E(O2-h-YN) - E(h-YN) - E(O2); E_ads(SCG on O2) = E(SCG@O2-h-YN) - E(O2-h-YN) - E(SCG). Collect all band gaps (pristine, H2S@h-YN, SO2@h-YN, O2-h-YN, H2S@O2-h-YN, SO2@O2-h-YN). Write results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"adsorption_energies": {"H2S_on_pristine": float, "SO2_on_pristine": float, "O2_on_pristine": float, "H2S_on_O2_hYN": float, "SO2_on_O2_hYN": float}, "band_gaps": {"pristine_hYN": float, "H2S_on_pristine": float, "SO2_on_pristine": float, "O2_hYN": float, "H2S_on_O2_hYN": float, "SO2_on_O2_hYN": float}, "total_energies": {"hYN": float, "H2S_molecule": float, "SO2_molecule": float, "O2_molecule": float, "H2S_on_pristine": float, "SO2_on_pristine": float, "O2_on_pristine": float, "H2S_on_O2_hYN": float, "SO2_on_O2_hYN": float}}
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
- description: Main scored artifact containing adsorption energies and band gaps reproduced from DFT calculations.
- schema:
  - `type`: object
  - `required`: `adsorption_energies`, `band_gaps`, `total_energies`
  - `properties`:
    - `adsorption_energies`:
      - `type`: object
      - `required`: `H2S_on_pristine`, `SO2_on_pristine`, `O2_on_pristine`, `H2S_on_O2_hYN`, `SO2_on_O2_hYN`
      - `description`: Adsorption energies in eV, as defined in the workflow.
    - `band_gaps`:
      - `type`: object
      - `required`: `pristine_hYN`, `H2S_on_pristine`, `SO2_on_pristine`, `O2_hYN`, `H2S_on_O2_hYN`, `SO2_on_O2_hYN`
      - `description`: Indirect band gaps in eV.
    - `total_energies`:
      - `type`: object
      - `required`: `hYN`, `H2S_molecule`, `SO2_molecule`, `O2_molecule`, `H2S_on_pristine`, `SO2_on_pristine`, `O2_on_pristine`, `H2S_on_O2_hYN`, `SO2_on_O2_hYN`
      - `description`: Total DFT energies in eV (included for completeness, not directly scored).

Notes: Only adsorption energies and band gaps are scored; total energies are present for optional internal consistency checks.

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
        "type": "object",
        "required": [
          "adsorption_energies",
          "band_gaps",
          "total_energies"
        ],
        "properties": {
          "adsorption_energies": {
            "type": "object",
            "required": [
              "H2S_on_pristine",
              "SO2_on_pristine",
              "O2_on_pristine",
              "H2S_on_O2_hYN",
              "SO2_on_O2_hYN"
            ],
            "description": "Adsorption energies in eV, as defined in the workflow."
          },
          "band_gaps": {
            "type": "object",
            "required": [
              "pristine_hYN",
              "H2S_on_pristine",
              "SO2_on_pristine",
              "O2_hYN",
              "H2S_on_O2_hYN",
              "SO2_on_O2_hYN"
            ],
            "description": "Indirect band gaps in eV."
          },
          "total_energies": {
            "type": "object",
            "required": [
              "hYN",
              "H2S_molecule",
              "SO2_molecule",
              "O2_molecule",
              "H2S_on_pristine",
              "SO2_on_pristine",
              "O2_on_pristine",
              "H2S_on_O2_hYN",
              "SO2_on_O2_hYN"
            ],
            "description": "Total DFT energies in eV (included for completeness, not directly scored)."
          }
        }
      },
      "description": "Main scored artifact containing adsorption energies and band gaps reproduced from DFT calculations."
    }
  ],
  "notes": "Only adsorption energies and band gaps are scored; total energies are present for optional internal consistency checks."
}
```

## How you are scored
A hidden verifier independently reads your results.json file and compares the reported adsorption energies and band gaps to reference values derived from the original study. Each quantity is checked against an appropriate tolerance; better agreement yields higher partial credit. Only the adsorption energies and band gaps are directly scored; the total energies are present for optional internal checks but not numerically scored. Reporting a single number is not sufficient—the verifier requires the full JSON structure with all required fields. The final reward is a weighted sum of per-quantity scores.
