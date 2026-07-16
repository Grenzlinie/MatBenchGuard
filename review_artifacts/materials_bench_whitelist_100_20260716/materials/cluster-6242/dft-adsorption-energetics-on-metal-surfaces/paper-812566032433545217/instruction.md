# DFT investigation of O2 and H2O adsorption on Ga2O3 monolayer

## Problem background
Two-dimensional Ga₂O₃ nanosheets are promising for high-power and ultraviolet optoelectronics, but their practical use depends on resistance to environmental degradation. Oxygen (O₂) and water (H₂O) are the main atmospheric species that can alter the structural and electronic properties of atomically thin materials. This task investigates the stability of a Ga₂O₃ monolayer when exposed to O₂ and H₂O by computing adsorption geometries, binding energies, charge transfer, dissociation barriers, and changes to the electronic band structure. The goal is to reproduce the first-principles predictions for these quantities using an open-source DFT approach.

## Approach
Use density functional theory (DFT) with the PBE exchange-correlation functional and a van der Waals dispersion correction (Grimme DFT-D2 scheme) to model the interactions. Construct a 3×2×1 supercell of the Ga₂O₃ monolayer (lattice parameters a=2.98 Å, b=5.76 Å) with a 20 Å vacuum layer. Optimize the pristine structure, then place an O₂ molecule and a H₂O molecule at several high-symmetry adsorption sites (e.g., the hollow site H5 over the bottom tetrahedral Ga) to find the most stable physisorption configuration. For each physisorbed system compute the binding energy (E_bind = E_total − E_substrate − E_molecule), the shortest molecule–sheet distance, the intramolecular bond lengths, and the net charge transfer (Bader analysis or equivalent). Perform a band structure calculation for the O₂-adsorbed system and extract the band gap and the positions of the HOMO and LUMO molecular levels relative to the VBM and CBM. For O₂, additionally determine the dissociation energy barrier: use the climbing-image nudged elastic band (CI-NEB) method with five images to connect the physisorbed state to a chemisorbed (dissociated) end state. All calculations are performed with an open-source DFT code (Quantum ESPRESSO) and publicly available pseudopotentials (e.g., from the SSSP library). The numerical settings (plane‑wave cutoff, k‑mesh, convergence criteria) are chosen by the solver to achieve accurate and converged results.

## Reproduction target
Produce the following JSON artifacts under /app/outputs:

- O2_physisorption_results.json: binding energy (eV), shortest molecule–sheet distance (Å), O–O bond length (Å), net charge transfer (e), band gap (eV), HOMO energy relative to VBM (eV), LUMO energy relative to CBM (eV).
- O2_dissociation_barrier.json: dissociation energy barrier (eV).
- H2O_physisorption_results.json: binding energy (eV), shortest molecule–sheet distance (Å), net charge transfer (e).

Each quantity must be computed from the DFT workflow described in the approach. The values are not known in advance; the objective is to reproduce the results of the reference study using a consistent, well‑converged computational setup.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Standard Solid-State Pseudopotentials (SSSP) library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Bader charge analysis code: https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: System setup
- Role: process
- Action: Construct a 3×2×1 supercell of the Ga2O3 monolayer using lattice parameters a=2.98 Å, b=5.76 Å, and add a 20 Å vacuum layer. Define adsorption sites including the hollow site H5 over the bottom tetrahedral Ga ion.
- Evidence: `/app/outputs/supercell_setup.txt`

### Step 2: Pristine reference calculation
- Role: process
- Action: Optimize the geometry of the pristine Ga2O3 nanosheet using DFT (PBE functional, van der Waals correction) and record the total energy E_Ga2O3.
- Evidence: `/app/outputs/pristine_energy.txt`

### Step 3: O2 chemisorption optimization
- Role: process
- Action: Optimize the geometry of dissociated O2 on Ga2O3 (two O atoms bound to nearby octahedral Ga ions) to obtain the final state for the CI-NEB calculation.
- Evidence: `/app/outputs/chemisorbed_O2.xyz`

### Step 4: O2 physisorption properties
- Role: scored (load-bearing)
- Action: Perform geometry optimization for an O2 molecule on the H5 site (sampling additional sites if desired to find the lowest-energy configuration). Compute binding energy E_bind = E_Ga2O3+O2 - E_Ga2O3 - E_O2. Extract the shortest molecule–sheet distance, O–O bond length, and net charge transfer (Bader or equivalent). Perform a band structure calculation for the optimized system and extract the band gap, the HOMO energy relative to the VBM, and the LUMO energy relative to the CBM.
- Output file: `/app/outputs/O2_physisorption_results.json`
- Format: json
- Contract: {"type":"object","required":{"binding_energy_eV":"float","molecule_sheet_distance_A":"float","O_O_bond_length_A":"float","net_charge_transfer_e":"float","band_gap_eV":"float","HOMO_below_VBM_eV":"float","LUMO_below_CBM_eV":"float"}}
- Scoring: scored by hidden verifier

### Step 5: O2 dissociation barrier
- Role: scored (load-bearing)
- Action: Using the climbing-image nudged elastic band (CI-NEB) method with 5 images, compute the minimum energy path from the physisorbed O2 state (obtained in the previous step) to the chemisorbed O2 state (from the process step). Extract the energy barrier as the energy difference between the transition state and the initial physisorbed state.
- Output file: `/app/outputs/O2_dissociation_barrier.json`
- Format: json
- Contract: {"type":"object","required":{"energy_barrier_eV":"float"}}
- Scoring: scored by hidden verifier

### Step 6: H2O physisorption properties
- Role: scored
- Action: Optimize the geometry of an H2O molecule on the Ga2O3 nanosheet (sample a flat orientation). Compute the binding energy, the shortest molecule–sheet distance, and the net charge transfer.
- Output file: `/app/outputs/H2O_physisorption_results.json`
- Format: json
- Contract: {"type":"object","required":{"binding_energy_eV":"float","molecule_sheet_distance_A":"float","net_charge_transfer_e":"float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/O2_physisorption_results.json`
- `/app/outputs/O2_dissociation_barrier.json`
- `/app/outputs/H2O_physisorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### O2_physisorption_results.json
- path: `/app/outputs/O2_physisorption_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing all computed quantities for O2 physisorption on Ga2O3 monolayer.
- schema:
  - `type`: object
  - `required`:
    - `binding_energy_eV`: float
    - `molecule_sheet_distance_A`: float
    - `O_O_bond_length_A`: float
    - `net_charge_transfer_e`: float
    - `band_gap_eV`: float
    - `HOMO_below_VBM_eV`: float
    - `LUMO_below_CBM_eV`: float

### O2_dissociation_barrier.json
- path: `/app/outputs/O2_dissociation_barrier.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the CI-NEB computed dissociation barrier for O2 on Ga2O3 monolayer.
- schema:
  - `type`: object
  - `required`:
    - `energy_barrier_eV`: float

### H2O_physisorption_results.json
- path: `/app/outputs/H2O_physisorption_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing computed quantities for H2O physisorption on Ga2O3 monolayer.
- schema:
  - `type`: object
  - `required`:
    - `binding_energy_eV`: float
    - `molecule_sheet_distance_A`: float
    - `net_charge_transfer_e`: float

Notes: All quantities are compared to the paper's reported values with appropriate tolerances; the agent must compute them from DFT using the described procedure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "O2_physisorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "binding_energy_eV": "float",
          "molecule_sheet_distance_A": "float",
          "O_O_bond_length_A": "float",
          "net_charge_transfer_e": "float",
          "band_gap_eV": "float",
          "HOMO_below_VBM_eV": "float",
          "LUMO_below_CBM_eV": "float"
        }
      },
      "description": "Scored artifact containing all computed quantities for O2 physisorption on Ga2O3 monolayer."
    },
    {
      "file": "O2_dissociation_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "energy_barrier_eV": "float"
        }
      },
      "description": "Scored artifact containing the CI-NEB computed dissociation barrier for O2 on Ga2O3 monolayer."
    },
    {
      "file": "H2O_physisorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "binding_energy_eV": "float",
          "molecule_sheet_distance_A": "float",
          "net_charge_transfer_e": "float"
        }
      },
      "description": "Scored artifact containing computed quantities for H2O physisorption on Ga2O3 monolayer."
    }
  ],
  "notes": "All quantities are compared to the paper's reported values with appropriate tolerances; the agent must compute them from DFT using the described procedure."
}
```

## How you are scored
A hidden verifier reads your three JSON output files and compares every numerical field to a set of reference values (the paper’s reported results, which are not disclosed to you). Comparison is performed with appropriate tolerances that account for the expected spread when using a different DFT implementation and pseudopotentials. The final reward is a weighted sum of the per‑field scores: accurate reproduction (within tolerance) yields high marks, while large deviations or missing values reduce the score. Reporting the paper’s numbers without actually performing the DFT calculations will not satisfy the tolerance windows and will receive a low reward. The verifier does not require you to match a specific code version or exact k‑mesh; it expects physically meaningful results that are consistent with the described methodology.
