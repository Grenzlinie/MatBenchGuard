# First-principles determination of interlayer exchange coupling in Fe/Cr superlattices

## Problem background
Interlayer exchange coupling in magnetic multilayers is a key phenomenon for spintronic devices. Fe/Cr superlattices show ferromagnetic (FM) coupling for very thin Cr layers and antiferromagnetic (AFM) coupling for thicker ones, with the coupling strength oscillating with Cr thickness. The electronic mechanism is thought to involve both direct d–d hybridization between Fe and Cr and indirect coupling via sp electrons, but their relative contributions and the thickness dependence are not fully understood.

## Approach
We use density functional theory (DFT) within the local spin density approximation (LSDA) to model b.c.c. (001) Fe/Cr superlattices. Following the theoretical setup of the original study, the periodic unit cell contains **2m** Fe atomic layers and **2n** Cr atomic layers, with m fixed to 3 (so **6** Fe layers per cell). The parameter n is the Cr thickness index; we consider n = 3, 4, 5, 6, 7, giving Cr layer counts of 6, 8, 10, 12, 14 respectively. Each atomic layer in the cell is represented by a single atom with all spins in that plane aligned identically.

For each n, self-consistent total-energy calculations are performed for two magnetic configurations:
- **Ferromagnetic (FM)**: All Fe magnetic moments aligned in the same direction.
- **Antiferromagnetic (AFM)**: Fe moments on neighbouring Fe layers point in opposite directions.

The energy difference **ΔE = (E_AFM – E_FM) / (n + m)** (in meV/atom) determines which ordering is stable (ΔE > 0 ⇒ FM; ΔE < 0 ⇒ AFM). The normalization factor (n + m) corresponds to the number of inequivalent layers in the cell (one atom per layer in the ASW description used in the paper), ensuring a direct comparison with the normalized results reported in the literature.

To disentangle the sp and d contributions to interlayer coupling, a non-self-consistent band analysis is performed **only for n = 5** (the strongest coupling case, as will be verified by the total-energy calculations). Starting from the self-consistent AFM solution, a ferromagnetic reference state is constructed by flipping all spins of one sublattice (for example, flipping all Cr layers that have negative moments or flipping the entire spin array of half the cell) so that all Fe moments become parallel. The electronic potentials are then frozen, and the band energies are recomputed with a common energy reference. The integrated number-of-states difference ΔN_{F−AF}(E) is computed separately for the sp and d characters of Fe and Cr atoms, yielding four curves: Fe_sp, Fe_d, Cr_sp, Cr_d. The resulting ΔN(E) curves reveal the energy ranges where the conduction electrons (sp) or d electrons favour the FM or AFM alignment.

## DFT parameters and computational details
The primitive cell is body-centred cubic (001) with experimental in-plane lattice constant **a = 2.829 Å** (fixed by substrate epitaxy). The perpendicular interlayer spacing is taken as **2.875 Å**, the average of elemental Fe and Cr lattice constants.

Use an **all-electron DFT code capable of LSDA** (e.g., Elk, with the `tasks` 0, 1, …; or Quantum ESPRESSO with appropriate pseudopotentials; note that any code producing consistent LSDA results is acceptable).

**Essential parameters:**
- k‑point mesh: **8 × 8 × 2** (or 8 × 8 × 4 if Brillouin zone symmetry permits; the mesh must be **identical** for the FM and AFM calculations to ensure consistent numerical differences).
- Plane‑wave energy cutoff or basis‑set equivalent: **at least 60 Ry** (for Elk, `rgkmax` around 7.0; for plane‑wave codes, 400 eV) and convergence to within **0.1 mRy/atom** in total energy.
- Self‑consistent field (SCF) convergence: total energy change < **10⁻⁶ Ry** or **10⁻⁵ eV** between iterations, and charge density change < **10⁻⁶**.
- Magnetic calculations: collinear spin polarisation; treat both Fe and Cr as magnetic; start from local magnetic moments in the neighbourhood of bulk values (Fe ~ 2.15 μB, interfacial Fe ~ 1.8 μB, interfacial Cr small and AFM‑coupled to Fe).

For each n, run two independent SCF calculations (FM and AFM). Save the total energy, the self‑consistent potentials, and the local magnetic moments for each atomic layer.

## Reproduction steps

### Step 1: Build Fe6/Cr₂n superlattice structural models
Construct the b.c.c. (001) Fe₆/Cr₂n unit cells for n=3,4,5,6,7. Use the lattice parameters and geometry described above. The cell contains exactly 2m = 6 Fe layers and 2n Cr layers; set initial atomic positions and spin orientations corresponding to the FM and AFM configurations (e.g., for AFM, alternate the sign of Fe moments; for FM, keep all Fe moments the same).

### Step 2: Self-consistent DFT total-energy calculations
Run the DFT calculations defined in the previous section for each n and both magnetic configurations (FM and AFM). Store the converged total energies and the complete set of potentials (including the effective potential, charge density, and magnetisation density) for each case. The AFM results for n=5 will be used in Step 4.

### Step 3: Magnetic ground state from total energies
For each n, extract the total energies from Step 2 and compute **ΔE = (E_AFM – E_FM) / (n + m)** in meV/atom (m=3). Determine the stable configuration: FM if ΔE > 0, AFM if ΔE < 0. Write a JSON file with exactly the required keys.

**Output file:** `/app/outputs/stability_table.json`
- Object with keys `"n=3"`, `"n=4"`, `"n=5"`, `"n=6"`, `"n=7"`.
- Each value is an object with `"delta_E"` (float, meV/atom) and `"stable_config"` (string, either `"FM"` or `"AFM"`).
- This file is scored.

### Step 4: Non-self-consistent band analysis for sp and d contributions at n=5
**Only for n=5**, perform the frozen‑potential analysis:

1. Take the self‑consistent AFM solution from Step 2.
2. Build a ferromagnetic reference configuration: flip half of the spins (for example, reverse the sign of the magnetisation density for all atoms belonging to one of the two spin sublattices defined by the AFM ordering) so that the cell becomes effectively FM in its magnetic alignment.
3. Freeze the resulting effective potentials.
4. Perform a non‑self‑consistent band energy calculation on this FM‑like configuration, ensuring the same k‑point mesh and basis set are used.
5. For the **same** AFM solution, perform an analogous band calculation (using the frozen AFM potentials).
6. For each atomic layer, decompose the density of states into `sp` and `d` characters, and compute the integrated number‑of‑states difference:

   **ΔN_{F−AF}(E) = ∫₋∞ᴱ [ n_AF(ε) – n_FM(ε) ] dε**

   over an energy range of **–0.5 eV to +0.1 eV relative to the Fermi level** (step size ~0.02 eV or finer). Sum the contributions separately for all Fe atoms and all Cr atoms in the cell, yielding four curves: `Fe_sp`, `Fe_d`, `Cr_sp`, `Cr_d`.

7. Write the results as an object of four arrays, each containing [energy_eV, delta_N] pairs.

**Output file:** `/app/outputs/delta_N_curves_n5.json`
- Object with keys `"Fe_sp"`, `"Fe_d"`, `"Cr_sp"`, `"Cr_d"`.
- Each value is a list of points `[energy_in_eV, ΔN]`.
- This file is scored.

## Output files
Write all artifacts under `/app/outputs`:
- `stability_table.json`
- `delta_N_curves_n5.json`

## Output contract
The exact schema required by the verifier is given below. All output files must conform to it.

### stability_table.json
- path: `/app/outputs/stability_table.json`
- format: json
- purpose: scored
- schema: object with required keys `"n=3"`, `"n=4"`, `"n=5"`, `"n=6"`, `"n=7"`. Each value object must have `"delta_E"` (float, meV/atom) and `"stable_config"` (string, `"FM"` or `"AFM"`).

### delta_N_curves_n5.json
- path: `/app/outputs/delta_N_curves_n5.json`
- format: json
- purpose: scored
- schema: object with required keys `"Fe_sp"`, `"Fe_d"`, `"Cr_sp"`, `"Cr_d"`. Each is an array of `[energy_eV, delta_N]` pairs; energies in eV relative to the Fermi level.

**Note:** You must perform the DFT calculations as described; the verifier checks the consistency of the outputs with the expected physical trends for this system, but does not require numerical agreement with any particular published value. The better the reproduction follows the procedures described above, the more likely the outputs will satisfy the scoring criteria.

## Self‑check (not scored)
A JSON copy of the output contract is provided below. Before finishing, write and run a script that verifies every output file against it: each declared file exists, JSON keys and types are correct. This does not guarantee scientific correctness.

```json
{
  "outputs": [
    {
      "file": "stability_table.json",
      "format": "json",
      "purpose": "scored",
      "schema": {
        "type": "object",
        "required": {
          "n=3": {"delta_E": "float (meV/atom)", "stable_config": "string ('FM' or 'AFM')"},
          "n=4": {"delta_E": "float (meV/atom)", "stable_config": "string ('FM' or 'AFM')"},
          "n=5": {"delta_E": "float (meV/atom)", "stable_config": "string ('FM' or 'AFM')"},
          "n=6": {"delta_E": "float (meV/atom)", "stable_config": "string ('FM' or 'AFM')"},
          "n=7": {"delta_E": "float (meV/atom)", "stable_config": "string ('FM' or 'AFM')"}
        }
      }
    },
    {
      "file": "delta_N_curves_n5.json",
      "format": "json",
      "purpose": "scored",
      "schema": {
        "type": "object",
        "required": {
          "Fe_sp": "array of [energy_eV, delta_N]",
          "Fe_d": "array of [energy_eV, delta_N]",
          "Cr_sp": "array of [energy_eV, delta_N]",
          "Cr_d": "array of [energy_eV, delta_N]"
        }
      }
    }
  ]
}
```