# Valence shell model phonon calculation for boron nitride structures

## Problem background
Boron nitride nanotubes (BNNTs) are wide‑gap semiconductors with properties that make them attractive for applications ranging from electronics to structural composites. Raman and infrared spectroscopies offer fast, non‑destructive characterization, but the interpretation of spectra requires knowledge of the lattice vibrations. This task addresses the calculation of key phonon properties — zone‑centre optical frequencies of bulk hexagonal boron nitride (h‑BN), the radial breathing mode (RBM) frequency as a function of nanotube radius, and the Raman‑active G‑band frequencies of a (10,10) armchair nanotube — using a valence shell model of the lattice dynamics.

## Approach
The core method is a valence shell model (VSM). Each ion is represented by a point core and a massless spherical shell, coupled by a spring; the shell carries charge to account for electronic polarizability. Long‑range Coulomb interactions are included, and short‑range covalent forces are described by valence force field terms: nearest‑neighbour and next‑to‑nearest‑neighbour bond stretching, in‑plane angle bending, and out‑of‑plane bending. For bulk h‑BN the dynamical matrix is built at the Γ point (in‑phase motions of the two formula units in the cell) and diagonalized to yield the optical phonon frequencies and eigenvectors. For single‑walled BNNTs the screw symmetry of the tube is exploited to work with a two‑atom unit cell; the tube radius and chiral angle are computed from the (n,m) indices assuming a B–N bond length of 1.44 Å and all atoms lying on a single cylindrical surface. The same VSM parameters describe the in‑plane interactions, and the phonon problem at the Γ point is solved for many tubes with radii between 5 and 25 Å. The RBM is identified as the lowest‑frequency fully‑symmetric radial mode. For the armchair (10,10) tube the zone‑centre Raman‑active modes are selected according to the rod‑group symmetry: species A_g, E1g, and E2g. All calculations use the following VSM parameter set, which is treated as a fixed input:

- Ionic charges (e): Z_B = +1.29, Z_N = −1.29
- Shell charges (e): Y_B = +1.90, Y_N = −1.90
- Anisotropic ionic polarizabilities (Å³): α∥ = 0.01, α⊥ = 0.61 (same for B and N)
- Nearest‑neighbour stretch (N/m): α₁(B–N) = 610.8
- Next‑to‑nearest‑neighbour stretch (N/m): α₂(B–B) = 23.6, α₂(N–N) = 2.5
- In‑plane bend (10⁻²⁰ N·m): γ₁(B–N–B) = 29.5, γ₁(N–B–N) = −10.0
- Out‑of‑plane bend (10⁻²⁰ N·m): γ₂ = 14.8 (same for B and N)
- Interlayer B–N repulsion: Born‑Mayer potential V(r) = a exp(−b r) with a = 638 eV and b = 3.18 Å⁻¹.

No further parameter fitting is required. The model assumes straight B–N bonds and neglects bond‑buckling effects, which are expected to have a negligible influence on the computed frequencies.

## Reproduction target
Produce the following three output files:

1. `bulk_hBN_zone_center.json` — the optical phonon frequencies of bulk h‑BN at the Γ point, labelled by their symmetry species: E1u(TO), E1u(LO), E2g symmetric in‑plane, A2u(TO), A2u(LO), B1g anti‑out‑of‑plane, B1g symmetric in‑phase out‑of‑plane, and E2g symmetric in‑phase in‑plane. All values in cm⁻¹.

2. `RBM_frequencies.csv` — a table of RBM frequencies for a representative set of BNNTs (armchair, zigzag, and chiral) whose radii cover the range 5–25 Å. Columns: radius_angstrom (float) and rbm_freq_cm⁻¹ (float).

3. `tube_10_10_raman_active.json` — the zone‑centre Raman‑active phonon frequencies of the armchair (10,10) BNNT. The file must contain at least the keys 'E2g_high' and 'E1_high' for the two prominent G‑band modes (in cm⁻¹). Additional Raman‑active modes may be included. The modes should correspond to the irreducible representations A_g, E1g, E2g of the tube’s rod group.

The computation must rely only on the VSM parameters listed in the Approach and on the standard structural model for BNNTs (B–N bond length 1.44 Å, all atoms on a single cylindrical surface).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute bulk h-BN zone-center optical phonon frequencies
- Role: scored
- Action: Implement a valence shell model for bulk hexagonal boron nitride using the fitted parameters (ionic charges, shell charges, anisotropic polarizabilities, stretch, bend, and Born–Mayer interlayer repulsion) as described in the method. Construct the dynamical matrix at the Γ point and diagonalize to obtain phonon frequencies. Assign the symmetry labels as specified (E1u(TO/LO), E2g, A2u, B1g). Write a JSON file with the computed frequencies.
- Output file: `/app/outputs/bulk_hBN_zone_center.json`
- Format: json
- Contract: {
  "E1u_TO": number (cm⁻¹),
  "E1u_LO": number (cm⁻¹),
  "E2g_symmetric_inplane": number (cm⁻¹),
  "A2u_TO": number (cm⁻¹),
  "A2u_LO": number (cm⁻¹),
  "B1g_anti_outplane": number (cm⁻¹),
  "B1g_sym_inphase_outplane": number (cm⁻¹),
  "E2g_sym_inphase_inplane": number (cm⁻¹)
}
- Scoring: scored by hidden verifier

### Step 2: Compute radial breathing mode frequencies for BNNTs of various radii
- Role: scored (load-bearing)
- Action: For a set of BNNTs covering the radius range 5–25 Å (include armchair, zigzag, and chiral types), construct the VSM model for each tube using the same fitted parameters. Compute the phonon dispersion at the Γ point and extract the radial breathing mode (RBM) frequency. Write a CSV file with columns 'radius_angstrom' and 'rbm_freq_cm⁻¹'.
- Output file: `/app/outputs/RBM_frequencies.csv`
- Format: csv
- Contract: A CSV table with columns radius_angstrom (float) and rbm_freq_cm⁻¹ (float).
- Scoring: scored by hidden verifier

### Step 3: Compute Raman‑active zone‑centre phonon frequencies of (10,10) BNNT
- Role: scored
- Action: Build the VSM for the (10,10) BNNT, compute the dynamical matrix at Γ, diagonalize to obtain phonon frequencies and eigenvectors. Identify the modes that are Raman‑active according to the rod-group symmetry analysis (species A_g, E1g, E2g). Write a JSON object with keys 'E2g_high' and 'E1_high' corresponding to the two prominent G-band frequencies, and optionally other Raman‑active modes.
- Output file: `/app/outputs/tube_10_10_raman_active.json`
- Format: json
- Contract: {
  "E2g_high": number (cm⁻¹),
  "E1_high": number (cm⁻¹)
} (additional keys optional)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_hBN_zone_center.json`
- `/app/outputs/RBM_frequencies.csv`
- `/app/outputs/tube_10_10_raman_active.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_hBN_zone_center.json
- path: `/app/outputs/bulk_hBN_zone_center.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed zone‑centre optical phonon frequencies of bulk h‑BN. Each frequency is compared to a hidden gold value within an absolute tolerance.
- schema:
  - `type`: object
  - `required`: `E1u_TO`, `E1u_LO`, `E2g_symmetric_inplane`, `A2u_TO`, `A2u_LO`, `B1g_anti_outplane`, `B1g_sym_inphase_outplane`, `E2g_sym_inphase_inplane`
  - `units`:
    - `E1u_TO`: cm⁻¹
    - `E1u_LO`: cm⁻¹
    - `E2g_symmetric_inplane`: cm⁻¹
    - `A2u_TO`: cm⁻¹
    - `A2u_LO`: cm⁻¹
    - `B1g_anti_outplane`: cm⁻¹
    - `B1g_sym_inphase_outplane`: cm⁻¹
    - `E2g_sym_inphase_inplane`: cm⁻¹

### RBM_frequencies.csv
- path: `/app/outputs/RBM_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: RBM frequencies for a range of BNNT radii. The checker fits ω = A/R and compares A to the hidden reference coefficient.
- schema:
  - `type`: table
  - `required_columns`: `radius_angstrom`, `rbm_freq_cm⁻¹`
  - `units`:
    - `radius_angstrom`: Å
    - `rbm_freq_cm⁻¹`: cm⁻¹

### tube_10_10_raman_active.json
- path: `/app/outputs/tube_10_10_raman_active.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Raman‑active zone‑centre frequencies of the (10,10) BNNT. Only the two most prominent G‑band modes are required; each is compared to hidden gold within an absolute tolerance.
- schema:
  - `type`: object
  - `required`: `E2g_high`, `E1_high`
  - `units`:
    - `E2g_high`: cm⁻¹
    - `E1_high`: cm⁻¹

Notes: The fitting of VSM parameters to experimental h‑BN data is omitted because the scored targets use the already‑published Table I parameters. The nonresonant Raman intensity calculation is omitted as its bond‑polarizability parameters are not fully specified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_hBN_zone_center.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "E1u_TO",
          "E1u_LO",
          "E2g_symmetric_inplane",
          "A2u_TO",
          "A2u_LO",
          "B1g_anti_outplane",
          "B1g_sym_inphase_outplane",
          "E2g_sym_inphase_inplane"
        ],
        "units": {
          "E1u_TO": "cm⁻¹",
          "E1u_LO": "cm⁻¹",
          "E2g_symmetric_inplane": "cm⁻¹",
          "A2u_TO": "cm⁻¹",
          "A2u_LO": "cm⁻¹",
          "B1g_anti_outplane": "cm⁻¹",
          "B1g_sym_inphase_outplane": "cm⁻¹",
          "E2g_sym_inphase_inplane": "cm⁻¹"
        }
      },
      "description": "Computed zone‑centre optical phonon frequencies of bulk h‑BN. Each frequency is compared to a hidden gold value within an absolute tolerance."
    },
    {
      "file": "RBM_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius_angstrom",
          "rbm_freq_cm⁻¹"
        ],
        "units": {
          "radius_angstrom": "Å",
          "rbm_freq_cm⁻¹": "cm⁻¹"
        }
      },
      "description": "RBM frequencies for a range of BNNT radii. The checker fits ω = A/R and compares A to the hidden reference coefficient."
    },
    {
      "file": "tube_10_10_raman_active.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "E2g_high",
          "E1_high"
        ],
        "units": {
          "E2g_high": "cm⁻¹",
          "E1_high": "cm⁻¹"
        }
      },
      "description": "Raman‑active zone‑centre frequencies of the (10,10) BNNT. Only the two most prominent G‑band modes are required; each is compared to hidden gold within an absolute tolerance."
    }
  ],
  "notes": "The fitting of VSM parameters to experimental h‑BN data is omitted because the scored targets use the already‑published Table I parameters. The nonresonant Raman intensity calculation is omitted as its bond‑polarizability parameters are not fully specified."
}
```

## How you are scored
A hidden verifier evaluates each output file independently and combines the scores into a final reward (a number between 0 and 1).

- `bulk_hBN_zone_center.json`: the verifier compares the computed frequencies to reference optical phonon frequencies of bulk h‑BN, using tolerances that accommodate minor numerical differences.
- `RBM_frequencies.csv`: the verifier fits the data to a power law ω(RBM) = A / R and checks whether the coefficient A agrees with the expected value.
- `tube_10_10_raman_active.json`: the verifier compares the reported Raman‑active frequencies to the known frequencies for the (10,10) tube, again allowing a tolerance that reflects legitimate implementational choices.

The exact weights and tolerance thresholds are defined in the checker and are not disclosed. Submitting physically correct values that are obtained from an honest implementation of the described VSM will yield a high score, while numbers that deviate substantially from the reference will receive a lower score. The verifier does not require any particular code or library; it only examines the content of the output files.
