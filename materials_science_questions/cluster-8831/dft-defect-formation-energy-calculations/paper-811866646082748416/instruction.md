# Pseudopotential Linear‑Response Calculation of Defect Formation Energies in FCC Metals

## Problem background
Point defects such as vacancies and interstitials govern diffusion and mechanical properties in metals. This work addresses the calculation of formation energies for monovacancies and non‑split interstitials (octahedral, tetrahedral, crowdion) in the fcc metals Cu, Ag, Au, and Pb, as well as the changes in these energies when a substitutional or interstitial impurity is introduced. The study employs three different pseudopotential‑exchange‑correlation combinations: Ashcroft‑Taylor with a standard core radius (AT), Ashcroft‑Taylor with a core radius fitted to the experimental vacancy formation energy (ATF), and Heine‑Abarenkov‑Taylor (HAT). The target of the reproduction is to compute these defect energies and the impurity‑modified energies from scratch using the Harrison linear‑response formalism, and to examine how the choice of pseudopotential affects the numerical results.

## Approach
The Harrison linear‑response pseudopotential theory is used. A defect in the lattice changes the structure‑dependent energy; the defect formation energy is obtained as the difference between the energy after defect creation and the energy of the perfect lattice, both expressed in terms of a host energy kernel U(q).

For a pure metal, the kernel U(q) is

$$
U(q) = \lim_{\eta\to\infty} \frac{2\pi e^{2} Z_H^{2}}{\Omega_H q^{2}} e^{-q^{2}/(4\eta)}
       + \big[\omega_H(q)\big]^{2} \varepsilon_H(q) \chi_H(q)
$$

where $\omega_H(q)$ is the pseudopotential, $\varepsilon_H(q)$ the dielectric function, and $\chi_H(q)$ the perturbation characteristic. For an impurity system, the difference kernel is

$$
\Delta U(q) = \lim_{\eta\to\infty} \frac{2\pi e^{2}(Z_I-Z_H)}{\Omega_H q^{2}} e^{-q^{2}/(4\eta)}
              + \big[\omega_I(q)-\omega_H(q)\big]\, \omega_H(q)\,\varepsilon_H(q)\,\chi_H(q).
$$

The pseudopotentials used are:
- Ashcroft empty‑core model:
  $\displaystyle \omega^{\rm Ashcroft}(q) = -\frac{4\pi Z e^{2}}{\Omega q^{2}} \cos(q r_c)$
- Heine‑Abarenkov model:
  $\displaystyle \omega^{\rm Heine-Abarenkov}(q) = \frac{4\pi A}{\Omega q^{3}}\big[q r_m \cos(q r_m)-\sin(q r_m)\big]
        - \frac{4\pi Z e^{2}}{\Omega q^{2}} \cos(q r_m)$

Taylor’s exchange‑correlation function is
$\displaystyle f^{\rm Taylor}(q) = \frac{q^{2}}{4 k_F^{2}}\left(1+\frac{0.1534}{\pi k_F}\right).$

Defect formation energies are then obtained by evaluating lattice sums and integrals:
- Monovacancy formation energy:
  $\displaystyle E_{FH}^{1v} = \sum_{q_0}' \frac{q_0}{3} \frac{\partial U(q_0)}{\partial q_0}
                            + \frac{\Omega_H}{2\pi^2} \int_0^\infty U(q)\,q^{2} dq$
- Interstitial formation energy (for site $\vec r_i$):
  $\displaystyle E_{FH}^{1t} = \sum_{q_0}' \Big[2(\cos\vec q_0\!\cdot\!\vec r_i -1)U(q_0)-
                            \frac{q_0}{3}\frac{\partial U(q_0)}{\partial q_0}\Big]
                            + \frac{\Omega_H}{2\pi^2} \int_0^\infty U(q)\,q^{2} dq$
- Vacancy‑impurity binding energy:
  $\displaystyle \Delta E_F^{v} = -\frac{\Omega_H}{\pi^2}
                            \int_0^\infty \frac{\sin(q|\vec r_v-\vec r_I|)}{q|\vec r_v-\vec r_I|}
                            \Delta U(q)\,q^{2} dq$
- Change in interstitial formation energy due to an impurity:
  $\displaystyle \Delta E_F^{t} = \sum_{q_0}' 2(\cos\vec q_0\!\cdot\!\vec r_i -1)\,\Delta U(q_0)
                            + \frac{\Omega_H}{\pi^2} \int_0^\infty \Delta U(q)\,q^{2} dq$

The sum $\sum_{q_0}'$ runs over the discrete reciprocal lattice vectors $q_0$ of the host; the integral over $q$ is performed on a quasi‑continuous grid. For the ATF combination the Ashcroft core radius $r_c$ is optimized so that the computed monovacancy formation energy matches the experimental value (provided in the host data) for each metal.

The approach is to write a numerical implementation of these expressions, using the host parameters (valence $Z$, lattice constant $a$, atomic volume $\Omega$, Fermi wave‑vector $k_F$, Fermi energy $\varepsilon_F$, and pseudopotential parameters) supplied for Cu, Ag, Au, and Pb. The two main outputs are tables of defect formation energies and of impurity‑induced energy changes, computed for all metals, all pseudopotential combinations, and all binary systems.

## Reproduction target
Compute, from first principles, the monovacancy formation energies $E_{FH}^{1v}$ and the non‑split interstitial formation energies $E_{FH}^{1t}$ for octahedral, tetrahedral, and crowdion sites in the four fcc metals Cu, Ag, Au, and Pb. Perform the calculations for each of the three pseudopotential combinations: AT (standard Ashcroft core radius), ATF (Ashcroft radius fitted to experimental $E_{FH}^{1v}$), and HAT (Heine‑Abarenkov model).

Additionally, compute for the twelve binary systems (each metal as host with the other three as impurities) the vacancy‑impurity binding energies $\Delta E_F^{v}$ and the changes in interstitial formation energies $\Delta E_F^{t}$ for the same three interstitial sites, again for the AT, ATF, and HAT combinations.

Produce two CSV files:
- `table2_formation_energies.csv` with the formation energies for all metals and all interstitial types.
- `table3_binding_energies.csv` with the impurity‑induced energy changes for all binary systems.

For Cu, Ag, and Au under the ATF and HAT combinations, the computed interstitial formation energies must satisfy the structural ordering $E_{\rm octahedral} < E_{\rm tetrahedral} < E_{\rm crowdion}$. This ordering is a required structural check.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Prepare host parameters and numerical grids
- Role: process
- Action: Define FCC lattice parameters for Cu, Ag, Au, Pb using host data (Z, a, Ω, k_F, ε_F). Generate reciprocal lattice wave numbers q0 for each metal and set up integration grid for quasi‑continuous q.
- Evidence: `/app/outputs/grid_info.csv`

### Step 2: Fit Ashcroft core radius to experimental vacancy formation energy
- Role: process
- Action: Implement the monovacancy formation energy expression using the Ashcroft pseudopotential and Taylor exchange‑correlation. For each metal, optimize the core radius r_c so that the computed E_FH^1v matches the experimental target (Cu 0.0831, Ag 0.0750, Au 0.0662, Pb 0.0426 Rydbergs). Record the fitted r_c (ATF parameter) for each metal.
- Evidence: `/app/outputs/fitted_rc.csv`

### Step 3: Compute host energy kernel U(q)
- Role: process
- Action: Evaluate the host energy kernel function U(q) for each metal (Cu, Ag, Au, Pb) and each pseudopotential combination (AT, ATF, HAT) using the appropriate pseudopotential parameters and Taylor exchange‑correlation on the integration q‑grid.
- Evidence: `/app/outputs/uq_kernel.npz`

### Step 4: Compute defect formation energies (E_FH^1v and E_FH^1t)
- Role: scored (load-bearing)
- Action: Using U(q) from step_03, compute monovacancy formation energy via the lattice‑sum and integral expression, and interstitial formation energies for octahedral, tetrahedral, and crowdion sites using the interstitial position vectors in the FCC lattice. Output a CSV with columns Metal, Type (Monovacancy/Octahedral/Tetrahedral/Crowdion), Combination (AT/ATF/HAT), and Energy_Rydbergs.
- Output file: `/app/outputs/table2_formation_energies.csv`
- Format: csv
- Contract: Columns: Metal (str), Type (Monovacancy|Octahedral|Tetrahedral|Crowdion), Combination (AT|ATF|HAT), Energy_Rydbergs (float)
- Scoring: scored by hidden verifier

### Step 5: Compute impurity–host kernel difference ΔU(q)
- Role: process
- Action: Evaluate the impurity‑host kernel difference ΔU(q) for each of the 12 binary systems (Cu, Ag, Au, Pb as hosts and impurities) using the host and impurity pseudopotential parameters.
- Evidence: `/app/outputs/delta_u_kernel.npz`

### Step 6: Compute binding and change energies (ΔE_F^v and ΔE_F^t)
- Role: scored (load-bearing)
- Action: Using ΔU(q) from step_05 and the nearest‑neighbour distance for each host, compute vacancy‑impurity binding energy ΔE_F^v via the integral expression. Compute interstitial impurity formation energy changes ΔE_F^t for octahedral, tetrahedral, and crowdion sites using the lattice‑sum and integral expression. Output a CSV with columns System, EnergyType, Combination, and Energy_Rydbergs for all 12 binary systems and all pseudopotential combinations.
- Output file: `/app/outputs/table3_binding_energies.csv`
- Format: csv
- Contract: Columns: System (str, e.g., CuAg), EnergyType (Delta_E_F^v | Delta_E_F^t_Octahedral | Delta_E_F^t_Tetrahedral | Delta_E_F^t_Crowdion), Combination (AT|ATF|HAT), Energy_Rydbergs (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table2_formation_energies.csv`
- `/app/outputs/table3_binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table2_formation_energies.csv
- path: `/app/outputs/table2_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Defect formation energies (monovacancy and non‑split interstitials) computed for Cu, Ag, Au, Pb under three pseudopotential combinations. Includes structural ordering verification for Cu, Ag, Au under ATF and HAT.
- schema:
  - `type`: table
  - `required_columns`: `Metal`, `Type`, `Combination`, `Energy_Rydbergs`
  - `units`:
    - `Energy_Rydbergs`: Rydbergs

### table3_binding_energies.csv
- path: `/app/outputs/table3_binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Change in defect formation energies upon impurity introduction (vacancy‑impurity binding and interstitial impurity changes) for all binary systems.
- schema:
  - `type`: table
  - `required_columns`: `System`, `EnergyType`, `Combination`, `Energy_Rydbergs`
  - `units`:
    - `Energy_Rydbergs`: Rydbergs

Notes: The ATF combination requires the agent to fit the Ashcroft core radius to experimental vacancy formation energies as an integral part of the workflow. Experimental reference values are provided only for the fitting step. All energies are in Rydbergs (1 Ry = 13.6057 eV). The checker will compare values against hidden paper‑reported references with appropriate tolerances and verify ordering trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table2_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Metal",
          "Type",
          "Combination",
          "Energy_Rydbergs"
        ],
        "units": {
          "Energy_Rydbergs": "Rydbergs"
        }
      },
      "description": "Defect formation energies (monovacancy and non‑split interstitials) computed for Cu, Ag, Au, Pb under three pseudopotential combinations. Includes structural ordering verification for Cu, Ag, Au under ATF and HAT."
    },
    {
      "file": "table3_binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "EnergyType",
          "Combination",
          "Energy_Rydbergs"
        ],
        "units": {
          "Energy_Rydbergs": "Rydbergs"
        }
      },
      "description": "Change in defect formation energies upon impurity introduction (vacancy‑impurity binding and interstitial impurity changes) for all binary systems."
    }
  ],
  "notes": "The ATF combination requires the agent to fit the Ashcroft core radius to experimental vacancy formation energies as an integral part of the workflow. Experimental reference values are provided only for the fitting step. All energies are in Rydbergs (1 Ry = 13.6057 eV). The checker will compare values against hidden paper‑reported references with appropriate tolerances and verify ordering trends."
}
```

## How you are scored
A hidden verifier independently examines the two CSV files you produce. It compares each energy value you report against reference values (derived from the original study) within a prescribed tolerance. For the formation energies in `table2_formation_energies.csv`, the verifier also checks that the structural ordering octahedral < tetrahedral < crowdion holds for Cu, Ag, and Au under the ATF and HAT combinations.

The final reward is proportional to the fraction of values that lie within tolerance and pass the structural checks; systematic offsets from the reference reduce the reward. No credit is given for merely reporting numbers – you must carry out the full workflow, including fitting the ATF core radius and evaluating all lattice sums and integrals, for your results to be considered valid.
