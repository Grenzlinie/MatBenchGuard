# Compute Elastic Moduli and Debye Temperature for Metallic Glasses using Bhatia-Singh Force-Constant Model

## Problem background
Metallic glasses are amorphous metallic alloys that exhibit high strength, elasticity, and corrosion resistance, making them attractive for numerous engineering applications. Their mechanical and thermal behaviour is strongly influenced by the vibrational dynamics of the atoms. A simple yet effective way to model the low‑energy vibrations is the Bhatia–Singh force‑constant model, which assumes a central force between nearest neighbours and a volume‑dependent force. In metallic glasses, the conduction electrons screen the ionic interactions, and the choice of the dielectric screening function significantly affects the computed phonon dispersion curves and, consequently, the derived elastic constants and Debye temperature.

In this task, we use the Bhatia–Singh model to compute the elastic moduli—Young’s modulus (E), bulk modulus (B), shear modulus (G)—and the Debye temperature (Θ_D) for four specific metallic glasses: Ca₇₀Mg₃₀, Mg₇₀Zn₃₀, Cu₅₇Zr₄₃, and Pd₇₇.₅Si₁₆.₅Cu₆. The investigation focuses on five different dielectric screening functions that describe the electron‑ion interaction: Hartree (H), Hubbard (HB), Overhauser (OH), Geldart–Vosko (GV), and self‑consistent screening (SCS). The objective is to determine how the choice of screening influences the computed material properties.

## Approach
The Bhatia–Singh model describes the phonon frequencies ω_L(q) (longitudinal) and ω_T(q) (transverse) in terms of two force constants β and δ, the ion density n_i, the mass density ρ, the nearest‑neighbour distance a, and a conduction‑electron contribution that involves the Thomas‑Fermi wave‑vector K_TF and the dielectric screening function ε(q). In the long‑wavelength limit (q → 0), the model yields the longitudinal and transverse sound velocities V_L(0) and V_T(0), from which the three elastic constants C₁₁, C₄₄, and C₁₂ (via the isotropic condition C₁₂ = C₁₁ − 2C₄₄) and the engineering moduli E, B, G are obtained through standard isotropic elasticity relations. The Debye temperature Θ_D follows from the two sound velocities and the ion density.

To use the model, one must first determine the underlying physical parameters for each glass. The task provides the results for a baseline screening (referred to as ABB‑RNS), which are used to calibrate the model. By inverting the relations between the elastic moduli, sound velocities, and densities, we can recover consistent values of the longitudinal sound velocity V_L(0), transverse sound velocity V_T(0), ion density n_i, and mass density ρ for each glass. The given ABB‑RNS values are:

| Glass          | E (10¹⁰ N/m²) | B (10¹⁰ N/m²) | G (10¹⁰ N/m²) | Θ_D (K) |
|----------------|---------------|---------------|---------------|---------|
| Ca₇₀Mg₃₀       | 1.90          | 2.40          | 0.69          | 261.87  |
| Mg₇₀Zn₃₀      | 6.01          | 8.25          | 2.17          | 351.11  |
| Cu₅₇Zr₄₃      | 5.79          | 5.81          | 2.17          | 339.26  |
| Pd₇₇.₅Si₁₆.₅Cu₆| 9.60         | 18.30         | 3.39          | 312.05  |

With these values, the force constants β and δ are obtained from the low‑q relations, and the electron‑ion force constant κ_e is computed from the Thomas‑Fermi model (using the mean valence z and the corresponding ion and electron densities).

Once the physical parameters and force constants are fixed, the sound velocities for the five dielectric screenings are evaluated. For each screening, the longitudinal sound velocity V_L(0) is extracted from the slope of the longitudinal dispersion curve ω_L(q) in the q → 0 limit, where the dispersion relation contains the corresponding dielectric function. The transverse sound velocity V_T(0) is independent of the screening and is computed directly from the force constants. From V_L(0) and V_T(0), the elastic constants and then E, B, G are calculated. Finally, the Debye temperature Θ_D is computed using the isotropic formula that combines the two sound velocities and the ion density.

## Reproduction target
Compute the elastic moduli E (Young’s modulus), B (bulk modulus), G (shear modulus), and the Debye temperature Θ_D for each of the four metallic glasses (Ca₇₀Mg₃₀, Mg₇₀Zn₃₀, Cu₅₇Zr₄₃, Pd₇₇.₅Si₁₆.₅Cu₆) under the five dielectric screenings: H (Hartree), HB (Hubbard), OH (Overhauser), GV (Geldart‑Vosko), and SCS (self‑consistent). The results must be written to the CSV file `/app/outputs/elastic_moduli.csv` with the following columns:

- `glass`: one of Ca70Mg30, Mg70Zn30, Cu57Zr43, Pd77.5Si16.5Cu6
- `screening`: one of H, HB, OH, GV, SCS
- `E`: Young’s modulus in units of 10¹⁰ N/m² (float)
- `B`: bulk modulus in units of 10¹⁰ N/m² (float)
- `G`: shear modulus in units of 10¹⁰ N/m² (float)
- `Theta_D`: Debye temperature in K (float)

The file must contain exactly 20 rows (one for each glass–screening combination) and no other columns. The values must be computed from the model using the derived physical parameters and the force constants as described.

## Assets

- Python scientific libraries (numpy, scipy, pandas): numpy scipy pandas

## Workflow steps

### Step 1: Derive input parameters from ABB-RNS results
- Role: process
- Action: For each metallic glass (Ca70Mg30, Mg70Zn30, Cu57Zr43, Pd77.5Si16.5Cu6), use the ABB-RNS column values (Young's modulus E, bulk modulus B, shear modulus G, Debye temperature Theta_D) from the paper's Table I to invert the model's low-q sound velocity relations and the Debye temperature formula, recovering the consistent set of physical input parameters: longitudinal sound velocity V_L0, transverse sound velocity V_T0, ion density n_i, mass density rho, and mean atomic mass M.
- Evidence: `/app/outputs/derived_parameters.json`

### Step 2: Compute auxiliary constants
- Role: process
- Action: Using the derived ion density n_i and mean atomic mass M, compute the nearest-neighbour distance a (using FCC or HCP packing relations as appropriate), the Wigner-Seitz radius r_s, the Thomas-Fermi wave number K_TF, and the conduction-electron force constant kappa_e according to the standard formulas described in the theory.
- Evidence: `/app/outputs/aux_constants.json`

### Step 3: Determine force constants beta and delta
- Role: process
- Action: For each glass, substitute the values of rho, V_L0, V_T0, and kappa_e into the low-q expressions relating sound velocities to force constants beta and delta, and solve the resulting two linear equations to obtain beta and delta.
- Evidence: `/app/outputs/force_constants.json`

### Step 4: Compute elastic moduli and Debye temperature for five dielectric screenings
- Role: scored (load-bearing)
- Action: For each glass, apply the five explicitly defined dielectric screenings (Hartree, Hubbard, Overhauser, Geldart-Vosko, self-consistent screening). Compute the longitudinal sound velocity V_L from the low-q limit of the longitudinal dispersion relation with the corresponding screening function, and the transverse sound velocity V_T from the screening-independent transverse expression. From V_L and V_T calculate the elastic constants C11, C44, C12, then the engineering moduli E, B, G (via standard isotropic elasticity relations), and finally the Debye temperature Theta_D. Write all results for all (glass, screening) combinations to /app/outputs/elastic_moduli.csv.
- Output file: `/app/outputs/elastic_moduli.csv`
- Format: csv
- Contract: CSV with columns: glass (text, one of Ca70Mg30, Mg70Zn30, Cu57Zr43, Pd77.5Si16.5Cu6), screening (text, one of H, HB, OH, GV, SCS), E (float, Young's modulus in 10^10 N/m^2), B (float, bulk modulus in 10^10 N/m^2), G (float, shear modulus in 10^10 N/m^2), Theta_D (float, Debye temperature in K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli.csv
- path: `/app/outputs/elastic_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The agent's computed elastic moduli (Young's modulus, bulk modulus, shear modulus) and Debye temperature for each metallic glass and each non-ABB-RNS dielectric screening, scored by comparing to the paper's Table I gold values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `glass`, `screening`, `E`, `B`, `G`, `Theta_D`
  - `units`:
    - `E`: 10^10 N/m^2
    - `B`: 10^10 N/m^2
    - `G`: 10^10 N/m^2
    - `Theta_D`: K
  - `notes`: glass and screening are categorical strings; all numeric columns are floating-point numbers in the units specified.

Notes: Only the five screening functions defined explicitly in the paper (H, HB, OH, GV, SCS) are scored. The ABB-RNS column is used internally to derive inputs but not scored. All numeric values must be in the same units as the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "glass",
          "screening",
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
        },
        "notes": "glass and screening are categorical strings; all numeric columns are floating-point numbers in the units specified."
      },
      "description": "The agent's computed elastic moduli (Young's modulus, bulk modulus, shear modulus) and Debye temperature for each metallic glass and each non-ABB-RNS dielectric screening, scored by comparing to the paper's Table I gold values within tolerance."
    }
  ],
  "notes": "Only the five screening functions defined explicitly in the paper (H, HB, OH, GV, SCS) are scored. The ABB-RNS column is used internally to derive inputs but not scored. All numeric values must be in the same units as the paper."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `/app/outputs/elastic_moduli.csv`. The verifier checks that the file exists, has the correct columns and exactly 20 rows, and that all numeric values are present and non‑empty. The main scoring compares your computed values for E, B, G, and Θ_D against reference values derived from the source publication. Comparison uses modest numerical tolerances designed to absorb legitimate variations arising from the implementation (e.g., numerical integration, floating‑point differences). The scoring function rewards closeness: values that fall within the tolerance window receive full credit, and deviations beyond the tolerance are penalised progressively, so a more accurate reproduction yields a higher score. Providing numbers without executing the required computational procedure is not sufficient to earn credit. Only the five non‑ABB‑RNS screenings are scored; the ABB‑RNS values you used as input are not part of the evaluation.
