# Self-consistent anion dipole correction to lattice energy of a rutile crystal

## Problem background
The rutile crystal structure (space group P4₂/mnm) places anions at sites that possess only two perpendicular reflection planes, which permits a non-zero permanent electric field at the anion site. This field can induce an electric dipole moment on the anion. The induced dipoles then contribute an additional term to the total lattice energy of the crystal. For TiO₂, the theoretical lattice energy calculated from a point-ion model is significantly lower than the experimental Born-Haber value, raising the question of whether the crystal is truly heteropolar. Before drawing that conclusion, it is necessary to compute the dipole contribution to the lattice energy and determine its magnitude. In this task you will perform a self-consistent calculation of the anion dipole contribution to the lattice energy of rutile TiO₂.

## Approach
The calculation proceeds in several stages. First, the point-ion lattice potentials at the titanium and oxygen sites are obtained by direct Coulomb summation over symmetric shells of unit cells, using ionic charges Ti⁴⁺ and O²⁻. From these potentials the Madelung constant is derived. Next, the electric field at an oxygen site due to the point ions (E_i) is evaluated by finite differences: the potential is computed at points displaced ±0.05 Å along the direction that lies at the intersection of the two reflection planes (the positive sense is toward the nearest titanium in the basal plane). To determine the field from the dipoles themselves, each oxygen ion is assigned a unit dipole moment P_u = e·1.0 Å oriented along E_i, and the resulting electric field E_d at an oxygen site is computed by the same finite-difference method. The actual oxygen dipole moment P is then obtained from the self-consistency condition P = A P_u = α (E_i + A E_d), where α is the oxygen ion polarizability and A = P/P_u. Given the actual dipole array, the electric potentials from the dipoles at the Ti and O sites are calculated, and the dipole energy contribution to the lattice energy is computed as ½ Σ q_i V_i (with q_i in multiples of e and V_i in volts), then converted to kcal mol⁻¹. Adding this to the point-ion lattice energy gives the total corrected theoretical lattice energy.

## Reproduction target
Your objective is to produce a JSON file `/app/outputs/results.json` containing the following computed quantities for rutile TiO₂ (using lattice parameters a=4.594 Å, c=2.959 Å, x=0.3054 and oxygen polarizability α=2.4×10⁻²⁴ cm³):
- Ti_point_ion_potential_V (float)
- O_point_ion_potential_V (float)
- Madelung_constant (float)
- E_i_V_per_m (float) – electric field from point ions at an oxygen site
- E_d_V_per_m (float) – electric field from unit dipoles at an oxygen site
- A (float) – scaling factor P/P_u
- O_dipole_moment_e_A (float) – actual oxygen dipole moment in e·Å
- dipolar_potential_Ti_V (float)
- dipolar_potential_O_V (float)
- dipole_energy_contribution_kcal_mol (float)
- total_corrected_lattice_energy_kcal_mol (float)
All numerical values must be the result of faithfully executing the self-consistent dipole correction calculation described in the workflow steps.

## Assets

- Rutile TiO2 lattice parameters (a, c, x) from Hurlen (1959)
- Oxygen ion polarizability α = 2.4×10⁻²⁴ cm³ (from Tessman, Kahn & Shockley 1953)

## Workflow steps

### Step 1: Compute point-ion potentials and Madelung constant
- Role: process
- Action: Perform direct Coulomb summation over symmetric shells of unit cells to converge the lattice potentials at Ti (0,0,0) and O (x,x,0) sites, using ionic charges Ti⁴⁺ and O²⁻. Compute the Madelung constant from the average Ti-O distance 1.961 Å.

### Step 2: Compute electric field from point ions at oxygen site
- Role: process
- Action: From the point-ion potential, evaluate the electric field E_i at an oxygen site by finite differences: calculate the potential at points 0.05 Å on each side of the site along the line of intersection of the two reflection planes (positive direction toward the nearest Ti in the basal plane).

### Step 3: Compute electric field from unit dipoles
- Role: process
- Action: Assign a unit dipole moment P_u = e·1.0 Å to each oxygen ion in the direction of E_i. Compute the resulting electric field E_d at an oxygen site using the same finite-difference method.

### Step 4: Solve for actual oxygen dipole moment
- Role: process
- Action: Solve the self-consistent equation P = A·P_u = α (E_i + A·E_d) for the scaling factor A using the oxygen polarizability α. Compute the actual dipole moment P = A·P_u.

### Step 5: Compute dipolar potentials at ion sites
- Role: process
- Action: Using the dipole array with the actual moment P, compute the electric potentials at the Ti and O sites.

### Step 6: Compute dipole energy contribution and total lattice energy
- Role: process
- Action: Compute the dipole contribution to the lattice energy using (1/2) Σ q_i V_i over the unit cell (q in multiples of e, V in volts) and convert to kcal/mol. Derive the point-ion lattice energy from the Madelung constant and sum to obtain the total corrected theoretical lattice energy.

### Step 7: Assemble final scored results
- Role: scored (load-bearing)
- Action: Collect all computed quantities from the previous steps into a single JSON file `results.json` containing the fields: Ti_point_ion_potential_V, O_point_ion_potential_V, Madelung_constant, E_i_V_per_m, E_d_V_per_m, A, O_dipole_moment_e_A, dipolar_potential_Ti_V, dipolar_potential_O_V, dipole_energy_contribution_kcal_mol, total_corrected_lattice_energy_kcal_mol.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"Ti_point_ion_potential_V": float, "O_point_ion_potential_V": float, "Madelung_constant": float, "E_i_V_per_m": float, "E_d_V_per_m": float, "A": float, "O_dipole_moment_e_A": float, "dipolar_potential_Ti_V": float, "dipolar_potential_O_V": float, "dipole_energy_contribution_kcal_mol": float, "total_corrected_lattice_energy_kcal_mol": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Aggregated numerical results from the self-consistent dipole correction calculation for rutile TiO2. The checker compares each field to the hidden paper-reported values with appropriate relative tolerances.
- schema:
  - `type`: object
  - `required`: `Ti_point_ion_potential_V`, `O_point_ion_potential_V`, `Madelung_constant`, `E_i_V_per_m`, `E_d_V_per_m`, `A`, `O_dipole_moment_e_A`, `dipolar_potential_Ti_V`, `dipolar_potential_O_V`, `dipole_energy_contribution_kcal_mol`, `total_corrected_lattice_energy_kcal_mol`
  - `properties`:
    - `Ti_point_ion_potential_V`:
      - `type`: number
    - `O_point_ion_potential_V`:
      - `type`: number
    - `Madelung_constant`:
      - `type`: number
    - `E_i_V_per_m`:
      - `type`: number
    - `E_d_V_per_m`:
      - `type`: number
    - `A`:
      - `type`: number
    - `O_dipole_moment_e_A`:
      - `type`: number
    - `dipolar_potential_Ti_V`:
      - `type`: number
    - `dipolar_potential_O_V`:
      - `type`: number
    - `dipole_energy_contribution_kcal_mol`:
      - `type`: number
    - `total_corrected_lattice_energy_kcal_mol`:
      - `type`: number

Notes: The task exclusively uses computational procedures and public constants; all inputs are specified from literature. The graded artifact is results.json; intermediate evidence files are not scored but document the execution.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ti_point_ion_potential_V",
          "O_point_ion_potential_V",
          "Madelung_constant",
          "E_i_V_per_m",
          "E_d_V_per_m",
          "A",
          "O_dipole_moment_e_A",
          "dipolar_potential_Ti_V",
          "dipolar_potential_O_V",
          "dipole_energy_contribution_kcal_mol",
          "total_corrected_lattice_energy_kcal_mol"
        ],
        "properties": {
          "Ti_point_ion_potential_V": {
            "type": "number"
          },
          "O_point_ion_potential_V": {
            "type": "number"
          },
          "Madelung_constant": {
            "type": "number"
          },
          "E_i_V_per_m": {
            "type": "number"
          },
          "E_d_V_per_m": {
            "type": "number"
          },
          "A": {
            "type": "number"
          },
          "O_dipole_moment_e_A": {
            "type": "number"
          },
          "dipolar_potential_Ti_V": {
            "type": "number"
          },
          "dipolar_potential_O_V": {
            "type": "number"
          },
          "dipole_energy_contribution_kcal_mol": {
            "type": "number"
          },
          "total_corrected_lattice_energy_kcal_mol": {
            "type": "number"
          }
        }
      },
      "description": "Aggregated numerical results from the self-consistent dipole correction calculation for rutile TiO2. The checker compares each field to the hidden paper-reported values with appropriate relative tolerances."
    }
  ],
  "notes": "The task exclusively uses computational procedures and public constants; all inputs are specified from literature. The graded artifact is results.json; intermediate evidence files are not scored but document the execution."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `/app/outputs/results.json` and compares each numeric field to reference values using appropriate relative tolerances. Each field that is present, within the correct format, and within tolerance contributes to the final score; the fields are weighted, with the primary quantities (dipole moment, dipole energy contribution, and total corrected lattice energy) carrying the highest weight. Simply reporting numbers that look plausible is not sufficient — the verifier tests whether the computed values are physically consistent with the specified crystal parameters and the self-consistent dipole model. There is no partial credit for steps that are skipped or for numbers that are far outside the tolerance ranges.