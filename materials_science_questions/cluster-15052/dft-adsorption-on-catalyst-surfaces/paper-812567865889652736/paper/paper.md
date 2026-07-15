Applied Surface Science 537 (2021) 147711

![](./images/812567865889652736_1.jpg)

Contents lists available at ScienceDirect

Applied Surface Science

journal homepage: www.elsevier.com/locate/apsusc

![](./images/812567865889652736_2.jpg)

# Scavenging properties of yttrium nitride monolayer towards toxic sulfur gases

Apinya Ngoipala$^{a}$, Thanayut Kaewmaraya$^{a,b,*}$, Tanveer Hussain$^{c,*}$, Amir Karton$^{c}$

$^{a}$ Integrated Nanotechnology Research Center, Department of Physics, Khon Kaen University, Khon Kaen 40002, Thailand
$^{b}$ Institute of Nanomaterials Research and Innovation for Energy (IN-RIE), Research Network of NANOTEC- KKU (RNN), Khon Kaen University, Khon Kaen, 40002, Thailand
$^{c}$ School of Molecular Sciences, The University of Western Australia, Perth, WA 6009, Australia

![](./images/812567865889652736_3.jpg)

## ARTICLE INFO

**Keywords:**
2D monolayer
Gas adsorption
Electronic structure properties
Charge transfer

## ABSTRACT

We employ first-principles calculations based on density functional theory (DFT) to investigate the adsorption characteristics of a novel 2D material, hexagonal yttrium nitride (h-YN) monolayer, towards sulfur-containing gases (SCG) such as H₂S and SO₂. Dispersion corrected DFT calculations were carried out to explore the adsorption mechanism, structural and electronic properties of pristine and SCG-adsorbed h-YN (with and without the presence of O₂). Our calculations reveal that both H₂S and SO₂ are strongly adsorbed on pristine h-YN with adsorption energies of -3.24 and -4.21 eV, respectively. However, the presence of molecular oxygen plays an important role in reducing the adsorption energies to -2.46 and -1.75 eV for H₂S and SO₂, respectively. Strong chemisorption, even in the presence of O₂, makes h-YN suitable for non-reversible capturing of H₂S and SO₂. In case of SO₂, molecular adsorption coupled with significant variations in the electronic properties and charge transfer indicates the suitability of h-YN for SO₂ capture and a disposable sensing material.

## 1. Introduction

Sulfur-containing gases (SCG) such as sulfur dioxide (SO₂) and hydrogen sulfide (H₂S) are toxic chemicals to humans and animals at low concentrations. These major pollutants are generally produced from anthropogenic activities and they can be emitted to the atmosphere. In particular, SO₂ can be produced industrially from the combustion of materials that contain sulfur, e.g., coal, oil, fossil fuels, and minerals [1]. The annual emission of this gas is estimated to be $1.20\times10^{8}$ tons worldwide [2]. Meanwhile, H₂S occurs naturally in crude petroleum, volcanic gas, natural gas, and it can also be generated via decompositions of organic matters and sewage [3]. According to the World Health Organization (WHO), estimated $8.3\times10^{5}$ tons of H₂S are globally released to the atmosphere each year. As a result, the released SCG have major impacts on both human health and the environment if not handled properly [4-6]. Therefore, it is crucial to effectively capture them from oil and gas industries to reduce air pollution. In recent years, a variety of materials including charcoal carbon [7], activated carbon [8], fullerene [9], zeolites [10,11], and metal organic frameworks (MOF) [12] have been demonstrated as promising removal of SCG. Moreover, increasing attentions of gas adsorption have been paid to two-dimensional (2D) crystals [13], the materials consisting of single or few layers of atoms. Typical 2D materials possess high surface-to-volume ratio and high electrical conductivities [14]. These preferable features expectedly profits applications associated with the gas adsorption (such as gas sensors, gas separation, and gas capturing) [13].

To date, numerous experimental and theoretical studies have reported the feasibility of various 2D materials (i.e., graphene and their derivatives [15], MoS₂ [16], phosphorene [17,18]) as efficient adsorbents for common pollutants [19-27]. This is because of the underlying charge transfer process between a 2D sorbent and target analytes which characterizes the weak physisorption and strong chemisorption [13,28], depending on the magnitudes of adsorption energies [18]. Moreover, 2D materials also allow possibilities to tune the magnitudes of adsorption energies by means of doping, strain, and surface functionalization [13]. In particular, these can benefit the adsorption capacities and the regeneration [11]. The latter is desirable for practical reversible gas capturing applications and it is one of the major problems found in 3D capturing materials [11]. Very recently, 2D hexagonal yttrium nitride monolayer (h-YN) has been predicted by Zheng et al. [29]. The novel h-YN is a semiconductor with an indirect band gap of 2.32 eV and it exhibits desirable dynamical, thermal and

* Corresponding authors at: Integrated Nanotechnology Research Center, Department of Physics, Khon Kaen University, Khon Kaen 40002, Thailand (T. Kaewmaraya).
E-mail addresses: thakaew@kku.ac.th (T. Kaewmaraya), t.hussain@uq.edu.au (T. Hussain).

https://doi.org/10.1016/j.apsusc.2020.147711
Received 10 February 2020; Received in revised form 7 August 2020; Accepted 27 August 2020
Available online 14 September 2020
0169-4332/ © 2020 Elsevier B.V. All rights reserved.

mechanical stabilities. It also possesses high electron and hole mobility of up to $10^{4}\ \text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$ and $10^{3}\ \text{cm}^{2}\text{V}^{-1}\text{s}^{-1}$, respectively, indicating the light electron effective masses and rapid electrical transport. These appealing features render h-YN a promising candidate in future nanoscale applications, including gas storage or removal. However, to the best of our knowledge, there has been no study on h-YN in SCG storage/ removal applications.

In this work, we investigate the adsorption characteristics of h-YN towards SCG in the presence of environmental oxygen impurities by means of periodic boundary condition density functional theory (DFT) procedures. Our findings reveal that both $\text{H}_{2}\text{S}$ and $\text{SO}_{2}$ are strongly adsorbed on pristine h-YN, being practically elusive for reversible capturing. On the other hand, the presence of ambient $\text{O}_{2}$ on h-YN (i.e., $\text{O}_{2}$-h-YN) significantly reduces the adsorption energies of $\text{H}_{2}\text{S}$ and $\text{SO}_{2}$ as compared to pristine h-YN. In addition, the electronic properties of pristine h-YN and $\text{O}_{2}$-h-YN are remarkably altered upon SCG exposure.

## 2. Computational details

Density functional theory (DFT) calculations were carried out as implemented in the Vienna *Ab-Initio* Simulation Package (VASP) [30,31]. The projector augmented-wave (PAW) pseudopotentials [32] were used to treat electron-ion interactions. The generalized gradient approximation (GGA) functional of Perdew, Burke, and Ernzerhof (PBE) [33] was used for the electronic exchange and correlation energies. Van der Waals interactions were included by using Grimme's DFT-D2 approach [34]. A cutoff energy for the plane wave basis was set to 400 eV. A supercell of $5\ \times\ 5\ \times\ 1$ of h-YN containing 50 atoms (Y = 25 and N = 25) was constructed. A vacuum space of $20\ \mathring{\text{A}}$ along the z direction was added to eradicate spurious interaction between adjoining images of the layers. The sampling of the Brillouin zone (BZ) using the Monkhorst-Pack scheme [35] was employed with $5\ \times\ 5\ \times\ 1$ k-points for geometry relaxation and $7\ \times\ 7\ \times\ 1$ k-points for estimation density of states (DOS). The structures were fully optimized until the Hellmann-Feynman force acting on each atom was less than $0.01\ \text{eV}/\mathring{\text{A}}$. The energy of convergence tolerance was set to be $1\ \times\ 10^{-7}$ eV. The adsorption energies ($\text{E}_{\text{ads}}$) were calculated by using the following relations:

$$
\text{E}_{\text{ads}}\ (\text{SCG}) = \text{E}\ (\text{SCG@h-YN}) - \text{E}\ (\text{h-YN}) - \text{E}\ (\text{SCG}) \tag{1}
$$

$$
\text{E}_{\text{ads}}\ (\text{O}_{2}) = \text{E}\ (\text{O}_{2}\text{-h-YN}) - \text{E}\ (\text{h-YN}) - \text{E}\ (\text{O}_{2}) \tag{2}
$$

$$
\text{E}_{\text{ads}}\ (\text{SCG@O}_{2}) = \text{E}\ (\text{SCG@O}_{2}\text{-h-YN} + \text{SCG}) - \text{E}\ (\text{O}_{2}\text{-h-YN}) - \text{E}\ (\text{SCG}) \tag{3}
$$

where E(SCG@h-YN) and E(SCGO$_2$-h-YN) represent the total energies of SCG adsorbed on pristine and h-YN in the presence of $\text{O}_{2}$, respectively. E(h-YN) and E($\text{O}_{2}$-h-YN) represent the total energies of pristine and h-YN loaded with $\text{O}_{2}$, respectively. E(SCG) and E($\text{O}_{2}$) represent the total energies of SCG and $\text{O}_{2}$, respectively.

## 3. Results and discussion

We first describe the structural properties of h-YN. The top and side views of the optimized structures of h-YN are shown in Fig. 1(a). The calculated lattice constant, Y—N bond length, and N—Y—N bond angle of h-YN are $3.767\ \mathring{\text{A}}$, $2.175\ \mathring{\text{A}}$, and $120^\circ$, respectively, in relatively good agreement with previous theoretical results [29].

To get insights into the electronic properties of pristine h-YN, we have calculated the band structure and density of states (DOS). The band structure, shown in Fig. 2(a), indicates the semiconducting character with the indirect gap of 0.722 eV where the valence band maximum (VBM) and the conduction band minimum (CBM) are located at K and $\Gamma$, respectively. This gap is smaller than the reported values at the GGA + U level (1.144 eV) and the HSE06 level (2.322 eV) due to the self-interaction underestimation inherent in the GGA-PBE method.

![](./images/812567865889652736_4.jpg)

Fig. 1. Optimized structures (top and side views) of (a) h-YN, (b) $\text{H}_{2}\text{S@h-YN}$, and (c) $\text{SO}_{2}@\text{h-YN}$. Blue, cyan, yellow, pink, and red balls represent Y, N, S, H, and O atoms, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Despite the difference in the energy gap, the calculated band structure possesses the similar feature to that obtained by the HSE06 level [29]. Furthermore, the orbitally projected DOS (PDOS) depicted in Fig. 2(b) reveals that the VBM is primarily composed of the overlap between Y (p) and N (p) orbitals. Meanwhile, the CBM is predominantly contributed by Y (d). This finding is consistent with the previous study [29].

Next, we investigated the exposure of SCG on pristine h-YN by considering four different adsorption sites, including, Y-top, N-top, bridge (Y—N), hollow (Y—N) and various orientations of the SCG molecules at each site were taken into account. Our findings reveal the relatively high adsorption energies ($\text{E}_{\text{ads}}$) of $-3.24$ eV and $-4.21$ eV for $\text{H}_{2}\text{S}$ and $\text{SO}_{2}$, respectively, characterizing the immense chemisorption. The lowest energy configurations of SCGs adsorbed on h-YN are depicted in Fig. 1(b, c). Upon adsorption of $\text{H}_{2}\text{S}$, one of the H—S bonds dissociatively breaks and the released H atom now binds to the nearby N atom of h-YN with a bond length of $1.048\ \mathring{\text{A}}$. Meanwhile, the HS radical remains adsorbed at the hollow site with a distance of $2.912\ \mathring{\text{A}}$ above the surface. As implied by the prominent adsorption energy, the exposure of $\text{H}_{2}\text{S}$ causes notable changes in the band structure of host h-YN, as shown in Fig. 3(a). Although, the band structure of $\text{H}_{2}\text{S}$-adsorbed h-YN preserves the indirect gap feature, the gap gets enlarged to 0.862 eV, which accounts for 19.4% larger than that of pristine h-YN. Furthermore, Fig. 3(b) shows the PDOS of $\text{H}_{2}\text{S}$-adsorbed h-YN where H1 and H2 define the dissociated H atom and the bound H atom as HS. We found that there is a strong overlap between N (p) and H1 (p) at around $-0.5$ eV and between Y (d), N (p), and $\text{H}_{2}\text{S}$ (p) at around $-1.0$ and $-2.0$ eV. In particular, there is the overlap peak between N (p) and H1 (p) at around $-0.5$ eV in PDOS of Fig. 3(b). This is because the dissociated H1 atom of the molecule forms the H-N bond with the nearby N atom of h-YN by receiving partial charges from the unfilled 2p orbitals of N to the H-s orbitals. The charge transfer is also supported by the charge density difference presented below.

In case of $\text{SO}_{2}$ adsorption, the $\text{SO}_{2}$ molecule chemisorps on h-YN, resulting in the elongation of the S—O bond lengths to $1.545\ \mathring{\text{A}}$ and $1.547\ \mathring{\text{A}}$ and the reduction of O—S—O bond angle to $108^\circ$. The S atom of $\text{SO}_{2}$ binds to N atom of h-YN at a distance of $1.643\ \mathring{\text{A}}$ and O atoms bind to the nearby Y atoms at a distance of $3.134\ \mathring{\text{A}}$ as shown in Fig. 1(c). Like $\text{H}_{2}\text{S}$ adsorption, there is a major alteration in electronic behavior of h-YN upon the adsorption of $\text{SO}_{2}$. As illustrated in Fig. 4(a), the band gap of h-YN adsorbed with $\text{SO}_{2}$ changes to 0.976 eV, which is 35.2%

![](./images/812567865889652736_5.jpg)

Fig. 2. (a) Band structure and (b) Projected density of states (DOS) of h-YN.

higher than that of pristine h-YN. A strong overlap between Y (d), N (p), and $SO_2$ (p) at $-1.5$ eV verifies a strong h-YN-$SO_2$ binding as shown in Fig. 4(b). Furthermore, there is the increment of the total DOS intensity at $-1.0$ eV.

The gas sensing mechanism of 2D materials is generally described by the charge transfer between the target gas species and the sensing materials [13,28]. This mechanism is facilitated by the difference in the electronegativities among them. The atom with a high electronegativity typically tends to attract electrons towards itself and vice versa. Here, the electronegativities of Y, N, H, O, and S are 1.22, 3.04, 2.20, 3.44 and 2.58, respectively [36]. The overall electronegativities of gas mo- lecules are greater than the h-YN sheets. As a result, the immense gas-h-YN interactions are ascribed to electron transfer from the h-YN sheets to the gas molecules as manifested by the graphical plots of charge density difference as shown in Fig. 5. Thus, the presence of SCG conclusively leads to p-type doping to h-YN that consequently changes the conductivity after the gas exposure.

The strong adsorption energies of $H_2S$ and $SO_2$ on pristine h-YN indicate that the material is improper for practical gas sensing applications. However, it can be used for non-reversible scavenging applications. In order to study the adsorption performance under a practical working condition, we have studied the adsorption response of h-YN towards SCG in the presence of environmental oxygen impurities. We therefore introduced the $O_2$ molecule over h-YN by considering different binding sites and orientations (i.e., parallel and perpendicular arrangements of the $O_2$ molecule). Under the lowest energy config- uration as illustrated in Fig. 6(a), the $O_2$ molecule dissociates into O atoms, which are then bonded to the nearby N atoms of h-YN at a distance of $1.618$ Å each. The adsorption energy is found to be $-6.15$ eV, indicating that h-YN is very sensitive to $O_2$. There is a sig- nificant variation in the electronic properties of h-YN upon $O_2$ ex- posure. It can be seen from Fig. 7(a) that h-YN in the presence of $O_2$ ($O_2$-h-YN) preserves a semiconducting character with an indirect band gap of $0.960$ eV, which is 33.0% greater than the pristine h-YN. Fur- thermore, the peak of PDOS in Fig. 7(b) emerges at around $-0.75$ eV, which is originated from a strong overlap between N (p) and $O_2$ (p) to render the strong h-YN-$O_2$ binding. After obtaining the $O_2$-h-YN, we investigated the exposure of SCG in the similar way as that of pristine h-

![](./images/812567865889652736_6.jpg)

Fig. 3. (a) Band structure and (b) projected density of states (PDOS) of $H_2S@$h-YN. Here, H1 and H2 represent the H atom from $H_2S$ that binds to an N atom in h-YN and the other H atom that remains bound to S atom, respectively.

![](./images/812567865889652736_7.jpg)

Fig. 4. (a) Band structure and (b) Projected density of states (DOS) of SO₂@h-YN.

YN in the absence of O₂. The lowest energy configuration of O₂-h-YN after H₂S exposure is shown in Fig. 6(b). We found that the adsorption energy is decreased to $-2.46$ eV, which is significantly smaller than that on the pristine h-YN. However, the H₂S adsorption mechanism on O₂-h-YN remains similar to its adsorption on pristine monolayer, which is the dissociation of H₂S into H and HS fragments, where H binds to the N atom with a bond length of 1.052 Å, while HS stays over the hollow site at a distance of 2.869 Å. Considering the electronic behavior of H₂S adsorbed on O₂-h-YN, the band structure and PDOS reveal that O₂-h-YN adsorbed by H₂S exhibits a semiconducting behavior with an indirect band gap of 0.976 eV, as seen in Fig. 8(a). Like the H₂S adsorption on the pristine h-YN, Fig. 8(b) shows the overlap between the states from O₂-h-YN and H₂S are observed from $-0.5$ to $-1.0$ eV, which validates strong binding mechanism of O₂-h-YN-H₂S.

In case of SO₂ adsorption, the SO₂ molecule binds to the O₂-h-YN by adopting a vertical orientation where the O atoms bind to the nearby Y atoms at distances of 2.334 Å and 2.371 Å, as given in Fig. 6(c). The S-O bond lengths elongate to 1.519 Å and 1.526 Å, whereas the O-S-O bond angle decreases to 113°. Like H₂S adsorption, the adsorption energy for SO₂ is significantly reduced to $-1.75$ eV. The band structure, shown in Fig. 9(a), reveals that O₂-h-YN adsorbed by SO₂ is a semiconductor with an increasing indirect band gap of 1.032 eV. The O₂-h-YN-SO₂ binding mechanism can be seen by the overlap between Y (p) and O (p) of SO₂ at the VBM in PDOS in Fig. 9(b). Furthermore, the electronic states of the two spin components of O₂-h-YN loaded with SO₂ are distributed unsymmetrically near the VBM, indicating a magnetic character. The magnetic moments mainly come from the SO₂ molecule and the calculated magnetic moments are 0.281 and 0.303 μB for S and O atoms, respectively.

Moreover, Fig. 10 shows the charge density difference of the SCG adsorption on O₂-h-YN. Like the SCG adsorption on pristine h-YN, the charge gets transferred from SCG to O₂-h-YN as evident by the electron accumulation on the sheet surface. This leads to the notable modification in the electrical conductivity of O₂-h-YN upon SCG exposure because of the enhanced electron concentration. Additionally, a significant decrease in adsorption energies of SCG on O₂-h-YN is attributed to the relatively less amount of charge transfer between SCG and O₂-h-YN as compared with the pristine monolayer. This is further supported by the quantitative analysis of Bader charge. As mentioned above that the charge transfer mechanism alters the conductivity (resistivity) of SCG adsorbed h-YN and O₂-h-YN systems. This can fundamentally give rise to the variation in work function ($\Phi$) of h-YN and O₂-h-YN. Therefore, we have calculated $\Phi$ of h-YN and O₂-h-YN systems with and without SCG molecules by the following relation

$$
\Phi = \mathrm{V}_{\infty} - \mathrm{E}_\mathrm{f}
$$

Here, $\Phi$, $\mathrm{V}_{\infty}$ and $\mathrm{E}_\mathrm{f}$ are work function, potential level at infinity (far off point from the surface) and Fermi level, respectively. The calculated values of $\Phi$ are given in Fig. 11. Apparently, the exposure of SCG molecules over h-YN and O₂-h-YN systems lifts their work functions.

From what has been discussed above, the presence of O₂ in h-YN plays an important role not only in employing practical conditions for gas adsorption but also in reducing the extremely strong adsorption energies of SCG (H₂S and SO₂). However, the dissociative adsorption mechanism and high adsorption energy of H₂S on O₂-h-YN is not suitable for reversible adsorption-desorption of H₂S. While considering SO₂ exposure, the molecular adsorption of SO₂ on O₂-h-YN indicates that it is possible to use O₂-h-YN as an effective and reversible sensor

![](./images/812567865889652736_8.jpg)

Fig. 5. Charge density difference (top and side views) of (a) H₂S@h-YN and (b) SO₂@ h-YN. Yellow and cyan isosurfaces with the value of 0.002 e/Å³ represent the accumulation (+) and depletion (-) of electrons, respectively. The charge density difference is calculated by $\rho$ (SCG@h-YN) $-\rho$ (h-YN) $-\rho$ (SCG), where $\rho$ is charge density. The dashed line marks the average atomic coordinates of h-YN along the z-direction.

![](./images/812567865889652736_9.jpg)

Fig. 6. Optimized structures (top and side views) of (a) O₂-h-YN, (b) H₂S@O₂-h-YN, and (c) SO₂@O₂-h-YN. Blue, cyan, yellow, pink, and red balls represent Y, N, S, H, and O atoms, respectively.

![](./images/812567865889652736_10.jpg)

Fig. 7. (a) Band structure and (b) Projected density of states (PDOS) of O₂-h-YN.

![](./images/812567865889652736_11.jpg)

Fig. 8. (a) Band structure and (b) Projected density of states (PDOS) of H₂S@O₂-h-YN.

![](./images/812567865889652736_12.jpg)

Fig. 9. (a) Band structure and (b) Projected density of states (PDOS) of SO₂@O₂-h-YN.

![](./images/812567865889652736_13.jpg)

Fig. 10. Charge density difference (top and side views) of (a) H₂S@O₂-h-YN and (b) SO₂@O₂-h-YN. Yellow and cyan isosurfaces with the value of 0.002 e/Å³ represent the accumulation (+) and depletion (-) of electrons, respectively. The dashed line marks the average atomic coordinates of h-YN along the z-direction.

![](./images/812567865889652736_14.jpg)

Fig. 11. Work functions of the different systems considered in this study.

[37].

## 4. Conclusions

Spin-polarized, van der Waals corrected first-principles based on DFT calculations were carried out to investigate the scavenging personalities of h-YN towards SCG like H₂S and SO₂ in its pristine form and in the presence of environmental oxygen impurities. Our calculations reveal that H₂S molecule dissociates and binds with h-YN, while SO₂ does not dissociate. The adsorption energies of both gases on the pristine monolayer of h-YN are chemically strong. In case of the presence of O₂ in h-YN, the adsorption energies of H₂S and SO₂ on O₂-h-YN are tremendously declined as compared to their values on pristine h-YN. However, H₂S binds with O₂-h-YN in a dissociative manner and the adsorption energy is still high; thus, h-YN is conclusively unsuitable for H₂S storage/removal. Moreover, there are major alterations in electronic properties of h-YN after the exposure of SCG. In the case of SO₂ adsorption, significant changes of electronic properties in terms of energy gap and charge transfer result in the change of conductivity of O₂-h-YN, which indicates a suitable material for SO₂ scavenging. Especially, molecular adsorption with the appropriate adsorption energy of SO₂ would support the possible of h-YN for use as effective scavenging materials for SO₂ in O₂ rich environment.

for SO₂. It should be noted that the adsorption process under practical conditions involves the competitive adsorption of various types of adsorbates, which requires in-depth investigations of numerous factors including the gas concentration, the diffusion rates of individual gases and thermodynamics [37,38]. However, our work provides the fundamental roles of the adsorption of individual SO₂ and H₂S gases essential for subsequently analyzing the adsorption in the practical environment

# CRediT authorship contribution statement
Apinya Ngoipala: Writing - original draft. Thanayut Kaewmaraya: Writing - original draft, Supervision. Tanveer Hussain: Conceptualization, Data curation, Writing - original draft, Writing - review & editing, Supervision. Amir Karton: Writing - review & editing, Supervision.

# Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# Acknowledgements
TK acknowledges the Development and Promotion of Science and Technology Talent Project (DPST) for the financial support of this project (005/2559). The Nano-technology Centre (NANOTEC), NSTDA Ministry of Science and Technology (Thailand) also supports TK through its program of Centre of Excellence Network, Integrated Nano-technology Research Centre Khon Kaen University (Thai-land). TH and AK are indebted to the resources at NCI National Facility at the Australian National University supported by the Australian Government and computational resources provided by the Pawsey Supercomputing Centre with funding from the Australian Government and the Government of Western Australia. A.K. acknowledges an Australian Research Council (ARC) Future Fellowship (FT170100373).

# References
[1] P. Tyagi, et al., Efficient detection of $\text{SO}_2$ gas using $\text{SnO}_2$ based sensor loaded with metal oxide catalysts, Procedia Eng. 87 (2014) 1075–1078.

[2] Z. Klimont, S.J. Smith, J. Cofala, The last decade of global anthropogenic sulfur dioxide: 2000-2011 emissions, Environ. Res. Lett. 8 (1) (2013) 014003.

[3] J. Sarfraz, et al., A printed $\text{H}_2\text{S}$ sensor with electro-optical response, Sens. Actuators, B 191 (2014) 821–827.

[4] C. Liewhiran, et al., The Monitoring of $\text{H}_2\text{S}$ and $\text{SO}_2$ noxious gases from industrial environment with sensors based on flame-spray-made $\text{SnO}_2$ nanoparticles, Eng. J. 16 (3) (2012) 123–134.

[5] N.S. Ramgir, et al., Room temperature $\text{H}_2\text{S}$ sensor based on Au modified ZnO nanowires, Sens. Actuators, B 186 (2013) 718–726.

[6] P. Tyagi, et al., Metal oxide catalyst assisted $\text{SnO}_2$ thin film based $\text{SO}_2$ gas sensor, Sens. Actuators, B 224 (2016) 282–289.

[7] R.J. Sappok, P.L. Walker, Removal of SO2 from flue gases using carbon at elevated temperatures, J. Air Pollut. Control Assoc. 19 (11) (1969) 856–861.

[8] L. Shi, et al., Characterization and mechanisms of H2S and SO2 adsorption by activated carbon, Energy Fuels 29 (10) (2015) 6678–6685.

[9] Z. Mahdavifar, Z. Nomresaz, E. Shakerzadeh, Hetero-fullerenes C59M (M = B, Al, Ga, Ge, N, P, As) for sulfur dioxide gas sensing: computational approach, Chem. Phys. 530 (2020) 110606.

[10] Y. Huang, et al., Removal of typical industrial gaseous pollutants: from carbon, zeolite, and metal-organic frameworks to molecularly imprinted adsorbents, Aerosol Air Qual. Res. 19 (9) (2019) 2130–2150.

[11] M. Ozekmekci, G. Salkic, M.F. Fellah, Use of zeolites for the removal of H2S: A minireview, Fuel Process. Technol. 139 (2015) 49–60.

[12] E. Martínez-Ahumada, et al., MOF materials for the capture of highly toxic H2S and SO2, Organometallics 39 (7) (2020) 883–915.

[13] S. Yang, C. Jiang, S.-H. Wei, Gas sensing in 2D materials, Appl. Phys. Rev. 4 (2) (2017) 021304.

[14] Rao, C.N.R.A.W., U V, 2019 Inorganic Materials beyond Graphene. 2D Inorganic Materials beyond Graphene.

[15] T. Wang, et al., A review on graphene-based gas/vapor sensors with unique properties and potential applications, Nano-Micro Lett. 8 (2) (2016) 95–119.

[16] H. Qian, et al., H2S and SO2 adsorption on Pt-MoS2 adsorbent for partial discharge elimination: A DFT study, Results Phys. 12 (2019) 107–112.

[17] L. Kou, T. Frauenheim, C. Chen, Phosphorene as a superior gas sensor: selective adsorption and distinct I-V response, J. Phys. Chem. Lett. 5 (15) (2014) 2675–2681.

[18] T. Kaewmaraya, et al., Novel green phosphorene as a superior chemical gas sensing material, J. Hazard. Mater. 401 (2021) 123340.

[19] T. Hussain, M. Hankel, D.J. Searles, Improving sensing of sulfur-containing gas molecules with ZnO monolayers by implanting dopants and defects, J. Phys. Chem. C 121 (44) (2017) 24365–24375.

[20] T. Hussain, et al., Defected and functionalized germanene-based nanosensors under sulfur comprising gas exposure, ACS Sens. 3 (4) (2018) 867–874.

[21] N. Zhang, et al., Room-temperature high-sensitivity $\text{H}_2\text{S}$ gas sensor based on dendritic ZnO nanostructures with macroscale in appearance, J. Appl. Phys. 103 (10) (2008) 104305.

[22] Q. Yang, et al., First-principles study of sulfur dioxide sensor based on phosphorenes, IEEE Electron Device Lett. 37 (5) (2016) 660–662.

[23] X.-P. Chen, et al., Sulfur dioxide and nitrogen dioxide gas sensor based on arsenene: a first-principle study, IEEE Electron. Device Lett. 38 (5) (2017) 661–664.

[24] T. Kaewmaraya, et al., Drastic improvement in gas-sensing characteristics of phosphorene nanosheets under vacancy defects and elemental functionalization, J. Phys. Chem. C 122 (35) (2018) 20186–20193.

[25] H. Vovusha, et al., Sensitivity enhancement of stanene towards toxic $\text{SO}_2$ and $\text{H}_2\text{S}$, Appl. Surf. Sci. 495 (2019) 143622.

[26] T. Liu, et al., A first-principles study of gas molecule adsorption on borophene, AIP Adv. 7 (12) (2017) 125007.

[27] H. Cui, X. Zhang, D. Chen, Borophene: A promising adsorbent material with strong ability and capacity for $\text{SO}_2$ adsorption, Appl. Phys. A 124 (9) (2018) 636.

[28] B. Chakraborty, Chapter 5 – Electronic structure and theoretical aspects on sensing application of 2D materials, in: M. Hywel, C.S. Rout, D.J. Late (Eds.), Fundamentals and Sensing Applications of 2D Materials, Woodhead Publishing, 2019, pp. 145–203.

[29] K. Zheng, et al., Intriguing electronic insensitivity and high carrier mobility in monolayer hexagonal YN, J. Mater. Chem. C 6 (18) (2018) 4943–4951.

[30] G. Kresse, J. Hafner, Ab initio molecular-dynamics simulation of the liquid-metal-amorphous-semiconductor transition in germanium, Phys. Rev. B 49 (20) (1994) 14251.

[31] J. Hafner, Ab-initio simulations of materials using VASP: Density-functional theory and beyond, J. Comput. Chem. 29 (13) (2008) 2044–2078.

[32] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (24) (1994) 17953.

[33] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (18) (1996) 3865.

[34] S. Grimme, Semiempirical GGA-type density functional constructed with a long-range dispersion correction, J. Comput. Chem. 27 (15) (2006) 1787–1799.

[35] H.J. Monkhorst, J.D. Pack, Special points for brillouin-zone integrations, Phys. Rev. B 13 (12) (1976) 5188.

[36] J. Emsley, The Elements, Clarendon Press; Oxford University Press, Oxford, New York, 1998.

[37] V.M. Gun'ko, Competitive adsorption, Theor. Exp. Chem. 43 (3) (2007) 139–183.

[38] A. Tvardovski, D. Tondeur, E. Favre, Description of multicomponent adsorption and absorption phenomena from a single viewpoint, J. Colloid Interface Sci. 265 (2) (2003) 239–244.