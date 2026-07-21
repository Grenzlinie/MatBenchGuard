# Ripplocation–Vacancy Coupling in 2D WSe₂

## Problem background
Two-dimensional WSe₂ layers can develop structural deformations known as ripplocations when subjected to mechanical loading. Simultaneously, point defects such as Se vacancies are common in these materials and can influence their mechanical and electronic properties. Understanding how curvature and vacancy formation energies interact is important for defect engineering and for controlling growth of high-quality 2D WSe₂. The target of this task is to compute, using a reactive empirical potential (ReaxFF), the formation energies of pristine and Se-vacancy-containing ripplocations as a function of buckling height, and to determine whether a mechanochemical coupling exists between monolayer bending and vacancy formation.

## Approach
We use the published W/Se/H ReaxFF force field parameters (provided with the problem resources, see resources.json) to perform energy minimisations of various atomic models of a WSe₂ bilayer. The workflow constructs: (i) a flat, pristine AB‑stacked bilayer (R0); (ii) four compressed ripplocation models (R1–R4) with increasing buckling heights; (iii) the corresponding defective models in which a Se vacancy is introduced on each layer (R0‑vac and R1‑vac to R4‑vac); and (iv) a flat monolayer with two isolated Se vacancies to study the two‑vacancy ripple energy. After relaxing all structures with LAMMPS (or an equivalent ReaxFF‑capable code), the bulk chemical potentials of bcc‑W and α‑Se are computed. From the relaxed total energies and these chemical potentials, formation energies are derived: the pristine ripplocation formation energy relative to R0, the vacancy formation energy in each defective ripplocation, and the defective‑ripplocation formation energy relative to flat defective R0‑vac. Finally, the buckling height Δh is extracted and the observed trends are summarised.

## Key parameters (from the ReaxFF‑optimised monolayer)
- 2H‑WSe₂ monolayer lattice constant: **a = 3.29 Å**, **γ = 120°** (hexagonal unit cell).
- Monolayer thickness (Se‑Se vertical separation): **h<sub>Se‑Se</sub> = 3.09 Å**.
- Bilayer AB‑stacked interlayer spacing: **d<sub>inter</sub> = 6.52 Å**.
- W‑Se bond distance: **2.57 Å**.
- Unit cell basis vectors (for a hexagonal cell with vacuum in the z‑direction):
  - **a₁** = (a, 0, 0)
  - **a₂** = (−a/2, a·√3/2, 0)
  - **a₃** = (0, 0, L<sub>z</sub>)   where L<sub>z</sub> is large enough to include vacuum (~30 Å).

### Atomic positions in the monolayer unit cell
One WSe₂ unit cell contains 1 W and 2 Se atoms.
Using the hexagonal basis above, fractional coordinates (and corresponding Cartesian ones) are:
- W:   frac (0,0,0)  →  Cartesian (0, 0, 0)
- Se₁: frac (1/3, 2/3, +d)  →  Cartesian (0, a/√3 ≈ 1.900 Å, +d)
- Se₂: frac (1/3, 2/3, −d)  →  Cartesian (0, a/√3, −d)
where **d = h<sub>Se‑Se</sub>/2 = 1.545 Å**. (These coordinates give the correct W‑Se bond length.)

## Model construction

### 0. General notes
- Always add a vacuum region in the z‑direction so that periodic images do not interact; a total cell height of **30 Å** is sufficient.
- Use periodic boundary conditions in all three dimensions.
- For the bilayer, stack two monolayers with AB (Bernal) stacking: translate the second layer by **d<sub>inter</sub> = 6.52 Å** along z, and shift it in‑plane by **(a/√3, 0, 0)** (or equivalently by the fractional vector (1/3, 2/3, 0) of the hexagonal cell) so that one layer’s W sits above the other layer’s Se hexagon centre.

### 1. Flat pristine bilayer R0
- Supercell size: **24 × 1** in the zigzag direction (x‑axis, along a₁) and armchair direction (y‑axis, along a₂).  
  This yields a box of approximate size:
  - L<sub>x</sub> = 24 × 3.29 = **78.96 Å**
  - L<sub>y</sub> = a·√3 ≈ **5.70 Å**
  - L<sub>z</sub> = **30 Å** (including vacuum)
- Build the AB bilayer with 24×1 repeats.
- This is the reference flat model **R0**.

### 2. Compressed ripplocation models R1–R4
- Starting from R0, compress the cell **along the zigzag direction** (x‑axis) by the following amounts:
  - R1: **21.9 %** compression → new L<sub>x</sub> = 78.96 × (1 − 0.219) ≈ 61.65 Å
  - R2: **33.6 %** compression → new L<sub>x</sub> ≈ 52.44 Å
  - R3: **40.1 %** compression → new L<sub>x</sub> ≈ 47.30 Å
  - R4: **45.3 %** compression → new L<sub>x</sub> ≈ 43.18 Å
- Keep L<sub>y</sub> and L<sub>z</sub> unchanged. Scale the atomic coordinates uniformly in x so that fractional coordinates remain the same.
- These models, after relaxation, will develop ripplocations; label them **R1, R2, R3, R4**.

### 3. Defective models (Se vacancies)
- **R0‑vac**: Starting from R0, remove **one Se atom from the top layer and one Se atom from the bottom layer** at two locations that are far apart (e.g. near opposite ends of the cell) to minimise interaction. The result is the flat defective reference **R0‑vac**.
- **R1‑vac … R4‑vac**: For each compressed ripplocation model R1–R4, remove a Se‑Se pair in the **concave region of highest curvature**:
  - After relaxation of the pristine ripplocation, the structure will develop a concave (inwardly bent) region. Locate the Se atoms with the **lowest z‑coordinates** (the deepest concavity). From those atoms, choose one Se atom in the top layer and the Se atom in the bottom layer that has nearly the same (x,y) position, and remove them both.
  - If the concave region is symmetric, the pair should be centred near the middle of the ripplocation.
  - The resulting defective models are **R1‑vac, R2‑vac, R3‑vac, R4‑vac**.

### 4. Flat monolayer with two isolated Se vacancies (for two‑vacancy ripple energy)
- Build a **flat monolayer** (not bilayer) using the same 24×1 unit cell as R0 but with only one layer (no second layer). The cell dimensions are the same as R0.
- Label the pristine monolayer **M0**.
- In M0, remove **one Se atom from the top Se layer and one Se atom from the bottom Se layer** (since the monolayer has two Se planes) at positions that are separated by at least half the cell length to avoid interaction. This creates the defect‑pair monolayer **M0‑2vac**.

## Energy minimisation
For every model (R0, R1–R4, R0‑vac, R1‑vac–R4‑vac, M0, M0‑2vac) and for the bulk reference crystals:
1. Use the provided ReaxFF force field with LAMMPS (or any ReaxFF‑capable code).
2. Perform geometry optimisation until the force on each atom is ≤ **0.02 eV/Å** (or a comparably strict threshold).
3. Record the final total energy (in eV) of each relaxed structure.

Additionally, obtain the **chemical potentials**:
- Optimise a bulk **bcc‑W** supercell (e.g. 3×3×3 conventional cell) with the same ReaxFF potential, divide the total energy by the number of W atoms → **μ<sub>W</sub>** (eV/atom).
- Optimise a bulk **α‑Se** crystal (trigonal, a 3‑chain cell) with the same potential, divide total energy by the number of Se atoms → **μ<sub>Se</sub>** (eV/atom).

## Formation energy definitions
Given the relaxed total energies:

- **Pristine ripplocation formation energy** (relative to flat bilayer R0):  
  **E<sup>f</sup><sub>ripp</sub>(Rn) = E(Rn) − E(R0)**

- **Vacancy formation energy in a ripplocation** (referenced to the corresponding pristine ripplocation):  
  **E<sub>vac</sub>(Rn‑vac) = E(Rn‑vac) − E(Rn) + μ<sub>Se</sub>**

- **Defective‑ripplocation formation energy** (relative to flat defective R0‑vac):  
  **E<sup>f</sup><sub>ripp‑vac</sub>(Rn‑vac) = E(Rn‑vac) − E(R0‑vac)**

- **Two‑vacancy ripple energy** (for the flat monolayer with two isolated Se vacancies):  
  **E<sub>2vac</sub> = E(M0‑2vac) − E(M0) + 2·μ<sub>Se</sub>**

## Buckling height extraction
For each relaxed ripplocation model (pristine and defective), the buckling height is defined as the span of the Se‑atom z‑coordinates:  
**Δh = max(z<sub>Se</sub>) − min(z<sub>Se</sub>)**  
For flat models, set Δh = 0.

## Reproduction target
Produce two scored artifacts:
- `ripplocation_energies.json`: Contains the total energies and derived formation energies for all models, the chemical potentials used, and the two‑vacancy ripple energy. This file must follow the exact schema declared in the output contract.
- `trend_summary.txt`: A plain‑text table of buckling height vs. pristine ripplocation formation energy and vacancy formation energy, together with the computed two‑vacancy ripple energy and explicit statements describing the observed trends. The checker will verify that the reported energies and trends are internally consistent and conform to the expected behavior of the force field.

## Workflow steps

### Step 1: Generate models
- Action: Construct all required atomic models as described in the Model construction section. Prepare input files for energy minimisation. Document the construction in a log file.
- Evidence: `/app/outputs/model_generation.log`

### Step 2: ReaxFF energy minimisation
- Action: Run geometry optimisation for all structures (R0, R1–R4, R0‑vac, R1‑vac–R4‑vac, M0, M0‑2vac) with the ReaxFF force field. Also optimise the bulk W and Se reference crystals. Record the final total energies and structural data.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Compute chemical potentials
- Action: From the relaxed bulk cells, extract μ_W and μ_Se as described above. Report them in a log.
- Evidence: `/app/outputs/chemical_potentials.log`

### Step 4: Compute formation energies and output results
- Role: scored (load‑bearing)
- Action: Using the relaxed total energies and chemical potentials, compute the formation energies according to the formulas. Extract buckling heights for all ripplocation models. Write the results to `ripplocation_energies.json` with the keys `two_vacancy_ripple_energy`, `chemical_potentials`, and `models` containing the prescribed fields and units.
- Output file: `/app/outputs/ripplocation_energies.json`
- Format: json
- Contract: See output contract.

### Step 5: Summarise mechanochemical coupling trends
- Role: scored
- Action: Write a plain‑text file `trend_summary.txt` that lists the buckling heights and the corresponding pristine ripplocation formation energies E<sup>f</sup><sub>ripp</sub> and vacancy formation energies E<sub>vac</sub>. Explicitly state the observed trends: (i) E<sup>f</sup><sub>ripp</sub> increases monotonically with Δh, (ii) E<sub>vac</sub> decreases monotonically with Δh, (iii) E<sub>vac</sub> becomes negative at the highest Δh, (iv) the defective ripplocation total energy becomes lower than the pristine ripplocation total energy at large Δh. Also include the computed two‑vacancy ripple energy.
- Output file: `/app/outputs/trend_summary.txt`
- Format: txt
- Contract: See output contract.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ripplocation_energies.json
- path: `/app/outputs/ripplocation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The computed raw total energies, derived formation energies for all ripplocation models, and the two‑vacancy ripple energy. The checker verifies that the formation energies follow the required monotonic trends and that the two‑vacancy ripple energy matches a hidden reference value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `two_vacancy_ripple_energy`: float (eV)
    - `chemical_potentials`: object with mu_W and mu_Se (eV)
    - `models`: array of objects {name, type, buckling_height (Å), total_energy (eV), formation_energy_pristine (eV) (pristine only), formation_energy_vacancy (eV) (defective only), formation_energy_defective_ripplocation (eV) (defective only)}

### trend_summary.txt
- path: `/app/outputs/trend_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: A human‑readable summary that the checker audits to confirm the reported trends and consistency with the numerical JSON output.
- schema:
  - `type`: text
  - `required_content`: A table of buckling heights vs E_ripp^f and E_vac, the two‑vacancy ripple energy, and explicit statements that the four mechanochemical coupling trends hold.

### Evidence logs (unscored, but required by workflow)
- `model_generation.log`: Log of model generation step.
- `relaxation.log`: Log of energy minimisation step.
- `chemical_potentials.log`: Log of chemical potential computation.

Notes: The JSON file is the load‑bearing scored artifact; the checker will verify the monotonic trends and compare the two‑vacancy ripple energy to a hidden gold value (exact_match with tolerance). The plain‑text summary is scored structurally.

## How you are scored
Each scored artifact is independently evaluated by a hidden verifier. For `ripplocation_energies.json`, the checker recomputes formation energies from the provided total energies and chemical potentials, then assesses whether the reported trends satisfy required structural relationships. The two‑vacancy ripple energy is compared to a hidden reference value within a tolerance. For `trend_summary.txt`, the checker confirms that the numerical values match those in the JSON file and that the stated trend observations are correct. Successful reproduction requires that the workflow steps are genuinely executed in order; merely reporting numbers, even if correct, is not sufficient. The final reward is a weighted combination of the scores from the individual stages.