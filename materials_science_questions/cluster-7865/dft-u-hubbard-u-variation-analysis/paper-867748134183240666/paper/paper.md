# Dilute magnetic semiconductor and half-metal behaviors in $3d$ transition-metal doped black and blue phosphorenes: a first-principles study

Weiyang Yu, $^{1,2}$ Zhili Zhu, $^{1}$ Chun-Yao Niu, $^{1}$ Chong Li, $^{1}$ Jun-Hyung Cho, $^{3,1, *}$ and Yu Jia $^{1, \dagger}$

$^{1}$ International Laboratory for Quantum Functional Materials of Henan, and School of Physics and Engineering, Zhengzhou University, Zhengzhou, 450001, China
$^{2}$ School of Physics and Chemistry, Henan Polytechnic University, Jiaozuo, 454000, China
$^{3}$ Department of Physics and Research Institute for Natural Sciences, Hanyang University, 17 Haengdang-Dong, Seongdong-Ku, Seoul 133-791, Korea
(Dated: July 26, 2021)

## Abstract
We present first-principles density-functional calculations for the structural, electronic, and magnetic properties of substitutional $3d$ transition metal (TM) impurities in two-dimensional black and blue phosphorenes. We find that the magnetic properties of such substitutional impurities can be understood in terms of a simple model based on the Hund's rule. The TM-doped black phosphorenes with Ti, V, Cr, Mn, Fe and Ni impurities show dilute magnetic semiconductor (DMS) properties while those with Sc and Co impurities show nonmagnetic properties. On the other hand, the TM-doped blue phosphorenes with V, Cr, Mn and Fe impurities show DMS properties, those with Ti and Ni impurities show half-metal properties, whereas Sc and Co doped systems show nonmagnetic properties. We identify two different regimes depending on the occupation of the hybridized electronic states of TM and phosphorous atoms: (i) bonding states are completely empty or filled for Sc- and Co-doped black and blue phosphorenes, leading to non-magnetic; (ii) non-bonding $d$ states are partially occupied for Ti-, V-, Cr-, Mn-, Fe- and Ni-doped black and blue phosphorenes, giving rise to large and localized spin moments. These results provide a new route for the potential applications of dilute magnetic semiconductor and half-metal in spintronic devices by employing black and blue phosphorenes.

**Keywords:** Dilute magnetic semiconductor, half-metal, transition metal doping, phosphorene

PACS numbers: 73.22.-f, 75.50.Pp, 75.75.+a

## 1. Introduction
Two-dimensional (2D) materials, graphene and silicene, are currently the subject of intense theoretical and experimental research especially for their novel electronic device applications. $^{1,2}$ Graphene and silicene have demonstrated many exquisite phenomena originating from the characteristic conical dispersion and chiral behavior of their valence and conduction bands around the Fermi level. $^{3-5}$ Generally speaking, the nanostructures of graphene and silicene such as nanoribbons, nanotubes and their interconnections have opened new routes for experimental and theoretical studies in the field of nanoelectronics. $^{6}$ Very recently, black phosphorene, a single layer of black phosphorus (BP) was successfully fabricated through exfoliation from the bulk black phosphorus, $^{7}$ and therefore becomes, besides graphene and silicene, another stable elemental 2D material. The black phosphorene presents some advantages superior to other previously studied 2D semiconductors because of its intriguing electronic properties, thereby drawing enormous interest from the society of materials science. $^{8-14}$ Recently, Li et $al^{15}$ reported that black phosphorene could be applied to the channel of the field effect transistor (FET) device that has a high carrier mobility of $\sim 10^{3} \mathrm{cm}^{2}/\mathrm{V} \cdot \mathrm{s}$ and an on/off ratio of $\sim 10^{4}$ at room temperature. As the allotrope of black phosphorene, blue phosphorene has the same stability as black phosphorene at room temperature, and its band gap is larger than black phosphorene $^{16}$. These good electronic properties of black and blue phosphorene nanosheets can be useful for the development of future nanoelectronic devices, spintronics, and related applications. $^{17-25}$

For the design of practical electronic devices, defects and impurities have been employed to tune the electrical, optical, and other properties. Over the last decades the resulting of dilute magnetic semiconductors (DMS) and half-metals have achieved important developments, $^{26-35}$ both in fundamental aspects and prospective technological applications. Indeed, it was possible to understand the underlying mechanisms of interaction between dilute magnetic impurities allowing ferromagnetic semiconductors at room temperature. $^{32,33}$ For prospective applications, the integration between 2D semiconductors and magnetic data storage enables the development of two-dimensional spintronics devices such as spin valve, spin-based transistors, non-volatile magnetoresistive memories and even magnetically enhanced optoelectronics devices. $^{36}$

Meanwhile, in spite of the success of 2D materials such as graphene, silicene, $^{37}$ transition metal dichalcogenides (TMDCs) $^{38,39}$ and black phosphorene $^{18,40,41}$, there has been rare study on the dilute magnetic characters of doped 2D black phosphorene except the work of Hashmi et $al^{42}$ and Sui et $al^{43}$, while half-metal properties in doped blue phosphorene have remained unexplored so far. From a technical point of view, 2D semiconductors have other superior factors that can be exploited in magnetic or spintronic devices. First, the carrier concentra-

tion can be externally controlled by voltage gating. Sec- ondly, there is room to improve the control of the impu- rity concentration, for example, by employing adatoms as impurities with concentrations above the solubility limit. In practice, studies of magnetic semiconductor nanos- tructures with lower dimensionalities, including semicon- ductor nanocrystals and nanowires $^{31,44-46}$ doped with transition metals (TM), demonstrated that the confine- ment effect and the improved control of magnetic dopantscan be used to increase the Curie temperature. $^{47,48}$

In this work, we focus on substitutional $3 d$ TM im purities (from Sc to Ni) in black and blue phosphorenes to investigate their dilute magnetic characters and half- metal properties. Using first-principles density functional theory (DFT) calculations, we study the structural, elec- tronic, and magnetic properties of substitutional $3 d$ TM impurities in black and blue phosphorenes. One of our key results is that the electronic and magnetic properties of these substitutional impurities can be understood by a simple model based on the hybridization between theTM $d$ orbitals and the defect (i.e., phosphorous vacancy) levels. This model together with the calculated band structure provides an explanation for the non-trivial be- haviors of the binding energy and the spin moments for all the systems considered. Concisely, we distinguish two different regimes that depend on the electron filling of TM-phosphorous hybridized levels: (i) completely unoc- cupied (occupied) bonding states for Sc (Co) lead to non- magnetic; (ii) partially occupied non-bonding $d$ shell for Ti, V, Cr, Mn, Fe and Ni give rise to large and localized spin moments.

This paper is organized as follows. After a brief de- scription of the computational details in section 2, we present the geometry structures, binding energies and magnetic properties of all the substitutional TM impuri- ties studied in section 3. We also present the general ideas behind our model of the metal-phosphorus hybridization in the considered systems. In section 4, the electronic structure of the unreconstructed $D_{3 h}$ phosphorus vacancy in pristine phosphorene, along with the electronic struc- ture of the different groups of impurities are presented. Finally, we give a summary with some general conclu- sions.

### 2. Computational Details
The present DFT calculations were performed using the Vienna $a b$ initio Simulation Package (VASP) code with a plane-wave basis set. $^{49,50}$ Projector augmented wave (PAW) potentials $^{51}$ were used to describe the core electrons and the generalized gradient approximation(GGA) of Perdew, Burke and Ernzernhof (PBE) $^{52}$ was adopted for exchange-correlation energy. To examine the reliability of the PBE method on the magnetic proper- ties of the black and blue phosphorenes containing $3 d$ TM impurity atoms, we also considered the effect of the on-site Coulomb interaction $U$ on the magnetic prop erty within the PBE $+U$ method. $^{53}$ A kinetic energycutoff of the plane-wave basis set was used to be 500 eV and for the structural optimization, convergence of

![](./images/867748134183240666_1.jpg)

FIG. 1: (a) Top and side views of a diamond-like $2 \times 2$ super cell of black phosphorene used in the present calculations. (b) Top and side views of blue phosphorene. (c) Spin density of black phosphorene containing a vacancy with an isosurface of0.005 e/Å³.

Hellmann-Feynman residual forces less than 0.01 eV/Å per atom was achieved. Because the convergence with respect to the number of $k$-points was especially criti cal to obtain accurate results for the spin moment in the systems studied, we used an adequate number of $k$- points for all the different supercell sizes, equivalent to $9 \times 9 \times 1$ Monkhorst-Pack $^{54}$ sampling. The Fermi level wassmeared by the Gaussian method with a width of 0.05

![](./images/867748134183240666_2.jpg)

FIG. 2: (a), (b) Structural parameters and binding energies (c) of the substitutional TM-doped black phosphorenes. The corresponding ones of the substitutional TM-doped blue phosphorenes are given in (d), (e), and (f).

eV. Most of our results were obtained using 2×2/4×4 crystallographic symmetrical supercells of black and blue phosphorenes, with a doping concentration of 3.13%, as shown in Fig. 1(a) and (b). We also checked the results by performing calculations using larger supercells up to 4×4/6×6 [concentration of 1.56(1.39)%] for several ele- ments. In order to avoid spurious interactions between periodic images of the defective phosphorene layer, a vac- uum spacing perpendicular to the plane was employed to be larger than $\sim 15 \AA$.

3. Structural, energetic, and magnetic proper- ties of TM doped in black and blue phosphorenes

In this section we provide our results for the geome- tries, binding energies, and spin moments of substitu- tional TMs in black and blue phosphorenes.

3.1 Geometrical parameters and binding ener- gies

The typical structure of the systems studied in this paper is presented in Fig. 1. Fig. 1(a) shows the diamond-like 2×2 supercell structure of monolayer black phosphorene, with a doping concentration of 3.13%. In view of symmetry and doping isotropy, the diamond- shape unit cell was employed instead of the rectan- gle unit cell. As shown in Fig. 1(a), the op- timized lattice constants are $a_{1}=3.310 \AA$, $a_{2}=4.589 \AA$, and $a_{1}'=a_{2}'=(a_{1}^{2}+a_{2}^{2})^{1/2}=5.658 \AA$, and the angle between the basis vectors $a_{1}'$ and $a_{2}'$ is $71.89^{\circ}$. These values are consistent with experiment $^{55}$ and other theoreti cal calculations $^{56}$ . Fig. 1(b) displays the optimized structure of the blue phosphorene with lattice constants $a_{1}''=a_{2}''=3.330 \AA$, and their angle $\theta'=60^{\circ}$, which are in good agreement with previous DFT calculations $^{16}$ .

We begin to study a pure black phosphorene with a monovacancy. Fig. 1(c) shows the spin density of black phosphorene with a monovacancy. Similar to the results reported by Ma et $al^{57}$ , the phosphorus atoms around the vacancy undergo a Jahn-Teller distortion, and two of the phosphorus atoms close to the vacancy site move towards each other to form a P-P distance of $1.832 \AA$, which is $0.408 \AA$ smaller than that of the intrinsic phosphorene. The ground state of the system has a magnetic moment of $1.00 \mu_{B} /$ unit cell, most of which is concentrated at the two P atoms with the unsaturated bonds, as seen in Fig.1(c).

The structural parameters and energetic properties of the substitutional TMs in black and blue phosphorenes are shown in Fig. 2. For TM-doped black phosphorene, the bond angles $\theta_{1}$ and $\theta_{2}$ monotonically increase from Sc to Ni [see Fig. 2(b)]. Meanwhile, the bond lengths $d_{1}$ and $d_{2}$ decrease for Sc-, Ti-, and V-doped systems and increase for Cr-doped system, and then decrease again for Mn-, Fe-, and Co-doped systems, and then increase for

![](./images/867748134183240666_3.jpg)

FIG. 3: (a) Spin moments of the isolated TMs and their substitutions in black and blue phosphorenes as a function of the number of valence electrons (Slater-Pauling-type plot). Schematic diagram of spin moment in doped black phosphorene (b) and blue phosphorene (c) in terms of Hund's rule, respectively.

<table>
<caption>TABLE I: Electronic charges of each atomic species in the TM-doped black and blue phosphorenes, obtained using Bader charge analysis. The positive (negative) sign represents the gained (lost) electrons.</caption>
<tbody><tr><th colspan="2">Atoms</th><td>Sc</td><td>Ti</td><td>V</td><td>Cr</td><td>Mn</td><td>Fe</td><td>Co</td><td>Ni</td></tr>
<tr><th rowspan="2">black-P</th><th>TM</th><td>-1.54</td><td>-1.23</td><td>-0.97</td><td>-0.87</td><td>-0.61</td><td>-0.37</td><td>-0.19</td><td>-0.16</td></tr>
<tr><th>Nearest-P</th><td>+0.97</td><td>+0.78</td><td>+0.59</td><td>+0.59</td><td>+0.33</td><td>+0.12</td><td>0.00</td><td>+0.07</td></tr>
<tr><th rowspan="2">blue-P</th><th>TM</th><td>-1.55</td><td>-1.27</td><td>-1.05</td><td>-0.88</td><td>-0.57</td><td>-0.40</td><td>-0.21</td><td>-0.20</td></tr>
<tr><th>Nearest-P</th><td>+0.32</td><td>+0.27</td><td>+0.26</td><td>+0.20</td><td>+0.12</td><td>+0.07</td><td>0.00</td><td>+0.02</td></tr>
</tbody>
</table>

Ni-doped system [see Fig. 2(a)]. These behaviors of the bond lengths and bond angles reflect the size of the TM atoms. As for TM-doped blue phosphorene, the bond length $d_3$ decreases from Sc to Mn and then increases from Mn to Ni [see Fig. 2(d)], while the band angle $\theta_3$ shows an oscillating behavior [see Fig. 2(e)].

Figure 2(c) shows the calculated binding energies ($E_b$) of the TM-doped black phosphorenes, where $E_b$ is defined as -($E_{total}$-$E_{phosphorene}$-$E_{atom}$). Here, $E_{total}$ is the energy of the whole configuration, $E_{phosphorene}$ is the energy of the phosphorene with a vacancy and $E_{atom}$ represents the energy of an isolated dopant atom. We find a continuous increase of the binding energy from Sc to Cr, and then decrease from Mn to Ni, and the binding energies for the considered TMs are in the range of 0.375-5.466 eV. Interestingly, Cr-doped system has the maximum binding energy. This peculiar behavior is related with the interplay between the energy down-shift and the compression of the $3d$ shell of the TM as the atomic number increases. Although this explanation will be more clear when the metal-phosphorus hybridization levels are discussed below, we note that the behavior of the binding energies of the substitutional $3d$ TM arises from two competing effects:

(i) From Sc to Cr, the decrease of $d_1$ and $d_2$ reflects an increase in the bonding strength between the TM and phosphorous atoms, and (ii) From Mn to Ni, as the $3d$ shell is occupied, its hybridization with the phosphorous vacancy states is weakened to decrease the binding energy.

It is noticeable that this trend of the energetics for the TM-doped black phosphorenes is very similar to that for the TM-doped blue phosphorenes [see Fig. 2(f)].

### 3.2 Spin moments

The spin moments of substitutional TMs in black and blue phosphorenes are displayed in Fig. 3(a), together with those of the isolated TM atoms. We find that the spin moments of the isolated TM atoms are 1, 3, 5, 6, 5, 4, 3, and 1 $\mu_B$ from Sc to Ni, respectively. On the other hand, the TM-substituted black phosphorenes have the zero magnetic moment for Sc and Co, but 1, 2, 3, 2, 1, and 1 $\mu_B$ for Ti, V, Cr, Mn, Fe, and Ni, respectively, which are the same as the corresponding cases in blue phosphorene. For both of the TM-substituted black and blue phosphorenes, we analyze the charge transfer using Bader charge (see Table I). We find that for both cases, the TM atoms lose electron charges while the nearest phosphorous atoms gain electron charges. It is notable that the magnitudes of gained and lost charges decrease as the atomic number increases.

Interestingly, as shown in Fig. 3(a), the total spin moments have the integer values of 0, 1, 2, 3, 2, 1, 0, and 1 $\mu_B$ for Sc-, Ti-, V-, Cr-, Mn-, Fe-, Co-, and Ni-doped black and blue phosphorenes, respectively.

According to a recent first-principles study of substitutional TM impurities in graphene, $^{58}$ the spin moments are calculated to be 0, 0, 1, 2, 3, 2, 1, and 1 $\mu_B$ for Sc-, Ti-, V-, Cr-, Mn-, Fe-, Co-, and Ni-doped graphene systems, respectively. These values are well compared with 0, 1, 2, 3, 2, 1, 0, and 1 $\mu_B$ for Sc-, Ti-, V-, Cr-, Mn-, Fe-, Co-, and Ni-doped black and blue phosphorenes, respectively. It is interesting to note that the spin moment of each TM impurity (except Sc and Ni) in graphene is smaller by 1 $\mu_B$ compared to the corresponding one in black and blue phosphorenes. This may be attributed to the different bonding natures of graphene and phosphorene: i.e., $sp^2$ bonding in graphene and $sp^3$ bonding in phosphorene. Since one valence electron of TM impurities in graphene

<table>
<caption>TABLE II: Spin moments in the TM impurity ($S_M$) and the nearest phosphorus neighbors ($S_{P1}$ and $S_{P2}$) for different substitutional TMs in black and blue phosphorenes, together with the spin moments of the isolated TM atoms ($S_{iso-atom}$). $S_{tot}$ is the total spin moment of the doped black and blue phosphorenes. The band gaps ($E_g$) of TM-doped black (blue) phosphorenes are also given. The values in parentheses are the PBE + $U$ band gaps.</caption>
<tbody>
<tr>
<td></td>
<td>Doped-atom</td>
<td>$S_M$ ($\mu_B$)</td>
<td>$S_{P1}$ ($\mu_B$)</td>
<td>$S_{P2}$ ($\mu_B$)</td>
<td>$S_{tot}$ ($\mu_B$)</td>
<td>$S_{iso-atom}$ ($\mu_B$)</td>
<td>$E_g$ (eV)</td>
</tr>
<tr>
<td rowspan="8">black-P</td>
<td>Sc</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0.97 (1.36)</td>
</tr>
<tr>
<td>Ti</td>
<td>0.986</td>
<td>-0.014</td>
<td>-0.017</td>
<td>1.00</td>
<td>3.00</td>
<td>0.36 (0.90)</td>
</tr>
<tr>
<td>V</td>
<td>1.977</td>
<td>-0.001</td>
<td>-0.002</td>
<td>2.00</td>
<td>5.00</td>
<td>0.07 (0.09)</td>
</tr>
<tr>
<td>Cr</td>
<td>3.082</td>
<td>-0.076</td>
<td>-0.085</td>
<td>3.00</td>
<td>6.00</td>
<td>0.72 (0.93)</td>
</tr>
<tr>
<td>Mn</td>
<td>2.207</td>
<td>-0.053</td>
<td>-0.060</td>
<td>2.00</td>
<td>5.00</td>
<td>0.39 (0.82)</td>
</tr>
<tr>
<td>Fe</td>
<td>1.097</td>
<td>-0.036</td>
<td>-0.019</td>
<td>1.00</td>
<td>4.00</td>
<td>0.27 (0.90)</td>
</tr>
<tr>
<td>Co</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0.61 (1.08)</td>
</tr>
<tr>
<td>Ni</td>
<td>0.953</td>
<td>0.064</td>
<td>-0.007</td>
<td>1.00</td>
<td>1.00</td>
<td>0.09 (0.46)</td>
</tr>
<tr>
<td rowspan="8">blue-P</td>
<td>Sc</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>1.35 (1.59)</td>
</tr>
<tr>
<td>Ti</td>
<td>0.992</td>
<td>-0.020</td>
<td>-0.020</td>
<td>1.00</td>
<td></td>
<td>0 (0.73)</td>
</tr>
<tr>
<td>V</td>
<td>2.032</td>
<td>-0.055</td>
<td>-0.055</td>
<td>2.00</td>
<td></td>
<td>0.15 (0.47)</td>
</tr>
<tr>
<td>Cr</td>
<td>3.147</td>
<td>-0.083</td>
<td>-0.083</td>
<td>3.00</td>
<td></td>
<td>0.91 (1.63)</td>
</tr>
<tr>
<td>Mn</td>
<td>1.954</td>
<td>-0.032</td>
<td>-0.020</td>
<td>2.00</td>
<td></td>
<td>0.12 (0.73)</td>
</tr>
<tr>
<td>Fe</td>
<td>1.247</td>
<td>-0.044</td>
<td>-0.044</td>
<td>1.00</td>
<td></td>
<td>0.35 (0.91)</td>
</tr>
<tr>
<td>Co</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0.69 (1.12)</td>
</tr>
<tr>
<td>Ni</td>
<td>0.967</td>
<td>0.039</td>
<td>0.039</td>
<td>1.00</td>
<td></td>
<td>0 (0)</td>
</tr>
</tbody>
</table>

participates in $\pi$ bonding with neighboring C atoms, the spin moment is likely to decrease by $1\ \mu_B$. To understand this deeply, we draw the schematic diagram of spin mo- ment according to Hund's rule in Fig. 3(b). We here note that the valence electron configurations of Sc, Ti, V, Cr, Mn, Fe, Co and Ni are $3d^14s^2$, $3d^24s^2$, $3d^34s^2$, $3d^54s^1$, $3d^54s^2$, $3d^64s^2$, $3d^74s^2$, $3d^84s^2$, respectively. Briefly, we can distinguish the several regimes depending on the fill- ing of electronic levels:

(i) Sc-doped black phosphorene have the empty Sc- phosphorous bonding levels, leading to a zero spin mo- ment.

(ii) Co-doped black phosphorene have fully occupied Co-phosphorous bonding levels, leading to a zero spin moment.

(iii) Ti-, V-, and Cr-doped black phosphorene have par- tially occupied TM-phosphorous bonding levels with the spin moments of 1.00, 2.00, and $3.00\ \mu_B$, respectively.

(iv) Mn-, Fe-, and Ni-doped black phosphorene have partially occupied non-bonding $3d$ levels with the spin moments of 2.00, 1.00, and $1.00\ \mu_B$.

It is notable that the spin moments of TM-doped blue phosphorene [see Fig. 3(c)] are the same as those of black phosphorene because the energy states of $s$ and $d$ in the outermost orbital of TM atoms and phosphorus atom are very close to each other.

To explore the underlying mechanism of the magnetic moments in TM-doped black and blue phosphorenes, the Mulliken population analysis was performed to list the results in Table II. We find that the spin moments of the TM impurities ($S_M$) have a dominant contribution for the nearest phosphorus neighbors ($S_{P1}$ and $S_{P2}$). The calculated spin moments of TM impurities for Ti, V, Cr, Mn, Fe and Ni in doped black phosphorene are $S_M =$ 0.986, 1.977, 3.082, 2.207, 1.097, and $0.953\ \mu_B$, respec- tively, close to the above-discussed Hund's analysis. Sim- ilarly, the spin moments of TM impurities for Ti, V, Cr, Mn, Fe and Ni in doped blue phosphorenes are $S_M =$ 0.992, 2.032, 3.147, 1.954, 1.247, and $0.967\ \mu_B$, respec- tively.

![](./images/867748134183240666_4.jpg)

FIG. 4: (color online). Band structure and density of states of the undoped defective black phosphorene. The red lines represent majority spin band, while the black lines represent minority spin band. The energy zero represents the Fermi level.

### 4. Analysis of the electronic structures
We first examine the electronic structure of a single phosphorous vacancy in black phosphorene. As substitu- tional impurities in black phosphorene, most of the TM atoms studied here exhibit a symmetrical configuration of $C_{2h}^3$. $^{59}$ For this reason, it is particularly instructive to analyze their electronic structures with the hybridization between the atomic levels of the TM atoms and those associated with a relaxed $C_{2h}^3$ symmetrical phosphorus

![](./images/867748134183240666_5.jpg)

FIG. 5: (color online). Band structures of Sc-, Ti-, V-, Cr-, Mn-, Fe-, Co- and Ni-doped black (a) and blue (b) phosphorenes, respectively. The red (black) lines represent the majority (minority) spin band. The energy zero represents the Fermi level.

![](./images/867748134183240666_6.jpg)

FIG. 6: (color online). Band structures of Ti-, Ni-doped blue phosphorenes obtained using the PBE + $U$ calculation with $U = 5.5$, $6.5$ eV, respectively. The red (black) lines represent the majority (minority) spin band. The energy zero represents the Fermi level.

vacancy. As shown in Fig. 4, the $C_{2h}^{3}$ vacancy shows a considerable spin polarization of $1.00\ \mu_{B}$, indicating a dilute magnetic property.

To further shed light on the underlying mechanism of magnetic properties in the TM-doped black and blue phosphorene structures, we plot the spin-polarized band structures of TM-doped black and blue phosphorenes in Fig. 5(a) and (b), respectively. Interestingly, the majority and minority spin bands for Ti-, V-, Cr-, Mn-, Fe-, and Ni-doped black phosphorene show semiconducting characters [see Fig. 5(a)], indicating dilute magnetic properties. On the other hand, Sc- and Co-doped black phosphorene exhibit zero spin moment, whereas Ti- and Ni-doped blue phosphorene show half-metal characters [see Fig. 5(b)]. Note that V-, Cr-, Mn-, and Fe-doped blue phosphorenes exhibit dilute semiconducting characters, while Sc- and Co-doped blue phosphorenes have zero spin moment.

In general, substitutional TM impurities in black and blue phosphorenes exhibit very similar behaviors in their energetic and magnetic properties. This result indicates that the structural differences of black- and blue-phosphorene lattices are insensitive to determine the energetic and magnetic properties of TM-doped black and blue phosphorenes, as shown in Fig. 2, 3, and 5.

It is interesting to examine the effect of the on-site Coulomb interaction $U$ on the magnetic properties of the substitutional $3d$ TM impurities in black and blue phosphorenes. We perform the PBE + $U$ calculations for all the considered systems, where the values of $U = 4.0, 5.5, 3.3, 3.5, 3.5, 4.3, 3.3$, and $6.5$ eV are chosen for Sc-, Ti-, V-, Cr-, Mn-, Fe-, Co-, and Ni-doped systems, respectively. $^{60-62}$ The calculated PBE + $U$ band gaps ($Eg$) of Sc-, Ti-, V-, Cr-, Mn-, Fe-, Co-, and Ni-doped black and blue phosphorenes are listed in Table II. We find that $Eg$ of the magnetic semiconductor obtained using PBE + $U$ increases by $\sim 30\%$ compared to the PBE results. However, it is noticeable that the spin moment does not change depending on the PBE and PBE + $U$ methods. Interestingly, we find that the PBE + $U$ band structure of Ti-doped blue phosphorene shows a magnetic semiconductor property with a gap opening (see Fig. 6), different from the half-metallic character predicted by PBE. This indicates that $U$ in Ti-doped blue phosphorene splits the narrow half-filled bands crossing the Fermi level into lower and upper Hubbard bands. On the other hand, the half-metallic character of Ni-doped blue phos-

![](./images/867748134183240666_7.jpg)

FIG. 7: (color online). Spin polarized total (upper panel) and partial (lower panel) density of states of Sc-, Ti-, V-, Cr-, Mn-, Fe-, Co- and Ni-doped black (a) and blue (b) phosphorenes, respectively. The energy zero represents the Fermi level.

phorene predicted by PBE is preserved in the PBE + $U$ band structure (see Fig. 6), because the bands crossing the Fermi level have relatively larger band widths com- pared to those in Ti-doped blue phosphorene [see Fig. 5(b)].

A general picture of the dilute magnetic and half-metal features of the TM-doped black and blue phosphorenes can be seen from the analysis of the spin-polarized total and partial DOS, as shown in Fig. 7. As for Sc- and Co- doped black phosphorenes, the total DOS of the major- ity and minority states are completely compensated with each other, yielding zero spin moment [see Fig. 7(a)]. It is found that for Ti-, V-, Cr-, Mn-, Fe- and Ni-doped black phosphorenes, the total DOS of the majority and minority states are not compensated below $E_F$ and show a gap opening, indicating dilute magnetic semiconduct- ing properties. We note that the DOS of Sc- and Co-doped blue phosphorene show nonmagnetic properties; those of Ti- and Ni-doped blue phosphorene show half- metal properties; V-, Cr-, Mn-, Fe-doped blue phospho- renes show dilute magnetic semiconductor characters [see Fig. 7(b)]. From the analysis of the spin-polarized total and partial DOS, it is seen that the magnetic moments are well localized at the TM atom site, and the $d_{xy}$ and $d_{x^2-y^2}$ orbitals are dominant for the contribution to the partial DOS.

### 5. Conclusions
We have performed a first-principles DFT calculation for the structural, energetic, and magnetic properties of a series of substitutional $3d$ TM impurities in black and blue phosphorenes. We provided a simple model based on Hund's rule for understanding the calculated electronic and magnetic properties of the considered systems, where the dilute-semiconducting and half-metal features, spin moment, and binding energy are varied depending on the atomic number of the TM atoms. The spin-polarized band structures and DOS calculations show that for black phosphorene, the Ti-, V-, Cr-, Mn-, Fe- and Ni-doped systems have dilute magnetic semiconductor properties, while Sc- and Co-doped systems have no magnetism. For blue phosphorene, the Ti- and Ni-doped systems show half-metal properties, while V-, Cr-, Mn- and Fe-doped systems show dilute magnetic semiconductor characters, Sc- and Co-doped systems show non-magnetism.

Since substitutional impurities of $3d$ TM atoms in black and blue phosphorenes exhibit some intriguing elec- tronic and magnetic properties, such doped systems can provide an interesting route to tune various functions for spin electronic devices based on black and blue phos- phorenes. This functional ability together with the high stability of substitutional impurities can open a route to fabricate ordered arrays of these impurities at predefined locations, which would allow the experimental tests of the theoretical predictions of unusual magnetic interactions mediated by black and blue phosphorenes.

### Acknowledgements
We thank Prof. Zhenyu Zhang for helpful discussions. This work was supported by the National Basic Research Program of China (Grant No. 2012CB921300), Na- tional Natural Science Foundation of China (Grant Nos.

11274280 and 11304288), and National Research Foun- dation of Korea (Grant No. 2015R1A2A2A01003248).

* e-mail address:chojh@hanyang.ac.kr
† e-mail address:jiayu@zzu.edu.cn

1 A. K. Geim and K. S. Novoselov, The rise of graphene, Nat. Mater, 2007, 6, 183.
2 A. H. Castro Neto, F. Guinea, N. M. Peres, K. S. Novoselov and A. K. Geim, The electronic properties of graphene, Rev. Mod. Phys., 2009, 81, 109.
3 K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. V. Grigorieva, S. V. Dubonos and A. A. Firsov, Two-dimensional gas of massless Dirac fermions in graphene, Nature, 2005, 438, 197.
4 M. I. Katsnelson, K. S. Novoselov and A. K. Geim, Chiral tunnelling and the Klein paradox in graphene, Nat. Phys., 2006, 2, 620.
5 C. Park, Y. W. Son, M. L. Cohen and S. G. Louie, Anisotropic behaviours of massless Dirac fermions in graphene under periodic potentials, Nat. Phys., 2008, 4, 213.
6 P. Avouris, Z. Chen and V. Perebeinos, Carbon-based elec- tronics, Nat. Nanotechnol., 2007, 2, 605.
7 E. S. Reich, Phosphorene excites materials scientists, Na- ture, 2014, 506, 19.
8 Z. L. Zhu, C. Li, W. Y. Yu, D. H. Chang, Q. Sun and Y. Jia, Magnetism of zigzag edge phosphorene nanoribbons, Appl. Phys. Lett., 2014, 105, 113105.
9 V. Tran, R. Sklaski, Y. F. Liang and L. Yang, Layer- controlled band gap and anisotropic excitons in few-layer black phosphorus, Phys. Rev. B: Condens. Matter Mater. Phys., 2014, 89, 235319.
10 R. X. Fei and L. Yang, Strain-engineering the anisotropic electrical conductance of few-Layer black phosphorus, Nano Lett., 2014, 14, 2884.
11 R. X. Fei and L. Yang, Lattice vibrational modes and Raman scattering spectra of strained phosphorene, Appl. Phys. Lett., 2014, 105, 083120.
12 V. Tranm and L. Yang, Unusual Scaling Laws of the Band Gap and Optical Absorption of Phosphorene Nanoribbons, Phys. Rev. B: Condens. Matter Mater. Phys., 2014, 89,245407.
13 Z. L. Zhu, W. Y. Yu, X. Y. Ren, Q. Sun and Y. Jia, Grain boundary in phosphorene and its unique roles on C and O doping, Europ. Lett., 2015, 109, 47003.
14 W. Y. Yu, Z. L. Zhu, C. Y. Niu, C. Li, J. H. Cho and Y. Jia, Anomalous doping effect in black phosphorene using first- principles calculations, Phys. Chem. Chem. Phys., 2015,17, 16351.
15 L. Li, Y. Yu, G. J. Ye, Q. Ge, X. Ou, H. Wu, D. Feng, X. H. Chen and Y. B. Zhang, Black phosphorus fieled-effect transistors, Nat. Nanotechnol., 2014, 9, 372.
16 Z. Zhu and D. Tomanek, Semiconducting layered blue phosphorus: A computational study, Phys. Rev. Lett.,2014, 112, 176802.
17 M. Buscema, D. J. Groenendijk, S. I. Blanter, G. A. Steele, H. S. J. Van der Zant and A. C. Gomez, Fast and broad- band photoresponse of few-layer black phosphorus field- effect transistors, Nano Lett., 2014, 14, 3347.
18 Y. Q. Cai, Q. Q. Ke, G. Zhang and Y. W. Zhang, Ener- getics, charge transfer, and magnetism of small molecules physisorbed on phosphorene, J. Phys. Chem. C, 2015, 119,3102.
19 V. V. Kulish, O. I. Malyi, C. Perssonc and P. Wu, Adsorp- tion of metal adatoms on single-layer phosphorene, Phys. Chem. Chem. Phys., 2015, 17, 992.
20 V. V. Kulish, O. I. Malyi, C. Persson and P. Wu, Phos- phorene as an anode material for Na-ion?batteries: a first- principles study, Phys. Chem. Chem. Phys., 2015, 17,13921.
21 D. W. Boukhvalov, A. N. Rudenko, D. A. Prishchenko, V. G. Mazurenko and M. I. Katsnelson, Chemical modi- fications and stability of phosphorene with impurities: a first principles study, Phys. Chem. Chem. Phys., 2015, 17,15209.
22 G. Z. Qin, Q.B. Yan, Z. Z. Qin, S. Y. Yue, M. Hu and G. Su, Anisotropic intrinsic lattice thermal conductivity of phosphorene from first principles, Phys. Chem. Chem. Phys., 2015, 17, 4854.
23 X. Liu, Y. W. Wen, Z. Z.Chen, B. Shan and R. Chen, A first-principles study of sodium adsorption and diffusion on phosphorene, Phys. Chem. Chem. Phys., 2015, 17, 16398.
24 H. L. Zheng, J. M. Zhang, B. S. Yang, X. B. Du and Y. Yan, A first-principles study on the magnetic properties of nonmetal atom doped phosphorene monolayers, Phys. Chem. Chem. Phys., 2015, 17, 16341.
25 J. Dai and X. C. Zeng, Structure and stability of two di- mensional phosphorene with =O or =NH functionaliza- tion, RSC Adu., 2014, 4, 48017.
26 T. Dielt, H. Ohno, F. Matsukura, J. Cibert and D. Ferrand, Zener model description of ferromagnetism in zinc-blende magnetic semiconductors, Science, 2000, 287, 1019.
27 H. Ohno, D. Chiba, F. Matsukura, T. Omiya, E. Abe, T. Dielt, Y. Ohno and K. Ohtani, Electric-field control of ferromagnetism, Nature, 2000, 408, 944.
28 H. Ohno, Making nonmagnetic semiconductors ferromag- netic, Science, 1998, 281, 951.
29 K. Sato, L. Bergqvist, J. Kudrnovsky, P. H. Dederichs, O. Eriksson, I. Turek, B. Sanyal, G. Bouzerar, H. Katayama- Yoshida, V. A. Dinh, T. Fukushima, H. Kizaki and R. Zeller, First-principles theory of dilute magnetic semicon- ductors, Rev. Mod. Phys., 2010, 82, 1633.
30 A. Zunger, S. Lany and H. Raebiger, Trend: The quest for dilute ferromagnetism in semiconductors: Guides and misguides by theory, Physics, 2010, 3, 53.
31 T. Dielt, A ten-year perspective on dilute magnetic semi- conductors and oxides, Nat. Mater., 2010, 9, 965.
32 Y. Matsumoto, M. Murakami, T. Shono, T. Hasegawa, T. Fukumura, M. Kawasaki, P. Ahmet, T. Chikyow, S. Koshi- hara, H. Koinuma, Room-temperature ferromagnetism in transparent transition metal-doped titanium dioxide, Sci- ence, 2001, 291, 854.
33 J. M. Coey, M. Venkatesan and C. B. Fitzgerald, Donor im- purity band exchange in dilute ferromagnetic oxides, Nat. Mater., 2005, 4, 173.
34 Z. L. Zhu, W. G. Chen, Q. Sun and Y. Jia, Half-metal be- haviour mediated by self-doping of topological line defect combining with adsorption of 3d transition-metal atomic chains in graphene, J. Phys. D: Appl. Phys., 2014, 47,

055303.

35 Y. Feng, W. X. Ji, B. J. Huang, X. L. Chen, F. Li, P. Li, C. W. Zhang and P. J. Wang, The magnetic and optical properties of $3d$ transition metal doped $SnO_2$ nanosheets, $RSC$ $Adv.$, 2015, 5, 24306.

36 I. Zutic, J. Fabian and S. Das Sarma, Spintronics: Fun- damentals and applications, Rev. Mod. Phys., 2004, 76, 323.

37 K. S. Novoselov, A, K. Geim, S. Morozov, D. Jiang, Y. Zhang, S. Dubonos, I. Grigorieva and A. Firsov, Electric field effect in atomically thin carbon films, Science, 2004, 306, 666.

38 K. Novoselov, D. Jiang, F. Schedin, T. Booth, V. Khotke- vich, S. Morozov and A. Geim, Two-dimensional atomic crystals, Proc. Natl. Acad. Sci. U.S.A., 2005, 102, 10451.

39 K. F. Mak, C. Lee, J. Hone, J. Shan and T. F. Heinz, Atomically thin MoS2: a new direct-gap semiconductor, Phys. Rev. Lett., 2010, 105, 136805.

40 T. Hu and J. S. Hong, First-principles ptudy of metal adatom adsorption on black phosphorene, J. Phys. Chem. C, 2015, 119, 8199.

41 I. Khan and J. S. Hong, Manipulation of magnetic state in phosphorene layer by non-magnetic impurity doping, New J. Phys., 2015, 17, 023056.

42 A. Hashmi and J. Hong, Transition metal doped phospho- rene: first-Principles study, J. Phys. Chem. C, 2015, 119, 9198.

43 X. L. Sui, C. Si, B. Shao, X. L. Zou, J. Wu, B. L. Gu and W. H. Duan, Tunable magnetism in transition-metal- decorated phosphorene, J. Phys. Chem. C, 2015, 119, 10059.

44 K. R. Kittilstved and D. R. Gamelin, Activation of high- Tc ferromagnetism in $Mn^{2+}$-doped ZnO using amines, J. Am. Chem. Soc., 2005, 127, 5292.

45 Y. Rao, H. Xu, Y. Liang and S. Hark, Synthesis, micro- structural and magnetic properties of Mn-doped ZnO nanowires, Cryst. Eng. Comm., 2011, 13, 2566.

46 J. H. Park, M. G. Kim, H. M. Jang, S. Ryu and Y. M. Kim, Co-metal clustering as the origin of ferromagnetism in Co-doped ZnO thin films, Appl. Phys. Lett., 2004, 84, 1338.

47 L. Seixas, A. Carvalho, A. H. Castro Neto, Atomically thin dilute magnetism in Co-doped phosphorene, Phys. Rev. B: Condens. Matter Mater. Phys., 2015, 91, 155138.

48 A. Ramasubramaniam and D. Naveh, Mn-doped mono- layer $MoS_2$: an atomically thin dilute magnetic semicon- ductor, Phys. Rev. B: Condens. Matter Mater. Phys., 2013, 87, 195201.

49 G. Kresse and J. Furthmller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 1996, 6, 15.

50 G. Kresse and J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B: Condens. Matter Mater. Phys., 1993, 48, 13115.

51 P. E. Blochl, Projector augmented-wave method, Phys. Rev. B: Condens. Matter Mater. Phys., 1994, 50, 17953.

52 J. P. Perdew, K. Burke and M. Ernzerhof, Generalized gra- dient approximation made simple, Phys. Rev. Lett., 1996, 77, 3865.

53 S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys and A. P. Sutton, Electronic structure and elastic properties of strongly correlated metal oxides from first principles: LSDA + U, SIC-LSDA and EELS Study of $UO_2$ and NiO Phys. Rev. B: Condens. Matter Mater. Phys., 1995, 57, 1505.

54 H. J. Monkhosrt and J. D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B: Condens. Mat- ter Mater. Phys., 1976, 13, 5188.

55 W. A. Crichton, M. Mezouar, G. Monaco and S. Falconi, Phosphorus: New in situ powder data from large-volume apparatus, Powder Diffraction, 2003, 18, 155.

56 J. S. Qiao, X. H. Kong, Z. X. Hu, F. Yang and W. Ji, High-mobility transport anisotropy and linear dichroism in few-layer black phosphorus, Nat. Comm., 2014, 5, 4475.

57 Y. C. Ma, P. O. Lehtinen, A. S. Foster and R. M. Nieminen, Magnetic properties of vacancies in graphene and single- walled carbon nanotubes, New J. Phys., 2004, 6, 68.

58 E. J. G. Santos, A. Ayuela and D. Sanchez-Portal, First- principles study of substitutional metal impurities in graphene: structural, electronic and magnetic properties, New J. Phys., 2010, 12, 053012.

59 J. Ribeiro-Soares, R. M. Almeida, L. G. Cancado, M. S. Dresselhaus and A. Jorio, Group theory forstructural anal- ysis and lattice vibrations in phosphorene systems, Phys. Rev. B: Condens. Matter Mater. Phys., 2015, 91, 205421.

60 D. P. Rai and R. K. Thapa, An abinitio study of the half- metallic properties of $Co_2TGe$ (T=Sc, Ti, V, Cr, Mn, Fe): LSDA $+U$ method, Journal of the Korean Physical Soci- ety, 2013, 62, 1652.

61 W. L. Huang, Q. Zhu, W. Ge, H. Li, Oxygen-vacancy for- mation in $LaMO_3$ (M = Ti, V, Cr, Mn, Fe, Co, Ni) calcu- lated at both GGA and GGA $+U$ levels, Comput. Mater. Sci., 2011, 50, 1088.

62 G. Pari, S. Mathi Jaya, G. Subramoniam, and R. Asoka- mani, Density-functional descriytion of the electronic structure of $LaMO_3$ (M =Sc, Ti, V, Cr, Mn, Fe, co, Ni) Phys. Rev. B: Condens. Matter Mater. Phys., 1995, 51, 16575.