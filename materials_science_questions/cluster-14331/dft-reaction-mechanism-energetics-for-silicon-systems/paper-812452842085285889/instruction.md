# Quantum-Chemical Energetics of SiF4 Desorption from SiO2 Surfaces

## Problem background
The wet etching of silicon dioxide (SiO2) films in hydrogen fluoride (HF) solutions is a critical step in semiconductor manufacturing, yet the atomic-scale mechanism by which SiF4 molecules detach from the surface remains incompletely understood. Previous kinetic studies suggested that the reaction is driven by nucleophilic attack of HF2⁻ ions on surface silicon atoms and electrophilic attack of H⁺ ions on oxygen atoms, but quantum-chemical evidence for a complete desorption pathway was lacking. The target of this reproduction is to compute, using semi-empirical quantum chemistry, the energetic and structural changes during SiF4 desorption from a model SiO2 surface and thereby quantify the activation barrier and dissociative steps that characterise the process.

## Approach
The core method is the extended Hückel molecular orbital (EHMO) approximation, a semi-empirical quantum-chemical technique that captures covalent bonding trends with low computational cost. The approach constructs a finite cluster model (HO)₃Si–O–SiF₃ to represent the F-terminated SiO2 surface under attack. Using Slater-type atomic orbitals and standard Coulomb integrals for H, O, F, and Si, the Hamiltonian and overlap matrices are built and diagonalised to obtain molecular orbital energies and total electronic energy.  
The following atomic parameters and Slater exponents must be used (ξ denotes the Slater exponent, H_μμ the diagonal Coulomb integrals in eV):

| atom | n  | ξ_s   | H_ss (eV) | ξ_p   | H_pp (eV) |
|------|----|-------|-----------|-------|------------|
| H    | 1  | 1.3   | -13.6     | —     | —          |
| O    | 2  | 2.275 | -32.3     | 2.275 | -14.8      |
| F    | 2  | 2.425 | -40.0     | 2.425 | -18.1      |
| Si   | 3  | 1.383 | -17.3     | 1.383 | -9.2       |

The off-diagonal Hamiltonian matrix elements follow the weighted Wolfsberg–Helmholtz formula:  
`H_μν = (K/2) (H_μμ + H_νν) S_μν` with `K = 1.75`.  
Overlap integrals `S_μν` must be evaluated analytically from the Slater-type orbitals.

The reaction is explored through a series of constrained geometry scans:

1. **Isolated SiF4 molecule** – scan the Si–F bond length to locate the equilibrium distance that minimises the total electronic energy. This distance will be used subsequently as the equilibrium Si–F bond length in the surface cluster.
2. **Linear HF2⁻ ion** – compute the total electronic energy on a two‑dimensional grid of the two H–F distances to map the potential energy surface for the dissociation HF2⁻ → F⁻ + HF and locate the saddle point.
3. **Desorption without H⁺ attack** – build the (HO)₃SiOSiF₃ cluster (with the equilibrium Si–F bond length found in step 1) and scan a grid of the O–Si distance `r(O–Si)` and the attacking F⁻ distance `r(Si–F⁻)`, relaxing the O–Si–F angle at each point to minimise the energy. The H⁺ ion is kept at infinite distance.
4. **Desorption with H⁺ attack** – repeat the same scan as step 3 but now place the attacking H⁺ ion at a fixed distance `r(O–H⁺) = 0.92 Å` from the back‑bond oxygen. This is the primary surface from which the desorption activation energy is extracted.
5. **Analysis** – extract the key numerical quantities from the raw grids and compile a summary report, and construct angular/population trends along the minimum‑energy path.

Mulliken atomic bond populations are used to monitor the strength of the Si–O back bond.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement the extended Hückel method
- **Role:** process
- **Action:** Write a reusable function that, given a set of nuclear coordinates (element labels and positions in Å), builds the Hamiltonian and overlap matrices using the Slater‑type parameters and the formula above, solves the generalised eigenvalue problem `H C = ε S C` (e.g. with `scipy.linalg.eigh`), and returns the total electronic energy (sum of occupied eigenvalues) and, optionally, the Mulliken bond populations.
- The function must be able to treat any number of atoms and must compute all non‑zero overlap integrals analytically.

### Step 2: SiF4 binding energy scan
- **Role:** scored
- **Action:** Construct an isolated SiF4 molecule with ideal tetrahedral geometry. Scan the Si–F bond length over a dense grid covering the vicinity of the expected minimum (e.g. 1.4–1.9 Å). For each distance compute the total electronic energy. Save the results.
- **Output file:** `/app/outputs/sif4_binding_curve.csv`
- **Format:** csv
- **Contract:** Two columns: `r_Si_F` (Å, float), `total_energy` (eV, float). The grid must be dense enough to resolve the minimum.

### Step 3: HF2⁻ dissociation potential energy surface
- **Role:** scored
- **Action:** Build the linear HF2⁻ ion. Compute the total electronic energy on a two‑dimensional grid of the two H–F distances `r(FH–F⁻)` and `r(F⁻–HF)`. The grid must cover the symmetric saddle region and the asymmetric dissociation valleys (suggested range: each distance 0.8–2.5 Å, grid spacing ≤ 0.05 Å).
- **Output file:** `/app/outputs/hf2_dissociation_surface.csv`
- **Format:** csv
- **Contract:** Three columns: `r_FH_Fminus` (Å, float), `r_Fminus_HF` (Å, float), `total_energy` (eV, float). Resolution must be sufficient to reliably locate a saddle point.

### Step 4: Desorption energy surface without H⁺ attack
- **Role:** scored
- **Action:** Construct the (HO)₃SiOSiF₃ cluster. The cluster geometry uses the following **fixed** internal coordinates:
  - `R(Si–O) = 1.601 Å` (for the O–Si back bond in the initial geometry),
  - `R(O–H) = 0.92 Å` (for the terminal OH groups, if any),
  - `∠O–Si–O = 109.47°`, `∠Si–O–Si = 180.0°`.
  - **Si–F bond length:** use the equilibrium distance obtained from Step 2.
- With the H⁺ ion held at infinite distance, perform a grid scan over the two coordinates:
  - `r(O–Si)` — the O–Si back‑bond distance, varied from 1.601 Å to 2.651 Å,
  - `r(Si–F⁻)` — the distance between the Si atom and the attacking F⁻ ion, varied from the equilibrium Si–F distance (from Step 2) to 3.035 Å.
- At each grid point, relax the O–Si–F bond angle to minimise the total electronic energy (a simple angular energy optimisation is sufficient). Record the final total energy, the optimised O–Si–F angle, and the Mulliken Si–O bond population.
- **Output file:** `/app/outputs/desorption_energy_surface_without_Hplus.csv`
- **Format:** csv
- **Contract:** Columns: `r_O_Si` (Å, float), `r_Si_Fminus` (Å, float), `total_energy` (eV, float), `optimized_O_Si_F_angle` (deg, float), `Si_O_bond_population` (float, dimensionless).

### Step 5: Desorption energy surface with H⁺ attack
- **Role:** scored (load‑bearing)
- **Action:** Repeat the same cluster setup and grid scan as in Step 4, but now place the attacking hydrogen ion at a fixed distance `r(O–H⁺) = 0.92 Å` from the back‑bond oxygen. The H⁺ position must be aligned appropriately (approximately perpendicular to the Si–O bond, as reasoned from frontier‑orbital arguments). Again, relax the O–Si–F angle at every grid point and record total energy, optimised angle, and Si–O bond population.
- **Output file:** `/app/outputs/desorption_energy_surface_with_Hplus.csv`
- **Format:** csv
- **Contract:** Same columns as Step 4.

### Step 6: Activation energy report
- **Role:** scored
- **Action:** Analyse the raw energy surfaces produced in Steps 2, 3 and 5:
  - From the SiF4 binding curve, determine the equilibrium Si–F bond length (minimum energy).
  - On the HF2⁻ surface, locate the saddle point (defined as the energy maximum along the symmetric line `r1 ≈ r2` and a minimum in the perpendicular direction) and compute the dissociation barrier relative to the lowest dissociation valley.
  - On the desorption surface with H⁺, find the minimum‑energy path from the initial basin (smallest `r(O–Si)`, largest `r(Si–F⁻)`) to the final basin (largest `r(O–Si)`, smallest `r(Si–F⁻)`) and identify the transition state. Compute the desorption activation energy as the energy difference between the transition state and the initial minimum.
- Compile the extracted values into a JSON report. All numeric values must be recorded as floats.
- **Output file:** `/app/outputs/activation_energy_report.json`
- **Format:** json
- **Contract:** A JSON object with exactly these keys (use `0.0` as a placeholder in the schema below, you must fill in your computed values):

```json
{
  "sif4_equilibrium_bond_length": 0.0,
  "hf2_dissociation_barrier": 0.0,
  "hf2_saddle_r": 0.0,
  "siF4_desorption_activation_energy": 0.0,
  "transition_state_r_O_Si": 0.0,
  "transition_state_r_Si_Fminus": 0.0,
  "angle_range": [0.0, 0.0],
  "bond_population_range": [0.0, 0.0]
}
```

- `angle_range` is a list of two floats: [minimum O–Si–F angle, maximum O–Si–F angle] (degrees) observed on the H⁺‑attacked surface.
- `bond_population_range` is a list of two floats: [maximum Si–O bond population, minimum Si–O bond population] (dimensionless) on the same surface.

### Step 7: Angle and bond population trend along reaction coordinate
- **Role:** scored
- **Action:** From the desorption energy surfaces (Steps 4 and 5), extract the minimum‑energy path. Project the optimised O–Si–F angle and the Si–O Mulliken bond population onto the reaction coordinate `rc = r(O–Si) – r(Si–F⁻)`. Write a table containing the trend for both the `with_Hplus` and `without_Hplus` cases.
- **Output file:** `/app/outputs/angle_population_trend.csv`
- **Format:** csv
- **Contract:** Columns: `case` (string, `'with_Hplus'` or `'without_Hplus'`), `reaction_coordinate_rc` (Å, float), `optimized_O_Si_F_angle` (deg, float), `Si_O_bond_population` (float, dimensionless). Rows sorted by `rc`.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sif4_binding_curve.csv`
- `/app/outputs/hf2_dissociation_surface.csv`
- `/app/outputs/desorption_energy_surface_without_Hplus.csv`
- `/app/outputs/desorption_energy_surface_with_Hplus.csv`
- `/app/outputs/activation_energy_report.json`
- `/app/outputs/angle_population_trend.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sif4_binding_curve.csv
- **path:** `/app/outputs/sif4_binding_curve.csv`
- **format:** csv
- **purpose:** scored
- **target_policy:** metric_recompute
- **description:** Computed total electronic energy of an isolated SiF4 molecule as a function of the Si–F bond length. The checker extracts the equilibrium bond length from this curve.
- **schema:**
  - `type`: table
  - `required_columns`: `r_Si_F`, `total_energy`
  - `units`:
    - `r_Si_F`: Å
    - `total_energy`: eV

### hf2_dissociation_surface.csv
- **path:** `/app/outputs/hf2_dissociation_surface.csv`
- **format:** csv
- **purpose:** scored
- **target_policy:** metric_recompute
- **description:** Potential energy surface for HF2⁻ dissociation. The checker locates the saddle point and computes the dissociation barrier.
- **schema:**
  - `type`: table
  - `required_columns`: `r_FH_Fminus`, `r_Fminus_HF`, `total_energy`
  - `units`:
    - `r_FH_Fminus`: Å
    - `r_Fminus_HF`: Å
    - `total_energy`: eV

### desorption_energy_surface_without_Hplus.csv
- **path:** `/app/outputs/desorption_energy_surface_without_Hplus.csv`
- **format:** csv
- **purpose:** scored (reference surface)
- **target_policy:** metric_recompute
- **description:** Desorption energy surface computed without hydrogen attack. Used for trend comparisons and to verify the effect of H⁺.
- **schema:**
  - `type`: table
  - `required_columns`: `r_O_Si`, `r_Si_Fminus`, `total_energy`, `optimized_O_Si_F_angle`, `Si_O_bond_population`
  - `units`:
    - `r_O_Si`: Å
    - `r_Si_Fminus`: Å
    - `total_energy`: eV
    - `optimized_O_Si_F_angle`: deg
    - `Si_O_bond_population`: dimensionless

### desorption_energy_surface_with_Hplus.csv
- **path:** `/app/outputs/desorption_energy_surface_with_Hplus.csv`
- **format:** csv
- **purpose:** scored (load‑bearing)
- **target_policy:** metric_recompute
- **description:** Desorption energy surface computed with explicit H⁺ attack. The checker extracts the transition state and activation energy from this surface. Load‑bearing: cannot be fabricated without running the core calculation.
- **schema:**
  - `type`: table
  - `required_columns`: `r_O_Si`, `r_Si_Fminus`, `total_energy`, `optimized_O_Si_F_angle`, `Si_O_bond_population`
  - `units`:
    - `r_O_Si`: Å
    - `r_Si_Fminus`: Å
    - `total_energy`: eV
    - `optimized_O_Si_F_angle`: deg
    - `Si_O_bond_population`: dimensionless

### activation_energy_report.json
- **path:** `/app/outputs/activation_energy_report.json`
- **format:** json
- **purpose:** scored
- **target_policy:** exact_match
- **description:** Summary report containing the extracted key quantities. Checked against hidden reference values with tolerances.
- **schema:**
  - `type`: object
  - `required`:
    - `sif4_equilibrium_bond_length`: float (Å)
    - `hf2_dissociation_barrier`: float (eV)
    - `hf2_saddle_r`: float (Å)
    - `siF4_desorption_activation_energy`: float (eV)
    - `transition_state_r_O_Si`: float (Å)
    - `transition_state_r_Si_Fminus`: float (Å)
    - `angle_range`: list of two floats (min, max) in deg
    - `bond_population_range`: list of two floats (max, min) dimensionless

### angle_population_trend.csv
- **path:** `/app/outputs/angle_population_trend.csv`
- **format:** csv
- **purpose:** scored
- **target_policy:** structural_audit
- **description:** Trend of O–Si–F angle and Si–O bond population along the minimum‑energy desorption path for both H⁺ conditions. The checker verifies monotonic decrease in angle and population, with steeper collapse for the `with_Hplus` case.
- **schema:**
  - `type`: table
  - `required_columns`: `case`, `reaction_coordinate_rc`, `optimized_O_Si_F_angle`, `Si_O_bond_population`
  - `units`:
    - `reaction_coordinate_rc`: Å
    - `optimized_O_Si_F_angle`: deg
    - `Si_O_bond_population`: dimensionless

**Notes:** All energies are in eV, lengths in Å, angles in degrees. The desorption surface with H⁺ is the principal scored artifact; its activation energy must be derived from the computed grid. The angle and population trend must show monotonic changes consistent with the underlying physics.

## Self-check before finishing (optional, not scored)

Double-check your output files against the output contract above: every declared file exists, JSON objects contain all required keys, and CSV files contain all required columns. Fix any mismatch before finishing. This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness.

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that independently processes each file according to a pre‑set rubric, measuring how closely the quantities you computed match the reference results. The verifier does **not** simply read a single claimed number; it recomputes key figures from your raw grids (locating minima and saddle points, extracting barriers and equilibrium distances) and checks monotonic trends and structural consistency. Each scored artifact carries a weight, with the desorption energy surface under H⁺ attack (load‑bearing) receiving the largest share, followed by the HF2⁻ dissociation surface and the SiF4 binding curve; the report and trend files each contribute a smaller fraction. Reporting the paper’s numbers without the underlying computation is insufficient — the reward depends on the numerical content of the raw data files and their agreement with the expected energetic and structural behaviour.