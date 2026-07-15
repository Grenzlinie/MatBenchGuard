# Effects of defects and impurities on the adsorption of $\mathrm{H}_{2}\mathrm{O}$ on smithsonite (101) surfaces: Insight from DFT-D and MD

Yuanjia Luo $^{\mathrm{a}}$, Leming Ou $^{\mathrm{a},*}$, Jianhua Chen $^{\mathrm{b}}$, Guofan Zhang $^{\mathrm{a}}$, Yuqin Xia $^{\mathrm{a}}$, Bohan Zhu $^{\mathrm{a}}$, Hanyu Zhou $^{\mathrm{a}}$

${}^{\mathrm{a}}$ School of Minerals Processing and Bioengineering, Central South University, Changsha 410083, China
${}^{\mathrm{b}}$ College of Resources and Metallurgy, Guangxi University, Nanning 530004, China

---

## GRAPHICAL ABSTRACT

The adsorption of $\mathrm{H}_{2}\mathrm{O}$ on defective and impurity smithsonite surfaces was all depressed than the perfect surface.

![](./images/811969382904233985_1.jpg)

---

## ARTICLE INFO

**Keywords:**
Defects and impurities
$\mathrm{H}_{2}\mathrm{O}$
Smithsonite surface
Adsorption forms
DFT-D
MD

---

## ABSTRACT

In this paper, DFT-D calculations and MD simulations were first performed to systematically study the $\mathrm{H}_{2}\mathrm{O}$ adsorption on smithsonite (101) surface with different defects and impurities, mainly including Zn-vacancy defect and Fe, Mn, Cd, Co impurities. We found the $\mathrm{H}_{2}\mathrm{O}$ adsorption on the defective and impurity smithsonite surfaces were all depressed compared with the perfect surface. Moreover, we found the adsorption forms of $\mathrm{H}_{2}\mathrm{O}$ also changed greatly. The single $\mathrm{H}_{2}\mathrm{O}$ on perfect surface was dissociated adsorption, which mainly included the hybridizations of Zn 3d with O 2p orbitals as well as H 1s with O 2p orbitals, while that on Zn-vacancy surfaces changed to molecular adsorption, which mainly included the hybridization between Zn 3d and O 2p orbitals, and that on impurity surfaces can be observed both molecular and dissociated adsorption, which mainly included the hybridizations of d orbital of impurity atoms with O 2p orbital as well as H 1s with O 2p orbitals for the dissociated adsorption while d orbital of impurity atoms with O 2p orbital for the molecular adsorption. The analysis results demonstrated that the adsorption of $\mathrm{H}_{2}\mathrm{O}$ on the perfect smithsonite (101) surface was stronger and more stable than that on the defective and impurity surfaces.

---

## 1. Introduction

As a typical zinc oxide mineral [1-3], smithsonite is an effective way to obtain zinc. With the continuous development of society and economy, zinc sulfide resources are increasingly exhausted [4-9]. Thus, the extraction of zinc oxide is becoming more and more important.

---

* Corresponding author.
E-mail address: olm614@csu.edu.cn (L. Ou).

https://doi.org/10.1016/j.colsurfa.2021.127300
Received 2 July 2021; Received in revised form 28 July 2021; Accepted 30 July 2021
Available online 2 August 2021
0927-7757/© 2021 Elsevier B.V. All rights reserved.

The nature minerals are always embedded some defects and impu- rities in its crystal lattice [10-20], especially the smithsonite, the Zn-vacancy defect, Fe, Mn, Cd, Co impurities can be easily found in its crystal lattice [21], which is often accompanied by the changes of the color of smithsonite. The formation of the defects and impurities is mainly attributed to the high temperature and pressure environments during the mineralization, and these defects and impurities will affect the surface structure and electronic properties of the mineral, and further affect the interactions between the adsorbents and mineral surface.

Flotation is still the commonly used method to separate smithsonite from its gangues such as quartz and calcite [22-25], which is a technology that is carried out in the water. In this case, the $H_2O$ will pre-adsorb on the mineral surface. Thus, it is very necessary to study the $H_2O$ adsorption on the mineral surface to get an in-depth understanding of the subsequent adsorption of the flotation reagents. The adsorption mechanism of $H_2O$ on different surfaces varies [26-29]. Xing et al. studied the adsorption be- haviors of $H_2O$ on different types of C-vacancy coal surface, the results showed that the interaction of $H_2O$ with C-vacancy defective surface was promoted [20]. Min et al. studied the hydration mechanism of kaolinite by DFT calculations and MD simulations, the results showed that $H_2O$ mainly adsorbed on the kaolinite surface by H-bond [28]. Yann et al. studied the hydration of scheelite combined experiments and simulations, the results showed that $H_2O$ preferred to adsorb on scheelite surface by the molecular form instead of dissociation [30]. Chen et al. studied the $H_2O$ adsorption on the surfaces of ZnS and Cu-activated ZnS by DFT simulations, the results showed that the adsorption behaviors of $H_2O$ changed greatly after the surface was activated by Cu, indicating the Cu substitution has a great effect on the $H_2O$ adsorption on ZnS surface [31]. Currently, few studies were found to systematically study the adsorption of $H_2O$ on the defective and impurity smithsonite (101) surfaces, and the adsorption mechanism of $H_2O$ on the defective and impurity smithsonite surfaces is also unclear and understudied. A better understanding can help in-depth study the subsequent adsorption of the flotation reagents on mineral surfaces.

DFT calculations and MD simulations are a good method to investi- gate the adsorption of reagents on mineral surfaces [32-64], which can provide a direct illustration of the surface reactions on the mineral surface. In this paper, we first systematically studied the $H_2O$ adsorption on smithsonite surfaces containing different defects and impurities, and the surface model, adsorption configuration, formation energy, substi- tution energy and adsorption energy, cohesive energy, electron density, density of state, electron density difference, and Mulliken bond popu-lation have been analyzed to uncover the adsorption mechanism of $H_2O$ on defective and impurity smithsonite (101) surfaces. This study can provide references for the mineral processing, metallurgical industries, chemicals and materials.

## 2. Computational details

### 2.1. Computational methods

For DFT calculation, all the structural optimization and adsorption calculations were conducted using the CASTEP module in Materials Studio 2019 [65-73], which developed by Accelrys company of Amer-ica. The initial lattice parameters of the smithsonite crystal were a = b = $4.6528, c = 15.025, \alpha = \beta = 90^\circ$, and $\gamma = 120^\circ$, and it became a = b = $4.7287, c = 15.351, \alpha = \beta = 90^\circ$, and $\gamma = 120^\circ$ after optimization. The difference of them was merely 1.65%, which implied that the smith-sonite model and calculation method of this simulations were reliable. The GGA/PW91 functional and ultrasoft pseudopotentials were used during the electron calculations [74-80]. After the test, a cutoff energy of 340 eV was adopted and the precision of the k-point was set as fine. Meanwhile, the TS method for DFT-D correction was used and spin polarization was also considered in this study. The SCF tolerance was set as $2 \times 10^{-6}$ eV/atom, and the convergence tolerances of energy,maximum force, maximum displacement were selected as $2.0 \times 10^{-5}$ eV/atom, 0.05 eV/Å, and 0.002 Å, respectively.

The smithsonite (101) surface was cleaved based on the optimized smithsonite crystal and was used for creating the surface model because it has been reported that the surface energy of which is the lowest [2,63,64]. After building a $(2 \times 2 \times 1)$ surface slab, a surface model composed of five atomic layers was constructed. Meanwhile, a thickness of $15 \mathring{A}$ vacuum layers was built. The $H_2O$ was placed into a $15 \times 15 \times 15 \mathring{A}$ cell for optimization in advance. It was allowed for the $H_2O$ and the two topmost atomic layers to relax while the three bottom atomic layers were fixed.

For molecular dynamics simulation (MD), a vacuum thickness of 50 Å was constructed to eliminate the influence of periodic boundary conditions [32,33]. we constructed a spherical water cluster $(13\ H_2O)$ with a radius of $4 \mathring{A}$ to simulate the wetting behavior of the different smithsonite surfaces. The surface constructions and the water cluster were pre-optimized by CASTEP module to obtain the initial charges for MD simulation. Then, MM optimization of which using universal force field was conducted. The initial places of the spherical water cluster were above the defects and impurities on smithsonite surfaces. Then, MD simulations were carried out using NVT ensemble at 298 K. The temperature-control method was Nosé. The total simulation time was 500 ps and the time steps were 1 fs. The long-range electrostatic in-teractions used the Ewald summation method, and van der Waals in-teractions adopted the atom-based method.

### 2.2. Post-processing

The formation energies of the Zn-vacancy smithsonite surfaces can be obtained by the following equation:

$$
\Delta \mathrm{E}=\mathrm{E}_{\mathrm{Zn} \text { atom }}+\mathrm{E}_{\text {defect surface }}-\mathrm{E}_{\text {perfect surface }} \tag{1}
$$

Herein, $E_{Zn\ atom}$ represents the energy of Zn atom, $E_{defect\ surface}$ refers to the energy of the defective smithsonite surface after optimization, and $E_{perfect\ surface}$ is the energy of the optimized perfect surface.

The substitution energies of the impurity smithsonite (101) surfaces were calculated by the following equation:

$$
\Delta \mathrm{E}=\mathrm{E}_{\text {perfect surface }}+\mathrm{E}_{\text {impurity atom }}-\mathrm{E}_{\mathrm{Zn} \text { atom }}-\mathrm{E}_{\text {impurity surface }} \tag{2}
$$

Herein, $E_{perfect\ surface}$ and $E_{impurity\ surface}$ refer to the energies of the perfect and impurity smithsonite surfaces, respectively. $E_{impurity\ atom}$ represents the energy of impurity atom and $E_{Zn\ atom}$ is the energy of Zn atom.

The $H_2O$ were initially close to the T-site and B-site on the surface, and the initial positions of it on corresponding sites on perfect, defective, and impurity smithsonite surfaces were the same. The initial places of the spherical water cluster were above the defects and impurities on smithsonite surfaces. The larger average adsorption energy and the smaller cohesive energy mean the water cluster tended to maintain its spherical shape, conversely, the water cluster tended to wet the surface.

The average adsorption energies and average cohesive energies of $H_2O$ on the different surfaces can be obtained by the following Eqs. (3) and (4), respectively:

$$
E_{a d}=\frac{\mathrm{E}(\mathrm{H} 2 \mathrm{O}) \mathrm{n}+\mathrm{Slab}-(\mathrm{ESlab}+\mathrm{E}(\mathrm{H} 2 \mathrm{O}) \mathrm{n})}{n} \tag{3}
$$

$$
E_{c o}=\frac{\mathrm{E}(\mathrm{H} 2 \mathrm{O}) \mathrm{n}-(\mathrm{nE}(\mathrm{H} 2 \mathrm{O}))}{n} \tag{4}
$$

Herein, $E_{(H2O)n+slab}$ is the total energy of the smithsonite slab after n $H_2O$ adsorption, $E_{slab}$ refers to the energy of the smithsonite slab, and $E_{(H2O)n}$ represents the total energy of n $H_2O$. E(H2O) refers to the energy of single $H_2O$.

The more negative the above four energies are, the easier the re-actions become.

![](./images/811969382904233985_2.jpg)

Fig. 1. The formation energies of the defective and impurity smithsonite (101) surfaces with and without the DFT-D correction method.

## 3. Results and discussion

### 3.1. Geometry optimization and formation energies of the perfect, defective, and impurity smithsonite (101) surfaces

The formation energies of the different defects and impurities on the smithsonite (101) surfaces with and without the DFT-D correction method are shown in Fig. 1. From Fig. 1, it can be seen that all of the formation energies of the defective and impurity smithsonite surfaces were negative. This indicated that the Zn-vacancy defect, Fe-impurity, Cd-impurity, Mn-impurity, Co-impurity were all can be embedded into the smithsonite surface. Moreover, the formation energies of Fe, Mn, Co impurity smithsonite surface exhibited more negative values, indicating Fe, Mn and Co-impurities were more easily to form on smithsonite surface. These were corresponding well with the practice.

Fig. 2 shows the optimized models of the perfect, VT defect, VB defect, TFe-impurity, BFe-impurity, TCd-impurity, BCd-impurity, TMn-impurity, BMn-impurity, TCo-impurity, and BCo-impurity smithsonite (101) surfaces. It can be seen from Fig. 2(a) that the Zn sites on the smithsonite surface include the top site (T-site) and bottom site (B-site). That is to say, the defective and doped sites also include two sites. Meanwhile, from Fig. 2(a)-(k), you can see that the atoms on the defective and impurity smithsonite surfaces were all observed some movements, and the atoms on different smithsonite surfaces experienced different relaxation. This indicated the surface structures of smithsonite changed greatly after the formation of the different defects and impurities on the surface.

![](./images/811969382904233985_3.jpg)

Fig. 2. The optimized models of the perfect (a), VT defect (b), VB defect (c), TFe-impurity (d), BFe-impurity (e), TCd-impurity (f), BCd-impurity (g), TMn-impurity (h), BMn-impurity (i), TCo-impurity (j) and BCo-impurity (k) smithsonite (101) surfaces.

### 3.2. The electronic properties of the perfect, defective, and impurity smithsonite (101) surfaces

Fig. 3 shows the partial density of states (PDOS) of some atoms on perfect, VT defect, VB defect, TFe-impurity, BFe-impurity, TCd-impurity, BCd-impurity, TMn-impurity, BMn-impurity, TCo-impurity, and BCo-impurity smithsonite (101) surfaces. From Fig. 3, it can be seen the neighboring O 2s and O 2p orbitals were strongly hybridized with d orbital of impurity atoms, indicating that the neighboring O atom could firmly bound the impurity atoms on the impurity smithsonite surfaces. That is to say, strong chemical bonding between impurity atoms and neighboring O atom were formed. In addition, the peaks around Fermi level in PDOS of Zn-vacancy smithsonite surface reduced remarkably, denoting the reduction of the chemical reactivity. Moreover, the impurity levels of Fe, Cd, Mn, and Co can be obviously observed in Fig. 3, and the impurity levels of Fe, Mn, and Co were located around the Fermi level while that of Cd was located in the range of $-10\ \text{eV}$ to $-7.5$. These changes in the electronic properties of the perfect, defective, and impurity smithsonite (101) surfaces have a great

![](./images/811969382904233985_4.jpg)

Fig. 3. The PDOS of some atoms on perfect (a), VT defect (b), VB defect (c), TFe-impurity (d), BFe-impurity (e), TCd-impurity (f), BCd-impurity (g), TMn-impurity (h), BMn-impurity (i), TCo-impurity (j) and BCo-impurity (k) smithsonite (101) surfaces.

effect on the subsequent adsorption mechanism of smithsonite system.

Fig. 4 shows the electron densities of the perfect, VT defect, VB defect, TFe-impurity, BFe-impurity, TCd-impurity, BCd-impurity, TMn-impurity, BMn-impurity, TCo-impurity, and BCo-impurity smithsonite (101) surfaces. From Fig. 4, it can be obvious observed that the electron densities also produced remarkable changes.

![](./images/811969382904233985_5.jpg)

Fig. 3. (continued).

### 3.3. The adsorption of $\boldsymbol{H_2O}$ on perfect, defective, and impurity smithsonite (101) surfaces

The adsorption behaviors of $\ce{H2O}$ on perfect, defective, and impurity smithsonite (101) surfaces were systematically investigated with and without the DFT-D correction method, and the adsorption energies and adsorption models are presented in Figs. 5 and 6, respectively. As shown in Fig. 5, the adsorption energies of $\ce{H2O}$ on defective and impurity

![](./images/811969382904233985_6.jpg)

Fig. 4. The electron densities of the perfect (a), VT defect (b), VB defect (c), TFe-impurity (d), BFe-impurity (e), TCd-impurity (f), BCd-impurity (g), TMn-impurity (h), BMn-impurity (i), TCo-impurity (j) and BCo-impurity (k) smithsonite (101) surfaces.

![](./images/811969382904233985_7.jpg)

Fig. 5. The adsorption energies of $H_2O$ on the perfect, defective, and impurity smithsonite (101) surfaces with and without the DFT-D correction method.

smithsonite surfaces all increased greatly compared with the perfect surface, indicating the presence of Zn-vacancy defect and Fe, Cd, Mn, Co impurities all depressed the adsorption of $H_2O$ on smithsonite surface.

The optimized models after $H_2O$ interaction with the TZn and BZn sites on perfect smithsonite (101) surface, VT and VB sites on defective surfaces, and TFe, BFe, TCd, BCd, TMn, BMn, TCo, and BCo sites on impurity surfaces are shown in Fig. 6, and the corresponding atomic distances were marked. As illustrated in Fig. 6, the $H_2O$ exhibited different adsorption behaviors on the perfect, defective, and impurity smithsonite (101) surfaces, and the newly formed bonds after $H_2O$ adsorption on the corresponding sites on the different smithsonite surface were very close to the covalent radius of Zn—O (1.99 Å), Fe—O (1.91 Å), Cd—O (2.22 Å), Mn—O (1.91 Å), Co—O (1.90 Å) and O—H (1.11 Å), indicating the novel bonding of the corresponding atoms. For the perfect smithsonite surface, the $H_2O$ adsorption on TZn and BZn sites was both dissociated and the adsorption mainly included interaction between O of $H_2O$ and surface Zn as well as the interaction between H of $H_2O$ and surface O. For the defective surfaces, it was interesting to note that the $H_2O$ adsorption on the two sites on the surface both altered to molecular form, and the adsorption mainly composed of interaction between O of $H_2O$ and surface Zn. Meanwhile, the Zn—O distances became larger compared with the perfect surface, implying the $H_2O$ adsorption was weakened. For the impurity surfaces, most of $H_2O$ can still adsorb in the dissociated form while $H_2O$ on some sites became not dissociated, and the dissociated adsorption mainly consisted of the interaction between O of $H_2O$ and impurity atoms on the surface as well as the interaction between H of $H_2O$ and surface O while the molecular adsorption mainly composed of the interaction between impurity atoms

![](./images/811969382904233985_8.jpg)

Fig. 6. The optimized models after $H_2O$ interaction with the TZn (a) and BZn (b) sites on perfect smithsonite (101) surface, VT (c) and VB (d) sites on defective surfaces, and TFe (e), BFe (f), TCd (g), BCd (h), TMn (i), BMn (j), TCo (k) and BCo (l) sites on impurity surfaces.

on the surface and O atom of $H_2O$.

### 3.4. The electronic properties of the perfect, defective, and impurity smithsonite (101) surfaces after interaction with $H_2O$

To further reveal the effect of different defects and impurities on the $H_2O$ adsorption, the PDOS of the bonding atoms on different smithsonite surfaces were analyzed, and the results are presented in Fig. 7. For the perfect smithsonite surface, apparent orbital hybridizations occurred, which mainly included the overlaps of 3d orbital of surface Zn atom with O 2p orbital of $H_2O$ O as well as 2p orbital of surface O with H 1s orbital. For the Zn-vacancy surfaces, the interaction mainly consisted of surface Zn atom interacted with O atom of $H_2O$, which can be explained by the overlaps of Zn 3d with O 2p orbitals. Meanwhile, the overlaps were weaker than those on the perfect surface, indicating the weaker adsorption of $H_2O$. For the impurity surfaces, the dissociated adsorption of $H_2O$ mainly included the overlaps of d orbital of impurity atoms on the surface with O 2p orbital of $H_2O$ O as well as 2p orbital of surface O with H 1s orbital while the molecular adsorption mainly composed of the hybridization between d orbital of impurity atoms on the surface and O 2p orbital of $H_2O$ O.

To understand the charge transfers after $H_2O$ adsorption, the electron density difference of the bonding atoms after $H_2O$ interaction with the corresponding sites on different smithsonite surfaces were analyzed, and the electron losses (blue) and electron acceptances (red) of the interactions between $H_2O$ and different smithsonite (101) surfaces are shown in Fig. 8. From Fig. 8, it can be seen, for the perfect smithsonite surface, the interaction mainly included the electron losses of surface Zn and H of $H_2O$ as well as electron acceptances of $H_2O$ O and surface O. For the defective surfaces, the $H_2O$ was not dissociated and it mainly composed of electron losses of surface Zn and electron acceptances of O from $H_2O$. For the impurity surfaces, some of the $H_2O$ were dissociated and some of it not. The dissociation mainly consisted of the electron losses of impurity atoms on the surface and H of $H_2O$ as well as electron acceptances of $H_2O$ O and surface O while the molecular adsorption mainly included the electron losses of impurity atoms on the surface and electron acceptances of O from $H_2O$.

To further reveal the reason why the $H_2O$ adsorption behaviors on perfect, defective, and impurity smithsonite surfaces were different, the Mulliken bond populations of the bonding atoms after $H_2O$ adsorption were analyzed and the results are listed in Table 1. The larger the Mulliken bond population is, the more stable the newly formed bond is. It can be seen from Table 1 that the Mulliken bond populations of the formed Fe—O1, Cd—O1, Mn—O1, Co—O1, and O2—H bonds were all not larger than those of the corresponding bonds on the perfect surface, indicating the newly formed bonds on the perfect smithsonite surface were more stable, that is to say, the interaction of $H_2O$ with the perfect surface was stronger. This agrees well with the calculation results of the adsorption energy.

![](./images/811969382904233985_9.jpg)

Fig. 7. The PDOS of the bonding atom after $H_2O$ interaction with the TZn (a) and BZn (b) sites on perfect smithsonite (101) surface, VT (c) and VB (d) sites on defective surfaces, and TFe (e), BFe (f), TCd (g), BCd (h), TMn (i), BMn (j), TCo (k) and BCo (l) sites on impurity surfaces (O1 from $H_2O$ and O2 from smithsonite surface). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/811969382904233985_10.jpg)

Fig. 7. (continued).

### 3.5. Molecular dynamic simulations

To validate the adsorption behaviors of $\mathrm{H}_{2} \mathrm{O}$ on different smithsonite surfaces, the interactions between a spherical water cluster and the different smithsonite surfaces were investigated by the molecular dynamics simulations, and the simulation results are shown in Fig. 9 and

![](./images/811969382904233985_11.jpg)

Fig. 8. The electron density difference of the bonding atom after $H_2O$ interaction with the TZn (a) and BZn (b) sites on perfect smithsonite (101) surface, VT (c) and VB (d) sites on defective surfaces, and TFe (e), BFe (f), TCd (g), BCd (h), TMn (i), BMn (j), TCo (k) and BCo (l) sites on impurity surfaces.

<table>
<caption>Table 1 The Mulliken bond populations of Zn—O1, Fe—O1, Cd—O1, Mn—O1, Co—O1, and O2—H (O1 from $H_2O$ and O2 from the smithsonite surface).</caption>
<thead>
<tr>
<th>Adsorption surfaces</th>
<th>Adsorption sites</th>
<th>Bonds</th>
<th>Populations</th>
<th>Length (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Perfect surface</td>
<td>TZn</td>
<td>Zn—O1</td>
<td>0.70</td>
<td>1.92/2.70</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O2—H</td>
<td>0.62</td>
<td>0.97</td>
</tr>
<tr>
<td></td>
<td>BZn</td>
<td>Zn—O1</td>
<td>0.68</td>
<td>1.98/1.98</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O2—H</td>
<td>0.60</td>
<td>0.97</td>
</tr>
<tr>
<td>VT defective surface</td>
<td>TZn</td>
<td>Zn—O1</td>
<td>0.25</td>
<td>2.06</td>
</tr>
<tr>
<td>VB defective surface</td>
<td>BZn</td>
<td>Zn—O1</td>
<td>0.24</td>
<td>2.06</td>
</tr>
<tr>
<td></td>
<td>TFe</td>
<td>Fe—O1</td>
<td>0.31</td>
<td>1.91</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O2—H</td>
<td>0.61</td>
<td>0.98</td>
</tr>
<tr>
<td>BFe-impurity surface</td>
<td>BFe</td>
<td>Fe—O1</td>
<td>0.20</td>
<td>2.05</td>
</tr>
<tr>
<td>TCd-impurity surface</td>
<td>TCd</td>
<td>Cd—O1</td>
<td>0.33</td>
<td>2.12</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O2—H</td>
<td>0.48</td>
<td>1.08</td>
</tr>
<tr>
<td>BCd-impurity surface</td>
<td>BCd</td>
<td>Cd—O1</td>
<td>0.18</td>
<td>2.30</td>
</tr>
<tr>
<td>TMn-impurity surface</td>
<td>TMn</td>
<td>Mn—O1</td>
<td>0.42</td>
<td>1.85</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O2—H</td>
<td>0.62</td>
<td>0.98</td>
</tr>
<tr>
<td>BMn-impurity surface</td>
<td>BMn</td>
<td>Mn—O1</td>
<td>0.23</td>
<td>2.12</td>
</tr>
<tr>
<td>TCo-impurity surface</td>
<td>TCo</td>
<td>Co—O1</td>
<td>0.40</td>
<td>1.79</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O2—H</td>
<td>0.62</td>
<td>0.98</td>
</tr>
<tr>
<td>BCo-impurity surface</td>
<td>BCo</td>
<td>Co—O1</td>
<td>0.34</td>
<td>1.99</td>
</tr>
<tr>
<td></td>
<td></td>
<td>O2—H</td>
<td>0.58</td>
<td>1.00</td>
</tr>
</tbody>
</table>

Table 2. The initial places of the spherical water cluster were above the defects and impurities on smithsonite surfaces. The larger average adsorption energy and the smaller cohesive energy mean the water cluster tended to maintain its spherical shape, conversely, the water cluster tended to wet the surface. It can be seen from Table 2, the average adsorption energy of the water cluster on the perfect smith- sonite surface was the smallest and the cohesive energy of it was the largest. This indicated that the water cluster was very easy to wet the perfect smithsonite surface. However, for the defective and impurity surfaces, all of the average adsorption energies of the water cluster generated increases and all of the cohesive energies of it produced de- creases compared with the perfect surface, indicating the adsorption of $H_2O$ on the defective and impurity surfaces was all weakened, which agrees well with the results of DFT calculations.

### 4. Conclusion

In summary, we have systematically studied the $H_2O$ adsorption on the smithsonite surfaces containing different defect (Zn-vacancy) and impurities (Fe, Mn, Cd, and Co impurities) using DFT-D calculations and MD simulations by analysis of the surface model, adsorption configu- ration, formation energy, substitution energy, and adsorption energy, cohesive energy, electron density, density of state, electron density difference, and Mulliken bond population. The following conclusions are obtained:

(1) The formation energies of Fe, Mn, Co-impurity smithsonite sur- faces were more negative, indicating Fe, Co, and Mn impurities were more easily to form on smithsonite surfaces. The defects and

![](./images/811969382904233985_12.jpg)

Fig. 9. The equilibrium configurations after the interactions between the spherical water cluster (a) and the perfect (b), VT defect (c), VB defect (d), TFe-impurity (e), BFe-impurity (f), TCd-impurity (g), BCd-impurity (h), TMn-impurity (i), BMn-impurity (j), TCo-impurity (k) and BCo-impurity (l) smithsonite (101) surfaces.

<table><caption>Table 2 The average adsorption energies ($E_\text{ad}$) and cohesive energies ($E_\text{co}$) of $\text{H}_2\text{O}$.</caption>
<thead>
<tr>
<th>Surface models</th>
<th>Cohesive energies (kcal/mol)</th>
<th>Adsorption energies (kcal/mol)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Perfect smithsonite surface</td>
<td>5.16</td>
<td>–19.31</td>
</tr>
<tr>
<td>VT defective surface</td>
<td>–2.23</td>
<td>–10.85</td>
</tr>
<tr>
<td>VB defective surface</td>
<td>–3.12</td>
<td>–12.78</td>
</tr>
<tr>
<td>TFe-impurity surface</td>
<td>–7.60</td>
<td>–6.98</td>
</tr>
<tr>
<td>BFe-impurity surface</td>
<td>–2.43</td>
<td>–11.35</td>
</tr>
<tr>
<td>TCd-impurity surface</td>
<td>–12.76</td>
<td>–1.39</td>
</tr>
<tr>
<td>BCd-impurity surface</td>
<td>–12.37</td>
<td>–1.99</td>
</tr>
<tr>
<td>TMn-impurity surface</td>
<td>–9.77</td>
<td>–5.12</td>
</tr>
<tr>
<td>BMn-impurity surface</td>
<td>–0.38</td>
<td>–13.75</td>
</tr>
<tr>
<td>TCo-impurity surface</td>
<td>–4.02</td>
<td>–10.24</td>
</tr>
<tr>
<td>BCo-impurity surface</td>
<td>–9.36</td>
<td>–5.76</td>
</tr>
</tbody>
</table>

impurities remarkably changed the surface structure and electronic properties of smithsonite.

(2) The adsorption energies of $\text{H}_2\text{O}$ on defective and impurity smithsonite surfaces all produced a great increase compared with the perfect surface, indicating the adsorption of $\text{H}_2\text{O}$ on Zn-vacancy, Fe-impurity, Mn-impurity, Cd-impurity, and Co-impurity smithsonite surfaces were all depressed.

(3) The adsorption forms of $\text{H}_2\text{O}$ on defective and impurity smithsonite surfaces also changed greatly. The $\text{H}_2\text{O}$ adsorption on the perfect smithsonite surface was dissociated while that on the Zn-vacancy surface changed to molecular adsorption. Moreover, the molecular adsorption of $\text{H}_2\text{O}$ on some sites on impurity surfaces can also be observed.

(4) The adsorption of $\text{H}_2\text{O}$ on perfect smithsonite surface mainly included the hybridizations of 3d orbital of surface Zn atom with O 2p orbital of $\text{H}_2\text{O}$ O as well as 2p orbital of surface O with H 1s orbital, on defective surfaces mainly composed of the hybridization of Zn 3d orbital with O 2p orbital of $\text{H}_2\text{O}$ O, and on impurity surfaces mainly included the hybridizations of d orbital of impurity atoms on the surface with O 2p orbital of $\text{H}_2\text{O}$ O as well as 2p orbital of surface O with H 1s orbital for the dissociated adsorption of $\text{H}_2\text{O}$ while mainly consisted of the hybridization between d orbital of impurity atoms on the surface and O 2p orbital of $\text{H}_2\text{O}$ O for the molecular adsorption. Meanwhile, remarkable electron transfers were accompanied by the bonding of the corresponding atoms when $\text{H}_2\text{O}$ interacted with the different smithsonite surfaces.

(5) The analysis results of the density of states and Mulliken bond populations demonstrated that the adsorption of $\text{H}_2\text{O}$ on the perfect smithsonite (101) surface was stronger and more stable than that on the defective and impurity surfaces.

### CRediT authorship contribution statement

Yuanjia Luo: Conceptualization, Methodology, Investigation, Writing – original draft. Leming Ou: Supervision, Validation, Writing – review & editing, Funding acquisition. Guofan Zhang: Supervision, Validation, Writing – review & editing, Funding acquisition. Jianhua Chen: Software. Yuqin Xia: Formal analysis, Resources. Bohan Zhu: Formal analysis, Resources. Hanyu Zhou: Formal analysis, Resources.

### Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Acknowledgments

This study was financially supported by the National Natural Science Foundation of China (No. 51674291).

### References

[1] S. Bai, C. Li, X. Fu, Z. Ding, S. Wen, Promoting sulfidation of smithsonite by zinc sulfide species increase with addition of ammonium chloride and its effect on flotation performance, Miner. Eng. 125 (2018) 190–199.

[2] Y. Chen, M. Liu, J. Chen, Y. Li, C. Zhao, X. Mu, A density functional based tight binding (DFTB+) study on the sulfidization-amine flotation mechanism of smithsonite, Appl. Surf. Sci. 458 (2018) 454–463.

[3] K. Jia, Q. Feng, G. Zhang, W. Ji, W. Zhang, B. Yang, The role of S(II) and Pb(II) in xanthate flotation of smithsonite: surface properties and mechanism, Appl. Surf. Sci. 442 (2018) 92-100.

[4] Y. Chen, X. Tang, Selective flotation separation of smithsonite from calcite by application of amino trimethylene phosphonic acid as depressant, Appl. Surf. Sci. 512 (2020), 145663.

[5] Y. Chen, G. Zhang, M. Wang, Q. Shi, D. Liu, Q. Li, Utilization of sodium carbonate to eliminate the adverse effect of Ca2+ on smithsonite sulphidisation flotation, Miner. Eng. 132 (2019) 121-125.

[6] M. Liu, J. Chen, Y. Chen, Y. Zhu, Interaction between smithsonite and carboxyl collectors with different molecular structure in the presence of water: a theoretical and experimental study, Appl. Surf. Sci. 510 (2020), 145410.

[7] Q. Feng, S. Wen, Formation of zinc sulfide species on smithsonite surfaces and its response to flotation performance, J. Alloy. Compd. 709 (2017) 602-608.

[8] S. Bai, C. Li, X. Fu, J. Liu, S. Wen, Characterization of zinc sulfide species on smithsonite surfaces during sulfidation processing: effect of ammonia liquor, J. Ind. Eng. Chem. 61 (2018) 19-27.

[9] R. Deng, Y. Hu, J. Ku, W. Zuo, Z. Yang, Adsorption of Fe(III) on smithsonite surfaces and implications for flotation, Colloids Surf. A: Physicochem. Eng. Asp. 533 (2017) 308-315.

[10] J. Chen, Y. Chen, A first-principle study of the effect of vacancy defects and impurities on the adsorption of O2 on sphalerite surfaces, Colloids Surf. A: Physicochem. Eng. Asp. 363 (2010) 56-63.

[11] Y. Chen, J. Chen, The first-principle study of the effect of lattice impurity on adsorption of CN on sphalerite surface, Miner. Eng. 23 (2010) 676-684.

[12] S. Lehner, K. Savage, M. Ciobanu, D.E. Cliffel, The effect of As, Co, and Ni impurities on pyrite oxidation kinetics: an electrochemical study of synthetic pyrite, Geochim. Cosmochim. Acta 71 (2007) 2491-2509.

[13] Y.-Q. Li, J.-H. Chen, J. Guo, DFT study of influences of As, Co and Ni impurities on pyrite (100) surface oxidation by O2 molecule, Chem. Phys. Lett. 511 (2011) 389-392.

[14] Y. Chen, J. Chen, J. Guo, A DFT study on the effect of lattice impurities on the electronic structures and floatability of sphalerite, Miner. Eng. 23 (2010) 1120-1130.

[15] J. Chen, B. Ke, L. Lan, Y. Li, Influence of Ag, Sb, Bi and Zn impurities on electrochemical and flotation behaviour of galena, Miner. Eng. 72 (2015) 10-16.

[16] X. Zhou, C. Zhao, G. Wu, J. Chen, Y. Li, DFT study on the electronic structure and optical properties of N, Al, and N-Al doped graphene, Appl. Surf. Sci. 459 (2018) 354-362.

[17] J.-h. Chen, Y. Chen, Y.-q Li, Effect of vacancy defects on electronic properties and activation of sphalerite (110) surface by first-principles, Trans. Nonferrous Met. Soc. China 20 (2010) 502-506.

[18] Y.-q. Li, J.-h. Chen, Y. Chen, J. Guo, Density functional theory study of influence of impurity on electronic properties and reactivity of pyrite, Trans. Nonferrous Met. Soc. China 21 (2011) 1887-1895.

[19] H.T. Nguyen, M.T. Nguyen, Effects of sulfur-deficient defect and water on rearrangements of formamide on pyrite (100) surface, J. Phys. Chem. A 118 (2014) 4079-4086.

[20] C. Wang, Y. Xing, Y. Xia, P. Chen, W. Chen, J. Tan, C. Zhang, X. Gui, Effect of vacancy defects on electronic properties and wettability of coal surface, Appl. Surf. Sci. 511 (2020), 145546.

[21] Y. Luo, L. Ou, G. Zhang, J. Chen, Y. Li, Q. Shi, B. Zhu, Y. Xia, S. Chen, Z. Zhang, Q. Mai, H. Zhou, H. Zhou, The effect of surface vacancy on adsorption of HS on smithsonite (1 0 1) surface: a DFT study, Colloids Surf. A: Physicochem. Eng. Asp. (2021).

[22] H.J. Liu, G.F. Zhang, Y.J. Luo, Effect of depressants in the selective flotation of smithsonite and calcite using cationic collector, Physicochem. Probl. Miner. Process. 56 (2020) 1-10.

[23] Y. Luo, G. Zhang, C. Li, Q. Mai, H. Liu, H. Zhou, Q. Shi, Flotation separation of smithsonite from calcite using a new depressant fenugreek gum, Colloids Surf. A: Physicochem. Asp. 582 (2019), 123794.

[24] Y. Luo, G. Zhang, Q. Mai, H. Liu, C. Li, H. Feng, Flotation separation of smithsonite from calcite using depressant sodium alginate and mixed cationic/anionic collectors, Colloids Surf. A: Physicochem. Eng. Asp. 586 (2020), 124227.

[25] C. Liu, G. Zhu, S. Song, H. Li, Flotation separation of smithsonite from quartz using calcium lignosulphonate as a depressant and sodium oleate as a collector, Miner. Eng. 131 (2019) 385-391.

[26] X. Yu, X. Zhang, H. Wang, G. Feng, High coverage water adsorption on the CuO (111) surface, Appl. Surf. Sci. 425 (2017) 803-810.

[27] L. Zhou, F. Xiu, M. Qiu, S. Xia, L. Yu, The adsorption and dissociation of water molecule on goethite (010) surface: a DFT approach, Appl. Surf. Sci. 392 (2017) 760-767.

[28] J. Chen, F.-f. Min, L.-y. Liu, C.-f Liu, Mechanism research on surface hydration of kaolinite, insights from DFT and MD simulations, Appl. Surf. Sci. 476 (2019) 6-15.

[29] L. Shi, S. Meng, S. Jungsuttiwong, S. Namuangruk, Z.-H. Lu, L. Li, R. Zhang, G. Feng, S. Qing, Z. Gao, X. Yu, High coverage H2O adsorption on CuAl2O4 surface: a DFT study, Appl. Surf. Sci. 507 (2020), 145162.

[30] Y. Foucaud, R.L.S. Canevesi, A. Celzard, V. Fierro, M. Badawi, Hydration mechanisms of scheelite from adsorption isotherms and ab initio molecular dynamics simulations, Appl. Surf. Sci. (2021).

[31] Y. Li, J. Chen, Y. Chen, Y. Zhu, Y. Liu, DFT simulation on interaction of H2O molecules with ZnS and Cu-activated surfaces, J. Phys. Chem. C 123 (2019) 3048-3057.

[32] Y. Xia, Y. Xing, M. Li, M. Liu, J. Tan, Y. Cao, X. Gui, Studying interactions between undecane and graphite surfaces by chemical force microscopy and molecular dynamics simulations, Fuel 269 (2020), 117367.

[33] Y. Xia, R. Zhang, Y. Xing, X. Gui, Improving the adsorption of oily collector on the surface of low-rank coal during flotation using a cationic surfactant: an experimental and molecular dynamics simulation study, Fuel 235 (2019) 687-695.

[34] L. Xu, Y. Hu, H. Wu, J. Tian, J. Liu, Z. Gao, L. Wang, Surface crystal chemistry of spodumene with different size fractions and implications for flotation, Sep. Purif. Technol. 169 (2016) 33-42.

[35] H. Zhang, W. Liu, C. Han, H. Hao, Effects of monohydric alcohols on the flotation of magnesite and dolomite by sodium oleate, J. Mol. Liq. 249 (2018) 1060-1067.

[36] H. Zhang, W. Liu, H. Xu, Q. Zhuo, X. Sun, Adsorption behavior of methyl laurate and dodecane on the sub-bituminous coal surface: molecular dynamics simulation and experimental study, Minerals 9 (2019) 30.

[37] N. Nan, Y. Zhu, Y. Han, J. Liu, Molecular modeling of interactions between N-(carboxymethyl)-N-tetradecylglycine and fluorapatite, Minerals 9 (2019) 278.

[38] C. Peng, Y. Zhong, F. Min, Adsorption of alkylamine cations on montmorillonite (001) surface: a density functional theory study, Appl. Clay Sci. 152 (2018) 249-258.

[39] X. Wang, Q. Zhang, X. Li, J. Ye, L. Li, Structural and electronic properties of different terminations for quartz (001) surfaces as well as water molecule adsorption on it: a first-principles study, Minerals 8 (2018) 58.

[40] X. Wang, Q. Zhang, S. Mao, W. Cheng, A theoretical study on the electronic structure and floatability of rare earth elements (La, Ce, Nd and Y) bearing fluorapatite, Minerals 9 (2019) 500.

[41] A. Liu, J.-c Fan, M.-q Fan, Quantum chemical calculations and molecular dynamics simulations of amine collector adsorption on quartz (0 0 1) surface in the aqueous solution, Int. J. Miner. Process. 134 (2015) 1-10.

[42] A. Sarvaramini, D. Azizi, F. Larachi, Hydroxamic acid interactions with solvated cerium hydroxides in the flotation of monazite and bastnäsite-experiments and DFT study, Appl. Surf. Sci. 387 (2016) 986-995.

[43] A. Sarvaramini, F. Larachi, B. Hart, Collector attachment to lead-activated sphalerite - experiments and DFT study on pH and solvent effects, Appl. Surf. Sci. 367 (2016) 459-472.

[44] G. Liu, J. Xiao, D. Zhou, H. Zhong, P. Choi, Z. Xu, A DFT study on the structurereactivity relationship of thiophosphorus acids as flotation collectors with sulfide minerals: implication of surface adsorption, Colloids Surf. A: Physicochem. Eng. Asp. 434 (2013) 243-252.

[45] D. Azizi, F. Larachi, Surface interactions and flotation behavior of calcite, dolomite and ankerite with alkyl hydroxamic acid bearing collector and sodium silicate, Colloids Surf. A: Physicochem. Eng. Asp. 537 (2018) 126-138.

[46] Y. Zhu, B. Luo, C. Sun, J. Liu, H. Sun, Y. Li, Y. Han, Density functional theory study of α-Bromolauric acid adsorption on the α-quartz (1 0 1) surface, Miner. Eng. 92 (2016) 72-77.

[47] S.S. Rath, H. Sahoo, B. Das, B.K. Mishra, Density functional calculations of amines on the (101) face of quartz, Miner. Eng. 69 (2014) 57-64.

[48] G.R. Quezada, R.E. Rozas, P.G. Toledo, Polyacrylamide adsorption on (1 0 1) quartz surfaces in saltwater for a range of pH values by molecular dynamics simulations, Miner. Eng. 162 (2021), 106741.

[49] D. Azizi, F. Larachi, DFT simulations of pyrite galvanic interactions with bulk, solid-solution and nanoparticle Au occurrences - insights into gold cyanidation, Miner. Eng. 149 (2020), 106239.

[50] G. Zhu, Y. Cao, Y. Wang, X. Wang, J.D. Miller, D. Lu, X. Zheng, Surface chemistry features of spodumene with isomorphous substitution, Miner. Eng. 146 (2020), 106139.

[51] G. Zhu, X. Wang, E. Li, Y. Wang, J.D. Miller, Wetting characteristics of spodumene surfaces as influenced by collector adsorption, Miner. Eng. 130 (2019) 117-128.

[52] G. Liu, H. Zhong, T. Dai, L. Xia, Investigation of the effect of N-substituents on performance of thiocarbamates as selective collectors for copper sulfides by ab initio calculations, Miner. Eng. 21 (2008) 1050-1054.

[53] G. Zhao, H. Zhong, X. Qiu, S. Wang, Y. Gao, Z. Dai, J. Huang, G. Liu, The DFT study of cyclohexyl hydroxamic acid as a collector in scheelite flotation, Miner. Eng. 49 (2013) 54-60.

[54] Q. Feng, S. Wen, J. Deng, W. Zhao, DFT study on the interaction between hydrogen sulfide ions and cerussite (110) surface, Appl. Surf. Sci. 396 (2017) 920-925.

[55] H. Yi, F. Jia, Y. Zhao, W. Wang, S. Song, H. Li, C. Liu, Wettability of montmorillonite (0 0 1) surface as affected by surface charge and exchangeable cations: a molecular dynamic study, Appl. Surf. Sci. 459 (2018) 148-154.

[56] Z. Chang, C. Sun, J. Kou, G. Fu, X. Qi, Experimental and molecular dynamics simulation study on the effect of polyacrylamide on bauxite flotation, Miner. Eng. 164 (2021), 106810.

[57] X. Yang, S. Liu, G. Liu, H. Zhong, A study on the structure-reactivity relationship of aliphatic oxime derivatives as copper chelating agents and malachite flotation collectors, J. Ind. Eng. Chem. 46 (2017) 404-415.

[58] L. Li, H. Hao, Z. Yuan, Z. Liu, C. Li, Regulating effects of citric acid and pregelatinized starch on selective flocculation flotation of micro-fine siderite, J. Mol. Liq. 315 (2020), 113726.

[59] Y. Han, W. Liu, J. Chen, DFT simulation of the adsorption of sodium silicate species on kaolinite surfaces, Appl. Surf. Sci. 370 (2016) 403-409.

[60] B. Bag, B. Das, B.K. Mishra, Geometrical optimization of xanthate collectors with copper ions and their response to flotation, Miner. Eng. 24 (2011) 760-765.

[61] Y. Xia, G. Rong, Y. Xing, X. Gui, Synergistic adsorption of polar and nonpolar reagents on oxygen-containing graphite surfaces: implications for low-rank coal flotation, J. Colloid Interface Sci. 557 (2019) 276-281.

[62] J. Chen, The interaction of flotation reagents with metal ions in mineral surfaces: a perspective from coordination chemistry, Miner. Eng. 171 (2021), 107067.

[63] Y. Luo, L. Ou, G. Zhang, J. Chen, Y. Li, Q. Shi, B. Zhu, Y. Xia, S. Chen, Z. Zhang, Q. Mai, H. Zhou, H. Zhou, The effect of surface vacancy on adsorption of HS on

smithsonite (101) surface: a DFT study, Colloids Surf. A: Physicochem. Eng. Asp. 624 (2021), 126713.

[64] Y. Luo, L. Ou, J. Chen, G. Zhang, S. Jin, Y. Xia, B. Zhu, H. Zhou, DFT insights into the sulfidation mechanism of Fe-impurity smithsonite, Miner. Eng. 170 (2021), 107057.

[65] T. Qiu, Q. Nie, Y. He, Q. Yuan, Density functional theory study of cyanide adsorption on the sphalerite (1 1 0) surface, Appl. Surf. Sci. 465 (2019) 678-685.

[66] J.-H. Chen, Y.-Q. Li, L.-H. Lan, J. Guo, Interactions of xanthate with pyrite and galena surfaces in the presence and absence of oxygen, J. Ind. Eng. Chem. 20 (2014) 268-273.

[67] Y. Li, J. Chen, D. Kang, J. Guo, Depression of pyrite in alkaline medium and its subsequent activation by copper, Miner. Eng. 26 (2012) 64-69.

[68] L. Li, C. Zhang, Z. Yuan, X. Xu, Z. Song, AFM and DFT study of depression of hematite in oleate-starch-hematite flotation system, Appl. Surf. Sci. 480 (2019) 749-758.

[69] B. Li, S. Liu, J. Guo, L. Zhang, Interaction between low rank coal and kaolinite particles: a DFT simulation, Appl. Surf. Sci. 456 (2018) 215-220.

[70] Z. Zhang, Q. Zhou, Z. Yuan, L. Zhao, J. Dong, Adsorption of Mg2+ and K+ on the kaolinite (0 0 1) surface in aqueous system: a combined DFT and AIMD study with an experimental verification, Appl. Surf. Sci. 538 (2021), 148158.

[71] D. Wu, Y. Mao, J. Deng, S. Wen, Activation mechanism of ammonium ions on sulfidation of malachite (-201) surface by DFT study, Appl. Surf. Sci. 410 (2017) 126-133.

[72] T. Qiu, S. Qiu, H. Wu, H. Yan, X. Li, X. Zhou, Adsorption of hydrated [Y(OH)2]+ on kaolinite (001) surface: insight from DFT simulation, Powder Technol. 387 (2021) 80-87.

[73] H. Sun, B. Yang, Z. Zhu, W. Yin, Q. Sheng, Y. Hou, J. Yao, Paneth cell alertness to pathogens maintained by vitamin D receptors, Gastroenterology 160 (2021) 1269-1283.

[74] Y. Chen, X. Liu, J. Chen, Steric hindrance effect on adsorption of xanthate on sphalerite surface: a DFT study, Miner. Eng. 165 (2021), 106834.

[75] M.L. Chen, J.H. Chen, Y.Q. Li, J.H. Deng, High-fat diet induces cardiac remodelling and dysfunction: assessment of the role played by SIRT3 loss, J. Cell. Mol. Med. 19 (2015) 1847-1856. S9-2-S9-5.

[76] Z. Chen, Y. Nong, J. Chen, Y. Chen, B. Yu, A DFT study on corrosion mechanism of steel bar under water-oxygen interaction, Comput. Mater. Sci. 171 (2020), 109265.

[77] Y. Li, J. Chen, Y. Chen, C. Zhao, M.-H. Lee, T.-H. Lin, DFT+U study on the electronic structures and optical properties of pyrite and marcasite, Comput. Mater. Sci. 150 (2018) 346-352.

[78] Y. Wang, Y. Xian, S. Wen, J. Deng, D. Wu, The electronic structures of magnesium-bearing anosovite (Mg Ti3-O5 $0 \leq \mathrm{n} \leq 1$) and its response to flotation, J. Alloy. Compd. 708 (2017) 982-988.

[79] C. Zhao, D. Huang, J. Chen, Y. Li, Y. Chen, W. Li, The interaction of cyanide with pyrite, marcasite and pyrrhotite, Miner. Eng. 95 (2016) 131-137.

[80] Y. Zeng, J. Liu, S.-s Ru, S.-m Wen, Y. Wang, DFT study the adsorption of ethyl xanthate on the S-site of Cu-activated sphalerite (1 1 0) surface in the presence of water molecule, Results Phys. 13 (2019), 102271.