# Reproduce DFT-based surface energy analysis of Au segregation in Cu3Au(111) surface

## Problem background
Cu3Au is a model binary alloy that exhibits an order-disorder transition at 663 K and has been widely studied for surface segregation phenomena. At the (111) surface, the bulk-truncated composition is 25% Au, but it is an open question whether Au segregates to the topmost layer and what the equilibrium surface stoichiometry is under realistic thermodynamic conditions. First-principles density-functional theory (DFT) calculations can provide a zero-temperature prediction of the surface composition by comparing the surface free energies of different atomic arrangements as a function of the chemical potentials of Cu and Au.

## Approach
The computational approach uses DFT with the PBE exchange-correlation functional and ultrasoft pseudopotentials as implemented in Quantum ESPRESSO. First, reference total energies for bulk fcc Cu, fcc Au, and the ordered L1₂ Cu₃Au phase are calculated to obtain per-atom energies and the equilibrium lattice constant. Then, a series of symmetric nine-layer slab models of the (111) surface is built, each containing four atoms per layer and a 2 nm vacuum gap. The Au concentration is varied systematically in the two outermost layers (0%, 25%, 50%, 75%, 100%), while the inner layers retain bulk stoichiometry, yielding 19 distinct compositions. For each slab, the positions of the three outermost layers on each side are relaxed until forces converge. The total energy, number of Cu and Au atoms, and surface area are recorded. Finally, surface free energies are computed as a function of the Cu chemical potential, with the allowed range of μ_Cu bounded by the bulk Cu atom energy (Cu-rich limit) and the formation enthalpy of Cu₃Au (Au-rich limit). The most stable surface composition is identified by finding which slab yields the lowest surface energy at the two endpoints of μ_Cu.

## Reproduction target
1. Compute bulk reference energies and the L1₂ Cu₃Au lattice constant, output as `bulk_reference.json`.
2. Construct 19 slab geometries and relax them using DFT; collect total energies, atom counts, and surface areas per slab into `slab_energies.csv`.
3. From the bulk and slab energies, compute the surface free energy for each composition as a function of Cu chemical potential, determine the upper and lower bounds of μ_Cu, and identify which composition has the lowest surface energy at the Cu-rich bound and which at the Au-rich bound. Write the result to `surface_energy_analysis.json` as `mu_Cu_upper`, `mu_Cu_lower`, `stable_at_upper`, and `stable_at_lower` (composition labels).

## Assets

- Quantum ESPRESSO: http://www.quantum-espresso.org/
- PBE ultrasoft pseudopotentials for Cu and Au: PSlibrary

## Workflow steps

### Step 1: Bulk reference DFT calculations
- Role: scored
- Action: Perform DFT total-energy calculations for bulk fcc Cu, fcc Au, and L12 Cu3Au to obtain total energies per atom (or per formula unit) and the equilibrium lattice constant of Cu3Au. Write results to /app/outputs/bulk_reference.json.
- Output file: `/app/outputs/bulk_reference.json`
- Format: json
- Contract: {"E_bulk_Cu": number (eV/atom), "E_bulk_Au": number (eV/atom), "E_bulk_Cu3Au": number (eV/f.u.), "lattice_constant_Cu3Au": number (angstrom)}
- Scoring: scored by hidden verifier

### Step 2: Construct slab models
- Role: process
- Action: Generate 19 initial slab geometries for the (111) surface: a 9-layer symmetric slab with 4 atoms per layer, 2 nm vacuum, and Au concentrations of 0, 25, 50, 75, 100% in the top two layers while inner layers are at bulk stoichiometry. Store the input files for the subsequent DFT relaxation step.
- Evidence: none

### Step 3: DFT relaxation of slab models and energy collection
- Role: scored
- Action: For each of the 19 slab configurations, relax the atomic positions of the three outermost layers on each side until forces are below 0.001 Ry/bohr, using DFT with the PBE functional, ultrasoft pseudopotentials, a plane-wave cutoff of 50 Ry, and a 7x7x1 Monkhorst-Pack k-point grid. Extract the total energy, number of Cu and Au atoms, and surface area. Write the compiled results to /app/outputs/slab_energies.csv.
- Output file: `/app/outputs/slab_energies.csv`
- Format: csv
- Contract: CSV with columns: composition_label (string, e.g. '50/25'), total_energy (float, eV), N_Cu (int), N_Au (int), surface_area (float, angstrom^2)
- Scoring: scored by hidden verifier

### Step 4: Surface energy analysis and stability determination
- Role: scored (load-bearing)
- Action: Using the bulk reference energies from step bulk_reference and the slab energies from step slab_relaxation, compute the surface free energy γ_surf for each slab as a function of Cu chemical potential within the allowed thermodynamic bounds. Identify which composition has the lowest surface energy at the upper bound (Cu-rich) and at the lower bound (Au-rich). Write the results to /app/outputs/surface_energy_analysis.json.
- Output file: `/app/outputs/surface_energy_analysis.json`
- Format: json
- Contract: {"mu_Cu_upper": number (eV, relative to bulk Cu), "mu_Cu_lower": number (eV), "stable_at_upper": string (composition_label), "stable_at_lower": string (composition_label)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_reference.json`
- `/app/outputs/slab_energies.csv`
- `/app/outputs/surface_energy_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_reference.json
- path: `/app/outputs/bulk_reference.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Bulk reference energies and lattice constant used to compute formation energy and chemical potential bounds.
- schema:
  - `type`: object
  - `required`:
    - `E_bulk_Cu`: number (eV/atom)
    - `E_bulk_Au`: number (eV/atom)
    - `E_bulk_Cu3Au`: number (eV/f.u.)
    - `lattice_constant_Cu3Au`: number (angstrom)

### slab_energies.csv
- path: `/app/outputs/slab_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total energies and composition data for all 19 slab stoichiometries, used to recompute surface energies and stability.
- schema:
  - `type`: table
  - `required_columns`: `composition_label`, `total_energy`, `N_Cu`, `N_Au`, `surface_area`
  - `units`:
    - `total_energy`: eV
    - `surface_area`: angstrom^2

### surface_energy_analysis.json
- path: `/app/outputs/surface_energy_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Determined stable surface stoichiometries at the Cu-rich and Au-rich chemical potential endpoints.
- schema:
  - `type`: object
  - `required`:
    - `mu_Cu_upper`: number (eV, relative to bulk Cu)
    - `mu_Cu_lower`: number (eV)
    - `stable_at_upper`: string (composition_label)
    - `stable_at_lower`: string (composition_label)

Notes: No hidden gold values are disclosed here. The checker will recompute formation energy and surface energies from the raw artifacts and confirm the stable compositions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_reference.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "E_bulk_Cu": "number (eV/atom)",
          "E_bulk_Au": "number (eV/atom)",
          "E_bulk_Cu3Au": "number (eV/f.u.)",
          "lattice_constant_Cu3Au": "number (angstrom)"
        }
      },
      "description": "Bulk reference energies and lattice constant used to compute formation energy and chemical potential bounds."
    },
    {
      "file": "slab_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_label",
          "total_energy",
          "N_Cu",
          "N_Au",
          "surface_area"
        ],
        "units": {
          "total_energy": "eV",
          "surface_area": "angstrom^2"
        }
      },
      "description": "Total energies and composition data for all 19 slab stoichiometries, used to recompute surface energies and stability."
    },
    {
      "file": "surface_energy_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "mu_Cu_upper": "number (eV, relative to bulk Cu)",
          "mu_Cu_lower": "number (eV)",
          "stable_at_upper": "string (composition_label)",
          "stable_at_lower": "string (composition_label)"
        }
      },
      "description": "Determined stable surface stoichiometries at the Cu-rich and Au-rich chemical potential endpoints."
    }
  ],
  "notes": "No hidden gold values are disclosed here. The checker will recompute formation energy and surface energies from the raw artifacts and confirm the stable compositions."
}
```

## How you are scored
A hidden verifier checks your outputs against internal reference criteria. For `bulk_reference.json`, it verifies the values are physically plausible and recomputes the formation energy from the provided energies. For `slab_energies.csv`, it validates the format and uses the energies together with the bulk references to recalculate surface energies. For `surface_energy_analysis.json`, it compares your reported stable compositions at the two chemical-potential endpoints to the expected results. Each scored artifact contributes a weight to the final reward; the surface energy analysis is the primary determinant. Simply writing plausible numbers without running the DFT workflow will not yield a high score.
