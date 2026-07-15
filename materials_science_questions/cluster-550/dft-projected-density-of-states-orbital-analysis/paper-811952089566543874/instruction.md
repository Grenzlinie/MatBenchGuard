# DFT Odd–Even Effects in Biphenyl Alkanethiol SAMs: Torsion, XPS, and RAIRS Reproduction

## Problem background
Self-assembled monolayers (SAMs) of ω-(biphenyl-4-yl)alkanethiols (BPnT) on Au(111) exhibit pronounced odd–even effects with the number n of methylene spacer units. These effects are seen in packing density, X-ray photoelectron spectroscopy (XPS) core-level shifts, and reflection‑absorption infrared spectra (RAIRS). The microscopic origin lies in the competition between the preferred sulfur‑gold bonding geometry and intermolecular packing forces among the biphenyl moieties. First‑principles calculations can probe how structural parameters such as the inter‑ring torsion angle ω vary with n and with the alternation of surface coverage, and whether such variations can account for the experimentally observed odd–even spectroscopic signatures.

## Approach
We employ density‑functional theory (DFT) to model the SAMs using a repeated‑slab approach. The Au(111) substrate is represented by five layers of gold atoms, and the thiol molecules are adsorbed with sulfur placed between the fcc‑hollow and bridge sites. Two coverage regimes are considered, corresponding to the experimentally observed structures: high coverage (H, p(√3×3) lateral unit cell, 2 molecules) for odd‑n chains and low coverage (L, p(2√3×2) unit cell, 2 molecules) for even‑n chains. All molecular atoms and the top two gold layers are fully relaxed. From the relaxed geometries we extract the torsion angle ω between the two phenyl rings. Core‑level S 2p₃/₂ binding energies are computed within the final‑state approximation, referenced to a sub‑monolayer of atomic sulfur on Au(111). Vibrational frequencies and infrared (IR) intensities are obtained from finite‑displacement Hessian calculations; only the four strongest modes below 1600 cm⁻¹ are considered, and the intensity is evaluated as the square of the dipole‑moment derivative along the surface normal. The workflow is designed to be executed with an open‑source planewave‑pseudopotential DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials.

## Reproduction target
Compute and report in the designated JSON files: (i) the absolute inter‑ring torsion angles ω (in degrees) for BP2T (L‑coverage), BP3T (H‑coverage), BP4T (L‑coverage), and BP5T (H‑coverage); (ii) the S 2p₃/₂ core‑level binding energies (in eV) for these same four systems; (iii) the vibrational frequencies (in cm⁻¹) and IR intensities (arbitrary units) of the four strongest normal modes below 1600 cm⁻¹ for BP3T and BP4T. The aim is to produce the key structural and spectroscopic quantities that govern the parity‑dependent behavior in this class of SAMs.

## Assets

- Quantum ESPRESSO (open‑source DFT package): https://www.quantum-espresso.org/
- Standard solid‑state pseudopotentials (SSSP) library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT geometry optimization of BPnT SAMs
- Role: process
- Action: Construct Au(111) slab models (5 layers, lattice constant 2.952 Å) and molecular layers of ω-(biphenyl-4-yl)alkanethiols (BPnT) with H atoms removed from the thiol group. Set up the two coverage regimes: H‑coverage (p(√3×3) unit cell, 2 molecules) for BP3T and BP5T; L‑coverage (p(2√3×2) unit cell, 2 molecules) for BP2T and BP4T. Place the sulfur atom between the fcc‑hollow and bridge sites. Using an open‑source planewave‑pseudopotential DFT code (e.g., Quantum ESPRESSO), relax all molecular atoms and the top two Au layers until forces are below 0.01 eV/Å. Save the relaxed atomic coordinates for later analysis.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Extract inter‑ring torsion angles
- Role: scored
- Action: From the relaxed coordinates, compute the dihedral (torsion) angle ω between the two phenyl rings of the biphenyl moiety for each structure (BP2T_L, BP3T_H, BP4T_L, BP5T_H). Report the absolute values in degrees.
- Output file: `/app/outputs/torsion_angles.json`
- Format: json
- Contract: {"molecules": [{"name": "BP2T_L", "omega_deg": float}, {"name": "BP3T_H", "omega_deg": float}, {"name": "BP4T_L", "omega_deg": float}, {"name": "BP5T_H", "omega_deg": float}]}
- Scoring: scored by hidden verifier

### Step 3: Compute S 2p3/2 core‑level binding energies
- Role: scored
- Action: For each relaxed SAM structure, perform a total energy calculation of the ground state and a separate total energy calculation with a core hole on one sulfur atom (final‑state approximation). Also compute the energy of a reference system (atomic S on Au(111) submonolayer). Evaluate the S 2p3/2 binding energy as the difference between the core‑excited and ground‑state total energies, referenced to the atomic S/Au value. Report the binding energies for each molecule.
- Output file: `/app/outputs/xps_shifts.json`
- Format: json
- Contract: {"binding_energies": [{"molecule": "BP2T_L", "s2p3_2_eV": float}, {"molecule": "BP3T_H", "s2p3_2_eV": float}, {"molecule": "BP4T_L", "s2p3_2_eV": float}, {"molecule": "BP5T_H", "s2p3_2_eV": float}]}
- Scoring: scored by hidden verifier

### Step 4: Vibrational analysis and RAIRS spectra for BP3T and BP4T
- Role: scored (load-bearing)
- Action: Using the relaxed geometries from the optimization step for BP3T (H‑coverage) and BP4T (L‑coverage), displace each atom in the molecular layer by ±0.02 Å along the Cartesian directions and compute the forces. Build the Hessian matrix, diagonalize to obtain vibrational frequencies, and evaluate the derivative of the dipole moment along the surface normal for each normal mode to obtain IR intensities. Identify the four strongest modes below 1600 cm⁻¹ (labeled νa, νb, νc, νd) and record their frequencies and intensities.
- Output file: `/app/outputs/rairs_modes.json`
- Format: json
- Contract: {"modes": [{"molecule": "BP3T_H", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_a"}, {"molecule": "BP3T_H", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_b"}, {"molecule": "BP3T_H", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_c"}, {"molecule": "BP3T_H", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_d"}, {"molecule": "BP4T_L", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_a"}, {"molecule": "BP4T_L", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_b"}, {"molecule": "BP4T_L", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_c"}, {"molecule": "BP4T_L", "frequency_cm-1": float, "intensity_arb": float, "label": "nu_d"}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/torsion_angles.json`
- `/app/outputs/xps_shifts.json`
- `/app/outputs/rairs_modes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### torsion_angles.json
- path: `/app/outputs/torsion_angles.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Inter‑ring torsion angles ω for BP2T (L), BP3T (H), BP4T (L), BP5T (H). Checker compares |ω| to hidden paper‑reported values with an allowed tolerance.
- schema:
  - `type`: object
  - `required`:
    - `molecules`: array of objects
  - `items`:
    - `name`: string
    - `omega_deg`: float

### xps_shifts.json
- path: `/app/outputs/xps_shifts.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: S 2p3/2 core‑level binding energies for the four SAM systems. Checker verifies the odd‑even trend and absolute values against hidden paper references with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `binding_energies`: array of objects
  - `items`:
    - `molecule`: string
    - `s2p3_2_eV`: float

### rairs_modes.json
- path: `/app/outputs/rairs_modes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Vibrational frequencies and IR intensities for the four strongest modes below 1600 cm⁻¹ of BP3T (H) and BP4T (L). Checker computes frequency shifts and intensity changes and compares them to hidden paper‑reported values with relative tolerances.
- schema:
  - `type`: object
  - `required`:
    - `modes`: array of objects
  - `items`:
    - `molecule`: string
    - `frequency_cm-1`: float
    - `intensity_arb`: float
    - `label`: string

Notes: The scored outputs cover the core structural and spectroscopic claims (torsion angles, XPS shifts, RAIRS modes). Interface energetics (work‑function modification, level alignment) are excluded to keep the reproduction focused on the main structural mechanism.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "torsion_angles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "molecules": "array of objects"
        },
        "items": {
          "name": "string",
          "omega_deg": "float"
        }
      },
      "description": "Inter‑ring torsion angles ω for BP2T (L), BP3T (H), BP4T (L), BP5T (H). Checker compares |ω| to hidden paper‑reported values with an allowed tolerance."
    },
    {
      "file": "xps_shifts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "binding_energies": "array of objects"
        },
        "items": {
          "molecule": "string",
          "s2p3_2_eV": "float"
        }
      },
      "description": "S 2p3/2 core‑level binding energies for the four SAM systems. Checker verifies the odd‑even trend and absolute values against hidden paper references with tolerance."
    },
    {
      "file": "rairs_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "modes": "array of objects"
        },
        "items": {
          "molecule": "string",
          "frequency_cm-1": "float",
          "intensity_arb": "float",
          "label": "string"
        }
      },
      "description": "Vibrational frequencies and IR intensities for the four strongest modes below 1600 cm⁻¹ of BP3T (H) and BP4T (L). Checker computes frequency shifts and intensity changes and compares them to hidden paper‑reported values with relative tolerances."
    }
  ],
  "notes": "The scored outputs cover the core structural and spectroscopic claims (torsion angles, XPS shifts, RAIRS modes). Interface energetics (work‑function modification, level alignment) are excluded to keep the reproduction focused on the main structural mechanism."
}
```

## How you are scored
Your submitted JSON output files will be evaluated by a hidden verifier. The verifier independently checks the torsion angles, core‑level binding energies, and RAIRS mode frequencies/intensities against reference values derived from the original study. Each scored artifact is assigned a weight, and the individual scores are combined to yield the final reward. You do not need to know the reference numbers; simply follow the workflow and report your computed results as accurately as possible.
