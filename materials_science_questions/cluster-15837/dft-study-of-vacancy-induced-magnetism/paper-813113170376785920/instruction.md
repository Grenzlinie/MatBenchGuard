## Problem background

Silicon carbide (SiC) nanotubes are promising nanomaterials for electronics, spintronics, and sensing applications. Their physical properties can be engineered by bundling individual nanotubes into crystalline arrays or by introducing intrinsic point defects such as carbon or silicon vacancies. Understanding how these structural modifications alter the lattice constants, band gap, bulk modulus, charge distribution, and carrier transport properties is essential for designing nanoscale devices. Reproducing these property changes from first-principles calculations provides a quantitative benchmark for the effects of bundling and vacancy defects on nanotube behaviour.

## Approach

Use spin-polarised density functional theory (DFT) with the Quantum ESPRESSO package to compute the physical properties of single-walled (7,7) SiC nanotubes in four distinct configurations:

1. **Isolated single-walled (7,7) SiC nanotube (ISW-NT)** — the pristine reference system.
2. **Tetragonal crystalline bundle of (7,7) SiC nanotubes (BSW-NT)** — nanotubes packed in a tetragonal lattice.
3. **Isolated (7,7) nanotube with a carbon line vacancy (ISW-NT with C vacancy)** — one line of carbon atoms removed from the unit cell.
4. **Isolated (7,7) nanotube with a silicon line vacancy (ISW-NT with Si vacancy)** — one line of silicon atoms removed from the unit cell.

The computational procedure for each configuration follows three stages. First, construct the unit cell and set up DFT input files using ultrasoft pseudopotentials (4 valence electrons each for C and Si, s²p²), a plane-wave kinetic energy cutoff of 350 eV, and Gaussian smearing of 0.1 eV. For isolated tubes, use a k-point grid of 1×1×20 and set the cross-section lattice parameters to 30 Å to prevent spurious tube–tube interactions. For the bundle, use a k-point grid of 8×8×8.

Second, perform variable-cell structural relaxation by minimising the total energy with respect to unit-cell volume and atomic positions. Calculate the total energy at several unit-cell volumes around the expected equilibrium and fit the energy-versus-volume data to Murnaghan's equation of state to extract equilibrium lattice constants, bulk modulus, tubular diameter, and radial buckling.

Third, use the relaxed geometries to run spin-polarised self-consistent field (SCF) calculations followed by non-self-consistent band-structure calculations along high-symmetry k-point paths. From these, obtain the Kohn-Sham band structure, total and projected density of states, electron charge density, and total magnetisation. Post-process the results to derive band gaps (with transition k-points), effective masses of electrons and holes at the band edges, and carrier velocities along the tube axis.

## Reproduction target

Compute and report the full set of structural and electronic properties for all four configurations in a single `results.json` file. The target quantities are:

- **Structural**: lattice constants a, b, c; tubular diameter; radial buckling; symmetry number; bulk modulus along the a, b, and c axes (the in-plane moduli may be absent for isolated tubes).
- **Electronic**: band gap value and transition k-points (for semiconducting systems; report null for metallic systems); effective masses of electrons (conduction band) and holes (valence band) in units of the free-electron mass m₀; carrier velocities v_z along the tube axis for both bands.
- **Charge and magnetism**: orbital-projected charge density averages (s and p orbitals for C and Si atoms, plus total charge per formula unit); total magnetisation.

All quantities should be obtained from the same DFT framework (same pseudopotentials, cutoff, smearing, and k-point grids) to ensure internal consistency. The metallic (ISW-NT with Si vacancy) system has no band gap; report its band gap and hole effective mass/velocity as null, and report the electron effective mass and carrier velocity at the Fermi level.

## Assets

- **Quantum ESPRESSO** — open-source DFT package for electronic-structure calculations based on plane waves and pseudopotentials. Access: https://www.quantum-espresso.org/
- **Ultrasoft pseudopotentials for C and Si** — pseudopotentials treating 4 valence electrons per atom (s²p²) for both carbon and silicon. Available from the SSSP precision library (https://www.materialscloud.org/discover/sssp) or as built-in pseudopotentials distributed with Quantum ESPRESSO.

No other external datasets, models, or pre-computed files are required. The atomic structures are constructed from the chirality and defect specifications described in the Approach section.

## Workflow steps

### Step 1: System setup and input generation
- Role: process
- Action: Construct unit cells for the four systems (ISW-NT, BSW-NT, ISW-NT with C vacancy, ISW-NT with Si vacancy) and generate Quantum ESPRESSO input files for structural relaxation. The (7,7) armchair nanotube unit cell contains 28 atoms in the pristine case and 27 atoms for each vacancy-defected case. The bundle uses a tetragonal unit cell with one nanotube per cell. For isolated tubes, set the cross-section (a and b) lattice parameters to 30 Å. Use ultrasoft pseudopotentials for C and Si (4 valence electrons, s²p²), a kinetic energy cutoff of 350 eV, Gaussian smearing of 0.1 eV, k-point grids of 1×1×20 (isolated tubes) and 8×8×8 (bundle).
- Evidence: none

### Step 2: Structural relaxation and equation-of-state fitting
- Role: process
- Action: For each of the four systems, perform variable-cell structural relaxation to minimise the total energy with respect to unit-cell volume and internal atomic positions. Compute the total energy at several unit-cell volumes spanning the equilibrium, then fit the energy-versus-volume data to Murnaghan's equation of state. From the fit, extract the equilibrium lattice constants (a, b, c), bulk modulus components (along a, b, c axes), tubular diameter (distance between opposite atomic centres on the tube circumference), and radial buckling (difference between the radii of the C and Si atomic shells). The fit also yields the minimum-energy volume, confirming the relaxed geometry.
- Evidence: none

### Step 3: Electronic structure calculation
- Role: process
- Action: Using the relaxed geometries obtained in Step 2, run spin-polarised DFT calculations: first a self-consistent field (SCF) calculation to obtain the ground-state charge density, then a non-self-consistent (NSCF) calculation on a dense k-point mesh, followed by a band-structure calculation along the high-symmetry path Γ → Z (the tube axis direction) to obtain Kohn-Sham eigenvalues. Compute the total density of states (TDOS) and the atom- and orbital-projected density of states (PDOS) for C and Si s and p orbitals. Extract the total magnetisation from the SCF output.
- Evidence: none

### Step 4: Compile all properties into results.json (load-bearing)
- Role: scored (load-bearing)
- Action: Post-process all DFT outputs from Steps 2 and 3 to extract and compile the complete set of physical properties for each of the four configurations into a single JSON file. For each system compute: lattice constants a, b, c (Å); tubular diameter (Å); radial buckling (Å); symmetry number (integer); bulk modulus along a, b, c axes (kbar, with a and b set to null for isolated tubes where they are not defined); band gap value (eV) and transition k-points as a descriptive string (for the metallic Si-vacancy system, report value and transition as null); effective mass of electrons (CB) and holes (VB) in units of m₀ (for the metallic system, report VB as null); carrier velocity v_z along the tube axis for CB and VB (m/s; VB null for metallic); charge density averages for s and p orbitals of C and Si plus total charge (e); total magnetisation (μB).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with four top-level keys: `ISW_NT`, `BSW_NT`, `ISW_NTC`, `ISW_NTSi`. Each key maps to an object containing all the property fields listed above. Numeric values should be stored as JSON numbers (not strings), with null used for undefined or inapplicable entries (in-plane bulk moduli for isolated tubes, band gap fields for metallic systems, hole effective mass and velocity for metallic systems).
- Scoring: scored by hidden verifier

## Output files

All artifacts must be written under `/app/outputs/`:

- `/app/outputs/results.json` — Complete structural and electronic properties for all four configurations, containing every quantity described in the Reproduction target.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Complete structural and electronic properties for all four SiC nanotube configurations. Each top-level key corresponds to one configuration and contains all computed quantities. Numeric values are JSON numbers; undefined entries use JSON null.
- schema:
  - `type`: object
  - `required`:
    - `ISW_NT`: object — properties for isolated (7,7) SiC nanotube
    - `BSW_NT`: object — properties for tetragonal bundle
    - `ISW_NTC`: object — properties for isolated tube with C line vacancy
    - `ISW_NTSi`: object — properties for isolated tube with Si line vacancy
  - `items`:
    - `lattice_constants`:
      - `a`: float (Å)
      - `b`: float (Å)
      - `c`: float (Å)
    - `tubular_diameter`: float (Å)
    - `radial_buckling`: float (Å)
    - `symmetry_number`: int
    - `bulk_modulus`:
      - `a`: float or null (kbar; null for isolated tubes)
      - `b`: float or null (kbar; null for isolated tubes)
      - `c`: float (kbar)
    - `band_gap`:
      - `value`: float or null (eV; null for metallic systems)
      - `transition`: string or null (e.g. '0.65 π/c → 0.95 π/c, Γ → Z'; null for metallic)
    - `effective_mass`:
      - `CB`: float (m₀)
      - `VB`: float or null (m₀; null for metallic systems)
    - `velocity_z`:
      - `CB`: float (m/s)
      - `VB`: float or null (m/s; null for metallic systems)
    - `charge_density`:
      - `s_C`: float (e)
      - `s_Si`: float (e)
      - `p_C`: float (e)
      - `p_Si`: float (e)
      - `total`: float (e)
    - `total_magnetization`: float (μB)

Notes: The verifier compares each numerical property against hidden reference values with appropriate per-quantity tolerances. Structural trends across configurations (e.g. ordering of axial lattice constants) are also checked. The metallic Si-vacancy system (ISW_NTSi) should report band_gap.value=null and band_gap.transition=null, with effective_mass.VB=null and velocity_z.VB=null. All systems are nonmagnetic; total_magnetization should be approximately zero.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ISW_NT": "object — properties for isolated (7,7) SiC nanotube",
          "BSW_NT": "object — properties for tetragonal bundle",
          "ISW_NTC": "object — properties for isolated tube with C line vacancy",
          "ISW_NTSi": "object — properties for isolated tube with Si line vacancy"
        },
        "items": {
          "lattice_constants": {
            "a": "float (Å)",
            "b": "float (Å)",
            "c": "float (Å)"
          },
          "tubular_diameter": "float (Å)",
          "radial_buckling": "float (Å)",
          "symmetry_number": "int",
          "bulk_modulus": {
            "a": "float or null (kbar; null for isolated tubes)",
            "b": "float or null (kbar; null for isolated tubes)",
            "c": "float (kbar)"
          },
          "band_gap": {
            "value": "float or null (eV; null for metallic systems)",
            "transition": "string or null (e.g. '0.65 π/c → 0.95 π/c, Γ → Z'; null for metallic)"
          },
          "effective_mass": {
            "CB": "float (m₀)",
            "VB": "float or null (m₀; null for metallic systems)"
          },
          "velocity_z": {
            "CB": "float (m/s)",
            "VB": "float or null (m/s; null for metallic systems)"
          },
          "charge_density": {
            "s_C": "float (e)",
            "s_Si": "float (e)",
            "p_C": "float (e)",
            "p_Si": "float (e)",
            "total": "float (e)"
          },
          "total_magnetization": "float (μB)"
        }
      },
      "description": "Complete structural and electronic properties for all four SiC nanotube configurations. Each top-level key corresponds to one configuration and contains all computed quantities. Numeric values are JSON numbers; undefined entries use JSON null."
    }
  ],
  "notes": "The verifier compares each numerical property against hidden reference values with appropriate per-quantity tolerances. Structural trends across configurations (e.g. ordering of axial lattice constants) are also checked. The metallic Si-vacancy system (ISW_NTSi) should report band_gap.value=null and band_gap.transition=null, with effective_mass.VB=null and velocity_z.VB=null. All systems are nonmagnetic; total_magnetization should be approximately zero."
}
```

## How you are scored

A hidden verifier reads your `results.json`, extracts each numerical property for each of the four configurations, and compares every quantity against independently established reference values using appropriate tolerances. Each category of property (lattice constants, band gap, bulk modulus, effective masses, velocities, charge densities, magnetisation) contributes a weighted portion to the final reward. The verifier also checks that structural trends are physically consistent (for example, the ordering of axial lattice constants across the four configurations). Simply reporting numbers that match a reference without genuinely running the DFT workflow is not sufficient — the verifier cross-validates internal consistency across related quantities. A missing or malformed `results.json` receives zero credit for that step.

---

**Note on compute resources**: This workflow requires running multiple DFT calculations (variable-cell relaxations at several volumes plus electronic-structure calculations) for four distinct systems. The total computational cost is substantial. You may use appropriate external or remote high-performance computing resources to execute the Quantum ESPRESSO calculations, then collect the final `results.json` under `/app/outputs/`. The verifier itself is lightweight and runs quickly in the sandbox.
