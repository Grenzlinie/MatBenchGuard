# First-principles Fermi surface topology computation

## Problem background
Iron-based layered superconductors such as AFe2As2 (A=Ba) and ReOFeAs (Re=La) exhibit high-temperature superconductivity. The low-energy electronic structure — especially the Fe-3d band dispersions and their coupling to arsenic states near the Fermi level — is thought to underpin the superconducting mechanism. First-principles density functional theory (DFT) calculations can directly characterize these electronic features, including the Fe-d bandwidth, the shape and filling of the density of states, and the Fermi surface topology. This reproduction task recomputes these quantities for the two prototype compounds BaFe2As2 and LaOFeAs, providing a quantitative comparison that informs the degree to which the simpler AFe2As2 system can serve as a minimal model for the whole class of FeAs-layered superconductors.

## Approach
The strategy is an all-electron or pseudopotential DFT calculation within the local density approximation (LDA), using an openly available plane-wave or similar basis-set code. First, input structures are built from the published crystal data for BaFe2As2 (body-centred tetragonal I4/mmm) and LaOFeAs (primitive tetragonal P4/nmm). Self-consistent field (SCF) calculations are then performed to converge the Kohn-Sham eigenvalues. From the SCF results, a dense k‑mesh non‑self‑consistent calculation yields the total and Fe-d projected densities of states (DOS). Band structures are obtained by computing eigenvalues along a standard high‑symmetry path of the tetragonal Brillouin zone. Finally, the number of hole-like bands that cross the Fermi level at the Γ point and the number of electron-like bands at the X point are extracted from the band eigenvalues, and the Fe-d bandwidth — defined as the energy interval where the Fe-d DOS exceeds 10% of its maximum — is computed from the DOS tables. The key quantitative comparison is the Fe-d bandwidth difference between the two compounds.

All Kohn-Sham eigenvalues (bands, DOS) are referenced to the Fermi level: the Fermi energy is set to zero, so that negative values indicate occupied states and positive values indicate unoccupied states. The band structures are written with energies already shifted by the Fermi level.

## High‑symmetry k‑point coordinates
For both BaFe2As2 and LaOFeAs the band structure is computed along the tetragonal path Γ‑X‑M‑Γ‑Z. The k‑point coordinates are given in fractional units of the reciprocal lattice vectors (2π/a and 2π/c). Use exactly the following coordinates:

| Point | (kx, ky, kz) |
|-------|----------------|
| Γ     | (0.0, 0.0, 0.0) |
| X     | (0.5, 0.0, 0.0) |
| M     | (0.5, 0.5, 0.0) |
| Γ     | (0.0, 0.0, 0.0) |
| Z     | (0.0, 0.0, 0.5) |

The hidden verifier will extract the Γ‑point and X‑point eigenvalues by matching these coordinates exactly (within floating‑point tolerance). Every k‑point along the path must be written with these coordinates, not with Cartesian or other representations.

## Reproduction target
Perform DFT LDA calculations for BaFe2As2 and LaOFeAs. Produce and save the following files:

- `dos_BaFe2As2.dat` and `dos_LaOFeAs.dat`: text files with three columns — energy (eV), total DOS (states/eV/cell), and Fe‑d partial DOS (states/eV/cell).
- `bands_BaFe2As2.dat` and `bands_LaOFeAs.dat`: text files where each line holds kx, ky, kz (in units of 2π/a), an integer band index, and the band eigenvalue (eV), spanning a high‑symmetry k‑path (e.g., Γ–X–M–Γ–Z).
- `fermi_surface_topology.txt`: a plain text file that states, for each compound, the number of hole-like Fermi sheets at the Γ point and the number of electron-like sheets at the X point (e.g., `holes_at_Gamma: N`, `electrons_at_X: M`).
- `bandwidth_comparison.txt`: a plain text file containing the Fe‑d bandwidth (in eV) for each compound and their signed difference (`Difference: Z.ZZ eV`).

All outputs must be placed under `/app/outputs`.

## Assets

- Quantum ESPRESSO (or similar open-source DFT package): https://www.quantum-espresso.org/
- GBRV pseudopotentials (or equivalent LDA set): https://www.quantum-espresso.org/pseudopotentials/gbrv

## Workflow steps

### Step 1: Crystal structure preparation
- Role: process
- Action: Prepare DFT input files for BaFe2As2 (space group I4/mmm, a=3.9090 Å, c=13.2122 Å, atomic positions: Ba (0,0,0), Fe (0.5,0,0.25), As (0,0,0.3538)) and LaOFeAs (space group P4/nmm, a=4.03533 Å, c=8.74090 Å, atomic positions: La (0.25,0.25,0.14154), Fe (0.75,0.25,0.5), As (0.25,0.25,0.6512), O (0.75,0.25,0)).
- Evidence: none

### Step 2: LDA self-consistent field calculations
- Role: process
- Action: Run density functional theory (DFT) LDA self-consistent field calculations for both BaFe2As2 and LaOFeAs using an open-source DFT code (e.g., Quantum ESPRESSO), to obtain converged charge density and Kohn-Sham eigenvalues. The Fermi level obtained from the SCF calculation is the energy zero for all subsequent steps.
- Evidence: none

### Step 3: Density of states for BaFe2As2
- Role: scored
- Action: Compute total and Fe-d partial density of states for BaFe2As2 from the SCF eigenvalues, using a dense k-point mesh and appropriate smearing. The energy axis must be shifted so that the Fermi level is at 0 eV. Save to dos_BaFe2As2.dat.
- Output file: `/app/outputs/dos_BaFe2As2.dat`
- Format: txt
- Contract: Columns: energy (eV), total_dos (states/eV/cell), fe_d_dos (states/eV/cell)
- Scoring: scored by hidden verifier

### Step 4: Density of states for LaOFeAs
- Role: scored
- Action: Compute total and Fe-d partial density of states for LaOFeAs analogously to step 3. Fermi level at 0 eV. Save to dos_LaOFeAs.dat.
- Output file: `/app/outputs/dos_LaOFeAs.dat`
- Format: txt
- Contract: Columns: energy (eV), total_dos (states/eV/cell), fe_d_dos (states/eV/cell)
- Scoring: scored by hidden verifier

### Step 5: Band structure for BaFe2As2
- Role: scored
- Action: Compute energy eigenvalues along the high‑symmetry k‑path Γ → X → M → Γ → Z (coordinates given in the "High‑symmetry k‑point coordinates" section above; fractional units of 2π/a and 2π/c). Energies must be shifted so that the Fermi level is at 0 eV. Write bands_BaFe2As2.dat with one line per k‑point per band containing kx, ky, kz, band index (integer), and eigenvalue (eV).
- Output file: `/app/outputs/bands_BaFe2As2.dat`
- Format: txt
- Contract: Columns: kx, ky, kz (2π/a), band_index (integer), eigenvalue (eV)
- Scoring: scored by hidden verifier

### Step 6: Band structure for LaOFeAs
- Role: scored
- Action: Compute band structure for LaOFeAs analogously, using the same high‑symmetry path and coordinates (Γ‑X‑M‑Γ‑Z with coordinates from the "High‑symmetry k‑point coordinates" section). Save to bands_LaOFeAs.dat. Energies relative to Fermi level (0 eV).
- Output file: `/app/outputs/bands_LaOFeAs.dat`
- Format: txt
- Contract: Columns: kx, ky, kz (2π/a), band_index (integer), eigenvalue (eV)
- Scoring: scored by hidden verifier

### Step 7: Fermi surface topology analysis
- Role: scored
- Action: From the band structure data, determine for each compound the number of hole-like bands crossing the Fermi level at the Γ point and the number of electron-like bands at the X point. The Fermi level is at 0 eV. A band is considered hole-like at Γ if its eigenvalue at Γ (coordinate (0.0,0.0,0.0)) is negative. A band is considered electron-like at X if its eigenvalue at X (coordinate (0.5,0.0,0.0)) is negative. Write a text file fermi_surface_topology.txt with these counts.
- Output file: `/app/outputs/fermi_surface_topology.txt`
- Format: txt
- Contract: Text: for each compound, lines 'holes_at_Gamma: N', 'electrons_at_X: M'.
- Scoring: scored by hidden verifier

### Step 8: Fe-d bandwidth comparison
- Role: scored (load-bearing)
- Action: From the Fe-d partial density of states data in dos_BaFe2As2.dat and dos_LaOFeAs.dat, compute the Fe-d bandwidth for each compound. The bandwidth is defined as the energy range where the Fe‑d DOS exceeds 10% of its maximum value. Write bandwidth_comparison.txt containing the bandwidth values and their signed difference.
- Output file: `/app/outputs/bandwidth_comparison.txt`
- Format: txt
- Contract: Text: lines 'BaFe2As2 bandwidth: X.XX eV', 'LaOFeAs bandwidth: Y.YY eV', 'Difference: Z.ZZ eV'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_BaFe2As2.dat`
- `/app/outputs/dos_LaOFeAs.dat`
- `/app/outputs/bands_BaFe2As2.dat`
- `/app/outputs/bands_LaOFeAs.dat`
- `/app/outputs/fermi_surface_topology.txt`
- `/app/outputs/bandwidth_comparison.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_BaFe2As2.dat
- path: `/app/outputs/dos_BaFe2As2.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total and Fe-d partial DOS for BaFe2As2; used to derive Fe-d bandwidth.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_dos`, `fe_d_dos`

### dos_LaOFeAs.dat
- path: `/app/outputs/dos_LaOFeAs.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total and Fe-d partial DOS for LaOFeAs; used to derive Fe-d bandwidth.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_dos`, `fe_d_dos`

### bands_BaFe2As2.dat
- path: `/app/outputs/bands_BaFe2As2.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Band structure eigenvalues for BaFe2As2 along high-symmetry path; used to verify Fermi surface topology.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `kz`, `band_index`, `eigenvalue`

### bands_LaOFeAs.dat
- path: `/app/outputs/bands_LaOFeAs.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Band structure eigenvalues for LaOFeAs; used to verify Fermi surface topology.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `kz`, `band_index`, `eigenvalue`

### fermi_surface_topology.txt
- path: `/app/outputs/fermi_surface_topology.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Number of hole-like bands at Γ and electron-like bands at X for each compound.
- schema:
  - `type`: text

### bandwidth_comparison.txt
- path: `/app/outputs/bandwidth_comparison.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Fe-d bandwidth values for BaFe2As2 and LaOFeAs, and their difference.
- schema:
  - `type`: text

Notes: The checker recomputes Fe-d bandwidth from the DOS tables and Fermi surface counts from the band structure files. The DOS and band files are audited structurally; the derived topology and bandwidth are scored against hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_BaFe2As2.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_dos",
          "fe_d_dos"
        ]
      },
      "description": "Total and Fe-d partial DOS for BaFe2As2; used to derive Fe-d bandwidth."
    },
    {
      "file": "dos_LaOFeAs.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_dos",
          "fe_d_dos"
        ]
      },
      "description": "Total and Fe-d partial DOS for LaOFeAs; used to derive Fe-d bandwidth."
    },
    {
      "file": "bands_BaFe2As2.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "kz",
          "band_index",
          "eigenvalue"
        ]
      },
      "description": "Band structure eigenvalues for BaFe2As2 along high-symmetry path; used to verify Fermi surface topology."
    },
    {
      "file": "bands_LaOFeAs.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "kz",
          "band_index",
          "eigenvalue"
        ]
      },
      "description": "Band structure eigenvalues for LaOFeAs; used to verify Fermi surface topology."
    },
    {
      "file": "fermi_surface_topology.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Number of hole-like bands at Γ and electron-like bands at X for each compound."
    },
    {
      "file": "bandwidth_comparison.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text"
      },
      "description": "Fe-d bandwidth values for BaFe2As2 and LaOFeAs, and their difference."
    }
  ],
  "notes": "The checker recomputes Fe-d bandwidth from the DOS tables and Fermi surface counts from the band structure files. The DOS and band files are audited structurally; the derived topology and bandwidth are scored against hidden reference values."
}
```

## How you are scored
A hidden verifier independently reads your submitted raw artifacts and recomputes the key quantities from them:

- From the DOS files (`dos_BaFe2As2.dat` and `dos_LaOFeAs.dat`) the verifier calculates the Fe‑d bandwidth for each compound (energy range where the Fe‑d DOS exceeds 10% of its maximum) and then derives the bandwidth difference. Your score for this load‑bearing step is high when the recomputed difference is close to the expected physical value.
- From the band structure files (`bands_BaFe2As2.dat` and `bands_LaOFeAs.dat`) the verifier counts the number of hole bands at Γ and electron bands at X for each material. It matches Γ by k‑coordinates (0.0,0.0,0.0) and X by (0.5,0.0,0.0), using the energies referenced to zero Fermi level. A band is considered hole‑like at Γ if its eigenvalue is negative, and electron‑like at X if its eigenvalue is negative. Exact match with the expected topology earns full credit for this stage.
- The DOS and band files themselves also undergo a light structural audit (correct columns, ranges); this carries a small weight to reward complete and well‑formed data.

The final reward is a real number between 0 and 1, aggregating the weighted scores of all scored stages. Success requires producing the artifacts by genuinely executing the workflow, not merely reporting the paper's numbers.