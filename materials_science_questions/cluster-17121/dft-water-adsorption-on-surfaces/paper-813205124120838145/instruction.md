# Adhesion Energies of SDS Surfactant Monolayers on TiO2 Polymorphs

## Problem background
Surfactants such as sodium dodecyl sulfate (SDS) are widely used as organic templates to control the nucleation and growth of titania (TiO₂) nanostructures. The binding strength of an SDS monolayer on a given TiO₂ surface influences which polymorph (anatase or rutile) and which crystallographic orientation are favoured during nucleation. In this task we compute the adhesion energies of SDS monolayers on eight low‑index TiO₂ surfaces — anatase (100), (110), (011), (001) and rutile (100), (110), (011), (001) — both in vacuum and accounting for the displacement of water molecules that would be present in an experimental synthesis.

## Approach
The adhesion is assessed through atomistic molecular dynamics (MD) simulations. A combined force field is assembled from the Matsui–Akaogi model for TiO₂ (with scaled Lennard‑Jones parameters to correct for the charge difference between the two models) and the Domínguez force field for SDS (a united‑carbon‑atom tail, explicit sulfate headgroup, and sodium counterions) and SPC water. For each of the eight surfaces, atomistic slabs ~3 nm × 3 nm with a 7 nm vacuum gap are built from the bulk crystal structure. SDS molecules are placed at three surface densities (~2.2, 3.3, and 4.4 nm⁻²) in an all‑trans configuration. Each system is equilibrated and a production trajectory is run at 300 K in the canonical ensemble. The total adhesion energy β is computed by averaging the difference between the configurational energy of the combined surface‑monolayer system and the sum of the energies of the isolated components, divided by the surface area. To account for water displacement, two additional simulations are performed per surface‑density combination: one with a water slab on both sides of the crystal and the monolayer at one end, and another with the monolayer directly on the crystal and water on the opposite side. The modified adhesion energy β′ is obtained from the difference of the configurational energies of these two setups divided by the area, averaged over a production period. All simulations must use the specified force fields and an MD engine that supports them (e.g., DL_POLY Classic or LAMMPS).

## Reproduction target
Produce two CSV files containing the computed adhesion energies for every surface‑density combination: `beta_in_vacuo.csv` (columns: surface, density_nm2, beta_J_m2) and `beta_water_modified.csv` (columns: surface, density_nm2, beta_prime_J_m2). The values must be computed from the MD trajectories as described in the workflow. The task is considered successfully reproduced if the CSV data, when checked by a hidden verifier, satisfy the structural relationships that characterise the paper’s main findings. These relationships concern the sign of all adhesion energies, the ordering of surfaces by binding strength for the in‑vacuo energies, the consistency of that ordering when water displacement is included, and the reduction in spread among surfaces after accounting for water.

## Assets

- Matsui–Akaogi TiO2 force field: 10.1080/08927029108022409
- Domínguez SDS/water force field: 10.1021/jp204250k
- SPC water model
- MD simulation engine: https://www.scd.stfc.ac.uk/Pages/DL_POLY.aspx
- TiO2 crystal structures

## Workflow steps

### Step 1: Force field assembly and surface slab construction
- Role: process
- Action: Combine the Matsui–Akaogi TiO2 force field with the Domínguez SDS/water force field, scale the Lennard‑Jones epsilon parameters of Ti and O to correct charge differences, then construct atomistic slabs for the eight low‑index surfaces (anatase (100),(110),(011),(001); rutile (100),(110),(011),(001)) with lateral dimensions ~3 nm, thickness ~1.5 nm, and a 7 nm vacuum gap.
- Evidence: `/app/outputs/surface_slabs.pkl`

### Step 2: Initial SDS monolayer placement
- Role: process
- Action: For each surface slab, place SDS molecules at three densities (~2.2, ~3.3, ~4.4 nm⁻²) using a random‑avoiding algorithm (e.g. Poisson disk sampling). Surfactants are initially in all‑trans configuration with tails normal to the surface.
- Evidence: `/app/outputs/initial_configs.pkl`

### Step 3: In vacuo adhesion energies (β)
- Role: scored
- Action: For each surface–density combination run NVT molecular dynamics in vacuum at 300 K. Equilibrate, then collect a production trajectory. Compute the total adhesion energy β as the average of the difference in configurational energies between the combined system and its isolated components, summed over all surfactant components. Save the results.
- Output file: `/app/outputs/beta_in_vacuo.csv`
- Format: csv
- Contract: columns: surface (string), density_nm2 (float), beta_J_m2 (float)
- Scoring: scored by hidden verifier

### Step 4: Water‑modified adhesion energies (β′)
- Role: scored
- Action: For each surface–density combination build two water‑containing systems (Simulation I: water slab on both sides of the crystal with monolayer at one end; Simulation II: monolayer on crystal, water repositioned on the other side) using SPC water. Run NVT MD at 300 K, equilibrate, and collect a production trajectory for both configurations. Compute the modified adhesion energy β′ as the difference in configurational energies between the two simulations divided by the surface area, averaged over production. Save the results.
- Output file: `/app/outputs/beta_water_modified.csv`
- Format: csv
- Contract: columns: surface (string), density_nm2 (float), beta_prime_J_m2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/beta_in_vacuo.csv`
- `/app/outputs/beta_water_modified.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### beta_in_vacuo.csv
- path: `/app/outputs/beta_in_vacuo.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: In vacuo adhesion energies (β) for eight TiO₂ surfaces at three SDS monolayer densities.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `density_nm2`, `beta_J_m2`

### beta_water_modified.csv
- path: `/app/outputs/beta_water_modified.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Water‑modified adhesion energies (β′) accounting for water displacement, for the same surfaces and densities.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `density_nm2`, `beta_prime_J_m2`

Notes: The checker verifies that all β and β′ are negative, that A(100) is the most negative (strongest binding), R(110) the second most negative, and A(001) the least negative for β and that the same ordering holds for β′. It also checks that the range of β′ is smaller than that of β at each density. Exact numerical values are not required; the audit tolerates implementation‑dependent variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "beta_in_vacuo.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "density_nm2",
          "beta_J_m2"
        ]
      },
      "description": "In vacuo adhesion energies (β) for eight TiO₂ surfaces at three SDS monolayer densities."
    },
    {
      "file": "beta_water_modified.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "density_nm2",
          "beta_prime_J_m2"
        ]
      },
      "description": "Water‑modified adhesion energies (β′) accounting for water displacement, for the same surfaces and densities."
    }
  ],
  "notes": "The checker verifies that all β and β′ are negative, that A(100) is the most negative (strongest binding), R(110) the second most negative, and A(001) the least negative for β and that the same ordering holds for β′. It also checks that the range of β′ is smaller than that of β at each density. Exact numerical values are not required; the audit tolerates implementation‑dependent variations."
}
```

## How you are scored
A hidden verifier will read your CSV files and evaluate them against a set of structural requirements that encapsulate the key claims of the paper. Specifically, the verifier checks that all reported adhesion energies are negative, that the surfaces are ordered in a particular way (with a specified surface showing the most negative β, another the second most negative, and a third the least negative), that the same ordering holds for β′, and that for every density the range (maximum minus minimum) of β′ is smaller than the range of β. Each requirement carries a weight, and the final score is a weighted sum of these structural checks. The verifier does not compare your numerical values to a set of gold numbers; it only verifies the sign and the relative rankings and spreads. Thus you must run the full MD workflow and produce physically meaningful energies that satisfy these relationships.
