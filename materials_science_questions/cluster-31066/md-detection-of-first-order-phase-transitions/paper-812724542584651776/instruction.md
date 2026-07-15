# Confinement-Induced Liquid-Solid Phase Transition Detection via Molecular Dynamics

## Problem background
When water is confined between hydrophobic surfaces at nanoscale separations, it can exhibit liquid-solid phase transitions that are not observed in the bulk. This task investigates the thermodynamics of such confined water using molecular dynamics simulations. The focus is on computing the slopes of the liquid-solid phase boundaries in the confined system via the Clapeyron relations, which link changes in temperature, lateral pressure, and wall separation to differences in entropy, volume, and solvation pressure between coexisting phases.

## Approach
Constant-lateral-pressure (NPxxT) molecular dynamics simulations of TIP4P water between two parallel hydrophobic (9-3 Lennard-Jones) walls are performed at a fixed temperature and lateral pressure. The wall-wall separation H is systematically varied, and for each H the normal pressure Pzz, internal energy U, lateral area A, and particle number N are recorded. Per-particle quantities—entropy, volume, area, and the product aΔP—are computed. Phase transitions are identified by locating abrupt changes in Pzz and energy as H is changed. For each stable phase, the mean values of these per-particle quantities are obtained, and the confined-system Clapeyron equations are used to calculate the slopes of the phase boundaries in the Pxx–T, Pxx–H, and H–T planes for every observed liquid-solid transition.

## Reproduction target
Produce the per-H thermodynamic data from the NPxxT MD simulations and, from that data, compute the three Clapeyron slopes (dT/dPxx, dPxx/dH, dH/dT) for each of the two liquid-solid phase transitions that occur between the thick liquid (α), bilayer amorphous solid (β), and thin liquid (γ) phases of confined TIP4P water. The results are reported as a CSV of simulation state variables and a JSON file containing the six slope values.

## Assets

- TIP4P water model parameters: https://doi.org/10.1063/1.445869
- 9-3 Lennard-Jones wall-water interaction parameters (hydrophobic surface): https://doi.org/10.1063/1.467147
- LAMMPS molecular dynamics package (or equivalent open-source MD engine): https://www.lammps.org/

## Workflow steps

### Step 1: Run NPxxT MD simulations and produce per-H thermodynamic data
- Role: scored
- Action: Perform constant-lateral-pressure (NPxxT) molecular dynamics simulations of TIP4P water confined between two parallel hydrophobic (9-3 Lennard-Jones) walls at T=270 K and Pxx=0.1 MPa with N=240 molecules. Vary the wall-wall separation H from 10.0 Å down to 6.5 Å in steps of 0.1 Å, then back up to 10.0 Å. For each H, after equilibration run production and record the average normal pressure Pzz, total internal energy U, lateral area A, and number of molecules N. Compute per-particle quantities: entropy s approximated by (u - Pxx v)/T (with u=U/N), volume v=Ah/N, area a=A/N, and aΔP = a*(Pzz - Pxx). Save all rows in the output CSV.
- Output file: `/app/outputs/step_01_simulation_data.csv`
- Format: csv
- Contract: CSV with columns: H (float, Å), Pzz (float, MPa), u (float, kJ/mol), s (float, J/mol/K), v (float, Å³), a (float, Å²), aDP (float, Å² MPa). One row per H value; rows can be from compression and expansion runs.
- Scoring: scored by hidden verifier

### Step 2: Identify phase transitions and compute Clapeyron slopes
- Role: scored (load-bearing)
- Action: Read the simulation data CSV. Identify the three phases (thick liquid α, bilayer amorphous solid β, thin liquid γ) by locating H regions where Pzz and energy show abrupt changes on compression. Determine the rows belonging to each phase and compute the mean of s, v, and aΔP for each phase. Use the Clapeyron equations for the confined NPxxT ensemble to calculate the three coexistence slopes (dT/dPxx, dPxx/dH, dH/dT) for the α→β transition and for the β→γ transition. Output a JSON file with the six slope values.
- Output file: `/app/outputs/step_02_phase_boundaries.json`
- Format: json
- Contract: JSON object with keys 'alpha_beta' and 'beta_gamma'. Each key maps to an object with keys 'dT_dPxx' (float, K/MPa), 'dPxx_dH' (float, MPa/Å), 'dH_dT' (float, Å/K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_simulation_data.csv`
- `/app/outputs/step_02_phase_boundaries.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_simulation_data.csv
- path: `/app/outputs/step_01_simulation_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw thermodynamic data from NPxxT MD simulations; checked for first-order phase transition signatures (discontinuous drops in Pzz) on compression.
- schema:
  - `type`: table
  - `required_columns`: `H`, `Pzz`, `u`, `s`, `v`, `a`, `aDP`
  - `units`:
    - `H`: Å
    - `Pzz`: MPa
    - `u`: kJ/mol
    - `s`: J/mol/K
    - `v`: Å³
    - `a`: Å²
    - `aDP`: Å² MPa

### step_02_phase_boundaries.json
- path: `/app/outputs/step_02_phase_boundaries.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Clapeyron slopes for the α→β and β→γ liquid-solid phase boundaries of confined water; the checker compares the reported slopes to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `alpha_beta`: object with keys dT_dPxx, dPxx_dH, dH_dT
    - `beta_gamma`: object with keys dT_dPxx, dPxx_dH, dH_dT
  - `items`:
    - `dT_dPxx`: K/MPa
    - `dPxx_dH`: MPa/Å
    - `dH_dT`: Å/K

Notes: The step_02 Clapeyron slopes are scored by reference match against hidden gold values. The step_01 CSV is audited for phase-transition signatures. The NPT solvation force curves are not scored as a separate artifact because the main quantitative reproduction target (phase boundary slopes) is fully captured by the NPxxT system, and scoring the qualitative force curves would require leaking the exact figure values from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_simulation_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "H",
          "Pzz",
          "u",
          "s",
          "v",
          "a",
          "aDP"
        ],
        "units": {
          "H": "Å",
          "Pzz": "MPa",
          "u": "kJ/mol",
          "s": "J/mol/K",
          "v": "Å³",
          "a": "Å²",
          "aDP": "Å² MPa"
        }
      },
      "description": "Raw thermodynamic data from NPxxT MD simulations; checked for first-order phase transition signatures (discontinuous drops in Pzz) on compression."
    },
    {
      "file": "step_02_phase_boundaries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha_beta": "object with keys dT_dPxx, dPxx_dH, dH_dT",
          "beta_gamma": "object with keys dT_dPxx, dPxx_dH, dH_dT"
        },
        "items": {
          "dT_dPxx": "K/MPa",
          "dPxx_dH": "MPa/Å",
          "dH_dT": "Å/K"
        }
      },
      "description": "Clapeyron slopes for the α→β and β→γ liquid-solid phase boundaries of confined water; the checker compares the reported slopes to hidden reference values."
    }
  ],
  "notes": "The step_02 Clapeyron slopes are scored by reference match against hidden gold values. The step_01 CSV is audited for phase-transition signatures. The NPT solvation force curves are not scored as a separate artifact because the main quantitative reproduction target (phase boundary slopes) is fully captured by the NPxxT system, and scoring the qualitative force curves would require leaking the exact figure values from the paper."
}
```

## How you are scored
A hidden verifier independently evaluates the artifacts from each workflow step. The simulation data CSV (Step 1) is audited for signatures of first-order phase transitions—specifically, abrupt drops in normal pressure Pzz on compression in the expected separation ranges. The phase boundary JSON (Step 2) is scored by recomputing the six Clapeyron slopes directly from the per-H data you supply: the verifier identifies the phases, computes per-phase averages, calculates the slopes using the confined-system Clapeyron equations, and compares the results against reference values. The final reward is a weighted combination of the scores from these stages. Providing the correct simulation data and accurately derived slopes is necessary; reporting plausible numbers without correctly executed simulations and phase identification will not pass.
