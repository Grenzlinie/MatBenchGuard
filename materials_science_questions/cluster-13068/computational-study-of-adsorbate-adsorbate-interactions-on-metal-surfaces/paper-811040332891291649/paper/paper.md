![](./images/811040332891291649_1.jpg)

Surface Science 338 (1995) 169-182

![](./images/811040332891291649_2.jpg)

# The scattering of Ar from Ag(111): a molecular dynamics study

R.J.W.E. Lahaye $^{a,b,*}$, A.W. Kleyn $^{a}$, S. Stolte $^{b}$, S. Holloway $^{c}$

$^{a}$ FOM-Institute for Atomic and Molecular Physics, Kruislaan 407, 1098 SJ Amsterdam, The Netherlands
$^{b}$ Physical Chemistry and Laser Centre, Vrije Universiteit, De Boelelaan 1083, 1081 HV Amsterdam, The Netherlands
$^{c}$ Surface Science Research Centre, University of Liverpool, Liverpool L69 3BX, UK

Received 15 May 1995; accepted for publication 3 July 1995

## Abstract
A static potential energy surface (PES) for Ar-Ag(111), based upon the local density approximation, is tested in a molecular dynamics study. The PES is a pairwise additive potential and no potential parameters are optimized to fit experimental data. A large crystal with nearest neighbour interaction simulates the solid. Using this PES it is possible to describe the trends of the experimental data for thermal incidence energies (0.2-2.6 eV), including the transition from thermal to structure scattering. In addition we employ the potential for a broad range of incidence energies (0.01-100 eV) for a static surface and one with a surface temperature of 600 K. The high symmetry of a static surface results in the appearance of surface rainbows. At finite temperatures, all angular distributions are broadened and the rainbows disappear either due to the thermal vibrations of the surface (for low incidence energies), or due to their positional disorder (for high incidence energies). For low incidence energies, multiple collisions with the surface occur. The multiply colliding atoms do not grossly change the angular width. It is the effect of the thermal vibrations of the surface atoms that causes a large increase of the angular width for the low incidence energies. Sticking also occurs for low energies, an effect that strongly depends on the surface temperature. For high incidence energies scattering after penetration contributes to the distributions and sticking/implantation occurs.

Keywords: Atom-solid interactions, scattering, diffraction; Computer simulations; Low index single crystal surfaces; Molecular dynamics; Silver; Solid-gas interfaces

## 1. Introduction
From experimental data on gas-surface interactions it is rather difficult to extract a full description of the scattering dynamics. In special cases simple models can give insight in the underlying dynamics, but a full classical trajectory calculation makes it possible to study the dynamics of a wide range of experimental data. Since knowledge of the dynamics for even the simplest systems is incomplete, we present in this pa- per a classical trajectory study on a prototypical sys- tem, Ar scattering from Ag(111). For a wide range of incident Ar energies (0.01-100 eV), we will simulate the influence of the attractive potential on the dynam- ics and test the potential energy surface (PES) used in this work.

Generally, the energy range of an atomic beam can be divided into several regimes with respect to the well depth and the surface temperature. For incidence ener- gies exceeding the well depth $\varepsilon$ ($E_{\mathrm{i}} \gg \varepsilon$), direct scattering occurs having a single collision with the surface (one classical turning point). For lower energies when $E_{\mathrm{i}} \ll \varepsilon$ adsorption in the well occurs. The transition

* Corresponding author. Fax: +31 20 6684106; E-mail: kleyn@amolf.nl.

0039-6028/95/$09.50 © 1995 Elsevier Science B.V. All rights reserved
SSDI 0039-6028(95)00698-2

between these regimes where $E_{\mathrm{i}} \approx \varepsilon$ is the least studied and will be examined here. Another separation of the energy regime relates to the thermal energy of the surface atoms. For thermal scattering $(E_{\mathrm{i}} \leq k_{\mathrm{B}} T)$ the surface is rather smooth and tends to conserve parallel momentum. This has led to the introduction of the so-called cube models [1] for which a single mass represents the surface. The relative energy $E_{\mathrm{f}} / E_{\mathrm{i}}$ follows the curve of parallel momentum conservation:

$$
\frac{E_{\mathrm{f}}}{E_{\mathrm{i}}}=\frac{\sin ^{2} \theta_{\mathrm{i}}}{\sin ^{2} \theta_{\mathrm{f}}}, \tag{1}
$$

where $E_{\mathrm{i}}$ and $E_{\mathrm{f}}$ are the incidence and outgoing energy of the impinging atom and $\theta_{\mathrm{i}}$ and $\theta_{\mathrm{f}}$ are the incidence and outgoing angles with respect to the surface normal. Only perpendicular momentum can be transferred to the cube and this will uniquely determine the final angle $\theta_{\mathrm{f}}$. A spread in final scattering angles results from the differing transfer of normal momentum (e.g. due to thermal vibrations). This results in the typical curve of parallel momentum conservation (see, for example, Fig. 2).

When the incidence energy exceeds the thermal energy of the surface atoms $(E_{\mathrm{i}} \gg k_{\mathrm{B}} T)$ structure scattering will occur and the surface will appear like a rippled mirror [2] or even a lattice of isolated hard spheres. In these cases surface rainbows may be observed [3]. At energies above 100 eV we come into the regime usually reserved for low energy ion scattering, for which the dynamics is quite well understood [4-6]. The simplest collision model in this case is that of a (series of) hard sphere collisions. The relative energy for a binary collision between hard spheres is given by:

$$
\frac{E_{\mathrm{f}}}{E_{\mathrm{i}}}=\left[\frac{\sqrt{1-\left(\frac{m}{M}\right)^{2} \sin ^{2}\left(\theta_{\mathrm{i}}+\theta_{\mathrm{f}}\right)}-\frac{m}{M} \cos \left(\theta_{\mathrm{i}}+\theta_{\mathrm{f}}\right)}{1+\frac{m}{M}}\right]^{2}, \tag{2}
$$

where $m$ and $M$ are the masses of the two colliding hard spheres. The spread in final scattering angles now comes from the different impact parameters within a unit cell, resulting in the relative energy curve of the binary collision (see, for example, Fig. 2). In the transition regime $(E_{\mathrm{i}} \approx k_{\mathrm{B}} T)$ the scattering dynamics show an intermediate situation between Eqs. (1) and (2). The collective behaviour of the surface atoms requires a more elaborate model for the crystal, including many atoms, interactions between the crystal atoms and a phonon bath with finite temperature.

The PES, as proposed in an earlier paper by Kirchner et al. [7], is a fit to calculations with the local density approximation (LDA). The Ar interacts with a cluster of 10 and 19 Ag atoms describing an atop and centre site potential for Ar-Ag(111). These calculations show a short range repulsion with a small attractive well. An exponential fit to the data represents the repulsion, that has been shown to be very accurate for other systems in the energy range of 100 up to 5000 eV [5,8-10]. By design, it is impossible for LDA calculations to describe the inherently non-local van der Waals energy and therefore applications of LDA calculations are restricted to incidence energies where the attractive well is negligible. Lundqvist et al. [11] recently included the van der Waals interaction into the LDA calculations for rare gas diatoms, but this is not applicable for the more complex systems as Ar-Ag(111). However, the LDA calculations for Ar on Ag(111) have a well depth that is comparable with the van der Waals well of 0.1 eV [7,12]. The attractive well originates from the delocalized electrons at the surface and its main parameter is the distance $Z$ to the surface. An extra term in the total potential then takes account for the well and the influence of the delocalized electrons. We investigate the potential over a broad energy range and show that it is also applicable for low incidence energies.

We model the gas-surface scattering by molecular dynamics (MD) where the time dependence of the crystal is modeled by brute force, including nearest neighbour interaction in the force field for a large number of crystal atoms. A crystal of 3125 atoms simulates the heat bath of the solid. The advantage of such a large substrate is the possibility to trace atoms that make more than one collision with the surface [13]. The model provides a very simple and parameter free method for the thermal fluctuations of the solid. It has a disadvantage that it requires large amounts of computer time. The classical equations of motion describe the dynamics. Quantum effects are ignored because the de Broglie wavelength of the impinging atom is much smaller than the lattice constant of the crystal and the energy transfer will exceed the phonon bandwidth (typically 25-40 meV [14]). There is a special interest in multiple collision events, because experimentalists invoke these phenomena to explain unusual

energy transfer to the solid [15,16] and anomalous angular widths at low energies [17]. We show that those multiple collisions exist for Ar-Ag(111).

Gas-surface PES's have been developed for a vari- ety of systems and several energy regimes. Barker et al. [18] proposed an empirical potential for Xe- Pt(111), with assumptions to include the influence of the delocalized electrons at the surface. The poten- tial describes the adsorption as well as the scatteringdynamics very well for incidence energies up to 14.3 eV. However, the model does not provide a gen- eral method to derive a potential for other systems. Head-Gordon et al. [20] have also used an empiri- cal potential to describe trapping and desorption for Ar-Pt(111). For high energies (10-100 eV), ex- ponential fits to LDA calculations show that these fits are adequate for a number of systems (e.g. K- Ag(111), Na-Ag(111) [10], $Na^{+}-Cu(001)$ [5], $K^{+}-W(110)$ [21]).

We have chosen the Ar-Ag(111) system because a potential energy surface has been calculated for this system. Moreover, the system has been investigated recently by molecular beam scattering [22]. In ad- dition, the dynamics are expected to be rather sim- ple because the projectile's mass is less than half of the surface atoms. In the next sections we will treat in more detail the crystal, the PES and the numerical method used. We then compare the PES with experi- mental results and continue with a trajectory analysis for a much broader energy range (0.01-100 eV). The analysis shows the influence of the well depth, the de- pendence on the surface temperature and the occur- rence of multiple collisions with the surface. Finally the angular width and the sticking probability is in- vestigated in this energy range. All data shown here concerns the inplane scattering. Out-of-plane scatter- ing will be presented in a forthcoming paper.

## 2. The interaction potentials

### 2.1. The crystal

The crystal consists of 3125 atoms in a face-centred cubic lattice exposed to present a (111)-surface of25×25 atoms and 4 additional subsurface layers. The interaction between the crystal atoms is via a nearest neighbour, anharmonic potential. As a boundary con- dition the edge atoms are fixed to their equilibriumsites, except for those surface atoms lying in the z=0 plane. A crystal atom i feels the potential $V_{i}$ from itssurrounding nearest neighbours:

$$
\begin{aligned}
V_{i}= & \sum_{j \in\{N N\}} \frac{1}{2} k_{1}\left(r_{i j}-d\right)^{2}+\frac{1}{3} k_{2}\left(r_{i j}-d\right)^{3} \\
& +\frac{1}{4} k_{3}\left(r_{i j}-d\right)^{4},
\end{aligned}
$$

where {NN} is the ensemble of nearest neighbours of atom $i, r_{i j}$ is the distance between atom i and its j th nearest neighbour and the constant d is the nearest neighbour distance at equilibrium lattice positions (i.e. the lattice constant $4.09 \AA$ divided by $\sqrt{2}$ ). $k_{1}, k_{2}$ and k3 are the force constants.

In the harmonic approximation (for which $k_{2}=k_{3}=$ 0 ) the mean square displacement $< u^{2}>$ of a crystal atomand the force constant $k_{1}$ are [23-26]:

$$
\left\langle u^{2}\right\rangle=\frac{3 \hbar^{2} T}{M_{\mathrm{Ag}} k_{\mathrm{B}} \Theta^{2}}, \quad(3)
$$

$$
k_{1}=\frac{3}{8} M_{\mathrm{Ag}}\left(k_{\mathrm{B}} \Theta / \hbar\right)^{2}, \quad(4)
$$

where $M_{Ag}$ is the mass of an Ag atom, $\Theta$ is the Debye temperature, T is the temperature of the crystal and $k_{B}$ and $\hbar$ are Boltzmann's and Planck's constants, re spectively. The value of $\frac{3}{8}$ in Eq. (4) is used to obtain the correct value for the right mean square displace- ment of the bulk and surface atoms as described by Eq. (3). Since the Debye temperature is different for the bulk and the surface, all force constants connected to a surface atom are calculated with the surface De- bye temperature.

The harmonic description for the crystal is very good in the temperature regime used in this work, since the displacement of the crystal atoms from the equilibrium positions is rather small (about $0.3 \AA$ at600 K). A pure harmonic crystal has the disadvantage that different phonon modes of the lattice vibrations do not interact with each other. The anharmonic force constants $k_{2}$ and $k_{3}$ invoke the interactions between modes of lattice vibrations [26]. A Taylor expansion of a general Lennard-Jones potential [27] yields ap-proximate values of the anharmonic force constants:

$$
k_{2}=-\frac{21}{2 d} k_{1}, \quad(5)
$$

$$
k_{3}=\frac{371}{6 d^{2}} k_{1}. \quad(6)
$$

<table>
<caption>Table 1
The values of the Debye temperatures $\Theta$ [25,26] and the force constants $k_1$, $k_2$ and $k_3$ for the surface and the bulk</caption>
<thead>
<tr>
<th></th>
<th>$\Theta$
(K)</th>
<th>$k_1$
(eV/Å²)</th>
<th>$k_2$
(eV/Å³)</th>
<th>$k_3$
(eV/Å⁴)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Surface</td>
<td>104</td>
<td>0.7772</td>
<td>–2.8218</td>
<td>5.7459</td>
</tr>
<tr>
<td>Bulk</td>
<td>225</td>
<td>3.6379</td>
<td>–13.2077</td>
<td>26.8939</td>
</tr>
</tbody>
</table>

The relations in Eqs. (5) and (6) are independent of the actual values for $\sigma$ and $\varepsilon$ in the Lennard-Jones potential. The values of the force constants used in this work are listed in Table 1. The harmonic approach is erroneous for high energetic incident atoms, because the displacement of the surface atoms around the impact area is large due to the energy transfer (for 100 eV the displacement can be 4 Å). However, at these high energies the time scale of the interaction at the surface is so short that the impinging atom is already far away from the surface before the displacement of the surface atoms is large. Consequently, the influence of the enhanced displacement of the surface atoms is negligible on the scattering dynamics.

This model of the crystal does not include the quantum zero point vibrations of the crystal atoms. This is only of importance below the Debye temperature, and is of little significance for what follows. After completion of the calculations new force constants for Ag(111) have been published [28], that are somewhat higher. This would imply that our simulations have effectively been carried out for higher surface temperatures than listed. The effects are expected to be small.

### 2.2. The Ar-Ag(111) potential

We use the Ar-Ag(111) PES as calculated by Kirchner et al. [7]. The potential is based on a Born-Mayer fit to the LDA for an Ar-Ag diatom. Such a simple Born-Mayer potential fit has been shown to be very accurate in the higher energy range (100-5000 eV [5,8-10,29]), since at these energies all collisions with the surface reduce to simultaneous collisions or series of binary collisions with single crystal atoms. For lower incidence energies this is no longer the case. A previous approach was to take the Born-Mayer potential fit different for the first and the second layer atoms [21]. However, the LDA calculations, using clusters of 10 or 19 Ag atoms, show that the Born-Mayer potential fit needs a correction for the difference in repulsion at the atop and centre sites. This effect is attributable to the extra repulsion of the delocalized electrons at the surface and the correction is put into a Z-dependent potential connected to the surface atoms [18]. This potential describes also the well, that has its origin in the long range van der Waals attraction. However, the range of the attractive potential is not correct, for reasons that are described in the introduction.

To parameterize the PES as proposed by Kirchner et al., we use a summation of repulsive pair potentials and a Z-dependent global pair potential. This choice is motivated by a study on many body corrections for rare gas interactions that shows a strong linearity in the embedding functions [30], implying that the interaction is essentially pairwise. The Ar-Ag(111) interaction potential is a Born-Mayer repulsive pair potential $V_{BM}$ summed over all crystal atoms and the Z-dependent potential $V_Z$ is summed and weighted over all surface atoms:
$$
V_{\text{tot}}(\boldsymbol{R}) = \sum_{i \in \{C\}} V_{\text{BM}}(|\boldsymbol{R}_i|) + \sum_{i \in \{S\}} V_Z(\boldsymbol{R}_i) , \tag{7}
$$
with
$$
\boldsymbol{R}_i = \begin{pmatrix} X_i \\ Y_i \\ Z_i \end{pmatrix} = \boldsymbol{R} - \boldsymbol{r}_i ,
$$
$$
V_{\text{BM}}(\rho_i) = A \, \mathrm{e}^{-\alpha \, \rho_i} ,
$$
$$
V_Z(\boldsymbol{R}_i) = W(Z_i) \frac{\mathrm{e}^{-\sigma \left(X_i^2+Y_i^2\right)}}{\sum_{k \in \{S\}} \mathrm{e}^{-\sigma \left(X_k^2+Y_k^2\right)}} ,
$$
$$
W(Z_i) = -B \left(Z_i - z_0\right) \mathrm{e}^{-\gamma \, Z_i^4} .
$$

The vectors $\boldsymbol{R}$ and $\boldsymbol{r}_i$ are the positions of the Ar atom and the $i$th crystal atom respectively, $\{C\}$ is the ensemble of all crystal atoms and $\{S\}$ the ensemble of all surface atoms. $Z_i$ is the Z-distance between the Ar atom and the $i$th crystal atom, determining the value of $W$. $X_i$ and $Y_i$ are used to weight the contribution of $W(Z)$ over the surface atoms. The functional forms of $V_{\text{BM}}$ and $W$ as well as the parameter values are the same as in the work of Kirchner: $A = 10608.0$ eV, $\alpha = 4.2487$ Å⁻¹, $B = 1.28$ eV Å⁻¹, $z_0 = 2.6$ Å and $\gamma = 0.0183$ Å⁻⁴.

![](./images/811040332891291649_3.jpg)

Fig. 1. The upper two panels show the contour plots of the Ar-Ag(111) potential energy surface along two azimuth orientations of the surface. $X$ is the line along the surface and $Z$ is the height to the surface plane. Distances are in ångström and the contour values in electronvolts. Underneath a small surface unit cell is drawn to indicate the two azimuth orientations.

Since for the LDA calculations all atoms are at rest in the equilibrium positions $r_{i}^{0}$, the potential has to be augmented for dynamical trajectory calculations, where the energy is required for arbitrary lattice positions $r_{i}$. In the fit of Kirchner, $W(Z)$ is independent of the individual $Z$-coordinates of the surface atoms, preventing the Ar from losing any energy to the lattice. This is incorrect and we remedy this by attaching $W(Z)$ to the surface atoms. The range parameter $\sigma$ determines how the surface atoms contribute to this potential. The further away in the $XY$-plane, the less the contribution is. $\sigma$ is $0.149 \mathring{A}^{-2}$ and is such that about 10 surface atoms contribute to $V_{Z}$ which is quite reasonable for Ar and $Ag(111)$. Changing $\sigma$ by 10% does not affect the results significantly. Barker et al. [18] made a similar assumption with a value of $\sigma = 0.22 \mathring{A}^{-2}$ for $Ar-Pt(111)$. Note that when the surface atoms are in their lattice equilibrium positions, $\sum_{i \in \{ S \}} V_{Z}(R_{i})$ equals $W(Z)$ of the static fit to the LDA calculations of Kirchner.

The total potential has a well depth of 0.098 eV for the atop site at a distance of $3.17 \mathring{A}$ above the surface and 0.1 eV for the centre site at $3.12 \mathring{A}$. Fig. 1 shows a contour plot of the PES for two directions along the surface.

### 3. Numerical method

The classical equations of motion are numerically solved, using the velocity Verlet integration method [31-33]. The integration time step depends on the incidence energy, and the total energy is conserved within 0.1 percent over the entire trajectory for all incidence energies. The time step varies from 0.23 fs for 200 eV to 6.3 fs for 0.03 eV. In the case of a static surface, 10000 atoms are scattered for a single data set with the impact parameters systematically scanned over the surface unit cell. For the finite temperature, about 30000 atoms are scattered per data set and a random number generator [34] yields the impact parameters in the surface unit cell. The same random number generator yields the values for the Boltzmann distribution for the velocities of the crystal atoms. Initially the crystal atoms are set to their equilibrium positions. In order to get a surface temperature of 600 K, a Boltzmann velocity distribution of 1200 K is used followed by a thermalization. During the thermalization half of the kinetic energy flows into potential energy, resulting in a surface temperature of 600 K. We have verified that the anharmonic terms in the crystal potential have no significant influence on the thermalization process.

The Ar atoms start their trajectory from a height of 5.25 Å above the surface, where the potential is less than $10^{-5}$ eV. The trajectory calculations are determined when an Ar atom either:
(1) appears again at 5.25 Å above the surface,
(2) approaches within a distance of 5 atoms from the edge of the crystal, or
(3) makes more than 10 collisions with the surface.
The first criterion determines the class of atoms that are directly and indirectly inelastically scattered. The second criterion prevents the Ar "falling off the edge" of the crystal and the third criterion sets a time limit to trace atoms that make multiple collisions with the surface. When the velocity in the Z-direction changes sign it is registered as a turning point in the trajectory. A single turning point implies a single collision with the surface, three turning points two collisions with the surface etc. The last two criteria also contain those atoms that are considered to be trapped on the surface.

---

### 4. Comparison with experiment

Our first task is to test the PES as given in Section 2.2 against experimental data. A set of experiments [22] for several incidence energies and surface temperatures for an Ar beam through $40^{\circ}$ incidence angle will be compared with our MD simulation. The experimental data set has an incidence energy range of $0.2<E_{\mathrm{i}}<2.6$ eV for a surface temperature of 600 K. For $E_{\mathrm{i}}=1.0$ eV the surface temperature is varied from 330 to 800 K. The scattering azimuth in the experiments is unknown and only in-plane scattered atoms are detected. The simulations scatter the atoms along the $[10 \overline{1}]$ direction and the detector is simulated by an in-plane window subtending $7.6 \times 10^{-3}$ sterrad at the surface. Fig. 2 shows the relative energies $E_{\mathrm{f}} / E_{\mathrm{i}}$ and some intensity distributions for the experimental data and the simulations.

For $E_{\mathrm{i}}=0.2$ eV the relative energy follows the trend of parallel momentum conservation as described by Eq. (1). In this regime of thermal scattering, the surface appears to be quite flat and atoms scattering at lower $\theta_{\mathrm{f}}$ gain translational energy from the (vibrating) surface atoms. However, the simulations do not converge exactly to the curve of parallel momentum conservation, because a small lateral corrugation always persists even for the low incidence energies (see Sections 5.1 and 5.2). Increasing the incidence energy to 0.5 eV, the relative energy curve starts to deviate from parallel momentum conservation particularly at low exit angles. This indicates the transition to structure scattering arising from the increased lateral corrugation. For $E_{\mathrm{i}}=1$ and 2.6 eV the relative energy changes towards the shape that is characteristic for hard sphere collisions as described by Eq. (2). Both experimental data and simulations show that the surface in this energy range behaves in between the cube and the hard sphere collision model.

Intensity distributions broaden with increasing temperature, as seen in the lower panels of Fig. 2, although the relative energy is basically unaffected by the surface temperature. The angular widths of the intensity distributions shown in Fig. 7 indicate that the simulations indeed capture the experimental trends, with a minimum around 1 eV.

Although the overall experimental trends are well reproduced by simulations and this PES, the absolute results are overall too high in final energy and the peak

![](./images/811040332891291649_4.jpg)

Fig. 2. Comparison between average final energy distributions and angular flux distributions from experiments [22] and simulations for in-plane scattering of Ar from Ag(111). The incidence angle is $40^{\circ}$. Angles are measured with respect to the surface normal.

in the intensity distribution is shifted towards the sur- face normal. The calculated width as function of the energy, is overestimated, but shows qualitative agree- ment with the experimental data. Deviations are due to the fact that the $Z$-dependent potential in Eq. (7) is not quite right. Since the PES is deduced from the LDA calculations, no parameter have been optimized to fit the experimental data, leading to the conclusion that the pairwise LDA description accounts for the ex- perimental trends quite adequately.

## 5. Collision dynamics

### 5.1. Scattering distributions for a static surface

In addition to the PES it is the motion of the surface atoms, due to the finite temperature, that will deter- mine the trajectory of an impinging atom. Often the surface motion blurs sensitive features of the potential and mixes the lateral and thermal corrugation [19]. To discriminate against the thermal effects, we start to analyse the collision dynamics for a "static" surface. In this model the crystal atoms are set initially to their equilibrium positions, with no vibrational energy, but still interact via the potential field of Eq. (3). This effectively allows the crystal to carry away energy by recoiling following impact by the incident Ar atom. The more corrugated the PES, the wider is the spread in $\theta_{f}$. Selecting a constant energy, the PES shows a sine-wave-like surface to the incident atom, leading to surface rainbows [35] in the scattering distribu- tions. For such a static surface there is also a clear distinction between scattered and trapped atoms, be- cause once trapped in the well an atom can not escape on the timescale of the simulation.

One should keep in mind that all simulations are done for the incidence angle of $40^{\circ}$ and only scattered atoms in-plane contribute, simulating a detector with a finite acceptance angle. Figs. 3a and 3b show the results for a static crystal.

The "perpendicular" energy for 0.1 eV is rather low $(E_{i} \cos ^{2} \theta_{i} \approx 0.06 eV)$ and the atoms will be ac celerated considerably by the well depth, that leads to a high energy loss and the low value of $E_{f} / E_{i}$ in Fig. 3a. The incident atom is also refracted on enter- ing the well [36]. Atoms that escape, also have to pass through the well before they leave the surface. On their outward journey, the well refracts the atoms towards the surface and the intensity distribution in Fig. 3b shows this shift towards the surface. Moreover, the intensity distribution shows three peaks. The out- ermost peaks are surface rainbows, due to the (small) lateral corrugation of the well.

For $E_{i}=1.0 eV$ the PES is still rather smooth (see Fig. 1), but now the influence of the well vanishes. No extra energy loss or refraction affects the scattered atoms and therefore the relative energy in Fig. 3a is high (0.7-0.8) and the direction of the main peak in the intensity distribution is about $45^{\circ}$. The peaks in the

![](./images/811040332891291649_5.jpg)

Fig. 3. Simulations for in-plane scattering of Ar from Ag(111) with an incidence angle of $40^{\circ}$, measured with respect to the surface normal. (a) and (b) belong to a static surface, (c) and (d) to 600 K.

intensity distribution come from scattering at different impact points in the surface unit cell, as previously reported by [37]. The outermost (rainbow) peaks, just before the intensity drops to zero, consist of atoms scattered from the surroundings of the atop site (the "up-hill' potential surface scatters in low exit angles and the "down-hill' scatters in the high exit angles). The central peak of the distribution (at $\theta_{\mathrm{f}}$ between $40^{\circ}$ and $50^{\circ}$ ) consists mainly of centre site scattering and a small number of atop scattering events. The central peak itself shows a splitting into two peaks. Atoms make zig-zag collisions through the centre site to scatter in-plane and the small difference in focusing by the up-hill and down-hill potential at the centre site gives rise to the splitting of the central peak. At these outgoing angles $(40^{\circ}-50^{\circ})$ there is also a kink in the relative energy due to the lower energy loss at the centre sites.

For $E_{\mathrm{i}}=10 \mathrm{eV}$ the relative energy decreases due to the ability of the more energetic atoms to penetrate the surface to a greater extent. Fewer surface atoms contribute to the repulsion at the turning point, so the effective mass driven by the repulsive force is smaller, leading to a higher energy transfer. The increase of the lateral corrugation causes a broader distribution in $\theta_{\mathrm{f}}$ and the intensity distribution shows again four peaks, similar to the $1 \mathrm{eV}$ distribution. The two leftmost peaks, originating from scattering at the up-hill potential, shift with incidence energy whereas the two right peaks (at $45^{\circ}$ and $55^{\circ}$ ), arising from the downhill potential, do not shift with energy. A collision with the down-hill potential is a grazing interaction and the impinging atom will be scattered along the surface, subsequently making a second collision with the surface atom and finally emerging from the surface. Such a collision with two surface atoms compensates the difference in shape of the potential for different energies. Therefore scattering from the down-hill potential tends to make $\theta_{\mathrm{f}}$ independent of the incidence energy. However, a collision with the up-hill potential is a more head-on collision with a surface atom and the impinging atom is reflected by a collision with a single crystal atom. It is therefore the shape of the PES that determines the outgoing angle and how the peaks shift with the incidence energy.

For incidence energies of $100 \mathrm{eV}$ the scattering dynamics is described quite well by the binary collision model. Direct scattering only occurs in the neighbourhood of the atop site because atoms impinging between the surface atoms penetrate into the crystal. That scattering from atop collisions dominates, is also confirmed by the intensity distribution where only peaks arising from atop collisions survive. For low $\theta_{\mathrm{f}}$ the atoms undergo a single binary collision with a surface atom and therefore the relative energy follows the curve of the binary collision model. However, at these low $\theta_{\mathrm{f}}$ there is an additional contribution from atoms leaving the surface after penetration, resulting in an average relative energy slightly lower than the binary collision model predicts. For higher exit angles the impinging atoms make successive collisions with two surface atoms, equivalent to a pair of grazing, binary zig-zag collisions with an energy loss that is lower than that for a single binary collision [38].

![](./images/811040332891291649_6.jpg)

Fig. 4. The angular intensity distributions for in-plane scattering of Ar from Ag(111) with an incidence angle of $40^{\circ}$ and two incidence energies: 0.1 eV and 1 eV. "600 K frozen" means a displacement of the crystal atoms corresponding to 600 K, without thermal energy. The corresponding widths are drawn in the inset.

All simulations were performed along the $[10 \overline{1}]$ azimuth. For the low energies of 0.1 and 1 eV the influence of the crystal orientation is negligible, but for the higher energies of 10 and 100 eV the peak intensities and positions change with azimuth. The influence of the crystal orientation has been studied extensively in experiments and theoretical calculations for ion scattering [10,21,38,39] but will not be discussed here.

### 5.2. Finite temperature effects

The features appearing for a static crystal change radically once the surface acquires a finite temperature. This has two broad effects on the surface atoms: firstly, the crystal atoms are in general displaced from their equilibrium positions, and secondly, the atoms vibrate with the thermal energy around their equilibrium positions. Which of these dominates the dynamics depends on the incidence energy. For high energies, the collision time is rather short, the impinging atom sees a snap shot of a "frozen" crystal and only the static displacement of the surface atoms is important. For low incidence energies the collision time is longer and the impinging atom experiences vibrations in the surface atoms, resulting in a gain of translational energy at low $\theta_{\mathrm{f}}$ and extra energy loss at high $\theta_{\mathrm{f}}$.

For example, at $T_{\mathrm{s}}=600 \mathrm{~K}$ the thermal energy per surface atom is about $78 \mathrm{meV}\left(\frac{3}{2} k_{\mathrm{B}} T\right)$ and the mean displacement about $0.3 \AA$ (Eq. (3)). A crystal with no thermal energy, but with the atoms displaced corresponding to a 600 K distribution will give a feeling for the effects of the displacement alone. Fig. 4 compares a so called frozen crystal with a "normal" crystal of 600 K and a static one, for two incidence energies, 0.1 and 1 eV, of an Ar beam impinging through an angle of $40^{\circ}$. The rainbow peaks, arising for the static crystal, disappear for the frozen 600 K one. Therefore, for both energies, the displacement is enough to wash out the rainbow peaks. For $E_{\mathrm{i}}=0.1 \mathrm{eV}$, the displacement of the surface atoms causes a shift of the angular distribution towards the surface normal and this shift increases when the thermal vibrations are included. For 1 eV, such a shift is as good as absent. The increase of the angular width by the displacement of the surface atoms is for both incidence energies the same, as shown in the inset of Fig. 4. However, the thermal vibrations are more dominant for 0.1 eV than for 1 eV. Increasing the incidence energy will even more reduce the influence of the thermal vibrations.

The influence of a 600 K surface is shown in Figs. 3c and 3d. The relative energy curves show the validity of the cube models (Eq. (1)), with parallel momentum conservation for the lowest $E_{\mathrm{i}}$ and the binary collision model (Eq. (2)) describing the higher energy data. The relative energy curve of 0.1 eV now shows the trend to conserve parallel momentum, in contrast to the static surface case. The motion of the surface atoms smoothes the PES, such that the surface appears relatively flat. The acceleration into the well results in an exchange between parallel and perpendicular momentum, which in turn results in a slight deviation from the cube model. Comparing results with those from

a static surface, we see that now the scattered atoms gain translational energy from the surface atoms and the thermal energy of the surface atoms broadens the intensity distribution with the centroid shifted towards the surface normal.

For the higher energies in Fig. 3c, the conservation of parallel momentum in the scattering event breaks down since the lateral corrugation increases. For 1 and 10 eV we are in a regime in between the parallel momentum conservation and the binary collision model. Increasing the incidence energy further up to 100 eV reduces the dynamics to simple binary collisions.

Comparing Figs. 3b and 3d makes it clear that the influence of the surface temperature is not limited to the low incidence energy range. Even for 10 eV and 100 eV the lattice motion breaks the symmetry of the PES, the scattering distributions broaden and the rainbow peaks disappear.

### 5.3. Multiple collisions

For $\theta_{\mathrm{i}}=40^{\circ}$ the incidence energy splits up into a "perpendicular" component $(E_{\mathrm{i}} \cos^{2}40^{\circ}=0.59\ E_{\mathrm{i}})$ and a "parallel" component $(E_{\mathrm{i}} \sin^{2}40^{\circ}=0.41\ E_{\mathrm{i}})$, according to the components of the momentum vector. An atom makes multiple collisions with the surface if it transfers enough perpendicular energy to the solid that it can not escape out of the potential. An atom may finally escape by gaining perpendicular energy from a (vibrating) surface atom or by transferring parallel energy into perpendicular energy. During the MD simulation, every sign change of the Ar velocity in the Z-direction has been registered as a turning point. One turning point corresponds to a single collision, three turning points to a double collision and so forth.

For incidence energies below 1.0 eV a considerable number of atoms hop along the surface before scattering away. In this energy range the probability of multiple collisions depends on the crystal temperature. In the limit of a static surface, atoms make no multiple collisions: they either escape after a single collision or they are trapped into the well for the duration of the simulation. The probability for multiple collisions decreases for lower crystal temperatures as shown in Fig. 5 for $E_{\mathrm{i}}$=0.5 and 0.03 eV. For 0.03 eV the total contribution of multiple collisions for in-plane scattering is 12% for 200 K whereas for 600 K it is 25%.

![](./images/811040332891291649_7.jpg)

Fig. 5. Probability of multiple collisions for in-plane scattering of Ar from Ag(111). The incidence angle is $40^{\circ}$, with respect to the surface normal.

The perpendicular energy accommodation at the surface is very fast (within 2 or 3 collisions with the surface), but the parallel energy is more or less conserved on the time scale of the multiple collisions [20,13]. Since the escape mechanism at these low energies is due the to thermal vibrations of the surface atoms, the atoms escape with a broad distribution. This is shown in Fig. 6a, where the contributions to the total distribution arising from single and multiple collisions are plotted separately. Though atoms suffering multiple collisions need longer to escape than those directly scattered, the time difference is too small to separate the contributions experimentally. Therefore it is plausible to assume that in the experiments a mixture of atoms with single and multiple collisions will be measured in the detector.

The probability for multiple collisions with the sur-

![](./images/811040332891291649_8.jpg)

Fig. 6. Angular intensity distributions for in-plane scattering of Ar from Ag(111) and a surface temperature of 600 K. The multiple collisions are the collection of scattered atoms with more than one collision with the surface. The total distribution is the sum over the single collision and the multiple collisions.

face depends also on the incidence energy as shown in Fig. 5. For energies below the well depth ($\varepsilon = 0.1$ eV) the atoms get trapped in the well, but can either escape by an encounter with a fast moving surface atom or by the transfer of parallel into perpendicular momentum in a collision with a surface atom severely displaced from its equilibrium position. Increasing $E_{\mathrm{i}}$ will negate the influence of the well and the motion of the surface atoms and more atoms will make a single collision with the repulsive wall of the PES. Fig. 6b shows nicely how the contribution from multiple collisions vanishes at 0.5 eV. However, at high energies, atoms penetrate into the crystal at the centre and bridge sites. A simultaneous interaction with two or three surface atoms causes a high energy loss (in the order of 90%) while penetrating the surface layer [40]. This large energy transfer to the surface atoms makes the crystal locally very hot. These highly energetic surface atoms may, in turn, eject the Ar from the surface through low $\theta_{\mathrm{f}}$ following an inelastic event and scattering away. Sign changes in the velocity of a subsurface atom are counted as multiple collisions. The probability for a single collision and subsurface multiple collisions for $E_{\mathrm{i}} = 100$ eV is shown in Fig. 5. Fig. 6c shows that for 100 eV, the multiply colliding atoms scatter towards the surface normal and the singly colliding atoms have a much broader distribution.

## 6. Incidence energy dependence of the angular width

Fig. 7 shows the angular width as function of the incidence energy for the recently obtained experimental data [22]. The width goes through a minimum around 1 eV. Other systems, like Ar-W(100) and $\mathrm{N}_{2}-$ W(100) [17] show a similar behaviour. The increase of the width for the higher energies can be understood in terms of an increase of the surface corrugation due to the PES (structure scattering), but a convincing explanation for the trend in the low energy range (between 0.1 and 1 eV) has yet to appear. Suggestions in the literature include multiple collisions and/or thermal induced roughness of the surface via the vibrations of the surface atoms. While both effects are present (but not distinguishable) in experiments, MD calculations allow these to be separated quite easily in the analysis.

Let us first switch off the thermal part of the problem and investigate the width for a static surface with recoil. The intensity distributions are non-Gaussian (see Fig. 3b) and the angular width is then best defined using the first and second moments of the intensity distribution:

$$
2 \Delta \theta_{\mathrm{f}}=2 \sqrt{\left\langle\theta_{\mathrm{f}}^{2}\right\rangle-\left\langle\theta_{\mathrm{f}}\right\rangle^{2}}, \tag{8}
$$

with

$$
\left\langle\theta_{\mathrm{f}}^{n}\right\rangle=\frac{\int_{0}^{\pi / 2} \theta_{\mathrm{f}}^{n} I\left(\theta_{\mathrm{f}}\right) \mathrm{d} \theta_{\mathrm{f}}}{\int_{0}^{\pi / 2} I\left(\theta_{\mathrm{f}}\right) \mathrm{d} \theta_{\mathrm{f}}},
$$

where $\theta_{\mathrm{f}}$ is the outgoing angle and $I(\theta_{\mathrm{f}})$ is the intensity distribution. The width, $2 \Delta \theta_{\mathrm{f}}$, is for a Gaus-

![](./images/811040332891291649_9.jpg)

Fig. 7. The angular width of the intensity distribution, defined in Eq. (8), as function of the incidence energy. The incidence angle is $40^{\circ}$ with respect to the surface normal.

sian distribution equal to the full width at half maximum (FWHM). The angular width for a static surface, shown in Fig. 7, also has a minimum around 1 eV. As this indicates, there is only a small increase of the angular width below 1 eV. For the low energy range the atoms feel only the influence of the well, since the surface atoms have no thermal vibrations and multiple collisions do not occur (atoms either make single collisions or get trapped). The influence of the well is not enough to explain the experimental data. Obviously thermal effects are necessary to provide a better understanding of the trend in the angular width.

The influence of the surface temperature on the angular width is also shown in Fig. 7 for simulations at 600 K. For the low incidence energies, the increase of the width is very large and the trend of the experimental data set is nicely reproduced. Besides a roughening via the thermal vibrations of the surface, for the low incidence energies the finite temperature introduces multiple collisions of the Ar with the surface.

Figs. 6a and 6b show the contribution of the multiple collisions to the angular distribution for $E_{\mathrm{i}}=0.03 \mathrm{eV}$ and 0.5 eV. For 0.03 eV the number of multiple collisions adds up to about 25%. However, the multiple collision events increase the angular width by less than 1 degree. The difference in the angular width for a static surface and a 600 K one at these energies is 20 degrees. From this we conclude that thermal vibrations of the surface atoms give the main contribution to the increase of the width at low incidence energies. The influence from the multiple collisions is much less, although they do occur with a considerable probability at low energies.

For 0.5 eV we see in Fig. 6b that the contribution of multiple collisions vanishes, though the angular width increases with about 20 degrees compared to a static surface. In this case thermal vibrations must increase the angular width.

As expected, the higher the incidence energy, the less is the influence of the thermal vibrations. For incidence energies above 20 eV (with an incidence angle of $40^{\circ}$) the influence of the surface temperature is negligible.

![](./images/811040332891291649_10.jpg)

Fig. 8. The sticking probability for Ar on Ag(111) for several surface temperatures as function of the incidence energy. The incidence angle is $40^{\circ}$.

### 7. Sticking and implantation

Sticking is used for those atoms that do not leave the surface on the time scale of the experiment. If the atoms desorb within that time scale, the particles were trapped at the surface. The time scale on which atoms desorb from the surface (typically a microsecond) is impossible to trace with MD calculations that use time steps in the order of femtoseconds. One needs to make assumptions to deem the atom to be stuck at the surface and terminate the trajectory calculation accordingly. Head-Gordon et al. [20] list several alternatives based on the energy accommodation at the surface and the surface temperature, but the appearance of multiple collisions makes an acceptable definition for sticking

ing difficult. Atoms move along the surface and still can leave the surface after several collisions within a relatively short time scale. To keep sticking as simple as possible, we define sticking for those atoms that do not escape from the surface during the time scale of the trajectory calculation. This means that sticking occurs for atoms that hop along the crystal surface until they reach the edge of the crystal or they make more the 10 collisions with the surface. At high in- cidence energies atoms penetrate into the crystal and those, that find no way out of the crystal, stick. This simple assumption for sticking results in the sticking probability as shown in Fig. 8.

Below 1 eV the sticking probability shows a strong temperature dependence. No experimental data for the sticking of Ar on Ag(111) is available, but the sticking data for Ar-Pt(111) show a similar behaviour in this energy regime [20]. Above 1 eV the sticking proba- bility is at first zero. Above 20 eV the energy is high enough that atoms penetrate into the crystal and trans- fer most of their incidence energy to the crystal atoms. This gives rise to sticking/implantation for high en- ergies. Now there is no temperature dependence since the incidence energy exceeds by far the thermal energy of the crystal atoms. It may be obvious that this stick- ing/implantation phenomenon happens at the centre and bridge sites on the surface, which makes the pro- cess site dependent [10].

## 8. Conclusion

With a large scale molecular dynamics simulation, we have tested a potential for Ar on Ag(111). This interaction potential is based upon the local density approximation for an Ar atom approaching a cluster of Ag atoms. For incidence energies $0.2 < E_{\mathrm{i}} < 2.6$ eV, both experimental data and the simulations show the transition from thermal scattering into structure scat- tering. In addition the angular distributions and the corresponding widths are nicely in accord with the experimental data. Special attention is paid to the un- usual increase of the angular width for low incidence energies. Though multiply colliding atoms have a rela- tively high contribution to the scattering, it is the ther- mal vibrations of the surface atoms that induce the large spread in the angular distributions.

For an extended energy regime up to 100 eV, the in- fluence of a finite temperature is investigated by com- paring the results of a static surface with one at a sur- face temperature of 600 K. The static surface has no thermal vibrations and consequently the impinging Ar atom can not gain translational energy from surface atoms. This strongly affects the dynamics at low inci- dence energies and we demonstrate that parallel mo- mentum conservation does not hold for the static sur- face. For a static surface, the crystal atoms are initially in their equilibrium positions and this highly ordered arrangement gives rise to the appearance of surface rainbows. These rainbows disappear at finite temper- atures. The influence of the thermal vibrations of the surface atoms on the scattering dynamics decreases for higher incidence energies, but then it is the displace- ment of the surface atoms that affects the angular dis- tributions tending to wash out the surface rainbows. For incidence energies of 100 eV we also see scatter- ing after penetration into the solid. Those atoms scatter preferentially towards the surface normal. The stick- ing probability shows a strong dependence on both the incidence energy and the surface temperature.

## Acknowledgements

This work is part of the research program of the "Stichting voor Fundamenteel Onderzoek der Ma- terie" (FOM), that is financially supported by the "Nederlandse Organisatie voor Wetenschappelijk On- derzoek" (NWO). The collaboration between Ams- terdam and Liverpool is supported by the E.C. Science Program ERBSCI*CT910721. All calculations have been performed on an 8 node SP1 system from IBM installed at the Academic Computing Services Ams- terdam (SARA). We thank SARA, the University of Amsterdam, the "Vrije Universiteit" in Amsterdam, the "Stichting Mathematisch Centrum" and IBM Netherlands for providing access to the system.

## References

[1] E. Grimmelmann, J. Tully and M. Cardillo, J. Chem. Phys. 72 (1980) 1039.
[2] J. Tully, J. Chem. Phys. 92 (1990) 680.
[3] A. Kleyn and T. Horn, Phys. Rep. 199 (1991) 191.
[4] D. Adler and B. Cooper, Phys. Rev. B 43 (1991) 3876.
[5] B. Cooper, C. DiRubio, G. Kimmel and R. McEachern, Nucl. Instrum. Meth. Phys. Res. B 64 (1992) 49.

[6] H. Winters, H. Coufal, C. Rettner and D. Bethune, Phys. Rev. B 41 (1990) 6240.

[7] E. Kirchner, A. Kleyn and E. Baerends, J. Chem. Phys. 101 (1994) 9155.

[8] D. Goodstein, R. McEachern and B. Cooper, Phys. Rev. B 39 (1989) 13129.

[9] P. van den Hoek, A. Tenner, A. Kleyn and E. Baerends, Phys. Rev. B 34 (1986) 5030.

[10] T. Horn, P. Haochang, P. van den Hoek and A. Kleyn, Surf. Sci. 201 (1988) 573.

[11] B. Lundqvist, Y. Andersson, H. Shao, S. Chan and D. Langreth, Int. J. Quantum Chem. in press.

[12] N. Lang, Phys. Rev. Lett. 46 (1981) 842.

[13] R. Smith, A. Kara and S. Holloway, Surf. Sci. 281 (1993) 296.

[14] J. Harris, Mechanical Energy Transfer in Particle-Surface Collisions (The Royal Society of Chemistry, Cambridge, 1990) ch. 1, p. 35.

[15] F. Geuzebroek, A. Wiskerke, M. Tenner and A. Kleyn, J. Phys. Chem. 95 (1991) 8409.

[16] A. Wiskerke, C. Taatjes, A. Kleyn, R. Lahaye, S. Stolte, D. Bronnikov and B. Hayden, Chem. Phys. Lett. 216 (1993) 93.

[17] C. Rettner and E. Schweizer, Surf. Sci. 203 (1988) L677.

[18] J. Barker and C. Rettner, J. Chem. Phys. 97 (1992) 5844, see also Ref. [19]).

[19] J. Barker and C. Rettner, J. Chem. Phys. 101 (1994) 9202.

[20] M. Head-Gordon, J. Tully, C. Rettner, C. Mullins and D. Auerbach, J. Chem. Phys. 94 (1991) 1516.

[21] A. Tenner, R. Saxon, K. Gillen, D. Harrison, Jr., T. Horn and A. Kleyn, Surf. Sci. 172 (1986) 121.

[22] A. Raukema, R. Dirksen and A. Kleyn, Probing the (dual) repulsive wall in the interaction of oxygen, nitrogen and argon with the Ag(111) surface, J. Chem. Phys., submitted.

[23] L. Feldman and J. Mayer, Fundamentals of surface and thin film analysis, 1st ed. (Elsevier, Amsterdam, 1986) ch. 7.3, pp. 158-160.

[24] A. Maradudin, E. Montroll, G. Weiss and I. Ipatova, Theory of Lattice Dynamics in the Harmonic Approximation, in: Solid State Physics: Advances in Research and Applications, Eds. H. Ehrenreich, F. Seitz and D. Turnbull (Academic Press, London, 1971) ch. VII.2, p. 310.

[25] G. Somorjai, Chemistry in Two Dimensions: Surfaces, 1st ed. (Cornell University Press, Ithaca, NY, 1981) ch. 4, pp. 169-170.

[26] G. Somorjai, Introduction to Surface Chemistry and Catalysis, 1st ed. (Wiley, New York, 1994) ch. 4.2.3, pp. 319-324.

[27] N. Ashcroft and N. Mermin, Solid State Physics (Sauders College, Philadelphia, PN, 1976) ch. 20, pp. 398-400.

[28] P. Statiris, H. Lu and T. Gustafsson, Phys. Rev. Lett. 72 (1994) 3574.

[29] P. van den Hoek, A. Kleyn and E. Baerends, Comm. Atomic Mol. Phys. 23 (1989) 93.

[30] J. Nørskov, Rep. Prog. Phys. 53 (1990) 1253.

[31] L. Verlet, Phys. Rev. 159 (1967) 98.

[32] S. Koonin, Computational Physics, 1st ed. (Benjamin/Cummings, Menlo Park, CA, 1986) ch. 3.1, pp. 50-51.

[33] M. Allen and D. Tildesley, Computer Simulations of Liquids (Oxford University Press, New York, 1987) ch. 3.2.1, pp. 78-82.

[34] M. Allen and D. Tildesley, Computer Simulations of Liquids (Oxford University Press, New York, 1987) Appendix G, pp. 347-349.

[35] T. Horn, A. Kleyn and B. Dijkhuis, Chem. Phys. 149 (1991) 275.

[36] J. Harris, A. Liebsch, G. Comsa, G. Mechtersheimer, B. Poelsema and S. Tomoda, Surf. Sci. 118 (1982) 279.

[37] J. Barker, D. Dion and R. Merrill, Surf. Sci. 95 (1980) 15.

[38] A. Tenner, K. Gillen and A. Kleyn, Nucl. Instrum. Meth. Phys. Res. B 17 (1986) 108.

[39] U. van Slooten, O. Teodoro, A. Kleyn, J. Los, D. Teillet- Billy and J. Gauyacq, Surf. Sci. 179 (1994) 227.

[40] R. Lahaye, S. Stolte, A. Kleyn, R. Smith and S. Holloway, Surf. Sci. 307 (1994) 188.

[41] M. Allen and D. Tildesley, Computer Simulations of Liquids, 1st ed. (Oxford University Press, New York, 1987).