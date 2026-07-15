# Quasiharmonic phonon analysis of thermal expansion in CdSe nanoplatelets

## Problem background
Cadmium selenide (CdSe) nanoplatelets are quasi‑two‑dimensional semiconductor nanocrystals that can exhibit pronounced negative thermal expansion (NTE) — a counterintuitive shrinking in the in‑plane direction as temperature rises. Understanding the magnitude and temperature range of this negative expansion as a function of nanoplatelet thickness is important for temperature‑dependent optical applications and for validating first‑principles predictions. In bulk CdSe, the thermodynamically stable phase is wurtzite, but the material may also crystallise in a metastable zinc‑blende structure. Both phases display a modest negative CTE at low temperatures. This task measures the in‑plane coefficient of linear thermal expansion (CTE) for F‑terminated CdSe nanoplatelets of different thicknesses and for bulk CdSe, using density‑functional theory (DFT) within the quasiharmonic approximation (QHA).

## Approach
The reproduction follows a DFT‑based quasiharmonic workflow. The free energy of a crystal unit cell is written as a sum of the total DFT energy and the vibrational free energy of a system of harmonic oscillators whose frequencies depend on the strain state. The key steps are: (i) relax the bulk structures (zinc‑blende and wurtzite) to obtain equilibrium lattice parameters; (ii) compute mechanical stresses for a set of isotropic (zinc‑blende) or isotropic‑plus‑axial (wurtzite) strains and fit the strain as a quadratic function of stress; (iii) perform density‑functional perturbation theory (DFPT) phonon calculations for a few strained configurations on a coarse q‑mesh, interpolate the phonon frequencies to a fine mesh, and compute the vibrational free energy \(F_\text{vib}(T,u)\); (iv) for each temperature, solve the stress‑free condition \(\partial F/\partial u = 0\) to obtain the equilibrium strain; (v) differentiate strain with respect to temperature to obtain the linear CTE. For nanoplatelets, [001]‑oriented zinc‑blende slab supercells of thickness 2, 3, 4, and 5 monolayers (ML) are built, with both surfaces terminated by fluorine atoms and a 20 Å vacuum gap. Biaxial in‑plane strains are applied, and the same QHA procedure yields the in‑plane CTE. This workflow requires the ABINIT DFT code and LDA norm‑conserving pseudopotentials for Cd, Se, and F.

## Reproduction target
Compute the linear coefficient of thermal expansion (CTE) as a function of temperature for the following systems:
- bulk CdSe in the zinc‑blende structure
- bulk CdSe in the wurtzite structure (both along the \(a\) and \(c\) axes)
- F‑terminated CdSe nanoplatelets of thickness 2 ML, 3 ML, 4 ML, and 5 ML.

The temperature range is 5 K to 1000 K. Output a CSV file (`/app/outputs/cte_curves.csv`) that gives the CTE (in units of K⁻¹) for each structure at the temperatures 50 K, 100 K, 200 K, 300 K, 400 K, 500 K, 600 K, 700 K, 800 K, 900 K, and 1000 K. The structure identifiers in the CSV must be exactly: `zb`, `wurtzite_a`, `wurtzite_c`, `2ML`, `3ML`, `4ML`, `5ML`.

## Assets

- ABINIT (density-functional theory code): https://www.abinit.org/downloads
- LDA norm-conserving pseudopotentials (RRKJ) for Cd, Se, F: https://www.abinit.org/psp-tables

## Workflow steps

### Step 1: Relax bulk zinc-blende CdSe
- Role: process
- Action: Optimise the geometry of bulk zinc-blende CdSe to obtain the equilibrium lattice constant a0.
- Evidence: `/app/outputs/zb_lattice.json`

### Step 2: Stress–strain relation for zinc-blende CdSe
- Role: process
- Action: Compute mechanical stress σ_xx for isotropic strains from −0.01 to 0.01 and fit u_xx ≈ c1 σ_xx + c2 σ_xx².
- Evidence: `/app/outputs/zb_stress_fit.json`

### Step 3: Phonon calculations for zinc-blende CdSe
- Role: process
- Action: Perform DFPT phonon calculations for isotropic strains u_xx = −0.01, 0, 0.01 on a coarse q‑mesh and interpolate to a fine mesh; save interpolated phonon frequencies.
- Evidence: `/app/outputs/zb_phonon_data.npz`

### Step 4: Relax bulk wurtzite CdSe
- Role: process
- Action: Optimise the geometry of bulk wurtzite CdSe to obtain equilibrium lattice constants a0, c0 and the internal z parameter.
- Evidence: `/app/outputs/wz_lattice.json`

### Step 5: Stress–strain relation for wurtzite CdSe
- Role: process
- Action: For 13 strain pairs (u_xx, u_zz) compute σ_xx and σ_zz, optimise internal z at each strain, and fit u_xx, u_zz as quadratic functions of stress.
- Evidence: `/app/outputs/wz_stress_fit.json`

### Step 6: Phonon calculations for wurtzite CdSe
- Role: process
- Action: Calculate phonon frequencies for the same 13 strain pairs using DFPT on a coarse mesh and interpolate to a fine mesh.
- Evidence: `/app/outputs/wz_phonon_data.npz`

### Step 7: Build nanoplatelet models
- Role: process
- Action: Construct [001]-oriented zinc-blende nanoplatelet supercells with thicknesses 2, 3, 4, 5 monolayers terminated by F atoms, including a 20 Å vacuum gap.
- Evidence: `/app/outputs/npl_structures.json`

### Step 8: DFT calculations for strained nanoplatelets
- Role: process
- Action: For each nanoplatelet model, relax atomic positions at biaxial in‑plane strains u_xx = 0, ±0.01, ±0.02, compute σ_xx, and calculate phonon frequencies on a coarse q‑mesh; interpolate to a fine mesh.
- Evidence: `/app/outputs/npl_data.npz`

### Step 9: Quasiharmonic analysis and CTE output
- Role: scored (load-bearing)
- Action: For all structures, compute vibrational free energy F_vib(T,u) from interpolated phonons, solve for equilibrium strain at each temperature, differentiate to obtain linear CTE, and write the CSV file.
- Output file: `/app/outputs/cte_curves.csv`
- Format: csv
- Contract: columns: structure (str), temperature_K (float), cte_K_minus1 (float). structure ∈ {zb, wurtzite_a, wurtzite_c, 2ML, 3ML, 4ML, 5ML}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cte_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cte_curves.csv
- path: `/app/outputs/cte_curves.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Coefficient of linear thermal expansion for CdSe bulk and nanoplatelets. Checked against hidden reference curves; relative error must not exceed a hidden tolerance and the ordering at 300 K must be correct.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `temperature_K`, `cte_K_minus1`
  - `units`:
    - `temperature_K`: K
    - `cte_K_minus1`: K⁻¹
  - `expected_structures`: `zb`, `wurtzite_a`, `wurtzite_c`, `2ML`, `3ML`, `4ML`, `5ML`
  - `expected_temperatures`: `50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `1000`

Notes: The solver must recompute CTE from first principles; no gold values are provided. The verifier uses a hidden table of reference CTE values extracted from the paper's figures to check accuracy and the required monotonic trend at 300 K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cte_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "temperature_K",
          "cte_K_minus1"
        ],
        "units": {
          "temperature_K": "K",
          "cte_K_minus1": "K⁻¹"
        },
        "expected_structures": [
          "zb",
          "wurtzite_a",
          "wurtzite_c",
          "2ML",
          "3ML",
          "4ML",
          "5ML"
        ],
        "expected_temperatures": [
          50,
          100,
          200,
          300,
          400,
          500,
          600,
          700,
          800,
          900,
          1000
        ]
      },
      "description": "Coefficient of linear thermal expansion for CdSe bulk and nanoplatelets. Checked against hidden reference curves; relative error must not exceed a hidden tolerance and the ordering at 300 K must be correct."
    }
  ],
  "notes": "The solver must recompute CTE from first principles; no gold values are provided. The verifier uses a hidden table of reference CTE values extracted from the paper's figures to check accuracy and the required monotonic trend at 300 K."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/cte_curves.csv` and compares your computed CTE values against reference curves (extracted from the computational study that first reported these results). The verifier checks two things: (1) the numerical accuracy of the CTE at all required temperatures for every structure, using a relative‑error metric that allows for the spread expected when the same theoretical framework is implemented with different computational parameters; (2) a structural trend — that at 300 K the CTE ordering across nanoplatelet thicknesses follows \(2\text{ML} < 3\text{ML} < 4\text{ML} < 5\text{ML}\). The final score is a weighted combination of these checks, reported as a number between 0 and 1. The tolerances and exact gold values are hidden; only a genuine first‑principles computation that faithfully executes the required steps can satisfy the verifier.
