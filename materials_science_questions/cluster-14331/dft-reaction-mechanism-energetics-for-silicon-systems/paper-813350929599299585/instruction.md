# Ab Initio Study of Three-Center Si–H–Si Bonding in Silicon Hydride Model Clusters

## Problem background
Hydrogenated amorphous silicon may contain three-center Si–H–Si bonds (often denoted T0) that can exchange charge to form a cation T+ and an anion T−. The stability and geometry of these three-center species influence the density of unpaired electrons in the material. This computational study models the three-center bonds using the molecular cluster H3Si–H–SiH3, where terminal silicon atoms are saturated by three hydrogens. The goal is to compute optimized structures and total energies for the cation, neutral radical, anion, and a set of reference silanes (SiH4, SiH3+, SiH3, SiH3−, singlet SiH2) to characterize the nature of the three-center bond.

## Approach
The computations use spin-restricted Hartree–Fock for closed-shell species (T+, T−, SiH4, SiH3+, SiH3−, SiH2) and spin-unrestricted HF for the open-shell neutral SiH3 and T0. A standard effective core potential (e.g., LANL2DZ) is employed for silicon, paired with a double-zeta basis for hydrogen. Equilibrium geometries are optimized with an open-source quantum chemistry package (e.g., PySCF). For the cation T+, a C3 symmetry constraint is applied so that the two terminal silyl groups are identical; for T0 and T− full optimizations are performed without symmetry restrictions. Total SCF energies are collected, and the binding energies of the three-center species are computed as E_bind(X) = E(X) − E(SiH4) − E(SiH3^{charge}), where the charge‑matching silyl reference (SiH3+, SiH3, or SiH3−) is used for X = T+, T0, T−, respectively.

## Reproduction target
Produce the following output files under /app/outputs:

- **optimized_geometries.csv**: for the three species T+, T0, and T−, list the two central Si–H distances (Si(1)–H(1) and Si(2)–H(1)) and the Si(1)–Si(2) distance, all in Å.
- **total_energies.csv**: the converged SCF total energy (hartree) for each of the eight species (SiH4, SiH3+, SiH3, SiH3−, SiH2, T+, T0, T−).
- **binding_energies.csv**: the binding energy (kcal/mol, 1 a.u. = 627.54 kcal/mol) for T+, T0, and T− computed from the total energies as defined in the approach.

The structural symmetry of the three-center bond and the magnitude of the binding energies are verified against hidden criteria derived from a reference computation with the same protocol.

## Assets

- PySCF: pyscf

## Workflow steps

### Step 1: Reference silane geometry optimization and energy computation
- Role: process
- Action: Optimize the geometries and compute the total electronic energies of SiH4, SiH3+, SiH3, SiH3-, and singlet SiH2 using spin-restricted HF for closed-shell species and unrestricted HF for open-shell SiH3. Use a standard effective core potential for silicon (e.g., LANL2DZ) and a double-zeta basis for hydrogen.
- Evidence: none

### Step 2: Three-center model geometry optimization and energy computation
- Role: process
- Action: Optimize the geometries of T+ (cation, closed-shell), T0 (neutral radical, open-shell), and T- (anion, closed-shell) for the molecular model H3Si–H–SiH3 with terminal silicon atoms each saturated by three hydrogens. For T+, enforce C3 symmetry to obtain identical terminal silyl groups; for T0 and T-, perform full optimizations without symmetry constraints. Use the same HF method, ECP, and basis set as in the reference silane step.
- Evidence: none

### Step 3: Key bond lengths of three-center species
- Role: scored
- Action: Extract the final optimized distances from the three-center species calculations: for T+, T0, and T-, record the two central Si–H distances (Si(1)–H(1) and Si(2)–H(1)) and the Si(1)–Si(2) distance, all in Å. Write the data to optimized_geometries.csv.
- Output file: `/app/outputs/optimized_geometries.csv`
- Format: csv
- Contract: molecule (string), atom1 (string), atom2 (string), distance_angstrom (float)
- Scoring: scored by hidden verifier

### Step 4: Total electronic energies of all species
- Role: scored
- Action: Collect the converged total electronic energies (in hartree) for SiH4, SiH3+, SiH3, SiH3-, SiH2, T+, T0, and T- and write them to total_energies.csv.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: molecule (string), energy_hartree (float)
- Scoring: scored by hidden verifier

### Step 5: Binding energies of T+, T0, and T-
- Role: scored (load-bearing)
- Action: Compute the binding energy as E_bind(X) = E(X) − E(SiH4) − E(SiH3^{charge}) for X = T+ using SiH3+, T0 using SiH3, and T- using SiH3- as reference. Use 1 a.u. = 627.54 kcal/mol. Write the results to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: molecule (string), binding_energy_kcal_per_mol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_geometries.csv`
- `/app/outputs/total_energies.csv`
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_geometries.csv
- path: `/app/outputs/optimized_geometries.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Optimized bond lengths for the three-center species. The scorer checks that for T+ the two central Si–H distances are equal to within a tolerance, and that for T0 and T- the two central Si–H distances differ substantially, consistent with asymmetric three-center bonding.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `atom1`, `atom2`, `distance_angstrom`
  - `units`:
    - `distance_angstrom`: angstrom

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total electronic energies (SCF) of all reference silanes and three-center model species. The scorer compares reported energies to hidden reference values obtained from a standard run with the same ECP/basis.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `energy_hartree`
  - `units`:
    - `energy_hartree`: hartree

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies of T+, T0, and T- computed from total energies. The scorer checks that the T+ binding energy is negative and substantial (within a hidden range), while T0 and T- are near zero, reflecting the stability of the symmetric three-center bond only in the cation.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `binding_energy_kcal_per_mol`
  - `units`:
    - `binding_energy_kcal_per_mol`: kcal/mol

Notes: The scoring does not depend on exact agreement with the original paper's LP-31G basis set values. A standard ECP/valence basis (e.g., LANL2DZ on Si, double-zeta on H) is used; the hidden reference values are derived from a run with the same standard protocol. The geometric symmetry conditions are checked via structural audit; energies and binding energies are compared to those reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "atom1",
          "atom2",
          "distance_angstrom"
        ],
        "units": {
          "distance_angstrom": "angstrom"
        }
      },
      "description": "Optimized bond lengths for the three-center species. The scorer checks that for T+ the two central Si–H distances are equal to within a tolerance, and that for T0 and T- the two central Si–H distances differ substantially, consistent with asymmetric three-center bonding."
    },
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "energy_hartree"
        ],
        "units": {
          "energy_hartree": "hartree"
        }
      },
      "description": "Total electronic energies (SCF) of all reference silanes and three-center model species. The scorer compares reported energies to hidden reference values obtained from a standard run with the same ECP/basis."
    },
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "binding_energy_kcal_per_mol"
        ],
        "units": {
          "binding_energy_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Binding energies of T+, T0, and T- computed from total energies. The scorer checks that the T+ binding energy is negative and substantial (within a hidden range), while T0 and T- are near zero, reflecting the stability of the symmetric three-center bond only in the cation."
    }
  ],
  "notes": "The scoring does not depend on exact agreement with the original paper's LP-31G basis set values. A standard ECP/valence basis (e.g., LANL2DZ on Si, double-zeta on H) is used; the hidden reference values are derived from a run with the same standard protocol. The geometric symmetry conditions are checked via structural audit; energies and binding energies are compared to those reference values."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact.

- **optimized_geometries.csv**: structural audit checks are applied. The two central Si–H distances of T+ must be nearly equal within a hidden tolerance, while for T0 and T− the two central Si–H distances must differ by more than a hidden threshold.
- **total_energies.csv** and **binding_energies.csv**: the reported values are compared to hidden reference values obtained from a standard run with the same computational setup (HF with effective core potential and a double‑zeta basis). The binding energies are checked against hidden magnitude constraints that are consistent with the hypothesis about three‑center bond stability.

Each stage contributes a share of the total reward; the final reward is the weighted sum. Submitting the paper's reported numbers without an actual computational run will not satisfy the scoring.
