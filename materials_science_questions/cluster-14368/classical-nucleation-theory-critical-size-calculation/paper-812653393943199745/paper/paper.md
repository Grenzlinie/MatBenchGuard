# Breakdown of the Capillarity Approximation in Binary Nucleation: A Density Functional Study†

Ari Laaksonen*,‡ and Ismo Napari§

Department of Applied Physics, University of Kuopio, P.O.Box 1627, Kuopio, Finland 70211, and
Department of Physics, University of Helsinki, P.O. Box 64, Helsinki, Finland 00014

Received: May 1, 2001; In Final Form: August 7, 2001

The binary classical nucleation theory is known to produce unphysical predictions of gas−liquid nucleation in systems in which the surface tension has a strong composition dependence. It has been shown earlier, using thermodynamic methods, that the unphysical predictions are related to the capillarity approximation, i.e., the assumption that the critical nucleus surface tension equals the surface tension of a flat interface. In this paper, we apply the density functional theory of nucleation to a surface active system and show by numerical calculations that the capillarity approximation breaks down severely for critical nuclei of intermediate composition. In these nuclei, the concentration profile of the surface active component shows a strong maximum in the nucleus surface layer.

## I. Introduction

The classical nucleation theory (CNT) is based on the assumption that the surface tension of a small liquid droplet equals the surface tension of a flat surface: the capillarity approximation. Although various attempts have been made in order to include the size dependence of surface tension¹ into phenomenological nucleation theories, the resulting theories²⁻⁵ have not been much more successful than the CNT. In one-component systems, the CNT describes the gas−liquid transition often amazingly well, predicting nearly correct supersaturation dependences of the nucleation rate, although the predicted temperature dependences mostly disagree with experimental findings. However, in binary gas−liquid nucleation, the CNT breaks down completely, producing unphysical predictions of the properties of critical nuclei in systems where the surface tension has a strong composition dependence.

The binary CNT was first derived by Neumann and Döring,⁶ who applied it to the water−ethanol system and discovered that at certain vapor activities the theory predicts that the total number of water molecules in the critical nucleus becomes negative. The work of Neumann and Döring was forgotten for several decades after World War II. The next development in binary CNT was the seminal 1950 paper by Howard Reiss,⁷ who considered saddle surfaces formed by binary clusters in the free energy space. Perhaps luckily, Reiss only studied systems which did not have compositional gradients of surface tension, and he thereby avoided tackling the unphysical predictions. After Wilemski⁸ had rederived the binary CNT equations of Neumann and Döring, it was soon found⁹ that activity plots (plots showing how the gas phase activities of the two species can be varied keeping the nucleation rate constant) show strange humps instead of monotonic behavior in systems with strong surface tension gradients. These humps were subsequently¹⁰ shown to correspond to negative excess number of particles over the uniform vapor in critical nuclei.

We have recently¹¹ shown, using thermodynamic argumentation, that the unphysical predictions result directly from the failure of the capillarity approximation. In the present paper, we make density functional calculations on the properties of critical nuclei in a surface active binary system and corroborate the conclusion that the capillarity approximation fails badly when the surface tension depends strongly on droplet composition, leading to predictions of negative excess number of particles for the species with higher surface tension.

## II. Density Functional Theory

The binary fluid system under consideration consists of spherical hard-core atoms (monomers) and molecules composed of two fused hard spheres (dimers). To study this system, we employ density functional theory (DFT) together with the interaction site model in the local density approximation. In this approach, the grand potential functional $\Omega$ of the inhomogeneous fluid is written as¹²

$$
\begin{aligned}
\beta \Omega[\rho_{0}(\mathbf{r}), \rho_{1}(\mathbf{r}), \rho_{2}(\mathbf{r})] & =\int \mathrm{d} \mathbf{r} \rho_{0}(\mathbf{r}) \ln \rho_{0}(\mathbf{r})+ \\
& \sum_{j=1}^{2} \int \mathrm{d} \mathbf{r} \rho_{j}(\mathbf{r}) \ln f_{j}(\mathbf{r})+\int \mathrm{d} \mathbf{r} \Psi[\eta(\mathbf{r})] \rho_{\mathrm{s}}(\mathbf{r})- \\
& \int \int \mathrm{d} \mathbf{r} \mathrm{d} \mathbf{r}^{\prime} s^{(2)}\left(\left|\mathbf{r}-\mathbf{r}^{\prime}\right|\right) f_{1}(\mathbf{r}) f_{2}(\mathbf{r})+ \\
& \frac{\beta}{2} \sum_{j, k=0}^{2} \int \int \mathrm{d} \mathbf{r} \mathrm{d} \mathbf{r}^{\prime} \phi_{j k}^{\mathrm{LJ}}\left(\left|\mathbf{r}-\mathbf{r}^{\prime}\right|\right) \rho_{j}(\mathbf{r}) \rho_{k}\left(\mathbf{r}^{\prime}\right)- \\
& \beta \sum_{j=0}^{2} \mu_{j} \int \rho_{j}(\mathbf{r}) \mathrm{d} \mathbf{r} \quad(1)
\end{aligned}
$$

where $\beta=1/k_{\mathrm{B}}T$ with $T$ the absolute temperature and $k_{\mathrm{B}}$ Boltzmann’s constant. Here $\rho_{0}(\mathbf{r})$ and $\rho_{i}(\mathbf{r})$ are the number densities of monomers (index 0) and the two parts of the dimer molecule or sites (indices 1 and 2). The total density is $\rho_{\mathrm{s}}(\mathbf{r})$, and the packing fraction is given by $\eta(\mathbf{r})=\sum_{i=0}^{2} v \rho_{i}(\mathbf{r})$, where $v=\pi/6\sigma^{2}$ is the molecular volume for a hard-sphere, which is the same for all components, because we only consider hard

---
† Part of the special issue “Howard Reiss Festschrift”.
* To whom correspondence should be addressed.
‡ University of Kuopio.
§ University of Helsinki.

10.1021/jp0116454 CCC: $20.00
© 2001 American Chemical Society
Published on Web 10/09/2001

spheres of the same size $\sigma$. The chemical potential of the hard sphere component $i$ is denoted by $\mu_{i}$. The auxiliary functions $f_{i}(\mathbf{r})$ are related to the activities of the molecular sites.

The first two terms on the right-hand side of eq 1 comprise the ideal-gas part, whereas the third and the fifth terms are contributions from the repulsive hard-sphere system and the attractive perturbation, respectively. The excess free energy per particle over the ideal gas $\Psi$ is given by the formulas of Carnahan and Starling. $^{13}$ The perturbative system is treated according to Weeks-Chandler-Andersen scheme $^{14}$ with the attractive interactions obtained from the Lennard-Jones (LJ) potential. The bonding between the two particles in the dimer molecule cause a decrease in entropy which is included in the fourth term, where $s^{(2)}$ is an intramolecular correlation function. The dimers are assumed to have a rigid bond length $\sigma$; therefore, the correlation function is represented by $s^{(2)}(r)=(4 \pi \sigma^{2})^{-1} \delta(r-\sigma)$.

Minimizing eq 1 with respect to functions $\rho_{i}(\mathbf{r})$ and $f_{i}(\mathbf{r})$ gives a set of integral equations $^{12}$ from which the density profiles of planar gas-liquid interfaces or spherical droplets can be solved in respective geometries. $^{15}$ For homogeneous states these equations reduce to particularly simple forms. Noting that the densities of the dimer sites are now equal $(\rho_{1}=\rho_{2}=\rho)$, we can write the chemical potentials as

$$
\mu_{0}=k_{\mathrm{B}} T \ln \rho_{0}+U_{0} \tag{2}
$$

$$
\mu=\mu_{1}+\mu_{2}=k_{\mathrm{B}} T \ln \rho+U_{1}+U_{2} \tag{3}
$$

where functions $U_{i}$ are defined as

$$
\beta U_{i}=\Psi+\Psi^{\prime} v \rho_{\mathrm{s}}-\beta \sum_{j=0}^{2} \alpha_{i j} \rho_{j} \tag{4}
$$

with $\alpha_{i j}=-\int \mathrm{d} \mathbf{r} \phi_{i j}^{\mathrm{LJ}}(r)$. Pressure is obtained from

$$
P=k_{\mathrm{B}} T\left(\rho_{0}+\rho\right)+k_{\mathrm{B}} T \Psi^{\prime} v \rho_{\mathrm{s}}^{2}-\frac{1}{2} \sum_{i, j=0}^{2} \alpha_{i j} \rho_{i} \rho_{j} \tag{5}
$$

The surface tension of a planar gas-liquid interface $\gamma_{\infty}$ is calculated from the equilibrium density profiles as

$$
\gamma_{\infty} A=\Omega\left[\left\{\rho_{i}(\mathbf{r})\right\}\right]-\Omega_{\mathrm{e}} \tag{6}
$$

where $A$ is the area of the interface and $\Omega_{\mathrm{e}}$ is the grand potential evaluated at the coexisting bulk densities which are obtained by equating the chemical potentials from eqs 2 and 3 and pressures from eq 5 for vapor and liquid states. In a similar fashion, the work of formation of a critical droplet $\Delta \Omega$ is found from

$$
\Delta \Omega=\Omega\left[\left\{\rho_{i}(\mathbf{r})\right\}\right]-\Omega_{\mathrm{v}} \tag{7}
$$

where $\Omega_{\mathrm{v}}$ corresponds to the grand potential of a uniform vapor at given gas-phase activities $a_{i}=\exp \left(\mu_{i} / k_{\mathrm{B}} T\right)$.

The desired behavior of the fluid system is obtained by providing appropriate parameters for the LJ potential

$$
\phi_{i j}^{\mathrm{LJ}}(r)=4 \epsilon_{i j}\left[\left(\frac{\sigma_{i j}}{r}\right)^{12}-\left(\frac{\sigma_{i j}}{r}\right)^{6}\right] \quad (i \text { and } j=0,1, \text { and } 2) \tag{8}
$$

We assume the standard arithmetic mean rule for the length parameters $\sigma_{i j}$; however, the energy parameters $\epsilon_{i j}$ for the cross interactions are modified as

$$
\epsilon_{i j}=\left(1-k_{i j}\right) \sqrt{\epsilon_{i i} \epsilon_{j j}} \tag{9}
$$

where for the present case $\epsilon_{11}=\epsilon_{22}=0.6 \epsilon, k_{12}=0, k_{01}=-0.3$, and $k_{02}=0.374$ (the energy parameter of the monomer component $\epsilon_{00}$ is denoted as $\epsilon$ ). This choice results in an enhanced surface activity of the dimer component. Furthermore, the dimer site 1 is strongly attracted to monomers ("monophilic" site), whereas the site 2 experiences much weaker attraction ("monophobic" site), thus inducing a preferred orientation of dimers with respect to monomers at gas-liquid interfaces; however, the bulk liquid phases of this system are homogeneous at all liquid compositions within the local density approximation. All our calculations are performed at temperature $T / \epsilon=0.7$ where the liquid is fully miscible but just on the brink of immiscibility.

### III. Thermodynamics

We consider a two-component liquid droplet with a volume $V$ in equilibrium with the vapor phase. The droplet contains $g_{1}$ and $g_{2}$ molecules of species 1 and 2, respectively, it is modeled as spherical, and it has a sharp boundary (Gibbs dividing surface) between the uniform liquid and vapor phases. The differences between the real nucleus with a smoothly varying density profile and the droplet model nucleus are expressed as surface excess quantities. The total numbers of molecules, $g_{1}$ and $g_{2}$, are then independent of the choice of dividing surface:

$$
g_{i}=n_{l i}-n_{v i}+n_{s i} \tag{10}
$$

Here $n_{l i}=V \rho_{l i}$, and $\rho_{l i}$ denotes the density of species $i$ in the droplet. Correspondingly, $n_{v i}=V \rho_{v i}$, with $\rho_{v i}$ as the density of species $i$ in the vapor phase; thus, $g_{i}$ represents the excess number of molecules in the droplet over the uniform vapor. The difference between the numbers of molecules obtained by integration over the actual and over the droplet model density profiles is given by $n_{s i}$.

The pressure difference between the vapor and the droplet interior is given by the Laplace equation

$$
\Delta P=P_{l}-P_{v}=\frac{2 \gamma}{R_{\mathrm{t}}} \tag{11}
$$

where $\gamma$ is the surface tension of the droplet and the subscript $\mathrm{t}$ of the radius $R_{\mathrm{t}}$ denotes the surface of tension. The reversible work of formation of the droplet is

$$
W=-\Delta P V_{t}+4 \pi R_{\mathrm{t}}^{2} \gamma \tag{12}
$$

We now proceed to derive equations for the droplet radius and work of formation that make use of chemical potential rather than pressure differences. The liquid-phase chemical potentials are related to pressure via

$$
\mathrm{d} \mu_{l i}=v_{l i} \mathrm{~d} P_{l} \tag{13}
$$

at constant temperature and liquid composition; $v_{l i}$ denotes the partial molecular volume of species $i$. Making the assumption of incompressible liquid, we can integrate eq 13 from $P_{v}$ to $P_{l}$ to obtain

$$
v_{l i} \Delta P=-\Delta \mu_{i} \tag{14}
$$

where $\Delta \mu_{i}=\mu_{l i}\left(P_{l}\right)-\mu_{l i}\left(P_{v}\right)=\mu_{v i}\left(P_{v}\right)-\mu_{l i}\left(P_{v}\right)$, and the latter equality follows from the equilibrium between the droplet and the vapor. From eq 14, it follows that

$$
\Delta \mu_{1} / v_{l 1}=\Delta \mu_{2} / v_{l 2} \tag{15}
$$

which can be used to numerically determine the nucleus composition. Substituting for $\Delta P$ in eqs 11 and 12, we obtain the Kelvin equation for the droplet radius and an equation for the work of formation as

$$
R_{\mathrm{t}}=\frac{2 \gamma v_{l i}}{\Delta \mu_{i}} \tag{16}
$$

$$
W=(4 \pi / 3) R_{t}^{2} \gamma \tag{17}
$$

The usual form of the classical nucleation theory is now obtained by making the assumption that the surface tension of the droplet, $\gamma$, equals the surface tension of a flat interface, $\gamma_{\infty}$. We have recently shown $^{11}$ that in binary systems the requirement that surface tension is independent of droplet curvature is equivalent to the requirement that the surface of tension coincides with the special equimolar surface denoted by radius $R_{\mathrm{e}}$ at which the following condition is fulfilled:

$$
n_{s 1} v_{1}+n_{s 2} v_{2}=0 \tag{18}
$$

When eq 18 holds at the surface of tension, we can write $R = R_{\mathrm{t}} = R_{\mathrm{e}}$ and

$$
R=\frac{2 \gamma_{\infty} v_{l i}}{\Delta \mu_{i}} \tag{19}
$$

$$
W=(4 \pi / 3) R^{2} \gamma_{\infty} \tag{20}
$$

which are the binary CNT equations for the radius and work of formation of the critical nucleus.

### IV. Results and Discussion

The unphysical behavior produced by the binary CNT for our model system can be seen in Figure 1. On the curves of Figure 1, the free energy of the critical cluster rather than the nucleation rate is kept constant; however, the variation of the rate along a curve is modest. The density functional curves behave monotonically and have a negative slope throughout the activity space, whereas the upper classical curve exhibits a region of positive slope. The CNT prediction is counterintuitive: if the dimer activity is kept constant (e.g., at $a_{\mathrm{D}}=1.5$) and monomer vapor is added continuously into the system, the nucleation rate must first increase, then decrease, and then increase again in order for the activity plot to show a hump. Furthermore, in a binary system, the nucleation theorem $^{16,17}$ leads to: $^{18}$

$$
\left(\frac{\partial \mu_{v 1}}{\partial \mu_{v 2}}\right)_{\Delta \Omega}=-\frac{g_{2}}{g_{1}} \tag{21}
$$

indicating that a positive slope in an activity plot corresponds to a negative excess number of particles $g_{i}$ in a critical cluster, which of course is not only counterintuitive but also unphysical.

In our recent paper, $^{11}$ we made classical nucleation calculations on the water-ethanol system and traced the reason for the appearance of the negative excess number of particles $g_{i}$ back to the assumption that $R_{\mathrm{t}}=R_{\mathrm{e}}$ (or, in other words, that $\gamma$ $=\gamma_{\infty}$). In Figures $2-4$, we present direct numerical evidence from DFT calculations supporting this conclusion. The figures present surface tension ratios $\gamma / \gamma_{\infty}$ and differences between the two radii, $\left(R_{\mathrm{e}}-R_{\mathrm{t}}\right) / R_{\mathrm{t}}$. The surface tension of the droplet, $\gamma$, and the radius to the surface of tension, $R_{\mathrm{t}}$, were obtained from eqs 11 and 12. Note that the liquid pressure, $P_{1}$, applied in these calculations was obtained from the equation-of-state relations $2-5$, giving the pressure of a liquid phase in equilibrium with the supersaturated vapor, and it does not necessarily have the same value as the pressure in the center of the actual density functional nucleus. Similarly, when calculating the radius to the equimolar surface, $R_{\mathrm{e}}$, the reference density and composition were taken to be those of a liquid in equilibrium with the supersaturated vapor, which generally are somewhat different from the density and the composition in the center of the nucleus. The equilibrium composition obtained from eqs $2-5$ was also applied in calculation of $\gamma_{\infty}$.

![](./images/812653393943199745_1.jpg)

**Figure 1.** Activity plots for two different constant nucleus free energies. See text for details.

![](./images/812653393943199745_2.jpg)

**Figure 2.** Ratios of nucleus surface tension to flat interface surface tension as a function of gas-phase monomer activity. The markers correspond to nuclei shown in Figure 1.

Figure 2 shows the surface tension ratios $\gamma / \gamma_{\infty}$ for the critical nuclei corresponding to the activity plot of Figure 1. With the $\Delta \Omega / \epsilon=60$ curve, the ratio decreases starting from $a_{\mathrm{m}}=0$, and the decrease becomes quite steep at monomer gas-phase activities between 1.25 and 1.5. As can be seen from Figure 1, the slope of the activity plot becomes positive at $a_{\mathrm{m}}=1.25$. All in all, the classical and density functional activity plots are quite far from each other in the monomer activity range of 1.25-3.5, where the surface tension ratio is below 0.95. The $\gamma / \gamma_{\infty}$

![](./images/812653393943199745_3.jpg)

Figure 3. Difference of the radii to the equimolar surface and to the surface of tension, normalized by nucleus size, as a function of monomer activity. The markers correspond to the nuclei shown in Figure 1.

![](./images/812653393943199745_4.jpg)

Figure 4. Density profiles of monomers (M) and the monophilic (D₁) and monophobic (D₂) ends of dimer molecules in critical nuclei at $\Delta\Omega/\epsilon = 60$.

curve for $\Delta\Omega/\epsilon = 400$ shows also a minimum, but a less pronounced one; this time the surface tension ratio is mostly above 0.95. However, it can be noted from Figure 1 that the CNT and DFT activity plots start departing somewhat as the decrease of the surface tension ratio becomes steeper.

Figure 3 shows the differences in the surface of tension and equimolar radii as functions of monomer gas-phase activity. As can be expected based on Figure 2, the difference for $\Delta\Omega/\epsilon = 60$ increases rapidly at the monomer activity range 1.25−1.5. The maximum difference between $R_{\rm e}$ and $R_{\rm t}$ is roughly 15% of the nucleus radius, which in absolute terms equals $0.65\sigma$. For $\Delta\Omega/\epsilon = 400$, the maximum value of $R_{\rm e} - R_{\rm t}$ is $0.45\sigma$, i.e., not very much smaller than that for $\Delta\Omega/\epsilon = 60$. However, this time the difference is only 4% of the nucleus radius, indicating that in relative terms the capillarity approximation is reasonable, unlike with the smaller nuclei. The variation in radius as a function of $a_{\rm M}$ does not have any qualitative effect on Figure 3 because $R_{\rm t}$ is a monotonically decreasing function; if we consider clusters of constant size, $R_{\rm e} - R_{\rm t}$ still shows a maximum.

Figure 4 shows density profiles of the critical nuclei at four different monomer activities of Figure 3. The three curves shown in each panel correspond to monomer density (M) and to the densities of monophilic (D₁) and monophobic (D₂) ends of the dimer molecules. At dimer-rich vapors, the profiles indicate that the surface layers of the nuclei are depleted of monomers, the dimer densities are monotonically decreasing from nucleus center toward the vapor, and the dimers show very little orientational ordering. Above $a_{\rm M} = 1.0$, a flip-over of the density profiles in the center of the nuclei takes place, and at $a_{\rm M} = 1.75$, most of the dimers are already concentrated in the surface layers with monophobic ends oriented toward the vapor. The worst failure of the capillarity approximation takes place with clusters having a high concentration of dimers on the nucleus surface and a depletion of dimers in the interior. The orientation of the dimers may contribute to the large nonzero values of $R_{\rm e} - R_{\rm t}$ somewhat, but it cannot be the main source, because the unphysical behavior can also be seen in surface active systems in which both molecular species are spherical.¹⁹

### V. Conclusion

We have studied the surface tensions of binary critical nuclei in a system in which the planar surface tension exhibits a strong compositional gradient. The ratio of cluster surface tension to planar surface tension exhibits a strong minimum at intermediate nucleus compositions. The deviation of the nucleus surface tension from the planar value is related to the deviation of the surface of tension ($R_{\rm t}$) from the equimolar surface ($R_{\rm e}$) specified by the condition $n_{s1}v_1 + n_{s2}v_2 = 0$. Our calculations show that the minimum in the surface tension ratio is accompanied by a strong maximum in the ratio $(R_{\rm e} - R_{\rm t})/R_{\rm t}$. The maximum occurs in nuclei in which the surface active component shows a density maximum in the nucleus surface layer. The breakdown of the capillarity approximation in this manner leads to the well-known unphysical predictions produced by the binary classical nucleation theory.

**Acknowledgment.** A.L. acknowledges financial support by the Academy of Finland (Project No. 44278).

### References and Notes

(1) Tolman, R. C. *J. Chem. Phys.* **1949**, *17*, 333.
(2) Dillmann, A.; Mayer, G. E. A. *J. Chem. Phys.* **1991**, *94*, 3872.
(3) Laaksonen, A.; Ford, I. J.; Kulmala, M. *Phys. Rev. E* **1994**, *49*, 5517.
(4) Kalikmanov, V. I.; van Dongen, M. E. H. *J. Chem. Phys.* **1995**, *103*, 4250.
(5) Talanquer, V. *J. Chem. Phys.* **1997**, *106*, 9957.
(6) Döring, W.; Neumann, K. *Z. Phys. Chem. A* **1940**, *186*, 193. Neumann, K.; Döring, W. *Z. Phys. Chem. A* **1940**, *186*, 203.
(7) Reiss, H. *J. Chem. Phys.* **1950**, *18*, 840.
(8) Wilemski, G. J. *Chem. Phys.* **1984**, *80*, 1370.
(9) Garnier, J. P.; Mirabel, P.; Migault, B. *Chem. Phys. Lett.* **1985**, *115*, 101.

(10) Laaksonen, A.; Kulmala, M.; Wagner, P. E. *J. Chem. Phys.* **1993**, 99, 6832.

(11) Laaksonen, A.; McGraw, R.; Vehkamäki, H. *J. Chem. Phys.* **1999**, 111, 2019.

(12) Napari, I.; Laaksonen, A.; Strey, R. *J. Chem. Phys.* **2000**, 113, 4476.
Napari, I.; Laaksonen, A.; Strey, R. *J. Chem. Phys.* **2000**, 113, 4480.

(13) Mansoori, G. A.; Carnahan, N. F.; Starling, K. E.; Leland, T. W.
*J. Chem. Phys.* **1971**, 54, 1523.

(14) Weeks, J. D.; Chandler, D.; Andersen, H. C. *J. Chem. Phys.* **1971**, 54, 5237.

(15) Napari, I.; Laaksonen, A. *J. Chem. Phys.* **1999**, 111, 5485.

(16) Viisanen, Y.; Strey, R.; Reiss, H. *J. Chem. Phys.* **1993**, 99, 4680.

(17) Oxtoby, D. W.; Kashchiev, D. *J. Chem. Phys.* **1994**, 100, 7665.

(18) Oxtoby, D. W.; Laaksonen, A. *J. Chem. Phys.* **1995**, 102, 6846.

(19) Laaksonen, A.; Oxtoby, D. W. *J. Chem. Phys.* **1995**, 102, 5803.