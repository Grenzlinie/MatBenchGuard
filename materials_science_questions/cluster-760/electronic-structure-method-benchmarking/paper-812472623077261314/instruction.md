# Reproducing benchmark CCSD(T)/CBS binding energies for large noncovalent complexes

## Problem background
Accurate benchmark interaction energies for large noncovalent complexes are essential to validate and develop lower-cost computational methods (density functionals, semi-empirical methods, force-fields, machine-learning potentials) for biomolecular recognition, host-guest chemistry, and supramolecular assembly. The gold standard coupled cluster with single, double, and perturbative triple excitations [CCSD(T)] is widely relied upon for reliable reference noncovalent interactions, but its steep computational scaling with system size has hindered its application to systems beyond small molecules. Local correlation schemes—in particular the domain based local pair natural orbital (DLPNO) method—reduce the cost dramatically, making it feasible to approach CCSD(T) accuracy for large complexes. Nevertheless, benchmark CCSD(T) binding energies at the complete basis set (CBS) limit are still scarce for complexes with a hundred or more atoms. This task provides a route to obtain such benchmarks for nine prototypical large complexes: the seven dispersion-bound dimers of the L7 dataset, the DNA-ellipticine intercalation complex, and the buckycatcher‑C₆₀ host–guest complex, using a focal-point method that combines Hartree–Fock and second-order Møller–Plesset perturbation theory (MP2) at the CBS limit with a local coupled-cluster triples correction.

## Approach
The binding energy of each complex is built from three components computed with full counterpoise correction:
1. **HF/CBS** — the Hartree–Fock interaction energy at the CBS limit, obtained directly from a large basis set or via a two-point extrapolation.
2. **MP2 correlation/CBS** — the MP2 correlation contribution extrapolated to the CBS limit using a two-point inverse-power formula.
3. **ΔCCSD(T)/CBS** — a higher-order correlation correction beyond MP2, computed as the difference between the DLPNO‑CCSD(T₀) and MP2 correlation energies in a smaller basis set and extrapolated to the CBS limit. The DLPNO‑CCSD(T₀) calculations use the TightPNO threshold to control the local truncation error.

The final binding energy is the sum of (1), (2), and (3); for the buckycatcher‑C₆₀ complex a deformation-energy correction is also subtracted. Based on a systematic convergence study, the protocol prescribes different basis-set sequences and extrapolation exponents for the three families of complexes:
- L7 dimers: HF from aug‑cc‑pVQZ, MP2 correlation from a(T,Q)Z (β = 3), ΔCCSD(T) from heavy‑aug‑cc‑pVDZ / heavy‑aug‑cc‑pVTZ (β = 2.51) for the five smaller complexes and cc‑pVDZ / cc‑pVTZ (β = 3) for the two largest.
- DNA‑ellipticine: HF from heavy‑aug‑cc‑pVQZ, MP2 correlation from ha(T,Q)Z (β = 3), ΔCCSD(T) from (D,T)Z (β = 3).
- Buckeycatcher‑C₆₀: HF from jun‑cc‑pVQZ, MP2 correlation from ha(D,T)Z (β = 2.51), ΔCCSD(T) from (D,T)Z (β = 3).

All HF and MP2 calculations use the PSI4 quantum chemistry package; the DLPNO‑CCSD(T₀) calculations use ORCA with the TightPNO setting.

## Reproduction target
Compute the DLPNO‑CCSD(T₀)/CBS binding energies (in kcal/mol) for the following nine complexes by executing the workflow steps below:
- C2C2PD, C3A, C3GC, CBH, GCGC, GGG, PHE (the L7 dataset dimers)
- DNA‑ellipticine
- buckycatcher‑C60

Write the results to /app/outputs/binding_energies.json as a JSON object whose keys are the exact complex names listed above and whose values are the corresponding binding energies as floating-point numbers.

## Assets

- L7 dataset molecular geometries: https://www.begdb.com/
- Supplementary Material of the paper (J. Chem. Phys. 154, 154104): 10.1063/5.0042906
- PSI4 quantum chemistry package: https://psicode.org/
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Retrieve molecular geometries
- Role: process
- Action: Download the Cartesian coordinates for all L7 complexes from BEGDB or Sedlak et al. supplementary material, and for DNA-ellipticine and buckycatcher-C60 from the paper's supplementary material (DOI: 10.1063/5.0042906).
- Evidence: `/app/outputs/geometries_manifest.txt`

### Step 2: Compute HF/CBS binding energies
- Role: process
- Action: For each complex, perform counterpoise-corrected Hartree–Fock single‑point energy calculations using the recommended basis sets: aug‑cc‑pVQZ for L7, heavy‑aug‑cc‑pVQZ for DNA‑ellipticine, and jun‑cc‑pVQZ for buckycatcher‑C60. Compute the binding energy as E_complex − (E_monomer1 + E_monomer2). Use PSI4 or equivalent HF program.
- Evidence: `/app/outputs/hf_binding.json`

### Step 3: Compute MP2 correlation/CBS energies
- Role: process
- Action: For each complex, run counterpoise‑corrected MP2 calculations with the required basis pairs and extract correlation energies. Extrapolate to the complete basis set limit using the specified two‑point formulas with appropriate β exponents: a(T,Q)Z (β=3) for L7, ha(T,Q)Z (β=3) for DNA‑ellipticine, and ha(D,T)Z (β=2.51) for buckycatcher‑C60.
- Evidence: `/app/outputs/mp2_corr.json`

### Step 4: Compute ΔCCSD(T)/CBS correction
- Role: process
- Action: Run DLPNO‑CCSD(T₀) calculations with TightPNO threshold on the required basis sets and compute Δ = E_corr^{DLPNO‑CCSD(T₀)} − E_corr^{MP2} for each basis. Extrapolate Δ to CBS: ha(D,T)Z (β=2.51) for the five smaller L7 complexes; (D,T)Z (β=3) for the four larger complexes (C3A, C3GC, DNA‑ellipticine, buckycatcher‑C60).
- Evidence: `/app/outputs/delta_ccsdt.json`

### Step 5: Assemble and report final binding energies
- Role: scored
- Action: For each complex, compute the final DLPNO‑CCSD(T₀)/CBS binding energy as E_HF/CBS + E_corr_MP2/CBS + ΔCCSD(T)/CBS. For buckycatcher‑C60, also compute and include deformation energy. Write the resulting binding energies (kcal/mol) to /app/outputs/binding_energies.json.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"C2C2PD": float, "C3A": float, "C3GC": float, "CBH": float, "GCGC": float, "GGG": float, "PHE": float, "DNA-ellipticine": float, "buckycatcher-C60": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DLPNO-CCSD(T0)/CBS benchmark binding energies for seven L7 complexes, DNA-ellipticine, and buckycatcher-C60.
- schema:
  - `type`: object
  - `required`:
    - `C2C2PD`: number
    - `C3A`: number
    - `C3GC`: number
    - `CBH`: number
    - `GCGC`: number
    - `GGG`: number
    - `PHE`: number
    - `DNA-ellipticine`: number
    - `buckycatcher-C60`: number
  - `units`:
    - `C2C2PD`: kcal/mol
    - `C3A`: kcal/mol
    - `C3GC`: kcal/mol
    - `CBH`: kcal/mol
    - `GCGC`: kcal/mol
    - `GGG`: kcal/mol
    - `PHE`: kcal/mol
    - `DNA-ellipticine`: kcal/mol
    - `buckycatcher-C60`: kcal/mol

Notes: The hidden checker compares each entry to paper-reported gold values with tolerances (exact_match). All values must be negative for bound complexes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C2C2PD": "number",
          "C3A": "number",
          "C3GC": "number",
          "CBH": "number",
          "GCGC": "number",
          "GGG": "number",
          "PHE": "number",
          "DNA-ellipticine": "number",
          "buckycatcher-C60": "number"
        },
        "units": {
          "C2C2PD": "kcal/mol",
          "C3A": "kcal/mol",
          "C3GC": "kcal/mol",
          "CBH": "kcal/mol",
          "GCGC": "kcal/mol",
          "GGG": "kcal/mol",
          "PHE": "kcal/mol",
          "DNA-ellipticine": "kcal/mol",
          "buckycatcher-C60": "kcal/mol"
        }
      },
      "description": "DLPNO-CCSD(T0)/CBS benchmark binding energies for seven L7 complexes, DNA-ellipticine, and buckycatcher-C60."
    }
  ],
  "notes": "The hidden checker compares each entry to paper-reported gold values with tolerances (exact_match). All values must be negative for bound complexes."
}
```

## How you are scored
A hidden verifier reads your binding_energies.json and independently compares each binding energy against the expected reference value for that complex. Each entry is checked for closeness within a predetermined tolerance; the verifier also confirms that every binding energy is negative (bound complexes) and that the relative ordering among the complexes is consistent with the expected ordering. The final reward is the fraction of complexes that satisfy the tolerance, sign, and ordering criteria. No credit is awarded for intermediate artifacts; the binding energies carry the full score.
