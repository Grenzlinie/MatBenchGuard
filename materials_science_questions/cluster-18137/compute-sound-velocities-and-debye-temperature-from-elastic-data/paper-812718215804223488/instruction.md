# Compute Acoustic Phonon Properties and Lattice Thermal Conductivity for Type-I Si/Ge Clathrates

## Problem background
Type‑I clathrates (Si₄₆ and Ge₄₆) have a cage‑like host framework that can encapsulate alkali (Na, K) or alkaline‑earth (Ba) guest atoms. Filling the cages introduces rattling modes, modifies the phonon dispersion, and leads to glass‑like low lattice thermal conductivity, making these materials candidates for thermoelectric applications. The interplay between guest atoms and the host lattice changes the acoustic phonon group velocities, the Grüneisen parameter (a measure of anharmonicity), the Debye temperatures, and ultimately the lattice thermal conductivity. This task computes those changes for the seven stable clathrate compositions: empty Si₄₆ and Ge₄₆, and their Na‑, K‑, and Ba‑filled variants, including cases where spontaneous framework vacancies appear (K₈Ge₄₄□₂ and Ba₈Ge₄₃□₃).

## Approach
The workflow uses first‑principles density functional theory (DFT) with the PBEsol functional, followed by harmonic and quasi‑harmonic phonon calculations.

1. **Structure relaxation** – Fully relax the lattice vectors and atomic positions of each of the seven clathrate systems until forces are small.
2. **Harmonic phonon dispersions** – Compute the phonon band structure in the harmonic approximation (e.g., with `phonopy`) by constructing force constants from finite displacements of a supercell. This yields eigenfrequencies along a high‑symmetry path through the Brillouin zone.
3. **Group velocities** – Numerically differentiate the phonon frequencies to obtain mode‑resolved group velocities, then extract the average group velocities of the transverse acoustic (TA) and longitudinal acoustic (LA) branches (v_TA, v_LA).
4. **Grüneisen parameters** – Apply volume strains to the relaxed cells and recompute the harmonic phonon dispersions (quasi‑harmonic approximation). From the frequency shifts, derive mode‑resolved Grüneisen parameters and branch‑averaged γ_TA, γ_LA as well as the temperature‑averaged Grüneisen parameter at 300 K.
5. **Debye temperatures and sound velocity** – From the phonon dispersions, identify the maximum acoustic frequencies at the Brillouin‑zone boundary. Convert these to per‑branch Debye temperatures (θ_TA, θ_LA) and compute the average Debye temperature θ_D using the average sound velocity v_s, which itself is obtained from v_TA, v_LA, the unit‑cell volume, and the number of atoms.
6. **Lattice thermal conductivity** – Using the Debye–Callaway formalism with the Asen–Palmer modification, model the normal and Umklapp scattering lifetimes from the computed group velocities, Grüneisen parameters, Debye temperatures, and the average atomic mass and cell volume. Integrate to obtain the lattice thermal conductivity κ_l at 300 K for each system.
7. **Spectral width change** – From the harmonic phonon dispersions, determine the minimum and maximum frequencies to compute the phonon spectral width for each system. For every filled clathrate, calculate the percentage reduction in spectral width relative to its corresponding empty host (Si₄₆ or Ge₄₆).

The results are compiled into two structured JSON files that are evaluated by the hidden verifier.

## Reproduction target
Compute the acoustic phonon properties and lattice thermal conductivity for the seven clathrate systems (Si₄₆, Na₈Si₄₆, K₈Si₄₆, Ba₈Si₄₆, Ge₄₆, K₈Ge₄₄□₂, Ba₈Ge₄₃□₃) and report them in two JSON files under `/app/outputs`:

1. `table1_results.json` – For each system, provide the average Grüneisen parameter at 300 K (`avg_gamma`), the branch‑averaged Grüneisen parameters (`gamma_TA`, `gamma_LA`), the group velocities of the TA and LA branches (`v_TA`, `v_LA`), the average sound velocity (`v_s`), the per‑branch Debye temperatures (`theta_TA`, `theta_LA`), the average Debye temperature (`theta_D`), and the lattice thermal conductivity κ_l at 300 K (`kappa_l`). Units: group velocities in km s⁻¹, temperatures in K, thermal conductivity in W m⁻¹ K⁻¹.

2. `spectral_width_report.json` – For the empty hosts Si₄₆ and Ge₄₆, report the spectral width (maximum – minimum frequency). For each filled system, report the percentage reduction of its spectral width relative to the corresponding empty host.

## Assets

- FHI-aims: https://aimsclub.fhi-berlin.mpg.de/
- phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Perform DFT geometry relaxation for the seven clathrate compositions: Si46, Na8Si46, K8Si46, Ba8Si46, Ge46, K8Ge44□2, and Ba8Ge43□3. Use PBEsol functional and relax atomic positions and lattice vectors until forces are below 0.001 eV/Å.
- Evidence: `/app/outputs/relaxed_structures.log`

### Step 2: Harmonic phonon dispersions
- Role: process
- Action: Compute harmonic phonon band structures for each relaxed system using the harmonic approximation (e.g., with phonopy) on supercells. Obtain eigenfrequencies along a suitable high-symmetry path covering the Brillouin zone.
- Evidence: `/app/outputs/phonon_bands.hdf5`

### Step 3: Group velocities
- Role: process
- Action: Compute mode-resolved phonon group velocities by numerical differentiation of the harmonic frequencies. Extract average group velocities for the transverse acoustic (TA) and longitudinal acoustic (LA) branches (v_TA, v_LA) for each system.
- Evidence: `/app/outputs/group_velocities.json`

### Step 4: Grüneisen parameters
- Role: process
- Action: Perform quasi-harmonic phonon calculations by applying volume strain to the relaxed cells. Calculate mode-resolved Grüneisen parameters. Derive the average Grüneisen parameter at 300 K and branch-averaged γ_TA, γ_LA for each system.
- Evidence: `/app/outputs/gruneisen.json`

### Step 5: Debye temperatures and sound velocity
- Role: process
- Action: From the phonon dispersions, extract maximum acoustic frequencies at the Brillouin-zone boundary for TA and LA modes. Compute per-mode Debye temperatures (θ_TA, θ_LA) and the average Debye temperature θ_D from the average sound velocity v_s. Compute v_s from v_TA, v_LA, unit-cell volume, and number of atoms.
- Evidence: `/app/outputs/debye_temperatures.json`

### Step 6: Table of acoustic properties and lattice thermal conductivity
- Role: scored (load-bearing)
- Action: Using the computed group velocities, Grüneisen parameters, Debye temperatures, average atomic mass, and unit-cell volume, calculate the lattice thermal conductivity κ_l at 300 K for each system via the Debye–Callaway model with Asen-Palmer modification. Compile the results together with the average Grüneisen parameter, branch-resolved Grüneisen parameters, group velocities, sound velocity, and Debye temperatures into a structured JSON file.
- Output file: `/app/outputs/table1_results.json`
- Format: json
- Contract: {"Si46": {"avg_gamma": <float>, "gamma_TA": <float>, "gamma_LA": <float>, "v_TA": <float>, "v_LA": <float>, "v_s": <float>, "theta_TA": <float>, "theta_LA": <float>, "theta_D": <float>, "kappa_l": <float>}, ...}
- Scoring: scored by hidden verifier

### Step 7: Phonon spectral width reduction
- Role: scored
- Action: From the phonon dispersions, determine the minimum and maximum frequencies to compute the phonon spectrum width for each system. For each filled system, calculate the percentage reduction in spectrum width relative to the corresponding empty host (Si46 or Ge46). Report the reference widths for the empty hosts as well.
- Output file: `/app/outputs/spectral_width_report.json`
- Format: json
- Contract: {"Si46": {"spectral_width": <float>}, "Ge46": {"spectral_width": <float>}, "Na8Si46": {"reduction_percent": <float>}, "K8Si46": {"reduction_percent": <float>}, "Ba8Si46": {"reduction_percent": <float>}, "K8Ge44□2": {"reduction_percent": <float>}, "Ba8Ge43□3": {"reduction_percent": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1_results.json`
- `/app/outputs/spectral_width_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1_results.json
- path: `/app/outputs/table1_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduced acoustic phonon properties and lattice thermal conductivity for all seven clathrate systems, corresponding to the quantities in the paper's Table 1.
- schema:
  - `type`: object
  - `required`:
    - `Si46`: object
    - `Na8Si46`: object
    - `K8Si46`: object
    - `Ba8Si46`: object
    - `Ge46`: object
    - `K8Ge44□2`: object
    - `Ba8Ge43□3`: object
  - `items`:
    - `avg_gamma`: float
    - `gamma_TA`: float
    - `gamma_LA`: float
    - `v_TA`: float
    - `v_LA`: float
    - `v_s`: float
    - `theta_TA`: float
    - `theta_LA`: float
    - `theta_D`: float
    - `kappa_l`: float
  - `units`:
    - `v_TA`: km/s
    - `v_LA`: km/s
    - `v_s`: km/s
    - `theta_TA`: K
    - `theta_LA`: K
    - `theta_D`: K
    - `kappa_l`: W/mK

### spectral_width_report.json
- path: `/app/outputs/spectral_width_report.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon spectrum widths for empty hosts and the filling-induced percentage reductions for filled systems.
- schema:
  - `type`: object
  - `required`:
    - `Si46`: object
    - `Ge46`: object
    - `Na8Si46`: object
    - `K8Si46`: object
    - `Ba8Si46`: object
    - `K8Ge44□2`: object
    - `Ba8Ge43□3`: object
  - `items`:
    - `spectral_width`: float
    - `reduction_percent`: float

Notes: All quantities are computed for the seven systems at 300 K where applicable. The checker scores table1_results.json by comparing the reported values to hidden paper-derived references within appropriate per-quantity tolerances. The spectral_width_report.json is scored by verifying that the reduction percentages fall within the physically expected ranges (Si-based: ~20–40%, Ge-based: ~5–15%) and that the empty-host widths are plausible.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Si46": "object",
          "Na8Si46": "object",
          "K8Si46": "object",
          "Ba8Si46": "object",
          "Ge46": "object",
          "K8Ge44□2": "object",
          "Ba8Ge43□3": "object"
        },
        "items": {
          "avg_gamma": "float",
          "gamma_TA": "float",
          "gamma_LA": "float",
          "v_TA": "float",
          "v_LA": "float",
          "v_s": "float",
          "theta_TA": "float",
          "theta_LA": "float",
          "theta_D": "float",
          "kappa_l": "float"
        },
        "units": {
          "v_TA": "km/s",
          "v_LA": "km/s",
          "v_s": "km/s",
          "theta_TA": "K",
          "theta_LA": "K",
          "theta_D": "K",
          "kappa_l": "W/mK"
        }
      },
      "description": "Reproduced acoustic phonon properties and lattice thermal conductivity for all seven clathrate systems, corresponding to the quantities in the paper's Table 1."
    },
    {
      "file": "spectral_width_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Si46": "object",
          "Ge46": "object",
          "Na8Si46": "object",
          "K8Si46": "object",
          "Ba8Si46": "object",
          "K8Ge44□2": "object",
          "Ba8Ge43□3": "object"
        },
        "items": {
          "spectral_width": "float",
          "reduction_percent": "float"
        }
      },
      "description": "Phonon spectrum widths for empty hosts and the filling-induced percentage reductions for filled systems."
    }
  ],
  "notes": "All quantities are computed for the seven systems at 300 K where applicable. The checker scores table1_results.json by comparing the reported values to hidden paper-derived references within appropriate per-quantity tolerances. The spectral_width_report.json is scored by verifying that the reduction percentages fall within the physically expected ranges (Si-based: ~20–40%, Ge-based: ~5–15%) and that the empty-host widths are plausible."
}
```

## How you are scored
A hidden verifier will independently read your output files and check them against reference criteria. Each scored artifact carries a weight, and the final reward is a weighted combination of the scores. Merely reporting numbers that match some expected values is not sufficient; the verifier assesses whether your computed quantities are physically plausible, consistent with the protocol, and meet the structural and quantitative requirements defined in the output contract. The evaluation is fully automatic and based solely on the files you submit under `/app/outputs`.
