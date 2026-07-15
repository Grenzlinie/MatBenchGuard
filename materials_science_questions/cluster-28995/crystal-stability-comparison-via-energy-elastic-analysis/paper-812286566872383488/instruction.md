# Tight-binding single-electron spectra for 13-atom clusters (fcc-like, hcp-like, icosahedral)

## Problem background
We consider three 13-atom clusters with distinct geometries: fcc‑like (cubo‑octahedral, O_h symmetry), hcp‑like (D_3h symmetry), and icosahedral (I_h symmetry). For such small systems, the electronic energy levels and their filling can strongly influence which atomic arrangement is preferred. This task implements a tight‑binding model with s and p valence orbitals on each atom to compute the single‑electron energy spectrum (eigenvalues and degeneracies) and, from it, the total electronic energy for various numbers of electrons per atom. The comparison of total energies among the three cluster types evaluates the electronic contribution to morphological stability, without including classical Lennard‑Jones contributions.

## Approach
Each cluster is described by the tight‑binding parameters:
- On‑site atomic energies ε_s, ε_p;
- Centre‑surface transfer integrals V_s, V_sp, V_p;
- For the icosahedral cluster only, additional surface–surface transfer integrals V_s′, V_sp′, V_p′.

Using the symmetry of each cluster we block‑diagonalize the Hamiltonian. The resulting sub‑matrices for each irreducible representation are given below. The golden ratio τ = (1+√5)/2 ≈ 1.6180.

All matrices are written with respect to LCAO basis functions ordered as: s‑orbitals first, then p‑orbitals. The diagonal entries contain the on‑site energies; off‑diagonal ones are scaled by the appropriate transfer integrals.

**fcc‑like cluster (O_h)**

A_1g (1 occurrence)
```
[[ε_s − 6 V_s,   0,               2 √3 V_sp],
 [0,            ε_s + 2 V_s,     2 V_sp],
 [2 √3 V_sp,    2 V_sp,          ε_p − V_p]]
```

A_2g (1 occurrence)
```
 ε_p − 2 V_p
```

E_g (2 occurrences)
```
[[ε_s + 2 V_s,   √3 V_sp,   V_sp],
 [√3 V_sp,       ε_p + V_p, 0],
 [V_sp,          0,         ε_p − V_p]]
```

T_1g (3 occurrences)
```
[[ε_p + τ V_p,   0            ],
 [0,             ε_p + τ_− V_p]]
```
with τ_− = (1−√5)/2 ≈ −0.6180.

T_2g (3 occurrences)
```
[[ε_s,               2 √((2+τ)/5) V_sp,  2 √((2+τ_−)/5) V_sp],
 [2 √((2+τ)/5) V_sp,  ε_p − τ V_p,        0                  ],
 [2 √((2+τ_−)/5) V_sp,0,                   ε_p − τ_− V_p      ]]
```

A_2u (1 occurrence)
```
 ε_p + V_p
```

E_u (2 occurrences)
```
 ε_p + V_p
```

T_1u (3 occurrences)
```
[[ε_s − 2 V_s,  2 V_sp,   √2 V_sp,   √2 V_sp,   √2 V_sp],
 [2 V_sp,       ε_p,      V_p,        −V_p,       −√2 V_p],
 [√2 V_sp,       V_p,      ε_p+√2 V_p, 0,         0     ],
 [√2 V_sp,      −V_p,       0,        ε_p−√2 V_p, 0     ],
 [√2 V_sp,      −√2 V_p,   0,         0,         ε_p−V_p]]
```

T_2u (3 occurrences)
```
[[ε_s + 2 V_s,   √2 V_sp,   0],
 [√2 V_sp,       ε_p + V_p, 0],
 [0,             0,         ε_p]]
```

**hcp‑like cluster (D_3h)**

The matrices contain decimal coefficients that are exact algebraic roots of certain polynomials; here they are given to four decimal places. The numerical values –1.8539, –1.4058, –0.9288, 0.6885 are roots of 24x^4+84x^3+66x^2−35x−40 = 0 (for A_1′). Other roots come from similar equations specified below.

A_1′ (1 occurrence)
```
[[ε_s−6 V_s,   0,               0,               0,               0,              0,              0              ],
 [0,           ε_s,             0,               0,               0,              0,              0              ],
 [0,           0,               ε_s+2 V_s,       0,               0,              0,              0              ],
 [−0.8122 V_sp,−1.0225 V_sp,    0.1883 V_sp,    ε_p−1.8539 V_p,  0,              0,              0              ],
 [ 1.3078 V_sp,−1.3293 V_sp,   −0.5003 V_sp,    0,               ε_p−1.4058 V_p, 0,              0              ],
 [ 3.1233 V_sp, 0.2403 V_sp,    1.9364 V_sp,    0,               0,              ε_p−0.9288 V_p, 0              ],
 [−0.0116 V_sp,−1.1386 V_sp,    0.0796 V_sp,    0,               0,              0,              ε_p+0.6885 V_p  ]]
```

A_2′ (1 occurrence)
```
[[ε_s+2 V_s,    0.0382 V_sp,  1.3385 V_sp,  0.4549 V_sp],
 [0.0382 V_sp,   ε_p−0.0280 V_p, 0,           0],
 [1.3385 V_sp,   0,            ε_p+0.9320 V_p, 0],
 [0.4549 V_sp,   0,            0,             ε_p+1.5960 V_p]]
```
The p‑state secular equation is 24x³−60x²+34x+1=0.

E′ (2 occurrences)
```
[[ε_s−2.0861 V_s, 0,               0,               0,               0,            0,            0,            0,            0,            0,            0,            0              ],
 [0,              ε_s+0.5720 V_s,  0,               0,               0,            0,            0,            0,            0,            0,            0,            0              ],
 [0,              0,               ε_s+2.5141 V_s,  0,               0,            0,            0,            0,            0,            0,            0,            0              ],
 [−1.2432 V_sp,   −0.6101 V_sp,    0.5700 V_sp,     ε_p−2.5178 V_p, 0,            0,            0,            0,            0,            0,            0,            0              ],
 [ 0.5020 V_sp,    1.1432 V_sp,    0.5377 V_sp,     0,               ε_p−1.3444 V_p,0,            0,            0,            0,            0,            0,            0              ],
 [−0.5749 V_sp,    0.1617 V_sp,    0.1303 V_sp,     0,               0,            ε_p−0.7640 V_p,0,            0,            0,            0,            0,            0              ],
 [ 0.8931 V_sp,   −1.0855 V_sp,    0.9727 V_sp,     0,               0,            0,            ε_p+0.3788 V_p,0,            0,            0,            0,            0              ],
 [−0.2520 V_sp,    0.1922 V_sp,   −0.3135 V_sp,     0,               0,            0,            0,            ε_p+0.6627 V_p,0,            0,            0,            0              ],
 [−0.8891 V_sp,   −0.5516 V_sp,   −1.3739 V_sp,     0,               0,            0,            0,            0,            ε_p+0.8718 V_p,0,            0,            0              ],
 [ 0.5938 V_sp,   −0.1863 V_sp,    0.7576 V_sp,     0,               0,            0,            0,            0,            0,            ε_p+1.0224 V_p,0,            0              ],
 [−1.9660 V_sp,    0.6624 V_sp,   −0.0216 V_sp,     0,               0,            0,            0,            0,            0,            0,            ε_p+2.1905 V_p, 0]            ]
```
The s‑secular equation is x³−x²−5x+3=0; the p‑secular equation is 576x⁸−288x⁷−4512x⁶+3480x⁵+7176x⁴−7298x³−1523x²+3125x−730=0.

A_1″ (1 occurrence)
```
[[ε_p+ (3+√105)V_p/12,  0],
 [0,                    ε_p+ (3−√105)V_p/12]]
```

A_2″ (1 occurrence)
```
[[ε_s−2 V_s,     2.5163 V_sp,  0.1123 V_sp,  0.8844 V_sp,  1.5937 V_sp],
 [2.5163 V_sp,   ε_p−2.4884 V_p, 0,            0,            0],
 [0.1123 V_sp,    0,            ε_p−1.7448 V_p, 0,            0],
 [0.8844 V_sp,    0,            0,            ε_p+0.5671 V_p, 0],
 [1.5937 V_sp,    0,            0,            0,            ε_p+2.1661 V_p]]
```
The p‑secular equation is 24x⁴+84x³+66x²−35x−4=0.

E″ (2 occurrences)
```
[[ε_s+V_s,    1.0882 V_sp,  0.7834 V_sp,  0.3300 V_sp,  1.4956 V_sp,  0.1522 V_sp],
 [1.0882 V_sp, ε_p−1.4175 V_p, 0,         0,            0,            0],
 [0.7834 V_sp,  0,          ε_p−1.1014 V_p, 0,            0,            0],
 [0.3300 V_sp,  0,          0,          ε_p+0.3253 V_p, 0,            0],
 [1.4956 V_sp,  0,          0,          0,            ε_p+1.0947 V_p, 0],
 [0.1522 V_sp,  0,          0,          0,            0,            ε_p+1.5990 V_p]]
```
The p‑secular equation is 36x⁵−18x⁴−123x³+48x²+96x−32=0.

**Icosahedral cluster (I_h)**

For this cluster the surface–surface transfer integrals are distinguished by a prime. Two choices for the ratio will be evaluated: V′ = V (identical) and V′ = √0.8 V = 0.8944 V.

A_g (1 occurrence)
```
[[ε_s,          √12 V_s,           √12 V_sp],
 [√12 V_sp,     ε_s − 5 V_s′,      √(15−5τ) V_sp′],
 [√12 V_sp,     √(15−5τ) V_sp′,    ε_p + (τ−3) V_p′]]
```

T_1g (3 occurrences)
```
 ε_p + (1+τ/2) V_p′
```

G_g (4 occurrences)
```
 ε_p
```

H_g (5 occurrences)
```
[[ε_s+V_s′,            √(3+τ) V_sp′,                      0              ],
 [√(3+τ) V_sp′,        ε_p + (6−7τ)V_p′/11,              3√(60+18τ) V_p′/22],
 [0,                   3√(60+18τ) V_p′/22,                ε_p + (3τ−12)V_p′/22]]
```

T_1u (3 occurrences)
```
[[ε_s − (2τ−1) V_s′,   2 V_sp,                √(7+τ) V_sp′,                0                     ],
 [2 V_sp,              ε_p,                  2√((5−2τ)/11) V_p,           2√((6+2τ)/11) V_p     ],
 [√(7+τ) V_sp′,        2√((5−2τ)/11) V_p,   ε_p + (16−13τ)V_p′/11,        √2 (15+5τ) V_p′/22    ],
 [0,                   2√((6+2τ)/11) V_p,    √2 (15+5τ) V_p′/22,          ε_p + (15τ−10)V_p′/22]]
```

T_2u (3 occurrences)
```
[[ε_s + (2τ−1) V_s′,   √(3−τ) V_sp′],
 [√(3−τ) V_sp′,        ε_p + (τ−1) V_p′]]
```

G_u (4 occurrences)
```
 ε_p − τ V_p′
```

H_u (5 occurrences)
```
 ε_p + τ V_p′ /2
```

We examine two limiting parameter regimes:
1. **Separation limit** – |ε_p − ε_s| ≫ max(|V_s|,|V_sp|,|V_p|) so that s and p levels do not mix. Within this limit we first solve only the s‑submatrices (treating p‑states as decoupled) and then the p‑submatrices separately.
2. **s‑p hybridization limit** – ε_p = ε_s, V_p = √3 V_sp = 3 V_s > 0 (sp³ hybridization). All submatrices are diagonalised together.

For the icosahedral cluster we additionally repeat the calculations for the two choices of surface–surface integrals mentioned above.

## Reproduction target
Produce the single‑electron energy eigenvalues λ, their degeneracies m, and (when available from the eigenvector analysis) the squared amplitude |ψ(0)|² of the central atom for:
- the s‑derived levels in the separation limit (energy measured as ε_s + λ V_s),
- the p‑derived levels in the separation limit (energy measured as ε_p + λ V_p),
- all levels in the hybridization limit (energy measured as ε_s + λ V_s).

The data must be generated for the three cluster geometries (fcc‑like, hcp‑like, icosahedral) and, for the icosahedral cluster, for both surface transfer integral ratios V′=V and V′=√0.8 V. Save these results in the three JSON files exactly as described in the steps.

Afterwards, use the obtained level schemes to compute the total electronic energy for each cluster and each V′ ratio at integer electron numbers per atom n_e. Fill the single‑particle levels with electrons observing spin degeneracy (2 electrons per orbital). Consider:
- for the separation limit, n_e = 1,…,5 for the s‑level scheme and n_e = 1,…,5 for the p‑level scheme (totalling 10 cases),
- for the hybridization limit, n_e = 1,…,7.
For each n_e, sum the lowest occupied eigenvalues to obtain the total electronic energy, and record which cluster yields the lowest energy. Output these values and the stability ordering in the total_energies.json file.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Build Hamiltonian submatrices
- Role: process
- Action: Using the atomic orbital basis (s and p) and the tight-binding parameters (atomic energy levels ε_s, ε_p; transfer integrals V_s, V_sp, V_p for centre-surface, and for the icosahedral cluster the surface-surface V_s', V_sp', V_p'), construct the block-diagonalized Hamiltonian submatrices for each irreducible representation for the three 13-atom clusters: fcc-like (O_h symmetry), hcp-like (D_{3h} symmetry), and icosahedral (I_h symmetry). The explicit matrix forms are derived from the point group decompositions given in standard group-theoretical tight-binding approach; implement them directly without relying on pre-computed numeric constants.
- Evidence: none

### Step 2: Compute s-level eigenvalues for separation limit
- Role: scored
- Action: Set |ε_p-ε_s| >> max(|V_s|,|V_sp|,|V_p|) so that no s-p hybridization occurs. For each cluster and the two icosahedral surface-surface transfer integral ratios (V'=V and V'=√0.8 V), solve the secular equations from the s-submatrices. Output the eigenvalues λ (energy = ε_s + λ V_s), degeneracies m, and squared central-atom amplitude |ψ(0)|² where available.
- Output file: `/app/outputs/separation_limit_s_levels.json`
- Format: json
- Contract: {"type": "object", "properties": {"fcc": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "hcp": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "icosahedron_VequalV": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "icosahedron_Vsqrt_0_8V": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}
- Scoring: scored by hidden verifier

### Step 3: Compute p-level eigenvalues for separation limit
- Role: scored
- Action: Same separation limit; solve the secular equations for the p-submatrices. Output eigenvalues λ (energy = ε_p + λ V_p), degeneracies m, and |ψ(0)|² where given.
- Output file: `/app/outputs/separation_limit_p_levels.json`
- Format: json
- Contract: {"type": "object", "properties": {"fcc": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "hcp": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "icosahedron_VequalV": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "icosahedron_Vsqrt_0_8V": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}
- Scoring: scored by hidden verifier

### Step 4: Compute eigenvalues for s-p hybridization limit
- Role: scored
- Action: Set ε_p = ε_s, V_p = √3 V_sp = 3 V_s > 0 (sp³ hybridization limit). Solve the secular equations for all submatrices for each cluster and both V' ratios. Output eigenvalues λ (energy = ε_s + λ V_s), degeneracies m, and |ψ(0)|².
- Output file: `/app/outputs/hybridization_limit_levels.json`
- Format: json
- Contract: {"type": "object", "properties": {"fcc": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "hcp": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "icosahedron_VequalV": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "icosahedron_Vsqrt_0_8V": {"type": "array", "items": {"type": "object", "properties": {"lambda": {"type": "number"}, "psi_sq": {"type": ["number", "null"]}, "m": {"type": "integer"}}, "required": ["lambda", "psi_sq", "m"]}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}
- Scoring: scored by hidden verifier

### Step 5: Compute total electronic energies and stability ordering
- Role: scored (load-bearing)
- Action: For each electron count per atom (n_e = 1,…,5 for separation limit s-only and p-only cases; n_e = 1,…,7 for hybridization limit), fill the single-particle levels from the computed eigenvalues using spin degeneracy (2 electrons per level). Sum the lowest 13·n_e eigenvalues to obtain the total electronic energy for each cluster and V' choice. Report the total energies and denote which cluster has the lowest energy for each n_e.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: {"type": "object", "properties": {"separation_limit": {"type": "object", "properties": {"s1": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "p1": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "2": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "3": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "4": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "5": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}}, "required": ["s1", "p1", "2", "3", "4", "5"]}, "hybridization_limit": {"type": "object", "properties": {"1": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "2": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "3": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "4": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "5": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "6": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}, "7": {"type": "object", "properties": {"fcc": {"type": "number"}, "hcp": {"type": "number"}, "icosahedron_VequalV": {"type": "number"}, "icosahedron_Vsqrt_0_8V": {"type": "number"}}, "required": ["fcc", "hcp", "icosahedron_VequalV", "icosahedron_Vsqrt_0_8V"]}}, "required": ["1", "2", "3", "4", "5", "6", "7"]}}, "required": ["separation_limit", "hybridization_limit"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/separation_limit_s_levels.json`
- `/app/outputs/separation_limit_p_levels.json`
- `/app/outputs/hybridization_limit_levels.json`
- `/app/outputs/total_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### separation_limit_s_levels.json
- path: `/app/outputs/separation_limit_s_levels.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single-electron energy levels of s-derived states in the separation limit. Each entry contains the eigenvalue lambda (scaled by V_s), the squared central-atom amplitude psi_sq if available (null otherwise), and the degeneracy m.
- schema:
  - `type`: object
  - `required`:
    - `fcc`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `hcp`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `icosahedron_VequalV`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `icosahedron_Vsqrt_0_8V`: array of {lambda: number, psi_sq: number|null, m: integer}

### separation_limit_p_levels.json
- path: `/app/outputs/separation_limit_p_levels.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single-electron energy levels of p-derived states in the separation limit. Values scaled by V_p.
- schema:
  - `type`: object
  - `required`:
    - `fcc`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `hcp`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `icosahedron_VequalV`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `icosahedron_Vsqrt_0_8V`: array of {lambda: number, psi_sq: number|null, m: integer}

### hybridization_limit_levels.json
- path: `/app/outputs/hybridization_limit_levels.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single-electron energy levels in the s-p hybridization limit. Values scaled by V_s.
- schema:
  - `type`: object
  - `required`:
    - `fcc`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `hcp`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `icosahedron_VequalV`: array of {lambda: number, psi_sq: number|null, m: integer}
    - `icosahedron_Vsqrt_0_8V`: array of {lambda: number, psi_sq: number|null, m: integer}

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total electronic energies for each cluster and electron count, and the resulting most stable configuration for each case. The ordering of which cluster has the lowest energy is also verified.
- schema:
  - `type`: object
  - `required`:
    - `separation_limit`: object with keys s1, p1, 2, 3, 4, 5, each containing an object with keys fcc, hcp, icosahedron_VequalV, icosahedron_Vsqrt_0_8V (number)
    - `hybridization_limit`: object with keys 1..7, each containing an object with keys fcc, hcp, icosahedron_VequalV, icosahedron_Vsqrt_0_8V (number)

Notes: The classical Lennard-Jones energy minimization and group-theoretical derivation of the Hamiltonian matrices are not required outputs; the agent must implement the given explicit matrices. The figures are not evaluated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "separation_limit_s_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "fcc": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "hcp": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "icosahedron_VequalV": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "icosahedron_Vsqrt_0_8V": "array of {lambda: number, psi_sq: number|null, m: integer}"
        }
      },
      "description": "Single-electron energy levels of s-derived states in the separation limit. Each entry contains the eigenvalue lambda (scaled by V_s), the squared central-atom amplitude psi_sq if available (null otherwise), and the degeneracy m."
    },
    {
      "file": "separation_limit_p_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "fcc": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "hcp": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "icosahedron_VequalV": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "icosahedron_Vsqrt_0_8V": "array of {lambda: number, psi_sq: number|null, m: integer}"
        }
      },
      "description": "Single-electron energy levels of p-derived states in the separation limit. Values scaled by V_p."
    },
    {
      "file": "hybridization_limit_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "fcc": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "hcp": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "icosahedron_VequalV": "array of {lambda: number, psi_sq: number|null, m: integer}",
          "icosahedron_Vsqrt_0_8V": "array of {lambda: number, psi_sq: number|null, m: integer}"
        }
      },
      "description": "Single-electron energy levels in the s-p hybridization limit. Values scaled by V_s."
    },
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "separation_limit": "object with keys s1, p1, 2, 3, 4, 5, each containing an object with keys fcc, hcp, icosahedron_VequalV, icosahedron_Vsqrt_0_8V (number)",
          "hybridization_limit": "object with keys 1..7, each containing an object with keys fcc, hcp, icosahedron_VequalV, icosahedron_Vsqrt_0_8V (number)"
        }
      },
      "description": "Total electronic energies for each cluster and electron count, and the resulting most stable configuration for each case. The ordering of which cluster has the lowest energy is also verified."
    }
  ],
  "notes": "The classical Lennard-Jones energy minimization and group-theoretical derivation of the Hamiltonian matrices are not required outputs; the agent must implement the given explicit matrices. The figures are not evaluated."
}
```

## How you are scored
A hidden verifier inspects your four JSON artifacts. It compares each eigenvalue λ, degeneracy m, and (where applicable) the central‑atom amplitude |ψ(0)|² against reference values with an appropriate numerical tolerance. Total electronic energies are similarly compared to reference values, and the ordering of which cluster has the lowest energy at each electron count is checked for correctness. Each step carries a weight; the final reward is a weighted combination of the scores across the artifacts. Reporting the paper’s numbers without having solved the secular equations will not produce acceptable agreement with the reference data.
