# DFT Molecular Dynamics of Hydrogen Diffusion in a-Si:H under Photoexcitation

## Problem background
Hydrogenated amorphous silicon (a‑Si:H) is a technologically important semiconductor that exhibits light‑induced metastability: prolonged illumination causes reversible degradation of its electronic properties – the Staebler‑Wronski effect. Experiments have associated this effect with enhanced hydrogen diffusion and the possible formation of paired‑hydrogen configurations. This task reproduces a first‑principles molecular‑dynamics investigation of whether simulated optical excitation (produced by altering the electronic occupation) changes the mobility of hydrogen in an a‑Si:H network and whether it leads to the appearance of silicon dihydride (SiH₂) structural units.

## Approach
Use density‑functional theory with the SIESTA code (GGA exchange‑correlation functional, double‑ζ polarized basis set, norm‑conserving Troullier‑Martins pseudopotentials). First, generate a hydrogenated amorphous silicon model by applying the Wooten‑Winer‑Weaire (WWW) algorithm to obtain a defect‑free a‑Si backbone, removing a few silicon atoms to create vacancies, and saturating the resulting dangling bonds with hydrogen. Relax the model with DFT. From the relaxed structure, run two independent NVT molecular‑dynamics simulations at 300 K for 10 ps (time step 0.5 fs): (1) an electronic ground‑state simulation, and (2) a simulated light‑excited state where one extra electron is placed just above the Fermi level and kept during the whole dynamics; after 10 ps the system is returned to the ground state and relaxed. From the atomic trajectories of both runs, compute the time‑averaged mean squared displacement (MSD) of all hydrogen atoms. Examine the final relaxed structure of the excited‑state run to locate any silicon atom bonded to two hydrogens (a dihydride) and record the H–H distance. Document the simulation parameters in a metadata log.

## Reproduction target
From the ground‑state and light‑excited MD trajectories, compute the time‑averaged mean squared displacement (MSD) of all hydrogen atoms and write the two values (in Å²) to `msd_results.txt`. From the final relaxed geometry of the light‑excited run, identify every Si atom that is bonded to two H atoms and write the H–H distance (in Å) for each such SiH₂ unit to `sih2_hh_distance.txt`. Produce a `simulation_log.txt` that records the number of atoms, temperature (300 K), time step (0.5 fs), total MD steps (20000), pseudopotential type and exchange‑correlation functional used, and confirms that both the ground‑state and the light‑excited MD were performed.

## Assets

- SIESTA DFT code: https://departments.icmab.es/leem/siesta/
- Troullier-Martins pseudopotentials for Si and H (SIESTA format): SIESTA pseudopotential database or ATOM program
- WWW algorithm implementation for a-Si model: https://github.com/anyexample/www-silicon

## Workflow steps

### Step 1: Generate hydrogenated a-Si:H model
- Role: process
- Action: Create an a-Si:H model with ≈70–230 atoms containing at least one dangling bond. Starting from a defect-free a-Si model (e.g., 64 atoms) generated via the WWW method, remove a few Si atoms to create vacancies, and terminate all dangling bonds with H at ~1.5 Å from Si. Perform DFT relaxation with SIESTA (GGA, DZP basis, Troullier-Martins pseudopotentials, forces <0.04 eV/Å). Save the relaxed coordinates.
- Evidence: `/app/outputs/initial_relaxed.xyz`

### Step 2: Ground-state molecular dynamics simulation
- Role: process
- Action: Starting from the relaxed model, perform NVT MD at 300 K for 10 ps with 0.5 fs time step using SIESTA (same DFT settings). Keep the electronic ground state throughout. Save the trajectory (e.g., atomic positions at regular intervals).
- Evidence: `/app/outputs/gs_trajectory.xyz`

### Step 3: Light-excited state molecular dynamics simulation
- Role: process
- Action: Start from the same relaxed model. Implement photoexcitation protocol: add one extra electron just above the Fermi level (alter occupation), run MD for 10 ps at 300 K with 0.5 fs time step while holding the altered occupation. After 10 ps, return to ground state (remove extra electron) and perform a final geometry relaxation. Save the trajectory and the final relaxed geometry.
- Evidence: `/app/outputs/light_final_relaxed.xyz`

### Step 4: Write simulation metadata log
- Role: scored
- Action: Produce a text file documenting the simulation parameters: number of atoms, temperature (300 K), time step (0.5 fs), total MD steps (20000), pseudopotential type (Troullier-Martins) and functional (GGA), and confirm that both ground-state and light-excited MD were performed.
- Output file: `/app/outputs/simulation_log.txt`
- Format: txt
- Contract: Free-text with required keywords: atom count, temperature, timestep, steps, pseudopotential, functional, and statements 'ground-state MD performed' and 'light-excited MD performed'.
- Scoring: scored by hidden verifier

### Step 5: Compute hydrogen mean squared displacement
- Role: scored (load-bearing)
- Action: From the atomic trajectories of the ground-state and light-excited MD runs, compute the time-averaged mean squared displacement of all hydrogen atoms (using the formula from the paper). Write two numbers to a file: one for ground-state MSD and one for light-excited MSD.
- Output file: `/app/outputs/msd_results.txt`
- Format: txt
- Contract: Two lines: 'ground_state_msd: <float> Ang^2' and 'light_excited_msd: <float> Ang^2'.
- Scoring: scored by hidden verifier

### Step 6: Identify dihydride SiH2 configurations and report H-H distance
- Role: scored (load-bearing)
- Action: Analyze the final relaxed light-excited structure. Find any Si atom bonded to two H atoms (bond length < ~1.9 Å). For each such SiH2 unit, compute the H-H distance and write it to the output file.
- Output file: `/app/outputs/sih2_hh_distance.txt`
- Format: txt
- Contract: One line per SiH2 unit: 'SiH2_HH_distance: <float> Ang'. At least one line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_log.txt`
- `/app/outputs/msd_results.txt`
- `/app/outputs/sih2_hh_distance.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_log.txt
- path: `/app/outputs/simulation_log.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Metadata log confirming simulation parameters and executed MD runs.
- schema:
  - `type`: text
  - `required`:
    - `keywords`: `atom count`, `temperature`, `timestep`, `steps`, `pseudopotential`, `functional`, `ground-state MD performed`, `light-excited MD performed`

### msd_results.txt
- path: `/app/outputs/msd_results.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Time-averaged mean squared displacement of H atoms; must show light_excited_msd > ground_state_msd.
- schema:
  - `type`: text
  - `required`:
    - `lines`: `ground_state_msd: <float> Ang^2`, `light_excited_msd: <float> Ang^2`

### sih2_hh_distance.txt
- path: `/app/outputs/sih2_hh_distance.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Reported H-H distances for any SiH2 dihydride units; at least one line required with a distance in plausible range (2.2–2.6 Å).
- schema:
  - `type`: text
  - `required`:
    - `lines`: `SiH2_HH_distance: <float> Ang`

Notes: Scoring is structural: msd_results.txt checked for enhancement (light > ground), sih2_hh_distance.txt checked for presence and plausible H-H distance range, simulation_log.txt audited for required keywords. No exact value match to the paper is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_log.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "keywords": [
            "atom count",
            "temperature",
            "timestep",
            "steps",
            "pseudopotential",
            "functional",
            "ground-state MD performed",
            "light-excited MD performed"
          ]
        }
      },
      "description": "Metadata log confirming simulation parameters and executed MD runs."
    },
    {
      "file": "msd_results.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "lines": [
            "ground_state_msd: <float> Ang^2",
            "light_excited_msd: <float> Ang^2"
          ]
        }
      },
      "description": "Time-averaged mean squared displacement of H atoms; must show light_excited_msd > ground_state_msd."
    },
    {
      "file": "sih2_hh_distance.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "lines": [
            "SiH2_HH_distance: <float> Ang"
          ]
        }
      },
      "description": "Reported H-H distances for any SiH2 dihydride units; at least one line required with a distance in plausible range (2.2–2.6 Å)."
    }
  ],
  "notes": "Scoring is structural: msd_results.txt checked for enhancement (light > ground), sih2_hh_distance.txt checked for presence and plausible H-H distance range, simulation_log.txt audited for required keywords. No exact value match to the paper is required."
}
```

## How you are scored
A hidden verifier independently inspects each output file. It checks that `msd_results.txt` contains two non‑negative, properly formatted MSD values; that `sih2_hh_distance.txt` reports at least one H–H distance and that the distance lies within a chemically plausible range for a SiH₂ configuration; and that `simulation_log.txt` includes all required metadata keywords. The verifier does not compare your numbers to published figures; it evaluates whether the produced artifacts meet structural and physical consistency criteria. The three checks are weighted (highest weight on the MSD and dihydride evidence) and combined into a final reward score between 0 and 1.
