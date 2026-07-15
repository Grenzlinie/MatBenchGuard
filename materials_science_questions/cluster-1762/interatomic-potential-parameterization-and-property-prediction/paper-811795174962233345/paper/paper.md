# Polar clusters in impurity-doped quantum paraelectric $\mathbf{K_{1-x}Li_xTaO_3}$

Grégory Geneste, $^{1,2}$ Jean-Michel Kiat, $^{2,3}$ Hiroko Yokota, $^{4}$ Yoshiaki Uesu, $^{4}$ and Florence Porcher $^{3}$

$^{1}$CEA, DAM, DIF, F-91297 Arpajon, France
$^{2}$Laboratoire Structures, Propriétés et Modélisation des Solides, CNRS-UMR 8580, Ecole Centrale Paris, Grande Voie des Vignes, 92295 Châtenay-Malabry Cedex, France
$^{3}$Laboratoire Léon Brillouin, CE Saclay CNRS-UMR 12, 91991 Gif-sur-Yvette Cedex, France
$^{4}$Department of Physics, Waseda University, 3-4-1 Okubo, Shinjuku-ku, Tokyo 169-0002, Japan

(Received 10 February 2010; revised manuscript received 15 March 2010; published 15 April 2010)

From density-functional calculations, we show that large off-center motions $(\approx 1.0$ Å) of Li impurities in the $KTaO_3$ matrix (studied at 3.7% concentration) create very anisotropic polar clusters oriented along the Li off-center dipole. The polarization induced by Li in the matrix decreases very sharply in the lateral directions so that polar clusters are only $\approx$ two lattice constants thick (one-dimensional or needlelike clusters). The polarization in such polar regions is mainly constituted by the displacements in the (highly polarizable) matrix rather than by the impurity itself. These results suggest that Li-doped potassium tantalate (3.7% concentration) is not ferroelectric at low temperature and rather behaves as a relaxor. These small polar zones around Li correlate at $T_B$ to form larger polar nanoregions, in which the matrix remains however nonpolar. This is confirmed by a low temperature neutron-diffraction analysis showing that the $KTaO_3$ matrix remains paraelectric. Li-doped $KTaO_3$ is an order-disorder system with a very deep local potential felt by the Li impurities $(\approx -200$ meV). The energy barrier for Li hopping is estimated at 80–90 meV. An analytic expression for this local potential is provided, as well as a simple model describing the energetics of $K_{1-x}Li_xTaO_3$.

DOI: 10.1103/PhysRevB.81.144112
PACS number(s): 77.84.Ek, 61.72.Dd

## I. INTRODUCTION

Quantum paraelectrics (QPs), in which zero-point motions suppress ferroelectricity (FE) (Ref. 1) have been the subject of numerous studies since long time because they display mostly intriguing behaviors, one of which being a saturation at very low temperature $(T<T_S)$ of the static dielectric permittivity $\epsilon_S$, that can reach in some cases gigantic values. Two famous systems exhibiting this behavior are $SrTiO_3$ (STO), for which $T_S$$\approx 35$ K and $\epsilon_S$$\approx 24000$, and $KTaO_3$ (KTO), for which $T_S$$\approx 16$ K and $\epsilon_S$$\approx 4000$. The intrinsic mechanisms of quantum paraelectricity are still a subject of debate. The existence of a FE instability in STO (in the cubic $Pm\overline{3}m$ parent phase as well as in the tetragonal $I4/mcm$ low-temperature phase) is quite well established from first-principles calculations, $^{2,3}$ and its suppression due to zero-point motions from path integral quantum Monte Carlo simulations. $^{4}$

However in KTO, no FE instability is found in the framework of the local density approximation (LDA) to density-functional theory (DFT): this compound exhibits only low-frequency TO modes. $^{5}$ Yet both materials present a similar evolution of the dielectric permittivity with temperature, i.e., a large increase followed by a saturation when $T$ is decreased down to zero Kelvin. It has been suggested that in KTO, the LDA fails to correctly reproduce the quantum paraelectric behavior, i.e., a weak FE instability which would be suppressed by quantum zero-point motions. This argument is strongly supported by Monte Carlo simulations. $^{6}$ However, the terahertz time-domain spectroscopy (THz-TDS) measurements of Ichikawa et al. $^{7}$ seem to confirm that the (stable) TO1 mode is responsible for the large dielectric response of KTO at low temperature. The question of an underlying FE instability in KTO is thus still under debate.

These “conventional” QPs have low saturation temperatures $T_S$. However, the possibility to shift $T_S$ to higher temperatures in view of technological applications (having a high dielectric-permittivity constant on a large temperature range due to saturation) is a challenge which points the need for a deeper understanding of such materials. Fifteen years ago, Kim et al. $^{8}$ and Inaguma et al. $^{9}$ found that two other compounds, $CaTiO_3$ (CTO) and $La_{1/2}Na_{1/2}TiO_3$ (LNTO), exhibit the same low-temperature dielectric behavior, but with a rather high $T_S$ ($\approx 50$ K for CTO and $\approx 90$ K for LNTO). Since the discovery of this unexpected “high-temperature quantum paraelectricity,” and even though smaller values of $\epsilon_S$ ($\approx 360$ and $\approx 170$, respectively) are measured in those compounds, the research on quantum paraelectric materials has gained new interest.

We have recently performed several studies of these quantum paraelectric compounds. In the case of LNTO, we have pointed out that this compound might have very weak ferroelectric instabilities, weaker than in STO and that the chemical disorder associated to the statistical occupation of La/Na on the A site is probably responsible for the low dielectric response and the structural distortions. $^{10,11}$ This could be a difference with CTO that does not have unstable modes in its ground-state orthorhombic structure according to the local density approximation to density functional theory, $^{12}$ suggesting that this compound is not a real quantum paraelectric crystal in the sense of a ferroelectric mode suppressed by quantum zero-point motions. $^{1}$ We have also focused on another perovskite compound, $BaZrO_3$ (BZO) and showed that it behaves like CTO and LNTO but with a much lower value of $T_S$ and $\epsilon_S$: $^{13}$ we have stressed that, contrary to STO and KTO, there is no FE instability in the BZO compound, but that zero-point motions are necessary to explain the quantitative $\epsilon_S(T)$ evolution and also probably the absence of oxygen octahedra rotations at low temperature (that do exist in

STO). Therefore BZO is, in essence, different from the quantum paraelectric compounds studied up to now.

This result regarding the role of disorder on $\epsilon_S$ in LNTO is interesting because the doping of quantum paraelectric by impurities or solid solution has been extensively studied. In particular, niobium, lithium, or sodium-doped potassium tantalate $KTaO_3$, or calcium-doped strontium titanate $SrTiO_3$ (SCT) were shown to have a dipole glass state for small doping rate but a ferroelectric state above a critical concentration, with strong consequences on the value of maximal permittivity and its temperature dependence. The intrinsic mechanisms responsible for this behavior in impurity-doped quantum paraelectrics remain unclear.

In such compounds the dipole moment of the *off-center* impurity ions and the corresponding reorientation dynamics are considered to have a drastic influence upon the dielectric properties. On the other hand, such properties have also been observed when barium is inserted in the structure of STO although the difference in ionic size between Ba and Sr cannot lead to such off-center dipole moments. In the $Sr_{1-x}Ba_xTiO_3$ system, a picture in which the progressive introduction of Sr inside $BaTiO_3$ induces a progressive breaking of the ferroelectric state toward mesoscopic random-field domains and eventually to a glassy state with dipolar clusters has emerged. We have shown that below a critical concentration $x<x_c$, the $Sr_{1-x}Ba_xTiO_3$ compound may be called "incipient" ferroelectric and becomes a "true" ferroelectric compound for higher Ba concentrations. These results gave the limit for the existence of the macroscopic (or mesoscopic) spontaneous polarization which is associated to the "true" ferroelectric phases.

A combined structural and *ab initio* study of Ca doping in STO (SCT) revealed that the introduction of small ions into the STO matrix is not as simple as in the classical picture.³ These results suggested that polar instabilities originating from the weak off-center displacements of $Ca^{2+}$ ions ($\approx0.08$ Å) are not likely to directly polarize the host matrix by an electrostatic mechanism. Instead, we suggested the possible role of random fields in inducing the presence of disordered polar nanoclusters, which is similar to polar nanoregions (PNRs) in relaxor materials. The polar instabilities intrinsic to STO are almost not modified by the presence of Ca ions. In SCT, the polarization is on the same order of magnitude as what it would be in pure STO if it were ferroelectric (i.e., without quantum effects). This is why we have pointed out the possible role of random fields in the appearance of PNRs or microregions. These random fields could be of elastic nature and could originate from the possible tensile strain created by the Ca dopant.

In this latter study we pointed out also the difference with another impurity-doped quantum paraelectric, $K_{1-x}Li_xTaO_3$ (KLT), in which the Li off-center motion is much larger than that of Ca in SCT, as shown by recent *ab initio* calculations [$]\approx1$ Å (Ref. 14)[$], previous calculations¹⁵,¹⁶ and various experiments.¹⁷⁻¹⁹ KLT is a very interesting system because it shows strong analogy with relaxor materials. Indeed the high electric-field tunability of permittivity of pure KTO was interpreted as originating from the existence of polar clusters, whereas the absence of such clusters in CTO and LNTO was inferred from the lack of tunability. The existence of such clusters was also evidenced in KLT under electric field²⁰,²¹ using a second-harmonic generation microscope (SHGM), showing again similarities with the physical picture of relaxor compounds, which are characterized by the existence of PNRs. For a review on the structural aspects of this class of materials, see, for instance, Ref. 22 and references therein.

Having in mind these results, we conduct in the present work first-principles calculations to get more insight into the physics of KLT. We examine more particularly how the KTO matrix is polarized around a Li dipolar impurity by using a large $3×3×3$ supercell (3.7% doping rate) and determine the shape of the energy landscape felt by the impurities. We also examine the interaction between two neighboring Li impurities in various configurations. Our results suggest that KLT is not ferroelectric at low temperature, even at this large impurity level (3.7%). We confirm this result by a low-temperature neutron-diffraction analysis. We also provide a simple model describing the energetics of KLT in terms of a local potential and dipole-dipole interactions, which could be used in future molecular dynamics or Monte Carlo simulations.

## II. EXPERIMENTAL SETUP

Single crystals (named hereafter KLT2 and KLT5) of KLT with 2.4% and 5.3% of Lithium were grown by the self-flux method with $Ta_2O_5$, $Li_2CO_3$, and an excess of $K_2CO_3$ as a flux. The exact Li concentration $x$ was determined by the empirical relation between $x$ and the transition temperature which is defined by the disappearance temperature of SH intensity in zero-field heating after a field-cooling process (see Ref. 23 for more details). These single crystals were grinded in order to form powders. Structural studies by neutron diffraction were performed by Rietveld analysis with full patterns collected at temperatures of 300 and 10 K on the 3T2 high-resolution goniometer implemented on a thermal source (1.227 Å) using the Orphée reactor facilities at Laboratoire Léon Brillouin at Saclay; refinements were carried out with the XND software.

## III. COMPUTATIONAL DETAILS

We perform first-principles calculations in the framework of the density-functional theory.²⁴ The exchange and correlation energy is treated in the LDA. We have used the ABINIT code²⁵ with Troullier-Martins pseudopotentials.²⁶ The K pseudopotential treats as valence electrons the $3p^6$ and $4s^1$ (seven electrons) and is generated from an ionic configuration $K^+$. That of Ta treats as valence electrons the $6s^1$ and $5d^4$ (five electrons, the $4f$ electrons are put in the core). Our pseudopotential for Li treats as valence electrons the three electrons $1s^2$ and $2s^1$. In the final relaxed configurations, the maximal component of the atomic forces is below 6.0 $×10^{-4}$ Ha/bohr ($\approx0.03$ eV/Å). We use a plane-wave cutoff of 30 Ha, for which the equilibrium lattice constants of KTO and $Li_2O$ are perfectly converged, respectively at 3.932 Å (expt: 3.983 Å,²⁰ Leung:²⁷ 3.957 Å, and Singh:⁵ 3.96 Å) and 4.596 Å (expt: 4.61 Å). Thus we have an underestimation of 1.3% in the case of KTO, and 0.3% in the

case of $\mathrm{Li_2O}$, typical of the LDA. The First Brillouin Zone of the KTO five-atom unit cell is sampled with a $6×6×6$ mesh.

The introduction of Li impurities is performed in a 3 $×3×3$ supercell (135 atoms) whose First Brillouin Zone is accordingly sampled with a $2×2×2$ mesh and whose lattice parameter is three times the experimental value of the KTO lattice constant [3.983 Å (Ref. 20)]. We also perform a few calculations on pure cubic KTO by using the density- functional perturbative theory$^{28}$ to obtain its vibration eigenmodes at the $\Gamma$ point and its dielectric properties (electronic dielectric tensor, Born effective charges, and static dielectric tensor).

Finally, we evaluate the polarization induced by the Li off-center motion in the framework of the so-called modern theory of polarization, through a series of Berry-phase calculations (see the details hereafter). These computations are performed using the $2×2×2$ $k$-point mesh after checking that a $4×4×4$ mesh provides with identical results.

An extensive study of KLT using density-functional calculations can be found in Ref. 14. Concerning the Li displacements and associated energies, our results match very well with this previous pioneering work (only slight differences are found related to the different Li concentration) but the present study completes this work by focusing on the polarization around one Li impurity, and this is why a very large $3×3×3$ supercell (135 atoms) has been used.

## IV. EXPERIMENTAL RESULTS
We have reported$^{20}$ a high-resolution x-ray diffraction study of single crystals of KTL in which we observed for doping with Li at 3%, at least and above, a tetragonal distortion at low temperature. This distortion displays a behavior with two characteristic temperatures: it appears below a $T_B$ temperature and increases below a $T_p$ temperature. However this distortion is very weak: at 10 K for 3% of lithium the value is 0.095% and for 7% of lithium is 0.17%. SHG experiments at zero field and with applied electric field allowed to conclude that PNRs nucleate around $T_B$ and grow toward $T_p$ to form ferroelectric microdomains below this temperature. *However these microdomains become macroscopic only in a field cooling process and below $T_p$.*

In the present neutron study we are therefore interested to look for the possibility of a true polar phase to occur at low temperature with no electric field, that is, a long-range ferroelectric phase. We have performed neutron Rietveld analysis of KLT2 and KLT5, each of them at room temperature and at 10 K. The purpose of this paper is not to give a detailed analysis of the results but only the main points. First of all, it is important to notice the (although trivial) point: both K and Li atoms contribute in the neutron diffusion on the crystallographic A site of the ABO3 perovskite structure in the form of an average value with components, respectively, equal to 0.370 and $-0.194$ but weighted by the occupation rate. As the content in Li in the elementary cell is very weak, 2.4% and 5.3%, the total contribution of lithium in the diffracted intensities is negligible. It means that the neutron structural diffraction probes only the contribution of the KT matrix but gives no information about the displacements of Li, which has been reported and confirmed in the calculation part as high as 1 Å.

<table>
<caption>Table I. Neutron-diffraction experiments: Rietveld agreement factors.</caption>
<thead>
<tr>
<th>Compounds</th>
<th>KTL 2.4%</th>
<th>KTL 2.4%</th>
<th>KTL 5.3%</th>
<th>KTL 5.3%</th>
</tr>
</thead>
<tbody>
<tr>
<td>Temperature (K)</td>
<td>300</td>
<td>10</td>
<td>300</td>
<td>10</td>
</tr>
<tr>
<td>Rwp (%)</td>
<td>3.54</td>
<td>3.52</td>
<td>5.39</td>
<td>4.65</td>
</tr>
<tr>
<td>RB (%)</td>
<td>1.69</td>
<td>1.32</td>
<td>2.23</td>
<td>2.35</td>
</tr>
<tr>
<td>G.O.F.</td>
<td>2.96</td>
<td>2.35</td>
<td>3.12</td>
<td>3.01</td>
</tr>
<tr>
<td>Rexpected</td>
<td>1.50</td>
<td>1.50</td>
<td>1.50</td>
<td>1.50</td>
</tr>
</tbody>
</table>

Very satisfactory fittings of the patterns both at room temperature and at 10 K with a simple cubic $Pm\overline{3}m$ phase (in which all atoms stand in special Wickoff positions) were obtained, as this can be seen in Table I in which we give classical Rietveld agreement factors; moreover no anomaly in the thermal parameters which could have been associated with disorder was observed. Starting from these cubic solutions, we have tried to refine the two low-temperature patterns by introducing a tetragonal distortion as measured from x-ray experiments with (i) a nonpolar tetragonal phase with $P4/mmm$ space group and (ii) a polar tetragonal phase with $P4mm$ space group, classically observed in ferroelectric perovskites. However the cubic model gave a very good fitting of the data and no improvement was obtained when relaxing the space group to lower symmetry (such as tetragonal), i.e., with a higher number of refined parameters. Therefore these results show that the introduction of up to at least 5.4% of lithium in the structure does not induce any detectable changes in the atomic positions of K, Ta, and O atoms that should appear if the structure were ferroelectric with a long range order.

## V. THEORETICAL RESULTS
### A. First-principles study of the KTO matrix
First we focus on pure cubic KTO. The eigenfrequencies of the vibration modes at $\Gamma$ (each three times degenerate), computed at the experimental lattice constant (3.983 Å), are gathered in Table II. No imaginary eigenfrequency is found. Our calculations confirm therefore that within the LDA, there is no FE instability in $KTaO_3$, in full agreement with

<table>
<caption>Table II. Eigenfrequencies of cubic KTO at the $\Gamma$ point.</caption>
<thead>
<tr>
<th>Mode</th>
<th>TO1 ($\Gamma_{15}$)</th>
<th>TO2 ($\Gamma_{15}$)</th>
<th>$\Gamma_{25}$</th>
<th>TO3 ($\Gamma_{15}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Present work</td>
<td>68.2</td>
<td>214.3</td>
<td>297.7</td>
<td>536.4</td>
</tr>
<tr>
<td>Singh$^{\text{a}}$</td>
<td>80</td>
<td>172</td>
<td>264</td>
<td>528</td>
</tr>
<tr>
<td>Expt.$^{\text{b}}$</td>
<td>24</td>
<td>197</td>
<td>274</td>
<td></td>
</tr>
<tr>
<td>Expt.$^{\text{c}}$</td>
<td>81</td>
<td>199</td>
<td></td>
<td>546</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">${}^{\text{a}}$Reference 5.</td>
</tr>
<tr>
<td colspan="5">${}^{\text{b}}$Reference 29.</td>
</tr>
<tr>
<td colspan="5">${}^{\text{c}}$Reference 30.</td>
</tr>
</tfoot>
</table>

<table>
<caption>TABLE III. Born effective charges, electronic and static dielectric tensor in cubic KTO, computed at the experimental lattice constant $a_0$=3.983 Å.</caption>
<tbody>
<tr>
<td>
$\epsilon^\infty$
</td>
<td colspan="4">
5.15
</td>
</tr>
<tr>
<td>
$\epsilon_S$
</td>
<td colspan="4">
341.3
</td>
</tr>
<tr>
<td>
</td>
<td>
K
</td>
<td>
Ta
</td>
<td>
$O_\perp$
</td>
<td>
$O_\parallel$
</td>
</tr>
<tr>
<td>
$Z^*$
</td>
<td>
1.11
</td>
<td>
8.31
</td>
<td>
$-$1.72
</td>
<td>
$-$5.98
</td>
</tr>
</tbody>
</table>

previous LDA calculations. $^{5,6}$ However, the small value of the TO1 eigenfrequency (68.2 ${\rm cm}^{-1}$) suggests that this compound is, as expected, highly polarizable.

Indeed, the low-frequency TO1 mode of KTO gives rise to a high dielectric response not so high however than the experimental one at low temperature: at the experimental lattice constant, the computed static dielectric constant is $\epsilon_S$=341.3 (Table III). However, the TO1 eigenfrequency is very dependent on the lattice constant used in the calculation: if the latter is increased, the TO1 mode progressively softens and the static dielectric constant increases accordingly (Table IV). At a critical lattice constant $\approx$3.995 Å, TO1 becomes unstable (which would yield a ferroelectric structure through a displacive phase transition above this critical value).

Note the very high value of the Ta and $O_\parallel$ Born effective charges, similarly to what can be found in many ferroelectric systems. In the case of potassium, the Born effective charge (1.11) is very close to the formal charge +1.

### B. Li-doped KTO
In a 3$\times$3$\times$3 supercell (thus corresponding to a 3.7% Li concentration), one K atom is replaced by a Li atom. The Li atom is left free to displace along the [001], [110], and [111] directions. The lattice constant is fixed to its experimental value ($a_0$=3.983 Å), which means that the simulation box is cubic with a size=$3a_0$. We also optimize the same supercell with Li kept fixed at the origin (thus without off-center displacement) in a $Pm\overline{3}m$ symmetry (Table V).

In this work, we are interested in atomic displacements between the high-symmetry ($Pm\overline{3}m$) configuration and other optimized configurations with Li displaced in the previously mentioned directions. The displacement field corresponding to a given configuration is obtained in the following way: (i) we calculate the displacement of atom $i$ between the high-symmetry cubic configuration and the stable configuration with Li displaced and obtain a first displacement field $\tilde{\Delta}r_i'$
<table>
<caption>TABLE IV. TO1 eigenfrequency and static dielectric constant as a function of the lattice constant in cubic KTO.</caption>
<tbody>
<tr>
<td>
Lattice constant
</td>
<td>
TO1
</td>
<td>
$\epsilon_S$
</td>
</tr>
<tr>
<td>
(Å)
</td>
<td>
(cm$^{-1}$)
</td>
<td>
</td>
</tr>
<tr>
<td>
3.983
</td>
<td>
68.2
</td>
<td>
341.3
</td>
</tr>
<tr>
<td>
3.990
</td>
<td>
44.2
</td>
<td>
824.9
</td>
</tr>
<tr>
<td>
3.993
</td>
<td>
28.4
</td>
<td>
1932.9
</td>
</tr>
<tr>
<td>
3.994
</td>
<td>
15.7
</td>
<td>
5840.7
</td>
</tr>
<tr>
<td>
3.995
</td>
<td>
21.4$i$
</td>
<td>
</td>
</tr>
</tbody>
</table>

and (ii) we subtract from all these displacements the quantity $(\Sigma_i M_i \tilde{\Delta}r_i')/(\Sigma_i M_i)$ so that the obtained field of displacements $\tilde{\Delta}r_i$ is such as: $\Sigma_i M_i \tilde{\Delta}r_i=\tilde{0}$.

The displacement is thus assumed to occur under the condition of fixed mass center. Indeed, as explained hereafter, a forward displacement of Li is accompanied by a polarization of the surrounding KTO matrix, some atoms moving forward and other backward. Anyway, some parts of the supercell are not affected by this polarization and could also be used as reference fixed points. We have checked that within the present choice, the displacements of these atoms are $\leq$0.01 Å.

### 1. Li off-center stable position
First of all, the most stable position is found along the [001] direction (the total energy is lowered by 0.194 eV with respect to the cubic structure with the Li in its high-symmetry position). We find a very large off-center displacement of Li along [001] $\approx$1.01 Å, in very good agreement with the calculations of Prosandeev *et al.*$^{14}$ (1.009 Å). Around Li, the KTO matrix is polarized (see below).

We now evaluate the dipole induced by such a displacement. To this aim, we calculate the Berry-phase polarization along a path joining the high-symmetry cubic configuration to the tetragonal-like configuration with Li displaced along [001]. Six configurations along this path are computed, with the atomic positions in configuration $i$($i$=1..6) defined by $x_\lambda^{(i)}=x_0+\lambda(x_1-x_0)$, where $\lambda$=0.2$\times(i-1)$, and $x_0$ and $x_1$ are, respectively, the atomic positions in the initial high-symmetry cubic configuration and the final stable tetragonal-like position with Li displaced along [001]. We obtain a regular curve for the polarization provided we add one polarization quantum $Q$=$2eR/\Omega$=0.224 C/m$^2$ ($R$=$3a_0$ is the supercell parameter and $\Omega$ its volume) for the two last con-
<table>
<caption>TABLE V. Energies (eV) of the optimized configurations of a 3$\times$3$\times$3 supercell with one Li impurity, Cartesian components of the Li displacement, and corresponding electric dipole. The energy of the high-symmetry configuration with no Li off-center displacement is taken as reference.</caption>
<tbody>
<tr>
<td>
Li off-center
</td>
<td>
No
</td>
<td>
[001]
</td>
<td>
[110]
</td>
<td>
[111]
</td>
</tr>
<tr>
<td>
Energy (eV)
</td>
<td>
0
</td>
<td>
$-$0.194
</td>
<td>
$-$0.108
</td>
<td>
$-$0.112
</td>
</tr>
<tr>
<td>
Li displacement
</td>
<td>
</td>
<td>
$\Delta r_z$=1.01
</td>
<td>
$\Delta r_x$=$\Delta r_y$=0.48
</td>
<td>
$\Delta r_x$=$\Delta r_y$=$\Delta r_z$=0.40
</td>
</tr>
<tr>
<td>
(Å)
</td>
<td>
($\Delta r_x$=$\Delta r_y$=$\Delta r_z$=0)
</td>
<td>
($\Delta r_x$=$\Delta r_y$=0)
</td>
<td>
($\Delta r_z$=0)
</td>
<td>
</td>
</tr>
<tr>
<td>
Dipole ($e$Å)
</td>
<td>
0
</td>
<td>
8.32
</td>
<td>
6.95
</td>
<td>
6.73
</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE VI. Contributions of the Li impurity and of the KTO matrix to the dipole induced by the Li displacement along [001] in the $3\times 3\times 3$ supercell, computed from the atomic displacements and the atomic Born effective charges (in parenthesis, computation from Berry-phase).</caption>
<tbody><tr><th></th><td>Total</td><td>Li</td><td>matrix</td></tr>
<tr><th>Dipole ($e$ Å)</th><td>8.32 (8.12)</td><td>1.25</td><td>7.07</td></tr>
<tr><th>Polarization (C/m²)</th><td>0.078 (0.076)</td><td></td><td></td></tr>
<tr><th colspan="4">(3.7% Li concentration)</th></tr>
</tbody></table>

figurations. The spontaneous polarization is then obtained by subtracting the first value ($i$=1) to the last one ($i$=6): $P_{z}=P_{z}(i=6)-P_{z}(i=1)$. We find $P_{z}$=0.076 C/m²=7.6 μC/cm². The corresponding dipole induced by the Li off-center motion is 8.12$e$ Å ($e$ is the elementary charge).

Now we estimate the dipole induced by the sole Li off-center motion (without the polarization of the surrounding matrix) to separate the contributions of the impurity from that of the matrix. Starting from the high-symmetry cubic configuration, only the Li is displaced along [001] by an amount $\Delta z_{Li}$. If we note by $\Delta P_{z}$ the $z$ component of the polarization induced by this motion, the limit, for small $\Delta z_{Li}$, of the ratio $\Delta P_{z}/\Delta z_{Li}$ gives access to the $zz$ component of the Li Born effective charge tensor:
$$
Z_{\mathrm{Li},zz}^{*}=\lim_{\Delta z_{\mathrm{Li}}\to 0}\,\Omega\frac{\Delta P_{z}}{\Delta z_{\mathrm{Li}}}\tag{1}
$$
in which $\Omega$ is the volume of the supercell. Three off-center configurations are computed, in which Li is displaced by 0.1, 0.2, and 0.3 Å, respectively. From these calculations, we estimate $Z_{\mathrm{Li},zz}^{*}$=1.24, very close to the Born effective charge of K in KTO(1.11). Assuming that the Li Born effective charge is constant along the path joining the high-symmetry position to the stable Li position along [001],³¹ we estimate the contribution of Li to the total dipole at $\approx$1.25$e$ Å.

Note that the total dipole calculated from the Born effective charges (1.24 for Li and those of K, Ta, and O in KTO) and the atomic displacements (instead of the Berry-phase method) is 8.32$e$ Å, in very good agreement with the value obtained from the Berry-phase calculation.³² The various contributions to the polarization (Li+KTO matrix) are summarized in Table VI. Interestingly, the Li contribution is only $\approx$15% of the total dipole, which gives strong evidence to the important role played by the surrounding matrix in the dielectric properties of KLT.

Second, we focus on the local polar distortions surrounding the Li impurity displaced along [001] to localize in space this polarization of the matrix. We quantify these distortions by measuring the alternating Ta-O distances along the [001] direction in the different Ta-O chains of the simulation box (Table VII). In the supercell we use, there are in fact by symmetry only three different kinds of chains (see Fig. 1).

In the four Ta-O chains oriented along the $z$ direction (that of the Li dipole) and immediately surrounding the Li impurity (chain 1 on Fig. 1), the mean distortion is 0.10 Å. This distortion decreases very quickly with increasing distance in the lateral directions: the distortion is only 0.024 and 0.018 Å in chains 2 and 3. Thus in the center of the supercell, at only $\approx 2a_{0}$ from the eight Li located at the corners of the supercell (by the periodic boundary conditions), the polar distortion is very small ($d_{3}$-$d_{4}$≈0.02–0.03 Å).

<table>
<caption>TABLE VII. Ta-O interatomic distances in the Ta-O chains oriented along [001]. The $d_{i}$ refer to Fig. 1. The differences $d_{i}$-$d_{i+1}$ quantify the polar distortions in the different unit cells of the supercell.</caption>
<tbody><tr><th></th><td>Chain 1</td><td>Chain 2</td><td>Chain 3</td></tr>
<tr><th>$d_{1}$</th><td>2.025</td><td>1.996</td><td>1.997</td></tr>
<tr><th>$d_{2}$</th><td>1.947</td><td>1.977</td><td>1.981</td></tr>
<tr><th>$d_{3}$</th><td>2.050</td><td>2.009</td><td>2.005</td></tr>
<tr><th>$d_{4}$</th><td>1.939</td><td>1.975</td><td>1.980</td></tr>
<tr><th>$d_{5}$</th><td>2.053</td><td>2.006</td><td>1.999</td></tr>
<tr><th>$d_{6}$</th><td>1.935</td><td>1.986</td><td>1.987</td></tr>
<tr><th>$d_{1}$-$d_{2}$</th><td>0.078</td><td>0.019</td><td>0.016</td></tr>
<tr><th>$d_{3}$-$d_{4}$</th><td>0.111</td><td>0.034</td><td>0.025</td></tr>
<tr><th>$d_{5}$-$d_{6}$</th><td>0.118</td><td>0.020</td><td>0.012</td></tr>
<tr><th>Average</th><td>0.102</td><td>0.024</td><td>0.018</td></tr>
</tbody></table>

We confirm this point by examining for instance the contributions to the total dipole along $z$ due to each Ta atom (the Ta charge effective times the Ta displacement). For each Ta located in the four $z$-oriented chains surrounding Li, this contribution is between 0.15 and 0.23$e$ Å. For all the other Ta of the supercell, the absolute value of this contribution is between 0.05 and 0.08$e$ Å.

Thus, the KTO matrix is strongly polarized in needlelike regions (polar clusters) of 1–2 lattice constant thickness oriented along the Li dipole. Unfortunately, the supercell we use is too small to avoid the overlapping between such re-

![](./images/811795174962233345_1.jpg)

FIG. 1. (Color online) The Ta-O distances surrounding the Li impurity in the $3\times 3\times 3$ supercell used in the present work. All the other Ta-O bonds along $z$ in the supercell are equivalent by symmetry to one of the 18 $z$-oriented bonds represented on this picture.

gions along the direction of the polarization. It is thus diffi- cult to extrapolate from the present results an order of mag- nitude of the size these polar regions would have along the direction of the polarization if they did not overlap. Note however that the shape of these regions is probably close to that of the so-called ferroelectric correlation volume, $^{33}$ which is usually viewed as a needle-shaped ellipsoid of size $l \times l$  $\times L$ with $l \approx 1-2 ~nm$ and $L$ can reach $10 ~nm$ or more.

### 2. Local soft mode associated to the Li impurity
Pure KTO does not contain (within the LDA) any un- stable vibration mode. But introducing a $Li$ in the place of a K atom makes unstable polar modes appear in the cubic con- figuration. Strictly speaking, a rigorous characterization of these soft modes would require to perform linear-response calculations on the supercell in the high-symmetry configu- ration, which is very time consuming. Instead, we character- ize these soft modes in an approximate way through the fi- nite displacements presented above. There are three degenerate modes, each of them developing atomic eigendis- placements in one Cartesian direction (in the previous sec- tion, only the $z$ -polarized soft mode has been described).
We can obtain approximately the eigendisplacement field $\xi_{i, z}$ of this mode from the finite displacements
$$\xi_{i, z} \approx \frac{\Delta z_{i}}{\|\Delta Z\|}\qquad(2)$$
with $\Delta z_{i}$ the $z$ displacement of atom $i$ and $\|\Delta Z\|^{2}=\Sigma_{i} \Delta z_{i}^{2}$ (the eigendisplacement vector is dimensionless and normalized).
The component of $\xi_{z}$ on $Li$ is $0.97(1.01 \AA)$ , which means that most of the polar displacement is due to $Li$ . And yet the contribution of $Li$ to the dipole is much weaker (15\% of the total dipole), as explained above. This is due to the large effective charges of $Ta$ and $O$ by comparison to $Li$ , thus producing a large dipole with small displacements.
It is also easy to evaluate the effective charge of this soft mode from the atomic Born effective charges of $Li$ (previ ously calculated), those of $K, Ta$ , and $O$ (calculated in bulk KTO) and from the eigendisplacements
$$Z_{z}^{*} \approx \sum_{i} Z_{z z, i}^{*} \xi_{i, z}.\qquad(3)$$

We find $Z_{z}^{*}=7.98$ . Calculations with Li displaced along[100] and [010] allow to define $\xi_{i, x}$ and $\xi_{i, y}$ and would yield $Z_{x}^{*}=Z_{y}^{*}=7.98$ . It is possible to define a local mode $\vec{u}$ (which has the dimension of a displacement), that consists of a field of atomic displacements defined, on atom $i$ , with respect to the high-symmetry configuration, by $\Delta x_{i}=\xi_{i, x} u_{x}, \Delta y_{i}=\xi_{i, y} u_{y}$ , and $\Delta z_{i}=\xi_{i, z} u_{z}$ . (where $\xi_{i, \alpha}$ is the component on atom $i$ of the soft mode eigendisplacement vector along the $\alpha$ direction defined above). In the stable configuration with $Li$ displaced along [001], the local mode would be therefore $\vec{u}=(u_{x}$ =0,u, =0,u2=1.04 A).
We have to note that our calculations unfortunately suffer from the fact that the displacements patterns induced in the matrix (polar clusters) overlap along the polar direction (Fig.1), due to periodic boundary conditions. For this reason we cannot determine precisely the displacement field of the local mode at 8-10 $\AA$ from the Li impurity along the polar axis. A more accurate determination of the $Li$ -induced local mode would require to use much larger supercells in the direction of the Li displacement, which was not possible in the present case. Thus, we will determine hereafter an approximate shape of the energy landscape seen by the impurity as a function of the $Li$ displacement rather than of the local mode.

### 3. Local potential felt by the Li impurities
We now displace $Li$ in other directions to establish, at least in an approximate way, the energy landscape felt by this impurity. This potential energy surface can be seen as result- ing from the sum of a local potential $V^{loc }$ and an electrostatic interaction between the polar clusters $E^{d p l}$ . Thus the energy of a set of $N$ Li-induced dipolar clusters with Li displace ments $\vec{\Delta} r_{1},..., \vec{\Delta} r_{N}$ writes
$$E\left(\vec{\Delta} r_{1}, \ldots, \vec{\Delta} r_{N}\right)=\sum_{i} V^{l o c}\left(\vec{\Delta} r_{i}\right)+E^{d p l}\left(\vec{\Delta} r_{1}, \ldots, \vec{\Delta} r_{N}\right).$$

The long-range part writes
$$E^{d p l}\left(\vec{\Delta} r_{1}, \ldots, \vec{\Delta} r_{N}\right)=\frac{Z^{* 2}}{\epsilon_{S}} \sum_{i<j} \frac{\vec{\Delta} r_{i} \cdot \vec{\Delta} r_{j}-3\left(\hat{\vec{R}}_{i j} \cdot \vec{\Delta} r_{i}\right)\left(\hat{\vec{R}}_{i j} \cdot \vec{\Delta} r_{j}\right)}{R_{i j}^{3}}$$
with $\hat{\vec{R}}_{i j}=\vec{R}_{i j} / R_{i j}, \vec{R}_{i j}$ being the vector joining dipole $i$ to di pole $j. Z^{*}$ is the effective charge of the local mode previously estimated $(Z^{*}=7.98)$ and $\epsilon_{S}$ is the static dielectric constant of the KTO matrix in the present computation $(\epsilon_{S}=341.3)$ . Con sidering the cubic symmetry of the undisplaced configura- tion, the local potential $V^{l o c}$ can be written, as usual, underthe following form, up to sixth order in the $\vec{\Delta} r$ :
$$\begin{aligned}
V^{l o c}\left(\Delta r_{x}, \Delta r_{y}, \Delta r_{z}\right)= & A_{1}\left(\Delta r_{x}^{2}+\Delta r_{y}^{2}+\Delta r_{z}^{2}\right)+A_{11}\left(\Delta r_{x}^{4}+\Delta r_{y}^{4}\right. \\
& \left.+\Delta r_{z}^{4}\right)+A_{12}\left(\Delta r_{x}^{2} \Delta r_{y}^{2}+\Delta r_{x}^{2} \Delta r_{z}^{2}\right. \\
& \left.+\Delta r_{y}^{2} \Delta r_{z}^{2}\right)+A_{111}\left(\Delta r_{x}^{6}+\Delta r_{y}^{6}+\Delta r_{z}^{6}\right) \\
& +A_{112}\left[\Delta r_{x}^{2}\left(\Delta r_{y}^{4}+\Delta r_{z}^{4}\right)+\Delta r_{y}^{2}\left(\Delta r_{x}^{4}+\Delta r_{z}^{4}\right)\right. \\
& \left.+\Delta r_{z}^{2}\left(\Delta r_{x}^{4}+\Delta r_{y}^{4}\right)\right]+A_{123} \Delta r_{x}^{2} \Delta r_{y}^{2} \Delta r_{z}^{2}.
\end{aligned}$$

Having the total energy corresponding to $\vec{\Delta} r=\overrightarrow{0}$ and that of the stable position along [001], we complete the study by optimizing (saddle point) configurations with $Li$ displaced along [110] and [111], and treat the displacement patterns as previously (by imposing that the atomic motions do not change the mass center).
Along [111], the minimum is found for $\Delta r_{x}=\Delta r_{y}=\Delta r_{z}$ =0.404 A at an energy -0.112 eV (with respect to the high- symmetry site). The dipole induced by this displacement field, estimated by the means of atomic effective charges and displacements (renormalized so as the mass center is fixed), is $3.88 e \AA$ along each direction, which provides a total di pole amplitude of $6.73 e \AA$ .
Along [110], the minimum is found for $\Delta r_{x}=\Delta r_{y}$ =0.484 A (Ar,=0), at an energy -0.108 eV (with respect to the high-symmetry site), thus very close to the previous saddle point by only $4 meV$ . In the same manner, the dipole

<table>
 <thead>
  <tr>
   <th colspan="4">
    TABLE VIII. Coefficients of the local potential felt by the Li impurity in the KTO matrix.
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    A₁
   </td>
   <td>
    $-$0.362
   </td>
   <td>
    eV/Å²
   </td>
   <td>
    Harmonic
   </td>
  </tr>
  <tr>
   <td>
    A₁₁
   </td>
   <td>
    +0.156
   </td>
   <td>
    eV/Å⁴
   </td>
   <td>
    Anharmonic
   </td>
  </tr>
  <tr>
   <td>
    A₁₂
   </td>
   <td>
    +0.0388
   </td>
   <td>
    eV/Å⁴
   </td>
   <td>
    Anharmonic
   </td>
  </tr>
  <tr>
   <td>
    A₁₁₁
   </td>
   <td>
    +0.0154
   </td>
   <td>
    eV/Å⁶
   </td>
   <td>
    Anharmonic
   </td>
  </tr>
  <tr>
   <td>
    A₁₁₂
   </td>
   <td>
    +1.75028
   </td>
   <td>
    eV/Å⁶
   </td>
   <td>
    Anharmonic
   </td>
  </tr>
  <tr>
   <td>
    A₁₂₃
   </td>
   <td>
    +1.367
   </td>
   <td>
    eV/Å⁶
   </td>
   <td>
    Anharmonic
   </td>
  </tr>
 </tbody>
</table>

induced by this displacement field, estimated by the means of atomic effective charges and displacements (renormalized so as the mass center is fixed), is $4.92e$ Å along the $x$ and $y$ directions, which provides a total dipole amplitude of $6.95e$ Å, close to the previous value. The results are gathered in Table V.

To obtain the local potential as a function of Li displacement, we must first subtract from these energies the contribution due to the dipole-dipole interaction between periodic images of the off-center Li. This is achieved by the knowledge of the electric dipole corresponding to each configuration. This interaction is estimated using the theoretical static dielectric constant of bulk KTO within the present lattice constant ($\epsilon_{S}$=341.3) that produces an important screening. Thus the corresponding dipole-dipole interactions are weak with respect to the local potential.

Then, fitting Eq. (4) on the new energies obtained and on the Li position in the minima of the three optimized configurations, we get an estimation of the coefficients describing the local potential felt by the impurities (Table VIII). The corresponding energy landscape is plotted on Fig. 2 along [001], [110], and [111].

### 4. Energy barrier for Li rotation
From the previous calculations, we now estimate the energy barrier Li has to overcome to go from one of its six stable sites to another. The lowest-energy saddle point is along [111] and involves a $E_{d}$=82 meV barrier (without subtracting the dipole-dipole correction). Note, however, that the saddle point along [110] provides a very close value (86 meV).

Such a value can be used to estimate in a very rough and approximate way the mean time $\tau$ spent by one Li in one stable site before (thermally) hopping to a neighboring site, by $\tau$=$\frac{1}{\nu}e^{E_{d}/k_{B}T}$, $\nu$ being an attempt frequency for the hopping mechanism, fixed at the typical value $\frac{1}{\nu}$≈10⁻¹³ s. At $T$=300 K, we obtain $\tau(T$=300 K)≈2.4 ps, and this value increases rapidly when the temperature decreases. At 100 K, we have $\tau(T$=100 K)≈1.4 ns and at 50 K, $\tau(T$=50 K)≈$1.9 \times 10^{-5}$ s, indicating a freezing of the impurities in their local potential at low temperature.

### C. Interaction between two first-neighbor Li impurities
In this section, we now examine two Li impurities in first-neighbor relative positions in the same supercell. The previous model does not stand in that case since (i) short-range interactions are acting between impurities and (ii) the electrostatic interaction is not as screened by the matrix. Three different configurations are studied, by changing the relative off-center displacements of the two Li, as shown on Fig. 3.

![](./images/811795174962233345_2.jpg)

FIG. 2. (Color online) Local potential (eV) as a function of Li displacement [panel (a): $x$ component and panel (b): norm of the Li displacement vector] along the three directions [001], [110], and [111], as deduced from the analytical model [Eq. (4)].

As expected from simple electrostatics, the (c) configuration, in which the two Li are displaced in the same direction along the line separating them, is the most stable. The energy of the system with respect to a configuration in which the

![](./images/811795174962233345_3.jpg)

FIG. 3. The three configurations studied in Sec. V C and their energies with respect to a configuration in which the two Li are undisplaced. The arrows correspond to the different off-center displacements of the Li impurities.

two Li are undisplaced is -0.551 eV. Next come configura- tion (b) and (a). By subtracting the energy of a single Li dipole displaced along [001], we define an interaction energy between the two impurities. In configuration (c), this in- teraction is strongly stabilizing (-163 meV) and destabiliz- ing in configuration (a) (+43 meV) while it is very weak (+4 meV) in configuration (b).

Thus, the interaction between first-neighbor Li impurities strongly favors a kind of ferroelectric order between first- neighbor Li impurities. It is clear therefore that a pair of Li does not behave as two single Li ions and generates a polar cluster much larger than a single Li.

## VI. DISCUSSION
### A. Polar state of KLT at low temperature

From our calculations, we conclude that KLT is a strong order-disorder system in which the impurities go off-center along the [100]-type directions, by feeling a very deep local potential $(\approx-0.2$ eV), mainly due to the (short-range) inter action with the neighboring matrix rather than to the (long- range) interaction with other Li impurities.

This suggests that Li-doped $KTaO_{3}$ (at the high concen tration of 3.7%) cannot be ferroelectric at low temperature since the Li dipole-Li dipole contribution to the energy of the system is much weaker than the local potential itself. At low temperature, the impurities are probably frozen in one of their six possible satellite sites without creating long-range ferroelectric order. Moreover, the polarization in the host ma- trix around each dipolar impurity decreases very rapidly with respect to the distance in the lateral directions so that at $\approx \sqrt{3} a_{0}$ from $Li$ , the polarization is almost zero in the matrix. It is thus highly improbable that a lattice of dipolar impuri- ties, even at the high concentration of 3.7%, can create a long-range ferroelectric order in a matrix that is intrinsically(quantum) paraelectric. This picture is confirmed by the neutron-diffraction experiments which reveal no trace of any displacement of the KTO matrix which could indicate the existence of long-range polarization.

At this point it should be stressed that substitution of Li ions in the quantum paraelectric KTO yields at low tempera- ture a dielectric peak (instead of saturation), whose maxi- mum temperature $T_{m}$ increases with the Li concentration. However, the polar state below $T_{m}$ is not well understood. Some reports insist that it is a long-range ferroelectric phase and others explain it with the dipole glass picture. On the other hand, Toulouse et al. $^{34}$ pointed out that KLT is a kind of relaxor, based on dielectric dispersion characteristics andneutron-diffuse-scattering experiments. Our recent study $^{20,21}$  performed with a combination of SHGM and x-ray diffrac- tion showed the occurrence of a Li-induced tetragonal distor- tion below a $T_{B}$ temperature, which also corresponds to the deviation temperature of the Curie-Weiss behavior of the di- electric constant with a twofold characteristic as explained above: between $T_{B}$ and a $T_{p}$ temperature, the tetragonality is only a weak lattice deformation, but it is nonpolar on aver- age. These facts and others strongly suggested that PNRs nucleate around $T_{B}$ and grow toward $T_{p}$ . PNRs might de velop around a group of dipoles formed by off-center Li ions, whose directions are one of the six symmetry- equivalent (100), and are randomly distributed. Thus a mac- roscopic long-range ordered polarization does not appear. However a lattice strain is induced by the average of polar- ization fluctuation through the electrostrictive effect. The phase below $T_{p}$ is polar even without electric field. However, it should be constituted of “ferroelectric microdomains.” In- deed below $T_{p}$ , a larger deformation observed by x-ray dif fraction and a field-induced SHG intensity start to develop while no significant SHG appears in the zero-field-cooling process. The apparent contradiction between the report of a very weak tetragonal strain by high resolution x-ray diffrac- tion and the neutron experiment which evidenced no devia- tion from a cubic paraelectric phase is explained by the ex- istence of the microdomain polar state whose average contribution to strain and polarization is zero, as also ob- served by the SHG experiments in which a signal is observed only when an electric field is applied.

Comparison of both diffraction and SHG data is interest- ing as it allows to gain information on the breaking of inver- sion symmetry at different scales. Although this range of sensibility slightly changes with the physical system probed and with the experimental conditions, it can be roughly said that the former experiments probe mainly the medium- andlong-range symmetries (roughly from some hundredth of $\AA$  up to a micrometer scale), whereas the latter is also sensitive to the local order (roughly on a nanometer scale) because the SHG signal is a measure of the squared ferroelectric order parameter $\langle P^{2}\rangle$ and its fluctuation $\Delta\langle P^{2}\rangle$ . It is therefore dif ficult in some cases to decide whether a system is a “real”’ long-range ferroelectric phase or if the polarization is only short ranged and does not collapse into a macroscopic state. However now we have clarified the global picture of KLT: in the vicinity of $T_{B}$ , the density of PNRs is not large and each polar region fluctuates independently to form a super- paraelectric state. The macroscopic symmetry of the interme- diate phase $(T_{p}<T<T_{B})$ is cubic on average but with ex tremely weak tetragonal distortion due to PNRs; approaching T,, PNRs start to interact with each other, which provides characteristic relaxing dielectric dispersion. Below $T_{p}$ , a mi crodomain ferroelectric state occurs but the polarization does not develop at a long-range scale.

In Ca-doped strontium titanate $^{3}$ the situation is almost the same excepted that (i) the host matrix $(SrTiO_{3})$ has a weak ferroelectric instability (within the LDA) that is supposed to be suppressed by quantum zero-point motions $^{4}$ and (ii) the introduction of Ca impurities in the place of Sr, that go slightly off-center and produce a small dipole, are unable to produce an energetic stabilization that is significantly higher than that associated to the intrinsic ferroelectric instability of the matrix.

We believe that the picture developed here is probably more general and can be extrapolated to a wide variety of materials consisting of a highly polarizable paraelectric ma-trix with dipolar impurities inside (Li-doped $KTaO_{3}, Nb$  doped $KTaO_{3}$ , Ca-doped $SrTiO_{3},^{3}$ etc). A possible ferroelec tricity in those materials at low temperature is a long- standing debate. In the present case, KLT behaves rather as a relaxor than as a ferroelectric, as also suggested by the tem- perature and frequency evolution of the dielectric constant.

### B. Microscopic picture of KLT

We emphasize that the polar clusters observed by *ab initio* calculations around the Li impurity are different from the PNRs experimentally observed since a PNR consists of a larger volume within which several Li-induced polar clusters are correlated. Thus the shape found in *ab initio* (1D or needlelike) is not incompatible with the shape of the PNRs suggested from neutron scattering experiments. $^{35,36}$

The fact that PNRs consist of several Li-induced polar clusters can be inferred from (i) the very deep local potential (-0.2 eV) felt by the Li, which indicates that each Li remains off-center up to very high temperature, while the PNRs are supposed to appear at $T_{B}$. (ii) The size of the PNRs, measured by Yong *et al.*: $^{35}$ these authors find the PNR to have disklike shapes, characterized therefore by two correlation lengths. The maximum of the smallest correlation length measured by these authors is 30 and 46 Å (according to the Li concentration), providing PNRs much larger than the polar clusters modelized in this work by *ab initio*.

Comparison of the previous experimental and theoretical results allows to propose the following microscopic picture of KLT. Above $T_{B}$, each Li form a polar cluster in its neighborhood with a needlelike shape as described by the previous calculations. These polar clusters are very weakly correlated and fluctuate rapidly as shown by the characteristic times previously estimated (a few picoseconds at 300 K).

At $T_{B}$, several Li-induced polar clusters correlate within a characteristic volume (PNR). This correlation is enough to induce a (non polar) tetragonal distortion of the matrix. The dynamics of these PNRs is progressively slowing. But the PNRs remain uncorrelated between each other. Below $T_{B}$, with decreasing temperature, the PNRs progressively grow and their number increases. The increase in their size is consistent with the increase in the correlation length measured in Ref. 35 and the $T_{p}$ corresponds to the $T_{c}$ measured in this work.

Finally at $T_{p}$, the PNRs are correlated on larger characteristic volumes (constituting the ferroelectric microdomains). This induces a larger tetragonal distortion.

However, on average, the matrix itself remains unpolarized whatever the temperature since *only the small zones around the Li—the so-called polar clusters-are polar*. The different steps are summarized on Fig. 4. This microscopic picture is very close to the one proposed by Bürgel *et al.* $^{37}$ on the Ca-doped $SrTiO_{3}$ system. In the KLT system, we observe also ferroelastic domains from the x-ray diffraction study of Ref. 20 (each one consisting of several PNRs), that differ from each other by the direction of the tetragonality, just as in the SCT case.

![](./images/811795174962233345_4.jpg)

FIG. 4. (Color online) Schematic representation of the PNR formation in KLT. $T>T_{B}$: the Li-induced polar clusters (in yellow) are weakly correlated and oscillate around $\langle 100 \rangle$-type directions; $T_{p}<T<T_{B}$: two PNRs appear at $T_{B}$ (gray area); and the Li-induced polar clusters are correlated within the PNR and the two PNR are uncorrelated (in each PNR, a weak tetragonal distortion appears). Their correlations and size increase when the temperature approaches $T_{p}$; $T<T_{p}$: the PNRs have grown and reached the state of microdomain. Their number and their correlations are important. The only polar parts of the materials are the yellow areas.

### VII. CONCLUSION

In this work, we have studied by density-functional calculations the $K_{1-x}Li_{x}TaO_{3}$ system in a $3 \times 3 \times 3$ supercell. We have confirmed that Li stabilizes in six satellite sites along the $\langle 100 \rangle$-type directions, with a very deep local potential $\approx -200$ meV, making KLT an order-disorder system in which the dipoles associated to the Li impurities weakly interact by a long-range electrostatic interaction and feel a deep local potential within the matrix. We have found that a field of polar displacements develops in the KTO matrix along the direction of the off-center Li with a needlelike shape (1D or needlelike cluster).

We have proposed that the polar nanoregions that appear at $T_{B}$ consist of several of these small Li-induced polar clusters. Below $T_{B}$, these polar nanoregions grow and correlate with each other until a temperature $T_{p}$, at which they form ferroelectric microdomains.

An analytic model based on this simple decomposition of the total energy with parameters fitted on *ab initio* DFT-LDA results, has been provided. Although this model is much more rough than the effective Hamiltonians used for ferroelectric materials (in particular, the degrees of freedom of the KTO matrix are not accounted for), we think it is likely to be used in future Monte Carlo or molecular dynamics simulations of KLT viewed as a relaxor.


$^{1}$J. G. Bednorz and K. A. Müller, Phys. Rev. Lett. $\textbf{52}$, 2289 (1984).

$^{2}$N. Sai and D. Vanderbilt, Phys. Rev. B $\textbf{62}$, 13942 (2000).

$^{3}$G. Geneste and J.-M. Kiat, Phys. Rev. B $\textbf{77}$, 174101 (2008).

$^{4}$W. Zhong and D. Vanderbilt, Phys. Rev. B $\textbf{53}$, 5047 (1996).

$^{5}$D. J. Singh, Phys. Rev. B $\textbf{53}$, 176 (1996).

$^{6}$A. R. Akbarzadeh, L. Bellaiche, K. Leung, J. Iñiguez, and D. Vanderbilt, Phys. Rev. B $\textbf{70}$, 054103 (2004).

$^{7}$Y. Ichikawa, M. Nagai, and K. Tanaka, Phys. Rev. B $\textbf{71}$, 092106 (2005).

$^{8}$I. S. Kim, M. Itoh, and T. Nakamura, J. Solid State Chem. $\textbf{101}$, 77 (1992).

$^{9}$Y. Inaguma, J.-H. Sohn, I.-S. Kim, M. Itoh, and T. Nakamura, J. Phys. Soc. Jpn. $\textbf{61}$, 3831 (1992).

$^{10}$G. Geneste, J.-M. Kiat, C. Malibert, and J. Chaigneau, Phys. Rev. B $\textbf{75}$, 174107 (2007).

$^{11}$G. Geneste, J.-M. Kiat, and C. Malibert, Phys. Rev. B $\textbf{77}$, 052106 (2008).

$^{12}$E. Cockayne and B. P. Burton, Phys. Rev. B $\textbf{62}$, 3735 (2000).

$^{13}$A. R. Akbarzadeh, I. Kornev, C. Malibert, L. Bellaiche, and J.-M. Kiat, Phys. Rev. B $\textbf{72}$, 205104 (2005).

$^{14}$S. A. Prosandeev, E. Cockayne, and B. P. Burton, Phys. Rev. B $\textbf{68}$, 014120 (2003).

$^{15}$R. I. Eglitis, A. V. Postnikov, and G. Borstel, Phys. Rev. B $\textbf{55}$, 12976 (1997).

$^{16}$M. Exner, C. R. A. Catlow, H. Donnerberg, and O. F. Schirmer, J. Phys.: Condens. Matter $\textbf{6}$, 3379 (1994).

$^{17}$J.-J. van der Klink and F. Borsa, Phys. Rev. B $\textbf{30}$, 52 (1984).

$^{18}$E.-A. Zhurova, V. E. Zavodnik, and V. G. Tsirelson, Kristallografiya $\textbf{40}$, 816 (1995) [Crystallogr. Rep. $\textbf{40}$, 753 (1995)].

$^{19}$H. Vogt, Phys. Rev. B $\textbf{58}$, 9916 (1998).

$^{20}$H. Yokota, Y. Uesu, C. Malibert, and J.-M. Kiat, Phys. Rev. B $\textbf{75}$, 184113 (2007).

$^{21}$Y. Uesu, H. Yokota, J.-M. Kiat, and C. Malibert, Ferroelectrics $\textbf{347}$, 37 (2007).

$^{22}$J.-M. Kiat and D. Dkhil, in *From the Structure of Relaxor to the Structure of MPB Systems*, Advanced Dielectric, Piezoelectric and Ferroelectric Materials; Synthesis, Properties and Applications, edited by Pr. Z. G. Ye (Woodhead, Cambridge, UK, 2007), Vol. 41.

$^{23}$H. Yokota, T. Oyama, and Y. Uesu, Phys. Rev. B $\textbf{72}$, 144103 (2005).

$^{24}$W. Kohn and L. J. Sham, Phys. Rev. $\textbf{140}$, A1133 (1965).

$^{25}$The ABINIT code is a common project of the Université Catholique de Louvain, Corning Incorporated, and other contributors (http://www.abinit.org). See also X. Gonze, J.-M. Beuken, R. Caracas, F. Detraux, M. Fuchs, G.-M. Rignanese, L. Sindic, M. Verstraete, G. Zerah, F. Jollet, M. Torrent, A. Roy, M. Mikami, Ph. Ghosez, J.-Y. Raty, and D. C. Allan, Comp. Mat. Sci. $\textbf{25}$, 478–492 (2002).

$^{26}$N. Troullier and J. L. Martins, Phys. Rev. B $\textbf{43}$, 1993 (1991); $\textbf{43}$, 8861 (1991).

$^{27}$K. Leung, Phys. Rev. B $\textbf{63}$, 134415 (2001).

$^{28}$X. Gonze and C. Lee, Phys. Rev. B $\textbf{55}$, 10355 (1997).

$^{29}$C. H. Perry, R. Currat, H. Buhay, R. M. Migoni, W. G. Stirling, and J. D. Axe, Phys. Rev. B $\textbf{39}$, 8666 (1989).

$^{30}$H. Vogt and H. Uwe, Phys. Rev. B $\textbf{29}$, 1030 (1984).

$^{31}$The fact that the atomic Born effective charges do not vary significantly when displacing the atoms from the reference high-symmetry configuration to the Li off-center stable one is caused by the linear evolution of the Berry-phase polarization as a function of atomic displacements when the atoms are displaced from the high-symmetry configuration to the stable one with Li along [001].

$^{32}$Using the Born effective charges of bulk KTO and that of Li deduced from the present calculation induces a slight violation of the effective charge neutrality. However, this violation is small as compared to the total absolute charge and the comparison with the Berry-phase calculation indicates that the approximation made is good.

$^{33}$G. Geneste, E. Bousquet, and Ph. Ghosez, J Comput. Theor. Nanosci. $\textbf{5}$, 517 (2008).

$^{34}$J. Toulouse, B. E. Vugmeister, and R. Pattnaik, Phys. Rev. Lett. $\textbf{73}$, 3467 (1994).

$^{35}$G. Yong, J. Toulouse, R. Erwin, S. M. Shapiro, and B. Hennion, Phys. Rev. B $\textbf{62}$, 14736 (2000).

$^{36}$S. Wakimoto, G. A. Samara, R. K. Grubbs, E. L. Venturini, L. A. Boatner, G. Xu, G. Shirane, and S. H. Lee, Phys. Rev. B $\textbf{74}$, 054101 (2006).

$^{37}$A. Bürgel, W. Kleemann, and U. Bianchi, Phys. Rev. B $\textbf{53}$, 5222 (1996).