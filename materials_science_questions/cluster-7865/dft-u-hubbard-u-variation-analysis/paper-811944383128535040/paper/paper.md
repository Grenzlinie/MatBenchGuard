# Electronic structure and magnetism of Eu-doped GaN: first-principles study based on LDA+U

This article has been downloaded from IOPscience. Please scroll down to see the full text article.

2008 J. Phys. D: Appl. Phys. 41 035004

(http://iopscience.iop.org/0022-3727/41/3/035004)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:
IP Address: 128.250.144.144
The article was downloaded on 14/09/2013 at 14:37

Please note that [terms and conditions apply].

# Electronic structure and magnetism of Eu-doped GaN: first-principles study based on LDA + U

S Goumri-Said¹ and M B Kanoun²,³

¹ Laboratoire de Physique de l'Etat Condensé, UMR CNRS 6087, Institut de Recherche en Ingénierie Moléculaire et Matériaux Fonctionnels, FR CNRS 2575 Université du Maine, Avenue Olivier Messiaen-72085, Le Mans Cedex 9, France
² Laboratoire de Métallurgie Physique, UMR 6630 du CNRS, Université de Poitiers, Bt. SP2MI, Bd Pierre et Marie Curie, BP 30179, 86962 Futuroscope, Chasseneuil Cedex, France

E-mail: Souraya.Goumri-Said@univ-lemans.fr

Received 18 June 2007, in final form 27 November 2007
Published 11 January 2008
Online at stacks.iop.org/JPhysD/41/035004

## Abstract
Electronic and magnetic properties of the rare-earth-doped III-nitride semiconductor $\mathrm{Ga_{1-x}Eu_xN}$ ($x=0.0625$) is studied with the full potential (linearized) augmented plane wave method plus the local orbitals method, where we have explored the electronic and magnetic properties of the ferromagnetic $\mathrm{Ga_{1-x}Eu_xN}$ in the zinc-blende phase. The existence of Eu 4f orbitals has demonstrated that the common local density approximation leads to quantitatively and qualitatively wrong results, while the LDA + U method performs much better. In this paper we present only the results related to the LDA + U method. It is found from the calculation of density of states that the Eu f orbitals spin-polarize the host system and they are predominant in this diluted magnetic semiconductor. The magnetic description is achieved by the calculation of spin densities difference contours and the magnetic moment.

(Some figures in this article are in colour only in the electronic version)

---

## 1. Introduction

The miniaturization in microelectronics and the need for functional compounds have brought up many new tasks in material processing. Due to the constantly shrinking length scale a deeper understanding of the structure and the interfaces of the applied materials is indispensable. The field of 'spintronic' involves the spin of the electrons as a new parameter and opens up a new class of electronics. Furthermore, semiconductor-based spintronics may present a greater wealth of possibilities, which is different from metallic spin devices that just provide new ways to store and read information in hard disks, tapes or MRAM. Consequently the electronic and magnetic properties of diluted magnetic semiconductors (DMSs) are of particular interest to offer a pathway between a magnetic information and an optical signal [1,2].

Experimentally, it has been attempted to grow transition-metal (TM)-doped and rare-earth (RE)-doped GaN in order to improve the Curie temperature. Ferromagnetic order was observed in GaCrN, GaGdN and GaDyN samples even at high temperatures [3,4]. Moreover it has been proven that rare-earth doping of GaN appears to be an alternative way for the realization of light-emitting diodes in the visible range, and it has spurred interest in GaN doped with Eu, Sm or Pr (red emission), Tm (blue) and Er, Ho or Tb (green). The rare-earth doping option is particularly attractive in the case of red and green light as a possible way in which to elude problems related to the growth of InGaN with high In content [5–9].

Theoretically, most of the materials that have been studied are semiconductors doped with partially filled 3d transition metals. Because of the strong coupling between the magnetic ions 3d states and the coupling to the host p states, diluted magnetic nitride and oxide semiconductors have been predicted and, in some cases, observed to show hole-mediated ferromagnetic behaviour above room temperatures [10]. These calculations showed also that V-, Mn- and Cr-doped GaN

³ Also affiliated to Equipe Physique de l'Etat Solide, LPT, Département de Physique, Faculté des Sciences, Université de Tlemcen, BP 13000, Tlemcen, Algeria.

are promising candidates as room temperature ferromagnetic semiconductors and that Cr-doped GaN has the most stable ferromagnetic states.

In the area of RE-doped semiconductors, a recent theoretical study by first-principles calculation was performed for $Ga_{1-x}Gd_xN$ ($x = 0.25$) and showed that the interactions between Gd atoms in undoped $Ga_{1-x}Gd_xN$ are antiferromagnetic in nature, but this can be changed by introducing donors to the material; different from most 3d DMSs, ferromagnetism in $Ga_{1-x}Gd_xN$ is electron mediated [11]. In fact, on one hand, 4f orbitals are more localized and the direct coupling between the 4f ions may be weak. On the other hand, 4f RE elements can have larger magnetic moments than the 3d elements, and, unlike the d states, f electrons can couple strongly with the host s electrons, leading to the possibility of electron-mediated ferromagnetism in these materials. It can therefore be anticipated that for a Eu impurity in cubic $Ga_{1-x}Eu_xN$ LDA is incapable of describing correctly the interaction between these localized and strongly correlated 4f electrons and the itinerant 3d states of the host material. This could be overcome by treating the 4f states as core states, an approach that has been used in the past with some success for lanthanides and some RE elements [12-14]. In this way, however, one forces the f electrons to behave exactly as in free atoms, which is not entirely correct. An efficient and popular way to improve on the LDA failure without resorting to fully atomic 4f behaviour is to use the LDA + U method [15-17]. In LDA + U, the correlation absent in LDA is reintroduced by an on-site Coulomb repulsion parameter $U$, to which an a priori value has to be assigned. The LDA + U method has been used in some recent works with considerable success [18].

To get a deep understanding of the nature of magnetic coupling in these RE-doped systems, in this work, we perform total energy calculation of $Ga_{0.9375}Eu_{0.0625}N$. The paper is organized as follows. In the next section, we briefly describe computational details, the employed method and the supercell. Section 3 is devoted to the electronic properties; mainly the density of states (DOS) and the calculation of exchange constants are described. In section 4, we present our calculated magnetic properties. The paper ends with the main conclusions about the electronic structure and magnetism of $Ga_{0.9375}Eu_{0.0625}N$.

## 2. Computational details

Our calculations were performed within density functional theory (DFT) [19] using the augmented plane waves + the local orbitals (APW + lo) method as implemented in the WIEN2k package [20] to solve the scalar relativistic Kohn- Sham equations. In the APW + lo method, the wave functions are expanded in spherical harmonics inside non-overlapping atomic spheres of radius $R_{MT}$, and in plane waves in the remaining space of the unit cell (= the interstitial region). For N and Ga atoms $R_{MT}$ values of 1.50 and 1.9 (a.u.) were chosen, while for the RE impurity we used $R_{MT}=2.6$ (a.u.). The maximum $l$ for the expansion of the wave function in spherical harmonics inside the spheres was taken to be $l_{max}=10$. The plane wave expansion of the wave function in the interstitial
![](./images/811944383128535040_1.jpg)

Figure 1. The supercell used in the calculations.

region was made up to $K_{max}=7.5/R_{MT}^{min}$ and the charge density was Fourier expanded up to $G_{max}=16$. For the LDA + U method, we use the scheme introduced by Anisimov et al [21] with an approximate correction for the self-interaction correction (SIC). This is probably best suited for our system and for a full potential method we use an effective $U_{eff}=U-J$, setting $J=0.07$ and $U=0.44$ (Ry) for Eu atom [22].

In order to reproduce the situation of an isolated Eu impurity in zinc-blende GaN, we use the supercell approach with a cubic supercell having a symmetry of a simple cubic lattice for the 32-atoms/cell. The infinite crystal is constructed by exact replications of this supercell, all Eu atoms have the same neighbouring atoms and possess the same spin. Consequently the $Ga_{1-x}Eu_xN$ phases so constructed are ferromagnetic and ordered (see figure 1). The $k$ integration over the Brillouin zone is performed using Monkhorst and Pack [23] mesh, yielding to 90k points for the supercell calculations. The self-consistent calculations are considered to be converged only when the calculated total energy of the crystal converge to less than 1 mRy.

The lattice constant of $Ga_{1-x}Eu_xN$ (with $x=0.0625$) is determined by fitting the data obtained from the self-consistent calculations of energy versus the volume of the supercell to the Murnaghan equation of state [24]. It is important to note here that the virtual crystal approximation (VCA) is checked and we find that $a^{VCA}=xa^{AC}+(1-x)a^{BC})$, where $a^{AC}=a^{EuN}=5.2499$ Å and $a^{BC}=a^{GaN}=4.461$ Å [25]. The equilibrium lattice parameter for $Ga_{0.9375}Eu_{0.0625}N$ is found equal to 4.51 Å.

## 3. Electronic properties

In order to understand the electronic structure of the ferromagnetic $Ga_{0.9375}Eu_{0.0625}N$, we calculate the total DOS as shown in figure 2. We also display the partial densities of Eu 4f orbitals. One can see that by applying the LDA + U

![](./images/811944383128535040_2.jpg)

Figure 2. Total and partial DOS of $Ga_{1-x}Eu_xN$ (with $x=0.0625$). The vertical line denotes the position of the Fermi energy, which has been chosen to be 0.0 (eV).

approximation, we do not observe the overlapping of orbitals with the $E_F$ level situated at 0 eV as observed when we use the purely LDA. Moreover, when we carefully examine this result, we observe the dominance of Eu 4f to majority spin in the valence band (VB) and of the minority spin in the conduction band. We observe that the spin up Eu 4f are centred at $(-2.1\ \text{eV})$ in the VB and are empty for the conduction band (CB) and vice versa for spin down bands, they are empty in VB and centreed at 2.92 (eV) with a more localized peak at 2.4 eV. Furthermore, we can deduce the effective f band exchange $(x)$ splitting $\Delta_x(f)$, which is defined as the separation between the corresponding spin up and spin down peaks. It is found equal to $-7.98\ \text{eV}$. In order to illustrate and quantify the nature of the attraction in the $Ga_{1-x}Eu_xN$, we calculate the exchange splitting $\Delta = E_v^\uparrow - E_v^\downarrow$ of the top of the valence bands for spin up and spin down. We find it equal to $+0.095\ (\text{eV})$. The negative value of $\Delta_x(f)$ and the positive value of exchange splitting indicate that the effective potential for the majority spin is more attractive than that for the minority spin, which the opposite of the other DMSs doped by transition metals as Mn [26], where d bands play an important role. One can conclude this description that this unusual behaviour is mainly due to the f orbitals.

In order to complete the electronic description, it has been shown that the ferromagnetic band structure calculations can be used to estimate the exchange constants $N_0\alpha$ and $N_0\beta$. Assuming the usual Kondo interactions, these coefficients are defined in [1,2,10,26]. We calculate the exchange constants by evaluating the spin splitting of CB and VB bands. We find a positive value for $N_0\alpha=0.21\ \text{eV}$ and a negative value for $N_0\beta=-1.09\ \text{eV}$. The net effect is that the exchange splitting at the VB $(N_0\beta)$ is smaller than that observed in TM-doped GaN [27] but does not differ much from the values in typical DMSs. They are very similar to the values observed in Mn-doped II-VI [25].

## 4. Magnetic properties

In order to explore the magnetic properties, firstly, we are interested in the calculation of the magnetic moment (see

<table><caption>Table 1. Calculated local and total magnetic moments (in $\mu_B$) inside the MT spheres of $Ga_{1-x}Eu_xN$ (with $x=0.0625$). The total moment is the sum of all the local moments and the magnetic moment of the interstitial region.</caption>
<tbody><tr><td>$M^{Total}\ (\mu_B/\text{cell})$</td><td>6.23</td></tr>
<tr><td>$M^{Eu}\ (\mu_B)$</td><td>5.83</td></tr>
<tr><td>$M^N\ (\mu_B)$</td><td>0.10</td></tr>
<tr><td>$M^{Ga}\ (\mu_B)$</td><td>0.09</td></tr>
<tr><td>$M^{\text{Interstitial}}\ (\mu_B)$</td><td>0.21</td></tr>
</tbody></table>

table 1). The main part of this magnetic moment is strongly localized on the Eu site. The additional contributions to the total magnetic moment appear to come from N and Ga atoms to Eu. When we observe more carefully the values of the different magnetic contributions, the spatial distribution of impurity states is intimately linked with the value of magnetic moments on different atoms. The total magnetic moment amounts to $6.23\ \mu_B$. In fact, one of the unique features observed in RE-doped GaN is the colossal magnetic moment, such as in recently studied Gd-doped GaN [11,27], where it was observed that (at very low Gd concentrations) $(10^{-16}\ \text{cm}^3$, the total effective magnetic moment per Gd atom could be as high as $4000\ \mu_B$. This is quite unusual because the atomic moment of Gd is only $8\ \mu_B$, and in the hypothetical zinc-blende GdN the moment per Gd is only $7\ \mu_B$ and this is a similar situation for our system $Ga_{1-x}Eu_xN$ with a $5.83\ \mu_B$ for Eu. In fact, when the Eu concentration increases, the effective moments per Eu decrease. This observation was explained through a phenomenological model, which assumes that rare-earth atoms polarize the GaN matrix in a certain radius around them and each host atom within the radius has an induced magnetic moment.

Finally, we examine the spin-density difference (difference between majority and minority spin densities). The spin density is plotted in the (1 1 0) plane around Eu atom. One can see from these contours that the main moments in the supercell come from Eu atoms. The N atoms being the nearest neighbours of Eu atoms give a negative contribution to the total moments and the Ga atoms contribute with a small positive moment. Figure 3 shows that different Eu-Eu configurations have little effects on the spin-density distribution of Eu atoms and the spin-density distribution of the nearby N atoms.

## 5. Conclusion

Electronic and magnetic properties of $Ga_{1-x}Eu_xN\ (x=0.0625)$ DMS were studied by first-principles FP-L/APW + lo calculations based on LDA + U approach. It is found that due to the existence of Eu f, $Ga_{1-x}Eu_xN$ shows some unique behaviour which is drastically different from TM-doped GaN, and the calculated exchange constants $N_0\alpha$ and $N_0\beta$ confirm this unusual behaviour. The spin-density difference for (1 1 0) plane around Eu atom showed a negative spin-density difference concentrated around the N nuclei than in the homogeneous one, especially around the N atom shared as first neighbour by both Eu atoms. This is in good agreement with the calculated total magnetic moment (i.e. $6.00\ \mu_B$) and the respective contributions of Eu, N and Ga atoms. The main

![](./images/811944383128535040_3.jpg)

Figure 3. Contour plot of spin densities difference of $Ga_{1-x}Eu_x$N (with $x = 0.0625$).

part of this magnetic moment comes from the Eu-impurity atom.

## Acknowledgments
This work was supported partially by financial and computational resources from the 'EXCITING' network and at Kaiserlautern University (Germany) and sources from 'Région de la Loire' and the CCIPL centre at Institut des Matériaux de Nantes (IMN) (France). F Calvayrac and F Boucher are acknowledged for their computational assistance.

## References
[1] Zutic I, Fabian J and Das Sarma S 2004 *Rev. Mod. Phys.* **76** 323
Awschalom D D and Kawakami R K 2000 *Nature (Lond.)* **408** 923
Dietl T, Ohno H, Matsukura F, Cibert J and Ferrand D 2000 *Science* **287** 1019

[2] Awschalom D D, Loss D and Samarth N (ed) 2002 *Semiconductors Spintronics and Quantum Computation* (Berlin: Springer)

[3] Hashimoto M, Zhou Y K, Kanamura M and Asahi H 2002 *Solid State Commun.* **122** 37

[4] Teraguchi N, Suzuki A, Nanishi Y, Zhou Y K, Hashimoto M and Asahi H 2002 *Solid State Commun.* **122** 651

[5] Lee D S and Steckl A J 2002 *Appl. Phys. Lett.* **81** 2331

[6] Morishima S, Maruyama T and Akimoto K 2000 *J. Cryst. Growth* **209** 378

[7] Morishima S, Maruyama T, Tanaka M, Masumoto Y and Akimoto K 1999 *Phys. Status Solidi a* **176** 113

[8] Hara K, Ohtake N and Ishii K 1999 *Phys. Status Solidi b* **216** 625

[9] Steckl A J, Garter M, Lee D S, Heikenfeld J and Birkhahn R 2001 *Appl. Phys. Lett.* **75** 2184
Sato K and Katayama-Yoshida H 2001 *Japan. J. Appl. Phys.* **40** L485

[10] Kanoun M B, Goumri-Said S, Merad A E and Cibert J 2005 *J. Phys. D: Appl. Phys.* **38** 1853

[11] Gustavo Dalpian M and Su-Huai Wei 2005 *Phys. Rev. B* **72** 115201

[12] Akai H, Akai M, Blugel S, Zeller R and Dederichs P H 1984 *J. Magn. Magn. Mater.* **45** 291

[13] Akai M, Akai H and Kanamori J 1985 *J. Phys. Soc. Japan* **54** 4246

[14] Akai H, Akai M and Kanamori J 1985 *J. Phys. Soc. Japan* **54** 4257

[15] Anisimov V I and Gunnarsson O 1991 *Phys. Rev. B* **43** 7570

[16] Czyżyzyk M T and Sawatzky G A 1994 *Phys. Rev. B* **49** 14211

[17] Anisimov V I, Solovyev I V, Korotin M A, Czyżyzyk M T and Sawatzky G A 1993 *Phys. Rev. B* **48** 16929
Wei S-H and Alex Zunger 1993 *Phys. Rev. B* **48** 6111

[18] Petukhov A G, Mazin I I, Chioncel L and Lichtenstein A I 2003 *Phys. Rev. B* **67** 153106
Anisimov V I, Aryasetiawan F and Lichtenstein A I 1997 *J. Phys.: Condens. Matter* **9** 767
Antonov V N, Harmon B N and Yaresko A N 2002 *Phys. Rev. B* **66** 165208
Laskowski R, Blaha P and Schwarz K 2003 *Phys. Rev. B* **67** 075102
Boukhvalov D W, Dobrovitski V V, Katsnelson M I, Lichtenstein A I, Harmon B N and Kogerler P 2003 *J. Appl. Phys.* **93** 7080

[19] Dreizler R and Gross E K U 1990 *Density-Functional Theory* (New York: Springer)

[20] Blaha P, Schwarz K, Madsen G K H, Kvasnicka D and Luitz J 2001 *WIEN2k, An Augmented-Plane-Wave + Local Orbitals Program for Calculating Crystal Properties* (Austria: Karlheinz Schwarz, Techn Wien) ISBN 3-9501031-1-2

[21] Anisimov V I, Zaanen J and Andersen O K 1991 *Phys. Rev. B* **44** 943

[22] Madsen G K H and Novak P 2005 *Europhys. Lett.* **69** 777

[23] Monkhorst H J and Pack J D 1976 *Phys. Rev. B* **13** 5188

[24] Murnaghan F D 1944 *Proc. Natl. Acad. Sci. U.S.A* **30** 244

[25] Kanoun M B, Merad A E, Cibert J, Aourag H and Merad G 2004 *J. Alloys Compounds* **366** 86
Kanoun M B, Goumri-Said S, Merad A E, Merad G, Cibert J and Aourag H 2004 *Semicond. Sci. Technol.* **19** 1220

[26] Merad A E, Kanoun M B and Goumri-Said S 2006 *J. Magn. Magn. Mater.* **302** 536

[27] Dhar S, Brandt O, Ramsteiner M, Sapega V F and Ploog K H 2005 *Phys. Rev. Lett.* **94** 037205

4