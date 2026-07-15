# Classical MD of FeOOH Surfaces: Hydroxyl Site Distributions and Hydrogen-Bond Statistics

## Problem background
Identifying the types, densities, and hydrogen‑bonding patterns of surface hydroxyl groups on lepidocrocite (γ‑FeOOH) and goethite (α‑FeOOH) crystallographic planes is essential for understanding these minerals' reactivity in natural and industrial settings. Classical molecular dynamics (MD) simulations can predict which OH motifs (–OH, μ‑OH, μ₃‑OH) are present on each plane and how they form hydrogen‑bond networks, providing a structural basis for interpreting experimental spectra such as FTIR. This task targets the computational prediction of hydroxyl site distributions and hydrogen‑bond statistics for specific crystallographic planes of these two iron oxyhydroxide polymorphs.

## Approach
Build charge‑neutral slab models of lepidocrocite (010) and (001) and goethite (110) and (021) using the crystallographic unit‑cell parameters and the atomic compositions reported for each plane. Simulate each slab by classical MD in the NPT ensemble at 300 K, employing the CLAYFF force field for oxygen and hydroxyls, the revised CLAYFF parameters for Fe³⁺, and flexible SPC water where water molecules are present. Analyze the production trajectories for hydrogen bonds using an O···H distance cut‑off. From these analyses, compute the surface site density of μ‑OH groups on lepidocrocite (010), the median donor–hydrogen–acceptor angle and fraction of –OH donors involved in hydrogen bonds on lepidocrocite (001), the donor–acceptor angles and donor fractions for –OH···–OH and μ₃,ᵣ‑OH···HO– interactions on goethite (110), and characterize the hydrogen‑bond connectivity on the goethite (021) plane. The results are organized into structured output files as described in the workflow steps.

## Reproduction target
Produce a structured CSV file (`hydrogen_bond_statistics.csv`) with numerical hydrogen‑bond statistics for the lepidocrocite (010) and (001) planes and the goethite (110) plane, including surface site densities, median donor–acceptor angles, and donor fractions for specific hydroxyl species and interactions. Additionally, produce a text file (`goethite_021_hbond_summary.txt`) containing a qualitative description of the hydrogen‑bond network on the goethite (021) plane, emphasizing its extensive connectivity. The exact properties to compute and the format of each output are specified in the workflow steps and output contract.

## Assets

- Gromacs (v4.5.3 or later): https://www.gromacs.org/
- CLAYFF force field parameters (O, OH, Fe³⁺ revisions): 10.1021/jp0363287 (original CLAYFF); 10.1016/j.gca.2011.02.022 (revised Fe³⁺)
- Crystallographic data for lepidocrocite and goethite: Wyckoff, Crystal Structures 1 (1963); Yang et al., Acta Cryst. E62, i250 (2006)
- Slab composition specifications (from the paper)

## Workflow steps

### Step 1: Construct charge-neutral slab models
- Role: process
- Action: Build charge-neutral slab supercells for the four crystallographic planes (lepidocrocite (010), (001); goethite (110), (021)) using the reported atomic compositions and the unit-cell parameters of lepidocrocite and goethite. Terminate dangling bonds with surface oxygens or protons to achieve neutrality. The slab thickness should be about 3 nm and a vacuum gap of at least 8 nm between periodic images must be introduced.
- Evidence: `/app/outputs/slab_topology.gro`

### Step 2: Run classical MD equilibration and production
- Role: process
- Action: For each slab, perform an energy minimization, then a 5 ns NPT equilibration at 300 K with a 0.5 fs timestep, using the CLAYFF force field (including the revised Fe³⁺ parameters and flexible SPC water where applicable) and particle-mesh Ewald for electrostatics. Continue with a 5 ns NPT production run. Use Gromacs (v4.5.3 or compatible version).
- Evidence: `/app/outputs/production_md.log`

### Step 3: Hydrogen-bond statistics for (010), (001) and (110) planes
- Role: scored (load-bearing)
- Action: From the production trajectories, extract hydrogen-bond data using an O···H distance cut-off of 0.3 nm. Compute: (a) surface site density of isolated μ-OH groups on lepidocrocite (010); (b) median donor-hydrogen-acceptor angle and fraction of -OH donors involved in hydrogen bonds on lepidocrocite (001); (c) donor-acceptor angle and donor fraction for -OH···-OH interactions, and the corresponding values for μ₃,ᵣ-OH···HO– interactions on goethite (110). Write these values to a structured CSV file.
- Output file: `/app/outputs/hydrogen_bond_statistics.csv`
- Format: csv
- Contract: CSV with columns: plane, species_or_interaction, property, value, unit. Expected properties include site_density (sites_per_nm2), median_donor_acceptor_angle (deg), donor_fraction (fraction).
- Scoring: scored by hidden verifier

### Step 4: Hydrogen-bond summary for goethite (021) plane
- Role: scored
- Action: Analyze the hydrogen-bond network on the goethite (021) plane from the MD trajectory. Observe the connectivity among -OH, μ-OH and -OH₂ groups, and record that the network is so extensive and complex that no discrete O-H stretching bands can be assigned to individual groups. Write this qualitative conclusion to a text file.
- Output file: `/app/outputs/goethite_021_hbond_summary.txt`
- Format: txt
- Contract: Plain text stating that the hydrogen-bond network on goethite (021) is extensive and prevents discrete O-H stretching band assignment.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hydrogen_bond_statistics.csv`
- `/app/outputs/goethite_021_hbond_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hydrogen_bond_statistics.csv
- path: `/app/outputs/hydrogen_bond_statistics.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Numerical hydrogen-bond statistics for lepidocrocite (010), (001) and goethite (110) planes.
- schema:
  - `type`: table
  - `required_columns`: `plane`, `species_or_interaction`, `property`, `value`, `unit`
  - `description`: Each row contains one hydrogen-bond statistic. See step description for the required properties.

### goethite_021_hbond_summary.txt
- path: `/app/outputs/goethite_021_hbond_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Qualitative summary of hydrogen bonding on the goethite (021) plane.
- schema:
  - `type`: text
  - `description`: A qualitative statement that the hydrogen-bond network on goethite (021) is extensive and prevents discrete band assignment.

Notes: The quantitative CSV is checked against hidden paper gold with tolerances; the text file is checked for existence and presence of the expected statement.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hydrogen_bond_statistics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "plane",
          "species_or_interaction",
          "property",
          "value",
          "unit"
        ],
        "description": "Each row contains one hydrogen-bond statistic. See step description for the required properties."
      },
      "description": "Numerical hydrogen-bond statistics for lepidocrocite (010), (001) and goethite (110) planes."
    },
    {
      "file": "goethite_021_hbond_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "A qualitative statement that the hydrogen-bond network on goethite (021) is extensive and prevents discrete band assignment."
      },
      "description": "Qualitative summary of hydrogen bonding on the goethite (021) plane."
    }
  ],
  "notes": "The quantitative CSV is checked against hidden paper gold with tolerances; the text file is checked for existence and presence of the expected statement."
}
```

## How you are scored
A hidden verifier independently inspects each workflow artifact. The numerical statistics in `hydrogen_bond_statistics.csv` are compared against hidden reference values (within appropriate tolerances) to assess correctness. The qualitative summary in `goethite_021_hbond_summary.txt` is audited for existence and for containing the expected statement about the extensive hydrogen‑bond network. The final reward is a weighted sum of these scores. Success requires that your simulation produces values consistent with the reference; reporting numbers from the literature without performing the simulation workflow will not pass.
