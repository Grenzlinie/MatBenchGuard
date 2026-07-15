# The freezing transition of flexible membranes

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2002 Europhys. Lett. 58 60

(http://iopscience.iop.org/0295-5075/58/1/060)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 130.237.165.40
This content was downloaded on 22/08/2015 at 03:56

Please note that terms and conditions apply.

EUROPHYSICS LETTERS
1 April 2002

Europhys. Lett., **58** (1), pp. 60–66 (2002)

# The freezing transition of flexible membranes

G. GOMPPER $^1$ and D. M. KROLL $^2$

$^1$ Institut für Festkörperforschung, Forschungszentrum Jülich
D-52425 Jülich, Germany
$^2$ Department of Medicinal Chemistry and Minnesota Supercomputer Institute
University of Minnesota - 308 Harvard Street SE, Minneapolis, MN 55455, USA

(received 16 November 2001; accepted in final form 17 January 2002)

PACS 61.20.Ja – Computer simulation of liquid structure.
PACS 61.72.Bb – Theories and models of crystal defects.
PACS 87.16.Dg – Membranes, bilayers, and vesicles.

**Abstract.** – The freezing transition of a network model for flexible tensionless membranes fluctuating about a planar reference state is investigated by Monte Carlo simulations and scaling arguments. The bond-orientational order parameter susceptibility is analyzed for three values of the bending rigidity $\kappa$, and it is found that for sufficiently large $\kappa$ the low-temperature hexatic phase melts via a universal Kosterlitz-Thouless transition. These results are consistent with recent theoretical predictions that the crumpled-to-crinkled transition occurs via disclination melting for all bending rigidities and tether lengths. However, our simulations provide evidence that the transition becomes first order at very low bending rigidity.

The internal order of membranes —tensionless two-dimensional sheets composed of molecules that are different than the surrounding medium— is dramatically influenced by the fact that they are embedded in three dimensions and can buckle or fluctuate out of plane [1,2]. For example, whereas a rigid membrane can possess quasi-long-range (QLR) translational order at sufficiently low temperatures, the ability to buckle reduces the energy of free dislocations and has lead to the conjecture that it is actually finite, so that crystalline order is destroyed at any finite temperature [3]. The resulting low-temperature phase is a hexatic, which has QLR bond-orientational order.

Renormalization group calculations [4–6] indicate that hexatic order stiffens the membrane, so that unlike fluid membranes in which the bending rigidity, $\kappa$, scales to zero at long length scales, $\kappa$ approaches at constant times the hexatic rigidity, $K_{\text{H}}$, in this limit. The hexatic membrane is therefore more rigid than a fluid membrane, and is said to be “crinkled” [4–6]. The exact mechanism by which the hexatic membrane melts into the disordered, fluid phase at higher temperatures is not completely resolved; however, a recent detailed analysis [5,6] of the low-temperature crinkled-to-crumpled transition predicts that thermally induced shape fluctuations cause a $\kappa$-dependent reduction of $K_{\text{H}}$ and that the transition is controlled by a single fixed point for *all* $(\beta K_{\text{H}})^{-1} > 0$ and $1.2 \gtrsim (\beta\kappa)^{-1} > 0$ (where $\beta = 1/k_{\text{B}}T$). The resulting critical behavior is predicted to be that of the Kosterlitz-Thouless (KT) disclination unbinding transition [7]. For $(\beta\kappa)^{-1} \lesssim 1.2$, the membrane is expected to remain in the fluid phase.

© EDP Sciences

Simulation studies of the freezing of flexible vesicles of spherical topology have provided strong evidence in support of the suggestion that the low-temperature phase of flexible membranes is a hexatic [8,9]. In particular, it was found that for short tether lengths (low temperatures), the density of "free" dislocations, $n_{\text{dloc}}$, with Burgers vector $|\boldsymbol{b}|=\langle l\rangle$, where $\langle l\rangle$ is the mean nearest-neighbor separation, scales as

$$
\frac{1}{\beta \kappa} \ln \left(n_{\text{dloc}}\right)=-\Theta\left(\frac{\kappa}{K_{0}\langle l\rangle^{2}}\right),
\tag{1}
$$

where $K_0$ is the two-dimensional Young modulus of the network, indicating that the free energy of dislocations is indeed finite even for the shortest tether lengths studied. Unfortunately, the spherical topology of the vesicles prevented a detailed characterization of the transition in terms of the orientational order parameter. Furthermore, an analysis [10] of the sine- Gordon model of membrane freezing indicates that shape fluctuations of spherical vesicles cause disclinations to be screened at length scales larger than $R(\kappa/K_{\text{H}})^{1/2}$, where $R$ is the radius of the vesicle. When the screening length is much larger than the system size, screening is unimportant, and a normal KT transition should occur. However, if it is smaller than the system size, there are unbound disclinations at all non-zero temperatures, and strictly speaking, the hexatic phase does not exist, although there may still be a sharp crossover in many quantities, as observed in refs. [8,9].

Experimental studies of the phase behavior and melting of membranes have been performed recently for stacked crystalline sheets of the membrane protein bacteriorhodopsin [11,12]. In this system, the protein forms a hexagonal crystal at low temperatures, which is embedded in a fluid lipid bilayer. Melting is controlled by varying the temperature or by swelling with water. Indeed, the melting temperature is found to depend on the lamellar spacing [12], as expected from the defect-induced melting scenario described above [13]. However, the transition is found to be first order, possibly due to the overall repulsive electrostatic interaction between the membranes.

Currently, Monte Carlo simulations of triangulated surfaces therefore provide the best tool for investigating the freezing transition of flexible membranes. In this paper we present the results of a Monte Carlo simulation study of the freezing of low-bending-rigidity membranes fluctuating about a planar reference state. Because of the flat reference state, there should be no smearing beyond standard finite size effects, and a detailed analysis of the hexatic- to-fluid transition is possible. We employ the same tether-and-bead model of self-avoiding membranes [8,9,14–16] used in our earlier studies of vesicles. The model consists of $N$ hard spheres of diameter $\sigma_0=1$ which are connected by tethers of maximum extension $l_0<\sqrt{3}\sigma_0$ to form a planar triangular network with periodic boundary conditions. In order to allow for diffusion within the membrane, tethers can be cut and reattached between the four beads which form two neighboring triangles. We use the discretization [17]

$$
E_{b}=\lambda \sum_{\langle i j\rangle}\left(1-\boldsymbol{n}_{i} \cdot \boldsymbol{n}_{j}\right),
\tag{2}
$$

for the curvature energy, where the sum runs over all pairs of neighboring triangles, and $\boldsymbol{n}_i$ is the surface normal vector of triangle $i$. The parameter $\lambda$ in eq. (2) is related to the bending rigidity $\kappa$ of the continuum curvature model by $\kappa=\lambda/\sqrt{3}$ [18]. This model contains only two parameters, the bending rigidity $\lambda$, which controls the out-of-plane fluctuations, and the tether length $l_0$, which controls the in-plane density.

In order to minimize finite-size effects, periodic boundary conditions were employed. The simulation cell has a projection on the $x$-$y$ plane which is an equilateral parallelogram with an

![](./images/812128915874119682_1.jpg)

Fig. 1 – Density of (a) "free" dislocations, $\langle n_{\rm dloc} \rangle$, and (b) sevenfold disclinations, $\langle n_{\rm disc}^7 \rangle$, as a function of the tether length $l_0$. Data from earlier studies of the freezing of flexible vesicles [8,9] are shown for $N=247$ with $\beta\lambda=1.5$ ($\square$) and $\beta\lambda=2$ ($\triangle$), as well as $N=407$ with $\beta\lambda=1.5$ ($\blacksquare$), $\beta\lambda=2$ ($\blacktriangle$), and $\beta\lambda=3$ ($\blacktriangledown$). Data from the present simulations are shown for $\beta\lambda=1.5$ ($\triangleleft$), $\beta\lambda=2$ ($\triangleright$), and $\beta\lambda=3$ ($\circ$), for system sizes $N=784$ (solid lines), $N=400$ (dashed lines), and $N=196$ (dash-dotted lines).

internal angle of $60^\circ$. The membrane is therefore oriented, on average, perpendicular to the $z$-axis. The constant pressure procedure we used is described in ref. [9], and the simulations were performed for zero spreading pressure. A Monte Carlo step then consists of a random dis- placement of all beads in the cube $[-s,s]^3$, followed by $N$ attempted tether cuts. An attempt to increment the projected area of the membrane was made every five Monte Carlo steps.

The simulations were performed in the isotropic, fluid phase and in the transition region for three values of the bending rigidity, $\beta\lambda=1.5$, 2, and 3. System sizes $N=196$, 400, and 784 were studied, and averages were taken over up to 500 million Monte Carlo steps per particle. The network's elastic constants have been determined in earlier studies of the same model [9].

Figure 1 presents a comparison of results for the density of "free" dislocations (i.e., 5/7- pairs which have only six-fold coordinated vertices as nearest neighbors), $\langle n_{\rm dloc} \rangle$, and sevenfold disclinations, $\langle n_{\rm disc}^7 \rangle$, obtained in the present series of simulations and our earlier study of freezing of flexible vesicles [8,9]. As can be seen, the defect densities measured in the current set of simulations increase rapidly at a value of the tether length which depends on the bending rigidity and the system size, with a finite size shift to shorter tether lengths with increasing system size. In contrast, the transition is much broader for vesicular networks, consistent with the prediction of ref. [10] that there is no transition in this case, and that the screening of disclinations increases the disclination density for small values of the ratio $\kappa/K_{\rm H}$, so that the fluid phase effectively extends to smaller tether lengths.

The behavior of the bond angle order parameter, $\psi_6$, has been used to characterize the tran- sition in more detail. The bond angle order parameter is defined by $\psi_6 = \left| \frac{1}{N_b} \sum_b \exp[6i\theta_b] \right|$, where the sum on $b$ is over the $N_b=3N$ nearest-neighbor bonds of the network and $\theta_b$ is the angle between the projection of bond $b$ on the $x$-$y$ plane and some fixed reference axis. Histograms of the bond angle order parameter for values of the tether length near the transi- tion are shown in fig. 2. Figure 2(a) contains results for $\beta\lambda=3$. For the largest system size, there is a single peak in the histograms for all values of the tether length, and the position of this peak shifts to larger values as the tether length is decreased, consistent with a continuous phase transition. For the two smaller system sizes, however, there is a persistent, distinct peak at $\psi_6 \approx 0.47$. Contributions to this peak arise from configurations in which there are no free dislocations. For $N=196$, the histograms are bimodal, with peaks at zero and $\psi_6 \approx 0.47$.

![](./images/812128915874119682_2.jpg)

Fig. 2 – Normalized order parameter histograms $P(\psi_6)$ for (a) $\beta\lambda=3$ and $N=196$, $l_0=1.520$ (solid line), $N=400$, $l_0=1.505$ (dashed line), and $N=784$, $l_0=1.495$ (dash-dotted line), (b) $\beta\lambda=2$ and $N=196$, $l_0=1.465$ (solid line), $N=400$, $l_0=1.4475$ (dashed line), and $N=784$, $l_0=1.440$ (dash-dotted line), and (c) $\beta\lambda=1.5$ and $N=196$, $l_0=1.395$ (solid line), $N=400$, $l_0=1.375$ (dashed line), and $N=784$, $l_0=1.370$ (dash-dotted line) and $l_0=1.375$ (long-dashed line).

The histogram for the intermediate system size, while still exhibiting a peak arising from dislocation-free configurations, has an additional broader peak that shifts towards zero with increasing tether length. In this case, it appears that transitions between states with two or more free dislocations occur frequently, without any nucleation barrier. The most probable explanation of this behavior is that the density of unbound dislocations in the nascent hexatic phase is so low that for $N=196$ and 400 the network is too small to correctly describe the defect structure of this phase. It could also be that the periodic boundary conditions —by imposing a nonlocal constraint on the system— artificially stabilize the ordered phase. In fact, the bond flipping algorithm we apply, only allows for the pairwise creation of disclinations. In any case, the data for $N=784$ indicate that this finite-size artifact is sufficiently small for this system size that we can be confident that the transition is continuous in the thermodynamic limit for $\beta\lambda=3$.

For $\beta\lambda=2$ the situation is rather similar. In particular, dislocation-free configurations again contribute to a persistent peak near $\psi_6=0.5$ in the two smaller system sizes. However, for $N=784$, the contribution from defect-free configurations is sufficiently small that we are confident that the transition is also continuous for this value of the bending rigidity. The evolution of the order parameter histograms as a function of the tether length for $\beta\lambda=2$ and $N=784$ is illustrated in fig. 3.

The behavior observed for $\beta\lambda=1.5$ is different. In fig. 2(c) it can be seen that the histograms for all three system sizes are bimodal, with peaks at zero and $\psi_6\approx0.55$, so that there is a discontinuous transition with decreasing tether length for the system sizes studied. The discontinuous character of the transition in this case can also be seen in the behavior of the defect densities in fig. 1. Whereas the rapid increase in the density of 7-fold disclinations occurs at slightly smaller tether lengths than that of $\langle n_{\rm dloc}\rangle$ for $\beta\lambda=2$ and 3, for $\beta\lambda=1.5$, it occurs at the same values of the tether length.

It is clear from the previous discussion that finite-size effects are sufficiently large that only data for the largest system size, $N=784$, can be used to determine the detailed nature of the transition for $\beta\lambda=2$ and 3. The KT theory of disclination melting [7] predicts that in an infinite system, the order parameter susceptibility $\chi_6\equiv N\langle\psi_6^2\rangle$ diverges as
$$
\chi_6=a_\chi\exp\left[b_\chi/(l_0-l_0^{*})^{1/2}\right],\tag{3}
$$
as the transition is approached in the isotropic, fluid phase for $l_0-l_0^{*}\to0^{+}$, where $l_0^{*}$ is

![](./images/812128915874119682_3.jpg)

Fig. 3

![](./images/812128915874119682_4.jpg)

Fig. 4

Fig. 3 – $P(\psi_6)$ for $\beta\lambda=2$ and $N=784$ for several values of the tether length, $l_0$, spanning the hexatic-fluid transition: $l_0=1.435$ (solid line), $l_0=1.4375$ (dashed line), $l_0=1.440$ (dash-dotted line), $l_0=1.4425$ (dotted line), $l_0=1.445$ (long-dashed line), and $l_0=1.450$ (dash-dot-dotted line).

Fig. 4 – Finite-size scaling plot of the scaled bond angle susceptibility $\chi_6/L^{1.75}$ as a function of $\xi_6/L$. As discussed in the text, only data for $N=784$ and $\beta\lambda=2$ ($\triangleright$) and $\beta\lambda=3$ ($\circ$), which are least affected by finite-system-size effects, are plotted. The solid line is a plot of $(\xi_6/L)^{1.75}$.

the value of the tether length at the transition. A fit of our data for $\chi_6$ (for $N=784$ and $\beta\lambda=3$) to eq. (3) yields $a_\chi=0.511\pm0.22$, $b_\chi=0.748\pm0.108$, and $l_0^*=1.487\pm0.002$. A similar fit to data for $\beta\lambda=2$ assuming the same value of $b_\chi$, gives $a_\chi=0.419\pm0.019$ and $l_0^*=1.4278\pm0.0006$.

The quality of these fits can be seen in a finite-size scaling plot of the data for $\chi_6$ [19]. KT theory predicts that in an infinite system, the correlation length diverges as [7]
$$
\xi_6=a_\xi\exp\left[b_\xi/(l_0-l_0^*)^{1/2}\right],\tag{4}
$$
for $l_0-l_0^*\to0^+$. However,
$$
\chi_6\sim\xi_6^{2-\eta_6},\tag{5}
$$
with $\eta_6=1/4$ at the transition, so that
$$
b_\chi=(2-\eta_6)b_\xi=1.75b_\xi.\tag{6}
$$

Using the results of the fit of $\chi_6$, we can therefore determine $\xi_6$; in the following, we assume $\xi_6=\chi_6^{4/7}$, with $\chi_6$ given by eq. (3). A finite-size scaling plot $\chi_6/L^{1.75}\equiv\Xi(\xi_6/L)$, with $L=\sqrt{N}$, as a function of $\xi_6/L$, is shown in fig. 4. As can be seen, the scaling is excellent, indicating that eqs. (3)-(6) provide a consistent description of the data. Furthermore, the fact that the data for both values of bending rigidity scale in the same way, with only a $\lambda$-dependent shift of the value of the critical tether length, provides strong support for the prediction of refs. [5,6,10] that thermally induced shape fluctuations cause a $\kappa$-dependent reduction of $K_{\rm H}$ and that the transition is controlled by a single fixed point, at least for $\beta\lambda\gtrsim2$.

Figure 5 contains a plot of our data for $\langle z^2\rangle/N$, the scaled mean-square value of the out-of-plane fluctuations as a function of the tether length. It can be seen that $\langle z^2\rangle$ scales approximately as $N$ in both the fluid and hexatic phases. Indeed, if the scale dependence of the bending rigidity is neglected, one expects $\langle z^2\rangle\simeq(\beta\kappa)^{-1}N/(16\pi^3)$. Our data in the

![](./images/812128915874119682_5.jpg)

Fig. 5

![](./images/812128915874119682_6.jpg)

Fig. 6

Fig. 5 - Scaled mean-square amplitude of the out-of-plane fluctuations $\langle z^2 \rangle / N$ as a function of the tether length $l_0$. Symbol and line definitions correspond to those in fig. 1.

Fig. 6 - Phase diagram in the $(\beta K_0 \langle l \rangle^2)^{-1}$-$(\beta \kappa)^{-1}$ plane. The solid symbols ($\bullet$) are estimates for the phase boundary obtained from the current simulations and from simulations of melting of a network model confined to two dimensions. The open symbols ($\circ$) are estimates obtained from simulations of spherical vesicles. The solid line is meant to serve as a guide to the eye.

fluid phase are too close to the transition and too noisy to discern the small size-dependent logarithmic renormalization of the bending rigidity. For $\beta \lambda = 1.5$, we are sufficiently close to the crumpled state that occasional large-amplitude out-of-plane fluctuations make it very difficult to obtain accurate ensemble averages.

Following ref. [9], we present our results for the phase diagram in the $(\beta K_0 \langle l \rangle^2)^{-1}$-$(\beta \kappa)^{-1}$ plane in fig. 6. The solid symbols ($\bullet$) are estimates for the phase boundary obtained in the current simulations and a recent study of the the same network model in two dimensions [20] using results for the Young modulus published in ref. [9]. This phase diagram has a striking similarity with the one obtained from renormalization group calculations in refs. [5,6]. Note, however, that i) we plot the data as a function of the two-dimensional Young modulus of a tethered network of the same tether length, while the field-theoretical model uses the hexatic stiffness $K_{\rm H}$, and ii) the stability of the hexatic phase extrapolates to values of the bending rigidity as low as $\beta \kappa \simeq 0.56$, while renormalization group calculations suggest a higher limit of $\beta \kappa \simeq 0.83$. It is important to note, however, that the field-theoretical calculations are valid only for sufficiently large $\kappa$. The open symbols in fig. 6 are estimates obtained from simulations of spherical vesicles [8,9]. In the latter simulations, the location of the crossover from the hexatic to fluid phase was estimated indirectly from the behavior of several quantities such as the system-size-dependence of the reduced volume, the density of "free" 7-fold disclinations and $\langle n_{\rm disc}^7 \rangle$, and the bond flip acceptance rate.

For $\beta \lambda \gtrsim 2$, simulation results presented in this paper clearly show that the transition is continuous, and that the critical behavior is consistent with the predictions of refs. [5,6,10]. For smaller values of the bending rigidity, the situation is less clear. Our results for $\beta \lambda = 1.5$ are consistent with a first-order transition for the system sizes we simulated. However, it is possible that this behavior is a finite-size artifact, and that the transition becomes continuous for larger system sizes. Similarly, although all our results for $\beta \lambda = 2$ and 3 are consistent with a KT transition, we cannot, for the current range of system sizes, completely exclude

a transition with a power law singularity. Simulations of substantially larger systems will be required to determine the nature of the transition for $\beta\lambda \lesssim 1.5$ and validate in detail the singular behavior at the transition.

We have presented strong evidence that the Kosterlitz-Thouless freezing scenario applies to flexible membranes, at least for sufficiently large bending rigidity. Experimentally, stacks of membranes provide the best hope for studying this transition in detail. It would therefore be interesting to extend our simulations to stacks of several membranes and to investigate the dependence of the nature of the transition on the type of intramembrane interactions.

***

This work was supported in part by the National Science Foundation under Grants No. DMR-9712134 and DMR-0083219 and the donors of The Petroleum Research Fund, adminis- tered by the ACS.

## REFERENCES

[1] NELSON, D. R., in *Fluctuating Geometries in Statistical Mechanics and Field Theory*, edited by DAVID F., GINSPARG P. and ZINN-JUSTIN J. (North-Holland, Amsterdam) 1996, pp. 423-477.
[2] GOMPPER G. and KROLL D. M., *J. Phys. Condens. Matter*, **9** (1997) 8795.
[3] SEUNG H. S. and NELSON D. R., *Phys. Rev. A*, **38** (1988) 1005.
[4] GUITTER E. and KARDAR M., *Europhys. Lett.*, **13** (1990) 441.
[5] PARK J.-M. and LUBENSKY T. C., *Phys. Rev. E*, **53** (1996) 2648.
[6] PARK J.-M. and LUBENSKY T. C., *Phys. Rev. E*, **53** (1996) 2665.
[7] NELSON D. R., in *Phase Transitions and Critical Phenomena*, edited by DOMB C. and LEBOWITZ J., Vol. **7** (Academic Press, London) 1983, pp. 1-99.
[8] GOMPPER G. and KROLL D. M., *Phys. Rev. Lett.*, **78** (1997) 2859.
[9] GOMPPER G. and KROLL D. M., *J. Phys. I*, **7** (1997) 1369.
[10] PARK J.-M., *Phys. Rev. E*, **54** (1996) 5414.
[11] KOLTOVER I., SALDITT T., RIGAUD J.-L. and SAFINYA C. R., *Phys. Rev. Lett.*, **81** (1998) 2494.
[12] KOLTOVER I., RÄDLER J. O., SALDITT T., ROTHSCHILD K. J. and SAFINYA C. R., *Phys. Rev. Lett.*, **82** (1999) 3184.
[13] MORSE D. C. and LUBENSKY T. C., *J. Phys. II*, **3** (1993) 531.
[14] HO J.-S. and BAUMGÄRTNER A., *Europhys. Lett.*, **12** (1990) 295.
[15] KROLL D. M. and GOMPPER G., *Science*, **255** (1992) 968.
[16] BOAL D. H. and RAO M., *Phys. Rev. A*, **45** (1992) R6947.
[17] KANTOR Y. and NELSON D. R., *Phys. Rev. Lett.*, **58** (1987) 2774.
[18] GOMPPER G. and KROLL D. M., *J. Phys. I*, **6** (1996) 1305.
[19] JASTER A., *Europhys. Lett.*, **42** (1998) 277.
[20] GOMPPER G. and KROLL D. M., *Eur. Phys. J. E*, **1** (2000) 153.
