# DFT calculation of hydrogen interstitial formation energies in Ti3SiC2

## Problem background
Ti3SiC2 is a MAX phase material that combines metallic and ceramic properties, such as good electrical conductivity, machinability, and oxidation resistance. In hydrogen-rich environments, interstitial hydrogen can influence the stability and mechanical properties of the material. To assess this, it is important to determine the formation energies and lattice volume changes when a single hydrogen atom occupies interstitial sites in the Ti3SiC2 crystal. This experiment examines three candidate interstitial positions (I‑Ti, I‑SiTi, I‑SiC) and asks: what are their relative stabilities and how does the lattice deform?

## Approach
We use plane-wave density functional theory (DFT) with norm-conserving pseudopotentials and the generalized gradient approximation (GGA) for exchange‑correlation. A 2×1×1 supercell of Ti3SiC2 (24 atoms) is employed, with a single H atom added at each interstitial site. Total energies of the perfect crystal and an isolated H atom are computed as references. After full geometry optimization of each doped supercell, the formation energy of the interstitial is obtained as Ef = Edoped − Eperfect − EH, and the relative volume change ΔV is derived from the relaxed cell volumes. Three distinct interstitial configurations are considered: I‑Ti, I‑SiTi, and I‑SiC. The calculations can be performed with any open‑source DFT code that supports the required features, such as Quantum ESPRESSO.

## Reproduction target
Produce a JSON file containing, for each of the three interstitial sites, the computed formation energy (eV) and relative volume change (%), together with the underlying total energies Edoped, Eperfect, and EH. The file must follow the schema specified under Output contract and be written to /app/outputs/formation_energies_and_volume_changes.json.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org
- Norm-conserving pseudopotentials for Ti, Si, C, H: https://www.materialscloud.org/discover/sssp
- Ti3SiC2 crystal structure

## Workflow steps

### Step 1: Geometry optimization of perfect Ti3SiC2
- Role: process
- Action: Perform DFT geometry optimization (variable-cell relaxation) of the perfect Ti3SiC2 unit cell. Use norm-conserving pseudopotentials, GGA exchange-correlation, and a suitably large plane-wave cutoff and k-point mesh to relax both lattice parameters and atomic positions. Obtain the equilibrium total energy E_perfect and relaxed cell volume V_perfect.
- Evidence: none

### Step 2: Total energy of an isolated hydrogen atom
- Role: process
- Action: Calculate the total energy of an isolated hydrogen atom in a large supercell using the same DFT parameters as for the crystal (norm-conserving pseudopotential, GGA, plane-wave cutoff). Record the energy E_H.
- Evidence: none

### Step 3: Geometry optimization of H‑doped supercells
- Role: process
- Action: For each interstitial site (I‑Ti, I‑SiTi, I‑SiC) construct a 2×1×1 supercell (24 atoms) of Ti3SiC2, insert one hydrogen atom at the defined position, and perform full geometry optimization (atomic positions and cell parameters) using the same DFT setup as for the perfect crystal. For each case, record the final total energy E_doped and the relaxed supercell volume V_relax.
- Evidence: none

### Step 4: Compute formation energies and volume changes
- Role: scored (load-bearing)
- Action: From the energies and volumes obtained in the previous steps, compute for each site: formation energy E_H_f = E_doped − E_perfect − E_H and relative volume change ΔV = (V_relax − V_perfect)/V_perfect × 100%. Output a JSON array containing one object per interstitial site with the computed quantities and the underlying total energies.
- Output file: `/app/outputs/formation_energies_and_volume_changes.json`
- Format: json
- Contract: A JSON array of three objects, one per site, each with keys: site (string, one of 'I-Ti','I-SiTi','I-SiC'), E_doped (float, eV), E_perfect (float, eV), E_H (float, eV), formation_energy_eV (float), volume_change_percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies_and_volume_changes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies_and_volume_changes.json
- path: `/app/outputs/formation_energies_and_volume_changes.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Formation energies and volume changes for hydrogen interstitials at the three sites, with all total energies used in the derivation.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `site`:
        - `type`: string
      - `E_doped`:
        - `type`: number
        - `units`: eV
      - `E_perfect`:
        - `type`: number
        - `units`: eV
      - `E_H`:
        - `type`: number
        - `units`: eV
      - `formation_energy_eV`:
        - `type`: number
        - `units`: eV
      - `volume_change_percent`:
        - `type`: number
        - `units`: %
    - `required`: `site`, `E_doped`, `E_perfect`, `E_H`, `formation_energy_eV`, `volume_change_percent`

Notes: The checker will internally recompute formation_energy_eV from the provided E_doped, E_perfect, E_H to verify consistency, then compare formation energies and volume changes against hidden reference values derived from the paper. The DFT calculations must use norm-conserving pseudopotentials and GGA; approximate agreement within method-dependent spread is expected.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies_and_volume_changes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "site": {
              "type": "string"
            },
            "E_doped": {
              "type": "number",
              "units": "eV"
            },
            "E_perfect": {
              "type": "number",
              "units": "eV"
            },
            "E_H": {
              "type": "number",
              "units": "eV"
            },
            "formation_energy_eV": {
              "type": "number",
              "units": "eV"
            },
            "volume_change_percent": {
              "type": "number",
              "units": "%"
            }
          },
          "required": [
            "site",
            "E_doped",
            "E_perfect",
            "E_H",
            "formation_energy_eV",
            "volume_change_percent"
          ]
        }
      },
      "description": "Formation energies and volume changes for hydrogen interstitials at the three sites, with all total energies used in the derivation."
    }
  ],
  "notes": "The checker will internally recompute formation_energy_eV from the provided E_doped, E_perfect, E_H to verify consistency, then compare formation energies and volume changes against hidden reference values derived from the paper. The DFT calculations must use norm-conserving pseudopotentials and GGA; approximate agreement within method-dependent spread is expected."
}
```

## How you are scored
A hidden verifier will read your JSON file. It will first verify that the reported formation energies are internally consistent by recomputing Ef from the supplied Edoped, Eperfect, and EH. It will then compare your reported formation energies and volume changes against established reference values (hidden) using appropriate tolerances. Additionally, the verifier will check that the relative ordering of the three sites is physically correct. Full credit requires all values to be within tolerance and the ordering to be correct; partial credit may be awarded for correctly reproducing the ordering alone.
