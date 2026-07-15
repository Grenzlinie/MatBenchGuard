# Phonon stability and electronic properties of a 2D silicon germanide monolayer

## Problem background
Two-dimensional honeycomb materials beyond graphene, such as silicene and germanene, are predicted to host massless Dirac fermions with linear electronic dispersion. A novel silicon germanide (SiGe) monolayer, built by alternating Si and Ge atoms in a buckled honeycomb lattice, has also been proposed. Validating this candidate requires an independent first‑principles assessment of its structural parameters, energetic and kinetic stability, electronic band features, and the effect of sublattice‑selective hydrogenation on magnetism. This task reproduces those computational predictions from scratch using open‑source tools.

## Approach
The work employs density‑functional theory (DFT) within the generalised gradient approximation (PW91 functional) as implemented in an open‑source plane‑wave code. A buckled honeycomb SiGe monolayer is constructed, and both low‑buckled (LB) and high‑buckled (HB) geometries are optimised. Total energies of the monolayer and isolated Si and Ge atoms provide cohesive energies. Phonon dispersion relations are computed via the force‑constant method to check for imaginary modes, and the vibrational free‑energy correction at T = 300 K is evaluated. Electronic band structures are obtained non‑self‑consistently along high‑symmetry lines to examine Dirac‑cone formation and to extract the Fermi velocity by fitting the π/π* bands near the K point. Half‑hydrogenation is modelled by attaching hydrogen to all Si atoms (HSiGe) or to all Ge atoms (SiGeH); spin‑polarised DFT calculations for ferromagnetic, antiferromagnetic, and nonmagnetic configurations determine the magnetic ground state. Finally, a 2D Ising Metropolis Monte Carlo simulation on a large supercell is used to estimate the Curie temperature from the exchange coupling inferred from the DFT energy differences. The key comparisons are between the LB and HB structures, between pristine SiGe and the hydrogenated configurations, and between the two hydrogenation patterns.

## Reproduction target
Produce the following quantities by executing the full pipeline, and save them in the specified JSON output files:

- step_01_structural.json: buckling amplitude (Å), in‑plane lattice constant (Å), and average Si–Ge bond length (Å) for the low‑buckled SiGe monolayer.
- step_02_cohesive.json: cohesive energies per unit cell (eV) for the LB and HB configurations, the vibrational free‑energy contribution ΔF at T = 300 K (eV/cell), and E_coh(LB) + ΔF.
- step_03_phonon_stability.json: a boolean indicating whether no imaginary frequencies are present, the minimum phonon frequency across the Brillouin zone (cm⁻¹), and the three acoustic mode frequencies at the Γ point (cm⁻¹).
- step_04_band_structure.json: Fermi velocity (10⁵ m s⁻¹) from a linear fit of the π/π* bands near the K point, and the bandgap (eV) at the K point.
- step_05_hydrogenation.json: for HSiGe and SiGeH separately – buckling amplitude (Å), Si–Ge bond length (Å), the X–H bond length (Si–H or Ge–H) (Å), magnetic moment per unit cell (µB), and GGA bandgap (eV); also the energy difference E_HSiGe − E_SiGeH (eV) per primitive cell and the Curie temperature (K) from the Monte Carlo simulation.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP pseudopotential library (Si, Ge, efficiency): https://www.materialscloud.org/discover/sssp
- Python scientific stack (numpy, scipy, matplotlib, ase): pypi

## Workflow steps

### Step 1: DFT total energy calculations for SiGe monolayer
- Role: process
- Action: Perform DFT total energy calculations for the SiGe monolayer using a plane-wave code with the PW91-GGA exchange-correlation functional. Optimize the atomic structure of the low-buckled (LB) and high-buckled (HB) configurations, varying lattice constant, buckling, and ionic positions until forces converge. Also compute total energies for isolated Si and Ge atoms. Save the optimized structures and total energies.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: Extract structural parameters
- Role: scored
- Action: From the optimized LB SiGe geometry, extract the in-plane lattice constant, vertical buckling amplitude (distance between Si and Ge sublattices), and average Si-Ge bond length. Write the values into step_01_structural.json.
- Output file: `/app/outputs/step_01_structural.json`
- Format: json
- Contract: {"buckling_amplitude_Ang": float, "lattice_constant_Ang": float, "bond_length_Ang": float}
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion calculation for SiGe LB
- Role: process
- Action: Using the optimized LB SiGe structure, perform phonon calculations by constructing supercells and computing forces via DFT as needed to obtain the dynamical matrix. Use a finite-displacement or linear-response approach with an appropriate phonon code (e.g., Phonopy). Compute phonon frequencies on a grid and interpolate along high-symmetry paths. Record the phonon frequencies and check for imaginary modes.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 4: Phonon stability and frequencies
- Role: scored
- Action: From the phonon calculation, determine the presence of any imaginary frequencies (negative values below a small threshold). Record the lowest frequency across the Brillouin zone and list the three acoustic mode frequencies at the Gamma point. Write to step_03_phonon_stability.json.
- Output file: `/app/outputs/step_03_phonon_stability.json`
- Format: json
- Contract: {"no_imaginary_freq": bool, "minimum_frequency_cm-1": float, "phonon_frequencies_at_Gamma_cm-1": [float]}
- Scoring: scored by hidden verifier

### Step 5: Cohesive energy and vibrational free energy
- Role: scored
- Action: Using the total energies from step1 and the phonon frequencies from step3/step4, compute the cohesive energy per unit cell: E_coh = E_total(SiGe) - (E_total(Si) + E_total(Ge)). For the LB configuration, compute the vibrational free-energy contribution ΔF at T = 300 K from the phonon frequencies using the standard harmonic-oscillator free-energy formula. Report E_coh(LB), E_coh(HB), ΔF, and E_coh(LB)+ΔF in step_02_cohesive.json.
- Output file: `/app/outputs/step_02_cohesive.json`
- Format: json
- Contract: {"E_coh_LB_eV_per_cell": float, "E_coh_HB_eV_per_cell": float, "Delta_F_eV_per_cell": float, "E_coh_plus_Delta_F_eV_per_cell": float}
- Scoring: scored by hidden verifier

### Step 6: Electronic band structure calculation
- Role: process
- Action: Using the optimized LB SiGe structure, perform a non-self-consistent electronic band structure calculation along high-symmetry lines including the K point, using a dense k-point grid. Compute the eigenvalues to resolve the π and π* bands near the Fermi level.
- Evidence: `/app/outputs/bands.dat`

### Step 7: Dirac cone analysis: Fermi velocity and bandgap
- Role: scored
- Action: From the band structure, extract the bandgap at the K point (which should be zero if the Dirac cone is preserved). Fit the linear dispersion E(k) = v_F |k-K| of the π/π* bands near K to obtain the Fermi velocity v_F. Write the Fermi velocity in units of 10^5 m/s and the bandgap in eV to step_04_band_structure.json.
- Output file: `/app/outputs/step_04_band_structure.json`
- Format: json
- Contract: {"Fermi_velocity_10e5_m_per_s": float, "bandgap_eV": float}
- Scoring: scored by hidden verifier

### Step 8: Half-hydrogenation DFT calculations
- Role: process
- Action: Build half-hydrogenated configurations: HSiGe (H on Si) and SiGeH (H on Ge). Use the same DFT settings as step1 to relax their structures. Additionally, compute spin-polarized DFT for HSiGe with ferromagnetic (FM), antiferromagnetic (AFM), and nonmagnetic (NM) initial spin configurations to identify the ground-state magnetic order. Record the optimized geometries and total energies.
- Evidence: `/app/outputs/hydrogenation_results.json`

### Step 9: Curie temperature Monte Carlo simulation
- Role: process
- Action: From the energy differences between FM and AFM configurations of HSiGe, extract the effective exchange coupling constant J for a 2D Ising model on the magnetic sublattice. Perform Monte Carlo simulations on a large 2D lattice (e.g., 100×100) of Ising spins with the extracted J, using the Metropolis algorithm. Sweep temperature, record the average magnetization, and determine the Curie temperature from the magnetization curve or heat capacity peak.
- Evidence: `/app/outputs/curie_temperature.dat`

### Step 10: Half-hydrogenation properties and Curie temperature
- Role: scored (load-bearing)
- Action: Compile the following results from step8 and step9 into step_05_hydrogenation.json: structural parameters for HSiGe and SiGeH (buckling amplitude, Si–Ge bond length, Si–H bond length for HSiGe, Ge–H bond length for SiGeH); magnetic moment per unit cell for HSiGe (from the FM configuration); GGA bandgap; energy difference E_HSiGe − E_SiGeH (per primitive cell); and Curie temperature. All values in the units specified below.
- Output file: `/app/outputs/step_05_hydrogenation.json`
- Format: json
- Contract: {"HSiGe": {"buckling_amplitude_Ang": float, "Si_Ge_bond_Ang": float, "Si_H_bond_Ang": float, "magnetic_moment_muB": float, "bandgap_eV": float}, "SiGeH": {"buckling_amplitude_Ang": float, "Si_Ge_bond_Ang": float, "Ge_H_bond_Ang": float, "magnetic_moment_muB": float, "bandgap_eV": float}, "energy_difference_HSiGe_minus_SiGeH_eV": float, "Curie_temperature_K": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural.json`
- `/app/outputs/step_02_cohesive.json`
- `/app/outputs/step_03_phonon_stability.json`
- `/app/outputs/step_04_band_structure.json`
- `/app/outputs/step_05_hydrogenation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural.json
- path: `/app/outputs/step_01_structural.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized structural parameters of the low-buckled SiGe monolayer.
- schema:
  - `type`: object
  - `required`:
    - `buckling_amplitude_Ang`: number
    - `lattice_constant_Ang`: number
    - `bond_length_Ang`: number

### step_02_cohesive.json
- path: `/app/outputs/step_02_cohesive.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Cohesive energies and vibrational free-energy correction at T=300 K.
- schema:
  - `type`: object
  - `required`:
    - `E_coh_LB_eV_per_cell`: number
    - `E_coh_HB_eV_per_cell`: number
    - `Delta_F_eV_per_cell`: number
    - `E_coh_plus_Delta_F_eV_per_cell`: number

### step_03_phonon_stability.json
- path: `/app/outputs/step_03_phonon_stability.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon stability check: absence of imaginary modes and Γ-point acoustic frequencies.
- schema:
  - `type`: object
  - `required`:
    - `no_imaginary_freq`: boolean
    - `minimum_frequency_cm-1`: number
    - `phonon_frequencies_at_Gamma_cm-1`: array
  - `items`:
    - `phonon_frequencies_at_Gamma_cm-1`: number

### step_04_band_structure.json
- path: `/app/outputs/step_04_band_structure.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fermi velocity from Dirac cone fitting and bandgap at the K point.
- schema:
  - `type`: object
  - `required`:
    - `Fermi_velocity_10e5_m_per_s`: number
    - `bandgap_eV`: number

### step_05_hydrogenation.json
- path: `/app/outputs/step_05_hydrogenation.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Properties of half-hydrogenated SiGe: geometries, magnetic moments, bandgaps, relative stability, and Curie temperature.
- schema:
  - `type`: object
  - `required`:
    - `HSiGe`: object
    - `SiGeH`: object
    - `energy_difference_HSiGe_minus_SiGeH_eV`: number
    - `Curie_temperature_K`: number
  - `HSiGe`:
    - `buckling_amplitude_Ang`: number
    - `Si_Ge_bond_Ang`: number
    - `Si_H_bond_Ang`: number
    - `magnetic_moment_muB`: number
    - `bandgap_eV`: number
  - `SiGeH`:
    - `buckling_amplitude_Ang`: number
    - `Si_Ge_bond_Ang`: number
    - `Ge_H_bond_Ang`: number
    - `magnetic_moment_muB`: number
    - `bandgap_eV`: number

Notes: The task reproduces the main computational results of the paper: structural parameters, cohesive energies with vibrational correction, phonon stability, Fermi velocity, and half‑hydrogenation properties including Curie temperature. All scored artifacts are produced by an open‑source DFT+phonon+Monte Carlo pipeline; the agent must re‑run the full workflow, not use pre‑computed values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "buckling_amplitude_Ang": "number",
          "lattice_constant_Ang": "number",
          "bond_length_Ang": "number"
        }
      },
      "description": "Optimized structural parameters of the low-buckled SiGe monolayer."
    },
    {
      "file": "step_02_cohesive.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_coh_LB_eV_per_cell": "number",
          "E_coh_HB_eV_per_cell": "number",
          "Delta_F_eV_per_cell": "number",
          "E_coh_plus_Delta_F_eV_per_cell": "number"
        }
      },
      "description": "Cohesive energies and vibrational free-energy correction at T=300 K."
    },
    {
      "file": "step_03_phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "no_imaginary_freq": "boolean",
          "minimum_frequency_cm-1": "number",
          "phonon_frequencies_at_Gamma_cm-1": "array"
        },
        "items": {
          "phonon_frequencies_at_Gamma_cm-1": "number"
        }
      },
      "description": "Phonon stability check: absence of imaginary modes and Γ-point acoustic frequencies."
    },
    {
      "file": "step_04_band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Fermi_velocity_10e5_m_per_s": "number",
          "bandgap_eV": "number"
        }
      },
      "description": "Fermi velocity from Dirac cone fitting and bandgap at the K point."
    },
    {
      "file": "step_05_hydrogenation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "HSiGe": "object",
          "SiGeH": "object",
          "energy_difference_HSiGe_minus_SiGeH_eV": "number",
          "Curie_temperature_K": "number"
        },
        "HSiGe": {
          "buckling_amplitude_Ang": "number",
          "Si_Ge_bond_Ang": "number",
          "Si_H_bond_Ang": "number",
          "magnetic_moment_muB": "number",
          "bandgap_eV": "number"
        },
        "SiGeH": {
          "buckling_amplitude_Ang": "number",
          "Si_Ge_bond_Ang": "number",
          "Ge_H_bond_Ang": "number",
          "magnetic_moment_muB": "number",
          "bandgap_eV": "number"
        }
      },
      "description": "Properties of half-hydrogenated SiGe: geometries, magnetic moments, bandgaps, relative stability, and Curie temperature."
    }
  ],
  "notes": "The task reproduces the main computational results of the paper: structural parameters, cohesive energies with vibrational correction, phonon stability, Fermi velocity, and half‑hydrogenation properties including Curie temperature. All scored artifacts are produced by an open‑source DFT+phonon+Monte Carlo pipeline; the agent must re‑run the full workflow, not use pre‑computed values."
}
```

## How you are scored
A hidden automated verifier independently scores each of the five scored JSON artifacts. For every artifact, the verifier checks that the submitted numbers satisfy the physical requirements a correct reproduction would meet – comparing against expected structural trends, stability conditions, linear‑dispersion features, and magnetic ordering signatures, all with appropriate hidden tolerances. The stages are weighted, with the hydrogenation output (step_05) carrying the largest weight because it is load‑bearing; simply reporting numbers from published tables without actually performing the required DFT, phonon, and Monte Carlo calculations will not pass. The verifier’s exact criteria and tolerances are not disclosed; you must compute each quantity from first principles using the described approach.
