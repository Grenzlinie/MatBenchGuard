# DFT study of Ga substitutional defect in rutile SnO2: Off-center relaxation and strain effect on acceptor level

## Problem background
Tin dioxide (SnO₂) is a wide-band-gap oxide semiconductor with excellent transparency and thermal/chemical stability. As-grown SnO₂ typically exhibits n-type conductivity, and achieving p-type doping has proven difficult. Substituting group-III elements, such as gallium, onto the tin site (Ga_Sn) could, in principle, provide a hole acceptor. However, previous computational studies have reached conflicting conclusions: some predict Ga_Sn to be a shallow acceptor, while others find it to be a deep acceptor. Additionally, it has been suggested that applying compressive strain might make the acceptor level shallower. This task uses hybrid density functional theory (HSE) to investigate the Ga_Sn defect in rutile SnO₂, first in the bulk crystal and then under an isotropic compressive volume strain of about 6.2% (representing the effect of Si alloying). The central open questions are: (1) how much energy is gained when the neutral defect relaxes from the symmetric on-center geometry to an off-center configuration, and (2) what is the defect transition level ε(0/−) in bulk SnO₂ and under compression?

## Approach
The approach is first-principles density functional theory (DFT) using a hybrid functional (HSE or equivalent, e.g., PBE0) as implemented in an open-source DFT code. The workflow begins with optimization of the rutile SnO₂ unit cell and computation of its bulk total energy and valence band maximum (VBM). Reference energies for the chemical potentials of Sn, O, and Ga are obtained from metallic α-Sn, an isolated O₂ molecule, and β-Ga₂O₃. A 2×2×3 supercell (72 atoms) is constructed, and one Sn atom is replaced by Ga to form the Ga_Sn defect. Atomic positions are relaxed until forces are small. For the neutral charge state both on-center and off-center starting geometries are explored; for the −1 charge state only the on-center configuration is relaxed. Total energies of these relaxed configurations are recorded. Using the standard defect formation energy formalism with a Makov-Payne finite-size correction (Madelung constant 2.84, dielectric constant 12.33), formation energies are computed as a function of the Fermi level. The transition level ε(0/−) is the Fermi energy at which the formation energies of the neutral and −1 charge states are equal. The energy lowering ΔE of the neutral defect due to off-center relaxation is found by comparing the relaxed total energies of the two neutral configurations. The effect of compressive strain is modeled by isotropically compressing the pristine supercell volume by 6.22% (scaling all lattice vectors). The host total energy and VBM are recomputed, the Ga_Sn defect is introduced and relaxed in both charge states (starting from on-center geometries), and the transition level is extracted again. The required outputs are the three numerically computed quantities: ΔE, bulk ε(0/−), and compressed ε(0/−). All calculations use the hybrid functional, and Python scripts (numpy, scipy) perform the formation energy and transition level analysis.

## Reproduction target
Compute and save the following three numerical results in separate JSON files under /app/outputs:

1. `neutral_relaxation_energy.json`: the energy lowering (ΔE in eV) of the neutral Ga_Sn defect when it moves from the on-center to the off-center configuration in bulk SnO₂.
2. `bulk_transition_level.json`: the defect transition level ε(0/−) (in eV above the VBM) for Ga_Sn in bulk SnO₂.
3. `compressed_transition_level.json`: the defect transition level ε(0/−) (in eV above the VBM) for Ga_Sn when the SnO₂ supercell is isotropically compressed by 6.22% volume.

Each value must be produced by the DFT-based workflow described in the steps below; no other sources may be used.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/download
- SSSP pseudopotential library (efficiency) for Sn, O, Ga: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python packages (numpy, scipy, json): numpy scipy
- Rutile SnO2 crystal structure: 10.1524/zkri.1956.107.1-2.196
- Metallic α-Sn structure
- β-Ga2O3 crystal structure

## Workflow steps

### Step 1: HSE bulk optimization of SnO2
- Role: process
- Action: Optimize the rutile SnO2 primitive cell using the HSE hybrid functional starting from experimental lattice parameters. Converge k‑mesh and energy cutoff appropriately. Record the relaxed lattice parameters, total energy per formula unit, and valence band maximum (VBM) energy in a reference file for subsequent calculations.
- Evidence: `/app/outputs/bulk_reference.json`

### Step 2: Reference energies for chemical potentials
- Role: process
- Action: Compute HSE total energies for: (a) metallic α‑Sn (per atom), (b) an isolated O₂ molecule in a large box (half the energy per atom for μ_O), and (c) β‑Ga₂O₃ (per formula unit). Store these energies in a file for use in formation energy calculations.
- Evidence: `/app/outputs/chemical_potentials.json`

### Step 3: Defect supercell relaxations in bulk SnO2
- Role: process
- Action: Construct a 2×2×3 supercell (72 atoms) from the optimized bulk SnO2. Substitute one Sn with Ga to create Ga_Sn. Relax atomic positions until forces <0.025 eV/Å for the following configurations: (i) neutral charge state starting from the on-center geometry, (ii) neutral charge state starting from an off-center geometry with one Ga–O bond broken, (iii) -1 charge state starting from the on-center geometry. Record the total energy of each relaxed configuration in a file.
- Evidence: `/app/outputs/defect_total_energies_bulk.json`

### Step 4: Neutral off-center relaxation energy (bulk)
- Role: scored (load-bearing)
- Action: Using the total energies from step3, compute the formation energies of the neutral defect in on-center and off-center configurations, following the standard defect formation formalism with the Makov–Payne finite-size correction and appropriate Madelung constant and dielectric constant. Determine the energy lowering ΔE = E(off‑center) − E(on‑center) in eV. Write a JSON file {"energy_difference_eV": <value>}.
- Output file: `/app/outputs/neutral_relaxation_energy.json`
- Format: json
- Contract: {"type": "object", "required": {"energy_difference_eV": "number"}}
- Scoring: scored by hidden verifier

### Step 5: Bulk transition level ε(0/−)
- Role: scored (load-bearing)
- Action: Using the total energies from step3, the host total energy and VBM from step1, the chemical potentials from step2, and the same finite-size correction, compute the formation energies as a function of Fermi level for both charge states. Determine the ε(0/−) transition level (the Fermi energy where formation energies of neutral and −1 are equal). Write a JSON file {"epsilon_0_minus_eV": <level above VBM in eV>}.
- Output file: `/app/outputs/bulk_transition_level.json`
- Format: json
- Contract: {"type": "object", "required": {"epsilon_0_minus_eV": "number"}}
- Scoring: scored by hidden verifier

### Step 6: Pristine compressed supercell reference
- Role: process
- Action: Isotropically compress the bulk SnO2 supercell by reducing the cell volume by 6.22% (scale all lattice vectors uniformly). Using HSE, compute the total energy and VBM of this compressed pristine supercell. Record these values in a file for later formation energy analysis.
- Evidence: `/app/outputs/compressed_host_reference.json`

### Step 7: Defect relaxations in compressed supercell
- Role: process
- Action: In the compressed supercell from step6, substitute one Sn with Ga. Relax atomic positions for charge states q=0 and q=−1 starting from on-center geometries, using the same force convergence criterion as before. Record the total energies of each relaxed configuration in a file.
- Evidence: `/app/outputs/defect_total_energies_compressed.json`

### Step 8: Compressed transition level ε(0/−)
- Role: scored (load-bearing)
- Action: Using the host total energy and VBM from step6, the defect total energies from step7, the chemical potentials from step2, and the finite-size correction (same parameters as before), compute formation energies and extract the ε(0/−) transition level. Write a JSON file {"epsilon_0_minus_eV": <level above VBM in eV>}.
- Output file: `/app/outputs/compressed_transition_level.json`
- Format: json
- Contract: {"type": "object", "required": {"epsilon_0_minus_eV": "number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/neutral_relaxation_energy.json`
- `/app/outputs/bulk_transition_level.json`
- `/app/outputs/compressed_transition_level.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### neutral_relaxation_energy.json
- path: `/app/outputs/neutral_relaxation_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy difference between off-center and on-center neutral Ga_Sn configurations in bulk SnO2 (eV). Compared to the paper-reported reference with tolerance for method-dependent spread.
- schema:
  - `type`: object
  - `required`:
    - `energy_difference_eV`: number

### bulk_transition_level.json
- path: `/app/outputs/bulk_transition_level.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Defect transition level ε(0/−) for Ga_Sn in bulk SnO2 (eV above VBM). Compared to the paper-reported reference with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `epsilon_0_minus_eV`: number

### compressed_transition_level.json
- path: `/app/outputs/compressed_transition_level.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Defect transition level ε(0/−) for Ga_Sn under 6.22% volume compression (eV above VBM). Compared to the paper-reported reference with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `epsilon_0_minus_eV`: number

Notes: The checker compares the submitted values to the paper-reported quantitative results using appropriate tolerances that account for expected variations due to different implementations of HSE and pseudopotentials. The exact tolerances are part of the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "neutral_relaxation_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "energy_difference_eV": "number"
        }
      },
      "description": "Energy difference between off-center and on-center neutral Ga_Sn configurations in bulk SnO2 (eV). Compared to the paper-reported reference with tolerance for method-dependent spread."
    },
    {
      "file": "bulk_transition_level.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_0_minus_eV": "number"
        }
      },
      "description": "Defect transition level ε(0/−) for Ga_Sn in bulk SnO2 (eV above VBM). Compared to the paper-reported reference with tolerance."
    },
    {
      "file": "compressed_transition_level.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_0_minus_eV": "number"
        }
      },
      "description": "Defect transition level ε(0/−) for Ga_Sn under 6.22% volume compression (eV above VBM). Compared to the paper-reported reference with tolerance."
    }
  ],
  "notes": "The checker compares the submitted values to the paper-reported quantitative results using appropriate tolerances that account for expected variations due to different implementations of HSE and pseudopotentials. The exact tolerances are part of the hidden grading specification."
}
```

## How you are scored
Each of the three scored output files is evaluated independently by a hidden verifier that compares your submitted numbers to reference values. The verifier checks that the neutral relaxation energy is positive and matches the expected magnitude within a tolerance, that both the bulk and compressed transition levels exceed a minimum depth, and that the change in the transition level under compression is consistent with a modest shift (the level does not become dramatically shallower). The final reward is a weighted combination across these checks. Reporting the paper's numerical result without executing the DFT workflow will not satisfy the verifier, because the checks include trend requirements that are difficult to satisfy with random or generic numbers.
