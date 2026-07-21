# Kinetic Monte Carlo Surface Intermixing Simulation

## Problem background
During epitaxial growth of Ge on Si(001), atoms from the deposited germanium layer can exchange with silicon atoms in the top substrate layers, a process called intermixing. This intermixing leads to a temperature-dependent graded Ge concentration profile near the interface, rather than an abrupt transition. Understanding these profiles and the resulting energetics is important for predicting when the flat film becomes unstable and begins to form three-dimensional islands (quantum dots). We will compute the composition of the intermixed layers and the chemical potential of the flat epilayer as more Ge is added, and use a reference island potential to determine at which film thickness the flat epilayer becomes energetically unfavorable.

## Approach
We model intermixing with a flexible-lattice Monte Carlo simulation of the Si(001) substrate with Ge epilayers. The simulation uses a diamond lattice with realistic surface dimer reconstructions, the Tersoff empirical potential to evaluate energy, and conjugate-gradient minimisation to relax atomic positions after each swap attempt. Atom exchanges are attempted only between the top two crystal layers using the Metropolis algorithm at the given temperature; layers that become fully buried are frozen and no longer participate in later exchanges.

For the first analysis, we construct a Si(001) slab (16×16 lateral unit cells, 16 mobile layers + 2 fixed bottom layers) and deposit 1 monolayer (ML) of Ge in a (2×8) surface reconstruction. The top two layers are equilibrated at 600 °C, and we measure the fraction of surface atoms that are Ge after equilibration.

For the main growth study, we switch to an 8×8 lateral cell substrate of the same vertical structure. We deposit seven whole Ge monolayers one by one, each with a (2×8) reconstruction, and equilibrate the top two layers at 800 °C for 150 Monte Carlo steps after each deposition. We record the Ge atomic fraction in each of the seven crystal layers after all seven layers have been added, as well as the total energy of the slab after the addition of each epilayer.

From the recorded energies we compute the chemical potential of the flat epilayer relative to bulk Ge for each deposited monolayer using:

μ_epi = (E_epi – E_ref) / N – ε_Ge

where E_epi is the total energy after depositing that epilayer, E_ref is the energy before that epilayer was added, N is the number of atoms added, and ε_Ge = –3.8506 eV/atom is the cohesive energy of bulk germanium. We compare the computed μ_epi values to a known reference island chemical potential of 31 meV/atom to determine the onset of islanding.

## Reproduction target
Produce three scored output files by running the simulations described in the workflow steps:

1. `surface_composition.json` — the fraction of surface atoms that are Ge after 1 ML Ge/Si(001) has been equilibrated at 600 °C.
2. `composition_profile.json` — a 7-element array of Ge atomic fractions (layer 1 = topmost surface layer) after growing seven Ge monolayers at 800 °C with intermixing.
3. `chemical_potential.json` — a 7-element array of chemical potentials (in eV) for each epilayer (1 through 7) at 800 °C, computed from the slab energies recorded during the growth simulation.

A hidden verifier will compare these outputs to the paper's published results, and will also check that the chemical potential values obey the expected crossover behaviour with respect to the reference island potential (31 meV/atom).

## Assets

- LAMMPS: https://www.lammps.org/
- Tersoff potential parameters for Si and Ge (available in LAMMPS)

## Workflow steps

### Step 1: Develop simulation engine and construct substrate
- Role: process
- Action: Implement the flexible-lattice Monte Carlo simulation that constructs a diamond-lattice Si(001) substrate with (2×1) surface dimer reconstruction, 16×16 lateral unit cells (unit cell length 5.43 Å), 16 mobile layers + 2 fixed bottom layers, periodic boundaries; uses Tersoff potential for energy and conjugate-gradient relaxation to force < 10⁻³ eV/Å; performs Metropolis Monte Carlo exchanges of atoms within the top two layers. The code must also support deposition of Ge epilayers with (2×8) reconstruction.
- Evidence: implementation code (not submitted as a scored file)

### Step 2: Run single-layer equilibration at 600°C
- Role: scored
- Action: Construct a Si(001) substrate (16×16 lateral unit cells, 16 mobile layers + 2 fixed) with 1 ML of Ge in (2×8) reconstruction. Equilibrate the top two layers for 25 Monte Carlo steps (MCS) equilibration followed by 25 MCS measurement at 600°C. Record the final fraction of surface atoms that are Ge.
- Output file: `/app/outputs/surface_composition.json`
- Format: json
- Contract: {"surface_ge_fraction": float}
- Scoring: scored by hidden verifier

### Step 3: Run multilayer growth at 800°C
- Role: scored (load-bearing)
- Action: Starting from an 8×8 unit cell Si(001) substrate (16 mobile layers + 2 fixed), deposit seven whole monolayers of Ge one by one, each with (2×8) reconstruction. After each deposition, equilibrate the top two layers for 150 MCS at 800°C. After all layers are deposited, record the Ge atomic fraction in each of the seven crystal layers (1 = topmost).
- Output file: `/app/outputs/composition_profile.json`
- Format: json
- Contract: [float, float, float, float, float, float, float]
- Scoring: scored by hidden verifier

### Step 4: Compute chemical potentials
- Role: scored
- Action: Using the total energies recorded after each epilayer deposition in the multilayer growth simulation, compute the chemical potential per epilayer via μ_epi = (E_epi - E_ref)/N - ε_Ge, where E_epi is the total energy with that epilayer, E_ref the energy before the epilayer was added, N the number of added atoms, and ε_Ge = -3.8506 eV/atom. Output the seven chemical potentials in eV.
- Output file: `/app/outputs/chemical_potential.json`
- Format: json
- Contract: [float, float, float, float, float, float, float]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_composition.json`
- `/app/outputs/composition_profile.json`
- `/app/outputs/chemical_potential.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_composition.json
- path: `/app/outputs/surface_composition.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Surface Ge atomic fraction after 1 ML Ge/Si(001) equilibration at 600°C. The checker compares against the paper-reported value from Figure 5.
- schema:
  - `type`: object
  - `required`:
    - `surface_ge_fraction`: float

### composition_profile.json
- path: `/app/outputs/composition_profile.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ge composition profile (fraction) across the top 7 layers after 7 ML growth at 800°C. Compared to the paper's depth profile (Figure 7).
- schema:
  - `type`: array
  - `items`:
    - ``: float

### chemical_potential.json
- path: `/app/outputs/chemical_potential.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Chemical potentials (eV) for epilayers 1 through 7. Checker compares to Figure 10 and also verifies that the chemical potential values cross above the reference island potential (31 meV/atom) at the expected monolayer number.
- schema:
  - `type`: array
  - `items`:
    - ``: float

Notes: Scoring uses a result-level compare (T0) against hidden paper-reported values from Figures 5, 7, and 10, with appropriate tolerances. An additional structural check (T3) on the chemical potential array ensures the islanding onset after 3-4 monolayers is captured.

## How you are scored
Your submission is evaluated by a hidden verifier that runs automatically. For each scored output file (`surface_composition.json`, `composition_profile.json`, `chemical_potential.json`), the verifier compares your reported value(s) to the paper's reference results using appropriate tolerances that account for the stochastic nature of the Monte Carlo simulation. Additionally, the verifier checks the chemical potential array against the expected structural behaviour: it verifies that the flat‑epilayer potential is lower than the island potential (31 meV/atom) for the initial monolayers and crosses above it at the monolayer thickness that the paper reports. The individual scores are weighted (the growth profile and chemical potentials carry the largest weight) and combined into a final reward between 0 and 1. Simply reporting the paper's numbers without actually running the simulation will not pass the structural check.