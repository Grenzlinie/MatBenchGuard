# Si dangling bond and Si-Si bond defect energies in Si3N4 and Si3N4:O

## Problem background
Silicon nitride (Si₃N₄) and silicon dioxide (SiO₂) films are widely used as gate dielectrics and passivation layers. Native bonding defects — Si dangling bonds and Si—Si bonds — can introduce electronic states inside the band gap, which affect device performance by acting as charge traps or leakage paths. Understanding how the local chemical environment, in particular the presence of oxygen impurity atoms substituting for nitrogen in Si₃N₄ and nitrogen impurity atoms substituting for oxygen in SiO₂, shifts these defect-state energies is important for designing low‑defect deposited films.

## Approach
This reproduction uses a tight-binding cluster Bethe Lattice model. A Bethe lattice (no closed loops beyond the central cluster) represents the amorphous network. The electronic structure is obtained by a Green’s function recursion method applied to an sp³ tight-binding Hamiltonian, yielding the local density of states (LDOS).

First, a reference calculation on pure Si₃N₄ gives the average DOS and local DOS on each atom, from which the valence band top (Ev) is determined.

Then, four defect clusters are constructed:
- a Si dangling bond in pure Si₃N₄ (Si bonded to three N neighbours),
- a Si dangling bond in Si₃N₄:O (Si bonded to two N and one O neighbour),
- a Si—Si bond in pure Si₃N₄,
- a Si—Si bond in Si₃N₄:O.

For each configuration the LDOS on the defect Si atom(s) is computed, and the energy of the defect-related peak within the gap is recorded relative to Ev.

All tight-binding parameters are given below.

### Si₃N₄ and Si₃N₄:O
- Si: Es = −2.18 eV, Ep = 4.92 eV
- N:  Es′ = −14.2 eV, Ep′ = −5.2 eV
- Hopping integrals (eV): Vss′σ = −2.47, Vsp′σ = 4.76, Vs′pσ = 8.23, Vpp′σ = 4.67, Vpp′π = −1.21

For the oxygen‑alloyed case (Si₃N₄:O), the Si self‑energies are adjusted to:
- Si: Es = −1.77 eV, Ep = 5.33 eV
(the O self‑energies are the SiO₂ values: Es′ = −19.6 eV, Ep′ = −6.8 eV; O appears only as a neighbour to the defect Si).

### SiO₂ and SiO₂:N
- Si: Es = −0.55 eV, Ep = 6.55 eV
- O:  Es′ = −19.6 eV, Ep′ = −6.8 eV
- Hopping integrals (eV): Vss′σ = −2.85, Vsp′σ = 5.40, Vs′pσ = 9.50, Vpp′σ = 5.40, Vpp′π = −1.40

For the nitrogen‑alloyed case (SiO₂:N), the Si self‑energies are adjusted to:
- Si: Es = −0.96 eV, Ep = 6.14 eV
(the N impurity uses the N self‑energies from Si₃N₄: Es′ = −14.2 eV, Ep′ = −5.2 eV).

### Si—Si bonds
For Si—Si bonds in any host (Si₃N₄, Si₃N₄:O, SiO₂, SiO₂:N) the Si–Si hopping parameters are:
- Vss′σ = −1.94 eV, Vsp′σ = 1.75 eV, Vpp′σ = 3.05 eV, Vpp′π = −1.08 eV.
The Si self‑energies are those of the respective host (pure or alloyed).

### Dangling bonds
Si atoms carrying a dangling bond use the same self‑energies as in the corresponding host (pure or alloyed).

The defect energies obtained for all configurations reveal how near‑neighbour impurity atoms influence the gap‑state spectrum.

## Reproduction target
Produce a JSON file `defect_energies.json` at `/app/outputs/` containing the energies (in eV above the respective valence band top) of the defect‑induced peak in the LDOS for the eight defect configurations: Si dangling bond in Si₃N₄, Si dangling bond in Si₃N₄:O, Si—Si bond in Si₃N₄, Si—Si bond in Si₃N₄:O, Si dangling bond in SiO₂, Si dangling bond in SiO₂:N, Si—Si bond in SiO₂, and Si—Si bond in SiO₂:N. The keys must be exactly `Si_dangling_bond_Si3N4`, `Si_dangling_bond_Si3N4_O`, `Si_Si_bond_Si3N4`, `Si_Si_bond_Si3N4_O`, `Si_dangling_bond_SiO2`, `Si_dangling_bond_SiO2_N`, `Si_Si_bond_SiO2`, and `Si_Si_bond_SiO2_N`.

## Assets

- Python with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute reference electronic structure of pure Si₃N₄
- Role: process
- Action: Using the tight‑binding parameters for Si₃N₄ and the cluster Bethe Lattice model for the perfect network, compute the average density of states (DOS) and local DOS for each atom type. Determine the valence band top (Ev_Si3N4) from the computed DOS. This reference energy is required to place Si₃N₄ defect‑state energies on an absolute scale.
- Evidence: `/app/outputs/si3n4_reference_dos.json`

### Step 2: Compute reference electronic structure of pure SiO₂
- Role: process
- Action: Using the tight‑binding parameters for SiO₂ and the cluster Bethe Lattice model for the perfect network, compute the average density of states (DOS) and local DOS for each atom type. Determine the valence band top (Ev_SiO2) from the computed DOS. This reference energy is required to place SiO₂ defect‑state energies on an absolute scale.
- Evidence: `/app/outputs/sio2_reference_dos.json`

### Step 3: Compute defect state energies for Si dangling bond and Si—Si bond in Si₃N₄, Si₃N₄:O, SiO₂, and SiO₂:N
- Role: scored (load-bearing)
- Action: Construct cluster Bethe Lattice models for each defect configuration: (i) Si dangling bond in Si₃N₄ (Si with three N neighbours), (ii) Si dangling bond in Si₃N₄:O (Si with two N and one O neighbour), (iii) Si—Si bond in Si₃N₄, (iv) Si—Si bond in Si₃N₄:O, (v) Si dangling bond in SiO₂ (Si with three O neighbours), (vi) Si dangling bond in SiO₂:N (Si with two O and one N neighbour), (vii) Si—Si bond in SiO₂, (viii) Si—Si bond in SiO₂:N. Use the tight‑binding parameters from Table I, including the alloy‑adjusted Si self‑energies for Si₃N₄:O and SiO₂:N, and the Si—Si bond hopping parameters. For each configuration, compute the local density of states (LDOS) on the defect Si atom(s), identify the defect‑related peak within the band gap, and record its energy relative to the respective valence band top (Ev_Si3N4 for Si₃N₄‑based defects, Ev_SiO2 for SiO₂‑based defects). Write the eight energies (in eV) to defect_energies.json.
- Output file: `/app/outputs/defect_energies.json`
- Format: json
- Contract: JSON object with keys: 'Si_dangling_bond_Si3N4', 'Si_dangling_bond_Si3N4_O', 'Si_Si_bond_Si3N4', 'Si_Si_bond_Si3N4_O', 'Si_dangling_bond_SiO2', 'Si_dangling_bond_SiO2_N', 'Si_Si_bond_SiO2', 'Si_Si_bond_SiO2_N'. Each value is a floating‑point number (eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_energies.json
- path: `/app/outputs/defect_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Defect‑state energies (in eV above the respective valence band top) for the Si dangling bond and Si‑Si bond in pure and alloyed Si₃N₄ and SiO₂.
- schema:
  - `type`: object
  - `required`: `Si_dangling_bond_Si3N4`, `Si_dangling_bond_Si3N4_O`, `Si_Si_bond_Si3N4`, `Si_Si_bond_Si3N4_O`, `Si_dangling_bond_SiO2`, `Si_dangling_bond_SiO2_N`, `Si_Si_bond_SiO2`, `Si_Si_bond_SiO2_N`

Notes: The valence band references Ev_Si3N4 and Ev_SiO2 are obtained from the reference DOS calculations of the pure hosts. Only the Si₃N₄ and SiO₂ defect configurations are in scope; hydrogen‑related clusters are excluded because their tight‑binding parameters for H are not provided in the public paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Si_dangling_bond_Si3N4",
          "Si_dangling_bond_Si3N4_O",
          "Si_Si_bond_Si3N4",
          "Si_Si_bond_Si3N4_O",
          "Si_dangling_bond_SiO2",
          "Si_dangling_bond_SiO2_N",
          "Si_Si_bond_SiO2",
          "Si_Si_bond_SiO2_N"
        ]
      },
      "description": "Defect‑state energies (in eV above the respective valence band top) for the Si dangling bond and Si‑Si bond in pure and alloyed Si₃N₄ and SiO₂."
    }
  ],
  "notes": "The valence band references Ev_Si3N4 and Ev_SiO2 are obtained from the reference DOS calculations of the pure hosts. Only the Si₃N₄ and SiO₂ defect configurations are in scope; hydrogen‑related clusters are excluded because their tight‑binding parameters for H are not provided in the public paper."
}
```

## How you are scored
A hidden verifier will read your `defect_energies.json` and compare each energy value against predetermined reference values, applying tolerance margins appropriate for numerical tight-binding implementations. The verifier may also check that the set of energies exhibits physically self-consistent behaviour with respect to the alloying effect of oxygen. Your score is a weighted combination of these checks. Carrying out the required workflow steps and producing the evidence artifacts (including the reference DOS) is necessary; simply reporting numbers without executing the computation will not meet the scoring criteria.
