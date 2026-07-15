# Compute Spin-Orbit Energy Levels of IrCl₆²⁻ in D₄ₕ Symmetry Using Angular Overlap Ligand-Field Theory

## Problem background
The interpretation of optical absorption spectra of hexachloro-iridate(IV) complexes, IrCl6^2-, is complicated by overlapping low-energy ligand-field (lf) and charge-transfer (ct) transitions, both split by large spin-orbit coupling and low-symmetry distortions. In the B-region (~18000-22000 cm^-1) of K2SnCl6:Ir4+, it is unclear whether the observed bands originate from parity-forbidden lf transitions (from the ^4T1g state) or from parity-forbidden ct transitions from t2g ligand orbitals. Angular overlap ligand-field (AOM) theory can predict the spin-orbit energy levels of the ^4T1g manifold under approximate D4h symmetry, providing a quantitative test of the lf assignment. This task computes the ^4T1g spin-orbit components using an AOM Hamiltonian with published parameters and the actual distortion geometry extracted from the host crystal structure, enabling verification of the expected energy range, level ordering, and fine splittings.

## Approach
The angular overlap model parametrizes the metal-ligand interactions via σ- and π-donation strengths (eσ and eπ) that scale with the metal-ligand distance (usually r^-5). The host crystal K2SnCl6 undergoes a phase transition that slightly distorts the SnCl6^2- octahedron to approximate D4h symmetry; the axial and equatorial bond lengths are extracted from the low-temperature crystal structure. The ligand-field Hamiltonian for a d^5 ion (Ir^4+) is constructed in the full |LSJM⟩ basis, including the AOM matrix, electron-electron repulsion (Racah parameters B and C), and spin-orbit coupling (ζ). Diagonalization yields the spin-orbit eigenstates. The six lowest excited states (relative to the ground state Γ7(^2T2g)) that belong to the ^4T1g manifold are identified and their energies (in cm^-1) and ordering are recorded. The AOM radial parameters eσ and eπ are adjusted from their reference values (eσ=13850 cm^-1, eπ=2760 cm^-1) using the actual bond lengths and the r^-5 radial dependence. The calculation uses the standard Racah parameters B=600 cm^-1, C=3060 cm^-1, and spin-orbit constant ζ=2900 cm^-1.

## Reproduction target
Implement the angular-overlap ligand-field calculation for IrCl6^2- in the K2SnCl6 host lattice, as described. Produce a JSON file containing the energies (relative to the ground state) of the six lowest spin-orbit components of the ^4T1g state: the two Γ8^a states, the Γ7 state, the two Γ8^b states, and the Γ6 state. The output must also include the energy difference between the two Γ8^b components (the Γ8^b splitting). The computed energies are compared to benchmark values derived from the original spectroscopic study to assess whether the B-region absorptions can be attributed to ligand-field transitions of ^4T1g parentage.

## Assets

- Low-temperature crystal structure of K₂SnCl₆: https://doi.org/10.1107/S0567740878005782
- Python numerical libraries: numpy, scipy

## Workflow steps

### Step 1: Extract D4h distortion parameters from K2SnCl6 crystal structure
- Role: process
- Action: Obtain the low-temperature crystal structure of K2SnCl6 from Boysen & Hewat (1978, DOI: 10.1107/S0567740878005782). Extract the Sn-Cl bond lengths and angles for the SnCl6 octahedron. Determine the approximate D4h axial elongation or compression relative to the average equatorial bond length. Output the axial and equatorial metal-ligand distances used to derive the AOM radial parameters.
- Evidence: `/app/outputs/extracted_geometry.json`

### Step 2: Angular-overlap ligand-field calculation for IrCl62- in D4h
- Role: scored (load-bearing)
- Action: Using the D4h geometry from step_01_extract_geometry, implement an angular-overlap ligand-field (AOM) Hamiltonian for an Ir4+ (d5) complex in D4h symmetry. Include interelectronic repulsion (Racah parameters B=600 cm-1, C=3060 cm-1) and spin-orbit coupling (ζ=2900 cm-1). Use the AOM radial parameters eσ=13850 cm-1, eπ=2760 cm-1, adjusting for the specific axial and equatorial bond lengths via the standard r-5 radial dependence. Construct and diagonalize the full d5 ligand-field plus Coulomb plus spin-orbit matrix in the |LSJM⟩ basis. From the resulting eigenstates, identify the six lowest spin-orbit components derived from the 4T1g manifold: the two Γ8a components, the Γ7 component, the two Γ8b components, and the Γ6 component, all relative to the ground state Γ7(2T2g). Output their energies and ordering.
- Output file: `/app/outputs/lf_energies_computed.json`
- Format: json
- Contract: A JSON object with fields: 'energies' (array of objects, each with 'state' (string: 'Gamma8_a_1', 'Gamma8_a_2', 'Gamma7', 'Gamma8_b_1', 'Gamma8_b_2', 'Gamma6'), 'energy_cm1' (float, energy relative to ground state in cm-1), 'order' (integer 1–6)); 'Gamma8_b_splitting_cm1' (float, absolute energy difference between the two Gamma8_b states in cm-1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lf_energies_computed.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lf_energies_computed.json
- path: `/app/outputs/lf_energies_computed.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed spin-orbit energy levels of the 4T1g manifold under D4h distortion. The hidden checker verifies structural consistency: all energies must fall within the expected range for the B-region, the level ordering must match the pattern predicted by ligand-field theory, and the splittings of the Γ8^a and Γ8^b states (and the separation between the two Γ8^b components) must be within hidden tolerances of paper-derived reference values. No specific numeric targets are disclosed.
- schema:
  - `type`: object
  - `required`:
    - `energies`: array of objects with keys state, energy_cm1, order
    - `Gamma8_b_splitting_cm1`: float
  - `items`:
    - `state`: string
    - `energy_cm1`: float
    - `order`: integer
  - `units`:
    - `energy_cm1`: cm-1
    - `Gamma8_b_splitting_cm1`: cm-1

Notes: Verification combines T3 structural checks (energy range, ordering) with T0 result-level comparison on splittings. All tolerances are hidden but are derived from the paper's reported values and expected toolchain spread. The AOM radial parameters eσ and eπ should be adjusted from the reference values (13850, 2760) using the r-5 radial dependence to account for the actual axial and equatorial bond lengths extracted from the crystal structure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lf_energies_computed.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "energies": "array of objects with keys state, energy_cm1, order",
          "Gamma8_b_splitting_cm1": "float"
        },
        "items": {
          "state": "string",
          "energy_cm1": "float",
          "order": "integer"
        },
        "units": {
          "energy_cm1": "cm-1",
          "Gamma8_b_splitting_cm1": "cm-1"
        }
      },
      "description": "Computed spin-orbit energy levels of the 4T1g manifold under D4h distortion. The hidden checker verifies structural consistency: all energies must fall within the expected range for the B-region, the level ordering must match the pattern predicted by ligand-field theory, and the splittings of the Γ8^a and Γ8^b states (and the separation between the two Γ8^b components) must be within hidden tolerances of paper-derived reference values. No specific numeric targets are disclosed."
    }
  ],
  "notes": "Verification combines T3 structural checks (energy range, ordering) with T0 result-level comparison on splittings. All tolerances are hidden but are derived from the paper's reported values and expected toolchain spread. The AOM radial parameters eσ and eπ should be adjusted from the reference values (13850, 2760) using the r-5 radial dependence to account for the actual axial and equatorial bond lengths extracted from the crystal structure."
}
```

## How you are scored
The hidden verifier reads your lf_energies_computed.json. It checks structural constraints: (1) all six energies fall within the expected range for the B-region (as specified in the output contract); (2) the level ordering matches the pattern predicted by theory; (3) the splittings of the Γ8^a and Γ8^b states, and the separation between the two Γ8^b components, are within allowed tolerances of the paper-derived reference values. A weighted combination of these checks yields a score between 0 and 1. No single exact value must be matched; tolerances account for implementation-dependent variations. You must compute and report the quantities; guessing will likely fail the multi-dimensional checks.
