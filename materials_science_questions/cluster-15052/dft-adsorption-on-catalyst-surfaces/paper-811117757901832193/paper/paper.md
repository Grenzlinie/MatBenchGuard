The role of $H_2O$ and $O_2$ molecules and phosphorus vacancies in the structure instability of phosphorene

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2017 2D Mater. 4 015010

(http://iopscience.iop.org/2053-1583/4/1/015010)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 130.133.8.114
This content was downloaded on 05/11/2016 at 08:34

Please note that terms and conditions apply.

You may also be interested in:

Substitutionally doped phosphorene: electronic properties and gas sensor
Nawat Suvansinpan, Fayyaz Hussain, Gang Zhang et al.

Atomic vacancies significantly degrade the mechanical properties of phosphorene
Zhen-Dong Sha, Qing-Xiang Pei, Ying-Yan Zhang et al.

Geometric and electronic structures of mono- and di-vacancies in phosphorene
Ting Hu and Jinming Dong

Degradation of phosphorene in air: Understanding at atomic level
Gaoxue Wang, William J Slough, Ravindra Pandey et al.

Grain boundary in phosphorene and its unique roles on C and O doping
Zhi-Li Zhu, Wei-Yang Yu, Xiao-Yan Ren et al.

Atomic structures and electronic properties of phosphorene grain boundaries
Yu Guo, Si Zhou, Junfeng Zhang et al.

Theoretical study of the interaction of electron donor and acceptor molecules with monolayer WS2
C J Zhou, W H Yang, Y P Wu et al.

# 2D Materials

## PAPER

# The role of $H_2O$ and $O_2$ molecules and phosphorus vacancies in the structure instability of phosphorene

Andrey A Kistanov¹², Yongqing Cai², Kun Zhou¹, Sergey V Dmitriev³⁴ and Yong-Wei Zhang²

¹ School of Mechanical and Aerospace Engineering, Nanyang Technological University, 639798, Singapore
² Institute of High Performance Computing, Agency for Science, Technology and Research, 138632, Singapore
³ Institute for Metals Superplasticity Problems, Russian Academy of Sciences, 450001 Ufa, Russia
⁴ Saint Petersburg State Polytechnical University, 195251 St. Petersburg, Russia

E-mail: caiy@ihpc.a-star.edu.sg, kzhou@ntu.edu.sg and zhangyw@ihpc.a-star.edu.sg

Keywords: phosphorene, vacancy, water and oxygen, oxidation

---

## Abstract
The poor structural stability of phosphorene in air was commonly ascribed to humidity and oxygen molecules. Recent exfoliation of phosphorene in deoxygenated water promotes the need to re-examine the role of $H_2O$ and $O_2$ molecules. Considering the presence of high population of vacancies in phosphorene, we investigate the interaction of $H_2O$ and $O_2$ molecules with vacancy-contained phosphorene using first-principles calculations. In contrast to the common notion that physisorbed molecules tend to have a stronger adsorption at vacancy sites, we show that $H_2O$ has nearly the same adsorption energy at the vacancy site as that at the perfect one. Charge transfer analysis shows that $O_2$ is a strong electron scavenger, which transfers the lone-pair electrons of the phosphorus atoms to the $2\pi^*$ antibonding orbital of $O_2$. As a result, the barrier for the O–O bond splitting to form O–P bonds is reduced from 0.81 eV at the perfect site to 0.59 eV at the defect site, leading to an about 5000 faster oxidizing rate at the defect site than at the perfect site at room temperature. Hence, our work reveals that the vacancy in phosphorene shows a stronger oxygen affinity than the perfect phosphorene lattice site. Structural degradation of phosphorene due to oxidation may occur rapidly at edges and grain boundaries where vacancies tend to agglomerate.

---

## Introduction
Phosphorene, the monolayer honeycomb structure of black phosphorus, has recently attracted great attention [1–5] due to its direct finite band gap [6, 7], intriguing chemical [8–11] and optical properties [12, 13]. Owing to strong quantum confinement, phosphorene exhibits a thickness-dependent work function and band gap (0.39 eV for bulk and 1.52 eV for monolayer) [14], ideal for infrared optoelectronics applications. In addition, its high carrier mobility [3] of $1000\ \mathrm{cm^2\ V^{-1}\ s^{-1}}$ at room temperature implies its promising applications in transistors and other nanoelectronic devices. Furthermore, its asymmetric electronic and phononic conduction [15, 16], negative Poisson’s ratio [17] and highly flexible structure [18], also suggest that it is a promising material for thermoelectric and mechanoelectrical applications [19–24].

Clearly, those applications require our ability to massively produce large-area and high-quality phosphorene. Unlike other two-dimensional (2D) materials, such as graphene, boron nitride, and $\mathrm{MoS_2}$, phosphorene still cannot be fabricated by chemical vapor deposition owing to its relatively chemically reactive character. Currently, high-quality phosphorene sheets can only be obtained either by pressure-induced phase transformation [25] or by mechanical exfoliation [2], which, in general, suffers from poor scalability. In addition, liquid phase exfoliation, a conventional method for massive production of other 2D materials, has to be properly tailored in order to avoid the structural degradation of phosphorene arising from water and oxygen molecules [26–29]. To meet this requirement, anhydrous organic solvents have been used. Nevertheless, this method has some disadvantages, such as a limited exfoliation yield and sub-optimal flake size distribution of phosphorene compared with other 2D materials exfoliated in aqueous solutions [1, 30, 31]. More recently, a scalable, high-yield and environmentally benign approach was

---

© 2016 IOP Publishing Ltd

demonstrated via chemical exfoliation of phosphor- ene [32]. Although water is generally considered as a direct cause of structural degradation of phosphorene, interestingly, this method is actually based on aqueous dispersion in deoxygenated water. Clearly, the gen- erally assumed detrimental role of water needs to be reexamined, and the protective mechanism of deox-ygenated water and the interactions of water and $O_{2}$  with phosphorene need to be understood.

Another important concern of phosphorene is related to its intrinsic instability arising from its phos- phorus vacancies. It is known that for atomically thin2D materials, lattice imperfections can be easily intro- duced during fabrication or intentionally produced via electron beam or other high-energy particle excita- tions [33-35]. For phosphorene, this issue seems to be even more critical since the atomic vacancies in phos- phorene are calculated to be easily formed and abun- dant at ambient condition with their much lower formation energy (1.65 eV) than other 2D materials[36]. In addition, vacancies in phosphorene are highly mobile with an ultralow diffusion barrier of 0.30 eV compared to 1.39 eV for vacancy in graphene [36]. Such itinerant vacancies may greatly affect the stability of phosphorene in air with respect to the interaction with environmental molecules. While most of the pre- vious studies only focus on the effects of environ- mental molecules absorbed on perfect phosphorene[37-42], the interactions of defected phosphorene with environmental molecules have not been con- sidered so far.

In the present work, using first-principle calcula-tions, we investigate the effect of absorption of $H_{2} O$  and $O_{2}$ molecules on the electronic structures of per fect, mono-vacancy (MV), and di-vacancy (DV)-con- tained phosphorene. It is found that unlike graphene and $MoS_{2}$ , where defects enhance the adsorption of molecules at defective sites [38, 43], the vacancy-con- tained phosphorene shows almost the same chemical susceptibility to water as perfect phosphorene, due to their comparable energy release during adsorption, whereas for $O_{2}$ , the presence of DV can greatly pro mote its adsorption. Since vacancies in phosphorene are abundant and itinerant [36], as a consequence, oxygen molecules may be easily trapped at those defect sites. We find that the vacancies have significant effects on the oxidation of phosphorene with a 5000 faster oxidizing rate at the defect site than at the perfect site. As the vacancies tend to accumulate at the edges and grain boundaries, structural failure is highly likely to initiate at these sites. We predict that passivating the vacancies should be an effective strategy to promote the stability of phosphorene. Moreover, vacancies in phosphorene are found to be able to modulate the charge transfer between water and $O_{2}$ molecules and phosphorene. The findings revealed here may render new ways to protect phosphorene from structure degradation and control the polarity and concentra- tion of charge carriers in phosphorene.

## Computational methods
Density functional theory calculations were per- formed by using VASP [44] packages. Perdew-Burke-Ernzerhof [45] exchange-correlation functionalsunder the generalized gradient approximation (GGA) were selected. The Van der Waals corrected func- tional with Becke88 optimization (optB88) [46] was used for treating the dispersive interactions during the noncovalent chemical functionalization of phosphor- ene with small molecules. All the structures were fully relaxed until the total energy and atomic forces were smaller than $10^{-5} eV$ and $0.01 eV \AA^{-1}$ , respectively. The effects of MV and DV in phosphorene were considered by removing one or two phosphorus atoms in a $4 ×5 ×1$ supercell (80 phosphorus atoms). Periodic boundary conditions were applied in the two in-plane transverse directions, together with a vacuum space with a thickness of $20 \AA$ . For all the considered cases, we chose the energy cutoff of 400 eV and the firstBrillouin zone was sampled with a $10 ×10 ×1$  k-mesh grid. The absorption energy $(E_{a})$ of a molecule on perfect and vacancy-contained phosphorene sur- faces was calculated as $E_{a}=E_{Mol+P}-E_{P}-E_{Mol}$ , where $E_{Mol+P}, E_{P}$ and $E_{Mol}$ are the energies of the molecule adsorbed phosphorene, phosphorene sur- face, and molecule, respectively. The reaction barriers are calculated by using the climbing image nudged elastic band method.

## Results and discussions
### Electronic structure of vacancy-contained phosphorene
According to the band structure shown in figure 1(a)(lower panel), perfect phosphorene is a direct semi- conductor with a band gap of 0.88 eV, which is consistent with previous studies [18, 38, 39, 47, 48]. Note that this value is grossly underestimated due to the well-known deficiency in GGA. Similar to gra- phene, there exist many phases of MV and DV in phosphorene [36, 49-51]. Herein we only examine the lowest energy configuration of MV, which consists ofpentagon-nonagon (59) rings as shown in figure 1(b)(upper panel), and that of DV, which consists of pentagon-heptagon-pentagon-heptagon (5757) rings as shown in figure 1(c) (upper panel).

For the 59 MV, removal of a phosphorus atom from perfect phosphorene creates unpassivated atoms and dangling bonds in the defect core. While the MV- contained phosphorene exhibits essentially the same band gap as perfect phosphorene, there is a significant readjustment of band lines according to figure 1(b)(lower panel). A partially occupied defect band, which crosses the Fermi level, appears at about 0.01 eV above the valence band maximum (VBM) of the host phos- phorene, suggesting easy production of hole states (p- type conduction) even upon moderate thermal

![](./images/811117757901832193_1.jpg)

<table>
<caption>Table 1. Absorption energy ($E_{\mathrm{a}}$), charge transfer ($\Delta q$) from $\mathrm{H_2O}$ and $\mathrm{O_2}$ molecules to phosphorene, and $\mathrm{X-P}$ bond length ($B_{\mathrm{X-P}}$), where X represents the $\mathrm{H_2O}$ or $\mathrm{O_2}$ molecules. Note that a positive $\Delta q$ indicates the transfer of electrons from the molecules to phosphorene.</caption>
<thead>
<tr>
<th>Molecule</th>
<th>Phosphorene</th>
<th>$E_{\mathrm{a}}$ (eV)</th>
<th>$\Delta q$ ($e$)</th>
<th>$B_{\mathrm{X-P}}$ (Å)</th>
<th>Molecule</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">$\mathrm{H_2O}$</td>
<td>Perfect</td>
<td>$-$0.187</td>
<td>0.010</td>
<td>3.01</td>
<td>Donor</td>
</tr>
<tr>
<td>MV</td>
<td>$-$0.193</td>
<td>0.120</td>
<td>2.42</td>
<td>Donor</td>
</tr>
<tr>
<td>DV</td>
<td>$-$0.205</td>
<td>0.050</td>
<td>2.66</td>
<td>Donor</td>
</tr>
<tr>
<td rowspan="3">$\mathrm{O_2}$</td>
<td>Perfect</td>
<td>$-$0.489</td>
<td>$-$0.036</td>
<td>2.80</td>
<td>Acceptor</td>
</tr>
<tr>
<td>MV</td>
<td>$-$0.489</td>
<td>$-$0.030</td>
<td>2.94</td>
<td>Acceptor</td>
</tr>
<tr>
<td>DV</td>
<td>$-$0.705</td>
<td>0.010</td>
<td>3.02</td>
<td>Donor</td>
</tr>
</tbody>
</table>

excitations. Although MV-contained phosphorene still possesses a direct band gap, the VBM of the host phosphorene shifts from $\Gamma$ point in the perfect case to Y point. This change in the band structure may affect the optical emission efficiency of phosphorene.

For the DV-contained phosphorene, it is found that the 5757 DV defect shifts the VBM and conduction band minimum downward and upward, respectively, which leads to an increase in the band gap up to 1.04 eV (figure 1(c)). This increase may arise from the large lattice distortion and local strain induced by the DV [36]. Unlike MV defect, there is no defect state in the band gap for the DV-contained phosphorene due to the absence of dangling bond and the full passivation of atoms. In addition, similar to the MV case, the VBM shifts from $\Gamma$ to Y point and there is a direct-to-indirect band gap transition upon the introduction of 5757 DV. Such an increase in the band gap and direct-indirect band gap transition could be detectable in optical spectrum, and blue shifts of the emission and adsorption peaks may be used to corroborate the presence of the 5757 DV defect.

### Physisorption of $\mathrm{H_2O}$ and $\mathrm{O_2}$ molecules above vacancies
We next consider the physisorption of the $\mathrm{H_2O}$ and $\mathrm{O_2}$ molecules above the phosphorus-deficient phosphorene. For each molecule, we have examined several possible absorption positions on perfect and defected phosphorene. All subsequent calculations on the electronic properties and energetics are based on the lowest-energy configuration and the energetics data of the $\mathrm{H_2O}$ and $\mathrm{O_2}$ adsorptions are compiled in table 1.

![](./images/811117757901832193_2.jpg)

Figure 2. Top and side views of the examined possible absorption configurations of $H_2O$ molecule adsorbed on phosphorene. (a)-(c) for perfect, (d)-(f) with MV defect, (j), (h) and (i) with DV defect. The balls in blue and red and white represent phosphorus, oxygen and hydrogen atoms, respectively. The lowest-energy configurations of $H_2O$ molecule adsorbed on phosphorene are shown in (a), (d) and (j) for perfect, with MV defect and with DV defect, respectively.

The three lowest energy configurations for $H_2O$ and $O_2$ physical adsorptions on perfect, MV and DV-con- tained phosphorene are shown in figures 2 and 3, respectively. For the most stable binding configurations of $H_2O$ adsorbed on perfect phosphorene (figure 2(a)), one of the $O-H$ bonds is oriented parallel to the surface along the armchair direction while the other is nearly normal to the surface. The in-plane $O-H$ bond is

![](./images/811117757901832193_3.jpg)

located directly above the ridge of phosphorene. The distance from the molecule to the surface is $3.01\ \mathring{A}$ and the binding energy $E_a$ is $-0.187$ eV, which is consistent with previous work on phosphorene [37]. For the most stable binding configuration of $\text{H}_2\text{O}$ adsorption on the MV defect (figure 2(d)), both of the two $\text{O}—\text{H}$ bonds are oriented nearly parallel to the surface and located directly above the MV position. The distance from the molecule to the surface is $2.42\ \mathring{A}$ and the binding energy $E_a$ is $-0.193$ eV. Figure 2(j) shows the lowest-energy

![](./images/811117757901832193_4.jpg)

geometry of $H_2O$ adsorbed on phosphorene with the DV defect, where the $H_2O$ is located above one of the pentagon rings of the 5757 defect with the adsorption height of $2.66\mathring{A}$ and the binding energy $E_a$ of $-0.205$ eV.

For the most stable binding configuration of $O_2$ adsorbed on perfect phosphorene (figure 3(a)), the $O-O$ bond is oriented parallel to the surface along the armchair direction and located directly above the ridge. The distance from the molecule to the surface is $2.80\mathring{A}$ and the binding energy $E_a$ is $-0.489$ eV. The most stable configuration for the $O_2$ molecule absorbed on the MV defect is presented in figure 3(d), where the $O-O$ bond is located directly above the MV position, tilting about $45^\circ$ away from the surface. The distance from the molecule to the surface is $2.94\mathring{A}$ and the binding energy $E_a$ is $-0.489$ eV. For the most stable configurations of $O_2$ adsorbed on the DV defect (figure 3(j)), the $O-O$ bond deviates slightly from the in-plane surface and is located directly above the central $P-P$ bond shared by the two neighboring heptagons. The distance from the molecule to the surface is $3.02\mathring{A}$ and the binding energy $E_a$ is $-0.705$ eV. The $O-O$ bond length of the isolated molecule changes from $1.22\mathring{A}$ to $1.25$, $1.24$, and $1.24\mathring{A}$, upon adsorption on perfect, MV, and DV-contained phosphorene, respectively. This elongation of the $O-O$ bond length signifies a strong electron transfer between the substrate and the $O_2$ molecule, and the transferred charges mostly occupy the $2\pi^*$ antibonding orbital. Therefore, the $O-O$ bond is weakened even for a physisorbed $O_2$ molecule on phosphorene, and as a result, the energy for the $O-O$ bond splitting is lowered, explaining the high affinity of phosphorene to oxygen.

Interestingly, in contrast to the common notion that defects in 2D materials generally have a higher chemical affinity to adsorbates, our results show that the presence of MV has almost negligible effect on the binding energy $E_a$ of $H_2O$ and $O_2$ compared with the adsorption on perfect surface. A possible underlying reason is that the defect states are well self-passivated due to the highly puckered structure of phosphorene since the atoms in the defect core cross two neighboring ridges and tend to have a stronger interaction and hybridization than other planar 2D materials like graphene and $MoS_2$. The above scenario is consistent with previous study showing that the defects in phosphorene are nearly electronically inert [52]. For the DV defect, it can only slightly enhance the physisorption of $H_2O$ molecule (with $E_a$ from $-0.187$ eV for perfect case to $-0.205$ eV for DV case) but greatly promote the adsorption of $O_2$ molecule (with $E_a$ from $-0.489$ eV for perfect case to $-0.705$ eV for DV case). The promoted interaction may be due to the large lattice distortion and bond deformation around the DV core. Our study suggests that the vacancy-contained phosphorene shows almost the same affinity to the water molecules from the thermodynamics point of view due to the comparable energy release with the physisorption above the perfect lattice.

### Electronic structure and states alignment
Figures 4(a)-(c) presents the density of states (DOS) of perfect phosphorene, and phosphorene with MV and DV defects, respectively. It is shown that a MV defect can cause an enhancement in the electronic

![](./images/811117757901832193_5.jpg)

Figure 5. Band structure of $O_2$ on phosphorene: (a) perfect, (b) with MV defect, and (c) with DV defect. Energetic levels associated with the $O_2$ are plotted in red.

states around the top of the valence band as reflected by the increase in the peak intensity in the local density of states (LDOS) in figure 4(b) compared with that of perfect phosphorene in figure 4(a). This is attributed to the newly formed defect states above the VBM as shown in the band structure of figure 1. For the 5757 DV defect, as shown in figure 4(c), the DOS profile is quite similar to that of perfect phosphorene, and there are no defect states within the band gap.

In contrast, for the $H_2O$ physisorption, no additional electronic state within the fundamental band gap is formed for either perfect or defected phosphorene (figures 4(d)-(f)). The value of the respective band gap for perfect, MV and DV-contained phosphorene is almost the same as pristine phosphorene. However, the presence of vacancies on the surface significantly affects the alignment of the molecular levels of $H_2O$ with respect to those of phosphorene. The three highest occupied molecular orbitals (HOMO) of the $H_2O$ molecule, named according to the irreducible representation of the point group of $H_2O$, are $1b_1$ (HOMO), $3a_1$ (HOMO-1), and $1b_2$ (HOMO-2). All these levels are greatly upwardly shifted by around 1 eV in the MV- and DV-contained phosphorene. This readjustment of alignment of the molecular levels is a clear indication of a different amount of charge transfer and different interactions between water and phosphorene. Interestingly, for $H_2O$ adsorbed on perfect sheet, the $3a_1$ orbital is the most broadened one due to its favored orbital mixing with the P atom. The situation becomes different for the adsorption of MV and DV defects, where the $1b_1$ state of the $H_2O$ molecule is the most broadened one. This difference reflects the fact that $H_2O$ is prone to have a different binding mechanism at the vacancy site compared with prefect one.

In contrast, for $O_2$ molecule, its physisorption can substantially modify the electronic structure of both perfect and defected phosphorene. Figures 4(g)-(i) shows the LDOS for perfect, MV and DV-contained phosphorene, respectively. The adsorption of $O_2$ induces additional states with HOMO being located in the proximity of the VBM region. For all the cases, the antibonding LUMO state ($2\pi^*$, down) is located in the band gap of phosphorene above the Fermi level, while the HOMO state ($2\pi$, up) is slightly broadened for perfect and narrowed for MV and DV-contained phosphorene. Figure 5 shows the band structure of $O_2$-adsorbed phosphorene for the three cases. The spin triplet states (LUMO, $2\pi^*$) of $O_2$ remains unoccupied for all the cases with the degeneracy being strongly lifted for the perfect case. Unlike the case of $H_2O$ molecule absorption, the alignment of the energetic level of orbitals of $O_2$ with that of phosphorene is almost insensitive to the presence of vacancies. Therefore, the $O_2$ passivation of vacancies is able to induce trap states in the band gap of phosphorene, which is different from the case of sulfur vacancy in $MoS_2$, where the $O_2$ adsorption at the vacancy site can change the electronic nature of the vacancies from carrier-traps to electronically benign sites [38].

### Modulation of carrier density and charge transfer
To analyze the electronic interaction between the $H_2O$ and $O_2$ molecules with phosphorene, we calculated the differential charge density (DCD) $\Delta\rho(\mathbf{r})$ defined as the difference between the total charge density of molecularly adsorbed phosphorene system subtracted by the sum of the charge densities of the isolated molecule and the naked phosphorene. To obtain the exact amount of transferred charge from the $H_2O$ or $O_2$ molecule, the plane-averaged DCD $\Delta\rho(z)$ along the normal direction (z) of the phosphorene sheet is calculated by integrating $\Delta\rho(\mathbf{r})$ within the basal plane at the z point. The amount of transferred charge at z

![](./images/811117757901832193_6.jpg)

point is given by $\Delta Q(z) = \int_{-\infty}^{z} \Delta \rho(z')dz'$. Based on
the $\Delta Q(z)$ curves, the total amount of charge donated
by the molecule is read at the interface between the
molecule and the phosphorene, where $\Delta \rho(z)$ shows a
zero value. The isosurface of $\Delta \rho(\mathbf{r})$ for the $\mathrm{H_2O}$
molecule adsorbed on perfect phosphorene and phos-
phorene with MV and DV defects is depicted in
figures 6(a)-(c), respectively. It is seen that there is a
depletion of electrons in $\mathrm{H_2O}$ molecule and an
accumulation of electrons in the nearest P atoms of
perfect surface (figure 6(a)), and the $\mathrm{H_2O}$ molecule
donates electrons to phosphorene with around 0.01 $e$
per molecule. In the case MV defect, the donor ability
of $\mathrm{H_2O}$ molecule is increased and the total amount of
transferred charge increases significantly up to 0.12 $e$.
In case of DV defect, the total amount of transferred
charge from $\mathrm{H_2O}$ is 0.05 $e$. Due to the charge transfer
from water to phosphorene, an effective dipole point-
ing toward vacuum should be established across the
molecule-phosphorene interface. It is expected that
the surface coverage of $\mathrm{H_2O}$ molecules under humid-
ity condition could decrease the work function of
phosphorene layer due to the presence of the dipole
layer, which in turn could affect the charge injection
from the electrode to the channel layer and thus the
device performance.

Figures 7(a)-(c) presents the isosurface of $\Delta \rho(r)$
for the $\mathrm{O_2}$ molecule adsorbed on perfect phosphorene,
and phosphorene with MV and DV defects, respec-
tively. It is found that $\mathrm{O_2}$ accepts electrons from per-
fect phosphorene with around 0.035 $e$ per molecule.
The MV defect slightly decreases the donor ability of
$\mathrm{O_2}$ molecule with the total amount of charge transfer
amounting to 0.03 $e$. In contrast, the DV defect
receives a tiny charge transfer of 0.01 $e$ from the mole-
cule, partly due to the fully compensated structure and
weak dipole interaction. Therefore, the carrier density
of phosphorene can be modulated by water molecules,
oxygen molecules and vacancies.

### Effect of MV on the dissociation of $\mathrm{O_2}$ molecule
Experiments have shown that phosphorene can be
easily oxidized in air condition largely due to the
oxygen molecules [26-29]. However, the underlying
mechanism of the kinetic process from gas $\mathrm{O_2}$
molecule to form chemically bonded O-P species is
still unclear. Recent work [37] on GaS and $\mathrm{MoS_2}$
semiconductors has shown that most molecules,
including $\mathrm{H_2O}$, are only physisorbed on defects, while

![](./images/811117757901832193_7.jpg)

the $O_2$ molecule may reach chemisorbed state from the physisorbed state if the energy barrier is overcome. The present study shows that $H_2O$ molecule can only be physisorbed while $O_2$ molecule experiences an energy barrier from the physisorption to chemisorption on phosphorene. We find that this barrier can be strongly affected by the presence of vacancies in phosphorene. The detailed pathway from the initial state, to the transition state and to the final state for oxidation of phosphorene by $O_2$ gas molecule on perfect and MV sites are shown in figures 8(a)–(c). The calculated energy barrier $E_b$ for the perfect case is 0.81 eV. From figure 8(b), it is seen that the presence of MV can significantly reduce the barrier to 0.59 eV. According to these results, a large amount of $O_2$ molecules in air is able to be physisorbed at room temperature. Our obtained results on the chemisorbed energies (4 eV per $O_2$) are in good agreement with a recent work [53].

According to the rate theory, the transition time from the physisorbed state to the chemisorbed state is $t \approx 1/(f \cdot e^{-E_b/k_b \cdot T})$, where $E_b$ is the barrier, $k_b$ is the Boltzmann constant, $T$ is a temperature and $f$ is the attempt frequency, defined as $f = n \cdot v \cdot s_d$, where $n$ is $O_2$ density in air, $v$ is the speed, and $s_d$ can be taken as the square of lattice parameter. Hence, at the room temperature of 300 K, one atmospheric pressure, and $f$ of arround $10^8$ molecules $s^{-1}$, the time of $O_2$ molecule chemisorbtion on perfect phosphorene is $t \approx 109$ h. This value reduces to 1.33 min on the MV site, which is about 5000 times shorter. Thus, our work suggests that the oxidation rate is much higher at the vacancies than at the perfect sites and that phosphorene sheets with high-concentration vacancies can be more easily oxidized than vacancy-free phosphorene. Passivation and repairment of these vacancies in phosphorene should be effective in enhancing the chemical stability of phosphorene. However, the oxidation is also limited by the possible absorbed sites. The formation energy of P vacancy is 1.65 eV, and the concentration of the intrinsic vacancy estimated by $N_{host} ^* \exp(-1.65/kT)$, where $N_{host}$ is the total number of P atoms of the corresponding perfect lattice, is several orders of magnitude smaller than that of the host P

![](./images/811117757901832193_8.jpg)

sites. Hence, the oxidation rate of phosphorene is still largely dominated by the reaction at the perfect sites. Effects of vacancies tend to be more significant for small size phosphorene flakes which contain a large amount of edges with accumulated vacancies.

## Conclusions
By using first-principles calculations, we investigate the interaction of vacancy-contained phosphorene with $\mathrm{H}_{2} \mathrm{O}$ and $\mathrm{O}_{2}$ molecules. It is found that different from other 2D materials, vacancy-contained phosphorene is almost inert to $\mathrm{H}_{2} \mathrm{O}$ with the adsorption energy being almost the same as that in perfect phosphorene. For both perfect and vacancy-contained phosphorene, $\mathrm{H}_{2} \mathrm{O}$ molecule does not introduce any defect states in the band gap while the frontier orbitals of $\mathrm{O}_{2}$ molecule are aligned in the band gap of the VBM of the phosphorene. $\mathrm{O}_{2}$ molecule increases hole carriers and serves as a good electron scavenger for adsorption above perfect phosphorene. Vacancy-modulated charge transfer from $\mathrm{H}_{2} \mathrm{O}$ and $\mathrm{O}_{2}$ molecules may allow the modulation of the concentration and polarity of carriers in phosphorene. Finally, we investigate the kinetics of $\mathrm{O}_{2}$ dissociation and find that the oxidation rate is around 5000 times faster in the vacancy site than the perfect site. Phosphorene samples with a large amount of vacancies should be more easily oxidized than those of low-vacancy contained phosphorene. The new understandings revealed here for the interactions of $\mathrm{O}_{2}$ and $\mathrm{H}_{2} \mathrm{O}$ molecules with phosphorene may inspire new strategies to exfoliate and protect phosphorene.

## Acknowledgments
The authors gratefully acknowledge the financial support from the Ministry of Education, Singapore

(Academic Research Fund TIER 1-RG128/14), the Agency for Science, Technology and Research (A*STAR), Singapore, and the use of computing resources at the A*STAR Computational Resource Centre, Singapore. This work was supported in part by a grant from the Science and Engineering Research Council (152-70-00017). Sergey V Dmitriev acknowl- edges financial support from the Russian Science Foundation grant N 14-13-00982.

## References

[1] Yasaei P, Kuma B, Foroozan T, Wang C, Asadi M, Tuschel D, Indacochea J E, Klie R F and Khojin A S 2015 High-quality black phosphorus atomic layers by liquid-phase exfoliation *Adv. Mater.* **27** 1887–92

[2] Castellanos-Gomez A *et al* 2014 Isolation and characterization of few-layer black phosphorus *2D Mater.* **1** 025001

[3] Liu H, Neal A, Zhu Z, Luo Z, Xu X, Tománek D and Ye P 2014 Phosphorene: an unexplored 2D semiconductor with a high hole mobility *ACS Nano* **8** 4033–41

[4] Guan J, Zhu Z and Tománek D 2014 Tiling phosphorene *ACS Nano* **8** 12763–8

[5] Jing Y, Zhang X and Zhou Z 2016 Phosphorene: what can we know from computations? *WIREs Comput. Mol. Sci.* **6** 5–19

[6] Rodin A S, Carvalho A and Castro Neto A H 2014 Strain-induced gap modification in black phosphorus *Phys. Rev. Lett.* **112** 176801

[7] Tran V, Soklaski R, Liang Y F and Yang L 2014 Layer-controlled band gap and anisotropic excitons in few-layer black phosphorus *Phys. Rev. B* **89** 235319

[8] Favron A, Gaufres E, Fossard F, Phaneuf-L’Heureux A-L, Tang N, Lévesque P L, Loiseau A, Leonelli R, Francoeur S and Martel R 2015 Photooxidation and quantum confinement effects in exfoliated black phosphorus *Nat. Mater.* **14** 826–32

[9] Wang H, Yang X, Shao W, Chen S, Xie J, Zhang X, Wang J and Xie Y 2015 Ultrathin black phosphorus nanosheets for efficient singlet oxygen generation *J. Am. Chem. Soc.* **137** 11376–82

[10] Rahman M Z, Kwong C W, Davey K and Qiao S Z 2016 2D phosphorene as a water splitting photocatalyst: fundamentals to applications *Energy Environ. Sci.* **9** 709–28

[11] Gan Z X, Sun L L, Wu X L, Meng M, Shen J C and Chu P K 2015 Tunable photoluminescence from sheet-like black phosphorus crystal by electrochemical oxidation *Appl. Phys. Lett.* **107** 021901

[12] Qiao J, Kong X, Hu Z, Yang F and Ji W 2014 High-mobility transport anisotropy and linear dichroism in few-layer black phosphorus *Nat. Commun.* **5** 4475

[13] Jing Y, Tang Q, He P, Zhou Z and Shen P 2015 Small molecules make big differences: molecular doping effects on electronic and optical properties of phosphorene *Nanotechnology* **26** 095201

[14] Cai Y, Zhang G and Zhang Y-W 2014 Layer-dependent band alignment and work function of few-layer phosphorene *Sci. Rep.* **4** 6677

[15] Cai Y, Ke Q, Zhang G, Feng Y P, Shenoy V B and Zhang Y-W 2015 Giant phononic anisotropy and unusual anharmonicity of phosphorene: interlayer coupling and strain engineering *Adv. Funct. Mater.* **25** 2230–6

[16] Fei R and Yang L 2014 Strain-engineering the anisotropic electrical conductance of few-layer black phosphorus *Nano Lett.* **14** 2884–9

[17] Jiang J-W and Park H S 2014 Negative Poisson’s ratio in single-layer black phosphorus *Nat. Commun.* **5** 4727

[18] Kistanov A A, Cai Y, Zhou K, Dmitriev S V and Zhang Y-W 2016 Large electronic anisotropy and enhanced chemical activity of highly rippled phosphorene *J. Phys. Chem. C* **120** 6876–84

[19] Li L, Yu Y, Ye G J, Ge Q, Ou X, Wu H, Feng D, Chen X H and Zhang Y 2014 Black phosphorus field-effect transistors *Nat. Nanotechnol.* **9** 372–7

[20] Zhao S, Kang W and Xueac J 2014 The potential application of phosphorene as an anode material in Li-ion batteries *J. Mater. Chem. A* **2** 19046–52

[21] Xia F, Wang H and Jia Y 2014 Rediscovering black phosphorus as an anisotropic layered material for optoelectronics and electronics *Nat. Commun.* **5** 4458

[22] Du Y, Liu H, Deng Y and Ye P D 2014 Device perspective for black phosphorus field-effect transistors: contact resistance, ambipolar behavior, and scaling *ACS Nano* **8** 10035–42

[23] Quereda J, San-Jose P, Parente V, Vaquero-Garzon L, Molina-Mendoza A J, Agrait N, Rubio-Bollinger G, Guinea F, Roldán R and Castellanos-Gomez A 2016 Strong modulation of optical properties in black phosphorus through strain-engineered rippling *Nano Lett.* **16** 2931–7

[24] Buscema M, Groenendijk D J, Steele G A, van der Zant H S J and Castellanos-Gomez A 2014 Photovoltaic effect in few-layer black phosphorus PN junctions defined by local electrostatic gating *Nat. Commun.* **5** 4651

[25] Li X, Deng B, Wang X, Chen S, Vaisman M, Karato S, Pan G, Lee M L, Cha J and Wang H 2015 Synthesis of thin-film black phosphorus on a flexible substrate *2D Mater.* **2** 031002

[26] Kang J, Wood J D, Wells S A, Lee J-H, Liu X, Chen K-S and Hersam M C 2015 Solvent exfoliation of electronic-grade, two-dimensional black phosphorus *ACS Nano* **9** 3596–604

[27] Serrano-Ruiz M, Caporali M, Ienco A, Piazza V, Heun S and Peruzzini M 2016 The role of water in the preparation and stabilization of high-quality phosphorene flakes *Adv. Mater. Interfaces* **3** 1500441

[28] Xu J-Y, Gao L-F, Hu C-X, Zhu Z-Y, Zhao M, Wang Q and Zhang H-L 2016 Preparation of large size, few-layer black phosphorus nanosheets via phytic acid-assisted liquid exfoliation *Chem. Commun.* **52** 8107–10

[29] Passaglia E, Cicogna F, Lorenzetti G, Legnaioli S, Caporali M, Serrano-Ruiz M, Ienco A and Peruzzini M 2016 Novel polystyrene-based nanocomposites by phosphorene dispersion *RSC Adv.* **6** 53777–83

[30] Hanlon D *et al* 2015 Liquid exfoliation of solvent-stabilized few-layer black phosphorus for applications beyond electronics *Nat. Commun.* **6** 8563

[31] Zhao W, Xue Z, Wang J, Jiang J, Zhao X and Mu T 2015 Large-scale, highly efficient, and green liquid-exfoliation of black phosphorus in ionic liquids *ACS Appl. Mater. Interfaces* **7** 27608–12

[32] Kang J, Wells S A, Wood J D, Lee J-H, Liu X, Ryder C R, Zhu J, Guest J R, Husko C A and Hersam M C 2016 Stable aqueous dispersions of optically and electronically active phosphorene *Proc. Natl Acad. Sci.* **113** 11688–93

[33] Song Y L, Zhang Y, Zhang J M, Lu D B and Xu K W 2011 First-principles study of the structural and electronic properties of armchair silicene nanoribbons with vacancies *J. Mol. Struct.* **990** 75–8

[34] Yazyev O V and Helm L 2007 Defect-induced magnetism in graphene *Phys. Rev. B* **75** 125408

[35] Ataca C, Sahin H, Akturk E and Ciraci S 2011 Mechanical and electronic properties of MoS₂ nanoribbons and their defects *J. Phys. Chem. C* **115** 3934–41

[36] Cai Y, Ke Q, Zhang G, Yakobson B I and Zhang Y-W 2016 Highly itinerant atomic vacancies in phosphorene *J. Am. Chem. Soc.* **138** 10199–206

[37] Cai Y, Ke Q, Zhang G and Zhang Y-W 2015 Energetics, charge transfer, and magnetism of small molecules physisorbed on phosphorene *J. Phys. Chem. C* **119** 3102–10

[38] Liu Y, Stradins P and Wei S H 2016 Air passivation of chalcogen vacancies in two-dimensional semiconductors *Angew. Chem. Int. Ed.* **55** 965–8

[39] Hu T and Dong J 2015 Geometric and electronic structures of mono- and di-vacancies in phosphorene *Nanotechnology* **26** 065705

[40] Wang G, Slough W J, Pandey R and Karna S P 2016 Degradation of phosphorene in air: understanding at atomic level *2D Mater.* **3** 025011

[41] Utt K L, Rivero P, Mehboudi M, Harriss E, Borunda M F, SanJuan A A P and Barraza-Lopez S 2015 Intrinsic defects,

fluctuations of the local shape, and the photo-oxidation of black phosphorus ACS Cent. Sci. 1 320–7

[42] Wood J D, Wells S A, Jariwala D, Chen K-S, Cho E, Sangwan V K, Liu X, Lauhon L J, Marks T J and Hersam M C 2014 Effective passivation of exfoliated black phosphorus transistors against ambient degradation Nano Lett. 14 6964–70

[43] Banhart F, Kotakoski J and Krasheninnikov A V 2011 Structural defects in graphene ACS Nano 5 26–41

[44] Kresse G and Furthmüller J 1996 Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set Phys. Rev. B 54 11169

[45] Perdew J P, Burke K and Ernzerhof M 1996 Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set Phys. Rev. Lett. 77 3865–8

[46] Becke A D 1988 Density-functional exchange-energy approximation with correct asymptotic behavior Phys. Rev. A 38 3098

[47] Hu W and Yang J 2015 Defects in phosphorene J. Phys. Chem. C 119 20474–80

[48] Srivastava P, Hembram K P S S, Mizuseki H, Lee K-R, Han S S and Kim S 2015 Tuning the electronic and magnetic properties of phosphorene by vacancies and adatoms J. Phys. Chem. C 119 6530–8

[49] Li X B, Guo P, Cao T F, Liu H, Lau W M and Liu L M 2015 Structures, stabilities, and electronic properties of defects in monolayer black phosphorus Sci. Rep. 5 10848

[50] Wang V, Kawazoe Y and Geng W T 2015 Native point defects in few-layer phosphorene Phys. Rev. B 91 045433

[51] Guo Y and Robertson J 2015 Vacancy and doping states in monolayer and bulk black phosphorus Sci. Rep. 5 14165

[52] Liu Y, Xu F, Zhang Z, Penev E S and Yakobson B I 2014 Two-dimensional mono-elemental semiconductor with electronically inactive defects: the case of phosphorus Nano Lett. 14 6782–6

[53] Ziletti A, Carvalho A, Campbell D K, Coker D F and Castro Neto A H 2015 Oxygen defects in phosphorene Phys. Rev. Lett. 114 046801