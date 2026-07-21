# Phase diagram of TMD heterobilayer with competing Coulomb interaction and chiral tunnelling

## Problem background
Van der Waals heterobilayers of transition metal dichalcogenides (TMDs) can host a rich interplay of Coulomb interaction and interlayer quantum tunnelling. When the two layers feature type-II band alignment with spin-valley locking, an interlayer bias can tune the band gap $E_g$ and allow competition between an exciton superfluid (driven by Coulomb attraction that favours $s$-wave electron-hole coherence) and a chiral tunnelling term (which creates/annihilates electron-hole pairs exclusively in the $p$-wave channel). This competition is predicted to give rise to multiple quantum phases — including normal insulator, exciton superfluid, magnetic exciton superfluid, coexisting quantum anomalous Hall and exciton superfluid, quantum spin Hall, and quantum anomalous Hall insulators — as the band gap and the interlayer dielectric constant $\varepsilon_\perp$ are varied. The task is to compute the ground-state phase diagram of this system: find which phase occupies each point in the $(E_g, \varepsilon_\perp)$ plane.

## Approach
The heterobilayer is modelled at the mean-field level by a two-band Hamiltonian for the $\pm K$ valleys. Intra- and inter-layer Coulomb interactions are treated in the Hartree-Fock approximation, and the interlayer tunnelling has a momentum-space form $t_{\tau\mathbf{k}} \propto (\tau k_x - i k_y)$ enforced by $C_3$ symmetry ($\tau=\pm1$ denotes valley). The self-consistent gap equation couples the order parameter $\Delta_{\tau\mathbf{k}}$ to the Coulomb potential. The material parameters are taken from published first-principles calculations: interlayer distance $D=0.62$ nm, dielectric anisotropy $\varepsilon_\parallel/\varepsilon_\perp=1.6$, reduced mass $m=0.5\,m_0$, valence-band hopping $t_{vv}=14.4$ meV, Dirac velocity $v=3.512$ eV·Å, and monolayer gap $M=1.66$ eV. You will discretize the momentum space, set up the Hamiltonian, and solve the non-linear gap equation for $\Delta_{\tau\mathbf{k}}$ at each point of a grid spanning $E_g\in[-0.4,0.4]$ eV and $\varepsilon_\perp\in[2,20]$. Multiple initial guesses must be tried to capture all stable solutions. From the converged order parameter you will then classify the ground state by analysing its $s$-wave vs $p$-wave character, spin polarization (charge imbalance between valleys), and topological Hall conductivity (Chern number or spin Chern number).

## Reproduction target
Produce a CSV file `phase_diagram.csv` whose rows correspond to every $(E_g, \varepsilon_\perp)$ grid point: $E_g$ from $-0.4$ eV to $+0.4$ eV in steps $\le 0.02$ eV; $\varepsilon_\perp$ from $2$ to $20$ in steps $\le 1$. Each row must contain the band gap (eV), the dielectric constant (dimensionless), and an integer phase label:
- 0 = Normal insulator (NI)
- 1 = Exciton superfluid (ES)
- 2 = Magnetic exciton superfluid (MES)
- 3 = Coexisting QAH and ES (QAH-ES)
- 4 = Quantum spin Hall (QSH)
- 5 = Quantum anomalous Hall (QAH)

The classification must be based solely on the self-consistent solutions obtained with the given parameters.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Solve self-consistent gap equation
- Role: process
- Action: Build the two-band mean-field Hamiltonian for a TMD heterobilayer including intra- and inter-layer Coulomb interactions and a chiral interlayer tunnelling term. Use the provided material parameters (D=0.62 nm, ε∥/ε⊥=1.6, m=0.5 m₀, t_vv=14.4 meV, v=3.512 eV·Å, M=1.66 eV). Discretize momentum space and solve the valley-coupled self-consistent gap equation (Hartree-Fock) for the order parameter Δ_{τk} on a grid covering band gap Eg ∈ [-0.4, 0.4] eV (step ≤ 0.02 eV) and interlayer dielectric constant ε⊥ ∈ [2, 20] (step ≤ 1). Iterate from multiple initial trial order parameters to find stable solutions, and store the converged order parameter, coherence factors u, v, and quasiparticle energies for each grid point.
- Evidence: `/app/outputs/raw_solutions.npz`

### Step 2: Phase classification and diagram
- Role: scored (load-bearing)
- Action: From the raw solutions (step_01), determine the phase at each (Eg, ε⊥) grid point by analyzing the symmetry of the order parameter (s-wave vs p-wave), the spin polarization, and the topological Hall conductivity. Map the phases to integer labels: 0=Normal insulator (NI), 1=Exciton superfluid (ES), 2=Magnetic exciton superfluid (MES), 3=Coexisting QAH and ES (QAH-ES), 4=Quantum spin Hall (QSH), 5=Quantum anomalous Hall (QAH). Write a CSV file with columns Eg (eV), epsilon_perp (dimensionless), phase (integer label).
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: CSV with columns: Eg (float, eV), epsilon_perp (float, dimensionless), phase (integer 0..5).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file mapping each (Eg, epsilon_perp) grid point to a phase label integer. Reproduces the main phase diagram of the paper.
- schema:
  - `type`: table
  - `required_columns`: `Eg`, `epsilon_perp`, `phase`
  - `units`:
    - `Eg`: eV
    - `epsilon_perp`: dimensionless

Notes: The phase labels must correspond to the classification scheme described in the instructions. The checker will compare the labels at a set of hidden (Eg, epsilon_perp) points to a reference derived from the paper, allowing neighbor labels at phase boundaries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Eg",
          "epsilon_perp",
          "phase"
        ],
        "units": {
          "Eg": "eV",
          "epsilon_perp": "dimensionless"
        }
      },
      "description": "CSV file mapping each (Eg, epsilon_perp) grid point to a phase label integer. Reproduces the main phase diagram of the paper."
    }
  ],
  "notes": "The phase labels must correspond to the classification scheme described in the instructions. The checker will compare the labels at a set of hidden (Eg, epsilon_perp) points to a reference derived from the paper, allowing neighbor labels at phase boundaries."
}
```

## How you are scored
A hidden verifier reads your `phase_diagram.csv` and compares the phase label at a set of predefined $(E_g, \varepsilon_\perp)$ test points to a reference digitised from the original publication. A label is considered correct if it matches exactly, or if the point lies within one grid step of a phase boundary the neighbour label is also accepted. Additionally, the verifier checks that for each fixed $\varepsilon_\perp$ the sequence of phases as $E_g$ decreases (from positive to negative) follows the pattern expected from the physics: a normal insulator at large $E_g$ gives way first to a superfluid phase and then, in the inverted regime, to topological insulating phases with possible magnetic variants at weak screening. The reward is proportional to the fraction of test points correctly labelled, with bonuses for correct phase sequences. Full credit is awarded at $\ge 80\%$ accuracy. No auxiliary outputs are scored.
