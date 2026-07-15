# Grand Canonical Monte Carlo Adsorption Isotherms

## Problem background
Electrochemical metal deposition in nanometric surface defects is a key technique for nanostructuring. Controlling the deposit's location and morphology at the atomic scale is challenging and depends sensitively on the balance between adsorbate–substrate and adsorbate–adsorbate interactions. In this task, we study the decoration of a nanometer-sized cavity on a Au(111) surface by Cu and Ag atoms. The simulations predict how the cavity is filled and whether clusters grow above the surface, which is essential for understanding and controlling nanostructuring processes. The goal is to compute the equilibrium number of deposited atoms and their average binding energy as functions of the chemical potential, revealing the distinct filling behaviors.

## Approach
Atomistic Grand Canonical Monte Carlo (GCMC) simulations are performed for two metal–substrate systems at 300 K: Cu on Au(111) and Ag on Au(111). The interactions are described by Embedded Atom Method (EAM) potentials — the Barrera potential for Cu–Au and the Foiles potential for Ag–Au. The substrate is modelled as an Au(111) slab containing a nanocavity of width 22 Å and depth three atomic layers. In the GCMC method, the chemical potential μ of the adsorbate species is fixed, and Monte Carlo moves (particle displacements, insertions, and removals) sample the equilibrium distribution of the number of adsorbed atoms N and the total potential energy U of the system. By sweeping μ across a range that covers wall decoration up to multilayer formation, we obtain the adsorption isotherm (N vs. μ) and compute the average binding energy per atom as (U_system − U_substrate)/N as a function of μ. Comparing the two systems highlights how the relative strength of adsorbate–substrate versus adsorbate–adsorbate interactions governs the cavity filling pathway.

## Reproduction target
Produce two CSV files, cu_adsorption_isotherm.csv and ag_adsorption_isotherm.csv, each containing columns chemical_potential (in eV), num_atoms (integer, ≥0), and avg_binding_energy (eV/atom, negative). The chemical potential grid must span the full sequence of cavity decoration stages: from the earliest decoration of the cavity walls through stepwise filling and — where applicable — multilayer cluster growth above the surface. The isotherms and binding energy curves must be consistent with the underlying physics: the number of adsorbed atoms should be non-decreasing with chemical potential, and features such as plateaus and sudden jumps should reflect distinct structural states.

## Assets

- EAM potential for Cu-Au (Barrera et al., 2000): 10.1088/0965-0393/8/4/306
- EAM potential for Ag-Au (Foiles et al., 1986): 10.1103/PhysRevB.33.7983
- Molecular dynamics package with GCMC support (e.g., LAMMPS or ASE): https://www.lammps.org

## Workflow steps

### Step 1: System setup and EAM potential loading
- Role: process
- Action: Construct an Au(111) slab with a nanocavity (width 22 Å, depth 3 atomic layers) and load the Cu–Au (Barrera) and Ag–Au (Foiles) EAM potentials. Verify the initial configurations are ready for GCMC simulations.
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Cu/Au adsorption isotherm
- Role: scored (load-bearing)
- Action: Run Grand Canonical Monte Carlo simulations for Cu deposition on the Au(111) nanocavity at 300 K over a range of chemical potentials covering wall decoration to multilayer growth. For each chemical potential, record the equilibrium number of adsorbed Cu atoms and the total potential energy. Compute the average binding energy per atom as (U(system) − U(substrate))/num_atoms. Write the results to cu_adsorption_isotherm.csv.
- Output file: `/app/outputs/cu_adsorption_isotherm.csv`
- Format: csv
- Contract: columns: chemical_potential (eV), num_atoms (integer, >=0), avg_binding_energy (eV/atom, negative)
- Scoring: scored by hidden verifier

### Step 3: Ag/Au adsorption isotherm
- Role: scored (load-bearing)
- Action: Run Grand Canonical Monte Carlo simulations for Ag deposition on the Au(111) nanocavity at 300 K over a range of chemical potentials covering wall decoration to bilayer growth. Record the equilibrium number of Ag atoms and total energy, compute the average binding energy per atom, and write the results to ag_adsorption_isotherm.csv.
- Output file: `/app/outputs/ag_adsorption_isotherm.csv`
- Format: csv
- Contract: columns: chemical_potential (eV), num_atoms (integer, >=0), avg_binding_energy (eV/atom, negative)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cu_adsorption_isotherm.csv`
- `/app/outputs/ag_adsorption_isotherm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cu_adsorption_isotherm.csv
- path: `/app/outputs/cu_adsorption_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Cu/Au adsorption isotherm: number of deposited Cu atoms and average binding energy per atom as functions of chemical potential.
- schema:
  - `type`: table
  - `required_columns`: `chemical_potential`, `num_atoms`, `avg_binding_energy`
  - `units`:
    - `chemical_potential`: eV
    - `avg_binding_energy`: eV/atom

### ag_adsorption_isotherm.csv
- path: `/app/outputs/ag_adsorption_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ag/Au adsorption isotherm: number of deposited Ag atoms and average binding energy per atom as functions of chemical potential.
- schema:
  - `type`: table
  - `required_columns`: `chemical_potential`, `num_atoms`, `avg_binding_energy`
  - `units`:
    - `chemical_potential`: eV
    - `avg_binding_energy`: eV/atom

Notes: The checker compares the step positions (chemical potentials where num_atoms increases abruptly) and the plateau values of avg_binding_energy against hidden gold values extracted from the paper's figures. Only the CSV files are required; energy histograms and excess energy analysis are not scored outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cu_adsorption_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "chemical_potential",
          "num_atoms",
          "avg_binding_energy"
        ],
        "units": {
          "chemical_potential": "eV",
          "avg_binding_energy": "eV/atom"
        }
      },
      "description": "Cu/Au adsorption isotherm: number of deposited Cu atoms and average binding energy per atom as functions of chemical potential."
    },
    {
      "file": "ag_adsorption_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "chemical_potential",
          "num_atoms",
          "avg_binding_energy"
        ],
        "units": {
          "chemical_potential": "eV",
          "avg_binding_energy": "eV/atom"
        }
      },
      "description": "Ag/Au adsorption isotherm: number of deposited Ag atoms and average binding energy per atom as functions of chemical potential."
    }
  ],
  "notes": "The checker compares the step positions (chemical potentials where num_atoms increases abruptly) and the plateau values of avg_binding_energy against hidden gold values extracted from the paper's figures. Only the CSV files are required; energy histograms and excess energy analysis are not scored outputs."
}
```

## How you are scored
A hidden verifier evaluates each output CSV independently. For each file, the checker extracts the positions of abrupt steps in num_atoms (chemical potentials where the atom count increases sharply) and the corresponding plateau values of avg_binding_energy. These extracted features are compared against a pre-determined reference derived from the source study using appropriate tolerances. Additionally, structural trends are checked: num_atoms must be non-decreasing with increasing chemical potential, and avg_binding_energy must become more negative and then plateau or show distinct steps. The verification does not depend on a single oversimplified number; rather, it assesses whether the computed isotherms capture the correct sequence of cavity decoration events. The overall reward is a weighted combination of the scores from the two stages.
