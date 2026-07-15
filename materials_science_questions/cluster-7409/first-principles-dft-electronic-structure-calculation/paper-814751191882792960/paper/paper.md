![](./images/814751191882792960_1.jpg)

# Behaviour of hydrogen in wide band gap oxides
H. Li and J. Robertson

Citation: *Journal of Applied Physics* **115**, 203708 (2014); doi: 10.1063/1.4878415
View online: http://dx.doi.org/10.1063/1.4878415
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/115/20?ver=pdfcov
Published by the AIP Publishing

---

## Articles you may be interested in
Effects of Ag-induced acceptor defects on the band gap tuning and conductivity of Li:ZnO films
J. Appl. Phys. **113**, 203518 (2013); 10.1063/1.4807932

Thermally activated below-band-gap excitation behind green photoluminescence in ZnO
J. Appl. Phys. **111**, 093525 (2012); 10.1063/1.4712624

Current-driven hydrogen incorporation in zinc oxide
Appl. Phys. Lett. **91**, 212102 (2007); 10.1063/1.2816119

Behavior of hydrogen in wide band gap oxides
J. Appl. Phys. **102**, 083710 (2007); 10.1063/1.2798910

Role of Intentionally Incorporated Hydrogen in WideBandGap ZnO Thin Film Prepared by PhotoMOCVD Technique
AIP Conf. Proc. **772**, 195 (2005); 10.1063/1.1994060

---

![](./images/814751191882792960_2.jpg)

[This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to ] IP:
131.156.59.191 On: Fri, 05 Sep 2014 14:09:01

JOURNAL OF APPLIED PHYSICS 115, 203708 (2014)
![](./images/814751191882792960_3.jpg)

# Behaviour of hydrogen in wide band gap oxides
H. Li and J. Robertson
Department of Engineering, Cambridge University, Cambridge CB2 1PZ, United Kingdom
(Received 24 March 2014; accepted 5 May 2014; published online 27 May 2014)

The defect formation energies and atomic geometries of interstitial hydrogen in its different charge states in a number of wide band gap oxides are calculated by the Heyd, Scuseria, Ernzerhof hybrid functional. As in semiconductors, two behaviours are found, it acts either as an amphoteric defect or as a shallow donor. There are large scale lattice relaxations between the different charge states for the case of the amphoteric defect. Interestingly, we find that the +/− transition level does have a good alignment below the vacuum level, as was found previously for tetrahedral semiconductors.
© 2014 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4878415]

## I. INTRODUCTION
Hydrogen is a ubiquitous impurity in many solids and particularly in oxides. It strongly affects the electronic and structural properties of these materials. Interstitial hydrogen can act in two ways in a semiconducting or insulating oxide lattice. $^{1-6}$ It can be an amphoteric impurity, giving rise to deep gap states with positive, neutral, and negative charge states, or it can form a shallow level at the conduction band (CB) edge and act as a donor. There can be other configurations of hydrogen incorporation into oxide, such as "hidden hydrogen," perhaps $H_2$ molecules, which dissociate at elevated temperatures; substitutional $H_O$ forming multicentre bonds which has been theoretically predicted to account for n-type conductivity of $ZnO;^{7}$ complex protonated cation vacancies (Ruetschi defects) are predicted and are expected to play an important role in photoelectrochemistry, catalysis, and surface transport, $^{8}$ but these variety will not be considered here. Although hydrogen often has beneficial effects in covalently bonded semiconductors by passivating defects by tying off their dangling bond defects, in oxides however, donor activity is often undesirable as it leads to uncontrollable conduction and the presence of fixed charge. $^{9}$

At a theoretical level, the interstitial hydrogen atom is an unusual impurity, which creates large lattice relaxations of the adjacent atoms in its different charge states. In the tetrahedrally bonded semiconductors, van de Walle and Neugebauer $^{4}$ observed that the +/− transition level of interstitial hydrogen tended to lie at a similar energy as the charge neutrality level (CNL) of the host semiconductor, and it was found that the CNL tended to lie at a relative constant energy of 4.5 eV below the vacuum level. The CNL is the branch point of the complex band structure of the bulk band structure, and is closely related to band offsets between semiconductors. $^{10}$

On the other hand, the behaviour of hydrogen in oxides can vary considerably between different classes of oxides. $^{3,5}$ We have previously studied the behaviour of hydrogen in oxides using density functional theory (DFT). In such DFT calculations, the band gap error of DFT is a serious problem, as it is more likely to give a certain defect as a donor than the correct calculation. Therefore, previously we calculated the defect's atomic structure using DFT (using the generalised gradient approximation, GGA) and then calculated the energy levels using a different functional, the weighted density approximation (WDA), $^{11,12}$ which largely corrected the band gap error. This approach was chosen largely by computational resources. However, there are two problems with this approach. First, the predicted structure from local density approximation (LDA) depends on the correct band gap. Second, WDA is less reliable than other methods to correct the band gap error. Therefore, we use here the Heyd, Scuseria, Ernzerhof (HSE06) hybrid function method $^{13-15}$ to calculate simultaneously the atomic structure and the electronic structure of the hydrogen defect.

Our objective is to test where the similarity of the +/− transition level of hydrogen to the material's bulk CNL energy extends to oxides. Therefore, we study a wide range of oxides, with different coordinations and lattice symmetries, particularly those with small or large electron affinities and ionisation potentials. We choose $SiO_2$ and $Al_2O_3$ as s,p bonded wide gap oxides. We choose $GeO_2$ and $Ga_2O_3$ as oxides with band gaps and CNLs close to the borderline of 4.5 eV below the vacuum level. We choose $HfO_2, La_2O_3$, and $LaAlO_3$ as examples of wide gap, high dielectric constant where hydrogen had a range of behaviours in our previous study. We study $TiO_2$ and $SnO_2$ as examples of transparent conducting oxides (TCOs) where hydrogen is expected to form a shallow centre. Finally, we choose $CuAlO_2, CuInO_2$ and $SrCu_2O_2$ as cases of p-type TCOs with valence band (VB) edges lying quite high in energy with respect to the vacuum level, to see if the +/− level could enter the valence band. The examples are largely chosen from two classes of oxides: the gate oxides such as $LaAlO_3$, $HfO_2, La_2O_3, GeO_2, Al_2O_3, MgO$, and the TCOs including $SnO_2, TiO_2, Ga_2O_3$, and $CuAlO_2$.

Experimentally, Cox et al. $^{16,17}$ have made extensive studies on whether muonium forms localized or delocalized levels in many semiconductors and oxides. Muonium acts chemically like H, but with a smaller mass. Thus, muonium spin resonance provides a unique experimental signature of whether the H level is deep or shallow.

## II. METHOD
We use the plane wave pseudopotential code CASTEP. $^{18}$ The atomic potentials are represented by

norm-conserving pseudopotentials. The semi-core d orbitals for Ga are included as valence orbitals. A plane wave cutoff energy of 800 eV is used. The calculations used the HSE06 hybrid functional. In this, a fraction $\alpha$ of the short-range separated part of the Hartree-Fock (HF) exchange is mixed with the GGA exchange-correlation integral. $^{13-15}$ This corrects the band gap errors of pure GGA. The standard HSE uses a fraction $\alpha=0.25$, and this is mostly used in practice. However some groups have adjusted $\alpha$ to fit the band gap, $^{19,20}$ while some have noted that larger $\alpha$ values are needed in HSE for wider band gap systems. $^{21-23}$ In our work, we also vary $\alpha$ to fit the band gap for wider gap systems. A fixed screening length $\mu=0.106$ bohrs $^{-1}$ is used. $^{13}$

For the defect calculations, the lattice parameters for crystalline oxides are set to the experimental values, and only the internal atomic coordinates are relaxed for the interstitial H. The H states are quite localized, so that we do not use very large supercells. We constructed the supercells that contain 33-49 atoms for various oxides. The H atom is placed in an arbitrary position near the centre of the open interstitial site. The k point mesh is $2 \times 2 \times 2$ and the cutoff energy is 800 eV. The defect formation energies are defined as usual by
$$
H_{q}\left(E_{F}, \mu\right)=\left[E_{q}-E_{H}\right]+q\left(E_{V}+\Delta E_{F}\right)+\sum_{\alpha} n_{\alpha}\left(\mu_{\alpha}^{0}+\Delta \mu_{\alpha}\right)
$$
where $E_{q}$ and $E_{H}$ are the total energy of a defect cell and a perfect cell, respectively, calculated for charge $q, \Delta E_{F}$ is the Fermi energy with respect to the valence band edge, $n_{\alpha}$ is the number of atoms of element $\alpha$, and $\mu_{\alpha}^{0}$ is the reference chemical potential, following the method described by Lany and Zunger. $^{24}$ The charge transition level $E(q+1 / q)$ is defined as the Fermi energy $E_{F}$ at which the formation energy of the charge states q+1 and q is equal.

## III. RESULTS AND DISCUSSION
### A. Quartz-SiO₂

We first consider H in $SiO_{2}$. $SiO_{2}$ is the least polar of the oxides considered here. It has open lattice with directional, covalent bonds and a very wide band gap of 9.0 eV. Figs. 1(a)-1(c) show the relaxed atomic configurations of H in $SiO_{2}$ in the different charge states. For $H^{-}$, the H forms a single bond of length $1.51 \mathring{A}$ to a more positively charged Si site. This makes the Si five-fold coordinated, and the Si and its three neighbouring O turn into a flatten structure, forming a bond to the fourth O perpendicular to the $Si-O_{3}$ group with the H on the opposite side. For $H^{0}$, H forms an isolated interstitial site, about $2.40 \mathring{A}$ away from other oxygen sites. It does not disturb the surrounding lattice. For $H^{+}$, H forms a short O-H bond of length of $0.98 \mathring{A}$ to a host O atom. The oxygen becomes three fold coordinated in a pyramidal configuration. Unlike in other oxides, H does not need to break a host bond to form the O-H bond, because of the small O coordination number. The atomic configurations of H in $SiO_{2}$ obtained by HSE06 are basically the same as those obtained by GGA. $^{12,25}$

The defect formation energy diagram of H in $SiO_{2}$ is shown in Figure 1(d). It is interesting to note from the relative formation energy (with respect to $E(H^{0})$ ) vs Fermi energy that $H^{0}$ state is never the lowest energy state: $H^{+}$ and $H^{-}$ states are the lowest energy state for Fermi energy in the lower part and upper part of the band gap, respectively. The (+/-) transition level is indicated by an arrow. This means that the defect is a negative U defect. U is defined as $U=E(+/ 0)-E(0 /-)$. The negative U arises because of the large atomic relaxation occurring at the positive site.

In the absence of relaxation or electron-electron repulsion, $E(+/ 0) \approx E(0 /-)$. However, if there is strong relaxation, as in this case, then E(0/-) lies below E(+/0) and the relaxation energy is $U=E(+/ 0)-E(0 /-)$. H is known to be deep in $SiO_{2},^{25,26}$ consistent with our calculation that (+/-)

![](./images/814751191882792960_4.jpg)

FIG. 1. Atomic configurations of H interstitial of different charge states in q-$SiO_{2}$, (a) $H^{-}$, (b) $H^{0}$, (c) $H^{+}$, and (d) charge transition diagram.

<table>
<caption>Table I. Fraction of Hartree-Fock exchange used here, and HSE06 band gap for each oxide, compared to experimental band gaps.⁴⁹</caption>
<tbody>
<tr>
<td>Compound</td>
<td>Fraction of HF exchange</td>
<td>HSE06 band gap (eV)</td>
<td>Exp band gap (eV)</td>
</tr>
<tr>
<td>m-HfO₂</td>
<td>0.30</td>
<td>5.8</td>
<td>6.0</td>
</tr>
<tr>
<td>La₂O₃</td>
<td>0.29</td>
<td>5.2</td>
<td>6.0</td>
</tr>
<tr>
<td>θ-Al₂O₃</td>
<td>0.29</td>
<td>6.8</td>
<td>7.0</td>
</tr>
<tr>
<td>Ga₂O₃</td>
<td>0.50</td>
<td>4.8</td>
<td>5.0</td>
</tr>
<tr>
<td>q-GeO₂</td>
<td>0.30</td>
<td>5.6</td>
<td>6.0</td>
</tr>
<tr>
<td>r-GeO₂</td>
<td>0.30</td>
<td>4.3</td>
<td>4.7</td>
</tr>
<tr>
<td>SnO₂</td>
<td>0.29</td>
<td>3.6</td>
<td>3.6</td>
</tr>
<tr>
<td>TiO₂</td>
<td>0.15</td>
<td>3.0</td>
<td>3.2</td>
</tr>
<tr>
<td>LaAlO₃</td>
<td>0.50</td>
<td>5.5</td>
<td>5.6</td>
</tr>
<tr>
<td>CuAlO₂</td>
<td>0.15</td>
<td>3.0</td>
<td>3.0</td>
</tr>
<tr>
<td>α-Al₂O₃</td>
<td>0.29</td>
<td>8.5</td>
<td>8.8</td>
</tr>
<tr>
<td>MgO</td>
<td>0.40</td>
<td>7.5</td>
<td>7.8</td>
</tr>
<tr>
<td>SiO₂</td>
<td>0.35</td>
<td>8.7</td>
<td>9.0</td>
</tr>
<tr>
<td>CuInO₂</td>
<td>0.30</td>
<td>1.9</td>
<td>2.0</td>
</tr>
<tr>
<td>SrCu₂O₂</td>
<td>0.35</td>
<td>3.1</td>
<td>3.3</td>
</tr>
</tbody>
</table>

lies $\sim$5.4 eV above the VB edge and $\sim$3.6 eV below the CB edge.

### B. Quartz-GeO₂ and rutile-GeO₂

We consider hydrogen in two stable polymorphs of GeO₂, quartz (q$-$) GeO₂ and rutile (r$-$) GeO₂. q-GeO₂ consists of 4-fold coordinated Ge and 2-fold coordinated O, while r-GeO₂ consists of 6-fold coordinated Ge and 3-fold O. The main purpose is that r-GeO₂ has smaller band gap than that of q-GeO₂, as shown in Table I. q-GeO₂ has the same crystal symmetry as q-SiO₂. For H⁻ in q-GeO₂, the atomic configuration (Fig. 2(a)) shows that hydrogen binds to a Ge. This makes the Ge five-fold coordinated and the Ge-O bonds move away to accommodate the Ge-H bond. The Ge-H bond length is $\sim$1.55 Å. For H⁰, in q-GeO₂ hydrogen forms an isolated interstitial and does not disturb the surrounding lattice. This differs from Xiong’s GGA result¹² which shows H⁰ binding to an oxygen. For H⁺ in q-GeO₂, hydrogen binds to an oxygen, with bond length of $\sim$0.99 Å.

H in q-GeO₂ shows similar atomic configurations for each charge state as it does in q-SiO₂. Hydrogen shows negative U behavior and H⁰ is never a stable state. The (+/−) level lies $\sim$1.0 eV below the CB edge of q-GeO₂, forming a deep state, but now in the top half of the band gap compared to the behaviour in SiO₂. This is in contrast to Xiong’s hybrid functional result²⁷ of (+/−) level but based on a GGA relaxed geometry where (+/−) level was found to be shallow.

On the other hand, for H⁻ in r-GeO₂ (Fig. 3), hydrogen breaks a Ge–O bond and sits near a bond centre, bonding to a Ge. Ge looses another two bonds to oxygen and becomes 4-fold coordinated to O. The Ge–H bond length is $\sim$1.38 Å. In r-GeO₂ H bonds to an oxygen with a O–H bond length of $\sim$0.98 Å. For H⁺ in r-GeO₂, hydrogen bonds to an oxygen, with bond length of $\sim$0.98 Å. Despite the larger oxygen coordination number in r-GeO₂, H⁺ does not break the Ge–O bonds.

The charge transition levels in Fig. 3 for r-GeO₂ show that hydrogen again has a negative U behavior. The (+/−) level lies $\sim$0.5 eV below the CB edge of r-GeO₂ which indicates a borderline between donor and deep. This shows that r-GeO₂ differs from SnO₂ and TiO₂ discussed later, where H acts as a shallow donor, because of their smaller band gaps.

### C. α-Al₂O₃ and θ-Al₂O₃

Electronic conduction in alumina is important for a number of electronic devices. Hydrogen interstitial has been found to be responsible for electron transport in Al₂O₃,²⁸ apart from oxygen vacancy.²⁹ Two polymorphs of Al₂O₃ are considered. In α-Al₂O₃ (corundum), Al is six-fold coordinated and O is 4-fold. In θ-Al₂O₃, half of the Al are four fold and the other half are six fold; 2/3 of the O are three fold and the rest are four fold. α-Al₂O₃ has large band gap of 8.8 eV comparable with that of q-SiO₂, while θ-Al₂O₃ has lower

![](./images/814751191882792960_5.jpg)

FIG. 2. Atomic configurations of H interstitial of different charge states in q-GeO₂, (a) H⁻, (b) H⁰, (c) H⁺, and (d) charge transition diagram.

![](./images/814751191882792960_6.jpg)

![](./images/814751191882792960_7.jpg)

FIG. 3. Atomic configurations of H in- terstitial of different charge states in r- GeO₂, (a) H⁻, (b) H⁰, (c) H⁺, and (d) charge transition diagram.

band gap of 7 eV, as seen in Table I. $\theta$-Al₂O₃ is a model²⁹ of $\alpha$-Al₂O₃ grown by atomic layer deposition (ALD), where the band gap is even lower, about 6.4 eV. Al₂O₃ is more polar than SiO₂. The atomic configurations of H in $\alpha$-Al₂O₃ and $\theta$-Al₂O₃ are shown in Figs. 4 and 5, respectively.

We first consider H⁻. In $\alpha$-Al₂O₃, H⁻ binds to two Al atoms along the z axis with a bond length of 1.67 Å. These two Al atoms relax significantly toward the central H⁻, due to attraction of the negative charged H⁻. They lose back bonds with three O atoms. This is a different geometry than that pre- dicted by GGA,¹² where the H⁻ only binds to one Al atom. In $\theta$-Al₂O₃, H⁻ also binds to two 4-fold coordinated Al atoms with a bond length of 1.56 Å. The two Al atoms are attracted toward the central H⁻ but without losing bonds to the O atoms.

For H⁰, in $\alpha$-Al₂O₃ H⁰ forms an isolated interstitial, which does not bind to any host atom or cause its adjacent atoms to relax much from their initial positions. This is also the same in $\theta$-Al₂O₃. For H⁺, in $\alpha$-Al₂O₃ H⁺ binds to an O atom with a bond length of 0.98 Å. This O atom has large displacement toward H⁺ due to the attraction of the positive charge and it loses two Al–O bonds, being three fold coordi- nated. In the GGA relaxed geometry,¹² however, this O atom only loses one bond with Al. In $\theta$-Al₂O₃, H⁺ binds to a three-fold O without breaking its bonds with Al. The O–H bond length is 1.10 Å.

We then consider the charge transition levels for H in $\alpha$- Al₂O₃ and $\theta$-Al₂O₃, as shown in Figs. 4(d) and 5(d), respec- tively. H⁰ is not a stable state in the range of Fermi energy across the band gap in either oxide. Interstitial H shows neg- ative U in both oxides due to large geometry relaxation between different charge states. In $\alpha$-Al₂O₃, the (+/−) level lies about 5.3 eV above the VB edge and thus 3.5 eV below

![](./images/814751191882792960_8.jpg)

![](./images/814751191882792960_9.jpg)

FIG. 4. Atomic configurations of H in- terstitial of different charge states in $\alpha$- Al₂O₃, (a) H⁻, (b) H⁰, (c) H⁺, and (d) charge transition diagram.

![](./images/814751191882792960_10.jpg)

![](./images/814751191882792960_11.jpg)

FIG. 5. Atomic configurations of H in-
terstitial of different charge states in $\theta$-
Al₂O₃, (a) H⁻, (b) H⁰, (c) H⁺, and (d)
charge transition diagram.

the CB edge, which is a deep state. In $\theta$-Al₂O₃, (+/−) level
lies around 4.8 eV above the VB edge and 2.0 eV below the
CB edge, which is also deep. Weber *et al.*³⁰ calculated the
charge transition level in $\kappa$-Al₂O₃ using LDA and found that
(+/−) level is at about 3.0 eV above the VB edge, closer to
the VB edge than our results.

### D. MgO

We next consider H in MgO. This oxide has the rock
salt structure, which is rather close packed. The atomic con-
figurations of H in MgO are shown in Figure 6. For H⁻, H⁻
binds to four neighbouring Mg cations, which relax symmet-
rically toward the central H⁻, this is different from the asym-
metric relaxation of Mg atoms by GGA.¹² The O–H bond
length is 1.77 Å. For H⁰, H⁰ stays in the centre of the neigh-
bouring Mg atoms without much disturbing the surrounding
lattice and it forms a weak Mg–H bond of length 1.87 Å. For
H⁺, H⁺ retains weak bonds with three Mg atoms at the same
time of binding strongly to an O atom. The O–H bond length
is 0.96 Å. Fig. 6(d) shows the resulting charge transition lev-
els. The H shows negative U behaviour and is deep. The
(+/−) level lies around 5.3 eV above the VB edge and
2.1 eV below the CB edge.

### E. m-HfO₂

We now consider H in monoclinic (m-) HfO₂. m-HfO₂
is the stable polymorph of HfO₂. The chemical bonds of
m-HfO₂ are very ionic. The Hf atoms are seven fold coordi-
nated, the oxygen atoms are three- and four-fold coordi-
nated. The atomic configurations of H in m-HfO₂ are shown
in Fig. 7. In H⁻, H⁻ binds to two Hf atoms with a Hf–O
bond length of 1.97 Å. This is clearly in contrast to the
GGA results¹² which show H⁻ binding to an oxygen in
c-HfO₂. The formation of Hf–H bonds attracts the Hf atoms

![](./images/814751191882792960_12.jpg)

![](./images/814751191882792960_13.jpg)

FIG. 6. Atomic configurations of H in-
terstitial of different charge states in
MgO, (a) H⁻, (b) H⁰, (c) H⁺, and (d)
charge transition diagram.

![](./images/814751191882792960_14.jpg)

![](./images/814751191882792960_15.jpg)

FIG. 7. Atomic configurations of H interstitial of different charge states in m-HfO₂, (a) H⁻, (b) H⁰, (c) H⁺, and (d) charge transition diagram.

toward $H^{-}$ centre and this causes the breaking of two Hf-O backbonds. For $H^{0}$, $H^{0}$ forms an isolated interstitial, relatively faraway from neighboring atoms without disturbing the surrounding lattice. This is different from the GGA results $^{12}$ where $H^{0}$ binds to an oxygen. For $H^{+}$, $H^{+}$ binds to a three-fold coordinated oxygen with a O-H bond length of $0.96\ \text{Å}$. From the charge transition diagram in Fig. 7(d), H in m-HfO₂ is a negative U defect and $H^{0}$ is not stable at any Fermi energy in the gap. H in m-HfO₂ is found to be deep, with the (+/-) level lying about 4.0 eV above the VB edge and 1.8 eV below the CB edge. This is in contrast to the GGA + WDA conclusion that H is shallow in c-HfO₂. $^{12}$ H interstitial in m-HfO₂ was previously studied by LDA by Kang et al. $^{31}$ and recently been re-examined by HSE by Lyons et al. $^{32}$ The (+/-) transition level predicted in Ref. 32 is close to ours. Similarly, the hydrogen interstitial in a yttria-stabilized cubic zirconia has been studied by a hybrid functional and a (+/-) level about 3.4 eV above the VB edge was found. $^{33}$

### F. $La_{2}O_{3}$

In $La_{2}O_{3}$, La atoms are 7-fold coordinated, two thirds of the O atoms are four-fold and the rest are six-fold. The atomic configurations of H in $La_{2}O_{3}$ are shown in Fig. 8. For $H^{-}$, $H^{-}$ binds to three La atoms with La-H bond length of $2.36\ \text{Å}$. The formation of La-H bonds attracts the Hf atoms toward H-centre and this causes the breaking of two La-O backbonds. For $H^{0}$, $H^{0}$ still binds to two metal atoms but the bond lengths are $0.10\ \text{Å}$ longer than those in the case of $H^{-}$, indicating the tendency of $H^{-}$ to be an isolated interstitial. This is different from the GGA results $^{12}$ where $H^{0}$ binds to an oxygen. For

![](./images/814751191882792960_16.jpg)

![](./images/814751191882792960_17.jpg)

FIG. 8. Atomic configurations of H interstitial of different charge states in La₂O₃, (a) H⁻, (b) H⁰, (c) H⁺, and (d) charge transition diagram.

![](./images/814751191882792960_18.jpg)

![](./images/814751191882792960_19.jpg)

FIG. 9. Atomic configurations of H in- terstitial of different charge states in LaAlO₃, (a) H⁻, (b) H⁰, (c) H⁺, and (d) charge transition diagram.

$H^{+}$, $H^{+}$ binds to an oxygen with O-H bond length of $0.95\mathring{A}$. The initially 4-fold coordinated oxygen losses one bond with La to let $H^{+}$ sit at the site, the $OH^{-}$ ion and its three bonded La ions form a flatten pyramid with the O-H bond at the apex. The charge transition levels in Fig. 8(d) indicate that H in $La_{2}O_{3}$ is deep with the (+/-) level lying 3.0 eV above the VB edge and 2.3 eV below the CB edge. This contrasts to the GGA + WDA result that H is shallow donor in $La_{2}O_{3}$ where the (+/-) level is just above the CB edge. $^{12}$

As a similar trivalent metal oxide to $La_{2}O_{3}$, the hydrogen interstitial in bixbyite $Y_{2}O_{3}$ has been systematically studied by hybrid functionals and a similar H geometry has been found. $^{34}$ The (+/-) level is also deep in $Y_{2}O_{3}$ about 4.0 eV above the VB edge.

### G. LaAlO₃

LaAlO₃ is a perovskite oxide. The atomic configurations of H in LaAlO₃ are shown in Fig. 9. For $H^{-}$, $H^{-}$ binds to two La atoms with La-H bond length of $2.08\mathring{A}$. For $H^{0}$, $H^{0}$ does not form isolated interstitial but forms bond with an oxygen and two La atoms, the H-O bond length is $1.07\mathring{A}$. In $H^{+}$, $H^{+}$ binds to an oxygen with O-H bond length of $0.97\mathring{A}$, similar to that in $H^{0}$. The charge transition levels of H in LaAlO₃ (Fig. 9(d)) show that (+/-) lies at 4.3 eV above the VB edge and about 1.0 eV below the CB edge, which is a borderline between shallow and deep. This is in contrast to the GGA + WDA conclusion that H is a shallow donor in LaAlO₃. $^{12}$

### H. Ga₂O₃

$Ga_{2}O_{3}$ has the same crystalline symmetry as that of $\theta$-Al₂O₃. Half of the Ga are four fold and the other half are six fold sites; 2/3 of the O are three fold and the rest are four fold. We include the semi-core 3d electrons of Ga explicitly in our calculation. The atomic configurations of H in $Ga_{2}O_{3}$ are shown in Fig. 10. For $H^{-}$, $H^{-}$ binds to two Ga atoms, which behaves similarly to that in $\theta$-Al₂O₃. The Ga-H bond length is $1.63\mathring{A}$. For $H^{0}$, instead of being an isolated interstitial as in $\theta$-Al₂O₃, it bonds to an three-fold oxygen with O-H bond length of $1.10\mathring{A}$. For $H^{+}$, $H^{+}$ binds to a three-fold oxygen with O-H bond length of $1.10\mathring{A}$. We then consider the charge transition levels as shown in Figure 10(d). (+/-) level is just above the CB edge in $Ga_{2}O_{3}$, indicating that H serves as shallow donor in $Ga_{2}O_{3}$. H in $Ga_{2}O_{3}$ is known to be shallow donor experimentally $^{35}$ and this has been demonstrated by hybrid functional calculation. $^{36}$

### I. TiO₂ and SnO₂

TiO₂ and SnO₂ have the same crystalline symmetry as that of r-GeO₂. The atomic configurations of H in TiO₂ and SnO₂ are shown in Figures 11 and 12, respectively. For $H^{-}$ in both TiO₂ and SnO₂, $H^{-}$ binds to an oxygen. This is an entirely different behaviour of $H^{-}$ compared to $H^{-}$ in the oxides considered above, where $H^{-}$ always binds to the cations. The $H^{-}$ and $H^{0}$ configurations of H are the same as $H^{+}$. For $H^{+}$ in both TiO₂ and SnO₂, H binds to an oxygen. The O-H bond lengths are $0.98\mathring{A}$ and $0.98\mathring{A}$ in TiO₂ and SnO₂, respectively. In each case, H binds to the oxygen without the need to break the host metal-O bond, and it barely disturbs the host lattice because the donor state is now delocalized.

We consider the charge transition properties, as shown in Figures 11(d) and 12(d) for TiO₂ and SnO₂, respectively. We found that $H^{+}$ is always the lowest energy state for all Fermi energies across the band gap. The (+/-) levels are above the CB edge for both oxides. This means that H acts as shallow donor in both oxides. As there is minor geometry relaxation of H in different charge states, the relaxation energy $\mathrm{U}=\mathrm{E}(+/0)-\mathrm{E}(0/-)$ is small. These properties agree with previous density functional results. $^{3,5}$

H in SnO₂ is known to be a shallow donor experimentally $^{37}$ and has been demonstrated by a previous hybrid functional calculation. $^{38}$ H in TiO₂ has been found to serve as shallow donor. $^{39,40}$ Despite the similar atomic structure of

![](./images/814751191882792960_20.jpg)

FIG. 10. Atomic configurations of H interstitial of different charge states in $Ga_{2}O_{3}$, (a) $H^{-}$, (b) $H^{0}$, (c) $H^{+}$, and (d) charge transition diagram.

interstitial hydrogen in both $SnO_{2}$ and $TiO_{2}$, IR spectroscopy suggests that interstitial H gives rise to small polaron and the donor electron is self-trapped at Ti in $TiO_{2}$, due to the d-character nature of conduction band states in $TiO_{2}$ rather than the s- and p-characters as in $SnO_{2}.^{41}$

### J. $CuAlO_{2}, CuInO_{2}, SrCu_{2}O_{2}$
Finally, we consider $CuAlO_{2}, CuInO_{2}$, and $SrCu_{2}O_{2}$. An extensive study on the electronic structures of the Cu based TCO family using hybrid functionals has been carried out, $^{42}$ as it belongs to only a few classes of TCOs that show p-type conductivity. The limits to doping are also studied. $^{43}$ As accidentally doping by intrinsic defects or hydrogen interstitial has been widely reported for many TCOs, the intrinsic defects in $CuAlO_{2}$ have been studied and the conductivity limits have been demonstrated. $^{44}$ Here, we consider H as an extrinsic source. We use the hexagonal phase of $CuAlO_{2}$. Although not having been reported experimentally, we still use the hexagonal phase of $CuInO_{2}$, adopting the lattice parameters from HSE calculation, $^{45}$ for the purpose of direct comparison with hexagonal $CuAlO_{2}$. They are p-type TCOs with a relative high valence band energy. For $H^{-}$, in $CuAlO_{2}$ hydrogen is found to bind to three adjacent Cu atoms with bond length $\sim 1.71\mathring{A}$, forming a flat structure, as shown in Fig. 13(a). For $H^{0}$, in $CuAlO_{2}$ the atomic configuration is similar to that of $H^{-}$ with Cu-O bond length $\sim 1.70\mathring{A}$. For $H^{+}$, in $CuAlO_{2}$ hydrogen binds to an oxygen, forcing the oxygen to lose a back bond with an Al atom behind, this is the $H_{i}^{AB2}$ interstitial site in p-type $Cu_{2}O$ described in Scanlon and Watson $^{46}$ Scanlon $^{46}$ found that the hydrogen interstitial was most stable in all charge states at a tetrahedral site binding to four Cu atoms. However, this is debatable. $^{47,48}$ The generally observed behavior of H in oxides is that cationic H

![](./images/814751191882792960_21.jpg)

FIG. 11. Atomic configurations of H interstitial of different charge states in $TiO_{2}$, (a) $H^{-}$, (b) $H^{0}$, (c) $H^{+}$, and (d) charge transition diagram.

![](./images/814751191882792960_22.jpg)

FIG. 12. Atomic configurations of H interstitial of different charge states in SnO₂, (a) H⁻, (b) H⁰, (c) H⁺, and (d) charge transition diagram.

binds to an oxygen, forming a single O–H bond. We also consider a H⁺ interstitial site that is 3-fold coordinated by the neighboring Cu atoms, the same as the H⁰ and H⁻ sites. We found that this interstitial geometry is $\sim$0.9 eV less stable for H⁺. H⁺ still favours bonding to an oxygen. The atomic structures of H of different charge states in CuInO₂ are similar to those in CuAlO₂ (not shown); H in +1 charge state is also found to be 1.6 eV more stable binding to O than to Cu in CuInO₂. The charge transition levels then indicate that the H⁰ state is not stable for all Fermi energies across the band gap, and the H interstitial is a negative U defect. The formation energy of H⁺ bonding to the Cu cation site is shown for comparison, as the higher line. The (+/−) level lies near mid-gap. Despite the rather low CNL energy, the +/− level lies above the VB edge, in both CuAlO₂ and CuInO₂.

![](./images/814751191882792960_23.jpg)

FIG. 13. Atomic configurations of H interstitial of different charge states in CuAlO₂, (a) H⁻, (b) H⁺, and (c) charge transition diagram.

In SrCu₂O₂, For H⁻¹, H stays in the centre of the tetrahedral site by four Cu cations with Cu-H distance of 1.87 Å, as shown in Fig. 14(a). For H⁰, H also occupies the centre of Cu tetrahedron. Cu tetrahedron is only slightly disturbed by H in these two cases. For H⁺¹, H is found to be stable binding to an oxygen, resulting in a six fold coordinated oxygen. The O–H bond length is 1.00 Å. The formation of O–H bond is accompanied by large distortion of Cu tetrahedron where a Cu nearby significantly relaxes away from the tetrahedron centre. The possibility of H binding to Cu cation in the +1 charge state is also examined. We found it 1.0 eV less stable than binding to O anion. The charge transition diagram

![](./images/814751191882792960_24.jpg)

FIG. 14. Atomic configurations of H interstitial of different charge states in SrCu₂O₂, (a) H⁻, (b) H⁺, and (c) charge transition diagram.

features similarly to those of $CuAlO_2$ and $CuInO_2$ where (+/−) level is near mid-gap.

## K. Band alignments
It is interesting to arrange the $+/-$ transition energies (red lines) according to the band alignments of the host materials, as is done in Fig. 15. The materials were aligned according to their electron affinity (EA) values as determined by photoemission and electrochemical methods. $^{49-63}$ For the purpose of comparison, CNL of each oxide is also shown as orange line in the diagram. A collection of EA and CNL val- ues were given in Robertson. $^{49}$ Explicitly, the EA data for TCOs: $SnO_{2}, CuAlO_{2}, CuInO_{2}$ , and $SrCu_{2} O_{2}$ are from Hosono $^{50}$ and for $Ga_{2} O_{3}$ are from Minami et al. $^{51}$ The EA data for $TiO_{2}$ are from Gratzel $^{52}$ and Klein. $^{54}$ The EA of $HfO_{2}$ was measured by Sayan et al., $^{56}$ Cook et al., $^{57}$ and Liu; $^{53}$ the latter is used. The EA data for $LaAlO_{3}$ are from Edge et al. $^{58}$ The EA for $La_{2} O_{3}$ and $\theta-Al_{2} O_{3}$ are not known, we use estimated values as proposed in Robertson and Falabretti $^{59}$ and Fonseca et al. $^{60}$ We also note the band align ment found by Afanasev. $^{59}$ The EA of $SiO_{2}$ and $q-GeO_{2}$ are from barrier height measurements on Si and Ge, respec- tively. We assume an alignment of $q-GeO_{2}$ and $r-GeO_{2}$ va lence band maximum since both valence band tops mainly consists of $O$ p states. The EA data for $MgO$ are from Sze and $Ng^{62}$ The EA data for $\alpha-Al_{2} O_{3}$ are from Schmickler andSchultze. $^{63}$

Previously Xiong et al. $^{12}$ suggested that the $(+/-)$ level might lie at a constant energy above the oxide VB edge, based on their GGA + WDA study. On the other hand, Kilic et al. $^{3}$ proposed a "hydrogen pinning level" at about3.0 ±0.4eV below the vacuum level, based on a LDA plus empirical correction to the band gap. Our value is deeper than this.

For semiconductors, van de Walle and Neugebauer $^{4}$  pointed out that the $(+/-)$ level seems to lie at about $4.5 eV$ below the vacuum level, based on a LDA study. This was explained as follows. $H$ has three charge states, $-, 0$ , and +. For cases where hydrogen gives rise to a deep gap state, then the $H^{+}$ site binds to the anion by breaking a host cation-anion bond, and this leaves a cation dangling bond. On the other hand, $H^{-}$ binds to the cation, by breaking a cation-anion bond and so it leaves an anion dangling bond. The average energy of the cation dangling bond and the anion dangling bond is roughly the CNL, a reference energy. The interesting fact is that this reference energy related to the band structures also seems to lie at a definite energy of about $4.5 eV$ below the vacuum level, even though the bands could in principle lie at any energy below the vacuum level. Now the tetrahedrally bonded semiconductors are a narrow range of materials, structurally. It is possible that this refer- ence energy could apply more generally, if a wider class of materials is tested, as here.

![](./images/814751191882792960_25.jpg)

FIG. 15. Band structures of oxides are aligned to the vacuum level according to experimental values. Dashed line is guide for eyes suggesting a constant value of $(+/-)$ below the vacuum.

We see with the new HSE calculations that the $+/-$ lev els do line up reasonably close to the CNL energies, and at a roughly constant energy below the vacuum level, Fig. 13. We find that $(+/-)$ levels of each oxide tend to lie at a rela tive constant value $\sim 3.9 eV$ below the vacuum. This value is deeper that in Kilic and Zunger $^{3}$ but higher than van deWalle. $^{4}$

In oxides that we considered, there is no guarantee that the $(+/-)$ levels lie at the same energy as the CNL. This is because in oxides, $H^{+}$ can datively bind to the oxygen site without needing to break a metal-oxygen bond, so there need be no close relationship to dangling bonds as there was in the case of tetrahedral semiconductors.

## IV. CONCLUSION
We have studied the behaviour of interstitial hydrogen in various oxides, using the hybrid functional HSE06 to relax the atomic and electronic structures. The oxide bonds vary from covalent to ionic and their band gaps range from $2.0 eV$ to $9.0 eV$ . The behaviours of hydrogen in these oxides have two types: the first one is that $H$ acts as amphoteric intersti tial with $(+/-)$ level in the band gap. The role of such $H$ is a compensating centre and always counteracts the prevailing conductivity. Oxides in which $H$ behaves like this include $SiO_{2}, GeO_{2}, Al_{2} O_{3}, MgO, m-HfO_{2}, La_{2} O_{3}, LaAlO_{3}$ , $CuAlO_{2}, CuInO_{2}$ , and $SrCu_{2} O_{2}$ , of which $H$ in $r-GeO_{2}$ is a borderline between donor and deep, $H$ in $LaAlO_{3}$ is a border line between shallow and deep. $H$ in these oxides show a large negative $U$ effect due to large geometry relaxation indifferent charge states. Typically, $H^{+}$ binds to an oxygen, $H^{0}$  forms isolated interstitial and $H^{-}$ binds to a cation.

The second type is that $H$ acts as shallow donor with $(+/-)$ level above the CB edge. $Ga_{2} O_{3}, TiO_{2}$ , and $SnO_{2}$ are included for this type of hydrogen behaviour. $H^{+}$ is the sta ble state in the span of Fermi energy across the band gap in these oxides. For $TiO_{2}$ and $SnO_{2}, H$ in different charge states always binds to an oxygen and there is no significant geome- try relaxation of $H$ in different charge states, thus the relaxa tion energy $U$ is small. For $Ga_{2} O_{3}, H^{0}$ tends to bind with an oxygen which has similar structure to $H^{+}$ . The $+/-$ transi tion level is found to lie at a roughly constant energy~3.9eV below the vacuum level.

1C. G. Van de Walle, P. J. H. Denteneer, Y. Bar- Yam, and S. T. Pantelides, Phys. Rev. B 39, 10791 (1989); J. Neugebauer and C. G. Van De Walle, Phys. Rev. Lett. 75, 4452 (1995).

$^{2}$C. G. van de Walle, *Phys. Rev. Lett.* **85**, 1012 (2000).

$^{3}$C. Kilic and A. Zunger, *Appl. Phys. Lett.* **81**, 73 (2002).

$^{4}$C. G. van de Walle and J. Neugebauer, *Nature* **423**, 626 (2003).

$^{5}$P. W. Peacock and J. Robertson, *Appl. Phys. Lett.* **83**, 2025 (2003); J. Robertson and P. W. Peacock, *Thin Solid Films* **445**, 155 (2003).

$^{6}$M. D. McCluskey, M. C. Tarun, and S. T. Teklemichael, *J. Mater. Res.* **27**, 2190 (2012).

$^{7}$A. Janotti and C. G. van de Walle, *Nature Mater.* **6**, 44 (2007).

$^{8}$T. Norby, *MRS Bull.* **34**, 923–928 (2009).

$^{9}$K. Xiong and J. Robertson, *Appl. Phys. Lett.* **85**, 2577 (2004).

$^{10}$J. Robertson, *J. Vac. Sci. Technol.*, **B 18**, 1785 (2000).

$^{11}$J. Robertson, K. Xiong, and S. J. Clark, *Thin Solid Films* **496**, 1 (2006).

$^{12}$K. Xiong, J. Robertson, and S. J. Clark, *J. Appl. Phys.* **102**, 083710 (2007).

$^{13}$J. Heyd, G. E. Scuseria, and M. Ernzerhof, *J. Chem. Phys.* **118**, 8207 (2003); **124**, 219906E (2006).

$^{14}$J. Heyd and G. E. Scuseria, *J. Chem. Phys.* **121**, 1187 (2004).

$^{15}$A. V. Krakau, O. A. Vydrov, A. F. Izmaylov, and G. E. Scuseria, *J. Chem. Phys.* **125**, 224106 (2006).

$^{16}$S. F. J. Cox, *J. Phys.: Condens. Matter* **15**, R1727 (2003).

$^{17}$S. F. J. Cox, J. L. Gavartin, J. S. Lord, S. P. Cottrell, J. M. Gil, H. V. Alberto, J. P. Duarte, R. C. Vilao, N. A. Campos, D. J. Keeble, E. A. Davis, M. Charlton, and D. P. van der Werf, *J. Phys.: Condens. Matter* **18**, 1079 (2006).

$^{18}$M. D. Segall, P. J. D. Lindan, M. J. Probert, C. J. Pickard, P. J. Hasnip, S. J. Clark, and M. C. Payne, *J. Phys.: Condens. Matter* **14**, 2717 (2002).

$^{19}$F. Oba, A. Togo, I. Tanaka, J. Paier, and G. Kresse, *Phys. Rev. B* **77**, 245202 (2008).

$^{20}$A. Janotti, J. B. Varley, P. Rinke, N. Umezawa, G. Kresse, and C. G. Van de Walle, *Phys. Rev. B* **81**, 085210 (2010).

$^{21}$M. A. L. Marques, J. Vidal, M. J. T. Oliveira, L. Reining, and S. Botti, *Phys. Rev. B* **83**, 035119 (2011).

$^{22}$W. Chen and A. Pasquarello, *Phys. Rev. B* **86**, 035134 (2012).

$^{23}$S. J. Clark and J. Robertson, *Phys. Rev. B* **82**, 085208 (2010).

$^{24}$S. Lany and A. Zunger, *Phys. Rev. B* **78**, 235104 (2008).

$^{25}$A. Yokozawa and Y. Miyamoto, *Phys. Rev. B* **55**, 13783 (1997).

$^{26}$P. E. Blochl and J. H. Stathis, *Phys. Rev. Lett.* **83**, 372 (1999).

$^{27}$K. Xiong, L. Lin, J. Robertson, and K. J. Cho, *Appl. Phys. Lett.* **99**, 032902 (2011).

$^{28}$D. R. Jennison, P. A. Schultz, and J. P. Sullivan, *Phys. Rev. B* **69**, 041405(R) (2004).

$^{29}$D. Liu, S. J. Clark, and J. Robertson, *Appl. Phys. Lett.* **96**, 032905 (2010).

$^{30}$J. R. Weber, A. Janotti, and C. G. Van de Walle, *Microelectron. Eng.* **86**, 1756 (2009).

$^{31}$J. Kang, E. C. Lee, K. J. Chang, and Y. G. Jin, *Appl. Phys. Lett.* **84**, 3894 (2004).

$^{32}$J. L. Lyons, A. Janotti, and C. G. van de Walle, *Microelectron. Eng.* **88**, 1452 (2011).

$^{33}$A. G. Marinopoulos, *Phys. Rev. B* **86**, 155144 (2012).

$^{34}$E. L. Silva, A. G. Marinopoulos, R. C. Vilao, R. B. L. Vieira, H. V. Alberto, J. Piroto Duarte, and J. M. Gil, *Phys. Rev. B* **85**, 165211 (2012).

$^{35}$P. D. C. King, I. McKenzie, and T. D. Veal, *Appl. Phys. Lett.* **96**, 062110 (2010).

$^{36}$J. B. Varley, J. R. Weber, A. Janotti, and C. G. Van de Walle, *Appl. Phys. Lett.* **97**, 142106 (2010).

$^{37}$P. D. C. King, R. L. Lichti, Y. G. Celebi, J. M. Gil, R. C. Vilao, H. V. Alberto, J. Piroto Duarte, D. J. Payne, R. G. Egdell, I. McKenzie, C. F. McConville, S. F. J. Cox, and T. D. Veal, *Phys. Rev. B* **80**, 081201(R) (2009).

$^{38}$A. K. Singh, A. Janotti, M. Scheffler, and C. G. Van de Walle, *Phys. Rev. Lett.* **101**, 055502 (2008).

$^{39}$F. Herklotz, E. V. Lavrov, and J. Weber, *Phys. Rev. B* **83**, 235202 (2011).

$^{40}$D. A. Panayotov and J. J. T. Yates, *Chem. Phys. Lett.* **436**, 204 (2007).

$^{41}$M. Stavola, F. Bekisli, W. Yin, K. Smithe, W. B. Fowler, and L. A. Boatner, *J. Appl. Phys.* **115**, 012001 (2014).

$^{42}$R. Gillen and J. Robertson, *Phys. Rev. B* **84**, 035125 (2011).

$^{43}$J. Robertson and S. J. Clark, *Phys. Rev. B* **83**, 075205 (2011).

$^{44}$D. O. Scanlon and G. W. Watson, *J. Phys. Chem. Lett.* **1**, 3195 (2010).

$^{45}$M. Kumar, H. Zhao, and C. Persson, *Semicond. Sci. Technol.* **28**, 065003 (2013).

$^{46}$D. O. Scanlon and G. W. Watson, *Phys. Rev. Lett.* **106**, 186403 (2011).

$^{47}$K. Biswas, M. H. Du, J. T-Thienprasert, S. Limpijumnong, and D. J. Singh, *Phys. Rev. Lett.* **108**, 219703 (2012).

$^{48}$D. O. Scanlon and G. W. Watson, *Phys. Rev. Lett.* **108**, 219704 (2012).

$^{49}$J. Robertson, *J. Vac. Sci. Technol.*, **A 31**, 050821 (2013).

$^{50}$H. Hosono, in *Recent Progress in Transparent Electronics*, edited by A. Facchetti and T. Marks (Wiley, New York, 2010), Chap. 2.

$^{51}$T. Minami, T. Miyata, and T. Yamamoto, *Surf. Coat. Technol.* **108–109**, 583 (1998).

$^{52}$M. Gratzel, *Nature (London)* **414**, 338 (2001).

$^{53}$Z. Q. Liu, W. K. Chiam, J. S. Pan, and C. M. Ng, *J. Appl. Phys.* **109**, 093701 (2011).

$^{54}$A. Klein, *J. Am. Ceram. Soc.* **96**, 331 (2013).

$^{55}$M. T. Greiner, M. G. Helander, W. M. Tang, Z. B. Wang, J. Qiu, and Z. H. Lu, *Nature Mater.* **11**, 76 (2011).

$^{56}$S. Sayan, E. Garfunkel, and S. Suzer, *Appl. Phys. Lett.* **80**, 2135 (2002).

$^{57}$T. E. Cook, C. C. Fulton, W. J. Mecouch, R. F. Davis, G. Lucovsky, and R. J. Nemanich, *J. Appl. Phys.* **94**, 7155 (2003).

$^{58}$L. F. Edge, D. G. Schlom, S. A. Chambers, E. Cicerella, J. L. Freeouf, B. Hollander, and J. Schubert, *Appl. Phys. Lett.* **84**, 726 (2004).

$^{59}$J. Robertson and B. Falabretti, *J. Appl. Phys.* **100**, 014111 (2006).

$^{60}$L. R. C. Fonseca, D. Liu, and J. Robertson, *Appl. Phys. Lett.* **93**, 122905 (2008).

$^{61}$V. V. Afanasev and A. Stesmans, *J. Appl. Phys.* **102**, 081301 (2007).

$^{62}$R. E. Thomas, J. W. Gibson, and G. A. Haas, *Appl. Surf. Sci.* **5**, 398 (1980); K. Shi, P. F. Zhang, H. Y. Wei, C. M. Ziao, C. M. Li, X. L. Liu, S. Y. Yang, Q. S. Zhu, and Z. G. Wang, *Solid State Commun.* **152**, 938 (2012); S. M. Sze and K. K. Ng, *Physics of Semiconductor Devices* (Wiley, 2007).

$^{63}$W. Schmickler and J. W. Schultze, in *Modern Aspects of Electrochemistry*, edited by J. M. O'Bockris (Plenum, London, 1986), Vol. 17.