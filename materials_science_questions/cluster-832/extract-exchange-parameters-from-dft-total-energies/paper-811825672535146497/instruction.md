# Compute magnetic exchange coupling and moments for a frustrated spin-chain oxide

## Problem background
Sr₃NiPtO₆ is a geometrically frustrated spin-chain oxide that does not show long-range magnetic order down to 1.8 K, exhibiting spin-liquid-like behavior. The crystal structure is rhombohedral (space group R-3c) and contains one-dimensional chains of alternating NiO₆ trigonal prisms and PtO₆ octahedra along the c-axis. To understand the anomalous magnetic properties, one must determine the electronic ground state (insulating vs metallic), the magnitude of the Ni magnetic moment, the nature of the intra-chain magnetic coupling (ferromagnetic or antiferromagnetic), and the role of spin-orbit coupling on orbital moments. Density functional theory calculations can address these questions by computing the total energies, spin and orbital magnetic moments, band gaps, and the exchange coupling J.

## Approach
The investigation uses density functional theory (DFT) within the generalized gradient approximation (GGA) of Wu and Cohen. The electronic structure is studied for the crystal structure taken from published lattice parameters and atomic positions (space group R-3c). Several spin configurations are computed using a plane-wave or all-electron code: (i) a non-magnetic reference; (ii) ferromagnetic (all Ni spins parallel) to obtain Ferromagnetic total energy, Ni spin moment, total spin moment per formula unit, and the down-spin band gap; (iii) ferromagnetic including spin-orbit coupling (SOC) to extract orbital magnetic moments on Ni and Pt; and (iv) antiferromagnetic along the chain (antiparallel Ni neighbors) to obtain the AFM total energy. The Heisenberg exchange parameter J (in kelvin) is derived from the FM-AFM total energy difference using a mapping for an S=1 dimer. The spin-only effective paramagnetic moment is computed as μ = 2√(S(S+1)) from the spin moment, and the total effective moment is obtained by combining the spin and orbital contributions. All relevant computed and derived quantities are collected into a single JSON file.

## Reproduction target
Produce a JSON file named `computed_results.json` in `/app/outputs/` containing the key DFT-computed quantities obtained from your own calculations. The file must include: ferromagnetic and antiferromagnetic total energies per formula unit (in Rydberg), their energy difference (meV/f.u.), Ni spin magnetic moment (μB), total spin magnetic moment per formula unit (μB), the ferromagnetic down-spin band gap (eV), the Heisenberg exchange parameter J (K), the Ni and Pt orbital magnetic moments from the SOC calculation (μB), and the effective paramagnetic moment (μB). All quantities must be derived from the DFT runs described in the workflow steps.

## Assets

- Crystal structure of Sr3NiPtO6: 10.1021/cm9807732
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Pseudopotentials for Sr, Ni, Pt, O: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Set up crystal structure
- Role: process
- Action: Construct the crystal structure of Sr3NiPtO6 from the literature lattice parameters and atomic positions (rhombohedral, space group R-3c). Generate input files for the DFT code.
- Evidence: none

### Step 2: Non-magnetic GGA calculation
- Role: process
- Action: Perform a self-consistent non-magnetic GGA calculation. Record the total energy for reference.
- Evidence: none

### Step 3: Ferromagnetic GGA calculation
- Role: process
- Action: Perform a spin-polarized ferromagnetic GGA calculation. Extract the Ni spin magnetic moment, the total spin magnetic moment per formula unit, the ferromagnetic total energy, and the down-spin band gap.
- Evidence: none

### Step 4: Ferromagnetic GGA+SOC calculation
- Role: process
- Action: Perform a ferromagnetic GGA calculation including spin-orbit coupling. Extract the orbital magnetic moments on Ni and Pt. Verify that the spin moments remain essentially unchanged.
- Evidence: none

### Step 5: Antiferromagnetic GGA calculation
- Role: process
- Action: Perform an antiferromagnetic GGA calculation with antiparallel Ni spin alignment along the chain. Record the total energy.
- Evidence: none

### Step 6: Compile final results and derive exchange/effective moments
- Role: scored (load-bearing)
- Action: From the FM and AFM total energies, compute the Heisenberg exchange parameter J (in kelvin) using a mapping for an S=1 dimer. From the spin moment compute the spin-only effective paramagnetic moment (μ = 2√(S(S+1))). Combine with the orbital contribution to obtain the total effective paramagnetic moment. Write all computed and derived quantities to /app/outputs/computed_results.json according to the output contract.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: Keys: fm_total_energy_per_fu_Ry (float), afm_total_energy_per_fu_Ry (float), energy_difference_meV_per_fu (float), ni_spin_moment_muB (float), total_spin_moment_per_fu_muB (float), band_gap_fm_down_spin_eV (float), exchange_J_K (float), ni_orbital_moment_soc_muB (float), pt_orbital_moment_soc_muB (float), effective_paramagnetic_moment_muB (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the key DFT-derived quantities for Sr3NiPtO6. All fields are numeric values computed from the agent's own DFT runs.
- schema:
  - `type`: object
  - `required`:
    - `fm_total_energy_per_fu_Ry`: number (Rydberg per formula unit)
    - `afm_total_energy_per_fu_Ry`: number (Rydberg per formula unit)
    - `energy_difference_meV_per_fu`: number (meV per formula unit)
    - `ni_spin_moment_muB`: number (Bohr magneton)
    - `total_spin_moment_per_fu_muB`: number (Bohr magneton per formula unit)
    - `band_gap_fm_down_spin_eV`: number (eV)
    - `exchange_J_K`: number (kelvin)
    - `ni_orbital_moment_soc_muB`: number (Bohr magneton)
    - `pt_orbital_moment_soc_muB`: number (Bohr magneton)
    - `effective_paramagnetic_moment_muB`: number (Bohr magneton)
  - `items`: object

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "fm_total_energy_per_fu_Ry": "number (Rydberg per formula unit)",
          "afm_total_energy_per_fu_Ry": "number (Rydberg per formula unit)",
          "energy_difference_meV_per_fu": "number (meV per formula unit)",
          "ni_spin_moment_muB": "number (Bohr magneton)",
          "total_spin_moment_per_fu_muB": "number (Bohr magneton per formula unit)",
          "band_gap_fm_down_spin_eV": "number (eV)",
          "exchange_J_K": "number (kelvin)",
          "ni_orbital_moment_soc_muB": "number (Bohr magneton)",
          "pt_orbital_moment_soc_muB": "number (Bohr magneton)",
          "effective_paramagnetic_moment_muB": "number (Bohr magneton)"
        },
        "items": {}
      },
      "description": "Scored artifact containing the key DFT-derived quantities for Sr3NiPtO6. All fields are numeric values computed from the agent's own DFT runs."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/computed_results.json` and independently scores every field. Each numeric value is compared against the paper's reported gold value using tolerances that account for differences in DFT implementations and pseudopotentials. Additionally, the verifier may recompute derived quantities — the exchange parameter J and the effective paramagnetic moment — from your reported raw total energies and magnetic moments to verify internal consistency. The final reward is a weighted average across all fields; a solution that falls within tolerance for every quantity earns full credit. Simply reporting the paper’s numbers without performing the actual calculations is not sufficient, because the verifier cross-checks derived quantities against the raw energies.
