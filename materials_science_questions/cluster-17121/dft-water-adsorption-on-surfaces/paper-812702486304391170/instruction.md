# Molecular Dynamics of Benzoate Adsorption on Hydrated Calcite at Varying Salinity

## Problem background
Carbonate rock reservoirs often become oil-wet over geological time due to adsorption of polar organic molecules from crude oil onto pore surfaces, particularly aromatic acids with carboxyl groups. Understanding the molecular-level interactions that control this adsorption is important for designing improved oil recovery strategies, including low-salinity waterflooding. The calcite {10-14} surface in contact with brine forms structured hydration layers, and the presence of dissolved ions may modulate how organic molecules access and bind to the mineral surface. This task investigates the interfacial structuring of a model aromatic acid (benzoate, the deprotonated form of benzoic acid) at the calcite/brine interface as a function of NaCl salinity. The goal is to compute the distribution and dynamics of water, ions, and benzoate at three representative salinity levels and determine how salinity alters the adsorption behaviour of the organic molecules.

## Approach
Atomistic molecular dynamics (MD) simulations are used to model a slit-pore system consisting of two parallel calcite {10-14} slabs confining a solution of water, NaCl, and benzoate molecules. Three salinity conditions are prepared: deionized water (DW, 0 ppm NaCl), low-salinity brine (LS, 5000 ppm), and seawater (SW, 45000 ppm), each with additional Na+ ions to neutralize the benzoate charge. The calcite slab is described by the force field of Xiao et al., water by the flexible TIP3P/Fw model, and benzoate and ions by the OPLS-AA force field. After building the initial configurations, each system is equilibrated at 80 °C and 30 MPa following a two-stage protocol (thermal equilibration with a mobile upper slab, then pressurization), followed by a 50 ns NVT production run with atomic coordinates saved every 0.5 ps. Analysis is performed on the last 20 ns of each trajectory. The quantities extracted are: one-dimensional number density profiles of all species along the surface normal, radial distribution functions g(r) for Na+-benzoate and Na+-water oxygen pairs within the interfacial region (the zone where water density oscillates near the surface), and the time-dependent survival probability of benzoate molecules in the interfacial region, integrated to obtain residence times. The comparison across the three salinity conditions reveals how ion concentration affects the interfacial structuring and the persistence of organic molecules near the mineral surface.

## Reproduction target
Run atomistic MD simulations of a calcite {10-14} slit pore filled with brine and 24 benzoate molecules at three NaCl salinities (DW: 0 ppm, LS: 5000 ppm, SW: 45000 ppm, plus neutralizing Na+). From the last 20 ns of each 50 ns production trajectory, compute and output the following artifacts covering all three salinity conditions: (1) 1D number density profiles of water oxygen, water hydrogen, benzoate, Na+, and Cl- along the surface normal; (2) the radial distribution function g(r) for Na+-benzoate pairs at the interface; (3) the radial distribution function g(r) for Na+-water oxygen pairs at the interface; (4) the survival probability P(t) of benzoate molecules in the interfacial region as a function of time; and (5) the corresponding residence time obtained by integrating each survival probability curve. The target is a complete, self-consistent set of these quantities that captures the structural and dynamical features of the calcite/brine/benzoate interface and their dependence on salinity.

## Assets

- LAMMPS molecular dynamics package: https://lammps.sandia.gov
- Calcite force field (Xiao et al., J. Phys. Chem. C 2011): 10.1021/jp204555p
- TIP3P/Fw water model: 10.1063/1.445869
- OPLS-AA force field for benzoate and ions: 10.1021/ja9621760
- PACKMOL: http://m3g.iqm.unicamp.br/packmol

## Workflow steps

### Step 1: Build simulation cells for DW, LS, SW
- Role: process
- Action: Construct three initial LAMMPS data files: calcite {10-14} slab (56.67 x 54.89 x 19.77 Å, 1078 CaCO3 units), 24 benzoate molecules, 6183 water molecules, and appropriate Na+ and Cl- counts to achieve salinities 0 ppm (DW), 5000 ppm (LS), and 45000 ppm (SW) plus neutralizing Na+ ions. Use the TIP3P/Fw and OPLS-AA force fields.
- Evidence: `/app/outputs/initial_cells.log`

### Step 2: Run MD equilibration and production
- Role: process
- Action: For each salinity, equilibrate the system at 80 °C and 30 MPa using LAMMPS with the NPT/NVT protocol described in the paper, then run 50 ns production dynamics saving atomic coordinates every 0.5 ps.
- Evidence: `/app/outputs/md_evidence.tar.gz`

### Step 3: Compute number density profiles
- Role: scored (load-bearing)
- Action: From the last 20 ns of each trajectory, compute the z-dependent number density of water oxygen (Ow), water hydrogen (Hw), benzoate (Bz), Na+, and Cl- averaged over both calcite slabs. Output one file with all salinities.
- Output file: `/app/outputs/density_profiles.csv`
- Format: csv
- Contract: salinity (string: DW/LS/SW), z (float, Å), Ow_density (float, atoms/Å³), Hw_density (float), Bz_density (float), Na_density (float), Cl_density (float)
- Scoring: scored by hidden verifier

### Step 4: Compute Na+ - benzoate RDF at interface
- Role: scored
- Action: Calculate the radial distribution function g(r) between Na+ ions and the benzoate center of mass (or carboxylate carbon) for molecules located within the interfacial region (defined as the oscillatory portion of the density profile within ~1 nm of the surface). Output for each salinity.
- Output file: `/app/outputs/rdf_Na_Bz_interface.csv`
- Format: csv
- Contract: salinity (string), r (float, Å), g_r (float)
- Scoring: scored by hidden verifier

### Step 5: Compute Na+ - water Ow RDF at interface
- Role: scored
- Action: Calculate g(r) between Na+ ions and water oxygen atoms inside the interfacial region. Output for each salinity.
- Output file: `/app/outputs/rdf_Na_Ow_interface.csv`
- Format: csv
- Contract: salinity (string), r (float, Å), g_r (float)
- Scoring: scored by hidden verifier

### Step 6: Compute benzoate survival probability
- Role: scored
- Action: For the interfacial region, compute the survival probability P(t) of benzoate molecules using the standard definition from the paper. Average over all timesteps in the last 20 ns. Output P(t) as a function of time for each salinity.
- Output file: `/app/outputs/survival_probability.csv`
- Format: csv
- Contract: salinity (string), time (ps, float), p_t (float)
- Scoring: scored by hidden verifier

### Step 7: Compute benzoate residence times
- Role: scored
- Action: Integrate the survival probability curves to obtain the residence time for each salinity. Output the single scalar value per salinity.
- Output file: `/app/outputs/residence_times.csv`
- Format: csv
- Contract: salinity (string), residence_time (ps, float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/density_profiles.csv`
- `/app/outputs/rdf_Na_Bz_interface.csv`
- `/app/outputs/rdf_Na_Ow_interface.csv`
- `/app/outputs/survival_probability.csv`
- `/app/outputs/residence_times.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### density_profiles.csv
- path: `/app/outputs/density_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Number density profiles of water oxygen, hydrogen, benzoate, Na+, and Cl- along the surface normal for DW, LS, SW salinities.
- schema:
  - `type`: table
  - `required_columns`: `salinity`, `z`, `Ow_density`, `Hw_density`, `Bz_density`, `Na_density`, `Cl_density`
  - `units`:
    - `z`: Å
    - `Ow_density`: atoms/Å³
    - `Hw_density`: atoms/Å³
    - `Bz_density`: atoms/Å³
    - `Na_density`: atoms/Å³
    - `Cl_density`: atoms/Å³

### rdf_Na_Bz_interface.csv
- path: `/app/outputs/rdf_Na_Bz_interface.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Radial distribution function g(r) for Na+ - benzoate pairs at the calcite/brine interface, for each salinity.
- schema:
  - `type`: table
  - `required_columns`: `salinity`, `r`, `g_r`
  - `units`:
    - `r`: Å
    - `g_r`: dimensionless

### rdf_Na_Ow_interface.csv
- path: `/app/outputs/rdf_Na_Ow_interface.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Radial distribution function g(r) for Na+ - water oxygen pairs at the interface, for each salinity.
- schema:
  - `type`: table
  - `required_columns`: `salinity`, `r`, `g_r`
  - `units`:
    - `r`: Å
    - `g_r`: dimensionless

### survival_probability.csv
- path: `/app/outputs/survival_probability.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Survival probability P(t) of benzoate molecules at the interface for each salinity.
- schema:
  - `type`: table
  - `required_columns`: `salinity`, `time`, `p_t`
  - `units`:
    - `time`: ps
    - `p_t`: dimensionless

### residence_times.csv
- path: `/app/outputs/residence_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Benzoate residence times at the interface, one per salinity.
- schema:
  - `type`: table
  - `required_columns`: `salinity`, `residence_time`
  - `units`:
    - `residence_time`: ps

Notes: All artifacts must be produced from the last 20 ns of 50 ns MD trajectories for the three salinities DW, LS, SW. Density profiles are averaged over both calcite slabs. The exact system dimensions and force fields are as specified in the steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "density_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "salinity",
          "z",
          "Ow_density",
          "Hw_density",
          "Bz_density",
          "Na_density",
          "Cl_density"
        ],
        "units": {
          "z": "Å",
          "Ow_density": "atoms/Å³",
          "Hw_density": "atoms/Å³",
          "Bz_density": "atoms/Å³",
          "Na_density": "atoms/Å³",
          "Cl_density": "atoms/Å³"
        }
      },
      "description": "Number density profiles of water oxygen, hydrogen, benzoate, Na+, and Cl- along the surface normal for DW, LS, SW salinities."
    },
    {
      "file": "rdf_Na_Bz_interface.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "salinity",
          "r",
          "g_r"
        ],
        "units": {
          "r": "Å",
          "g_r": "dimensionless"
        }
      },
      "description": "Radial distribution function g(r) for Na+ - benzoate pairs at the calcite/brine interface, for each salinity."
    },
    {
      "file": "rdf_Na_Ow_interface.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "salinity",
          "r",
          "g_r"
        ],
        "units": {
          "r": "Å",
          "g_r": "dimensionless"
        }
      },
      "description": "Radial distribution function g(r) for Na+ - water oxygen pairs at the interface, for each salinity."
    },
    {
      "file": "survival_probability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "salinity",
          "time",
          "p_t"
        ],
        "units": {
          "time": "ps",
          "p_t": "dimensionless"
        }
      },
      "description": "Survival probability P(t) of benzoate molecules at the interface for each salinity."
    },
    {
      "file": "residence_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "salinity",
          "residence_time"
        ],
        "units": {
          "residence_time": "ps"
        }
      },
      "description": "Benzoate residence times at the interface, one per salinity."
    }
  ],
  "notes": "All artifacts must be produced from the last 20 ns of 50 ns MD trajectories for the three salinities DW, LS, SW. Density profiles are averaged over both calcite slabs. The exact system dimensions and force fields are as specified in the steps."
}
```

## How you are scored
Each of the five scored output files is independently evaluated by a hidden verifier that compares your submitted artifact against reference expectations derived from the underlying physical system. The verifier checks structural features of the density profiles (such as the presence and relative positioning of hydration layers and solute peaks), the shape and key features of the radial distribution functions, the decay behaviour of the survival probability curves, and the consistency of the residence times across conditions. Checks may include verifying that certain relationships between the three salinity conditions are physically reasonable and internally consistent. Each scored artifact carries a share of the total reward (the highest weight is on the density profiles, with the remaining weight distributed among the RDFs, survival probability, and residence times). Reporting plausible numbers without having executed the workflow will not match the hidden reference. You must produce all output files at the exact paths and in the exact formats specified in the output contract; files that are missing, unparseable, or fail schema validation receive zero credit for that component.
