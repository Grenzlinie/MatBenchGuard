# Molecular Dynamics Simulation of Fracture in Silicate Glasses: Bulk and Nanowire Mechanical Properties

## Problem background
Oxide glasses such as silica (SiO₂) and soda‑silicate (20Na₂O·80SiO₂, NS20) are essential engineering materials, but their practical strength is limited by inherent brittleness and by surface flaws. Understanding the atomic‑scale mechanisms that control fracture, intrinsic strength, and elasticity is crucial for designing stronger glasses. Classical molecular dynamics (MD) simulations can isolate the intrinsic mechanical response—strength, strain at failure, and elastic modulus—under well‑defined conditions and reveal how system size, composition, and the presence of nanoscopic defects influence the ductility or brittleness of the material. This task reproduces such simulations for both bulk glasses and glass nanowires, providing quantitative insight into the factors governing mechanical reliability at the nanoscale.

## Approach
The workflow uses classical MD with the PMMCS rigid‑ion pair potential, implemented in an MD package capable of Ewald summation and anisotropic NPT (e.g., LAMMPS). Amorphous bulk glasses are generated via a melt‑quench protocol: a random high‑temperature melt is equilibrated and then cooled to room temperature under pressure control to match experimental densities. For defective silica models, repulsive fictitious atoms are inserted to create artificial nanovoids (a 1.0 nm spherical void and a 2.0×1.0×1.0 nm void) and the system is remelted to obtain void‑containing glass structures. Nanowires are cast by placing a bulk parallelepiped inside a carbon nanotube template and applying a short‑range exponential repulsive potential between carbon and glass atoms; after the same melt‑quench cycle the template is removed to leave a free‑standing nanowire. Finally, uniaxial tensile tests are performed at a constant engineering strain rate along the wire/long axis, with lateral pressure relaxation (anisotropic NPT). The resulting stress‑strain curves are analyzed to extract the peak engineering stress (intrinsic strength), the strain at peak stress (strain at failure), and the zero‑strain Young's modulus via a linear fit to the low‑strain elastic region. The procedure is applied to seven distinct glass systems: two compositions (SiO₂ and NS20), three bulk geometries (flaw‑free, with 1.0 nm void, with 2.0 nm void), and two nanowire geometries.

## Reproduction target
Compute and report the mechanical properties for each of the following seven glass systems:
- SiO₂ bulk (30,000 atoms)
- SiO₂ with a 1.0 nm spherical void
- SiO₂ with a 2.0×1.0×1.0 nm void
- SiO₂ nanowire
- NS20 bulk (30,000 atoms)
- NS20 bulk (60,000 atoms)
- NS20 nanowire

For every system, output:
- intrinsic strength (maximum engineering stress, in GPa)
- strain at failure (strain at peak stress, in percent; for the notched models where this quantity is not defined, use null)
- zero‑strain Young's modulus (GPa)

Save the results as a JSON array to `/app/outputs/mechanical_properties.json`. Each array entry must be an object with the fields `system` (string), `strength_GPa` (number), `strain_at_failure_percent` (number or null), and `youngs_modulus_GPa` (number). All seven system entries are required.

## Assets

- PMMCS interatomic potential parameters for SiO2 and Na2O-silicate: 10.1021/jp0611018
- Molecular dynamics simulation package (e.g. LAMMPS): https://www.lammps.org/

## Workflow steps

### Step 1: Generate bulk glass structures
- Role: process
- Action: Generate bulk amorphous SiO2 (30,000 atoms) and NS20 (30,000 atoms) glasses using a melt-quench MD protocol (heat to 5000 K, cool to 300 K) with the PMMCS interatomic potential; relax in NPT at 300 K to target experimental densities (SiO2 2.20 g/cm³, NS20 2.39 g/cm³). Produce a 60,000-atom NS20 model by replicating the 30k cell along z.
- Evidence: `/app/outputs/bulk_models.pkl`

### Step 2: Create defective SiO2 models with nanovoids
- Role: process
- Action: Using the 30k SiO2 bulk structure, insert repulsive fictitious atoms to create a spherical void of 1.0 nm diameter and a void of dimensions 2.0×1.0×1.0 nm; remelt and cool using the same melt-quench protocol to obtain defective glass models.
- Evidence: `/app/outputs/defective_models.pkl`

### Step 3: Cast glass nanowires
- Role: process
- Action: Place bulk parallelepiped structures (SiO2 and NS20) inside carbon nanotubes; apply an exponential repulsive potential between C and glass atoms to confine the melt; perform melt-quench (same protocol); remove the CNT and relax in NPT at 300 K to obtain SiO2 and NS20 nanowires.
- Evidence: `/app/outputs/nanowire_models.pkl`

### Step 4: Uniaxial tensile tests and mechanical property extraction
- Role: scored (load-bearing)
- Action: For each of the seven glass systems (SiO2 bulk 30k, SiO2 notched 1.0 nm, SiO2 notched 2.0 nm, SiO2 nanowire, NS20 bulk 30k, NS20 bulk 60k, NS20 nanowire), run uniaxial tension MD along z at a strain rate of 10^9 s⁻¹ and 300 K with NPT lateral relaxation. Compute engineering stress-strain curves. Extract intrinsic strength (maximum stress in GPa), strain at failure (strain at peak stress in %, null for notched models where unavailable), and zero-strain Young's modulus (linear fit to 0–5% strain for NS20, 0–12% for SiO2). Output results as a JSON array to mechanical_properties.json.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: Array of objects with keys: system (string), strength_GPa (number), strain_at_failure_percent (number or null), youngs_modulus_GPa (number). Required: system, strength_GPa, youngs_modulus_GPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON array containing the extracted mechanical properties for each of the seven simulated glass systems. The checker verifies that all required systems are present and compares the values to the hidden gold (paper Table 1) within per-property tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `strength_GPa`, `youngs_modulus_GPa`
    - `properties`:
      - `system`:
        - `type`: string
      - `strength_GPa`:
        - `type`: number
      - `strain_at_failure_percent`:
        - `type`: number
        - `nullable`: True
      - `youngs_modulus_GPa`:
        - `type`: number

Notes: Strain at failure for notched models may be omitted (null) as the paper does not report it. All other systems must provide all three properties.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "strength_GPa",
            "youngs_modulus_GPa"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "strength_GPa": {
              "type": "number"
            },
            "strain_at_failure_percent": {
              "type": "number",
              "nullable": true
            },
            "youngs_modulus_GPa": {
              "type": "number"
            }
          }
        }
      },
      "description": "JSON array containing the extracted mechanical properties for each of the seven simulated glass systems. The checker verifies that all required systems are present and compares the values to the hidden gold (paper Table 1) within per-property tolerances."
    }
  ],
  "notes": "Strain at failure for notched models may be omitted (null) as the paper does not report it. All other systems must provide all three properties."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/mechanical_properties.json`. The verifier checks that the seven required system entries are present. For each entry, it compares the reported strength, strain at failure, and Young's modulus against reference values derived from the original study. A system passes if all its reported quantities fall within the verifier's acceptable range; systems with missing values or values outside that range do not pass. The final score is the fraction of systems that fully pass (a number between 0.0 and 1.0). Because the reference values are hidden and the acceptance tolerances are tight, you must genuinely execute the full simulation pipeline described in the workflow steps. Merely outputting a known textbook value or guessing will not succeed.
