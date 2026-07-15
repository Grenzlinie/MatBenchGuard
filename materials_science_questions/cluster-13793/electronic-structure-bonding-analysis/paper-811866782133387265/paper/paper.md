# First principles studies of ZrNi and ZrNiH₃
S.F. Matar *

Université de Bordeaux, CNRS, ICMCB, 87 Avenue du Docteur Albert Schweitzer, F-33608 Pessac Cedex, France

---

## ARTICLE INFO
**Article history:**
Received 22 January 2009
In final form 6 March 2009
Available online 12 March 2009

This work is dedicated to Volker Eyert.

## ABSTRACT
Changes in electronic structure due to hydrogen uptake within ZrNi alloy system leading to the experimental hydride composition ZrNiH₃, are examined ab initio using both pseudo-potential and all electron calculations. In order to establish trends in stability hypothetic ZrNiH and ZrNiH₂ are also examined and proposed to act as transition phases in a stepwise hydrogen desorption process. Analyses of the site projected density of states and of the chemical bonding point to meaningful changes of the electronic structure whereby hydrogen brings new states within the valence band and is found to preferably bind with Ni rather than with Zr.

© 2009 Elsevier B.V. All rights reserved.

---

### 1. Introduction
Binary equiatomic (1:1) alloys exhibit interesting physical properties such as that of shape memory for TiNi [1] and ZrRh [2]. Other 1:1 systems exhibit the ability to uptake relatively large amounts of hydrogen. This is the case of ZrNi which absorbs 3 atoms/formula unit (fu) leading to ZrNiH₃ (1:1:3) [3]. The resulting hydrogen storage capacity which amounts to ~3% allows to consider it as a candidate for on-board vehicular applications [4]. Other 1:1:3 hydride systems are also known such as for CeNi [5]. One route to their synthesis is the energetic mechanical grinding of constituents [6].

Effects of hydrogen such as the changes of the electronic structure and the strength of the chemical bonding between constituents are important to understand at both the fundamental and application levels. This is herein modeled within the density functional theory DFT [7,8] with a study of ZrNi and ZrNiH₃. Furthermore, for the purpose of establishing trends in electronic structures, the two intermediate hypothetic mono- and di-hydrides are investigated, namely ZrNiH and ZrNiH₂. For this purpose two complementary DFT-based methods are used: Firstly with pseudo-potential methodology a geometry optimization is carried out to obtain equilibrium energies and volumes for the four systems and relative binding energy of H within. Then all electrons calculations are carried out to examine the role of each constituent in the density of states and the relevant chemical bonding properties for metal-H interaction.

### 2. Computational framework
Within DFT, calculations of the optimized geometries and relative stabilities are carried out in the framework of a pseudo-potential (PP) approach within the Vienna ab initio simulation package (VASP) code [9]. Projector augmented wave (PAW) [10,11] potentials are used as built within the generalized gradient approximation (GGA) [12] scheme. The optimization of the structural parameters is performed until the forces on the atoms are less than 0.02 eV/Å and all stress components are below 0.003 eV/Å³. The calculations are converged at an energy cut-off of 269.56 eV for the plane-wave basis set. The tetrahedron method with Blöchl corrections [10] as well as a Methfessel-Paxton scheme [13] for conducting systems are applied for both geometry relaxation and total energy calculations. Brillouin zone (BZ) integrals [14] are approximated using a **k**-point grids with a starting mesh of $4*4*4$ up to $8*8*8$ for best convergence and relaxation to zero strains.

All-electron calculations are performed using the scalar-relativistic implementation of the augmented spherical wave (ASW) method [15,16]. Likewise the computations are based on DFT and the GGA scheme as parametrized by Wu and Cohen [17]. In the ASW method, the wave function is expanded in atom-centered augmented spherical waves, which are Hankel functions and numerical solutions of Schrödinger's equation, respectively, outside and inside the so-called augmentation spheres. In the minimal ASW basis set the outermost shells represent the valence states and the matrix elements are constructed using partial waves up to $l_{max.}+1=3$ for Zr and Ni and $l_{max.}+1=2$ for H. Convergence is obtained when negligible variations for the charges ($\Delta Q=10^{-8}$) and for the total energy ($\Delta E=10^{-7}$ eV), are observed between two successive iterative cycles. The ASW method uses the atomic sphere approximation (ASA) which assumes overlapping spheres centered on the atomic sites where the potential has a spherical symmetry. In order to represent the correct shape of the potential in the large voids of the crystal structure (Fig. 1), additional augmentation spheres are inserted to avoid an otherwise too large overlap between the actual atomic spheres. These are called empty spheres (ES) described as pseudo-atoms with zero atomic number and basis set $l_{max.}+1=2$, allowing them to receive

---
* Fax: +33 540002761.
E-mail address: s.matar@u-bordeaux1.fr

0009-2614/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.cplett.2009.03.022

![](./images/811866782133387265_1.jpg)

Fig. 1. ZrNiH₃ orthorhombic structure. Large (red), medium (blue) and small black and grey spheres are for Zr, Ni and H. The latter are respectively within Zr₃Ni₂ and Zr₃Ni insertion sites polyhedra (cf. text) (For interpretation of the references in color in this figure legend, the reader is referred to the web version of this article.).

charges from the neighboring atomic species. Further, covalence effects within the lattice can be better accounted for. The choice of these sites as well as the augmentation radii are automatically determined using the sphere-geometry optimization algorithm [18]. In the case of the Cmcm structure of presently studied systems ES were found to be inserted within (4c) and (8e) sites between actual atomic species. The BZ integrations are performed using the linear tetrahedron method with up to 576 $\mathbf{k}$-points within the irreducible wedge [10,16]. The chemical bonding properties were analyzed using the covalent bond energy (ECOV) criterion [19] which combines both Hamiltonian and overlap populations. In the plots (Fig. 4), negative, positive and zero magnitudes of the unit-less ECOV are indicative of bonding, antibonding, and non-bonding interactions respectively.

## 3. Geometry optimization from pseudo-potential calculations

### 3.1. Crystal structure and calculational results

Both ZrNi and ZrNiH₃ crystallize in the base centered orthorhombic Cmcm space group (SG), Number: 63 [20,21]; there are 4 formula units (fu) per cell, but due to the base centered SG, only two fu are explicitly accounted for in the calculations. Table 1 re-groups the experimental data as well as the calculated ones. The uptake of 3 hydrogen atoms per fu giving ZrNiH₃, results in an isotropic expansion of the cell and hydrogen atoms are dispatched over two different sets of sites. H₁ and H₂ are then found in [Zr₃Ni₂] trigonal bipyramids and [Zr₃Ni] tetrahedra respectively. The coordination polyhedra of the two hydrogen sites are shown within the crystal structure in Fig. 1. Starting from the crystal data in Table 1, a full geometry relaxation was carried out for both 1:1 and 1:1:3 systems. Further, in order to enable comparisons and trends in stability, the mono- and di-hydrides were also examined. The first one by considering the occupation of (4c) H₁ positions, the second with only (8f) H₂ ones. For ZrNiH₂ model preliminary calculations were also attempted assuming full (4c) and partial (8f) occupations in order to obtain the 1:1:2 stoichiometry. But the partial occupation of (8f) sites led to the loss of orthorhombic symmetry leading to a triclinic one with an energy destabilization. After geometry optimization the orthorhombic symmetry is kept for all systems within the base centered Cmcm SG. The calculated values Table 1) show small deviations with respect to the experimental lattice volume and internal coordinates as given in Table 1. The lattice constants and volumes of the intermediate hydrides are calculated in between those of the actual 1:1 and 1:1:3 systems. The trend is toward a progressive increase of cell volume upon H insertion.

### 3.2. Geometry optimization and energetics

In a second step a set of calculations was done around optimized minima to obtain the equilibrium ground state energy/volume values from the quadratic fit of the curves with a second order Birch equation of state (EOS) [22]. Fig. 2a shows the respective $E=f(V)$ curves which have minima but exhibit a rather flat variation. The equilibrium values are then obtained with a moderate goodness of fit magnitude: $\chi^{2}=10^{-4}$ (this value should be closer to $10^{-6}$), so that an error can be expected on the volume: $\Delta V \sim \pm 2-3$ Å³. A comparison of $V_{eq.}$ with the values from geometry optimization shows such differences. Nevertheless volumes remain close to experimental values for 1:1 and 1:1:3. An energy decrease from the 1:1 system down to the 1:1:3 one is observed, with the 1:1:1 and 1:1:2 hypothetic systems in-between. This can be expected from the extra electron brought by additional H. From the equilibrium values in Table 1, ZrNi and ZrNiH₃ are found with volumes close to the experimental ones. The bulk moduli $B_{0}$ are also obtained from the fit results. Although affected by the error above the trend is toward a slight increase of $B_{0}$ from the alloy system toward the 1:1:3 hydride with an intermediate value for 1:1:1 and 1:1:2 hydrides. It can be suggested that this relative

<table><caption>Table 1
Geometry optimization results for ZrNi and its hydrides. Space group Cmcm, no. 63. Experimental values are in italics.</caption>
<thead>
  <tr>
    <th>System</th>
    <th>ZrNi [3]</th>
    <th>ZrNiH</th>
    <th>ZrNiH₂</th>
    <th>ZrNiH₃ [21]</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>a-latt. const. (Å)</td>
    <td>3.287/3.268</td>
    <td>3.43</td>
    <td>3.41</td>
    <td>3.498/3.53</td>
  </tr>
  <tr>
    <td>b/a</td>
    <td>3.07/3.04</td>
    <td>2.98</td>
    <td>3.06</td>
    <td>2.97/2.97</td>
  </tr>
  <tr>
    <td>c/a</td>
    <td>1.23/1.26</td>
    <td>1.20</td>
    <td>1.27</td>
    <td>1.23/1.218</td>
  </tr>
  <tr>
    <td>Atoms at 4c $(0,y,\frac{1}{4})$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$y_{Ni}$</td>
    <td>0.362/0.361</td>
    <td>0.42</td>
    <td>0.435</td>
    <td>0.426 /0.43</td>
  </tr>
  <tr>
    <td>$y_{Zr}$</td>
    <td>0.083/0.082</td>
    <td>0.14</td>
    <td>0.141</td>
    <td>0.139/0.14</td>
  </tr>
  <tr>
    <td>$y_{H_{1}}$ s</td>
    <td>–</td>
    <td>0.916</td>
    <td>–</td>
    <td>0.931/0.956</td>
  </tr>
  <tr>
    <td>$H_{2}$ at 8f $(0,y,z)$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$y$</td>
    <td>–</td>
    <td>–</td>
    <td>0.313</td>
    <td>0.312/0.298</td>
  </tr>
  <tr>
    <td>$z$</td>
    <td>–</td>
    <td>–</td>
    <td>0.687</td>
    <td>0.687/0.507</td>
  </tr>
  <tr>
    <td>Vol./4 fu (Å³)</td>
    <td>134.1/133.14</td>
    <td>144.3</td>
    <td>154.1</td>
    <td>156.8 /159.08</td>
  </tr>
  <tr>
    <td>Equil. vol./4 fu (Å³)</td>
    <td>135.94/133.14</td>
    <td>145.68</td>
    <td>155.98</td>
    <td>158.57/159.08</td>
  </tr>
  <tr>
    <td>Equil. energy/4 fu (eV)</td>
    <td>–59.08</td>
    <td>–73.74</td>
    <td>–89.54</td>
    <td>–105.12</td>
  </tr>
  <tr>
    <td>Bulk modulus (GPa)</td>
    <td>138</td>
    <td>147</td>
    <td>149</td>
    <td>155</td>
  </tr>
</tbody>
</table>

![](./images/811866782133387265_2.jpg)

Fig. 2. ZrNi and ZrNi-H systems: (a) Energy versus volume curves; fit values with Birch EOS are given in Table 1 and (b) graphic display of the different equilibrium $E_0, V_0$ with connecting lines added as guide for the eye, cf. text. Mono- and dihydrides are hypothetic.

'hardening' is due to the formation of increasing number of hydrogen-metal bonds within the alloy lattice. This feature will be developed hereafter when discussing the chemical bonding.

The $E_0, V_0$ equilibrium values are then plotted in Fig. 2b for all 4 systems. With respect to a line joining the 1:1 and 1:1:3 systems, ZrNiH and $ZrNiH_2$ are found off the line; this agrees with their hypothetic existence. However one can notice a larger deviation, i.e. a destabilization of $ZrNiH_2$ with respect to the monohydride which is found closer to the line. This could point to a stronger bonding of hydrogen when it is in (4c) positions. This is detailed in next section describing the chemical bonding.

From the energy results we examine the stability of hydrogen within the 1:1 system using the following expression: $E_{stabil.} = E_{(ZrNiH_x)} - E_{(ZrNi)} - xE_{(H_2)}$ given for 2 fu. While the two first terms of the right hand side equality are the equilibrium values obtained from the calculations, $(E_{H_2})$ is derived from PP-PAW-GGA calculations of $H_2$. This is done by placing dihydrogen in a cube box with $a = 4.5$ Å. The resulting energy, $(E_{H_2}) = -6.651$ eV is the total electronic energy. It includes twice the energy of monohydrogen and needs to be corrected by the zero point energy (ZPE). In order to establish comparison with experiment calculations were carried out for one H in a similar box, resulting in an energy of $-0.95$ eV. For $H_2$, ZPE amounts to $\sim 0.28$ eV as calculated by the same method (VASP) [23]. The binding energy of $H_2$ is then $-4.47$ eV which comes close in magnitude to the dissociation energy (inverse sign) of the molecule as obtained from fluorescence excitation spectroscopy: $\sim 36118$ cm$^{-1}$, i.e. $\sim 4.48$ eV [24]. Then with E($H_2$) validated and the equilibrium energy values we extract the stabilization energies of hydrogen in the different hydride lattices: $E_{H-stabil.}^{ZrNiH} = -0.679$ eV, per $H_2$; $E_{H-stabil.}^{ZrNiH_2} = -1.928$ eV for 4H, i.e. $-0.964$ eV per $H_2$ and $E_{H-stabil.}^{ZrNiH_3} = -3.067$ eV for 6H, i.e. $-1.02$ per $H_2$. Consequently H is found most stable within $ZrNiH_3$, in agreement with its experimental existence. However, if this compound were to be used in hydrogen storage devices, we suggest that H release should be stepwise because the energy cost to expell all 3 hydrogens ($ZrNiH_3 \rightarrow ZrNi$) would be too high compared to an energy difference from one system to the other going up the line in Fig. 2b. In this context the di- and mono-hydrides can be considered as metastable, transition systems. While further experimental evidence is needed in this context, the energies involved in these mechanisms compare fairly well with those computed for H within $TiCo_3$ with $\Delta E = 0.305$ eV [25]. Also from experiment the activation energy of hydrogen within $LaNi_5$ is found amounting to 0.224 eV per atom [26].

### 4. All electrons calculations

Calculations of the electronic structure and properties of chemical bonding were then carried out for ZrNi and $ZrNiH_3$. At energy self-consistent convergence charge exchange with small amounts of $\sim 0.3$ electrons was found from Zr toward Ni and ES in ZrNi and from Zr to Ni, H and ES in $ZrNiH_3$. This is in agreement with

![](./images/811866782133387265_3.jpg)

Fig. 3. Site projected DOS for (a) ZrNi and (b) $ZrNiH_3$.

the larger electronegativity of $ \text{Ni} $, $ \chi = 1.91 $ with respect to $ \text{Zr} $ $ \chi = 1.33 $ at Pauling scale [27]. The slight charge transfer toward the empty spheres (ES) over s, p valence basis sets is a sign of covalence ensured by their insertion within ZrNi and points to the completeness of the electronic representation of the system.

### 4.1. Density of states
The site projected density of states (PDOS) are shown in Fig. 3 in which the Fermi level, $ E_F $ is taken as zero energy. For ZrNi (Fig. 3a) the valence band (VB) is mainly dominated by Ni d states centered well below $ E_F $ because Ni is a late element in the 3d series; whereas Zr which is an early element in the 4d series has its states broader and mainly centered above $ E_F $ within the conduction band (CB). From the similar peak shapes there is quantum mixing between the two constituents within the VB due to the itinerant (delocalized) states. ES PDOS which arise from charge transfer are shown to extend over the VB albeit with very small intensity. When H is introduced (Fig. 3b) extra states are created in the lower part of the VB which becomes more extended and broadened, as well as just below $ E_F $. Simultaneously the intensity of Zr PDOS within the VB becomes smaller. This pertains to the chemical role of H which should bind differently to the Zr and Ni metal sublattices through its s, p valence basis set. With respect to Fig. 3a ES PDOS are now larger and seen to prevail in the lower part of the VB as charge transfer within ES comes from Zr, Ni as well as H. From both PDOS plots which run similar to actual atomic species, the presence of ES ensures for the covalence.

The presence of both 3d (Ni) and 4d (Zr) transition metals might raise the problem of the effect of self-interaction error on the relevant orbitals. This pertains to the interaction of the electron with itself, present in the used DFT functional. This causes a spread out of the charge distribution, leading to non physical metallisation for the system which can be a problem for insulating systems. In this case the 'classic' DFT functionals are no more sufficient and calling for other schemes such as LDA+U (Hubbard U) and self-interaction correction (SIC) becomes necessary [28]. On the contrary ZrNi as well as its hydrides are all metallic and itinerant states which enable for the chemical bonding within the VB involve a delocalization of a small part of d states.

### 4.2. Chemical bonding
Fig. 4 shows the metal-H interactions for the two hydrogen sites $ \text{H}_1 $ and $ \text{H}_2 $ which interact with both Zr and Ni. The major part of the VB is of bonding character (negative ECOV intensities), i.e. up to $ -2 $ eV where antibonding states start to occur. The main contribution to the bonding arises from Ni-H interactions due to systematically larger Zr-H separations: $ \langle d_{\text{Zr-H}} \rangle \sim 1.95\ \mathring{\text{A}} $ while $ \langle d_{\text{Ni-H}} \rangle \sim 1.75\ \mathring{\text{A}} $. However the larger intensity for $ \text{Ni-H}_1 $ versus $ \text{Ni-H}_2 $ bonds cannot be due to distance criteria because of their close magnitudes: $ \text{d(Ni-H}_1\text{)/d(Ni-H}_2 = 1.783/1.772 $. It can be rather suggested that the coordination polyhedra are at the origin of this feature (cf. Fig. 1): $ [\text{Zr}_3\text{Ni}_2] $ trigonal bipyramids for $ \text{H}_1 $ and $ [\text{Zr}_3\text{Ni}] $ tetrahedra for $ \text{H}_2 $, i.e. with twice more Ni nearest neighbors for $ \text{H}_1 $. Within a conceptual molecular orbital (MO) scheme one may expect $ \sigma $ Ni-H bonding involving low energy lying itinerant states (s, p like) up to $ -4 $ eV, then $ \pi $-type in the range $ [-4,-2 $ eV] involving d states; this is followed by the antibonding counterparts: $ \pi^* $ from $ -2 $ to 1 eV above $ E_F $ and lastly $ \sigma^* $ from 2 to 6 eV. Needless to say that this schematic view shows little separation between the levels due to their merging into bands on one hand and to the covalent character of the system; i.e. this MO like scheme would stand better for an ionic hydride such as $ \text{Mg}_2\text{FeH}_6 $ [29] or $ \text{K}_2\text{PtH}_6 $ [30].

![](./images/811866782133387265_4.jpg)

Fig. 4. Metal-H bonding in $ \text{ZrNiH}_3 $.

### Conclusion
The aim of this work was to address the crystal and electronic structure changes due to hydrogen insertion within ZrNi within DFT methodology. Besides the experimentally evidenced $ \text{ZrNiH}_3 $ and for the purpose of establishing trends in stability, the investigation was extended to two hypothetic hydrides: $ \text{ZrNiH}_2 $ and ZrNiH. From energy versus volume curves, these are found to be metastable but would play a role as intermediate phases in a stepwise desorption mechanism of hydrogen. The analyses of the DOS and chemical bonding point to large changes within the valence band with new states brought by hydrogen and to stronger Ni-H versus Zr-H bonds. It can be suggested that this metal-hydrogen bonding should play a role in the hardening of the alloy as observed from the increase of bulk moduli. Further a reinforcement of $ \text{Ni-H}_1 $ bonds is due to its particular environment with twice more Ni atoms.

### Acknowledgements
Computational facilities provided by the University Bordeaux 1, Pôle M3PEC-Mésocentre are acknowledged.

### References
[1] X. Huang, G.J. Ackland, K.M. Rabe, Nature Mater. 2 (2003) 307.
[2] E.L. Semenova, Y.V. Kudryavtsev, J. Alloys Compd. 203 (1994) 165.
[3] W.L. Korst, Acta Cryst. 66 (1962) 370.
[4] K. Fukuda, in: Proceedings of WE-NET Hydrogen Energy Symposium, Tokyo, 1999.
[5] J.-L. Bobet, E. Grigorova, B. Chevalier, M. Khrussanova, P. Peshev, Intermetallics 14 (2006) 208.
[6] M. Nakhl, J.-L. Bobet, B. Chevalier, B. Darriet, J. Metastable Nanocryst. Mater. 10 (2000) 637.
[7] P. Hohenberg, W. Kohn, Phys. Rev. 136 (1964) 864.
[8] W. Kohn, L.J. Sham, Phys. Rev. 140 (1965) 1133.
[9] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.
[10] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.
[11] G. Kresse, J. Joubert, Phys. Rev. B 59 (1999) 1758.
[12] J. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[13] M. Methfessel, A.T. Paxton, Phys. Rev. B 40 (1989) 3616.
[14] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[15] A.R. Williams, J. Kübler, C.D. Gelatt, Phys. Rev. B 19 (1979) 6094.
[16] V. Eyert, The Augmented Spherical Wave Method - A Comprehensive Treatment, Lecture Notes in Physics, vol. 719, Springer, Berlin Heidelberg, 2007.
[17] Z. Wu, R.E. Cohen, Phys. Rev. B 73 (2006) 235116.
[18] V. Eyert, K.-H. Höck, Phys. Rev. B 57 (1998) 12727.
[19] G. Bester, M. Fähnle, J. Phys.: Condens. Matter 13 (2001) 11541.
[20] M.E. Kirkpatrick, D.M. Bailey, J.F. Smith, Acta Cryst. 115 (1962) 252.
[21] S.W. Peterson, V.N. Sadana, W.L. Korst, J. de Phys. (Paris) 25 (1964) 451.
[22] F. Birch, J. Geophys. Res. 83 (1978) 1257.

[23] O.I. Velikikhatnyi, P.N. Kumta, Mater. Sci. Eng. B 140 (2007) 114.

[24] A. Balakrishnan, V. Smith, B.P. Stoicheff, Phys. Rev. Lett. 68 (1992) 2149.

[25] S.F. Matar, Solid State Sci. (2009), doi:10.1016/j.solidstatesciences.2009.01.004.

[26] T. Haraki, N. Inomata, H. Uchida, J. Alloys Compd. 407 (1999) 293.

[27] L. Pauling, Nature of the Chemical Bond, third edn., Cornell University Press, Ithaca, NY, 1960. p. 88107.

[28] P. Cortone, Phys. Rev. A 38 (1988) 3850.

[29] S.V. Halilov, D.J. Singh, M. Gupta, R. Gupta, Phys. Rev. B 70 (2004) 195117.

[30] S.F. Matar, unpublished results, 2009.