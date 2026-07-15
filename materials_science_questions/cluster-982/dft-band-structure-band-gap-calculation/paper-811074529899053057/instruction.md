# Stanene/MoS2 Heterostructure DFT Band Gap and Effective Mass Reproduction

## Problem background
Stanene, a two-dimensional honeycomb monolayer of tin atoms, hosts a Dirac cone at the K point, suggesting high carrier mobility. However, pristine stanene is a zero-gap semiconductor, limiting its use in switching devices. Placing stanene on a substrate such as monolayer MoS2 may break the sublattice symmetry, inducing a band gap while preserving the Dirac-like dispersion. This task reproduces a density functional theory (DFT) calculation of the electronic properties of the stanene/MoS2 heterostructure to determine whether a band gap opens and to quantify the resulting effective masses and binding energy for the hollow stacking pattern.

## Approach
We perform first-principles DFT calculations using the plane-wave code Quantum ESPRESSO with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and a van der Waals correction. The heterostructure model is built from publicly available crystal structures: monolayer stanene (low-buckled honeycomb) and monolayer MoS2 (2H phase), combined into a 2×2 stanene / 3×3 MoS2 supercell with the hollow stacking pattern and a ~20 Å vacuum layer. After relaxing the atomic positions of the heterostructure, we compute the total energies of the combined system and of the isolated monolayers to obtain the binding energy per Sn atom. A band structure calculation is performed along the high-symmetry path K–M–Γ. From the resulting electronic bands near K we extract the direct band gap and perform parabolic fits to obtain the electron and hole effective masses along the K–M and K–Γ directions.

## Reproduction target
Compute the following six quantities for the hollow-pattern stanene/MoS2 heterostructure at the equilibrium interlayer spacing, using DFT with the PBE functional and a van der Waals correction: direct band gap at the K point (eV), electron effective masses along K–M and K–Γ (units of free electron mass m0), hole effective masses along K–M and K–Γ (units of m0), and binding energy per Sn atom (meV). Report all values inside results.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency Pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure databases (e.g., Materials Project): https://materialsproject.org/

## Workflow steps

### Step 1: Build stanene/MoS2 heterostructure model
- Role: process
- Action: Obtain crystal structures of monolayer stanene (low-buckled honeycomb) and monolayer MoS2 (2H phase) from a public database. Build the hollow-pattern stanene/MoS2 heterostructure with a 2×2 stanene and 3×3 MoS2 lateral supercell, a ~20 Å vacuum layer, and the equilibrium interlayer distance. Output the atomic coordinates in a format suitable for Quantum ESPRESSO.
- Evidence: `/app/outputs/heterostructure_input.in`

### Step 2: DFT relaxation, band structure, and property extraction
- Role: scored (load-bearing)
- Action: Perform DFT calculations using PBE-GGA with vdW correction in Quantum ESPRESSO: (1) relax atomic positions of the heterostructure; (2) compute total energies of isolated stanene and MoS2 monolayers for binding energy; (3) run a band structure calculation along K-M-Γ; (4) extract the direct band gap at the K point; (5) fit parabolic bands near K to obtain effective masses for electrons and holes along K-M and K-Γ; (6) calculate the binding energy per Sn atom. Write all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"band_gap_eV": "number", "binding_energy_meV_per_Sn": "number", "effective_mass_electron_KM": "number", "effective_mass_electron_KG": "number", "effective_mass_hole_KM": "number", "effective_mass_hole_KG": "number"}
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
- description: JSON file containing the six scored quantities computed from the DFT calculations.
- schema:
  - `type`: object
  - `required`: `band_gap_eV`, `binding_energy_meV_per_Sn`, `effective_mass_electron_KM`, `effective_mass_electron_KG`, `effective_mass_hole_KM`, `effective_mass_hole_KG`
  - `properties`:
    - `band_gap_eV`:
      - `type`: number
      - `description`: Direct band gap at the K point in eV.
    - `binding_energy_meV_per_Sn`:
      - `type`: number
      - `description`: Binding energy per Sn atom in meV.
    - `effective_mass_electron_KM`:
      - `type`: number
      - `description`: Electron effective mass along K-M in units of free electron mass m0.
    - `effective_mass_electron_KG`:
      - `type`: number
      - `description`: Electron effective mass along K-Γ in units of free electron mass m0.
    - `effective_mass_hole_KM`:
      - `type`: number
      - `description`: Hole effective mass along K-M in units of free electron mass m0.
    - `effective_mass_hole_KG`:
      - `type`: number
      - `description`: Hole effective mass along K-Γ in units of free electron mass m0.

Notes: Only the hollow pattern and PBE level (no SOC) are required. The values are the agent's computed results; the hidden checker compares them to reference values.

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
          "band_gap_eV",
          "binding_energy_meV_per_Sn",
          "effective_mass_electron_KM",
          "effective_mass_electron_KG",
          "effective_mass_hole_KM",
          "effective_mass_hole_KG"
        ],
        "properties": {
          "band_gap_eV": {
            "type": "number",
            "description": "Direct band gap at the K point in eV."
          },
          "binding_energy_meV_per_Sn": {
            "type": "number",
            "description": "Binding energy per Sn atom in meV."
          },
          "effective_mass_electron_KM": {
            "type": "number",
            "description": "Electron effective mass along K-M in units of free electron mass m0."
          },
          "effective_mass_electron_KG": {
            "type": "number",
            "description": "Electron effective mass along K-Γ in units of free electron mass m0."
          },
          "effective_mass_hole_KM": {
            "type": "number",
            "description": "Hole effective mass along K-M in units of free electron mass m0."
          },
          "effective_mass_hole_KG": {
            "type": "number",
            "description": "Hole effective mass along K-Γ in units of free electron mass m0."
          }
        }
      },
      "description": "JSON file containing the six scored quantities computed from the DFT calculations."
    }
  ],
  "notes": "Only the hollow pattern and PBE level (no SOC) are required. The values are the agent's computed results; the hidden checker compares them to reference values."
}
```

## How you are scored
A hidden verifier reads results.json and checks that all six fields are present and numeric. It then scores each value by comparing it to a hidden reference. The comparison uses tolerances that reflect the expected spread when re-running DFT with Quantum ESPRESSO instead of the reference code, so a correctly executed workflow will score well. Each of the six quantities contributes equally to the final reward. Simply looking up and reporting numbers from the literature without performing the full DFT simulation will not match the hidden reference and will yield a low score.
