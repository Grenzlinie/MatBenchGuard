# DFT-based structural and electronic properties of SiC nanotubes

## Problem background
Silicon carbide (SiC) nanotubes are promising materials for electronics and optoelectronics. Engineering their physical properties through bundling into crystalline structures or introducing intrinsic point defects (carbon or silicon vacancies) can dramatically alter their stability, electronic structure, and mechanical response. Understanding how these modifications affect key properties—lattice constants, bulk moduli, band gaps, effective masses, charge distribution, and carrier velocities—is crucial for device design. You will compute these properties for a (7,7) armchair SiC nanotube in four configurations: isolated single-walled, tetragonal crystalline bundle, and isolated with a line of either carbon or silicon vacancies.

## Approach
The computational approach uses density functional theory (DFT) within the plane-wave pseudopotential framework, implemented in Quantum ESPRESSO. Four (7,7) armchair SiC nanotube systems are considered: an isolated single-walled nanotube (ISW-NT), a tetragonal crystalline bundle (BSW-NT), an isolated nanotube with a line of carbon vacancies (ISW-NT_C), and an isolated nanotube with a line of silicon vacancies (ISW-NT_Si).

For each system, variable-cell structural relaxations are performed to minimize total energy, generating energy-versus-volume data. The energy curves are fit to the Murnaghan equation of state to obtain equilibrium lattice constants and bulk moduli. At the equilibrium geometry, self-consistent field (SCF) calculations and non-self-consistent band structure calculations along high-symmetry directions are carried out. From the band structure, the band gap, band gap type, effective masses, and carrier velocities along the tube axis are extracted. Charge transfer and orbital character are analyzed via projected charges from the SCF results. The goal is to compute a comprehensive set of structural, electronic, and charge properties for the four systems and to compare their behavior.

## Reproduction target
Produce a JSON file (`reproduced_properties.json`) that contains, for each of the four SiC nanotube systems, the equilibrium lattice constants, bulk moduli, structural parameters (tubular diameter, radial buckling, symmetry), electronic properties (band gap, band gap type, band gap transition k-points, effective masses, carrier velocities, Fermi-level positions), and average projected charges (s and p orbitals for C and Si) computed from your DFT workflow. The JSON schema is specified in the output contract. The goal is to compute these quantities accurately from the DFT protocol described and to provide them in the required format.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Ultrasoft pseudopotentials for C and Si (PBE, 4 valence electrons): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Generate initial structures for the four SiC nanotube systems
- Role: process
- Action: Create atomic coordinates and unit cell parameters for the four configurations: isolated single-walled (7,7) SiC nanotube (ISW-NT), tetragonal crystalline bundle (BSW-NT), isolated nanotube with a line of carbon vacancies (ISW-NT_C), and isolated nanotube with a line of silicon vacancies (ISW-NT_Si). Use a cross-sectional cell of 30 Å for isolated tubes and a tetragonal cell for the bundle with an initial intertube distance around 2.85 Å. Output Quantum ESPRESSO input structure files for all systems.
- Evidence: `/app/outputs/init_structures.log`

### Step 2: Run DFT calculations (variable‑cell relaxation, SCF, band structure)
- Role: process
- Action: Perform density functional theory calculations using Quantum ESPRESSO for all four systems. For each system, run a series of variable‑cell relaxations at different volumes to obtain total energy vs volume data. At the predicted equilibrium volume, run a self‑consistent field (SCF) calculation followed by a non‑self‑consistent band structure calculation. Use ultrasoft pseudopotentials, a kinetic energy cutoff of roughly 350 eV, Gaussian smearing of 0.1 eV, k‑point grids 1×1×20 for isolated and defected tubes and 8×8×8 for the bundle, and force convergence tighter than 0.001 Ry/au. Collect the total energy vs volume points, the relaxed atomic positions, the SCF charge density, and the band energies along the high‑symmetry path.
- Evidence: `/app/outputs/dft_outputs.log`

### Step 3: Extract all physical properties from DFT outputs
- Role: scored
- Action: From the DFT raw outputs, fit the energy‑volume data to Murnaghan's equation of state to obtain equilibrium lattice constants and bulk moduli. Compute structural descriptors: tubular diameter, radial buckling, symmetry number, translational vector, and (for the bundle) wall‑to‑wall distance. Analyze the electronic band structure to determine the band gap value, band gap type, band gap transition k‑points, effective masses of electrons and holes, carrier velocities along the tube axis, and the energy differences E_f - E_VBM and E_CBM - E_f. Compute average s and p projected charges for carbon and silicon atoms from the SCF projections. Compile all results into a single JSON file.
- Output file: `/app/outputs/reproduced_properties.json`
- Format: json
- Contract: { "ISW_NT": { "num_atoms": int, "lattice_constants": {"a": float, "b": float, "c": float}, "bulk_modulus": {"a": float or null, "b": float or null, "c": float}, "tubular_diameter": float, "radial_buckling": float, "symmetry": int, "band_gap": float or null, "band_gap_type": "indirect" or null, "band_gap_transition": string or null, "effective_mass": {"electron": float, "hole": float or null}, "velocity": {"electron": float, "hole": float or null}, "ef_minus_evbm": float or null, "ecbm_minus_ef": float or null, "charge_s_C": float, "charge_s_Si": float, "charge_p_C": float, "charge_p_Si": float, "total_charge": float }, ... similarly for BSW_NT, ISW_NT_C, ISW_NT_Si }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_properties.json
- path: `/app/outputs/reproduced_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Aggregated physical properties for the four SiC nanotube systems. Units: lattice constants in Å, bulk modulus in kbar, tubular diameter in Å, radial buckling in Å, band gap in eV, effective mass in units of free electron mass (m0), carrier velocities in 10⁵ m/s, energies (ef_minus_evbm, ecbm_minus_ef) in eV, charges in electrons.
- schema:
  - `type`: object
  - `required`:
    - `ISW_NT`:
      - `num_atoms`: integer
      - `lattice_constants`:
        - `a`: float
        - `b`: float
        - `c`: float
      - `bulk_modulus`:
        - `a`: float or null
        - `b`: float or null
        - `c`: float
      - `tubular_diameter`: float
      - `radial_buckling`: float
      - `symmetry`: integer
      - `band_gap`: float or null
      - `band_gap_type`: string or null
      - `band_gap_transition`: string or null
      - `effective_mass`:
        - `electron`: float
        - `hole`: float or null
      - `velocity`:
        - `electron`: float
        - `hole`: float or null
      - `ef_minus_evbm`: float or null
      - `ecbm_minus_ef`: float or null
      - `charge_s_C`: float
      - `charge_s_Si`: float
      - `charge_p_C`: float
      - `charge_p_Si`: float
      - `total_charge`: float
    - `BSW_NT`: same structure as ISW_NT
    - `ISW_NT_C`: same structure as ISW_NT
    - `ISW_NT_Si`: same structure as ISW_NT

Notes: The output contains the equilibrium lattice constants and bulk moduli obtained from Murnaghan fits, structural parameters (diameter, buckling, symmetry), electronic properties (band gap, effective masses, velocities, Fermi‑level positions), and average projected charges for C and Si. All values are for the fully relaxed structures at the equilibrium volume computed under the DFT settings described in the workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ISW_NT": {
            "num_atoms": "integer",
            "lattice_constants": {
              "a": "float",
              "b": "float",
              "c": "float"
            },
            "bulk_modulus": {
              "a": "float or null",
              "b": "float or null",
              "c": "float"
            },
            "tubular_diameter": "float",
            "radial_buckling": "float",
            "symmetry": "integer",
            "band_gap": "float or null",
            "band_gap_type": "string or null",
            "band_gap_transition": "string or null",
            "effective_mass": {
              "electron": "float",
              "hole": "float or null"
            },
            "velocity": {
              "electron": "float",
              "hole": "float or null"
            },
            "ef_minus_evbm": "float or null",
            "ecbm_minus_ef": "float or null",
            "charge_s_C": "float",
            "charge_s_Si": "float",
            "charge_p_C": "float",
            "charge_p_Si": "float",
            "total_charge": "float"
          },
          "BSW_NT": "same structure as ISW_NT",
          "ISW_NT_C": "same structure as ISW_NT",
          "ISW_NT_Si": "same structure as ISW_NT"
        }
      },
      "description": "Aggregated physical properties for the four SiC nanotube systems. Units: lattice constants in Å, bulk modulus in kbar, tubular diameter in Å, radial buckling in Å, band gap in eV, effective mass in units of free electron mass (m0), carrier velocities in 10⁵ m/s, energies (ef_minus_evbm, ecbm_minus_ef) in eV, charges in electrons."
    }
  ],
  "notes": "The output contains the equilibrium lattice constants and bulk moduli obtained from Murnaghan fits, structural parameters (diameter, buckling, symmetry), electronic properties (band gap, effective masses, velocities, Fermi‑level positions), and average projected charges for C and Si. All values are for the fully relaxed structures at the equilibrium volume computed under the DFT settings described in the workflow."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores each required artifact. For `reproduced_properties.json`, the verifier compares your reported values to reference values (obtained from the same computational protocol) using relative tolerances appropriate for DFT calculations. It also checks that structural and electronic trends across the four systems are physically correct (e.g., lattice constant ordering, band gap hierarchy, metallic versus semiconducting behavior). The final reward is a weighted sum of the individual property agreements. Simply reporting numbers that look plausible is not sufficient; you must execute the full DFT workflow as described in the steps and extract results from the raw outputs.
