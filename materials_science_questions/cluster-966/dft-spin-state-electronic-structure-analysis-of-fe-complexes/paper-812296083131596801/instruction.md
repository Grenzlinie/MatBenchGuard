# Ab initio SCF study of Fischer-type Cr carbene: equilibrium geometry, bond energy, rotational barrier, and charge distribution

## Problem background
Fischer-type metal carbene complexes are central intermediates in many organometallic reactions, including olefin metathesis and catalytic processes. Understanding the electronic structure and bonding of the metal–carbon double bond is fundamental to explaining their stability and reactivity. The chromium pentacarbonyl carbene complex (CO)₅Cr=CH(OH) is a prototypical system for investigating the nature of this bond. Key quantitative characteristics include the equilibrium Cr=C bond length, the bond dissociation energy, the rotational barrier (which reflects the degree of double-bond character), and the charge distribution between the metal and the carbene ligand. Determining these quantities by ab initio quantum chemistry provides insight into the σ-donation/π-back-donation mechanism that governs the metal–carbene interaction.

## Approach
The reproduction uses ab initio restricted Hartree–Fock (RHF) calculations with minimal basis sets: the MINI‑2 basis for chromium and the 3G contraction for carbon, oxygen, and hydrogen. The molecular geometry of (CO)₅Cr=CH(OH) is assembled from standard bond lengths and angles: the Cr–C(O) distances are 1.87 Å (used for both trans and cis carbonyl ligands), the C≡O bond length within the carbonyl groups is 1.13 Å, and the carbene fragment CH(OH) is planar with C–O = 1.33 Å, C–H = 1.09 Å, O–H = 0.96 Å, and bond angles of approximately 120°. The Cr=C distance is varied to locate the equilibrium value, and the dihedral angle θ describing rotation about the Cr=C bond is scanned while the carbene plane is held fixed. The total energies of the isolated fragments (CO)₅Cr and CH(OH) in their singlet states are computed at the same level to obtain the bond dissociation energy Dₑ = E(Cr fragment) + E(CHOH fragment) – E(complex at equilibrium). Mulliken population analysis at the equilibrium geometry yields the gross atomic charges on Cr and on the carbene carbon. All calculations are carried out with the open‑source quantum chemistry package PySCF, which provides RHF routines and Mulliken analysis. The workflow is organized into three stages: fragment SCF calculations, geometry scans with population analysis, and extraction of the target properties from the raw data.

## Reproduction target
Reproduce the four quantitative descriptors of the Cr=C double bond in (CO)₅Cr=CH(OH): (i) equilibrium Cr=C bond length (Å); (ii) bond dissociation energy to singlet fragments (kcal/mol); (iii) rotational barrier around the Cr=C bond (kcal/mol); and (iv) Mulliken gross atomic charges on Cr and on the carbene carbon (electron units). These results must be written to `/app/outputs/results.json` with the keys specified in the output contract.

## Assets

- PySCF: pyscf
- MINI-2 basis set for Cr (Tatewaki–Huzinaga): 10.1063/1.438926
- 3G minimal basis for C, O, H (Tavouktsoglou–Huzinaga): 10.1063/1.441811

## Workflow steps

### Step 1: Fragment SCF calculations
- Role: process
- Action: Perform RHF/SCF single-point calculations on the singlet-state fragments (CO)5Cr and CH(OH) using the specified molecular geometries and the basis sets (MINI-2 for Cr, 3G for C, O, H). Record the total energies of both fragments.
- Evidence: `/app/outputs/fragment_energies.json`

### Step 2: Complex geometry scans and Mulliken population analysis
- Role: process
- Action: Run RHF/SCF calculations on the chromium carbene complex (CO)5Cr=CH(OH) at a series of Cr=C distances (e.g., 1.8–2.2 Å) with the rotational angle fixed at 0°, and at a series of rotational angles (0–90°) at the equilibrium distance, using the same basis sets. Save the total energy at each geometry. At the equilibrium geometry also perform Mulliken population analysis and record the gross atomic charges on Cr and the carbene carbon.
- Evidence: `/app/outputs/scan_data.json`

### Step 3: Extract equilibrium properties
- Role: scored (load-bearing)
- Action: From the scan data and the fragment energies, determine the equilibrium Cr=C bond length (energy minimum in the distance scan), the bond dissociation energy (Dₑ = E((CO)5Cr, singlet) + E(CH(OH), singlet) − E(complex at equilibrium), all evaluated at the respective minima/basis sets), the rotational barrier (ΔE = maximum − minimum from the rotational scan), and the Mulliken gross atomic charges on Cr and the carbene carbon at the equilibrium geometry. Write these quantities to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"equilibrium_bond_length_angstrom": <float>, "bond_dissociation_energy_kcal_mol": <float>, "rotational_barrier_kcal_mol": <float>, "gross_atomic_charge_Cr": <float>, "gross_atomic_charge_C_carb": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reproduced key quantitative properties of the Cr=C double bond: equilibrium bond length, bond dissociation energy (to singlet fragments), rotational barrier, and Mulliken gross atomic charges on Cr and carbene carbon, as computed by ab initio SCF with minimal basis sets.
- schema:
  - `type`: object
  - `required`:
    - `equilibrium_bond_length_angstrom`: float
    - `bond_dissociation_energy_kcal_mol`: float
    - `rotational_barrier_kcal_mol`: float
    - `gross_atomic_charge_Cr`: float
    - `gross_atomic_charge_C_carb`: float
  - `units`:
    - `equilibrium_bond_length_angstrom`: angstrom
    - `bond_dissociation_energy_kcal_mol`: kcal/mol
    - `rotational_barrier_kcal_mol`: kcal/mol
    - `gross_atomic_charge_Cr`: electron charge
    - `gross_atomic_charge_C_carb`: electron charge

Notes: The hidden checker compares each numeric field in results.json to the corresponding paper-reported value, applying tolerances appropriate for a re-implementation of the same method with a different software package.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "equilibrium_bond_length_angstrom": "float",
          "bond_dissociation_energy_kcal_mol": "float",
          "rotational_barrier_kcal_mol": "float",
          "gross_atomic_charge_Cr": "float",
          "gross_atomic_charge_C_carb": "float"
        },
        "units": {
          "equilibrium_bond_length_angstrom": "angstrom",
          "bond_dissociation_energy_kcal_mol": "kcal/mol",
          "rotational_barrier_kcal_mol": "kcal/mol",
          "gross_atomic_charge_Cr": "electron charge",
          "gross_atomic_charge_C_carb": "electron charge"
        }
      },
      "description": "Reproduced key quantitative properties of the Cr=C double bond: equilibrium bond length, bond dissociation energy (to singlet fragments), rotational barrier, and Mulliken gross atomic charges on Cr and carbene carbon, as computed by ab initio SCF with minimal basis sets."
    }
  ],
  "notes": "The hidden checker compares each numeric field in results.json to the corresponding paper-reported value, applying tolerances appropriate for a re-implementation of the same method with a different software package."
}
```

## How you are scored
A hidden verifier compares each numeric field in your `results.json` to undisclosed reference values, using tolerances appropriate for an independent re‑implementation of the same method with a different software package. Each field carries a weight, and the final reward is a weighted combination of the individual accuracies; partial credit is possible. The verifier does not inspect your intermediate data, only the final `results.json`. You must genuinely execute the calculations to obtain the numbers; simply fabricating the output will not be detected by the comparison mechanism but defeats the purpose of the task.
