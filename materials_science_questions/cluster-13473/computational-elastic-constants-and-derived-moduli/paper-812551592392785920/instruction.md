# Computational Reproduction of Poly(Ionic Liquid) Thermal and Mechanical Properties from Molecular Dynamics

## Problem background
Poly(ionic liquid) (PIL) networks, formed by cross-linking ionic liquid monomers, are attractive as ion-conducting materials and structural polymers. Their thermal and mechanical properties—glass transition temperature (Tg), elastic moduli—and the transport of small anions through the polymer matrix are thought to depend on the strength of electrostatic interactions between the cationic polymer backbone and the anions, which in turn is influenced by anion size and the rigidity of the ionic liquid monomer. Understanding these structure–property relationships is essential for designing PILs with targeted combinations of stiffness, thermal stability, and ion mobility. This task investigates three PIL variants built from two bis(epoxidized) imidazolium monomers, EIM2 and EIM1, each cross-linked with tris(2-aminoethyl)amine (TAEA) and fully neutralized with either TFSI⁻ or Cl⁻ anions. By performing molecular dynamics (MD) simulations on each system at 90% cross-linking, you will compute four key quantities: (1) the first peak position of the cation–anion radial distribution function, which reflects interionic packing; (2) the glass transition temperature; (3) Young’s modulus; and (4) the anion self-diffusion coefficient. The goal is to determine how these properties vary across the three systems and whether the variations align with the expected roles of anion size and monomer flexibility.

## Approach
Use all-atom molecular dynamics simulations to reconstruct the cross-linked PIL networks and extract their structural, thermal, mechanical, and transport properties. First, build molecular models of the three systems (EIM2/TFSI⁻, EIM2/Cl⁻, EIM1/TFSI⁻) with a stoichiometry of 3:2 for ionic liquid monomer:TAEA and 300 anions per simulation box. Perform distance‑based cross‑linking simulations to reach 90 % degree of cross‑linking. Then subject each cross‑linked configuration to a cooling ramp from 700 K to 200 K under NPT conditions; fit the density–temperature curve with a hyperbolic regression to extract the glass transition temperature Tg. Equilibrate an independent sample of each system at 300 K and use the production trajectory to compute (a) the cation–anion radial distribution function (center‑of‑mass of anion to imidazolium nitrogen atoms) to locate the first peak position r_peak, and (b) the mean‑square displacement of the anion centre‑of‑mass to obtain the self‑diffusion coefficient D from the long‑time linear slope. Separately, perform uniaxial‑tension simulations at 300 K and a constant strain rate; compute Young’s modulus E from the linear region of the stress–strain curve. The workflow should be carried out with a general‑purpose, open‑source force field (e.g., OPLS‑AA or GAFF) rather than the proprietary OPLS3e field used in the original work, and the final results must be reported for all three systems. Throughout, manage simulations using an open‑source MD engine such as LAMMPS or GROMACS.

## Reproduction target
Compute the following four properties for each of the three PIL systems (EIM2/TFSI⁻, EIM2/Cl⁻, EIM1/TFSI⁻) at 90 % cross‑linking:
- r_peak (Å): the first peak position of the cation–anion radial distribution function,
- Tg (K): the glass transition temperature extracted from density–temperature cooling curves,
- E (GPa): Young’s modulus obtained from uniaxial tension simulations at 300 K,
- D (cm²/s): the anion self‑diffusion coefficient at 300 K.

Assemble these twelve numbers into a single CSV file. The absolute values are expected to lie within a generous range of the reference literature results, acknowledging that a different force field and simulation toolchain will introduce systematic shifts. The verifier will assess the reported numbers against hidden reference criteria.

## Assets

- Molecular dynamics engine (LAMMPS or GROMACS): https://lammps.sandia.gov
- General-purpose force field parameters (OPLS-AA, GAFF, or similar): https://ligpargen.openbabel.org

## Workflow steps

### Step 1: System construction and cross-linking simulation
- Role: process
- Action: Build molecular models of the three PIL systems (EIM2/TFSI⁻, EIM2/Cl⁻, EIM1/TFSI⁻) with a stoichiometry of 3:2 for ionic liquid monomer:TAEA and 300 anions. Run distance-based cross-linking simulations to achieve 90 % degree of cross-linking.
- Evidence: `/app/outputs/crosslink_info.txt`

### Step 2: Annealing MD and glass transition temperature extraction
- Role: process
- Action: Using the cross-linked configurations, perform NPT annealing cycles from 700 K to 200 K (20 K steps). Record density vs. temperature and fit a hyperbolic regression model to extract Tg.
- Evidence: `/app/outputs/annealing_density.csv`

### Step 3: Equilibration MD at 300 K
- Role: process
- Action: Equilibrate each cross-linked system at 300 K (e.g., 20 ns NVT production after an initial equilibration phase) and collect trajectories for structural and dynamic analysis.
- Evidence: none

### Step 4: Cation–anion radial distribution function analysis
- Role: process
- Action: From the 300 K trajectory, compute the radial distribution function g(r) between the center-of-mass of the anion and the imidazolium nitrogen atoms. Identify the first peak position (r_peak, Å) for each system.
- Evidence: `/app/outputs/rdf_data.csv`

### Step 5: Mechanical deformation and Young’s modulus calculation
- Role: process
- Action: Perform uniaxial tension MD simulations at a constant strain rate in NVT at 300 K. Compute Young’s modulus (E, GPa) from the linear region of the averaged stress–strain curves.
- Evidence: `/app/outputs/stress_strain.csv`

### Step 6: Anion diffusion coefficient calculation
- Role: process
- Action: From the 300 K trajectory, compute the mean square displacement (MSD) of the anion center-of-mass. Fit the long-time linear region to obtain the self-diffusion coefficient D (cm²/s).
- Evidence: `/app/outputs/msd_data.csv`

### Step 7: Compile final scored artifact
- Role: scored (load-bearing)
- Action: Assemble the computed quantities (r_peak, Tg, E, D) for each of the three PIL systems into a single CSV file.
- Output file: `/app/outputs/step_01_properties.csv`
- Format: csv
- Contract: system (string), r_peak_AA (float), Tg_K (float), E_GPa (float), D_cm2s (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_properties.csv
- path: `/app/outputs/step_01_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-system computed properties: first peak distance of cation–anion radial distribution function, glass transition temperature, Young's modulus, and anion self-diffusion coefficient for three PIL systems (EIM2/TFSI⁻, EIM2/Cl⁻, EIM1/TFSI⁻) at 90 % cross-linking.
- schema:
  - `type`: table
  - `required_columns`: `system`, `r_peak_AA`, `Tg_K`, `E_GPa`, `D_cm2s`
  - `units`:
    - `r_peak_AA`: Å
    - `Tg_K`: K
    - `E_GPa`: GPa
    - `D_cm2s`: cm²/s

Notes: The hidden checker reads this CSV and compares each quantity against paper-reported reference values with generous tolerances. Scoring is based on correct reproduction of the relative trends (ordering among systems) and approximate absolute magnitudes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "r_peak_AA",
          "Tg_K",
          "E_GPa",
          "D_cm2s"
        ],
        "units": {
          "r_peak_AA": "Å",
          "Tg_K": "K",
          "E_GPa": "GPa",
          "D_cm2s": "cm²/s"
        }
      },
      "description": "Per-system computed properties: first peak distance of cation–anion radial distribution function, glass transition temperature, Young's modulus, and anion self-diffusion coefficient for three PIL systems (EIM2/TFSI⁻, EIM2/Cl⁻, EIM1/TFSI⁻) at 90 % cross-linking."
    }
  ],
  "notes": "The hidden checker reads this CSV and compares each quantity against paper-reported reference values with generous tolerances. Scoring is based on correct reproduction of the relative trends (ordering among systems) and approximate absolute magnitudes."
}
```

## How you are scored
A hidden verifier reads your submitted `step_01_properties.csv` and compares each quantity against a set of reference values and ordering expectations that are derived from the original publication. The verifier does not re‑run any simulation; it only inspects the final CSV. Scoring is based on two equally important criteria: (1) correct relative trends across the three systems for r_peak, Tg, E, and D, and (2) approximate agreement of the absolute values with the literature reference, using generous tolerances (±50 %) to account for differences in the force field, MD engine, and simulation details. Each correctly reproduced trend and each value that falls within the tolerance range contributes to the overall reward, which is a number between 0 and 1. The final reward will be the fraction of the required checks that pass. Note that simply copying the paper’s reported numbers without running the simulation pipeline will not satisfy the tolerance and trend requirements because the verifier uses a hidden reference; honest execution of the entire workflow is necessary to obtain the correct pattern of results.
