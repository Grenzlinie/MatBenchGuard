# Charge orders in extended two-orbital Hubbard model

## Problem background
Organic charge-transfer salts such as κ-(BEDT-TTF)₂X exhibit a rich interplay of charge, orbital, and spin degrees of freedom due to strong electronic correlations. A minimal model to capture these phenomena is the extended two-orbital Hubbard model on an anisotropic triangular lattice at 3/4 filling, where each lattice site (dimer) contains two molecular orbitals (c and f). The model includes intramolecular Hubbard U, intermolecular Coulomb interactions (V_{b1}, V_{b2}, V_p, V_q), and hopping terms that define the kinetic energy. Understanding the resulting ground states—including possible charge-ordered insulating and metallic phases—is important for explaining experimental observations of ferroelectricity and competing orders in these materials.

## Approach
We employ variational Monte Carlo (VMC) with Jastrow-Slater wave functions to approximate the ground state of the two-orbital Hubbard model. The wave function consists of a long-range density-density Jastrow factor multiplied by a Slater determinant, which is taken as the ground state of an auxiliary Hamiltonian. For insulating regimes, the auxiliary Hamiltonian includes site-dependent chemical potentials with wave vector Q = (0,0) or (π,π) to describe polar and nonpolar charge orders, and staggered magnetic fields to allow antiferromagnetic order. For metallic regimes, a 12-sublattice chemical potential pattern is introduced to capture honeycomb-like charge order. Variational parameters (Jastrow pseudopotentials, chemical potentials, magnetic fields) are optimized by minimizing the energy via Monte Carlo sampling.

The workflow proceeds in several stages: first, analytic atomic-limit energies are derived to establish the phase competition (a required intermediate). Then, VMC is used to scan the interaction parameters (V_p, V_q) along the line V_p + V_q = 3 t_{b1} in the large-U regime (U/t_{b1}=10, V_{b1}/t_{b1}=4, V_{b2}/t_{b1}=2) to identify the phase boundaries between the polar charge-ordered insulator (PCOI), dimer-Mott insulator (DMI), and polar' charge-ordered insulator (PCOI'). From the optimized wave functions, charge structure factors and charge-disproportionation structure factors are computed. Finally, for a different small-U metallic regime (U/t_{b1}=6, V_{b1}/t_{b1}=4, V_{p}/t_{b1}=3.5, V_{q}/t_{b1}=3), VMC with a 12-sublattice ansatz yields the electron density profile.

## Reproduction target
For the extended two-orbital Hubbard model at 3/4 filling with the given hopping parameters, produce three key artifacts:

1. Phase boundaries in the large-U insulating regime: a JSON file specifying the V_p/t_{b1} values where the ground state changes from PCOI to DMI and from DMI to PCOI' along the line V_p+V_q = 3 t_{b1}.
2. Charge structure factors: a JSON file containing the total charge structure factor N(q) and charge-disproportionation structure factor N_CD(q) at q=(0,0) and (π,π) for each of the insulating phases (PCOI, PCOI', NPCOI, DMI).
3. Charge-density profile of the 12-sublattice charge-ordered metal: a CSV file with the electron density per sublattice for both c and f orbitals in the small-U metallic regime.

These outputs must be computed by implementing the VMC method as described; the hidden verifier will compare them to reference results.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute atomic-limit energies and phase boundaries
- Role: process
- Action: Derive analytic energies per dimer for the polar (PCOI, PCOI') and nonpolar (NPCOI) charge-ordered configurations in the atomic limit (all hopping amplitudes zero). Compute the phase boundaries in the V_p–V_q plane and the degeneracy condition V_p=V_q=(V_{b1}+V_{b2})/2.
- Evidence: `/app/outputs/atomic_limit_energies.txt`

### Step 2: Determine phase boundaries for insulating phases from VMC
- Role: scored (load-bearing)
- Action: For the large-U regime (U/tb1=10, Vb1/tb1=4, Vb2/tb1=2), perform variational Monte Carlo (Jastrow-Slater wave functions with charge and magnetic order parameters) on a set of Vp and Vq values along the line Vp+Vq=3tb1. Identify the transition points where the lowest-energy phase changes between PCOI, DMI, and PCOI'. Output the phase boundaries as a JSON object.
- Output file: `/app/outputs/large_U_phase_boundaries.json`
- Format: json
- Contract: JSON object with keys: 'PCOI_to_DMI_Vp_over_tb1' (float), 'DMI_to_PCOI_prime_Vp_over_tb1' (float), and optionally 'NPCOI_region' (boolean, indicating whether the NPCOI phase appears along the scanned line).
- Scoring: scored by hidden verifier

### Step 3: Compute charge structure factors for insulating phases
- Role: scored
- Action: Using the optimized wave functions from the large-U scan, compute the total charge structure factor N(q) and the charge-disproportionation structure factor N_CD(q) for the stable phases (PCOI, PCOI', NPCOI, DMI) at the representative momenta q=(0,0) and q=(π,π). Output a JSON file with the values.
- Output file: `/app/outputs/charge_structure_factors.json`
- Format: json
- Contract: JSON object with keys for each phase: 'PCOI', 'PCOI_prime', 'NPCOI', 'DMI'. Each is an object containing: 'N_CD_q00' (float), 'N_CD_qpipi' (float), 'N_qpipi' (float). qpipi denotes q=(π,π).
- Scoring: scored by hidden verifier

### Step 4: Compute sublattice charge density for 12-sublattice charge-ordered metal
- Role: scored (load-bearing)
- Action: In the small-U metallic regime (U/tb1=6, Vb1/tb1=4, Vp/tb1=3.5, Vq/tb1=3), perform VMC simulations with a 12-sublattice auxiliary Hamiltonian to obtain the electron density per sublattice. Output a CSV file with the density values for the c and f orbitals on each of the 12 sublattices.
- Output file: `/app/outputs/COM_density_profile.csv`
- Format: csv
- Contract: CSV with 3 columns: 'sublattice' (integer 0–11), 'density_c' (float), 'density_f' (float). Each row corresponds to one sublattice.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/large_U_phase_boundaries.json`
- `/app/outputs/charge_structure_factors.json`
- `/app/outputs/COM_density_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### large_U_phase_boundaries.json
- path: `/app/outputs/large_U_phase_boundaries.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phase boundaries in units of Vp/tb1 for the transition from PCOI to DMI and from DMI to PCOI' along the line Vp+Vq=3tb1. Optionally includes NPCOI_region boolean.
- schema:
  - `type`: object
  - `required`:
    - `PCOI_to_DMI_Vp_over_tb1`: float
    - `DMI_to_PCOI_prime_Vp_over_tb1`: float
  - `items`: object

### charge_structure_factors.json
- path: `/app/outputs/charge_structure_factors.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Charge structure factors N(q) and N_CD(q) at q=(0,0) and q=(π,π) for each insulating phase. The pattern of peaks is used to verify charge order type.
- schema:
  - `type`: object
  - `required`:
    - `PCOI`: object
    - `PCOI_prime`: object
    - `NPCOI`: object
    - `DMI`: object
  - `items`:
    - `N_CD_q00`: float
    - `N_CD_qpipi`: float
    - `N_qpipi`: float

### COM_density_profile.csv
- path: `/app/outputs/COM_density_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electron density per sublattice for the 12-sublattice charge-ordered metal, showing rich-rich-poor sequence.
- schema:
  - `type`: table
  - `required_columns`: `sublattice`, `density_c`, `density_f`
  - `units`:
    - `density_c`: electrons per orbital
    - `density_f`: electrons per orbital

Notes: All scored artifacts are checked against paper-reported reference values or structural patterns with appropriate hidden tolerances. The instruction.md will not reveal gold values or tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "large_U_phase_boundaries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "PCOI_to_DMI_Vp_over_tb1": "float",
          "DMI_to_PCOI_prime_Vp_over_tb1": "float"
        },
        "items": {}
      },
      "description": "Phase boundaries in units of Vp/tb1 for the transition from PCOI to DMI and from DMI to PCOI' along the line Vp+Vq=3tb1. Optionally includes NPCOI_region boolean."
    },
    {
      "file": "charge_structure_factors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "PCOI": "object",
          "PCOI_prime": "object",
          "NPCOI": "object",
          "DMI": "object"
        },
        "items": {
          "N_CD_q00": "float",
          "N_CD_qpipi": "float",
          "N_qpipi": "float"
        }
      },
      "description": "Charge structure factors N(q) and N_CD(q) at q=(0,0) and q=(π,π) for each insulating phase. The pattern of peaks is used to verify charge order type."
    },
    {
      "file": "COM_density_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "sublattice",
          "density_c",
          "density_f"
        ],
        "units": {
          "density_c": "electrons per orbital",
          "density_f": "electrons per orbital"
        }
      },
      "description": "Electron density per sublattice for the 12-sublattice charge-ordered metal, showing rich-rich-poor sequence."
    }
  ],
  "notes": "All scored artifacts are checked against paper-reported reference values or structural patterns with appropriate hidden tolerances. The instruction.md will not reveal gold values or tolerances."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. The verifier reads the three output files (large_U_phase_boundaries.json, charge_structure_factors.json, COM_density_profile.csv) and compares your computed values against hidden reference numbers and structural patterns. For the phase boundaries, it checks that the transition points are within appropriate tolerances. For the structure factors, it verifies that the expected peaks (or absence thereof) appear for each phase. For the density profile, it confirms the characteristic rich-rich-poor sequence across the 12 sublattices. The final reward is a weighted sum of scores from each artifact, based on how closely they match the expected physical behavior. The reference values and exact tolerances are not disclosed; you must produce results through a faithful implementation of the variational Monte Carlo method.
