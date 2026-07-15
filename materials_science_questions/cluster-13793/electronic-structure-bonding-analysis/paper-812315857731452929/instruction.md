# DFT Calculations of Sc2AC MAX Phases Properties

## Problem background
MAX phases are layered carbides exhibiting a combination of metallic and ceramic properties, making them attractive for high-temperature structural applications. This task investigates the Sc₂AC family (A = Al, Ga, In, Tl), which have been proposed as weakly coupled MAX phases. The central open question is whether the bulk modulus of the constituent binary carbide ScC is conserved in the ternary phases and whether a pseudogap appears near the Fermi level. Your goal is to compute the structural, elastic, and electronic properties that determine this classification.

## Approach
You will use density functional theory (DFT) within the generalized gradient approximation (GGA) to simulate Sc₂AC (A = Al, Ga, In, Tl), the binary ScC, and the elemental references (Sc hcp, C graphite, and the A elements in their standard structures). All calculations employ an open-source plane-wave code with appropriate pseudopotentials. For each Sc₂AC and for ScC, you will obtain total energy as a function of volume by performing geometry relaxations at a series of fixed volumes. From the resulting energy–volume (E–V) curves you will fit the Birch–Murnaghan equation of state to extract equilibrium lattice parameters, volume per atom, and bulk modulus. The formation energy per atom of each Sc₂AC phase is computed from the total energies of the compound and its elemental references. Finally, you will compute the total density of states (DOS) at the equilibrium structure and locate the major pseudogap minimum below the Fermi level.

## Reproduction target
Produce two JSON files:

1. **`relaxed_params.json`** – for each of Sc₂AlC, Sc₂GaC, Sc₂InC, Sc₂TlC, and ScC, report the equilibrium lattice parameter *a* (Å), hexagonal *c/a* ratio, equilibrium volume per atom V₀ (Å³/atom), bulk modulus *B* (GPa), and (for the Sc₂AC phases only) formation energy per atom *E_f* (eV/atom).

2. **`pseudogap.json`** – for each Sc₂AC compound, report the energy of the first DOS minimum below the Fermi level (eV, relative to the Fermi level).

All values must be computed from your own DFT workflow; reporting the paper’s numbers without performing the calculations is insufficient.

## Assets

- Quantum ESPRESSO (or other open-source plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency set) or equivalent: https://www.materialscloud.org/discover/sssp/table/efficiency
- Standard elemental crystal structures (Sc hcp, C graphite, A elements in their standard structures, ScC rocksalt)

## Workflow steps

### Step 1: DFT calculations for Sc2AC, elemental references, and ScC
- Role: process
- Action: Perform plane-wave DFT calculations with GGA for Sc2AC (A=Al, Ga, In, Tl), ScC, and elemental references Sc (hcp), C (graphite), and A elements in their standard structures. For each Sc2AC and ScC, run a series of fixed-volume geometry relaxations to obtain total energy vs volume data. Use an open-source DFT code and appropriate pseudopotentials. Ignore spin polarization.
- Evidence: `/app/outputs/dft_log.txt`

### Step 2: Extract structural parameters, bulk moduli, and formation energies
- Role: scored (load-bearing)
- Action: From the E–V data generated in step-1, fit the Birch–Murnaghan equation of state to obtain equilibrium volume, lattice parameter a, c/a ratio, and bulk modulus for each Sc2AC compound and for ScC. Compute the formation energy per atom for each Sc2AC using the total energies of the compound and elemental references. Output all values in a JSON file.
- Output file: `/app/outputs/relaxed_params.json`
- Format: json
- Contract: JSON array of 5 objects. Each object has keys: compound (string), a_A (float, omit for ScC), c_over_a (float, omit for ScC), V_o_A3_per_atom (float, omit for ScC), B_GPa (float), E_f_eV_per_atom (float, omit for ScC). Example entry: {"compound":"Sc2AlC","a_A":0.0,"c_over_a":0.0,"V_o_A3_per_atom":0.0,"B_GPa":0,"E_f_eV_per_atom":0.0}
- Scoring: scored by hidden verifier

### Step 3: Calculate pseudogap energies from density of states
- Role: scored
- Action: For each Sc2AC compound, compute the total density of states (DOS) at the equilibrium structure from step-1. Identify the energy of the major pseudogap minimum (first minimum below the Fermi level) relative to the Fermi level. Record this energy for each compound.
- Output file: `/app/outputs/pseudogap.json`
- Format: json
- Contract: JSON array of 4 objects. Each object has keys: compound (string), pseudogap_energy_eV (float). Example: {"compound":"Sc2AlC","pseudogap_energy_eV":0.0}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_params.json`
- `/app/outputs/pseudogap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_params.json
- path: `/app/outputs/relaxed_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice parameters, bulk moduli, and formation energies for Sc2AC and ScC.

### pseudogap.json
- path: `/app/outputs/pseudogap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Pseudogap energies for Sc2AC phases.

Notes: T0 result-level comparison against paper-reported values with tolerances (a ±0.02 Å, c/a ±0.1, V_o ±0.5 Å³/atom, B ±5 GPa, E_f ±0.05 eV/atom, pseudogap ±0.1 eV).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {},
      "description": "Equilibrium lattice parameters, bulk moduli, and formation energies for Sc2AC and ScC."
    },
    {
      "file": "pseudogap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {},
      "description": "Pseudogap energies for Sc2AC phases."
    }
  ],
  "notes": "T0 result-level comparison against paper-reported values with tolerances (a ±0.02 Å, c/a ±0.1, V_o ±0.5 Å³/atom, B ±5 GPa, E_f ±0.05 eV/atom, pseudogap ±0.1 eV)."
}
```

## How you are scored
A hidden verifier runs after your submission. It reads your `relaxed_params.json` and `pseudogap.json`, and compares each reported value to a hidden reference derived from the published experiment. Your total reward (0–1) is the weighted sum over all scored quantities: each quantity that falls within an allowed deviation from the reference earns full credit, and quantities outside that range earn zero. The weights emphasize the structural and elastic properties (bulk moduli, lattice parameters, volumes) and the formation energies, with a smaller weight for the pseudogap energies. The verifier does not inspect your DFT inputs or intermediate files—only the final JSON outputs are scored.
