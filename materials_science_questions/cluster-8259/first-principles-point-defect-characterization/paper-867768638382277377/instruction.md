# Hybrid DFT calculation of lanthanide substitutional defect energy levels and optical transitions in GaN

## Problem background
Lanthanide (RE) doped GaN is a candidate material for optoelectronics, spintronics, and potentially quantum technologies. A fundamental understanding of how RE dopants interact with the GaN host is crucial: their stable valence states, the position of their defect energy levels in the band gap, and the associated optical transitions determine the material's performance. This work focuses on substitutional lanthanide defects, LnGa, where a Ga atom is replaced by a lanthanide (Ln = La–Lu). Using hybrid density-functional calculations, one can systematically map the defect formation energetics and derive thermodynamic transition levels as well as optical absorption/emission energies for charge-transfer processes. The goal is to compute, from first principles, the formation energies of LnGa defects, derive the thermodynamic transition levels ε(+/0) and ε(0/−), and obtain optical peak energies for selected systems, thereby revealing the valence stability pattern and the charge-transfer optical properties of the materials.

## Approach
The methodology rests on hybrid density-functional theory (DFT) that treats all orbitals on equal footing, using a screened Hartree–Fock exchange component (HSE-like functional). A 96-atom wurtzite GaN supercell is employed; one Ga atom is replaced by a lanthanide to form the LnGa defect.

Three main stages are carried out:

1. Bulk GaN reference calculation: the lattice parameters, valence-band maximum (VBM), and total energy of pristine GaN are obtained with the same functional, providing the energy reference and Fermi-level alignment.

2. Defect supercell relaxations: for each selected Ln (La, Ce, Eu, Yb, Lu), the atomic positions are relaxed in the neutral (0) and the relevant charged states (+1, −1) at fixed lattice constants. Total energies and geometry status (relaxed or constrained) are recorded.

3. Analysis: from the total energies and the bulk VBM, formation energies are computed as a function of the Fermi level using the standard formation energy expression for charged defects (which relates total energies, chemical potentials, and the Fermi level). The crossing points of formation energy lines of different charge states give the thermodynamic transition levels ε(+/0) and ε(0/−). For optical (charge-transfer) transitions of Ce and Eu, single-point calculations are performed where the final charge state is evaluated in the relaxed geometry of the initial state, and vice versa, to obtain the Franck–Condon shifts and the absorption/emission peak energies.

All calculations are to be performed with an open-source DFT code capable of hybrid functionals (e.g., Quantum ESPRESSO), using pseudopotentials that include the Ln 4f electrons in the valence. The chemical potentials are chosen such that transition levels are independent of their specific values, so the exact choice does not affect the target quantities.

## Reproduction target
Produce a single JSON file (`reproduction_results.json`) that contains:

- `total_energies`: for each Ln (La, Ce, Eu, Yb, Lu) and each required charge state, the total energy in eV and the geometry type (relaxed or constrained).
- `transition_levels`: the derived ε(+/0) and ε(0/−) values (in eV) for each Ln where they exist; null if not applicable.
- `optical_transitions`: for Ce and Eu, the absorption and emission peak energies (`absorption_eV`, `emission_eV`) and the relaxation energies in the excited and ground states, all in eV, obtained from the constrained-geometry single-point calculations.
- `valence_summary`: for each Ln, a string summarizing the stable valence states deduced from the calculations (e.g., '3+', '3+/4+', '3+/2+').

The values must be derived from the DFT results; the hidden verifier will recompute formation energies and transition levels from the provided total energies and compare against expected references. Qualitative patterns—such as the presence/absence of in-gap levels for certain lanthanides—must be consistent with the computed quantities.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials or PSlibrary: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Bulk GaN HSE reference calculation
- Role: process
- Action: Compute optimized lattice parameters, valence-band maximum (VBM), and bulk total energy of wurtzite GaN using a hybrid functional (HSE-like) DFT code. Save the VBM and total energy to a file.
- Evidence: `/app/outputs/reference_data.json`

### Step 2: Defect supercell relaxations
- Role: process
- Action: Construct a 96-atom wurtzite GaN supercell. For each selected lanthanide (La, Ce, Eu, Yb, Lu), substitute one Ga atom to create LnGa defect. Relax internal coordinates for neutral (0) and relevant charged states (+1, -1) as indicated, using the same hybrid functional. Record total energies and geometry status (relaxed/constrained) in a file.
- Evidence: `/app/outputs/relaxed_energies.json`

### Step 3: Compute thermodynamic transition levels and optical energies
- Role: scored (load-bearing)
- Action: Using the bulk VBM from step 0 and the defect total energies from step 1, compute formation energies at Fermi level=0, derive thermodynamic transition levels epsilon(+/0) and epsilon(0/-) for Ce, Eu, Yb, and confirm absence of in-gap levels for La and Lu. For Ce and Eu, compute optical absorption and emission peak energies for the charge-transfer transitions, performing single-point calculations of the final charge state in the relaxed geometry of the initial state and vice versa. Collect total energies, transition levels, optical energies, and a summary of stable valence states into reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: { 'total_energies': dict[Ln][charge_state] -> { 'total_energy_eV': float, 'geometry': 'relaxed' | 'constrained' }, 'transition_levels': dict[Ln] -> { 'epsilon_plus_over_0': float | null, 'epsilon_0_over_minus': float | null }, 'optical_transitions': dict[Ln] -> { 'absorption_eV': float, 'emission_eV': float, 'relaxation_energy_excited_eV': float, 'relaxation_energy_ground_eV': float }, 'valence_summary': dict[Ln] -> string }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Full reproduction data: total energies, derived transition levels, optical energies, and valence assignments.
- schema:
  - `type`: object
  - `required`:
    - `total_energies`: object mapping Ln symbol to charge state keys, values objects with keys total_energy_eV (eV) and geometry (string)
    - `transition_levels`: object mapping Ln to keys epsilon_plus_over_0 (eV or null) and epsilon_0_over_minus (eV or null)
    - `optical_transitions`: object mapping Ln (Ce, Eu) to keys absorption_eV, emission_eV, relaxation_energy_excited_eV, relaxation_energy_ground_eV (all eV)
    - `valence_summary`: object mapping Ln to a string describing stable valence states (e.g., '3+', '3+/4+', '3+/2+')

Notes: Transition levels and optical energies are derived from the provided total energies; checker will recompute and compare to hidden references with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "total_energies": "object mapping Ln symbol to charge state keys, values objects with keys total_energy_eV (eV) and geometry (string)",
          "transition_levels": "object mapping Ln to keys epsilon_plus_over_0 (eV or null) and epsilon_0_over_minus (eV or null)",
          "optical_transitions": "object mapping Ln (Ce, Eu) to keys absorption_eV, emission_eV, relaxation_energy_excited_eV, relaxation_energy_ground_eV (all eV)",
          "valence_summary": "object mapping Ln to a string describing stable valence states (e.g., '3+', '3+/4+', '3+/2+')"
        }
      },
      "description": "Full reproduction data: total energies, derived transition levels, optical energies, and valence assignments."
    }
  ],
  "notes": "Transition levels and optical energies are derived from the provided total energies; checker will recompute and compare to hidden references with appropriate tolerances."
}
```

## How you are scored
A hidden verifier checks each scored stage independently and combines the stage scores by weight. The verifier does not simply read a reported final number; it recomputes the formation energies and transition levels from the `total_energies` block you provide, using the standard formation energy expression for charged defects. It then compares the recomputed ε(+/0) and ε(0/−) values to hidden reference data within prescribed tolerances. For optical transitions, it similarly recomputes absorption and emission energies from your supplied constrained-geometry energies and checks them against hidden reference values. Additionally, structural/qualitative patterns—e.g., whether certain lanthanides exhibit in-gap levels, and the presence of multiple valence states—are verified against the expected pattern. Reporting the paper's target numbers without actually performing the DFT workflow will not satisfy the recompute checks. The final reward is a weighted sum of scores for each artifact, with the transition-level and optical-energy comparisons carrying the majority of the weight.
