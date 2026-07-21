ORIGINAL RESEARCH ARTICLE

# Electronic, Magnetic, and Magnetocaloric Properties of $\mathbf{NdMnO_3}$ Simple Perovskite

H. MAGOUSSI, $^{1,2}$ S. AMRAOUI, $^{1,3}$ A. FERAOUN, $^{1,4}$ and M. KEROUAD $^{1,5}$

1.—Laboratoire Physique des Matériaux et Modélisation des Systèmes (LP2MS), Unité Associée au CNRST-URAC: 08, Faculty of Sciences, University of Moulay Ismail, B.P. 11201, Zitoune, Meknes, Morocco. 2.—e-mail: houdamagoussi2@gmail.com. 3.—e-mail: contactamraoui@gmail.com. 4.—e-mail: ab.feraoun@gmail.com. 5.—e-mail: mkerou@yahoo.fr

Using density functional theory calculations within the generalized gradient approximation, the electronic density of states and band structure of $NdMnO_3$ simple perovskite are analyzed. It is found that the compound behaves as a ferromagnetic half-metal material. By using Monte Carlo simulations within the framework of the Ising model, the effects of the crystal field and the exchange interaction between the magnetic atoms Mn–Mn and Nd–Mn on the magnetization, susceptibility, specific heat, and internal energy are investigated. The magnetocaloric effect of $NdMnO_3$ is also examined. It is observed that the relative cooling power (RCP) increases when the applied magnetic field or Mn–Mn exchange interaction is increased, whereas the RCP decreases when the crystal field or Nd–Mn exchange interaction is increased. These results show that $NdMnO_3$ is a potential candidate for use in magnetic refrigeration and spintronic applications.

**Key words:** $NdMnO_3$ perovskite, ab initio, Monte Carlo simulation, Ising model, magnetocaloric effects

---

## INTRODUCTION

Perovskites have attracted attention because of their spin polarization at the Fermi level. Their half-metallic ferromagnetic behavior with a significant magnetic moment contributes to the development of the semiconductor technology. $^{1,2}$ These compounds are encouraging for use in several applications, in particular in spintronic devices $^{3,4}$ and for microwave and high-power applications. $^{5,6}$ The main applications of perovskites are in magnetic disk drives, magnetic memories, $^{7,8}$ magnetic hybrid technology, magnetic tunnel junctions, spin injection devices, nonvolatile magnetic random-access memories (MRAM), magnetic sensors, microelectronics, and telecommunications. $^{9,10}$ Researchers have found that perovskites can generate laser light. $^{11}$ Perovskites are also used as photocatalysts. $^{12,13}$

Generally, simple perovskite compounds have the formula $ABO_3$, where $A$ denotes a low-charge cation such as rare- or alkaline-earth metals or alkali metals, while $B$ is a small cation, usually a transition metal. $^{14}$ The crystal structure of most $RMnO_3$ compounds (where $R$ is rare earth: $R=$ La, Nd, Pr) is orthorhombic with $Pnma$ symmetry. $^{15}$ Rare-earth manganites with perovskite-type structure have been studied because of their potential applications as catalytic, electrical, and magnetic materials, hence their characteristics in terms of physical or chemical properties have been widely studied. $^{16}$ Neodymium-based $NdMnO_3$ (NMO) material is a member of the perovskite family that shows a variety of interesting properties such as negative magnetization, $^{17}$ reorientation of Mn ions in the NMO matrix, $^{18}$ magnetic anisotropy, $^{19}$ etc. The dielectric behavior of $NdMnO_3$ manganite thin films grown on (100) single-crystalline $(LaAlO_3)_{0.3}$ $(Sr_2AlTaO_6)_{0.7}$ substrate by pulsed laser deposition has also been reported. $^{20}$ The phase formation and particle size of neodymium manganate ($NdMnO_3$) have been determined by x-ray diffraction analysis

(Received September 14, 2020; accepted November 16, 2020; published online January 3, 2021)

and transmission electron microscopy. $^{21}$ The effect of Zn doping on the structural and magnetic prop- erties of $NdMnO_{3}$ has been investigated by neutron diffraction and direct-current (DC) magnetic sus- ceptibility measurements. $^{22}$ Neodymium man ganate $(NdMnO_{3})$ nanoparticles have been synthesized by the sol-gel process. Using x-ray diffraction (XRD) analysis and energy dispersive x- ray spectroscopy (EDS) techniques, Jacob et al. examined the phase diagram of the NdMnO system and the thermodynamic properties of $NdMnO_{2}$ and $NdMnO_{3} \cdot^{23}$ Theoretically, a short-range force con stant model was applied for the first time to investigate phonons in $NdMnO_{3}$ perovskite in orthorhombic phase. $^{24}$ Using the full potential linear augmented plane-wave (FPLAPW) method based on density functional theory (DFT), Bouad- jemi et al. studied the structural, electronic, optical, and magnetic properties of the orthorhombic NdMnO3 oxide perovskite, using both the general- ized gradient approximation (GGA) and (GGA + U) approaches, $^{25}$ where the basic role of the U correc tion is to treat the strong on-site Coulomb interac- tion of localized electrons with an additional Hubbard-like term. Masrour et al. investigated the magnetocaloric effect in $NdMnO_{3}$ perovskite by using Monte Carlo simulations. $^{26}$ The magneticproperties and magnetocaloric effect in $NdMnO_{3}$  have been investigated using a classical Heisenberg Hamiltonian with nearest- and next-nearest-neigh- bor interactions. The Hamiltonian parameters were fit to reproduce experimental results. $^{27}$ GThe elec tronic and magnetic properties of double perovskite have been studied by using ab initio and Monte Carlo methods. $^{28,29}$ To the best of the authors' knowledge, all research work carried out on the NdMnO3 system has treated it as a ferromagnetic system. $^{26}$ However, in this work, based on DFT calculations, it is found that the manganese atoms are antiferromagnetically coupled. Using ab initio calculations and Monte Carlo simulations, the elec- tronic (band structure, density of states, and mag- netic moment) and magnetic properties(magnetization, susceptibility, energy, and specificheat) and the magnetocaloric effect of $NdMnO_{3}$  perovskite are studied. The remainder of this manuscript is organized as follows: section "Ab Ini- tio Calculations" provides details regarding the ab initio calculations. Section Monte Carlo Simula- tions is devoted to the Monte Carlo study. Finally, the paper is summarized in section "Conclusions".

## AB INITIO CALCULATIONS

### Computational Details

The calculations are based on density functional theory (DFT) with the full potential linearized augmented plane wave (FPLAPW) method to studythe electronic and magnetic properties of $NdMnO_{3}$  simple perovskite. The generalized gradient approx- imation (GGA) is employed to treat the exchange- correlation potential. A cutoff of 6.0 is specified via the product $R_{MT} \cdot K_{MAX}$ , where $R_{MT}$ is the smallest muffin-tin sphere radius and $K_{MAX}$ is the magnitude of the largest wavevector. To avoid overlap, the atomic muffin-tin spheres are taken as 2.40 atomic units (a.u.), 1.93 a.u., and 1.66 a.u. for Nd, Mn, and O, respectively. About $500 k$ -points in the irre ducible Brillouin zone are used for self-consistent convergence.

## Crystal Structure

The studied $NdMnO_{3}$ simple perovskite adopts anorthorhombic structure $(a \neq b \neq c$  and α = β = γ = 90°) in space group Pnma (no. 62). The structure contains $MnO_{6}$ octahedrons, in which Mn cations are surrounded by six oxygen anions, with neodymium cations filling interstitial spaces between the $MnO_{6}$ octahedrons, as shown in Fig. 1. To optimize the cell parameters, the energy as a function of the unit cell volume is investigated, by setting the directions (up or down) of the Nd and Mn spins. The energies calculated for NMO with paramagnetic (PM), ferromagnetic (FM), and anti- ferromagnetic (AFM) order are presented in Table I, as done in Refs. $^{30-32}$ These results show that NMO(FM) has the lowest energy $(-88,117.1786$ Ry) with the GGA + U approach, thus the optimized unit cell parameters $a, b$ , and $c$ are $5.33 \AA, 5.62 \AA$ , and7.43 A, respectively. The atomic positions are also presented in Table II.

## Magnetic Ordering

The magnetic properties of $NdMnO_{3}$ simple perovskite are mainly governed by the exchange coupling betweenthe magnetic elements $Nd^{3+}$ with $spin \sigma=3 / 2$ and $Mn^{3+}$  with $spin S=2$ . Besides, the magnetic order of a simple perovskite is essentially due to the orientation of the spins in the system (the spin-up or spin-down polarization). The stable configuration is that which achieves the lowest energy. To determine this stable state of the simple perovskite oxide $NdMnO_{3}$ , the energy is calculated for the different configurations $(E_{Nd \uparrow Nd \uparrow Mn \uparrow Mn \uparrow}, E_{Nd \uparrow Nd \uparrow Mn \downarrow Mn \downarrow}$ , $E_{Nd \downarrow Nd \downarrow Mn \uparrow Mn \uparrow}, E_{Nd \downarrow Nd \downarrow Mn \downarrow Mn \downarrow}, E_{Nd \uparrow Nd \uparrow Mn \uparrow MN \downarrow}$ , and ENd Nd Mn MN ). It is found that the energy is minimal when the neodymium cations are ferromagnetically

![](./images/812519601978998785_1.jpg)

Fig. 1. Schematic of crystal structure of $NdMnO_{3}$ perovskite.

<table><caption>Table I. Calculated energy, lattice parameter, and volume of NdMnO₃ for different magnetic orders</caption>
<thead>
  <tr>
    <th></th>
    <th>Parameter</th>
    <th>NMO (PM)</th>
    <th>NMO (FM)</th>
    <th>NMO (AFM)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="5">GGA</td>
    <td>$E$ (Ry)</td>
    <td>−88,117.0353</td>
    <td>−88,117.1522</td>
    <td>−88,117.0950</td>
  </tr>
  <tr>
    <td>$a$ (Å)</td>
    <td>5.27</td>
    <td>5.39</td>
    <td>5.45</td>
  </tr>
  <tr>
    <td>$b$ (Å)</td>
    <td>5.73</td>
    <td>5.74</td>
    <td>5.86</td>
  </tr>
  <tr>
    <td>$c$ (Å)</td>
    <td>6.83</td>
    <td>7.44</td>
    <td>7.59</td>
  </tr>
  <tr>
    <td>$V$ (Å³)</td>
    <td>206.25</td>
    <td>230.18</td>
    <td>242.40</td>
  </tr>
  <tr>
    <td rowspan="5">GGA + U</td>
    <td>$E$ (Ry)</td>
    <td>−88,117.0952</td>
    <td>−88,117.1786</td>
    <td>−88,117.0951</td>
  </tr>
  <tr>
    <td>$a$ (Å)</td>
    <td>5.44</td>
    <td>5.33</td>
    <td>5.44</td>
  </tr>
  <tr>
    <td>$b$ (Å)</td>
    <td>5.86</td>
    <td>5.62</td>
    <td>5.86</td>
  </tr>
  <tr>
    <td>$c$ (Å)</td>
    <td>7.59</td>
    <td>7.43</td>
    <td>7.60</td>
  </tr>
  <tr>
    <td>$V$ (Å³)</td>
    <td>241.96</td>
    <td>222.56</td>
    <td>242.27</td>
  </tr>
</tbody>
</table>

<table><caption>Table II. Atomic positions in NdMnO₃ simple perovskite</caption>
<thead>
  <tr>
    <th>Atom</th>
    <th>$x$</th>
    <th>$y$</th>
    <th>$z$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Nd</td>
    <td>0.51</td>
    <td>0.42</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>Nd</td>
    <td>0.98</td>
    <td>0.92</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>Nd</td>
    <td>0.48</td>
    <td>0.57</td>
    <td>0.75</td>
  </tr>
  <tr>
    <td>Nd</td>
    <td>0.01</td>
    <td>0.07</td>
    <td>0.75</td>
  </tr>
  <tr>
    <td>Mn</td>
    <td>0</td>
    <td>0.50</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Mn</td>
    <td>0.50</td>
    <td>0</td>
    <td>0.50</td>
  </tr>
  <tr>
    <td>Mn</td>
    <td>0</td>
    <td>0.50</td>
    <td>0.50</td>
  </tr>
  <tr>
    <td>Mn</td>
    <td>0.50</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>O</td>
    <td>0.09</td>
    <td>0.52</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>O</td>
    <td>0.21</td>
    <td>0.81</td>
    <td>0.54</td>
  </tr>
  <tr>
    <td>O</td>
    <td>0.21</td>
    <td>0.81</td>
    <td>0.95</td>
  </tr>
  <tr>
    <td>O</td>
    <td>0.28</td>
    <td>0.31</td>
    <td>0.95</td>
  </tr>
  <tr>
    <td>O</td>
    <td>0.28</td>
    <td>0.31</td>
    <td>0.54</td>
  </tr>
</tbody>
</table>

<table><caption>Table III. Partial and total calculated magnetic moment of NdMnO₃</caption>
<thead>
  <tr>
    <th>Element</th>
    <th>Magnetic Moments ($\mu_\text{B}$)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\mu_\text{Nd}$</td>
    <td>3.01</td>
  </tr>
  <tr>
    <td>$\mu_\text{Mn}$</td>
    <td>−3.13; 3.13</td>
  </tr>
  <tr>
    <td>$\mu_\text{O}$</td>
    <td>−0.03</td>
  </tr>
  <tr>
    <td>$\mu_\text{Total}$</td>
    <td>11.91</td>
  </tr>
</tbody>
</table>

coupled while the manganese cations are antiferromagnetically coupled. In other words, the magnetic order of the manganese sublattice is antiferromagnetic while that of the neodymium sublattice is ferromagnetic. Therefore, the NdMnO₃ compound can be classified as a ferromagnetic material, since the system has a nonzero total moment. This result will be taken into consideration in the Monte Carlo study.

The total and partial magnetic moments per unit cell are presented in Table III. The magnetic moment of the different elements constituting NdMnO₃ simple perovskite in its stable configuration depend on the polarization of each element in the compound, thus the magnetic moment of manganese takes a negative or positive value in its down or up polarization. In addition, the oxygen magnetic moment shows a weak value because O $p$ orbitals are fully occupied, which can also be explained by its position located in the antiferromagnetic Mn(up)–O–Mn(down) interaction, while the distance between the oxygen and manganese atoms is also shorter than that between oxygen and neodymium.

### Electronic Properties
The spin-polarized band structure of NdMnO₃ simple perovskite calculated using the GGA is plotted along the high-symmetry points Y, Z, U, X, S, R, and T in the first Brillouin zone in Fig. 2. The Fermi level is set at 0 eV. From the spin-down band structure, it is found that NdMnO₃ exhibits semiconductor behavior with a direct bandgap of $E_\text{g}=2.49$ eV, where the valence-band maximum and conduction-band minimum are at about −1.91 eV and 0.58 eV, respectively. Meanwhile, according to the spin-up band structure, the simple perovskite behaves as a metallic oxide, because of the overlap of the valence and conduction band at the Fermi level. The presence of both metallic and semiconductor behavior indicates that NdMnO₃ simple perovskite is a half-metal oxide. To confirm these results obtained for the NdMnO₃ compound, the electronic density of states is computed.

The total and partial densities of states (PDOS) for NdMnO₃ simple perovskite are obtained by spin-polarized calculations in the GGA with the Fermi level set to 0 eV. From the total density of states in Fig. 3a, the spin-up polarization at the Fermi level shows metallic behavior. However, the spin-down density of states shows semiconductor nature with a bandgap of about $E_\text{g}=2.49$ eV. These results indicate half-metallic behavior of NdMnO₃ simple perovskite, confirming the results described above based on the band structure. On the other hand, the nonsymmetric total density of states indicates the magnetic behavior of the compound. These results immediately suggest the use of NdMnO₃ in spintronic device applications. The contribution of each ion in NdMnO₃ to the total density of states is

![](./images/812519601978998785_2.jpg)

Fig. 2. Spin-up (a) and spin-down (b) band structure of NdMnO₃ simple perovskite obtained from GGA calculations.

investigated in Fig. 3b. The PDOS of the neody-
mium and manganese cations are essentially
responsible for the magnetic behavior of NdMnO₃
oxide, given their nonsymmetric density of states.
The electronic density of states of the oxygen
element is not perfectly symmetrical, a result that
also indicates that it makes a very weak contribu-
tion to the magnetism of NdMnO₃ simple per-
ovskite. In Fig. 3c, note that the behavior of the
neodymium and manganese atoms near the Fermi
level is essentially governed by the Nd 4f and Mn 3d
orbitals. In addition, the $3d$-$t_{2g}$ and $3d$-$e_{g}$ orbitals of
the Mn $3d$ orbital are due to the effect of the
octahedral crystal field generated by the MnO₆
octahedra of oxygen anions surrounding each man-
ganese cation (Fig. 1). This crystal field is respon-
sible for splitting the five-degenerate $3d$ level into
triply degenerate $t_{2g}$) states ($d_{xz}, d_{yz}$, and $d_{xy})$) with
lower energy and doubly degenerate $e_{g}$ states
($d_{x^2 - y^2}$, and $d_{z^2}$) states with higher energy for both
spin up at 0 eV and 0.73 eV and spin down at 2.1 eV
and 2.83 eV.

## MONTE CARLO SIMULATIONS

### Model and Formalism

The studied NdMnO₃ simple perovskite is pre-
sented in Fig. 1. Nd³⁺ and Mn³⁺ are the magnetic
elements of the compound, described by a magnetic
spin moment of $\sigma = 3/2$ ($\pm 3/2, \pm 1/2$) and
$S = 2(\pm 2, \pm 1, 0)$, respectively. The Hamiltonian of
the Ising model is given by

$$
\begin{aligned}
H= & -\sum_{\langle m,n\rangle} J_{\mathrm{MnMn}} S_{m}^{z} S_{n}^{z}-\sum_{\langle i,j\rangle} J_{\mathrm{NdNd}} \sigma_{i}^{z} \sigma_{j}^{z} \\
& -\sum_{\langle i,m\rangle} J_{\mathrm{NdMn}} \sigma_{i}^{z} S_{m}^{z}-\sum_{i} D_{\mathrm{s}}\left(S_{i}^{2}\right) \\
& -\sum_{i} h\left(S_{i}^{z}+\sigma_{i}^{z}\right),
\end{aligned}
\tag{1}
$$

where $< i,j >$ stands for the first nearest-neighbor
sites $i$ and $j$. $J_{\mathrm{MnMn}}$ is the antiferromagnetic
exchange coupling between Mn and Mn
($J_{\mathrm{MnMn}}<0$), $J_{\mathrm{NdNd}}$ is the ferromagnetic exchange
coupling between Nd and Nd ($J_{\mathrm{NdNd}}>0$), and $J_{\mathrm{NdMn}}$
is the exchange interaction between Nd and Mn.
$J_{\mathrm{NdMn}}>0$ when Nd is coupled with Mn in up
direction $\uparrow$ (Mn⁺), and $J_{\mathrm{NdMn}}<0$ when Nd is coupled
with Mn in down direction $\downarrow$ (Mn⁻). $D_{\mathrm{s}}$ is the crystal
field, and $h$ is the external magnetic field.

Monte Carlo simulations are carried out, flipping
the spins one at a time according to the heat bath
algorithm.³³ Each data point is obtained for $10^{5}$
Monte Carlo steps after discarding the first $5 \times 10^{4}$
steps. To study the effect of the system size on the
results, simulations with different values of $L$ are
carried out. No significant differences were found

![](./images/812519601978998785_3.jpg)

Fig. 3. (a) Total density of states, (b) Nd, Mn, and O element density of states, and (c) Nd f, Mn d, and O p orbital density of states of NdMnO₃ obtained from GGA calculations.

after $L = 28$, hence the results are reported for a system size taken to be $L = 32$.

The total magnetization $M_T$ per site is given by
$$
M_{\mathrm{T}}=\frac{N_{\mathrm{Nd}} M_{\mathrm{Nd}}+\left(N_{\mathrm{Mn}^{+}} M_{\mathrm{Mn}^{+}}+N_{\mathrm{Mn}^{-}} M_{\mathrm{Mn}^{-}}\right)}{N_{\mathrm{T}}}, \quad (2)
$$
where
$$
M_{\mathrm{Mn}^{+}}=\left|M_{\mathrm{Mn}^{-}}\right|=\frac{\sum_{i}^{N_{\mathrm{Mn}} / 2} S_{i}}{N_{\mathrm{Mn}} / 2}, M_{\mathrm{Nd}}=\frac{\sum_{i}^{N_{\mathrm{Nd}}} \sigma_{i}}{N_{\mathrm{Nd}}}.
$$

The total susceptibility is
$$
\chi_{\mathrm{T}}=\frac{\left(N_{\mathrm{Nd}} \chi_{\mathrm{Nd}}+\left(N_{\mathrm{Mn}^{+}} \chi_{\mathrm{Mn}^{+}}+N_{\mathrm{Mn}^{-}} \chi_{\mathrm{Mn}^{-}}\right)\right)}{N_{\mathrm{T}}}, \quad (3)
$$
where
$$
\begin{aligned}
\chi_{\mathrm{Nd}}= & \beta N_{\mathrm{Nd}}\left(<\left(M_{\mathrm{Nd}}\right)^{2}>-<M_{\mathrm{Nd}}>^{2}\right), \chi_{\mathrm{Mn}^{+}} \\
= & \beta N_{\mathrm{Mn}^{+}}\left(<\left(M_{\mathrm{Mn}^{+}}\right)^{2}>-<M_{\mathrm{Mn}^{+}}>^{2}\right) \\
\chi_{\mathrm{Mn}^{-}}= & \beta N_{\mathrm{Mn}^{-}}\left(<\left(M_{\mathrm{Mn}^{-}}\right)^{2}>-<M_{\mathrm{Mn}^{-}}>^{2}\right) \\
N_{\mathrm{T}}= & N_{\mathrm{Nd}}+N_{\mathrm{Mn}^{+}}+N_{\mathrm{Mn}^{-}}.
\end{aligned}
$$

The total energy and specific heat of the system are evaluated according to the relations
$$
\mathrm{E}=\frac{<H>}{N_{\mathrm{T}}}, \quad (4)
$$

$$
C_{v}=\frac{N_{\mathrm{T}}}{K_{\mathrm{B}} T^{2}}\left[<E^{2}>-<E>^{2}\right], \quad (5)
$$
where $K_{\mathrm{B}}$ is the Boltzmann constant and $T$ is the absolute temperature.

The magnetic entropy is given by
$$
\Delta S_{\mathrm{m}}(T, h)=\int_{0}^{h}\left(\frac{\partial M_{\mathrm{T}}}{\partial T}\right)_{h_{i}} \mathrm{~d} h_{i}. \quad (6)
$$

The following relation is used to calculate the relative cooling power (RCP):
$\mathrm{RCP}=\Delta S_{\mathrm{m}}(T, h)_{\max } \times \delta T_{\mathrm{FWHM}}$, which can be determined from the peak value of $\Delta S_{\mathrm{m}}(T, h)$ and the full-width at half-maximum (FWHM) $\delta T_{\mathrm{FWHM}}$.

For simplicity, throughout the simulations, we take $R_{1}=|J_{\mathrm{NdMn}} / J_{\mathrm{NdNd}}|, \quad R_{2}=J_{\mathrm{MnMn}} / J_{\mathrm{NdNd}}$, $d_{\mathrm{s}}=D_{\mathrm{s}} / J_{\mathrm{NdNd}}, \quad H_{\mathrm{e}}=h / J_{\mathrm{NdNd}}$, and $t=T / J_{\mathrm{NdNd}}$, and assume that $J_{\mathrm{NdNd}}=1$.

## Results and Discussion

This section is devoted to a study of the magnetic properties and magnetocaloric effect in the NMO system. Figure 4 shows the magnetizations, susceptibilities, specific heats, and internal energies of the system sublattices and the total system versus the crystal field $d_{\mathrm{s}}$ for $t=1.2, R_{2}=-4.2, H_{\mathrm{e}}=0$, and two values of $R_{1}\left(R_{1}=0.5\right.$ and 5.0). It is seen that the total magnetizations $M_{\mathrm{Mn}}$ and $M_{\mathrm{Nd}}$ are not influenced by changing $R_{1}$ and $d_{\mathrm{s}}$; that is, $M_{\mathrm{Mn}}=0$ since it is antiferromagnetically ordered and $M_{\mathrm{Nd}}=1.5$. However, the sublattice magnetizations $M_{\mathrm{Mn}^{+}}$and $M_{\mathrm{Mn}^{-}}$are strongly influenced by the change of $R_{1}$ and $d_{\mathrm{s}}$; that is, for $R_{1}=0.5$, it is seen that the magnetizations $M_{\mathrm{Mn}^{+}}$and $M_{\mathrm{Mn}^{-}}$present four plateaus when changing $d_{\mathrm{s}}$, with three first-order transitions between them at $d_{\mathrm{s}_{\mathrm{c} 1}}=-23.2, d_{\mathrm{s}_{\mathrm{c} 2}}=-19.1$, and $d_{\mathrm{s}_{\mathrm{c} 3}}=-14.7$. The first plateau has $M_{\mathrm{Mn}^{+}}=M_{\mathrm{Mn}^{-}}=0$ for $d_{\mathrm{s}}<d_{\mathrm{s}_{\mathrm{c} 1}}$; this value is explained by the fact that all the spins are in the 0 state. The second plateau occurs for $d_{\mathrm{s}_{\mathrm{c} 1}}<d_{\mathrm{s}}<d_{\mathrm{s}_{\mathrm{c} 2}}$ with $M_{\mathrm{Mn}^{+}}=-M_{\mathrm{Mn}^{-}}=0.33$; these magnetization values can be explained by the fact that $67 \%$ of the spins are in state 0, whereas $33 \%$ are in the states $\pm 1$. The third plateau is present for $d_{\mathrm{s}_{\mathrm{c} 2}}<d_{\mathrm{s}}<d_{\mathrm{s}_{\mathrm{c} 3}}$ with $M_{\mathrm{Mn}^{+}}=-M_{\mathrm{Mn}^{-}}=1.0$, where all the spins of the sublattices are in the $\pm 1$ states. Finally, the fourth one is obtained for $d_{\mathrm{s}}>d_{\mathrm{s}_{\mathrm{c} 3}}$, where all the spins are in the $\pm 2$ states, hence the magnetizations are $M_{\mathrm{Mn}^{+}}=+2$ and $M_{\mathrm{Mn}^{-}}=-2$. The same variations are found for $R_{1}=5$, the only differences lying in the positions of the first-order transitions, as in this case they occur at relatively high negative values of $d_{\mathrm{s}}\left(d_{s_{1}}=-77.3, \quad d_{s_{2}}=-73.2, \quad\right.$ and $d_{s_{3}}=-32.8$ ). It is observed that the range of the crystal field $d_{\mathrm{s}}$ between $d_{\mathrm{s}_{\mathrm{c} 2}}$ and $d_{\mathrm{s}_{\mathrm{c} 3}}$ is increased when $R_{1}$ is increased. It is noteworthy that the susceptibilities $\chi_{\mathrm{Nd}}, \chi_{\mathrm{Mn}^{+}}, \chi_{\mathrm{Mn}^{-}}$, and $\chi_{\mathrm{t}}$ and the specific heats $C v_{\mathrm{Nd}}, C v_{\mathrm{Mn}^{+}}$, and $C v_{\mathrm{Mn}^{-}}, C v_{\mathrm{t}}$ exhibit peaks at $d_{\mathrm{s}_{\mathrm{c} 1}}, d_{\mathrm{s}_{\mathrm{c} 2}}$,

![](./images/812519601978998785_4.jpg)

Fig. 4. Magnetizations, susceptibilities, specific heats, and internal energies of the system sublattices and and the total system as functions of $d_{\mathrm{s}}$ for $t=1.2$, $R_{2}=-1$, and two values of $R_{1}$ ($R_{1}=0.5,5$).

![](./images/812519601978998785_5.jpg)

Fig. 5. Magnetizations, susceptibilities, specific heats, and internal energies of the system sublattices and and the total system as functions of $R_{2}$ for $t=1.2$, $d_{\mathrm{s}}=-15$, and different values of $R_{1}$ ($R_{1}=0.5$, 1, 2.5, and 3.5).

and $d_{\mathrm{sc} 3}$. Note also the internal energy of the system starts from its ground state and exhibits jumps at the values $d_{\mathrm{sc} 1}$, $d_{\mathrm{sc} 2}$, and $d_{\mathrm{sc} 3}$. These results confirm the existence of the first-order transitions.

Figure 5 shows plots of the magnetizations, sus- ceptibilities, specific heats, and internal energies of the system sublattices and the total system as functions of the exchange interaction $R_{2}$ for $d_{\mathrm{s}}=-15$, $t=1.2$, and different values of $R_{1}$ ($R_{1}=0.5,1.0,2.5$, and 3.5). As in Fig. 4, it is seen that the magnetizations $M_{\mathrm{Mn}}$ and $M_{\mathrm{Nd}}$ are not influenced by changing $R_{1}$ and $R_{2}$ ($M_{\mathrm{Mn}}=0$ and

$M_{\mathrm{Nd}}=1.5$). It is noteworthy that the sublattice magnetizations $M_{\mathrm{Mn}^{+}}$and $M_{\mathrm{Mn}^{-}}$are strongly influ enced by changing $R_{1}$ and $R_{2}$; that is, for $R_{1}=0.5$, when increasing $R_{2}, M_{\mathrm{Mn}^{+}}$and $M_{\mathrm{Mn}^{-}}$present four plateaus with three first-order transitions at $R_{2_{c 1}}=-4.2, R_{2_{c 2}}=-2.8$, and $R_{2_{c 3}}=-2$. For $R_{2}<R_{2_{c 1}}$, the system favors the high states $\pm 2$, hence $M_{\mathrm{Mn}^{+}}=+2$ and $M_{\mathrm{Mn}^{-}}=-2$, while the second plateau occurs for $R_{2_{c 1}}<R_{2}<R_{2_{c 2}}$, where all the spins of the sublattices are in the $\pm 1$ states ($M_{\mathrm{Mn}^{+}}=+1$ and $M_{\mathrm{Mn}^{-}}=-1$). The third plateau appears for $R_{2_{c 2}}<R_{2}<R_{2_{c 3}}$ with $M_{\mathrm{Mn}^{+}}=+0.33$ and $M_{\mathrm{Mn}^{-}}=-0.33$; these magnetization values can be explained by the fact that $33\%$ of the spins are in the $\pm 1$ states whereas $67\%$ are in the 0 state. Finally, the fourth one is observed for $R_{2}>R_{2_{c 3}}$, where all the spins are in the 0 state, hence the magnetizations are $M_{\mathrm{Mn}^{+}}=M_{\mathrm{Mn}^{-}}=0$. For $R_{1}=1$, the sublattice magnetizations $M_{\mathrm{Mn}^{+}}$and $M_{\mathrm{Mn}^{-}}$present three plateaus with two transitions: a first-order transi tion from $\pm 2$ to $\pm 1$ states at $R_{2}=-3.6$, and a second-order one from $\pm 1$ to 0 states at $R_{2}=-0.9$. For $R_{1}=2.5$, the sublattice magnetizations $M_{\mathrm{Mn}^{+}}$ and $M_{\mathrm{Mn}^{-}}$present only two plateaus with one first order transition from $\pm 2$ to $\pm 1$ states at $R_{2}=-1.6$. When $R_{1}=3.5$, the sublattice magnetizations $M_{\mathrm{Mn}^{+}}$ and $M_{\mathrm{Mn}^{-}}$remain at their high values $\pm 2$ (the spins are in the $\pm 2$ states). It can be concluded that, when increasing $R_{1}$, high spin state values and thus high magnetization are favored. It is also observed that the susceptibilities and specific heats present peaks corresponding to the mentioned transitions, which are confirmed by the jumps in the internal energies at the first-order transitions.

Figure 6 shows plots of the total magnetization $M_{\mathrm{t}}$ (a), total susceptibility $\chi_{\mathrm{t}}$ (b), and total internal energy $E_{\mathrm{t}}$ (c) of the system as functions of temper ature for $R_{1}=1, R_{2}=-1$ and different values of $d_{\mathrm{s}}$ ($d_{\mathrm{s}}=15,0,-15$, and $-30$). It is found that, when $t$ increases, $M_{\mathrm{t}}$ decreases from its saturation value ($M_{\mathrm{t}}=0.75$) and approaches zero at $t_{\mathrm{c}}$. Note that, for $d_{\mathrm{s}}=-15, \chi_{\mathrm{t}}$ exhibits, in addition to the peak corre sponding to $t_{\mathrm{c}}$, another peak corresponding to the rapid change of $M_{\mathrm{Mn}^{+}}$and $M_{\mathrm{Mn}^{-}}$confirmed by Fig. 7. This behavior was also observed in Ref. 34. It is also shown that the internal energy increases from its minimum (ground state) to reach its saturation value for high values of $t$.

The relative cooling power (RCP) is another important factor for assessing the usefulness of magnetic refrigerant materials. $^{35}$ The RCP depends not only on the magnitude of $\triangle S_{\mathrm{m}}$ but also on the temperature dependence of $\triangle S_{\mathrm{m}}$ and the full-width at half-maximum of $\triangle S_{\mathrm{m}}^{\max }.^{36}$ We study the influ ence of the Hamiltonian parameter of the system on the magnetocaloric effect. Figure 8 shows the mag netic entropy $\triangle S_{\mathrm{m}}$ (a) and magnetization $M_{\mathrm{t}}$ (b) as functions of temperature for $R_{1}=1, R_{2}=-1$ and different values of the external magnetic field ($H_{\mathrm{e}}=3,6,9$, and 12). Note that the curve of $\triangle S_{\mathrm{m}}$ presents a maximum in the low temperature region (the maximum obtained at the low temperature

![](./images/812519601978998785_6.jpg)

Fig. 6. Magnetizations $M_{\mathrm{t}}$ (a), susceptibilities $\chi_{\mathrm{t}}$ (b), and internal energies $E_{\mathrm{Nd}}$ (c) of the total system as functions of $t$ for $R_{1}=1$, $R_{2}=-1$, and different values of the crystal field ($d_{\mathrm{s}}=15,0,-15$, and $-30$).

region in the curve of $M_{\mathrm{t}}$ in Fig. 8b is responsible for this behavior) and a minimum around the critical temperature, the intensity of the latter depending strongly on the value of $H_{\mathrm{e}}$. Figure 8c shows the field dependence of the RCP of the system, for $d_{\mathrm{s}}=0, R_{1}=-1$, and $R_{1}=1$. It can be seen that the values of RCP increase monotonically as the field is increased, to reach the value $|\mathrm{RCP}|=0.26$ for $H_{\mathrm{e}}=12$.

To examine the effect of the crystal field on the magnetic entropy and RCP, $\triangle S_{\mathrm{m}}$ is plotted (Fig. 9a) as a function of temperature for $R_{2}=-1, R_{1}=1, H_{\mathrm{e}}=1$, and different values of $d_{\mathrm{s}}$ ($d_{\mathrm{s}}=-15,0$, and 15). It is observed that $\triangle S_{\mathrm{m}}$ presents a minimum at $t_{\mathrm{c}}$, which shifts to the high temperature region with increasing $d_{\mathrm{s}}$. It is also observed that, for $d_{\mathrm{s}}=-15, \triangle S_{\mathrm{m}}$ presents a maximum in the low temperature region which corresponds to the rapid change of the magnetizations $M_{\mathrm{Mn}^{+}}$confirmed in Fig. 7. For the same parameters, the crystal field dependence of the RCP is shown in Fig. 9b. Note that the RCP decreases with increasing $d_{\mathrm{s}}$ and that its values are weak compared with those in Fig. 8c $d_{\mathrm{s}}$.

![](./images/812519601978998785_7.jpg)

To investigate the influence of the exchange interaction on the magnetocaloric effect of the system, the magnetic entropy (Fig. 10a) and RCP (Fig. 10b) are plotted for $R_{2}=-1 d_{\mathrm{s}}=-15, H_{\mathrm{e}}=1$, and different values of $R_{1}$ ($R_{1}=-1.5,2.5$, and 3.5). It is seen that $\triangle S_{\mathrm{m}}$ presents a weak maximum at low temperature (which disappears with increasing $R_{2}$) and a minimum around $T_{\mathrm{c}}$ with an intensity that depends strongly on $R_{1}$. It is also seen that the RCP values (Fig. 10b) approach those in Fig. 9b and that the RCP decreases with increasing $R_{1}$. It can be concluded that $R_{1}$ and $d_{\mathrm{s}}$ have the same effect on the RCP.

Figure 11 presents $\triangle S_{\mathrm{m}}$ as a function of temperature for different values of $R_{2}$ (Fig. 11a) and the RCP as a function of $R_{2}$ (Fig. 11b) for $R_{1}=1, d_{\mathrm{s}}=0$, and $H_{\mathrm{e}}=1$. It is observed that $\triangle S_{\mathrm{m}}$ presents a maximum around $T_{c}$ which moves to high temperatures with increasing $R_{2}$. It is also observed in Fig. 11b that the values of RCP increase with increasing $R_{2}$ and reach the value $\mathrm{RCP}=0.06$ for $R_{2}=1$. Note that the values of RCP are weak compared with those in the previous figures.

## CONCLUSIONS

Density functional theory calculations in the generalized gradient approximation and Monte Carlo simulations are used to study the electronic and magnetic properties and magnetocaloric effects of $\mathrm{NdMnO}_{3}$ simple perovskite. It is found that the system behaves as a ferromagnetic half-metal. The effect of the Hamiltonian parameters on the

![](./images/812519601978998785_8.jpg)

![](./images/812519601978998785_9.jpg)

Fig. 9. Temperature dependence of magnetic entropy (a) for different values of the crystal field ($d_{\rm s} = -15$, 0, and 15) and the crystal field dependence of RCP (b) for $R_1 = 1, R_2 = -1$, and $H_{\rm e} = 1$.

![](./images/812519601978998785_10.jpg)

Fig. 10. Temperature dependence of magnetic entropy (a) for different values of the exchange interaction $R_1$ ($R_1 = 1.5, 2.5$, and 3.5) and the exchange interaction $R_1$ dependence of RCP (b) for $d_{\rm s} = -15, R_2 = -1$, and $H_{\rm e} = 1$.

magnetizations, susceptibilities, specific heats, and internal energies of the system is studied. The results show that the magnetizations $M_{\rm t}$ and $M_{\rm Nd}$ are not influenced by changing the system parameters, while the manganese sublattice magnetizations $M_{\rm Mn^+}$ and $M_{\rm Mn^-}$ are strongly influenced by changing $d_{\rm s}, R_2$, and $R_1$; That is, these magnetizations present plateaus separated by first-order transitions which move to high negative values of $d_{\rm s}$ with increasing $R_1$. However, these transitions disappear when increasing both $R_1$ and $R_2$. It is also observed that the RCP increases when $H_{\rm e}$ or $R_2$ is

![](./images/812519601978998785_11.jpg)

Fig. 11. Temperature dependence of magnetic entropy (a) for different values of the exchange interaction $R_{2}$ ($R_{2}=-1.5,-2$, and -2.5) and the exchange interaction $R_{1}$ dependence of RCP (b) for $d_{s}=0, R_{1}=1$, and $H_{e}=1$.

increased, whereas it decreases when $R_{1}$ or $d_{s}$ is increased.

## CONFLICT OF INTEREST

The authors declare that they have no conflicts of interest.

## REFERENCES

1. S.A. Wolf, D.D. Awschalom, R.A. Buhrman, J.M. Daughton, S. vonMolnar, M.L. Roukes, A.Y. Chtchel-kanova, and D.M. Treger, *Science* 294, 1488 (2001).
2. W.E. Pickett and J.S. Moodera, *Phys. Today* 54, 39 (2001).
3. H.N. Chen and S.H. Yang, *Adv. Mater.* 29, 1603994 (2017).
4. G. Yang, H.W. Lei, H. Tao, X.L. Zheng, J.J. Ma, and Q. Liu, *Small* 13, 1601769 (2017).
5. M. Fiebig, *J. Phys. D* 38, R123 (2005).
6. S. Sidi Ahmed, M. Boujnah, L. Bahmad, A. Benyoussef, and A. El Kenz, *Chem. Phys. Lett.* 685, 191 (2017).
7. H.-T. Jeng and G.Y. Guo, *Phys. Rev. B* 67, 094438 (2003).
8. D.P. Rai, A. Shankar, M.P. Ghimire, Sandeep, and R.K. Thapa, *Comput. Mater. Sci.* 101, 313 (2015).
9. S. Wurmehl, G.H. Fecher, H.C. Kandpal, V. Ksenofontov, C. Felser, and H.J. Lin, *Appl. Phys. Lett.* 88, 032503 (2006).
10. M. Karaca, S. Kervan, and N. Kervan, *J. Alloys Compd.* 639, 162 (2015).
11. P.J. Dereen, A. Bednarkiewicz, Ph Goldner, and O. Guillot- Noel, *J. Appl. Phys.* 103, 043102 (2008).
12. U.G. Akpan and B.H. Hameed, *Appl. Catal.* 357, 1 (2010).
13. Ni, et al. *J. Nanosci. Nanotechnol.* 16, 1046 (2016).
14. H.-R. Wenk and A. Bulakh, Cambridge University Press, New York, NY, ISBN. 978, 52958 (2004).
15. A. Munoz, J.A. Alonso, M.J. Martinez-Lope, J.L. Garcia- Munoz, and M.T. Fernandez- Diaz, *J. Phys. Condens. Mat- ter.* 12, 1361 (2000).
16. C.P. Khattak, F.F.Y. Wang, K.A. Gschneider, Jr., and L. Eyring (Eds.), *Hdb. Phys. Chem. Rare Earths* 3, 525 (1979).
17. F. Bartolome, J. Herrero-Albillos, and L.M. Garcia, J. Bar- tolome, *J. Appl. Phys.* 97, 10A503 (2005).
18. A.A. Mukhin, V. Yu Ivanov, V.D. Travkin, and A.M. Bal- bashov, *J. Magn. Magn. Mater.* 226, 1139 (2001).
19. S. Jandl, A.A. Mukhi, V. YuIvanov, A. Balbashov, and M. Orlita, *J. Magn. Magn. Mater.* 321, 3607 (2009).
20. M. Udeshi, B. Vyas, and P. Trivedi et al, *Nucl. Instrum. Methods Phys. Res. B* 365, 560 (2015).
21. S. Saha, S. Chanda, A. Dutta, and T.P. Sinha, *Mater. Res. Bull.* 48, 4917 (2013).
22. B. Vyasa, H. Kundaliaa, M. Udeshia, P. Trivedib, S. Raya- prold, and D.G. Kuberkare, *Ceram. Int.* 43, 14962 (2017).
23. K.T. Jacob, M. Attaluri, and K. Fitzner, *Calphad.* 26, 313 (2002).
24. H.C. Guptaa, V. Sharmaa, U. Tripathia, and N. Ranib, *J. Phys. Chem. Solids* 66, 1314 (2005).
25. B. Bouadjemi, S. Bentata, A. Abbad, and W. Benstaali, Solid State Commun. 207, 9 (2015).
26. R. Masrour, A. Jabar, A. Benyoussef, M. Hamedoun, and E.K. Hilil, *J. Magn. Magn. Mater.* 401, 91 (2016).
27. J.S. Salcedo-Gallo, D.F. Rodríguez-Patiño, J.D. Alzate-Car- dona, H. Barco-Ríos, and E. Restrepo-Parra, *Phys. Lett. A* 382, 2069 (2018).
28. S. Amraoui, A. Feraoun, and M. Kerouad, *J. Phys. Chem. Solids* 131, 189 (2019).
29. S. Amraoui, A. Feraoun, and M. Kerouad, *Phys. A Stat. Mech. Appl.* 550, 124198 (2020).
30. K. Wang, N. Si, Y.-L. Zhang, F. Zhang, A.-B. Guo, and W. Jiang, *Vacuum* 165, 105 (2019).
31. C. Wu, W. Zheng, W. Feng, and W. Jiang, *J. Phys. Soc. Jpn.* 89, 064713 (2020).
32. C. Wu, W. Zheng, N. Si, W.J. Feng, F.G. Zhang, and W. Jiang, *Chin. J. Phys.* 66, 436 (2020).
33. M.E.J. Newman and G.T. Barkema, Oxford University Press, Oxford, 4, 1 (1999).
34. T.M.D. Nguyen, T.K.V. Nguyen, K. Makio, K. Kensuke, M.H. Phan, and T.H. Ngo, *VNU J. Sci. Math. Phys.* 32, 1 (2016).
35. A. Kitanovski and P.W. Egolf, *Int. J. Refrig.* 29, 3 (2006).
36. W.J. Kuen, L.K. Pah, A.H. Shaari, C.S. Kien, N.S. Wei, and A.G.H.M ing, *Pertanika J. Sci. Technol.* 20, 81 (2012).

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institu- tional affiliations.
