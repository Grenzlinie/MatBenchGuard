# First-principles magnetic ground state determination

## Problem background
Anti-perovskite materials ANMn3 (A = Ni, Zn) exhibit interesting magneto-electronic properties such as giant magnetoresistance and negative thermal expansion. Density functional theory (DFT) is used to investigate their structural, electronic, and magnetic properties. The goal is to determine the magnetic ground state (ferromagnetic vs. antiferromagnetic), assess metallic character from the density of states at the Fermi level, and compute the corresponding structural parameters and magnetic moments on the Mn atoms.

## Approach
Spin-polarized DFT calculations are performed within the generalized gradient approximation (GGA) and GGA+U (Hubbard U correction for Mn 3d orbitals). For each compound, the equilibrium lattice constant and bulk modulus are obtained by fitting total energies over a range of volumes to the Birch–Murnaghan equation of state. Self-consistent spin-polarized runs are then carried out for both ferromagnetic (FM) and antiferromagnetic (AFM) spin configurations. The density of states at the Fermi level is extracted for the metallic characterization, and the magnetic moment on Mn is computed from the ground-state spin density. The same protocol is repeated with GGA+U to obtain corrected magnetic moments.

### Critical DFT parameters
- **GGA+U scheme**: A Hubbard correction is applied to the Mn 3d orbitals with an effective Hubbard parameter **Ueff = 0.07 Ry** (as optimized in the paper, where Ueff = U – J). This value is essential to reproduce the GGA+U magnetic moments reported in the paper.
- **Antiferromagnetic (AFM) configuration**: The AFM calculations are performed using a **double cell** (e.g., a 1×1×2 supercell containing two formula units) to accommodate the required spin ordering. The Mn atoms' spins are arranged in an **alternating ↑↓ pattern**: in the supercell, successive Mn layers along the stacking direction take opposite spin directions, so that each Mn has antiparallel alignment with its nearest Mn neighbors. This corresponds to the magnetic ordering described in the paper as “the ↑↓ magnetic ordering”. Any structurally equivalent arrangement that yields zero net magnetic moment in the supercell and alternates spin directions on neighboring Mn atoms is acceptable.

## Reproduction target
For the cubic anti-perovskites NiNMn3 and ZnNMn3 (space group Pm-3m, with A at (0,0,0), N at (½,½,½), and Mn at (½,½,0) and symmetry-equivalent sites):
  1. Optimize the lattice constant by varying the unit‑cell volume and fitting the energy‑volume data to the Birch–Murnaghan equation of state; extract the equilibrium lattice constant (Å) and bulk modulus (GPa).  
     *Hint*: The experimental lattice constants (3.886 Å for NiNMn3, 3.884 Å for ZnNMn3) can be used as initial guesses for the volume scan.
  2. Compute the spin‑polarized density of states at the Fermi level (states/eV) to confirm metallic character.
  3. Calculate total energies for a ferromagnetic (FM) and an antiferromagnetic (AFM) spin arrangement; from the energy difference determine the magnetic ground state and report which configuration is stable.
  4. Compute the **average absolute magnetic moment on Mn** (μB) in the ground state (AFM) using both GGA and GGA+U. For GGA+U, apply Ueff = 0.07 Ry on the Mn 3d orbitals.
All quantities must be reported in two JSON files, one per compound, following the prescribed schemas.

## Assets

- Quantum ESPRESSO (or equivalent DFT code supporting GGA and GGA+U): https://www.quantum-espresso.org/
- Pseudopotentials for Ni, Zn, Mn, N (e.g., SSSP library or GBRV): https://www.materialscloud.org/discover/sssp/
- Crystal structure parameters for NiNMn3 and ZnNMn3 (Pm-3m, atoms as given above; experimental lattice constants ~3.886 Å and ~3.884 Å)

## Workflow steps

### Step 1: Structural optimization for NiNMn3
- Role: process
- Action: Perform DFT structural optimization for NiNMn3 in the ferromagnetic configuration by calculating total energies for a range of lattice constants around the experimental value and fitting the energy vs. volume curve to the Birch-Murnaghan equation of state to obtain the equilibrium lattice constant, bulk modulus, and ground-state total energy.
- Evidence: none

### Step 2: Spin-polarized DOS and magnetic calculations for NiNMn3
- Role: process
- Action: Using the optimized structure from step_01, perform spin-polarized DFT calculations with GGA and GGA+U to compute total and partial DOS (extract DOS at the Fermi level), total energies for ferromagnetic (FM) and anti-ferromagnetic (AFM) spin configurations, and magnetic moments per atom.  
  - For **GGA+U**, set the Hubbard U parameter to **Ueff = 0.07 Ry on Mn 3d**.  
  - For the **AFM calculations**, build a **1×1×2 supercell (double cell)** and assign Mn atomic spins in an alternating ↑↓ pattern (neighboring Mn atoms with opposite spin directions).
- Evidence: none

### Step 3: Compile NiNMn3 results
- Role: scored
- Action: Gather the computed quantities from steps 01-02 and write a JSON file NiNMn3_results.json containing the optimized lattice constant, bulk modulus, FM and AFM total energies, energy difference, ground state, magnetic moment on Mn (GGA and GGA+U), and DOS at the Fermi level.
- Output file: `/app/outputs/NiNMn3_results.json`
- Format: json
- Contract: {'compound': string, 'lattice_constant_GGA': number, 'bulk_modulus_GGA': number, 'FM_energy_GGA': number, 'AFM_energy_GGA': number, 'Delta_E_FM_AFM_GGA': number, 'ground_state': string, 'magnetic_moment_Mn_GGA': number, 'magnetic_moment_Mn_GGA_plus_U': number, 'DOS_at_Fermi_level_GGA': number}
- Scoring: scored by hidden verifier

### Step 4: Structural optimization for ZnNMn3
- Role: process
- Action: Perform DFT structural optimization for ZnNMn3 in the ferromagnetic configuration by calculating total energies for a range of lattice constants around the experimental value and fitting to the Birch-Murnaghan equation of state to obtain the equilibrium lattice constant and bulk modulus.
- Evidence: none

### Step 5: Spin-polarized DOS and magnetic calculations for ZnNMn3
- Role: process
- Action: Using the optimized structure from step_04, perform spin-polarized DFT calculations (GGA, GGA+U) to compute DOS at the Fermi level, FM and AFM total energies, and magnetic moments.  
  - For **GGA+U**, set **Ueff = 0.07 Ry on Mn 3d**.  
  - For the **AFM calculations**, use a 1×1×2 supercell with alternating ↑↓ Mn spin ordering.
- Evidence: none

### Step 6: Compile ZnNMn3 results
- Role: scored
- Action: Gather the computed quantities from steps 04-05 and write a JSON file ZnNMn3_results.json with the same schema as NiNMn3_results.json.
- Output file: `/app/outputs/ZnNMn3_results.json`
- Format: json
- Contract: {'compound': string, 'lattice_constant_GGA': number, 'bulk_modulus_GGA': number, 'FM_energy_GGA': number, 'AFM_energy_GGA': number, 'Delta_E_FM_AFM_GGA': number, 'ground_state': string, 'magnetic_moment_Mn_GGA': number, 'magnetic_moment_Mn_GGA_plus_U': number, 'DOS_at_Fermi_level_GGA': number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/NiNMn3_results.json`
- `/app/outputs/ZnNMn3_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### NiNMn3_results.json
- path: `/app/outputs/NiNMn3_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final compiled results for NiNMn3: lattice constant, bulk modulus, FM and AFM energies, energy difference, magnetic ground state, Mn magnetic moments (GGA and GGA+U), and DOS at the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `lattice_constant_GGA`: number (Angstrom)
    - `bulk_modulus_GGA`: number (GPa)
    - `FM_energy_GGA`: number (Ry)
    - `AFM_energy_GGA`: number (Ry)
    - `Delta_E_FM_AFM_GGA`: number (Ry)
    - `ground_state`: string
    - `magnetic_moment_Mn_GGA`: number (Bohr magneton)
    - `magnetic_moment_Mn_GGA_plus_U`: number (Bohr magneton)
    - `DOS_at_Fermi_level_GGA`: number (states/eV)

### ZnNMn3_results.json
- path: `/app/outputs/ZnNMn3_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final compiled results for ZnNMn3: lattice constant, bulk modulus, FM and AFM energies, energy difference, magnetic ground state, Mn magnetic moments (GGA and GGA+U), and DOS at the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `lattice_constant_GGA`: number (Angstrom)
    - `bulk_modulus_GGA`: number (GPa)
    - `FM_energy_GGA`: number (Ry)
    - `AFM_energy_GGA`: number (Ry)
    - `Delta_E_FM_AFM_GGA`: number (Ry)
    - `ground_state`: string
    - `magnetic_moment_Mn_GGA`: number (Bohr magneton)
    - `magnetic_moment_Mn_GGA_plus_U`: number (Bohr magneton)
    - `DOS_at_Fermi_level_GGA`: number (states/eV)

Notes: Scoring against paper-reported reference values with pre-defined tolerances: lattice constant ±2%, bulk modulus ±15%, energy difference ±0.02 Ry, Mn magnetic moment ±0.3 μB, and DOS at Fermi level > 2.0 states/eV to confirm metallic character.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "NiNMn3_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "lattice_constant_GGA": "number (Angstrom)",
          "bulk_modulus_GGA": "number (GPa)",
          "FM_energy_GGA": "number (Ry)",
          "AFM_energy_GGA": "number (Ry)",
          "Delta_E_FM_AFM_GGA": "number (Ry)",
          "ground_state": "string",
          "magnetic_moment_Mn_GGA": "number (Bohr magneton)",
          "magnetic_moment_Mn_GGA_plus_U": "number (Bohr magneton)",
          "DOS_at_Fermi_level_GGA": "number (states/eV)"
        }
      },
      "description": "Final compiled results for NiNMn3: lattice constant, bulk modulus, FM and AFM energies, energy difference, magnetic ground state, Mn magnetic moments (GGA and GGA+U), and DOS at the Fermi level."
    },
    {
      "file": "ZnNMn3_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "lattice_constant_GGA": "number (Angstrom)",
          "bulk_modulus_GGA": "number (GPa)",
          "FM_energy_GGA": "number (Ry)",
          "AFM_energy_GGA": "number (Ry)",
          "Delta_E_FM_AFM_GGA": "number (Ry)",
          "ground_state": "string",
          "magnetic_moment_Mn_GGA": "number (Bohr magneton)",
          "magnetic_moment_Mn_GGA_plus_U": "number (Bohr magneton)",
          "DOS_at_Fermi_level_GGA": "number (states/eV)"
        }
      },
      "description": "Final compiled results for ZnNMn3: lattice constant, bulk modulus, FM and AFM energies, energy difference, magnetic ground state, Mn magnetic moments (GGA and GGA+U), and DOS at the Fermi level."
    }
  ],
  "notes": "Scoring against paper-reported reference values with pre-defined tolerances: lattice constant ±2%, bulk modulus ±15%, energy difference ±0.02 Ry, Mn magnetic moment ±0.3 μB, and DOS at Fermi level > 2.0 states/eV to confirm metallic character."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the two output JSON files. It compares each numeric value (lattice constant, bulk modulus, energy difference, Mn magnetic moment, DOS at Fermi level) and the ground‑state label to a hidden reference with predefined tolerances. Each file is scored independently, and the final reward is a weighted combination. Only the contents of the JSON files are scored; intermediate DFT outputs are not directly graded. Results that fall within the acceptable range earn full credit, while larger deviations receive proportionally less credit. The scoring rewards a correct physical reproduction, not a specific numeric match, and reflects how well the computed properties align with the expected DFT results.