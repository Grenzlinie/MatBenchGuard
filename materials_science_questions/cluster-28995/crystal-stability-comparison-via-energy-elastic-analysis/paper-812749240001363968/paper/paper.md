# High temperature–high pressure phase transformation of Cu

Urmimala Dey$^{\text{a}}$, Nilanjan Mitra$^{\text{a,b,*}}$, A. Taraphder$^{\text{a,c,d,*}}$

$^{\text{a}}$ Centre for Theoretical Studies, Indian Institute of Technology, Kharagpur-721302, India
$^{\text{b}}$ Civil Engineering Department, Indian Institute of Technology, Kharagpur-721302, India
$^{\text{c}}$ Department of Physics, Indian Institute of Technology, Kharagpur-721302, India
$^{\text{d}}$ School of Basic Sciences, Indian Institute of Technology, Mandi, HP 175005 India

---

## ARTICLE INFO

**Keywords:**
Phase transition
Single crystal Cu
High temperature high pressure
DFT
Hemholtz free energy
Gibbs free energy
Quasiharmonic approximation

## ABSTRACT

DFT calculations (typically done at 0 K), Helmholtz free energy and Gibbs free energy calculations (for high temperature) within the quasi-harmonic approximation have been done in this manuscript to probe a metastable phase of Cu observed at high temperature and high pressure. The high electronic thermal conductivity observed for this new metastable phase of Cu may be beneficial for high temperature engineering applications in electronic and spacecraft device designs.

---

### 1. Introduction

Typically Cu exists as a face-centered-cubic material at ambient temperature and pressure conditions. The non-existence of body centered phase of Cu at ambient pressure and 0 K temperature has been proved by numerous researchers through DFT based studies [1,2]. However, it is interesting to observe that in molecular beam epitaxy, BCC films of Cu have been grown pseudomorphically on Pd{001}, Pt {001}, Ag{001} and Fe{001} substrate [3–6]. Typically in beam epitaxy, the sample is subjected to a constrained pressure (which in this case is induced by the substrate grain boundary). The controversy of unstable existence of body centered phase of Cu at ambient pressure and temperature conditions along with experimental observations of body centered phase of Cu in epitaxy was eventually resolved. The explanation provided was that the stable substrates, acting as grain boundaries, influence the phase change in Cu and it can happen only in thin films and not for bulk material or even thick films [7]. An existence of a BCT phase of Cu with $c/a = 0.93$ was demonstrated [8] which is observed to be tetragonally stable by calculation of the epitaxial Bain path of Cu. However, it has also been mentioned in the manuscript since this special BCT phase does not satisfy all the stability criteria imposed on elastic constants, it is unstable against other modes of shear deformation. Typically, these $ab$ initio studies have been carried out at 0 K; there maybe a possibility of stable body-centered phase of Cu at higher temperatures and pressures which is yet to be explored.

Apart from molecular beam epitaxy studies which typically constrains the lattice structure by application of pressure from substrate grain boundaries, Cu-based shape memory alloys also exhibit a BCC phase at high temperatures. It has been reported through Neutron diffraction studies that body centered phase of Cu is present in Cu based shape memory alloys such as in Cu-Zn-Al, [9] Cu-Al-Ni, [10] Cu-Al-Pd, [11] Cu-Al-Be [12] in which the whole TA2[110] phonon branch was observed to soften with temperature as transition temperature is approached. It should be mentioned in this regard that it is well known that entropy changes in a Martensitic Transformation is due to contributions from vibrational component of the crystal lattice and electronic contributions near the Fermi surface. Friedel [13] postulated that even though body centered phase of Cu is energetically unstable at 0 K, it may be the preferred system at high temperature due to its large entropy resulting from low-energy vibrational transverse modes. For Cu based shape memory alloys it was observed through calorimetric and magnetic measurements that vibration of the lattice (specifically the coupling between homogeneous shear and short wavelength phonon) is the main reason for stability of the BCC phase at high temperature and the electronic contribution to entropy change is negligible [14–16]. Comparing this low lying phonon branch to Zener elastic modes, [17] a new Hamiltonian has also been proposed [18] which displays vibrational-entropy-driven first-order solid-solid diffusionless martensitic phase transitions. The model Hamiltonian is suitable for high temperature applications since it employs anharmonic intersite couplings which alters the vibration stiffness with changes in temperature.

It should be realized that in Cu-based soft memory alloys, the Cu

---

* Corresponding authors at: Centre for Theoretical Studies, Indian Institute of Technology, Kharagpur-721302, India.
E-mail addresses: nilanjan@civil.iitkgp.ac.in (N. Mitra), arghya@phy.iitkgp.ernet.in (A. Taraphder).

https://doi.org/10.1016/j.commatsci.2019.109154
Received 13 April 2019; Received in revised form 28 June 2019; Accepted 19 July 2019
0927-0256/ © 2019 Elsevier B.V. All rights reserved.

![](./images/812749240001363968_1.jpg)

Fig. 1. Crystal structures of the (a) FCC (space group Fm3m) and the (b) BCT (space group I4/mmm) phases of Cu.

crystal structure is constrained (due to presence of other materials eventually resulting in development of pressure) which undergoes a phase transition to that of a body centered phase on high temperature. Thereby, given this observation it is quite conceivable that under high temperature and pressure conditions there may exist a body centered phase of Cu. Body centered tetragonal phase of Cu was also demon- strated to develop when Cu single crystals are subjected to shock compression along the [100] direction at a piston velocity of around 1.5-2 km/s [19].

This present study is aimed at investigating the possibility of ex- istence of a metastable body centered tetragonal phase of Cu at high temperature and pressure. The study also demonstrates changes in properties of the material that are associated with phase transformation of Cu from FCC to BCT phase; which might have future engineering applications.

## 2. Simulation methodology

We perform density functional theory calculations using the full potential linearized augmented plane wave (FLAPW) method im- plemented in the WIEN2K package [20]. The generalized gradient ap- proximation (GGA) of Perdew-Burke-Ernzerhof (PBE) [21] is employed for the exchange-correlation part. Three other functionals, namely, local-density approximation (LDA) [22], GGA-PBEsol exchange-corre- lation [23] and GGA functional of Wu and Cohen (WC) [24] are also employed. However, it is found that GGA of PBE gives the equilibrium lattice parameter ($a_{PBE}=3.605$ Å) closest to the experimental value of $a_{expt}=3.615$ Å compared to the other exchange-correlation functionals ($a_{LDA}=3.498$ Å, $a_{PBEsol}=3.543$ Å, $a_{WC}=3.550$ Å) and thereby GGA-PBE functional has been chosen for further calculations in this manuscript. A k-mesh of $20×20×20$ k-points is used for the whole Brillouin zone. We use $L_{max}=12$ for the expansion of partial waves and $G_{max}=14$ Bohr⁻¹ for the charge Fourier expansion. The muffin tin radii (RMT) and $K_{max}$ are chosen such that $RMT×K_{max}=7.0$, where $K_{max}$ is the largest plane wave vector used in the plane-wave expansion.

Phonon dispersion spectra and free energies are calculated within the framework of quasi-harmonic approximation (QHA) using the finite displacement method in the PHONOPY code [25]. For calculating the real space force constants we use the projector augmented wave (PAW) method as implemented in the Vienna Ab initio Simulation Package (VASP) [26]. We take an energy cutoff of 500 eV for the plane waves and a $11×11×11$ Monkhorst-Pack k-mesh [27] is adopted to integrate the full Brillouin zone. The atomic positions are relaxed until the maximum Hellmann-Feynman forces on the atom are smaller than 1 meV/Å. Energy convergence criterion is set to $10^{-8}$ eV. The effect of thermal expansion is taken into account within the QHA to calculate the Gibbs free energy at high pressure starting from the Helmholtz free energy computed at 10 different volumes about the 0 K equilibrium volume.

We determine the elastic constants by analyzing the changes in the calculated stress values resulting from changes in the strain as im- plemented in the VASP code. In the stress-strain approach, a set of linear equations are constructed from the stress tensors calculated from each deformation and the solutions of the linear system of equations are found by using orthogonal matrix factorizations. This approach uses the well-known tensorial form of the Hooke's law, that describes the rela- tion between the stress component and the applied strain [28]. The symmetric elastic constants are calculated after fully relaxing a crystal structure.

Transport properties are determined with the BoltzTraP code [29] interfaced with WIEN2K using a dense k-mesh of $30×30×30$ k-points. In order to obtain an analytical expression of bands, BoltzTraP code depends on a well tested smoothed Fourier interpolation. The constant relaxation time approximation is used in the calculations. Since the electrons contributing to transport reside in a narrow energy range due to the delta-function like Fermi broadening, the relaxation time can be assumed to be nearly the same for all the electrons. In our DFT calcu- lations, the temperature dependence of the electronic band structure is ignored.

## 3. Results

It is well known that at ambient pressure and temperature, Cu crystallizes in a face-centered cubic (FCC) structure with space group symmetry Fm$\overline{3}$m (No. 225), as shown in Fig. 1(a).

In order to obtain the equilibrium lattice parameters, the total en- ergy of the system is optimized as a function of volume and the data is fitted to the Birch-Murnaghan (B-M) equation of state [30,31],
$$
P(V)=\frac{3B}{2}\left[\left(\frac{V_0}{V}\right)^{\frac{7}{3}}-\left(\frac{V_0}{V}\right)^{\frac{5}{3}}\right]×\left\{1+\frac{3}{4}(B'-4)\left[\left(\frac{V_0}{V}\right)^{\frac{2}{3}}-1\right]\right\} \tag{1}
$$
where, $P, V_0, V, B, B'$ denote the pressure, reference volume, deformed volume, bulk modulus and the pressure derivative of the bulk modulus respectively.

At ambient pressure, total energy optimization with respect to the cell volume shows that the minimum energy structure of the FCC phase corresponds to the equilibrium lattice parameter of $a=3.605$ Å. When assigned to the BCT structure with space group I4/mmm (i.e. $\frac{c}{a}=1.414$), it corresponds to $a=2.550$ Åand $c=3.605$ Åwhich match well with the previous first-principles total energy calculations of BCT Cu by Morrison et al. [32]. The crystal structure of the BCT phase is shown in Fig. 1(b).

However, when it is subjected to high pressure, the FCC structure becomes unstable with respect to a tetragonal distortion and at shock pressure of ~80 GPa, the FCC structure is transformed into a body centered tetragonal (BCT) structure [19]. This FCC-BCT phase transi- tion results in the appearance of a local minimum in the total energy versus $\frac{c}{a}$ ratio curve, as shown in Fig. 2. In Fig. 2, we plot the total energy as a function of the $\frac{c}{a}$ ratio, keeping the volume of the cell fixed at $8.99$ Å³/atom, which according to the equation to the state (Eq. (1)) corresponds to ~80 GPa pressure. It is found that there are two minima in the relative energy versus $\frac{c}{a}$ plot. The global minimum occurs at

![](./images/812749240001363968_2.jpg)

Fig. 2. DFT calculated energy (relative to the ground state energy $E_0$) of the different phases of Cu versus $\frac{c}{a}$ ratio under high pressure (~80 GPa). At high pressure, a local minimum appears for $\frac{c}{a}=0.966$. Energy of this high pressure BCT phase is lower than the BCC phase. However, the global minimum corresponds to the FCC phase with $\frac{c}{a}=1.414$. In the inset we show the zoomed figure to clearly identify the positions of the two minima. The blue squares denote the positions of the FCC, BCC and BCT structures.

$\frac{c}{a}=1.414$, corresponding to the FCC structure and the local minimum appears at $\frac{c}{a}=0.966$, which is 29.8 meV higher in energy compared to the FCC phase. There exists another metastable BCC phase very close to the BCT phase, 1.1 meV higher in energy than the BCT structure. The obtained $\frac{c}{a}$ ratio for the high pressure BCT phase is consistent with the previously reported value of $\frac{c}{a}$ found in the shock wave study of single crystal Cu [19]. The calculated equilibrium lattice parameters of the high pressure BCT structure are $a=2.650$ Åand $c=2.560$ Å. Since the energy difference between the BCC and BCT phases is very small, the total energy of the system is recalculated as a function of the $\frac{c}{a}$ ratio with increased accuracy (with $30\times30\times30$ k-mesh grid and $RMT\times K_{max}=9.0$). It is observed that with increased accuracy, there is no qualitative change in the nature of the plot, however, the energy difference between the metastable BCC and BCT phases increases to 1.48 meV ($E_{BCC}-E_{BCT}=1.48$ meV) and the local minimum occurs at $\frac{c}{a}=0.967$.

In order to check the mechanical stability of the high pressure BCT phase found, the phonon spectrum of the BCT structure is calculated using the equilibrium lattice parameters and it is compared with the phonon spectrum of the FCC phase. As seen from Fig. 3, the transverse acoustic (TA) modes are hardened in the BCT phase along the Z-$\Gamma$ and $\Gamma$-Z' directions. On the contrary, a soft mode appears along the $[\xi\xi0]$ direction. In case of Cu-based shape memory alloys, it is found that the low energy of the TA2 [110] phonon mode contributes significantly to the excess of entropy which stabilizes the tetragonal phase at high temperature [14] and has been proved experimentally [14]. However, the softening of the TA2 mode near the X-point indicates that the shear modulus, obtained by taking the derivative of the TA2 mode will be negative and will lead to the mechanical instability of the BCT phase at high pressure.

<table>
<caption>Table 1
Elastic constants of the FCC and BCT phases of Cu at $T=0$ K. Since the shear modulus $c'$ is negative for the BCT phase, the BCT structure is unstable with respect to shear deformations and will be mechanically unstable.</caption>
<thead>
<tr>
<th>Elastic constants in GPa</th>
<th>FCC Cu</th>
<th>BCT Cu</th>
</tr>
</thead>
<tbody>
<tr>
<td>$c_{11}$</td>
<td>230.81</td>
<td>400.60</td>
</tr>
<tr>
<td>$c_{12}$</td>
<td>119.00</td>
<td>445.16</td>
</tr>
<tr>
<td>$c_{13}$</td>
<td>–</td>
<td>376.98</td>
</tr>
<tr>
<td>$c_{33}$</td>
<td>–</td>
<td>488.77</td>
</tr>
<tr>
<td>$c_{44}$</td>
<td>114.01</td>
<td>267.47</td>
</tr>
<tr>
<td>$c_{66}$</td>
<td>–</td>
<td>278.43</td>
</tr>
<tr>
<td>$c'$</td>
<td>55.91</td>
<td>−22.28</td>
</tr>
</tbody>
</table>

The calculated elastic constants of the FCC and BCT structures are shown in Table 1. For cubic systems, the elastic matrix $c_{ij}$ has only three independent components: $c_{11}$, $c_{12}$ and $c_{44}$ and the Born stability criteria for the mechanical stability of cubic systems are given by [28]

$$c_{11}-c_{12}>0 \tag{2a}$$

$$c_{11}+2c_{12}>0 \tag{2b}$$

$$c_{44}>0 \tag{2c}$$

However, in case of tetragonal systems, there are six independent elastic constants: $c_{11}$, $c_{12}$, $c_{13}$, $c_{33}$, $c_{44}$ and $c_{66}$, which satisfy the following necessary and sufficient conditions for the stability of a tetragonal system [28]:

![](./images/812749240001363968_3.jpg)

Fig. 3. Phonon band dispersions for the known FCC (left) phase and the high pressure BCT (right) phase of Cu. The filled circles denote the LA modes and the open circles show the TA modes. LA and TA are the longitudinal and transverse acoustic modes respectively. T1 and T2 are the two TA modes. In the BCT phase, softening of phonon modes along the $[\xi\xi0]$ direction indicates the dynamical instability of the BCT structure at low temperature (0 K) and high pressure.

![](./images/812749240001363968_4.jpg)

Fig. 4. The per atom free energy of the BCT phase of Cu relative to the FCC and BCC phases as a function of temperature. For the Helmholtz free energy, the volume is fixed at $8.99 \AA^3$/atom corresponding to ~80 GPa pressure, whereas, for the calculation of Gibbs free energy, the pressure is kept fixed at ~80 GPa. The Gibbs free energy data show that as the temperature raises, the BCT phase gains stability over the other two phases.

$$
c_{11}>\left|c_{12}\right| \tag{3a}
$$

$$
2 c_{13}^{2}<c_{33}\left(c_{11}+c_{12}\right) \tag{3b}
$$

$$
c_{44}>0 \tag{3c}
$$

$$
c_{66}>0 \tag{3d}
$$

Our DFT calculated elastic constants for the FCC phase, as listed in Table 1, fulfill all the stability criteria (Eq. (2)), which implies that the FCC phase is stable at ambient pressure and low temperature. By contrast, the elastic constants of the high pressure BCT phase satisfy the conditions (3b), (3c) and (3d), but fail to satisfy condition (3a). Therefore, the shear modulus $c^{\prime}=\frac{c_{11}-c_{12}}{2}<0$ (Table 1), suggesting that the BCT structure would decrease its energy by deformations of the cell and as a result the BCT phase will be unstable at low temperature (0 K).

However, the dynamical instability of a crystal structure at low temperature does not mean that the crystal structure is unstable at high temperature. Since our *ab initio* calculations are carried out at ground state ($T=0$ K), there may be a possibility that the BCT phase may attain stability at high temperature. For example, the body centered cubic (BCC) phase of Fe gains stability at high temperature, [33-35] though it is not stable at high pressure and low temperature ($T=0$ K). From Fig. 2 we find that at high pressure, the BCT phase results in the appearance of a local minimum in the energy vs. $\frac{c}{a}$ ratio plot, however, the energy of the BCT phase is higher than the FCC minimum, indicating that the FCC phase is more stable compared to the BCT phase at low temperature and high pressure (~80 GPa). Also, there exists a metastable BCC phase very close in energy to the BCT phase. Therefore, in order to check the relative stabilities of the three phases (FCC, BCC and BCT) at higher temperatures, we calculate the Helmholtz free energies (per atom) of the three phases employing the information of the phonon density of states at the volume $8.99 \AA^3$/atom.

In the harmonic approximation, the lattice vibrations are considered as independent harmonic oscillators and the constant volume Helmholtz free energy is calculated as the sum of the lattice energy of the 0 K equilibrium structure and the temperature dependent vibrational free energy contribution of all the phonon modes [36]. However, as the temperature rises above zero, both the lattice energy and phonon contributions change due to the variation in the lattice volume as a result of thermal expansion or contraction. Therefore, it is necessary to consider the anharmonic effects to account for the temperature dependence of the thermodynamic potentials, which can be introduced by the quasi-harmonic approximation (QHA). The Harmonic phonon model of lattice dynamics considers all inter-atomic forces as harmonic. However, this model fails to consider dynamics at finite temperature in which the equilibrium distance between atoms becomes dependent on temperature. Thereby, the quasi-harmonic approximation is considered in which the phonon frequencies are volume dependent and for each volume harmonic approximation holds. In the QHA, a part of the temperature effect is included in the total energy through phonon (Helmholtz) free energy at constant volume. Since the thermal properties are required at constant pressure, some transformation should be made from function of $V$ to function of $P$. Therefore, the constant-volume Helmholtz free energy $F(V, T)$ is evaluated for a range of volumes about the zero temperature equilibrium volume as a function of temperature and calculate the Gibbs free energy $G(P, T)$ by minimizing $F(V, T)$ with respect to volume at a constant pressure $P$. [36,37]

$$
G(T, P)=\min _{V}\left[U(V)+F_{\text {phonon }}(V, T)+P V\right]=\min _{V}[F(V, T)+P V] \tag{4}
$$

The volume dependencies of the electronic and phonon energies are different and as a result, the equilibrium volume obtained by minimizing the function in the square bracket of Eq. (4) will be different from that calculated from electronic structure at 0 K. With increasing temperature, $F_{\text {phonon }}(V, T)$ changes, which in turn changes the equilibrium volume. Thus the thermal expansion is taken into account in the QHA.

Therefore, at any arbitrary temperatures, we determine the Gibbs free energy by fitting the free energy to an equation of state (Birch-Murnaghan equation of state in this work) as a function of volume. Since Gibbs free energy is experimentally more relevant, we calculate the Gibbs free energy of the two phases of Cu at a constant pressure of 80 GPa within the QHA to compare the relative stabilities of the two phases. In Fig. 4, we show the Helmholtz free energy and the Gibbs free energy per atom of the BCT phase relative to the FCC and BCC phases as a function of temperature. From Fig. 4, it is found that at high pressure (~80 GPa), Helmholtz free energy of the BCT phase is always lower than that of the FCC phase, whereas, the Gibbs free energy data show that the FCC to BCT transition takes place at ~600 K. When compared to the BCC phase, the Helmholtz free energy plot shows that the BCT phase is less stable than the BCC phase. However, the Gibbs free energy data, calculated within the QHA, show that at all temperatures the BCT phase is more stable compared to the BCC phase, confirming that at the temperature and pressure of shock wave (80 GPa and 1130 K) [19], the BCT phase is the most stable phase. Since the Helmholtz free energy is calculated in the harmonic approximation and the Gibbs free energy is calculated in the quasi-harmonic approximation, we find that the introduction of the anharmonic effects is necessary for the correct description of the stability of the BCT phase.

In the above discussion, we show the stability of the metastable BCT phase of Cu at the temperature and pressure of the shock wave (80 GPa and 1130 K), which is consistent with the results obtained in the Molecular Dynamics (MD) simulations of single crystal Cu by Neogi et al. [19] However, the predictions of DFT and MD methods may not

![](./images/812749240001363968_5.jpg)

Fig. 5. Relative energy of the different phases of Cu as a function of $\frac{c}{a}$ ratio at fixed volumes of $9.89\ \mathring{A}^3$/atom and $8.35\ \mathring{A}^3$/atom corresponding to ~40 GPa and ~120 GPa pressures respectively. In both cases, the global minimum corresponds to the FCC structure. For ~40 GPa pressure, the local minimum occurs at $\frac{c}{a}=0.966$, whereas, it is shifted to $\frac{c}{a}=0.972$ when we use ~120 GPa pressure. In the inset we show the zoomed figures to clearly identify the positions of the minima. The green squares denote the positions of the local and global minima.

![](./images/812749240001363968_6.jpg)

Fig. 6. Phonon band dispersions of the BCT phase of Cu at (a) ~40 GPa and (b) ~120 GPa pressures. At both pressure values a soft phonon appears along the $[\xi\xi0]$ direction, indicating the dynamical instability of the BCT structure at low temperature (0 K). (c) The per atom Gibbs free energy of the BCT structure relative to the FCC and BCC phases as a function of temperature for two different applied pressures. For ~40 GPa pressure, the Gibbs free energy of the FCC phase is always lower than that of the BCT and BCC phases. On the other hand, the Gibbs free energy data at ~120 GPa pressure show that the BCT phase gains stability at higher temperature. The BCC phase is always less stable than the BCT phase and the FFC to BCT phase transition takes place at ~300 K.

be always consistent and more systematical calculations are needed to study the stability of Cu at various pressures by DFT. Therefore, in order to check the effect of pressure on the stability of the BCT phase of Cu, we calculate the total energy of Cu as a function of $\frac{c}{a}$ ratio at fixed volumes of $9.89\ \mathring{A}^3$/atom and $8.35\ \mathring{A}^3$/atom corresponding to ~40 GPa and ~120 GPa pressures respectively. Fig. 5 shows that in both cases, the global minimum corresponds to the FCC structure and the qualitative nature of the plots are similar. However, for ~40 GPa pressure, the local minimum occurs at $\frac{c}{a}=0.966$, whereas, it is shifted to $\frac{c}{a}=0.972$ when we use ~120 GPa pressure. The phonon spectrums in

![](./images/812749240001363968_7.jpg)

Fig. 7. Electronic band structures of the (a) FCC and (b) high pressure (~80 GPa) BCT phases of Cu. As seen, the number of holes are less in the BCT structure. Therefore, the electrical conductivity as well as the electronic thermal conductivity are expected to be higher for the BCT phase. (c) Total density of states (DOS) of the two phases of Cu as a function of energy. Here, $E_F$ is the Fermi level. Since there are finite density of states near the Fermi level, both the structures are metallic.

Figs. 6(a) and 6(b) show that in both cases, the BCT structure is not dynamically stable at 0 K temperature. In order to check the relative stability of the metastable BCT phase compared to the BCC and FCC phases at higher temperatures, we evaluate the Gibbs free energies within the quasi-harmonic approximation for the two different pressure values. From Fig. 6(c) we see that for ~40 GPa pressure, the Gibbs free energy of the FCC phase is always lower than that of the BCT and BCC phases. On the other hand, the Gibbs free energy data at ~120 GPa pressure show that the BCT phase gains stability at higher temperature. The BCC phase is always less stable than the BCT phase and the FFC to BCT phase transition takes place at ~300 K, which is much lower than the FCC-BCT phase transition temperature found for ~80 GPa pressure, as shown in Fig. 4. This brings us to conclude that the BCT phase of Cu gains stability with increasing pressure and temperature i.e. we simultaneously need to apply high pressure and high temperature to stabilize the metastable BCT phase of Cu.

The calculated electronic band structures and the density of states (DOS) of FCC and high pressure (~80 GPa) BCT phases of Cu (Fig. 7) show that both the structures have finite DOS near the Fermi level and therefore they will show metallic behaviour. Investigating the electronic band structures (Figs. 7(a) and 7(b)) of FCC and BCT Cu, we find that in case of FCC Cu, there exist three hole pockets near the Fermi level $E_F$: one along the $\Gamma-X$ direction, one at the $L$ point and one along the $K-\Gamma$ direction, whereas, in case of BCT Cu, there are only two hole pockets present near the Fermi level $E_F$: one along the $\Gamma-X$ direction and the other along the $N-\Gamma$ direction, indicating that the number of holes is less in case of the BCT structure. Therefore, the electrical conductivity as well as the electronic thermal conductivity are expected to be higher for the BCT phase, though the DOS at the Fermi level $E_F$ (as seen from Fig. 7(c)) is less in BCT Cu compared to the FCC phase. Based on the calculated band structures, we find out the electronic thermal conductivity of the two phases as a function of temperature for a fixed chemical potential using the semi-classical Boltzmann theory [38]. Though the thermal conductivity of a material consists of both electronic $(\kappa^0)$ and phonon $(\kappa^l)$ parts, BoltzTraP calculates only the electronic thermal conductivity $\kappa^0$ in terms of the relaxation time $\tau$, assuming that $\tau$ is constant and direction independent, where the interaction of the electrons with phonons or lattice imperfections are not taken into account. The thermal conductivity of a material with particle velocity $v$, heat capacity $C$ per unit volume, and mean free path $l$ is given by, $\kappa = \frac{1}{3}Cvl$, which for a free electron gas, reduces to $\kappa^0 = \frac{\pi^2 n K_B^2 \tau T}{3m}$. Here, $n$ is the electron density, $K_B$ is the Boltzmann constant and $m$ is the free electron mass. Therefore, the electronic thermal conductivity of metallic Cu will increase linearly with temperature as seen from Fig. 8, where we find that as temperature rises, the electronic thermal conductivity of both the phases of Cu increases linearly with

![](./images/812749240001363968_8.jpg)

Fig. 8. The electronic thermal conductivity of the two phases of Cu as a func-
tion of temperature. The high thermal conductivity of the BCT structure shows
that it can be used as a good thermal conductor in electronic and spacecraft
devices.

increasing temperature. However, the slope is higher in case of the BCT
phase, which might suggest possible applications of this phase of the
material for electronic devices, such as cooling chips or in spacecraft
thermal control applications.

It should also be noted that as temperature increases the electron
mean free path is reduced by collisions with phonons and phonon
contributions become significant. So, there is a need to determine the
phonon contributions to evaluate the total thermal conductivity (as are
typically done in experiments [41]) before any conclusive statement
can be made with regards to usage of the material in high temperature
situations.

## 4. Conclusions

The possibility of the existence of a metastable body-centered tet-
ragonal phase for Cu has been established in this study. These states
may be achieved on simultaneous application of high temperature and
pressure to a bulk sample of Cu, which is brought about by shock
loading. The constant-volume Helmholtz free energy and the constant-
pressure Gibbs free energy distributions at a high pressure demonstrate
the stability of the BCT phase compared to the FCC and BCC phases at
high temperatures, realized through shock loading. Also, the BCT phase
of Cu is observed to have high electronic thermal conductivity com-
pared to that of the FCC phase and may be beneficial for different high
temperature engineering applications.

The entire study has been based on quasi-harmonic approximations.
One must note that in the QHA, the thermodynamic properties are
calculated excluding the imaginary modes from the partition function.
However, a proper description requires the renormalization of ima-
ginary modes using self-consistent phonon theory and this re-
normalization scheme may give rise to additional low-energy phonon
modes which will have significant contributions to the free energies
[39]. Also, the quasi-harmonic approximation is found to be valid up to
about 67% of the melting point [40] and thus the complete description
of the system requires the inclusion of higher order anharmonic terms.

### CRediT authorship contribution statement

Urmimala Dey: Methodology, Software, Validation, Data_curation,
Writing_%E2%80%93_original_draft. Nilanjan Mitra: Conceptualization,
Writing_%E2%80%93_original_draft, Writing_%E2%80%93_review_
%26_editing, Supervision. A. Taraphder: Writing_%
E2%80%93_original_draft, Writing_%E2%80%93_review_%26_editing,
Supervision.

### Acknowledgments

UD appreciates access to the computing facilities of the DST-FIST
(phase-II) project installed in the Department of Physics, IIT Kharagpur,
India. UD would like to acknowledge Dr. Monodeep Chakroborty for
some useful discussions and the Ministry of Human Resource
Development for research fellowship.

### References

[1] Z.W. Lu, S.-H. Wei, A. Zunger, Phys. Rev. B 41 (1990) 2699.
[2] T. Kraft, P.M. Marcus, M. Methfessel, M. Scheffler, Phys. Rev. B 48 (1993) 5886.
[3] Z.Q. Wang, S.H. Lu, Y.S. Li, F. Jona, P.M. Marcus, Phys. Rev. B 35 (1987) 9322(R).
[4] H. Li, S.C. Wu, D. Tian, J. Quinn, Y.S. Li, F. Jona, P.M. Marcus, Phys. Rev. B 40
(1989) 5841(R).
[5] H. Li, D. Tian, J. Quinn, Y.S. Li, F. Jona, P.M. Marcus, Phys. Rev. B 43 (1991) 6342.
[6] Y.S. Li, J. Quinn, H. Li, D. Tian, F. Jona, P.M. Marcus, Phys. Rev. B 44 (1991) 8261.
[7] L.G. Wang, M. Šob, Phys. Rev. B 60 (1999) 844.
[8] F. Jona, P.M. Marcus, Phys. Rev. B 63 (2001) 094113.
[9] G. Guenin, S. Hautecler, R. Pynn, P.F. Gobin, L. Delaey, Scr. Metall. 13 (1979)
429-430.
[10] S. Hoshino, G. Shirane, M. Suezawa, T. Kajitani, Jpn. J. Appl. Phys. 14 (1975) 1233.
[11] A. Nagasawa, A. Kuwabara, Y. Morii, K. Fuchizaki, S. Funahashi, Mater. Trans. JIM
33 (1992) 203-207.
[12] L. Mañosa, J. Zarestky, T. Lograsso, D.W. Delaney, C. Stassis, Phys. Rev. B 48 (1993)
15708.
[13] J. Friedel, J. Phys. Lett. 35 (1974) 59-63.
[14] A. Planes, L. Mañosa, D.R. Jara, J. Ortín, Phy. Rev. B 45 (1992) 7633.
[15] L. Mañosa, A. Planes, J. Ortín, B. Martínez, Phys. Rev. B 48 (1993) 3611.
[16] A. Planes, L. Mañosa, E. Vives, Phys. Rev. B 53 (1996) 3039.
[17] C. Zener, Phys. Rev. 71 (1947) 846.
[18] J.R. Morris, R.J. Gooding, Phys. Rev. Lett. 65 (1990) 1769.
[19] A. Neogi, N. Mitra, Sci. Rep. 7 (2017) 7337.
[20] K. Schwarz, P. Blaha, G. Madsen, Comput. Phys. Commun. 147 (2002) 71-76.
[21] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[22] W. Kohn, L.J. Sham, Phys. Rev. 140 (1965) A1133.
[23] J.P. Perdew, A. Ruzsinszky, G.I. Csonka, O.A. Vydrov, G.E. Scuseria,
L.A. Constantin, X. Zhou, K. Burke, Phys. Rev. Lett. 102 (2009) 039902.
[24] Z. Wu, R.E. Cohen, Phys. Rev. B 73 (2006) 235116.
[25] A. Togo, F. Oba, I. Tanaka, Phys. Rev. B 78 (2008) 134106.
[26] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169-11186.
[27] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188-5192.
[28] F. Mouhat, F.-X. Coudert, Phys. Rev. B90 (2014) 224104.
[29] G.K.H. Madsen, D.J. Singh, Comput. Phys. Commun. 175 (2006) 67-71.
[30] F.D. Murnaghan, Am. J. Math. 49 (1937) 235.
[31] F. Birch, Phys. Rev. 71 (1947) 809.
[32] I.A. Morrison, M.H. Kang, E.J. Mele, Phys. Rev. B 39 (1989) 1575.
[33] M. Matsui, O.L. Anderson, Phys. Earth Planet. Inter. 103 (1997) 55.
[34] A.B. Belonoshko, R. Ahuja, B. Johansson, Nature 424 (2003) 1032.
[35] L. Vocadlo, D. Alfe, M.J. Gillan, I.G. Wood, J.P. Brodholt, G.D. Price, Nature 424
(2003) 536.
[36] M. Sternik, K. Parlinski, J. Chem. Phys. 123 (2005) 204708.
[37] A. Togo, L. Chaput, I. Tanaka, G. Hug, Phys. Rev. B 81 (2010) 174301.
[38] J.R. Chelikowsky, S.G. Louie, Quantum Theory of Real Materials, Kluwer, Boston,
1996, pp. 219-250.
[39] E.L. da Silva, J.M. Skelton, S.C. Parker, A. Walsh, Phys. Rev. B 91 (2015) 144107.
[40] J.M. Skelton, S.C. Parker, A. Togo, I. Tanaka, A. Walsh, Phys. Rev. B 89 (2014)
205203.
[41] J.P. Moore, D.L. McElroy, R.S. Graves, Can. J. Phys. 45 (12) (1967) 3849-3865.