# Calculating Re Site Preference and Ideal Shear Strength in Ni3Al

## Problem background
Ni-based single-crystal superalloys rely on coherent γ′-Ni₃Al precipitates for high-temperature strength. The addition of rhenium (Re) is known to improve creep resistance, but the underlying mechanisms remain debated. Key unresolved questions are whether Re atoms prefer the Al or Ni sublattice in the L1₂ structure, how pairs of Re defects interact (attraction vs. repulsion), and how single and double Re additions affect the ideal shear strength of the γ′ phase. First-principles calculations can address these questions by computing the site-preference energy factor, the correlative energies between Re defects at different separations and sublattice occupations, and the ideal shear strength σ_max along a relevant slip direction. Understanding these quantities is critical for guiding alloy design and for explaining the creep behaviour of Re-containing superalloys.

## Approach
We use density functional theory (DFT) calculations to evaluate total energies of Ni₃Al supercells with and without Re substitutions. The procedure consists of three stages.

1. **Single-defect energetics and site preference.** A series of 3×3×3 supercells (108 atoms) is built for the perfect crystal and for point defects: Re on an Al site (Re_Al), Re on a Ni site (Re_Ni), an Al antisite at a Ni site (Al_Ni), and a Ni antisite at an Al site (Ni_Al). After relaxing the atomic positions, formation enthalpies are computed from the total energies and the elemental reference energies of fcc Ni, fcc Al, and hcp Re. These enthalpies define a reaction energy factor that quantifies the preference of Re for the Al vs. Ni sublattice.

2. **Double-Re correlative energies.** For several double-Re configurations in 3×3×3 supercells—Re atoms placed at Al–Al, Al–Ni, and Ni–Ni sites with first or sixth nearest‑neighbor separations—the formation enthalpies are obtained. The correlative energy ΔE of each pair is the difference between the pair formation enthalpy and the sum of the corresponding single-defect formation enthalpies, providing a measure of the interaction (attractive or repulsive) between Re defects.

3. **Ideal shear strength.** Supercells are rotated so that the [11-2] direction lies parallel to the lattice vector a and the (111) plane normal is parallel to c. A series of DFT calculations is performed under fixed incremental shear strains ε along [11-2] on the (111) plane, with relaxation of atomic positions and cell shape. The shear stress σ_xy is recorded at each strain, yielding a stress–strain curve. The maximum stress σ_max is extracted for four configurations: pure Ni₃Al, Re_Al, Re_Ni1, and a double Re at Al–Al sites with an interlayer, second‑neighbor arrangement (V_Re_Al_Re_Al(2nd)).

## Reproduction target
The task is to produce the following four scored artifacts by carrying out the DFT workflow described in the steps:

- **Formation enthalpies of point defects** (`step_01_formation_enthalpies.json`): enthalpies (eV) for Re_Al, Re_Ni, Al_Ni, Ni_Al, and the perfect supercell.
- **Site-preference energy factor** (`step_02_energy_factor.json`): the energy factor E_Re^{Ni→Al} (eV) derived from the single-defect formation enthalpies.
- **Correlative energies of double‑Re pairs** (`step_03_correlative_energies.json`): for each of the configurations Al–Al 2nd, Al–Al 6th, Al–Ni 1st, and Ni–Ni 1st, report the optimized inter‑defect distance d (Å) and the correlative energy ΔE (eV).
- **Ideal shear strengths** (`step_04_shear_strengths.json`): for the four configurations pure, Re_Al, Re_Ni1, and V_Re_Al_Re_Al(2nd), report the maximum shear stress σ_max (GPa) along [11-2](111).

All values must be computed from DFT total energies using the workflow defined in the steps; the exact pseudopotential choice and numerical settings are left to the solver, but the resulting trends must reflect the physics of Re-doped γ′-Ni₃Al.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Lattice constant optimization of L12-Ni3Al
- Role: process
- Action: Perform variable-cell relaxation of L12-Ni3Al unit cell using DFT to obtain equilibrium lattice parameter a0.
- Evidence: `/app/outputs/lattice_constant.txt`

### Step 2: Supercell generation
- Role: process
- Action: Generate 3×3×3 supercells (108 atoms) for perfect Ni3Al and defect configurations (Re_Al, Re_Ni, Al_Ni, Ni_Al) and 2×2×2 rotated supercells (32 atoms) for shear configurations (pure Ni3Al, Re_Al, Re_Ni1, V_Re_Al_Re_Al(2nd)) using the optimized a0.
- Evidence: `/app/outputs/supercell_manifest.json`

### Step 3: Elemental reference energies
- Role: process
- Action: Compute total energies per atom for fcc-Ni, fcc-Al, and hcp-Re using the same DFT parameters as for supercells.
- Evidence: `/app/outputs/reference_energies.json`

### Step 4: DFT total energies for 3×3×3 single-defect supercells
- Role: process
- Action: Perform DFT relaxations (atomic positions only) for the perfect Ni3Al 3×3×3 supercell and the four single-defect configurations (Re_Al, Re_Ni, Al_Ni, Ni_Al). Collect relaxed total energies.
- Evidence: `/app/outputs/single_defect_energies.json`

### Step 5: Formation enthalpies of point defects (scored)
- Role: scored
- Action: Compute defect formation enthalpies H_i using the formula H_i = E(defect) - E(perfect) - (n+m)E(Re) + n E(Ni) + m E(Al) for each defect type (Re_Al, Re_Ni, Al_Ni, Ni_Al, perfect).
- Output file: `/app/outputs/step_01_formation_enthalpies.json`
- Format: json
- Contract: {"Re_Al": float, "Re_Ni": float, "Al_Ni": float, "Ni_Al": float, "perfect": 0.0}
- Scoring: scored by hidden verifier

### Step 6: Energy factor for Re site preference (scored)
- Role: scored
- Action: Compute the energy factor E_Re^{Ni→Al} = (H_Re_Al + H_Al_Ni) - (H_Re_Ni + H_perfect).
- Output file: `/app/outputs/step_02_energy_factor.json`
- Format: json
- Contract: {"E_Re_Ni_to_Al": float}
- Scoring: scored by hidden verifier

### Step 7: DFT total energies for 3×3×3 double-Re supercells
- Role: process
- Action: Perform DFT relaxations for the four double-Re configurations: M_ReAl_ReAl(2nd), M_ReAl_ReAl(6th), M_ReAl_ReNi(1st), M_ReNi_ReNi(1st). Collect relaxed total energies.
- Evidence: `/app/outputs/double_defect_energies.json`

### Step 8: Correlative energies of double-Re pairs (scored)
- Role: scored
- Action: For each double-Re configuration, compute formation enthalpy H_{ReA+ReB} and correlative energy ΔE = H_{ReA+ReB} - H_ReA - H_ReB using the single-defect formation enthalpies. Include inter-defect distance d and configuration label.
- Output file: `/app/outputs/step_03_correlative_energies.json`
- Format: json
- Contract: {"configurations": [{"label": "Al-Al 2nd", "d": float, "Delta_E": float}, {"label": "Al-Al 6th", "d": float, "Delta_E": float}, {"label": "Al-Ni 1st", "d": float, "Delta_E": float}, {"label": "Ni-Ni 1st", "d": float, "Delta_E": float}]}
- Scoring: scored by hidden verifier

### Step 9: DFT shear deformation simulations
- Role: process
- Action: For each of the four 2×2×2 configurations (pure Ni3Al, Re_Al, Re_Ni1, V_Re_Al_Re_Al(2nd)), perform a series of DFT calculations under incremental shear strains along [11-2] on the (111) plane, relaxing atom positions and cell shape under fixed strain. Record stress σ_xy at each strain.
- Evidence: `/app/outputs/stress_strain_data.json`

### Step 10: Ideal shear strengths (scored)
- Role: scored (load-bearing)
- Action: From the stress-strain curves, determine the maximum shear stress σ_max for each configuration.
- Output file: `/app/outputs/step_04_shear_strengths.json`
- Format: json
- Contract: {"configurations": [{"label": "pure", "sigma_max": float}, {"label": "Re_Al", "sigma_max": float}, {"label": "Re_Ni1", "sigma_max": float}, {"label": "V_Re_Al_Re_Al(2nd)", "sigma_max": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_enthalpies.json`
- `/app/outputs/step_02_energy_factor.json`
- `/app/outputs/step_03_correlative_energies.json`
- `/app/outputs/step_04_shear_strengths.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_enthalpies.json
- path: `/app/outputs/step_01_formation_enthalpies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation enthalpies of point defects in Ni3Al.
- schema:
  - `type`: object
  - `required`:
    - `Re_Al`: number (eV)
    - `Re_Ni`: number (eV)
    - `Al_Ni`: number (eV)
    - `Ni_Al`: number (eV)
    - `perfect`: number (0.0)

### step_02_energy_factor.json
- path: `/app/outputs/step_02_energy_factor.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Energy factor for Re site preference.
- schema:
  - `type`: object
  - `required`:
    - `E_Re_Ni_to_Al`: number (eV)

### step_03_correlative_energies.json
- path: `/app/outputs/step_03_correlative_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Correlative energies for double-Re configurations.
- schema:
  - `type`: object
  - `required`:
    - `configurations`: array
  - `items`:
    - `label`: string
    - `d`: number (Å)
    - `Delta_E`: number (eV)

### step_04_shear_strengths.json
- path: `/app/outputs/step_04_shear_strengths.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Ideal shear strengths along [11-2](111) for pure Ni3Al, Re_Al, Re_Ni1, and V_Re_Al_Re_Al(2nd).
- schema:
  - `type`: object
  - `required`:
    - `configurations`: array
  - `items`:
    - `label`: string
    - `sigma_max`: number (GPa)

Notes: Scoring is performed by a hidden verifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_enthalpies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Re_Al": "number (eV)",
          "Re_Ni": "number (eV)",
          "Al_Ni": "number (eV)",
          "Ni_Al": "number (eV)",
          "perfect": "number (0.0)"
        }
      },
      "description": "Formation enthalpies of point defects in Ni3Al."
    },
    {
      "file": "step_02_energy_factor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "E_Re_Ni_to_Al": "number (eV)"
        }
      },
      "description": "Energy factor for Re site preference."
    },
    {
      "file": "step_03_correlative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "configurations": "array"
        },
        "items": {
          "label": "string",
          "d": "number (Å)",
          "Delta_E": "number (eV)"
        }
      },
      "description": "Correlative energies for double-Re configurations."
    },
    {
      "file": "step_04_shear_strengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "configurations": "array"
        },
        "items": {
          "label": "string",
          "sigma_max": "number (GPa)"
        }
      },
      "description": "Ideal shear strengths along [11-2](111) for pure Ni3Al, Re_Al, Re_Ni1, and V_Re_Al_Re_Al(2nd)."
    }
  ],
  "notes": "Scoring is performed by a hidden verifier."
}
```

## How you are scored
A hidden verifier independently reads each of the four output JSON files. It checks that the files are present and correctly formatted, then evaluates the computed quantities against a set of expected physical relationships (e.g., the sign of the site-preference energy factor, the sign of correlative energies for specific pair types, and the relative ordering of the shear strengths). Each stage is given a score between 0 and 1, and the weighted sum of the stage scores determines the final reward. The verifier uses numerical tolerances appropriate for DFT reproducibility; exact reproduction of a specific paper's numerical values is not required, but the qualitative trends and relative magnitudes must be correctly captured.
