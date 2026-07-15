# Effective formation energy calculation for D03-Fe3Al using DFT

## Problem background
D03-Fe$_3$Al is an intermetallic compound with a bcc-derived ordered structure (space group Fm-3m, lattice parameter ~5.79 Å) that is considered a candidate for high-temperature structural applications. Its high-temperature diffusion properties are largely controlled by point defects, particularly vacancies. The compound has multiple crystallographic sublattices – Fe atoms occupy the α and γ sublattices, while Al atoms sit on the β sublattice – making it possible for vacancies and antisite defects to form on distinct sublattices with different energetic costs. This task addresses the determination of effective formation energies of single atomic defects in iron-rich Fe-Al systems near the stoichiometric composition. Understanding which vacancies dominate and whether structural (constitutional) defects exist guides models of diffusion and ordering in this class of intermetallics. The problem is to compute these effective formation energies from first-principles DFT total energy calculations and a statistically‑rigorous grand‑canonical defect formalism.

## Approach
The method uses two stages. First, ab-initio total energies are computed for D03-Fe$_3$Al supercells containing 16 atoms (fully relaxed atomic positions). A perfect supercell and defective supercells are constructed for compositions Fe$_x$Al$_{100-x}$ with x = 70, 75, 80. Each defective supercell contains one of six point defects: a Fe vacancy on the α sublattice, a Fe vacancy on the γ sublattice, an Al vacancy, a Fe antisite on the Al sublattice, an Al antisite on the Fe γ sublattice, and an Al antisite on the Fe α sublattice. An open-source plane-wave pseudopotential DFT code (e.g., Quantum ESPRESSO) is used with appropriate pseudopotentials for Fe and Al. Atomic positions are fully relaxed before recording the final total energy of each configuration. Second, the total energies are inserted into a grand-canonical defect formalism that neglects defect entropies and assumes constant volume. Chemical potentials for Fe and Al are determined self-consistently from the composition constraints and the condition that the grand-canonical potential J equals zero at zero pressure. This yields effective formation energies for each defect type, which are temperature-independent in the treatment (a good approximation for this system). The effective formation energies are not simply the raw defect formation energies; they reflect the cooperative influence of all defect species and depend on composition. The output is a single CSV file containing the computed effective formation energy (eV) for each defect–composition pair.

## Reproduction target
Produce a CSV file `effective_formation_energies.csv` with columns `defect_type` (string, one of: `Fe_vac_alpha`, `Fe_vac_gamma`, `Al_vac`, `Fe_antisite_Al`, `Al_antisite_Fe_gamma`, `Al_antisite_Fe_alpha`), `composition` (integer: 70, 75, 80), and `energy_eV` (float, effective formation energy in eV). The energies must be derived solely from DFT total energies of the relaxed 16-atom supercells via the grand-canonical formalism; no external energy references or empirical adjustments are permitted. The hidden verifier will evaluate the accuracy of the reported values against a reference, and will also examine internal physical consistency—for example, whether the relative ordering of vacancy formation energies is plausible, whether antisite defect energies lie close to zero, and whether the energies exhibit only weak variation across the three compositions. You do not need to match a specific published table; your computed values will be judged against the reference with allowances for toolchain-dependent systematic differences.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- Pseudopotentials for Fe and Al (e.g., SSSP or PSlibrary): https://www.quantum-espresso.org/pseudopotentials
- D03-Fe3Al crystal structure (space group Fm-3m, lattice parameter ~5.79 Å)

## Workflow steps

### Step 1: Construct supercells and run DFT total energy calculations with relaxation
- Role: process
- Action: Generate perfect and defective 16-atom D03-Fe3Al supercells for compositions x=70,75,80 with single point defects (Fe vacancy on α and γ sublattices, Al vacancy, Fe antisite on Al, Al antisite on Fe γ and α). Perform DFT total energy calculations using an open-source plane-wave pseudopotential code (e.g., Quantum ESPRESSO) with appropriate pseudopotentials, fully relaxing atomic positions and recording final total energies.
- Evidence: `/app/outputs/total_energies.csv`

### Step 2: Compute effective formation energies via grand-canonical formalism
- Role: scored (load-bearing)
- Action: Using the total energies from the DFT calculations and the grand-canonical defect formalism (neglect defect entropies, fixed volume, chemical potentials determined from composition and J=0 condition), compute the effective formation energies for each defect type at each composition for the relaxed N=16 supercell. Output the results as a CSV file.
- Output file: `/app/outputs/effective_formation_energies.csv`
- Format: csv
- Contract: defect_type (string), composition (integer), energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_formation_energies.csv
- path: `/app/outputs/effective_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective formation energies for six defect types at three compositions (x=70,75,80) for the relaxed N=16 supercell, computed from DFT total energies via the grand-canonical formalism.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `composition`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

Notes: Energies must be derived solely from the DFT calculations; no external energy references are allowed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "composition",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Effective formation energies for six defect types at three compositions (x=70,75,80) for the relaxed N=16 supercell, computed from DFT total energies via the grand-canonical formalism."
    }
  ],
  "notes": "Energies must be derived solely from the DFT calculations; no external energy references are allowed."
}
```

## How you are scored
A hidden verifier reads your `effective_formation_energies.csv` file and checks it against a carefully constructed reference that accounts for legitimate differences caused by using an open-source DFT code instead of the original mixed-basis pseudopotential code. The total score (0–1) is a weighted combination of several checks:

- **Absolute energy comparison** for the three vacancy types at composition x=75: each reported energy is compared to the corresponding reference value; the allowed difference (tolerance) is set so that a correct DFT+analysis carried out with a modern open-source plane-wave code can achieve full credit, while random guesses or systematic errors fall short.
- **Physical ordering check**: for composition x=75 the relative order of the three vacancy formation energies is verified (the verifier checks that one specific vacancy type has the lowest energy, the next is higher, and the third is highest).
- **Antisite near-zero check**: for all three compositions, the effective formation energies of the antisite defects are required to be close to zero, consistent with the physical expectation that these are the structural defects in the system.
- **Composition dependence**: the variation of a key vacancy formation energy across x = 70, 75, 80 is examined; the standard deviation must be very small, confirming that the energies are nearly composition-independent.

The checks are coded into the verifier; you do not know the exact reference values or tolerances. Your job is to execute the DFT calculations and the grand-canonical analysis correctly—the verifier then determines whether your results are physically sound and numerically consistent with the published findings.
