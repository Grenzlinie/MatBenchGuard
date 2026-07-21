# Reproduction task

## Problem background
Thin layers of amorphous SiOₓ are used as gas barriers on polymer films; their performance depends on porosity. This task concerns a kinetic Monte Carlo model that extends the continuous random network (CRN) method with dangling-bond kinetics to simulate vapour deposition of nonstoichiometric amorphous silica. The goal is to investigate how the porosity of the deposited layer varies with the nucleation-site density (NSD) on the substrate and with the oxygen content x.

## Approach
The model describes amorphous SiOₓ as a network of Si and O atoms with well-defined coordination numbers (Si up to 4, O up to 2; no O–O bonds). The total energy of a configuration is

E = E^{CRN} + N_{Si}^{d}·E_{Si}^{d} + N_{O}^{d}·E_{O}^{d} + U_{rep},

where N^{d} is the number of dangling bonds. The CRN energy is a valence-force field:

E^{CRN} = ½ Σ_i K_r^{αβ} (r_i^{αβ} - r_0^{αβ})² + ½ Σ_{i,j} K_θ^{αβγ} (cos θ_{ij}^{αβγ} - cos θ_0^{αβγ})²,

with sums over bonds and bond angles. Dangling-bond energies are E_{Si}^{d}=1 eV and E_{O}^{d}=4 eV. A short-range repulsion U_{rep} penalises non-bonded atoms that come within second-neighbour distances:

U_{rep} = Σ_{α,β} ∫_{R}^{∞} F_{rep}·exp[−(r / R₀^{αβ})^{20}] dr,

where R is the equilibrium distance between atoms α and β (taken as the bond length a₀^{αβ}) and F_{rep} is a large constant.

Force constants, equilibrium geometries, and repulsion radii are:

| Parameter | Value |
|---|---|
| K_r^{Si–O} | 27.0 eV/Å² |
| K_r^{Si–Si} | 9.08 eV/Å² |
| K_θ^{Si–Si–Si} | 3.58 eV |
| K_θ^{Si–Si–O} | 3.93 eV |
| K_θ^{O–Si–O} | 4.32 eV |
| K_θ^{Si–O–Si} | 0.75 eV |
| r₀^{Si–O} | 1.60 Å |
| r₀^{Si–Si} | 2.35 Å |
| cos θ₀^{Si–O–Si} | −0.8 |
| cos θ₀^{O–Si–O} = cos θ₀^{Si–Si–O} = cos θ₀^{Si–Si–Si} | −0.333 |
| R₀^{Si–O} | 3.12 Å |
| R₀^{Si–Si} | 3.00 Å |
| R₀^{O–O} | 2.54 Å |

The simulation cell has a substrate area of 2.4×2.4 nm² with periodic boundary conditions parallel to the substrate. Nucleation sites (random positions) are each initialised as a surface Si atom. Growth proceeds by repeated deposition of Si or O atoms at randomly chosen dangling bonds of surface atoms, maintaining the target composition. Each arriving atom is delivered to a dangling bond within a surface layer of thickness 10 Å. After each deposition, the system is relaxed by a sequence of MC moves: breaking bonds, forming/annihilating dangling bonds, and migrating dangling bonds. Every move is followed by full energy minimisation with respect to atomic positions, and accepted or rejected via the Metropolis criterion with an effective temperature kT = 0.5 eV for atoms that just arrived and kT = 0.05 eV for all other atoms.

Porosity is measured by superimposing a cubic mesh of side 0.4 Å on the final configuration. An atomic sphere of radius 2.5 Å is placed on every atom; mesh cells that do not overlap any sphere are counted as pore. The pore volume fraction (porosity) and the pore surface-to-volume ratio are computed from this classification.

## Reproduction target
Produce the simulated porosity (relative pore volume) and pore surface-to-volume ratio for two series of conditions:

1. **Fixed composition SiO₁.₈**: vary the nucleation-site density (NSD) over at least three values spanning a range from less than 1 nm⁻² to greater than 4 nm⁻². For each NSD compute porosity and surface-to-volume ratio, and save the results in `porosity_nsd.csv`.
2. **Fixed NSD = 1.74 nm⁻²**: vary the oxygen content x over at least four values from 0 to 2. For each x compute porosity and surface-to-volume ratio, and save the results in `porosity_x.csv`.

## Assets
No external datasets, model files, or pre‑trained weights are required. The entire simulation is implemented from scratch. Use Python (≥ 3.9) with standard numerical libraries: **numpy** and **scipy**. Optional visualisation can use **matplotlib**. All software is open‑source and freely available. No proprietary tools are needed.

## Workflow steps

### Step 1: KMC growth simulation of SiOx films
- Role: process
- Action: Implement a kinetic Monte Carlo simulation of vapour deposition of amorphous SiOx using the algorithm described in the paper. Use the parameters from Table I (force constants, equilibrium geometries, repulsion, dangling-bond energies, effective temperatures). For each required combination of nucleation-site density (NSD) and oxygen composition x, deposit ~3000 atoms on a 2.4×2.4 nm² substrate with randomly placed nucleation sites (initially silicon atoms) and periodic boundary conditions parallel to the substrate. Apply MC moves (bond break, bond formation, dangling-bond migration) with full valence-force energy minimisation and Metropolis acceptance, using effective kT = 0.5 eV for moves involving newly arrived atoms and 0.05 eV for others. Save the final atomic configurations for each run.
- Evidence: none

### Step 2: Porosity vs. nucleation site density (x=1.8)
- Role: scored (load-bearing)
- Action: From the atomic configurations generated at fixed x = 1.8 for several NSD values spanning <1 nm⁻² to >4 nm⁻², compute porosity (relative pore volume) using a cubic mesh of side 0.4 Å and atomic spheres of radius 2.5 Å. Also compute the pore surface-to-volume ratio. Write the results to `/app/outputs/porosity_nsd.csv`.
- Output file: `/app/outputs/porosity_nsd.csv`
- Format: csv
- Contract: One row per simulated NSD. Columns: `nsd_nm2` (float, nucleation site density in nm⁻²), `porosity` (float, dimensionless pore volume fraction), `surface_volume_ratio` (float, in nm⁻¹).
- Scoring: scored by hidden verifier

### Step 3: Porosity vs. oxygen composition x (NSD=1.74 nm⁻²)
- Role: scored (load-bearing)
- Action: From the atomic configurations generated at fixed NSD = 1.74 nm⁻² for several x values at least spanning 0, 0.5, 1.0, 1.5, 2.0, compute porosity and pore surface-to-volume ratio using the same mesh method. Write the results to `/app/outputs/porosity_x.csv`.
- Output file: `/app/outputs/porosity_x.csv`
- Format: csv
- Contract: One row per simulated x. Columns: `x` (float, oxygen composition), `porosity` (float), `surface_volume_ratio` (float, in nm⁻¹).
- Scoring: scored by hidden verifier

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### porosity_nsd.csv
- path: `/app/outputs/porosity_nsd.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Porosity and surface-to-volume ratio vs nucleation site density at fixed x=1.8
- schema:
  - `columns`: `nsd_nm2`, `porosity`, `surface_volume_ratio`
  - `dtypes`:
    - `nsd_nm2`: float
    - `porosity`: float
    - `surface_volume_ratio`: float

### porosity_x.csv
- path: `/app/outputs/porosity_x.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Porosity and surface-to-volume ratio vs oxygen composition at fixed NSD=1.74 nm⁻²
- schema:
  - `columns`: `x`, `porosity`, `surface_volume_ratio`
  - `dtypes`:
    - `x`: float
    - `porosity`: float
    - `surface_volume_ratio`: float

Notes: Both CSV files are scored by a hidden verifier that checks monotonic trends and absolute magnitude bounds without rerunning the simulation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "porosity_nsd.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "columns": [
          "nsd_nm2",
          "porosity",
          "surface_volume_ratio"
        ],
        "dtypes": {
          "nsd_nm2": "float",
          "porosity": "float",
          "surface_volume_ratio": "float"
        }
      },
      "description": "Porosity and surface-to-volume ratio vs nucleation site density at fixed x=1.8"
    },
    {
      "file": "porosity_x.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "columns": [
          "x",
          "porosity",
          "surface_volume_ratio"
        ],
        "dtypes": {
          "x": "float",
          "porosity": "float",
          "surface_volume_ratio": "float"
        }
      },
      "description": "Porosity and surface-to-volume ratio vs oxygen composition at fixed NSD=1.74 nm⁻²"
    }
  ],
  "notes": "Both CSV files are scored by a hidden verifier that checks monotonic trends and absolute magnitude bounds without rerunning the simulation."
}
```

## How you are scored
A hidden verifier will independently score your two output CSV files. The verifier checks that the porosity exhibits the physically expected monotonic trends and that the absolute porosity values fall within physically plausible ranges for a correct simulation. The surface‑to‑volume ratio trend is used as a secondary check (strictly increasing with NSD, and positive for all composition values). The final reward is a weighted combination of the scores for the two artifacts, with partial credit possible if only the monotonic trends are satisfied. The exact scoring thresholds and tolerances are not disclosed; the only reliable way to obtain a high score is to implement the model faithfully as described.