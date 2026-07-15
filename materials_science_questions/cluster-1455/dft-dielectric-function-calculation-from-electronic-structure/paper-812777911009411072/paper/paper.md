Integrated Ferroelectrics
An International Journal

ISSN: 1058-4587 (Print) 1607-8489 (Online) Journal homepage: https://www.tandfonline.com/loi/ginf20

# The study of magnetic and electronic properties of Ni doped ZnO in low dimensional polar and non-polar surfaces structure by density functional theory

Chumpol Supatutkul, Sittichain Pramchu, Atchara Punya Jaroenjittichai & Yongyut Laosiritaworn

To cite this article: Chumpol Supatutkul, Sittichain Pramchu, Atchara Punya Jaroenjittichai & Yongyut Laosiritaworn (2019) The study of magnetic and electronic properties of Ni doped ZnO in low dimensional polar and non-polar surfaces structure by density functional theory, Integrated Ferroelectrics, 195:1, 208-219, DOI: 10.1080/10584587.2019.1570034

To link to this article: https://doi.org/10.1080/10584587.2019.1570034

![](./images/812777911009411072_1.jpg)
Published online: 07 May 2019.

![](./images/812777911009411072_2.jpg)
Submit your article to this journal ➚

![](./images/812777911009411072_3.jpg)
Article views: 1

![](./images/812777911009411072_4.jpg)
View Crossmark data ➚

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=ginf20

INTEGRATED FERROELECTRICS
2019, VOL. 195, 208–219
https://doi.org/10.1080/10584587.2019.1570034

![](./images/812777911009411072_5.jpg)

![](./images/812777911009411072_6.jpg)

# The study of magnetic and electronic properties of Ni doped ZnO in low dimensional polar and non-polar surfaces structure by density functional theory

Chumpol Supatutkul, Sittichain Pramchu, Atchara Punya Jaroenjittichai, and Yongyut Laosiritaworn

Department of Physics and Materials Science Faculty of Science, Chiang Mai University, Chiang Mai, Thailand

## ABSTRACT
The study of ZnO nanostructures is interested because the various types of nanostructures can be easily fabricated. However, the magnetic ground state of Ni-doped ZnO nanostructures can either be ferromagnetic or antiferromagnetic. Therefore, this work used DFT calculation to investigate the ZnO in low dimensional structures in both polar (0001) surfaces and non-polar (10$\overline{1}$0) surfaces. The two Ni atoms were substituted on the Zn sites. The results show that the polar (0001) surfaces is more stable than the non-polar (10$\overline{1}$0) surfaces. The energy differences between ferromagnetic states and antiferromagnetic state indicate that the ground states are ferromagnetic except only when the Ni atoms substitute on the slab surface in ZnO polar (0001) surfaces. The total magnetic moments of about $4\,\mu_B$ are found to be contributed by the Ni-$3d$ states in both polar and non-polar surfaces, and the half-metallic behavior is also predicted in the ZnO non-polar (10$\overline{1}$0) surfaces.

## ARTICLE HISTORY
Received 31 October 2017
Accepted 22 June 2018

## KEYWORDS
Ni-doped ZnO; ZnO polar (0001) surfaces; ZnO non-polar (10$\overline{1}$0) surfaces;
Density Functional Theory

## 1. Introduction
Dilute magnetic semiconductor (DMS) is non-magnetic semiconductor doped with a small fraction of magnetic elements where the magnetic atoms replace host cations. The fascinating of DMSs beyond conventional charge-based electronics is that they possess both charge and spin which can be manipulated and utilized in spintronics devices [1, 2]. The III-V based DMSs, e.g. (Ga,Mn)As, has been studied and experimented. However, since their ferromagnetic curie temperatures are typically less than the operating temperature, i.e. the room temperature, their best utilization is rather limited. Nevertheless, researchers have recently showed that ZnO-based DMSs yield intrinsic room-temperature ferromagnetism which is a promising candidate in spintronic applications [3]. Specifically, ZnO is a II-VI compound that has various useful properties such as piezoelectric, optical transparent, and magnetic (depending on how it is dope). For instance, ZnO in wurtzite structure has wide band gap and a large exciton binding energy [4]. Furthermore, it has polar surfaces which are arisen from alternating planes

---
CONTACT Y. Laosiritaworn  ![](./images/812777911009411072_7.jpg) yongyut_laosiritaworn@yahoo.com ![](./images/812777911009411072_8.jpg) Department of Physics and Materials Science, Faculty of Science, Chiang Mai University, Chiang Mai 50200, Thailand
© 2019 Taylor & Francis Group, LLC

between $O^{2-}$ and $Zn^{2+}$ ions stacking along the $c$-axis. Then, the positive charge on (0001)-Zn terminated and negative charge on $(000\overline{1})$-O terminated layers produce spontaneous polarization along the growth direction (dipole moments is perpendicular to the surface). Since many transition metal doped in ZnO (ZnO:TM) has been theoretically predicted to be ferromagnetic at room temperature, as described by Zener Model [5]. Many experimental techniques were then carried out to fabricate the ferromagnetic ZnO:TM. However, their magnetic properties somewhat depend on fabrication techniques and preparation conditions, which cause some difficulties in the reproduction. On the other hand, there was an experimental report that Ni-doped ZnO yields pronounced ferromagnetism compare with other ZnO:TMs, which are mostly antiferromagnetic [6]. However, it was further found that the ferromagnetism comes from the Ni clusters (as a secondary phase in the ZnO matrix) or even found that ZnO:Ni presents only paramagnetic phase in some reports [7]. The experimentalists also found that the magnetic moment of ZnO:Ni in low dimensions or nanostructure can yield either antiferromagnetism or ferromagnetism. These discrepancies on ZnO:Ni magnetism results bring some ambiguities in the topic, and require fundamental understanding in the origin and mechanism of ferromagnetic to sort out. Usually, the normal (uncontrolled) preparation of ZnO nanostructure leads to the various random growth of ZnO nanostructure morphologies and provide diverse nanosized effects. These nanosized effects play dominant roles in defining electronic structures and even magnetic properties. The $Zn_{0.96}Ni_{0.04}O$ thin-films prepared by radio frequency magnetron sputtering were showed that its properties depend on the films thickness. The magnetic moment is about $2\ \mu_B$/Ni at the films thickness of 15 nm and then drastically decreases to $0.08\ \mu_B$/Ni when the film thickness is about 330 nm [8]. Therefore, the reduced dimensionality as well as the surface effects may be the cause and origin of ferromagnetism in ZnO:Ni films. The underlying understanding of nano- and surface-effects in ferromagnetic mechanism of ZnO:Ni films could then provide approaches for controlling DMS properties applicable for desired spintronic devices. To seek for this knowledge is the objective of this study.

## 2. Materials and methods

In this work, electrical and magnetic profiles of Ni-doped ZnO were studied using density functional theory (DFT) within the framework of pseudo potential plane wave method implemented in Quantum Espresso package [9]. The DFT calculation used the generalized gradient approximation (GGA) in treating the exchange correlation potential as implemented by Pewdew-Burke-Ernzerhof functional (PBE) [10]. The pseudopotential calculation included valence electrons from orbitals {2s, 2p} of O atom, {3p, 3d} of Ni atom, and {3p, 3d, 4s} of Zn atom. The Ni-doped ZnO supercell slabs in polar (0001) surface consist of 96 atoms ($3a\times2b\times4c$) and non-polar $(10\overline{1}0)$ surfaces consist of 96 atoms ($4a\times2b\times3c$). The electron wave function was expanded in plane wave up to a cut off energy of 200 Ry and a gamma-centered grid of $2\times2\times1$ $k$-points and $1\times2\times2$ $k$-point were used for the ZnO polar (0001) and non-polar $(10\overline{1}0)$ surfaces, respectively. Then, the surface effect of Ni-doped ZnO was studied by substituting two Ni atoms on different Zn sites to represent the concentration of 4.16%. The impurity defects were categorized/modeled into three types, which are bulk, surface, and mixed

![](./images/812777911009411072_9.jpg)

Figure 1. The impurity defect models are bulk defect ((a) and (d)), surface defect ((b) and (e)), and mixed defect ((c) and (f)) in ZnO polar surface ((a)-(c)) and ZnO non-polar surface ((d)-(f)). The purple, red, and gray spheres are represented Zn, O, and Ni atoms, respectively.

defects (consisting of both bulk and surface defects) as shown in Figure 1a–c for ZnO polar surface and Figure 1d–f for ZnO non-polar surface. The surface defect has two Ni atoms substituting on two nearest Zn sites on slab surface, but the bulk defect has two Ni atoms substituting on Zn sites at the interior (the middle of the bulk). Then, the mixed defect has Ni atoms substituting on Zn sites deep down inside the bulk (i.e. bulk defect) and another one substituting on Zn site on the surface. So, the surface and the bulk defects represent the short Ni-Ni configuration, whereas the mixed defect represents the far Ni-Ni configuration. The total energies of Ni-doped ZnO were calculated in relaxed structures with two spin-polarized Ni atoms coupled ferromagnetically and antiferromagnetically in $c$-direction of ZnO polar (0001) and $a$-direction of ZnO non-polar (10$\overline{1}$0) surfaces. In each type/model, all atomic positions were relaxed by forced optimization.

<table>
<caption>Table 1. The DFT calculation results for energy difference $\Delta E = E_{AFM}-E_{FM}$, relative energy $E_r$, total magnetic moment, the magnetic moment per Ni ion, and magnetic ground state in each structure.</caption>
<thead>
<tr>
<th>Impurity defect</th>
<th>$\Delta E$(meV)</th>
<th>$E_r$(eV)</th>
<th>Total magnetic moment ($\mu_B$)</th>
<th>Magnetic moment of Ni ions</th>
<th>Magnetic ground state</th>
</tr>
</thead>
<tbody>
<tr>
<td>ZnO polar surface (0001)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bulk</td>
<td>156.004</td>
<td>0.278</td>
<td>4.36 (4.50)</td>
<td>1.5912 (1.5612)</td>
<td>FM</td>
</tr>
<tr>
<td>Surface</td>
<td>191.904</td>
<td>0</td>
<td>3.67 (3.86)</td>
<td>1.5230 (1.2430)</td>
<td>FM</td>
</tr>
<tr>
<td>Mixed</td>
<td>−0.974</td>
<td>0.232</td>
<td>0.80 (4.47)</td>
<td>1.6721 (−1.3340)</td>
<td>AFM</td>
</tr>
<tr>
<td>ZnO non-polar surface (10$\overline{1}$0)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bulk</td>
<td>49.486</td>
<td>4.401</td>
<td>4.11 (4.27)</td>
<td>1.5339 (1.5737)</td>
<td>FM</td>
</tr>
<tr>
<td>Surface</td>
<td>34.446</td>
<td>3.863</td>
<td>4.21 (4.42)</td>
<td>1.6238 (1.3930)</td>
<td>FM</td>
</tr>
<tr>
<td>Mixed</td>
<td>0.370</td>
<td>4.033</td>
<td>4.07 (4.30)</td>
<td>1.5843 (1.4369)</td>
<td>FM</td>
</tr>
</tbody>
</table>

## 3. Results and discussions

Firstly, the magnetic moment of bulk nickel was found as $0.45\ \mu_\text{B}$/Ni by the DFT calculation. It agrees well with the experimental result of the nickel cluster which has $0.4\ \mu_\text{B}$/Ni measured by x-ray magnetic circular dichroism (XMCD) [11]. From the DFT investigation of Ni impurity defect in ZnO with (0001) polar surface, the ground state was found in ferromagnetic phase for both surface and bulk defects as shown in Table 1. The surface defect yields total magnetic moment of $3.67\ \mu_\text{B}$ which is smaller than that of the bulk defect which has $4.36\ \mu_\text{B}$ of total magnetic moment. The magnetic moment in the surface defect is smaller than that in the bulk defect because the electros has more delocalized on the surface due to the low coordination and broken symmetry of surface atoms [12]. However, the surface defect is more energetic favorable in existing than the bulk defect (about 278 meV) for the Ni impurity doped in ZnO with (0001) polar surface. For the mixed defect, the antiferromagnetic state has energy slightly lower than that of the ferromagnetic state (about 0.974 meV), which suggests that this kind of defect may exist in the paramagnetic phase. As the surface defect is the most stable structures comparing with the bulk and the mixed defects, this means that the Ni atoms tend to cluster on the surface when doping in ZnO with (0001) polar surface. Note that, in the mixed defect, the total magnetic moment is $0.80\ \mu_\text{B}$ when two Ni atoms are coupled antiferromagnetically. This small remnant magnetic could possibly indicate ferrimagnetic state. The Ni doped ZnO on the non-polar (10$\overline{1}$0) surfaces were also investigated in the same manner as that on the polar (0001) surface. The ferromagnetic ground state was found existing for all kind of defects in ZnO with non-polar (10$\overline{1}$0) surface. The total magnetic moments of all impurity defects in ZnO with non-polar (10$\overline{1}$0) surface are larger than $4.0\ \mu_\text{B}$, where the most stable structure is again the surface defect similar to the case of ZnO with polar (0001) surface. Nevertheless, the mixed defect seems to be paramagnetic indicated by its small energy difference ($\Delta E$) of 0.370 meV, which is easily to get perturbed by thermal disturbance. Remark that when considering the stability of both polar and non-polar surfaces of Ni-doped ZnO, the relative energy ($E_r$) was calculated with respect to the surface defect in ZnO polar surface (0001), for indicating which one is the most stable structure. These relative energy $E_r$ shows that the defects in polar surface are more energetic favorable than those in non-polar surface as shown in Table 1. Note that the relative energy between the polar and non-polar surface structure is different more than about 3.5 eV. This energy difference implies the ZnO polar surface (0001) needs more thermal energy to demagnetize

magnetic moments than the ZnO non-polar surface (10$\overline{1}$0). So the curies temperature of the ZnO polar surface (0001) may be higher than the ZnO non-polar surface (10$\overline{1}$0). In addition, among surface, bulk and mixed defects, the surface defect is the most stable structure for both ZnO polar and non-polar surfaces, and their ground states are ferro- magnetic. This implies when being doped with Ni atoms, the doping atoms tend to cluster on the surfaces and their spins align ferromagnetically.

Next, to clarify about the origin of magnetic moment in Ni-doped ZnO in both polar and non-polar surfaces, the density of state (DOS) of each ground state were deter- mined. The total DOS of each impurity defects in Ni-doped ZnO on polar and non- polar surfaces are shown in Figures 2 and 3. These total DOSs give information of mag- netic moments being originated from states with energy about 4eV below from the Fermi level. The DOS of surface defects evidently show that spin up and spin down states near the Fermi level are asymmetrical as same as the DOS of bulk defect, which is the cause of magnetic moment emerging. For the ZnO polar (0001) surface, the DOS of mixed defect (Figure 2c) show some small differences between spin up and spin down states at energy about 1 eV below the Fermi level, which explains small remnant magnetic moment of 0.8 $\mu_B$ and suggests antiferromagnetic ground states. Moreover, the energy gap evidently exists in the spin up channel but shows the metallic state in the spin down channel in all of the impurity defects in the ZnO with non-polar (10$\overline{1}$0) surface, as shown in Figure 3. These existence of semiconductor state on one of the spin channel and the metallic state on the other spin channel suggests the half metallic behavior in the Ni-doped ZnO with non-polar (10$\overline{1}$0) surface, which is useful for spin- tronic application. Next, the partial density of states (PDOS) were determined to verify how the doping of Ni atoms modifies electronic states and contributes to the total mag- netic moment of ZnO with polar and non-polar surfaces slabs. The PDOS shows that two doped-Ni atoms modify the states close to the Fermi level, as can be seen in Figures 4 and 5. The Ni-3d orbital was found to be the key in modifying electronic states near Fermi level and contributes the most to the magnetic moment. On the other hand, the slightly asymmetric of PDOS in O-2p orbital near the Fermi level suggests that the O-2p orbital hybridizes with the Ni-3d orbital. This hybridization implies elec- trons being shared between two Ni atoms with nearest O atoms, leading to magnetic moment being induced on the nearest O atoms. Note that, the Zn-4s orbital contribute mainly on the conduction band for all defect types. The PDOSs of the bulk defect in Figures 4a and 5a show that the large magnetic moment comes from the Ni-3d states that lie below the Fermi level where almost the spin up states are filled up. The mag- netic moments contributed by each Ni atom are almost the same (as shown in Table 1), but the size of magnetic moments are different from the 2.0 $\mu_B$/Ni. Theoretically, the one empty 3d state contributed 1 $\mu_B$ of magnetic moment, however the electron delocal- ization reduces the magnetic moment by 30-50% of their atomic values [11]. The empty3d state of Ni atom in the bulk was calculated to be 1.5 states [13, 14] and in the sur- face cluster was calculated to be 0.7-1.2 states [15].

Moreover, the relative energy $(E_r)$ is indicating that the Ni:ZnO favor the short range ferromagnetic coupling of Ni atoms as the surface defect. The existing of short range ferromagnetic coupling in this Ni:ZnO can be described by the double exchange inter- action [16]. Where, the Ni-O-Ni interactions are found by the unequally of magnetic

![](./images/812777911009411072_10.jpg)

Figure 2. The total DOS of (a) bulk defect (b) surface defect and (c) mixed defect in ZnO polar surface, i.e. the (0001) slab. The Fermi energy level is set to zero.

![](./images/812777911009411072_11.jpg)

Figure 3. The total DOS of (a) bulk defect (b) surface defect and (c) mixed defect in ZnO non-polar surface, i.e. the (10$\overline{1}$0) slab. The Fermi energy level is set to zero.

![](./images/812777911009411072_12.jpg)

Figure 4. The PDOS of (a) bulk defect (b) surface defect and (c) mixed defect in ZnO polar surface,
i.e. the (0001) slab. The Fermi energy level is set to zero.

![](./images/812777911009411072_13.jpg)

Figure 5. PDOS of (a) bulk defect (b) surface defect and (c) mixed defect in ZnO non-polar surface (10$\overline{1}$0) slab. The Fermi energy level is set to zero.

moment on each Ni atoms as shown in Table 1 because the O gives up its spin to the one of nearest Ni atoms and the others Ni atom give up its spin to the O. Nevertheless, in the case of the surface defect (i.e. results in Figures 4b and 5b), the PDOSs are also modified by the two Ni atoms in the same way as that in the bulk defects, where almost the spin up states are filled up in Ni-3d orbital. However, the magnetic moments con- tributed by each Ni ion on the surface are quite different due to the different surface effect. This is because of the different environment of the atomic structure around Ni atoms when being on the surface and residing within the bulk, so the influence of potential arisen from other nearby atoms is lesser when being on the surface. For the mixed defect in ZnO with polar (0001) surface (i.e. see Figure 4c), the PDOS shows that almost the same amount of both spin up and spin down states are filled in Ni-3d orbital. The magnetic moments contributed by Ni atoms are $1.6721 \mu_{B}$ and $-1.3340 \mu_{B}$. The opposite sign (direction) of the Ni magnetic moment infers the structure is in the antiferromagnetic ground state, where Ni atom substituted on the surface has smaller magnetic moment magnitude. On the other hands, the mixed defect in ZnO non-polar $(10 \overline{1} 0)$ surface has ferromagnetic ground state. The magnetic moment of Ni atom sub stituting on the surface is smaller comparing with that of the Ni atom substituting in the bulk, which yield magnetic moment are $1.5843 \mu_{B}$ and $1.4369 \mu_{B}$, respectively. Because of Ni atom on the surface has more electron delocalization than the Ni atom in the bulk, the magnetic moment of the Ni on the surface is smaller. Note that the mag- netic moment per Ni atom in the bulk $(0.45 \mu_{B} / Ni)$ is much lower than the magnetic moment per Ni atom in these Ni-doped ZnO slabs due to the presence of a surface. Usually, the magnetic moments are increased in the low dimension due to the broken bond and relaxation of the surface atoms [17].

For the dielectric constant calculation of ZnO, only the dielectric constant of the non-polar surface can be determined because band energy gap only found in the non-polar surface but the polar surface show metallic behavior. DFT with GGA is known that it is usually under estimate band gap which yield the ZnO polar surface is in metallic state due to the overlapping of O-2p orbital overlap with the Zn-4s orbital. The calculated dielectric constant of ZnO non-polar $(10 \overline{1} 0)$ surface are showed in Table2. As the same reason, we have shown earlier that all studied cases of the Ni-doped ZnO slab in this work have the metallic state in spin down channel due to the Ni-3d orbital. So, the dielectric constant could not be found either in both Ni-doped ZnO polar and non-polar surface slab. Howerver, the experiment could measure the dielectric constant of Ni-doped ZnO and found that it is dominantly improve the dielectric for transition metal doped ZnO as mentioned in [18]. For the further study, to calculate dielectric constant of Ni-doped ZnO system, the methods such as DFT with Hubbard model (DFT + U) or hybrid functional should be used to correct the band gap and then the dielectric constant of Ni-doped ZnO may be found if the metallic behavior is disappeared.

Table 2. Dielectric constant calculation at high frequency.
<table>
<thead>
  <tr>
    <th>Dielectric constant</th>
    <th>ZnO (10$\overline{1}$0)</th>
    <th>ZnO (0001)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\varepsilon_{11}$</td>
    <td>2.12</td>
    <td>Metal</td>
  </tr>
  <tr>
    <td>$\varepsilon_{22}$</td>
    <td>3.12</td>
    <td>Metal</td>
  </tr>
  <tr>
    <td>$\varepsilon_{33}$</td>
    <td>3.17</td>
    <td>Metal</td>
  </tr>
</tbody>
</table>

## 4. Conclusions

The DFT investigations of Ni-doped ZnO in polar (0001) and non-polar (10$\overline{1}$0) surfaces have shown that the polar surface is more stable than the non-polar (10$\overline{1}$0) surface when doping by Ni atoms. Usually, the ZnO polar (0001) surface is less stable than the non-polar (10$\overline{1}$0) surface in the ZnO nanostructures due to the unbalanced charge of the Zn-terminated and O-terminated surface. Then, the Ni-doped ZnO have been pre- dicted to have ferromagnetic ground states except the mixed defect in ZnO polar (0001) surface slab, which has potential to be ferrimagnetic. The origin of magnetic moment is mainly contributed by the Ni-3d orbital, where the Ni atom on the slab surface has magnetic moment smaller than the bulk substitution due to the surface effect. Moreover, the half-metallic behavior that is useful for spintronic applications also found in all of the Ni configurations of the ZnO non-polar (10$\overline{1}$0) surface and in surface defect of ZnO polar (0001) surface.

## Funding

This work is supported by CMU Research Group Grant. The Development and Promotion of Science and Technology Talents Project (DPST, Thailand) is acknowledged for supporting CS.

## References

1.  P. V. Radovanovic, and D. R. Gamelin, High-temperature ferromagnetism in Ni2+-Doped ZnO aggregates prepared from colloidal diluted magnetic semiconductor quantum dots, *Phys. Rev. Lett.* **91**, 1572021 (2003).
2.  M. Zhong *et al.*, Effect of oxygen vacancy induced by pulsed magnetic field on the room-temperature ferromagnetic Ni-doped ZnO synthesized by hydrothermal method. *J. Alloys Cmpd.* **675**, 286 (2016). DOI: 10.1016/j.jallcom.2016.03.062.
3.  K. T. Kim*et al.*, Characteristics of Nickel-doped Zinc Oxide thin films prepared by sol-gel method. *Surface Coatings Technol.* **202** (22-23), 5650 (2008). DOI: 10.1016/j.surfcoat.2008.06.078.
4.  S. Datta*et al.*, Study of morphology effects on magnetic interactions and band gap varia- tions for 3 d late transition metal bi-doped ZnO nanostructures by hybrid DFT calcula- tions, *J. Chem. Phys.* **143** (8), 084309 (2015). DOI: 10.1063/1.4929510.
5.  T. Dietl *et al.*, Zener model description of ferromagnetism in zinc-blende magnetic semi- conductors. *Science* **287** (5455), 1019 (2000).
6.  J. Ren, H. Zhang, and X. Cheng, Electronic and magnetic properties of all 3d transition- metal-doped ZnO monolayers. *Int. J. Quantum Chem.* **113** (19), 2243 (2013). DOI: 10.1002/ qua.24442.
7.  G. Gu *et al.*, Magnetism in transition-metal-doped ZnO: A first-principles study. *J. Appl. Phys.* **112** (2), 023913 (2012). DOI: 10.1063/1.4739450.
8.  X. J. Liu *et al.*, Intrinsic and extrinsic origins of room temperature ferromagnetism in Ni- doped ZnO films, *J. Phys. D: Appl. Phys.* **42** (3), 035004 (2009). DOI: 10.1088/0022-3727/42/3/035004.
9.  P. Giannozzi *et al.*, QUANTUM ESPRESSO: A modular and open-source software project for quantum simulations of materials. *J. Phys: Condens. Matter.* **21** (39), 395502 (2009). DOI: 10.1088/0953-8984/21/39/395502.
10. J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, *Phys. Rev. Lett.* **77** (18), 3865 (1996).
11. A. Langenberg *et al.*, Spin and orbital magnetic moments of size-selected iron, cobalt, and nickel clusters, *Phys. Rev. B - Condensed Matter Mater. Phys.* **90**, 184420 (2014).

12. G. Guzmán-Ramírez *et al.*, Stability, structural, and magnetic phase diagrams of ternary ferromagnetic 3d-transition-metal clusters with five and six atoms. *J. Chem. Phys.* **134** (5), 054101 (2011). DOI: 10.1063/1.3533954.

13. H. Basch, M. D. Newton, and J. W. Moskowitz, The electronic structure of small nickel atom clusters, *J. Chem. Phys.* **73** (9), 4492 (1980). DOI: 10.1063/1.440687.

14. G. Pacchioni, and P. Fantucci, Spin states and quenching of magnetism in naked and car- bonylated nickel clusters. *Chem. Phys. Lett.* **134** (5), 407 (1987). DOI: 10.1016/0009-2614(87)87163-4.

15. R. Wu, and A. J. Freeman, Limitation of the magnetic-circular-dichroism spin sum rule for transition metals and importance of the magnetic dipole term, *Phys. Rev. Lett.* **73** (14), 1994 (1994).

16. C. Zener, Interaction between the $d$-Shells in the transition metals. II. Ferromagnetic compounds of manganese with perovskite structure, *Phys. Rev.* **82** (3), 403 (1951). DOI: 10.1103/PhysRev.82.403.

17. S. E. Apselet *al.*, Surface-enhanced magnetism in nickel clusters, *Phys. Rev. Lett.* **76** (9), 1441 (1996).

18. S. Rajeh *et al.*, Structural, morphological, optical and opto-thermal properties of Ni-doped ZnO thin films using spray pyrolysis chemical technique, *Bull. Mater. Sci.* **39** (1), 177 (2016). DOI: 10.1007/s12034-015-1132-4.