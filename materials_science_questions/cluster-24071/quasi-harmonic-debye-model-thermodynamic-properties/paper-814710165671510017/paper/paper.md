Investigations of the half-metallic behavior and the magnetic and thermodynamic properties of half-Heusler CoMnTe and RuMnTe compounds: A first-principles study

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2014 Chinese Phys. B 23 087103

(http://iopscience.iop.org/1674-1056/23/8/087103)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 202.28.191.34
This content was downloaded on 21/02/2015 at 15:48

Please note that terms and conditions apply.

# Investigations of the half-metallic behavior and the magnetic and thermodynamic properties of half-Heusler CoMnTe and RuMnTe compounds: A first-principles study

T. Djaafri$^{\mathrm{a)}}$, A. Djaafri$^{\mathrm{a)}}$, A. Elias$^{\mathrm{a)}}$, G. Murtaza$^{\mathrm{b)\dagger}}$, R. Khenata$^{\mathrm{c)\ddagger}}$, R. Ahmed$^{\mathrm{d)}}$, S. Bin Omran$^{\mathrm{e)}}$, and D. Rached$^{\mathrm{f)}}$

$^{\mathrm{a)}}$Department of Physics, Faculty of Science, Dr Tahar Moulay University, 20000 Saida, Algeria
$^{\mathrm{b)}}$Modeling Laboratory, Department of Physics, Islamia College Peshawar, Pakistan
$^{\mathrm{c)}}$LPQ3M Laboratory, Department of Physics, Faculty of Science and Technology, Mascara University, 29000 Mascara, Algeria
$^{\mathrm{d)}}$Department of Physics, Faculty of Science, Universiti Teknologi Malaysia, UTM Skudai, 81310 Johor, Malaysia
$^{\mathrm{e)}}$Department of Physics and Astronomy, College of Science, King Saud University, P. O. Box 2455, Riyadh 11451, Saudi Arabia
$^{\mathrm{f)}}$Department of Physics, Faculty of Science, Djillali Liabes University, 22000 Sidi Bel-Abbes, Algeria

(Received 12 January 2014; revised manuscript received 28 February 2014; published online 20 June 2014)

First-principles spin-polarized density functional theory (DFT) investigations of the structural, electronic, magnetic, and thermodynamics characteristics of the half-Heusler, CoMnTe and RuMnTe compounds are carried out. Calculations are accomplished within a state of the art full-potential (FP) linearized $(L)$ augmented plane wave plus a local orbital (APW+lo) computational approach framed within DFT. The generalized gradient approximation (GGA) parameterized by Perdew, Burke, and Ernzerhof (PBE) is implemented as an exchange correlation functional as a part of the total energy calculation. From the analysis of the calculated electronic band structure as well as the density of states for both compounds, a strong hybridization between d states of the higher valent transition metal (TM) atoms (Co, Ru) and lower valent TM atoms of (Mn) is observed. Furthermore, total and partial density of states (PDOS) of the ground state and the results of spin magnetic moments reveal that these compounds are both stable and ideal half-metallic ferromagnetic. The effects of the unit cell volume on the magnetic properties and half-metallicity are crucial. It is worth noting that our computed results of the total spin magnetic moments, for CoMnTe equal to $4\ \mu_{\mathrm{B}}$ and $3\ \mu_{\mathrm{B}}$ per unit cell for RuMnTe, nicely follow the rule $\mu_{\mathrm{tot}}=Z_{\mathrm{t}}-18$. Using the quasi-harmonic Debye model, which considers the phononic effects, the effects of pressure $P$ and temperature $T$ on the lattice parameter, bulk modulus, thermal expansion coefficient, Debye temperature, and heat capacity for these compounds are investigated for the first time.

**Keywords:** half-Heusler alloys, half-metallic behavior, magnetism, thermodynamic properties, first principles methods

**PACS:** 71.15.Ap, 71.15.Mb, 74.25.Bt, 75.50.Gg
**DOI:** 10.1088/1674-1056/23/8/087103

## 1. Introduction

The magnetic materials particularly of the crystallographic phase $\mathrm{C1_{b}}$ of the half-Heusler compounds have been an active field of research, as a consequence of their frequently emerging novel properties and field of applications since their first discovery by Fritz Heusler.$^{[1]}$ In 1983, Groot *et al.*$^{[2]}$ discovered the half-metallic ferromagnetism in half-Heusler NiMnSb and PtMnSb compounds, and further revealed their potentials for promising technological applications. Moreover, the importance of these materials has been uncovered by viewing the novel features of the electronic band structure and magnetic behavior of half-Heusler NiMnSb compounds.$^{[3]}$ The target of recent research related to half-Heusler materials is to investigate ferromagnetic half-Heusler compounds exhibiting the magnetic shape memory effect, magnetic field induced super-elasticity, and large strain-induced changes in the magnetization.$^{[4-20]}$ In this regard, several efforts have been devoted and a lot of them are on the way to studying their electronic, magnetic, and thermodynamic properties of these systems on the basis of band structure calculations,$^{[21]}$ however, some aspects are still vague. To contribute to this active area of research, which is expected to soon undergo a revolution in technological applications because of the multi-functional properties that can be offered by a single half-Heusler ternary compound, we study the structural, electronic, magnetic, and thermodynamic properties of CoMnTe and RuMnTe by one of the most accurate approaches to electronic band structure, i.e. first-principles. The main difference between NiMnSb and, CoMnTe and RuMnTe compounds is that the magnetic moments of Co and Ni are higher than the Ru moment.$^{[3,19]}$ Surprisingly, the properties of a large number of Heusler compounds can be predicted by the direct counting of valence electrons. Based on their $\mathrm{C1_{b}}$ structure and the total number of valence electrons, the compounds CoMnTe and RuMnTe are expected to exhibit their half-metallic ferromagnetic natures. Electronic band structures of CoMnTe and RuMnTe compounds exhibit their metallic natures for spin up, and show their semiconductor behaviors for spin down. The effects of

---
$^{\dagger}$Corresponding author. E-mail: murtaza@icp.edu.pk
$^{\ddagger}$Corresponding author. E-mail: khenata_rabah@yahoo.fr
© 2014 Chinese Physical Society and IOP Publishing Ltd
http://iopscience.iop.org/cpb http://cpb.iphy.ac.cn
087103-1

the unit cell volume on the magnetic properties and the half-metallicity are crucial. It is interesting to note that the scale of the total spin moment is exactly consistent with the total number of valence electrons. Moreover, by applying a quasi-harmonic Debye model to CoMnTe and RuMnTe compounds, calculations of heat capacity at constant volume ($C_V$), heat capacity at constant pressure ($C_P$), Debye temperature ($\theta$), thermal expansion ($\alpha$), and the Grüneisen parameter ($\gamma$) in a temperature range of 0 K–1200 K in steps of 100 K and in a pressure range of 0 GPa–45 GPa in steps of 5 GPa are performed, and the obtained results are in nice agreement with those from the Debye theory, which is extensively applied to a wide range of materials.

## 2. Crystal structure
Heusler compounds ($X2YZ$) are defined as the ternary intermetallic compounds.$^{[1]}$ At the stoichiometric composition, the half-Heusler compounds ($XYZ$) each crystallize into a C1b structure. The elements associated with the $X$, $Y$, and $Z$ are (Co, Ru), Mn, and Te, respectively. The unit cell consists of four interpenetrating face-centered cubic sublattices with the positions (0, 0, 0) for Co and Ru, $(1/4,1/4,1/4)$ (for Mn, and $(3/4,3/4,3/4)$ for Te. The site $(1/2,1/2,1/2)$ is vacant in the half-Heusler compound. The crystal structure of the half-Heusler CoMnTe compound is shown in Fig. 1 as a prototype.

![](./images/814710165671510017_1.jpg)

Fig. 1. (color online) Crystal structure of the CoMnTe.

## 3. Computational details
Computations regarding geometry optimization, electronic structure calculations, and magnetic properties are performed within the FP-L(APW+lo) computational approach as realized in the WIEN2k package.$^{[22]}$ To incorporate an exchange correlation functional part into total energy functional calculations, GGA-PBE$^{[23]}$ is used, whereas to include the relativistic effects, the scalar approximation suggested by Koelling and Harmon is adopted. To control the size of the basis set for reasonable convergence, the value of cutoff parameter $R_{\text{MT}}$, $^*K_{\text{max}}=8.0$, and the value of $l=10$ is used to control the expansion of the partial waves inside the Muffin tins spheres. The values of radius $R_{\text{MT}}$ are chosen to be proportional to their ionic radii such that the spheres do not overlap. By the use of total energy convergence test to obtain the energy precision of $10^{-5}$ Ry/formula unit, 3000 $k$-points are adopted in the first part of the Brillouin zone.

To study thermal effects, quasi-harmonic Debye model realized in the Gibbs program$^{[24]}$ is used. This model is sufficiently flexible in giving all thermo dynamical quantities by incorporating the obtained results of energy and volume. We give, here, a brief description of this model.$^{[24-29]}$
In this model, non-equilibrium Gibbs function $G^{*}(V;P,T)$ is described in the following form:
$$
G^{*}(V;P,T)=E(V)+PV+A_{\text{vib}}(\Theta(V);T), \tag{1}
$$
where $E(V)$ represents the total energy/formula unit, $PV$ is the constant hydrostatic pressure condition, $\Theta(V)$ is the Debye temperature, and $A_{\text{vib}}$ is the lattice vibration that is expressed as
$$
A_{\text{vib}}(\Theta;T)=nk_{\text{B}}T\left[\frac{9\Theta}{8T}+3\ln\left(1-\mathrm{e}^{-\Theta/T}\right)-D(\Theta/T)\right]. \tag{2}
$$

In Eq. (2), $n$ represents the number of atoms/formula unit, $k_{\text{B}}$ the well-known Boltzmann constant, and the last term $D(\Theta/T)$ on the right-hand side represents the Debye integral. Here for an anisotropic solid, $\Theta$ is expressed by the following expression:
$$
\Theta=\frac{\hbar}{K}\left[6\pi^{2}V^{1/2}n\right]^{1/3}f(\sigma)\sqrt{\frac{B_{\text{s}}}{M}}. \tag{3}
$$

In Eq. (3), $M$ is the molecular mass, and $B_{\text{S}}$ the adiabatic bulk modulus, which is estimated in terms of static compressibility by using the following relation:
$$
B_{\text{s}}\cong B(V)=V\frac{\mathrm{d}^{2}E(V)}{\mathrm{d}V^{2}}, \tag{4}
$$
where $f(v)$ is defined as
$$
f(v)=\left\{3\left[2\left(\frac{21+v}{31-2v}\right)^{3/2}+\left(\frac{11+v}{31-v}\right)^{3/2}\right]^{-1}\right\}^{1/3}, \tag{5}
$$
and $v$ is the Poisson ratio in the above relation.

Minimization of the non-equilibrium Gibbs function $G^{*}(V;P,T)$ with respect to volume $V$ at constant pressure and temperature is attained as
$$
\left(\frac{\partial G^{*}(V;P,T)}{\partial V}\right)_{P,T}=0. \tag{6}
$$

By solving Eq. (6), one can obtain a relation for $V(P,T)$, i.e. thermal equation of state (EOS). Using Eq. (6) for different

thermal properties, i.e., isothermal bulk modulus $(B_T)$, specific heat capacity values at constant volume $(C_V)$ and at constant pressure $(C_P)$, and thermal expansion coefficient $\alpha$ can be evaluated using the following formulas:

$$
B_{T}(P, T)=V\left(\frac{\partial^{2} G^{*}(V ; P, T)}{\partial V^{2}}\right)_{P, T}, \tag{7}
$$

$$
C_{V}=3 n k_{\mathrm{B}}\left[4 D(\Theta / T)-\frac{3 \Theta / T}{\mathrm{e}^{\Theta / T}-1}\right], \tag{8}
$$

$$
C_{P}=C_{V}(1+\alpha \gamma T), \tag{9}
$$

$$
\alpha=\frac{\gamma C_{V}}{B_{T} V}, \tag{10}
$$

where $\gamma$ is the Grüneisen parameter and is calculated from the following expression:

$$
\gamma=-\frac{\mathrm{d} \ln \Theta(V)}{\mathrm{d} \ln V}. \tag{11}
$$

## 4. Results and discussion

### 4.1. Total energy and electronic structure

For both Heusler CoMnTe and RuMnTe compounds, first of all, the total energies for their paramagnetic and ferromagnetic states are calculated in terms of the volume per formula unit. It is found that the paramagnetic phase has high energy as compared with the ferromagnetic phase. Our optimized results for volume $(V_0)$, energy $(E_0)$, equilibrium lattice constant $(a_0)$, and bulk modulus $(B)$ calculated for the ferromagnetic phase are shown in Table 1. These results are obtained for both compounds by fitting data for energy as a function of volume to the Murnaghan equation of state $^{[32]}$, as shown in Figs. 2 and 3. The energy difference $(\Delta E)$ between paramagnetic and ferromagnetic states is also calculated and the results are given in Table 1. There are no experimental results available to us for these compounds, but our values for CoMnTe are in excellent agreement with those obtained by Selçuk Kervan *et al.* $^{[30]}$ using the full potential linearized augmented plane wave method. At equilibrium lattice constants calculated spin-polarized band structures in the ferromagnetic phase for minority spin electrons are demonstrated in Figs. 4 and 5 for CoMnTe and RuMnTe compounds respectively. From Figs. 4 and 5, it is obvious that the majority spin electrons exhibit metallic natures of the compounds and the minority spin channels display a band gap of 1.08 eV for CoMnTe and 0.83 eV for RuMnTe around the Fermi level, revealing their semiconducting natures. However, the natures of the band energy gaps are found to be indirect between the $\Gamma$ point of the highest occupied band (valence band) and the $X$ point for the lowest unoccupied band (conduction band). These semiconducting natures of the minority spin electrons and metallic natures of the majority spin channel of these compounds are very analogous to those of NiMnSb and FeMnSb$^{[33]}$ and show that these systems are half-metallic ferromagnetic.

![](./images/814710165671510017_2.jpg)

Fig. 2. (color online) Curves of total energy versus volume per formula unit for the paramagnetic (PM) and ferromagnetic (FM) states of CoMnTe.

![](./images/814710165671510017_3.jpg)

Fig. 3. (color online) Curves of total energy versus volume per formula unit for the paramagnetic (PM) and ferromagnetic (FM) states of RuMnTe.

![](./images/814710165671510017_4.jpg)

Fig. 4. Electronic band structure for minority spin electrons in CoMnTe.

<table>
<caption>Table 1. Predicted values of equilibrium lattice constant $a_0$, volume $V_0$, energy $E_0$, and bulk modulus $B$ for the ferromagnetic phase and $\Delta E$ energy difference between paramagnetic states and the ferromagnetic states.</caption>
<thead>
<tr>
<th></th>
<th>$a_0$/Å</th>
<th>$V_0$/a.u.$^3$</th>
<th>$B$/GPa</th>
<th>$B'$</th>
<th>$E_0$/eV</th>
<th>$\Delta E$/eV</th>
</tr>
</thead>
<tbody>
<tr>
<td>CoMnTe</td>
<td>5.876</td>
<td>342.347</td>
<td>118.869</td>
<td>4.832</td>
<td>−254398.605</td>
<td>1.583</td>
</tr>
<tr>
<td></td>
<td>5.86$^\text{a}$</td>
<td></td>
<td>119.97$^\text{a}$</td>
<td></td>
<td></td>
<td>1.55$^\text{a}$</td>
</tr>
<tr>
<td>RuMnTe</td>
<td>6.092</td>
<td>381.373</td>
<td>124.485</td>
<td>5.978</td>
<td>−339800.069</td>
<td>1.254</td>
</tr>
</tbody>
</table>

$^\text{a}$ Ref. [30]

![](./images/814710165671510017_5.jpg)

Fig. 5. Electronic band structure for minority spin electrons in RuMnTe.

To further depict the electronic structures of these compounds, spin-projected total and partial density of states (DOS) are also calculated and are represented in Figs. 6 and 7 for CoMnTe and RuMnTe, respectively. The negative values of total and partial densities of states correspond to the minority-spin electrons. Examinations of Figs. 6 and 7 reveal that the densities of states near the half-metallic gap, where the influences of the s and d states are insignificant, are dominated by the d-states of Co, Ru, and Mn. It is noted that the bonding d states are largely contributed from Co and Ru, whereas antibonding d states are predominantly belonging to the Mn characteristic. The corresponding d–d bandgap near the Fermi level originates from the strong hybridization between d states of higher valent TM atoms and the d states of lower valent TM atoms. The vertical dashed lines in the DOS presented in Figs. 6 and 7 represent the Fermi level ($E_{\rm F}$), which is fixed to zero.

![](./images/814710165671510017_6.jpg)

Fig. 6. Calculated spin-projected total and partial DOSs of CoMnTe.

For the spin-up states, the Fermi levels of CoMnTe and RuMnTe are located on the tails of the peaks of the partial densities of states (PDOSs) of Co and Ru, which are situated at $\approx -0.47$ eV for Co and at $\approx 0.24$ eV for Ru; alternatively, the Fermi levels can be considered to be located on the tail of the peak at $\approx -0.48$ eV of the total density of states (TDOS) for CoMnTe and on the tail of the peak at $\approx 0.23$ eV of the TDOS for RuMnTe. By contrast, the Fermi levels are located at the energy gaps for the spin-down states. The positions of the main Co peaks are located at $-1.47$ eV for the spin down and at $-2.68$ eV for the spin up, whereas for Ru they are situated at $-2.59$ eV for the spin down and at $-3.04$ eV for the spin up. Total densities of states result from the contribution of each partial density of states; it is noticeable that the main peaks remain approximately at the same positions as in the partial densities of states. Similar profiles of the densities of states are noted in both compounds. However, the band gap in the spin down is wider for CoMnTe. From the further analyses of TDOS in Figs. 6 and 7 it is found that the s and p states of Te reside in the lowest parts of the total densities of states and Te-s states are situated at $\approx$12.6 eV below $E_{\rm F}$.

![](./images/814710165671510017_7.jpg)

Fig. 7. Calculated spin-projected total and partial DOSs of RuMnTe.

### 4.2. Origin of the half-metallic gap

Admixture of the several elements is responsible for the peculiarities of half-metallic ferromagnetism of these CoMnTe and RuMnTe. The half-metallic behaviors of these compounds are closely related to the symmetry of their ${\rm C1_b}$ crystal structure, the number of valence electrons, covalent bonding, and the large swap splitting of the Mn-3d electron band states.$^{[34]}$ As described by Galanakis *et al.*,$^{[35,36]}$ the main reason for the creation of bonding and anti-bonding bands is because of the strong hybridization between the d states of the lower valent TM (Mn) atoms and the higher valent TM (Co and Ru) atoms. Filled bonding states are located typically at a higher valent TM atom site, while unoccupied anti-bonding states are at a lower valent TM atom site. Minority-occupied d state bonding is largely contributed from Co and Ru, whereas anti-bonding d states predominantly belong to the Mn characteristic. These types of structures are stable when solely the bonding states are occupied. The elements containing sp states are very important for half-Heusler compounds because of their particular role in tuning their several physical properties and structural stabilities of ${\rm C1_b}$ compounds. Each Mn atom is surrounded by

six nearest neighbors Te atoms in the structure under investigation. The strong electrostatic repulsion of the $e_g$ states at the Te atoms leads partly to the splitting of 3d states of Mn atoms into low-lying $t_{2g}$ triplet states; this phenomenon is a result of the interaction of Mn with the Te-p states. The development of the band gap is a result of the separation of occupied d bonding states from unoccupied d anti-bonding states because of the shifting of Mn-3d states to higher energies in the minority band, as schematically shown in Fig. 8; whereas in the majority band, by the shifting of Mn-3d states to lower energies, a common 3d band together with Co-3d states is formed. A similar reason can be applied to RuMnTe to explain its band gap origin. Thus, CoMnTe and RuMnTe are half-metal in the minority band with a gap at $E_F$ and metallic in the majority band. Therefore, in the sense of their band gap origin, these compounds are comparable to the semiconducting compounds like GaAs as the GaAs is strengthened by hybridizing the higher Ga-s and p states with the lower As-s and p states.

The calculated values of the total and partial magnetic moment $\mu_{\text{tot}}$ are listed in Table 2. The values of $\mu_{\text{tot}}$ are $4\ \mu_{\text{B}}$ and $3\ \mu_{\text{B}}$ per unit cell, respectively, for CoMnTe and RuMnTe, and the biggest part is contributed from the Mn atom. Up to now, there have been no experimental results on magnetic moments available to compare with our values. Our computed magnetic moments for the CoMnTe compound are in excellent agreement with FPLAW and the pseudo potential values obtained by Selçuk Kervan and Nazmiye Kerva$^{[30]}$ and by Lin $et\ al.,^{[31]}$ respectively. The total magnetic moment of the half-metallic half-Heusler compound is estimated by applying the rule $\mu_{\text{tot}}=Z_t - 18$, where $Z_t=N\uparrow+N\downarrow$ and $\mu_{\text{tot}}=N\uparrow-N\downarrow$. $N\uparrow$ represents the number of spin-up electrons, and $N\downarrow$ the number of spin-down electrons.

![](./images/814710165671510017_8.jpg)

Fig. 8. Schematic illustration of the origin of the gap in the minority band in CoMnTe.$^{[36]}$

<table>
<caption>Table 2. Values of magnetic moment per formula unit ($\mu_{\text{tot}}$), $M$ ($M$ = Co, Ru, Mn, and Te) magnetic moment ($\mu_{\text{M}}$), magnetic moment in the interstitial region ($\mu_{\text{int}}$), Fermi level $E_{\text{F}}$, and HM gap ($E_{\text{g}}$).</caption>
<tbody>
<tr>
<th></th>
<td>$\mu_{\text{tot}}/\mu_{\text{B}}$</td>
<td>$\mu_{\text{Co}}/\mu_{\text{B}}$</td>
<td>$\mu_{\text{Ru}}/\mu_{\text{B}}$</td>
<td>$\mu_{\text{Mn}}/\mu_{\text{B}}$</td>
<td>$\mu_{\text{Te}}/\mu_{\text{B}}$</td>
<td>$\mu_{\text{int}}/\mu_{\text{B}}$</td>
<td>$E_{\text{F}}/\text{eV}$</td>
<td>HM gaps/eV</td>
</tr>
<tr>
<th>CoMnTe</th>
<td>4.00</td>
<td>0.39</td>
<td>–</td>
<td>3.49</td>
<td>–0.01</td>
<td>0.14</td>
<td>9.13</td>
<td>1.08</td>
</tr>
<tr>
<th></th>
<td>$4.00^{\text{a}}$</td>
<td>$0.38^{\text{a}}$</td>
<td></td>
<td>$3.50^{\text{a}}$</td>
<td>$-0.04^{\text{a}}$</td>
<td></td>
<td>$1.13^{\text{a}}$</td>
<td></td>
</tr>
<tr>
<th></th>
<td>$4.00^{\text{b}}$</td>
<td>$0.40^{\text{b}}$</td>
<td></td>
<td>$3.48^{\text{b}}$</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>RuMnTe</th>
<td>3.00</td>
<td>–</td>
<td>–0.29</td>
<td>3.28</td>
<td>–0.03</td>
<td>0.05</td>
<td>10.50</td>
<td>0.83</td>
</tr>
<tr>
<th colspan="9">$^{\text{a}}$ Ref. [31] $^{\text{b}}$ Ref. [30]</th>
</tr>
</tbody>
</table>

Nine minority bands of half-Heusler compounds are fully occupied, which is in accordance with the straightforward rule of 18 regarding half-metallicity in the $\text{Cl}_b$ structure.$^{[37-42]}$ CoMnTe has 22 valence electrons per unit cell and RuMnTe has 21.9 valence electrons that are contributed from Co, 8 valence electrons from Ru, 7 valence electrons from Mn, and 6 valence electrons from Te. The value of the calculated total magnetic moment nicely follows the above rule, i.e. $\mu_{\text{tot}}=Z_t - 18$.

The calculated magnetic moment at the Mn site is $3.28\ \mu_{\text{B}}$ in RuMnTe but it is increased if Ru is replaced by Co ($\approx3.49\ \mu_{\text{B}}$), as shown in Table 2, while the contribution of Te is negative. The magnetic moment at the Co site is $0.39\ \mu_{\text{B}}$, which is significantly larger than at the Ru site ($-0.2\ \mu_{\text{B}}$). Thus, the replacement of Co by Ru modifies the total magnetic moment from $4\ \mu_{\text{B}}$ to $3\ \mu_{\text{B}}$. In fact, all half-Heusler compounds containing Mn each have a large value of total magnetic moment due to the contributions of Mn in the full-Heusler compounds.$^{[31]}$

To see the influences of strains on the magnetic characteristics of the CoMnTe and RuMnTe, we study the variation of the magnetic moment with the unit cell volume. Figure 9 depicts the variations of the total magnetic moment and spin moment of Co, Ru, Mn, and Te atoms with cell volume. It is clear from Fig. 9 that when CoMnTe and RuMnTe unit cells are expanded, hybridizations between Co, Ru, and Mn decrease; as a result, the spin moments of the Co and Ru decrease, while the Mn spin moment increases. However, total magnetic moments/formula units almost remain unchanged for both CoMnTe and RuMnTe compounds. The variation in the total moment is found to be less than $0.01\ \mu_{\text{B}}$ for each compound during contraction and expansion, as compared with the predicted equilibrium unit cell volume. It is interesting to note that during the contraction and expansion, the change in the number of occupied minority-spin states is also small. Regarding the $E_{\text{F}}$ contraction, it shifts it upwards in energy whereas the expansion shifts it downwards.$^{[24]}$ The half-metallic gaps remain non-zero when the unit cell volume is changed from $-5\%$ to $+5\%$ for CoMnTe and RuMnTe but for NiCrSe, reinforcement of the half-metallicity behavior is reported during expansion and vice versa.$^{[24]}$ Thus, these results signify the crucial role of unit cell volume in the magnetic properties and

half-metallicity.

![](./images/814710165671510017_9.jpg)

Fig. 9. (color online) The unit cell volume dependences of the total magnetic moments (square symbols) and the spin moments of Co and Ru (circle symbols), Mn (up triangle symbols), Te (down triangle symbols), and interstitial (diamond symbols) for CoMnTe and RuMnTe.

## 5. Thermodynamic properties

The values of thermodynamic parameters are computed at the level of the quasi-harmonic Debye model approach for half-Heusler CoMnTe and RuMnTe compounds. These calculations are done for specific heats at constant volume ($C_V$) and constant pressure ($C_P$), Debye temperature ($\theta$), thermal expansion coefficient ($\alpha$), and Grüneisen parameter ($\gamma$) in the temperature range of 0 K–1200 K in steps of 100 K and at pressure ranging from 0 GPa to 45 GPa in steps of 5 GPa.

It is seen from Figs. 10 and 11 that the isothermal bulk modulus increases at the constant temperature as pressure increases, whereas the isothermal bulk modulus decreases at the constant pressure with the increase of temperature. In Figs. 12 and 13, our calculated results for $C_V$ and $C_P$ each as a function of temperature are illustrated for CoMnTe and RuMnTe compounds.

The specific heat capacity is closely related to the temperature dependence of fundamental thermodynamic functions, and it is the most important parameter for linking thermodynamics with dynamics and microscopic structure. It is clear that when the temperature is below 650 K, the $C_V$ and $C_P$ variations are very close together exhibiting strong dependence on temperature due to the anharmonic approximation used in this scheme of calculations. While at high temperatures, the $C_V$ approaches to a constant value ($\approx75\ \mathrm{J{\cdot}mol^{-1}{\cdot}K^{-1}}$), obeying Dulong and Petit's rule, which is followed by all solids at high temperatures, owing to the suppression of the anharmonic effect.$^{[29]}$ It is remarkable that the specific heat capacity at constant pressure $C_P$ increases monotonically with the increase of temperature.

Many physical properties of solids are closely related to the Debye temperature ($\theta$) and Grüneisen parameter ($\gamma$).
The variations of the results of these parameters are shown in Table 3. It is found that the Debye temperature increases with increasing pressure whereas the Grüneisen parameter decreases when the temperature is kept constant. However, at the constant pressure, the Debye temperature decreases and the Grüneisen parameter increases as the temperature increases.

<table>
<caption>Table 3. Calculated values of Debye temperature $\theta$(K) and Grüneisen parameter ($\gamma$) of CoMnTe and RuMnTe at various pressures and temperatures.</caption>
<thead>
<tr>
<th>$T$/K</th>
<th></th>
<th>$P$/GPa</th>
<th>0</th>
<th>15</th>
<th>30</th>
<th>45</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">300</td>
<td rowspan="2">RuMnTe</td>
<td>$\theta$</td>
<td>363.91</td>
<td>461.66</td>
<td>525.79</td>
<td>574.97</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>2.79</td>
<td>2.14</td>
<td>1.82</td>
<td>1.63</td>
</tr>
<tr>
<td rowspan="2">CoMnTe</td>
<td>$\theta$</td>
<td>365.83</td>
<td>477.93</td>
<td>558.28</td>
<td>622.18</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>2.71</td>
<td>2.41</td>
<td>2.20</td>
<td>2.04</td>
</tr>
<tr>
<td rowspan="4">600</td>
<td rowspan="2">RuMnTe</td>
<td>$\theta$</td>
<td>347.22</td>
<td>454.15</td>
<td>520.93</td>
<td>571.43</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>2.93</td>
<td>2.18</td>
<td>1.84</td>
<td>1.64</td>
</tr>
<tr>
<td rowspan="2">CoMnTe</td>
<td>$\theta$</td>
<td>347.66</td>
<td>466.32</td>
<td>549.94</td>
<td>615.63</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>2.76</td>
<td>2.44</td>
<td>2.22</td>
<td>2.06</td>
</tr>
<tr>
<td rowspan="4">900</td>
<td rowspan="2">RuMnTe</td>
<td>$\theta$</td>
<td>326.05</td>
<td>445.82</td>
<td>515.80</td>
<td>567.68</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>3.12</td>
<td>2.22</td>
<td>1.87</td>
<td>1.65</td>
</tr>
<tr>
<td rowspan="2">CoMnTe</td>
<td>$\theta$</td>
<td>327.58</td>
<td>453.80</td>
<td>540.85</td>
<td>608.51</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>2.80</td>
<td>2.48</td>
<td>2.24</td>
<td>2.08</td>
</tr>
<tr>
<td rowspan="4">1200</td>
<td rowspan="2">RuMnTe</td>
<td>$\theta$</td>
<td>297.80</td>
<td>436.65</td>
<td>510.09</td>
<td>563.78</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>3.39</td>
<td>2.28</td>
<td>1.89</td>
<td>1.67</td>
</tr>
<tr>
<td rowspan="2">CoMnTe</td>
<td>$\theta$</td>
<td>305.63</td>
<td>440.27</td>
<td>531.38</td>
<td>601.06</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>2.86</td>
<td>2.51</td>
<td>2.27</td>
<td>2.09</td>
</tr>
</tbody>
</table>

![](./images/814710165671510017_10.jpg)

Fig. 10. (color online) Curves of bulk modulus versus temperature at different pressures for RuMnTe and CoMnTe.

![](./images/814710165671510017_11.jpg)

Fig. 11. (color online) Curves of bulk modulus versus pressure at different temperatures for RuMnTe and CoMnTe.

![](./images/814710165671510017_12.jpg)

Fig. 12. (color online) Variations of specific heat capacity $C_V$ with temperature at various pressures for the half-Heusler alloys RuMnTe and CoMnTe.

![](./images/814710165671510017_13.jpg)

Fig. 13. (color online) Variations of specific heat capacity $C_P$ with temperature at various pressures for the half-Heusler alloys RuMnTe and CoMnTe.

![](./images/814710165671510017_14.jpg)

Fig. 14. (color online) Variations of calculated values of thermal expansion $\alpha$ with temperature at various pressures for half-Heusler alloys RuMnTe and CoMnTe.

The volume thermal expansion coefficient ($\alpha$) reflects the temperature dependence of volume at constant pressure:

$$
\alpha = \frac{1}{V} \left( \frac{\partial V}{\partial T} \right)_p.
$$

Figure 14 shows the variations of the thermal expansion coefficient with temperature at different pressures. From this figure, we can see that the thermal expansion increases sharply with temperature going up to 300 K then slowly for temperature higher than 300 K, and gradually turns into a linear increase. At a fixed temperature, the higher the pressure the smaller the thermal expansion coefficient is, indicating that high pressure suppresses thermal expansion. At zero pressure and 300 K, the values of the thermal expansion $\alpha$ for RuMnTe and CoMnTe are $4.89 \times 10^{-5}\ \text{K}^{-1}$ and $5.71 \times 10^{-5}\ \text{K}^{-1}$, respectively.

## 6. Conclusions

First-principles DFT studies related to CoMnTe and RuMnTe are performed. Our studies confirm that these compounds are half-metallic ferromagnetic materials. It is found that these materials behave as metals for the majority spin bands and exhibit semiconducting characteristics for minority spin bands. The origin of the band gap is traced out in the strong hybridization between the d states of higher valent TM atoms and lower valent TM atoms. The role of the elements containing sp states is crucial in tuning several physical properties of half-Heusler compounds and structural stability of $C1_b$ compounds. Our calculated values of the total magnetic moment $\mu_{\text{tot}}$ are $4\ \mu_{\text{B}}$ and $3\ \mu_{\text{B}}$ per unit cell for CoMnTe and RuMnTe, respectively, and most of it is contributed from the Mn atom. The total spin moment scale is accurately in agreement with the total number of valence electrons cotained by the atoms of these compounds. The calculated value of $\mu_{\text{tot}}$ is in line with the rule of $\mu_{\text{tot}} = Z_{\text{t}} - 18$. The effect of the unit cell volume is found to be decisive for the magnetic properties and the half-metallicity characteristics. Finally, the thermodynamic properties including the isothermal bulk modulus, heat capacity, Debye temperature, and the thermal expansion coefficients of the half-Heusler CoMnTe and RuMnTe compounds are investigated using the quasi-harmonic Debye model. The observed variations accord well with the results of the Debye theory, which is regularly applied to several materials.

## Acknowledgments

The authors (Khenata and Bin-Omran) acknowledge the financial support provided by the Deanship of Scientific Research at King Saud University for funding this work through research group project No: RPG-VPP-088.

## References

[1] Heusler F 1903 *Verh. Dtsch. Phys. Ges.* **5** 219
[2] de Groot R A, Mueller F M, van Engen P G and Buschow K H J 1984 *Appl. Phys.* **55** 2151
[3] Galanaki I an Dederich P H 2005 *J. Phys.: Condens. Matter* **676** 1
[4] Endo K, Phayama T and Kitamura R 1964 *J. Phys. Soc. Jpn.* **19** 1494
[5] Kubler J 1984 *Physica B* **127** 257
[6] Dunlap R, Stroink G and Dini K 1986 *J. Phys. F: Met. Phys.* **16** 1083

087103-7

[7] Zukovski W, Andrejezuk A, Dobrzyeski L, Cooper M J, Dixon M A G, Gardelis S, Lawson P K, Buslaps T, Kaprzyk S, Neumann K U and Ziebeck K R 1997 *J. Phys.: Condens. Matter* **9** 10993

[8] Worgull J, Petti E and Trivisonno J 1996 *Phys. Rev. B* **54** 15695

[9] Plogmann S, Schlatholter T, Braun J and Neumann M 1999 *Phys. Rev. B* **60** 6428

[10] Ishada S, Ishada J, Asano S and Yamashita J 1978 *J. Phys. Soc. Jpn.* **45** 1239

[11] Kubler J, Williams A R and Sommers C B 1983 *Phys. Rev. B* **28** 1745

[12] Fujii S, Ishida S and Asano S 1989 *J. Phys. Soc. Jpn.* **58** 3657

[13] Webster P J and Ziebeck K R A 1973 *J. Phys. Chem. Solids* **34** 1647

[14] Aquela A A, Enkovaara J, Uliakko K and Nieminen R E 1999 *J. Phys.: Condens. Matter* **11** 2017

[15] Deb A and Sakurai Y 2000 *J. Phys.: Condens. Matter* **12** 2997

[16] Kakeshita K and Ullakko K 2002 *MRS Bulletin* **27** 105

[17] Mullner R, Chermenko V A and Kostorz G 2003 *Ser. Mater.* **49** 129

[18] Chernenko V A, L'vov V A, Mullner R, Kostorz G and Takagi T 2004 *Phys. Rev. B* **69** 134410

[19] Kulkova S E, Eremeev S V and Kulkov S S 2004 *Solid State Commun.* **130** 793

[20] Kulkova S E, Eremeev S V, Kakeshita T, Kulkov S S and Rudenski G E 2006 *Mater. Trans.* **47** 599

[21] de Groot R A, van der Kraan A M and Buschow K H J 1986 *J. Magn. Magn. Mater.* **61** 330

[22] Blaha P, Schwarz K, Sorantin P and Trickey S B 1990 *Comput. Phys. Commun.* **59** 399

[23] Wong K M, Alay-e-Abbas S M, Fang Y, Shaukat A and Lei Y 2013 *J. Appl. Phys.* **114** 034901

[24] Blonco M A, Francisco E and Luaña V 2004 *Comput. Phys. Commun.* **158** 57

[25] Blonco M A, Pendás A M, Francisco E, Recio J M and Franco R 1996 *J. Mol. Struct. Theochem* **368** 245

[26] Francisco E, Blonco M A and Sanjurjo G 2001 *Phys. Rev. B* **63** 049107

[27] Merabiha O, Seddik T, Khenata R, Murtaza G, Bouhemadou A, Tak-agiwa Y, Bin Omran S and Rached D 2014 *J. Alloys Compd.* **586** 529

[28] Bouhemadou A, Khenata R and Amrani B 2009 *Physica B* **404** 3534

[29] Peng F, Fu H and Yang X 2008 *Physica B* **403** 2851

[30] Selçuk Kervan and Nazmiye Kervan 2014 *Intermetallics* **46** 45

[31] Lin S Y, Yang X B and Zhao Y J 2014 *J. Magn. Magn. Mater.* **350** 119

[32] Murnaghan F D 1944 *Proc. Natl. Acad. Sci. USA* **30** 244

[33] Otto M J, van Woerden R A M, van der Valk P J, Wijngaard J, van Bruggen C F, Haas C and Buschow K H J 1989 *J. Phys.: Condens. Matter* **1** 2341

[34] de Groot R A, Mueller F M, van Engen P G and Buschow K H J 1983 *Phys. Rev. Lett.* **50** 2024

[35] Galanakis I, Dederichs P H and Papanikolaou N 2002 *Phys. Rev. B* **66** 134428

[36] Galanakis I, Dederichs P H and Papanikolaou N 2002 *Phys. Rev. B* **66** 174429

[37] Ishida S, Fujii S, Kashiwagi S and Asano S 1995 *J. Phys. Soc. Jpn.* **64** 2152

[38] Fujii S, Ishida S and Asano S 1995 *J. Phys. Soc. Jpn.* **64** 185

[39] Zhang M, Liu Z H, Hu H N, Liu G D, Cui Y T, Wu G H, Brek R, de Boer F R and Li Y X 2004 *J. Appl. Phys.* **95** 7219

[40] Nanda B R K and Dasgupta I 2003 *J. Phys.: Condens. Matter* **15** 7307

[41] Jung D, Koo H J and Whangbo M J 2000 *J. Mol. Struct. Theochem* **527** 113

[42] Zhang M, Dai X, Hu H, Lui G, Cui Y, Chen J, Wang J and Wu G 2003 *J. Phys.: Condens. Matter* **15** 7891