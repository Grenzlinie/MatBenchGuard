# A first-principles study of the La-H system

G. Schöllhammer$^{\rm a}$, W. Wolf$^{\rm b}$, P. Herzig$^{\rm a,}$, K. Yvon$^{\rm c}$, P. Vajda$^{\rm d}$

$^{\rm a}$ Institut für Physikalische Chemie, Universität Wien, Währinger Straße 42, 1090 Wien, Austria
$^{\rm b}$ Materials Design s. a. r. l., 44, av. F.-A. Bartholdi, 72000 Le Mans, France
$^{\rm c}$ Laboratoire de Cristallographie, Université de Genève, Quai Ernest-Ansermet 24, 1211 Genève 4, Switzerland
$^{\rm d}$ Laboratoire des Solides Irradiés, École Polytechnique, 91128 Palaiseau Cedex, France

---

## ARTICLE INFO

**Article history:**
Received 30 June 2008
Received in revised form 2 October 2008
Accepted 2 October 2008
Available online 25 November 2008

**PACS:**
81.05.Je
71.15.Mb
71.15.Nc
61.72.J-
78.20.Bh

**Keywords:**
Metal hydrides
Electronic properties
Computer simulations

## ABSTRACT

Results from first-principles investigations of the structural, electronic, and vibrational properties for three concentration ranges (stoichiometries close to elemental La, $\text{LaH}_2$, and $\text{LaH}_3$) within the La-H system are presented.

© 2008 Elsevier B.V. All rights reserved.

---

## 1. Introduction

The binary La-H system is of great interest, because of a concentration-dependent metal-insulator transition at a composition near $\text{LaH}_{2.8}$ [1] and the "switchable mirror" phenomenon for thin La films [2]. However, not much is known about details of the crystal structure and of the phase diagram as well as the mechanism of the metal-insulator transition.

Elemental La exists as a double-hexagonal close-packed (dhcp) phase below $\sim$310 ∘C. The homogeneity range of the solution of H in the dhcp phase is very narrow. $\text{LaH}_2$, which shows metallic behaviour, crystallizes in the fluorite structure with all tetrahedral interstices of the fcc La lattice occupied and all octahedral sites vacant. As additional H is incorporated in the octahedral interstices of the La lattice, a composition of $\text{LaH}_3$ is reached. However, these octahedral H atoms of the cubic $\text{LaH}_{3-x}$ phase ($x>0$) are generally not located in the centres of the metal-atom octahedra [3], but are displaced along the $\langle 1\ 1\ 1\rangle$ direction towards the tetrahedral interstices. In $\text{LaH}_{2.96}$ these displacements are as large as 0.37 Å [3] and lead to a pronounced shortening of the La-H bonds. This effect has been related to the size of the rare-earth atom and the compositional range of the cubic fcc phase [4]. Recently [5] it has been shown that displacements of octahedral H atoms of this magnitude may be caused by H vacancies in adjacent tetrahedral interstices for which the presence of a few percent cannot be excluded by standard experimental techniques.

For the present investigation we have performed first-principles calculations for ordered model structures. For the dhcp lattice they have been obtained from the $2\times 2\times 1$ and $3\times 3\times 1$ supercells of the conventional unit cell (containing 16 and 36 La atoms, respectively) and for the fcc lattice from either the $2\times 2\times 2$ supercell of the cubic unit cell (32 La atoms) or a rhombohedral cell with 16 La atoms spanned by the basis vectors resulting from considering the 32-atom cell as formally being body centred. The H atoms have been placed at the tetrahedral and/or octahedral sites; structure optimizations and total-energy calculations have been performed.

## 2. First-principles calculations

For the performed structure optimizations and total energy calculations the Vienna ab initio simulation package (VASP)

---

* Corresponding author. Tel.: +43 1 4277 9524; fax: +43 1 4277 9524.
E-mail address: peter.herzig@univie.ac.at (P. Herzig).

0925-8388/$ – see front matter © 2008 Elsevier B.V. All rights reserved.
doi:10.1016/j.jallcom.2008.10.009

[6-8] has been used. By this method the Kohn-Sham equations of density functional theory (DFT) [9,10] with periodic boundary conditions are solved within a plane-wave basis set with electron-ion interactions described by the projector augmented wave (PAW) method [11,12]. The applied lanthanum PAW potential includes 5s5p6s5d4f. Exchange and correlation have been treated within the generalized gradient approximation (GGA) by Perdew et al. [13]. Reciprocal space sampling has been performed using Monkhorst-Pack $k$-meshes [14] and reciprocal-space integration has been performed by the linear tetrahedron method [15,16] including the Blöchl correction [17]. Optimization of structural parameters has been achieved by minimization of atomic forces and stress tensors applying the conjugate gradient technique.

A reference energy for ${\rm H}_2$ has been obtained by consistently computing the VASP total energy of a single ${\rm H}_2$ molecule in a sufficiently large otherwise empty simulation cell to exclude interactions between translation-symmetry copies; the H-H bond length has been optimized.

Phonon dispersions have been calculated from first principles by the direct method using the MedeA-Phonon software [18].

Electron densities have been calculated with the full-potential linearized augmented plane-wave (FLAPW) method (see [19] and references therein) using an exchange-correlation potential by Hedin and Lundqvist [20].

### 3. ${\rm LaH}_x$, $x \leq 0.125$

For elemental La the dhcp structure has turned out to be vibrationally and energetically stable at zero temperature. We have probed compositions from pure La to ${\rm LaH}_{0.125}$ by inserting one or two octahedral or tetrahedral H atoms into the dhcp ${\rm La}_{36}$ and ${\rm La}_{16}$ cells as well as into the fcc ${\rm La}_{32}$ and ${\rm La}_{16}$ cells. The resulting 79 structures have been optimized and their total energies have been calculated.

Comparing phonon dispersions for dhcp ${\rm La}_{36}{\rm H}$ with fcc ${\rm La}_{32}{\rm H}$ on the one hand and dhcp with fcc ${\rm La}_{16}{\rm H}$ on the other hand, it has turned out that for the lower H content (${\rm La}_{36}{\rm H}$ and ${\rm La}_{32}{\rm H}$: $c_{\rm H} \approx 3$ atom%) as well as for pure La the dhcp structure is vibrationally stable and the fcc structure is vibrationally unstable, whereas for the higher content in ${\rm La}_{16}{\rm H}$ ($c_{\rm H} \approx 6$ atom%) the fcc phase is vibrationally stable and the dhcp phase is vibrationally unstable.

![](./images/811887076235542528_1.jpg)

Fig. 1. Electronic band structure for ${\rm La}_{32}{\rm H}_{94}$ with two octahedral vacancies $3.9\,\text{\AA}$ apart (Brillouin zone corresponding to orthorhombic primitive Bravais lattice; energy scale with respect to Fermi energy).

![](./images/811887076235542528_2.jpg)

Fig. 2. Contour maps of the electron densities in the (1 1 0) plane for the first (top) and the second band (centre) below the Fermi level for ${\rm La}_{32}{\rm H}_{94}$ with two octahedral H vacancies $3.9\,\text{\AA}$ apart (see Fig. 1). The superimposed grey shadings may help to discern the regions of higher electron density (lighter grey areas) due to the two parallel La-La bonds across the H vacancies. The sketch at the bottom shows the positions of the atoms in the (1 1 0) plane, ${\rm H}^0$ and ${\rm H}^{\rm T}$ symbolize octahedrally and tetrahedrally coordinated H atoms, respectively.

This change of the phase stability is in agreement with the change of the formation energy, i.e. the reaction energy for
$$m\,\text{La}^{\text{dhcp}} + \left(\frac{1}{2}\right)\,{\rm H}_2 \rightarrow {\rm La}_m{\rm H}, \quad m=36,32,16$$
calculated from the total energies of the respective model structures and appropriate reference energies for La and for the ${\rm H}_2$ molecule.

Furthermore – and very surprisingly – it follows from the analysis of the total energies that the occupation of an octahedral interstitial site is energetically more favourable than the occupation of a tetrahedral site by $\sim 15\,\text{kJ/mol}\,{\rm H}_2$ (dhcp model structures) or $\sim 27\,\text{kJ/mol}\,{\rm H}_2$ (fcc model structures). This does not seem to have been verified yet experimentally.

For the 71 possible structures containing 2 H atoms per $La_{32}$ cell or $La_{16}$ cell, linear H-La-H arrangements with La-H distances of $\sim2.5\mathring{A}$ have turned out to be energetically favourable.

All investigated model structures have been found to be energetically destabilized by about 0.7-4.9 kJ/mol per La atom with respect to the phase segregation

$$\mathrm{LaH}_x \to \left(\frac{x}{2}\right)\mathrm{LaH}_2 + \left(1 - \frac{x}{2}\right)\mathrm{La}^{\mathrm{dhcp}}.$$

### 4. $\mathrm{LaH}_2$ and stoichiometries close to the dihydride

Stoichiometric $\mathrm{LaH}_2$ with fluorite structure is energetically stabilized by $\sim35$ kJ/mol per formula unit with respect to the phase separation into $\mathrm{La}^{\mathrm{dhcp}}$ and $\mathrm{LaH}_3$ (optimized orthorhombic structure, cf. Section 5). In addition, it is vibrationally stable.

Thirty-two model structures have been constructed based on the $\mathrm{La}_{32}\mathrm{H}_{64}$ cell and the rhombohedral $\mathrm{La}_{16}\mathrm{H}_{32}$ cell in the concentration range from $\mathrm{LaH}_{1.875}$ to $\mathrm{LaH}_{2.125}$.

The shift of a tetrahedral H atom in the stoichiometric dihydride to an octahedral site results in a loss of energy of $\sim180$ kJ/mol per $\mathrm{H}_2$. Adding hydrogen to the stoichiometric dihydride releases $\sim100$ kJ/mol per $\mathrm{H}_2$; the resulting super-stoichiometric model structures are stabilized by about 0.20-0.58 kJ/mol per La atom with respect to the phase separation into $\mathrm{LaH}_2$ and orthorhombic $\mathrm{LaH}_3$ (see below). Removing hydrogen requires about 270 kJ/mol per $\mathrm{H}_2$; the resulting sub-stoichiometric models are destabilized by about 1.3-4.9 kJ/mol per La atom with respect to the phase segregation into $\mathrm{LaH}_2$ and $\mathrm{La}^{\mathrm{dhcp}}$. The structure models for the sub-stoichiometric and super-stoichiometric dihydrides studied so far are vibrationally stable.

### 5. $\mathrm{LaH}_3$ and stoichiometries close to the trihydride

For stoichiometric $\mathrm{LaH}_3$, structure optimization for an $\mathrm{La}_{32}\mathrm{H}_{96}$ unit cell has led to an orthorhombically distorted structure ($Z$=4, lattice parameters: $a$=$8.010\mathring{A}$, $b$=$5.289\mathring{A}$, $c$=$4.079\mathring{A}$, corresponding to a change of cell dimensions of +1.9%, $-4.8\%$, +3.3% with respect to the cubic unit cell) which is about 2.1 kJ/mol per formula unit more stable than the ideal cubic structure. The distortion is accompanied by a volume increase of $\sim0.7\%$ and by large changes in the interatomic distances. Phonon calculations show that the undistorted cubic structure is unstable and the distorted structure is stable.

Starting from the $2 \times 2 \times 2$ supercell for $\mathrm{LaH}_3$ we have removed up to six H atoms (both octahedral and tetrahedral) and performed optimizations for about 50 different structures. For $\mathrm{La}_{32}\mathrm{H}_{94}$ ($\mathrm{LaH}_{2.94}$) with two octahedral H vacancies the most stable arrangement has turned out to be the one where the vacancies are $3.9\mathring{A}$ apart. The band structure for this model structure exhibits a band gap (Fig. 1) as expected from experiment. In Fig. 2 electron densities for the first two bands below the Fermi level are shown. These bands are mainly determined by the d states of the La atoms adjacent to the H vacancies which form bonds across these vacant sites. An analogous, but energetically less favourable bond formation leading to the opening of a band gap is always found (of course, only for cells containing an even number of electrons) when at least one octahedral H position is empty and also in the case of some structures with only tetrahedral H vacancies.

### 6. Résumé

For small H concentrations the occupation of octahedral interstitial sites is preferred both in dhcp and fcc La. Increasing H concentration stabilizes the cubic phase.

For stoichiometric $\mathrm{LaH}_3$ a stable orthorhombic structure has been found. For stoichiometries close to $\mathrm{LaH}_3$ pairs of octahedral H vacancies at the shortest possible distance ($3.9\mathring{A}$) are the energetically most favourable vacancy arrangements. For such pairs, as well as for many other vacancy arrangements close to $\mathrm{LaH}_3$, a band gap opens. This is caused by a vacancy-induced formation of energetically favourable La-La bonds and the lowering of the respective La-d states below the Fermi level.

Further investigations aimed at a first-principles study covering the complete composition range of the La-H phase diagram are in progress.

### Acknowledgement

This work has been supported by the Austrian Science Fund (FWF project no. P19205-N19).

### References

[1] P. Vajda, in: K.A. Gschneidner Jr., L. Eyring (Eds.), Handbook on the Physics and Chemistry of Rare Earths, vol. 20, Elsevier, Amsterdam, 1995, p. 207.
[2] J.N. Huiberts, R. Griessen, J.H. Rector, R.J. Wijngaarden, J.P. Dekker, D.G. de Groot, N.J. Koeman, Nature (Lond.) 380 (1996) 231.
[3] P. Fischer, W. Hälg, L. Schlapbach, K. Yvon, J. Less-Common Met. 60 (1978) 1.
[4] G. Renaudin, P. Fischer, K. Yvon, J. Alloys Compd. 330-332 (2002) 175.
[5] G. Renaudin, K. Yvon, W. Wolf, P. Herzig, J. Alloys Compd. 404-406 (2005) 55.
[6] http://cms.mpi.univie.ac.at/vasp/; http://www.materialsdesign.com/medea-vasp.htm.
[7] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.
[8] G. Kresse, J. Furthmüller, Comput. Mater. Sci. 6 (1996) 15.
[9] P. Hohenberg, W. Kohn, Phys. Rev. 136 (1964) B864.
[10] W. Kohn, L.J. Sham, Phys. Rev. 140 (1965) A1133.
[11] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.
[12] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758.
[13] J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh, C. Fiolhais, Phys. Rev. B 46 (1992) 6671.
[14] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[15] O. Jepsen, O.K. Andersen, Solid State Commun. 9 (1971) 1763.
[16] G. Lehmann, M. Taut, Phys. Status Solidi 54b (1972) 469.
[17] P.E. Blöchl, O. Jepsen, O.K. Andersen, Phys. Rev. B 49 (1994) 16223.
[18] MedeA-Phonon, Materials Design Inc., Angel Fire, NM, 2004.
[19] H.J.F. Jansen, A.J. Freeman, Phys. Rev. B 30 (1984) 561.
[20] (a) L. Hedin, B. Lundqvist, J. Phys. C: Solid State Phys. 4 (1971) 2064; (b) L. Hedin, S. Lundqvist, J. Phys. Coll. 33 (1972) 73, C3.