# Ensemble Monte Carlo Simulation of Ultrafast Carrier Relaxation in GaAs

## Problem background
In GaAs, high‑energy photoexcitation creates electrons that rapidly transfer into upper satellite valleys (X6, X7). Non‑equilibrium longitudinal optical (LO) phonons build up during the cascade, and the interaction between intervalley scattering and this hot‑phonon population can alter energy relaxation rates. Understanding how LO phonon distributions evolve in each valley and how they feed back onto carrier dynamics is important for ultrafast semiconductor physics. The goal is to compute the time‑dependent electron populations in the four valleys and the valley‑resolved LO phonon occupation at early times, under conditions where hot‑phonon effects may be absent or present.

## Approach
Use an ensemble Monte Carlo (EMC) simulation to track the relaxation of photoexcited electrons in GaAs. The conduction band is modeled with four non‑parabolic valleys: central (Γ), L, X6, and X7, whose effective masses satisfy m_Γ* < m_L* < m_X7* < m_X6*. Include intravalley and intervalley scattering by optical and acoustic phonons (using deformation‑potential and intervalley coupling constants) and screened carrier–carrier scattering. The light‑hole band is described by a piecewise‑continuous model that switches mass at a cut‑off wavevector. Photoexcitation is simulated by adding carriers during a 500 fs laser pulse centered at 293 nm with an energy spread of 60 meV, reaching a final density of 1×10¹⁷ cm⁻³ and a total ensemble of 5000 electrons. Run the simulation for 5 ps twice: once without hot‑phonon feedback (LO phonons remain at equilibrium), and once with non‑equilibrium LO phonon populations tracked independently in each valley. From each run, record the fraction of electrons in each valley as a function of time (Step 3). From the hot‑phonon run, extract the LO phonon occupation number versus phonon wavevector magnitude q for each valley at t=2.0 ps and t=2.5 ps (Steps 4–5).

## Reproduction target
Produce three scored CSV artifacts:

- **valley_populations.csv** – time‑resolved population fractions (0–5 ps) for the Γ, L, X6, and X7 valleys, with a column indicating whether hot phonons were enabled.
- **lo_phonon_spectrum_2ps.csv** – LO phonon occupation number as a function of |q| for each valley at t=2.0 ps (hot‑phonon run).
- **lo_phonon_spectrum_2_5ps.csv** – same at t=2.5 ps.

The simulation must be implemented from scratch using public GaAs parameters from the literature. The output files must adhere to the exact column schemas defined in the Workflow steps; the verifier will use these columns to compute the score.

## Assets

- GaAs band‑structure and scattering parameters from literature

## Workflow steps

### Step 1: Assemble GaAs simulation parameters and scattering routines
- Role: process
- Action: Gather from public literature the effective masses for Γ, L, X6, X7 valleys, light‑hole band parameters, LO phonon energy, deformation potentials, and intervalley coupling constants. Implement the functions to compute scattering rates and random free‑flight time for the ensemble Monte Carlo code.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Run ensemble Monte Carlo simulation
- Role: process
- Action: Implement the full EMC simulator with 5000 electrons, excitation density 1×10¹⁷ cm⁻³, 293 nm laser, 500 fs pulse, energy spread 60 meV. Simulate for 5 ps under two conditions: (a) without hot‑phonon feedback, (b) with hot‑phonon feedback (tracking LO phonon populations per valley). Save the raw trajectory data in memory or to a temporary file.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Extract time‑dependent valley populations
- Role: scored (load-bearing)
- Action: From the simulation trajectories, compile the electron population fractions in Γ, L, X6, X7 valleys as functions of time for both hot‑phonon conditions (hot_phonons=true and false). Write to valley_populations.csv.
- Output file: `/app/outputs/valley_populations.csv`
- Format: csv
- Contract: columns: time_ps (float), N_Gamma (float), N_L (float), N_X6 (float), N_X7 (float), hot_phonons (bool)
- Scoring: scored by hidden verifier

### Step 4: Extract LO phonon spectrum at 2.0 ps
- Role: scored
- Action: From the hot‑phonon simulation, extract the LO phonon occupation number as a function of phonon wavevector magnitude q for each valley at t=2.0 ps. Write to lo_phonon_spectrum_2ps.csv.
- Output file: `/app/outputs/lo_phonon_spectrum_2ps.csv`
- Format: csv
- Contract: columns: q_inv_nm (float), N_Gamma (float), N_L (float), N_X6 (float), N_X7 (float)
- Scoring: scored by hidden verifier

### Step 5: Extract LO phonon spectrum at 2.5 ps
- Role: scored
- Action: From the hot‑phonon simulation, extract the LO phonon occupation number as a function of q for each valley at t=2.5 ps. Write to lo_phonon_spectrum_2_5ps.csv.
- Output file: `/app/outputs/lo_phonon_spectrum_2_5ps.csv`
- Format: csv
- Contract: columns: q_inv_nm (float), N_Gamma (float), N_L (float), N_X6 (float), N_X7 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/valley_populations.csv`
- `/app/outputs/lo_phonon_spectrum_2ps.csv`
- `/app/outputs/lo_phonon_spectrum_2_5ps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### valley_populations.csv
- path: `/app/outputs/valley_populations.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time‑dependent electron population fractions in the four valleys for both hot‑phonon conditions.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `N_Gamma`, `N_L`, `N_X6`, `N_X7`, `hot_phonons`
  - `units`: object

### lo_phonon_spectrum_2ps.csv
- path: `/app/outputs/lo_phonon_spectrum_2ps.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Valley‑resolved LO phonon occupation numbers vs. phonon wavevector q at t=2.0 ps.
- schema:
  - `type`: table
  - `required_columns`: `q_inv_nm`, `N_Gamma`, `N_L`, `N_X6`, `N_X7`
  - `units`:
    - `q_inv_nm`: 1/nm

### lo_phonon_spectrum_2_5ps.csv
- path: `/app/outputs/lo_phonon_spectrum_2_5ps.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Valley‑resolved LO phonon occupation numbers vs. phonon wavevector q at t=2.5 ps.
- schema:
  - `type`: table
  - `required_columns`: `q_inv_nm`, `N_Gamma`, `N_L`, `N_X6`, `N_X7`
  - `units`:
    - `q_inv_nm`: 1/nm

Notes: Structural audit checks ordering of peak q-vectors (q_Γ < q_L < q_X7 < q_X6), minimal X7 contribution, and slower X6 decay with hot phonons. Exact numerical values are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "valley_populations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "N_Gamma",
          "N_L",
          "N_X6",
          "N_X7",
          "hot_phonons"
        ],
        "units": {}
      },
      "description": "Time‑dependent electron population fractions in the four valleys for both hot‑phonon conditions."
    },
    {
      "file": "lo_phonon_spectrum_2ps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_inv_nm",
          "N_Gamma",
          "N_L",
          "N_X6",
          "N_X7"
        ],
        "units": {
          "q_inv_nm": "1/nm"
        }
      },
      "description": "Valley‑resolved LO phonon occupation numbers vs. phonon wavevector q at t=2.0 ps."
    },
    {
      "file": "lo_phonon_spectrum_2_5ps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_inv_nm",
          "N_Gamma",
          "N_L",
          "N_X6",
          "N_X7"
        ],
        "units": {
          "q_inv_nm": "1/nm"
        }
      },
      "description": "Valley‑resolved LO phonon occupation numbers vs. phonon wavevector q at t=2.5 ps."
    }
  ],
  "notes": "Structural audit checks ordering of peak q-vectors (q_Γ < q_L < q_X7 < q_X6), minimal X7 contribution, and slower X6 decay with hot phonons. Exact numerical values are not required."
}
```

## How you are scored
A hidden verifier reads your three output files and assigns a portion of the final reward to each, combined into an overall score between 0 and 1. The verifier does not require exact numerical agreement with any reference; it checks qualitative physical trends that a correctly implemented simulation should exhibit, such as relative peak locations of the LO phonon distributions across valleys, the change in distribution shape with time, and the influence of hot‑phonon feedback on valley population dynamics. Each artifact is evaluated independently, and you must produce all three files in the specified format to receive a non‑zero score. Reporting a number from memory or from a prior guess is not sufficient – the simulation must actually be run and generate physically consistent results.
