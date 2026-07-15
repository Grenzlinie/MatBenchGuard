# Screening of the Disclination Elastic Field by a System of Dislocations

G. F. Sarafanov* and V. N. Perevezentsev**

Blagonravov Mechanical Engineering Research Institute (Nizhni Novgorod Branch), Russian Academy of Sciences, Nizhni Novgorod, Russia

e-mail: *sarafanov@sinn.ru; **pevn@uic.nnov.ru

Received June 20, 2005

**Abstract**—An effective Airy stress function of a disclination is constructed with allowance for the screening effect of a system of distributed dislocation charges. The spatial distributions of the stress tensor of a screened disclination and the dislocation charge density are determined. The elastic energy of a screened disclination is calculated. © 2005 Pleiades Publishing, Inc.

In the stage of developed plastic deformation, the collective modes of the motion of dislocations lead to the appearance of a large-scale order in the distribution of dislocations in the applied stress field. Such ordered dislocation structures are called mesodefects [1–3]. The characteristic mesodefects formed in the stage of developed plastic deformation have been established and classified, the most typical of them representing broken dislocation boundaries [4]. From the theoretical standpoint, it is interesting to understand why the formation of such boundaries in the bulk of grains is energetically favorable. This problem is especially important, since the existence of broken dislocation boundaries is prohibited by the classical theory of crystal lattice defects [5, 6].

According to [7, 8], broken subboundaries can be interpreted in many cases as partial disclinations. As is known, the elastic fields of disclinations grow with distance. In the existing models [8, 9], the screening of the elastic fields of disclinations is provided by allowance for the existence of disclinations of the opposite sign. Therefore, it is assumed that the disclination systems of real crystals always comprise dipoles, quadrupoles, and other compensated configurations. It should be noted, however, that (i) experiments show evidence for the existence of uncompensated broken dislocation boundaries (branching small-angle boundaries, subboundaries terminating with a “torch” of lattice dislocations of a deformed grain, etc.) [2] and (ii) it is evident that both nucleation and propagation of broken subboundaries (partial disclinations) in the bulk of grains proceeds as a result of the collective motion of dislocations.

In view of the above considerations, it is expedient to evaluate the elastic fields of disclination configurations taking into account the contribution due to surrounding dislocations, since their redistribution in the elastic field of disclinations can reduce the total elastic energy of the system. This Letter presents the results of the development of this approach.

Let us consider a wedge disclination (situated at the origin of a coordinate system) surrounded by an ensemble of edge dislocations, which realize plastic deformation in an external stress field $\sigma_e$. The dislocations are characterized by the density $\rho_a(\mathbf{r}, t)$ and the Burgers vector $b_a$ (oriented in the dislocation slip direction $(0_x(\mathbf{b}_a \parallel \mathbf{e}_x))$. The dislocation ensemble has a zero total Burgers vector $\sum_a b_a \rho_{a0} = 0$, where $\rho_{a0} = \rho_0/2$ is the density of a homogeneous distribution of dislocations in the given stress field $\sigma_e$ and $a = \pm$. The total elastic field due to the disclination and the ensemble of dislocations is determined by the effective Airy stress function

$$
\begin{aligned}
\psi^{\Sigma}(\mathbf{r}) & = \psi(\mathbf{r}) + \sum_{a} \int \rho_a(\mathbf{r}') \psi_a^e(|\mathbf{r} - \mathbf{r}'|) d\mathbf{r}' \\
& = \psi(\mathbf{r}) + D b \int I(\mathbf{r}')(y - y') \ln \frac{r_0}{|\mathbf{r} - \mathbf{r}'|} d\mathbf{r}',
\end{aligned} \tag{1}
$$

where $\psi(\mathbf{r}) = D\omega/2(r^2\ln(r/R) - r^2/2)$ is the Airy stress function for the wedge disclination [8], $R$ is the radius of truncation of the elastic field (e.g., the characteristic crystal size), $\omega$ is the disclination power, $\psi_a^e(\mathbf{r}) = -b_a D y \ln(r/r_0)$ is the Airy stress function for the edge dislocation [5], $I(\mathbf{r}) = \rho_+(\mathbf{r}) - \rho_-(\mathbf{r})$ is the excess dislocation density (dislocation charge), $D = G/2\pi(1 - v)$, $G$ is the shear modulus, and $v$ is the Poisson ratio.

A consistent analysis of the problem related to the determination of the effective Airy stress function $\psi^{\Sigma}(\mathbf{r})$ can be performed within the framework of a self-consistent field approximation which has been developed in plasma physics and is known as the Debye approxi-

mation [10]. A characteristic feature of this approximation is that, in the state of thermodynamic equilibrium, both electrons (e) and ions (i) in a self-consistent field ($U_{\text{eff}} = e\varphi_{\text{eff}}$) are distributed according to the Boltzmann law. Under the condition of electroneutrality ($n_{0\text{e}} = n_{0\text{i}} = n_0/2$), the charged particles obey the relation $(n_{\text{i}} - n_{\text{e}})/n_0 = \sinh(-e\varphi_{\text{eff}}/kT) \simeq -U_{\text{eff}}/kT$ characteristic of the given approximation [10].

In a Coulomb plasma, the equilibrium distribution of charged particles is established as a result of their thermal motion (and, accordingly, temperature plays the role of an external parameter determining the process of relaxation toward the equilibrium state). In the problem under consideration, a stationary state of the dislocation system under the conditions of plastic deformation is attained as a result of the generation and annihilation of dislocations. Here, an analog of the temperature is offered by the work of plastic deformation $T_{\text{ext}} \simeq b\sigma_e \bar{L}$, which corresponds to the propagation of a dislocation over a mean free path length $\bar{L}$.

Thus, applying the logic of the self-consistent field approximation to the problem under consideration, we may suggest that
$$
I(\mathbf{r}) = -\rho_0 \frac{U_{\text{eff}}(\mathbf{r})}{T_{\text{ext}}} = -\frac{\rho_0 b}{T_{\text{ext}}} \frac{\partial \psi^{\Sigma}(\mathbf{r})}{\partial y}, \tag{2}
$$
where $U_{\text{eff}}^a(\mathbf{r}) = b_a \partial \psi^{\Sigma}(\mathbf{r})/\partial y$ is the energy of interaction of a separate dislocation with the self-consistent elastic field. Passing to the Fourier components in Eqs. (1) and (2), we obtain
$$
\psi^{\Sigma}(\mathbf{k}) = \frac{4\pi D\omega}{|\mathbf{k}|^4 + 4k_y^2 r_d^{-2}}, \quad I(\mathbf{k}) = \frac{ik_y 4\omega b^{-1} r_d^{-2}}{|\mathbf{k}|^4 + 4k_y^2 r_d^{-2}}, \tag{3}
$$
where $r_d^{-2} = \pi\rho_0 b^2 D/T_{\text{ext}}$. Using relations (3), we can determine the stationary spatial distribution of the dislocation charge (see figure) in the elastic field of a disclination:
$$
\begin{aligned}
I(\mathbf{r}) &= \frac{1}{(2\pi)^2} \int \frac{ik_y 4\omega b^{-1} r_d^{-2}}{|\mathbf{k}|^4 + 4k_y^2 r_d^{-2}} e^{-i\mathbf{k}\mathbf{r}} d\mathbf{k} \\
&= I_e \sinh(y/r_d) K_0(r/r_d),
\end{aligned} \tag{4}
$$
where $I_c = \omega/\pi b r_d$ and $K_0(r/r_d)$ is the zero-order Macdonald function [11]. Finally, applying the inverse Fourier transformation and taking into account the unknown function $\psi^{\Sigma}(\mathbf{k})$, we obtain expressions for the stress tensor of the defect system under consideration:

![](./images/812128199893843970_1.jpg)

Stationary spatial distribution of the normalized excess dislocation density $I(x, y)/I_c$ in the field of a disclination situated at the origin of coordinates. The maximum dislocation charge $I = \pm 0.5I_c$ is observed at the points with $x = 0$, $y = \pm 0.8r_d$.

$$
\sigma_{yy}^{\Sigma}(\mathbf{r}) = \frac{\partial^2 \psi^{\Sigma}(\mathbf{r})}{\partial x^2} \tag{5}
$$
$$
= -D\omega\left[ \cosh(y/r_d) K_0(r/r_d) + \sinh(y/r_d)\frac{y}{r} K_1(r/r_d) \right],
$$

$$
\sigma_{xx}^{\Sigma}(\mathbf{r}) = \frac{\partial^2 \psi^{\Sigma}(\mathbf{r})}{\partial y^2} \tag{6}
$$
$$
= -D\omega\left[ \cosh(y/r_d) K_0(r/r_d) - \sinh(y/r_d)\frac{y}{r} K_1(r/r_d) \right],
$$

$$
\sigma_{xy}^{\Sigma}(\mathbf{r}) = -\frac{\partial^2 \psi^{\Sigma}(\mathbf{r})}{\partial x\partial y} \tag{7}
$$
$$
= -D\omega \sinh(y/r_d)\frac{x}{r} K_1(r/r_d),
$$

where $K_1(z) = -K_0'(z)$ is the first-order Macdonald function.

Equations (5)-(7) show that the elastic fields $\sigma_{ij}^{\Sigma}$ decay with distance and become very small at $r \gg r_d$ ($K_0(r/r_d) \sim \sqrt{\pi r_d/2r} e^{-r/r_d}$ [11]). For this reason, the parameter $r_d$ can be considered as the radius of screening of the elastic field of a disclination in the dislocation slip direction $0x$ (in the $0y$ direction, the elastic field

decays according to a hyperbolic law). It should also be noted that the spatial scale $r_d$ coincides with the screening radius introduced in [12].

Using expressions (5)-(7), we can readily determine the energy $W^{\Sigma}$ of the elastic field of the disclination-surrounding dislocations system:

$$
\begin{aligned}
W^{\Sigma}= & \frac{D^{2} \omega^{2}}{2 G} \int_{0}^{R} r d r \int_{0}^{2 \pi}\left[\sinh ^{2}\left(y / r_{d}\right) K_{1}^{2}\left(r / r_{d}\right)\right. \\
+ & \left.(1-2 v) \cosh ^{2}\left(y / r_{d}\right) K_{0}^{2}\left(r / r_{d}\right)\right] d \varphi \\
& \simeq \frac{\sqrt{\pi}}{4} D \omega^{2} r_{d}^{2} \sqrt{\frac{R}{r_{d}}}.
\end{aligned}
\tag{8}
$$

Comparing this formula to the energy $W=D \omega R^{2} / 8$ of an unscreened disclination [8], we obtain

$$
W^{\Sigma} / W=2 \sqrt{\pi}\left(r_{d} / R\right)^{3 / 2}. \tag{9}
$$

Let us obtain some estimates. The screening radius according to [12] is on the order of an average distance between dislocations. In the stage of developed plastic deformation, the density of dislocations is $\rho \sim 10^{10} \mathrm{~cm}^{-2}$ [1], so that $r_{d} \sim \rho^{-1 / 2} \simeq 10^{-5} \mathrm{~cm}$. Taking the characteristic scale $R$ equal to the grain size $D=2 \mu \mathrm{m}$, we obtain $W^{\Sigma} / W=3 \times 10^{-2}$, whereas for $D=10 \mu \mathrm{m}$ the screening effect is $W^{\Sigma} / W \sim 3 \times 10^{-3}$. Thus, a system of excess dislocations distributed according to the law (4) established for mesodefects produces effective screening of a disclination and significantly decreases the elastic energy of the disclination.

In the initial formulation, the problem was considered in infinite space. However, taking into account that the characteristic scale $r_{d}$ of decay of the elastic field is rather small (except for the direction perpendicular to the slip system), we may suggest that the obtained results can be generalized to the case of grains with dimensions $d \gg r_{d}$.

## REFERENCES

1. V. V. Rybin, *Large Plastic Deformations and Failure of Metals* (Metallurgiya, Moscow, 1986) [in Russian].
2. V. V. Rybin, Vopr. Materialoved., No. 4 (32), 11 (2002).
3. V. N. Perevezentsev and V. V. Rybin, Vopr. Materialoved., No. 4 (32), 113 (2002).
4. A. N. Vergazov, V. A. Likhachev, and V. V. Rybin, Fiz. Met. Metalloved. **42**, 146 (1976).
5. J. P. Hirth and J. Lothe, *Theory of Dislocations* (McGraw-Hill, New York, 1967; Atomizdat, Moscow, 1972).
6. A. M. Kosevich, *Physical Mechanics of Real Crystals* (Naukova Dumka, Kiev, 1981) [in Russian].
7. R. De Wit, J. Res. Natl. Bur. Stand., Sect. A **77**, 49, 359, 607 (1973).
8. V. I. Vladimirov and A. E. Romanov, *Disclinations in Crystals* (Nauka, Leningrad, 1986) [in Russian].
9. A. E. Pomanov, in *Proceedings of the International Conference "Nanomaterials under Severe Plastic Deformation (NANOSPD2)," Vienna, 2002* (Wiley-VCH, Weinheim, 2004), pp. 215-225.
10. L. D. Landau and E. M. Lifshitz, *Course of Theoretical Physics, Vol. 5: Statistical Physics* (Nauka, Moscow, 1976; Pergamon, Oxford, 1980).
11. V. S. Vladimirov, *Equations of Mathematical Physics* (Nauka, Moscow, 1981; Dekker, New York, 1971).
12. G. F. Sarafanov, Fiz. Tverd. Tela (St. Petersburg) **39**, 1575 (1997) [Phys. Solid State **39**, 1403 (1997)].

Translated by P. Pozdeev