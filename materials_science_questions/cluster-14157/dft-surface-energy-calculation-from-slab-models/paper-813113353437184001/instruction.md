# DFT Formation and Segregation Energies of M-Sn Bimetallic Surfaces

## Problem background
The catalytic conversion of biomass-derived succinic acid to 1,4-butanediol in aqueous phase relies on bimetallic catalysts such as Ru‑Sn on activated carbon. During continuous operation, leaching of Ni from stainless‑steel reactor walls can restructure the catalyst, forming unwanted Ni‑Sn sites that degrade performance. To evaluate this deactivation pathway, the thermodynamic driving force for Sn incorporation into Ru, Ni, and Pt close‑packed surfaces must be quantified. This task reproduces the key surface formation and subsurface‑to‑surface segregation energies of Sn in these metals, providing a computational basis for comparing bimetallic stability.

## Approach
Periodic density functional theory (DFT) calculations with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and the Tkatchenko–Scheffler van der Waals correction are used to model M(0001)/M(111) surfaces (M = Ru, Ni, Pt). Slab models are built with a vacuum region and dipole corrections; the bottom two atomic layers are fixed at bulk‑optimized positions, while the top three layers (including the surface layer) are allowed to relax. The calculations are performed in an open‑source DFT code (Quantum ESPRESSO, CP2K, or GPAW) with standard PBE pseudopotentials; the procedure scopes to any modern implementation that yields equivalent physical quantities.

### Definitions of the computed energies
All energies are reported per Sn atom.

#### Average surface formation energy, ΔE_f
For a slab containing 𝑁_Sn Sn atoms substituting surface metal atoms,
```
ΔE_f = [ E_tot(M-Sn slab) - E_tot(clean M slab) + N_Sn·(μ_M - μ_Sn) ] / N_Sn ,
```
where
- E_tot(M-Sn slab) is the total energy of the relaxed slab with Sn atoms,
- E_tot(clean M slab) is the total energy of the relaxed clean slab of the same size,
- μ_M = E_tot(bulk M) / (number of atoms in the bulk unit cell),
- μ_Sn = E_tot(bulk Sn) / (number of atoms in the bulk unit cell).

The bulk references are obtained from fully relaxed unit cells of the following ground‑state structures:
- Ru: hexagonal close-packed (hcp),
- Ni: face-centered cubic (fcc),
- Pt: face-centered cubic (fcc),
- Sn: α‑Sn (diamond structure).

**Important:** both the clean slab and the M-Sn slab must be relaxed under identical DFT settings. The Sn coverage (fraction of surface atoms replaced) is denoted in monolayers (ML), where 1 ML corresponds to one Sn atom per surface metal atom. For the 4×4 supercells used here (16 surface atoms per layer), the coverages 0.25, 0.50, and 0.75 ML correspond to 4, 8, and 12 Sn atoms, respectively.

#### Average subsurface‑to‑surface segregation energy, ΔE_seg
For each (metal, coverage) combination, the segregation energy is
```
ΔE_seg = [ E_tot(Sn@surface) - E_tot(Sn@subsurface) ] / N_Sn ,
```
where
- E_tot(Sn@surface) is the total energy of the lowest‑energy M-Sn slab chosen for the formation energy (Sn atoms reside in the top surface layer),
- E_tot(Sn@subsurface) is the total energy of the slab obtained by moving **all** Sn atoms from the top layer to the subsurface layer (immediately below the surface) while keeping their in‑plane fractional coordinates identical; the original surface sites are filled back with M atoms. This subsurface configuration is then relaxed under the same DFT settings (top three layers free, bottom two fixed).

A negative ΔE_seg means the Sn‑in‑surface configuration is energetically more favorable than Sn‑in‑subsurface (i.e., segregation to the surface is thermodynamically preferred).

### Choice of Sn arrangements (crucial for reproducibility)
The calculated energies depend on the arrangement of Sn atoms on the surface. To obtain results that match the reference (paper Figure 7), follow this protocol for **each metal** and **each coverage**:

1. Generate all symmetry‑inequivalent distributions of N_Sn Sn atoms on the 4×4 surface layer (16 sites). Use the surface periodic lattice symmetry. If full enumeration is not feasible, at least produce candidate configurations that cover different nearest‑neighbor Sn–Sn distances and different degrees of clustering.
2. For each candidate configuration, perform a DFT relaxation (top three layers free, bottom two fixed; all other parameters as in Section “Workflow steps”).
3. Select the configuration with the **lowest total energy** as the ground state for that (metal, coverage) pair.
4. Use this lowest‑energy configuration to compute ΔE_f and, later, ΔE_seg (by moving the same Sn atoms to the subsurface layer as described).

If more than one configuration yields essentially the same energy (within 5 meV/atom), any of them may be used; the resulting ΔE_f and ΔE_seg are expected to coincide with the reference values.

## Reproduction target
Produce two CSV files: `formation_energies.csv` and `segregation_energies.csv`. Each file must contain one row for every combination of metal (Ru, Ni, Pt) and coverage (0.25, 0.50, 0.75 ML). Columns: `metal` (string), `coverage_ML` (float), and the respective energy (float, in eV per Sn atom). The values must be computed by the DFT protocol described in the workflow steps. The primary goal is to obtain the numerical energies along with their relative trends across metals and coverages, which together reflect the thermodynamic driving forces for bimetallic surface formation and Sn segregation.

## Assets

- DFT code (Quantum ESPRESSO, CP2K, or GPAW): Open‑source DFT codes capable of periodic slab calculations with PBE functional and TS‑vdW correction. Available at: Quantum ESPRESSO (https://www.quantum‑espresso.org/), CP2K (https://www.cp2k.org/), GPAW (https://wiki.fysik.dtu.dk/gpaw/).
- PBE pseudopotentials for Ru, Ni, Pt, Sn: Available from SSSP library (https://www.materialscloud.org/discover/sssp/) or equivalent PAW/NC pseudopotentials at PBE level. The agent should select pseudopotentials appropriate for the chosen DFT code.
- Bulk crystal structures of Ru, Ni, Pt, and α‑Sn: Public databases: Materials Project (https://next‑gen.materialsproject.org/) or Crystallography Open Database (http://www.crystallography.net/). The agent should relax the bulk lattice parameters with the same DFT functional before building slabs.

## Workflow steps

### Step 1: Compute surface formation energies
- Role: scored (load-bearing)
- Action: Perform periodic DFT calculations for the close‑packed surfaces of Ru(0001), Ni(111), and Pt(111) with Sn atoms substituting surface metal atoms. Use the PBE exchange‑correlation functional with the Tkatchenko–Scheffler van der Waals correction. Build a 5‑layer 4×4 slab (16 atoms per layer), fix the bottom two layers, allow the top three layers to relax, add 30 Å vacuum, use an energy cutoff ≥400 eV and a 5×5×1 k‑mesh with dipole corrections. For each metal, consider Sn coverages of 0.25, 0.50, and 0.75 ML (i.e., 4, 8, and 12 Sn atoms, respectively). **For each coverage, follow the configuration‑selection protocol described in "Choice of Sn arrangements" to obtain the lowest‑energy Sn arrangement.** Compute the average formation energy per Sn atom, ΔE_f, using the formula given in Section “Approach”. Write the results to formation_energies.csv with columns metal, coverage_ML, delta_E_f_eV_per_Sn.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: metal (string: Ru, Ni, Pt), coverage_ML (float: 0.25, 0.5, 0.75), delta_E_f_eV_per_Sn (float, energy in eV per Sn atom). One row per (metal, coverage) combination.
- Scoring: scored by hidden verifier

### Step 2: Compute subsurface‑to‑surface segregation energies
- Role: scored (load-bearing)
- Action: Using the same DFT slab settings (PBE+TS‑vdW, 5‑layer 4×4 slab, top three layers relaxed, bottom two fixed, 30 Å vacuum, cutoff ≥400 eV, 5×5×1 k‑mesh, dipole corrections), compute the average subsurface‑to‑surface segregation energy per Sn atom, ΔE_seg, for M = Ru, Ni, Pt at Sn coverages of 0.25, 0.5, 0.75 ML. For each (metal, coverage) pair, take the lowest‑energy surface configuration identified in Step 1. Construct the corresponding subsurface configuration by moving **all** Sn atoms from the top layer to the subsurface layer (same in‑plane fractional coordinates) and filling the vacated surface sites with M atoms. Relax this subsurface slab (same relaxation constraints) and compute its total energy. Calculate ΔE_seg according to the formula in Section “Approach”. Write the results to segregation_energies.csv with columns metal, coverage_ML, delta_E_seg_eV_per_Sn.
- Output file: `/app/outputs/segregation_energies.csv`
- Format: csv
- Contract: CSV with columns: metal (string: Ru, Ni, Pt), coverage_ML (float: 0.25, 0.5, 0.75), delta_E_seg_eV_per_Sn (float, energy in eV per Sn atom). One row per (metal, coverage) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/segregation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average formation energy per Sn atom for M‑Sn surfaces (M=Ru,Ni,Pt) at coverages 0.25, 0.5, 0.75 ML.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `coverage_ML`, `delta_E_f_eV_per_Sn`
  - `column_types`:
    - `metal`: string
    - `coverage_ML`: float
    - `delta_E_f_eV_per_Sn`: float

### segregation_energies.csv
- path: `/app/outputs/segregation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average subsurface‑to‑surface segregation energy per Sn atom for M‑Sn surfaces (M=Ru,Ni,Pt) at coverages 0.25, 0.5, 0.75 ML.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `coverage_ML`, `delta_E_seg_eV_per_Sn`
  - `column_types`:
    - `metal`: string
    - `coverage_ML`: float
    - `delta_E_seg_eV_per_Sn`: float

Notes: The checker compares the reported energies to hidden reference values extracted from Figure 7 of the source paper. Tolerances absorb systematic differences between DFT codes and pseudopotentials while still requiring the correct relative ordering between metals.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "coverage_ML",
          "delta_E_f_eV_per_Sn"
        ],
        "column_types": {
          "metal": "string",
          "coverage_ML": "float",
          "delta_E_f_eV_per_Sn": "float"
        }
      },
      "description": "Average formation energy per Sn atom for M‑Sn surfaces (M=Ru,Ni,Pt) at coverages 0.25, 0.5, 0.75 ML."
    },
    {
      "file": "segregation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "coverage_ML",
          "delta_E_seg_eV_per_Sn"
        ],
        "column_types": {
          "metal": "string",
          "coverage_ML": "float",
          "delta_E_seg_eV_per_Sn": "float"
        }
      },
      "description": "Average subsurface‑to‑surface segregation energy per Sn atom for M‑Sn surfaces (M=Ru,Ni,Pt) at coverages 0.25, 0.5, 0.75 ML."
    }
  ],
  "notes": "The checker compares the reported energies to hidden reference values extracted from Figure 7 of the source paper. Tolerances absorb systematic differences between DFT codes and pseudopotentials while still requiring the correct relative ordering between metals."
}
```

## How you are scored
A hidden verifier independently scores each of the two output CSV files. It compares the submitted formation and segregation energies to hidden reference values derived from the same computational protocol, using tolerances that absorb legitimate differences between DFT codes and pseudopotentials while preserving the correct physical trends. The verifier rewards solutions that reproduce the expected relative ordering among metals (e.g., formation energy trend) and approximate magnitude windows. The scores from both artifacts are combined by weight to produce a final reward between 0 and 1. The workflow must be genuinely executed; fabricating or guessing the numbers without proper DFT calculations will not match the hidden reference within the required accuracy.