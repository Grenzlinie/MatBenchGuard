Accepted Manuscript

Title: Born-Oppenheimer Molecular Dynamics Simulation of
Pentanoic Acid Adsorption on $\alpha$-Al₂O₃

Author: André L. Martinotto Janete E. Zorzi Cláudio A.
Perottoni

![](./images/813126579478593536_1.jpg)

<table>
  <tr>
    <td>PII:</td>
    <td>S0169-4332(17)31682-3</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>http://dx.doi.org/doi:10.1016/j.apsusc.2017.06.038</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>APSUSC 36238</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>APSUSC</td>
  </tr>
  <tr>
    <td>Received date:</td>
    <td>4-12-2016</td>
  </tr>
  <tr>
    <td>Revised date:</td>
    <td>29-5-2017</td>
  </tr>
  <tr>
    <td>Accepted date:</td>
    <td>4-6-2017</td>
  </tr>
</table>

Please cite this article as: André L. Martinotto, Janete E. Zorzi, Cláudio A.
Perottoni, Born-Oppenheimer Molecular Dynamics Simulation of Pentanoic Acid
Adsorption on $\alpha$-Al₂O₃, <![CDATA[Applied Surface Science]]> (2017),
http://dx.doi.org/10.1016/j.apsusc.2017.06.038

This is a PDF file of an unedited manuscript that has been accepted for publication.
As a service to our customers we are providing this early version of the manuscript.
The manuscript will undergo copyediting, typesetting, and review of the resulting proof
before it is published in its final form. Please note that during the production process
errors may be discovered which could affect the content, and all legal disclaimers that
apply to the journal pertain.

# Born-Oppenheimer Molecular Dynamics Simulation of Pentanoic Acid Adsorption on $\alpha$-Al₂O₃

André L. Martinotto, Janete E. Zorzi, Cláudio A. Perottoni

Instituto de Materiais Cerâmicos, Universidade de Caxias do Sul, 95765-000, Bom Princípio, RS, Brazil

## Abstract

Adsorption of a single pentanoic acid ($\text{C}_5\text{H}_{10}\text{O}_2$) molecule on (0001) $\alpha$-Al₂O₃ in a vacuum was explored with the aid of Born-Oppenheimer molecular dynamics simulations. Computer simulations were carried out considering two different situations, namely a clean Al/O-terminated surface and, also, a (0001) $\alpha$-Al₂O₃ surface saturated with doubly-coordinated, isolated hydroxyls. In the first case, pentanoic acid adsorbs dissociatively, with the creation of an isolated surface hydroxyl, while the oxygen from the molecule's former carbonyl makes a bond to a nearby surface Al. On the other hand, pentanoic acid adsorbs on hydroxylated alumina by making a strong hydrogen bond to a surface oxygen, with the molecule aligning itself nearly parallel to the surface after full relaxation. For each case (i.e., pentanoic acid adsorption on Al/O-terminated or hydroxylated corundum surface), the different adsorption mechanism has a marked impact on the respective calculated infrared absorption spectrum, which can be of further use as an analytical tool to determine the underlying adsorption mechanism in actual experiments.

Keywords: $\alpha$-Al₂O₃, pentanoic acid, adsorption, molecular dynamics

---

*Corresponding author
Email address: jezorzi@ucs.br (Janete E. Zorzi)

---

Preprint submitted to Applied Surface Science
May 29, 2017

### 1. Introduction

Ceramic products are usually molded from powdered raw materials and commonly, as in the slip casting technique, the ceramic powder is first dispersed in a liquid medium. In such cases, ceramic processing must deal with the attractive interactions between ceramic particles that tend to agglomerate, difficulting processing [1]. A proper understanding of the ceramic surface chemistry and, particularly, the way it interacts to processing aid materials (such as surfactant agents) is paramount to devise strategies to overcome particle agglomeration and improve ceramics processability.

Given its widespread use, $\alpha$-Al$_2$O$_3$ (alpha-alumina or corundum) and its surface chemistry has been intensely studied over the years (see, for instance, [2, 3] and references therein). Unlike the bulk, the surface of oxide ceramic particles such as alumina is heterogeneous due to incomplete bonds and atomic rearrangements. In fact, the reactivity of alumina surface depends on the number and type of active sites, which varies among different crystallographic planes, and is affected by crystal imperfections [4]. Once a clean alumina surface is first exposed to water, there is a tendency to chemically stabilize the surface by hydroxylation [5, 6, 7]. Surface stabilization by hydroxylation can proceed in several different ways. One factor that differentiates the surface hydroxyls in alumina is the number of aluminum cations to which the OH group is coordinated, i.e., singly (Al-OH), doubly Al$_2-$OH or triply-coordinated Al$_3-$OH hydroxyls [8, 9].

The mechanism of water adsorption on alumina is particularly important and has been studied by computer simulation using several different methods [2, 10, 11, 12, 13, 14, 15]. Besides water, the adsorption of other small molecules (such as CO or O$_2$) on alumina has also been studied by computer simulation [16, 13]. The knowledge of the mechanism by which water and other gas molecules interacts to the alumina surface has practical consequences since the adsorption of such chemical species can reduce the number of active sites or change the way other molecules (such as processing aid agents) react with the surface.

Computer simulations of larger molecules interacting to the alumina sur-


face include studies on nitromethane and 1,1-diamino-2,2- dinitroethylene [17], glycine [18], formic acid [19, 20, 21], acetic and propionic acids [20], to cite just a few. Long chain carboxylic acids are often used as surfactants, as they promote steric repulsion between the ceramic oxide particles, thus improving their dispersion in liquid media. Pentanoic acid ($\mathrm{C_5H_{10}O_2}$) is a carboxylic acid with an intermediate carbon chain (longer than that of propionic acid but still amenable to computer simulations based on density functional theory), which makes it prone to find a minimum energy configuration in which the molecule is oriented either perpendicularly or parallel to the alumina surface. The actual way the molecules of pentanoic acid will orient themselves relatively to the alumina surface will possibly be affected by the chemical state of the ceramic surface (i.e., how the surface is terminated) and how the molecule is bonded to the top surface atoms. All this will further affect the corresponding infrared spectrum, which can thus be used as an experimental probe to infer on the particular adsorption mechanism in different experimental conditions.

In this work, Born-Oppenheimer molecular dynamics simulations were performed to explore the adsorption mechanism of pentanoic acid on the (0001) surface of $\mathrm{\alpha-Al_2O_3}$ in a vacuum, for both Al/O-terminated (anhydrous) and $\mathrm{Al_2O-H}$ (hydroxylated) surfaces. In each case, the corresponding infrared spectrum of the fully relaxed structure was also calculated. It is expected that the characteristic infrared absorption bands in the calculated spectra can be used as a guide to identify the way pentanoic acid (and similar carboxylic acids) interacts with the alumina surface in actual experiments.

## 2. Computational Details

All the calculations were performed according to Density Functional Theory (DFT) using Quantum Espresso and nonlinear core correction, scalar relativistic Rappe-Rabe-Kaxiras-Joannopoulos ultrasoft pseudopotentials. [22, 23] The calculations were performed for a 3x3 supercell slab model using periodic boundary conditions, with slabs separated by a vacuum region of $25\ \mathrm{\mathring{A}}$ to avoid unphysical

interactions. The exchange-correlation potential was taken into account in the generalized gradient approximation (GGA) using the Perdew-Burke-Ernzerhof functional for solids (PBESOL) [24]. The kinetic-energy cutoffs for valence electron wave functions and charge density were set as 60 Ry and 600 Ry, respectively. The reciprocal space sampling was restricted to the $\Gamma$ point. Both the reciprocal space sampling and the energy cutoff ensured total energy convergence within 1 mRy/atom. Dispersion interactions were included using Grimme's semiempirical correction [25].

The initial 3x3 supercell Al-terminated slab model for the $\alpha$-Al$_2$O$_3$ (0001) surface was created using Crystal06.[26]. A second surface, terminated by doubly-coordinated, isolated hydroxyls (Al$_2$O$-$H), was created by substituting H for the top Al atoms. Both surfaces had the top atomic layers fully relaxed in a vacuum, using the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm, before the introduction of the pentanoic acid molecule into the system. The uppermost layers of the corundum slabs were fully relaxed while the atoms at the two bottom layers were kept fixed at their respective positions in the corundum bulk structure. After optimization of the top surface layers, a single pentanoic acid molecule was added to the system, its lower end (the acidic group) positioned ca. $3\,\mathrm{\mathring{A}}$ above the surface. Born-Oppenheimer molecular dynamics (MD) calculations on the electronic ground state were thus performed using a time step of 20 Rydberg atomic units (approximately 0.967 56 fs). The system was allowed to evolve for about 630 fs and 1200 fs for the clean and the hydroxylated surfaces, respectively. These relatively short MD simulations were carried out just to the point in which the pentanoic acid molecule makes a chemical bond to the corundum surface. After that, both systems were further relaxed using the BFGS algorithm, with convergence thresholds for total energy and forces set to 0.01 mRy and 0.1 mRy/bohr, respectively. All figures representing snapshots of the simulated systems were generated using Jmol [27]. Finally, infrared spectra were calculated according to density functional perturbation theory (DFPT), [22] keeping the atoms of lower layers fixed at their equilibrium positions.


### 3. Results and Discussion

The (0001) corundum 3x3 supercell used in the calculations is represented in Fig. 1. Also in this figure, the clean and hydroxylated surfaces are represented both before and after optimization of the uppermost atomic layers. The dynamics of surface relaxation before the inclusion of the pentanoic acid molecule is also presented as computer animations available as supplementary materials [28, 29]. After relaxation, the uppermost oxygen and aluminum atoms lie almost in the same plane at the top layer of the initially Al-terminated surface, with the outermost Al atoms slightly displaced toward the vacuum, as previously reported in the literature [11]. On the other hand, the top layers of the $Al_2O-H$ surface keep the alternacy of Al and O layers, with doubly-coordinated isolated hydroxyls forming a rather regular pattern. Such long-range ordering of hydroxyls at the top of the $Al_2O-H$ surface results from energy minimization in the athermal limit and most surely should not be present in systems equilibrated at higher temperatures or even real hydroxylated alumina surfaces. However fictitious, this ordering of surface hydroxyls should have only a minor impact (if any) on the dynamics of pentanoic acid adsorption on the $Al_2O-H$ (0001) corundum surface.

![](./images/813126579478593536_2.jpg)

Figure 1: (a) Top view representation of the Al-terminated (0001) corundum surface 3x3 supercell before relaxation. Lateral views of the clean surface (b) before and (c) after (c) relaxation of the top atomic layers. Lateral views of the $Al_2O-H$ corundum surface (d) before and (e) after relaxation of the top atomic layers. Hydrogen, oxygen, and aluminum atoms are represented in light gray, red and blue colors, respectively.

The time evolution showing the dynamics of a single pentanoic acid mo- lecule over (0001) corundum Al/O-terminated and hydroxylated surfaces are
110 represented as a series of snapshots in Fig. 2 and 3, respectively. Two se- quences of animated snapshots illustrating these dynamics are also available as supplementary materials [30, 31].

![](./images/813126579478593536_3.jpg)

Figure 2: Sequence of snapshots showing the time evolution of the adsorption of a single pentanoic acid molecule on the Al/O-terminated (0001) corundum surface. The last snapshot represents the relaxed structure after BFGS optimization. Hydrogen, carbon, oxygen, and aluminum atoms are represented in light gray, dark gray, red and blue colors, respectively.

![](./images/813126579478593536_4.jpg)

Figure 3: Sequence of snapshots showing the time evolution of the adsorption of a single pen-
tanoic acid molecule on the $Al_2O-H$ (0001) corundum surface. The last snapshot represents
the relaxed structure after BFGS optimization. Hydrogen, carbon, oxygen, and aluminum
atoms are represented in light gray, dark gray, red and blue colors, respectively.

Detailed views of the fully relaxed pentanoic acid molecule adsorbed on the alumina surfaces are shown in Fig. 4. Also included are some bond lengths and interatomic distances before and after molecular dynamics and structural optimization.

![](./images/813126579478593536_5.jpg)

Figure 4: Some bond lengths and interatomic distances, in $\text{\AA}$, for a single pentanoic acid molecule adsorbed on the Al/O-terminated, clean (0001) $\alpha$-Al₂O₃ surface (a) before and (b) after molecular dynamics and BFGS optimization. The same for a pentanoic acid molecule adsorbed on the Al₂O$-$H (0001) corundum surface (c) before and (d) after molecular dynamics and BFGS optimization. Hydrogen, carbon, oxygen, and aluminum atoms are represented in light gray, dark gray, red and blue colors, respectively.

The dissociative adsorption of pentanoic acid on the Al/O-terminated surface very much resemble the adsorption of water [11], ethanol [32], formic and

lauric acids [21] on clean $\alpha$-Al$_2$O$_3$ surfaces. In fact, the surface Al atoms on
the Al/O-terminated (0001) corundum surface constitute strong Lewis acids
(electron acceptors) sites [11] to which the pentanoic acid molecule adsorbs dis-
sociatively. By interacting with the clean alumina surface, the acid molecule's
carbonyl double bond is broken while the oxygen binds to a nearby surface
aluminum, forming a C$-$O$-$Al bond with a C$-$O bond length of 1.31 Å. Mean-
while, the molecule's C$-$O$-$H group splits into a carbonyl and a proton, with
the latter forming an isolated hydroxyl by bonding to a nearby surface oxygen.
The formation of this new carbonyl is accompanied by a reduction of the car-
bon to oxygen bond length from 1.34 (in the original C$-$O$-$H group) to 1.23 Å
(in the new C=O). Just for comparison, the calculated C=O bond length for
the isolated molecule is 1.22 Å. The terminal oxygen atom of the newly formed
carbonyl, distant 1.77 Å from the hydrogen of the (also newly formed) isolated
surface hydroxyl, is well within the interatomic distance range for strong hyd-
rogen bonding [33], the effect of which on the corresponding infrared spectrum
will be discussed later.

Molecular dynamics simulation of pentanoic acid over the Al$_2$O$-$H (0001)
corundum surface revealed an entirely different evolution, in which the hydrogen
from the acid C$-$O$-$H group makes a bond to a surface oxygen, which locally be-
comes $\text{Al}_2\text{O}^{\overset{\text{H}}{-}}_{\underset{\text{H}}{-}}$. After full BFGS relaxation, the molecule lay down nearly paral-
lel to the alumina surface, pivoting on the central $\text{O}_{\text{ads}}$ of $\text{R}-\text{C}-\text{O}_{\text{ads}}-\text{H}-\text{O}_s\text{H}-\text{Al}_2$
(where the subscripts $ads$ and $s$ refer to oxygen atoms in the adsorbed penta-
noic acid molecule and the alumina surface, respectively). The relaxed structure
exhibits a hydrogen nearly halfway between the oxygen atom of the pentanoic
acid molecule ($\text{O}_{\text{ads}}-\text{H}$ bond length equal to 1.17 Å, 17% longer than the O$-$H
bond length in the isolated pentanoic acid molecule) and the surface oxygen
($\text{O}_s-\text{H}$ bond length equal to 1.24 Å). In fact, the similarity and the magnitude
of the $\text{O}_{\text{ads}}-\text{H}$ and $\text{O}_s-\text{H}$ bond lengths suggest a very strong hydrogen bonding
between the pentanoic acid molecule and the surface oxygen, with strong cova-
lent character [33]. As a secondary effect, upon adsorption the carbonyl bond

length slightly increases from 1.22 to $1.24\,\mathring{A}$.

After molecular dynamics and structural relaxation, the infrared spectra for both the pentanoic acid molecule adsorbed on the corundum Al/O-terminated surface and the hydroxylated surface were calculated. In these calculations the atoms of lower layers were kept fixed, i.e., they were not allowed to be displaced from their respective positions for the calculation of the corresponding elements of the dynamical matrix (see Fig. 5).

![](./images/813126579478593536_6.jpg)

Figure 5: Relaxed structures for a single pentanoic acid molecule adsorbed on (a) Al/O- terminated and (b) $Al_2O-H$ (0001) corundum surfaces. Hydrogen, carbon, oxygen, and aluminum atoms are represented in light gray, dark gray, red and blue colors, respectively. Light-colored atoms were kept fixed at their original positions for the calculation of the cor- responding infrared spectrum.

Figure 6 shows a comparison between the experimental infrared spectrum of pentanoic acid in the gas phase and the calculated infrared spectrum for the isolated pentanoic acid molecule in a vacuum, a single pentanoic acid mole- cule adsorbed on the Al/O-terminated alumina surface, and a single pentanoic acid molecule adsorbed on the doubly-coordinated hydroxyl-terminated alumina surface. The assignment of the main infrared bands in the theoretical infrared absorption spectra was aided by the analysis of animations of the corresponding normal modes eigenvectors. These animations are available as supplementary materials [34].

The experimental infrared absorption spectrum of pentanoic acid in the gas phase exhibits a major C=O stretching vibration absorption band at $1782\,\text{cm}^{-1}$. The infrared bands between 3000 and $2800\,\text{cm}^{-1}$ and between 1500 and $1300\,\text{cm}^{-1}$

![](./images/813126579478593536_7.jpg)

Figure 6: (a) Experimental infrared spectrum of pentanoic acid in the gas phase [35], and calculated infrared spectrum for a single pentanoic acid molecule (b) isolated in a vacuum, and adsorbed on (c) Al/O-terminated and (d) $Al_2O-H$ (0001) corundum surface. The infrared activity below $2500\mathrm{cm}^{-1}$ was multiplied by five in the bottom panel.

are assigned to stretching vibrations and angular deformations of $CH_2$ and $CH_3$ groups in the carbon chain, respectively. The intense band at $3574\mathrm{cm}^{-1}$ is
assigned to the O-H stretching mode [36]. Overall, there is a good agreement (both for band wavenumber and intensity) between experimental and theoreti- cal infrared absorption spectra for the isolated pentanoic acid molecule.

Upon pentanoic acid dissociative adsorption on the Al/O-terminated (0001) $\alpha$-$Al_2O_3$ surface, the newly formed isolated hydroxyl gives rise to an intense infrared band at $3189\mathrm{cm}^{-1}$. The $\mathrm{O_s-H}$ stretching band is shifted by $436\mathrm{cm}^{-1}$ (i.e., by about 12%, from $3625\mathrm{cm}^{-1}$ to $3189\mathrm{cm}^{-1}$) relatively to the hydroxyl stretching band wavenumber calculated for the isolated molecule. This marked band shift toward lower wavenumbers is consistent with a strong hydrogen bon- ding between the H atom of the isolated surface hydroxyl and the oxygen from the (also newly formed) carbonyl group in the pentanoic acid molecule. This hydrogen bonding also weakens the carbonyl (C=O) bond, as commented be-

fore. Indeed, upon dissociative adsorption, the hydrogen bonded pentanoic acid carbonyl exhibits an infrared absorption band shifted to lower wavenumbers, from $1765 \mathrm{~cm}^{-1}$ (in the isolated molecule) to $1621 \mathrm{~cm}^{-1}$. Surface Al-O stret-

ching modes are mainly responsible for the intense infrared bands at $938 \mathrm{~cm}^{-1}$ and $613 \mathrm{~cm}^{-1}$.

For pentanoic acid adsorbed over the $\mathrm{Al}_{2} \mathrm{O}-\mathrm{H}$ (0001) corundum surface, a series of infrared absorption bands from 3782 to $3372 \mathrm{~cm}^{-1}$ (including the most intense calculated infrared band, at $3385 \mathrm{~cm}^{-1}$ ) can be assigned to $\mathrm{O}_{\mathrm{s}}-\mathrm{H}$

stretching vibrations of isolated surface hydroxyls. As previously described, in this case the pentanoic acid molecule makes a very strong hydrogen bond to an oxygen atom at the top of the hydroxylated surface. This oxygen, which was already bonded to an hydrogen (forming an isolated hydroxyl), now forms
H
a surface $\mathrm{Al}_{2} \mathrm{O} \quad$ group. Upon adsorption of the pentanoic acid molecule,
H

the formerly isolated hydroxyl $\mathrm{O}_{\mathrm{s}}-\mathrm{H}$ stretching mode gives rise to an infrared absorption band at $3162 \mathrm{~cm}^{-1}$. Furthermore, the infrared absorption band at $1700 \mathrm{~cm}^{-1}$, which at first sight could be assigned to the carbonyl stretching vibration, actually is a complex vibrational mode involving contributions from C=O stretching plus a combination of stretching and angular deformation of

the $-\mathrm{O}_{\mathrm{ads}}-\mathrm{H}-\mathrm{O}_{\mathrm{s}}-$ bridge between the molecule and the alumina surface. Angular deformation of the $-\mathrm{O}_{\mathrm{ads}}-\mathrm{H}-\mathrm{O}_{\mathrm{s}}-$ chain also contributes to a weaker infrared band at $1520 \mathrm{~cm}^{-1}$, while the band at $1172 \mathrm{~cm}^{-1}$ can be assigned to a complex vibrational mode with contributions from $-\mathrm{O}_{\mathrm{ads}}-\mathrm{H}$ stretching, $\mathrm{CH}_{2}$ and $\mathrm{H}-\mathrm{O}_{\mathrm{s}}-\mathrm{H}$ rocking, as well as other minor surface atoms vibrations.

A complimentary set of eight MD simulations, followed by structural re- laxation using the BFGS algorithm, was carried out to assess the repeatability of the key features of the dynamics of a single pentanoic acid molecule over the (0001) corundum surface [37, 38]. In this set of complimentary calculati- ons (four for the anhydrous and four for the $\mathrm{Al}_{2} \mathrm{O}-\mathrm{H}$ terminated surface), all

MD simulations started with the pentanoic acid molecule randomly displaced horizontally, from 1.40 to $3.66 \AA$, relative to the molecule position in the two

simulations previously described. Total energies for the all the relaxed structu- res in this complimentary set of calculations are within 0.64 mRy/atom of the total energies for the corresponding previously described simulations.

Except for a single case each, all complimentary simulations with anhydrous and hydroxylated corundum surfaces have a minimum energy configuration with the pentanoic acid's carbon chain aligned, respectively, perpendicular and pa- rallel to the corundum surface. More importantly, all simulations ended up with the pentanoic acid molecule adsorbing dissociatively on the clean Al/O-terminated surface. Similarly, in all simulations carried out with the $\alpha$-$Al_2O_3$ surface saturated with isolated hydroxyls, the pentanoic acid molecule adsorbed by making a hydrogen bond to a surface oxygen. These conclusions do stand, no matter the horizontal displacement of the pentanoic acid molecule relative to the corundum surface at the beginning of the simulation. Moreover, the simi- lar dynamics exhibited by all the systems here explored gives further evidence that we have indeed found favorable adsorption sites for pentanoic acid on the anhydrous and the hydroxylated (0001) corundum surfaces. Furthermore, there is no reason to suppose that the fingerprint infrared bands previously described should be significantly different for any of the new relaxed structures, given that bonding of pentanoic acid to the corundum surface (both anhydrous and hydroxylated) hardly changed in this complimentary set of simulations.

### 4. Conclusions

Molecular dynamics simulations of a single pentanoic acid over a (0001) $\alpha$- $Al_2O_3$ surface allowed the identification of different adsorption mechanisms for a clean, anhydrous Al/O-terminated and a doubly-coordinated, isolated hydroxyl- terminated surface. In the former case, the pentanoic acid molecule adsorbs dissociatively by forming a $-C-O-Al$ bridge, with a proton being transfer- red to the surface. Adsorption is thus accompanied by the formation of an isolated surface hydroxyl, whose stretching mode infrared absorption band, at $3189\,\text{cm}^{-1}$, is shifted downward by $436\,\text{cm}^{-1}$ relative to the $\text{O-H}$ stretching

14
Page 14 of 22

vibration in the isolated molecule. Furthermore, a new carbonyl group is formed in the acid molecule, with a calculated stretching vibration at $1621\,\text{cm}^{-1}$, i.e., $144\,\text{cm}^{-1}$ below the corresponding infrared band for the isolated molecule.
Adsorption over the hydroxylated (0001) $\alpha\text{-Al}_2\text{O}_3$ surface occurs by forming a strong $-\text{O}_{\text{ads}}-\text{H}-\text{O}_{\text{s}}$ hydrogen bond, which contributes (along with the carbonyl stretching vibration) to a infrared absorption band at $1700\,\text{cm}^{-1}$. The findings here reported, mainly the characteristic infrared spectra, may be useful as a first guide for the identification of the underlying adsorption mechanism of pentanoic acid (and similar carboxylic acids) on alumina in actual experiments.

Extensions of this computational study to situations other than the surface in a vacuum may be sought after either explicitly including solvent (e.g., water) molecules or by means of a less computationally intensive self-consistent continuumsolvation model.[39]

## Acknowledgements

The financial support from Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq, research grants #304831/2014-0 and #304675/2015-6), Fundação de Amparo à Pesquisa do Estado do Rio Grande do Sul (FAPERGS), Secretaria de Desenvolvimento Econômico, Ciência e Tecnologia do Estado do Rio Grande do Sul (SDECT/RS), and Centro Nacional de Supercomputação da Universidade Federal do Rio Grande do Sul (CESUP/UFRGS) are gratefully acknowledged. Thanks are due also to Jaíne Webber and Robinson C. D. Cruz for discussions on the subject of this work.

## Supplementary Material

Supporting information to this manuscript includes supplementary material consisting of i) Animated sequence of snapshots illustrating the relaxation of the outermost atomic layers of Al/O-terminated (0001) corundum surface in a vacuum [28], ii) Animated sequence of snapshots illustrating the relaxation of the outermost atomic layers of $\text{Al}_2\text{O}-\text{H}$ (0001) corundum surface in a vacuum [29],

iii) Time evolution of a pentanoic acid molecule over Al/O-terminated (0001) corundum surface in a vaccuum [30], iv) Time evolution of a pentanoic acid molecule over $Al_2O-H$ (0001) corundum surface in a vacuum [31], v) Computer animations of normal modes eigenvectors for the main infrared absorption bands [34], vi) Four complimentary MD simulations and BFGS optimizations for a single pentanoic acid molecule over Al/O-terminated (0001) corundum surface in a vaccuum [37], and vii) Four complimentary MD simulations and BFGS optimizations for a single pentanoic acid molecule over $Al_2O-H$ (0001) corundum surface in a vacuum [38].

### References

[1] J. Reed, Principles of Ceramics Processing, 2nd Edition, John Wiley and Sons, US, 1995.

[2] K. C. Hass, W. F. Schneider, A. Curioni, W. Andreoni, The chemistry of water on alumina surfaces: Reaction dynamics from first principles, Science 282 (9) (1998) 265-268.

[3] B. Kasprzyk-Hordern, Chemistry of alumina, reactions in aqueous solution and its application in water treatment, Adv. Colloid Interfac. 110 (1) (2004) 19-48.

[4] H. Knözinger, P. Ratnasamy, Catalytic aluminas: Surface models and characterization of surface sites, Catal. Rev. 17 ((1)) (1978) 31-70.

[5] J. Webber, J. Zorzi, C. A. Perottoni, S. M. e Silva, R. Cruz., Identification of surface active sites of $\alpha$-al₂o₃ and their role in the adsorption of stearic acid., J. Mater. Sci 51 (11) (2016) 5170-5184.

[6] X.-G. Wang, A. Chaka, M. Scheffler, Effect of the environment on $\alpha$-Al₂O₃ (0001) surface structures, Phys. Rev. Lett. 84 (16) (2000) 3650.

[7] Z. Lodziana, J. K. Nørskov, P. Stoltze, The stability of the hydroxylated (0001) surface of $\alpha$-Al₂O₃, J. Chem. Phys. 118 (24) (2003) 11179-11188.

[8] G. V. Franks, Y. Gan, Charging behavior at the alumina-water interface and implications for ceramic processing, J. Am. Ceram. Soc. 90 (11) (2007) 3373-3388.

[9] T. H. Ballinger, J. T. Yates, Ir spectroscopic detection of lewis acid sites on alumina using adsorbed carbon monoxide. correlation with aluminum- hydroxyl group removal, Langmuir 7 (12) (1991) 3041-3045.

[10] N. H. de Leeuw, S. C. Parker, Effect of chemisorption and physisorption of water on the surface structure and stability of alpha-alumina, J. Am. Ceram. Soc. 82 (11) (1999) 3209-2316.

[11] K. C. Hass, , W. F. Schneider, A. Curioni, W. Andreoni, First-principles molecular dynamics simulations of $h_2o$ on $\alpha$-al₂o₃ (0001), J. Phys. Chem. B 104 (23) (2000) 5527-5540.

[12] Y. Tong, J. Wirth, H. Kirsch, M. Wolf, P. Saalfrank, R. K. Campen, Op- tically probing al-o and o-h vibrations to characterize water adsorption and surface reconstruction on $\alpha$-alumina: An experimental and theoretical study, J. Chem. Phys. 142 (5).

[13] E. Fernández, R. Eglitis, G. Borstel, L. Balbás, Ab initio calculations of $H_{2}O$ and $O_{2}$ adsorption on $Al_{2}O_{3}$ substrates, Comp. Mater. 39 (3) (2007) 587 - 592.

[14] V. Shapovalov, T. N. Truong, Ab initio study of water adsorption on $\alpha$- $Al_{2}O_{3}$ (0001) crystal surface, J. Phys. Chem. B 104 (42) (2000) 9859-9863.

[15] J. M. Wittbrodt, W. L. Hase, H. B. Schlegel, Ab initio study of the inte- raction of water with cluster models of the aluminum terminated (0001) $\alpha$-aluminum oxide surface, J. Phys. Chem. B 102 (34) (1998) 6539-6548.

[16] V. A. Nasluzov, V. V. Rivanenkov, A. M. Shor, K. M. Neyman, U. Birken- heuer, N. Rïsch, Density functional embedded cluster calculations on lewis acid centers of the $\alpha$-$Al_{2}O_{3}$ (0001) surface: Adsorption of a co probe, Int. J. Quantum Chem. 90 (1) (2002) 386-402.

[17] D. C. Sorescu, J. A. Boatz,, D. L. Thompson, First-principles calculations of the adsorption of nitromethane and 1,1-diamino-2,2-dinitroethylene (fox-7) molecules on the $\alpha$-Al$_2$O$_3$ (0001) surface, J. Phy. Chem. B 109 (4) (2005) 1451-1463.

[18] C. Arrouvel, B. Diawara, D. Costa, P. Marcus, Dft periodic study of the adsorption of glycine on the anhydrous and hydroxylated (0001) surfaces of $\alpha$-alumina, J. Phys. Chem. C 111 (49) (2007) 18164-18173.

[19] G. Rubasinghege, S. Ogden, J. Baltrusaitis, V. H. Grassian, Heterogeneous uptake and adsorption of gas-phase formic acid on oxide and clay particle surfaces: The roles of surface hydroxyl groups and adsorbed water in formic acid adsorption and the impact of formic acid adsorption on water uptake, J. Phys. Chem. A 117 (44) (2013) 11316-11327.

[20] S. R. Tong, L. Y. Wu, M. F. Ge, W. G. Wang, Z. F. Pu, Heterogeneous che- mistry of monocarboxylic acids on $\alpha$-Al$_2$O$_3$ at different relative humidities, Atmos. Chem. Phys. 10 (16) (2010) 7561-7574.

[21] M. Ruan, H. Hou, W. Li, B. Wang, Theoretical study of the adsorp- tion/dissociation reactions of formic acid on the $\alpha$-Al$_2$O$_3$ (0001) surface, J. Phys. Chem. C 118 (36) (2014) 20889-20898.

[22] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. D. Corso, S. de Gi- roncoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Maz- zarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, R. M. Wentzco- vitch, Quantum espresso: A modular and open-source software project for quantum simulations of materials, J. Phys-Condens. Mat. 21 (39) (2009) 395502.

URL http://stacks.iop.org/0953-8984/21/i=39/a=395502

[23] Quantum espresso pseudopotentials database.

URL http://www.quantum-espresso.org/pseudopotentials/

[24] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria,
L. A. Constantin, X. Zhou, K. Burke, Restoring the density-gradient ex-
pansion for exchange in solids and surfaces, Phys. Rev. Lett. 100 (2008)
136406. doi:10.1103/PhysRevLett.100.136406.

URL http://link.aps.org/doi/10.1103/PhysRevLett.100.136406

[25] S. Grimme, Semiempirical gga-type density functional constructed with a
long-range dispersion correction, J. Comput. Chem. 27 (15) (2006) 1787-
1799. doi:10.1002/jcc.20495.

URL http://dx.doi.org/10.1002/jcc.20495

[26] R. Dovesi, V. R. Saunders, C. Roetti, R. Orlando, C. M. Zicovich-Wilson,
F. Pascale, B. Civalleri, K. Doll, N. M. Harrison, I. J. Bush, P. D'Arco,
M. Llunell, CRYSTAL06 User's Manual (University of Torino, Torino,
2006).

[27] Jmol: An open-source java viewer for chemical structures in 3d.

URL http://www.jmol.org/

[28] Supplementary material - animated sequence of snapshots illustrating the
relaxation of the outermost atomic layers of Al/O-terminated (0001) cor-
undum surface in a vacuum.

URL http://www.if.ufrgs.br/~perott/SM1.mov

[29] Supplementary material - animated sequence of snapshots illustrating the
relaxation of the outermost atomic layers of $Al_2O-H$ (0001) corundum
surface in a vacuum.

URL http://www.if.ufrgs.br/~perott/SM2.mov

[30] Supplementary material - time evolution of a pentanoic acid molecule over
Al/O-terminated (0001) corundum surface in a vaccuum.

URL http://www.if.ufrgs.br/~perott/SM3.mov

[31] Supplementary material - time evolution of a pentanoic acid molecule over
$\ce{Al_{2}O-H}$ (0001) corundum surface in a vacuum.
URL http://www.if.ufrgs.br/~perott/SM4.mov

[32] K. Johnston, A van der waals density functional study of the adsorption of
ethanol on the $\alpha$-alumina (0001) surface, Surf. Sci. 621 (2014) 16-22.

[33] G. Desiraju, T. Steiner, The Weak Hydrogen Bond: In Structural Chemi-
stry and Biology, IUCr monographs on crystallography, Oxford University
Press, 2001.
URL https://books.google.com.br/books?id=aj-pjov8DW0C

[34] Supplementary material - computer animations of normal modes eigenvec-
tors for the main infrared absorption bands.
URL http://www.if.ufrgs.br/~perott/SM5.html

[35] NIST standard reference data program.
URL http://webbook.nist.gov/cgi/cbook.cgi?ID=C109524&Units=
SI&Type=IR-SPEC&Index=0#IR-SPEC

[36] J. Coates, Interpretation of infrared spectra, a practical approach, in: R. A.
Meyers (Ed.), Encyclopedia of Analytical Chemistry, John Wiley & Sons,
Chichester, 2000, pp. 10815-10837.

[37] Supplementary material - complimentary md simulations and bfgs optimi-
zations for a single pentanoic acid molecule over Al/O-terminated (0001)
corundum surface in a vaccuum.
URL http://www.if.ufrgs.br/~perott/SM6.mov

[38] Supplementary material - complimentary md simulations and bfgs optimi-
zations for a single pentanoic acid molecule over $\ce{Al_{2}O-H}$ (0001) corundum
surface in a vacuum.
URL http://www.if.ufrgs.br/~perott/SM7.mov

[39] O. Andreussi, I. Dabo, N. Marzari, Revised self-consistent continuum
solvation in electronic-structure calculations, J. Chem. Phys. 136 (6).

doi:http://dx.doi.org/10.1063/1.3676407.

URL http://scitation.aip.org/content/aip/journal/jcp/136/6/10.1063/1.3676407

Adsorption of a pentanoic acid molecule on α-Al₂O₃ was explored by MD simulations
Pentanoic acid adsorbs dissociatively on clean α-Al₂O₃ forming an isolated surface OH
Pentanoic acid adsorbs on hydroxylated Al₂O₃ by making a strong H-bond to a surface O
Different adsorption mechanism has a impact on the calculated IR absorption spectrum