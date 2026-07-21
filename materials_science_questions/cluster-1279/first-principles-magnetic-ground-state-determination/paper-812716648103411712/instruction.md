# DFT study of XF₃ (X = Be, Mg, Ca, Sr, Ba) compounds: half‑metallicity, stability and mechanical properties

## Problem background
Spintronic devices require materials that achieve full spin polarization, i.e., half‑metallic (HM) behavior where one spin channel is semiconducting and the other metallic. Heusler alloys without transition metals (d⁰ systems) are promising because they can offer small magnetic moments, wide spin gaps, and high Curie temperatures. The binary Heusler alloys XF₃ (X = Be, Mg, Ca, Sr, Ba) crystallize in the DO₃ structure. The high electronegativity of fluorine suggests strong ionic bonding with the alkaline‑earth X atoms, which may lead to robust half‑metallicity. This task aims to compute the structural, electronic, magnetic, and mechanical properties of these alloys from first principles, including the preservation of half‑metallicity under hydrostatic and tetragonal strains, to assess their suitability for spintronic applications.

## Approach
Use density functional theory (DFT) with the generalized gradient approximation (GGA) in the Perdew‑Burke‑Ernzerhof (PBE) form and projector augmented wave (PAW) potentials. Construct DO₃ unit cells for each alloy XF₃, placing F atoms at Wyckoff positions A(0,0,0), B(¼,¼,¼), C(½,½,½) and the X atom at D(¾,¾,¾).

Perform spin‑polarized total energy calculations for non‑magnetic (NM), ferromagnetic (FM), and antiferromagnetic (AFM) configurations. For the AFM configuration, set the initial magnetic moment of the F atom at Wyckoff position B opposite to that of the FM state while keeping the moments on the other atoms (F(A), F(C), and X) identical to those in the FM state; this corresponds to an antiferromagnetic ordering of the largest magnetic sublattice. Fit energy‑volume curves to locate the equilibrium lattice constant of the FM phase and confirm it as the ground state. Compute formation energy from the total energy of the compound and the bulk reference energies of elemental X and F; compute cohesive energy from the isolated‑atom energies and the compound total energy. Estimate the Curie temperature from the energy difference between AFM and FM phases via a mean‑field relation.

With the FM equilibrium geometry, compute the spin‑polarized density of states (DOS) and band structure. Determine the valence band maximum (VBM) and conduction band minimum (CBM) in the spin‑up channel, the spin‑up indirect gap, and the half‑metallic gap (the smallest absolute value among VBM and CBM). Verify that a gap exists in the spin‑up channel while the spin‑down channel is metallic. Integrate the total DOS to obtain the total magnetic moment and extract site‑resolved atomic magnetic moments and the interstitial moment.

Obtain the elastic constants C₁₁, C₁₂, C₄₄ by applying small distortions and analyzing the resulting energy changes. From these constants, derive the bulk modulus, shear modulus, Young’s modulus, Poisson’s ratio, Pugh’s ratio, and the anisotropy factor using the Voigt–Reuss–Hill averaging scheme.

Finally, investigate the robustness of half‑metallicity under hydrostatic strain (isotropic expansion/compression) and tetragonal strain (varying c/a ratio at constant volume). For each strain, compute the spin‑up band gap and half‑metallic gap. Identify the strain intervals (or c/a intervals) within which the half‑metallic gap remains positive, thereby defining the stability range of the HM state.

## Computational parameters (DFT settings)
All DFT calculations must use the following convergence‑critical parameters:

- Plane‑wave cutoff energy: **500 eV**  
- k‑point mesh for Brillouin‑zone sampling: **15 × 15 × 15**  
- Smearing method: **Gaussian** with a width of **0.2 eV**  
- Self‑consistent field (SCF) convergence criterion for total energy: **1 × 10⁻⁵ eV**  
- Maximum Hellmann‑Feynman force tolerance during structural relaxation: **0.02 eV/Å**

Use PAW pseudopotentials with the valence configurations listed below, and treat the exchange‑correlation functional at the PBE level:

- F: 2s²2p⁵  
- Be: 2s²  
- Mg: 3s²  
- Ca: 3p⁶4s²  
- Sr: 4s²4p⁶5s²  
- Ba: 5s²5p⁶6s²

These valence configurations are exactly those employed in the original study and must be used to ensure consistency.

> **Note on DFT code choice:** The original study used VASP, but you may use any DFT code that supports PAW potentials and the GGA‑PBE functional (e.g., GPAW, Quantum ESPRESSO, ABINIT). The use of different PAW‑code implementations may introduce small systematic shifts, but the expected deviations are within the tolerances accepted by the scoring verifier. No special tuning is required; simply adhere to the prescribed settings and valence configurations.

## Reference energies for formation and cohesion
To compute the formation energy  
E_f = E_tot − (E_X^bulk + 3 E_F^bulk),  
the reference energy E_F^bulk must be obtained from the F₂ molecule rather than any hypothetical solid phase of fluorine: calculate the total energy of an isolated F₂ molecule in a large supercell using the same DFT settings, and take E_F^bulk = E_F₂ / 2 (i.e., the energy per F atom).  
E_X^bulk is the energy per atom of the elemental solid X (Be, Mg, Ca, Sr, Ba) in its most stable bulk phase.  
For the cohesive energy, use the isolated‑atom energies of X and F, all computed with the same functional and pseudopotentials as the compounds.

## Elastic constants extraction
The three independent elastic constants C₁₁, C₁₂, and C₄₄ of the cubic (space group 225) XF₃ compounds are obtained by applying small, volume‑conserving strains to the equilibrium FM unit cell and fitting the resulting energy changes.

**Strain tensors** (E is the Green–Lagrange strain):

1. **Orthorhombic strain** (to obtain C₁₁ − C₁₂):  
   ```
   ( δ   0   0 )
   ( 0  −δ   0 )
   ( 0   0  δ²/(1−δ²) )
   ```
   The total energy change per unit volume follows  
   ΔE/V₀ = (C₁₁ − C₁₂) δ² + O(δ⁴).  
   Fit ΔE/V₀ vs. δ² for several small δ (e.g., |δ| ≤ 0.02) to extract (C₁₁ − C₁₂).

2. **Monoclinic strain** (to obtain C₄₄):  
   ```
   ( 0   δ/2   0 )
   ( δ/2 0     0 )
   ( 0   0    δ²/(4−δ²) )
   ```
   The energy change behaves as  
   ΔE/V₀ = (C₄₄/2) δ² + O(δ⁴).  
   Fit ΔE/V₀ vs. δ² to extract C₄₄.

The remaining constant C₁₁ is derived from the bulk modulus B via equilibrium equation of state fitting (e.g., Murnaghan or Birch–Murnaghan). For a cubic crystal, the bulk modulus is  
B = (C₁₁ + 2C₁₂)/3, so  
C₁₁ = 3B − 2C₁₂.  
Alternatively, if the isotropically deformed energy‑volume curve is fitted to obtain B, then with (C₁₁ − C₁₂) and B one can solve for C₁₁ and C₁₂ independently.

## Voigt–Reuss–Hill averaging for mechanical moduli
From the elastic constants C₁₁, C₁₂, C₄₄ (in GPa), the polycrystalline mechanical moduli are computed with the Voigt–Reuss–Hill scheme:

B = (C₁₁ + 2 C₁₂) / 3  
G_V (Voigt shear) = (C₁₁ − C₁₂ + 3 C₄₄) / 5  
G_R (Reuss shear) = 5 (C₁₁ − C₁₂) C₄₄ / [4 C₄₄ + 3 (C₁₁ − C₁₂)]  
G (Hill shear) = (G_V + G_R) / 2  

Young’s modulus: E = 9 B G / (3 B + G)  
Poisson’s ratio: ν = (3 B − 2 G) / [2 (3 B + G)]  
Pugh’s ratio: K = B / G  
Elastic anisotropy factor: A = 2 C₄₄ / (C₁₁ − C₁₂)

## Interstitial magnetic moment
The total magnetic moment per formula unit M_t (in μB) is obtained by integrating the spin‑polarized DOS up to the Fermi level (M_t = N↑ − N↓). The atomic magnetic moments are obtained from the site‑projected spin densities. The interstitial magnetic moment M_int is then computed as:

M_int = M_t − (M_F_A + M_F_B + M_F_C + M_X)

where M_F_A, M_F_B, M_F_C are the magnetic moments of the fluorine atoms at Wyckoff positions A, B, C and M_X is the magnetic moment of the alkaline‑earth atom. This definition follows the standard DFT output convention in which the “interstitial” contribution is the residual spin density not assigned to any atomic sphere.

## Reproduction target
For each of the five compounds BeF₃, MgF₃, CaF₃, SrF₃, and BaF₃, follow the DFT workflow and output a single JSON file (`calculated_properties.json`) that contains the following quantities:
- equilibrium lattice constant a (Å)
- formation energy E_f (eV/f.u.)
- cohesive energy E_c (eV/f.u.)
- Curie temperature T_C (K)
- total magnetic moment M_t (μB/f.u.)
- spin‑up band gap E_g_up (eV)
- half‑metallic gap E_g_HM (eV)
- valence band maximum VBM (eV) and conduction band minimum CBM (eV)
- atomic magnetic moments: M_F_A, M_F_B, M_F_C, M_X (μB/atom)
- interstitial magnetic moment M_int (μB/f.u.)
- elastic constants C11, C12, C44 (GPa) and derived moduli: bulk modulus B, shear modulus G, Young’s modulus E (all GPa), Poisson’s ratio ν, Pugh’s ratio K, anisotropy factor A
- hydrostatic strain range that preserves half‑metallicity: min_strain and max_strain (in %)
- tetragonal strain range that preserves half‑metallicity: min_c_over_a and max_c_over_a.

All values must be computed from first‑principles DFT calculations with the prescribed exchange‑correlation functional and PAW potentials, and using the numerical settings specified above. The objective is to produce a complete set of these properties as numerical entries in the JSON output.

## Assets

- DFT code with GGA‑PBE and PAW support: https://wiki.fysik.dtu.dk/gpaw/
- PAW pseudopotentials for Be, Mg, Ca, Sr, Ba, F: https://materialscloud.org/sssp/

## Workflow steps

### Step 1: Generate DO₃ crystal structures
- Role: process
- Action: For each X in Be, Mg, Ca, Sr, Ba, create a DO₃ unit cell (space group 225) with F(A), F(B), F(C) and X at Wyckoff coordinates A(0,0,0), B(¼,¼,¼), C(½,½,½), D(¾,¾,¾).
- Evidence: none

### Step 2: Calculate bulk reference energies
- Role: process
- Action: Using DFT (GGA‑PBE, PAW pseudopotentials), compute the total energy per atom of bulk elemental X (Be, Mg, Ca, Sr, Ba) in their stable phases. For fluorine, compute the total energy of an isolated F₂ molecule and obtain E_F_bulk = E_F₂ / 2 (energy per F atom). Use the same computational parameters (cutoff, k‑mesh, smearing, convergence) as for the compounds.
- Evidence: none

### Step 3: Calculate isolated atom reference energies
- Role: process
- Action: Compute total energy of isolated X and F atoms in large supercells using the same DFT settings.
- Evidence: none

### Step 4: Determine magnetic ground state and equilibrium lattice constants
- Role: process
- Action: Perform spin‑polarized DFT total‑energy calculations for non‑magnetic, antiferromagnetic, and ferromagnetic configurations. For the AFM configuration, initialize the magnetic moment of the F atom at Wyckoff B opposite to that of the FM state, leaving other moments unchanged. Compute energy‑volume curves. Determine equilibrium lattice constant for the FM phase and confirm FM is the lowest‑energy magnetic ordering.
- Evidence: `/app/outputs/energy_volume_data.json`

### Step 5: Compute thermodynamic stability and Curie temperature
- Role: process
- Action: Using the total energy of the FM compound, bulk reference energies (with F_bulk from F₂ molecule), and isolated‑atom energies, compute formation energy E_f = E_tot − (E_X_bulk + 3 E_F_bulk) and cohesive energy E_c = E_X_atom + 3 E_F_atom − E_tot. Estimate Curie temperature from the AFM‑FM energy difference using the mean‑field expression T_C = 2(E_AFM − E_FM) / (3 k_B), where k_B is the Boltzmann constant.
- Evidence: none

### Step 6: Compute electronic density of states and band structure
- Role: process
- Action: At the FM equilibrium geometry, perform a spin‑polarized SCF calculation with a dense k‑point mesh. Compute total and atom‑projected DOS and orbital‑projected band structure. Extract valence band maximum (VBM), conduction band minimum (CBM) in the spin‑up channel, spin‑up indirect band gap E_g_up = CBM − VBM, and half‑metallic gap E_g_HM = min(|VBM|, |CBM|). Verify a band gap in the spin‑up channel while the spin‑down channel is metallic.
- Evidence: `/app/outputs/dos_data.json`

### Step 7: Compute magnetic moments
- Role: process
- Action: Integrate the spin‑polarized total DOS up to the Fermi level to obtain numbers of valence electrons per formula unit N_up and N_down. Compute total magnetic moment M_t = N_up − N_down. Extract atomic magnetic moments on F(A), F(B), F(C), and X sites from self‑consistent DFT output, and compute the interstitial moment as M_int = M_t − (M_F_A + M_F_B + M_F_C + M_X).
- Evidence: none

### Step 8: Compute elastic constants and mechanical properties
- Role: process
- Action: Apply small strains to the equilibrium FM unit cell as described in the “Elastic constants extraction” section. Compute resulting energy changes to extract elastic constants C11, C12, C44. Using the Voigt–Reuss–Hill averaging formulas, calculate bulk modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio ν, Pugh’s ratio K = B/G, and anisotropy factor A = 2 C44/(C11 − C12).
- Evidence: none

### Step 9: Investigate strain effects on half‑metallicity
- Role: process
- Action: Perform DFT calculations for a range of hydrostatic strains (isotropic lattice changes) and tetragonal strains (varying c/a at fixed volume). At each strain point compute the spin‑up band gap and HM gap. Determine the bounds (minimum and maximum strain, or c/a ratio) within which the HM gap remains positive (half‑metallicity preserved).
- Evidence: `/app/outputs/strain_data.json`

### Step 10: Collect and output all calculated properties
- Role: scored (load‑bearing)
- Action: Gather all computed values from the previous steps and write them into a single JSON file according to the output contract.
- Output file: `/app/outputs/calculated_properties.json`
- Format: json
- Contract: Top‑level object with keys 'BeF3', 'MgF3', 'CaF3', 'SrF3', 'BaF3'. Each value is an object containing numeric fields: a (lattice constant in Å), E_f (formation energy eV/f.u.), E_c (cohesive energy eV/f.u.), T_C (Curie temperature K), M_t (total magnetic moment μB/f.u.), E_g_up (spin‑up band gap eV), E_g_HM (half‑metallic gap eV), VBM (eV), CBM (eV), M_F_A, M_F_B, M_F_C, M_X (atomic magnetic moments μB/atom), M_int (interstitial moment μB/f.u.), C11, C12, C44 (elastic constants GPa), B (bulk modulus GPa), G (shear modulus GPa), E (Young’s modulus GPa), nu (Poisson’s ratio), K (Pugh’s ratio), A (anisotropy factor), hydrostatic_HM_range (object with min_strain and max_strain in %), tetragonal_HM_range (object with min_c_over_a and max_c_over_a).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_properties.json
- path: `/app/outputs/calculated_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All computed physical properties for the five XF3 compounds. The checker compares these values to the paper‑reported references with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `BeF3`: object
    - `MgF3`: object
    - `CaF3`: object
    - `SrF3`: object
    - `BaF3`: object
  - `items`:
    - `a`: number (Å)
    - `E_f`: number (eV/f.u.)
    - `E_c`: number (eV/f.u.)
    - `T_C`: number (K)
    - `M_t`: number (μB/f.u.)
    - `E_g_up`: number (eV)
    - `E_g_HM`: number (eV)
    - `VBM`: number (eV)
    - `CBM`: number (eV)
    - `M_F_A`: number (μB/atom)
    - `M_F_B`: number (μB/atom)
    - `M_F_C`: number (μB/atom)
    - `M_X`: number (μB/atom)
    - `M_int`: number (μB/f.u.)
    - `C11`: number (GPa)
    - `C12`: number (GPa)
    - `C44`: number (GPa)
    - `B`: number (GPa)
    - `G`: number (GPa)
    - `E`: number (GPa)
    - `nu`: number
    - `K`: number
    - `A`: number
    - `hydrostatic_HM_range`:
      - `min_strain`: number (%)
      - `max_strain`: number (%)
    - `tetragonal_HM_range`:
      - `min_c_over_a`: number
      - `max_c_over_a`: number

Notes: The agent must compute each property by running the DFT workflow. The scored output is a single JSON file; all required fields must be present and numeric. Tolerances are hidden.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BeF3": "object",
          "MgF3": "object",
          "CaF3": "object",
          "SrF3": "object",
          "BaF3": "object"
        },
        "items": {
          "a": "number (Å)",
          "E_f": "number (eV/f.u.)",
          "E_c": "number (eV/f.u.)",
          "T_C": "number (K)",
          "M_t": "number (μB/f.u.)",
          "E_g_up": "number (eV)",
          "E_g_HM": "number (eV)",
          "VBM": "number (eV)",
          "CBM": "number (eV)",
          "M_F_A": "number (μB/atom)",
          "M_F_B": "number (μB/atom)",
          "M_F_C": "number (μB/atom)",
          "M_X": "number (μB/atom)",
          "M_int": "number (μB/f.u.)",
          "C11": "number (GPa)",
          "C12": "number (GPa)",
          "C44": "number (GPa)",
          "B": "number (GPa)",
          "G": "number (GPa)",
          "E": "number (GPa)",
          "nu": "number",
          "K": "number",
          "A": "number",
          "hydrostatic_HM_range": {
            "min_strain": "number (%)",
            "max_strain": "number (%)"
          },
          "tetragonal_HM_range": {
            "min_c_over_a": "number",
            "max_c_over_a": "number"
          }
        }
      },
      "description": "All computed physical properties for the five XF3 compounds. The checker compares these values to the paper-reported references with appropriate tolerances."
    }
  ],
  "notes": "The agent must compute each property by running the DFT workflow. The scored output is a single JSON file; all required fields must be present and numeric. Tolerances are hidden."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. It reads your `calculated_properties.json` and compares each computed property to reference values using appropriate tolerances. The overall score is a weighted sum over the property groups: half‑metallic character and band gaps, magnetic moments, elastic constants, lattice constants and thermodynamics, and strain robustness ranges. Some checks verify required structural relationships (e.g., mechanical stability conditions, integer magnetic moment, and qualitative trends across the compound series). Meeting or exceeding the reference quality yields full credit; larger deviations lead to reduced partial credit. Simply guessing or copying numbers without running the actual DFT calculations will not produce a score that matches the expected hidden tolerances. No manual inspection is performed; scoring is fully automatic.