# Monte Carlo Simulation of Spin Reorientation Transition in Ultrathin Magnetic Films

## Problem background
Ultrathin magnetic films can exhibit a spin reorientation transition (SRT), where the net magnetization direction switches from in-plane to out-of-plane as the temperature is lowered. Around the SRT temperature, an abrupt drop in magnetization is observed experimentally — a phenomenon called a pseudogap. For large-area films, complex magnetic domains are known to cause this pseudogap, but it is unclear whether a similar effect can arise in smaller, single-domain films purely from dynamical fluctuations. The question is whether such a film can enter a superparamagnetic state at the SRT temperature, characterized by large fluctuations of the magnetization direction while the magnetization magnitude remains nonzero. Answering this requires computing the temperature dependence of the magnetization components and the free-energy landscape as a function of perpendicular and in-plane magnetization.

## Approach
The system is modeled as a classical Heisenberg spin Hamiltonian on a square lattice with ferromagnetic exchange, long-range dipolar interactions, and uniaxial perpendicular anisotropy. The simulations use a Monte Carlo (Metropolis) cooling protocol to obtain thermal averages of the perpendicular and in-plane magnetizations as functions of temperature. The spin reorientation temperature (TSRT) is identified as the temperature where the two magnetization components cross. To characterize the state at TSRT, the free-energy as a function of the two magnetizations is computed via a Wang-Landau algorithm combined with the stochastic cutoff method, which efficiently handles dipolar interactions. The free-energy landscape reveals whether the system explores a broad region of magnetization space at the transition, indicating superparamagnetic behavior.

## Reproduction target
For a specific parameter set (J=1, C_d/J=0.028, C_u/J=0.2) on a 32×32×1 lattice with open boundaries:
1. Produce the temperature-dependent perpendicular magnetization m_perp and in-plane magnetization m_par from cooling Monte Carlo simulations (T=2.0 J down to 0.025 J in steps of 0.025 J), averaged over 10 independent runs. Output: `magnetization_curve.csv`.
2. Determine the spin reorientation transition temperature TSRT (in units of J) as the temperature where m_perp = m_par, using the magnetization curve. Output: `TSRT.txt`.
3. At TSRT, compute the free-energy difference F_diff = F(m_perp,m_par) - F_min on a grid covering (m_perp, m_par) space, using Wang-Landau with stochastic cutoff, averaged over 10 independent runs. Output: `free_energy_landscape.csv`.

## Assets
This is a compute-driven reproduction: all required inputs (model Hamiltonian, lattice, parameter values, and simulation protocols) are fully specified in the workflow. No external datasets, pre-trained models, or proprietary software are needed. The agent may use standard open-source scientific Python packages (e.g., numpy, scipy) to implement the simulations.

## Workflow steps

### Step 1: Cooling-protocol MC simulation for magnetization curve
- Role: scored
- Action: Implement the Hamiltonian for a classical Heisenberg model with exchange, dipolar, and uniaxial anisotropy on a 32x32x1 square lattice with open boundaries. Use parameters J=1, C_d=0.028, C_u=0.2. Initialize spins randomly. For each temperature T from 2.0 J down to 0.025 J in steps of 0.025 J, run 100,000 Metropolis Monte Carlo steps, using the last 50,000 steps to compute thermal averages of perpendicular magnetization m_perp = (1/N)|∑ S_i^z| and in-plane magnetization m_par = (1/N) sqrt((∑ S_i^x)^2 + (∑ S_i^y)^2), where N=1024. Repeat the full cooling protocol for 10 independent runs and average. Write the averaged m_perp and m_par for each temperature to magnetization_curve.csv.
- Output file: `/app/outputs/magnetization_curve.csv`
- Format: csv
- Contract: columns: T (float, units of J), m_perp (float, dimensionless), m_par (float, dimensionless). Each row corresponds to one temperature step.
- Scoring: scored by hidden verifier

### Step 2: Determine SRT temperature from magnetization curve
- Role: scored
- Action: Read magnetization_curve.csv. Identify the temperature at which m_perp and m_par cross: find the two consecutive temperature points where (m_perp - m_par) changes sign, and linearly interpolate to find T where m_perp = m_par. Write this temperature to TSRT.txt.
- Output file: `/app/outputs/TSRT.txt`
- Format: txt
- Contract: A single float value representing T_SRT in units of J.
- Scoring: scored by hidden verifier

### Step 3: Wang-Landau free-energy calculation at T_SRT
- Role: scored
- Action: Implement the Wang-Landau algorithm combined with the stochastic cutoff (SCO) method for dipolar interactions. Use initial ΔF=1, halve ΔF 20 times to 2^{-20}. Divide the (m_perp,m_par) space into bins of size 0.01×0.01 covering [0,0.85]×[0,0.85] such that sqrt(m_perp^2+m_par^2) ≤ 0.85. Check histogram flatness every 10,000 MC steps (all bins ≥ 80% of average count). Switch SCO every 10 MC steps. Use the case 2 parameters (J=1, C_d=0.028, C_u=0.2) and the lattice. Run the free-energy measurement at the temperature T_SRT read from TSRT.txt. Perform 10 independent runs and average the free-energy. Output the free-energy difference F_diff = F(m_perp,m_par) - F_min for every bin to free_energy_landscape.csv.
- Output file: `/app/outputs/free_energy_landscape.csv`
- Format: csv
- Contract: columns: m_perp_bin (float, bin center), m_par_bin (float, bin center), F_diff (float, units of J). Covers all bins with 0 <= m_perp <= 0.85, 0 <= m_par <= 0.85, step 0.01, subject to (m_perp^2+m_par^2)^0.5 <= 0.85.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_curve.csv`
- `/app/outputs/TSRT.txt`
- `/app/outputs/free_energy_landscape.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_curve.csv
- path: `/app/outputs/magnetization_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent perpendicular and in-plane magnetizations; the hidden checker recomputes T_SRT from this data and verifies monotonic trends.
- schema:
  - `type`: table
  - `required_columns`: `T`, `m_perp`, `m_par`
  - `units`:
    - `T`: J
    - `m_perp`: dimensionless
    - `m_par`: dimensionless

### TSRT.txt
- path: `/app/outputs/TSRT.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: The agent-reported SRT temperature; the checker recomputes T_SRT from magnetization_curve.csv and compares it to this value with a hidden tolerance.
- schema:
  - `type`: other
  - `description`: A single float value in units of J.

### free_energy_landscape.csv
- path: `/app/outputs/free_energy_landscape.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Free-energy landscape at T_SRT; the checker verifies that the low free-energy region (F_diff ≤ T_SRT) spans both perpendicular-dominated and in-plane-dominated magnetization states.
- schema:
  - `type`: table
  - `required_columns`: `m_perp_bin`, `m_par_bin`, `F_diff`
  - `units`:
    - `m_perp_bin`: dimensionless
    - `m_par_bin`: dimensionless
    - `F_diff`: J

Notes: All outputs are expected to be generated by the agent from the described simulations. The checker will not require external datasets; it will recompute quantities from the agent's artifacts and compare them against hidden reference values derived from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "m_perp",
          "m_par"
        ],
        "units": {
          "T": "J",
          "m_perp": "dimensionless",
          "m_par": "dimensionless"
        }
      },
      "description": "Temperature-dependent perpendicular and in-plane magnetizations; the hidden checker recomputes T_SRT from this data and verifies monotonic trends."
    },
    {
      "file": "TSRT.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "other",
        "description": "A single float value in units of J."
      },
      "description": "The agent-reported SRT temperature; the checker recomputes T_SRT from magnetization_curve.csv and compares it to this value with a hidden tolerance."
    },
    {
      "file": "free_energy_landscape.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "m_perp_bin",
          "m_par_bin",
          "F_diff"
        ],
        "units": {
          "m_perp_bin": "dimensionless",
          "m_par_bin": "dimensionless",
          "F_diff": "J"
        }
      },
      "description": "Free-energy landscape at T_SRT; the checker verifies that the low free-energy region (F_diff ≤ T_SRT) spans both perpendicular-dominated and in-plane-dominated magnetization states."
    }
  ],
  "notes": "All outputs are expected to be generated by the agent from the described simulations. The checker will not require external datasets; it will recompute quantities from the agent's artifacts and compare them against hidden reference values derived from the paper."
}
```

## How you are scored
A hidden verifier independently checks each of your three scored artifacts. From `magnetization_curve.csv` it recomputes the SRT temperature and verifies the expected monotonic trends. It compares the recomputed value with your `TSRT.txt`. It also performs a structural audit on `free_energy_landscape.csv` to confirm that the low-free-energy region spans both perpendicular-dominated and in-plane-dominated states. The final reward is a weighted combination of these checks. Simply writing a paper-reported number without producing the required raw artifacts will not pass the verification.
