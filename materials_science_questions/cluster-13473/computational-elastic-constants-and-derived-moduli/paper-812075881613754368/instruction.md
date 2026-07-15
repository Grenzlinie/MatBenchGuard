# Elastic Constants and Derived Mechanical Properties of Metallic Nanowires

## Problem background
Metallic nanowires are nanoscale contacts with excellent electrical conductance and high sensitivity, used in applications ranging from molecular electronics to nanomechanical systems. Their mechanical response under uniaxial tension depends on size and strain rate, exhibiting different deformation regimes from crystalline dislocation‑governed behaviour to amorphous plastic flow. For face‑centred‑cubic (fcc) noble metals such as gold (Au) and platinum (Pt), understanding how the mechanical properties — Young's modulus, first yield strain and stress, and rupture strain — vary with nanowire diameter and applied strain rate is essential for designing reliable nanoscale devices. Molecular dynamics (MD) simulations with many‑body potentials provide a way to quantify these structure–property relationships for nanowire diameters of a few nanometres, using purely computational means.

## Approach
The mechanical response is obtained by classical MD simulations using the simple Sutton–Chen many‑body potential, which describes interatomic interactions in fcc metals with power‑law repulsive and many‑body cohesive terms. The potential parameters for Au and Pt are:

| Parameter | Au       | Pt       |
|-----------|----------|----------|
| a (Å)     | 4.08     | 3.92     |
| ε (meV)   | 12.793   | 19.833   |
| c         | 34.408   | 34.408   |
| m         | 8        | 8        |
| n         | 10       | 10       |

The potential cutoff radius is 2.5 × nearest‑neighbour distance (≈ 2.5 × a/√2).

Nanowires with circular cross‑sections and a length‑to‑diameter aspect ratio of 2 are built: diameters of 5, 10 and 15 fcc lattice constants (approximately 2, 4, and 6 nm) and lengths of 10, 20, and 30 lattice constants. Fixed atom layers at the two ends enable strain application. After initial thermal equilibration at 300 K (Nosé–Hoover thermostat), the nanowire is relaxed to a near‑zero initial axial stress. Uniaxial tension is then applied along the [001] crystal direction by moving the end layers at a constant engineering strain rate of 4.0×10⁸, 4.0×10⁹, or 4.0×10¹⁰ s⁻¹, with the system evolving adiabatically. The axial virial stress, spatially averaged over all atoms, and the engineering strain are recorded throughout the deformation, yielding stress–strain curves for each condition.

For every combination of material (Au, Pt), size (5φ×10, 10φ×20, 15φ×30) and strain rate (4.0e8, 4.0e9, 4.0e10 s⁻¹) — 18 separate simulations — the resulting (strain, stress) data are dumped into a CSV file. The curves are the sole scored deliverable; all mechanical properties (Young's modulus, first yield strain/stress, rupture strain) are subsequently re‑derived from those raw curves by the checker. The simulations are implemented with the LAMMPS MD package.

## Reproduction target
Produce a single tar.gz archive containing 18 CSV files, one for each (material, size, strain‑rate) condition. File names follow the convention `{material}_{size}_{strainrate}.csv` (e.g., `Au_5phix10_4e8.csv`). Each CSV must contain two columns with header `strain,stress`: strain is dimensionless engineering strain, and stress is in GPa. The axis convention, simulation protocol, and the exact unit conversion are as described in the Approach and the workflow steps below. The submitted archive is the only artifact evaluated for scoring; the checker will extract the curves and recompute the mechanical properties (Young's modulus, first yield strain/stress, rupture strain) from them.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov

## Workflow steps

### Step 1: Build nanowire atomic configurations
- Role: process
- Action: Generate initial atomic configurations for Au and Pt nanowires with circular cross-sections of sizes 5φ×10, 10φ×20, 15φ×30 (fcc lattice constants from the potential; length-to-diameter ratio 2). Fix the end layers of atoms for subsequent strain application.
- Evidence: `/app/outputs/config_data_files`

### Step 2: MD simulations and stress–strain curve output
- Role: scored (load-bearing)
- Action: For each combination of material (Au, Pt), size (5φ×10, 10φ×20, 15φ×30), and strain rate (4.0e8, 4.0e9, 4.0e10 s⁻¹), perform a thermal equilibration at 300 K, stress‑free relaxation, then constant‑strain‑rate uniaxial tensile loading along [001] using the simple Sutton–Chen potential. Record the average axial engineering stress (virial per atom) and the corresponding engineering strain. Package 18 CSV files into the tar.gz archive.
- Output file: `/app/outputs/step_01_stress_strain_curves.tar.gz`
- Format: other
- Contract: Tar.gz archive with 18 CSV files; each CSV has header 'strain,stress' and rows of numeric values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stress_strain_curves.tar.gz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stress_strain_curves.tar.gz
- path: `/app/outputs/step_01_stress_strain_curves.tar.gz`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain curves from MD uniaxial tension simulations of Au and Pt nanowires. The checker recomputes Young's modulus, first yield strain/stress, and rupture strain.
- schema:
  - `type`: archive
  - `description`: Contains 18 CSV files with naming convention {material}_{size}_{strainrate}.csv. Each CSV has columns: strain (float), stress (float).

Notes: The checker extracts each CSV, computes young's modulus (linear fit), first yield strain/stress (first local maximum or global maximum depending on rate), and rupture strain (strain where stress drops below 0.1 GPa after yield). It compares to the paper's Table 6 values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stress_strain_curves.tar.gz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "archive",
        "description": "Contains 18 CSV files with naming convention {material}_{size}_{strainrate}.csv. Each CSV has columns: strain (float), stress (float)."
      },
      "description": "Stress-strain curves from MD uniaxial tension simulations of Au and Pt nanowires. The checker recomputes Young's modulus, first yield strain/stress, and rupture strain."
    }
  ],
  "notes": "The checker extracts each CSV, computes young's modulus (linear fit), first yield strain/stress (first local maximum or global maximum depending on rate), and rupture strain (strain where stress drops below 0.1 GPa after yield). It compares to the paper's Table 6 values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently processes the submitted `step_01_stress_strain_curves.tar.gz`. It extracts every CSV, recomputes Young's modulus (linear fit over the initial elastic region), identifies the first yield point (strain and stress at the first local maximum for the two lower strain rates, or at the global maximum for the highest rate), and determines the rupture strain (post‑yield strain where the stress drops close to zero). Each computed value is compared against a reference value for that condition. The fraction of comparisons that fall within the allowed tolerances (which are set to accommodate legitimate implementation and discretisation differences) is recorded as the score. Simply reporting numbers taken from the literature, without having executed the full molecular dynamics pipeline, will not yield passing results because the hidden checker works directly on the raw stress–strain curves.
