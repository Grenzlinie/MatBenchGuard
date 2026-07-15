# Potentially superhard hcp CrN₂ compound studied at high pressure

Zhonglong Zhao, Kuo Bao, Fubo Tian, Defang Duan, Bingbing Liu, and Tian Cui*

State Key Laboratory of Superhard Materials, College of Physics, Jilin University, Changchun 130012, China
(Received 10 October 2015; revised manuscript received 2 May 2016; published 8 June 2016)

Motivated by recent developments in nitrogen-rich transition-metal nitrides, the stability of chromium mononitride (CrN) and the possible formation of chromium dinitride (CrN₂) are studied using density functional theory (with the Perdew-Burke-Ernzerhof functional within the generalized gradient approximation, local density approximation plus $U$, and Heyd-Scuseria-Ernzerhof hybrid exchange-correlation potentials), $ab$ $initio$ evolutionary algorithm, as well as $ab$ $initio$ molecular dynamics. It is found that low-temperature orthorhombic CrN will transform into a hexagonal-close-packed (hcp) structure at above 108 GPa. Two hcp CrN₂, constructed by replacing the interstitial nitrogen in hcp CrN with nitrogen-nitrogen units, are predicted to be stable at above 7 GPa due to the physics of precompression. We show that the Cr-N bond length in hcp CrN₂ at 0 GPa is comparable to that of the CrN prototype at more than 45 GPa, and the electrons have been transformed from itinerant to localized, which results in unique metal-insulator transitions and a high hardness of 46 GPa. These results, therefore, provide crucial insights for designing covalence-dominated transition-metal compounds.

DOI: 10.1103/PhysRevB.93.214104

## I. INTRODUCTION

The design of new materials in transition-metal (TM) light-element (LE = B, C, N, and O) compounds with hardness rivaling traditional superhard materials (e.g., diamond and $c$-BN) has been one of the central themes of material science for over a decade [1,2]. The origin of the unusual high hardness is associated with the formation of three-dimensional (3D) covalent networks driven by directional hybridizations of LE $s,p$-TM $d$ electrons, which can effectively restrain nondirectional metallic bonds in pure metals [1]. The nature of TM-LE and LE-LE bonding (e.g., covalent or not), therefore, is a key factor influencing the hardness [3]. While promising superhard TM-LE compounds including OsB₂ [2], ReB₂ [4], FeB₄ [5], PtN₂ [6,7], IrN₂ [8], Re₂N [9], and Re₃N [9] with a large bulk modulus (close to 400 GPa) have been designed in the past decade, high synthesis conditions and weak metallic bonding are two of the most challenging troubles to overcome [10–13]. For example, the pressures required for synthesizing TM nitrides, e.g., platinum metal nitrides [6–8], $\eta$-Ta₂N₃ [14], and Re subnitrides [9], are relatively high and beyond the current capability for massive production. In addition, the hardness of boron-rich compounds such as OsB₂,ReB₂, and FeB₄ are typically below 30 GPa due to metallic TM-TM interactions [11] and (or) weak TM-LE bondings [10,12,13].

It is believed that the hardness of heavier TMs will not be increased significantly in their nitride phases [15]. However, a semiconductor PtN₂ with strong covalence and high hardness has been synthesized at high pressures (~45–50 GPa) and high temperatures (>2000 K) with the incorporation of N-N units into the Pt lattice [6,7,10,16,17]. Meaningfully, the extended studies [16,18] proved that the interstitial N-N unit plays a key role in developing hard TM nitrides, resulting in pyrite-type $3d$ TM nitrides that include MnN₂,CoN₂, and NiN₂ [18]. In this paper, we corroborate that the mechanism of action of merging the N-N units into TMs could be a kind of precompression physics. We show that hexagonal-close-packed (hcp) chromium dinitride (CrN₂) can be formed by a combination of high pressure [i.e., the pressure-volume (PV) works] and N-N precompression (i.e., the N-N unit interstitial), at a moderate pressure around 7 GPa, which possesses a high hardness of 46 GPa. By a detailed electronic structure analysis, we prove that both the charge distribution and bonding are tunable with N-N interstitial compression, resulting in strong covalence and a unique metal-insulator transition.

## II. COMPUTATIONAL DETAILS

First-principles calculations are performed by using the Vienna $ab$ $initio$ simulation package (VASP) [19] and the projector-augmented wave (PAW) method [20]. Both the Perdew-Burke-Ernzerhof functional within the generalized gradient approximation (GGA-PBE) [21] and local density approximation plus $U$ (LDA+$U$) [22–24] methods are used to describe the exchange-correlation potential. An effective on-site Coulomb repulsion $U = 3$ eV as suggested by Alling $et$ $al.$ [25] for CrN is applied to the Cr $3d$ orbitals according to the scheme of Dudarev $et$ $al.$ [24]. The Heyd-Scuseria-Ernzerhof (HSE) hybrid functional [26–28] is also used to examine the PBE and LDA+$U$ calculations. By performing accurate convergence tests, a cutoff energy of 520 eV and a Monkhorst-Pack $k$ mesh of $0.03 \times 2\pi$ Å⁻¹ are chosen, which ensures the total energies are well converged to better than 1 meV/formula units (f.u.). A magnetic ordering with an alternation of single Cr ferromagnetic (FM) sheets along the [0001] direction is considered as the antiferromagnetic (AF) state for hexagonal Cr-N compounds, as proposed by Miao $et$ $al.$ for NiAs-type MnN, CrN, and VN [29]. The magnetic disorder of paramagnetic (PM) cubic CrN is simulated by means of a special quasirandom structure method [25,30], using a 48-atom supercell to guarantee a zero spin correlation function in the first five coordination shells. The mechanical and dynamical stabilities are tested by the elastic constants (Born-Huang criteria [31]) and phonon frequencies, calculated with the strain-stress method [32] and the direct supercell method [33,34], respectively.

*cuitian@jlu.edu.cn

Zero-temperature crystal structure predictions are performed using the *ab initio* evolutionary algorithm USPEX code [35–37]. Structure cells with Cr:N ratios of 1:1, 1:1.5, 1:2, 1:3, and 1:4 within 2 and 4 f.u. are implemented at 0, 50, and 100 GPa, respectively. During the structure search, the first generation is produced randomly, and succeeding generations are obtained by applying 60% heredity, 10% atom transmutation, and 30% lattice mutation operations, respectively. The global stability of Cr-N compounds is investigated by constructing convex hulls at different pressures, defined as $H_{\text{form}}(\text{Cr}_x\text{N}_y) = [H(\text{Cr}_x\text{N}_y) - x H(\text{Cr}) - y H(\text{N})]$. Any structure with the formation enthalpy lying on the convex hull is considered to be thermodynamically stable. The enthalpies of bcc Cr and nitrogen in high-pressure phase order [38] are adopted as the reference of thermodynamics.

High-temperature effects on the structural stability are examined with *ab initio* molecular dynamics (MD) simulations using the *NVT* ($N$ number of particles, $V$ volume, $T$ temperature) ensemble [39–41], as implemented in the VASP code. The $\text{LDA} + U$ ($U=3$ eV) functional is considered. The model employed for $\text{CrN}_2$ contains 144 atoms, and the duration of each MD simulation is 20 ps (with a time step of 2 fs). The plane-wave cutoff is chosen as 520 eV for all MD simulations, and the Brillouin zone integration is restricted to the $\Gamma$ point of the supercell.

## III. RESULTS AND DISCUSSIONS

### A. Electron correlations and the stability of CrN

Room-temperature CrN is crystallized in a PM cubic rock-salt (rs) structure [42,43]. Below $\sim$273–286 K, it distorts into an AF orthorhombic phase with a magnetic ordering consisting of double FM sheets stacked antiferromagnetically along the [110] direction (denoted as orth-CrN or $\text{AF}^2[110]$-CrN) [42–45]. Within PBE, however, the experimental cubic and orthorhombic CrN are metastable compared with two small-volume nonmagnetic (NM) hexagonal CrN phases (WC and NiAs type), as showed in Fig. 1. This discrepancy tells us that there is a failure of the mean field approach in describing the Cr-N system (the LDA [46] and PW91 [47] agree on the PBE results) and the electrons are strongly correlated. The PBE errors can be rectified by using revised functionals, e.g., $\text{LDA}+U$ [48] or HSE methods, and the orth-CrN is correctly predicted as the low-temperature ground state (see Fig. 1). The calculated electronic density of states for WC-CrN using PBE and $\text{LDA}+U$ are shown in Fig. 2. We find that the PBE anomaly stems mainly from the descriptions of the hexagonal phases, and is a result of a wrong evaluation of the interactions among Cr $3d$ orbitals, i.e., there is an $\sim$1.5 eV underestimation of the energy splitting between the majority and minority spins.

Considering the small-volume character of the hexagonal CrN phases, e.g., the equilibrium volume of the FM WC-CrN is $\sim$10% less than that of orth-CrN calculated with $\text{LDA}+U$, high pressure is expected to be favorable for their stability. Our results indicate that WC-CrN is thermodynamically more stable than orth-CrN at above 108.4 GPa (see Fig. 3(a)], which can be attributed to the effects of the PV works, i.e., the orth-CrN has a relatively larger volume to sacrifice its enthalpy. However, the metallic nature of hexagonal CrN is maintained at high pressure, despite a rapid decline of the atomic magnetic moments. Note that both WC-CrN and NiAs-CrN are NM metals at even more than 100 GPa.

![](./images/811268059250556929_1.jpg)

FIG. 1. Energy vs volume ($E$-$V$) curves of different structures and magnetic states of CrN calculated with PBE and $\text{LDA}+U$ methods, respectively. HSE relative energies are given in stars. The $\text{AF}^1[110]$ is similar to the $\text{AF}^2[110]$ but with a single FM sheet alternately along the [110] direction.

### B. Precompression of N-N units and the stability of $\text{CrN}_2$

We study the effects of N-N units on Cr-N compounds by substituting the interstitial nitrogen with a N-N dimer in three hexagonal CrN phases (WC-, NiAs-, and AsNi-type structures are adopted as the prototypes), oriented in the [0001] direction to maintain the crystal symmetry and atomic coordination [see Figs. 4(a)–4(f)]. By allowing the structure to fully relax, we find that the equilibrium Cr-N distances in three $\text{CrN}_2$ (denoted as $\text{WC-CrN}_2$, $\text{NiAs-CrN}_2$, and $\text{AsNi-CrN}_2$) have

![](./images/811268059250556929_2.jpg)

FIG. 2. Electronic density of states of proposed hexagonal Cr nitrides at 0 GPa calculated with PBE and $\text{LDA}+U$ methods. The vertical dashed lines indicate the Fermi levels. The $\text{LDA}+U$ energy corrections for the spin splitting of WC-CrN are depicted in the black shadow.

![](./images/811268059250556929_3.jpg)

FIG. 3. Calculated (a) enthalpy difference vs pressure ($H_{\text{diff}}$-$P$) curves of CrN, (b) formation enthalpy vs pressure ($H_{\text{form}}$-$P$) curves of CrN$_2$, and (c) the convex hull diagram of Cr-N system at 10 GPa with LDA+$U$ method.

been compressed about 4.4% compared with those in the CrN prototypes, which are comparable to the lengths of the CrN phases at above 45 GPa. This result tells us that the approach of replacing the interstitial nitrogen with a N-N unit can make these hexagonal CrN phases as in a sort of compression (adding chemical pressure), and therefore reduces the pressures of synthesis. According to Fig. 3(b), WC-CrN$_2$ and AsNi-CrN$_2$ can be stable at above $\sim$7.3 GPa toward decomposition into orth-CrN and nitrogen (the enthalpy difference of WC-CrN$_2$ relative to AsNi-CrN$_2$ is only 0.06 eV/f.u. at 0 GPa). The cubic pyrite-type CrN$_2$ is not favorable compared to the hexagonal phases during the pressures considered [Fig. 3(b)].

To further test the stability of these hexagonal CrN$_2$ phases, we have simulated the zero-temperature high-pressure phase diagram of the Cr-N system toward different compositions by using the USPEX code [35-37]. The WC- and AsNi- type CrN$_2$ can be derived from the fourth and the 23rd generations (25 structures per generation) in 2 f.u. USPEX simulations at 0 GPa. These two CrN$_2$ phases are also the most stable phases during the 4 f.u. simulations at 0, 50, and 100 GPa, respectively. According to Fig. 3(c), the CrN$_2$ phases are thermodynamically stable toward decomposition into experimental orth-CrN and nitrogen at above their stable pressures. On the other hand, the dynamic and mechanical stabilities of CrN$_2$ have been tested by elastic constants and phonon curves. The proposed CrN$_2$ structures are dynamically and mechanically stable at 0 GPa because the calculated elastic constants meet the Born-Huang stability criteria [31] and no imaginary phonon frequency exists in the Brillouin zone (see Fig. 5 and Supplemental Material Table I [49]), which also implies that they are recoverable to ambient pressure.

![](./images/811268059250556929_4.jpg)

FIG. 4. Crystal structures and electron localization functions (ELFs) of (a) WC-CrN, (b) NiAs-CrN, (c) AsNi-CrN, (d) WC-CrN$_2$, (e) NiAs-CrN$_2$, and (f) AsNi-CrN$_2$ with the scales running from 0 (blue) to maximum (red). Bader charges (bold italics) and cell parameter $a$ are indicated. The calculated (0001) plane ELFs of WC-CrN$_2$ and NiAs-CrN$_2$ are showed in (g) and (h) with the same scales. The 3D bonding topologies of (i) N $\equiv$ N triple bond in $\alpha$-N$_2$, (j) N = N double bond in BaN$_2$, and (k) N-N single bond in pyrite-PtN$_2$ are showed with an isosurface at ELF = 0.85. The N-N single bonding pictures of WC-CrN$_2$ and AsNi-CrN$_2$ are shown in (l) and (m) with the same level. Data in (a)-(h) are calculated with LDA+$U$, while in (i)-(m) they are achieved with PBE for comparability. All data are calculated at 0 GPa.

![](./images/811268059250556929_5.jpg)

FIG. 5. Phonon dispersion curves of (a) WC-CrN₂ and (b) AsNi-CrN₂ at 0 GPa along the high symmetry directions of the Brillouin zone.

Thermal analysis experiments found that CrN coatings decomposed into Cr₂N and N₂ at above ~925 °C, and Cr₂N will sequentially decompose to Cr and N₂ at above ~1120 °C [50]. The decomposition of CrN₂ at high temperature, however, is not expected due to the strong Cr-N and N-N covalent bonds, as will be discussed below. Actually, platinum metal dinitrides (e.g., OsN₂, IrN₂, and PtN₂) with similar N-N interstitial configurations can survive at temperatures of more than 2000 K [6-8]. Besides, we have simulated the dynamical evolution of CrN₂ at high temperatures using the MD method. A 144-atom supercell constructed from the zero-pressure structure of AsNi-CrN₂ is chosen as the initial structure and heated gradually to reference temperatures at 500, 1000, 1500, and 2000 K (the heating rate is 0.25 K/fs). At each reference temperature, we performed 20 ps NVT MD simulations to get the equilibrium configuration and sample the radial distribution function (RDF) g(r), as showed in Fig. 6. It is shown that there are single RDF peaks at around 1.32 and 1.94 Å corresponding to the N-N and Cr-N bonds at zero temperature that remain unshifted (with an error of less than 2%) at high temperatures up to 2000 K, and which support the stability of CrN₂ at high temperatures.

<table>
<caption>TABLE I. Calculated zero-pressure lattice parameters, $a$,$c$, unit cell volume $V_0$, and atomic magnetic moment $M$ of hexagonal Cr-N compounds with different exchange-correlation potentials.</caption>
<thead>
  <tr>
    <th>Phases</th>
    <th>$E_{\text{xc}}$</th>
    <th>$a$ (Å)</th>
    <th>$c$ (Å)</th>
    <th>$V_0$(Å³)</th>
    <th>$M$($\mu_B$/Cr)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>WC-CrN (FM)</td>
    <td>PBE</td>
    <td>2.681</td>
    <td>2.599</td>
    <td>16.17</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td></td>
    <td>LDA+$U$</td>
    <td>2.663</td>
    <td>2.556</td>
    <td>15.70</td>
    <td>0.916</td>
  </tr>
  <tr>
    <td></td>
    <td>HSE</td>
    <td>2.701</td>
    <td>2.583</td>
    <td>16.32</td>
    <td>1.309</td>
  </tr>
  <tr>
    <td>NiAs-CrN (AF)</td>
    <td>PBE</td>
    <td>2.703</td>
    <td>5.146</td>
    <td>16.28</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td></td>
    <td>LDA+$U$</td>
    <td>2.901</td>
    <td>4.895</td>
    <td>17.85</td>
    <td>2.697</td>
  </tr>
  <tr>
    <td></td>
    <td>HSE</td>
    <td>2.926</td>
    <td>4.938</td>
    <td>18.31</td>
    <td>2.777</td>
  </tr>
  <tr>
    <td>AsNi-CrN (FM)</td>
    <td>PBE</td>
    <td>2.725</td>
    <td>5.087</td>
    <td>16.36</td>
    <td>0.511</td>
  </tr>
  <tr>
    <td></td>
    <td>LDA+$U$</td>
    <td>2.825</td>
    <td>5.032</td>
    <td>17.39</td>
    <td>2.617</td>
  </tr>
  <tr>
    <td></td>
    <td>HSE</td>
    <td>2.894</td>
    <td>5.196</td>
    <td>18.84</td>
    <td>3.114</td>
  </tr>
  <tr>
    <td>WC-CrN₂</td>
    <td>PBE</td>
    <td>2.725</td>
    <td>3.712</td>
    <td>23.86</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td></td>
    <td>LDA+$U$</td>
    <td>2.675</td>
    <td>3.674</td>
    <td>22.76</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td></td>
    <td>HSE</td>
    <td>2.691</td>
    <td>3.659</td>
    <td>22.95</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td>NiAs-CrN₂ (AF)</td>
    <td>PBE</td>
    <td>2.726</td>
    <td>7.520</td>
    <td>24.21</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td></td>
    <td>LDA+$U$</td>
    <td>2.965</td>
    <td>7.055</td>
    <td>26.86</td>
    <td>2.983</td>
  </tr>
  <tr>
    <td></td>
    <td>HSE</td>
    <td>3.013</td>
    <td>7.069</td>
    <td>27.78</td>
    <td>3.124</td>
  </tr>
  <tr>
    <td>AsNi-CrN₂</td>
    <td>PBE</td>
    <td>2.733</td>
    <td>7.382</td>
    <td>23.87</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td></td>
    <td>LDA+$U$</td>
    <td>2.682</td>
    <td>7.310</td>
    <td>22.77</td>
    <td>0.000</td>
  </tr>
  <tr>
    <td></td>
    <td>HSE</td>
    <td>2.698</td>
    <td>7.287</td>
    <td>22.97</td>
    <td>0.000</td>
  </tr>
</tbody>
</table>

![](./images/811268059250556929_6.jpg)

FIG. 6. Radial distribution functions $g_{\text{N-N}}(r)$ and $g_{\text{Cr-N}}(r)$ of the AsNi-CrN₂ supercell at different temperatures calculated with LDA+$U$ functional. The vertical gray lines indicate the equilibrium N-N and Cr-N bond lengths at 0 K.

Although the predicted stable pressure for CrN₂ is moderate, the introduction of additional nitrogen into the TM lattice may encounter a large energy barrier. For instance, Re₃N is predicted to be stable at zero pressure while the synthesis is at more than 13 GPa and 1600 K [9,51]. PtN₂ in a pyrite structure is calculated to be stable at above 15 GPa, while in the experiment the synthesis approaches 50 GPa and 2000 K [6,7,52]. Therefore, the synthesis of CrN₂ may also need additional high pressure (i.e., in the range of 20-50 GPa) and the assistance of high temperature. On the other hand, the exploration of an appropriate reaction route may be a further subject for CrN₂ synthesis. Note that MoS₂-type ReN₂ can be synthesized from a metathesis reaction between ReCl₅ and Li₃N at below 7.7 GPa [53].

### C. Metallic-covalent bonding transition induced by N-N interstitials

According to Fig. 2, hexagonal CrN₂ displays semiconductor characteristics with a ~0.5 eV band gap at the Fermi level. Therefore, there is a metal (FM)-insulator (NM) transition induced by the N-N interstitials, which heralds a complex action of N-N compression that distinguishes it from that of the direct high-pressure method, i.e., the PV works, as clarified below.

$\text{N} \equiv \text{N}$ forms into a triple bond in molecule N₂, while it is transformed into a double bond $\text{N} = \text{N}$ in alkaline-earth metal nitrides such as in BaN₂ [54]. In addition, single bond N-N was also identified [16]. The multiple N-N bonding can be distinguished with electron localizability in the position space and the filling of orbitals. The N-N single bond in CrN₂ differs substantially in its fulfilled antibonding $1\pi_g^*$ molecular orbital (Fig. 7), as indicated first by Wessel *et al.* for PtN₂ [16]. In BaN₂ and molecule N₂, the double ($\text{N} = \text{N}$) and triple ($\text{N} \equiv \text{N}$) bonds are manifested by large ionic charges or lone pairs on the sides of the N₂ unit [see Figs. 4(i) and 4(j)]. The N-N

![](./images/811268059250556929_7.jpg)

FIG. 7. Crystal orbital Hamilton population (COHP) analyses for CrN and ${\rm CrN_2}$ compounds at 0 GPa. The data are calculated with ${\rm LDA}+U$ and the analysis is performed with the projected COHP (pCOHP) method. The horizontal line at zero is the Fermi level.

single bond morphology is also verified by a more prominent ${\rm Cr-N_2}$ charge transfer ($\sim 0.12e$) in ${\rm CrN_2}$ compared with that in CrN, as marked in Figs. 4(a) and 4(d). Sandwiching the N-N unit in neighboring Cr layers, as a result, can localize the (spherical) itinerant electrons (around the nitrogen atoms in CrN) into N $2p$-Cr $3d$ hybrid orbitals, depleting the partially filled Cr-N antibonding states and transforming them into fulfilled bonding and antibonding states, as proved by the crystal orbital Hamilton population (COHP) analysis [55,56] in Fig. 7. The Cr-N bonding, therefore, has been transformed from a weak metallic bonding to a strongly covalent one, which is further supported by the increase of the electron localization function (ELF) maxima from 0.65 to 0.75 [see Figs. 4(a)–4(f)].

### D. 2D insulativity in ${\rm CrN_2}$

The (000$x$) Cr layers in ${\rm CrN_2}$ should be two-dimensional (2D) insulators since the compression of the N-N unit is uniaxial and makes less of a difference for the Cr intraplane lattice, as labeled in Figs. 4(a)–4(f). The ELFs of the (0001) Cr layer of ${\rm WC-CrN_2}$, ${\rm NiAs-CrN_2}$, and ${\rm AsNi-CrN_2}$ are depicted in Figs. 4(g) and 4(h), and Supplemental Material Fig. 1 [49] to understand the 2D insulativity. In ${\rm WC-CrN_2}$ and AsNi-${\rm CrN_2}$,N-N units adopt a simple hexagonal $AA$ arrangement and the neighboring N-N layers overlap with each other along the $c$ axis [Fig. 4(g)]. The Coulomb repulsion between the bonding pairs in adjacent six N-N units [labeled as numbers 1–6 in Fig. 4(g)] can fix the conduction electrons of the Cr layer into the center of every half Cr diamond, with the remaining half Cr diamond left empty [yellow lines in Fig. 4(g)]. The conduction electrons in the 2D Cr layers are therefore shielded. This insulating mechanism, however, cannot be reproduced by ${\rm NiAs-CrN_2}$ due to an $ABAB$ layered pattern of the N-N units along the $c$ axis [Fig. 4(h)]. The electrons in the 2D Cr layer are weakly localized and interconnected. In addition, the $ABAB$ pattern of the N-N sublattice can significantly decrease the Cr interlayer spacing (Table I), promoting the ${\rm Cr-N_2}$-Cr magnetic superexchange interactions [57] and leading to AF spin coupling [Fig. 3(b)].

<table>
<caption>TABLE II. Calculated zero-pressure bulk modulus $B$, shear modulus $G$, and Young’s modulus $E$ of Cr nitrides with different exchange-correlation potentials in comparison with available experimental results and the values of typical transition-metal compounds such as ${\rm ReB_2}$,${\rm PtN_2}$, and ${\rm FeB_4}$.</caption>
<thead>
  <tr>
    <th>Phases</th>
    <th></th>
    <th>$B$ (GPa)</th>
    <th>$G$ (GPa)</th>
    <th>$E$ (GPa)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>cubic-CrN (PM)</td>
    <td>GGA</td>
    <td>$247^{\rm a}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>${\rm LDA}+U$</td>
    <td>$288^{\rm a}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Ref. [45]</td>
    <td>257</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>${\rm orth\text{-}CrN\ (AF^2[110])}$</td>
    <td>GGA</td>
    <td>258</td>
    <td>150</td>
    <td>378</td>
  </tr>
  <tr>
    <td></td>
    <td>${\rm LDA}+U$</td>
    <td>281</td>
    <td>190</td>
    <td>465</td>
  </tr>
  <tr>
    <td></td>
    <td>Ref. [45]</td>
    <td>262</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>${\rm WC\text{-}CrN_2}$</td>
    <td>GGA</td>
    <td>327</td>
    <td>235</td>
    <td>570</td>
  </tr>
  <tr>
    <td></td>
    <td>${\rm LDA}+U$</td>
    <td>366</td>
    <td>256</td>
    <td>622</td>
  </tr>
  <tr>
    <td>${\rm AsNi\text{-}CrN_2}$</td>
    <td>GGA</td>
    <td>326</td>
    <td>231</td>
    <td>561</td>
  </tr>
  <tr>
    <td></td>
    <td>${\rm LDA}+U$</td>
    <td>364</td>
    <td>252</td>
    <td>615</td>
  </tr>
  <tr>
    <td>${\rm ReB_2}$</td>
    <td>GGA</td>
    <td>345</td>
    <td>271</td>
    <td>645</td>
  </tr>
  <tr>
    <td></td>
    <td>Ref. [4]</td>
    <td>360</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>${\rm Pyrite\text{-}PtN_2}$</td>
    <td>GGA</td>
    <td>289</td>
    <td>183</td>
    <td>453</td>
  </tr>
  <tr>
    <td></td>
    <td>Ref. [6]</td>
    <td>372</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>${\rm oP10\text{-}FeB_4}$</td>
    <td>GGA</td>
    <td>277</td>
    <td>186</td>
    <td>456</td>
  </tr>
  <tr>
    <td></td>
    <td>Ref. [5]</td>
    <td>252</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="5">${}^{\rm a}$Fitted by Birch-Murnaghan third-order equation of state (EOS) [61].</td>
  </tr>
</tfoot>
</table>

### E. High hardness induced by strong covalence

Our results proved that the origin of insulativity of ${\rm CrN_2}$ stems from a collaboration of strong N $2p$-Cr $3d$ orbital hybridization and electron-electron Coulomb repulsion. The strong covalence results in a demagnetization effect for hexagonal ${\rm CrN_2}$ (Table I), which in turn makes PBE a valid functional in describing the structures and electronic states (Table I and Fig. 2). The strong covalence dramatically strengthens the lattice. According to Table II, the calculated bulk modulus ($B$), shear modulus ($G$), and Young's modulus ($E$) of ${\rm WC-CrN_2}$ and ${\rm AsNi-CrN_2}$ are 30%, 43%, and 40% higher than those of cubic-CrN and orth-CrN, which catch the level of high hardness materials such as ${\rm PtN_2}$,${\rm ReB_2}$, and ${\rm FeB_4}$ [4–6]. Besides, the calculated 46 GPa hardnesses using the electronegativity model [58] for these two phases are above the threshold of superhard material (40 GPa) (see Supplemental Material Table II [49]).

We have clarified that the polymerized N-N unit plays important roles in lowering the pressure of synthesis as well as in the disappearance of the metallic bonding of Cr nitrides. The mechanism of interstitial compression is not limited to Cr nitrides and the form of nitrogen polymerization. Actually, nitrogen in a multiform, e.g., crooked N-N-N units and even nitrogen chains, can be used to reduce the metallicity of Re nitrides [59]. In addition, isostructural hexagonal tungsten dinitrides [60], besides the well-known pyrite-${\rm PtN_2}$, are predicted to have an analogous semiconducting superhard nature.

## IV. CONCLUSIONS

In summary, we have shown that it is possible to wipe out the metallic bonding and transform Cr-N compounds into hexagonal superhard materials ${\text{CrN}}_{2}$ with polymerized N-N interstitials, as supported by advanced density functional theory calculations, crystal structure prediction methods, and $ab$ initio molecular dynamics simulations. This is a consequence of the localization of itinerant electrons into $p$-$d$ hybrid orbitals along with the metallic-covalent Cr-N bonding transition in nature induced by the cooperation of high pressure and N-N precompression. Also, we have shown that $3d$ electron-electron Coulomb repulsion plays an important role in restricting the conduction electrons, resulting in unique 2D metal insulativity. Our results uncover the physical origin of a different class of hard TM nitrides that feature a high nitrogen contents and polymerized nitrogen atoms, which shed light on a promising approach for the design of covalent superhard TM-LE compounds.

## ACKNOWLEDGMENTS

This work was supported by the National Basic Research Program of China (No. 2011CB808200), National Natural Science Foundation of China (No. 51572108 and No. 51032001), Program for Changjiang Scholars and Innovative Research Team in University (No. IRT1132), and National Found for Fostering Talents of basic Science (No. J1103202). Parts of the calculations were performed in the High Performance Computing Center (HPCC) of Jilin University.

[1] R. B. Kaner, J. J. Gilman, and S. H. Tolbert, *Science* **308**, 1268 (2005).
[2] R. W. Cumberland, M. B. Weinberger, J. J. Gilman, S. M. Clark, S. H. Tolbert, and R. B. Kaner, *J. Am. Chem. Soc.* **127**, 7264 (2005).
[3] S.-H. Jhi, J. Ihm, S. G. Louie, and M. L. Cohen, *Nature* (London) **399**, 132 (1999).
[4] H.-Y. Chung, M. B. Weinberger, J. B. Levine, A. Kavner, J.-M. Yang, S. H. Tolbert, and R. B. Kaner, *Science* **316**, 436 (2007).
[5] H. Gou, N. Dubrovinskaia, E. Bykova, A. A. Tsirlin, D. Kasinathan, W. Schnelle, A. Richter, M. Merlini, M. Hanfland, A. M. Abakumov, D. Batuk, G. Van Tendeloo, Y. Nakajima, A. N. Kolmogorov, and L. Dubrovinsky, *Phys. Rev. Lett.* **111**, 157002 (2013).
[6] E. Gregoryanz, C. Sanloup, M. Somayazulu, J. Badro, G. Fiquet, H.-K. Mao, and R. J. Hemley, *Nat. Mater.* **3**, 294 (2004).
[7] J. C. Crowhurst, A. F. Goncharov, B. Sadigh, C. L. Evans, P. G. Morrall, J. L. Ferreira, and A. J. Nelson, *Science* **311**, 1275 (2006).
[8] A. F. Young, C. Sanloup, E. Gregoryanz, S. Scandolo, R. J. Hemley, and H.-K. Mao, *Phys. Rev. Lett.* **96**, 155501 (2006).
[9] A. Friedrich, B. Winkler, L. Bayarjargal, W. Morgenroth, E. A. Juarez-Arellano, V. Milman, K. Refson, M. Kunz, and K. Chen, *Phys. Rev. Lett.* **105**, 085504 (2010).
[10] X. Guo, L. Li, Z. Liu, D. Yu, J. He, R. Liu, B. Xu, Y. Tian, and H.-T. Wang, *J. Appl. Phys.* **104**, 023503 (2008).
[11] J. Yang, H. Sun, and C. F. Chen, *J. Am. Chem. Soc.* **130**, 7200 (2008).
[12] C. Zang, H. Sun, J. S. Tse, and C. Chen, *Phys. Rev. B* **86**, 014108 (2012).
[13] B. Li, H. Sun, and C. Chen, *Phys. Rev. B* **90**, 014106 (2014).
[14] A. Zerr, G. Miehe, J. W. Li, D. A. Dzivenko, V. K. Bulatov, H. Höfer, N. Bolfan-Casanova, M. Fialin, G. Brey, T. Watanabe, and M. Yoshimura, *Adv. Funct. Mater.* **19**, 2282 (2009).
[15] J. C. Grossman, A. Mizel, M. Côté, M. L. Cohen, and S. G. Louie, *Phys. Rev. B* **60**, 6343 (1999).
[16] M. Wessel and R. Dronskowski, *J. Am. Chem. Soc.* **132**, 2421 (2010).
[17] A. F. Young, J. A. Montoya, C. Sanloup, M. Lazzeri, E. Gregoryanz, and S. Scandolo, *Phys. Rev. B* **73**, 153102 (2006).
[18] Z. T. Y. Liu, D. Gall, and S. V. Khare, *Phys. Rev. B* **90**, 134102 (2014).
[19] G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).
[20] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).
[21] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).
[22] D. M. Ceperley and B. J. Alder, *Phys. Rev. Lett.* **45**, 566 (1980).
[23] V. I. Anisimov, J. Zaanen, and O. K. Andersen, *Phys. Rev. B* **44**, 943 (1991).
[24] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, *Phys. Rev. B* **57**, 1505 (1998).
[25] B. Alling, T. Marten, and I. A. Abrikosov, *Phys. Rev. B* **82**, 184430 (2010).
[26] J. Heyd, G. E. Scuseria, and M. Ernzerhof, *J. Chem. Phys.* **118**, 8207 (2003).
[27] J. Heyd and G. E. Scuseria, *J. Chem. Phys.* **121**, 1187 (2004).
[28] J. Heyd, G. E. Scuseria, and M. Ernzerhof, *J. Chem. Phys.* **124**, 219906 (2006).
[29] M. S. Miao and W. R. L. Lambrecht, *Phys. Rev. B* **71**, 214405 (2005).
[30] A. Zunger, S. H. Wei, L. G. Ferreira, and J. E. Bernard, *Phys. Rev. Lett.* **65**, 353 (1990).
[31] Z.-J. Wu, E.-J. Zhao, H.-P. Xiang, X.-F. Hao, X.-J. Liu, and J. Meng, *Phys. Rev. B* **76**, 054115 (2007).
[32] R. Hill, *Proc. Phys. Soc. London, Sect. A* **65**, 349 (1952).
[33] A. Togo, F. Oba, and I. Tanaka, *Phys. Rev. B* **78**, 134106 (2008).
[34] A. Togo, F. Oba, and I. Tanaka, *Phys. Rev. B* **77**, 184101 (2008).
[35] A. R. Oganov and C. W. Glass, *J. Chem. Phys.* **124**, 244704 (2006).
[36] A. R. Oganov, A. O. Lyakhov, and M. Valle, *Acc. Chem. Res.* **44**, 227 (2011).
[37] A. O. Lyakhov, A. R. Oganov, H. T. Stokes, and Q. Zhu, *Comput. Phys. Commun.* **184**, 1172 (2013).
[38] C. J. Pickard and R. J. Needs, *Phys. Rev. Lett.* **102**, 125702 (2009).
[39] S. Nosé, *J. Chem. Phys.* **81**, 511 (1984).
[40] N. Shuichi, *Prog. Theor. Phys. Suppl.* **103**, 1 (1991).
[41] D. M. Bylander and L. Kleinman, *Phys. Rev. B* **46**, 13756 (1992).

[42] L. M. Corliss, N. Elliott, and J. M. Hastings, *Phys. Rev.* **117**, 929 (1960).

[43] J. D. Browne, P. R. Liddell, R. Street, and T. Mills, *Phys. Status Solidi A* **1**, 715 (1970).

[44] A. Filippetti and N. A. Hill, *Phys. Rev. Lett.* **85**, 5166 (2000).

[45] S. Wang, X. Yu, J. Zhang, M. Chen, J. Zhu, L. Wang, D. He, Z. Lin, R. Zhang, K. Leinenweber, and Y. Zhao, *Phys. Rev. B* **86**, 064111 (2012).

[46] W. Kohn and L. J. Sham, *Phys. Rev.* **140**, A1133 (1965).

[47] J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, *Phys. Rev. B* **46**, 6671 (1992).

[48] L. Zhou, F. Körmann, D. Holec, M. Bartosik, B. Grabowski, J. Neugebauer, and P. H. Mayrhofer, *Phys. Rev. B* **90**, 184102 (2014).

[49] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.93.214104 for calculated elastic constants, hardness parameters, space groups, atomic coordinates, and electron localization functions of hexagonal Cr-N compounds.

[50] W. Ernst, J. Neidhardt, H. Willmann, B. Sartory, P. H. Mayrhofer, and C. Mitterer, *Thin Solid Films* **517**, 568 (2008).

[51] R. F. Zhang, Z. J. Lin, H.-K. Mao, and Y. Zhao, *Phys. Rev. B* **83**, 060101 (2011).

[52] D. Åberg, B. Sadigh, J. Crowhurst, and A. F. Goncharov, *Phys. Rev. Lett.* **100**, 095501 (2008).

[53] F. Kawamura, H. Yusa, and T. Taniguchi, *Appl. Phys. Lett.* **100**, 251910 (2012).

[54] G. V. Vajenine, G. Auffermann, Y. Prots, W. Schnelle, R. K. Kremer, A. Simon, and R. Kniep, *Inorg. Chem.* **40**, 4866 (2001).

[55] V. L. Deringer, A. L. Tchougréeff, and R. Dronskowski, *J. Phys. Chem. A* **115**, 5461 (2011).

[56] S. Maintz, V. L. Deringer, A. L. Tchougréeff, and R. Dronskowski, *J. Comput. Chem.* **34**, 2557 (2013).

[57] P. W. Anderson, *Phys. Rev.* **115**, 2 (1959).

[58] K. Li, X. Wang, F. Zhang, and D. Xue, *Phys. Rev. Lett.* **100**, 235504 (2008).

[59] Z. L. Zhao, K. Bao, D. Li, D. F. Duan, F. B. Tian, X. L. Jin, C. B. Chen, X. L. Huang, B. B. Liu, and T. Cui, *Sci. Rep.* **4**, 4797 (2014).

[60] H. Wang, Q. Li, Y. Li, Y. Xu, T. Cui, A. R. Oganov, and Y. Ma, *Phys. Rev. B* **79**, 132109 (2009).

[61] F. Birch, *Phys. Rev.* **71**, 809 (1947).