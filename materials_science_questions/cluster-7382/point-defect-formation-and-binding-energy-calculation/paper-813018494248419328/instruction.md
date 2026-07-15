# Hydrogen trapping and retention in Re-vacancy complexes in tungsten

## Problem background
Tungsten (W) is a candidate plasma-facing material in fusion reactors, but retention of hydrogen (H) isotopes under irradiation leads to blistering and performance degradation. Alloying with rhenium (Re) influences H behaviour, particularly in damaged materials where Re clusters form at radiation-induced vacancy sites. Understanding how Re atoms modify H trapping within vacancy complexes is crucial for predicting tritium inventory and material lifetime, yet the quantitative influence of Re on H retention in such complexes is not fully established.

## Approach
The study uses first-principles density-functional theory (DFT) to model defect supercells in bcc W containing substitutional Re, a mono-vacancy, and Re–vacancy (Reₘ–V) complexes with m = 1–8 Re atoms. Hydrogen atoms are placed at the most stable interstitial sites near each complex. After full geometry relaxation, total energies are obtained with an open-source plane-wave DFT code and GGA pseudopotentials. Post‑processing proceeds in four stages: (i) single‑H trapping energies of each Reₘ–V complex are computed with respect to a H atom at a tetrahedral interstitial site in pure W; (ii) the solution energy is decomposed into a mechanical contribution (lattice relaxation after H removal) and an electronic contribution; (iii) sequential trapping energies are computed for multi‑H loading in a pure mono‑vacancy, a Re₁–V complex, and a Re₄–V complex; (iv) the Polanyi–Wigner equation is applied to the sequential trapping energies, using an effective diffusion barrier and vibrational frequencies, to determine the maximum number of H atoms each vacancy type can retain at room temperature.

## Reproduction target
Produce the following four CSV files by first constructing all required supercells, running the DFT total‑energy calculations, and then performing the post‑processing analyses described in the workflow steps: (1) single‑H trapping energies for pure V and Reₘ–V complexes (m=1…8); (2) decomposition of the total solution energy into mechanical and electronic contributions for the same systems; (3) sequential trapping energies for multi‑H loading in pure V, Re₁–V, and Re₄–V; (4) the maximum number of H atoms retained at room temperature for these three vacancy types at two heating rates (1 K/s and 5 K/s). The correctness of the results is assessed by a hidden verifier that checks structural relationships among the computed quantities.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PW91 pseudopotentials (PSlibrary or SSSP): https://www.quantum-espresso.org/pseudopotentials
- Python 3 with numpy and pandas: numpy, pandas

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct atomic configurations for pure W (128-atom bcc), substitutional Re in W, a mono-vacancy, Re_m-V complexes (m = 1–8) with and without interstitial H, and reference pure W with a single H at a tetrahedral interstitial site. Use the experimental bcc W lattice constant of 2.753 Å. For Re_m-V complexes, use the ground-state configurations described in the paper's prior work (references [26,28,29]) – the solver must arrange Re atoms around the vacancy accordingly.
- Evidence: `/app/outputs/supercell_structures.zip`

### Step 2: DFT total-energy calculations
- Role: process
- Action: For each supercell from step_01, perform full geometry optimization (positions and cell volume) using an open-source DFT code with GGA-PW91 pseudopotentials, a plane-wave cutoff of 350 eV, and a k-point mesh equivalent to 3×3×3 for the 4×4×4 bcc supercell. Also compute the total energy of an isolated H₂ molecule in a large box for the reference energy. Output the final total energy and optimized atomic coordinates for each system.
- Evidence: `/app/outputs/dft_outputs.tar.gz`

### Step 3: Compute single H trapping energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in step_02, compute the trapping energy of a single H atom at each Re_m-V complex (m = 1–8) and in a pure mono-vacancy, using the definition: E_trap = E(Re_m-V-H) – E(Re_m-V) – [E(W+H_TIS) – E(W)]. For m=1, report the values for the two distinct sites (OIS-I and OIS-II). Output a CSV with columns: system, trapping_energy_eV.
- Output file: `/app/outputs/trapping_energies.csv`
- Format: csv
- Contract: CSV with columns: system (string, e.g. 'pure_V', 'Re1_V_OIS_I', 'Re1_V_OIS_II', 'Re2_V', ..., 'Re8_V'), trapping_energy_eV (float, negative values expected).
- Scoring: scored by hidden verifier

### Step 4: Decompose solution energy into mechanical and electronic contributions
- Role: scored
- Action: For each complex in step_03, compute the total solution energy E_sol = E(Re_m-V-H) – E(Re_m-V) – 0.5*E(H₂), then decompose it into mechanical contribution (MC) and electronic contribution (EC). MC is defined as the energy release when the metal lattice relaxes after removal of the H atom (i.e., the difference in total energy of the host with the relaxed geometry of the H-containing system versus that of the same host relaxed without H). EC = E_sol – MC. Output CSV with columns: system, total_solution_energy_eV, MC_eV, EC_eV.
- Output file: `/app/outputs/decomposition_energies.csv`
- Format: csv
- Contract: CSV with columns: system (same key as step_03), total_solution_energy_eV, MC_eV, EC_eV.
- Scoring: scored by hidden verifier

### Step 5: Compute sequential trapping energies for multi-H
- Role: scored
- Action: For a mono-vacancy, Re₁–V, and Re₄–V, compute the trapping energy of the n‑th H atom added, using the same definition as step_03 but for successive H atoms. Use the most stable configurations of the H‑loaded complexes as described in the text (H atoms gradually occupy OIS then shift to TIS). For V and Re₁‑V, compute up to n=12; for Re₄‑V, compute until the trapping energy becomes positive. Output CSV: system, n, trapping_energy_eV.
- Output file: `/app/outputs/sequential_trapping.csv`
- Format: csv
- Contract: CSV with columns: system ('pure_V', 'Re1_V', 'Re4_V'), n (integer 1..max), trapping_energy_eV.
- Scoring: scored by hidden verifier

### Step 6: Determine maximum H atoms at room temperature via Polanyi–Wigner
- Role: scored
- Action: Using the sequential trapping energies from step_05, a diffusion energy barrier of 0.18 eV (to convert to de‑trapping energy), and H vibrational frequencies in the range 15–35 THz (mean values per complex as reported), solve the Polanyi–Wigner equation for heating rates 1 K/s and 5 K/s to find the temperature at which the n‑th H is released. Then determine the maximum number n for which the release temperature exceeds 300 K (room temperature) for each system. Output CSV: system, heating_rate_K_per_s, max_n_H_at_RT.
- Output file: `/app/outputs/max_H_at_RT.csv`
- Format: csv
- Contract: CSV with columns: system ('pure_V', 'Re1_V', 'Re4_V'), heating_rate_K_per_s (1, 5), max_n_H_at_RT (integer).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/trapping_energies.csv`
- `/app/outputs/decomposition_energies.csv`
- `/app/outputs/sequential_trapping.csv`
- `/app/outputs/max_H_at_RT.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### trapping_energies.csv
- path: `/app/outputs/trapping_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Single H trapping energies in pure mono-vacancy and Re_m-V complexes (m=1..8). For Re1-V, includes separate rows for OIS-I and OIS-II. The checker verifies structural trends: Re1-V and Re2-V energies close to pure V, and for m>=3 monotonic increase.
- schema:
  - `required_columns`: `system`, `trapping_energy_eV`
  - `units`:
    - `trapping_energy_eV`: eV

### decomposition_energies.csv
- path: `/app/outputs/decomposition_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total solution energy and its mechanical (MC) and electronic (EC) contributions for the same H sites as in step_03. The checker verifies electronic dominance: EC variation from m=1 to m=8 >0.25 eV, while MC variation <0.05 eV.
- schema:
  - `required_columns`: `system`, `total_solution_energy_eV`, `MC_eV`, `EC_eV`
  - `units`:
    - `total_solution_energy_eV`: eV
    - `MC_eV`: eV
    - `EC_eV`: eV

### sequential_trapping.csv
- path: `/app/outputs/sequential_trapping.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Sequential trapping energies for multi-H loading in pure mono-vacancy, Re1-V, and Re4-V. The checker verifies that trapping energy increases (becomes less negative) with n.
- schema:
  - `required_columns`: `system`, `n`, `trapping_energy_eV`
  - `units`:
    - `trapping_energy_eV`: eV

### max_H_at_RT.csv
- path: `/app/outputs/max_H_at_RT.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Maximum number of H atoms retained at room temperature for each vacancy type and heating rate. The checker verifies ordering: max_n_H_at_RT(pure_V) > max_n_H_at_RT(Re1_V) > max_n_H_at_RT(Re4_V), with tolerances.
- schema:
  - `required_columns`: `system`, `heating_rate_K_per_s`, `max_n_H_at_RT`
  - `units`:
    - `max_n_H_at_RT`: integer count

Notes: All scored artifacts are produced from the DFT results of step_02 and post-processing. The checker will perform structural audits (trends, monotonicity, ordering) using hidden reference values derived from the paper. No exact numeric match is required; relative trends absorb systematic DFT code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "trapping_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "system",
          "trapping_energy_eV"
        ],
        "units": {
          "trapping_energy_eV": "eV"
        }
      },
      "description": "Single H trapping energies in pure mono-vacancy and Re_m-V complexes (m=1..8). For Re1-V, includes separate rows for OIS-I and OIS-II. The checker verifies structural trends: Re1-V and Re2-V energies close to pure V, and for m>=3 monotonic increase."
    },
    {
      "file": "decomposition_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "system",
          "total_solution_energy_eV",
          "MC_eV",
          "EC_eV"
        ],
        "units": {
          "total_solution_energy_eV": "eV",
          "MC_eV": "eV",
          "EC_eV": "eV"
        }
      },
      "description": "Total solution energy and its mechanical (MC) and electronic (EC) contributions for the same H sites as in step_03. The checker verifies electronic dominance: EC variation from m=1 to m=8 >0.25 eV, while MC variation <0.05 eV."
    },
    {
      "file": "sequential_trapping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "system",
          "n",
          "trapping_energy_eV"
        ],
        "units": {
          "trapping_energy_eV": "eV"
        }
      },
      "description": "Sequential trapping energies for multi-H loading in pure mono-vacancy, Re1-V, and Re4-V. The checker verifies that trapping energy increases (becomes less negative) with n."
    },
    {
      "file": "max_H_at_RT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_columns": [
          "system",
          "heating_rate_K_per_s",
          "max_n_H_at_RT"
        ],
        "units": {
          "max_n_H_at_RT": "integer count"
        }
      },
      "description": "Maximum number of H atoms retained at room temperature for each vacancy type and heating rate. The checker verifies ordering: max_n_H_at_RT(pure_V) > max_n_H_at_RT(Re1_V) > max_n_H_at_RT(Re4_V), with tolerances."
    }
  ],
  "notes": "All scored artifacts are produced from the DFT results of step_02 and post-processing. The checker will perform structural audits (trends, monotonicity, ordering) using hidden reference values derived from the paper. No exact numeric match is required; relative trends absorb systematic DFT code differences."
}
```

## How you are scored
A hidden verifier reads each of the four scored CSV artifacts and evaluates the reported values against hidden structural criteria derived from the expected physical behaviour. The verifier checks, for example, that certain trapping energies are approximately invariant across systems with similar local environments, that energy differences obey monotonic trends with increasing Re count, that the electronic contribution dominates over the mechanical contribution in specific regimes, and that the maximum H atom count at room temperature is consistent with the relative magnitudes of the sequential trapping energies. Exact numerical agreement with any external reference is not required; instead, the verifier confirms that the relationships among your computed numbers follow the physical trends implied by the system composition and H loading. The total reward is a weighted sum across the four stages, with the single‑H trapping energies and the Polanyi–Wigner retention analysis carrying the largest weight.
