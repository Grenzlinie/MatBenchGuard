# Revealing the Local Microstates of Fe-Mn-Al Medium Entropy Alloy:
## A Comprehensive First-principles Study

Ying Zhang $^{1}$ . William Yi Wang $^{1}$ . Chengxiong Zou $^{1}$ . Rui Bai $^{2}$ . Yidong Wu $^{2}$ . Deye lin $^{3}$ . Jun Wang $^{1}$ . Xidong Hui $^{2}$ .\ Xiubing Liang $^{1,4}$ . Jinshan $Li^{1}$

Received: 11 March 2021 / Revised: 6 April 2021 / Accepted: 3 May 2021
© The Chinese Society for Metals (CSM) and Springer-Verlag GmbH Germany, part of Springer Nature 2021

### Abstract
Entropy-stabilized multi-component alloys have been considered to be prospective structural materials attributing to their impressive mechanical and functional properties. The local chemical complexions, microstates and configurational transformations are essential to reveal the structure–property relationship, thus, to promote the development of advanced multi-component alloys. In the present work, effects of local lattice distortion (LLD) and microstates of various configurations on the equilibrium volume $(V_{0})$ , total energy, Fermi energy, magnetic moment $(\mu_{Mag})$ and electron work function $(\Phi)$ and bonding structures of the Fe–Mn–Al medium entropy alloy (MEA) have been investigated comprehensively by first-principles calculations. It is found that the $\Phi$ and $\mu_{Mag}$ of those MEA are proportional to the $V_{0}$ , which is dominated by lattice distortion. In terms of bonding charge density, both the strengthened clusters or the so-called short-range order structures and the weakly bonded spots or weak spots are characterized. While the presence of weakly bonded Al atoms implies a large LLD/mismatch, the Fe–Mn bonding pairs result in the formation of strengthened clusters, which dominate the local microstates and the configurational transitions. The variations of $\mu_{Mag}$ are associated with the enhancement of the nearest neighbor magnetic Fe and Mn atoms, attributing to the LLD caused by Al atoms, the local changes in the electronic structures. This work provides an atomic and electronic insight into the microstate-dominated solid-solution strengthening mechanism of Fe–Mn–Al MEA.

Keywords Medium entropy alloy · Bonding charge density · Magnetic moment · Microstates

Available online at http://link.springer.com/journal/40195.

⊗ William Yi Wang
wywang@nwpu.edu.cn

⊗ Xiubing Liang
liangxb_d@163.com

⊗ Jinshan Li
ljsh@nwpu.edu.cn

1 State Key Laboratory of Solidification Processing, Northwestern Polytechnical University, Xi’an 710072, China
2 State Key Laboratory for Advanced Metals and Materials, University of Science and Technology Beijing, Beijing 100083, China
3 CAEP Software Center for High Performance Numerical Simulation, Beijing 100088, China
4 Defense Innovation Institute, Academy of Military Sciences of the PLA of China, Beijing 100071, China

## 1 Introduction
Entropy-stabilized multi-component alloys comprised of various alloying systems for extensive composition range have been widely addressed in the structural metals research community [1–4]. Meanwhile, medium entropy alloys (MEAs) for ternary systems and high entropy alloys (HEAs) for quaternary or more systems, exhibit outstanding superior mechanical properties than traditional alloys, which is mainly affected by serious cocktail effect and lattice distortion [5]. Recently, the complex interactions and lattice distortions on electronic/atomic scale in HEAs and MEAs are under extensive experimental and theoretical studies [6–9]. As the consequence of a high degree of configurational disorder, complex chemical fluctuations could cause an abundance of microstates/configurations in multi-component alloys [10, 11]. Therefore, a comprehensive study of local chemical complexions, microstates and configurational transformations would provide a fundamental understanding of the structure–property relationship, which is essential

![](./images/812019289535021057_1.jpg)

Published online: 16 July 2021

![](./images/812019289535021057_2.jpg)

to develop the new strategies of designing advanced multi-component alloys.

The promising performance of HEAs and MEAs has attracted worldwide attention to identifying relationships between the extraordinary mechanical properties and the atomic-scale mechanisms. Attributing to the mix of neighboring atoms with different atomic sizes, the constituent atoms in MEAs and HEAs will yield an local lattice distortion (LLD) and an intrinsic elastic residual stress field [12]. Serious lattice distortion is one of the four core effects in multi-component alloys and has a profound influence on the alloy properties [13-16]. Compared with the CoCrFeNi HEA, the improved strength of CoCrFeNiPd could be dominated by the significant lattice misfit volume caused by Pd and the effects of the non-random composition fluctuations [17]. For both single-phase NbTaTiV and NbTaTiVZr BCC HEAs, their high strength is attributed to the lattice mismatch rather than modulus mismatch [6]. Through employing multiple tilting selected area electron diffraction (SAED) experiments, lattice distortion in the HEA could be directly observed in $\mathrm{Fe}_{33} \mathrm{Mn}_{13} \mathrm{Co}_{22} \mathrm{Cr}_{15} \mathrm{Ni}_{17}$ HEA [9]. Therefore, the effect of lattice distortion associated with the atomic size difference has been proposed to estimate the solid-solution strengthening mechanism [6, 8, 18-21].

Understandings of the local structural information are primary to study the thermodynamic, kinetic and mechanical properties (i.e., serrations) of the MEAs. The prominent synthesis properties of multi-composition alloys have been long associated with diverse microstructures induced by configurational transformation, which results in chemical composition complexity [15, 22]. In order to reveal the foundations of the configurational transformation and their contributions to mechanical properties, the structure-property relationship has been proposed based on the atomic long-range periodic interactions [11, 23]. It is known that configurational transformation represents transitions between various microstates corresponding to atom rearrangements [24]. Moreover, the local atomic arrangement dominated deformation has been widely observed [23-25]. For instance, a random atomic distribution would be decomposed into unique site-to-site lattice distortions and local chemical ordered structures of certain compositions at a lower temperature or after the annealing procedure [26, 27]. Motivated by atomic-scale fluctuations in composition and configuration, deformation behavior could be affected through the "glide plane softening" mechanism [23-25, 28]. The subsistent microstates enhance the activation energy barrier for dislocation-mediated plasticity [25], which will improve the work hardening and the strain-rate sensitivity [29]. For the glide resistance ability of lattice distortion and chemical short-range order, the strength of CoCrNi MEAs is determined by them [30]. The existence of disordered structures and the interaction between the local microstates and ordered lattices are the fundamental reasons for the diversity of mechanical properties. Referring to the chemical and structural complexity, it is extremely important to investigate the local fluctuations of chemistry and the topology. Therefore, the development of MEAs is primarily aimed to reveal both electronic concentrations and lattice distortions, which are critical for the development of advanced alloy design.

Additionally, the atomic-scale fluctuations of the chemical environment are expected to play important roles in magnetic behavior [31-33]. The appearance of the different magnetic properties in the BCC phases should be the consequence of the variation in composition and temperature [34]. For instance, the magnetic states of Fe and Fe alloys are critical to describing their phase stability. With increasing temperature, Fe will experience phase transformations as the unit cell volume expands, from ferromagnetic BCC state to paramagnetic FCC state at higher temperatures > 1043 K [13, 34]. The chemical disorder-induced magnetism property makes the situation in Fe-Al system even more complicated, as to become a promising candidate for magnetically patterned media [33, 35]. With the existence of chemical disorder, ferromagnetism could be activated, which is related to the rising nearest-neighbor magnetic atoms and local deformation in the electronic structure. Moreover, with increasing Al composition in Fe-Al, the contest between the first nearest-neighbor Fe-Fe ferromagnetic exchange and the second nearest-neighbor Fe-Al-Fe antiferromagnetic super-exchange, ferromagnetic order disappears [36]. Those variations in local electronic structures and chemical bonding caused by solute and microstate possess the extreme complexity of magnetism. So, it is essential to investigate the local order microstate, thus, to derive better properties of the materials.

In this work, in order to investigate the influence of configurational transformation on mechanical properties of Fe-Mn-Al MEA, the electrical properties and the electron work function ($\Phi$) are combined to characterize the connection between the local microstate and the material strength [37]. In addition, $\Phi$ related yield strength model has already been utilized quantitatively to present the contributions of solid-solution strengthening [37, 38]. Together with the criteria of $\Phi$, the coupling effect of valence electron concentration behavior and lattice distortion on solid-solution strengthening could be investigated comprehensively by first-principles calculations. The local atomic arrangements of the BCC Fe-28Mn-18.5Al (wt%) MEA are revealed by a similar atomic environment (SAE) approach. The electronic basis of the characterization of chemical complexity provides an insight into the influence of the microstate and LLD on the traditional solid-solution strengthening effect and magnetic properties. These results provide an atomic and electronic insight into the microstate-dominated solid-solution strengthening and weakening mechanisms.

![](./images/812019289535021057_3.jpg)

The observed generality of the atomic clusters can provide physical guidance on control the strength and ductility in the development of the advanced high-performance Fe-based MEA.

## 2 Methodology

### 2.1 Multi-Component Supercell Construction Via SAE

In this work, the SAE method [39] has been employed to construct a supercell model for the random alloy by setting the local atomic environments of all the lattice sites similar to each other [23, 40]. The atomic environment of a specific atom could be disassembled into series atom clusters constructed by the atom with its neighboring atoms [41]. For BCC Fe-28Mn-18.5Al (wt%) MEA, its space group number is 229 with the lattice parameters of $a=b=c=2.86$ Å, which are utilized to construct the supercell through enlarging the unit cell by $3×3×6$. By using SAE, the represented configurations simulating the solid-solution alloy are transferred to a minimization issue in the configuration space with the objective function. After 2000 Monte Carlo samplings over the atomic configurational space, 10 best candidate configurations of Fe-28Mn-18.5Al MEA were firstly addressed from the original 2000 ones, the first five of which with the lowest total energy were utilized for further investigations. The objective function describes the disordered situation of the supercell/configuration, which is expressed as [42]:

$$
g\left(A_{\mathrm{m}}, \sigma\right) \equiv \sqrt{\frac{1}{N\left(A_{\mathrm{m}}^{\sigma}\right)} \sum_{\tilde{A_{\mathrm{m}}^{\sigma}}} \tilde{f}^{2}\left(A_{\mathrm{m}}^{\sigma}\right)},
\tag{1}
$$

where $N(A_{\mathrm{m}}^{\sigma})$ denotes the number of classes of configurationally equivalent clusters in the type of $A_{\mathrm{m}}^{\sigma}$. Afterward, the space groups and the symmetry of those investigated supercells will be double-checked before the first-principles calculations.

### 2.2 First-Principles Calculations

All calculations in the present work, the generalized gradient approximation (GGA) [43] is employed for the exchange-correction functional and the projector augmented wave (PAW) [44] is utilized for the electron–ion interaction as implemented in Vienna Ab-initio Simulation Package (VASP) [45, 46]. The wave functions for the random Fe–Mn–Al configurations are sampled on $\Gamma$-centered $5×5×3$ mesh. The plane wave cutoff energy is set as 1.4 times the default cutoff energy (ENCUT$=400$ eV) for high accuracy calculations [47], and the energy convergence criterion of electronic self-consistency is $10^{-6}$ eV/atom.

The structures are fully relaxed by the Methfessel–Paxton technique [48], while the final total energy calculations are performed by the tetrahedron method incorporating Blöchl correction [49]. Bond structures are characterized by bonding electron density ($\Delta\rho$) [23, 50–52], revealing the complex electron environment induced by the variation of the lattice mismatch/distortion. It is calculated through the charge density difference between the fully relaxed structure of self-consistent calculations and the same structure of non-self-consistent calculations [23, 51, 52]. The isosurface structures with different values of $\Delta\rho$ are generated using the visualization for electronic and structure analysis (VESTA) software[53].

The electron work functions of 5 best structures are calculated by the Halas–Durakiewicz model as follows[54]:

$$
\phi=6.15 \alpha\left(\frac{r_{\mathrm{s}}}{a_{0}}\right)^{-1 / 2},
\tag{2}
$$

where $\alpha$ is an empirical parameter being either unity for most metals or 0.86 for alkali metals, $r_{\mathrm{s}}=1.3882(M / Z \rho)^{1 / 3}$ the effective radius of the electronic volume and $a_{0}$ the Bohr radius. The electron work function is calculated by the free-electron gas model from bulk properties, including the density—$\rho$, the valence—$Z$ and the atomic mass—$M$.

## 3 Results and Discussion

As shown in Fig. 1(a), the initial 10 candidate configurations are addressed after 2000 structural evolutions, illustrating these screened supercell structures for BCC Fe–Mn–Al MEA. The Al-cluster is highlighted by its relatively larger size. Herein, the random configurations of BCC Fe–Mn–Al MEA have been studied by using the SAE method of alloying elements in chemical disorder, and the local cluster behavior in the proposed structure has been elucidated. Figure 1(b) displays the primary topological structures of Al elements in diverse phase structures. It is worth mentioning that the distribution of Fe and Al atoms in the crystal lattice of FeAl (B2), $\mathrm{Fe}_{3} \mathrm{Al}\left(\mathrm{D} 0_{3}\right)$ and other phases has been studied by the X-ray diffraction method [55–57]. It is noted that there are exhibiting similar local chemical states between the Al atoms in these initial 10 random configurations and the diverse phase structures, which can be estimated by the schematic bond pattern of the Al-clusters. While the topology of the emblems of the corresponding phases is presented in Fig. 1(a), the cube, tetrahedrons, pyramid and diamond type bond structures highlight the position for B2, $\mathrm{D} 0_{3}$, B32 and $\mathrm{Fe}_{13} \mathrm{Al}_{13}$ phase of Al atoms, respectively. It is indicated that the presence of a local configurational transformation in the random configurations can support the approach to efficiently distinguish the local atomic arrangement.

![](./images/812019289535021057_4.jpg)

![](./images/812019289535021057_5.jpg)

Fig. 1 Schematic structure of the SAE model in a body-center-cubic (BCC) lattice of Fe-28Mn-18.5Al (wt%) quaternary alloy. a 3D views of the configurational transitions of the Al clusters via atomic rearrangements, including ten random arrangements. b Topological structure of Fe and Al atoms in the crystal lattice of A2, B2, D0₃,B32 and Fe₁₃Al₃ phases. The various colors characterize the different kinds of alloying elements for the given equiatomic Fe-Mn-Al BCC MEA alloy, which are kept consistently in the following related figures. In particular, the Fe, Mn and Al elements are in yellow, purple and green, respectively. Meanwhile, the free energies of 10 random arrangement configurations were obtained by first-principles calculations

The equilibrium properties of the selected energetic favorable configurations are summarized in Table 1 and displayed in Fig. 2 with gradient colors determined by its quantities, including lattice constant $(a)$, equilibrium volume $(V_{0})$, total energy $(E_{0})$, Fermi energy $(E_{\text{F}})$, magnetic moment $(\mu_{\text{Mag}})$ and electron work function. Herein, the $V_{0}$ and $a$ could be considered as the important parameters characterizing the LLD behavior of solutes. The adjustment of lattice distortion or local atomic configurations has grown an intriguing maneuver in the design of advanced metallic materials [38, 58-60]. Referring to $V_{0}$, the variation tendencies of $E_{0}$, $\Phi$, $E_{\text{F}}$ and $\mu_{\text{Mag}}$ are displayed in Fig. 2. It can be seen that the magnetic moment $\mu_{\text{Mag}}$ strongly depends on the volume, while $\mu_{\text{Mag}}$ is the sum of the magnetic moment for each atom in configuration. In line with Eq. (2), there is a linear relationship between $\Phi$ and $V_{0}$, as shown in Fig. 2(b). It is confidentially suggested that $\Phi$ should be considered as a dominant feature in the predictions of strength and solid-solution hardening mechanism. Here, the $\Phi$ of all configurations is roughly estimated by the CALPHAD-type mixing (or the so-called Vegard's law) to exhibit the interactions among various solute atoms[38].

Bonding charge density $(\Delta\rho)$ [23, 50, 51] provides an insight into the relative strength and deformation behaviors

<table>
<thead>
<tr>
<th></th>
<th>$A$ (Å)</th>
<th>$V_{0}$ (Å³)</th>
<th>$E_{0}$ (eV)</th>
<th>$E_{\text{F}}$ (eV)</th>
<th>$\mu_{\text{Mag}}$ ($\mu\text{B}$/supercell)</th>
<th>$\Phi$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Best-1</td>
<td>2.87</td>
<td>1281.82</td>
<td>$-$ 827.44</td>
<td>6.76</td>
<td>160.53</td>
<td>3.421</td>
</tr>
<tr>
<td>Best-2</td>
<td>2.86</td>
<td>1263.26</td>
<td>$-$ 827.25</td>
<td>6.80</td>
<td>156.19</td>
<td>3.429</td>
</tr>
<tr>
<td>Best-3</td>
<td>2.88</td>
<td>1284.91</td>
<td>$-$ 825.28</td>
<td>6.73</td>
<td>159.04</td>
<td>3.420</td>
</tr>
<tr>
<td>Best-4</td>
<td>2.81</td>
<td>1200.69</td>
<td>$-$ 816.69</td>
<td>7.43</td>
<td>74.67</td>
<td>3.458</td>
</tr>
<tr>
<td>Best-5</td>
<td>2.86</td>
<td>1256.86</td>
<td>$-$ 815.71</td>
<td>7.83</td>
<td>88.32</td>
<td>3.432</td>
</tr>
</tbody>
</table>

Table 1 Calculated lattice constants $(a)$, equilibrium volume $(V_{0})$, total energy $(E_{0})$, Fermi energy $(E_{\text{F}})$, magnetic moment $(\mu_{\text{Mag}})$ and electron work function $(\Phi)$ of 5 selected structures of BCC Fe-Mn-Al MEA predicted by first-principles calculations

![](./images/812019289535021057_6.jpg)

![](./images/812019289535021057_7.jpg)

Fig. 2 Predicted fundamental properties of the 5 selected stable random arrangements (Best-1, Best-2, Best-3, Best-4, Best-5) for the Fe-Mn-Al MEA, illustrating the effect of configurational transition on the a total energy $E_0$, b electron work function $\Phi$, c Fermi energy $E_{\text{F}}$, d magnetic moment $\mu_{\text{Mag}}$, respectively. e A radar chart that displays the rank of the calculated data for Fe-Mn-Al MEA

of pure metals [50, 61] and metallic materials [52, 62] by exhibited clear descriptions of bonding characteristics. Figure 3 shows the different views of bonding charge density isosurfaces of the 5 selected configurations. In Fig. 3(a), the ellipses with gradient colors emphasize the physical nature of weak spots caused by the coupling effect of LLD and valence electrons are characterized by the regions with a low bonding charge density. Moreover, the isosurfaces in red identify the atomic sites absorbing electrons ($\Delta\rho>0$). It is indicated that the weak spots are the locations of the partial agglomeration of Al element, which potentially contribute to the enhanced plasticity of the alloy. Furthermore, the hybridization between Al-sp and transition metal d-states is the driving force in bonding [63]. Therefore, the Fe-Al neighbors are energetically favored, but Al-Al neighbors are avoided. It is worth mentioning that the solute atoms with a large negative entropy of mixing ($\Delta H_{\text{mix}}$) tend to construct the clusters, while the $\Delta H_{\text{mix}}$ of Fe-Al, Fe-Mn and Al-Mn is -11, 0 and -19, respectively [64].

Due to the large mechanical (LLD) and chemical (solute atoms concentration) differences caused by their atomic radius (i.e., $r_{\text{Al}}=1.43$ Å, $r_{\text{Fe}}=1.26$ Å and $r_{\text{Mn}}=1.37$ Å) and valance electrons (i.e., Al—$3s^23p^1$, Fe—$3d^64s^2$, Mn—$3d^54s^2$), Al elements keep the largest atomic radius and the smallest valence electrons, as presented in Fig. 3(a). On the one hand, many regions enriched with Al atom form weaken spots, resulting in a large LLD caused by the difference in atomic sizes. Thus, the coupling effect of LLD and chemical disorder contributes to the formation of these weak spots. On the other hand, the bonding strength of Fe-Mn will be increased and the electron redistributions are homogeneously enlarging the size/strength of the local bond, resulting in the formation of clusters. The presence of strongly bonded Fe-Mn clusters and weakly bonded Al atoms implies a serrated deformation of MEA, resulting in intermittent avalanches of defect movement.

In the view of electronic redistributions or the bonding variations, some interesting patterns caused by the extremely large LLD can be captured, as shown in Fig. 3 (b). These isosurfaces in blue display the atomic sites contributing electrons ($\Delta\rho<0$). For instance, under the coupling influence of the chemical and the mechanical contributions, the shape of $\Delta\rho$ around Fe and Mn could change petals from full to scattered. Similarly, the Al atom has a dotted pattern because of its smaller number of valence electrons. To further analyze the bond structures between solute atoms, Al atoms contribute fewer electrons and when bonds with Fe/ Mn atoms, which has not been observed in Fig. 3(a). After the relaxation, those configurations convert from standard BCC to an obvious distorted structure, as clearly captured in Fig. 3. The higher density of $\Delta\rho$ results in stronger bonding strength[23, 50, 65]. It is evident that the bonding strength between the Fe/Mn atoms in the clusters forms the strongest part and Al atoms form the weakest part of the structures. This atomic distortion caused by solutes in multi-component alloys could not only impair the influence of lattice change on mechanical properties during rising temperature [4, 66] but also pins the sliding and transformation, which possibly correlated with high strength [67].

Bonding charge density between the atoms in BCC Fe-Mn-Al ternary alloy is shown in Fig. 4 for the different views. The charge depletion and accumulations between

![](./images/812019289535021057_8.jpg)

Fig. 3 Bonding-charge-density isosurface of five selected configurations for the random solutions of the given BCC Fe-Mn-Al MEA in a 3D view, respectively. a Isosurfaces in red display the atomic sites absorbing electrons ($\Delta\rho>0$), while b the isosurfaces in blue identify the atomic sites contributing electrons ($\Delta\rho<0$). Those solid ellipses highlight the weak bond features caused by the chemical (solute atoms) and the mechanical (local lattice distortion) contributions. The red, green and blue dash ellipses highlight the different bonding features of the Fe, Al and Mn atoms, respectively. In particular, the Fe, Mn and Al elements are in yellow, purple and green, respectively. Meanwhile, the free energies of 5 stable random arrangement configurations were obtained by first-principles calculations

nearest neighboring atoms provide crucial information on the atomic interaction and their bonding states. The dash ellipses highlight the anomers feature of atoms, which agree well with Fig. 3. The bonding electron densities of Al atoms evidently lower than Fe/Mn atoms, which are consisted of the aforementioned effective microstate/cluster strength- ening effect. According to detailed knowledge of the elec- tron transform in atomic structures, the remarkable overlap between the p-band of Al and d-band of neighboring Fe/ Mn atoms indicates a strong hybridization and formation of loosely packed weak spots. The p electrons of Al atoms form the d-p bonding electrons in the nearest layer of Fe-Al and Mn-Al, and this bonding has the property of oriented bonds (covalent bonds).

Moreover, the chemical disorder and LLD in the struc- tures named Best-4 and Best-5 have caused a dramatic distribution on charge density, yielding grotesque bonds and higher free energy among other structures. Therefore, associated with configurational transitions, the formation of weak spots can be attributed to bonded Fe-Mn clusters and weakly bonded Al atoms.

In Fig. 5, it can clearly identify that the collinear spin alignments of different atoms vary with their position by the coupling effect of chemical disorder and LLD/mismatch. Those observations revealed the presence of the spin-down states of magnetic spins trend to occur around the cluster. It is understood that the local magnetic moments are domi- nated by the local microstates, which can also be affected by the size of structural models or the quantity of statistical samples [68]. With solute of random atomic distributions and local structures, their local moments significantly vary upon different structures and atomic environments. More- over, the LLD caused by solutes could result in the local anti-ferromagnetic states, which are highlighted by these red dashed ellipses in Fig. 4. It is noted that the LLD dwindles the magnetic moment of Fe/Mn atoms through bond length reduction and enhances that by bond length increase, provid- ing an insight into the volume-dependent magnetic moment,

![](./images/812019289535021057_9.jpg)

![](./images/812019289535021057_10.jpg)

Fig. 4 a Influence of solute atoms and clusters on the bond structures of five selected configurations of the BCC Fe-Mn-Al MEA are character- ized by the 3D view of counter plots of bonding charge density. The spaces in red are for $\Delta \rho>0$, while those in blue are for $\Delta \rho<0$. b The (100) and (010) view of contour plots of $\Delta \rho 0.0015 e^{-} / \AA^{3}$ intervals, generated by VESTA package. In particular, the Fe, Mn and Al elements are in yellow, purple and green, respectively

as listed in Table 1 and Fig. 2(d). Otherwise, chemical dis- order and LLD could improve the magnetic moments by increasing both the spin-up and spin-down states, the small value of which also indicates a suppressed magnetism [32].

To obtain a further understanding of the influence of LLD on fundamental properties from electronic structure, Fig. 6 presents the total density of state (DOS) of these 5 best configurations, while their partial DOS (pDOS) are displayed in Fig. 7. Since the total DOS is mainly donated by the d-orbitals of Fe/Mn atoms, it could be commonly considered that the local structure transformation can be identified through the considerable shape features of DOS curves [69]. In the present Fe-Mn-Al MEA, it might result in a bimodal d-band pDOS, while a pseudo-band gap could appear in the middle. Meanwhile, both FCC and HCP struc- tures could induce a unimodal shape of d-band. As shown in Fig. 6, the bimodality features of pDOS indicate the various configurational-transformation tendency in those selected

![](./images/812019289535021057_11.jpg)

![](./images/812019289535021057_12.jpg)

Fig. 5 Collinear spin alignments of selected stable random arrangement structures in a 3D view for BCC Fe-Mn-Al MEA. The arrows in yellow and in purple identify Fe and Mn atoms, respectively. The spin flipping caused by local lattice distortions is highlighted by the dashed ellipse in red

structures. In addition, as shown in Fig. 7, the bonding peaks are concentrated below the Fermi energy up to -5, mainly due to the interaction between the d electrons of Fe and Mn atoms. A remarkable overlap between the sp-band pDOS of Al and those of neighboring Fe/Mn atoms can be captured. Since those clusters are mainly consisted of Fe and Mn atoms, the mixed valence electrons of Fe/Mn result in the enhanced pDOS near the Fermi energy to -5 and its overlap with neighboring Fe/Mn pDOSs. These features are consistent with the aforementioned bond character discussed in Figs. 3 and 4.

## 4 Conclusion

In summary, the local atomic arrangement of disordered configurations of BCC Fe-28Mn-18.5Al (wt%) MEA is revealed by the SAE model. The effect of configurational transition in the stable random arrangements on the equilibrium volume, total energy, Fermi energy, magnetic moment, electron work function and bonding structures of the Fe-Mn-Al MEA is comprehensively studied by first-principles calculations. The variation tendencies among $\Phi$ and $\mu_{\text{Mag}}$ referring to $V_0$ are discussed. In the view of the bonding charge density, the regions enriched in Al yield the formation of weak spots, which is attributed to the biggest atomic size and fewer valence electrons of Al than that of Fe and Mn in the Fe-Mn-Al MEA, yielding a large LLD/mismatch. The variations of magnetic properties are associated with the enhancement of the nearest neighbor magnetic atoms and local changes in the electronic structures, which can also be attributed to the LLD caused by Al atoms. Moreover, the change of the shape of density of state induced by local atomic arrangement reveals the configurational transformation in BCC Fe-Mn-Al MEA. The microstates revealed by the SAE model are essential for revealing the atomic and electronic basis for the local atomic arrangement-dependent properties, thus promoting the development of advanced low-cost high-performance multi-component Fe alloys.

![](./images/812019289535021057_13.jpg)

![](./images/812019289535021057_14.jpg)

Fig. 6 a–e Total density of states (DOS) of the same alloying elements in various configurations generated by the SAE model, the corresponding configurations can be found in Fig. 3. The Fermi level defines the zero of energy

![](./images/812019289535021057_15.jpg)

![](./images/812019289535021057_16.jpg)

![](./images/812019289535021057_17.jpg)

![](./images/812019289535021057_18.jpg)

![](./images/812019289535021057_19.jpg)

Fig. 7 Total density of states (DOS) and partial density of states (pDOS) of the same alloying elements in various configurations generated by the SAE model, the corresponding configurations can be found in Fig. 3. The Fermi level defines the zero of energy

Acknowledgements This work was financially supported by the Key Project of the Equipment Pre-Research Field Fund of China (No. 6140922010302) and the National Natural Science Foundation of China (No. 51690164). First-principles calculations were carried out on the clusters at the Northwestern Polytechnical University.

### References
[1] E.P. George, W.A. Curtin, C.C. Tasan, Acta Mater. **188**, 435 (2020)
[2] J.W. Bae, H.S. Kim, Scr. Mater. **186**, 169 (2020)
[3] P. Sathiyamoorthi, H.S. Kim, Prog. Mater. Sci. 100709 (2020)
[4] D.B. Miracle, O.N. Senkov, Acta Mater. **122**, 448 (2017)
[5] O.N. Senkov, J.D. Miller, D.B. Miracle, C. Woodward, Nat. Com- mun. **6**, 6529 (2015)

[6] C. Lee, Y. Chou, G. Kim, M.C. Gao, K. An, J. Brechtl, C. Zhang, W. Chen, J.D. Poplawsky, G. Song, Y. Ren, Y.C. Chou, P.K. Liaw, Adv. Mater. **32**, 2004029 (2020)
[7] S.S. Sohn, A. Kwiatkowski da Silva, Y. Ikeda, F. Körmann, W. Lu, W.S. Choi, B. Gault, D. Ponge, J. Neugebauer, D. Raabe, Adv. Mater. **31**, 1807142 (2019)
[8] C.C. Yen, G.R. Huang, Y.C. Tan, H.W. Yeh, D.J. Luo, K.T. Hsieh, E.W. Huang, J.W. Yeh, S.J. Lin, C.C. Wang, C.L. Kuo, S.Y. Chang, Y.C. Lo, J. Alloys Compd. **818**, 152876 (2020)
[9] W. Cao, M. Zheng, W. Ding, X. Mao, C. Wang, W. Wang, J. Xin, Mater. Res. Express **6**, 066558 (2019)
[10] F.H.W. Körmann, A.V. Ruban, M.H.F. Sluiter, Mater. Res. Lett. **5**, 35 (2017)
[11] W.Y. Wang, J. Wang, D. Lin, C. Zou, Y. Wu, Y. Hu, S.L. Shang, K.A. Darling, Y. Wang, X. Hui, J. Li, L.J. Kecskes, P.K. Liaw, Z.K. Liu, J. Phase Equilib. Diff. **38**, 404 (2017)
[12] S. Mu, S. Wimmer, S. Mankovsky, H. Ebert, G.M. Stocks, Scr. Mater. **170**, 189 (2019)

![](./images/812019289535021057_20.jpg)

[13] W.Y. Wang, S.L. Shang, Y. Wang, Y.J. Hu, K.A. Darling, L.J. Kecskes, S.N. Mathaudhu, X.D. Hui, Z.K. Liu, Mater. Chem. Phys. **162**, 748 (2015)

[14] Y.S. Hou, H.J. Xiang, X.G. Gong, Sci. Rep. **5**, 13159 (2015)

[15] J.W. Yeh, S.K. Chen, S.J. Lin, J.Y. Gan, T.S. Chin, T.T. Shun, C.H. Tsau, S.Y. Chang, Adv. Eng. Mater. **6**, 299 (2004)

[16] S. Jiang, H. Wang, Y. Wu, X. Liu, H. Chen, M. Yao, B. Gault, D. Ponge, D. Raabe, A. Hirata, M. Chen, Y. Wang, Z. Lu, Nature **544**, 460 (2017)

[17] B. Yin, W.A. Curtin, Mater. Res. Lett. **8**, 209 (2020)

[18] V.T. Nguyen, M. Qian, Z. Shi, T. Song, L. Huang, J. Zou, Intermetallics **101**, 39 (2018)

[19] C. Lee, G. Song, M.C. Gao, R. Feng, P. Chen, J. Brechtl, Y. Chen, K. An, W. Guo, J.D. Poplawsky, S. Li, A.T. Samaei, W. Chen, A. Hu, H. Choo, P.K. Liaw, Acta Mater. **160**, 158 (2018)

[20] G. Kim, H. Diao, C. Lee, A.T. Samaei, P. Tu, M. de Jong, K. An, D. Ma, P.K. Liaw, W. Chen, Acta Mater. **181**, 124 (2019)

[21] L.R. Owen, E.J. Pickering, H.Y. Playford, H.J. Stone, M.G. Tucker, N.G. Jones, Acta Mater. **122**, 11 (2017)

[22] B. Cantor, I.T.H. Chang, P. Knight, A.J.B. Vincent, Mater. Sci. Eng. A **375-377**, 213 (2004)

[23] W.Y. Wang, S.L. Shang, Y. Wang, F. Han, K.A. Darling, Y. Wu, X. Xie, O.N. Senkov, J. Li, X.D. Hui, K.A. Dahmen, P.K. Liaw, L.J. Kecskes, Z.K. Liu, N.P.J. Comput. Mater. **3**, 23 (2017)

[24] W.Y. Wang, B. Gan, D. Lin, J. Wang, Y. Wang, B. Tang, H. Kou, S. Shang, Y. Wang, X. Gao, H. Song, X. Hui, L.J. Kecskes, Z. Xia, K.A. Dahmen, P.K. Liaw, J. Li, Z.K. Liu, J. Mater. Sci. Technol. **53**, 192 (2020)

[25] E. Ma, Scr. Mater. **181**, 127 (2020)

[26] Y. Wu, F. Zhang, X. Yuan, H. Huang, X. Wen, Y. Wang, M. Zhang, H. Wu, X. Liu, H. Wang, S. Jiang, Z. Lu, J. Mater. Sci. Technol. **62**, 214 (2021)

[27] Z. Yanwen, G. Stocks, K. Jin, C. Lu, H. Bei, B. Sales, L. Wang, L. Béland, R.E. Stoller, G. Samolyuk, M. Caro, A. Caro, W. Weber, Nat. Commun. **6**, 8736 (2015)

[28] V. Gerold, H.P. Karnthaler, Acta Metall. **37**, 2177 (1989)

[29] Y. Zhao, J. Park, J. Jang, U. Ramamurty, Acta Mater. **202**, 124 (2021)

[30] W. Jian, Z. Xie, S. Xu, Y. Su, X. Yao, I.J. Beyerlein, Acta Mater. **199**, 352 (2020)

[31] D.M. Rodríguez, F. Plazaola, J.S. Garitaonandia, J.A. Jiménez, E. Apiñaniz, Intermetallics **24**, 38 (2012)

[32] V.R. Manga, J.E. Saal, Y. Wang, V.H. Crespi, Z.K. Liu, J. Appl. Phys. **108**, 103509 (2010)

[33] E. Menéndez, M.O. Liedke, J. Fassbender, T. Gemming, A. Weber, L.J. Heyderman, K.V. Rao, S.C. Deevi, S. Suriñach, M.D. Baró, J. Sort, J. Nogués, Small **5**, 229 (2009)

[34] D. Boukhvalov, Y. Gornostyrev, M. Katsnelson, A. Lichtenstein, Phys. Rev. Lett. **99**, 247205 (2008)

[35] R. Bali, S. Wintz, F. Meutzner, R. Hübner, R. Boucher, A.A. Ünal, S. Valencia, A. Neudert, K. Potzger, J. Bauch, F. Kronast, S. Facsko, J. Lindner, J. Fassbender, Nano Lett. **14**, 435 (2014)

[36] P. Shukla, M. Wortis, Phys. Rev. B **21**, 159 (1980)

[37] C.X. Zou, J.S. Li, W.Y. Wang, Y. Zhang, D.Y. Lin, R. Yuan, X. Wang, B. Tang, J. Wang, X. Gao, H.C. Kou, X. Hui, X.Q. Zeng, M. Qian, H.F. Song, Z.K. Liu, D.S. Xu, Acta Mater. **202**, 211 (2021)

[38] C.X. Zou, J.S. Li, W.Y. Wang, Y. Zhang, B. Tang, H. Wang, D.Y. Lin, J. Wang, H.C. Kou, D.S. Xu, Comp. Mater. Sci. **152**, 169 (2018)

[39] F.Y. Tian, D.Y. Lin, X.Y. Gao, Y.F. Zhao, H.F. Song, J. Chem. Phys. **153**, 13 (2020)

[40] H. Song, F. Tian, Q.M. Hu, L. Vitos, Y. Wang, J. Shen, N. Chen, Phys. Rev. Mater. **1**, 023404 (2017)

[41] G.L.W. Hart, L.J. Nelson, R.W. Forcade, Comp. Mater. Sci. **59**, 101 (2012)

[42] F. Tian, D.Y. Lin, X. Gao, Y.F. Zhao, H.F. Song, J. Chem. Phys. **153**, 089901 (2020)

[43] G. Kresse, D. Joubert, Phys. Rev. B **59**, 1758 (1999)

[44] Y. Wang, J.P. Perdew, Phys. Rev. B **44**, 13298 (1991)

[45] G. Kresse, J. Furthmuller, Phys. Rev. B: Condens. Matter **54**, 11169 (1996)

[46] G. Kresse, J. Furthmuller, Comp. Mater. Sci. **6**, 15 (1996)

[47] Y. Wang, L.Q. Chen, Z.K. Liu, S.N. Mathaudhu, Scr. Mater. **62**, 646 (2010)

[48] M. Methfessel, A.T. Paxton, Phys. Rev. B **40**, 3616 (1989)

[49] P.E. Blochl, O. Jepsen, O.K. Andersen, Phys. Rev. B **49**, 16223 (1994)

[50] P.N.H. Nakashima, A.E. Smith, J. Etheridge, B.C. Muddle, Science **331**, 1583 (2011)

[51] W.Y. Wang, K.A. Darling, Y. Wang, S.L. Shang, L.J. Kecskes, X.D. Hui, Z.K. Liu, Scr. Mater. **120**, 31 (2016)

[52] W.Y. Wang, Y. Wang, S.L. Shang, K.A. Darling, H. Kim, B. Tang, H.C. Kou, S.N. Mathaudhu, X.D. Hui, J.S. Li, L.J. Kecskes, Z.K. Liu, Mater. Res. Lett. **5**, 415 (2017)

[53] K. Momma, F. Izumi, J. Appl. Crystallogr. **44**, 1272 (2011)

[54] S. Halas, T. Durakiewicz, J. Phys.: Condens. Matter **10**, 10815 (1998)

[55] A.J. Bradley, A.H. Jay, W.L. Bragg, Proc. R. Soc. London, Ser. A **136**, 210 (1932)

[56] A. Lawley, R.W. Cahn, J. Phys. Chem. Solids **20**, 204 (1961)

[57] A. Taylor, R.M. Jones, J. Phys. Chem. Solids **6**, 16 (1958)

[58] W.Y. Wang, B. Tang, S.L. Shang, J. Wang, S. Li, Y. Wang, J. Zhu, S. Wei, J. Wang, K.A. Darling, S.N. Mathaudhu, Y. Wang, Y. Ren, X.D. Hui, L.J. Kecskes, J. Li, Z.K. Liu, Acta Mater. **170**, 231 (2019)

[59] Y. Zhang, J. Li, W.Y. Wang, P. Li, B. Tang, J. Wang, H. Kou, S. Shang, Y. Wang, L.J. Kecskes, X. Hui, Q. Feng, Z.K. Liu, J. Mater. Sci. **54**, 13609 (2019)

[60] W.Y. Wang, Y. Zhang, J. Li, C. Zou, B. Tang, H. Wang, D. Lin, J. Wang, H. Kou, D. Xu, J. Mater. Sci. **53**, 7493 (2018)

[61] S. Ogata, J. Li, S. Yip, Science **298**, 807 (2002)

[62] V.R. Manga, S.L. Shang, W.Y. Wang, Y. Wang, J. Liang, V.H. Crespi, Z.K. Liu, Acta Mater. **82**, 287 (2015)

[63] C.L. Fu, X. Wang, Mater. Sci. Eng. A **239-240**, 761 (1997)

[64] A. Takeuchi, A. Inoue, Mater. Trans. JIM **41**, 1372 (2000)

[65] G. Hua, D. Li, Phys. Status Solidi B **249**, 1517 (2012)

[66] Z. Li, S. Zhao, R.O. Ritchie, M.A. Meyers, Prog. Mater Sci. **102**, 296 (2019)

[67] Y.Y. Zhao, Z.F. Lei, Z.P. Lu, J.C. Huang, T.G. Nieh, Mater. Res. Lett. **7**, 340 (2019)

[68] W. Chen, X. Ding, Y. Feng, X. Liu, K. Liu, Z.P. Lu, D. Li, Y. Li, C.T. Liu, X.Q. Chen, J. Mater. Sci. Technol. **34**, 355 (2018)

[69] Y.J. Hu, G. Zhao, B. Zhang, C. Yang, M. Zhang, Z.K. Liu, X. Qian, L. Qi, Nat. Commun. **10**, 4484 (2019)

![](./images/812019289535021057_21.jpg)