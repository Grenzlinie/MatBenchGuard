# ELASTIC AND ACOUSTIC WAVE BAND STRUCTURE

M. M. SIGALAS
Department of Physics and Astronomy, Iowa State University, Ames, Iowa 50011, U.S.A.

AND

E. N. ECONOMOU
Department of Physics, University of Crete, 714 09, Crete, Greece

(Received 25 November 1991)

The problem of wave propagation in inhomogeneous media is of central importance in many branches of physics, mathematics and engineering. Over the past 25 years, attention has been focused on the question of localization [1-5] of Schrödinger's waves in disordered materials, following the seminal paper of Anderson [6]. In recent years, the question of localization has been extended to the case of classical waves [7-16]. John and Rangarajan [17] and Economou and Zdetsis [18] have pointed out the connection between possible localization of classical waves and the possible existence of gaps in the spectrum of periodic inhomogeneous media. Indeed, band gaps and possibly regions of very low density of states (DOS) in periodic systems would become regions of localized states if we gradually introduce disorder (positional, geometric and compositional). Thus, the question of band structure of classical waves has received increased attention. In particular, both the scalar (SC) wave equation has been studied [7-20] as well as the case of electromagnetic (EM) waves [21-26], and it is already known that the band structures of EM and SC waves have significant differences which are due to the vector character of EM waves.

In the present letter we report, for the first time (to the best of our knowledge), results for elastic (EL) and acoustic (AC) waves in periodic structures consisting of identical spheres placed periodically within a host homogeneous material. We expect that the vector character of EL waves being both transverse and longitudinal will generate new features over those present in SC and EM waves. Furthermore, in EL and AC waves there is an additional important parameter, the ratio of densities in the two regions which may be varied in a wide range of values, and which control the impedance mismatch and hence the propagtion. Thus, in addition to the application aspect of our results, we expect that the systematic study of AC and EL waves will provide richer physics and enhance our understanding of wave propagation and localization. Furthermore, EL and AC waves are very important on their own because they appear in many branches of science and engineering and because they permit easily controlled experiments.

The equation describing EL waves in inhomogeneous solids is given by [27]

$$
\frac{\partial^{2} u^{i}}{\partial t^{2}}=\frac{1}{\rho}\left\{\frac{\partial}{\partial x_{i}}\left(\lambda \frac{\partial u^{l}}{\partial x_{l}}\right)+\frac{\partial}{\partial x_{l}}\left[\mu\left(\frac{\partial u^{i}}{\partial x_{l}}+\frac{\partial u^{l}}{\partial x_{i}}\right)\right]\right\},
$$

where $u^{i}$ is the $i$ th component of the displacement vector $\mathbf{u}(\mathbf{r})$, $\lambda(\mathbf{r})$ and $\mu(\mathbf{r})$ are the so-called Lamé coefficients, and $\rho(\mathbf{r})$ is the density. The longitudinal and transverse velocities for the homogeneous case $(\lambda, \mu, \rho=$ constant) are given by

$$
c_{l}=\sqrt{(\lambda+2 \mu) / \rho}, \quad c_{t}=\sqrt{\mu / \rho}.
$$

---
0022-460X/92/200377+06 $08.00/0
© 1992 Academic Press Limited

378
LETTERS TO THE EDITOR

For fluids $\mu=0$, and, by introducing the pressure $p=-\lambda \nabla \mathbf{u}$, equation (1) can be recast as
$$
\partial^{2} p / \partial t^{2}=\lambda \nabla(\nabla p / \rho), \quad \mu=0. \quad(3)
$$

If $\rho$ is constant equation (2) reduces to the usual scalar wave equation
$$
\nabla^{2} p-\frac{1}{c^{2}} \frac{\partial^{2} p}{\partial t^{2}}=0, \quad c^{2}=\lambda / \rho, \quad \mu=0, \quad \rho=\text { constant. }
$$

For periodic media, Bloch's theorem asserts that $\mathbf{u}(\mathbf{r})$ (or $p(\mathbf{r})$ ) are of the form $\mathbf{u}(\mathbf{r})=\mathbf{u}_{\mathbf{k}} \mathrm{e}^{\mathrm{i} \mathbf{k r}}$, where $\mathbf{u}_{\mathbf{k}}$ is a periodic function with the same periodic structure as $\lambda(\mathbf{r}), \mu(\mathbf{r})$ and $\rho^{-1}(\mathbf{r})$. All these periodic functions can be expanded in Fourier series with corresponding coefficients $\mathbf{u}_{\mathbf{k}+\mathbf{G}}, \lambda_{\mathbf{G}}$ and $\rho_{\mathbf{G}}^{-1}$, respectively, where $\mathbf{G}$ are vectors of the reciprocal lattice. In terms of these coefficients, equation (1) becomes
$$
\begin{aligned}
\omega^{2} u_{\mathbf{k}+\mathbf{G}}^{i}= & \sum_{\mathbf{G}^{\prime}}\left\{\sum_{l, \mathbf{G}^{\prime \prime}} \rho_{\mathbf{G}-\mathbf{G}^{\prime}}^{-1}\left[\lambda_{\mathbf{G}^{\prime \prime}-\mathbf{G}^{\prime}}\left(\mathbf{k}+\mathbf{G}^{\prime}\right)_{l}\left(\mathbf{k}+\mathbf{G}^{\prime \prime}\right)_{i}+\mu_{\mathbf{G}^{\prime \prime}-\mathbf{G}^{\prime}}\left(\mathbf{k}+\mathbf{G}^{\prime}\right)_{i}\left(\mathbf{k}+\mathbf{G}^{\prime \prime}\right)_{l}\right] u_{\mathbf{k}+\mathbf{G}^{\prime}}^{l}\right. \\
& \left.+\sum_{\mathbf{G}^{\prime \prime}}\left[\rho_{\mathbf{G}-\mathbf{G}^{\prime}}^{-1} \mu_{\mathbf{G}^{\prime \prime}-\mathbf{G}^{\prime}} \sum_{j}\left(\mathbf{k}+\mathbf{G}^{\prime}\right)_{j}\left(\mathbf{k}+\mathbf{G}^{\prime \prime}\right)_{j}\right] u_{\mathbf{k}+\mathbf{G}^{\prime}}^{i}\right\}.
\end{aligned}
$$

If the infinite series is approximated by a sum of $N$ reciprocal vectors, equation (4) is reduced to a $3 N \times 3 N$ matrix eigenvalue equation which can be solved numerically. For equations (2) and (3), the same procedure leads to an $N \times N$ matrix equation.

In this letter we consider a composite periodic medium consisting of identical spheres of radius $R$ placed periodically within a host homogeneous material. The velocities of the sphere material are $c_{l_{i}}$ and $c_{t_{i}}$ and those of the host $c_{l_{0}}$ and $c_{t_{0}}$. The ratio of the densities $\rho_{i} / \rho_{o}$ is denoted by $y$. We have considered fcc, bcc, sc, diamond and hexagonal lattice structures. For each lattice structure one can easily determine the volume fraction of the spheres, $x$, in terms of the radius $R: x=4 \pi R^{3} / 3 V_{w}$, where $V_{w}$ is the volume of the Wigner Seitz cell.

We considered first the SC wave equation (equation (3)) for AC waves and then we examined the effects of a non-constant density (equation (2)). For the SC wave equation, the main result is that the first gap appears for volume fraction $x \approx 14 \%$ and $c_{l_{i}} / c_{l_{i}} \geqslant r_{c} \approx 2$ for both fcc and bcc structures. For the sc structure, the gap appear for lower values of $x(x \leqslant 10 \%)$ and higher value of $r_{c}\left(r_{c} \approx 2 \cdot 7\right)$. For hexagonal structure and ratio of the lattice constants $c / a \approx 3 / 4$, the results are quite similar to the fcc results. But when the ratio $c / a$ departs from this optimum value (either to lower or higher values), the appearance of the gaps becomes more difficult: e.g., comparing the band structures for $c / a=0 \cdot 5,0 \cdot 8$ and $1 \cdot 5$, we can see that the bands at the A point $[\pi / c(0,1,0)]$ are lower for $c / a=1 \cdot 5$, so it is not easy to find a gap in any direction. For $c / a=0 \cdot 5$, the bands at the $\mathrm{K}$ point $[2 \pi / a(2 / 3,0,0)]$ are lower than the bands at the A point. For the hcp structure, the first band is doubly degenerate across the $P$ axis for every value of $x$ and $c_{l_{0}} / c_{l_{i}}$, so it is impossible to find the first gap, which is associated with the lowest s-wave resonance. Similar degeneracy exists across the $Z$ axis of the diamond structure [25].

In Figure 1 we plot the density of states (DOS) for a characteristic case of a.c. waves $(\mu \equiv 0)$. In the middle panel (Figure $1(\mathrm{~b})$ ), the $\rho=$ constant $(y=1)$ case is shown exhibiting a rather large gap (due mainly to the s-wave scattering resonance [9]). Other gaps as well as dips in the DOS are present. In the upper panel a case is shown, where the density inside, $\rho_{i}$, is higher than the host density, $\rho_{o}$. All gaps have disappeared. Clearly, increasing the ratio $y \equiv \rho_{i} / \rho_{o}$ from one makes the appearance of gaps more difficult. On the contrary,

![](./images/812396032989069312_1.jpg)

Figure 1. Calculated DOS for acoustic waves $(\mu=0)$ propagating in a periodic system of spheres in an fcc lattice within a host material. The volume fraction, $x$, occupied by the spheres is $x=14.4\%$. The ratio of velocities is $c_{o}/c_{i}=2.65$. The ratio of densities is $\rho_{i}/\rho_{o}=5,1$ and $1/15$ or (a), (b) and (c), respectively.

when $y$ becomes much smaller than one (e.g., bubbles in liquid), huge gaps appear separated by narrow bands as shown in the lower panel of Figure 1. The reason is that the surface of each "bubble" in this case can be easily deformed, thus giving rise to a low frequency strong scatterings resonance. We conclude that the optimum case for the appearance of gaps or for the localization of a.c. waves is low density $(y \to 0)$, low velocity $(c_{li}/c_{lo} \ll 1)$ spheres (i.e., "bubbles") occupying a volume fraction of the order of $10\%$ of the host material.

We have also studied the full EL case $(\mu \neq 0$, equation (1)), first for $\rho=$ constant $(y=1)$ and then for $y \neq 1$. For the same $\mu$ (and $\rho$) in both regions, but different $\lambda$, the band structure of the longitudinal modes is qualitatively similar (but not identical) with that obtained from the SC wave equation; the transverse modes have an almost perfect plane wave, doubly degenerate structure. On the other hand, for the same value of $\lambda$ (and $\rho$) in both regions, but different $\mu$, and not too large a ratio of velocities, the band structure of the transverse modes is qualitatively similar to this obtained in the EM case [24-26], while the longitudinal modes departs strongly from the plane wave behavior. When all parameters vary, the longitudinal and transverse components are hybridized and the full complexity and richness of the EL case comes into play.

In Figure 2, we present explicit results for a case where $\rho_{i}=\rho_{o}$ (i.e., $y=1$) and $c_{l}/c_{t}$ is a little above $\sqrt{2}$, both inside and outside the spheres. This value, $\sqrt{2}$, is the lowest possible [27], and thus it allows the strongest mixing of longitudinal (L) and transverse (T) waves.

![](./images/812396032989069312_2.jpg)

Figure 2. Calculated band structure and DOS for elastic waves in an fcc periodic structure. The ratio $c_{l_{i}} / c_{t_{i}}=1 \cdot 501, c_{l_{o}} / c_{t_{o}}=1 \cdot 415, c_{l_{o}} / c_{l_{i}}=8 \cdot 17, \rho_{i} / \rho_{o}=1$ and $x=14 \cdot 4 \%$.

Since the wide separation of the L and T bands makes the appearance of simultaneous gaps extremely improbable, we guessed that the opposite case of the strongest mixing (obtained when $c_{l} / c_{t} \approx \sqrt{2}$) provides favorable condition for gaps to appear. Indeed, as shown in Figure 2, a rather narrow gap does appear. The ratio of the gap to mid-gap is about $5 \%$.

There is a single and a double degenerate band under the gap. These bands practically coincide and become flat near the edge of the Brillouin zone. For this reason the DOS has a sharp peak below the gap. Also, there is a single and a double degenerate band above the gap. These bands practically coincide and become flat near the center of the Brillouin zone, so the DOS have another peak above the gap. The accuracy of our numerical calculation does not permit us to find whether there are crossings or avoided crossings.

In Figure 3 we show the dependence of the threshold value of the ratio $c_{l_{o}} / c_{l_{i}} \equiv r_{c}$, on the volume fraction $x$ for the lowest gap. There is a threshold value of $x, x_{i}$, above which the lowest gap appears for very large value of $r_{c}$. As $x$ increases beyond $x_{i}, r_{c}$ decreases and reaches a minimum $r_{c}^{m}$ for an optimum value of $x, x_{m}$. As $x$ increases further beyond $x_{m}, r_{c}$ increases slowly and approaches infinity for an upper cut-off value of $x, x_{u}$. Thus, the lowest gap appears only for $x_{i} \leqslant x \leqslant x_{u}$. For the fcc case $x_{i} \approx 4 \%, x_{m} \approx 25 \%, x_{u} \approx 75 \%$ and $r_{c}^{m} \approx 4 \cdot 4$. For the simple scalar case the corresponding values are $x_{m} \approx 14 \%$ and $r_{c}^{m} \approx 2$. Thus, in the full elastic case, the gaps appears for higher ratio of velocities (at least by a factor of 2) and higher values of optimum $x$ as compared with the scalar case. In the diamond lattice, there is no gap just above the lowest three bands in contrast to the fcc case. However, a gap does appear at higher frequency above the lowest six bands.

We have examined the effects of varying density ratio $y \equiv \rho_{i} / \rho_{o}$. In contrast to the scalar acoustic case, we found that decreasing $y$ narrows and eventually eliminates the gap. Thus, hollow spheres within a solid do not seem to constitute a favorable scheme for elastic gaps or localization. Furthermore, and again in contrast to the scalar acoustic case, increasing

![](./images/812396032989069312_3.jpg)

Figure 3. The threshold value of the contrast $r_{c}=c_{l_{o}} / c_{l_{i}}$ for which the first frequency gap just opens up, plotted against the volume fraction $x$ for elastic waves in an fcc structure with $\rho_{i} / \rho_{o}=1, c_{l_{i}} / c_{t_{i}}=1.501$ and $c_{l_{o}} / c_{t_{o}}=1.415$.

$y$ above one widens the gap, e.g., by increasing $y$ to 4, the first gap increased by a factor of about 2.7. We have no simple physical interpretation for this unexpected result.

We have also studied the case of liquid spheres within a solid host, hoping that the complete absence of transverse waves within the spheres may help the gaps to appear. Because of numerical difficulties, we have only preliminary results for $x \leqslant 10 \%$, indicating that liquid spheres with greater density than the host material (e.g., $\mathrm{Hg}$ in $\mathrm{Al}$) seem to favor the appearance of gaps.

In conclusion, we have shown, for the first time, that frequency gaps do appear for EL waves propagating in systems composed of properly chosen solid (and possibly liquid) spheres placed periodically within an appropriate solid host material. The ratio of longitudinal and transverse velocities must be as close as possible to $\sqrt{2}$ in both regions, the density of the spheres must be greater than that of the host material, while the velocity must be smaller, e.g., favorable combinations likely to give gaps are $\mathrm{Au}$ or $\mathrm{Pb}$ or $\mathrm{Bi}$ spheres in $\mathrm{Al}$ or Si host. The study of EL waves in various lattices provides very useful data for understanding the interplay between crystal structure and scalar or vector character in the wave propagation, in the appearance of gaps and, consequently, in the localization of classical waves. This interplay has not been elucidated yet.

For AC waves propagating in periodic fluid or solid (with $\mu \approx 0$) and for density in the spheres much lower than in the host (e.g., bubbles in liquids), we find a huge lower gap and very narrow band above it. By weakly disordering such periodic systems we may obtain the most favorable case for finding and studying localized states, not only in the tails but even well within the bands.

Possible applications of the present results may appear in the construction of acoustic or ultrasound filters; in obtaining a very good thermal insulator at very low temperature by randomly placing bubbles in insulating liquids; and by probing experimentally mesoscopic structures in solids (in the range $1 \mathrm{~mm}$ to submicron) if a more quantitative understanding of the multiple scattering of elastic waves is achieved. Furthermore, the present work suggests the possibility of tailoring the low frequency part of the phonon spectrum by opening up artificial gaps and thus influencing physical properties for which low frequency phonons are important.

## REFERENCES

1. T. ANDO and H. FUKUYAMA (editors) 1988 *Anderson Localization*. Berlin: Springer.
2. P. A. LEE and T. V. RAMAKRISHNAM 1985 *Review of Modern Physics* 57, 287-337. Disordered electronic systems.

3. K. HANKE and Y. V. KOPAEV (editors) 1990 *Electronic Phase Transitions*. Amsterdam: North-
Holland.

4. E. N. ECONOMOU 1983 *Green's Functions in Quantum Physics*. Berlin: Springer.

5. K. A. BENEDICT and J. T. CHALKER (editors) 1991 *Localization 1990*. Bristol: IOP Publishing.

6. P. W. ANDERSON 1958 *Physical Review* **109**, 1492-1505. Absence of diffusion in certain random lattices.

7. P. SHENG (editor) 1990 *Scattering and Localization of Classical Waves in Random Media*. Singapore: World Scientific (for a recent review of the field).

8. S. JOHN 1985 *Physical Review Letters* **53**, 2169-2172. Electromagnetic absorption in a disordered medium near a photon mobility edge.

9. S. JOHN 1984 *Physical Review* **B31**, 304-309. Localization and absorption of waves in a weakly dissipative disordered medium.

10. P. W. ANDERSON 1985 *Philosophical Magazine* **B52**, 505-509. The question of classical localiza- tion: a theory of white paint?

11. P. SHENG and Z. Q. ZHANG 1986 *Physical Review Letters* **57**, 1879-1882. Scalar wave localiza- tion in a two component composite.

12. K. AYRA, Z. B. SU and J. L. BIRMAN 1986 *Physical Review Letters* **57**, 2725-2728. Anderson localization of electromagnetic waves in a dielectric medium of randomly distributed metal particles.

13. C. A. CONDAT and T. R. KIRKPATRICK 1987 *Physical Review Letters* **58**, 226-229. Observability of acoustic and optical localization.

14. C. M. SOUKOULIS, E. N. ECONOMOU, G. S. GREST and M. H. COHEN 1989 *Physical Review Letters* **B65**, 575-578. Existence of Anderson localization of classical waves in a random two component medium.

15. E. N. ECONOMOU and C. M. SOUKOULIS 1989 *Physical Review* **B40**, 7977-7980. Calculation of optical transport and localization quantities.

16. S. JOHN 1987 *Physical Review Letters* **58**, 2486-2489. Strong localization of photons in certain disordered dielectric superlattices.

17. S. JOHN and R. RANGARAJAN 1988 *Physical Review* **B38**, 10 101-10 104. Optimal structures for classical wave localization: an alternative to the Ioffe-Regel criterion.

18. E. N. ECONOMOU and A. ZDETSIS 1989 *Physical Review* **B40**, 1334-1337. Classical wave propa- gation in periodic structures.

19. K. M. LEUNG and Y. F. LIU 1990 *Physical Review* **B41**, 10 188-10 190. Photon band stucture: plane wave method.

20. S. SATPATHY, Z. ZHANG and M. R. SALEHPOUR 1990 *Physical Review Letters* **64**, 1239-1242. Theory of photons bands in three-dimensional periodic dielectric structures.

21. E. YABLONOVITCH 1987 *Physical Review Letters* **58**, 2059-2062. Inhibited spontaneous emission in solid state physics and electronics.

22. E. YABLONOVITCH and T. J. GMITTER 1989 *Physical Review Letters* **63**, 1950-1953. Photonic band structure: the face-centered-cubic case.

23. E. YABLONOVITCH 1990 in *Analogies in Optics and Micro Electronics* (W. van Haeringen and D. Lenstra, editors) 117-133. Netherlands: Kluwer Academic.

24. Z. ZHANG and S. SATPATHY 1990 *Physical Review Letters* **65**, 2650-2653. Electromagnetic propagation in periodic structures: Bloch wave solution of Maxwell's equations.

25. K. M. Ho, C. T. CHAN and C. M. SOUKOULIS 1990 *Physical Review Letters* **65**, 3152-3155. Existence of photonic gap in periodic dielectric structures.

26. K. M. LEUNG and Y. F. LIU 1990 *Physical Review Letters* **65**, 2646-2649. Full vector wave calculation of photonic band structure in face-centered-cubic dielectric media.

27. L. D. LANDAU and E. M. LIFSHITZ 1959 *Theory of Elasticity*. London: Pergamon Press.