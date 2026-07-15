# AIMD Simulation of Pb(II) and Selenite Adsorption on Goethite Surfaces

## Problem background
This task reproduces a first-principles density functional theory (DFT) study of Pb(II) and selenite (SeO3^2-) adsorption at the water–goethite (α-FeOOH) interface. Understanding how toxic heavy metals and oxyanions bind to mineral surfaces is a central question in environmental geochemistry. Here we use ab initio molecular dynamics (AIMD) and static DFT to determine the structural configurations of these adsorbed species on two dominant surface facets of goethite: the (101) and (210) surfaces. The key quantities to be computed are the Fe–Pb distances from finite-temperature AIMD simulations and the Se–Fe distance from a static geometry optimization, as well as the stability of a Pb(II)/selenite contact ion pair.

## Approach
The approach employs periodic DFT with the Perdew-Burke-Ernzerhof (PBE) functional and a Hubbard-U correction for Fe 3d orbitals (U=4 eV, J=1 eV) to describe the electronic structure. Slab models of the (101) and (210) surfaces are built from the bulk goethite crystal structure (Pnma space group), ensuring antiferromagnetic ordering and overall charge neutrality. Explicit water molecules are added to form a liquid-like interfacial region. For Pb(II) adsorption, AIMD simulations are run at 400 K with tritium mass for hydrogen and a time step of 0.5 fs, sampling the dynamic protonation states and coordination environment. Specific initial binding configurations are considered: on the (101) surface, a three-coordinated site with a deprotonated Fe3O group; on the (210) surface, a three-coordinated edge-plus-corner site; and for the ion pair, a Pb(II)/SeO3^2- complex on (210) with a monodentate Se–O–Fe bridge. A static DFT optimization is performed for selenite inserted bidentately on the (101) surface. The trajectories are analyzed by discarding an equilibration period and computing time-averaged Fe–Pb distances; the static structure yields the Se–Fe distance. The results are compiled into a single JSON file.

## Reproduction target
Produce the file `/app/outputs/results.json` with the following five fields, obtained from your simulations:
- `shortest_Fe_Pb_101`: the shortest time-averaged Fe–Pb distance (in Å) from the AIMD trajectory of Pb(II) on the goethite (101) surface (three-coordinated site, deprotonated Fe3O group).
- `shortest_Fe_Pb_210` and `second_shortest_Fe_Pb_210`: the two smallest time-averaged Fe–Pb distances (in Å) from the AIMD trajectory of Pb(II) on the goethite (210) surface (edge-plus-corner coordinated site).
- `Se_Fe_distance_101`: the Se–Fe distance (in Å) from the static optimized geometry of selenite (SeO3^2-) adsorbed on the goethite (101) surface in the bidentate insertion configuration. If two Se–Fe distances are nearly equal, report their average.
- `contact_ion_pair_stable`: a boolean, `true` if the selenite anion remains bonded to a surface Fe throughout the entire AIMD trajectory of the Pb(II)/SeO3^2- ion pair on (210), `false` otherwise.

## Assets

- Goethite crystal structure (Pnma): https://www.crystallography.net/cod/
- PBE pseudopotentials for Fe, O, H, Pb, Se: http://www.quantum-simulation.org/potentials/sg15_oncv/
- Periodic DFT code with AIMD capability: https://www.cp2k.org
- SPC/E water model parameters: https://en.wikipedia.org/wiki/SPC/E_model
- Packmol: https://m3g.github.io/packmol/

## Workflow steps

### Step 1: Construct goethite surface slabs
- Role: process
- Action: Retrieve the goethite crystal structure (Pnma) from a public database. Build periodic slab models for the (101) and (210) surfaces with antiferromagnetic ordering and overall charge neutrality. The (101) slab should have stoichiometry Fe32O72H48, dimensions approx. 11.06×12.18×25 Å³; the (210) slab Fe48O120H96, dims. 13.89×11.71×27.31 Å³. Terminate surfaces with appropriate OH/H2O groups according to the method: Fe3O, Fe2OH, Fe1OH on (101); Fe1OH, Fe1OH2, and two types of Fe2OH on (210).
- Evidence: `/app/outputs/slab_models.pdb`

### Step 2: Add water to surface cells
- Role: process
- Action: Determine the appropriate amount of water between the goethite surfaces using grand canonical Monte Carlo (GCMC) with SPC/E water and ClayFF, or by packing with Packmol, to achieve target water content: ~76 H2O for the (101) cell and 85–89 H2O for the (210) cell. Generate initial water configurations for AIMD.
- Evidence: `/app/outputs/water_configurations.pdb`

### Step 3: Static DFT optimization of selenite on (101)
- Role: process
- Action: Perform a static DFT geometry optimization of a SeO3^2- ion adsorbed on the goethite (101) surface in the bidentate insertion configuration (replacing two surface OH^- groups). The simulation cell must be charge neutral. Use the same DFT settings (PBE+U, plane-wave cutoff ~400 eV, Γ-point). Save the optimized atomic positions.
- Evidence: `/app/outputs/selenite_opt.xyz`

### Step 4: Prepare AIMD initial configurations for Pb(II) and ion pair
- Role: process
- Action: From the hydrated slab models, create three initial configurations for AIMD, ensuring overall charge neutrality of each cell:
1. Pb(II) on goethite (101) at the three-coordinated corner-plus-edge site, with the Fe3O group deprotonated and two Fe1OH groups protonated.
2. Pb(II) on goethite (210) at the three-coordinated edge-plus-corner site, with the coordinating Fe2OH group deprotonated and two Fe1OH groups (one may be initially protonated).
3. Pb(II)/SeO3^2- contact ion pair on goethite (210) where the selenite is bonded monodentately to a surface Fe and Pb is edge-shared.
- Evidence: `/app/outputs/aimd_initial_configs.pdb`

### Step 5: Run AIMD simulations
- Role: process
- Action: For each configuration from step 04, run an ab initio molecular dynamics simulation using the same DFT functional (PBE+U, U=4 eV, J=1 eV, plane-wave cutoff ~400 eV, Γ-point). Use a time step of 0.5 fs with tritium mass for hydrogen, thermostat at 400 K. Run for at least 10 ps. Save the trajectory coordinates and energies.
- Evidence: `/app/outputs/aimd_trajectories.tar.gz`

### Step 6: Analyze trajectories and compile results
- Role: scored (load-bearing)
- Action: Analyze the AIMD trajectories and the static selenite optimization to produce the required output file. For each AIMD trajectory, discard the first 1–2 ps as equilibration and compute time-averaged Fe-Pb distances over the remainder. For the static selenite geometry, compute the Se-Fe distance(s). Determine whether the contact ion pair remains attached (selenite remains bonded to a surface Fe throughout). Write these results as a JSON file with keys: shortest_Fe_Pb_101, shortest_Fe_Pb_210, second_shortest_Fe_Pb_210, Se_Fe_distance_101, contact_ion_pair_stable.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"shortest_Fe_Pb_101": <float in Å>, "shortest_Fe_Pb_210": <float in Å>, "second_shortest_Fe_Pb_210": <float in Å>, "Se_Fe_distance_101": <float in Å>, "contact_ion_pair_stable": <bool>}
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
- description: Reproduced structural parameters: time-averaged Fe-Pb distances from AIMD, Se-Fe distance from static DFT, and stability of the contact ion pair.
- schema:
  - `type`: object
  - `required`: `shortest_Fe_Pb_101`, `shortest_Fe_Pb_210`, `second_shortest_Fe_Pb_210`, `Se_Fe_distance_101`, `contact_ion_pair_stable`
  - `properties`:
    - `shortest_Fe_Pb_101`:
      - `type`: number
      - `unit`: angstrom
    - `shortest_Fe_Pb_210`:
      - `type`: number
      - `unit`: angstrom
    - `second_shortest_Fe_Pb_210`:
      - `type`: number
      - `unit`: angstrom
    - `Se_Fe_distance_101`:
      - `type`: number
      - `unit`: angstrom
    - `contact_ion_pair_stable`:
      - `type`: boolean

Notes: All distances are in angstroms. The checker compares each numeric field to the hidden paper-reported value with a prescribed tolerance, and checks the boolean against the paper's result. Reward is the fraction of the five fields that match.

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
          "shortest_Fe_Pb_101",
          "shortest_Fe_Pb_210",
          "second_shortest_Fe_Pb_210",
          "Se_Fe_distance_101",
          "contact_ion_pair_stable"
        ],
        "properties": {
          "shortest_Fe_Pb_101": {
            "type": "number",
            "unit": "angstrom"
          },
          "shortest_Fe_Pb_210": {
            "type": "number",
            "unit": "angstrom"
          },
          "second_shortest_Fe_Pb_210": {
            "type": "number",
            "unit": "angstrom"
          },
          "Se_Fe_distance_101": {
            "type": "number",
            "unit": "angstrom"
          },
          "contact_ion_pair_stable": {
            "type": "boolean"
          }
        }
      },
      "description": "Reproduced structural parameters: time-averaged Fe-Pb distances from AIMD, Se-Fe distance from static DFT, and stability of the contact ion pair."
    }
  ],
  "notes": "All distances are in angstroms. The checker compares each numeric field to the hidden paper-reported value with a prescribed tolerance, and checks the boolean against the paper's result. Reward is the fraction of the five fields that match."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/results.json`. Each numeric field (`shortest_Fe_Pb_101`, `shortest_Fe_Pb_210`, `second_shortest_Fe_Pb_210`, `Se_Fe_distance_101`) is compared against a hidden reference value using a predefined absolute tolerance; the boolean field `contact_ion_pair_stable` is checked for exact correctness. The five fields carry equal weight (0.2 each). The final reward is the fraction of fields that match the reference, a number between 0.0 and 1.0. The verifier does not re-run your simulations; it judges only the structural results you report. Producing physically accurate results from the specified protocol is the path to a high score.
