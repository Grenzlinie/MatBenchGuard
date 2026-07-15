# DFT Rigid-Shift Scan for ZrPc: Energy Barrier and Equilibrium Displacement

## Problem background
Metal phthalocyanines (MPc) containing early 4d transition-metal ions can adopt a non-planar 'shuttlecock' shape, which may impart a magnetic moment to the molecule. Designing a molecular magnetic switch requires understanding how the metal ion's position relative to the organic macrocycle influences the total energy and the magnetic state. A straightforward first step is to compute the energy landscape when the metal ion is rigidly shifted across a fixed, planar phthalocyanine (Pc) macrocycle. This provides the energy barrier for the ion to cross the molecular plane and identifies the preferred out-of-plane distance, laying the groundwork for more complex substrate-adsorbed switching studies.

## Approach
The procedure uses spin-polarized density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and the Grimme D2 semi-empirical van der Waals correction. The system consists of an isolated, planar Pc macrocycle (all atoms fixed in one plane) and a single Zr atom. A rigid-shift scan is performed: the Zr atom is placed at a series of distances d perpendicular to the Pc plane (ranging from 0.0 to 1.0 Å) while the Pc atoms are kept frozen. For each distance, a self-consistent DFT calculation is run, yielding the total energy of the system and the local magnetic moment on the Zr atom. From these data, the energy barrier (maximum energy minus minimum energy) and the equilibrium displacement (the distance at which the energy is minimized) are extracted. No structural relaxation of the Pc macrocycle is performed. All calculations use periodic boundary conditions with sufficient vacuum to isolate the molecule; the choice of k‑point sampling, plane‑wave energy cutoff, and pseudopotentials is left to the agent, provided they are adequate for a converged PBE+D2 treatment.

## Reproduction target
Use Quantum ESPRESSO (or a compatible open‑source DFT code) to compute, for a Zr atom rigidly shifted through a planar Pc macrocycle at distances d = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 Å, the total energy and the magnetic moment on Zr. From the results, determine the energy barrier (the difference between the highest and lowest total energy across these distances) and the equilibrium displacement d_min (the distance at which the total energy is lowest). Report the scan data in a CSV file and the extracted d_min in a separate text file. The magnetic moment at the equilibrium distance must also be obtainable from the CSV. The task is considered achieved if the computed barrier, equilibrium distance, and magnetic moment are physically reasonable and consistent with a genuine DFT calculation, as judged by a hidden verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Planar phthalocyanine (Pc) geometry
- SSSP pseudopotential library (PBE, PAW): https://www.materialscloud.org/discover/sssp/table
- Grimme D2 van der Waals correction: Quantum ESPRESSO

## Workflow steps

### Step 1: Build isolated ZrPc rigid-shift input structures
- Role: process
- Action: Construct the atomic coordinates of a planar phthalocyanine (Pc) macrocycle (all atoms in one plane, standard bond connectivity) and a Zr atom. Create a series of input geometry files where the Zr atom is placed at distances d = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 Å from the Pc plane along the molecular axis (perpendicular to the plane). The Pc coordinates remain fixed across all steps.
- Evidence: `/app/outputs/geometry_inputs_log.txt`

### Step 2: Run DFT rigid-shift scans for ZrPc and compile energy/moment
- Role: scored (load-bearing)
- Action: For each displacement d created in Step 1, run a spin-polarized DFT calculation using Quantum ESPRESSO with the PBE functional and Grimme D2 vdW correction (input_dft='PBE+D2'). Use adequate k-point sampling and energy cutoffs. From the converged calculation extract the total energy (in eV) and the magnetic moment on the Zr atom (integrated magnetization within a sphere or from the atomic projection). Collect the results for all d into a CSV file named energy_profile.csv with columns: d (in Å), total_energy (in eV), mag_moment (in μB).
- Output file: `/app/outputs/energy_profile.csv`
- Format: csv
- Contract: columns: d (float, Å), total_energy (float, eV), mag_moment (float, μB)
- Scoring: scored by hidden verifier

### Step 3: Determine equilibrium displacement from the scan
- Role: scored
- Action: From the energy_profile.csv produced in Step 2, identify the displacement d_min that yields the lowest total_energy (the equilibrium out-of-plane displacement). Write that single value (in Å, to two decimal places) into a text file named equilibrium_d.txt.
- Output file: `/app/outputs/equilibrium_d.txt`
- Format: txt
- Contract: a single floating-point number (e.g., '0.75')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_profile.csv`
- `/app/outputs/equilibrium_d.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_profile.csv
- path: `/app/outputs/energy_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file containing the DFT rigid-shift scan results: displacement d (Å), total energy (eV), and magnetic moment on Zr (μB) for six displacement steps from 0.0 Å to 1.0 Å. The checker will recompute the energy barrier (max-min energy) and the equilibrium displacement (d at min energy) and compare to hidden reference thresholds.
- schema:
  - `type`: table
  - `required_columns`: `d`, `total_energy`, `mag_moment`
  - `units`:
    - `d`: Å
    - `total_energy`: eV
    - `mag_moment`: μB

### equilibrium_d.txt
- path: `/app/outputs/equilibrium_d.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Text file containing the agent's extracted equilibrium displacement from the DFT scan. The checker will verify this value is consistent with the energy profile and lies within an acceptable tolerance of the paper-reported equilibrium distance.
- schema:
  - `type`: text
  - `description`: Single floating-point value representing the equilibrium out-of-plane displacement d_min (Å) to two decimal places.

Notes: All scored quantities are derived from the agent's DFT calculations. The energy barrier, equilibrium displacement, and magnetic moment at equilibrium are compared to paper-reported values using tolerance-based thresholds. The CSV serves as the raw data source for recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "d",
          "total_energy",
          "mag_moment"
        ],
        "units": {
          "d": "Å",
          "total_energy": "eV",
          "mag_moment": "μB"
        }
      },
      "description": "CSV file containing the DFT rigid-shift scan results: displacement d (Å), total energy (eV), and magnetic moment on Zr (μB) for six displacement steps from 0.0 Å to 1.0 Å. The checker will recompute the energy barrier (max-min energy) and the equilibrium displacement (d at min energy) and compare to hidden reference thresholds."
    },
    {
      "file": "equilibrium_d.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "Single floating-point value representing the equilibrium out-of-plane displacement d_min (Å) to two decimal places."
      },
      "description": "Text file containing the agent's extracted equilibrium displacement from the DFT scan. The checker will verify this value is consistent with the energy profile and lies within an acceptable tolerance of the paper-reported equilibrium distance."
    }
  ],
  "notes": "All scored quantities are derived from the agent's DFT calculations. The energy barrier, equilibrium displacement, and magnetic moment at equilibrium are compared to paper-reported values using tolerance-based thresholds. The CSV serves as the raw data source for recomputation."
}
```

## How you are scored
A hidden checker will inspect your submitted output files and compute several scores:

- Energy‑barrier score: The checker reads your energy_profile.csv, determines the barrier (max energy − min energy), and compares it to the expected value. A larger absolute deviation reduces the score.
- Equilibrium‑displacement score: The checker extracts the distance d_min from equilibrium_d.txt and verifies that it matches the row with the lowest energy in energy_profile.csv. It then compares this displacement against the expected equilibrium distance. Consistency among your files is required; a mismatch between the two outputs is penalised.
- Magnetic‑moment score: At the equilibrium distance identified from your CSV, the checker compares the reported magnetic moment on Zr to the expected value.
- Overall reward: The final score is a weighted combination of these components, with the energy barrier and equilibrium displacement carrying the largest weights, and the magnetic moment and file consistency receiving smaller weights.

The verifier uses tolerance thresholds that reflect the variability inherent in running DFT calculations with different implementations (e.g., pseudopotential choice, k‑point density, basis set cutoff). You must not rely on simply reporting the paper’s numbers; the checker cross‑validates your outputs and may include additional hidden checks to ensure the scan was genuinely performed.
