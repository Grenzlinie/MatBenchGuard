# DFT-LDA calculations of Al adatom adsorption and self-diffusion on Al(111)

## Problem background
Understanding how single adatoms diffuse on metal surfaces is crucial for predicting epitaxial growth modes. On the close-packed Al(111) surface, the self-diffusion of an isolated aluminium atom is determined by the adsorption energies at high-symmetry sites and the resulting energy barrier for hops between threefold-coordinated positions. The goal is to compute these adsorption energies and the corresponding diffusion barrier using density-functional theory within the local-density approximation, which provides accurate energies and allows mechanistic interpretation of surface diffusion.

## Approach
Use an open-source plane-wave DFT code with the LDA exchange-correlation functional and a norm-conserving fully separable pseudopotential for Al (s and p channels described by projection operators, d channel treated as local). Use a plane-wave kinetic energy cutoff of 8 Ry. The fcc Al lattice constant is taken as 3.98 Å, the value obtained by DFT-LDA in the paper; build the slab with this lattice parameter. For the slab calculations, sample the surface Brillouin zone with one special k-point located in its irreducible quarter (as in the paper). Model the Al(111) surface as a periodic slab with five atomic layers, at least 8 Å of vacuum, and a surface supercell of at least 3×3 to make the adatom effectively isolated. Perform self-consistent total-energy calculations, allowing atomic relaxation, for the clean slab and for the slab with one Al adatom placed at the four distinct high-symmetry sites (hcp, fcc, bridge, top). Also compute the total energy of an isolated Al atom in a large cell with the same cutoff. Record key total energies and relaxed geometries in a log file for reproducibility audit. From the converged total energies, derive the adsorption energy for each site as E_site = E_total(slab+adatom) − E_total(clean slab) − E_isolated_atom. Extract the adatom height above the top substrate layer for each adsorption configuration. The self-diffusion barrier on flat Al(111) is obtained as the energy difference between the minimum-energy adsorption site (identified from the computed site energies) and the saddle-point energy along the minimum-energy path between adjacent threefold sites; the saddle energy is taken as the higher of the bridge and fcc site energies along that path.

## Reproduction target
Produce a comma-separated file (`step_01_adsorption_energies.csv`) containing the computed adsorption energies (in eV) and the adatom heights (in Å) for the hcp, fcc, bridge, and top sites on the flat Al(111) surface. Each row corresponds to one site. Also produce a second file (`step_02_diffusion_barrier.txt`) containing a single floating-point number: the self-diffusion barrier (in eV) for an isolated Al adatom hopping between adjacent threefold sites on the flat Al(111) surface, as defined by the energy difference between the minimum-energy adsorption site and the saddle point (the higher of the bridge or fcc site energies) along the minimum-energy path between adjacent threefold sites.

## Assets

- Quantum ESPRESSO (or equivalent plane-wave DFT code): https://www.quantum-espresso.org/
- Al pseudopotential (LDA)
- LDA exchange-correlation functional
- Al fcc crystal structure (lattice constant 3.98 Å from the paper)

## Workflow steps

### Step 1: DFT-LDA total-energy calculations for Al(111) slab with adatom
- Role: process
- Action: Set up a five-layer Al(111) slab using the fcc lattice constant of 3.98 Å, with at least 8 Å vacuum and a surface supercell large enough to isolate the adatom (e.g., 3×3 or 4×4). Use one special k-point in the irreducible quarter of the surface Brillouin zone for Brillouin-zone sampling. Using an open-source plane-wave DFT code with LDA and an Al pseudopotential, perform self-consistent total-energy calculations, allowing relaxation, for the clean slab and for the slab with a single Al adatom placed at the hcp, fcc, bridge, and top sites. Also compute the total energy of an isolated Al atom in a large cell with the same cutoff. Record key total energies and relaxed geometries in a log file for reproducibility audit.

### Step 2: Compute site-resolved adsorption energies
- Role: scored
- Action: From the total energies obtained in Step 1, compute the adsorption energy for each site as E_site = E_total(slab+adatom) - E_total(clean slab) - E_isolated_atom. Also extract the adatom height above the top substrate layer for each site. Report the results for hcp, fcc, bridge, and top sites.
- Output file: `/app/outputs/step_01_adsorption_energies.csv`
- Format: csv
- Contract: Columns: site (string), adsorption_energy_eV (float), height_A (float).
- Scoring: scored by hidden verifier

### Step 3: Compute self-diffusion barrier
- Role: scored
- Action: Using the adsorption energies from Step 2, determine the self-diffusion barrier for an isolated Al adatom on flat Al(111). The barrier is the energy difference between the minimum-energy adsorption site (identified from the computed site energies) and the saddle point along the minimum-energy path between adjacent threefold sites. Take the saddle energy as the higher of the bridge and fcc energies along that path. Report the barrier value in eV.
- Output file: `/app/outputs/step_02_diffusion_barrier.txt`
- Format: txt
- Contract: One line: floating-point number (barrier in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_adsorption_energies.csv`
- `/app/outputs/step_02_diffusion_barrier.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_adsorption_energies.csv
- path: `/app/outputs/step_01_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Adsorption energies and adatom heights for Al adatom on Al(111) at four high-symmetry sites.
- schema:
  - `type`: table
  - `required_columns`: `site`, `adsorption_energy_eV`, `height_A`
  - `units`:
    - `adsorption_energy_eV`: eV
    - `height_A`: Å

### step_02_diffusion_barrier.txt
- path: `/app/outputs/step_02_diffusion_barrier.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Self-diffusion barrier for an isolated Al adatom on flat Al(111), computed as the energy difference between the minimum-energy adsorption site (determined from your computed site energies) and the saddle point (higher of bridge or fcc along the minimum-energy path).
- schema:
  - `type`: text
  - `format`: float

Notes: The checker will compare reported values to hidden reference values with appropriate tolerances that account for differences in DFT implementation and pseudopotential.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "adsorption_energy_eV",
          "height_A"
        ],
        "units": {
          "adsorption_energy_eV": "eV",
          "height_A": "Å"
        }
      },
      "description": "Adsorption energies and adatom heights for Al adatom on Al(111) at four high-symmetry sites."
    },
    {
      "file": "step_02_diffusion_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "float"
      },
      "description": "Self-diffusion barrier for an isolated Al adatom on flat Al(111), computed as the energy difference between the minimum-energy adsorption site (determined from your computed site energies) and the saddle point (higher of bridge or fcc along the minimum-energy path)."
    }
  ],
  "notes": "The checker will compare reported values to hidden reference values with appropriate tolerances that account for differences in DFT implementation and pseudopotential."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact. For `step_01_adsorption_energies.csv`, the verifier checks the reported adsorption energies and heights for each site against expected reference values, allowing tolerances that account for differences in DFT implementation, pseudopotential, and numerical choices. The site ordering among the energies (which site is most stable, which site is least stable) is also evaluated. For `step_02_diffusion_barrier.txt`, the verifier reads the single barrier value and compares it to an expected value with an appropriate tolerance. The final reward is a weighted combination of the scores for the adsorption energies, heights, and diffusion barrier, as detailed in the hidden grading specification. Reporting a number alone is not sufficient; the artifacts must be the result of carrying out the DFT workflow described above.