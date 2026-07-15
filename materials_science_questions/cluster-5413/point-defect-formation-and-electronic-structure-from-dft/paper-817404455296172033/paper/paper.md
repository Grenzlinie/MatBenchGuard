PHYSICAL REVIEW B 100, 184108 (2019)

# Theoretical investigation of iron incorporation in hexagonal barium titanate

Waheed A. Adeagbo, $^{1}$ Hichem Ben Hamed, $^{1}$ Sanjeev K. Nayak, $^{2}$ Rolf Böttcher, $^{3}$ Hans T. Langhammer, $^{4}$ and Wolfram Hergert $^{1}$

$^{1}$ Institute of Physics, Martin Luther University Halle-Wittenberg, Von-Seckendorff-Platz 1, 06120 Halle, Germany
$^{2}$ Department of Materials Science \& Engineering, Institute of Materials Science, University of Connecticut, Storrs, Connecticut 06269, USA
$^{3}$ Faculty of Physics and Earth Sciences, University of Leipzig, Linnéstraße 5, 04103 Leipzig, Germany
$^{4}$ Institute of Chemistry, Martin Luther University Halle-Wittenberg, Kurt-Mothes-Straße 2, 06120 Halle, Germany

![](./images/817404455296172033_1.jpg)
(Received 15 March 2019; revised manuscript received 10 September 2019; published 13 November 2019)

The incorporation of Fe impurities in hexagonal barium titanate is studied in the framework of density functional theory. Formation energies are calculated to find the most probable defect structure. The substitution of Fe at the two inequivalent Ti sites accompanied by oxygen vacancies in different positions is studied. Additionally, different charge states of defects are taken into account. The structural aspects of the different defects are also studied in detail. In summary, the theoretical results are in agreement with recent experimental results found by means of electron paramagnetic resonance.

DOI: 10.1103/PhysRevB.100.184108

## I. INTRODUCTION

The family of perovskite oxides of type $ABO_{3}$ is extremely interesting due to the wide range of solid-state phenomena they possess. Perovskites exhibit ferroelectricity, magnetism, magnetoresistance, and also superconductivity. Many of the perovskites are used in catalytic applications [1,2]. The physical and chemical properties can be altered by a controlled substitution of A- and/or B-site cations [3].

Barium titanate $(BaTiO_{3})$ is a perovskite with a wide range of technical applications [4-6]. Different phases of barium titanate are known experimentally. Aside from the well-known low-temperature-driven phase transitions of the cubic 3C modification $(c-BaTiO_{3})$, it exhibits also a high-temperature phase transition into the 6H hexagonal polymorph $(h-BaTiO_{3})$, also referred to as $6H-BaTiO_{3}$ in literature, occurring at $1430^{\circ}C$ in air [7,8]. This 6H hexagonal modification can be stabilized down to lower temperatures either by cooling in strongly reducing atmosphere [9,10] or by doping with particular acceptor ions [11-14].

Hexagonal $BaTiO_{3}$ is a system known to accommodate a very large amount of $3d$ transition metal ions replacing Ti ions in the host matrix. The influence of this ion substitution on the stabilization of the structure has been widely investigated experimentally, see, e.g., Refs. [11,15]. It has been shown that in case of doping by Cr, Mn, Fe, Co, Ni, or Cu, a relatively small concentration of $<1$ mol% is sufficient to produce a partial transition to the hexagonal phase and that a concentration of 2 mol% is almost always enough to cause a nearly complete phase transition [12-14,16-18].

Structure and stability of impurities and intrinsic point defects in $h-BaTiO_{3}$ was also investigated theoretically. A geometrical optimization of the hexagonal phase by means of density functional theory was performed by Coulson et al. [19]. Freeman et al. developed a potential model for $BaTiO_{3}$ that describes the cubic and hexagonal phases. This potential is used in rare earth metal incorporation and transition metal doping in $h-BaTiO_{3}$ [20,21]. Dawson et al. [22] used DFT methods to study intrinsic point defects such as cation and oxygen vacancies in $h-BaTiO_{3}$. Nayak et al. [23] have explored the charge states of Cr doping in an explicit electronic compensated scenario in $h-BaTiO_{3}$.

The incorporation of magnetic ions in barium titanate has raised the question on existence of magnetism and multi-ferroicity. Fe doped $BaTiO_{3}$ is of special interest here. Ray et al. [24] observed room temperature ferromagnetism in Fe-doped barium titanate as a diluted magnetic oxide and performed first-principles calculations to elucidate its magnetic properties. Valant et al. [25] discuss disorder-order transition in Fe doped $6H-BaTiO_{3}$. The $Fe^{3+}$ ions initially distributed on both crystallographically nonequivalent Ti sites break the symmetry of site occupancy and order onto one preferred Ti site upon prolonged heat treatment. Such a mechanism of atomic site redistribution is suggested to induce room-temperature ferromagnetism. The combination of magnetism with semiconducting properties makes $6H-BaTiO_{3}$ interesting for spintronics applications.

X-ray absorption spectroscopy (XAS) is used as an experimental tool to study the near edge structure (XANES) valence state of the impurity. The extended x-ray absorption fine structure (EXAFS) setup is used to get information about the local structure. The appearance of x-ray magnetic circular dichroism (XMCD) is a sign of ferromagnetism in the sample. XMCD is frequently used to study dilute magnetic semiconductors, e.g., for $3d$ codoping in ZnO [26,27], $p$-orbital magnetism in imperfect ZnO [28], defect induced ferromagnetism in oxides due to local reconstruction in the presence of point defects [29]. Similar physics is also applied to $6H-BaTiO_{3}$ [25,30]. Angle-dependent single crystal electron paramagnetic resonance (EPR) allows us to retrieve detailed information on the charge state and defect geometry of the impurity. A recent comprehensive analysis of EPR experiments on Fe in $6H-BaTiO_{3}$ by Böttcher et al. [31] provides such data.

The present paper presents results in the framework of density functional theory (DFT) for Fe impurities in $h-BaTiO_{3}$.

2469-9950/2019/100(18)/184108(11)
184108-1
©2019 American Physical Society

![](./images/817404455296172033_2.jpg)

FIG. 1. Crystal structure of $h$-BaTiO$_3$ showing exclusively corner-sharing oxygen octahedra of Ti(1) (light blue) and the face-sharing oxygen octahedra of Ti(2) (violet) in the elementary cell. The stacking of layers of inequivalent atoms is indicated at the right hand side [O(1)—yellow, O(2)—red]. The oxygen positions $Ui$ and $Vi$ are related to Ti(1) and Ti(2) sites, respectively.

It is a comprehensive investigation of the Fe incorporation accompanied by O vacancy formation. It extends the investigation of Nayak *et al.* [32] for Cr in $h$-BaTiO$_3$. The calculated formation energies allow conclusions about the preferred sites of incorporation and the oxidation state of the defect. The structural information provided by Böttcher *et al.* [31] encouraged also a detailed analysis of the geometry around the defects. The calculated geometric structure around the defect might also be useful in the interpretation of XAS experiments.

The paper is organized as follows: After a summary of the structural properties of $h$-BaTiO$_3$ and the defect structures considered here, the theoretical method is shortly explained. Next, the calculated formation energies are used to discuss the preferred substitution site and compensation mechanism. Finally detailed structural information about the most important defects is provided.

## II. POINT DEFECTS IN $h$-BaTiO$_3$

The crystal structure of $h$-BaTiO$_3$ belongs to the space group $P6_3/mmc$ (No. 194). The primitive cell consists of six functional units of BaTiO$_3$ with thirty atoms in total. The crystal structure can also be considered as layered with BaO$_3$ and TiO$_2$ layers stacked along the $c$ axis. The 6H polytype with a stacking sequence of (ABA)(CBC) is presented in Fig. 1. The types (1) and (2) of each element appear in the ratio 1: 2 in stoichiometric $h$-BaTiO$_3$.

They occupy interstitial positions between the BaO$_3$ layers and are located in the center of interlayer O octahedra. Figure 1 reveals that two types of TiO$_6$ octahedra appear in the crystal structure. Exclusively corner-sharing octahedra are formed by Ti(1) and O(2), while the face-sharing octahedra are formed by Ti(2) and both types of O.

Fe can appear in different oxidation states. The most common ones are Fe$^{2+}$ and Fe$^{3+}$ in the usual iron oxides, but high-valent cations are also possible [33]. The EPR experiments [31] reveal that iron is incorporated as Fe$^{3+}$ at Ti sites. Oxidation states from 2+ to 5+ will be investigated. A supercell charge compensated by an opposite charge in the jellium background is used to force a certain oxidation state. The discussion of oxidation states in modern material science is a nontrivial task [34].

Two charge compensation mechanisms are considered in our studies: Either an exclusively electronic charge compensation of the Fe defects or an additional compensation by oxygen vacancy charge. Fe can be substituted at Ti(1) or Ti(2) sites, designated as Fe$_{\text{Ti(1)}}$ and Fe$_{\text{Ti(2)}}$. Hence, if an additional oxygen vacancy (V$_O$) is considered, a series of inequivalent positions of V$_O$ have to be taken into account if nearest and next-nearest positions of V$_O$ to Fe are considered. Those positions are indicated as $Ui$ and $Vi$ for Ti(1) and Ti(2) sites, respectively, in Fig. 1. Related to Fe$_{\text{Ti(1)}}$ there are three potential V$_O$ sites named U1–U3 and six for Fe$_{\text{Ti(2)}}$ named V1–V6. The sites U1,V1,V2 are nearest neighbor sites with respect to the substituted Fe atom, while all others are next-nearest neighbor sites.

## III. COMPUTATIONAL APPROACH

The general scheme of the calculations is presented here. Additional details can be found in the Supplemental Material [35] (see, also, Refs. [29,36–39] therein).

### A. Electronic structure

The calculations are based on density functional theory and are performed by the plane-wave pseudopotential method as implemented in the Vienna *ab initio* simulation package (VASP) [40,41]. The PW'91 generalized gradient functional [39] was employed to describe electron-electron exchange and correlation interactions through the use of projector augmented wave (PAW) method [42,43], with Fe-$[3d^74s^1]$, Ba-$[5s^25p^66s^2]$, Ti$[3d^34s^1]$, and O-$[2s^22p^4]$ valence electrons treated self-consistently.

The theoretically found lattice constants $a=5.805$ Å, $c=14.077$ Å from Nayak *et al.* [32] are used. A $3\times3\times1$ supercell containing 270 atoms is constructed for the defect studies. Spin polarized calculations are performed corresponding to the substitution of Ti by Fe. One Fe atom per supercell corresponds to a concentration of 1.85 at.% in agreement with the impurity concentration of about 2 mol% in experiments. The kinetic energy cutoff for the plane waves is set to 400 eV. Structural relaxations are performed within the $\Gamma$-point approximation until the interatomic forces converged below the threshold value of $25$ meV Å$^{-1}$. The total energy and the density of states are computed by means of a $\Gamma$-centered $2\times2\times3$ Monkhorst-Pack k-point mesh.

The limitation of density-based exchange correlation functionals in DFT in accounting for the strong localization character of $d$ orbitals is overcome by the use of the DFT $+U$

approach [44,45]. We have to apply such corrections to the Fe $3d$ states of the impurity in $h$-BaTiO$_3$ and also to the Fe $3d$ states of Fe$_2$O$_3$ which is used for the calculation of the Fe chemical potential required in the consideration of formation energies. The Fe-$3d$ states are corrected in the GGA + U framework with $U = 4$ eV according to the scheme of Dudarev *et al.* [46].

### B. Formation energy

In order to characterize the stability of the considered configurations $D$ of an Fe impurity in the supercell, defect formation energies $E_{\text{form}}(\text{D}, q)$ for different charge states $q$ are calculated. The formation energy is calculated according to [23,32,47–49]

$$
\begin{aligned}
E_{\text{form}}(\text{D}, q) &= E(\text{D}, q) - E_{\text{Host}} + \sum_{i} p_{i}n_{i}\mu_{i} \\
&\quad + q(E_{\text{V}} + \Delta E_{\text{F}}) + E_{\text{corr}}.
\end{aligned}
\tag{1}
$$

Here, $E(\text{D}, q)$ and $E_{\text{Host}}$ are the total energies of the supercell with defect and charge state $q$ and the host supercell of the same size, respectively. The chemical potential $\mu_{i}$ is used to take into account the change of atoms of elemental species $i$. Thus, $n_{i}$ is the corresponding number of atoms and $p_{i}$ is $\mp 1$ according to whether the atom is added or removed from the supercell. $E_{\text{V}}$ is the valence band maximum of the host and $\Delta E_{\text{F}}$ represents the position of the Fermi level in the band gap related to $E_{\text{V}}$. $E_{\text{corr}}$ is a sum of corrections which takes into consideration the finite size effect, including the image charge and the potential alignment corrections (see Refs. [23,32,35,50] for details). Additional information about the stability of defect complexes follows from the binding energy (cf. Refs. [22,51]). If the defects $A$ and $B$ react to a complex $AB$ the binding energy can be found from the formation energies

$$
E_{B} = E_{\text{form}}(A) + E_{\text{form}}(B) - E_{\text{form}}(AB).
\tag{2}
$$

A positive binding energy indicates a stable, bound defect complex.

The following chemical potentials have been used in our studies:

$$
\mu_{\text{Ti}} = E(\text{TiO}_2) - 2\mu_{\text{O}},\quad \mu_{\text{Fe}} = \frac{1}{2}[E(\text{Fe}_2\text{O}_3) - 3\mu_{\text{O}}]. \tag{3}
$$

The chemical potential of oxygen $\mu_{\text{O}}$ is treated as a variable with an estimated upper limit of

$$
\mu_{\text{O}}^{\text{max}} = \frac{1}{2}E(\text{O}_2),
\tag{4}
$$

often called an “oxygen-rich” condition, where $E(\text{O}_2)$ is the total energy of a free, isolated O$_2$ molecule in the triplet state at $T = 0$ K [52]. Details of the calculation of the chemical potentials are given in the Supplemental Material [35] (see, also, Refs. [22,32,47–49,53,54] therein). With the above choice of chemical potentials, the formation energy of Eq. (1) becomes, cf. for substitution of one Ti atom by an Fe atom,

$$
\begin{aligned}
E_{\text{form}}(\text{D}, q) &= E(\text{D}, q) - E_{h\text{-BaTiO}_3} + [E(\text{TiO}_2) - 2\mu_{\text{O}}] \\
&\quad - \frac{1}{2}[E(\text{Fe}_2\text{O}_3) - 3\mu_{\text{O}}] + \mu_{\text{O}} \\
&\quad + q(E_{\text{V}} + \Delta E_{\text{F}}) + E_{\text{corr}}.
\end{aligned}
\tag{5}
$$

![](./images/817404455296172033_3.jpg)

FIG. 2. Relation between oxygen partial pressure ($p_{\text{O}_2}$) and the relative chemical potential of oxygen ($\Delta\mu_{\text{O}}$) at $T = 1400$ °C. The estimation is done by using Eq. (6) together with the absolute value for $\mu_{\text{O}}$ in the O-rich condition which is set to zero as in Ref. [52]). (Figure from Ref. [32].)

Equation (5) describes the substitution of one Ti atom by an Fe atom. The additional $\mu_{\text{O}}$ corresponds to the compensation mechanism by an oxygen vacancy. The advantage of an expression such as of (5) is in minimizing the number of parameters considered for the chemical potentials. In the present case the $\mu_{\text{O}}$ becomes the free parameter that defines the $\mu_{\text{Ti}}$ and $\mu_{\text{Fe}}$ through the enthalpy of corresponding oxide compounds. Furthermore, the oxygen chemical potential $\mu_{\text{O}}$ can be derived from the partial pressure of oxygen gas ($p_{\text{O}_2}$) and is given by the thermodynamic expression

$$
\mu_{\text{O}}(T, p_{\text{O}_2}) = \mu_{\text{O}}(T, p^\circ) + \frac{1}{2}kT \ln\left(\frac{p_{\text{O}_2}}{p^\circ}\right),
\tag{6}
$$

where, $p^\circ$ is the standard pressure of 1 bar. The values of $\mu_{\text{O}}(T, p^\circ)$ are taken from the NIST-JANAF thermochemical tables [55]. Equations (5) (and its equivalent as applicable for the defect under consideration) and (6) allow us to simulate real experimental conditions, i.e., a reducing or oxidizing atmosphere.

The chemical potential $\mu_{\text{O}}$ in Eq. (5) can be linked to Eq. (6), by choosing a common reference $\mu_{\text{O}}(0\ \text{K}, p) = \mu_{\text{O}}^{\text{max}}$ (cf. Reuter *et al.* [52]) and using $\Delta\mu_{\text{O}} = \mu_{\text{O}}(T, p_{\text{O}_2}) - \mu_{\text{O}}^{\text{max}}$. Figure 2 reveals the relation between $\Delta\mu_{\text{O}}$ and $p_{\text{O}_2}$ calculated from Eq. (6) at 1400 °C, which is the sintering temperature of the ceramic BaTiO$_3$ samples. The presence of a thermodynamic equilibrium between the atomic defects in the sample and the oxygen partial pressure of the surrounding can be assumed at this temperature. The experimentally covered range of $p_{\text{O}_2}$ from strongly reducing conditions using a gas mixture of H$_2$/Ar to pure oxygen at 1 bar corresponds to $\Delta\mu_{\text{O}}$ ranging from $-5.14$ eV to $-1.98$ eV, respectively. Common experimental environments are marked as vertical (blue) lines in Fig. 2.

<table><caption>Table I. Supercell magnetic moments (M) and formation energies ($\text{E}_{\text{form}}$) of an isolated Fe impurity for different charge states ($q = -2, -1, 0$, and $+1$) obtained from Eq. (5) using $\Delta\mu_{\text{O}}$ (air) and $\Delta E_{\text{F}} = 0$. The local magnetic moment of Fe atoms ($m_{\text{Fe}}$) and the effective partial atomic charge on Fe ($Q^{bc}$) from Bader analysis is also shown. $\Delta E_{\text{form}}$ is the difference in formation energy between the Ti(1) site and Ti(2) site.</caption>
<thead>
  <tr>
    <th>Site</th>
    <th>Property</th>
    <th>$q = -2$<br>$\text{Fe}^{2+}$</th>
    <th>$q = -1$<br>$\text{Fe}^{3+}$</th>
    <th>$q = 0$<br>$\text{Fe}^{4+}$</th>
    <th>$q = +1$<br>$\text{Fe}^{5+}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Ti(1)</td>
    <td>M ($\mu_{\text{B}}$)</td>
    <td>4.00</td>
    <td>5.00</td>
    <td>5.00</td>
    <td>5.00</td>
  </tr>
  <tr>
    <td></td>
    <td>$m_{\text{Fe}}$ ($\mu_{\text{B}}$)</td>
    <td>3.71</td>
    <td>3.83</td>
    <td>4.22</td>
    <td>4.21</td>
  </tr>
  <tr>
    <td></td>
    <td>$Q^{bc}$ ($e$)</td>
    <td>1.42</td>
    <td>1.68</td>
    <td>1.81</td>
    <td>1.83</td>
  </tr>
  <tr>
    <td></td>
    <td>$E_{\text{form}}$ (eV)</td>
    <td>3.392</td>
    <td>1.477</td>
    <td>1.040</td>
    <td>0.739</td>
  </tr>
  <tr>
    <td>Ti(2)</td>
    <td>M ($\mu_{\text{B}}$)</td>
    <td>4.00</td>
    <td>5.00</td>
    <td>4.00</td>
    <td>3.00</td>
  </tr>
  <tr>
    <td></td>
    <td>$m_{\text{Fe}}$ ($\mu_{\text{B}}$)</td>
    <td>3.72</td>
    <td>3.79</td>
    <td>3.83</td>
    <td>3.34</td>
  </tr>
  <tr>
    <td></td>
    <td>$Q^{bc}$ ($e$)</td>
    <td>1.36</td>
    <td>1.49</td>
    <td>1.68</td>
    <td>1.80</td>
  </tr>
  <tr>
    <td></td>
    <td>$E_{\text{form}}$ (eV)</td>
    <td>3.214</td>
    <td>1.379</td>
    <td>0.968</td>
    <td>0.226</td>
  </tr>
  <tr>
    <td></td>
    <td>$\Delta E_{\text{form}}$ (eV)</td>
    <td>0.178</td>
    <td>0.098</td>
    <td>0.072</td>
    <td>0.513</td>
  </tr>
</tbody>
</table>

## IV. RESULTS AND DISCUSSION

At first the calculated formation energies will be related to the electronic structure and experimental findings. Afterwards the structural and electronic aspects of the defects will be discussed in detail. The formation energies for the host systems for intrinsic defect complexes and rare earth element doping is considered in literature from DFT and empirical potentials, respectively [20,22]. Unlike the nature of dopants already considered in the literature, the Fe doping introduces additional complexity due to the variable oxidation states the dopant atom can acquire due to the interplay of crystal field energy and electron pairing energy.

### A. Formation energies

Table I summarizes the magnetic properties and formation energies of differently charged isolated Fe impurities, i.e., the exclusively electronic charge compensation mechanism is realized. The Fe atom is placed at the two inequivalent sites Ti(1) and Ti(2).

We have assumed that the $\text{Fe}^{2+}$, $\text{Fe}^{3+}$, $\text{Fe}^{4+}$, and $\text{Fe}^{5+}$ states correspond to the respective supercell charge states $q = -2, -1, 0$, and $+1$, in which the integral charges are constructed by adding electrons to ($q < 0$) or removing electrons from ($q > 0$) the neutral system (supercell), respectively. $\text{Fe}^{4+}$ is the neutral state with $q = 0$ in which Fe assumes the oxidation state of a Ti atom in the $4+$ state.

It can be seen that the formation energy at the Ti(1) site is for all cases higher than at the Ti(2) site, i.e., Fe at the Ti(2) site forms the more stable defect. The lowest formation energy is found for Fe at Ti(2) for the charge state $q = +1$, i.e., $\text{Fe}^{5+}$. The substituted Fe is located in a deformed octahedral environment built by the surrounding O atoms. The difference between the total moment of the supercell M and the Fe moment $m_{\text{Fe}}$ is a measure of the polarization of the surrounding oxygen atoms. For the $\text{Fe}^{4+}$ and $\text{Fe}^{5+}$ at the Ti(2) site, the polarization is much smaller. In the case of $\text{Fe}^{5+}$, a small negative polarization of the oxygen atoms occurs.

The $d$ levels of Fe in an ideal octahedral environment are split in $\text{t}_{2\text{g}}$ and $\text{e}_{\text{g}}$ sublevels by symmetry. The magnetic moments per supercell from the DFT calculations agree with the Fe moment in a high spin state at the Ti(2) site considered in an ionic picture. A better understanding of the charge transfer between the Fe atom and in its environment in the lowest energy configurations is obtained from Bader charge concept [56]. The calculated Bader effective charges are presented in Table I. $Q^{bc}$ on Fe only provides a relative, not an absolute, measure of the Fe charge state as $\text{Fe}^{2+}$, $\text{Fe}^{3+}$, $\text{Fe}^{4+}$, and $\text{Fe}^{5+}$ but increases with oxidation states. It is larger for Fe at the Ti(1) site than at the Ti(2) site. The change of $Q^{bc}$ (Bader charge) at $\text{Fe}^{4+}$ state is between 0.1 and $0.4\ e$. This confirms the fact that the oxidation states of Fe are not one to one correspondence to the integer charge states $q$ of the supercell as it is proved in Ref. [57]. The magnetic moment of the Fe doped $h$-BaTiO$_3$ systems were further cross checked with fixed-spin moment calculations, the lowest energy (same trend for formation energy) and the corresponding magnetic moments obtained from such analysis are shown in Table I. Overall, from the analysis of integrated partial density of states it is concluded that the minority $\text{e}_{\text{g}}$ defect state controls the electronic compensation of $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ both at Ti(1) and Ti(2) sites. The $\text{Fe}^{4+}$ state and the electronic compensation of $\text{Fe}^{5+}$ at the Ti(2) site is controlled by majority spin channel $\text{t}_{2\text{g}}$ near the Fermi level (see Ref. [35]). The Ba states are not considered here in this context of the defect problems. Thus, Figs. 3(a)–3(h) present the partial DOS of the Fe $3d$ states, the Ti $3d$ states, and the O $2p$ states. A strong hybridization of all those states can be seen in the valence band region. O $2p$ state contributions are negligible in the conduction band. The localized Fe $3d$ states hybridize mainly with $2p$ states of the neighboring O atoms. Changing from $\text{Fe}^{4+}$ to $\text{Fe}^{5+}$ state causes only small changes in the DOS in the case of Fe at the Ti(1) site. Hence, the magnetic moment is nearly unchanged. In the case of Fe at Ti(2) the change of the charge state shifts the peak at the Fermi energy into the unoccupied energy region accompanied by the appearance of a pronounced peak in the minority spin region, resulting in a lower Fe moment in the $\text{Fe}^{5+}$ state. This means an electron is removed from the Fe atom. The density of states for isolated Fe doping for the $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ states show peaks at the Fermi energy which are mainly due to the $d$ states of Fe for both Ti(1) and Ti(2) sites. In the case of $\text{Fe}^{4+}$ and $\text{Fe}^{5+}$, there is strong hybridization between Fe-$3d$ and O-$2p$ states with more states of O-$2p$ at Fermi level. This means that the holes in the valence band state due to the electron deficient condition is partly localized on the oxygen $2p$ orbitals that introduces hole carriers in a p-type system. The screening effect of hole charges affects the magnetic moment of Fe, which for 0 and $+1$ charges states are obtained $\approx 4.2\ \mu_{\text{B}}$. On the other hand, the magnetic moment of electron rich charge states $-2$ and $-1$ is found to be $3.7\ \mu_{\text{B}}$ and $4.2\ \mu_{\text{B}}$, respectively. The second compensation mechanism includes an O vacancy. The different positions of the vacancy with respect to Fe at the Ti(1) or Ti(2) site are indicated in Fig. 1. The O vacancy induces two excess electrons, thus only $\text{Fe}^{2+}$-V$_{\text{O}}$ and $\text{Fe}^{3+}$-V$_{\text{O}}$ are possible in the range of assumed oxidation states of Fe. Again, the effective Bader charges ($Q^{bc}$) calculated for $\text{Fe}^{2+}$-V$_{\text{O}}$ and $\text{Fe}^{3+}$-V$_{\text{O}}$ for Fe at Ti(1)/Ti(2) are on the average $1.35/1.15$ and

184108-4

![](./images/817404455296172033_4.jpg)

FIG. 3. Partial density of states for exclusively electronically charge-compensated defects at the Ti(1) site (a)-(d) and the Ti(2) site (e)-(h). Configuration (h) is the most stable one.

$1.73/1.58$ $e$, respectively, which are almost the same values for $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ states of the isolated point defect of Fe at Ti(1)/Ti(2).

The results for the different configurations, ordered with respect to the formation energy, are given in Table II. In both charge states the lowest formation energy is found for the U2 configuration. It can be seen that the configurations V2 and V6 [at the Ti(2) site] are close in formation energy. The oxygen vacancy is located in the first neighbor shell for the V2 configuration but in the next-nearest shell for V6. The formation energies for the $\text{Fe}^{2+}$-$\text{V}_O$'s are considerably higher. Table II also reveals that the formation energy does not systematically depend on the distance between Fe impurity and $\text{V}_O$.

Binding energies have been calculated from (2) for the complexes with U2, V2, and V1 structure from Table II. All complexes are stable ($E_b > 0$). The binding energy of Fe-$\text{V}_O$ complex is larger for $\text{Fe}^{3+}$-$\text{V}_O$ than those for $\text{Fe}^{2+}$-$\text{V}_O$. The largest binding energy is found for the complex with the U2 structure, i.e., the binding energies follow the formation energies given in Table II.

In the case of the isolated Fe impurity, $\text{Fe}^{5+}$ at the Ti(2) site is the most stable one with a magnetic moment of $3.3\ \mu_\text{B}$. In the case of the complex with $\text{V}_O$ the substitution at the Ti(1) site is more favorable. The magnetic moment of about $4.2\ \mu_\text{B}$ for $\text{Fe}^{3+}$-$\text{V}_O$ agrees with the corresponding value for the isolated Fe impurity in $\text{Fe}^{5+}$ state. For the substitution at the Ti(2) site the magnetic moment in the complex does not change considerably, but it is larger than for the isolated defect.

Figure 4 reveals that in the case of the $\text{V}_O$ charge-compensated defects the Fe $3d$ DOS shows similar features like for the single Fe defects presented in Fig. 3. Charge state and configuration affect the Fe $3d$ DOS mainly near the Fermi energy. In the higher oxidation state spin-down states are pushed into the unoccupied energy region leading to a small increase of the magnetic Fe moments. The theoretical results can be related to the recent EPR investigations of Fe doped $h$-BaTiO$_3$ single crystals by Böttcher *et al.* [31] which reveals three different $\text{Fe}^{3+}$ defect centers. Two of them were attributed to isolated $\text{Fe}^{3+}$ defects incorporated at Ti(1) and at Ti(2) sites, which could be distinguished by the different distortion of the Ti(1) and Ti(2) surrounding O octahedra which is reflected by a distinct difference of the fine structure parameters of both centers. The third detected center consists of $\text{Fe}^{3+}$ and a neighboring oxygen vacancy. From the EPR point of view 'isolated defect' means that

TABLE II. Comparison of the calculated properties for the $\text{Fe}_\text{Ti}$-$\text{V}_O$ complexes for various lattice positions of $\text{V}_O$. The different $\text{V}_O$ sites are indicated in Fig. 1.($d_{\text{Fe}-\text{V}_O}$—distance between Fe impurity and O vacancy, $m_\text{Fe}$—magnetic moment of Fe atom, $E_{\text{form}}$—formation energy of the defect obtained from Eq. (5) using $\Delta\mu_O$ (air), $\Delta E_{\text{form}}$—difference in formation energy with respect to the lowest value.) Data are presented in ascending order of $\text{Fe}^{3+}$ formation energy (Calculation for $\Delta E_\text{F} = 0.$)

<table>
  <thead>
    <tr>
      <th colspan="2">site</th>
      <th colspan="2">$\text{V}_O$</th>
      <th>$d_{\text{Fe}-\text{V}_O}$</th>
      <th>neighbor</th>
      <th colspan="3">$q=0, \text{M}=4\ \mu_\text{B}, (\text{Fe}^{2+}\text{-V}_O)$</th>
      <th colspan="3">$q=+1, \text{M}=5\ \mu_\text{B}, (\text{Fe}^{3+}\text{-V}_O)$</th>
    </tr>
    <tr>
      <th></th>
      <th>at</th>
      <th>type</th>
      <th></th>
      <th>($\mathring{\text{A}}$)</th>
      <th>shell</th>
      <th>$m_\text{Fe}$ ($\mu_\text{B}$)</th>
      <th>$E_{\text{form}}$ (eV)</th>
      <th>$\Delta E_{\text{form}}$ (eV)</th>
      <th>$m_\text{Fe}$ ($\mu_\text{B}$)</th>
      <th>$E_{\text{form}}$ (eV)</th>
      <th>$\Delta E_{\text{form}}$(eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ti(1)</td>
      <td>U2</td>
      <td>O(1)</td>
      <td></td>
      <td>4.57</td>
      <td>2</td>
      <td>3.71</td>
      <td>$-0.1876$</td>
      <td>0.0000</td>
      <td>4.22</td>
      <td>$-1.6774$</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <td></td>
      <td>U1</td>
      <td>O(2)</td>
      <td></td>
      <td>2.01</td>
      <td>1</td>
      <td>3.66</td>
      <td>0.2856</td>
      <td>0.4732</td>
      <td>4.13</td>
      <td>$-0.9931$</td>
      <td>0.6844</td>
    </tr>
    <tr>
      <td></td>
      <td>U3</td>
      <td>O(2)</td>
      <td></td>
      <td>4.59</td>
      <td>2</td>
      <td>3.71</td>
      <td>0.5642</td>
      <td>0.7518</td>
      <td>4.22</td>
      <td>$-0.9758$</td>
      <td>0.7020</td>
    </tr>
    <tr>
      <td>Ti(2)</td>
      <td>V2</td>
      <td>O(1)</td>
      <td></td>
      <td>2.01</td>
      <td>1</td>
      <td>3.91</td>
      <td>$-0.1183$</td>
      <td>0.0693</td>
      <td>4.11</td>
      <td>$-1.6322$</td>
      <td>0.0453</td>
    </tr>
    <tr>
      <td></td>
      <td>V6</td>
      <td>O(1)</td>
      <td></td>
      <td>4.77</td>
      <td>2</td>
      <td>3.70</td>
      <td>$-0.0540$</td>
      <td>0.1336</td>
      <td>4.16</td>
      <td>$-1.4848$</td>
      <td>0.1926</td>
    </tr>
    <tr>
      <td></td>
      <td>V4</td>
      <td>O(2)</td>
      <td></td>
      <td>4.39</td>
      <td>2</td>
      <td>3.69</td>
      <td>0.6186</td>
      <td>0.8062</td>
      <td>4.16</td>
      <td>$-0.9038$</td>
      <td>0.7736</td>
    </tr>
    <tr>
      <td></td>
      <td>V1</td>
      <td>O(2)</td>
      <td></td>
      <td>1.98</td>
      <td>1</td>
      <td>3.62</td>
      <td>0.3591</td>
      <td>0.5467</td>
      <td>4.07</td>
      <td>$-0.9017$</td>
      <td>0.7758</td>
    </tr>
    <tr>
      <td></td>
      <td>V3</td>
      <td>O(2)</td>
      <td></td>
      <td>4.10</td>
      <td>2</td>
      <td>3.69</td>
      <td>0.3718</td>
      <td>0.5594</td>
      <td>4.14</td>
      <td>$-0.8640$</td>
      <td>0.8135</td>
    </tr>
    <tr>
      <td></td>
      <td>V5</td>
      <td>O(2)</td>
      <td></td>
      <td>4.54</td>
      <td>2</td>
      <td>3.69</td>
      <td>0.5941</td>
      <td>0.7817</td>
      <td>4.16</td>
      <td>$-0.8608$</td>
      <td>0.8167</td>
    </tr>
  </tbody>
</table>

![](./images/817404455296172033_5.jpg)

FIG. 4. Partial density of states for $V_O$ charge-compensated defects with lowest formation energy at site Ti(1) in U2 configuration (a), (b) and at site Ti(2) in V2 configuration (c), (d). Configuration (b) is the most stable one.

the Fe surrounding oxygen octahedron is complete, i.e., no nearest neighbor oxygen vacancy exists. But the $V_O$ necessary for charge compensation could be situated already in the second coordination sphere of the Fe defect, which cannot be detected by the mentioned EPR experiments. Hence, the configurations U2, U3, and V3–V6 (cf. Fig. 1 and Table II) correspond to the isolated Fe defect from EPR point of view, while only configurations U1, V1, V2 could correspond to the EPR-detected $Fe^{3+}$-$V_O$ associate. Table II proves that the calculated formation energies correspond very well with the EPR findings. First, in experiment only $Fe^{3+}$ defects are found. The calculated formation energies for $Fe^{3+}$ are also lower than those for $Fe^{2+}$. Second, the lowest in formation energy are the U2, V2, and V6 configurations, which corresponds perfectly with the EPR results relating the experimentally detected $Fe_{Ti(1)}^{3+}$, $Fe_{Ti(2)}^{3+}$, and $Fe^{3+}$-$V_O$ to U2, V6, and V2, respectively. Using this assignment, quantitative EPR determines the concentration ratio of $Fe^{3+}$ defects to U2: V6: V2 = 12: 10: 1 [31]. In agreement with experiment, the formation energy of the U2 defects is found to be slightly lower than the V6 formation energy. But there is one distinct disagreement between experiment and calculation. Experimentally, the concentration of associates $Fe^{3+}$-$V_O$ (V2) is one order lower compared to the concentrations of isolated defects. Since the calculated formation energies of V2 and U2 are practically the same, one would expect similar concentrations which is not the case. This remarkable inconsistency in the case of the associate $Fe^{3+}$-$V_O$ occurs again in the following section discussing geometrical aspects of the iron defects. With a view on understanding the EPR results, we expanded our theoretical analysis to the $ab$ $initio$ thermodynamics. Figure 5 shows the dependence of the formation energy on the reduced chemical potential $\Delta\mu$ for the two compensation mechanisms. Only a selection of those configurations, which are lowest in formation energy (cf. Tables I and II) are presented. The fact that the exclusively electronically compensated defects $Fe^{2+}$, $Fe^{3+}$, $Fe^{4+}$, and $Fe^{5+}$ exhibit considerable higher formation energies (see Fig. 5 and Table I) is in correspondence with the known defect chemistry of $BaTiO_3$. Room temperature $p$-type conductivity of $BaTiO_3$ was never observed until now. Thus the formation of movable holes in the oxygen $2p$ band, corresponding to the defects in $Fe^{2+}$ and $Fe^{3+}$, is not expected. On the other hand, the formation energy of $Fe^{5+}$ state corresponding to donor doped material becomes only probable at highest oxygen chemical potentials near the O-rich limit. Already somewhat lower oxygen chemical potentials, still much higher than that of air, cause enough oxygen vacancies which lower the probability of the formation of $Fe^{5+}$ significantly.

![](./images/817404455296172033_6.jpg)

FIG. 5. Formation energies for a selection of defect configurations in dependence on the reduced formation energy $\Delta\mu$ for $\Delta E_F=0$.

Figures 6(a) and 6(b) better elucidate how the relative stability of charged defects is modified with respect to the position of Fermi level in the band gap. The formation energies for a selected defect configuration in dependence on $\Delta E_F$ both for the normal air condition and oxygen rich limit, respectively, are shown. As explained in connection with Fig. 5, $Fe^{5+}$ is not probable for normal air condition but it is highly favored

![](./images/817404455296172033_7.jpg)

FIG. 6. Formation energies for selected defect complexes as a function of $\Delta E_F$, with the position of the Fermi energy parametrized to lie between the VBM, $\Delta E_F=0$, and the DFT band gap value.

![](./images/817404455296172033_8.jpg)

FIG. 7. Local geometric structure around the inequivalent Ti sites in h-BaTiO₃: (a) structure around the Ti(1) site and (b) structure around a Ti(2) site. Furthermore, the angles $\theta_i$ are defined as angle between the bonds $L_i$ and the positive and negative $c$ axis, respectively. For pure h-BaTiO₃ the distances $L_i$ are identical around the Ti(1) site.

together with other uncompensated defects of Fe³⁺ and Fe²⁺ in the oxygen rich limit. The former defect is favorable when Fermi energy is close to the valence band maximum or the $p$-type condition, while the latter stability increases with Fermi level shifting toward the conduction band in the $n$-type region which are not experimentally observed. Other compensated defects are highly unfavored with increasing $\Delta E_{\text{F}}$ in the oxygen rich limit but their formation is probable under the reduced oxygen condition, especially when Fermi level shifts toward the top of the valence band maximum.

### B. Local geometric structure around the Fe impurities

To discuss the local geometric structure at the defects considered here, the quantities defined in Fig. 7 are used. The structures will be characterized by bond lengths of the surrounding oxygen atoms to the two inequivalent sites ($L_i$) and angles $\theta_i$ measured to the positive and negative $c$ axis, respectively. The angles and bond lengths are results from our DFT calculations. (see Ref. [35] for a comparison with other data). In undoped h-BTO the oxygen atoms around Ti(1) are equivalent, i.e., the bond lengths are $L_i = 2.0117$ Å and the

![](./images/817404455296172033_9.jpg)

FIG. 8. Fe-O bond lengths around the Fe impurity at the Ti(1) site (a)-(c) and at the Ti(2) site (d)-(f). The O labels $i$ correspond to the distances $L_i$ as defined in Fig. 7. (a) and (d) correspond to the exclusively electronic charge compensation mechanism, while the other cases include $V_O$. The dashed lines indicate the bond lengths in pure h-BTO. Symbol "○" marks the position of the oxygen vacancy in the first neighbor shell and the distance of $V_O$ from Fe (cf. Table II for the configurations). The background color helps to distinguish O(1) (gray) and O(2) (white) atoms.

![](./images/817404455296172033_10.jpg)

FIG. 9. Angles $\theta_i$, as defined in Fig. 7, around the Fe impurity at the Ti(1) site (a)-(c) and at the Ti(2) site (d)-(f) [the gray background marks O(1) atoms]. (a) and (d) correspond to the exclusively electronic charge compensation mechanism, while the other cases include $V_O$. The dashed lines indicate the angles in ideal h-BTO. Symbol "o" marks the position of the oxygen vacancy in the first neighbor shell and the corresponding angle of $V_O$ (cf. Table II for the configurations).

angles are $\theta_i = 55.708^\circ$, i.e., the oxygen octahedron is slightly compressed along the $c$ axis. The Ti(2) site is coordinated by nonequivalent oxygen atoms. One gets a stronger distortion of the oxygen octahedron and two distinct bond lengths Ti(2)-O(1) $\text{L}_A = \text{L}_i$ ($i=1,2,3$) and Ti(2)-O(2) $\text{L}_B = \text{L}_i$ ($i=4,5,6$) and the corresponding angles $\theta_A$ and $\theta_B$ are different.

The values are $\text{L}_A = 2.0154$ Å and $\text{L}_B = 1.9783$ Å, $\theta_A = 47.686^\circ$, and $\theta_i = 58.6^\circ$ respectively. A comparison of our crystal structure data with experimental data and other calculations is given in the Supplemental Material [35] (see, also, references [7,19,21,58-61] therein).

In Figs. 8 and 9 the deviations of bond length and angles from the ideal structure caused by the impurity are shown. The distances and angles of the pure h-BTO are indicated by dashed lines. Only three configurations with the lowest formation energy V2, V6, V1 are displayed in the case of $\text{Fe}_{\text{Ti(2)}}$.

If Fe is incorporated at the Ti(1) site [cf. Figs. 8(a)-8(c)] a tendency to larger distances can be seen. Figures 8(b) and 8(c) describe the oxygen vacancy compensation mechanism. The configurations U2, U3 show similar behavior because the vacancy is located in the next-nearest shell. Stronger changes are obtained for U1 having the vacancy at position 1 (cf. Fig. 7). The comparison of Figs. 8(b) and 8(c) reveals a stronger dependence of the distances from the oxidation state if the vacancy is located in the nearest neighbor shell. For the exclusively electronic charge compensation mechanism at the Ti(2) site [cf. Fig. 8(d)] it can be seen that a higher oxidation state leads to decreasing distances. Fe at Ti(2) for $\text{Fe}^{5+}$ is the lowest in formation energy for the exclusively electron charge compensated defects. Opposite bond pairs and also adjacent bonds behave such that one is contracted and the other is extended.

$\text{Fe}^{3+}$-$V_O$ with Fe at Ti(1) (U2 configuration) is the most stable defect configuration. The O vacancy is of O(1) type in the next-nearest-neighbor shell. The slight increase in the bond lengths are due to the Fe atom and not mainly caused by $V_O$. Next in formation energy comes $\text{Fe}^{3+}$-$V_O$ at Ti(2) (V2 and V6 configuration). For V2 the O vacancy is at position 1. Thus the length $\text{L}_1$ increases and the opposite bond $\text{L}_4$ decreases, while the others are approximately unaffected. In the V6 configuration the O vacancy is located in the next-nearest-neighbor shell. Thus, a slight increase in the bond lengths is obtained. Figure 9 summarizes the results for

the angles defined in Fig. 7. In the case of the exclusively electronic charge compensated defect the angles deviate only slightly from the values in undoped $h$-BaTiO$_3$. An increase of the angles for the O(1) atoms and a decrease for the O(2) atoms is obtained for Fe at Ti(2) for Fe$^{5+}$ representing the configuration with lowest formation energy.

The calculated angles $\theta_1$ (U1, V2) and $\theta_4$ (V1) related to associates Fe-V$_O$ for Fe$^{3+}$-V$_O$ (where V$_O$ and Fe are nearest neighbors) can be compared with data obtained by our EPR experiments [31]. The EPR spectrum of the associate Fe$^{3+}$-V$_O$ could be explained by a nearly axial crystal field, which symmetry axis corresponds to the direction between Fe$^{3+}$ and the neighboring V$_O$. Hence, the direction of the main axis of the fine structure tensor with the largest eigenvalue corresponds to this direction. Its angle to the $c$ axis was estimated to be $58.5^\circ$ [31]. On the other hand, according to Figs. 9(c) and 9(f) the angles for V$_O$ with respect to the $c$ axis are found to be: $\theta_{\text{U1}} = 57.5^\circ$, $\theta_{\text{V2}} = 47.5^\circ$, and $\theta_{\text{V1}} = 58.5^\circ$. The comparison between experiment and calculation clearly prefers the configurations U1 and V1 and excludes configuration V2, where the oxygen vacancy is located in the plane between the two adjacent Ti(2) sites. This oxygen plane is the peculiarity of the hexagonal compared to the cubic BTO structure. Since configuration V2 has the distinctly lowest formation energy among the three Fe-V$_O$ associate configurations for Fe$^{3+}$-V$_O$, interestingly, the DFT results are in contradiction with the experiment again only for this configuration. Remarkably, other theoretical work by Dawson *et al.* [21] using interatomic potentials between the constituents of the $h$-BaTiO$_3$ structure also found the V2 configuration as the most probable among the three possibilities. This shows that the isolated point defect obtained for the transition metals doped and the intrinsic defect especially for the compensating oxygen vacancy, like it is obtained in Refs. [21,22], has strong influence on the formation of the complexes.

## V. CONCLUSION

*Ab initio* calculations are used to study the incorporation of Fe in $h$-BaTiO$_3$ in detail. Defect formation energies are calculated for different oxidation states of Fe and both exclusively electron charge compensation and additional compensation by an oxygen vacancy. Due to high formation energies exclusively electron charge compensated defects are ruled out. Fe-V$_O$ complexes are lower in formation energy for Fe$^{3+}$-V$_O$ than the corresponding Fe$^{2+}$-V$_O$. This is in accordance with the results from EPR experiments. The kinds of the three defect configurations agree well with experiment, because two of them have the vacancy in the next-nearest-neighbor shell, which is an isolated defect from the EPR point of view. On the other hand, the differences in the formation energies found in the calculations do not reflect correctly the probability of the defects found in experiment. The angle of the Fe-V$_O$ direction can be extracted from the EPR experiments as well. We find a good agreement with this result for one investigated configuration, but this configuration is too high in energy. Both discrepancies between theory and experiment are related to the oxygen vacancy in the sharing plane of the oxygen octahedra surrounding the Ti(2) site.

The results from the DFT calculations help to interpret the experimental results with some caveats. The detailed structures for the defects in different charge states might be helpful to understand the doping physics in complex systems.

## ACKNOWLEDGMENTS

This work was funded by the German Research Foundation within the Collaborative Research Centre SFB 762 "Functionality of Oxide Interfaces" (Projects No. A4 and No. B1) and the German Academic Research Council (Project No. 31047526).

[1] J. Zhu, H. Li, L. Zhong, P. Xiao, X. Xu, X. Yang, Z. Zhao, and J. Li, Perovskite oxides: Preparation, characterizations, and applications in heterogeneous catalysis, *ACS Catalysis* **4**, 2917 (2014).

[2] M. Kubicek, A. H. Bork, and J. L.M. Rupp, Perovskite oxides - a review on a versatile material class for solar-to-fuel conversion processes, *J. Mater. Chem. A* **5**, 11983 (2017).

[3] N. Ramadass, ABO$_3$-type oxides-Their structure and properties-A bird's eye view, *Mater. Sci. Eng.* **36**, 231 (1978).

[4] A. J. Moulson and J. M. Herbert, *Electroceramics: Materials, Properties, Applications* (John Wiley and Sons, New York, 2003).

[5] M. Acosta, N. Novak, V. Rojas, S. Patel, R. Vaish, J. Koruza, G. A. Rossetti, and J. Rödel, BaTiO$_3$-based piezoelectrics: Fundamentals, current status, and perspectives, *Appl. Phys. Rev.* **4**, 041305 (2017).

[6] C. Christophe, Perovskites: A class of materials with multiple functionalities and applications, *Europhysics News* **49**, 10 (2018).

[7] R. D. Burbank and H. T. Evans, The crystal structure of hexagonal barium titanate, *Acta Crystallogr.* **1**, 330 (1948).

[8] K. W. Kirby and B. A. Wechsler, Phase relations in the barium titanate-titanium oxide system, *J. Am. Ceram. Soc.* **74**, 1841 (1991).

[9] D. Kolar, U. Kunaver, and A. Rečnik, Exaggerated anisotropic grain growth in hexagonal barium titanate ceramics, *Phys. Status Solidi* (a) **166**, 219 (1998).

[10] R. M. Glaister and H. F. Kay, An investigation of the cubic-hexagonal transition in barium titanate, *Proc. Phys. Soc., London* **76**, 763 (1960).

[11] G. M. Keith, M. J. Rampling, K. Sarma, N. Mc. Alford, and D. C. Sinclair, Synthesis and characterisation of doped 6H-BaTiO3 ceramics, *J. Eur. Ceram. Soc.* **24**, 1721 (2004).

[12] H. T. Langhammer, T. Müller, K.-H. Felgner, and H.-P. Abicht, Crystal structure and related properties of manganese-doped barium titanate ceramics, *J. Am. Ceram. Soc.* **83**, 605 (2000).

[13] H. T. Langhammer, T. Müler, R. Böttcher, and H.-P. Abicht, Structural and optical properties of chromium-doped hexagonal

barium titanate ceramics, J. Phys.: Condens. Matter **20**, 085206 (2008).

[14] R. Böttcher, H. T. Langhammer, T. Müller, and H.-P. Abicht, 3C-6H phase transition in $BaTiO_3$ induced by Fe ions: An electron paramagnetic resonance study, J. Phys.: Condens. Matter **20**, 505209 (2008).

[15] S. Jayanthi and T. R. N. Kutty, Dielectric properties if 3d transition metal substituted $BaTiO_3$ ceramics containing the hexagonal phase formation, J. Mater. Sci.: Mater. Electron. **19**, 615 (2008).

[16] H. T. Langhammer, T. Müller, R. Böttcher, and H.-P. Abicht, Crystal structure and related properties of copper-doped barium titanate ceramics, Solid State Sci. **5**, 965 (2003).

[17] R. Böttcher, H. T. Langhammer, and T. Müler, Paramagnetic resonance study of nickel ions in hexagonal barium titanate, J. Phys.: Condens. Matter **23**, 115903 (2011).

[18] The-Long Phan, P. Zhang, D. Grinting, S. C. Yu, N. X. Nghia, N. V. Dang, and V. D. Lam, Influences of annealing temperature on structural characterization and magnetic properties of Mn-doped $BaTiO_3$ ceramics, J. Appl. Phys. **112**, 013909 (2012).

[19] T. A. Colson, M. J. S. Spencer, and I. Yarovsky, A DFT study of the perovskite and hexagonal phases of $BaTiO_3$, Comput. Mater. Sci. **34**, 157 (2005).

[20] J. A. Dawson, C. L. Freeman, L.-B. Ben, J. H. Harding, and D. C. Sinclair, An atomistic study into the defect chemistry of hexagonal barium titanate, J. Appl. Phys. **109**, 084102 (2011).

[21] J. A. Dawson, C. L. Freeman, J. H. Harding, and D. C. Sinclair, Phase stabilisation of hexagonal barium titanate doped with transition metals: A computational study, J. Solid State Chem. **200**, 310 (2013).

[22] J. A. Dawson, J. H. Harding, H. Chen, and D. C. Sinclair, First-principles study of intrinsic point defects in hexagonal barium titanate, J. Appl. Phys. **111**, 094108 (2012).

[23] S. K. Nayak, W. A. Adeagbo, H. T. Langhammer, W. Hergert, T. Müller, and R. Böttcher, Study of charged defects for substitutionally doped chromium in hexagonal barium titanate from first-principles theory, Phys. Status Solidi RRL **8**, 527 (2014).

[24] S. Ray, P. Mahadevan, S. Mandal, S. R. Krishnakumar, C. S. Kuroda, T. Sasaki, T. Taniyama, and M. Itoh, High temperature ferromagnetism in single crystalline dilute Fe-doped $BaTiO_3$, Phys. Rev. B **77**, 104416 (2008).

[25] M. Valant, I. Arčon, I. Mikulska, and D. Lisjak, Cation Order-Disorder Transition in Fe-Doped 6H-$BaTiO_3$ for Dilute Room-Temperature Ferromagnetism, Chem. Mater. **25**, 3544 (2013).

[26] T. Tietze, M. Gacic, G. Schütz, G. Jakob, S. Brück, and E. Goering, XMCD studies on Co and Li doped ZnO magnetic semiconductors, New J. Phys. **10**, 055009 (2008).

[27] L. V. Bekenov, V. N. Antonov, S. Ostanin, A. N. Yaresko, I. V. Maznichenko, W. Hergert, I. Mertig, and A. Ernst, Electronic and magnetic properties of $(Zn_{1-x}V_x)$O diluted magnetic semiconductors elucidated from x-ray magnetic circular dichroism at V $L_{2,3}$ edges and first-principles calculations, Phys. Rev. B **84**, 134421 (2011).

[28] I. Lorite, B. Straube, H. Ohldag, P. Kumar, M. Villafuerte, P. Esquinazi, C. E. Rodríguez Torres, S. Perez de Heluani, V. N. Antonov, L. V. Bekenov, A. Ernst, M. Hoffmann, S. K. Nayak, W. A. Adeagbo, G. Fischer, and W. Hergert, Advances in methods to obtain and characterise room temperature magnetic ZnO, Appl. Phys. Lett. **106**, 082406 (2015).

[29] C. E. Rodríguez Torres, G. A. Pasquevich, P. M. Zélis, F. Golmar, S. P. Heluani, S. K. Nayak, W. A. Adeagbo, W. Hergert, M. Hoffman, A. Ernst, P. Esquinazi, and S. J. Stewart, Oxygen-vacancy-induced local ferromagnetism as a driving mechanism in enhancing the magnetic response of ferrites, Phys. Rev. B **89**, 104411 (2014).

[30] I. Mikulska, M. Valant, I. Arčon, and D. Lisjak, X-ray absorption spectroscopy studies of the room-temperature ferromagnetic Fe-doped 6H-$BaTiO_3$, J. Am. Ceram. Soc. **98**, 1156 (2015).

[31] R. Böttcher, H. T. Langhammer, S. Kücker, C. Eisenschmidt, and S. G. Ebbinghaus, On the incorporation of iron into hexagonal barium titanate: I. electron paramagnetic resonance (EPR) study, J. Phys.: Condens. Matter **30**, 425701 (2018).

[32] S. K. Nayak, H. T. Langhammer, W. A. Adeagbo, W. Hergert, T. Müller, and R. Böttcher, Chromium point defects in hexagonal $BaTiO_3$: A comparative study of first-principles calculations and experiments, Phys. Rev. B **91**, 155105 (2015).

[33] G. Demazeau, B. Buffat, M. Pouchard, and P. Hagenmuller, Recent developments in the field of high oxidation states of transition elements in oxides stabilization of six-coordinated Iron(V), Z. Anorg. Allg. Chem. **491**, 60 (1982).

[34] A. Walsh, A. A. Sokol, J. Buckeridge, D. O. Scanlon, and C. R. A. Catlow, Oxidation states and ionicity, Nat. Mater. **17**, 958 (2018).

[35] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.100.184108 for details about the computational setup such as the choice of correlation correction and charge compensation modeling, the calculation of formation energy detail, the crystal structure of $BaTiO_3$, the partial electronic density of states and charge density of Fe, and the change of Fe-Ti distances in the $FeTiO_9$ complex with respect to the charge states on the Fe.

[36] J. K. Shenton, D. R. Bowler, and W. L. Cheah, Effects of the Hubbard U on density functional-based predictions of $BiFeO_3$ properties, J. Phys.: Condens. Matter **29**, 445501 (2017).

[37] G. Rollmann, P. Entel, A. Rohrbach, and J. Hafner, High-pressure characteristics of $\alpha$-$Fe_2O_3$ using DFT+U, Phase Transitions **78**, 251 (2005).

[38] S. W. Hoh, L. Thomas, G. Jones, and D. J. Willock, A density functional study of oxygen vacancy formation on $\alpha$-$Fe_2O_3$(0001) surface and the effect of supported Au nanoparticles, Res. Chem. Intermed. **41**, 9587 (2015).

[39] J. P Perdew, Unified theory of exchange and correlation beyond the local density approximation, in *Electronic Structure of Solids '91*, edited by P. Ziesche and H. Eschrig, Physical Research (Akademie Verlag, Berlin, 1991), Vol. 17, pp. 11–20.

[40] G. Kresse and J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. **6**, 15 (1996).

[41] G. Kresse and J. Furthmüller, Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set, Phys. Rev. B **54**, 11169 (1996).

[42] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B **50**, 17953 (1994).

[43] G. Kresse and D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B **59**, 1758 (1999).

184108-10

[44] V. I. Anisimov, J. Zaanen, and O. K. Andersen, Band theory and Mott insulators: Hubbard U instead of Stoner I, *Phys. Rev. B* **44**, 943 (1991).

[45] A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Density-functional theory and strong interactions: Orbital ordering in Mott-Hubbard insulators, *Phys. Rev. B* **52**, R5467(R) (1995).

[46] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA+U study, *Phys. Rev. B* **57**, 1505 (1998).

[47] G. A. Baraff and M. Schlüter, Electronic Structure, Total Energies, and Abundances of the Elementary Point Defects in GaAs, *Phys. Rev. Lett.* **55**, 1327 (1985).

[48] S. B. Zhang and J. E. Northrup, Chemical Potential Dependence of Defect Formation Energies in GaAs: Application to Ga Self-Diffusion, *Phys. Rev. Lett.* **67**, 2339 (1991).

[49] J. Neugebauer and C. G. Van de Walle, Atomic geometry and electronic structure of native defects in GaN, *Phys. Rev. B* **50**, 8067(R) (1994).

[50] S. Lany and A. Zunger, Assessment of correction methods for the band-gap problem and for finite-size effects in supercell defect calculations: Case studies for ZnO and GaAs, *Phys. Rev. B* **78**, 235104 (2008).

[51] C. G. Van de Walle and J. Neugebauer, First-principles calculations for defects and impurities: Applications to III-nitrides, *J. Appl. Phys.* **95**, 3851 (2004).

[52] K. Reuter and M. Scheffler, Composition, structure, and stability of $RuO_2$(110) as a function of oxygen pressure, *Phys. Rev. B* **65**, 035406 (2001).

[53] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and K. A. Persson, The Materials Project: A materials genome approach to accelerating materials innovation, *APL Materials* **1**, 011002 (2013).

[54] A. Sabry, M. Ayadi, and A. Chouikh, Simulation of ionic crystals and calculation of electrostatic potentials, *Comp. Mater. Sci* **18**, 345 (2000).

[55] T. Allison, *JANAF Thermochemical Tables, NIST Standard Reference Database 13* (National Institute of Standards and Technology, 1996).

[56] R. F. W. Bader, *Atoms in Molecules: A Quantum Theory* (Oxford University Press, Oxford, 1990).

[57] H. Raebiger, S. Lany, and A. Zunger, Charge self-regulation upon changing the oxidation state of transition metals in insulators, *Nature* (London) **453**, 763 (2008).

[58] C. L. Freeman, J. A. Dawson, H.-R. Chen, J. H. Harding, L.-B. Ben, and D. C. Sinclair, A new potential model for barium titanate and its implications for rare-earth doping, *J. Mater. Chem.* **21**, 4861 (2011).

[59] J. Akimoto, Y. Gotoh, and Y. Oosawa, Refinement of hexagonal BaTiO₃, *Acta Crystallogr. Sect. C* **50**, 160 (1994).

[60] D. C. Sinclair, J. M. S. Skakle, F. D. Morrison, R. I. Smith, and T. P. Beales, Structure and electrical properties of oxygen-deficient hexagonal BaTiO₃, *J. Mater. Chem.* **9**, 1327 (1999).

[61] R. W. G. Wycoff, *Crystal Structures* (John Wiley and Sons, New York, 1965).