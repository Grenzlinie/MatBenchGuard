PHYSICAL REVIEW B **102**, 165424 (2020)

# Dynamical stability of two-dimensional metals in the periodic table

Shota Ono*
Department of Electrical, Electronic and Computer Engineering, Gifu University, Gifu 501-1193, Japan

![](./images/817400400226287619_1.jpg)
(Received 13 July 2020; revised 22 September 2020; accepted 14 October 2020; published 27 October 2020)

We study the dynamical stability of two-dimensional (2D) metals from Li to Pb in the periodic table. Using a first-principles approach, we calculate the phonon band structure of 2D metals that have planar hexagonal (HX), buckled honeycomb (bHC), and buckled square (bSQ) lattice structures. The bHC and bSQ are dynamically stable structures for most transition metals, whereas the HX and bHC are dynamically stable structures for alkali earth and noble metals. Thin films thicker than bHC and bSQ are dynamically stable for group 5 elements and indium. We demonstrate that the trend in the dynamical stability of 2D metals is correlated with that of three-dimensional (3D) metals. This provides design principles of ordered alloys: 2D metals are building blocks for constructing 3D alloys, where the similarity regarding the dynamical stability of different 2D metals is important for creating dynamically stable alloys.

DOI: 10.1103/PhysRevB.102.165424

## I. INTRODUCTION

To determine the crystal structure, the Bravais lattice with a basis, is a key ingredient in studying the properties of condensed matters [1,2]. From a point of view of computational materials science, this enables us to predict various properties of solids by using first-principles approach. However, it is not trivial to determine the crystal structure given the chemical composition of solids because many metastable structures (i.e., dynamically stable but not the ground state structure) exist in the potential energy surface. Also elemental metals in the periodic table have metastable structures: While most elemental metals have either the face-centered cubic (FCC), body-centered cubic (BCC), or hexagonal closed-packed (HCP) structures as its ground state, some elemental metals in a different structure are also dynamically stable [3]. Such a metastability in elemental metals has been renewed interest from both fundamental and practical points of view [4–8].

Recently, two-dimensional (2D) materials that consist of a few atomic layers have attracted significant interest because of the structural properties. Graphene has honeycomb (HC) structure with zero thickness [9]. In contrast, other 2D elements in group 14 have buckled HC (bHC) as a dynamically stable structure [10,11]. For example, silicene (Si), germanene (Ge), and stanene (Sn) have a total thickness of 0.45, 0.69, and 0.85 Å, respectively [11]. This is attributed to the fact that the bonding in the bulk prefers $sp^3$ to $sp^2$ character, producing the diamond structure but not the graphite-like structure. While these have HC or bHC structures, others can have another stable structures, such as the planar hexagonal (HX), square (SQ), and more complex geometries. For example, 2D allotropes of noble metals (Cu [12], Ag [13], and Au [14]), borophene (B) [15,16] and gallenene (Ga) [17] in group 13, pentagraphene in group 14 [18], phosphorene (P) [19], arsenene (As) [20], antimonene (Sb) [20], and bismuthene (Bi) [21] in group 15, and poloniumene (Po) in group 16 [22] have been proposed theoretically and/or created experimentally. Note that B and Ga require external strains (or substrate) to be stabilized.

It is interesting to investigate what is the metastable structures of 2D metals. Since elemental metals tend to have close packed structures in three-dimensional (3D) space, they would have HX or similar close packed structures. Recently, the stability of elemental 2D metals have been investigated by calculating the total energy within the density-functional theory (DFT) [23,24]. In fact, the planar HX [23] and bHC structures [24] have been proposed as stable structures. However, the dynamical stability of 2D metals has not been studied.

In this paper, we calculate the phonon band structure of elemental metals, from Li to Pb in the periodic table, in the monolayer structures (the planar HX, the bHC, and the buckled SQ (bSQ) structures) by using DFT and density-functional perturbation theory (DFPT). We show that most elemental metals are dynamically stable in the monolayer structures, that is, no imaginary phonon frequencies are observed within the first Brillouin zone. Based on this, we discuss the relationship of the dynamical stability between these 2D and 3D metals, where an atomically thin layer having the HX and SQ lattice structures can be a building block for constructing 3D crystals. This concept can be applied to a material design for dynamically stable alloys. As an example, we demonstrate how the dynamical stability of ordered AlCu and CuZn alloys is related to that of 2D metals.

Some exceptions are obtained: V, Nb, Ta, and In in the buckled structures are dynamically unstable, whereas those with thicker structures that are termed the 3HX or 3SQ in the present study, where three layers of the planar HX or SQ lattices are stacked along the direction perpendicular to the 2D plane, are dynamically stable. In the present paper, the thicker structures as well as monolayers are included to 2D metals.

*shota_o@gifu-u.ac.jp

2469-9950/2020/102(16)/165424(14)
165424-1
©2020 American Physical Society

For 2D Cs, Ba, Tl, and Ga, no stable structures are found at zero temperature and pressure.

The rest of paper is organized as follows. Section II describes computational details for DFT and DFPT calculations. Section III discusses the energetic and dynamical stabilities of 2D metals. The stability relationship between 2D and 3D metals and its application to prediction of ordered alloy structures are also discussed. Conclusion and future perspectives are presented in Sec. IV. The phonon dispersion relations in 2D metals are provided in Appendix A.

## II. COMPUTATIONAL DETAILS

We calculate the total energies of 2D metals based on DFT implemented in QUANTUM ESPRESSO (QE) code [25]. In the present study, we use the GGA-PBE functional [26] because it can describe various equilibrium properties of solid such as total energy, lattice constants, vibrational properties, and magnetic properties. We also use the GGA-PBEsol functional [27] because it improves surface energies that are small in the GGA-PBE functional [28]. We use the ultrasoft pseudopotentials generated by the scheme of Ref. [29], i.e., `pslibrary.1.0.0`. For Na, Mn, and Tc, `pslibrary.0.2`, `pslibrary.0.3.1`, and `pslibrary.0.3.0` are used, respectively. Spin-polarized (sp) calculations are performed for Cr, Mn, Fe, Co, and Ni only. The cutoff energies for the wavefunction and the charge density are 80 and 800 Ry, respectively, which are well above the suggested cutoff energies. The self-consistent field (scf) calculations are performed by using $30×30×1$ $k$ grid for 2D metals and $15×15×15$ $k$ grid for 3D alloys [30]. The primitive lattice vectors in units of the lattice constant $a$ are $(1,0,0)$, $(-1/2, \sqrt{3}/2, 0)$, and $(0, 0, c/a)$ for HX, bHC, and 3HX structures, and $(1,0,0)$, $(0,1,0)$, and $(0, 0, c/a)$ for bSQ and 3SQ structures. The size of $c$ is fixed to be $14$ Å, which is large enough to avoid spurious interactions between 2D layers in different unit cells. The Marzari-Vanderbilt smearing [31] with a broadening of $\sigma = 0.02$ Ry is used for all calculations.

The cohesive energy of the structure $j$ is defined as $E_j = \varepsilon_{\text{atom}} - \varepsilon_j$, where $\varepsilon_{\text{atom}}$ is the total energy of an atom in free space and $\varepsilon_j$ is the total energy per atom of the structure $j = $ HX, bHC, and bSQ. During the geometry optimization for the structure $j$, the total energy and forces are converged within $10^{-5}$ Ry and $10^{-4}$ a.u., respectively. The value of $\varepsilon_{\text{atom}}$ for all atoms is obtained from atom-in-a-box calculations (within non-spin-polarized (nsp) approximation) of a single atom in a unit cell with a volume of $15×15×15$ Å$^3$.

The dynamical stability of 2D metals is studied by performing the phonon band structure calculations within the DFPT [32] implemented in QE code [25]. For HX and bHC structures, $8×8×1$ $q$ grid (10 $q$ points) is used, while for bSQ structure, $6×6×1$ $q$ grid (10 $q$ points) is used. For 3HX and 3SQ structures, $6×6×1$ $q$ grid (7 and 10 $q$ points, respectively) is used. In cases of bHC W, bSQ W, and anti-ferromagnetic phase of HX Cr and Mn, the size of $q$ grid is decreased to $6×6×1$, $4×4×1$, and $4×2×1$, respectively, in order to reduce the computational costs. For AlCu and CuZn alloys, $4×4×4$ $q$ grid is used. The phonon energy is defined by $E_p = \text{sgn}(\omega^2)\hbar|\omega|$, where $\text{sgn}$ is the sign function, $\hbar$ is the Planck constant, and $\omega$ is the phonon frequency obtained by diagonalizing the dynamical matrix. $E_p$ is negative when $\omega$ is an imaginary number. If $E_p$ is positive over the entire Brillouin zone for an element in the structure $j$, such a structure is dynamically stable.

We note that monolayers studied in the present work have no electron energy gap around the Fermi level except Hg, which is checked by calculating the electron density-of-states for HX, bHC, and bSQ structures. The HX, bHC, and bSQ Hg have the energy gap of about 1 eV within GGA-PBE. The HX Hg has the energy gap of 0.4 eV, while the bHC and bSQ Hg have no energy gap within GGA-PBEsol. It has been known that many-body correction for the electron correlation energy is important to reproduce the bulk properties of Hg [33]. It is desirable to study the stability of 2D Hg beyond DFT approach. It is useful to note that bHC Sn obtained in the present study is a metal, while stanene is a Dirac-type semiconductor without spin-orbit coupling [11]. This implies that the former and the latter are 2D analogues of white tin having metallic phase and gray tin having semiconducting phase, respectively.

Throughout this paper below, we discuss the dynamical stability of 2D metals and 3D alloys based on the GGA-PBE calculation results. It would be valuable to note that the dynamically stable structures obtained from the GGA-PBEsol calculations are almost the same as those obtained from the GGA-PBE calculations. The differences are as follows: Within GGA-PBEsol, HX K and 3HX Tl are dynamically stable, while bSQ Cu, HX Au, bHC Au, and bSQ Hg are unstable. We have not studied the dynamical stability of Nb and Tc because no GGA-PBEsol potentials are available.

## III. RESULTS AND DISCUSSION

### A. Buckling effect

First, we demonstrate that the buckled structures become more energetically stable than the planar structure by calculating the potential energy surface. The unit cell of the bHC structure includes two atoms, whose positions are given by $(0, 0, +\delta)$ and $(0, a/\sqrt{3}, -\delta)$ with the lattice constant $a$ and the buckling height $\delta$ [see Fig. 1(b)]. Figure 1(a) shows the total energy variation as a function of $\delta$ and $a$ for 2D Ag, where the total energy is minimum when $\delta = 0.0$ Å and $a \simeq 4.6$ Å and when $\delta \simeq 1.2$ Å and $a \simeq 2.8$ Å. The local minimum of the former and the latter corresponds to the planar HC and bHC structures, respectively. The bHC is more stable than the planar HC and HX structures by 716 and 164 meV/atom, respectively. We also consider the bSQ structure with two atoms included in a unit cell, where the positions of atoms are given by $(0, 0, +\delta)$ and $(a/2, a/2, -\delta)$, as shown in Fig. 1(d). We plot the total energy as a function of $\delta$ and $a$ for 2D Ag in Fig. 1(c). The two local minimum correspond to the planar SQ and the bSQ structures. The values of $a$ in the bHC and bSQ structures are close to the nearest-neighbor (NN) interatomic distance in FCC Ag (2.89 Å).

Motivated by this fact, we set the initial guess of $a$ to the NN interatomic distance $d_{3\text{D}}$ in 3D metals [34] and optimize the geometry of the HX, bSQ, and bHC structures from Li to Pb in the periodic table. In addition, the initial guess of $\delta$ is set to $0.3d_{3\text{D}}$ for bHC and bSQ structures. The optimized

![](./images/817400400226287619_2.jpg)

FIG. 1. (a) The total energy variation as a function of $a$ and $\delta$ and (b) top and side views for the bHC structures of Ag. [(c) and (d)] Same as (a) and (b), respectively, but for the bSQ structure. The unit cell is enclosed by red lines. The layer thickness is equal to $2\delta$.

$\delta$s are distributed around $0.4d_{3D}$. Table I lists $E_j$ and the optimized parameters ($a_j$ and $\delta_j$) for $j = \text{HX}$, bHC, and bSQ, where the values of $\delta_{\text{HX}}$ that are equal to zero are omitted. For most elements, the bHC structure is the most energetically stable structure, while for Cr, Mo, Nb, Ti, V, W, and Zr (i.e., group 4, 5, and 6 metals except Hf and Ta), the bSQ is more stable than the bHC structure. Note that for bHC Mo, bHC W, and bSQ Mn, the initial guess of $\delta = 0.3d_{3D}$ leads to a highly buckled structure that is found to be dynamically unstable, as in silicene and germanene [10]. In these cases, we set $\delta = 0.1d_{3D}$ as an initial guess to yield a low-buckled structure that is dynamically stable as shown in Appendix A. The cohesive energies of the low-buckled structures are smaller than those of the high-buckled structures by 218, 597, and $-39$ meV/atom, respectively, in Mo, W, and Mn. The parameters for the low-buckled structure are listed in Table I.

Figures 2(a), 2(b), and 2(c) summarize the atomic number $Z$ dependence of $E_j$, $a_j$, and $\delta_j$ ($j = \text{HX}$, bHC, and bSQ), respectively. The period $X$ from two to six in the periodic table is indicated. Within the same period, an increase in $E_j$ is observed with an increase in $Z$, shown in Fig. 2(a). Except $X = 2$ and 3, this is followed by a decrease in $E_j$. Such non-monotonic behaviors are due to the presence of $d$ electrons, which have also been predicted in Ref. [23]. Mn, Tc, and Re in the group 7 have the largest $E_j$ in the same period. The $a_j$ and $\delta_j$ show opposite tendency with $Z$, as shown in Figs. 2(b) and 2(c), respectively: $a_j$ and $\delta_j$ have the minimum when $E_j$ is maximum in the same period. We stress in Fig. 2 that for all $j$s trends in the energetic stability are present with $Z$. Thus we expect that several properties of 2D metals can behave in a similar way, providing trend in the dynamical stability of elements as well. This will be demonstrated below.

### B. Metastability

In Table I, the dynamically stable structures are indicated by underlying the corresponding $E_j$. If the HX structure is dynamically stable, the bHC structure is also dynamically stable. This is because the bHC and HX structures belong to the same valley in the potential energy surface, as shown in Fig. 1(a). It is noteworthy that for Ag, Be, Ca, Cd, Mg, Rb, and Sr, the HX and bSQ structures are dynamically stable and unstable, respectively, although the size of $E_{\text{bSQ}}$ is larger than that of $E_{\text{HX}}$. Similarly, for Cr, Mo, and W, the bHC and bSQ structures are dynamically stable and unstable, respectively, although the size of $E_{\text{bSQ}}$ is larger than that of $E_{\text{bHC}}$. The unstable bSQ must be transformed into a lower-energy structure. In the present case, the imaginary frequencies are observed in the ZA phonons along the $\Gamma$-$X$ direction (see Appendi A). This means that the bSQ structure is unstable against the out-of-plane vibrations that can cause a structural transformation into a thicker structure. The latter would be more energetically stable as well as dynamically stable. This will be demonstrated below for V, Nb, Ta, and In.

![](./images/817400400226287619_3.jpg)

FIG. 2. The $Z$ dependence of (a) $E_j$, (b) $a_j$, and (c) $\delta_j$ for $j = \text{HX}$, bHC, and bSQ. The figure $X(=2,3,4,5$, and $6)$ indicates the period in the periodic table.

The phonon band structures from Li to Pb in the periodic table for (a) HX, (b) bHC, and (c) bSQ structures are shown in Appendix A. Figure 3 summarizes the dynamical stability of 2D metals, where the stability behaviors are similar in the same group in the periodic table. First, we focus on group 2 (Be, Mg, Ca, and Sr), group 11 (Cu, Ag, and Au), group 12 (Zn and Cd), and Rb that are dynamically stable in the HX structure. In order to understand why the HX structure is dynamically stable in these elements, we plot the cohesive

<table>
<caption>Table 1. $E_j$ (eV/atom), $a_j$ (Å), and $\delta_j$ (Å) for $j = \text{HX}$, $\text{bHC}$, and $\text{bSQ}$. “nsp” and “sp” in the parenthesis indicate the non-spin-polarized and spin-polarized calculations, respectively. The largest cohesive energy in an element is shown in bold. Among three structures, the dynamically stable structures are indicated by underlying the corresponding cohesive energies.</caption>
<thead>
<tr>
<th>
</th>
<th>
$E_{\text{HX}}$
</th>
<th>
$a_{\text{HX}}$
</th>
<th>
$E_{\text{bHC}}$
</th>
<th>
$a_{\text{bHC}}$
</th>
<th>
$\delta_{\text{bHC}}$
</th>
<th>
$E_{\text{bSQ}}$
</th>
<th>
$a_{\text{bSQ}}$
</th>
<th>
$\delta_{\text{bSQ}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
Ag
</td>
<td>
2.144
</td>
<td>
2.794
</td>
<td>
2.307
</td>
<td>
2.855
</td>
<td>
1.239
</td>
<td>
2.201
</td>
<td>
2.802
</td>
<td>
1.082
</td>
</tr>
<tr>
<td>
Al
</td>
<td>
2.842
</td>
<td>
2.682
</td>
<td>
3.217
</td>
<td>
2.748
</td>
<td>
1.227
</td>
<td>
3.085
</td>
<td>
2.713
</td>
<td>
1.088
</td>
</tr>
<tr>
<td>
Au
</td>
<td>
2.845
</td>
<td>
2.748
</td>
<td>
2.897
</td>
<td>
2.773
</td>
<td>
1.442
</td>
<td>
2.722
</td>
<td>
2.756
</td>
<td>
1.143
</td>
</tr>
<tr>
<td>
Ba
</td>
<td>
1.203
</td>
<td>
4.467
</td>
<td>
1.593
</td>
<td>
4.493
</td>
<td>
1.763
</td>
<td>
1.547
</td>
<td>
4.339
</td>
<td>
1.609
</td>
</tr>
<tr>
<td>
Be
</td>
<td>
2.997
</td>
<td>
2.126
</td>
<td>
3.354
</td>
<td>
2.157
</td>
<td>
0.959
</td>
<td>
3.181
</td>
<td>
2.090
</td>
<td>
0.799
</td>
</tr>
<tr>
<td>
Ca
</td>
<td>
1.181
</td>
<td>
3.866
</td>
<td>
1.584
</td>
<td>
3.924
</td>
<td>
1.503
</td>
<td>
1.530
</td>
<td>
3.792
</td>
<td>
1.340
</td>
</tr>
<tr>
<td>
Cd
</td>
<td>
0.487
</td>
<td>
2.922
</td>
<td>
0.642
</td>
<td>
2.950
</td>
<td>
1.489
</td>
<td>
0.505
</td>
<td>
2.938
</td>
<td>
1.378
</td>
</tr>
<tr>
<td>
Co (nsp)
</td>
<td>
5.028
</td>
<td>
2.302
</td>
<td>
5.902
</td>
<td>
2.379
</td>
<td>
0.975
</td>
<td>
5.619
</td>
<td>
2.366
</td>
<td>
0.821
</td>
</tr>
<tr>
<td>
Co (sp)
</td>
<td>
5.463
</td>
<td>
2.355
</td>
<td>
6.178
</td>
<td>
2.441
</td>
<td>
0.974
</td>
<td>
5.901
</td>
<td>
2.397
</td>
<td>
0.874
</td>
</tr>
<tr>
<td>
Cr (nsp)
</td>
<td>
6.440
</td>
<td>
2.340
</td>
<td>
7.388
</td>
<td>
2.788
</td>
<td>
0.716
</td>
<td>
7.411
</td>
<td>
2.280
</td>
<td>
1.053
</td>
</tr>
<tr>
<td>
Cr (sp)
</td>
<td>
6.735
</td>
<td>
2.690
</td>
<td>
7.388
</td>
<td>
2.788
</td>
<td>
0.716
</td>
<td>
7.411
</td>
<td>
2.280
</td>
<td>
1.053
</td>
</tr>
<tr>
<td>
Cs
</td>
<td>
0.554
</td>
<td>
5.385
</td>
<td>
0.635
</td>
<td>
5.213
</td>
<td>
2.110
</td>
<td>
0.626
</td>
<td>
5.250
</td>
<td>
2.031
</td>
</tr>
<tr>
<td>
Cu
</td>
<td>
3.154
</td>
<td>
2.428
</td>
<td>
3.407
</td>
<td>
2.496
</td>
<td>
1.063
</td>
<td>
3.280
</td>
<td>
2.468
</td>
<td>
0.912
</td>
</tr>
<tr>
<td>
Fe (nsp)
</td>
<td>
5.780
</td>
<td>
2.287
</td>
<td>
6.903
</td>
<td>
2.400
</td>
<td>
0.927
</td>
<td>
6.496
</td>
<td>
2.377
</td>
<td>
0.800
</td>
</tr>
<tr>
<td>
Fe (sp)
</td>
<td>
6.314
</td>
<td>
2.405
</td>
<td>
6.903
</td>
<td>
2.400
</td>
<td>
0.927
</td>
<td>
6.893
</td>
<td>
2.391
</td>
<td>
0.969
</td>
</tr>
<tr>
<td>
Ga
</td>
<td>
2.261
</td>
<td>
2.749
</td>
<td>
2.516
</td>
<td>
2.822
</td>
<td>
1.298
</td>
<td>
2.497
</td>
<td>
2.683
</td>
<td>
1.225
</td>
</tr>
<tr>
<td>
Hf
</td>
<td>
4.850
</td>
<td>
2.919
</td>
<td>
6.091
</td>
<td>
3.152
</td>
<td>
1.140
</td>
<td>
6.082
</td>
<td>
3.051
</td>
<td>
0.999
</td>
</tr>
<tr>
<td>
Hg
</td>
<td>
0.093
</td>
<td>
3.534
</td>
<td>
0.128
</td>
<td>
3.553
</td>
<td>
1.471
</td>
<td>
0.123
</td>
<td>
3.574
</td>
<td>
1.249
</td>
</tr>
<tr>
<td>
In
</td>
<td>
1.912
</td>
<td>
3.162
</td>
<td>
2.165
</td>
<td>
3.226
</td>
<td>
1.459
</td>
<td>
2.136
</td>
<td>
3.069
</td>
<td>
1.382
</td>
</tr>
<tr>
<td>
Ir
</td>
<td>
6.948
</td>
<td>
2.564
</td>
<td>
7.739
</td>
<td>
2.662
</td>
<td>
1.101
</td>
<td>
7.312
</td>
<td>
2.663
</td>
<td>
0.908
</td>
</tr>
<tr>
<td>
K
</td>
<td>
0.700
</td>
<td>
4.527
</td>
<td>
0.810
</td>
<td>
4.636
</td>
<td>
1.901
</td>
<td>
0.787
</td>
<td>
4.430
</td>
<td>
1.763
</td>
</tr>
<tr>
<td>
Li
</td>
<td>
1.311
</td>
<td>
3.091
</td>
<td>
1.561
</td>
<td>
3.102
</td>
<td>
1.159
</td>
<td>
1.538
</td>
<td>
2.960
</td>
<td>
1.085
</td>
</tr>
<tr>
<td>
Lu
</td>
<td>
2.595
</td>
<td>
3.338
</td>
<td>
3.533
</td>
<td>
3.433
</td>
<td>
1.320
</td>
<td>
3.434
</td>
<td>
3.419
</td>
<td>
1.103
</td>
</tr>
<tr>
<td>
Mg
</td>
<td>
0.952
</td>
<td>
3.058
</td>
<td>
1.241
</td>
<td>
3.087
</td>
<td>
1.354
</td>
<td>
1.106
</td>
<td>
3.046
</td>
<td>
1.174
</td>
</tr>
<tr>
<td>
Mn (nsp)
</td>
<td>
6.322
</td>
<td>
2.296
</td>
<td>
7.437
</td>
<td>
2.447
</td>
<td>
0.921
</td>
<td>
7.119
</td>
<td>
2.618
</td>
<td>
0.604
</td>
</tr>
<tr>
<td>
Mn (sp)
</td>
<td>
6.871
</td>
<td>
2.573
</td>
<td>
7.437
</td>
<td>
2.447
</td>
<td>
0.921
</td>
<td>
7.119
</td>
<td>
2.618
</td>
<td>
0.604
</td>
</tr>
<tr>
<td>
Mo
</td>
<td>
7.931
</td>
<td>
2.597
</td>
<td>
8.879
</td>
<td>
3.102
</td>
<td>
0.808
</td>
<td>
8.907
</td>
<td>
2.553
</td>
<td>
1.138
</td>
</tr>
<tr>
<td>
Na
</td>
<td>
0.937
</td>
<td>
3.659
</td>
<td>
1.064
</td>
<td>
3.681
</td>
<td>
1.519
</td>
<td>
1.036
</td>
<td>
3.519
</td>
<td>
1.404
</td>
</tr>
<tr>
<td>
Nb
</td>
<td>
7.122
</td>
<td>
2.700
</td>
<td>
7.865
</td>
<td>
3.187
</td>
<td>
0.907
</td>
<td>
8.157
</td>
<td>
2.663
</td>
<td>
1.179
</td>
</tr>
<tr>
<td>
Ni (nsp)
</td>
<td>
4.164
</td>
<td>
2.338
</td>
<td>
4.769
</td>
<td>
2.408
</td>
<td>
1.020
</td>
<td>
4.573
</td>
<td>
2.377
</td>
<td>
0.874
</td>
</tr>
<tr>
<td>
Ni (sp)
</td>
<td>
4.253
</td>
<td>
2.355
</td>
<td>
4.827
</td>
<td>
2.425
</td>
<td>
1.010
</td>
<td>
4.614
</td>
<td>
2.397
</td>
<td>
0.867
</td>
</tr>
<tr>
<td>
Os
</td>
<td>
8.202
</td>
<td>
2.553
</td>
<td>
9.510
</td>
<td>
2.681
</td>
<td>
1.034
</td>
<td>
8.861
</td>
<td>
2.698
</td>
<td>
0.850
</td>
</tr>
<tr>
<td>
Pb
</td>
<td>
2.795
</td>
<td>
3.305
</td>
<td>
3.139
</td>
<td>
3.535
</td>
<td>
1.322
</td>
<td>
3.129
</td>
<td>
3.428
</td>
<td>
1.195
</td>
</tr>
<tr>
<td>
Pd
</td>
<td>
2.847
</td>
<td>
2.631
</td>
<td>
3.407
</td>
<td>
2.701
</td>
<td>
1.175
</td>
<td>
3.238
</td>
<td>
2.658
</td>
<td>
1.024
</td>
</tr>
<tr>
<td>
Pt
</td>
<td>
5.082
</td>
<td>
2.611
</td>
<td>
5.391
</td>
<td>
2.695
</td>
<td>
1.205
</td>
<td>
5.150
</td>
<td>
2.650
</td>
<td>
1.040
</td>
</tr>
<tr>
<td>
Rb
</td>
<td>
0.619
</td>
<td>
4.925
</td>
<td>
0.715
</td>
<td>
4.974
</td>
<td>
2.051
</td>
<td>
0.692
</td>
<td>
4.754
</td>
<td>
1.903
</td>
</tr>
<tr>
<td>
Re
</td>
<td>
8.633
</td>
<td>
2.573
</td>
<td>
10.057
</td>
<td>
2.724
</td>
<td>
1.033
</td>
<td>
9.498
</td>
<td>
2.944
</td>
<td>
0.672
</td>
</tr>
<tr>
<td>
Rh
</td>
<td>
4.643
</td>
<td>
2.551
</td>
<td>
5.569
</td>
<td>
2.634
</td>
<td>
1.092
</td>
<td>
5.265
</td>
<td>
2.620
</td>
<td>
0.923
</td>
</tr>
<tr>
<td>
Ru
</td>
<td>
6.321
</td>
<td>
2.528
</td>
<td>
7.592
</td>
<td>
2.663
</td>
<td>
1.015
</td>
<td>
7.147
</td>
<td>
2.668
</td>
<td>
0.845
</td>
</tr>
<tr>
<td>
Sc
</td>
<td>
2.706
</td>
<td>
3.149
</td>
<td>
3.619
</td>
<td>
3.283
</td>
<td>
1.199
</td>
<td>
3.553
</td>
<td>
3.218
</td>
<td>
1.038
</td>
</tr>
<tr>
<td>
Sn
</td>
<td>
3.010
</td>
<td>
3.137
</td>
<td>
3.353
</td>
<td>
3.315
</td>
<td>
1.300
</td>
<td>
3.339
</td>
<td>
3.196
</td>
<td>
1.195
</td>
</tr>
<tr>
<td>
Sr
</td>
<td>
0.966
</td>
<td>
4.249
</td>
<td>
1.332
</td>
<td>
4.287
</td>
<td>
1.653
</td>
<td>
1.279
</td>
<td>
4.138
</td>
<td>
1.480
</td>
</tr>
<tr>
<td>
Ta
</td>
<td>
6.963
</td>
<td>
2.729
</td>
<td>
8.102
</td>
<td>
2.811
</td>
<td>
1.266
</td>
<td>
8.089
</td>
<td>
2.712
</td>
<td>
1.121
</td>
</tr>
<tr>
<td>
Tc
</td>
<td>
7.583
</td>
<td>
2.538
</td>
<td>
8.931
</td>
<td>
2.710
</td>
<td>
1.008
</td>
<td>
8.530
</td>
<td>
2.894
</td>
<td>
0.677
</td>
</tr>
<tr>
<td>
Ti
</td>
<td>
4.450
</td>
<td>
2.674
</td>
<td>
5.469
</td>
<td>
2.933
</td>
<td>
1.030
</td>
<td>
5.536
</td>
<td>
2.795
</td>
<td>
0.930
</td>
</tr>
<tr>
<td>
Tl
</td>
<td>
1.649
</td>
<td>
3.318
</td>
<td>
1.849
</td>
<td>
3.375
</td>
<td>
1.527
</td>
<td>
1.819
</td>
<td>
3.214
</td>
<td>
1.467
</td>
</tr>
<tr>
<td>
V
</td>
<td>
5.845
</td>
<td>
2.445
</td>
<td>
6.654
</td>
<td>
2.885
</td>
<td>
0.806
</td>
<td>
6.874
</td>
<td>
2.401
</td>
<td>
1.067
</td>
</tr>
<tr>
<td>
W
</td>
<td>
8.212
</td>
<td>
2.632
</td>
<td>
9.157
</td>
<td>
3.089
</td>
<td>
0.850
</td>
<td>
9.223
</td>
<td>
2.602
</td>
<td>
1.117
</td>
</tr>
<tr>
<td>
Y
</td>
<td>
2.779
</td>
<td>
3.424
</td>
<td>
3.672
</td>
<td>
3.567
</td>
<td>
1.346
</td>
<td>
3.590
</td>
<td>
3.493
</td>
<td>
1.168
</td>
</tr>
<tr>
<td>
Zn
</td>
<td>
0.862
</td>
<td>
2.538
</td>
<td>
1.039
</td>
<td>
2.569
</td>
<td>
1.308
</td>
<td>
0.817
</td>
<td>
2.537
</td>
<td>
1.194
</td>
</tr>
<tr>
<td>
Zr
</td>
<td>
5.096
</td>
<td>
2.918
</td>
<td>
6.059
</td>
<td>
3.203
</td>
<td>
1.166
</td>
<td>
6.112
</td>
<td>
3.016
</td>
<td>
1.077
</td>
</tr>
</tbody>
</table>

<table>
  <thead>
    <tr>
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>Li<br>bHC<br>-<br>BCC</td>
      <td>Be<br>HX<br>-<br>HCP</td>
      <td colspan="4">Symbol<br>2D HX structure<br>2D SQ structure<br>3D structure</td>
      <td colspan="4">HX = hexagonal<br>bHC = buckled honeycomb<br>3HX = 3-layered hexagonal<br>bSQ = buckled square<br>3SQ = 3-layered square<br>FCC = face-centered cubic<br>BCC = body-centered cubic<br>SC = simple cubic</td>
      <td colspan="2">CUB = cubic<br>TET = tetragonal<br>ORC = orthorhombic<br>HCP = hexagonal closed packed<br>DIA = diamond<br>RHL = rhombohedral</td>
      <td>B<br>stripe<br>TET</td>
      <td>C<br>HC<br>graphite</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Na<br>bHC<br>-<br>BCC</td>
      <td>Mg<br>HX<br>-<br>HCP</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Al<br>bHC<br>(bSQ)<br>FCC</td>
      <td>Si<br>bHC<br>DIA</td>
      <td>P<br>bHC<br>CUB</td>
      <td></td>
    </tr>
    <tr>
      <td>4</td>
      <td>K<br>bHC<br>-<br>BCC</td>
      <td>Ca<br>HX<br>-<br>FCC</td>
      <td>Sc<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Ti<br>-<br>bSQ<br>HCP</td>
      <td>V<br>-<br>3SQ<br>BCC</td>
      <td>Cr<br>bHC<br>-<br>BCC</td>
      <td>Mn<br>bHC<br>(bSQ)<br>CUB</td>
      <td>Fe<br>bHC<br>-<br>BCC</td>
      <td>Co<br>bHC<br>-<br>HCP</td>
      <td>Ni<br>bHC<br>(bSQ)<br>FCC</td>
      <td>Cu<br>HX<br>(bSQ)<br>FCC</td>
      <td>Zn<br>HX<br>-<br>HCP</td>
      <td>Ga<br>-<br>-<br>ORC</td>
      <td>Ge<br>-<br>DIA</td>
      <td>As<br>bHC<br>RHL</td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Rb<br>HX<br>-<br>BCC</td>
      <td>Sr<br>HX<br>-<br>FCC</td>
      <td>Y<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Zr<br>-<br>bSQ<br>HCP</td>
      <td>Nb<br>-<br>3SQ<br>BCC</td>
      <td>Mo<br>bHC<br>-<br>BCC</td>
      <td>Tc<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Ru<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Rh<br>bHC<br>(bSQ)<br>FCC</td>
      <td>Pd<br>bHC<br>(bSQ)<br>FCC</td>
      <td>Ag<br>HX<br>-<br>FCC</td>
      <td>Cd<br>HX<br>-<br>HCP</td>
      <td>In<br>3HX<br>-<br>TET</td>
      <td>Sn<br>bHC<br>-<br>TET</td>
      <td>Sb<br>bHC<br>RHL</td>
      <td></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Cs<br>-<br>-<br>BCC</td>
      <td>Ba<br>-<br>-<br>BCC</td>
      <td>Lu<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Hf<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Ta<br>-<br>3SQ<br>BCC</td>
      <td>W<br>bHC<br>-<br>BCC</td>
      <td>Re<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Os<br>bHC<br>(bSQ)<br>HCP</td>
      <td>Ir<br>bHC<br>(bSQ)<br>FCC</td>
      <td>Pt<br>bHC<br>(bSQ)<br>FCC</td>
      <td>Au<br>HX<br>-<br>FCC</td>
      <td>Hg<br>-<br>bSQ<br>RHL</td>
      <td>Tl<br>-<br>-<br>HCP</td>
      <td>Pb<br>bHC<br>(bSQ)<br>FCC</td>
      <td>Bi<br>bHC<br>RHL</td>
      <td>Po<br>SQ<br>SC</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2">(i) HX</td>
      <td colspan="3">(ii) bHC</td>
      <td colspan="4">(iii) bSQ</td>
      <td colspan="3">(iv) 3HX or 3SQ</td>
      <td colspan="4">(v) No stable 2D structures at zero temperature and pressure</td>
    </tr>
  </tbody>
</table>

FIG. 3. Periodic table for elemental 2D materials. The present results are colored. The stable 2D structures are indicated (The structure in parenthesis indicates the metastable phase). If the HX structure is dynamically stable, the bHC structure is also stable. Stable crystal structures in 3D materials are from Ref. [1]. The previously investigated structures that have dynamical stability include semiconductors of C [9], Si, Ge, and Sn [11], P [19], and As and Sb [20], and metals of Cu [12], Ag [13], Au [14], B [15,16], Ga [17], Bi [21], and Po [22].

energy difference between the bHC and HX structures $(E_{\text{bHC}} - E_{\text{HX}})$ as a function of $E_{\text{HX}}$ in Fig. 4. There is a tendency that the larger $E_{\text{HX}}$, the larger the energy difference. The elements that we consider are indicated by filled symbols: Be, Mg, Ca, Sr, and Rb (circle), Cu, Ag, and Au (square), and Zn and Cd (diamond). Due to small energy differences less than 400 meV, these can be isolated as a monolayer. Among them, HX Au has the lowest value (52 meV), which is larger than the total energy difference between bilayer and monolayer graphene (less than 20 meV) [35].

![](./images/817400400226287619_4.jpg)

FIG. 4. The cohesive energy difference between $E_{\text{bHC}}$ and $E_{\text{HX}}$ as a function of $E_{\text{HX}}$. The calculated data for the elements that are dynamically stable in the HX structure are plotted by filled symbols.

We study the stability of the group 2 (Be, Mg, Ca, and Sr) and group 11 (Cu, Ag, and Au) metals from another aspect. These are classified into divalent and monovalent metals having two and one $s$ electrons in the outermost shell, respectively. Since the distribution of the $s$ electron is spherically symmetric around the nucleus, the densely packed HX structure with no buckling is realized. In this sense, it is strange that the HX structure is unstable in alkali metals (Li, Na, and K).

Next, we focus on transition metals, most of which are dynamically stable in the bHC structure. In transition metals, the electronic states around the Fermi level consist of a mixture of $s$ and $p$ ($d$) electrons. Such a hybridized orbital is less spherical symmetry, creating the buckled structures, as realized in group 14 semiconductors (Si and Ge) [10]. With respect to the stability, the trivalent metal of Al is similar to transition metals rather than free electron metals (Na and K). Ti and Zr are anomalous in that those in the bHC and bSQ structures are dynamically unstable and stable, respectively.

In cases that the HX, bHC, and bSQ structures are unstable (i.e., V, Nb, Ta, Ga, In, and Tl), we examine the dynamical stability of thicker films in the 3HX and 3SQ structures. The positions of atoms are $(0, 0, 0)$, and $(0, a/\sqrt{3}, \pm 2\delta)$ for 3HX and $(0, 0, 0)$, and $(a/2, a/2, \pm 2\delta)$ for 3SQ structures in a unit cell described in Sec. II. Figures 5 and 6 show the phonon band structures of group 5 metals (V, Nb, and Ta) and group 13 metals (Ga, In, and Tl), respectively: left for 3HX and right for 3SQ structures. For group 5 metals, the 3SQ structure is dynamically stable, while the 3HX structure

![](./images/817400400226287619_5.jpg)

FIG. 5. The phonon band structures of group 5 metals of V, Nb, and Ta: (left) 3HX and (right) 3SQ structures.

is unstable. For group 13 metals, the 3HX In is dynamically stable only. The cohesive energy $E_{\text{tri}}$ (eV), the optimized lattice constant $a$ (Å), and the interlayer distance $2\delta$ (Å) for 3SQ V, 3SQ Nb, 3SQ Ta, and 3HX In are as follows: $(E_{\text{tri}}, a, 2\delta) = (6.947, 2.886, 1.404)$, $(8.209, 3.256, 1.471)$, $(8.195, 3.258, 1.469)$, and $(2.223, 3.315, 2.768)$. It should be emphasized that the magnitude of $E_{\text{tri}}$ is larger than those of

![](./images/817400400226287619_6.jpg)

FIG. 6. Same as Fig. 5 but for group 13 metals of Ga, In, and Tl.

![](./images/817400400226287619_7.jpg)

FIG. 7. The phonon band structures of (a) bHC Co and (b) bHC Ni. Spin-polarized calculations are performed.

$E_{\text{bHC}}$ and $E_{\text{bSQ}}$ listed in Table I, which proves a hypothesis mentioned in the first paragraph in Sec. III B.

Unfortunately, no dynamically stable structures are found for Cs, Ba, Ga, and Tl at zero pressure. The instability of these elements are due to the instability against the out-of-plane vibrations. Fortunately, the imaginary frequencies appear around $\Gamma$ point only, meaning that these 2D metals would be stable when the lateral size of the sample is smaller than the wavelength of the corresponding ZA phonons.

### C. Magnetic effects

The dynamical stability in the bHC structure does not change when the magnetic effects are included. The bHC phase of Cr, Mn, and Fe has nonmagnetic, while that of Co and Ni has ferromagnetic state with the magnetic moment 1.89 and $0.82\ \mu_{\text{B}}$ per atom, respectively (the Bohr magneton $\mu_{\text{B}}$). The bHC Co and bHC Ni are dynamically stable within spin-polarized calculations as shown in Figs. 7(a) and 7(b), respectively, as well as within non-spin-polarized calculations as shown in Appendix A. We find that the behavior of bHC is quite analogous to that of HCP phase. For 3D case, the HCP phase of Mn and Fe has nonmagnetic, while that of Cr, Co, and Ni has ferromagnetic state with $0.12$, $1.60$, and $0.59\ \mu_{\text{B}}$ per atom, respectively [36]. This means that bHC and HCP Cr, Mn, and Fe tend to have small or zero magnetic moment. In addition, HCP Co and Ni are elastically stable irrespective to the presence or absence of magnetic effects [37].

The trend of the dynamical stability in bSQ is different from that of bHC structure. Figure 8 shows the phonon band structure of bSQ Fe, Co, and Ni: left and right for the non-spin-polarized and spin-polarized calculations, respectively. Within non-spin-polarized calculations, the bSQ structure is dynamically stable. However, except Ni, those structures become dynamically unstable when magnetic effects are included, where the absolute magnetic moment per atom is $2.77$, $1.94$, and $0.82\ \mu_{B}$ for ferromagnetic Fe, Co, and Ni, respectively. This trend is similar to the stability of FCC Fe, where it is elastically stable and unstable in nonmagnetic and ferromagnetic states, respectively [37].

### D. Material design principles

We discuss how the dynamical stability of the 2D structure is related to that of the 3D structure in elemental metals. This is summarized in Fig. 9. (i) If the HX structure is dynamically stable in an elemental metal, the HCP and/or FCC structures are also stable (HX$\rightarrow$HCP and/or FCC) except Rb; (ii) If

![](./images/817400400226287619_8.jpg)

FIG. 8. The phonon band structure of Fe, Co, and Ni that have bSQ structure. Left for non-spin-polarized and right for spin-polarized calculations.

either the bHC or 3SQ structure is dynamically stable only, the BCC structure is stable (bHC or 3SQ$\to$BCC); (iii) If the bSQ structure is dynamically stable only, the HCP structure is stable (bSQ$\to$HCP); and (iv) If the bHC and bSQ structures are dynamically stable, where the bSQ is the metastable phase, the HCP (FCC) structure is stable for groups 3, 4, 7, and 8 (groups 9 and 10) metals (bHC and bSQ$\to$HCP or FCC).

The property (i), HX$\to$HCP and/or FCC, can be derived from the fact that the FCC and HCP structures consist of HX monolayers stacked along the (111) direction and the $c$ axis, respectively [1]. The property (ii), bHC or 3SQ$\to$BCC, is also a reasonable conclusion because the BCC structure is obtained by stacking the bHC and 3SQ structures along the (111) direction and $c$ axis, respectively. The property (iii), bSQ$\to$HCP, is derived from the fact that the HCP structure is obtained by stacking the elongated bSQ (along the diagonal direction of the square shaped unit cell) along the $c$ axis. The property (iv), bHC and bSQ$\to$HCP or FCC, may be understood as in the properties of (i) and (iii), while it is difficult to disentangle the stability properties of FCC and HCP. The understanding of the metastability of bSQ phase will be a key to resolve this issue.

Some elements do not follow these trends due to different 3D crystal structures: Hg has the rhombohedral structure, Mn has the cubic structure, and In and Sn have the tetragonal structure. We expect that these structures may be related to metastability of 2D structures different from the HX, bHC and bSQ. According to the DFT calculations [37], Fe (nsp), Fe (sp), Co (nsp), and Co (sp) have HCP, BCC, FCC, and HCP structures, respectively. The different stability between nsp and sp is attributed to a significant change in the potential energy surface in the presence of magnetic effects. We found that 2D Co (sp) does not follow the property (ii). It will be desirable to study how the magnetic effects influence the energy landscape in 2D magnetic materials in detail.

We have demonstrated that 2D structures can be building blocks for constructing 3D structures, so that we expect that some ordered alloys can also be constructed from two elements that show the same property above. In the present study, we focus on the binary Al-Cu system that has a complex phase diagram [38]. For the case of ordered AlCu, it is natural to consider that AlCu has the $\text{B}_h$ (WC) structure with HX Al and HX Cu layers stacked alternately, as shown in Fig. 10(a), since the bHC and HX structures in Al and Cu are dynamically stable, respectively, as shown in Fig. 3. Meanwhile, the $\text{L1}_0$ (CuAu) structure [see Fig. 10(b)] has been predicted to be more energetically stable structure [39]. This may be reasonable because Al and Cu have the bSQ as a metastable structure and also because the $\text{L1}_0$ structure consists of the SQ lattice of Al and the displaced SQ lattice of Cu stacked alternately along $c$ axis. Figures 10(c) and 10(d) show the phonon band structures of AlCu alloy in the $\text{B}_h$ and $\text{L1}_0$ structures, respectively, indicating that the $\text{B}_h$ is dynamically stable, whereas the $\text{L1}_0$ is unstable. The stability of the $\text{B}_h$ phase is robust against the thermal fluctuations up to 2500 K, which is confirmed by performing *ab initio* molecular dynamics (MD) simulations implemented in QE code [25]; see Appendix B for the details. We note that the energetic stability is not enough to yield the dynamical stability of alloys: For the present case, the $\text{L1}_0$ structure is more stable than the $\text{B}_h$ structure by 58 meV per unit cell. We can demonstrate that $\text{B}_h$ CuZn is dynamically stable as provided in Appendix B, while CuZn can have $\text{L1}_0$ or B2 (CsCl) structures as its ground state [40,41].

Our approach based on the list of dynamically stable structures in Figs. 3 and 9 provides a novel strategy for computational design of ordered alloys, which is summarized as follows. (1) Choose two elements that are dynamically stable in either the bHC or bSQ structures; (2) create a crystal structure such as $\text{B}_h$, B2, and $\text{L1}_0$ that consist of bHC or bSQ; and (3) optimize the lattice parameters and calculate the phonon band structure of the ordered alloy. The present strategy may be used for three structures of ordered alloys only. In order to predict the dynamical stability of more complex alloys such as in the $\text{L1}_2$ ($\text{CuAu}_3$) structure or disordered alloys, the stability of binary 2D or disordered monolayers should be investigated. More detailed investigations are left for future work.

## IV. CONCLUDING REMARKS

The phonon band structure of 2D metals in the periodic table has been calculated by assuming the HX, bHC, and bHC structures. The trend in the dynamical stability of 2D metals is correlated with that of 3D metals. This stability relationship between 2D and 3D metals has been applied to a prediction of the dynamical stability of 3D alloys. In order to establish design principles for alloys, it would be important to understand the origin of metastability in both elemental metals and alloys [4] and to calculate the energy landscape as a function of atom positions [42] in alloys. It is interesting to discuss how the present approach is related to the Pettifor's approach for the stability of binary alloys [43].

The present study has focused on the phonons of free-standing and ideal thin films of elemental metals at zero temperature and pressure. It would be interesting to study how the effects of substrate (or strain) [17], chemical adsorption

![](./images/817400400226287619_9.jpg)

■ Cs, Ba, Tl, and Ga: No stable 2D structures found at zero temperature and pressure.

FIG. 9. Relationship of the dynamical stability between 2D structures (HX, bHC, and bSQ) and 3D structures (HCP, FCC, and BCC) in elemental metals. Stable crystal structures in 3D metals are extracted from the periodic table depicted in Ref. [1]. Hg, Mn, and In and Sn have rhombohedral, cubic, and tetragonal structures as its ground state, respectively. Fe (nsp), Fe (sp), Co (nsp), and Co (sp) have HCP, BCC, FCC, and HCP structures, respectively, as predicted by DFT calculations [37]. The stability of multilayered structures (3SQ and 3HX) is investigated if the HX, bHC, and bSQ structures are unstable. Note that 2D Ga becomes dynamically stable when strains are imposed [17].

[24], vacancies [44], grain boundaries [45], and temperature [46] influence the phonon band structure and the dynamical stability of 2D metals. We note that the effect of spin-orbit coupling is important in heavy elements because it strongly influences the dynamical stability of 2D Bi [21] and 2D Po [22] as well as the metastability of FCC Pt in the HCP structure [5]. For a fundamental interest, it is interesting to calculate the electron-phonon coupling function (Eliashberg function) of 2D metals in order to find novel 2D superconductors [47–50]. It is also interesting to explore whether 2D Mn has more complex structures, since 3D Mn has the cubic structure with 58 atoms per unit cell [51].

Finally, we mention that it is still difficult to predict the synthesizability of materials (i.e., how to synthesize the predicted materials experimentally) within the framework of computational materials science. The energetic and dynamical stability of materials do not guarantee the successful synthesis

![](./images/817400400226287619_10.jpg)

FIG. 10. Schematic illustration of (a) $B_h$ and (b) $L1_0$ structures. The phonon band structure of (c) $B_h$ and (d) $L1_0$ AlCu alloys.

![](./images/817400400226287619_11.jpg)

FIG. 11. The phonon band structure of group 1 elements (Li, Na, K, Rb, and Cs) for (a) HX, (b) bHC, and (c) bSQ structures.

![](./images/817400400226287619_12.jpg)

FIG. 12. Same as Fig. 11 but for group 2 elements (Be, Mg, Ca, Sr, and Ba).

of them, as have been discussed in inorganic crystals [52], penta-graphene [53], and carbon and silicon molecules [54]. To establish the synthesizability of 2D metals, we have to understand the potential energy landscape characterized by many degrees of freedom, while such a theoretical investiga- tion is left for future work.

![](./images/817400400226287619_13.jpg)

FIG. 13. Same as Fig. 11 but for group 3 elements (Sc, Y, and Lu).

![](./images/817400400226287619_14.jpg)

FIG. 14. Same as Fig. 11 but for group 4 elements (Ti, Zr, and Hf).

## ACKNOWLEDGMENTS

This study is supported by the Nikki-Saneyoshi Founda- tion. A part of numerical calculations has been done using the facilities of the Supercomputer Center, the Institute for Solid State Physics, the University of Tokyo.

## APPENDIX A: PHONON BAND STRUCTURES OF 2D METALS

Figures 11–24 show the phonon band structures of groups 1–14 metals within non-spin-polarized calculations.

### Group 1: Li, Na, K, Rb, and Cs (alkali metals)

Figure 11 shows the phonon band structures of Li, Na, K, Rb, and Cs. The HX Rb is dynamically stable, while HX Li, Na, K, and Cs are unstable because the imaginary frequencies in the ZA branch are observed around $\Gamma$. When the bHC phase

![](./images/817400400226287619_15.jpg)

FIG. 15. Same as Fig. 11 but for group 5 elements (V, Nb, and Ta).

![](./images/817400400226287619_16.jpg)

FIG. 16. Same as Fig. 11 but for group 6 elements (Cr, Mo, and W).

is assumed, the ZA phonon modes are stabilized. This yields the dynamical stability of 2D Li, Na, and K, while the bHC Cs is still unstable. The alkali metals in the bSQ structure are all unstable. Note that the bSQ Rb is more energetically stable than the HX Rb by 73 meV/atom.

### Group 2: Be, Mg, Ca, Sr, and Ba (alkali earth metals)

Figure 12 shows the phonon band structures of Be, Mg, Ca, Sr, and Ba. The HX and bHC structures are dynamically stable except Ba. As the ion mass increases in the HX structure, the phonon softening behavior is observed in ZA branch. The maximum phonon energy is higher than that of the alkali metal in the same period because as listed in Table I the values of $E_j$ and $a_j$ in the alkali earth metals are larger and smaller than those in the alkali metals, respectively. The bSQ structure is dynamically unstable in alkali earth metals. The band structures of bHC and bSQ Ba are omitted due to no convergence in the scf calculations. As for Rb, 2D Be, Mg, Ca, and Sr in the bSQ structure are energetically more stable than those in the HX structure, while the former and the latter are dynamically unstable and stable, respectively.

![](./images/817400400226287619_17.jpg)

FIG. 17. Same as Fig. 11 but for group 7 elements (Mn, Tc, and Re).

![](./images/817400400226287619_18.jpg)

FIG. 18. Same as Fig. 11 but for group 8 elements (Fe, Ru, and Os).

### Group 3: Sc, Y, and Lu

Figure 13 shows the phonon band structures of Sc, Y, and Lu. The bHC and bSQ structures are dynamically stable. Since the bHC is energetically more stable than the bSQ structure as listed in Table I, the bSQ is regarded as a metastable state.

### Group 4: Ti, Zr, and Hf

Figure 14 shows the phonon band structures of Ti, Zr, and Hf. The HX structures are unstable against vibrations

![](./images/817400400226287619_19.jpg)

FIG. 19. Same as Fig. 11 but for group 9 elements (Co, Rh, and Ir).

![](./images/817400400226287619_20.jpg)

FIG. 20. Same as Fig. 11 but for group 10 elements (Ni, Pd, and Pt).

corresponding to the point M, which is different from the instability behavior observed in group 3 elements (Fig. 13). The bSQ structure is dynamically stable for these elements. Different from bHC Ti and Zr, the bHC Hf is more energetically stable than the bSQ structure by 9 meV per unit cell. The phonon softening at the point M is not strong compared to bHC Ti and Zr, yielding the dynamical stability in the bHC Hf only.

### Group 5: V, Nb, and Ta

Figure 15 shows the phonon band structures of V, Nb, and Ta. Monolayer structures are all dynamically unstable, whereas as shown in Sec. III B, the 3SQ structure is dynamically stable.

![](./images/817400400226287619_21.jpg)

FIG. 21. Same as Fig. 11 but for group 11 elements (Cu, Ag, and Au).

![](./images/817400400226287619_22.jpg)

FIG. 22. Same as Fig. 11 but for group 12 elements (Zn, Cd, and Hg).

### Group 6: Cr, Mo, and W

Figure 16 shows the phonon band structures of Cr, Mo, and W. These elements in the bHC structure are dynamically stable. It should be noted that for Mo and W, we have found other bHC structure (i.e., a highly buckled structure) different from the bHC structure listed in Table I. Although the cohesive energy in the former is larger than that in the latter, such a structure is dynamically unstable, as mentioned in Sec. III B.

![](./images/817400400226287619_23.jpg)

FIG. 23. Same as Fig. 11 but for group 13 elements (Al, Ga, In, and Tl).

![](./images/817400400226287619_24.jpg)

FIG. 24. Same as Fig. 11 but for group 14 elements (Sn and Pb).

## Group 7: Mn, Tc, and Re
Figure 17 shows the phonon band structures of Mn, Tc, and Re. The bHC and bSQ structures are dynamically stable in these elements, whereas the bSQ structure is metastable.

## Group 8: Fe, Ru, and Os
Figure 18 shows the phonon band structures of Fe, Ru, and Os. These have the bHC and bSQ as dynamically stable structures, while the bSQ is a metastable structure. Magnetic effects change the dynamical stability of bSQ Fe, as shown in Sec. III C.

## Group 9: Co, Rh, and Ir
Figure 19 shows the phonon band structures of Co, Rh, and Ir. These elements in the bHC and bSQ structures are dynamically stable, while the bSQ structure is metastable. Magnetic effects change the dynamical stability of bSQ Co, as shown in Sec. III C.

## Group 10: Ni, Pd, and Pt
Figure 20 shows the phonon band structures of Ni, Pd, and Pt. These elements in the bHC and bSQ structures are dynamically stable, while the bSQ is a metastable structure.

![](./images/817400400226287619_25.jpg)

FIG. 25. The time evolution of $\boldsymbol{u}$ for an Al atom in a unit cell of $B_h$ AlCu.

![](./images/817400400226287619_26.jpg)

FIG. 26. The phonon band structure of $B_h$ CuZn.

## Group 11: Cu, Ag, and Au (noble metals)
Figure 21 shows the phonon band structures of Cu, Ag, and Au. The HX and bHC structures are dynamically stable. The former result (the stability of HX) is consistent with the previous calculations [12–14]. Cu is dynamically stable in the form of bSQ structure and is the only element having no imaginary frequencies in all 2D structures. bSQ Ag is more energetically stable than HX Ag, while the former and the latter are dynamically unstable and stable, respectively.

## Group 12: Zn, Cd, and Hg
Figure 22 shows the phonon band structures of Zn, Cd, and Hg. For Zn and Cd, the HX and bHC structures are dynamically stable, while for Hg the bSQ structure is dynamically stable. Cd in the bSQ structure are more energetically stable than that in the HX structure. bSQ Hg is a semiconductor with an energy gap of 1 eV within GGA-PBE.

## Group 13: Al, Ga, In, and Tl
Figure 23 shows the phonon band structures of Al, Ga, In, and Tl. For all the elements, the HX structure is unstable. The bHC and bSQ structures are dynamically stable in Al only. The stability for Ga, In, and Tl in the trilayer structures is investigated in Sec. III B.

## Group 14: Sn and Pb
Figure 24 shows the phonon band structures of Sn and Pb. Sn and Pb have the bHC as a dynamically stable structure. The bSQ Pb is a metastable phase.

## APPENDIX B: 3D ALLOYS
The optimized lattice constants $(a,c)$ of ordered alloys are as follows. For AlCu alloys, $(a,c)=(2.787,4.077)$ Å for $B_h$ structure $(c/a=1.463)$ and $(2.900,3.202)$ Å for L1$_0$ structure $(c/a=1.104)$; and for $B_h$ CuZn, $(a,c)=(2.676,4.211)$ Å, i.e., $c/a=1.574$. In order to investigate the temperature effect on the dynamical stability of ordered alloys, the $ab$ initio molecular dynamics (MD) simulations for $B_h$ AlCu and CuZn alloys are performed using QE code [25]. The ionic temperature is controlled via the velocity scaling and increased from 500 K up to 3000 K with an increment of 500 K. A $2{\times}2{\times}2$ supercell with 16 atoms is considered. The Newton's equation is integrated by using Verlet algorithm

with a time step of 0.967 fs (20 a.u.) and up to 2.0 ps (2100 MD steps).

Figure 25 shows the time-evolution of the displacement vector $\boldsymbol{u}=(u_x, u_y, u_z)$ from the equilibrium position of an Al atom in a unit cell of $B_h$ AlCu at $T=2500$ K: The oscillation amplitude is about $0.4$ Å that is smaller than the lattice constant $a=2.787$ Å. Above $T=3000$ K, no scf convergence is obtained after some MD steps, since the atoms deviate from the equilibrium position largely.

Figure 26 shows the phonon band structure of $B_h$ CuZn. No imaginary phonon frequencies are observed, indicating that $B_h$ CuZn is dynamically stable at $T=0$ K. However, no scf convergence is obtained during the MD calculations assuming $2 \times 2 \times 2$ supercell.

[1] N. W. Ashcroft, N. D. Mermin, and D. Wei, *Solid State Physics* (Cengage Learning, Singapore, 2016).

[2] R. M. Martin, *Electronic Structure: Basic Theory and Practical Methods* (Cambridge University Press, Cambridge, 2004).

[3] G. Grimvall, B. Magyari-Köpe, V. Ozolinš, and K. A. Persson, Lattice instabilities in metallic elements, *Rev. Mod. Phys.* **84**, 945 (2012).

[4] A. Togo and I. Tanaka, Evolution of crystal structures in metallic elements, *Phys. Rev. B* **87**, 184104 (2013).

[5] S. Schönecker, X. Li, M. Richter, and L. Vitos, Lattice dynamics and metastability of FCC metals in the HCP structure and the crucial role of spin-orbit coupling in platinum, *Phys. Rev. B* **97**, 224305 (2018).

[6] X. Huang, S. Li, Y. Huang, S. Wu, X. Zhou, S. Li, C. L. Gan, F. Boey, C. A. Mirkin, and H. Zhang, Synthesis of hexagonal close-packed gold nanostructures, *Nat. Commun.* **2**, 292 (2011).

[7] A.-X. Yin, W.-C. Liu, J. Ke, W. Zhu, J. Gu, Y.-W. Zhang, and C.-H. Yan, Ru Nanocrystals with Shape-Dependent Surface-Enhanced Raman Spectra and Catalytic Properties: Controlled Synthesis and DFT Calculations, *J. Am. Chem. Soc.* **134**, 20479 (2012).

[8] X. Kong, K. Xu, C. Zhang, J. Dai, S. N. Oliaee, L. Li, X. Zeng, C. Wu, and Z. Peng, Free-Standing Two-Dimensional Ru Nanosheets with High Activity toward Water Splitting, *ACS Catal.* **6**, 1487 (2016).

[9] K. S. Novoselov, A. K. Geim, S. Morozov, D. Jiang, Y. Zhang, S. Dubonos, I. Grigorieva, and A. Firsov, Electric field effect in atomically thin carbon films, *Science* **306**, 666 (2004).

[10] S. Cahangirov, M. Topsakal, E. Aktürk, H. Şahin, and S. Ciraci, Two- and One-Dimensional Honeycomb Structures of Silicon and Germanium, *Phys. Rev. Lett.* **102**, 236804 (2009).

[11] S. Balendhran, S. Walia, H. Nili, S. Sriram, and M. Bhaskaran, Elemental Analogues of Graphene: Silicene, Germanene, Stanene, and Phosphorene, *Small* **11**, 640 (2015).

[12] L.-M. Yang, T. Frauenheim, and E. Ganz, Properties of the free-standing two-dimensional copper monolayer, *J. Nanomater.* **2016**, 8429510 (2016).

[13] L.-M. Yang, T. Frauenheim, and E. Ganz, The new dimension of silver, *Phys. Chem. Chem. Phys.* **17**, 19695 (2015).

[14] L.-M. Yang, T. Frauenheim, and E. Ganz, Glitter in a 2D monolayer, *Phys. Chem. Chem. Phys.* **17**, 26036 (2015).

[15] B. Feng, O. Sugino, R. Y. Liu, J. Zhang, R. Yukawa, M. Kawamura, T. Iimori, H. Kim, Y. Hasegawa, H. Li, L. Chen, K. Wu, H. Kumigashira, F. Komori, T. C. Chiang, S. Meng, and I. Matsuda, Dirac Fermions in Borophene, *Phys. Rev. Lett.* **118**, 096401 (2017).

[16] W. B. Li, L. J. Kong, C. Y. Chen, J. Gou, S. X. Sheng, W. F. Zhang, H. Li, L. Chen, P. Cheng, and K. H. Wu, Experimental realization of honeycomb borophene, *Sci. Bull.* **63**, 282 (2018).

[17] V. Kochat, A. Samanta, Y. Zhang, S. Bhowmick, P. Manimunda, S. A. S. Asif, A. S. Stender, R. Vajtai, A. K. Singh, C. S. Tiwary, and P. M. Ajayan, Atomically thin gallium layers from solid-melt exfoliation, *Sci. Adv.* **4**, e1701373 (2018).

[18] S. Zhang, J. Zhou, Q. Wang, X. Chen, Y. Kawazoe, and P. Jena, Penta-graphene: A new carbon allotrope, *Proc. Natl. Acad. Sci. USA* **112**, 2372 (2015).

[19] H. Liu, A. T. Neal, Z. Zhu, Z. Luo, X. Xu, D. Tománek, and P. D. Ye, Phosphorene: An unexplored 2D semiconductor with a high hole mobility, *ACS Nano* **8**, 4033 (2014).

[20] S. Zhang, Z. Yan, Y. Li, Z. Chen, and H. Zeng, Atomically thin arsenene and antimonene: Semimetal-semiconductor and indirect-direct band-gap transitions, *Angew. Chem., Int. Ed. Engl.* **54**, 3112 (2015).

[21] E. Aktürk, O. Ü. Aktürk, and S. Ciraci, Single and bilayer bismuthene: Stability at high temperature and mechanical and electronic properties, *Phys. Rev. B* **94**, 014115 (2016).

[22] S. Ono, Two-dimensional square lattice polonium stabilized by the spin-orbit coupling, *Sci. Rep.* **10**, 11810 (2020).

[23] J. Nevalaita and P. Koskinen, Atlas for the properties of elemental two-dimensional metals, *Phys. Rev. B* **97**, 035411 (2018).

[24] J. Hwang, Y. J. Oh, J. Kim, M. M. Sung, and K. Cho, Atomically thin transition metal layers: Atomic layer stabilization and metal-semiconductor transition, *J. Appl. Phys.* **123**, 154301 (2018).

[25] P. Giannozzi *et al.*, Advanced capabilities for materials modeling with Quantum ESPRESSO, *J. Phys.: Condens. Matter* **29**, 465901 (2017).

[26] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, *Phys. Rev. Lett.* **77**, 3865 (1996).

[27] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Restoring the Density-Gradient Expansion for Exchange in Solids and Surfaces, *Phys. Rev. Lett.* **100**, 136406 (2008).

[28] M. Ropo, K. Kokko, and L. Vitos, Assessing the Perdew-Burke-Ernzerhof exchange-correlation density functional revised for metallic bulk and surface systems, *Phys. Rev. B* **77**, 195445 (2008).

[29] A. Dal Corso, Pseudopotentials periodic table: From H to Pu, *Computational Material Science* **95**, 337 (2014).

[30] H. J. Monkhorst and J. D. Pack, Special points for Brillouin-zone integrations, *Phys. Rev. B* **13**, 5188 (1976).

[31] N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Thermal Contraction and Disordering of the Al(110) Surface, *Phys. Rev. Lett.* **82**, 3296 (1999).

[32] S. Baroni, S. Gironcoli, A. D. Corso, and P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory, *Rev. Mod. Phys.* **73**, 515 (2001).


[33] N. Gaston, B. Paulus, K. Rosciszewski, P. Schwerdtfeger, and H. Stoll, Lattice structure of mercury: Influence of electronic correlation, Phys. Rev. B 74, 094102 (2006).

[34] C. Kittel, *Introduction to Solid State Physics*, 8th ed. (Wiley, Hoboken, NJ, 2005).

[35] E. Mostaani, N. D. Drummond, and V. I. Fal'ko, Quantum Monte Carlo Calculation of the Binding Energy of Bilayer Graphene, Phys. Rev. Lett. 115, 115501 (2015).

[36] M. Podgórny and J. Goniakowski, Magnetism of hexagonal 3d transition metals, Phys. Rev. B 42, 6683 (1990).

[37] G. Y. Guo and H. H. Wang, Gradient-corrected density func- tional calculation of elastic constants of Fe, Co and Ni in BCC, FCC and HCP structures, Chin. J. Phys. 38, 949 (2000).

[38] V. T. Witusiewicz, U. Hecht, S. G. Fries, and S. Rex, The Ag- Al-Cu system: Part I: Reassessment of the constituent binaries on the basis of new experimental data, J. Alloys Compd. 385, 133 (2004).

[39] X. W. Zhou, D. K. Ward, and M. E. Foster, An analytical bond-order potential for the aluminum copper binary system, J. Alloys Compd. 680, 752 (2016).

[40] L. H. Beck and C. S. Smith, Copper-zinc constitution diagram, redetermined in the vicinity of the beta phase by means of quantitative metallography, JOM 4, 1079 (1952).

[41] P. E. A. Turchi, M. Sluiter, F. J. Pinski, D. D. Johnson, D. M. Nicholson, G. M. Stocks, and J. B. Staunton, First-Principles Study of Phase Stability in Cu-Zn Substitutional Alloys, Phys. Rev. Lett. 67, 1779 (1991).

[42] N. Gaston, B. Paulus, U. Wedig, and M. Jansen, Multiple Minima on the Energy Landscape of Elemental Zinc: A Wave Function Based *Ab Initio* Study, Phys. Rev. Lett. 100, 226404 (2008).

[43] D. Pettifor, *Bonding and Structure of Molecules and Solids* (Oxford University Press, New York, 2002).

[44] J. Nevalaita and P. Koskinen, Beyond ideal two-dimensional metals: Edges, vacancies, and polarizabilities, Phys. Rev. B 98, 115433 (2018).

[45] W. A. Diery, E. A. Moujaes, and R. W. Nunes, Nature of localized phonon modes of tilt grain boundaries in graphene, Carbon 140, 250 (2018).

[46] O. Hellman, I. A. Abrikosov, and S. I. Simak, Lattice dynamics of anharmonic solids from first principles, Phys. Rev. B 84, 180301(R) (2011).

[47] H. M. Zhang, Y. Sun, W. Li, J. P. Peng, C. L. Song, Y. Xing, Q. Zhang, J. Guan, Z. Li, Y. Zhao *et al.*, Detection of a Super- conducting Phase in a Two-Atom Layer of Hexagonal Ga Film Grown on Semiconducting GaN(0001), Phys. Rev. Lett. 114, 107003 (2015).

[48] Y. Liu, Z. Wang, X. Zhang, C. Liu, Y. Liu, Z. Zhou, J. Wang, Q. Wang, Y. Liu, C. Xi, M. Tian, H. Liu, J. Feng, X. C. Xie, and J. Wang, Interface-Induced Zeeman-Protected Superconductivity in Ultrathin Crystalline Lead Films, Phys. Rev. X 8, 021002 (2018).

[49] Y. Cao, V. Fatemi, S. Fang, K. Watanabe, T. Taniguchi, E. Kaxiras, and P. Jarillo-Herrero, Unconventional superconduc- tivity in magic-angle graphene superlattices, *Nature* (London) 556, 43 (2018).

[50] M. Yankowitz, S. Chen, H. Polishyn, Y. Zhang, K. Watanabe, T. Taniguchi, D. Graf, A. F. Young, and C. R. Dean, Tuning superconductivity in twisted bilayer graphene, *Science* 363, 1059 (2019).

[51] D. Hobbs, J. Hafner, and D. Spišák, Understanding the complex metallic element Mn. I. Crystalline and noncollinear magnetic structure of $\alpha$-Mn, Phys. Rev. B 68, 014407 (2003).

[52] W. Sun, S. T. Dacek, S. P. Ong, G. Hautier, A. Jain, W. D. Richards, A. C. Gamst, K. A. Persson, and G. Ceder, The thermodynamic scale of inorganic crystalline metastability, *Sci. Adv.* 2, e1600225 (2016).

[53] C. P. Ewels, X. Rocquefelte, H. W. Kroto, M. J. Rayson, P. R. Briddon, and M. I. Heggie, Predicting experimentally stable allotropes: Instability of penta-graphene, *Proc. Natl. Acad. Sci. USA* 112, 15609 (2015).

[54] D. S. De, B. Schaefer, B. von Issendorff, and S. Goedecker, Nonexistence of the decahedral Si₂₀H₂₀ cage: Levinthal's para- dox revisited, Phys. Rev. B 101, 214303 (2020).

165424-14