# Lithium absorption and migration on Li-Mg surfaces via DFT

## Problem background
Lithium metal anodes suffer from dendritic growth and poor cycling stability. Doping Li metal with small amounts of magnesium (Mg) has been shown to improve performance, but the optimal Mg content and the underlying mechanism remain unclear. Density functional theory (DFT) calculations can provide insight into Li deposition behavior on Li-Mg alloy surfaces and help identify the optimal doping level.

## Approach
Use an open-source DFT code (Quantum ESPRESSO) with standard PBE pseudopotentials to build slab models of the Li(100) surface with a thick vacuum layer (>16 Å). For Li-Mg alloy surfaces, substitute one surface Li atom with Mg and adjust the supercell size to achieve a range of Mg doping contents (near 0, 4.2, 4.5, 7, 12, and 24 wt%). For each surface, compute the total energy of the surface with an additional Li atom placed near the Mg center (or equivalent site for pure Li) and the energy of the isolated Li atom in vacuum; calculate absorption energy as E_absorption = E_total − E_surface − E_Li. Identify the Mg content that minimizes the absorption energy. Additionally, use the nudged elastic band (NEB) method to compute the migration activation barrier for Li diffusion on the pure Li surface and on the Li-Mg surface (~4.5 wt% Mg) for two paths: toward the Mg atom and away from the Mg atom, following the hopping mechanism over bridge sites. Report the absorption energies and the three migration barriers in structured JSON files.

## Reproduction target
Compute Li absorption energies on the Li(100) surface and on Li-Mg alloy surfaces with Mg contents of ~0, 4.2, 4.5, 7, 12, and 24 wt%. Identify the Mg content that minimizes the absorption energy. Also compute Li migration barriers via NEB on pure Li surface, on Li-Mg surface toward Mg, and on Li-Mg surface away from Mg. Report results in two JSON files:
- `/app/outputs/absorption_energies.json`: array of objects with fields `mg_wt_percent` and `absorption_energy_eV`.
- `/app/outputs/migration_barriers.json`: object with keys `pure_Li_barrier_eV`, `Li_Mg_toward_barrier_eV`, and `Li_Mg_away_barrier_eV`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build Li-Mg surface models
- Role: process
- Action: Construct slab models of the Li(100) surface (vacuum >16 Å) and Li-Mg alloy surfaces by substituting a surface Li atom with Mg and adjusting supercell size to achieve Mg doping contents of ~0, 4.2, 4.5, 7, 12, and 24 wt%. Also prepare the initial and final configurations for the NEB migration paths on pure Li and Li-Mg surfaces (toward and away from Mg).
- Evidence: `/app/outputs/surface_model_list.txt`

### Step 2: Compute Li absorption energies
- Role: scored (load-bearing)
- Action: For each surface model (pure Li and each Li-Mg doping level), relax the geometry and compute the total energy of the surface with an additional Li atom placed near the Mg center (or equivalent site for pure Li) and the energy of the isolated Li atom in vacuum. Calculate absorption energy as E_absorption = E_total - E_surface - E_Li. Report all absorption energies.
- Output file: `/app/outputs/absorption_energies.json`
- Format: json
- Contract: [{"mg_wt_percent": float, "absorption_energy_eV": float}]
- Scoring: scored by hidden verifier

### Step 3: Compute Li migration barriers via NEB
- Role: scored
- Action: Using the NEB method, determine the migration activation energy barrier for Li diffusion on pure Li(100) surface, and on Li-Mg surface for two paths: moving toward the Mg atom and moving away from the Mg atom. Follow the hopping mechanism over bridge sites. Report the three barriers.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: {"pure_Li_barrier_eV": float, "Li_Mg_toward_barrier_eV": float, "Li_Mg_away_barrier_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_energies.json`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_energies.json
- path: `/app/outputs/absorption_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Li absorption energies on pure Li and Li-Mg surfaces across a range of Mg doping levels. The checker will verify that a clear global minimum exists consistent with the expected doping.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `mg_wt_percent`, `absorption_energy_eV`
    - `properties`:
      - `mg_wt_percent`:
        - `type`: number
        - `description`: Mg doping content in weight percent
      - `absorption_energy_eV`:
        - `type`: number
        - `description`: Li absorption energy in eV

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Li migration energy barriers on pure Li and Li-Mg surfaces. The checker will verify that the Li-Mg barriers are significantly larger than the pure Li barrier.
- schema:
  - `type`: object
  - `required`: `pure_Li_barrier_eV`, `Li_Mg_toward_barrier_eV`, `Li_Mg_away_barrier_eV`
  - `properties`:
    - `pure_Li_barrier_eV`:
      - `type`: number
      - `description`: Li migration barrier on pure Li(100) surface, in eV
    - `Li_Mg_toward_barrier_eV`:
      - `type`: number
      - `description`: Li migration barrier on Li-Mg surface toward the Mg atom, in eV
    - `Li_Mg_away_barrier_eV`:
      - `type`: number
      - `description`: Li migration barrier on Li-Mg surface away from the Mg atom, in eV

Notes: Only the single-Mg absorption energy trend and the three migration barriers are scored; the two-Mg absorption energy illustration and all experimental battery results are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "mg_wt_percent",
            "absorption_energy_eV"
          ],
          "properties": {
            "mg_wt_percent": {
              "type": "number",
              "description": "Mg doping content in weight percent"
            },
            "absorption_energy_eV": {
              "type": "number",
              "description": "Li absorption energy in eV"
            }
          }
        }
      },
      "description": "Li absorption energies on pure Li and Li-Mg surfaces across a range of Mg doping levels. The checker will verify that a clear global minimum exists consistent with the expected doping."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "pure_Li_barrier_eV",
          "Li_Mg_toward_barrier_eV",
          "Li_Mg_away_barrier_eV"
        ],
        "properties": {
          "pure_Li_barrier_eV": {
            "type": "number",
            "description": "Li migration barrier on pure Li(100) surface, in eV"
          },
          "Li_Mg_toward_barrier_eV": {
            "type": "number",
            "description": "Li migration barrier on Li-Mg surface toward the Mg atom, in eV"
          },
          "Li_Mg_away_barrier_eV": {
            "type": "number",
            "description": "Li migration barrier on Li-Mg surface away from the Mg atom, in eV"
          }
        }
      },
      "description": "Li migration energy barriers on pure Li and Li-Mg surfaces. The checker will verify that the Li-Mg barriers are significantly larger than the pure Li barrier."
    }
  ],
  "notes": "Only the single-Mg absorption energy trend and the three migration barriers are scored; the two-Mg absorption energy illustration and all experimental battery results are excluded."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output. For absorption energies, the checker inspects structural properties (e.g., whether the global minimum occurs at the expected Mg content region) using the output contract's structural audit. For migration barriers, the checker applies a threshold-or-better rule: it verifies that the Li-Mg surface barriers (both toward and away) are at least a specified multiple of the pure Li barrier. The final reward is a weighted combination of scores from the two artifacts. Simply reporting the paper's numbers is not sufficient; your computed values must correctly reflect the expected trends and relative magnitudes.
