## Problem background

Antiferromagnetic transition-metal monoxides NiO, MnO, FeO, and CoO are Mott insulators whose electronic structure challenges conventional one-electron methods. Standard local spin-density-functional (LSDF) calculations predict metallic ground states for FeO and CoO, severely underestimate band gaps for MnO and NiO, and yield magnetic moments smaller than experimentally observed values. These failures arise because LSDF uses a single averaged potential for all electrons; in reality, electrons occupying unoccupied (conduction) bands experience a different effective potential—one that includes an additional screening electron—than those in occupied valence bands.

The unoccupied-states potential correction (USPC) addresses this by constructing orbital-dependent potentials that approximate the correlation-induced difference between ground-state and excited configurations. For orbitals that dominate unoccupied bands, the USPC uses a potential derived from an excited atomic configuration with one extra d electron, while leaving the ordinary LSDF potential for all other orbitals. This correction opens band gaps, brings magnetic moments into agreement with experiment, and restores insulating behaviour.

## Approach

The USPC method is implemented within the linearised muffin-tin orbital method in the atomic-sphere approximation (LMTO-ASA). The workflow consists of three stages:

1. **Reference LSDF calculation** – A standard self-consistent spin-polarised LMTO-ASA calculation is performed for each oxide to obtain the ground-state electronic structure and determine which d-orbital basis orbitals dominate the unoccupied bands. This step yields the d-orbital populations and the fractional d-contribution y of the unoccupied bands.

2. **USPC potential construction** – For each oxide, orbitals identified as dominating the unoccupied bands are treated with a modified atomic potential. The excited atomic configuration is taken as d^{x+y}(s,p)^{n−x−y}, where x is the ground-state d occupancy, y is the d contribution from the unoccupied band, and n is the total valence electrons. Atomic calculations are performed for these configurations to generate orbital-dependent potential functions P_{ilm}(E). The ordinary LSDF potential is retained for all other basis orbitals.

3. **LMTO-ASA calculation with USPC** – A second self-consistent spin-polarised LMTO-ASA run is carried out using the orbital-dependent potentials from stage 2, while the structure matrix S(k) remains unchanged. From the resulting electronic structure, the band gap is computed as the energy difference between the top of the valence band and the bottom of the conduction band, and the local magnetic moment is obtained as the total spin magnetic moment inside the metal atomic sphere.

## Reproduction target

For the four antiferromagnetic oxides NiO, MnO, FeO, and CoO in the NaCl-type crystal structure with antiferromagnetic AF2 (type-II) ordering, perform the USPC procedure described above. Compute the band gap (in eV) and the local magnetic moment (in Bohr magnetons per metal atom) for each compound. Report these quantities in a single CSV file.

## Assets

- **LMTO-ASA electronic structure code** – An implementation capable of spin-polarised calculations and per-orbital potential modifications is required. An open-source example is the Questaal suite (https://bitbucket.org/berkeleylab/questaalmfa). The agent may use this or any other LMTO-ASA implementation that supports the required features.
- **Crystal structures** – The lattice constants and atomic positions for NiO, MnO, FeO, and CoO in the antiferromagnetic (AF2) structure are standard and must be obtained from published crystallographic tables or databases (e.g., Wyckoff positions, ICSD). The agent should ensure that the correct magnetic cell is used for each compound.

## Workflow steps

### Step 1: Standard LSDF LMTO-ASA reference calculation
- Role: process
- Action: Perform a self-consistent spin-polarised LMTO-ASA calculation for each oxide (NiO, MnO, FeO, CoO) without the USPC. From the results, determine the d-orbital basis orbitals that give the major contribution to the unoccupied bands and record the ground-state d-orbital populations and the fractional d-contribution y of the unoccupied band.
- Evidence: `/app/outputs/lsdf_reference.json`

### Step 2: Construction of USPC potentials
- Role: process
- Action: Using the information from Step 1, construct USPC potentials for the unoccupied orbitals. For each orbital dominating an unoccupied band, compute the self-consistent atomic potential for the excited configuration d^{x+y}(s,p)^{n−x−y} and generate the corresponding potential functions P_{ilm}(E).
- Evidence: `/app/outputs/uspc_potentials.log`

### Step 3: Self-consistent LMTO-ASA with USPC and result extraction
- Role: scored (load-bearing)
- Action: Run a self-consistent spin-polarised LMTO-ASA calculation for each oxide using the USPC potentials from Step 2. For each oxide, compute the band gap as the energy difference between the top of the valence band and the bottom of the conduction band, and the local magnetic moment as the total spin magnetic moment inside the metal atomic sphere. Write the extracted values to the output file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: `material` (string), `band_gap_eV` (float), `magnetic_moment_mu_B` (float). One row per oxide: NiO, MnO, FeO, CoO.
- Scoring: scored by hidden verifier

## Output files

- `/app/outputs/results.csv` – Band gaps and magnetic moments (scored).
- `/app/outputs/lsdf_reference.json` – Optional evidence from the reference LSDF step.
- `/app/outputs/uspc_potentials.log` – Optional evidence from the USPC construction step.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: USPC-corrected band gaps (eV) and local magnetic moments (μB per metal atom) for the four antiferromagnetic oxides NiO, MnO, FeO, CoO.
- schema:
  - `type`: table
  - `required_columns`: `material`, `band_gap_eV`, `magnetic_moment_mu_B`
  - `units`:
    - `band_gap_eV`: eV
    - `magnetic_moment_mu_B`: μB

Notes: The hidden verifier will compare the reported band gaps and magnetic moments against reference values from published experimental/theoretical work using per-compound tolerances that account for implementation-dependent spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "band_gap_eV",
          "magnetic_moment_mu_B"
        ],
        "units": {
          "band_gap_eV": "eV",
          "magnetic_moment_mu_B": "μB"
        }
      },
      "description": "USPC-corrected band gaps (eV) and local magnetic moments (μB per metal atom) for the four antiferromagnetic oxides NiO, MnO, FeO, CoO."
    }
  ],
  "notes": "The hidden verifier will compare the reported band gaps and magnetic moments against reference values from published experimental/theoretical work using per-compound tolerances that account for implementation-dependent spread."
}
```
