# Crystal Stability Comparison via d-Electron Free Energy Calculation

## Problem background
Transition metals such as vanadium, chromium, manganese, and iron exhibit a variety of crystal structures at ambient conditions, with many preferring the body-centred cubic (bcc) arrangement. The origin of this structural preference is not fully captured by simple models. In particular, the role of the partially filled d-electron bands in determining phase stability is a central question in metallurgy and condensed-matter physics. This task investigates how d-electron interactions—specifically the balance between band-broadening attraction, orbital-overlap repulsion, and electronic entropy—contribute to the relative free energies of the bcc, face-centred cubic (fcc), and hexagonal close-packed (hcp) phases in the four metals. By computing the d-electron contribution to the free energy using a well-established pair-potential formalism, we can examine whether the d-electrons alone can account for the observed low-temperature structural stability.

## Approach
The approach employs the Wills-Harrison d-electron pair potential, which expresses the effective interaction between two transition-metal atoms as a function of their separation. The potential contains three physical contributions: an attractive Friedel band-broadening term proportional to Z_d(1−Z_d/10) and R_d^3/R^5, a repulsive term arising from the non-orthogonality of muffin-tin d-orbitals proportional to Z_d R_d^6/R^8, and a weak magnetic dipole-dipole term (∝ 1/R^3). The free energy per atom is then obtained by summing this pair potential over the lattice shells and subtracting the temperature-dependent electronic entropy term, which is given by (π²/3) k_B² n_d(E_F) T at T = 300 K. The relative stability of the bcc, fcc, and ideal hcp (c/a = √(8/3)) structures is assessed by comparing their cumulative free energies per shell. Two summation schemes are used: (i) the standard nearest-neighbour approximation in which the coordination number N_c appears inside the potential prefactor, and (ii) an extended scheme that uses the actual number of atoms N on each shell. The calculation proceeds by first tabulating the lattice shells (distance and occupancy) for each structure, then evaluating the pair potential at those distances with the element-specific parameters (atomic volume, d-electron count Z_d, d-state radius R_d, and d density of states at the Fermi level n_d(E_F)), and finally accumulating the free energy shell-by-shell up to at least 12 shells. The energy differences ΔF^{fcc−bcc} and ΔF^{fcc−hcp} are then derived from the accumulated free energies.

## Reproduction target
Reproduce the d-electron free energies and the energy differences for the four elements (V, Cr, Mn, Fe) in the bcc, fcc, and ideal hcp structures. For each element and structure, compute the accumulated free energy F_d at T = 300 K as a function of shell index, using both the nearest-neighbour (N_c) and the extended (actual N) methods. From these accumulated free energies, derive the shell-resolved differences ΔF^{fcc−bcc} = F_d(fcc) − F_d(bcc) and ΔF^{fcc−hcp} = F_d(fcc) − F_d(hcp). The result should include at least 12 shells for each combination and be reported in Rydberg units. The necessary input parameters (atomic volume, Z_d, R_d, n_d(E_F)) for V, Cr, Mn, Fe are provided explicitly in the workflow steps. The structural stability can be inferred from the sign and magnitude of the energy differences; however, the primary goal is to correctly compute and report the free energies and differences per shell.

## Assets

- NumPy: numpy
- Pandas: pandas

## Workflow steps

### Step 1: Compute d-electron pair potentials
- Role: process
- Action: For each element (V, Cr, Mn, Fe), compute the d-electron pair potential U_d(R) using the Wills-Harrison formula (band-broadening attraction, orbital-overlap repulsion, dipole-dipole term) and the given input parameters (atomic volume, Z_d, R_d, n_d(E_F)). Compute over a fine grid of interatomic distances R (atomic units).
- Evidence: `/app/outputs/pair_potential_curves.json`

### Step 2: Generate lattice shell data
- Role: process
- Action: For the bcc, fcc, and ideal hcp (c/a = sqrt(8/3)) structures, generate shell distances (R in atomic units) and the number of atoms N on each shell up to at least 12 shells. Also record nearest-neighbor distances and coordination numbers.
- Evidence: `/app/outputs/lattice_shells.json`

### Step 3: Calculate accumulated free energies (Nc and extended)
- Role: scored (load-bearing)
- Action: For each element, structure, and shell, compute the accumulated d-electron free energy F_d = 0.5 * sum_{shell} U_d(R)*N - T*S_d at T = 300 K. Use two methods: (1) nearest-neighbor (Nc) where the coordination number N_c appears in the potential prefactor, and (2) extended where the actual number of atoms N on each shell is used. Write free_energies.csv.
- Output file: `/app/outputs/free_energies.csv`
- Format: csv
- Contract: CSV with columns: element (string: V, Cr, Mn, Fe), structure (string: bcc, fcc, hcp), shell (integer), method (string: Nc or extended), N_atoms (integer), interatomic_distance (float, atomic units), pair_potential_Ud (float, Rydberg), cumulative_free_energy_Fd (float, Rydberg).
- Scoring: scored by hidden verifier

### Step 4: Compute energy differences
- Role: scored
- Action: From the cumulative free energies in free_energies.csv, compute ΔF^{fcc-bcc} = F_d(fcc) - F_d(bcc) and ΔF^{fcc-hcp} = F_d(fcc) - F_d(hcp) for each element, method, and shell. Write energy_differences.csv.
- Output file: `/app/outputs/energy_differences.csv`
- Format: csv
- Contract: CSV with columns: element (string), method (string), shell (integer), delta_F_fcc_bcc (float, Rydberg), delta_F_fcc_hcp (float, Rydberg).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energies.csv`
- `/app/outputs/energy_differences.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energies.csv
- path: `/app/outputs/free_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Accumulated d-electron free energies per shell for V, Cr, Mn, Fe in bcc, fcc, hcp using nearest-neighbor and extended methods. The checker recomputes the quantities from the input parameters and lattice geometry, comparing within tolerance, and uses these to compute energy differences.
- schema:
  - `type`: table
  - `required_columns`: `element`, `structure`, `shell`, `method`, `N_atoms`, `interatomic_distance`, `pair_potential_Ud`, `cumulative_free_energy_Fd`
  - `units`:
    - `interatomic_distance`: atomic units
    - `pair_potential_Ud`: Rydberg
    - `cumulative_free_energy_Fd`: Rydberg

### energy_differences.csv
- path: `/app/outputs/energy_differences.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Energy differences ΔF^{fcc-bcc} and ΔF^{fcc-hcp} derived from the free energies. The checker recomputes these differences from free_energies.csv and verifies they are positive for all shells (up to at least 10), confirming bcc stability.
- schema:
  - `type`: table
  - `required_columns`: `element`, `method`, `shell`, `delta_F_fcc_bcc`, `delta_F_fcc_hcp`
  - `units`:
    - `delta_F_fcc_bcc`: Rydberg
    - `delta_F_fcc_hcp`: Rydberg

Notes: The checker will recompute cumulative free energies and energy differences from free_energies.csv using the given formulas and input parameters, and verify the positivity of ΔF values, all within appropriate numerical tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "structure",
          "shell",
          "method",
          "N_atoms",
          "interatomic_distance",
          "pair_potential_Ud",
          "cumulative_free_energy_Fd"
        ],
        "units": {
          "interatomic_distance": "atomic units",
          "pair_potential_Ud": "Rydberg",
          "cumulative_free_energy_Fd": "Rydberg"
        }
      },
      "description": "Accumulated d-electron free energies per shell for V, Cr, Mn, Fe in bcc, fcc, hcp using nearest-neighbor and extended methods. The checker recomputes the quantities from the input parameters and lattice geometry, comparing within tolerance, and uses these to compute energy differences."
    },
    {
      "file": "energy_differences.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "method",
          "shell",
          "delta_F_fcc_bcc",
          "delta_F_fcc_hcp"
        ],
        "units": {
          "delta_F_fcc_bcc": "Rydberg",
          "delta_F_fcc_hcp": "Rydberg"
        }
      },
      "description": "Energy differences ΔF^{fcc-bcc} and ΔF^{fcc-hcp} derived from the free energies. The checker recomputes these differences from free_energies.csv and verifies they are positive for all shells (up to at least 10), confirming bcc stability."
    }
  ],
  "notes": "The checker will recompute cumulative free energies and energy differences from free_energies.csv using the given formulas and input parameters, and verify the positivity of ΔF values, all within appropriate numerical tolerances."
}
```

## How you are scored
A hidden verifier will independently recompute the accumulated free energies and energy differences using the same formulas and input parameters, starting from the lattice shell data you generate. The verifier will compare the recomputed quantities against the values in free_energies.csv and energy_differences.csv, and will also check the consistency between the two files. Each scored artifact (free_energies.csv and energy_differences.csv) carries a portion of the total reward. The final score is a weighted combination of the scores for each artifact, reflecting how closely your computed results align with the verifier's independent recomputation and with the expected physical behaviour of the system. Reporting the paper's numerical values is not sufficient; the task demands that you actually implement the model and compute the free energies and energy differences yourself.
