# Molecular Dynamics Simulations of Point Defect Production in Ferrite and Fe₃C Inclusion Systems

## Problem background
Ferritic-martensitic steels used in nuclear applications often contain carbide phases. Neutron irradiation produces collision cascades that create point defects — vacancies, interstitials, and antisite atoms — whose populations depend on the recoil energy, the ambient temperature, and the presence of carbide inclusions. Understanding how many point defects form and where they are located (especially near carbide-matrix interfaces) is important for predicting radiation damage. This task addresses the defect production in two model systems: pure α-iron (ferrite) and a ferrite cell containing a spherical Fe₃C (cementite) inclusion. You will compute the average numbers of antisites, vacancies, and interstitials per cascade as a function of recoil energy and temperature, and for the inclusion-containing cell you will also compute the radial distribution of these defects centred on the inclusion.

## Approach
Use classical molecular dynamics with the analytical bond-order potential for Fe-Cr-C. Construct two types of simulation cell: a cubic BCC Fe supercell (side ~100 Å) and a composite cell in which a spherical Fe₃C inclusion (radius ~20 Å) is embedded in an α-iron host. Equilibrate each cell at target temperatures of 400, 800, and 1000 K and zero pressure. For each cell type, temperature, and recoil energy (100, 500, 3000 eV), run 50 independent cascade simulations. Each cascade starts from a randomly chosen recoil position located near the cell centre, applies a Berendsen thermostat on thin border layers, and includes electronic stopping for atoms with kinetic energy ≥5 eV (Ziegler model), with a total simulation time of 50 ps. After the cascade relaxes, perform Wigner-Seitz cell analysis on the final atomic configuration to count vacancies, interstitials, and antisites. Average the counts over the 50 cascades for each condition. For the inclusion cell, also collect the spatial positions of the defects, bin them into spherical shells of width 5 Å around the inclusion centre, and compute the defect yield density per shell. The approach allows you to examine how the defect populations differ between pure ferrite and a ferrite‑carbide composite across the energy–temperature parameter space.

## Reproduction target
You must produce two scored artifacts:

1. `defect_counts.csv`: for every combination of cell type (`pure_Fe` and `Fe_Fe3C_inclusion`), recoil energy (100, 500, 3000 eV), and temperature (400, 800, 1000 K), report the average numbers of antisites, vacancies, and interstitials per cascade (averaged over the 50 cascades performed for that condition).

2. `radial_profiles.yaml`: for the inclusion cell only, provide the radial defect density profiles (antisites, vacancies, interstitials) at each energy/temperature combination, expressed as yield per unit volume in 5 Å wide spherical shells up to at least 50 Å from the inclusion centre.

The task is to carry out the full simulation and analysis pipeline described in the workflow steps and to write these two files in the specified formats.

## Assets

- Fe-Cr-C ABOP potential parameters (Henriksson 2013): 10.1088/0953-8984/25/44/445401
- Crystal structures for bcc Fe and cementite (Fe₃C): 10.1063/1.2991181
- LAMMPS molecular dynamics code: https://lammps.sandia.gov/
- Python analysis environment (numpy, scipy, pyyaml): numpy, scipy, pyyaml

## Workflow steps

### Step 1: Prepare and equilibrate pure ferrite cell
- Role: process
- Action: Construct an ~100 Å cubic BCC Fe supercell (lattice parameter a=2.89 Å). Equilibrate at 400, 800, and 1000 K and zero pressure for 50 ps using the Fe-Cr-C ABOP potential and Berendsen thermostat/barostat. Save relaxed cells.
- Evidence: `/app/outputs/cell_log.txt`

### Step 2: Prepare and equilibrate Fe cell with Fe₃C inclusion
- Role: process
- Action: Cut a spherical Fe₃C inclusion of radius ~20 Å from the relaxed pure cementite cell (DFT structure). Embed it into a relaxed pure Fe cell (radius-matched cavity) and carefully relax the composite cell at 400, 800, 1000 K and zero pressure for 50 ps using the same potential and thermostat/barostat.
- Evidence: `/app/outputs/cell_inclusion_log.txt`

### Step 3: Run cascade MD simulations
- Role: process
- Action: For each combination of cell type (pure Fe, Fe+Fe₃C), temperature (400, 800, 1000 K), and recoil energy (100, 500, 3000 eV), perform 50 independent cascade simulations. Use a Berendsen thermostat on 6 Å border layers, no pressure control, electronic stopping for atoms with kinetic energy ≥5 eV (Ziegler model), maximum simulation time 50 ps per cascade. Recoil positions are randomly chosen inside a 10 Å sphere centred on the inclusion centre (or the box centre for pure Fe).
- Evidence: `/app/outputs/cascade_run_log.txt`

### Step 4: Wigner-Seitz defect counting
- Role: scored (load-bearing)
- Action: Perform Wigner-Seitz cell analysis on the final configuration of every cascade. Count vacancies (empty WS cells), interstitials (WS cells with ≥2 atoms), and antisites (atoms on wrong element sites in the carbide). Compute the average N_V, N_I, N_AS per cascade for each (cell, energy, temperature) condition. Write the averaged counts to defect_counts.csv.
- Output file: `/app/outputs/defect_counts.csv`
- Format: csv
- Contract: Columns: cell_type (string: pure_Fe or Fe_Fe3C_inclusion), recoil_energy_eV (int), temperature_K (int), avg_antisites (float), avg_vacancies (float), avg_interstitials (float). One row per condition.
- Scoring: scored by hidden verifier

### Step 5: Radial defect distribution for inclusion cell
- Role: scored (load-bearing)
- Action: For the Fe+Fe₃C inclusion cell, collect defect positions (antisites, vacancies, interstitials) from all cascades at each energy/temperature. Compute the yield density Y(r) (defects per unit volume) in 5 Å wide spherical shells centred on the inclusion centre, averaged over the 50 cascades. Write the results to radial_profiles.yaml.
- Output file: `/app/outputs/radial_profiles.yaml`
- Format: other
- Contract: YAML dictionary keyed by condition string (e.g. 'Fe_Fe3C_inclusion_3000eV_1000K'); value is a list of shell objects: {radius_center (float, Å), antisite_density (float, atoms/Å³), vacancy_density (float), interstitial_density (float)}. Shell width 5 Å, up to at least 50 Å.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_counts.csv`
- `/app/outputs/radial_profiles.yaml`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_counts.csv
- path: `/app/outputs/defect_counts.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Averaged Wigner-Seitz defect counts per cascade for each combination of cell type, recoil energy, and temperature.
- schema:
  - `type`: table
  - `required_columns`: `cell_type`, `recoil_energy_eV`, `temperature_K`, `avg_antisites`, `avg_vacancies`, `avg_interstitials`
  - `units`:
    - `recoil_energy_eV`: eV
    - `temperature_K`: K

### radial_profiles.yaml
- path: `/app/outputs/radial_profiles.yaml`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Radial yield density profiles of defects for the Fe₃C inclusion cell.
- schema:
  - `type`: object
  - `required`:
    - `condition_key`: list of shell objects
  - `items`:
    - `radius_center`: float (Å)
    - `antisite_density`: float (atoms/Å³)
    - `vacancy_density`: float (atoms/Å³)
    - `interstitial_density`: float (atoms/Å³)

Notes: The scored outputs are evaluated by structural audit and statistical checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "cell_type",
          "recoil_energy_eV",
          "temperature_K",
          "avg_antisites",
          "avg_vacancies",
          "avg_interstitials"
        ],
        "units": {
          "recoil_energy_eV": "eV",
          "temperature_K": "K"
        }
      },
      "description": "Averaged Wigner-Seitz defect counts per cascade for each combination of cell type, recoil energy, and temperature."
    },
    {
      "file": "radial_profiles.yaml",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "condition_key": "list of shell objects"
        },
        "items": {
          "radius_center": "float (Å)",
          "antisite_density": "float (atoms/Å³)",
          "vacancy_density": "float (atoms/Å³)",
          "interstitial_density": "float (atoms/Å³)"
        }
      },
      "description": "Radial yield density profiles of defects for the Fe₃C inclusion cell."
    }
  ],
  "notes": "The scored outputs are evaluated by structural audit and statistical checks."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently examines both output files. The verifier checks the format and completeness of each artifact, then assesses the physical consistency and quality of the reported defect counts and radial distributions. The two scored artifacts are weighted; the detailed scoring logic is not revealed, but the verifier evaluates whether the computed results follow a physically plausible dependence on energy and temperature and whether the radial profile exhibits the expected features near the inclusion interface. Reporting numbers from the literature is not sufficient — the verifier only considers the data you actually computed and placed in the output files.
