# Electron-Induced Solid-State Amorphization in Li–Si Alloys: DFT-MD Reproduction

## Problem background
The lithiation of silicon electrodes in lithium-ion batteries results in solid-state amorphization, where crystalline Li-Si alloys that are thermodynamically stable do not form. Instead, an amorphous Li_xSi phase is produced during electrochemical cycling, except for the fully lithiated Li3.75Si phase which can crystallize. The mechanism driving this amorphization is not fully understood. Experimental observations suggest that local electron-rich conditions at the reaction front may be responsible, but this hypothesis needs computational validation. This task explores whether adding extra electrons to crystalline Li-Si alloys can destabilize the crystal structure and lead to an amorphous phase.

## Approach
The reproduction uses density functional theory molecular dynamics (DFT-MD) to simulate four crystalline Li-Si alloys (LiSi, Li1.71Si, Li3.25Si, Li3.75Si) at 300 K. Each alloy is simulated twice: under neutral conditions (N_e=0) and under electron-rich conditions (N_e=2 added electrons per supercell, with a compensating background charge). The time evolution of the atomic structure is monitored via the pair correlation function (PCF), and changes in the electronic structure are probed via the projected density of states (pDOS) on Si 3s and 3p orbitals. The key comparison is between the initial crystalline structure and the structure after 2.5 ps of MD simulation under electron-rich conditions, to assess whether amorphization occurs.

## Reproduction target
Produce three scored outputs:
1. A CSV file containing the pair correlation function g(r) for Li1.71Si at N_e=2 at four simulation time points (40 fs, 90 fs, 140 fs, 2500 fs). The columns are time_fs (fs), r (Å), and g_r (dimensionless).
2. A CSV file containing the projected density of states on Si 3s and 3p orbitals for Li1.71Si at N_e=2 at the initial (t=0) and final (t=2.5 ps) configurations. Columns: energy_eV (relative to Fermi level), pdos_s_initial, pdos_p_initial, pdos_s_final, pdos_p_final.
3. A JSON file summarizing the amorphization status (true=amorphized, false=crystalline) of each of the four alloys (LiSi, Li1.71Si, Li3.25Si, Li3.75Si) after 2.5 ps at 300 K under N_e=2.

## Assets

- SIESTA DFT code: https://siesta-project.org
- LiSi crystal structure
- Li1.71Si (Li12Si7) crystal structure
- Li3.25Si (Li13Si4) crystal structure
- Li3.75Si (Li15Si4) crystal structure
- Troullier-Martins LDA pseudopotentials for Li and Si

## Workflow steps

### Step 1: Build supercell models of Li–Si alloys
- Role: process
- Action: Build supercell models of LiSi (128 Li, 128 Si), Li1.71Si (192 Li, 112 Si), Li3.25Si (156 Li, 48 Si), and Li3.75Si (240 Li, 64 Si) using the crystal structures obtained from public databases.
- Evidence: `/app/outputs/supercell_build.log`

### Step 2: Ab initio molecular dynamics simulations
- Role: process
- Action: Run DFT-MD simulations with SIESTA (LDA, Troullier-Martins pseudopotentials, double-ζ basis, 150 Ry mesh cutoff, Γ-point, 1 fs timestep, compensating background) for each of the four Li-Si alloys at 300 K under neutral (N_e=0) and electron-rich (N_e=2) conditions, each for at least 2.5 ps. For Li1.71Si at N_e=2, save atomic coordinates at 40, 90, 140, and 2500 fs.
- Evidence: `/app/outputs/dftmd_simulation.log`

### Step 3: Pair correlation function analysis for Li1.71Si at N_e=2
- Role: scored (load-bearing)
- Action: Compute pair correlation function g(r) from the saved atomic coordinates of Li1.71Si at N_e=2 at each time (40, 90, 140, and 2500 fs) for r up to at least 10 Å. Output a CSV with columns time_fs, r, g_r.
- Output file: `/app/outputs/li171si_pcf_ne2.csv`
- Format: csv
- Contract: CSV with columns: time_fs (int), r (float), g_r (float). Each block is identified by a constant time_fs value.
- Scoring: scored by hidden verifier

### Step 4: Projected density of states analysis for Li1.71Si at N_e=2
- Role: scored (load-bearing)
- Action: Compute projected density of states on Si 3s and 3p orbitals for the Li1.71Si system at N_e=2 using the initial crystalline structure (t=0) and the final structure at 2.5 ps. Output a CSV with energy_eV, pdos_s_initial, pdos_p_initial, pdos_s_final, pdos_p_final.
- Output file: `/app/outputs/li171si_pdos_ne2.csv`
- Format: csv
- Contract: CSV with columns: energy_eV (float), pdos_s_initial (float), pdos_p_initial (float), pdos_s_final (float), pdos_p_final (float). Energy values are relative to the Fermi level.
- Scoring: scored by hidden verifier

### Step 5: Amorphization status summary
- Role: scored
- Action: Determine whether each Li-Si compound becomes amorphous after 2.5 ps at 300 K under N_e=2, using the final configurations from the DFT-MD simulations. Output a JSON with keys LiSi, Li1.71Si, Li3.25Si, Li3.75Si, each a boolean indicating amorphized (true) or crystalline (false).
- Output file: `/app/outputs/summary_amorphization.json`
- Format: json
- Contract: JSON object with keys: LiSi (bool), Li1.71Si (bool), Li3.25Si (bool), Li3.75Si (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/li171si_pcf_ne2.csv`
- `/app/outputs/li171si_pdos_ne2.csv`
- `/app/outputs/summary_amorphization.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### li171si_pcf_ne2.csv
- path: `/app/outputs/li171si_pcf_ne2.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pair correlation function blocks for Li1.71Si at N_e=2; checker verifies disappearance of sharp peaks beyond 6 Å in later time steps.
- schema:
  - `type`: table
  - `required_columns`: `time_fs`, `r`, `g_r`
  - `units`:
    - `time_fs`: fs
    - `r`: angstrom
    - `g_r`: dimensionless

### li171si_pdos_ne2.csv
- path: `/app/outputs/li171si_pdos_ne2.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Projected density of states on Si 3s/3p orbitals at t=0 and t=2.5 ps for Li1.71Si at N_e=2; checker verifies peak merging upon amorphization.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `pdos_s_initial`, `pdos_p_initial`, `pdos_s_final`, `pdos_p_final`
  - `units`:
    - `energy_eV`: eV
    - `pdos_s_initial`: arb.units
    - `pdos_p_initial`: arb.units
    - `pdos_s_final`: arb.units
    - `pdos_p_final`: arb.units

### summary_amorphization.json
- path: `/app/outputs/summary_amorphization.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Amorphization status of the four alloys under N_e=2 at 300 K; checker validates boolean assignments against the expected amorphization pattern.
- schema:
  - `type`: object
  - `required`:
    - `LiSi`: boolean
    - `Li1.71Si`: boolean
    - `Li3.25Si`: boolean
    - `Li3.75Si`: boolean

Notes: Scoring uses T3 structural checks: PCF long-range order loss, PDOS peak merging, and exact amorphization status pattern.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "li171si_pcf_ne2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_fs",
          "r",
          "g_r"
        ],
        "units": {
          "time_fs": "fs",
          "r": "angstrom",
          "g_r": "dimensionless"
        }
      },
      "description": "Pair correlation function blocks for Li1.71Si at N_e=2; checker verifies disappearance of sharp peaks beyond 6 Å in later time steps."
    },
    {
      "file": "li171si_pdos_ne2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "pdos_s_initial",
          "pdos_p_initial",
          "pdos_s_final",
          "pdos_p_final"
        ],
        "units": {
          "energy_eV": "eV",
          "pdos_s_initial": "arb.units",
          "pdos_p_initial": "arb.units",
          "pdos_s_final": "arb.units",
          "pdos_p_final": "arb.units"
        }
      },
      "description": "Projected density of states on Si 3s/3p orbitals at t=0 and t=2.5 ps for Li1.71Si at N_e=2; checker verifies peak merging upon amorphization."
    },
    {
      "file": "summary_amorphization.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LiSi": "boolean",
          "Li1.71Si": "boolean",
          "Li3.25Si": "boolean",
          "Li3.75Si": "boolean"
        }
      },
      "description": "Amorphization status of the four alloys under N_e=2 at 300 K; checker validates boolean assignments against the expected amorphization pattern."
    }
  ],
  "notes": "Scoring uses T3 structural checks: PCF long-range order loss, PDOS peak merging, and exact amorphization status pattern."
}
```

## How you are scored
Each scored output file is checked by a hidden verifier against structural criteria. For the PCF, the verifier checks the presence of sharp peaks beyond 6 Å at early times and their disappearance at later times, indicating loss of long-range order. For the pDOS, it checks whether initial multi-peak features in the Si 3s/3p channels merge into a single broad peak upon amorphization. For the amorphization summary, the verifier checks whether the assignment of amorphized vs crystalline matches the expected behavior. The overall reward is a weighted sum of the scores from these checks, rewarding correct reproduction of the amorphization pattern and the associated structural and electronic signatures.
