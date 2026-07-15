# Ab-initio SCF Energy and Properties of Pyrrole

## Problem background
Pyrrole is a five-membered aromatic heterocycle of significant chemical and biological interest. Accurate ab-initio quantum chemical calculations of its electronic structure provide benchmarks for approximate methods and aid in interpreting experimental spectra. Earlier studies employed relatively small basis sets, limiting the precision of computed energies, dipole moments, and orbital eigenvalues. This task reproduces a high-accuracy ab-initio calculation that uses a large Gaussian basis set and the experimentally determined microwave geometry to obtain these quantities. By carrying out the computation, you will determine the total electronic energy, dipole moment, and selected molecular orbital eigenvalues at a level of theory that greatly improves upon previous results.

## Approach
The method is an ab-initio LCAO-MO-SCF (Hartree–Fock) calculation on pyrrole. The molecular geometry is the precise microwave structure reported by Nygaard et al. (J. Mol. Struct. 3, 491 (1969)). A large Gaussian basis set is employed: for carbon and nitrogen, a 9s5p primitive set contracted to 4s2p using Dunning's contractions; for hydrogen, a 4s1p primitive set contracted to 3s1p, with the s-exponents scaled by 1.2 and a p-exponent of 0.80. The calculation starts from a symmetry‑adapted initial guess and iterates until the total energy converges to 3×10⁻⁷ a.u. or better. From the converged wavefunction, three properties are extracted: (1) the SCF total electronic energy, (2) the molecular dipole moment (magnitude and components in the principal axis system), and (3) the orbital eigenvalues of the highest occupied π orbitals of designated symmetries (1a₂, 2b₁, and 1b₁). These computed results can be compared with smaller-basis results and with experimental data.

## Reproduction target
The objective is to produce, from a single ab‑initio SCF calculation on pyrrole using the specified geometry and basis set, three output files:
- `total_energy.txt`: the total electronic energy in atomic units.
- `dipole_moment.txt`: the dipole moment magnitude and its components μ_a, μ_b, μ_c in Debye, each on a separate line.
- `homo_eigenvalues.json`: a JSON object with keys "1a2", "2b1", "1b1" and the corresponding orbital eigenvalues in atomic units.
You must run the SCF procedure to convergence and then extract these quantities from the converged wavefunction. The results will be compared against reference values for this computational protocol.

## Assets

- PySCF: pyscf
- Basis Set Exchange: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Perform SCF Calculation
- Role: process
- Action: Perform an ab-initio restricted Hartree-Fock SCF calculation on pyrrole using the experimental microwave geometry (Nygaard et al., J. Mol. Struct. 3, 491 (1969)) and the specified large Gaussian basis set (C,N: 9s5p -> 4s2p Dunning contractions; H: 4s1p -> 3s1p with s-exponents scaled by 1.2 and p-exponent 0.80) until the total energy converges to 3e-7 a.u. or better. Initialize with a symmetry-adapted guess.
- Evidence: `/app/outputs/scf_log.txt`

### Step 2: Total SCF Energy
- Role: scored (load-bearing)
- Action: From the converged SCF wavefunction, extract the total electronic energy (in atomic units) and write it to total_energy.txt.
- Output file: `/app/outputs/total_energy.txt`
- Format: txt
- Contract: A single line containing the floating-point number in atomic units (a.u.).
- Scoring: scored by hidden verifier

### Step 3: Dipole Moment
- Role: scored
- Action: From the converged SCF wavefunction, compute the molecular dipole moment magnitude and its components (μ_a, μ_b, μ_c) in the principal axis system and write to dipole_moment.txt.
- Output file: `/app/outputs/dipole_moment.txt`
- Format: txt
- Contract: Four lines: line1 magnitude (D), line2 μ_a component, line3 μ_b component, line4 μ_c component, each as a float.
- Scoring: scored by hidden verifier

### Step 4: HOMO Orbital Eigenvalues
- Role: scored
- Action: From the converged SCF wavefunction, extract the orbital eigenvalues for the highest occupied π molecular orbitals with symmetries 1a2, 2b1, and 1b1, and write to homo_eigenvalues.json.
- Output file: `/app/outputs/homo_eigenvalues.json`
- Format: json
- Contract: A JSON object with keys '1a2', '2b1', '1b1' (string labels) and float values representing orbital eigenvalues in a.u.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energy.txt`
- `/app/outputs/dipole_moment.txt`
- `/app/outputs/homo_eigenvalues.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energy.txt
- path: `/app/outputs/total_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: SCF total electronic energy of pyrrole, a single float in a.u.
- schema:
  - `type`: text
  - `units`: atomic units (a.u.)

### dipole_moment.txt
- path: `/app/outputs/dipole_moment.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Dipole moment magnitude and components of pyrrole in Debye.
- schema:
  - `type`: text
  - `required`: `magnitude`, `mu_a`, `mu_b`, `mu_c`
  - `units`: Debye (D)

### homo_eigenvalues.json
- path: `/app/outputs/homo_eigenvalues.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Orbital eigenvalues of the three highest occupied π molecular orbitals of pyrrole.
- schema:
  - `type`: object
  - `required`:
    - `1a2`: float (a.u.)
    - `2b1`: float (a.u.)
    - `1b1`: float (a.u.)
  - `items`: object
  - `units`: atomic units (a.u.)

Notes: All values are derived from a single SCF calculation. The dipole moment components are in the principal axis system.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "atomic units (a.u.)"
      },
      "description": "SCF total electronic energy of pyrrole, a single float in a.u."
    },
    {
      "file": "dipole_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": [
          "magnitude",
          "mu_a",
          "mu_b",
          "mu_c"
        ],
        "units": "Debye (D)"
      },
      "description": "Dipole moment magnitude and components of pyrrole in Debye."
    },
    {
      "file": "homo_eigenvalues.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "1a2": "float (a.u.)",
          "2b1": "float (a.u.)",
          "1b1": "float (a.u.)"
        },
        "items": {},
        "units": "atomic units (a.u.)"
      },
      "description": "Orbital eigenvalues of the three highest occupied π molecular orbitals of pyrrole."
    }
  ],
  "notes": "All values are derived from a single SCF calculation. The dipole moment components are in the principal axis system."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored output files. For each artifact, your submitted value is compared to a reference value derived from the literature for this identical geometry and basis set. Scoring uses fractional credit that decreases as the discrepancy grows beyond acceptable numerical tolerances; a value that meets or beats the reference threshold receives full credit. The verifier combines the per‑artifact scores (with weights that reflect their relative importance) into a single overall reward between 0.0 and 1.0. You do not need to match any specific published number—simply perform the calculation as specified and report the results accurately.
