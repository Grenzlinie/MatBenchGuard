# Site-resolved vacancy binding and Li segregation energies at Cu grain boundaries

## Problem background
Liquid lithium is a candidate material for fusion devices, but its compatibility with polycrystalline copper is poor, leading to liquid metal embrittlement (LME). Atomistic simulations suggest that LME susceptibility depends strongly on the structure of grain boundaries (GBs). Key energetic quantities that control the embrittlement are (a) the vacancy binding energy, which indicates how strongly Cu vacancies are bound to a GB site, and (b) the Li segregation energy, which measures the energetic preference for Li atoms to occupy GB sites instead of bulk Cu. This task computes these site-resolved energies for three common symmetrical tilt grain boundaries in Cu: Σ3(111), Σ3(112) and Σ5(310), enabling an investigation of how GB type affects the energetic driving force for embrittlement.

## Approach
We adopt a compute-driven approach using classical molecular statics with the Modified Analytic Embedded-Atom Method (MAEAM) interatomic potential for Cu-Li. First, construct the three symmetrical tilt GB models using the coincident site lattice method with the experimental Cu lattice constant (3.615 Å). Relax each GB via energy minimization. Next, compute bulk reference energies: the cohesive energy per atom of perfect Cu, the vacancy formation energy in bulk Cu, and the energy difference for substituting a Li atom into bulk Cu. These bulk references are needed to convert raw defect energies into binding and segregation energies. Finally, for each relaxed GB model, systematically remove Cu atoms (to create vacancies) or substitute Li atoms at atomic sites across several planes near the GB. After each perturbation, relax the configuration and compute the vacancy binding energy and Li segregation energy using the standard defect formation energy formalism. Output site-resolved energies as functions of distance from the GB plane for each GB type.

## Reproduction target
Produce two site-resolved datasets in CSV format:
1. `vacancy_binding_energies.csv` – columns: GB_type, site_index, distance_from_GB_plane (Å), vacancy_binding_energy (eV). For each GB type (Sigma3(111), Sigma3(112), Sigma5(310)), include at least 5 sites covering positions on the GB plane, the first few adjacent planes, and a bulk-like region.
2. `li_segregation_energies.csv` – same columns but with li_segregation_energy (eV). Use the same site indices as in the vacancy file.
The energies should be computed from fully relaxed configurations. The target is to reproduce the correct physical behavior: within a few Å of the GB, the energies should reflect the GB's influence; as distance increases, they should approach the bulk limit (zero for binding energy). The relative behavior across the three GB types is the primary focus.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/
- MAEAM interatomic potential for Cu-Li: 10.1007/s11051-015-3275-4

## Workflow steps

### Step 1: Construct and relax Cu STGB models
- Role: process
- Action: Construct Σ3(111), Σ3(112) and Σ5(310) symmetrical tilt grain boundaries using the coincident site lattice method with Cu lattice constant 3.615 Å. Relax each GB via energy minimization with the MAEAM potential. Record the relaxed atomic configurations and compute the GB energies.
- Evidence: `/app/outputs/gb_models.data`

### Step 2: Compute bulk reference energies
- Role: process
- Action: Using the MAEAM potential, compute the cohesive energy per atom of perfect Cu, the vacancy formation energy in bulk Cu, and the energy difference for substituting a Li atom into bulk Cu. These bulk references are needed for converting raw defect energies into formation/binding/segregation energies.
- Evidence: `/app/outputs/bulk_energies.csv`

### Step 3: Compute vacancy binding energies
- Role: scored (load-bearing)
- Action: For each relaxed GB model, identify atomic sites within a few planes of the GB. For each site, create a Cu vacancy, perform energy minimization, and compute the vacancy formation energy using Ef^α = E_GB^α - E_GB + E_coh. Then compute the vacancy binding energy Eb^α = Ef^α - Ef^0. Output the results ordered by site and distance from the GB plane.
- Output file: `/app/outputs/vacancy_binding_energies.csv`
- Format: csv
- Contract: Columns: GB_type (string, one of 'Sigma3(111)', 'Sigma3(112)', 'Sigma5(310)'), site_index (int), distance_from_GB_plane (float, Å), vacancy_binding_energy (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Compute Li segregation energies
- Role: scored (load-bearing)
- Action: Using the same set of sites as in the vacancy binding step, substitute a Li atom for a Cu atom at each site, perform energy minimization, and compute the Li segregation energy Eseg^α = (E_GB,Li^α - E_GB) - (E_B,Li^0 - E_B^0). Write the results similarly.
- Output file: `/app/outputs/li_segregation_energies.csv`
- Format: csv
- Contract: Columns: GB_type (string), site_index (int), distance_from_GB_plane (float, Å), li_segregation_energy (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_binding_energies.csv`
- `/app/outputs/li_segregation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_binding_energies.csv
- path: `/app/outputs/vacancy_binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Site-resolved Cu vacancy binding energies; the checker recomputes site-level agreement against hidden reference values and verifies the sign pattern (negative near Σ3(112)/Σ5(310), near-zero for Σ3(111)).
- schema:
  - `type`: table
  - `required_columns`: `GB_type`, `site_index`, `distance_from_GB_plane`, `vacancy_binding_energy`
  - `units`:
    - `distance_from_GB_plane`: Å
    - `vacancy_binding_energy`: eV

### li_segregation_energies.csv
- path: `/app/outputs/li_segregation_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Site-resolved Li segregation energies; the checker recomputes site-level agreement and verifies the sign pattern (negative near Σ3(112)/Σ5(310), near-zero for Σ3(111)).
- schema:
  - `type`: table
  - `required_columns`: `GB_type`, `site_index`, `distance_from_GB_plane`, `li_segregation_energy`
  - `units`:
    - `distance_from_GB_plane`: Å
    - `li_segregation_energy`: eV

Notes: The full solid-liquid MD simulation (3 ns) is omitted; only the site-resolved energy calculations are reproduced. The checker compares the computed binding/segregation energies against hidden reference values with appropriate tolerances and checks qualitative sign patterns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "GB_type",
          "site_index",
          "distance_from_GB_plane",
          "vacancy_binding_energy"
        ],
        "units": {
          "distance_from_GB_plane": "Å",
          "vacancy_binding_energy": "eV"
        }
      },
      "description": "Site-resolved Cu vacancy binding energies; the checker recomputes site-level agreement against hidden reference values and verifies the sign pattern (negative near Σ3(112)/Σ5(310), near-zero for Σ3(111))."
    },
    {
      "file": "li_segregation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "GB_type",
          "site_index",
          "distance_from_GB_plane",
          "li_segregation_energy"
        ],
        "units": {
          "distance_from_GB_plane": "Å",
          "li_segregation_energy": "eV"
        }
      },
      "description": "Site-resolved Li segregation energies; the checker recomputes site-level agreement and verifies the sign pattern (negative near Σ3(112)/Σ5(310), near-zero for Σ3(111))."
    }
  ],
  "notes": "The full solid-liquid MD simulation (3 ns) is omitted; only the site-resolved energy calculations are reproduced. The checker compares the computed binding/segregation energies against hidden reference values with appropriate tolerances and checks qualitative sign patterns."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's output artifact. For the two scored artifacts (vacancy binding energies and Li segregation energies), the verifier compares your computed site-resolved energies against hidden reference values derived from the original study. It checks:
- That the energies approach the expected bulk limit at large distances.
- That the sign and approximate magnitude at near-GB sites follow the correct pattern.
- That the relative ordering among the three GB types is consistent with the underlying physics.
The verifier combines the per-artifact scores (with the larger weight on the two scored CSV files) into a final reward between 0 and 1. Simply reporting the paper's numerical values is not sufficient; the verifier expects a physically meaningful output that results from correctly performing the energy minimizations and applying the defect energy formulas.
