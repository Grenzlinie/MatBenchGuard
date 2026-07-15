# Elastic moduli and Debye temperature of metallic glasses from phonon dispersion

## Problem background
Metallic glasses exhibit unique elastic and thermodynamic properties that can be understood through their vibrational dynamics. In particular, the low-momentum phonon dispersion relations determine the material's sound velocities, elastic constants, and Debye temperature. The sensitivity of the longitudinal phonon frequencies to the treatment of conduction-electron screening makes it possible to study how different dielectric models influence the predicted elastic moduli and Debye temperature for a set of binary and ternary metallic glasses. This task asks you to compute Young's modulus, bulk modulus, shear modulus, and Debye temperature for four representative metallic glasses under several common dielectric screening prescriptions, using a force-constant model originally proposed by Bhatia and Singh.

## Approach
The central theoretical framework is a spherical-force model in which nearest-neighbour central forces (parameterised by force constants β and δ) and a volume-dependent force from the conduction electrons (parameterised by κₑ) determine the phonon frequencies. The longitudinal dispersion ω_L(q) includes an explicit dependence on the dielectric screening function ε(q) through a shape-factor term; the transverse dispersion ω_T(q) is screening-independent. By fitting the force constants to the experimental or literature low‑q sound velocities for one reference screening, you can generate the full ω_L(q) curves for five additional dielectric screenings: Hartree (H), Hubbard (HB), Overhauser (OH), Geldart–Vosko (GV), and self-consistent screening (SCS). From the slopes of these curves at q → 0 you extract the corresponding longitudinal and transverse sound velocities, which then enter the isotropic elastic relations for C₁₁, C₄₄, C₁₂, Young's modulus E, bulk modulus B, shear modulus G, and the Debye temperature Θ_D. The entire pipeline is deterministic and can be implemented in Python with standard numerical libraries.

## Reproduction target
Your task is to compute a single CSV table that contains the elastic moduli E, B, G (in units of 10¹⁰ N/m²) and the Debye temperature Θ_D (in K) for four metallic glasses — Ca₇₀Mg₃₀, Mg₇₀Zn₃₀, Cu₅₇Zr₄₃, and Pd₇₇.₅Si₁₆.₅Cu₆ — each under six dielectric screening models: ABB‑RNS, Hartree, Hubbard, Overhauser, Geldart‑Vosko, and self‑consistent screening. For the ABB‑RNS screening you may use the sound velocities directly from the literature; for the other five screenings you must compute the phonon dispersion curves, extract the sound velocities from the low‑q slopes, and then calculate the moduli and Debye temperature. The output file must be written as elastic_moduli_table.csv under /app/outputs and contain exactly 24 rows (4 glasses × 6 screenings) with columns: Glass, Screening, E, B, G, Theta_D.

## Assets

- numpy: numpy
- scipy: scipy
- Hafner (1983) Phys. Rev. B 27, 678: 10.1103/PhysRevB.27.678
- Vitek (1983) in Amorphous Materials, AIME, p. 217
- Kobayashi & Takeuchi (1980) J. Phys. C 13, L969: 10.1088/0022-3719/13/34/004
- Golding et al (1972) Phys. Rev. Lett. 29, 68: 10.1103/PhysRevLett.29.68

## Workflow steps

### Step 1: Collect literature input parameters
- Role: process
- Action: From the specified literature references, obtain the limiting sound velocities V_L(0) and V_T(0), ion density n_i (or mass density rho), mean atomic mass M, mean valence z, coordination number N, and the structure type (FCC or HCP) for each of the four metallic glasses: Ca70Mg30, Mg70Zn30, Cu57Zr43, Pd77.5Si16.5Cu6.
- Evidence: `/app/outputs/literature_parameters.json`

### Step 2: Compute auxiliary quantities a and kappa_e
- Role: process
- Action: For each glass, compute nearest‑neighbour distance a from ion density using the structure‑dependent relation (FCC: n_i a^3 = sqrt(2); HCP: n_i a^3 = (4/√3)(c/a) with appropriate c/a ratio). Compute the conduction‑electron force constant kappa_e = 4 pi n_i^2 z^2 e^2 / K_TF^2, where K_TF^2 = 4 k_F / (pi a_0) with k_F = (3 pi^2 n_i z)^{1/3} and a_0 the Bohr radius.
- Evidence: `/app/outputs/aux_parameters.json`

### Step 3: Determine force constants beta and delta
- Role: process
- Action: Using the literature sound velocities V_L(0), V_T(0), mass density rho, coordination number N, and the computed kappa_e, solve the linear system rho V_L^2(0) = N (beta/3 + delta/5) + kappa_e, rho V_T^2(0) = N (beta/3 + delta/15) to obtain beta and delta for each glass.
- Evidence: `/app/outputs/force_constants.json`

### Step 4: Generate phonon dispersion curves for non‑ABB‑RNS screenings
- Role: process
- Action: For each glass, using the fitted beta, delta, a, rho, and kappa_e, compute the longitudinal phonon frequency omega_L(q) for the five dielectric screenings Hartree (H), Hubbard (HB), Overhauser (OH), Geldart–Vosko (GV), and self‑consistent screening (SCS) via the Bhatia–Singh formula that includes the shape factor and the screening‑specific dielectric function. Also compute the screening‑independent transverse frequency omega_T(q). Perform this over a dense q‑range near zero.
- Evidence: `/app/outputs/dispersion_curves.npz`

### Step 5: Extract sound velocities from dispersion slopes
- Role: process
- Action: For each glass and each of the five screenings, determine the longitudinal sound velocity V_L by fitting the low‑q slope of the corresponding omega_L(q) curve; obtain the transverse sound velocity V_T from the slope of the omega_T(q) curve.
- Evidence: `/app/outputs/sound_velocities.json`

### Step 6: Compute elastic moduli and Debye temperature for all screenings
- Role: scored (load-bearing)
- Action: For each glass and each screening (ABB‑RNS, H, HB, OH, GV, SCS), use the appropriate sound velocities: for ABB‑RNS, take V_L and V_T directly from the literature values collected in step 1; for the other five, use the V_L and V_T extracted from dispersion. From the sound velocities and mass density rho compute C11 = rho V_L^2, C44 = rho V_T^2, and set C12 = C11 − 2 C44 (isotropy). Then compute Young's modulus E = (C11−C12)(C11+2C12)/(C11+C12), bulk modulus B = (C11+2C12)/3, shear modulus G = 3EB/(9B−E), and Debye temperature Theta_D = (h/kB) (9 n_i/(4 pi))^{1/3} (1/V_L^3 + 1/V_T^3)^{-1/3}. Output a single CSV file elastic_moduli_table.csv with columns: Glass, Screening, E (in 10^10 N/m^2), B (in 10^10 N/m^2), G (in 10^10 N/m^2), Theta_D (K). The file must contain exactly 24 rows (4 glasses × 6 screenings).
- Output file: `/app/outputs/elastic_moduli_table.csv`
- Format: csv
- Contract: Glass: string, Screening: string, E: float, B: float, G: float, Theta_D: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_moduli_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli_table.csv
- path: `/app/outputs/elastic_moduli_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed elastic moduli (E, B, G) and Debye temperature (Theta_D) for four metallic glasses under six dielectric screening models. The checker will compare each numeric entry to hidden reference values with relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Glass`, `Screening`, `E`, `B`, `G`, `Theta_D`
  - `units`:
    - `E`: 10^10 N/m^2
    - `B`: 10^10 N/m^2
    - `G`: 10^10 N/m^2
    - `Theta_D`: K

Notes: The output must contain exactly 24 rows (4 glasses × 6 screenings). The screenings are: ABB‑RNS, H, HB, OH, GV, SCS. The glasses are: Ca70Mg30, Mg70Zn30, Cu57Zr43, Pd77.5Si16.5Cu6. Columns Glass and Screening are strings; E, B, G, Theta_D are floating-point numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_moduli_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Glass",
          "Screening",
          "E",
          "B",
          "G",
          "Theta_D"
        ],
        "units": {
          "E": "10^10 N/m^2",
          "B": "10^10 N/m^2",
          "G": "10^10 N/m^2",
          "Theta_D": "K"
        }
      },
      "description": "Computed elastic moduli (E, B, G) and Debye temperature (Theta_D) for four metallic glasses under six dielectric screening models. The checker will compare each numeric entry to hidden reference values with relative tolerance."
    }
  ],
  "notes": "The output must contain exactly 24 rows (4 glasses × 6 screenings). The screenings are: ABB‑RNS, H, HB, OH, GV, SCS. The glasses are: Ca70Mg30, Mg70Zn30, Cu57Zr43, Pd77.5Si16.5Cu6. Columns Glass and Screening are strings; E, B, G, Theta_D are floating-point numbers."
}
```

## How you are scored
A hidden verifier will examine your elastic_moduli_table.csv. It will first confirm that the file has the required structure (columns, 24 non‑duplicate rows). It will then compare each of the 96 numeric values (E, B, G, Θ_D) to a hidden reference derived from the literature. A partial credit scheme is applied: you earn reward proportional to the number of correctly reproduced entries. The verifier does not simply check that you have printed the expected numbers; it assumes that you have genuinely executed the pipeline because the required quantities depend on the proper implementation of the dielectric screening functions, the force‑constant fitting, and the low‑q slope extraction. Your total reward combines the structural checks and the numeric comparisons, with the final CSV carrying the dominant weight.
