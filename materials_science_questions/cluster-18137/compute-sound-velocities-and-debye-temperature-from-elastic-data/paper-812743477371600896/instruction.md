# Thermodynamic properties of P6_222‑X3 (X=C, Si, Ge) from elastic constants

## Problem background
Group‑14 element allotropes with super‑dense structures in the P6₂22 phase are candidates for thermal‑management applications. Sound velocities, the Debye temperature, and the minimum thermal conductivity are key indicators of thermal behaviour. Computing these properties from the elastic constants and density obtained via first‑principles calculations provides a rigorous evaluation of the predicted materials.

## Approach
First‑principles density functional theory (DFT) with the PBE functional and ultrasoft pseudopotentials is used to obtain the equilibrium geometry and the full elastic tensor of each material. The relaxed structure yields the lattice parameters and density; the stress‑strain method gives the independent elastic constants (C₁₁, C₃₃, C₄₄, C₆₆, C₁₂, C₁₃) and the polycrystalline Voigt–Reuss–Hill bulk and shear moduli. From these, the isotropic longitudinal and transverse sound velocities are computed via Navier’s equations, and the Debye temperature follows from the standard solid‑state formula. Single‑crystal elastic constants are used to obtain anisotropic sound velocities along the [001] and [100] directions. Finally, the minimum thermal conductivity κ_min at 300 K is calculated using Cahill’s model, both isotropically and along the two principal directions.

## Reproduction target
Compute the isotropic sound velocities (vⱼ, vₜ, vₘ) and Debye temperature Θ_D, the anisotropic sound velocities for propagation along [001] and [100], and the minimum thermal conductivity κ_min at 300 K for C₃, Si₃, and Ge₃ in the P6₂22 phase. Write the results to the three JSON output files as specified in the workflow steps.

## Assets

- Quantum ESPRESSO: quantum-espresso
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific stack: numpy scipy

## Workflow steps

### Step 1: Generate initial crystal structures
- Role: process
- Action: Construct hexagonal P6₂22 (No. 180) primitive or conventional cell for C₃, Si₃, Ge₃. Place three atoms at the 3c Wyckoff position (0.5, 0, 0). Estimate initial lattice parameters from covalent radii and the super‑dense packing (e.g., a≈2.6 Å, c≈2.8 Å for C; scale for Si/Ge).
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: DFT geometry optimization
- Role: process
- Action: For each material, run PBE geometry optimization (PWscf) to relax atomic positions and lattice parameters. Use energy cutoffs of 400 eV (C), 340 eV (Si), 240 eV (Ge), a Monkhorst‑Pack k‑point grid spacing ≤ 0.025 Å⁻¹, and SSSP ultrasoft pseudopotentials. Converge forces to < 1×10⁻⁵ Ry/Å.
- Evidence: `/app/outputs/relax_output.json`

### Step 3: DFT elastic constants calculation
- Role: process
- Action: Compute the full elastic tensor via the stress‑strain method for each relaxed structure using the same functional and pseudopotentials. Extract the independent constants (C₁₁, C₃₃, C₄₄, C₆₆, C₁₂, C₁₃) and derive the Voigt‑Reuss‑Hill bulk modulus B and shear modulus G. Store the density, the elastic constants, B, and G in elastic_constants.json.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 4: Compute isotropic sound velocities and Debye temperature
- Role: scored (load-bearing)
- Action: From the density, B, and G in elastic_constants.json, compute longitudinal (vl), transverse (vt), and mean (vm) sound velocities using Navier's equations. Then compute the Debye temperature ΘD using the standard formula (n=1; atomic masses: C 12.0107, Si 28.0855, Ge 72.63 u). Write the results to step_01_isotropic_thermo.json.
- Output file: `/app/outputs/step_01_isotropic_thermo.json`
- Format: json
- Contract: JSON object with top-level keys 'C3', 'Si3', 'Ge3'. Each value is an object with numeric fields: 'v_l' (m/s), 'v_t' (m/s), 'v_m' (m/s), 'Theta_D' (K).
- Scoring: scored by hidden verifier

### Step 5: Compute anisotropic sound velocities
- Role: scored (load-bearing)
- Action: Using the single‑crystal elastic constants and density from elastic_constants.json, compute directional sound velocities along the [001] and [100] propagation directions. For [001]: vl = √(C₃₃/ρ), vt1 = vt2 = √(C₄₄/ρ). For [100]: vl = √((C₁₁−C₁₂)/(2ρ)), vt1 = √(C₁₁/ρ), vt2 = √(C₄₄/ρ). Write the results to step_02_anisotropic_velocities.json.
- Output file: `/app/outputs/step_02_anisotropic_velocities.json`
- Format: json
- Contract: JSON object with keys 'C3', 'Si3', 'Ge3'. Each value is an object with keys '[001]' and '[100]', each containing numeric fields 'v_l' (m/s), 'v_t1' (m/s), 'v_t2' (m/s).
- Scoring: scored by hidden verifier

### Step 6: Compute minimum thermal conductivity
- Role: scored (load-bearing)
- Action: At 300 K, compute the isotropic minimum thermal conductivity κ_min using Cahill's model with the three isotropic sound velocities from step 4. Also compute directional κ_min for [001] and [100] using the corresponding anisotropic sound velocities from step 5. Write the results to step_03_min_thermal_conductivity.json.
- Output file: `/app/outputs/step_03_min_thermal_conductivity.json`
- Format: json
- Contract: JSON object with keys 'C3', 'Si3', 'Ge3'. Each value is an object with numeric fields: 'isotropic' (W/cm·K), '[001]' (W/cm·K), '[100]' (W/cm·K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_isotropic_thermo.json`
- `/app/outputs/step_02_anisotropic_velocities.json`
- `/app/outputs/step_03_min_thermal_conductivity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_isotropic_thermo.json
- path: `/app/outputs/step_01_isotropic_thermo.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Isotropic sound velocities and Debye temperature for the three P6₂22 allotropes.
- schema:
  - `type`: object
  - `description`: Top-level keys: C3, Si3, Ge3. Each value is an object with numeric fields: v_l (m/s), v_t (m/s), v_m (m/s), Theta_D (K).

### step_02_anisotropic_velocities.json
- path: `/app/outputs/step_02_anisotropic_velocities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Anisotropic sound velocities along [001] and [100] propagation directions.
- schema:
  - `type`: object
  - `description`: Keys: C3, Si3, Ge3. Each value is an object with keys '[001]' and '[100]', each mapping to an object with numeric fields: v_l (m/s), v_t1 (m/s), v_t2 (m/s).

### step_03_min_thermal_conductivity.json
- path: `/app/outputs/step_03_min_thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Minimum thermal conductivity at 300 K (isotropic and directional).
- schema:
  - `type`: object
  - `description`: Keys: C3, Si3, Ge3. Each value is an object with numeric fields: isotropic (W/cm·K), [001] (W/cm·K), [100] (W/cm·K).

Notes: The agent must produce elastic_constants.json (not scored). The checker recomputes thermodynamic quantities from it where possible.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_isotropic_thermo.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "description": "Top-level keys: C3, Si3, Ge3. Each value is an object with numeric fields: v_l (m/s), v_t (m/s), v_m (m/s), Theta_D (K)."
      },
      "description": "Isotropic sound velocities and Debye temperature for the three P6₂22 allotropes."
    },
    {
      "file": "step_02_anisotropic_velocities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "description": "Keys: C3, Si3, Ge3. Each value is an object with keys '[001]' and '[100]', each mapping to an object with numeric fields: v_l (m/s), v_t1 (m/s), v_t2 (m/s)."
      },
      "description": "Anisotropic sound velocities along [001] and [100] propagation directions."
    },
    {
      "file": "step_03_min_thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "description": "Keys: C3, Si3, Ge3. Each value is an object with numeric fields: isotropic (W/cm·K), [001] (W/cm·K), [100] (W/cm·K)."
      },
      "description": "Minimum thermal conductivity at 300 K (isotropic and directional)."
    }
  ],
  "notes": "The agent must produce elastic_constants.json (not scored). The checker recomputes thermodynamic quantities from it where possible."
}
```

## How you are scored
A hidden verifier independently evaluates your output files. The verifier reads step_01_isotropic_thermo.json, step_02_anisotropic_velocities.json, and step_03_min_thermal_conductivity.json, recomputes the thermodynamic quantities from the intermediate elastic constants and density you provide, and compares your values against reference values using small tolerances. Each output file contributes a weighted portion of the total score. To earn full credit, your results must be internally consistent and correctly derived from the DFT‑supplied inputs; reporting numbers without executing the required workflow steps will not pass.
