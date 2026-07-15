ARTICLE OPEN

# High-dimensional neural network potentials for magnetic systems using spin-dependent atom-centered symmetry functions

Marco Eckhoff $^{1}$ and Jörg Behler $^{1,2}$

Machine learning potentials have emerged as a powerful tool to extend the time and length scales of first-principles quality simulations. Still, most machine learning potentials cannot distinguish different electronic spin arrangements and thus are not applicable to materials in different magnetic states. Here we propose spin-dependent atom-centered symmetry functions as a type of descriptor taking the atomic spin degrees of freedom into account. When used as an input for a high-dimensional neural network potential (HDNNP), accurate potential energy surfaces of multicomponent systems can be constructed, describing multiple collinear magnetic states. We demonstrate the performance of these magnetic HDNNPs for the case of manganese oxide, MnO. The method predicts the magnetically distorted rhombohedral structure in excellent agreement with density functional theory and experiment. Its efficiency allows to determine the Néel temperature considering structural fluctuations, entropic effects, and defects. The method is general and is expected to be useful also for other types of systems such as oligonuclear transition metal complexes.

npj Computational Materials (2021)7:170; https://doi.org/10.1038/s41524-021-00636-z

## INTRODUCTION

In recent years, machine learning potentials (MLPs), which allow extending the time and length scales of first-principles quality atomistic simulations $^{1-3}$, have become a rapidly growing field of research. Increasingly complex systems have been investigated, driving developments and extending the applicability of MLPs. Many of the current MLPs can be classified into four generations as follows $^{4,5}$: the first generation of MLPs proposed already in $1995^{6}$ typically employs a single or a few feed-forward neural networks, making them applicable to low-dimensional systems $^{7,8}$. In 2007, second-generation MLPs have become available with the introduction of high-dimensional neural network potentials (HDNNP) $^{9-12}$. These MLPs are applicable to systems containing thousands of atoms by making use of the locality of a large part of the atomic interactions. For this purpose, the potential energy is calculated as a sum of local environment-dependent atomic energies defined by a cutoff radius. Most modern MLPs belong to this second generation, e.g., HDNNPs $^{9,13}$, Gaussian approximation potentials $^{14}$, moment tensor potentials (MTPs) $^{15}$, and many others $^{16-18}$. The third generation of MLPs includes long-range interactions, mainly electrostatics but also dispersion, beyond the cutoff radius. The electrostatic interactions can be based on element-specific fixed charges $^{14,19}$ or local environment-dependent atomic charges expressed by machine learning (ML) $^{20-22}$. Finally, fourth-generation MLPs take non-local or even global dependencies in the electronic structure into account, and consequently the atomic charges can adapt to non-local charge transfer and even different global charge states. The first method of this generation has been the charge equilibration neural network technique $^{23}$ and further methods such as Becke population neural networks (BpopNN) $^{24}$ and fourth-generation HDNNPs $^{25}$ have been introduced recently.

In spite of these advances, which extended the complexity of the systems and the physical phenomena that can be studied, a remaining limitation of MLPs is the inability to take different spin arrangements and thus magnetic interactions into account. The reason for this limitation is that typically MLPs are trained to represent the potential energy surface (PES) of one electronic state as a function of structural descriptors-most often but not necessarily the ground state of a system. With the exception of different global charge states in fourth-generation potentials, describing multiple electronic states usually requires to train separate MLPs for each state $^{26-30}$ or to use one MLP yielding a set of output energies corresponding to the different excited states $^{31-34}$. The unique structure-energy relation of a given state is a central component of nowadays MLPs and energy changes resulting from different spin arrangements give rise to contradictory information in the training process. Only very recently, magnetic MTPs (mMTPs) $^{35}$ have been proposed as an example of an MLP, which is able to describe magnetic systems containing a single element such as iron.

For studying magnetic materials, the description of a single magnetic state is insufficient, as the atomic magnetic moments fluctuate at finite temperatures. Atomic spin flips often play a role already at ambient temperatures, as the energy differences between different spin configurations are typically in the order of a few meV atom $^{-1}$ only. For example, the Curie and Néel temperatures, at which a material loses its ferromagnetic or antiferromagnetic state, are typically below 1000 and 500 K, respectively $^{36}$. Magnetic transitions often give rise to structural changes $^{37}$. However, current implementations of MLPs are not able to capture these effects, because the magnetic interaction is not included explicitly. For example, if an antiferromagnetic ground state is used for training the MLP, this state will be retained in simulations at higher temperatures irrespective of the magnetic ground state under these conditions.

$^{1}$Universität Göttingen, Institut für Physikalische Chemie, Theoretische Chemie, Tammannstrasse 6, 37077 Göttingen, Germany. $^{2}$Universität Göttingen, International Center for Advanced Studies of Energy Conversion (ICASEC), Tammannstrasse 6, 37077 Göttingen, Germany. $^{\otimes}$email: marco.eckhoff@chemie.uni-goettingen.de joerg.behler@uni-goettingen.de

Published in partnership with the Shanghai Institute of Ceramics of the Chinese Academy of Sciences
![](./images/811642506805510145_1.jpg)

To calculate the energy of a magnetic configuration in an atomistic simulation, models such as the Ising model³⁸, the Heisenberg model³⁹, and the Hubbard model⁴⁰ are widely used. However, these models are based on lattices, and structural and spin changes at finite temperatures cannot be considered simultaneously. Conventional interatomic potentials, which are able to take into account both contributions, have been developed only for a few systems such as iron⁴¹⁻⁴³. The only generally applicable option is the use of ab initio molecular dynamics, which is based on the explicit calculation of the electronic structure in each step and thus is able to distinguish different magnetic states. This approach, however, is inevitably associated with high computational costs restricting simulations to small systems and short timescales.

Beyond the field of PESs, several ML approaches have been developed to address the properties of magnetic compounds, e.g., for the prediction of magnetic moments³⁶ and ordering temperatures⁴⁴⁻⁴⁶ from structural parameters. Moreover, ML methods are able to classify ferromagnetic and antiferromagnetic ground-state materials⁴⁷ and to predict spin-state splittings and metal-ligand bond distances in transition metal complexes⁴⁸,⁴⁹. Recently, a high-dimensional neural network approach for the prediction of oxidation and spin states (high-dimensional neural network spin prediction (HDNNS)) has been developed⁵⁰ and also the Atoms-in-Molecules Network allows predicting atomic spins⁵¹.

In spite of these applications of ML to magnetic compounds, with the exception of mMTPs³⁵, to date there is no method enabling large-scale first-principles quality atomistic simulations of systems explicitly including magnetic interactions and different magnetic states. The main reason is that current MLPs use descriptors exclusively depending on the atomic structure, such as atom-centered symmetry functions (ACSF)⁵², smooth overlap of atomic positions⁵³, and many others⁵⁴. Exceptions are BpopNNs²⁴ and the recently introduced fourth generation of HDNNPs²⁵ in which the atomic charges are included as additional information besides the structural descriptors, to provide qualitative information about the electronic structure.

Describing the spin configuration in a form suitable as input for MLPs is very challenging, as not only the absolute spin values but also the relative spin-up and spin-down arrangements and the relative positions of the atoms are vital. Hence, to predict the energy and forces as a function of the geometric and spin configuration, spin-dependent descriptors are needed. Here we propose spin-dependent ACSFs (sACSFs) to construct MLPs simultaneously applicable to multiple magnetic states including excited states. The sACSFs add the description of the magnetic configuration for the case of collinear spin polarization corresponding to spin-polarized density functional theory (DFT) calculations, i.e., considering spin-up and spin-down electrons without an associated spatial direction. They produce atomic energies as a function of the local geometric and spin environment, and thus formally represent a second-generation potential that can also be combined with third- and fourth-generation MLPs to include additional physics such as long-range electrostatic interactions. In this work, we will benchmark sACSFs employing second-generation HDNNPs⁹, extending these potentials by an explicit dependence on the full collinear spin configuration space to describe magnetic interactions.

We choose manganese oxide, MnO, to assess the quality of the resulting magnetic HDNNPs (mHDNNP) that can be constructed using sACSFs, because of the well-characterized antiferromagnetic ground-state configuration⁵⁵,⁵⁶, the Néel temperature of $T_{\text{N}}^{\text{exp}} = 116\ \text{K}^{57,58}$, and the rhombohedral distortion of the antiferromagnetic phase with lattice constant $a^{\text{exp}} = 4.430\ \text{\AA}$ and lattice angle $\alpha^{\text{exp}} = 90.62^{\circ}$ at $8\ \text{K}^{59}$, making this system a very interesting and challenging benchmark case. The magnetic unit cell is a $2 \times 2 \times 2$ supercell of the geometric unit cell and is built from (111) planes of ferromagnetically coupled Mn ions⁵⁶.
These planes couple antiferromagnetically to the neighboring planes. Spin-polarized DFT calculations employing the hybrid functional PBE0⁶⁰,⁶¹ yield the correct magnetic ground state, called antiferromagnetic type II (AFM-II), with the rhombohedral lattice parameters $a^{\text{PBE0}} = 4.40\ \text{\AA}$ and $\alpha^{\text{PBE0}} = 90.88^{\circ}$ in good agreement with the experiment⁶². The rhombohedral distortion is a consequence of the magnetic anisotropy, which arises from the magnetic dipole interactions⁶³.

Using the mHDNNP, we are able to perform first-principles quality high-throughput studies of the equilibrium geometries and energetics of different collinear magnetic configurations. We can simulate the antiferromagnetic to paramagnetic phase transition to determine the Néel temperature and the associated structural changes. Moreover, the mHDNNP enables the inclusion of defects, and in simulations including Mn vacancies we investigate the formation of different oxidation states by using an additional HDNNS to analyze the temperature dependence of the magnetic moment of the obtained ferrimagnetic configuration.

# RESULTS AND DISCUSSION
## Magnetic high-dimensional neural network potential
The reference data set of the mHDNNP consists of 3101 $2 \times 2 \times 2$ bulk supercells of MnO and Mn₀.₉₆₉O in various magnetic states and their corresponding HSE06⁶⁴⁻⁶⁶ DFT energies and forces. The supercells include different displacements of the atomic positions from the ideal rock salt lattice and distortions of the lattice parameters as well. The construction of the reference data set is described in detail in the Supplementary Methods⁶⁷⁻⁶⁹.

Training this data set with conventional ACSFs yields an energy root mean squared error (RMSE) of about $11\ \text{meV atom}^{-1}$ in the best potential we were able to construct. This RMSE is an order of magnitude larger than the usual HDNNP accuracy of $1\ \text{meV atom}^{-1}$, because the ACSFs can only provide geometrical information to assign the energy. Thus, HDNNPs based on ACSFs only predict an averaged potential energy ignoring the magnetic configurations, whereas e.g., the HSE06 DFT functional yields an energy difference of $45.9\ \text{meV atom}^{-1}$ between the AFM-II order and the ferromagnetic (FM) order for the ideal rock salt MnO structure using the experimental lattice constant $a^{\text{exp}}$.

By including sACSFs to distinguish the magnetic configurations, the energy RMSE is reduced by one order of magnitude to about $1\ \text{meV atom}^{-1}$. The energy difference between the AFM-II and FM orders is resolved and is predicted to be $46.3\ \text{meV atom}^{-1}$ in excellent agreement with the HSE06 reference. Both results demonstrate the ability of the sACSFs to accurately describe the different magnetic configurations. The energy and force component prediction errors are plotted as a function of the reference values in Fig. 1a, b. The underlying number of MnₓO reference structures and key performance indicators such as RMSEs, maximum absolute errors, and fractions of data points with high errors are compiled in Table 1 for the training and test data sets. Even when including various magnetic states, the accuracy of the mHDNNP is in the typical region of state-of-the-art MLPs of $1\ \text{meV atom}^{-1}$ and $0.1\ \text{eV}\ a_0^{-1}$ for energies and forces with a test set energy RMSE of $1.11\ \text{meV atom}^{-1}$ and a test set force components RMSE of $0.066\ \text{eV}\ a_0^{-1}$. $a_0$ is the Bohr radius. In comparison, the RMSE of a recent mMTP for defect-free body centered cubic iron restricted to a fixed lattice parameter is $2.0\ \text{meV atom}^{-1}$³⁵, i.e., in the same order of magnitude.

The absolute atomic spin values $|M_S|$, equivalent to the half-difference of the number of spin-up and spin-down electrons, can be predicted by a separate HDNNS. This HDNNS is trained on the same reference structures covering the range of $1.7 < |M_S| < 2.4$ in case of Mn spins. The resulting RMSE value for these Mn spins is 0.03 for both the training and test set. Only 0.25% of the test data exhibits an error > 0.1, whereby the maximum absolute error is

![](./images/811642506805510145_2.jpg)

Fig. 1 Accuracy of the mHDNNP. a Energy errors $\Delta E=E^{\text{mHDNNP}}-E^{\text{HSE06}}$ as a function of the reference energy $E^{\text{HSE06}}$ and b force component errors $\Delta F=F^{\text{mHDNNP}}-F^{\text{HSE06}}$ as a function of the reference force components $F^{\text{HSE06}}$.

<table>
<caption>Table 1. Details of the mHDNNP fit.</caption>
<thead>
<tr>
<th></th>
<th>Training set</th>
<th>Test set</th>
</tr>
</thead>
<tbody>
<tr>
<td>$N_{\text{struct}}(\text{MnO})$</td>
<td>1387</td>
<td>156</td>
</tr>
<tr>
<td>$N_{\text{struct}}(\text{Mn}_{0.969}\text{O})$</td>
<td>1421</td>
<td>137</td>
</tr>
<tr>
<td>RMSE($E$)</td>
<td>0.86</td>
<td>1.11</td>
</tr>
<tr>
<td>$\Delta E_{\text{max}}$</td>
<td>3.4</td>
<td>4.3</td>
</tr>
<tr>
<td>$\Delta E>2.5$</td>
<td>1.07%</td>
<td>4.44%</td>
</tr>
<tr>
<td>RMSE($F$)</td>
<td>0.067</td>
<td>0.066</td>
</tr>
<tr>
<td>$\Delta F_{\text{max}}$</td>
<td>0.81</td>
<td>0.73</td>
</tr>
<tr>
<td>$\Delta F>0.25$</td>
<td>0.98%</td>
<td>0.89%</td>
</tr>
</tbody>
</table>

Number of Mn,O structures $N_{\text{struct}}$ in the training and test set, and the key performance indicators RMSE, maximum absolute error, and fraction of data points with energy and force errors of the mHDNNP higher than $2.5\,\text{meV}\,\text{atom}^{-1}$ and $0.25\,\text{eV}\,a_0^{-1}$, respectively. The reference energy range is $-5236.6\,\text{meV}\,\text{atom}^{-1}\leq E\leq-5021.2\,\text{meV}\,\text{atom}^{-1}$ and the reference force components range is $|F|\leq2.31\,\text{eV}\,a_0^{-1}$. Energies are provided in $\text{meV}\,\text{atom}^{-1}$ and force components in $\text{eV}\,a_0^{-1}$.

0.20 (Supplementary Fig. 1). Consequently, information about different Mn oxidation states and the magnetic moments can be obtained with accuracy comparable to the underlying first-principles method.

### Magnetic configurations

Besides the accurate description of the energetics, the sACSFs enable to predict structural changes arising from the magnetic configuration. For example, for the rhombohedral MnO global minimum structure with AFM-II order (Fig. 2a), an unconstrained optimization yields the lattice parameters $a^{\text{mHDNNP}}=4.433\,\text{\AA}$ and $\alpha^{\text{mHDNNP}}=90.77^{\circ}$ in very good agreement with the HSE06 DFT results $a^{\text{HSE06}}=4.434\,\text{\AA}$ and $\alpha^{\text{HSE06}}=90.89^{\circ}$, as well as experimental data $a^{\text{exp}}=4.430\,\text{\AA}$ and $\alpha^{\text{exp}}=90.62^{59}$.

![](./images/811642506805510145_3.jpg)

Fig. 2 Different magnetic orders of MnO. a Rhombohedral MnO global minimum structure with AFM-II order, b magnetic order degenerate to the cubic AFM-II order, c AFM-I order, and d FM order of MnO. Small red balls represent O atoms, large violet ones Mn atoms with spin-up, and large blue ones Mn atoms with spin-down$^{95}$. Different perspectives of the magnetic orders a and b are shown in the Supplementary Fig. 3.

Further, also excited magnetic configurations are predicted in excellent agreement with HSE06. For example, the lattice parameter of the resulting cubic lattice of the FM configuration (Fig. 2d) is $a_{\text{FM}}^{\text{mHDNNP}}=4.461\,\text{\AA}$ compared to $a_{\text{FM}}^{\text{HSE06}}=4.462\,\text{\AA}$. The energy difference to the global minimum is $45.8\,\text{meV}\,\text{atom}^{-1}$ in excellent agreement with the HSE06 value $45.5\,\text{meV}\,\text{atom}^{-1}$. The longer distances between ferromagnetically compared to antiferromagnetically interacting Mn ions in MnO are emphasized by the optimized lattice parameters of the AFM-I configuration (Fig. 2c) with tetragonal lattice parameters $a_{\text{AFM-I}}^{\text{mHDNNP}}=4.461\,\text{\AA}$ and $c_{\text{AFM-I}}^{\text{mHDNNP}}=4.414\,\text{\AA}$ ($a_{\text{AFM-I}}^{\text{HSE06}}=4.459\,\text{\AA}$ and $c_{\text{AFM-I}}^{\text{HSE06}}=4.420\,\text{\AA}$), as the lattice is elongated in both directions of FM interactions to the nearest neighbors. In conclusion, the lattices of FM (cubic), AFM-I (tetragonal), and AFM-II orders (rhombohedral), as well as other magnetic configurations can be distinguished due to the magnetic interaction. Further, the mHDNNP can provide information about the influence of defects on the magnetic order. For example, one spin-flip in the AFM-II configuration per $2\times2\times2$ supercell reduces the rhombohedral distortion by $0.09^{\circ}$ (HSE06: $0.11^{\circ}$). The corresponding energy increase is $1.5\,\text{meV}\,\text{atom}^{-1}$ (HSE06: $1.5\,\text{meV}\,\text{atom}^{-1}$).

The efficiency of the mHDNNP in combination with a basin-hopping Monte Carlo (MC) scheme$^{70}$ in which MC spin flips are employed instead of atomic displacements enables high-throughput searches of the minima in spin configuration space, which would be computationally too demanding employing DFT. The spin-flip basin-hopping MC simulations of $2\times2\times2$ MnO supercells and molecular dynamics (MD) simulations including MC spin flips (MDMC) of $6\times6\times6$ MnO supercells confirmed the rhombohedral AFM-II magnetic order to be the global minimum in agreement with experiments$^{56}$. However, if the lattice is restricted to be cubic, two degenerate global minima exist: the AFM-II configuration shown in Fig. 2a and another antiferromagnetic

order shown in Fig. 2b, which is not based on (111) planes of ferromagnetically coupled Mn ions. DFT calculations confirm this result. Radial distribution functions (Supplementary Fig. 4) show that the same ferromagnetic and antiferromagnetic interactions are present in the two configurations. This second cubic global minimum configuration stays cubic in an unconstrained optimiza- tion. The rhombohedral distortion of the AFM-II order can therefore be identified as the origin of the energetic preference. The energy gain by the rhombohedral distortion is 1.9 meV atom⁻¹ (HSE06: 2.1 meV atom⁻¹).

### Magnetic interactions
For the ideal cubic structure, a Heisenberg spin Hamiltonian can be constructed,

$$
H = -\frac{J_1 k_\mathrm{B}}{2} \sum_{i} \sum_{n_i} \boldsymbol{S}_i \boldsymbol{S}_{n_i} - \frac{J_2 k_\mathrm{B}}{2} \sum_{i} \sum_{m_i} \boldsymbol{S}_i \boldsymbol{S}_{m_i}, \tag{1}
$$

which includes the magnetic interactions of atom $i$ with its nearest neighbors $n_i$ and next nearest neighbors $m_i$. The strengths of the magnetic coupling between the vector spin operators $\boldsymbol{S}_i$ and $\boldsymbol{S}_{n_i}$, as well as $\boldsymbol{S}_i$ and $\boldsymbol{S}_{m_i}$, are given by the exchange coupling constants $J_1$ and $J_2$, respectively. $k_\mathrm{B}$ is the Boltzmann constant. The exchange coupling constants can be determined employing energy differences (per atom) between the FM, AFM-I, and AFM- II configurations. Rearranging Eq. (1) for these systems yields

$$
J_1 = \frac{E_\mathrm{AFM-I} - E_\mathrm{FM}}{4S^2 k_\mathrm{B}}, \tag{2}
$$

$$
J_2 = \frac{4E_\mathrm{AFM-II} - 3E_\mathrm{AFM-I} - E_\mathrm{FM}}{12S^2 k_\mathrm{B}}, \tag{3}
$$

with the spin $S = \frac{5}{2}$ of the high-spin $\mathrm{Mn}^\mathrm{II}$ ions (Supplementary Discussion). Using mean field theory⁷¹, the Néel temperature can be calculated as

$$
T_\mathrm{N} = -2S(S+1)J_2. \tag{4}
$$

Employing the HSE06 DFT energies for the lattice constant $a^\mathrm{exp}$, we obtain $J_1^\mathrm{HSE06} = -13.9$ K, $J_2^\mathrm{HSE06} = -14.5$ K, and $T_\mathrm{N}^\mathrm{HSE06} = 255$ K. The mHDNNP results match these values almost perfectly with $J_1^\mathrm{mHDNNP} = -14.0$ K, $J_2^\mathrm{mHDNNP} = -14.6$ K, and $T_\mathrm{N}^\mathrm{mHDNNP} = 256$ K. This agreement underlines the accuracy of the sACSFs and of the mHDNNP method in describing the multiple PESs of the MnO magnetic states.

The overestimation of HSE06 compared to the experimental Néel temperature $T_\mathrm{N}^\mathrm{exp} = 116$ K⁵⁷,⁵⁸ was also found for other hybrid DFT functionals in previous studies. For example, the PBE0 functional yields $T_\mathrm{N} = 240$ K⁶² and the HSE03 functional $T_\mathrm{N} =$ 230 K⁷². Similar to these functionals, HSE06 predicts too negative exchange coupling constants of MnO compared to the experi- mentally determined values $J_1^\mathrm{exp} = -8.5$ K and $J_2^\mathrm{exp} = -9.6$ K⁷³,⁷⁴. Therefore, the strength of antiferromagnetic interactions is overestimated favoring the stability of the antiferromagnetic phase. The Néel temperature is consequently overestimated by the mHDNNP as well, which is based on HSE06 reference data. This overestimation is thus not an inherent error of the mHDNNP method and the agreement with experiment could be improved by using another reference method.

### Néel temperature
Mean field theory misses the influence of specific magnetic configurations of MnO on the Néel temperature. Moreover, the underlying Heisenberg spin Hamiltonian restricts the system to a fixed lattice. Employing the mHDNNP, we can overcome both limitations step by step to reveal their influences on the Néel temperature. Conventional MC spin-flip simulations use a fixed lattice but allow exploring the specific states of MnO. Using isothermal-isobaric ($NpT$) MD trajectories in MDMC simulations, both the atomic positions and the lattice parameters can adapt to the magnetic configurations including thermal fluctuations.

The phase transition temperature is observable as peak in the molar heat capacity as a function of the temperature. The molar heat capacity at constant volume $C_V$ can be obtained from MC spin-flip simulations and the molar heat capacity at constant pressure $C_p$ from MDMC simulations as described in section "Simulation analysis."

To identify the AFM-II to PM transition, the temperature dependence of the order parameter $C$ defined in section "Simulation analysis" can be used. This order parameter takes into account the maximal alignment of the magnetic configura- tions to an AFM-II configuration. The order parameter is $C=1$ if the magnetic configuration corresponds to AFM-II during the entire simulation. It is $C=0.5$ in case of the second cubic global minimum. The variety of paramagnetic (PM) configurations leads to a smaller value $C \lesssim 0.2$, as the PM orders are not correlated to the AFM-II order.

MC spin-flip simulations of a cubic $6 \times 6 \times 6$ MnO supercell using the lattice constant $a^\mathrm{exp}$ yield a transition temperature of 300 K ($\mathrm{MC}_\mathrm{cub}^\mathrm{AFM-II}$ and $\mathrm{MC}_\mathrm{cub}$ in Fig. 3). We note that these simulations are different from MC simulations using only $J_1$ and $J_2$ coupled interactions, because here the full PES from the HSE06 reference data is explored. The order parameter of these simulations ($\mathrm{MC}_\mathrm{cub}^\mathrm{AFM-II}$ and $\mathrm{MC}_\mathrm{cub}$ in Fig. 4) proves that the transition temperature belongs to the antiferromagnetic to PM transition. The Néel temperature is the same for the disordering process ($\mathrm{MC}_\mathrm{cub}^\mathrm{AFM-II}$) and the ordering process ($\mathrm{MC}_\mathrm{cub}$), i.e., no hysteresis is present. The AFM-II to PM ($\mathrm{MC}_\mathrm{cub}^\mathrm{2nd}$) and the second cubic global minimum to PM ($\mathrm{MC}_\mathrm{cub}$) transition temperatures are identical because of the equal interactions of both cubic global minimum configurations. The ordering process can consequently also end in the second cubic global minimum configuration as had happened in the $\mathrm{MC}_\mathrm{cub}$ simulations at 120, 160, and 200 K. However, below the Néel temperature, the interconversion of both cubic global minima is kinetically hindered. In summary, the inclusion of specific state information increases the Néel temperature of MnO by about 50 K compared to the mean field theory.

The restriction to a cubic lattice is an approximation, because the AFM-II minimum energy configuration has a rhombohedral

![](./images/811642506805510145_4.jpg)

Fig. 3 Temperature dependence of the heat capacity. Molar heat capacity at constant volume $C_V$ (MC) and pressure $C_p$ (MDMC) divided by the Boltzmann constant $k_\mathrm{B}$ and the Avogadro constant $N_\mathrm{A}$ as a function of the temperature $T$ obtained in different simulation methods for $6 \times 6 \times 6$ MnO supercells. The superscript of the simulation method defines the initial magnetic configuration (cubic AFM-II or second global minimum), otherwise random initial magnetic orders are used. The subscript cub indicates the restriction to the cubic lattice with $a^\mathrm{exp}$=4.430 Å and the subscript min indicates an optimization of the initial structure prior to the MC simulation.

![](./images/811642506805510145_5.jpg)

Fig. 4 Temperature dependence of the order parameter. Order parameter $C$ as a function of the temperature $T$ obtained in different simulation methods for $6 \times 6 \times 6$ MnO supercells. The superscript of the simulation method defines the initial magnetic configuration (cubic AFM-II or second global minimum), otherwise random initial magnetic orders are used. The subscript cub indicates the restriction to the cubic lattice with $a^{\exp }=4.430 \AA$ and the subscript min indicates an optimization of the initial structure prior to the MC simulation. Lines are only drawn to guide the eyes.

lattice. Employing the rhombohedral lattice (MC$_{\text{min}}^{\text{AFM-II}}$) increases the Néel temperature to about 480 K. This increase can be explained by the mean energies of the AFM-II and PM configurations. Although the energy difference is $7.0 \, \text{meV atom}^{-1}$ for the experimental cubic lattice, it is $10.6 \, \text{meV atom}^{-1}$ for the rhombohedral lattice. To obtain similar Boltzmann factors during the MC$_{\text{min}}^{\text{AFM-II}}$ simulation compared to the MC$_{\text{cub}}^{\text{AFM-II}}$ simulation, the temperature has to be raised by the same factor of 1.5, which is similar to the increase of the Néel temperature (Supplementary Discussion). The data of the PM phase were calculated from 1000 PM configurations, whose magnetic orders were obtained during the 10 ns MDMC simulation at 400 K. On the other hand, an optimized lattice of the initial PM configuration (MC$_{\text{min}}$) leads to a Néel temperature of about 290 K. In conclusion, the choice of a specific fixed lattice can change the Néel temperature by about 200 K. Adapting the lattice and the atomic positions to the magnetic order is consequently of major importance to obtain reliable results.

$NpT$ MD enables to sample the thermodynamic equilibrium of the given magnetic configuration at pressure $p$ and temperature $T$ to get rid of simulation artifacts due to a restricted geometric structure. The MDMC simulations are therefore a much better representation of experimental conditions. MDMC simulations predict an AFM-II to PM transition at 300 K (MDMC$^{\text{AFM-II}}$ and MDMC in Figs. 3 and 4). This temperature is similar to the result of the cubic lattice due to a compensation of two main factors: the optimized AFM-II lattice (at $p=1$ bar) leads to an energy gain of $1.9 \, \text{meV atom}^{-1}$ compared to the cubic lattice with $a^{\exp}$, whereas the mean energy gain of the PM configurations is $1.3 \, \text{meV atom}^{-1}$. In addition, thermal fluctuations of the atomic positions are included in MDMC simulations leading to thermal expansion of the MnO lattice with increasing temperature. To quantify the energy increase due to the larger lattice volume, optimizations at various pressures of the AFM-II and PM configurations were performed. If the optimized volume at $p=1$ bar is increased to the volume given at 300 K in the MDMC simulations (Fig. 5), the energy of the AFM-II configuration is increased by $1.7 \, \text{meV atom}^{-1}$ and the mean energy of the PM configurations by $1.1 \, \text{meV atom}^{-1}$ (Supplementary Fig. 5$^{75,76}$).

The cube root of the mean lattice volume, i.e., a hypothetical averaged cubic lattice constant, shows a discontinuous increase of $0.005 \, \text{\AA}$ at the Néel temperature (Fig. 5). This increase is similar to the difference of the optimized AFM-II and PM values, which also differ by $0.005 \, \text{\AA}$. In accordance with the simulations, experimentally an increase of about $0.004 \, \text{\AA}$ has been observed at the Néel temperature$^{77}$. The mean lattice angle decreases from $90.77$ to $90.00^{\circ}$ at the Néel temperature as shown in the Supplementary Fig. 6 matching the experimental PM angle of $90.00^{\circ}$$^{77}$. This discontinuous change of the lattice volume and shape confirms a first-order magnetic phase transition$^{78,79}$.

![](./images/811642506805510145_6.jpg)

Fig. 5 Thermal expansion of MnO. Cube root of the mean volume per unit cell $\sqrt[3]{\bar{V}}$ as a function of the temperature $T$ obtained in 10 ns $NpT$ MD simulations including MC spin flips of $6 \times 6 \times 6$ MnO supercells and the optimized values at $p=1$ bar of the AFM-II and PM configurations. The straight lines represent linear fits for the high- and low-temperature regions.

The linear thermal expansion coefficient of the PM phase has been measured to be $a_{\text{L}}^{\exp }=12 \cdot 10^{-6} \mathrm{~K}^{-1}$ at $400 \mathrm{~K}^{80}$. Employing the data from the MDMC simulations of the PM phase $a_{\text{L}}^{\text{mHDNNP}}=14 \cdot 10^{-6} \mathrm{~K}^{-1}$ at 400 K is obtained in good agreement with the experiment.

In conclusion, mHDNNPs combine the accuracy and generality of first-principles methods with an efficiency close to spin lattice models. The Néel temperature of MnO calculated by mean field theory differs by about 50 K from the MC result, which explicitly samples the magnetic configurations. Including structural fluctuations in the prediction of magnetic transition temperatures is essential, because fixing the lattice to the low- or high-temperature configuration can lead to differences of about 200 K. mHDNNP-driven MD simulations including MC spin flips reveal a small volume increase and the disappearance of the rhombohedral distortion at the Néel temperature of MnO, as the method is able to provide mean geometric and thermodynamic data of the PM phase.

## Defects
Magnetic properties of bulk materials differ from those of nanoparticles and doped materials. Surfaces, interfaces, defects, and doping can change the magnetic order leading, e.g., to net surface spins or lower transition temperatures$^{81-83}$. Surface layers with different stoichiometries can lead to different magnetic orders, such as antiferromagnetic MnO nanoparticles with ferrimagnetic $\text{Mn}_3\text{O}_4$ shells$^{84}$. To confirm that such systems can, in principle, be described by mHDNNPs, we predict the impact of Mn vacancies using the mHDNNP. Mn vacancies alter the magnetic order and increase the oxidation states of the remaining Mn ions to compensate the oxygen excess ensuring overall charge neutrality. In principle, it is also possible to study the role of surfaces and doping, but our current parameterization is based on $\text{Mn}_x\text{O}$ bulk data only, with $x=0.969$ and 1, and thus the present mHDNNP is not applicable to these situations.

From the heat capacities shown in the Supplementary Fig. 7 and the order parameters in Fig. 6, the Néel temperatures can be determined to be $(298 \pm 1) \text{K}$ for MnO, $(296 \pm 1) \text{K}$ for $\text{Mn}_{0.999}\text{O}$, $(275 \pm 1) \text{K}$ for $\text{Mn}_{0.991}\text{O}$, and $(233 \pm 1) \text{K}$ for $\text{Mn}_{0.969}\text{O}$. The increasing Mn vacancy concentration decreases the Néel

![](./images/811642506805510145_7.jpg)

Fig. 6 Impact of Mn vacancies on the temperature dependence of the order parameter. Order parameter $C$ as a function of the temperature $T$ obtained in MDMC simulations for $6 \times 6 \times 6$ supercells of MnO, $\mathrm{Mn}_{0.999} \mathrm{O}, \mathrm{Mn}_{0.991} \mathrm{O}$, and $\mathrm{Mn}_{0.969} \mathrm{O}$.

temperature. The more Mn vacancies are present, the lower is the average number of magnetic neighbor ions whose interactions can support the stability of the ordered phase against temperature-induced fluctuations. Consequently, the Néel temperature can be used as a hint for the regularity of a material's crystal structure. This trend is in accordance with experiments that observe an increase of the magnetic transition temperature with higher contents of magnetic ions $^{81}$.

Employing the HDNNS, we are able to calculate the absolute magnitude of the atomic spins whose signs are provided in the input of the mHDNNP. In this way, we can investigate the impact of defects on the Mn oxidation states and the magnetization. For this purpose, we optimized the MnO and $\mathrm{Mn}_{0.969} \mathrm{O}$ structures with AFM-II order using the mHDNNP. For MnO, we observe 16 Mn ions with $M_{S}=2.26$ and 16 with $M_{S}=-2.26$ per magnetic unit cell, whereas for $\mathrm{Mn}_{0.969} \mathrm{O}$ we find 2 Mn ions with $M_{S}=1.83$, 14 with $2.24 \leq M_{S} \leq 2.26$, and 15 with $-2.26 \leq M_{S} \leq-2.24$. Consequently, in MnO all Mn ions are $\mathrm{Mn}^{\mathrm{II}}$ and in $\mathrm{Mn}_{0.969} \mathrm{O}$ two Mn ions per Mn vacancy are $\mathrm{Mn}^{\mathrm{III}}$, whereas the others are $\mathrm{Mn}^{\mathrm{II}}$. The difference of the $M_{S}$ values from the expected values of 2 and $\frac{5}{2}$ is also obtained in the HSE06 reference data. As expected, the excess of O ions due to the Mn vacancy is compensated by increased oxidation of Mn ions. To retain a small net magnetization, $\mathrm{Mn}^{\mathrm{III}}$ is formed at magnetic lattice sites, which do not have the same spin sign as the missing Mn ion. The sum of the atomic spins per magnetic unit cell is $\bar{M}_{S}=1.42$ for $\mathrm{Mn}_{0.969} \mathrm{O}$.

MDMC simulations of $6 \times 6 \times 6$ supercells analyzed by the HDNNS reveal that the magnetization of MnO is always zero as shown in Fig. 7, because it is either antiferromagnetic or paramagnetic. However, as the Mn vacancies are placed on an equidistant grid, the constructed $\mathrm{Mn}_{0.969} \mathrm{O}$ structure is ferrimagnetic at low temperatures. Below the transition temperature, the magnetization is finite but decreases with increasing temperature, because more and more spin flips happen. At the transition temperature of $233 \mathrm{~K}$, a sudden drop to zero occurs as the system becomes paramagnetic. The average number of $\mathrm{Mn}^{\mathrm{III}}$ ions during all MDMC simulations of $\mathrm{Mn}_{0.969} \mathrm{O}$ at different temperatures is predicted to be about 1.9 employing the criterion $\left|M_{S}\right|<2.025$. This value is slightly smaller than the ideal value of 2 such that most of the $\mathrm{Mn}^{\mathrm{III}}$ are identified correctly. In total, $99.5 \%$ of the $\mathrm{Mn}^{\mathrm{II}}$ and $\mathrm{Mn}^{\mathrm{III}}$ ions are assigned correctly.

In conclusion, Mn vacancies lead to a reduced Néel temperature and the formation of $\mathrm{Mn}^{\mathrm{III}}$ ions. The net magnetization induced by Mn vacancies drops to zero at the transition temperature. Consequently, different stoichiometries and associated oxidation states changes are accurately described by the mHDNNP, highlighting the generality and applicability of this method.

Beyond the present work, we expect the mHDNNP method to be a powerful tool for highly accurate, large-scale atomistic simulations of systems involving different magnetic states, such as a variety of magnetic materials and molecular transition metal complexes containing spin-polarized atoms. Theoretical predictions of the magnetic, geometric, and thermodynamical implications of surfaces, interfaces, defects, and doping can provide interesting control tactics for material properties and finally for technological applications.

![](./images/811642506805510145_8.jpg)

Fig. 7 Temperature dependence of the magnetization. Sum of the atomic spins per magnetic unit cell $\bar{M}_{S}$ as a function of the temperature $T$ obtained in optimizations and MDMC simulations for $6 \times 6 \times 6$ supercells of MnO and $\mathrm{Mn}_{0.969} \mathrm{O}$.

## METHODS
### High-dimensional neural network potential
The MLP used in this work is a second-generation HDNNP $^{9}$. In this method, the potential energy $E$ is constructed as a sum of atomic energy contributions,
$$
E=\sum_{m=1}^{N_{\text {elem }}} \sum_{n=1}^{N_{\text {atoms }}^{m}} E_{n}^{m}\left(\mathbf{G}_{n}^{m}\right),
\tag{5}
$$
for a system containing $N_{\text {elem }}$ elements and $N_{\text {atoms }}^{m}$ atoms of element $m$. For each element, an individual neural network is trained, which can provide the atomic energy as a function of the local chemical environment and which is evaluated as often as atoms of the respective element are present. The structural descriptors $\mathbf{G}_{n}^{m}$ are vectors of many-body ACSFs $^{52}$, which fulfill the mandatory translational, rotational, and permutational invariances of the PES and serve as input vectors of the atomic neural networks. ACSFs describe the local atomic environment as a function of the positions of all neighboring atoms inside a cutoff sphere of radius $R_{c}$. To include all energetically relevant interactions, the cutoff radius has to be sufficiently large. Besides the positions of the atoms, only the elements have to be specified leading to a potential being able to describe the making and breaking of bonds. The dimensionality of the ACSF vectors can be predefined for each element individually and does not depend on the atomic environments. This ensures that the number of input neurons of the atomic neural networks remains constant during MD simulations. After optimizing the parameters of the atomic neural networks in a training process using the potential energies and force components of reference systems obtained from DFT, the HDNNP can be applied in large-scale simulations at a small fraction of the computational costs. More details about HDNNPs, their construction, and validation can be found in several reviews $^{5,10-12}$.

### Atom-centered symmetry functions
Two types of ACSFs are most commonly used for the construction of HDNNPs: the radial symmetry functions,
$$
G_{i}^{\mathrm{rad}}=\sum_{j} \mathrm{e}^{-\eta R_{i j}^{2}} \cdot f_{c}\left(R_{i j}\right),
\tag{6}
$$
and the angular symmetry functions,
$$
G_{i}^{\mathrm{ang}}=2^{-\zeta} \sum_{j} \sum_{k \neq j}\left[1+\lambda \cos \left(\theta_{i j k}\right)\right]^{\zeta} \cdot \mathrm{e}^{-\eta\left(R_{i j}^{2}+R_{i k}^{2}+R_{j k}^{2}\right)} \cdot f_{c}\left(R_{i j}\right) \cdot f_{c}\left(R_{i k}\right) \cdot f_{c}\left(R_{j k}\right),
\tag{7}
$$


![](./images/811642506805510145_9.jpg)

Fig. 8. Interactions resulting in non-zero values of the radial and angular spin-augmentation functions. Red circles with a zero represent atoms with $s=0$, purple circles with a plus sign atoms with $s=1$, and blue circles with a minus sign atoms with $s=-1$. The first atom of each entry is the central atom $i$ of the sACSF. The order of the neighbor atoms in the angular interactions is insignificant. The inverse interactions (i.e., switching "+" and "-") yield the same result and are not shown for clarity.

$$
f_{\mathrm{c}}\left(R_{i j}\right)= \begin{cases}\frac{1}{2} \cos \left(\frac{\pi R_{i j}}{R_{\mathrm{c}}}\right)+\frac{1}{2} & \text { for } R_{i j} \leq R_{\mathrm{c}} \\ 0 & \text { otherwise }\end{cases}.
\tag{8}
$$

$R_{i j}$ is the distance between central atom $i$ and neighboring atom $j$. $\theta$ is the angle $j-i-k$ involving two neighbors $j$ and $k$. $\eta, \lambda$, and $\zeta$ are parameters defining the spatial shapes of the ACSFs. Consequently, the ACSF values only depend on the local geometric environment of the atoms. For multicomponent systems containing several elements, ACSFs for all element combinations are explicitly included. A detailed discussion of the properties of conventional ACSFs and further functional forms can be found in ref. $^{52}$.

### Spin-dependent atom-centered symmetry functions
In many cases, the representation of atomic oxidation and spin states, i.e., the absolute magnitude of the atomic spins, is possible in an indirect way even with conventional ACSFs as shown in our previous studies$^{50,69}$ and in the Supplementary Figs. 1 and 2 of this work. The reason is that different absolute spins in most cases change the geometric structure of the atomic environments. These different environments allow constructing the structure-energy relationship for the ground state by HDNNPs, as long as there is a unique relation between the geometric structure and the electronic configuration. Therefore, ACSFs are able to indirectly capture the energetic effects of the atomic spin magnitude via the geometric structure. Examples are different oxidation states or high- and low-spin states of transition metal ions, for which the different orbital occupations can give rise to structural changes in the local atomic environments such as different bond lengths or Jahn-Teller distortions.

However, the relative parallel and antiparallel arrangement of an atomic spin with respect to the spins of all other magnetic atoms in its environment is not captured by ACSFs. This information is required to distinguish different magnetic configurations and to predict the corresponding potential energies. To extend the applicability to arbitrary collinear spin arrangements, the signs of the atomic spins have to be known explicitly. In principle, also the explicit inclusion of absolute spin values is of interest, but we leave this aspect to future work here.

To describe the magnetic configuration, we introduce an atomic spin coordinate,
$$
s_{i}= \begin{cases}0 & \text { for }\left|M_{S}\right|<M_{S}^{\text {thres }} \\ \operatorname{sgn}\left(M_{S}\right) & \text { otherwise }\end{cases},
\tag{9}
$$
with
$$
M_{S}=\frac{1}{2}\left(n_{\uparrow}-n_{\downarrow}\right).
\tag{10}
$$

$M_{S}$ is the half-difference of the number of spin-up electrons $n_{\uparrow}$ and spin-down electrons $n_{\downarrow}$ of an atom $i$ in a collinear spin-polarized calculation. The atomic spin coordinate is equal to the sign of $M_{S}$, unless the absolute atomic spin value is smaller than a threshold value $M_{S}^{\text {thres }}$. The threshold is introduced to filter out noise in the spin reference data arising from the ambiguity in assigning spins in electronic structure calculations. In this work, $M_{S}^{\text {thres }}$ is set to 0.25. The set of atomic spin coordinates can represent all possible collinear magnetic configurations enabling to identify ferromagnetic and antiferromagnetic spin arrangements, as well as non-magnetic interactions.

To integrate the spin coordinates into the radial ACSFs, the radial spin-augmentation function (SAF) $M^{x}(s_{i}, s_{j})$ is employed,
$$
G_{i}^{\mathrm{rad}}=\sum_{j} M^{x}\left(s_{i}, s_{j}\right) \cdot \mathrm{e}^{-\eta R_{i j}^{2}} \cdot f_{\mathrm{c}}\left(R_{i j}\right).
\tag{11}
$$

Different radial SAFs, with $x=0,+,-$, are used to describe the interactions of same (ferromagnetic interactions) and opposite spin signs (antiferromagnetic interactions), respectively,
$$
M^{0}\left(s_{i}, s_{j}\right)=1,
\tag{12}
$$

$$
M^{+}\left(s_{i}, s_{j}\right)=\frac{1}{2}\left|s_{i} s_{j}\right| \cdot\left|s_{i}+s_{j}\right|,
\tag{13}
$$

$$
M^{-}\left(s_{i}, s_{j}\right)=\frac{1}{2}\left|s_{i} s_{j}\right| \cdot\left|s_{i}-s_{j}\right|.
\tag{14}
$$

The radial SAFs $M^{x}(s_{i}, s_{j})$ are non-zero only for specific combinations of the spin coordinates of the atom pairs as summarized in Fig. 8. This spin augmentation filters the contributions to the radial sACSF in Eq. (11), to distinguish the different magnetic interactions. Only interactions between atoms of parallel spins contribute to sACSFs containing $M^{+}$and only interactions between atoms of antiparallel spins contribute to a sACSFs containing $M^{-}$. If $s=0$ for one or both of the interacting atoms, $M^{+}$and $M^{-}$are zero, leaving only a contribution to the sACSF containing $M^{0}$. Taking the absolute values in $M^{+}$and $M^{-}$ensures that the descriptor only depends on the relative spin arrangement. In this way, a simultaneous sign change of all atomic spins does not change the value of the sACSFs, ensuring the invariance of the potential energy with respect to the absolute spin arrangement. $M^{0}$ is used to describe the non-magnetic, purely geometry-dependent interactions between an $s \neq 0$ atom and an $s=0$ atom or between two $s=0$ atoms, which are not included in the other terms.

When constructing an mHDNNP, it is sufficient to use sACSFs only as input for the atomic neural networks of elements exhibiting atoms with non-zero spins. For the atomic neural networks of all other elements, conventional ACSFs can be used, which is equivalent to using only $M^{0}$ and $M^{00}$ in the sACSFs of these elements. In the same way as ACSFs, sACSFs are constructed for all element combinations. The choice, which SAFs, i.e., only $M^{0}$ or both $M^{+}$and $M^{-}$, are required for a given element combination, can be made before constructing the potential, because in most systems the atoms of a given element are either all characterized by $s=0$ or by $s \neq 0$. For instance, in MnO the Mn atoms exhibit $s \neq 0$ and the O atoms correspond to $s=0$. Still, the method is also applicable to other systems including partly magnetically active elements. These systems require the use of $M^{0^{\prime}}$ (Supplementary Methods) instead of $M^{0}$, to explicitly separate non-magnetic from magnetic interactions, as well as a careful choice of $M_{S}^{\text {thres }}$ to assign physically meaningful spin coordinate values. For element combinations of partly magnetically active elements with (partly) magnetically active elements, all radial SAFs, $M^{0^{\prime}}$, $M^{+}$, and $M^{-}$, are required.

In a similar way, angular sACSFs can be defined as
$$
G_{i}^{\mathrm{ang}}=2^{-\zeta} \sum_{j} \sum_{k \neq j} M^{x x}\left(s_{i}, s_{j}, s_{k}\right) \cdot\left[1+\lambda \cos \left(\theta_{i j k}\right)\right]^{\zeta} \cdot \mathrm{e}^{-\eta\left(R_{i j}^{2}+R_{i k}^{2}+R_{j k}^{2}\right)} \cdot f_{\mathrm{c}}\left(R_{i j}\right) \cdot f_{\mathrm{c}}\left(R_{i k}\right) \cdot f_{\mathrm{c}}\left(R_{j k}\right),
\tag{15}
$$

containing the angular SAFs $M^{x x}(s_{i}, s_{j}, s_{k})$. They allow distinguishing three different interactions of a central $s \neq 0$ atom $i$ with two neighboring $s \neq 0$ atoms $j$ and $k$: (1) $s_{i}=s_{j}=s_{k}$, (2) $s_{i} \neq s_{j}=s_{k}$, and (3) $s_{i}=s_{j} \neq s_{k}$. The fourth possibility $s_{i}=s_{k} \neq s_{j}$ is equivalent to (3), as the sums over $j$ and $k$ in the angular sACSFs include the interactions $j-i-k$ and $k-i-j$, as both $j$ and $k$ sum over all contributing neighbor atoms to exclude any dependence on the order of the atoms. An efficient separation of these interactions is

M. Eckhoff and J. Behler

given by the functions,
$$M^{00}\left(s_{i}, s_{j}, s_{k}\right)=1, \tag{16}$$

$$M^{++}\left(s_{i}, s_{j}, s_{k}\right)=\left\{\begin{array}{ll}
\frac{1}{2}\left|s_{i}\right| \cdot\left(\left|s_{i}+s_{j}+s_{k}\right|-1\right) & \left\{\begin{array}{l}
\text { for } s_{j} \neq 0 \wedge s_{k} \neq 0 \\
\text { for } s_{j}=0 \wedge s_{k}=0
\end{array},\right. \\
\frac{1}{2}\left|s_{i}\right| \cdot\left|s_{i}+s_{j}+s_{k}\right| & \text { otherwise }
\end{array}\right. \tag{17}$$

$$M^{--}\left(s_{i}, s_{j}, s_{k}\right)=\left\{\begin{array}{ll}
\frac{1}{2}\left|s_{i}\right| \cdot\left(\left|s_{i}-s_{j}-s_{k}\right|-1\right) & \left\{\begin{array}{l}
\text { for } s_{j} \neq 0 \wedge s_{k} \neq 0 \\
\text { for } s_{j}=0 \wedge s_{k}=0
\end{array},\right. \\
\frac{1}{2}\left|s_{i}\right| \cdot\left|s_{i}-s_{j}-s_{k}\right| & \text { otherwise }
\end{array}\right. \tag{18}$$

$$M^{+-}\left(s_{i}, s_{j}, s_{k}\right)=\left|s_{i} s_{j} s_{k}\right| \cdot\left(\left|s_{i}+s_{j}-s_{k}\right|-1\right), \tag{19}$$
as depicted in Fig. 8. $M^{00}$ is required to describe interactions including more than one $s=0$ atom or if atom $i$ is $s=0$. $M^{++}, M^{--}$, and $M^{+-}$ yield 1 for the interaction types (1), (2), and (3), respectively, and 0 for the other types in case of $s \neq 0$ atoms. For the interactions of two $s \neq 0$ atoms with one $s=0$ atom, whereby atom $i$ is $s \neq 0$, only $M^{++}$ and $M^{--}$ are required, separating the ferromagnetic and antiferromagnetic interactions similarly as in the radial sACSFs. For systems in which atoms of the same element can be $M_{S} \neq 0$ and $M_{S}=0, M^{00^{\prime}}$ (Supplementary Methods) has to be used instead of $M^{00}$ to distinguish non-magnetic and magnetic interactions, and the contributions of $M^{++}$ and $M^{--}$ have to be further split as described in the Supplementary Methods and Supplementary Table 1.

In summary, the combination of both the arrangement of the spins and the geometry-dependent determination of the atomic spin magnitudes is essential to provide all the information necessary to construct reliable PESs in the case of collinear spins. The functional form of the sACSFs might look similar to an Ising-like description at first glance, but the method allows us to study all systems that can also be addressed by collinear DFT calculations, because the mHDNNP simultaneously depends on the geometric structure, indirectly on the atomic spin magnitudes, and on the atomic spin arrangements. For energy and force predictions, the specification of the elements, atomic coordinates, and atomic spin arrangements is required as input covering the full geometric and magnetic configuration space. Both the training of only several selected magnetic configurations and also the training of the full magnetic configuration space including excited magnetic states are possible using mHDNNPs.

### High-dimensional neural network spin prediction
HDNNS$^{50}$ can be used to obtain the absolute magnitude of the atomic spins $|M_{S}|$ as a function of the geometrical structure. From the absolute atomic spins, the oxidation and spin states can be derived. HDNNSs use the same atomic neural network topology as employed in HDNNPs. However, instead of atomic energy contributions, the absolute atomic spins are predicted, which can be directly obtained by the atomic neural networks without taking the sum in Eq. (5).

### Simulation analysis
Employing $NpT$ MD simulations, the heat capacity at constant pressure $C_{p}$ can be obtained from the fluctuations of the total energy,
$$\frac{C_{p}}{k_{\mathrm{B}} N_{\mathrm{A}}}=\frac{N_{\text {atoms }}}{k_{\mathrm{B}}^{2} T^{2} N_{\text {steps }}} \sum_{n=0}^{N_{\text {steps }}}\left[E_{\text {tot }}(n)-\bar{E}_{\text {tot }}\right]^{2}, \tag{20}$$
with $N_{\text{atoms}}$ atoms in the simulation cell, the mean simulation temperature $T$, the total energy per atom $E_{\text{tot}}(n)$ as a function of the MD time step $n$ for the total number of simulation steps $N_{\text{steps}}$, and the mean total energy per atom during the simulation $\bar{E}_{\text{tot}}$. $k_{\mathrm{B}}$ is the Boltzmann constant and $N_{\mathrm{A}}$ is the Avogadro constant.

From MC spin-flip simulations, the influence of the magnetic degrees of freedom on the heat capacity at constant volume $C_{V}$ can be calculated,
$$\frac{C_{V}}{k_{\mathrm{B}} N_{\mathrm{A}}}=3+\frac{N_{\text {atoms }}}{k_{\mathrm{B}}^{2} T^{2} N_{\text {steps }}} \sum_{n=0}^{N_{\text {steps }}}[E(n)-\bar{E}]^{2}. \tag{21}$$

The contribution of the atomic motions to $C_{V}$ is taken into account by $3k_{\text{B}}N_{\text{A}}$, as the atomic motions are not considered in the conventional MC spin-flip simulations. The energy fluctuation is calculated from the potential energies per atom $E(n)$ as a function of the MC step $n$ for the total number of steps $N_{\text{steps}}$ compared to the mean potential energy per atom $\bar{E}$.

The order parameter $C$ is defined as
$$C=\frac{1}{N_{\text {steps }}} \sum_{n=0}^{N_{\text {steps }}} \max \left[\left|\frac{\mathbf{s}_{(111)} \cdot \mathbf{s}(n)}{\left|\mathbf{s}_{(111)}\right| \cdot|\mathbf{s}(n)|}\right|,\left|\frac{\mathbf{s}_{(\overline{1} 11)} \cdot \mathbf{s}(n)}{\left|\mathbf{s}_{(\overline{1} 11)}\right| \cdot|\mathbf{s}(n)|}\right|,\left|\frac{\mathbf{s}_{(1 \overline{1} 1)} \cdot \mathbf{s}(n)}{\left|\mathbf{s}_{(1 \overline{1} 1)}\right| \cdot|\mathbf{s}(n)|}\right|,\left|\frac{\mathbf{s}_{(11 \overline{1})} \cdot \mathbf{s}(n)}{\left|\mathbf{s}_{(11 \overline{1})}\right| \cdot|\mathbf{s}(n)|}\right|\right], \tag{22}$$
with $\boldsymbol{s}$ being the vector of the atomic spin coordinates $s_{i}$ of each atom $i$ in the simulation cell,
$$\mathbf{s}=\left(s_{1}, \ldots, s_{N_{\text {atoms }}}\right)^{\top}. \tag{23}$$

The atomic spin coordinates are equal to the sign of the atomic spins as defined in Eq. (9). The vector $\boldsymbol{s}$ at step $n$ is compared with the vectors $\mathbf{s}_{(111)}$, $\mathbf{s}_{(\overline{1}11)}$, $\mathbf{s}_{(1\overline{1}1)}$, and $\mathbf{s}_{(11\overline{1})}$, which are the possible AFM-II configurations in different spatial orientations. For normalization both vectors are divided by their lengths. The maximum agreements of the relative magnetic configurations at each step are averaged over the simulation length, i.e., the most similar of the four AFM-II spatial orientations is used.

### Computational details
The collinear spin-polarized DFT reference calculations were performed employing the Fritz-Haber-Institute ab initio molecular simulations (FHI-aims) code (version 200112.2)$^{85,86}$. The screened hybrid exchange-correlation functional HSE06 ($\omega=0.11\ a_0$)$^{64-66}$ and the "intermediate" FHI-aims basis set of numeric atom-centered functions excluding the auxiliary 5g hydrogenic functions were employed. A $\boldsymbol{\Gamma}$-centered $\boldsymbol{k}$-point grid of $2 \times 2 \times 2$ was applied to calculate the $2 \times 2 \times 2$ supercells of MnO (64 atoms without vacancies). The convergence criterion for the self-consistency cycle was set to $10^{-6}\ \text{eV}$ for the total energies and $10^{-4}\ \text{eV}\ \mathring{\text{A}}^{-1}$ for the forces. Hirshfeld spin moments$^{87}$ were used to determine the atomic spin coordinates. Further details are given in the Supplementary Tables 2 and 3. An extensive benchmark for MnO employing hybrid DFT functionals can be found in our previous work$^{88}$.

The sACSFs were implemented in a modified version of the RuNNer code version 1.00$^{11,12,89}$ to construct the mHDNNP and HDNNS. A cutoff radius of $R_{\mathrm{c}}=10.5\ a_0$ was used. A list of the employed parameters of the $n_{G}^{m}$ sACSFs for each element $m$ in the mHDNNP is given in Tables 2 and 3. The atomic feed-forward neural networks of mHDNNP and HDNNS consist of $n_{G}^{m}$ input neurons, three hidden layers with 20, 15, and 10 neurons, respectively, and one output neuron. The mHDNNP was trained using the cohesive energies, i.e., the total energy minus the sum of the free atom energies, and using atomic force components obtained from DFT calculations of reference structures in different magnetic states. The HDNNS was trained on the absolute values of the Hirshfeld spin moments of the same reference structures. Ninety percent of these data were used for training the neural networks. The remaining data were used as test set. Further details about the training can be found in the Supplementary Tables 4 and $5^{50,69}$.

mHDNNP-driven MD simulations in combination with MC spin flips were carried out using the Large-scale Atomic/Molecular Massively Parallel Simulator$^{90,91}$ and the neural network potential package (n2p2)$^{92}$ as library for potentials generated with RuNNer. The n2p2 code was modified to enable the usage of sACSFs. The MD simulations with MC spin flips (MDMC) employed $6 \times 6 \times 6$ $\text{Mn}_{x}\text{O}$ supercells referring to the geometric unit cell, with $x=0.969, 0.991, 0.999, 1$, i.e., 1701, 1720, 1727, and 1728 atoms. They were run in the $NpT$ ensemble at a pressure of $p=1$ bar with a time step of 1 fs applying the Nosé-Hoover thermostat and barostat with coupling constants of 0.1 and 1 ps, respectively$^{93,94}$. MC spin flips were performed after each time step. The spin-flip rate is not set to measured or calculated rates to study dynamic properties but to sample the thermodynamic equilibrium efficiently. In all MDMC simulations, the

<table>
<caption>Table 2. Employed radial sACSFs.</caption>
<thead>
  <tr>
    <th>i-j</th>
    <th>$M^{\kappa}$</th>
    <th>$\eta\left[a_{0}^{-2}\right]$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>O-O</td>
    <td>$M^{0}$</td>
    <td>0, 0.00117, 0.00246, 0.00389, 0.00550</td>
  </tr>
  <tr>
    <td>O-Mn</td>
    <td>$M^{0}$</td>
    <td>0, 0.00369, 0.00882, 0.01636, 0.02809</td>
  </tr>
  <tr>
    <td>Mn-O</td>
    <td>$M^{0}$</td>
    <td>0, 0.00369, 0.00882, 0.01636, 0.02809</td>
  </tr>
  <tr>
    <td>Mn-Mn</td>
    <td>$M^{+}, M^{-}$</td>
    <td>0, 0.00085, 0.00176, 0.00274, 0.00381</td>
  </tr>
  <tr>
    <td colspan="3">All combinations of SAFs and symmetry function parameters are applied for the given element pairs using $R_{\mathrm{c}}=10.5\ a_0$.</td>
  </tr>
</tbody>
</table>

<table>
<caption>Table 3. Employed angular sACSFs.</caption>
<thead>
  <tr>
    <th>i-j-k</th>
    <th>$M^{xx}$</th>
    <th>$\lambda$</th>
    <th>$\zeta$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>O-O-O</td>
    <td>$M^{00}$</td>
    <td>$-1,1$</td>
    <td>$1,2,4,16$</td>
  </tr>
  <tr>
    <td>O-O-Mn</td>
    <td>$M^{00}$</td>
    <td>$-1,1$</td>
    <td>$1,2,4,16$</td>
  </tr>
  <tr>
    <td>O-Mn-Mn</td>
    <td>$M^{00}$</td>
    <td>$-1,1$</td>
    <td>$1,2,4,16$</td>
  </tr>
  <tr>
    <td>Mn-O-O</td>
    <td>$M^{00}$</td>
    <td>$-1,1$</td>
    <td>$1,2,4,16$</td>
  </tr>
  <tr>
    <td>Mn-O-Mn</td>
    <td>$M^{++},M^{-}$</td>
    <td>$-1,1$</td>
    <td>$1,2,4,16$</td>
  </tr>
  <tr>
    <td>Mn-Mn-Mn</td>
    <td>$M^{++},M^{-},M^{+-}$</td>
    <td>$-1,1$</td>
    <td>$1,2,4,16$</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="4">All combinations of SAFs and symmetry function parameters are applied for the given element combinations using $\eta=0a_0^{-2}$ and $R_c=10.5a_0$.</td>
  </tr>
</tfoot>
</table>

system was equilibrated for 1 ns before the acquisition period of 10 ns. In all conventional MC spin-flip simulations, i.e., no MD steps in between the MC spin flips, the equilibration was performed for $10^6$ steps and the acquisition consisted of $10^7$ steps.

## DATA AVAILABILITY
The data sets generated and analyzed during the current study are available from the corresponding author on reasonable request.

## CODE AVAILABILITY
The modified versions of RuNNer and n2p2 to enable the usage of sACSFs are available from the corresponding author on reasonable request. The modifications will be implemented in coming release versions under the GPL3 license.

Received: 29 April 2021; Accepted: 7 September 2021;
Published online: 15 October 2021

## REFERENCES
1. Behler, J. Perspective: machine learning potentials for atomistic simulations. J. Chem. Phys. 145, 170901 (2016).
2. Bartók, A. P. et al. Machine learning unifies the modeling of materials and molecules. Sci. Adv. 3, e1701816 (2017).
3. Noé, F., Tkatchenko, A., Müller, K.-R. & Clementi, C. Machine learning for molecular simulation. Annu. Rev. Phys. Chem. 71, 361–390 (2020).
4. Ko, T. W., Finkler, J. A., Goedecker, S. & Behler, J. General-purpose machine learning potentials capturing nonlocal charge transfer. Acc. Chem. Res. 54, 808–817 (2021).
5. Behler, J. Four generations of high-dimensional neural network potentials. Chem. Rev. 121, 10037–10072 (2021).
6. Blank, T. B., Brown, S. D., Calhoun, A. W. & Doren, D. J. Neural network models of potential energy surfaces. J. Chem. Phys. 103, 4129–4137 (1995).
7. Handley, C. M. & Popelier, P. L. A. Potential energy surfaces fitted by artificial neural networks. J. Phys. Chem. A 114, 3371–3383 (2010).
8. Behler, J. Neural network potential-energy surfaces in chemistry: a tool for large-scale simulations. Phys. Chem. Chem. Phys. 13, 17930–17955 (2011).
9. Behler, J. & Parrinello, M. Generalized neural-network representation of high-dimensional potential-energy surfaces. Phys. Rev. Lett. 98, 146401 (2007).
10. Behler, J. Representing potential energy surfaces by high-dimensional neural network potentials. J. Phys. Condens. Matter 26, 183001 (2014).
11. Behler, J. Constructing high-dimensional neural network potentials: a tutorial review. Int. J. Quantum Chem. 115, 1032–1050 (2015).
12. Behler, J. First principles neural network potentials for reactive simulations of large molecular and condensed systems. Angew. Chem. Int. Ed. 56, 12828–12840 (2017).
13. Smith, J. S., Isayev, O. & Roitberg, A. E. ANI-1: an extensible neural network potential with DFT accuracy at force field computational cost. Chem. Sci. 8, 3192–3203 (2017).
14. Bartók, A. P., Payne, M. C., Kondor, R. & Csányi, G. Gaussian approximation potentials: the accuracy of quantum mechanics, without the electrons. Phys. Rev. Lett. 104, 136403 (2010).
15. Shapeev, A. V. Moment tensor potentials: a class of systematically improvable interatomic potentials. Multiscale Model. Simul. 14, 1153–1173 (2016).
16. Balabin, R. M. & Lomakina, E. I. Support vector machine regression (LS-SVM)—an alternative to artificial neural networks (ANNs) for the analysis of quantum chemistry data? Phys. Chem. Chem. Phys. 13, 11710–11718 (2011).
17. Thompson, A. P., Swiler, L. P., Trott, C. R., Foiles, S. M. & Tucker, G. J. Spectral neighbor analysis method for automated generation of quantum-accurate interatomic potentials. J. Comp. Phys. 285, 316–330 (2015).
18. Drautz, R. Atomic cluster expansion for accurate and transferable interatomic potentials. Phys. Rev. B 99, 014104 (2019).
19. Deng, Z., Chen, C., Li, X.-G. & Ong, S. P. An electrostatic spectral neighbor analysis potential for lithium nitride. npj Comput. Mater. 5, 75 (2019).
20. Artrith, N., Morawietz, T. & Behler, J. High-dimensional neural-network potentials for multicomponent systems: applications to zinc oxide. Phys. Rev. B 83, 153101 (2011).
21. Morawietz, T., Sharma, V. & Behler, J. A neural network potential-energy surface for the water dimer based on environment-dependent atomic energies and charges. J. Chem. Phys. 136, 064103 (2012).
22. Yao, K., Herr, J. E., Toth, D. W., Mckintyre, R. & Parkhill, J. The TensorMol-0.1 model chemistry: a neural network augmented with long-range physics. Chem. Sci. 9, 2261–2269 (2018).
23. Ghasemi, S. A., Hofstetter, A., Saha, S. & Goedecker, S. Interatomic potentials for ionic systems with density functional accuracy based on charge densities obtained by a neural network. Phys. Rev. B 92, 045131 (2015).
24. Xie, X., Persson, K. A. & Small, D. W. Incorporating electronic information into machine learning potential energy surfaces via approaching the ground-state electronic energy as a function of atom-based electronic populations. J. Chem. Theory Comput. 16, 4256–4270 (2020).
25. Ko, T. W., Finkler, J. A., Goedecker, S. & Behler, J. A fourth-generation high-dimensional neural network potential with accurate electrostatics including non-local charge transfer. Nat. Commun. 12, 398 (2021).
26. Behler, J., Reuter, K. & Scheffler, M. Nonadiabatic effects in the dissociation of oxygen molecules at the Al(111) surface. Phys. Rev. B 77, 115421 (2008).
27. Dral, P. O., Barbatti, M. & Thiel, W. Nonadiabatic excited-state dynamics with machine learning. J. Phys. Chem. Lett. 9, 5660–5663 (2018).
28. Chen, W.-K., Liu, X.-Y., Fang, W.-H., Dral, P. O. & Cui, G. Deep learning for non-adiabatic excited-state dynamics. J. Phys. Chem. Lett. 9, 6702–6708 (2018).
29. Hu, D., Xie, Y., Li, X., Li, L. & Lan, Z. Inclusion of machine learning kernel ridge regression potential energy surfaces in on-the-fly nonadiabatic molecular dynamics simulation. J. Phys. Chem. Lett. 9, 2725–2732 (2018).
30. Wang, Y., Xie, C., Guo, H. & Yarkony, D. R. A quasi-diabatic representation of the 1,2¹A states of methylamine. J. Phys. Chem. A 123, 5231–5241 (2019).
31. Williams, D. M. G. & Eisfeld, W. Neural network diabatization: a new ansatz for accurate high-dimensional coupled potential energy surfaces. J. Chem. Phys. 149, 204106 (2018).
32. Westermayr, J. et al. Machine learning enables long time scale molecular photodynamics simulations. Chem. Sci. 10, 8100–8107 (2019).
33. Westermayr, J., Faber, F. A., Christensen, A. S., von Lilienfeld, O. A. & Marquetand, P. Neural networks and kernel ridge regression for excited states dynamics of $CH_2NH_2^{+\cdot}$: from single-state to multi-state representations and multi-property machinelearning models.Mach. Learn. Sci. Technol. 1, 025009 (2020).
34. Westermayr, J., Gastegger, M. & Marquetand, P. Combining SchNet and SHARC: the SchNarc machine learning approach for excited-state dynamics. J. Phys. Chem. Lett. 11, 3828–3834 (2020).
35. Novikov, I., Grabowski, B., Körmann, F. & Shapeev, A. Machine-learning interatomic potentials reproduce vibrational and magnetic degrees of freedom. Preprint at https://arxiv.org/abs/2012.12763 (2020).
36. Sanvito, S. et al. Machine Learning and High-Throughput Approaches to Magnetism 1–23 (Springer, 2018).
37. Greenwald, S. & Smart, J. S. Deformations in the crystal structures of anti-ferromagnetic compounds. Nature 166, 523–524 (1950).
38. Ising, E. Beitrag zur Theorie des Ferromagnetismus. Z. Phys. 31, 253–258 (1925).
39. Heisenberg, W. Zur Theorie des Ferromagnetismus. Z. Phys. 49, 619–636 (1928).
40. Hubbard, J. Electron correlations in narrow energy bands. Proc. R. Soc. Lond. A 276, 238–257 (1963).
41. Dudarev, S. L. & Derlet, P. M. A ‘magnetic’ interatomic potential for molecular dynamics simulations. J. Phys. Condens. Matter 17, 7097–7118 (2005).
42. Yin, J., Eisenbach, M., Nicholson, D. M. & Rusanu, A. Effect of lattice vibrations on magnetic phase transition in bcc iron. Phys. Rev. B 86, 214423 (2012).
43. Ma, P.-W., Dudarev, S. L. & Wróbel, J. S. Dynamic simulation of structural phase transitions in magnetic iron. Phys. Rev. B 96, 094418 (2017).
44. Sanvito, S. et al. Accelerated discovery of new magnets in the Heusler alloy family. Sci. Adv. 3, e1602241 (2017).
45. Nelson, J. & Sanvito, S. Predicting the Curie temperature of ferromagnets using machine learning. Phys. Rev. Mater. 3, 104405 (2019).
46. Nguyen, D.-N. et al. A regression-based model evaluation of the Curie temperature of transition-metal rare-earth compounds. J. Phys. Conf. Ser. 1290, 012009 (2019).

Published in partnership with the Shanghai Institute of Ceramics of the Chinese Academy of Sciences
npj Computational Materials (2021) 170

47. Long, T., Fortunato, N. M., Zhang, Y., Gutfleisch, O. & Zhang, H. An accelerating approach of designing ferromagnetic materials via machine learning modeling of magnetic ground state and Curie temperature. *Mater. Res. Lett.* **9**, 169–174 (2021).

48. Janet, J. P. & Kulik, H. J. Predicting electronic structure properties of transition metal complexes with neural networks. *Chem. Sci.* **8**, 5137–5152 (2017).

49. Janet, J. P., Chan, L. & Kulik, H. J. Accelerating chemical discovery with machine learning: Simulated evolution of spin crossover complexes with an artificial neural network. *J. Phys. Chem. Lett.* **9**, 1064–1071 (2018).

50. Eckhoff, M., Lausch, K. N., Blöchl, P. E. & Behler, J. Predicting oxidation and spin states by high-dimensional neural networks: applications to lithium manganese oxide spinels. *J. Chem. Phys.* **153**, 164107 (2020).

51. Zubatiuk, T. & Isayev, O. Development of multimodal machine learning potentials: Toward a physics-aware artificial intelligence. *Acc. Chem. Res.* **54**, 1575–1585 (2021).

52. Behler, J. Atom-centered symmetry functions for constructing high-dimensional neural network potentials. *J. Chem. Phys.* **134**, 074106 (2011).

53. Bartók, A. P., Kondor, R. & Csányi, G. On representing chemical environments. *Phys. Rev. B* **87**, 184115 (2013).

54. Langer, M. F., Goessmann, A. & Rupp, M. Representations of molecules and materials for interpolation of quantum-mechanical simulations via machine learning. Preprint at https://arxiv.org/abs/2003.12081 (2020).

55. Shull, C. G. & Smart, J. S. Detection of antiferromagnetism by neutron diffraction. *Phys. Rev.* **76**, 1256–1257 (1949).

56. Shull, C. G., Strauser, W. A. & Wollan, E. O. Neutron diffraction by paramagnetic and antiferromagnetic substances. *Phys. Rev.* **83**, 333–345 (1951).

57. Bizette, H., Squire, C. & Tsai, B. The λ transition point of the magnetic susceptibility in the manganosite MnO. *Comptes Rendus Acad. Sci.* **207**, 449 (1938).

58. Siegwarth, J. D. Mössbauer effect of divalent Fe⁵⁷ in NiO and MnO. *Phys. Rev.* **155**, 285–296 (1967).

59. Shaked, H., Faber Jr., J. & Hitterman, R. L. Low-temperature magnetic structure of MnO: A high-resolution neutron-diffraction study. *Phys. Rev. B* **38**, 11901–11903 (1988).

60. Perdew, J. P., Ernzerhof, M. & Burke, K. Rationale for mixing exact exchange with density functional approximations. *J. Chem. Phys.* **105**, 9982–9985 (1996).

61. Adamo, C. & Barone, V. Toward reliable density functional methods without adjustable parameters: the PBE0 model. *J. Chem. Phys.* **110**, 6158–6170 (1999).

62. Franchini, C., Bayer, V., Podloucký, R., Paier, J. & Kresse, G. Density functional theory study of MnO by a hybrid functional approach. *Phys. Rev. B* **72**, 045132 (2005).

63. Schrön, A., Rödl, C. & Bechstedt, F. Crystalline and magnetic anisotropy of the 3d-transition metal monoxides MnO, FeO, CoO, and NiO. *Phys. Rev. B* **86**, 115134 (2012).

64. Heyd, J., Scuseria, G. E. & Ernzerhof, M. Hybrid functionals based on a screened Coulomb potential. *J. Chem. Phys.* **118**, 8207–8215 (2003).

65. Heyd, J., Scuseria, G. E. & Ernzerhof, M. Erratum: "Hybrid functionals based on a screened Coulomb potential" [J. Chem. Phys. 118, 8207 (2003)]. *J. Chem. Phys.* **124**, 219906 (2006).

66. Krukau, A. V., Vydrov, O. A., Izmaylov, A. F. & Scuseria, G. E. Influence of the exchange screening parameter on the performance of screened hybrid functionals. *J. Chem. Phys.* **125**, 224106 (2006).

67. Artrith, N. & Behler, J. High-dimensional neural network potentials for metal surfaces: a prototype study for copper. *Phys. Rev. B* **85**, 045439 (2012).

68. Eckhoff, M. & Behler, J. From molecular fragments to the bulk: development of a neural network potential for MOF-5. *J. Chem. Theory Comput.* **15**, 3793–3809 (2019).

69. Eckhoff, M. et al. Closing the gap between theory and experiment for lithium manganese oxide spinels using a high-dimensional neural network potential. *Phys. Rev. B* **102**, 174102 (2020).

70. Wales, D. J. & Doye, J. P. K. Global optimization by basin-hopping and the lowest energy structures of Lennard-Jones clusters containing up to 110 atoms. *J. Phys. Chem. A* **101**, 5111–5116 (1997).

71. Ashcroft, N. W. & Mermin, N. D. *Solid State Physics* (Saunders College Publishing, New York, 1976).

72. Schrön, A., Rödl, C. & Bechstedt, F. Energetic stability and magnetic properties of MnO in the rocksalt, wurtzite, and zinc-blende structures: influence of exchange and correlation. *Phys. Rev. B* **82**, 165109 (2010).

73. Pepy, G. Spin waves in MnO; from 4°k to temperatures close to T_N. *J. Phys. Chem. Solids* **35**, 433–444 (1974).

74. Kohgi, M., Ishikawa, Y. & Endoh, Y. Inelastic neutron scattering study of spin waves in MnO. *Solid State Commun.* **11**, 391–394 (1972).

75. Murnaghan, F. D. Finite deformations of an elastic solid. *Am. J. Math.* **59**, 235–260 (1937).

76. Birch, F. Finite elastic strain of cubic crystals. *Phys. Rev.* **71**, 809–824 (1947).

77. Morosin, B. Exchange striction effects in MnO and MnS. *Phys. Rev. B* **1**, 236–243 (1970).

78. Seino, D., Miyahara, S. & Noro, Y. The magnetic susceptibility of MnO associated with the first-order phase transition. *Phys. Lett. A* **44**, 35–36 (1973).

79. Miyahara, S. & Seino, D. First order magnetic phase transition in MnO. *Phys. B* **86-88**, 1128–1129 (1977).

80. Suzuki, I., Okajima, S.-I. & Seya, K. Thermal expansion of single-crystal manganosite. *J. Phys. Earth* **27**, 63–69 (1979).

81. Jung, S. W. et al. Ferromagnetic properties of Zn₁₋ₓMnₓO epitaxial thin films. *Appl. Phys. Lett.* **80**, 4561–4563 (2002).

82. Lee, Y.-C., Pakhomov, A. B. & Krishnan, K. M. Size-driven magnetic transitions in monodisperse MnO nanocrystals. *J. Appl. Phys.* **107**, 09E124 (2010).

83. Sun, X. et al. Magnetic properties and spin structure of MnO single crystal and powder. *J. Phys. Conf. Ser.* **862**, 012027 (2017).

84. Berkowitz, A. E. et al. Antiferromagnetic MnO nanoparticles with ferrimagnetic Mn₃O₄ shells: doubly inverted core-shell system. *Phys. Rev. B* **77**, 024403 (2008).

85. Blum, V. et al. Ab initio molecular simulations with numeric atom-centered orbitals. *Comput. Phys. Commun.* **180**, 2175–2196 (2009).

86. FHI-aims. *Fritz-Haber-Institute Ab Initio Molecular Simulations Package*, https://aimsclub.fhi-berlin.mpg.de (2020).

87. Hirshfeld, F. L. Bonded-atom fragments for describing molecular charge densities. *Theor. Chim. Acta* **44**, 129–138 (1977).

88. Eckhoff, M., Blöchl, P. E. & Behler, J. Hybrid density functional theory benchmark study on lithium manganese oxides. *Phys. Rev. B* **101**, 205113 (2020).

89. Behler, J. *RuNNer*, http://gitlab.com/TheochemGoettingen/RuNNer (2019).

90. Plimpton, S. Fast parallel algorithms for short-range molecular dynamics. *J. Comput. Phys.* **117**, 1–19 (1995).

91. LAMMPS. *Large-scale Atomic/Molecular Massively Parallel Simulator*, http://lammps.sandia.gov (2019).

92. Singraber, A. *n2p2 – A Neural Network Potential Package*, https://github.com/CompPhysVienna/n2p2 (2019).

93. Nosé, S. A molecular dynamics method for simulations in the canonical ensemble. *Mol. Phys.* **52**, 255–268 (1984).

94. Hoover, W. G. Canonical dynamics: equilibrium phase-space distributions. *Phys. Rev. A* **31**, 1695–1697 (1985).

95. Stukowski, A. Visualization and analysis of atomistic simulation data with OVITO – the open visualization tool. *Model. Simul. Mater. Sci. Eng.* **18**, 015012 (2010).

## ACKNOWLEDGEMENTS
This project was funded by the Deutsche Forschungsgemeinschaft (DFG) - project number 217133147/SFB 1073, project C03. We gratefully acknowledge computing time provided by the Paderborn Center for Parallel Computing (PC²) and by the DFG (INST186/1294-1 FUGG, project number 405832858).

## AUTHOR CONTRIBUTIONS
M.E. conceived the sACSF approach and initiated the project. M.E. worked out and implemented the practical algorithms and performed all calculations. M.E. and J.B. contributed ideas to the project and analyzed the results. M.E. wrote the initial version of the manuscript and prepared the figures. M.E. and J.B. jointly edited the manuscript.

## FUNDING
Open Access funding enabled and organized by Projekt DEAL.

## COMPETING INTERESTS
The authors declare no competing interests.

## ADDITIONAL INFORMATION
Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41524-021-00636-z.

Correspondence and requests for materials should be addressed to Marco Eckhoff or Jörg Behler.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/811642506805510145_10.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2021

Published in partnership with the Shanghai Institute of Ceramics of the Chinese Academy of Sciences
npj Computational Materials (2021) 170