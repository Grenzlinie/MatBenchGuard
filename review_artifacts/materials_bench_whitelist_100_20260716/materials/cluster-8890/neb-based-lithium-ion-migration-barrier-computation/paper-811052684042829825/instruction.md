# Reproduce Charge Transport Mechanisms in Solid Li2S2

## Problem background
In lithium-sulfur (Li-S) batteries, solid lithium persulfide (Li₂S₂) forms as an intermediate discharge product alongside lithium sulfide (Li₂S). Unlike Li₂S, the charge transport mechanisms in Li₂S₂ are not well understood, yet they critically influence battery capacity, overpotential, and rate performance. This study investigates the electronic structure and the role of native defects and polarons as charge carriers in crystalline Li₂S₂ using first-principles density functional theory (DFT) calculations.

## Approach
The work employs DFT with the PBE functional for geometry optimization and the HSE06 hybrid functional for accurate electronic structure and energetics. Starting from the published p1 polymorph crystal structure of Li₂S₂, the unit cell is relaxed and a (3×3×2) supercell is constructed. Native defects are introduced: neutral and charged Li and S₂ vacancies, as well as electron and hole polarons (p⁻ and p⁺). Reference phases (bcc Li and an isolated S₈ molecule) are prepared. The total density of states is computed for the pristine supercell to extract band gaps under PBE and HSE06. Defect formation energies are calculated from total energies of the defect supercells and references under the charge neutrality condition. The climbing-image nudged elastic band (CI-NEB) method is used to find minimum energy paths for each charge carrier along the [100], [010], and [001] directions. Finally, mobilities are estimated via the Einstein relation using the harmonic mean of the lowest diffusion barriers, and the ionic and electronic conductivities at 300 K are derived.

## Reproduction target
Compute and report the following quantities for the p1 polymorph of Li₂S₂:
- The electronic band gap using the PBE functional and the HSE06 hybrid functional.
- Formation energies (in eV) of the negatively charged Li vacancy (V_Li⁻), the positively charged S₂ vacancy (V_S₂²⁺), the electron polaron (p⁻), and the hole polaron (p⁺).
- The minimum CI-NEB diffusion barriers (in eV) for V_Li⁻, V_S₂²⁺, p⁻, and p⁺ along the [100], [010], and [001] crystallographic directions.
- From these barriers and formation energies, the estimated mobilities (in cm² V⁻¹ s⁻¹) of the dominant carriers and the resulting ionic and electronic conductivities (in S cm⁻¹) at 300 K.

## Assets

- p1 Li2S2 crystal structure (CIF): 10.1016/j.jpowsour.2014.06.105
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Standard solid-state pseudopotentials (SSSP) library: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Obtain p1 Li2S2 crystal structure
- Role: process
- Action: Fetch the p1 polymorph crystal structure of Li2S2 from the public source (Feng et al. 2014). Save it as a CIF file for subsequent steps.
- Evidence: none

### Step 2: Geometry optimization of p1 unit cell
- Role: process
- Action: Perform DFT geometry optimization of the p1 Li2S2 unit cell using the PBE functional (Quantum ESPRESSO). Relax atomic positions and lattice parameters. Save the optimized structure.
- Evidence: none

### Step 3: Supercell construction and defect generation
- Role: process
- Action: Build a (3×3×2) supercell from the optimized unit cell. Create supercells containing the following native defects and polarons: neutral Li vacancy, neutral S2 vacancy, negatively charged Li vacancy (V_Li-), positively charged S2 vacancy (V_S2^2+), electron polaron (p-), and hole polaron (p+). Also prepare reference phases: bcc Li and an isolated S8 molecule.
- Evidence: none

### Step 4: Calculate band gaps
- Role: scored
- Action: Compute the total density of states (TDOS) for the pristine (3×3×2) supercell using the PBE and HSE06 functionals. Extract the band gaps as the energy difference between the conduction band minimum and valence band maximum.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"PBE_band_gap_eV": float, "HSE06_band_gap_eV": float}
- Scoring: scored by hidden verifier

### Step 5: Defect formation energies
- Role: scored
- Action: Compute total energies of all defect supercells and reference phases (bcc Li, S8) using HSE06. Calculate formation energies of V_Li-, V_S2^2+, p-, and p+ using the charge neutrality condition. Report the energies in eV.
- Output file: `/app/outputs/defect_formation_energies.json`
- Format: json
- Contract: [{"defect": "V_Li-", "energy_eV": float}, {"defect": "V_S2_2plus", "energy_eV": float}, {"defect": "p_minus", "energy_eV": float}, {"defect": "p_plus", "energy_eV": float}]
- Scoring: scored by hidden verifier

### Step 6: Diffusion barriers (CI-NEB)
- Role: scored (load-bearing)
- Action: For each charge carrier (V_Li-, V_S2^2+, p-, p+), perform climbing-image nudged elastic band (CI-NEB) calculations using HSE06 along the [100], [010], and the two consecutive [001] sub-paths ([001]-in and [001]-out) for V_Li- as defined in the paper. For V_S2^2+, p-, and p+, use the standard [100], [010], and [001] directions. Report the minimum energy barrier for each path.
- Output file: `/app/outputs/diffusion_barriers.json`
- Format: json
- Contract: [{"defect": "V_Li-", "direction": "[100]", "barrier_eV": float}, {"defect": "V_Li-", "direction": "[010]", "barrier_eV": float}, {"defect": "V_Li-", "direction": "[001]-in", "barrier_eV": float}, {"defect": "V_Li-", "direction": "[001]-out", "barrier_eV": float}, ... (all reported paths)]
- Scoring: scored by hidden verifier

### Step 7: Mobility and conductivity
- Role: scored
- Action: Using the harmonic mean of the lowest diffusion barriers for each carrier and the formation energies, estimate mobilities at T=300 K via the Einstein relation and compute the ionic and electronic conductivities.
- Output file: `/app/outputs/mobility_conductivity.json`
- Format: json
- Contract: {"T_K": 300, "mobility_V_Li_minus_cm2_Vs": float, "mobility_p_plus_cm2_Vs": float, "ionic_conductivity_S_cm": float, "electronic_conductivity_S_cm": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/defect_formation_energies.json`
- `/app/outputs/diffusion_barriers.json`
- `/app/outputs/mobility_conductivity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed PBE and HSE06 band gaps of crystalline Li2S2.
- schema:
  - `type`: object
  - `required`:
    - `PBE_band_gap_eV`: float
    - `HSE06_band_gap_eV`: float

### defect_formation_energies.json
- path: `/app/outputs/defect_formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Formation energies of V_Li-, V_S2^2+, p-, and p+ in eV.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`:
      - `defect`: string
      - `energy_eV`: float

### diffusion_barriers.json
- path: `/app/outputs/diffusion_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: CI-NEB migration barriers for each charge carrier along each crystallographic direction.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`:
      - `defect`: string
      - `direction`: string
      - `barrier_eV`: float

### mobility_conductivity.json
- path: `/app/outputs/mobility_conductivity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Estimated mobilities (cm2/V·s) and conductivities (S/cm) at 300 K.
- schema:
  - `type`: object
  - `required`:
    - `T_K`: float
    - `mobility_V_Li_minus_cm2_Vs`: float
    - `mobility_p_plus_cm2_Vs`: float
    - `ionic_conductivity_S_cm`: float
    - `electronic_conductivity_S_cm`: float

Notes: All quantities should be computed from scratch using Quantum ESPRESSO. Do not simply extract numbers from the source paper. The checker compares the reported values against hidden gold tolerances (not disclosed to the solver).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "PBE_band_gap_eV": "float",
          "HSE06_band_gap_eV": "float"
        }
      },
      "description": "Computed PBE and HSE06 band gaps of crystalline Li2S2."
    },
    {
      "file": "defect_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": {
            "defect": "string",
            "energy_eV": "float"
          }
        }
      },
      "description": "Formation energies of V_Li-, V_S2^2+, p-, and p+ in eV."
    },
    {
      "file": "diffusion_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": {
            "defect": "string",
            "direction": "string",
            "barrier_eV": "float"
          }
        }
      },
      "description": "CI-NEB migration barriers for each charge carrier along each crystallographic direction."
    },
    {
      "file": "mobility_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T_K": "float",
          "mobility_V_Li_minus_cm2_Vs": "float",
          "mobility_p_plus_cm2_Vs": "float",
          "ionic_conductivity_S_cm": "float",
          "electronic_conductivity_S_cm": "float"
        }
      },
      "description": "Estimated mobilities (cm2/V·s) and conductivities (S/cm) at 300 K."
    }
  ],
  "notes": "All quantities should be computed from scratch using Quantum ESPRESSO. Do not simply extract numbers from the source paper. The checker compares the reported values against hidden gold tolerances (not disclosed to the solver)."
}
```

## How you are scored
Each of the four scored output files (band_gaps.json, defect_formation_energies.json, diffusion_barriers.json, mobility_conductivity.json) is independently evaluated by a hidden verifier. The verifier compares your computed values to reference values using predefined tolerances and combines them by weight to produce an overall reward. Submitting numbers taken from the literature without performing the actual DFT workflow will not score well, because the verifier expects values consistent with a correct re‑execution of the described procedure. Follow the workflow steps exactly and ensure all required artifacts are written to the specified output paths.
