![](./images/812315369388638208_1.jpg)

Available online at www.sciencedirect.com
![](./images/812315369388638208_2.jpg)

Journal of Molecular Structure 739 (2005) 27-32

# Journal of
## MOLECULAR
## STRUCTURE
www.elsevier.com/locate/molstruc

# Sorption of organic solvents on the surface of crystalline syndiotactic polystyrene studied by molecular dynamics simulation

## Yoshinori Tamai⁎, Mitsuhiro Fukudaᵇ
aDepartment of Applied Physics, Faculty of Engineering, University of Fukui, Fukui 910-8507, Japan
ᵇTextile Materials Science Laboratory, Hyogo University of Teacher Education, Yashiro, Hyogo 673-1494, Japan

Received 29 March 2004; revised 27 April 2004; accepted 10 May 2004
Available online 24 November 2004

### Abstract
A molecular dynamics simulation was performed of the interface between the $\delta_{e}$ form of crystalline syndiotactic polystyrene and organic liquids, such as benzene and chloroform, in order to investigate the sorption-desorption mechanism of the solvents on the surface of the crystalline membranes, which have a molecular cavity. The sorption behavior was investigated using two surface models, i.e. the (100) and (010) interfaces. The sorption of the solvent molecules occurred only for the (100) interface model for both solvents. Chloroform was more likely absorbed by the membrane than benzene. It was found that the ordering of the liquid on the crystal surface plays an important role in the sorption mechanism.
© 2005 Elsevier B.V. All rights reserved.

**Keywords**: Crystal; Sorption; Polystyrene; Molecular dynamics; Simulation

## 1. Introduction
The $\delta$ form of the crystalline syndiotactic polystyrene (s-PS) is a clathrate molecular compound with various solvents, e.g. toluene [1], iodine [2], and 1,2-dichloroethane [3]. The emptied $\delta_{e}$ form [4] can be obtained by the extraction of the solvent molecules from the $\delta$ form. The $\delta_{e}$ form is rather stable below 400 K and is transformed into the $\gamma$ form at higher temperatures [5,6]. The stability of the $\delta_{e}$ form and the structural phase transition from the $\delta_{e}$ to $\gamma$ forms were investigated by a molecular dynamics (MD) simulation in our previous study [7].

The existence of large cavities in the $\delta_{e}$ form crystal is implied by its lower density, $0.977\ g/cm^{3}$ [4], which is significantly lower than that of the amorphous s-PS, $1.045\ g/cm^{3}$. To clarify the cavity structures in the $\delta_{e}$ form, both experimental and simulation studies have been performed [8-11]. In our previous study, [11], the cluster analysis of the free volume in the $\delta_{e}$ form clearly reveals the cavity structures; large individual holes are in an orderly manner connected by narrow channels. We call such a cavity structure a 'molecular cavity'. The smart membranes, which have a precisely controlled molecular cavity, may be used as high-performance separation membranes. For example, p-xylene is preferentially absorbed from the mixed solvents of m- and p-xylene, which are chemically alike, by the $\delta_{e}$ form [12].

The understanding of the sorption and desorption mechanism of small molecules in the $\delta$ form is essential in order to apply the s-PS crystal to the smart membranes. The mobility of small gases in the single crystal of the $\delta_{e}$ form was examined in a previous study [11,13]. The small gases, e.g. He, Ne, Ar, $O_{2}$, and $CO_{2}$, can translationally diffuse in the crystal. The diffusion mechanism consists of the large-amplitude oscillation in the cavities and the long-distance jumping through the narrow channels between cavities. The main diffusion path of small gases in the $\delta_{e}$ form was the (101) direction. Diffusion along the b-axis was also observed. As for the larger organic solvents, such as benzene, no translational diffusion was observed during 5 ns even at the higher temperature of 500 K [14]. Instead, a reorientational jumping motion about the $C_{6}$ symmetry axis of benzene was observed in the $\delta$ form [15].

⁎ Corresponding author. Tel.: +81 776 27 8032; fax: +81 776 27 8032.
E-mail address: tamai@polymer.apphy.fukui-u.ac.jp (Y. Tamai).

0022-2860/$ - see front matter © 2005 Elsevier B.V. All rights reserved.
doi:10.1016/j.molstruc.2004.05.037

<table>
<caption>Table 1
Atom types and non-bonded potential parameters of solventsª</caption>
<thead>
<tr>
<th>Atom type</th>
<th>$\sigma$ (Å)</th>
<th>$\varepsilon$ (kJ/mol)</th>
<th>$q$ (e)</th>
<th>Comment</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>CA</td>
<td>3.400</td>
<td>0.3601</td>
<td>$-0.1460$</td>
<td>Carbon (benzene)</td>
<td>[19,22]</td>
</tr>
<tr>
<td>HA</td>
<td>2.600</td>
<td>0.0628</td>
<td>$+0.1460$</td>
<td>Hydrogen (benzene)</td>
<td>[19,22]</td>
</tr>
<tr>
<td>CT</td>
<td>3.400</td>
<td>0.4580</td>
<td>$-0.3460$</td>
<td>Carbon ($\text{CHCl}_3$)</td>
<td>[21]</td>
</tr>
<tr>
<td>CL</td>
<td>3.471</td>
<td>1.1095</td>
<td>$+0.0121$</td>
<td>Chlorine ($\text{CHCl}_3$)</td>
<td>[21]</td>
</tr>
<tr>
<td>H3</td>
<td>2.115</td>
<td>0.0657</td>
<td>$+0.3097$</td>
<td>Hydrogen ($\text{CHCl}_3$)</td>
<td>[21]</td>
</tr>
</tbody>
</table>

$^{\text{a}}$ Combination rules for unlike atoms are $\sigma_{ij}=(\sigma_{ii}+\sigma_{jj})/2$ and $\varepsilon_{ij}=\sqrt{\varepsilon_{ii}\varepsilon_{jj}}$.

The fast reorientation of benzene in the $\delta$ form was also observed in the $^2$H NMR experiment of Trezza and Grassi [16].

The fact that no translational diffusion was observed for benzene seems to contradict the experimental results that the aromatic molecules, which are clathrated in the $\delta$ form, can be extracted from the crystal and can be absorbed by the crystal. How can the larger molecules, such as benzene, permeate through the narrow channels between the molecular cavities? In this study, an MD simulation was performed for the interface between the crystalline s-PS and the organic liquids, e.g. benzene ($\text{C}_6\text{H}_6$) and chloroform ($\text{CHCl}_3$), in order to investigate the sorption–desorption mechanism of the solvents on the surface of the $\delta$ form.

## 2. Simulation details

### 2.1. Force field

The simulation procedure is similar to that used in previous studies [7,11,15,17]. The bonded interactions of the bond angle, torsion angle, and improper torsion angle and the non-bonded interactions of Lennard–Jones and Coulomb were included in the potential function:

$$
\begin{aligned}
U= & \sum_{\text{angle}} k_{\theta}(\theta-\theta_{0})^{2}+\sum_{\text{torsion}} k_{\phi}[1+\cos(n\phi-\delta)] \\
& +\sum_{\text{improper}} k_{\psi}[1+\cos(n\psi-\delta)] \\
& +\sum_{i<j} 4 \varepsilon_{i j}\left[\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{12}-\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{6}\right]+\sum_{i<j} \frac{q_{i} q_{j}}{4 \pi \varepsilon_{0} r_{i j}}. \quad \text{(1)}
\end{aligned}
$$

The bond lengths were constrained to the equilibrium bond lengths, $r_0$, by the SHAKE method [18]. The bonded potential parameters were taken from the all-atom force field, AMBER [19,20]. The non-bonded potential parameters of s-PS are shown elsewhere [11]. The non-bonded and bonded potential parameters of the solvents are listed in Tables 1 and 2, respectively. The potential parameters for chloroform [21] are compatible with the AMBER force field. The atomic charges were obtained by the RESP approach so as to reproduce the electrostatic potential around the molecule [21]. The partial charge values of benzene ($\pm 0.146e$) [22] are slightly different from those of s-PS ($\pm 0.085$ e) [23]. The long-range non-bonded interactions were smoothly cut off at 14 Å.

### 2.2. Single crystal model

The initial structure of the single crystal of the $\delta_{\text{e}}$ form was generated on the basis of an X-ray diffraction experiment [4]. The space group is $P2_1/a$ and the main chain conformation is TTGG. According to the space group symmetry [24], the atomic coordinates were generated from the fractional coordinates of atoms in an asymmetric unit, which are listed in the literature [4]. An MD unit cell contains $3×4×6$ crystal units. The three-dimensional periodic boundary condition was applied such that the monomer units were infinitely connected along the $c$-axis. The MD simulation was performed for 200 ps at 300 K under ambient pressure after the equilibration runs of 50 ps. Since the simulation was started from the initial structure which was determined by the experiment, 10 ps is enough to equilibrate the crystal structure. Our simulation time for the

<table>
<caption>Table 2
Bonded potential parameters of solventsª</caption>
<thead>
<tr>
<th>Bond</th>
<th>$r_0$ (Å)</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>CA–CA</td>
<td>1.400</td>
<td>[19]</td>
</tr>
<tr>
<td>CA–HA</td>
<td>1.080</td>
<td>[19]</td>
</tr>
<tr>
<td>CT–CL</td>
<td>1.758</td>
<td>[21]</td>
</tr>
<tr>
<td>CT–H3</td>
<td>1.100</td>
<td>[21]</td>
</tr>
<tr>
<th>Angle</th>
<th>$\theta_0$ (deg.)</th>
<th>$k_0$ (kJ/mol rad$^2$)</th>
<th>Reference</th>
</tr>
<tr>
<td>CA–CA–CA</td>
<td>120.0</td>
<td>263.8</td>
<td>[19]</td>
</tr>
<tr>
<td>CA–CA–HA</td>
<td>120.0</td>
<td>209.3</td>
<td>[19,20]</td>
</tr>
<tr>
<td>CL–CT–CL</td>
<td>111.3</td>
<td>325.3</td>
<td>[21]</td>
</tr>
<tr>
<td>CL–CT–H3</td>
<td>107.7</td>
<td>159.5</td>
<td>[21]</td>
</tr>
<tr>
<th>Torsion angle</th>
<th>$n$</th>
<th>$k_\phi$ (kJ/mol)</th>
<th>$\delta$ (degrees)</th>
<th>Reference</th>
</tr>
<tr>
<td>CA–CA–CA–CA</td>
<td>2</td>
<td>15.177</td>
<td>180</td>
<td>[19]</td>
</tr>
<tr>
<td>CA–CA–CA–HA</td>
<td>2</td>
<td>15.177</td>
<td>180</td>
<td>[19]</td>
</tr>
<tr>
<td>HA–CA–CA–HA</td>
<td>2</td>
<td>15.177</td>
<td>180</td>
<td>[19]</td>
</tr>
<tr>
<th>Improper torsion</th>
<th>$n$</th>
<th>$k_\psi$ (kJ/mol)</th>
<th>$\delta$ (degrees)</th>
<th>Reference</th>
</tr>
<tr>
<td>CA–CA–CA–HA</td>
<td>2</td>
<td>4.605</td>
<td>180</td>
<td>[19]</td>
</tr>
</tbody>
</table>

$^{\text{a}}$ Bond lengths were constrained by the SHAKE method.

<table><caption>Table 3 Density and lattice constants of the s-PS $\delta_{\text{e}}$ form crystal</caption>
<thead>
<tr>
<th></th>
<th>$\rho$ ($\text{g/cm}^3$)</th>
<th>$a$ (Å)</th>
<th>$b$ (Å)</th>
<th>$c$ (Å)</th>
<th>$\alpha$ (degrees)</th>
<th>$\beta$ (degrees)</th>
<th>$\gamma$ (degrees)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Simulation</td>
<td>0.959</td>
<td>17.38</td>
<td>11.74</td>
<td>7.81</td>
<td>90.0</td>
<td>90.0</td>
<td>115.0</td>
</tr>
<tr>
<td>Experimentª</td>
<td>0.977</td>
<td>17.4</td>
<td>11.85</td>
<td>7.70</td>
<td>90</td>
<td>90</td>
<td>117</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="8">ª X-ray diffraction experiment of de Rosa et al. [4].</td>
</tr>
</tfoot>
</table>

single crystal model is sufficiently long compared with the equilibration time. Temperature and pressure tensors were controlled by the Nosé [25] and Parrinello–Rahman [26] methods, respectively. As for the single crystal model, all the edge lengths and the angles between edges were allowed to fluctuate. The virtual masses for the cell vectors and the time scaling parameter were set to $W_{\text{h}}$$=$$1$$\times$$10^4$ amu and $W_{\text{s}}$$=$$5$$\times$$10^6$ amu Å$^2$, respectively. The equations of motion were solved by a variant of the Verlet algorithm [27,28] with a time step of 1 fs, which is sufficiently short for the conservation of the Hamiltonian. The trajectories of the atoms were recorded every 500 steps for later analysis.

### 2.3. Crystal/liquid interface model

The two-phase interface models of the $\delta_{\text{e}}$ form and the organic liquids were constructed as follows. The configuration of the single crystal, whose lattice constants were close to the average values during the simulation, was extracted from the trajectory file. One of the crystal axes ($a$- or $b$-axis) was elongated approximately two times and the aroused vacant space was filled with the organic solvents. The solvent molecules were randomly inserted, avoiding severe overlaps between atoms by a scheme similar to the Metropolis Monte Carlo method. At this stage, the density of the liquid region was set to a lower value in order to complete the packing of the molecules. The number of solvent molecules is 576, which is four times the number of cavities in the single crystal model of the $\delta_{\text{e}}$ form. The total number of atoms in the unit cell was 16,128 and 12,096 for benzene and chloroform models, respectively. The (100) and (010) interface models, which were obtained by elongating $a$- and $b$-axis, respectively, were simulated for each solvent.

After a short constant NVT run of 1 ps at 300 K, the MD simulation was performed under the constant NPT condition using Nosé [25] and Parrinello–Rahman [26] methods. To prevent any unusual deformation of the unit cell, which is usually caused by the flexibility of the liquid region, the angles between the edges were constrained to the average values of the single crystal model; only the edge lengths were varied. Five equilibration runs of 10 ps each (total of 50 ps) were performed. At this stage, the virtual masses concerning one of the edges ($a$- and $b$-axes for (100) and (010) interface models, respectively) were set to a low value, $1.0$$\times$$10^2$ amu, and the others to a significantly higher value, $1.0$$\times$$10^8$ amu, in order to quickly equilibrate the cell dimensions only for the direction of the extended edge length without deformation of the crystal structure. After the cell dimensions were equilibrated, several equilibration runs were performed for a total of 250 ps using the same virtual masses in the simulation of the single crystal model. The sampling runs of 5 ns were then performed for each interface model.

A cluster machine with 28 processors (Pentium 4 and Xeon) was used for the simulation along with the molecular simulation program PAMPS [29,30] coded and developed by one of the authors (Y.T.).

## 3. Results and discussion

The structure of the single crystal model of the $\delta_{\text{e}}$ form was stable during the simulation runs. The density and

![](./images/812315369388638208_3.jpg)

Fig. 1. Time evolution of the edge lengths of the MD unit cell: (a) (100) and (b) (010) interface models with liquid benzene and chloroform.

the lattice constants obtained from the simulation for the single crystal model, listed in Table 3, are compared with the experimental data, which were determined by the X-ray diffraction experiment [4]. The experimental values were satisfactorily reproduced by the simulation.

The crystal/liquid two-phase interface models were constructed, based on the single crystal model, using the method described above. The time evolution of the edge lengths of the MD unit cell during the equilibration runs is shown in Fig. 1. The edge lengths were quickly equilibrated during the first 50 ps, where the virtual masses for one of the edge lengths (a- or b-axis) were set to the lower value. The other edge lengths were effectively fixed to the initial values because of the higher virtual masses. The density was mainly varied in the liquid region; the structure of the crystal region remained that of the single crystal model.

![](./images/812315369388638208_4.jpg)

Fig. 2. Snapshots of the (100) interface model between the $\delta_{\mathrm{e}}$ form crystal and the organic liquid projected on the $a-b$ and $a-c$ planes: (a) benzene, and (b) chloroform. The polymer and solvent molecules are indicated by thin and thick lines, respectively. Only the carbon and chlorine atoms are shown for simplicity.

After the equilibration runs of 50 ps, all the edge lengths were allowed to fluctuate, while constraining the angles between the edges to constant values.

After the equilibration runs totaled 300 ps, the sampling runs were performed for 5 ns at 300 K. Fig. 2 shows snapshots of the (100) interface models for benzene and chloroform after the MD simulation of 5 ns. In this model, the solvent molecules occasionally jumped into the crystal membrane and were trapped in a first layer cavity. The insertion path of the molecules on the surface agrees with the diffusion path of the small gases, i.e. the (101) direction [11]. The insertion process of the solvent molecules into the crystal was directly observed by monitoring the animation. After the benzene molecule interacts with the two phenyl rings of s-PS for a short time, the molecule occasionally jumps into the molecular cavity.

The snapshots of the (010) interface models after the 5 ns simulation are shown in Fig. 3. In these models, no solvent molecules entered into the crystal region. As seen from Fig. 3(a), the benzene molecules in the first solvation shell are clearly aligned on the surface of the crystal. This is in contrast to the liquid structure on the (100) surface, where the benzene molecules are randomly oriented. Because small gases can diffuse along the $b$-axis [11] (though the jump probability is low), the solvent molecules may also be absorbed along the $b$-axial direction. On the (010) surface, however, the solvent molecules are trapped by the polymer chains at positions which are different from the diffusion channels. The channels are located between the two polymer chains. Because the phase of the trapped position is shifted from that of the diffusion channels, the solvent molecules cannot be absorbed by the crystal across the (010) surface.

The number of the absorbed solvent molecules is 4 and 13 for benzene and chloroform, respectively. Though the sampling number is not sufficient to quantitatively account for the absorption rate, the chloroform molecules are, qualitatively, more easily absorbed than the benzene molecules. This is probably because the former are smaller in size than the latter. All the absorbed molecules were accumulated in the first layer cavities and did not enter into the deeper layers. A kind of 'sorption front' may be reproduced by the simulation. After a sufficient number of first layer cavities are filled with the solvent molecules,

![](./images/812315369388638208_5.jpg)

Fig. 3. Snapshots of the (010) interface model between the $\delta_{\mathrm{e}}$ from crystal and the organic liquid projected on the $a-b$ and $b-c$ planes: (a) benzene, and (b) chloroform. The polymer and solvent molecules are indicated by thin and thick lines, respectively. Only the carbon and chlorine atoms are shown for simplicity.

the spacing of the crystal along the $b$-axis may be elongated and the solvent molecules may be absorbed into the second layer. This is a mere assumption at this time. In order to clarify the sorption mechanism of the organic solvents on the surface of the $\delta$ form crystal, the simulation time has to be elongated. The long-time simulation is now in progress.

## 4. Conclusions
An MD simulation was performed using two-phase interface models between the organic liquids and the $\delta_{\mathrm{e}}$ form crystal of s-PS in order to investigate the sorption mechanism of the solvents into the crystalline polymer membranes, which have a molecular cavity. The sorption of the solvent molecules into the molecular cavities was observed only for the (100) interface model. The ordering of the liquid on the surface of the polymer crystal was found to play an important role in the sorption mechanism. On the (100) surface, the solvent molecules are randomly oriented. On the (010) surface, on the other hand, the crystal-like order of the liquid was observed on the crystal surface. The trapped positions of the solvent molecules were shifted from the diffusion channels along the $b$-axis. Therefore, the solvent molecules are preferentially absorbed on the (100) surface.

The role of the chain fluctuation in the crystal and the solvent mobility in the liquid phase is also of much interest. A further study, including the long-time simulation, the temperature dependence, and the effect of solvent species, is now in progress in order to obtain a design guide for smart membranes, which are constructed by polymer crystals with molecular cavities.

## Acknowledgements
The authors thank Prof. Y. Tsujita of the Nagoya Institute of Technology for the helpful discussions. This research was supported by the Ministry of Education, Science, Sports and Culture, Grant-in-Aid for Scientific Research on Priority Area, 13133203, and Grant-in-Aid for Young Scientists (B), 15750100.

## References
[1] Y. Chatani, Y. Shimane, T. Inagaki, T. Ijitsu, T. Yukinari, H. Shikuma, Polymer 34 (1993) 1620.
[2] Y. Chatani, T. Inagaki, Y. Shimane, H. Shikuma, Polymer 34 (1993) 4841.
[3] C. de Rosa, P. Rizzo, O.R. de Ballesteros, V. Petraccone, G. Guerra, Polymer 40 (1999) 2103.
[4] C. de Rosa, G. Guerra, V. Petraccone, B. Pirozzi, Macromolecules 30 (1997) 4147.
[5] Y.K. Wang, J.D. Savage, D. Yang, S.L. Hsu, Macromolecules 25 (1992) 3659.
[6] C. Manfredi, C. de Rosa, G. Guerra, M. Rapacciuolo, F. Auriemma, P. Corradini, Macromol. Chem. Phys. 196 (1995) 2795.
[7] Y. Tamai, M. Fukuda, Macromol. Rapid Commun. 23 (2002) 891.
[8] G. Guerra, G. Milano, V. Venditto, P. Musto, C. de Rosa, L. Cavallo, Chem. Mater. 12 (2000) 363.
[9] G. Milano, V. Venditto, G. Guerra, L. Cavallo, P. Ciambelli, D. Sannino, Chem. Mater. 13 (2001) 1506.
[10] G. Milano, G. Guerra, F. Müller-Plathe, Chem. Mater. 14 (2002) 2977.
[11] Y. Tamai, M. Fukuda, Polymer 44 (2003) 3279.
[12] M. Sivakumar, Y. Yamamoto, D. Amutharani, Y. Tsujita, H. Yoshimizu, T. Kinoshita, Macromol. Rapid Commun. 23 (2002) 77.
[13] Y. Tamai, M. Fukuda, Trans. Mater. Res. Soc. Jpn 2004; in press.
[14] Y. Tamai, M. Fukuda, unpublished.
[15] Y. Tamai, M. Fukuda, Chem. Phys. Lett. 371 (2003) 620.
[16] E. Trezza, A. Grassi, Macromol. Rapid Commun. 23 (2002) 260.
[17] Y. Tamai, M. Fukuda, Chem. Phys. Lett. 371 (2003) 217.
[18] J.P. Ryckaert, G. Ciccotti, H.J.C. Berendsen, J. Comput. Phys. 23 (1977) 327.
[19] W.D. Cornell, P. Cieplak, C.I. Bayly, I.R. Gould, K.M. Merz Jr., D.M. Ferguson, D.C. Spellmeyer, T. Fox, J.W. Caldwell, P.A. Kollman, J. Am. Chem. Soc. 117 (1995) 5179.
[20] D.A. Case, D.A. Pearlman, J.W. Caldwell, T.E. Cheatham III, J. Wang, W.S. Ross, C.L. Simmerling, T.A. Darden, K.M. Merz, R.V. Stanton, A.L. Cheng, J.J. Vincent, M. Crowley, V. Tsui, H. Gohlke, R.J. Radmer, Y. Duan, J. Pitera, I. Massova, G.L. Seibel, U.C. Singh, P.K. Weiner, P.A. Kollman, AMBER 7, University of California, San Francisco, 2000.
[21] T. Fox, P.A. Kollman, J. Phys. Chem. B 102 (1998) 8070.
[22] S.T. Howard, J.A. Platts, K. Woźniak, Chem. Phys. Lett. 239 (1995) 267.
[23] G.D. Smith, C. Ayyagari, R.L. Jaffe, M. Pekny, A. Bernarbo, J. Phys. Chem. A 102 (1998) 4694.
[24] T. Harn (Ed.),fifth ed. International Tables for Crystallography, vol. A, Space-Group Symmetry, Kluwer Academic Publishers, Dordrecht, 2002.
[25] S. Nosé, J. Chem. Phys. 81 (1984) 511.
[26] M. Parrinello, A. Rahman, J. Appl. Phys. 52 (1981) 7182.
[27] L. Verlet, Phys. Rev. 159 (1967) 98.
[28] M. Ferrario, J.P. Ryckaert, Mol. Phys. 54 (1985) 587.
[29] Y. Tamai, H. Tanaka, K. Nakanishi, Macromolecules 27 (1994) 4498.
[30] Y. Tamai, H. Tanaka, K. Nakanishi, Macromolecules 28 (1995) 2544.