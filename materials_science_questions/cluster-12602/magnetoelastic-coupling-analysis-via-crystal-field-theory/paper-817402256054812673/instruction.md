# Magnetoelastic coupling and surface energy analysis of Fe‑Ga alloys via DFT

## Objective
Fe‑Ga alloys (Galfenol) are rare‑earth‑free magnetostrictive materials. This task has two goals:

1. **Bulk substitution effect** – Build a 128‑atom supercell of Fe₇₉.₇Ga₂₀.₃ and two ternary analogues where two Ga atoms are replaced by Ag or Cu (Fe₇₉.₇Ga₁₈.₇Ag₁.₆, Fe₇₉.₇Ga₁₈.₇Cu₁.₆). Compute total energies and magnetocrystalline anisotropy energies (E_MCA) under tetragonal strain (±1%) using DFT with spin–orbit coupling and the torque method. From these raw data the magnetoelastic coupling coefficient *B*₁ and the tetragonal shear modulus *C′* can be derived by finite differences.

2. **Rigid‑band analysis** – For the pristine alloy, use the self‑consistent electronic structure at ±1% strain to perform a rigid‑band scan: shift the Fermi level to vary the total number of valence electrons *N*_e and recompute E_MCA. The output should show how the difference between the +1% and −1% strain curves behaves as *N*_e moves away from the system’s actual electron count.

3. **Surface energies with adsorbates** – Build slab models for three low‑index facets ((001), (110), (111)) with different Ga coverages in the topmost layer and with adsorbates (O, Os, H₂S) as well as clean surfaces. Compute the surface energy γ as a function of a variable Ga chemical potential, using a bulk equilibrium constraint.

You must write the three output files described in **Output files**.

---

## DFT calculation parameters
All DFT calculations must be performed with spin‑polarized GGA‑PBE, using the projector augmented wave (PAW) method. The following numerical settings must be used (derived from the literature on Fe–Ga):

- **Plane‑wave cutoff**: 500 eV  
- **k‑point meshes**:  
  - Bulk supercells: **5×5×5** Monkhorst–Pack grid  
  - Surface slab models: **7×7×1** Monkhorst–Pack grid  
- **Convergence criteria**:  
  - Forces on each atom < **0.01 eV/Å**  
  - Total energy convergence < **10⁻⁵ eV**  
- **Spin–orbit coupling (SOC)**: must be included for all magnetocrystalline anisotropy calculations. Use the torque method to obtain E_MCA from the expectation value of the angular derivative of the SOC Hamiltonian.
- **Valence states**: Fe‑3d4s4p, Ga‑4s4p, Cu‑3d4s, Ag‑4d5s, O‑2s2p, Os‑5d6s, S‑3s3p, H‑1s. Use standard PAW pseudopotentials that treat these electrons as valence.

---

## 1. Bulk alloys – strain and magnetocrystalline anisotropy

### Supercell construction
- **Pristine alloy**: a 4×4×4 supercell of the bcc‑derived Fe–Ga matrix, containing 128 atoms: 102 Fe and 26 Ga. This corresponds to the composition Fe₇₉.₇Ga₂₀.₃.
- **Ternary alloys**: create Fe₇₉.₇Ga₁₈.₇Ag₁.₆ and Fe₇₉.₇Ga₁₈.₇Cu₁.₆ by replacing **two** Ga atoms in the pristine supercell with Ag or Cu atoms. The two substitutional atoms must be placed **far apart** (distance > 4.1 Å) to avoid unphysical clustering.
- Fully relax all atomic positions and lattice parameters (both cell shape and volume) for the unstrained supercells before applying strain.

### Strain protocol
- Apply tetragonal strains **ε_z** of **–1%, 0%, +1%** along the *z* axis, while keeping the volume constant:  
  **ε_x = ε_y = –ε_z / 2**.
- For each strain, perform a self‑consistent DFT‑SOC calculation to obtain:
  - Total energy **E_total** (eV per supercell)
  - Magnetocrystalline anisotropy energy **E_MCA** (eV per supercell) obtained via the torque method.

### Output
Write the results to `/app/outputs/strain_and_emca_results.csv` with columns:  
`Alloy`, `Strain`, `E_total`, `E_MCA`.

---

## 2. Rigid‑band analysis of MCA vs electron count

Using the **self‑consistent charge density** of pristine Fe₇₉.₇Ga₂₀.₃ at ±1% strain, perform rigid‑band calculations:

- Shift the Fermi level (i.e., change the number of valence electrons in the supercell) while **keeping the charge density frozen**.
- Recompute E_MCA for each integer total valence electron count *N*_e.
- Evaluate *N*_e from **1140 to 1168** in steps of 2, for both the +1% and –1% strain states.
- Express the E_MCA values **per atom** (i.e., divide the supercell E_MCA by 128).

### Output
Write the results to `/app/outputs/emca_vs_electron_count.csv` with columns:  
`N_e`, `strain_plus1_E_MCA`, `strain_minus1_E_MCA`  
(units: *N*_e – integer count; E_MCA – eV per atom).

---

## 3. Surface energies with adsorbates

### Slab construction
For each of the three orientations (001), (110) and (111):

- Build a slab model of **9 atomic layers** with a **12 Å** vacuum gap.
- The in‑plane supercell should contain **4 surface atoms per layer** (i.e., a 2×2 expansion of the primitive surface cell) so that Ga coverages of 0%, 50%, 75% and 100% in the topmost layer can be realised.
- **Coverage definitions and top‑layer Ga placement**:  
  Label the four top‑layer sites by their fractional in‑plane coordinates relative to the surface unit cell: (0,0), (1,0), (0,1), (1,1). Fix the following Ga occupation pattern for each coverage to obtain a unique, deterministic slab model:
  - **0%** – No Ga; all four sites are Fe.
  - **50%** – Place Ga at sites (0,0) and (1,1) (maximally separated); the other two sites are Fe.
  - **75%** – Place Ga at sites (0,0), (1,0), (0,1); the remaining site (1,1) is Fe.
  - **100%** – All four sites are Ga.
  (In all cases, the deeper layers consist of the bulk‑like Fe‑Ga matrix; keep the total number of Fe and Ga atoms in the slab consistent with the target composition except for the deliberate top‑layer substitution described above.)
- For each orientation and coverage, prepare both a **clean** slab and slabs with one adsorbate:
  - **O atom** – placed on an **atop site**.  
    *Rule*: If the top layer contains Ga, attach O to the Ga atom at site (0,0) (or, for coverages where (0,0) is Fe, use the first Ga site encountered when scanning sites in order (0,0) → (1,0) → (0,1) → (1,1)). If the top layer has no Ga (0% coverage), attach O to the Fe atom at (0,0).
  - **Os atom** – placed on a **bridge site** between two neighbouring top‑layer atoms.  
    *Rule*: Prefer a bridge connecting a Ga and an Fe if such a pair exists. For 50% coverage, use the Ga‑Fe pair (0,0)‑(1,0). For 75%, use the Ga‑Fe pair (0,0)‑(1,1). For 100% (no Fe), use the Ga‑Ga bridge (0,0)‑(1,0). For 0% (no Ga), use the Fe‑Fe bridge (0,0)‑(1,0).
  - **H₂S molecule** – placed on an **atop site**, preferentially on Ga if present (using the same site‑selection rule as for O).
- Perform full DFT relaxation of all atomic positions for all slab models.

### Chemical potentials and reference states
The surface energy γ (J/m²) for a slab with *N_Fe* iron atoms, *N_Ga* gallium atoms, *N_ads* adsorbate molecules/atoms, and total DFT energy *E_slab* is:

**γ = (1 / 2A) [E_slab – N_Fe μ_Fe – N_Ga μ_Ga – N_ads μ_ads]**

where *A* is the surface area of one side of the slab (use the in‑plane dimensions of the supercell).

**Chemical potential references:**

- **μ_Fe** – taken as the total energy per atom of **bcc Fe** in its ground state.
- **μ_Ga** – treated as a variable (see below).
- **μ_O** = ½ E(O₂)   (energy of an isolated O₂ molecule)
- **μ_Os** = energy per atom of **hcp Os** metal
- **μ_H₂S** = energy of an isolated H₂S molecule
- **μ_Fe₁₃Ga₃** – the total energy of a bulk **D0₃‑ordered Fe₁₃Ga₃** system.
  - **Construction**: Build a 2×2×2 supercell of the bcc lattice (16 atoms). To realize the D0₃‑type ordering with three Ga atoms and 13 Fe atoms, place the Ga atoms at the following fractional coordinates (expressed with respect to the conventional cubic unit cell; the lattice constant *a* is to be fully relaxed):
    - Ga1: (0, 0, 0)
    - Ga2: (0, ½, ½)
    - Ga3: (½, 0, ½)
    All remaining 13 sites are Fe. This arrangement ensures that no two Ga atoms are first‑nearest neighbours, consistent with the D0₃ ordering tendency in Fe‑Ga.
  - Fully relax the cell shape, volume, and atomic positions. The resulting total energy **E_bulk_Fe₁₃Ga₃** is the value of μ_Fe₁₃Ga₃.

**Constraint:**  
The chemical potentials of the bulk phase must satisfy  

**μ_Fe₁₃Ga₃ = 13 μ_Fe + 3 μ_Ga**.

For each chosen value of μ_Ga you must determine μ_Fe from this relation, while not allowing μ_Fe to exceed the bcc Fe value (μ_Fe⁰). Explicit procedure:

1. Fix a target μ_Ga (the values you will use are from **–4.0 eV to 0.0 eV** in steps of ≤ 0.5 eV).
2. Compute μ_Fe_candidate = (μ_Fe₁₃Ga₃ – 3 μ_Ga) / 13.
3. If μ_Fe_candidate ≤ μ_Fe⁰, use μ_Fe = μ_Fe_candidate; otherwise set μ_Fe = μ_Fe⁰ (the latter corresponds to an Fe‑rich limit where bulk Fe precipitates).
4. Plug these μ_Fe and μ_Ga into the surface energy formula.

### Output
Write the results to `/app/outputs/surface_energies.csv` with columns:  
`Orientation`, `Ga_coverage`, `Adsorbent`, `mu_Ga`, `Surface_energy`.  
`Orientation` is a string: `001`, `110` or `111`.  
`Ga_coverage` is a string: `0%`, `50%`, `75%`, `100%`.  
`Adsorbent` is a string: `none`, `O`, `Os`, `H2S`.  
`mu_Ga` is in eV, `Surface_energy` in J/m².

---

## Output files (summary)
All CSV files must be placed under `/app/outputs`.

| File name | Required columns |
|-----------|------------------|
| `strain_and_emca_results.csv` | `Alloy`, `Strain`, `E_total`, `E_MCA` |
| `emca_vs_electron_count.csv` | `N_e`, `strain_plus1_E_MCA`, `strain_minus1_E_MCA` |
| `surface_energies.csv` | `Orientation`, `Ga_coverage`, `Adsorbent`, `mu_Ga`, `Surface_energy` |

The detailed schema (units, formats) is given in the sections above.

---

## Workflow summary

1. **Relax bulk supercells** (pristine, Ag‑substituted, Cu‑substituted).
2. **Apply strains** (±1% and 0%) and compute total energies and E_MCA with SOC torque method → `strain_and_emca_results.csv`.
3. **Rigid‑band scan**: using the pristine alloy’s SCF density at ±1% strain, shift the Fermi level to vary *N*_e and recompute E_MCA per atom → `emca_vs_electron_count.csv`.
4. **Build surface slabs** for the three orientations, all coverages, and all adsorbents; relax geometries.
5. **Compute surface energies** for each slab/adsorbate combination using the chemical‑potential formalism described above, for μ_Ga from –4.0 eV to 0.0 eV (≤ 0.5 eV step) → `surface_energies.csv`.

No intermediate log files are required; only the three CSV files listed above will be evaluated.