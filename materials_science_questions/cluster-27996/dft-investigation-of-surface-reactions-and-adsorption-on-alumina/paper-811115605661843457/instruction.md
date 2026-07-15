# Periodic Plane-Wave DFT Calculation of Offretite Zeolite Acidity from Substitution Energetics

## Problem background
Zeolites are critically important solid acid catalysts whose activity depends strongly on the local framework topology and the energetics of aluminum substitution and protonation. Understanding how the acid strength varies with the local geometry—bond lengths, bond angles, and the energetics of different oxygen sites—provides fundamental insight into their catalytic behaviour. This task uses first-principles density functional theory (DFT) to compute the structural parameters and energetic quantities of the zeolite offretite, relating acid strength to bond-angle patterns without relying on empirical data.

## Approach
The approach is periodic plane-wave DFT within the local density approximation (LDA). The electron–ion interaction is described with norm-conserving pseudopotentials for silicon and aluminum and an ultrasoft pseudopotential for oxygen, using a plane-wave cutoff of 16 Ry and Γ‑point Brillouin-zone sampling. Starting from the published crystallographic structure of all-silica offretite (hexagonal unit cell, a=b=13.291 Å, c=7.582 Å, 54 atoms), we fully relax the geometry to obtain an energy minimum and the corresponding SiO bond lengths and T‑O‑T angles. Then we substitute one silicon atom by aluminum at each of the two distinct tetrahedral sites (T1 and T2), compensating the resulting charge with a uniform positive background, and again relax to obtain Al‑O distances, Al‑O‑Si angles, and total energies. For each inequivalent oxygen adjacent to the Al, a proton is attached and a full relaxation yields bond lengths (Al‑O, Si‑O, O‑H), Al‑O‑Si and Al‑O‑H angles, and the total energy of the protonated configuration. From these total energies, together with calculated atomic reference energies of Si, Al, and H, we derive the proton affinity (energy gained when a proton binds to an Al-substituted site) and the (Al,H)/Si substitution energy (the energy cost to replace a framework silicon by an aluminum plus a charge-compensating proton). These computed quantities allow us to examine the relative stability of alumination at the two T sites and to assess how structural features correlate with acidity.

## Reproduction target
Carry out the complete DFT workflow described above and produce the following numerically defined results:

- The fully relaxed geometry of the all-silica offretite cell: all SiO bond lengths, all O‑T‑O bond angles, and the total energy.
- The relaxed geometries of the Al-substituted cells at T1 and T2: the four Al‑O bond lengths, the Al‑O‑Si angles for each oxygen, and the total energies.
- For every protonated configuration (four for T1, three for T2): the optimized bond lengths Al‑O, Si‑O, O‑H, the Al‑O‑Si and Al‑O‑H angles, and the total energy.
- From the total energies and the independently computed atomic energies of Si, Al, and H, compute the proton affinity (in kcal mol⁻¹) and the (Al,H)/Si substitution energy (in kcal mol⁻¹) for each protonated site, and tabulate them alongside the corresponding total energies (in au).
- Using the substitution energies, determine the relative (Al,H)/Si substitution energies of Al(T1) and Al(T2) with respect to the most stable protonated configuration at T1.

All final numbers must be written to the files listed in the workflow steps, formatted exactly as specified in the output contract.

## Assets

- Plane-wave DFT code (Quantum ESPRESSO, CP2K, or equivalent): https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Si and Al (Bachelet–Hamann–Schlüter in Kleinman–Bylander form) and Vanderbilt ultrasoft pseudopotential for O: http://pseudodojo.org/
- Offretite all-silica crystal structure (fractional coordinates and lattice parameters): 10.1107/S0567740872003014

## Workflow steps

### Step 1: Set up all-silica offretite unit cell
- Role: process
- Action: Obtain the crystallographic data of all-silica offretite from the public reference (Gard & Tait, Acta Cryst. B28, 825, 1972) and construct a periodic unit cell input for the DFT code using the hexagonal lattice parameters a=b=13.291 Å, c=7.582 Å, α=β=90°, γ=120°, space group P6₃/mmc, and the published fractional coordinates of 18 Si and 36 O atoms.
- Evidence: `/app/outputs/initial_structure_input.txt`

### Step 2: Relax all-silica offretite
- Role: scored
- Action: Perform a full geometry optimization of the all-silica offretite unit cell using LDA (Perdew–Zunger), a plane-wave cutoff of 16 Ry, Γ-point Brillouin-zone sampling, norm-conserving pseudopotentials for Si, and the Vanderbilt ultrasoft pseudopotential for O. Relax all atomic positions until residual forces are below 0.0014 au. Extract SiO bond lengths, T-O-T bond angles, and the total energy.
- Output file: `/app/outputs/offretite_geometry.txt`
- Format: txt
- Contract: type=text; pattern=One line per parameter: key=value. Keys include T1O1, T1O2, T1O3, T1O4, T2O4, T2O5, T2O6, T2O7 (bond lengths in Å), O1T1O2, O2T1O3, O3T1O4, O4T1O1, T1O3T1, T2O6T2, O4T2O5, O4T2O7, O5T2O6, O6T2O7 (angles in deg), and final line: E_tot_offretite=<value> (total energy in au).
- Scoring: scored by hidden verifier

### Step 3: Relax Al-substituted offretite (T1 and T2)
- Role: scored
- Action: Starting from the relaxed all-silica structure, substitute one Si by Al at the T1 site and separately at the T2 site, compensating the net charge with a uniform positive background charge. Perform full geometry optimization of each Al-substituted cell until residual forces are below 0.0006 au. Report Al-O bond lengths, Al-O-Si bond angles, and total energies for both Al(T1) and Al(T2).
- Output file: `/app/outputs/al_substituted_geometries.txt`
- Format: txt
- Contract: type=text; pattern=Two blocks, one for Al(T1) and one for Al(T2). Each block lists: dAlO#=<value> (for #=1-4 for T1, #=4-7 for T2, Å), αAlO#Si=<value> (deg for corresponding oxygen), and a final line: E_tot=<value> (total energy in au).
- Scoring: scored by hidden verifier

### Step 4: Relax protonated configurations
- Role: scored
- Action: For each inequivalent oxygen adjacent to Al(T1) (O1-O4) and Al(T2) (O4-O7), attach a proton and perform a full geometry optimization until residual forces are below 0.0006 au. For each configuration (T1OiH, T2OiH) extract the optimized bond lengths (Al-O, Si-O, O-H), Al-O-Si angle, Al-O-H angle, and the total energy.
- Output file: `/app/outputs/protonated_geometries.txt`
- Format: txt
- Contract: type=text; pattern=Blocks for each site: T1O1H, T1O2H, T1O3H, T1O4H, T2O5H, T2O6H, T2O7H. Each block contains lines: dAlO#=<value> (for relevant #, Å), dSiO=<value> (Å), dOH=<value> (Å), αAlOSi=<value> (deg), αAlOH=<value> (deg), and a final line: E_tot=<value> (total energy in au).
- Scoring: scored by hidden verifier

### Step 5: Compute atomic reference energies
- Role: process
- Action: Compute the total energies of isolated Si, Al, and H atoms using the same pseudopotentials, functional, and cutoff (16 Ry) by placing each atom in a large supercell. Save the resulting atomic energies.
- Evidence: `/app/outputs/atomic_energies.txt`

### Step 6: Compute proton affinities and substitution energies
- Role: scored (load-bearing)
- Action: Using the total energies of offretite (s1), Al(T1)/Al(T2) (s2), protonated configurations (s3), and atomic energies (s4), compute proton affinities and (Al,H)/Si substitution energies for each protonated oxygen site according to the energy difference schemes: proton affinity = E_tot[Al(Ti)] + E_at(H) – E_tot[TiOjH]; substitution energy = E_tot[TiOjH] + E_at(Si) – E_tot[offretite] – E_at(Al) – E_at(H). Output a table of results.
- Output file: `/app/outputs/protonated_energies.txt`
- Format: txt
- Contract: type=table; columns=['site', 'total_energy', 'proton_affinity', 'substitution_energy']; units=total_energy in au, proton_affinity and substitution_energy in kcal/mol; description=One line per protonated site (e.g., T1O1H, T1O2H, ..., T2O7H) with space-separated columns.
- Scoring: scored by hidden verifier

### Step 7: Compute relative Al substitution energies
- Role: scored
- Action: From the total energies of Al(T1) and Al(T2) and the substitution energies computed in s5, determine the most stable protonated configuration at T1 (i.e., the site with the lowest substitution energy) and use its substitution energy as the reference. Report the total energies of Al(T1) and Al(T2) and the relative (Al,H)/Si substitution energies (difference in kcal/mol with respect to the chosen reference).
- Output file: `/app/outputs/al_substitution_energies.txt`
- Format: txt
- Contract: type=table; columns=['site', 'total_energy', 'relative_substitution_energy']; units=total_energy in au, relative_substitution_energy in kcal/mol; description=Two lines: Al(T1) <total_energy> 0.0; Al(T2) <total_energy> <relative_substitution_energy>.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/offretite_geometry.txt`
- `/app/outputs/al_substituted_geometries.txt`
- `/app/outputs/protonated_geometries.txt`
- `/app/outputs/protonated_energies.txt`
- `/app/outputs/al_substitution_energies.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### offretite_geometry.txt
- path: `/app/outputs/offretite_geometry.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Relaxed geometry and total energy of all-silica offretite.
- schema:
  - `type`: text
  - `properties`: Key=value lines: bond lengths (Å) for T1O1, T1O2, T1O3, T1O4, T2O4, T2O5, T2O6, T2O7; bond angles (deg) for O1T1O2, O2T1O3, O3T1O4, O4T1O1, T1O3T1, T2O6T2, O4T2O5, O4T2O7, O5T2O6, O6T2O7; final line: E_tot_offretite=<value> (au).

### al_substituted_geometries.txt
- path: `/app/outputs/al_substituted_geometries.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Relaxed geometries and total energies of Al-substituted offretite at T1 and T2 sites.
- schema:
  - `type`: text
  - `properties`: Two blocks (Al(T1) and Al(T2)). Each block lists dAlO#<value> (Å) for appropriate oxygens, αAlO#Si<value> (deg), and total energy E_tot=<value> (au).

### protonated_geometries.txt
- path: `/app/outputs/protonated_geometries.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Structural parameters of all protonated offretite configurations.
- schema:
  - `type`: text
  - `properties`: Blocks for T1O1H, T1O2H, T1O3H, T1O4H, T2O5H, T2O6H, T2O7H. Each block: dAlO# (Å), dSiO (Å), dOH (Å), αAlOSi (deg), αAlOH (deg), and total energy E_tot=<value> (au).

### protonated_energies.txt
- path: `/app/outputs/protonated_energies.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Proton affinities and (Al,H)/Si substitution energies for each protonated oxygen site.
- schema:
  - `type`: table
  - `columns`: `site`, `total_energy (au)`, `proton_affinity (kcal/mol)`, `substitution_energy (kcal/mol)`
  - `description`: One line per protonated site (T1O1H, T1O2H, T1O3H, T1O4H, T2O5H, T2O6H, T2O7H).

### al_substitution_energies.txt
- path: `/app/outputs/al_substitution_energies.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Total energies of Al(T1) and Al(T2) and their relative (Al,H)/Si substitution energies.
- schema:
  - `type`: table
  - `columns`: `site`, `total_energy (au)`, `relative_substitution_energy (kcal/mol)`
  - `description`: Two lines: Al(T1) and Al(T2), with total energy and substitution energy relative to the most stable T1 protonated site.

Notes: All outputs are plain text with key=value or table formatting. The checker will compare reported numbers against hidden paper values with tolerances (±0.02 Å for bond lengths, ±2° for angles, ±0.01 au for total energies, ±2 kcal/mol for derived energies) and also check the ordering/sign of trends where applicable.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "offretite_geometry.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "properties": "Key=value lines: bond lengths (Å) for T1O1, T1O2, T1O3, T1O4, T2O4, T2O5, T2O6, T2O7; bond angles (deg) for O1T1O2, O2T1O3, O3T1O4, O4T1O1, T1O3T1, T2O6T2, O4T2O5, O4T2O7, O5T2O6, O6T2O7; final line: E_tot_offretite=<value> (au)."
      },
      "description": "Relaxed geometry and total energy of all-silica offretite."
    },
    {
      "file": "al_substituted_geometries.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "properties": "Two blocks (Al(T1) and Al(T2)). Each block lists dAlO#<value> (Å) for appropriate oxygens, αAlO#Si<value> (deg), and total energy E_tot=<value> (au)."
      },
      "description": "Relaxed geometries and total energies of Al-substituted offretite at T1 and T2 sites."
    },
    {
      "file": "protonated_geometries.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "properties": "Blocks for T1O1H, T1O2H, T1O3H, T1O4H, T2O5H, T2O6H, T2O7H. Each block: dAlO# (Å), dSiO (Å), dOH (Å), αAlOSi (deg), αAlOH (deg), and total energy E_tot=<value> (au)."
      },
      "description": "Structural parameters of all protonated offretite configurations."
    },
    {
      "file": "protonated_energies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          "site",
          "total_energy (au)",
          "proton_affinity (kcal/mol)",
          "substitution_energy (kcal/mol)"
        ],
        "description": "One line per protonated site (T1O1H, T1O2H, T1O3H, T1O4H, T2O5H, T2O6H, T2O7H)."
      },
      "description": "Proton affinities and (Al,H)/Si substitution energies for each protonated oxygen site."
    },
    {
      "file": "al_substitution_energies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          "site",
          "total_energy (au)",
          "relative_substitution_energy (kcal/mol)"
        ],
        "description": "Two lines: Al(T1) and Al(T2), with total energy and substitution energy relative to the most stable T1 protonated site."
      },
      "description": "Total energies of Al(T1) and Al(T2) and their relative (Al,H)/Si substitution energies."
    }
  ],
  "notes": "All outputs are plain text with key=value or table formatting. The checker will compare reported numbers against hidden paper values with tolerances (±0.02 Å for bond lengths, ±2° for angles, ±0.01 au for total energies, ±2 kcal/mol for derived energies) and also check the ordering/sign of trends where applicable."
}
```

## How you are scored
A hidden verifier will independently inspect each scored output file listed below. For each file, the verifier compares your reported numerical values (bond lengths, angles, total energies, and derived energies) against reference values that were obtained from the original paper, using appropriate tolerances to account for legitimate numerical differences between DFT implementations. Each output file contributes a fraction to the total reward; the final reward is the weighted sum. The verifier also checks that the output files follow the prescribed format and contain all required entries. Simply writing numbers that match the reference is not sufficient—the verifier expects values that are physically consistent with a genuine DFT execution.
