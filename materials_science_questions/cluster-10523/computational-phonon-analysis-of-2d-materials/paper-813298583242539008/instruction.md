# DFT Analysis of Hydrogenation and Fe Decoration of Edge-Reconstructed Graphene Nanoribbons

## Problem background
Edge-reconstructed graphene nanoribbons, where zigzag edges form alternating pentagon–heptagon pairs, are predicted to be more stable than their unreconstructed counterparts. Chemical functionalization of these reconstructed edges with hydrogen or transition metal adatoms could drastically alter their stability, vibrational properties, and magnetic behaviour. This task investigates the following open questions using first-principles calculations:

- For reconstructed zigzag nanoribbons of varying widths, which edge termination — single or dihydrogenated — is more favourable at zero temperature and under ambient conditions?
- How does edge reconstruction affect the lowest optical phonon modes compared to unreconstructed hydrogenated edges?
- When the reconstructed edges are decorated with iron atoms, how does the inter-edge magnetic exchange coupling depend on the ribbon width?

## Approach
The approach uses spin‑polarised density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and a plane‑wave basis, as implemented in the open‑source Quantum ESPRESSO package. The workflow proceeds as follows:

- Build unit cells for reconstructed zigzag nanoribbons (referred to as reczag) with widths of 4, 6, 8, 10, and 12 carbon rows. For each width, construct geometries with bare edges, monohydrogenated (1H) edges, and dihydrogenated (2H) edges. Analogous structures for unreconstructed zigzag nanoribbons (ZGNR) are also built for comparison.
- Fully relax all geometries to force convergence, obtain total energies, and – for the 2H reczag case – perform a frozen‑phonon analysis to find and freeze unstable modes that lead to a twisted stable geometry.
- Compute the formation energy for converting a 1H‑terminated edge into a 2H‑terminated edge per width, using the total energies of the relaxed ribbons and the reference energy of an isolated H₂ molecule.
- For the 12‑row reczag system, calculate the Gibbs free energy per unit edge length as a function of hydrogen gas pressure at 300 K, employing the total energies of bare, 1H‑, and 2H‑terminated ribbons together with the H₂ enthalpy and entropy from standard NIST‑JANAF thermochemical tables.
- Perform frozen‑phonon calculations at the Γ point for the 12‑row reczag and ZGNR structures with 1H and 2H termination, and extract the lowest optical phonon mode frequencies.
- For each reczag width, place one iron atom per heptagon at both edges, relax the structures in two spin configurations (ferromagnetic and antiferromagnetic alignment between the two edges), and record the corresponding total energies.

All DFT calculations use PBE pseudopotentials (e.g., from the SSSP library) and a plane‑wave cutoff adequate for convergence. The numerical parameters (k‑point mesh, cutoff, smearing, force threshold) are left to the agent’s judgement, provided the final trends are robust.

## Reproduction target
The objective is to produce four scored artifacts that together capture the key physical trends:

1. **formation_energies.csv** – For reczag ribbons of widths 4–12 rows, report the total energies of the 1H‑ and 2H‑terminated structures and the zero‑temperature formation energy E_f = E(2H) − [E(1H) + n·E(H₂)]. Determine the sign of E_f for every width.

2. **gibbs_free_energy.csv** – For the 12‑row reczag system at 300 K, output the Gibbs free energies per edge length of the 1H‑ and 2H‑terminated edges over a pressure range from 10⁻¹⁰ bar to 100 bar (including the ambient pressure of 1.01325 bar). Identify the pressure at which the 2H‑terminated edge becomes more stable than the 1H‑terminated edge.

3. **phonon_frequencies.csv** – For the 12‑row reczag and ZGNR systems with both 1H and 2H termination, report the lowest optical phonon mode frequency. The data must reveal whether edge reconstruction hardens the modes relative to the unreconstructed ZGNR.

4. **magnetic_coupling.csv** – For Fe‑decorated reczag ribbons of widths 4–12 rows, list the total energies for ferromagnetic (E_FM) and antiferromagnetic (E_AFM) inter‑edge alignment and compute ΔE = E_AFM − E_FM. The result must show the sign of ΔE at the narrowest and widest ribbons and how it evolves.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials for C, H, Fe (GGA-PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- NIST-JANAF Thermochemical Tables (H2 enthalpy and entropy): https://janaf.nist.gov/

## Workflow steps

### Step 1: Reference energy of H2 molecule
- Role: process
- Action: Perform a spin-polarized DFT calculation of an isolated H2 molecule using Quantum ESPRESSO with PBE functional and pseudopotentials to obtain its total energy E(H2).
- Evidence: `/app/outputs/h2_energy.log`

### Step 2: Geometry optimization of reczag and unreconstructed ZGNR structures
- Role: process
- Action: Construct initial geometries for reczag GNRs (widths 4, 6, 8, 10, 12 rows) with bare, 1H, and 2H edge terminations, and for unreconstructed zigzag GNRs (ZGNR) with 1H and 2H terminations. Perform full geometry optimizations with DFT (Quantum ESPRESSO, PBE, force convergence 0.005 eV/A). For the 2H reczag case, use frozen-phonon analysis to identify unstable modes and relax to the stable twisted geometry. Save final total energies and optimized coordinates.
- Evidence: `/app/outputs/gnr_optimizations.log`

### Step 3: Frozen-phonon calculation of optical phonon modes
- Role: process
- Action: For the optimized 12-row reczag (1H and 2H) and ZGNR (1H and 2H) structures, perform frozen-phonon calculations (Quantum ESPRESSO, refined k-mesh) to obtain phonon frequencies at the Gamma point.
- Evidence: `/app/outputs/phonon_calcs.log`

### Step 4: Fe-decorated reczag GNRs: geometry and total energies
- Role: process
- Action: For each width (4, 6, 8, 10, 12 rows), construct a reczag GNR with one Fe atom per heptagon at both edges. Perform DFT relaxation and static calculations in two spin configurations: ferromagnetic (FM) and antiferromagnetic (AFM) alignment between the two edges. Obtain the total energies E_FM and E_AFM for each width.
- Evidence: `/app/outputs/fe_gnr_calcs.log`

### Step 5: Formation energy of 2H vs 1H termination
- Role: scored
- Action: From the total energies E(G2H), E(G1H) obtained in the optimization step and E(H2) from the reference step, compute the formation energy E_f = E(G2H) - [E(G1H) + n*E(H2)] for each reczag width (n balances hydrogen count). Write the results to formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: width (integer), E_1H (eV, float), E_2H (eV, float), E_f (eV, float). One row per width 4,6,8,10,12.
- Scoring: scored by hidden verifier

### Step 6: Gibbs free energy and thermodynamic stability
- Role: scored (load-bearing)
- Action: For the 12-row reczag system, use the total energies E(G0H), E(G1H), E(G2H), E(H2), the unit cell length L, and H2 thermodynamic data (enthalpy, entropy from NIST-JANAF) to compute the Gibbs free energy per unit edge length G_1H and G_2H as a function of pressure at 300 K. Produce a table covering pressures from 1e-10 to 100 bar, including a row at ambient pressure 1.01325 bar, and save as gibbs_free_energy.csv.
- Output file: `/app/outputs/gibbs_free_energy.csv`
- Format: csv
- Contract: Columns: pressure_bar (float), G_2H (eV/angstrom, float), G_1H (eV/angstrom, float). One row per pressure point.
- Scoring: scored by hidden verifier

### Step 7: Lowest optical phonon mode hardening
- Role: scored
- Action: From the phonon calculation outputs, extract the lowest optical phonon mode frequency (in cm^-1) for the 12-row reczag (1H and 2H) and unreconstructed ZGNR (1H and 2H) systems. Save the results in phonon_frequencies.csv.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: system (string), lowest_optical_mode_cm1 (float). Expected system values: reczag_1H, reczag_2H, ZGNR_1H, ZGNR_2H.
- Scoring: scored by hidden verifier

### Step 8: Inter-edge magnetic exchange coupling
- Role: scored
- Action: Using the total energies E_FM and E_AFM from the Fe-decorated calculations, compute the exchange coupling energy delta_E = E_AFM - E_FM for each width. Write the result to magnetic_coupling.csv.
- Output file: `/app/outputs/magnetic_coupling.csv`
- Format: csv
- Contract: Columns: width (integer), E_FM (eV, float), E_AFM (eV, float), delta_E (eV, float). Positive delta_E -> FM ground state; negative -> AFM.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/gibbs_free_energy.csv`
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/magnetic_coupling.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energies for 2H vs 1H termination on reczag GNRs of widths 4-12 rows.
- schema:
  - `type`: table
  - `required_columns`: `width`, `E_1H`, `E_2H`, `E_f`
  - `units`:
    - `E_1H`: eV
    - `E_2H`: eV
    - `E_f`: eV

### gibbs_free_energy.csv
- path: `/app/outputs/gibbs_free_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Gibbs free energy per edge length for 2H and 1H terminated 12-row reczag GNR at 300 K vs. pressure.
- schema:
  - `type`: table
  - `required_columns`: `pressure_bar`, `G_2H`, `G_1H`
  - `units`:
    - `pressure_bar`: bar
    - `G_2H`: eV/angstrom
    - `G_1H`: eV/angstrom

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Lowest optical phonon mode frequencies for 12-row reczag and ZGNR with 1H and 2H termination.
- schema:
  - `type`: table
  - `required_columns`: `system`, `lowest_optical_mode_cm1`
  - `units`:
    - `lowest_optical_mode_cm1`: cm^-1

### magnetic_coupling.csv
- path: `/app/outputs/magnetic_coupling.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Inter-edge magnetic exchange coupling energies for Fe-decorated reczag GNRs of widths 4-12 rows.
- schema:
  - `type`: table
  - `required_columns`: `width`, `E_FM`, `E_AFM`, `delta_E`
  - `units`:
    - `E_FM`: eV
    - `E_AFM`: eV
    - `delta_E`: eV

Notes: The checker will recompute derived quantities (formation energies, transition pressure, frequency differences, sign changes) from these raw CSV files. All target comparisons are structural/trend-based: E_f < 0, transition pressure <= ambient, hardening condition reczag > ZGNR, and delta_E sign reversal with width.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "width",
          "E_1H",
          "E_2H",
          "E_f"
        ],
        "units": {
          "E_1H": "eV",
          "E_2H": "eV",
          "E_f": "eV"
        }
      },
      "description": "Formation energies for 2H vs 1H termination on reczag GNRs of widths 4-12 rows."
    },
    {
      "file": "gibbs_free_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_bar",
          "G_2H",
          "G_1H"
        ],
        "units": {
          "pressure_bar": "bar",
          "G_2H": "eV/angstrom",
          "G_1H": "eV/angstrom"
        }
      },
      "description": "Gibbs free energy per edge length for 2H and 1H terminated 12-row reczag GNR at 300 K vs. pressure."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "lowest_optical_mode_cm1"
        ],
        "units": {
          "lowest_optical_mode_cm1": "cm^-1"
        }
      },
      "description": "Lowest optical phonon mode frequencies for 12-row reczag and ZGNR with 1H and 2H termination."
    },
    {
      "file": "magnetic_coupling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "width",
          "E_FM",
          "E_AFM",
          "delta_E"
        ],
        "units": {
          "E_FM": "eV",
          "E_AFM": "eV",
          "delta_E": "eV"
        }
      },
      "description": "Inter-edge magnetic exchange coupling energies for Fe-decorated reczag GNRs of widths 4-12 rows."
    }
  ],
  "notes": "The checker will recompute derived quantities (formation energies, transition pressure, frequency differences, sign changes) from these raw CSV files. All target comparisons are structural/trend-based: E_f < 0, transition pressure <= ambient, hardening condition reczag > ZGNR, and delta_E sign reversal with width."
}
```

## How you are scored
A hidden verifier independently inspects each CSV artifact. It recomputes derived quantities (formation energies, Gibbs free energy crossing point, phonon frequency differences) and checks structural consistency:

- **formation_energies.csv:** the verifier confirms that E_f is negative for all widths.
- **gibbs_free_energy.csv:** the verifier locates the pressure where the G_2H and G_1H curves intersect and verifies that this transition pressure is at or below ambient pressure (1.01325 bar).
- **phonon_frequencies.csv:** the verifier checks that for each hydrogenation level the lowest optical mode of reczag is higher than that of ZGNR (hardening).
- **magnetic_coupling.csv:** the verifier verifies that ΔE is positive for width 4 and negative for width 12, with a monotonic sign change.

No exact numeric tolerance against the paper’s published values is required; the scoring relies on the presence and correct direction of the physical trends. The final reward (0–1) is a weighted combination of these four checks, with the main stability analysis (Gibbs free energy) and the magnetic coupling carrying the largest weight.
