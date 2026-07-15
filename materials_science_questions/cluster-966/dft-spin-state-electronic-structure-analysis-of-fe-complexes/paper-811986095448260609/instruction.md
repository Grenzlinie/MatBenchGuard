# DFT total-energy scan of Fe porphyrin on Co(100) and magnetic coupling

## Problem background
Controlling the magnetic state of paramagnetic molecules on ferromagnetic surfaces is a key challenge for molecular spintronics. Iron porphyrin molecules are promising building blocks, but the nature of the exchange coupling between the molecular Fe and the substrate is not obvious from structural arguments alone. Density functional theory (DFT) calculations can be used to compute the total energy for different magnetic alignments and to determine the equilibrium adsorption geometry, providing quantitative insight into the coupling mechanism. This task focuses on the unligated Fe(II) porphyrin adsorbed on a Co(100) surface, where the Fe–Co exchange is believed to be mediated by the porphyrin nitrogen atoms via a 90° indirect superexchange pathway.

## Approach
Perform spin‑polarized DFT total‑energy calculations using the GGA+U functional (with prescribed Hubbard U and exchange J on the Fe atom). Build a slab model of fcc Co(100) and place the unligated iron porphyrin molecule (constructed from the experimental geometry of Fe octaethylporphyrin(III) chloride after removing the chlorine atom) parallel to the surface. For a series of vertical Fe–Co distances, compute the total energy for both ferromagnetic (FM) and antiferromagnetic (AFM) alignment of the Fe and Co spin moments. The energy‑distance curves for the two alignments are then analysed to extract the equilibrium Fe–Co distance and the magnetic coupling preference.

## Reproduction target
Using the approach described, carry out a total‑energy scan for the unligated Fe porphyrin on Co(100) as a function of the vertical Fe–Co distance. At each distance, compute both FM and AFM spin configurations. Determine the Fe–Co distance that minimizes the total energy (the equilibrium distance). At that distance, compute the energy difference ΔE = E_AFM – E_FM. Write the computed total energies, energy difference, equilibrium distance, and the inferred coupling type ("FM" if ΔE > 0, "AFM" if ΔE < 0) to the file `/app/outputs/energies.json`.

## Assets

- Open-source DFT code (e.g. Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- Experimental geometry of Fe octaethylporphyrin(III) chloride (FeOEPCl)
- Fcc Co lattice parameter

## Workflow steps

### Step 1: Build surface slab models
- Role: process
- Action: Construct periodic slab models of fcc Co(100) and the unligated Fe(II) porphyrin molecule using the known experimental geometry (with chlorine removed) and the fcc lattice constant. Generate input structures for a series of vertical Fe–Co distances (e.g., 2.8–4.2 Å). For each distance, create both ferromagnetic (FM) and antiferromagnetic (AFM) initial spin configurations.
- Evidence: none

### Step 2: Run GGA+U total-energy calculations
- Role: process
- Action: For each structure from the previous step, perform spin-polarized DFT total-energy calculations using the GGA+U functional with Hubbard U=4 eV and exchange J=1 eV applied to the Fe atom. Use adequate plane-wave cutoff and k-point sampling. Compute total energies for FM and AFM spin alignments at each Fe–Co distance. Save the output logs for later analysis.
- Evidence: none

### Step 3: Determine equilibrium distance and FM/AFM energy difference
- Role: scored (load-bearing)
- Action: Parse the DFT total energies obtained in the previous step. Identify the Fe–Co distance that minimizes the total energy for FM and AFM configurations (the equilibrium distance). At that distance, compute the energy difference ΔE = E_AFM – E_FM. Write the results to energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: {"type": "object", "required": ["fm_total_energy", "afm_total_energy", "energy_difference_ev", "equilibrium_distance_angstrom", "coupling_type"], "properties": {"fm_total_energy": {"type": "number", "unit": "eV"}, "afm_total_energy": {"type": "number", "unit": "eV"}, "energy_difference_ev": {"type": "number", "unit": "eV"}, "equilibrium_distance_angstrom": {"type": "number", "unit": "Å"}, "coupling_type": {"type": "string", "enum": ["FM", "AFM"]}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the DFT total energies for FM and AFM alignments, the energy difference ΔE = E_AFM – E_FM, the equilibrium Fe–Co distance, and the coupling type. The checker compares these values against hidden reference values (paper's reported results) to confirm a ferromagnetic coupling and plausible geometry.
- schema:
  - `type`: object
  - `required`: `fm_total_energy`, `afm_total_energy`, `energy_difference_ev`, `equilibrium_distance_angstrom`, `coupling_type`
  - `units`:
    - `fm_total_energy`: eV
    - `afm_total_energy`: eV
    - `energy_difference_ev`: eV
    - `equilibrium_distance_angstrom`: Å

Notes: The DFT calculations are computationally intensive and may require high-performance computing resources. The agent may choose any open-source DFT code that implements GGA+U with adequate pseudopotentials; exact numerical values may differ slightly due to implementation details, which is accounted for in the scoring tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "fm_total_energy",
          "afm_total_energy",
          "energy_difference_ev",
          "equilibrium_distance_angstrom",
          "coupling_type"
        ],
        "units": {
          "fm_total_energy": "eV",
          "afm_total_energy": "eV",
          "energy_difference_ev": "eV",
          "equilibrium_distance_angstrom": "Å"
        }
      },
      "description": "Contains the DFT total energies for FM and AFM alignments, the energy difference ΔE = E_AFM – E_FM, the equilibrium Fe–Co distance, and the coupling type. The checker compares these values against hidden reference values (paper's reported results) to confirm a ferromagnetic coupling and plausible geometry."
    }
  ],
  "notes": "The DFT calculations are computationally intensive and may require high-performance computing resources. The agent may choose any open-source DFT code that implements GGA+U with adequate pseudopotentials; exact numerical values may differ slightly due to implementation details, which is accounted for in the scoring tolerances."
}
```

## How you are scored
A hidden verifier will read `/app/outputs/energies.json` and check that it contains the required fields (`fm_total_energy`, `afm_total_energy`, `energy_difference_ev`, `equilibrium_distance_angstrom`, `coupling_type`). It will verify that the coupling type is consistent with the sign of `energy_difference_ev` and that the equilibrium distance and energy difference are physically reasonable, comparing them against reference values from the original study. The verifier combines these checks into a single reward score between 0 and 1, with a higher score reflecting better agreement with the expected physics.
