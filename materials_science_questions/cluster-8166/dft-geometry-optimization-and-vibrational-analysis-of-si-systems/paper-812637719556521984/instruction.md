# Tight-Binding Calculation of Defect States and Hyperfine Splittings in Amorphous Silicon

## Problem background
Amorphous silicon (a-Si) is a technologically important material whose electronic properties are strongly influenced by coordination defects — three-coordinated dangling bonds and five-coordinated floating bonds. These defects give rise to states in the band gap and paramagnetic signals observable in electron spin resonance (ESR). A key open question is how to distinguish the two defect types from their electronic structure and hyperfine signatures. This task uses tight-binding electronic structure calculations on realistic a-Si structural models to characterise the defect states, compute the density of states (DOS), and determine the hyperfine splittings that would be observed in ESR experiments.

## Approach
The calculations are based on the nearest-neighbor tight-binding model of Chadi, using an sp³ basis per Si atom, 1/d² scaling of interatomic matrix elements, and a bond cutoff between the first and second peaks of the radial distribution function. Two structural models are used: (i) the fully four-coordinated W3 continuous random network of 216 atoms, and (ii) the BGS model of the same size that contains both dangling and floating bonds. The atomic positions are first relaxed to the lowest energy within the tight-binding model, which includes a repulsive two-body potential. The DOS of the relaxed fully-coordinated model reveals the size of the electronic gap. For the defect-containing BGS model, the different coordination sites are identified. To isolate individual defect states, the terminator-saturation technique is applied: all dangling bonds except the one being studied are passivated with hydrogen-like terminator atoms, each contributing a single s orbital with a chosen on-site energy and Slater-Koster interactions identical to those of Si. For each isolated defect, the wavefunction of the gap state is obtained, and the site amplitudes η² and s/p orbital components (α², β²) are extracted for the central defect atom and its neighbours. Finally, the hyperfine splitting ΔH is computed using the standard formula ΔH = (16π/3) (μⱼ/ Iⱼ) μ_B αⱼ² ηⱼ² |ψ₃ₛ(0)|², with the known ²⁹Si nuclear constants and the valence s-wavefunction density at the nucleus (31.5×10⁻²⁴ cm⁻³). The results from all terminator models are compiled and compared for dangling-bond and floating-bond environments.

## Reproduction target
1. **DOS of the fully-coordinated model** (`dos_w3.csv`): Compute the electronic density of states for the relaxed four-coordinated W3 model and write a CSV with columns `energy` (eV) and `dos` (arbitrary units). The DOS must show a clear energy gap.

2. **Wavefunction components and hyperfine splittings** (`wavefunction_data.csv`): From the isolated defect states in the BGS model, compile a CSV with columns `atom_index`, `coordination`, `eta_squared`, `alpha_squared`, `beta_squared`, and `delta_H` (Gauss) for every atom that participates in a defect state (central defect atom and its neighbours). The delta_H values must be computed from the preceding columns and the physical constants.

3. **Hyperfine summary** (`hyperfine_summary.txt`): Write a plain-text summary that states the numeric range of computed hyperfine splittings for atoms neighbouring floating bonds (five-coordinated defects), and notes how the splittings for dangling bonds compare. The summary must reflect the actual computed values, not any external reference.

## Assets

- W3 amorphous silicon model (216 atoms)
- BGS amorphous silicon model (216 atoms)
- Chadi tight-binding parameters for Si: 10.1103/PhysRevB.19.2074
- Hyperfine constants for Si-29

## Workflow steps

### Step 1: Obtain initial atomic coordinates for W3 and BGS models
- Role: process
- Action: Acquire or regenerate the atomic coordinates for the 216-atom continuous random network model of a-Si by Wooten-Winer-Weaire (W3, fully four-coordinated) and the 216-atom model containing coordination defects by Biswas-Grest-Soukoulis (BGS). These models are described in the literature; coordinates may be regenerated using the published Monte Carlo (W3) or molecular-dynamics (BGS) procedures or obtained from available repositories.
- Evidence: `/app/outputs/initial_coords.pkl`

### Step 2: Relax models with tight-binding energy minimization
- Role: process
- Action: Implement a nearest-neighbor tight-binding model with one s and three p orbitals per Si atom, using the Chadi parameters and a 1/d^2 scaling of interatomic matrix elements. Include a bond cutoff between the first and second peak of the radial distribution function. The total energy comprises the sum of electronic band-structure energies and a repulsive two-body potential derived from ab-initio total-energy calculations (Yin and Cohen, 1982). Perform energy minimization of the atomic positions for both the W3 and BGS models to obtain relaxed coordinates.
- Evidence: `/app/outputs/relaxed_coords.pkl`

### Step 3: Compute electronic DOS for relaxed W3 model
- Role: scored
- Action: Using the relaxed coordinates of the fully four-coordinated W3 model, perform a tight-binding electronic structure calculation (same Hamiltonian) to obtain the electronic density of states. Save the DOS as a function of energy.
- Output file: `/app/outputs/dos_w3.csv`
- Format: csv
- Contract: CSV with columns: energy (float, eV), dos (float, arbitrary units).
- Scoring: scored by hidden verifier

### Step 4: Isolate defect states using terminator saturation
- Role: process
- Action: Based on the relaxed BGS model, identify all dangling bonds and floating bonds. For each defect type (floating bond and dangling bond), construct a terminator-saturated model by saturating all other dangling bonds with terminator atoms. Terminators have a single s orbital with on-site energy 0 eV and the same ss and sp Slater-Koster interactions as Si. For each isolated defect, perform a tight-binding calculation to obtain the wavefunction and extract the site amplitudes η_j^2 and s/p components α_j^2, β_j^2 for the atoms involved in the defect state (the central defect atom and its neighbors). Save the intermediate wavefunction data.
- Evidence: `/app/outputs/terminator_wavefunction_data.pkl`

### Step 5: Compile wavefunction component data and compute hyperfine splittings
- Role: scored (load-bearing)
- Action: Read the intermediate wavefunction data from the terminator models. Compute the hyperfine splitting ΔH (in Gauss) for each site using the formula ΔH = (16π/3) * (μ_j/I_j) * μ_B * α_j^2 * η_j^2 * |ψ_{3s}(0)|^2, with the standard ^29Si nuclear constants and |ψ_{3s}(0)|^2 = 31.5×10^{-24} cm^{-3} (converted to consistent units). Write a CSV file containing, for each relevant atom (defect atoms and their immediate neighbors for floating and dangling bonds), the columns: atom_index, coordination, eta_squared, alpha_squared, beta_squared, delta_H.
- Output file: `/app/outputs/wavefunction_data.csv`
- Format: csv
- Contract: CSV with columns: atom_index (int), coordination (int), eta_squared (float), alpha_squared (float), beta_squared (float), delta_H (float, units Gauss).
- Scoring: scored by hidden verifier

### Step 6: Produce hyperfine splitting summary
- Role: scored
- Action: From the computed hyperfine splittings in wavefunction_data.csv, produce a concise text summary that: (a) states the range of hyperfine splittings for atoms neighboring floating bonds (five-coordinated defects) and mentions that this distribution leads to ESR line broadening; (b) states that the hyperfine splittings for dangling bonds are much smaller. Report the actual numeric ranges computed, not any reference values.
- Output file: `/app/outputs/hyperfine_summary.txt`
- Format: txt
- Contract: Plain text file containing sentences that report the numeric range of ΔH for floating-bond neighbours and indicate that dangling-bond splittings are smaller.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_w3.csv`
- `/app/outputs/wavefunction_data.csv`
- `/app/outputs/hyperfine_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_w3.csv
- path: `/app/outputs/dos_w3.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electronic density of states of the relaxed W3 model, expected to show a band gap.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `dos`
  - `units`:
    - `energy`: eV
    - `dos`: arbitrary

### wavefunction_data.csv
- path: `/app/outputs/wavefunction_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Wavefunction amplitudes, s/p components, and computed hyperfine splittings for atoms in defect environments. Delta_H is recomputed by the verifier from the other columns and the public physical constants.
- schema:
  - `type`: table
  - `required_columns`: `atom_index`, `coordination`, `eta_squared`, `alpha_squared`, `beta_squared`, `delta_H`
  - `units`:
    - `atom_index`: integer
    - `coordination`: integer
    - `eta_squared`: float
    - `alpha_squared`: float
    - `beta_squared`: float
    - `delta_H`: Gauss

### hyperfine_summary.txt
- path: `/app/outputs/hyperfine_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Text summary reporting the numeric range of hyperfine splittings for floating bonds and noting that dangling-bond splittings are smaller. The verifier checks the qualitative agreement and range consistency.
- schema:
  - `type`: text
  - `description`: Plain text file with sentences summarizing the computed hyperfine splitting ranges for floating-bond neighbours and dangling bonds.

Notes: The agent must implement the tight-binding model and all relaxation/terminator procedures without relying on pre-provided reference outputs. The physical constants and model coordinates are publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_w3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "dos"
        ],
        "units": {
          "energy": "eV",
          "dos": "arbitrary"
        }
      },
      "description": "Electronic density of states of the relaxed W3 model, expected to show a band gap."
    },
    {
      "file": "wavefunction_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom_index",
          "coordination",
          "eta_squared",
          "alpha_squared",
          "beta_squared",
          "delta_H"
        ],
        "units": {
          "atom_index": "integer",
          "coordination": "integer",
          "eta_squared": "float",
          "alpha_squared": "float",
          "beta_squared": "float",
          "delta_H": "Gauss"
        }
      },
      "description": "Wavefunction amplitudes, s/p components, and computed hyperfine splittings for atoms in defect environments. Delta_H is recomputed by the verifier from the other columns and the public physical constants."
    },
    {
      "file": "hyperfine_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Plain text file with sentences summarizing the computed hyperfine splitting ranges for floating-bond neighbours and dangling bonds."
      },
      "description": "Text summary reporting the numeric range of hyperfine splittings for floating bonds and noting that dangling-bond splittings are smaller. The verifier checks the qualitative agreement and range consistency."
    }
  ],
  "notes": "The agent must implement the tight-binding model and all relaxation/terminator procedures without relying on pre-provided reference outputs. The physical constants and model coordinates are publicly available."
}
```

## How you are scored
After you submit your artifacts, a hidden verifier will independently inspect each scored file. For `dos_w3.csv`, the verifier will check that a well-defined energy gap is present and consistent with the expected electronic structure. For `wavefunction_data.csv`, the verifier will recompute `delta_H` from the provided `eta_squared`, `alpha_squared`, and the public physical constants; it will then assess whether the hyperfine splittings follow the characteristic pattern that distinguishes floating-bond from dangling-bond environments. For `hyperfine_summary.txt`, the verifier will confirm that the reported numeric range is consistent with your own `wavefunction_data.csv` and that the qualitative comparison between defect types is correct. Simply reporting a number without the underlying computation is not sufficient; the verifier evaluates the actual computed data. The final reward is a weighted combination of the stages, with the largest weight on the wavefunction and hyperfine files.
