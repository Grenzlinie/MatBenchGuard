# DFT Defect Formation Energies for N Interstitials and Mg-Ga Complexes in GaN

## Problem background
Gallium nitride (GaN) is a technologically important wide-bandgap semiconductor used in optical and electronic devices. Native point defects such as nitrogen interstitials (N_I) can degrade device performance by acting as traps or compensating dopants. This task investigates the local-energy-minimum configurations, formation energies, and binding energies of N interstitials and their complexes with substitutional Mg acceptors in p-type GaN, using density-functional theory (DFT) with the generalized gradient approximation (GGA). The results should quantify the formation energies as functions of the Fermi level and the binding energies for the Mg_Ga N_I complexes, which are essential for understanding defect behavior under non-equilibrium conditions such as irradiation or ion implantation.

## Approach
The study uses DFT calculations within the GGA as formulated by Perdew and Wang (PW91). A 72-atom supercell of wurtzite GaN is constructed with the DFT-GGA lattice constants a=3.207 Å and c=5.223 Å. The Brillouin zone is sampled with a 2×2×2 Monkhorst-Pack k-point mesh, and the plane-wave basis is set with a kinetic-energy cutoff of 366 eV. Ultrasoft pseudopotentials are used, treating Ga 3d and Mg 2p electrons as valence.

Reference cohesive energies are computed for bulk wurtzite GaN (per formula unit), orthorhombic Ga (per atom), an isolated N₂ molecule (per atom), and cubic Mg₃N₂ (per formula unit). These are used to define chemical potentials under Ga-rich conditions.

The same computational setup is applied to supercells containing nitrogen interstitials in three distinct local-energy-minimum configurations (type-I split, type-II split, and channel-centered) for a range of charge states, and to supercells containing Mg_Ga N_I complexes formed by replacing a near-neighbor Ga atom with Mg around each split-interstitial orientation, in several charge states.

The formation energy of each defect is obtained from the cohesive energy of the defective supercell, the stoichiometrically weighted chemical potentials of the atomic species, and a charge-state term that depends linearly on the Fermi level. The binding energy of an Mg_Ga N_I complex is the energy gained when an isolated Mg_Ga^- acceptor and an isolated N_I with the appropriate charge combine to form the complex.

## Reproduction target
Your primary goal is to compute the cohesive energies for all required bulk and defect systems and collect them in the file `/app/outputs/cohesive_energies.csv`. The file must contain entries for bulk GaN, Ga, N₂, Mg₃N₂, and for every N interstitial configuration and charge state (type-I split, type-II split, channel-centered in the charge states listed in the workflow steps) as well as every Mg_Ga N_I complex configuration and charge state. From these raw cohesive energies, the hidden checker will derive formation energies as a function of the Fermi level and binding energies for the complexes, and will verify that the resulting formation-energy trends (e.g., relative stability among configurations as the Fermi level varies, correct ordering by charge state) and the binding energies are consistent with independent reference data. The reproduction is considered successful if the derived quantities fall within acceptable physical bounds and exhibit the expected structural relations, without requiring you to compute or report formation energies directly.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Pseudopotentials for Ga, N, Mg (PW91 GGA, ultrasoft, Ga 3d and Mg 2p in valence): https://www.materialscloud.org/discover/sssp/
- Python with numpy, scipy: numpy scipy

## Workflow steps

### Step 1: Bulk reference total-energy calculations
- Role: process
- Action: Perform DFT-GGA calculations for bulk wurtzite GaN, orthorhombic Ga, N2 molecule, and cubic Mg3N2 to obtain their total cohesive energies. Use the same pseudopotentials, cutoffs, and k-point sampling as in the defect calculations.
- Evidence: `/app/outputs/bulk_cohesive.log`

### Step 2: N_I defect supercell calculations
- Role: process
- Action: For the type-I split, type-II split, and channel-centered N interstitial configurations in charge states +3, +2, +1, 0, -1, -3 as specified, perform DFT-GGA calculations on a 72-atom supercell and extract cohesive energies (E_coh) of each defective supercell.
- Evidence: `/app/outputs/ni_defect_energies.json`

### Step 3: Mg_Ga N_I complex supercell calculations
- Role: process
- Action: For each Mg_Ga N_I complex configuration (Mg occupying each of the three nearest-neighbor Ga sites around type-I and type-II split interstitials) in charge states +2, +1, and 0, perform DFT-GGA calculations on the 72-atom supercell and extract cohesive energies.
- Evidence: `/app/outputs/mggani_energies.json`

### Step 4: Compile cohesive energies CSV
- Role: scored (load-bearing)
- Action: From the energies computed in the previous steps, assemble a CSV file `cohesive_energies.csv` with columns `system` and `cohesive_energy_eV`. Include all required systems: bulk_GaN, bulk_Ga, N2, Mg3N2, and each defect system (e.g., type_I_NI_+3, type_II_NI_+3, ..., channel_NI_-3, MgGaN_I_a_+2, ...).
- Output file: `/app/outputs/cohesive_energies.csv`
- Format: csv
- Contract: columns: system (string), cohesive_energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cohesive_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cohesive_energies.csv
- path: `/app/outputs/cohesive_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw cohesive energies for all structures: bulk phases, N interstitial defects, and Mg_Ga N_I complexes. The checker will derive formation and binding energies from these values and verify structural properties (charge-state ordering of formation energies, relative stability among interstitial configurations, crossover Fermi-level location, binding-energy positivity and ordering) against paper-reported trends.
- schema:
  - `type`: table
  - `required_columns`: `system`, `cohesive_energy_eV`
  - `units`:
    - `cohesive_energy_eV`: eV

Notes: The agent must compute cohesive energies for all systems listed in the instruction. The checker performs T3 structural audit: it recomputes formation energies from the cohesive energies and checks charge-state ordering, type-I vs type-II relative stability, channel-centered crossover, and binding-energy positivity/ordering. Absolute values are not compared pointwise because the agent's chemical potentials depend on their own bulk cohesive energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cohesive_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "cohesive_energy_eV"
        ],
        "units": {
          "cohesive_energy_eV": "eV"
        }
      },
      "description": "Raw cohesive energies for all structures: bulk phases, N interstitial defects, and Mg_Ga N_I complexes. The checker will derive formation and binding energies from these values and verify structural properties (charge-state ordering of formation energies, relative stability among interstitial configurations, crossover Fermi-level location, binding-energy positivity and ordering) against paper-reported trends."
    }
  ],
  "notes": "The agent must compute cohesive energies for all systems listed in the instruction. The checker performs T3 structural audit: it recomputes formation energies from the cohesive energies and checks charge-state ordering, type-I vs type-II relative stability, channel-centered crossover, and binding-energy positivity/ordering. Absolute values are not compared pointwise because the agent's chemical potentials depend on their own bulk cohesive energies."
}
```

## How you are scored
A hidden verifier reads your `cohesive_energies.csv` and independently computes formation energies and binding energies according to the same protocol described in the approach, using the chemical potentials derived from your bulk cohesive energies. It compares the derived quantities to reference data (which are not provided to you) and scores the submission on the following aspects:

- Accuracy of the derived formation energies (agreement at hidden Fermi-level values).
- Structural consistency checks, such as the ordering of formation energies among the different interstitial configurations and the expected sequence across charge states.
- Accuracy of the binding energies for the Mg_Ga N_I complexes.

Each aspect contributes a fraction of the total reward, with formation-energy accuracy and structural checks carrying the largest weight. Meeting or exceeding the reference thresholds yields full credit for each component; larger deviations result in a reduced score. The exact tolerances and weights are hidden, and the verifier's judgment is final.
