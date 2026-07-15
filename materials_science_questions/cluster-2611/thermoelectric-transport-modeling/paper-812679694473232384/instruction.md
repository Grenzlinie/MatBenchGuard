# Thermoelectric Power Factor Enhancement by Graphene Quantum Dot Adsorption on GeSe Monolayer

## Problem background
Thermoelectric materials convert waste heat into useful electricity. Among two-dimensional materials, germanium selenide (GeSe) monolayer is a promising candidate due to its favorable electronic properties. One route to boost thermoelectric performance is to adsorb a graphene quantum dot (GQD) on the monolayer, creating a hybrid structure that may increase the power factor (the product of squared Seebeck coefficient and electrical conductivity). This work investigates whether adsorbing a pyrene molecule (C₁₆H₁₀) on a 4×4 GeSe monolayer significantly raises the thermoelectric power factor at room temperature (300 K) compared to the pristine GeSe monolayer. Your task is to compute, from first-principles density functional theory (DFT) and the Boltzmann transport equation under constant relaxation time approximation, the electronic bandgap of isolated GeSe, the adsorption energy of pyrene on GeSe, and the maximum power factor at 300 K for both the pristine and GQD-adsorbed systems, then derive the power factor enhancement ratio.

## Approach
The workflow is a first-principles DFT and Boltzmann transport investigation. You will build atomistic models of a 4×4 GeSe monolayer and the pyrene GQD, then perform full geometry optimizations using Quantum ESPRESSO with the PBE functional, Grimme DFT‑D2 van der Waals correction, and standard pseudopotentials. After relaxing the isolated GeSe monolayer, the isolated GQD, and the combined GQD@GeSe system, you compute the adsorption energy from the total energies. Next, you run self‑consistent and band‑structure calculations to obtain electronic band energies for both the pristine GeSe monolayer and the GQD@GeSe monolayer. Using the band energies, you employ BoltzTraP (classic or BoltzTraP2) under the constant relaxation time approximation to evaluate the Seebeck coefficient (S), the electrical conductivity per relaxation time (σ/τ), and the power factor (S²σ/τ) as functions of doping level and temperature. From these transport data you extract the maximum power factor at 300 K for each system and the corresponding doping concentration. The entire comparison is between two conditions: pristine GeSe monolayer (the baseline) and GQD@GeSe (the hybrid system). No prior knowledge of the paper’s numbers is required; you compute everything from the described protocol and public resources.

## Reproduction target
Your goal is to compute and report the following key quantities from the complete DFT and BoltzTraP pipeline:
- Electronic bandgap of the pristine GeSe monolayer (eV).
- Adsorption energy of pyrene on the 4×4 GeSe monolayer (eV), defined as E_ad = E(GQD@GeSe) – [E(GeSe) + E(GQD)].
- At 300 K, for both the pristine GeSe monolayer and the GQD@GeSe monolayer, the maximum power factor (in W/mKs) and the doping concentration at which that maximum occurs.
- The power factor enhancement ratio: PF(GQD@GeSe) / PF(GeSe) at the 300 K maxima.

You must write these results to the exact JSON files specified in the workflow steps (bandgap.json, adsorption_energy.json, power_factor_enhancement.json). The task is self‑contained; the reported metrics are derived solely from running the described calculations, not from matching any pre‑given value.

## Assets

- Quantum ESPRESSO (QE): https://www.quantum-espresso.org/
- BoltzTraP (classic or BoltzTraP2): https://www.boltztrap.org/ or https://gitlab.com/sousaw/BoltzTraP2
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- GeSe crystal structure (orthorhombic Pnma): Crystallography Open Database (COD) or ICSD entry for GeSe
- Pyrene molecule (C16H10) structure: https://pubchem.ncbi.nlm.nih.gov/compound/31423

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Build a 4×4 supercell of GeSe monolayer (orthorhombic, with 15 Å vacuum) and the pyrene graphene quantum dot (C16H10) to prepare DFT input files.
- Evidence: `/app/outputs/dft_inputs_constructed.txt`

### Step 2: DFT optimization of isolated GeSe and GQD
- Role: process
- Action: Perform full geometry optimization of the isolated 4×4 GeSe monolayer and the isolated pyrene GQD using Quantum ESPRESSO with PBE, DFT-D2 van der Waals correction, 100 Ry plane-wave cutoff, and a 3×3×1 Monkhorst-Pack k-point grid. Save total energies and optimized structures.
- Evidence: `/app/outputs/dft_optimizations_isolated.json`

### Step 3: DFT optimization of GQD@GeSe and adsorption energy calculation
- Role: process
- Action: Place the relaxed GQD initially ~3.5 Å above the relaxed GeSe monolayer (parallel) and perform full geometry optimization of the combined system using the same DFT settings as step02. Compute the adsorption energy E_ad = E_combined - (E_GeSe + E_GQD) and record the equilibrium vertical separation.
- Evidence: `/app/outputs/dft_optimization_combined.json`

### Step 4: Electronic structure calculation
- Role: process
- Action: Using the optimized geometries from steps 02 and 03, run SCF and band-structure calculations (same DFT parameters) for both the pristine GeSe monolayer and the GQD@GeSe monolayer. Save band eigenvalues along a high-symmetry path.
- Evidence: `/app/outputs/dft_bandstructure.json`

### Step 5: Thermoelectric transport with BoltzTraP
- Role: process
- Action: Run BoltzTraP (or BoltzTraP2) using the band energies from step04 for both systems, under constant relaxation time approximation. Compute Seebeck coefficient S, electrical conductivity σ/τ, and power factor S²σ/τ as functions of doping level N and temperature T. Save the raw transport data.
- Evidence: `/app/outputs/boltztrap_output.json`

### Step 6: Report GeSe monolayer bandgap
- Role: scored
- Action: Extract the electronic bandgap of the pristine GeSe monolayer from the band structure data (step04). Write the value in eV.
- Output file: `/app/outputs/bandgap.json`
- Format: json
- Contract: { "type": "object", "required": ["bandgap_eV"], "units": {"bandgap_eV": "eV"} }
- Scoring: scored by hidden verifier

### Step 7: Report GQD adsorption energy
- Role: scored
- Action: From the optimized DFT energies (steps 02 and 03), compute the adsorption energy E_ad = E_combined - (E_GeSe + E_GQD). Write the value in eV.
- Output file: `/app/outputs/adsorption_energy.json`
- Format: json
- Contract: { "type": "object", "required": ["adsorption_energy_eV"], "units": {"adsorption_energy_eV": "eV"} }
- Scoring: scored by hidden verifier

### Step 8: Report power factor enhancement ratio
- Role: scored (load-bearing)
- Action: From the BoltzTraP output (step05), identify the maximum power factor at 300 K for both the pristine GeSe monolayer and the GQD@GeSe monolayer. Compute the enhancement ratio PF(GQD@GeSe) / PF(GeSe). Write the ratio, the individual maximum power factors, and the corresponding doping concentration.
- Output file: `/app/outputs/power_factor_enhancement.json`
- Format: json
- Contract: { "type": "object", "required": ["temperature_K", "GeSe_max_power_factor_W_per_mKs", "GQD_GeSe_max_power_factor_W_per_mKs", "power_factor_enhancement_ratio"], "units": { "temperature_K": "K", "GeSe_max_power_factor_W_per_mKs": "W/mKs", "GQD_GeSe_max_power_factor_W_per_mKs": "W/mKs", "power_factor_enhancement_ratio": "dimensionless" } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap.json`
- `/app/outputs/adsorption_energy.json`
- `/app/outputs/power_factor_enhancement.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap.json
- path: `/app/outputs/bandgap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic bandgap of the pristine GeSe monolayer. The checker compares the value against the paper-reported bandgap within a tolerance.
- schema:
  - `type`: object
  - `required`: `bandgap_eV`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `bandgap_eV`: eV

### adsorption_energy.json
- path: `/app/outputs/adsorption_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Adsorption energy of pyrene on the 4×4 GeSe monolayer. The checker compares the value against the paper-reported adsorption energy within a tolerance.
- schema:
  - `type`: object
  - `required`: `adsorption_energy_eV`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `adsorption_energy_eV`: eV

### power_factor_enhancement.json
- path: `/app/outputs/power_factor_enhancement.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Thermoelectric power factor enhancement ratio (PF_GQD@GeSe / PF_GeSe) at 300 K. Full credit is awarded if the ratio is at least the paper-reported threshold (≥3.5).
- schema:
  - `type`: object
  - `required`: `temperature_K`, `GeSe_max_power_factor_W_per_mKs`, `GQD_GeSe_max_power_factor_W_per_mKs`, `power_factor_enhancement_ratio`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `temperature_K`: K
    - `GeSe_max_power_factor_W_per_mKs`: W/mKs
    - `GQD_GeSe_max_power_factor_W_per_mKs`: W/mKs
    - `power_factor_enhancement_ratio`: dimensionless

Notes: The checker extracts the bandgap and adsorption energy for exact-match scoring within hidden tolerances. The power factor enhancement ratio is scored as threshold_or_better, so better-than-paper performance is not penalized. All other fields in the power factor output are for audit and documentation; only the ratio and its meeting of the threshold carry the main weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "bandgap_eV"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "bandgap_eV": "eV"
        }
      },
      "description": "Electronic bandgap of the pristine GeSe monolayer. The checker compares the value against the paper-reported bandgap within a tolerance."
    },
    {
      "file": "adsorption_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "adsorption_energy_eV"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "Adsorption energy of pyrene on the 4×4 GeSe monolayer. The checker compares the value against the paper-reported adsorption energy within a tolerance."
    },
    {
      "file": "power_factor_enhancement.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "temperature_K",
          "GeSe_max_power_factor_W_per_mKs",
          "GQD_GeSe_max_power_factor_W_per_mKs",
          "power_factor_enhancement_ratio"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "temperature_K": "K",
          "GeSe_max_power_factor_W_per_mKs": "W/mKs",
          "GQD_GeSe_max_power_factor_W_per_mKs": "W/mKs",
          "power_factor_enhancement_ratio": "dimensionless"
        }
      },
      "description": "Thermoelectric power factor enhancement ratio (PF_GQD@GeSe / PF_GeSe) at 300 K. Full credit is awarded if the ratio is at least the paper-reported threshold (≥3.5)."
    }
  ],
  "notes": "The checker extracts the bandgap and adsorption energy for exact-match scoring within hidden tolerances. The power factor enhancement ratio is scored as threshold_or_better, so better-than-paper performance is not penalized. All other fields in the power factor output are for audit and documentation; only the ratio and its meeting of the threshold carry the main weight."
}
```

## How you are scored
A hidden verifier will inspect the JSON artifacts you write to /app/outputs. Each scored output file contributes to your total reward:
- bandgap.json (15% weight): your computed GeSe monolayer bandgap is compared against a paper‑derived hidden reference within an undisclosed tolerance.
- adsorption_energy.json (15% weight): your adsorption energy is compared against a hidden reference within an undisclosed tolerance.
- power_factor_enhancement.json (70% weight): your computed power factor enhancement ratio must **meet or exceed** a hidden threshold derived from the paper’s reported result. Exceeding the threshold is not penalized; only failing to reach it reduces the score.

All hidden references are the actual values reported in the paper for the same quantities and conditions. The verifier only reads the submitted files; it has no access to your intermediate calculations. You must complete the entire DFT and transport workflow—merely reporting the paper’s numbers without performing the calculations will not pass.
