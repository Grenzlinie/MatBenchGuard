# Charge-unbinding transition in the two-dimensional classical Coulomb-plasma model by use of a variational Gaussian wave functional

Zhi-Jian Chen
Department of Physics, Shanghai Jiao Tong University, Shanghai 200030, China

Yu-Mei Zhang
Department of Physics, Tongji University, Shanghai 200092, China

Bo-Wei Xu
Department of Physics, Shanghai Jiao Tong University, Shanghai 200030, China

(Received 14 December 1993)

The charge-unbinding transitions in the two-dimensional classical Coulomb-plasma model are analyzed by use of the equivalence between the two-dimensional Coulomb plasma and $(1+1)$-dimensional quantum sine-Gordon models. The grand canonical potential and the screening length are obtained from the ground states of the $(1+1)$-dimensional quantum sine-Gordon model as derived by use of a variational Gaussian wave functional. We have shown that the charge-unbinding transition at small fugacity is a Kosterlitz-Thouless transition, while at large fugacity it is a first-order transition. The dependence of the potential on the mass is similar to that of the phenomenological Landau theory.

## I. INTRODUCTION

In recent years there have been extensive investigations of the charge-unbinding transition in the two-dimensional classical Coulomb-plasma model (2D CPM). $^{1-3}$ The charge-unbinding transition is an intuitive picture for the Kosterlitz-Thouless (KT) transition $^{4}$ in 2D solid-state physics. In the KT transition all the charges of the Coulomb plasma at low temperature are bound together into dipole pairs, whereas at higher temperature the pairs are broken. At very small fugacity Kosterlitz renormalization-group theory (RGT) is valid, $^{5}$ and predicts a continuous phase transition at the critical temperature. It is interesting to extend this charge-unbinding transition to the case of large fugacity in the 2D CPM. By modifying the Kosterlitz RGT with higher-order corrections, $^{1}$ Minnhagen showed that the charge-unbinding transition is a first-order transition at large fugacity. The first-order transition is also observed in numerical Monte Carlo simulations. $^{6}$

In the following sections, first we will show the equivalence between the 2D CPM at finite temperature and the $(1+1)$-dimensional quantum sine-Gordon model $[(1+1)$D SGM] in the ground state. The thermodynamic quantities of the 2D CPM have been mapped to the ground-state quantities of the $(1+1)$D SGM. Secondly, the phase transition in the 2DCPM is analyzed by use of the grand canonical potential and the screening length, which are obtained through use of a variational Gaussian wave functional. $^{7,8}$ In the last section, the main conclusions are summarized.

## II. THE 2D CPM AND (1+1)D SGM

The 2D CPM, which is a system composed of positive and negative charges with overall charge neutrality interacting with a logarithmic potential in two space dimensions, is defined through the grand partition function $Z_{\text{CP}}:^{2}$

$$
Z_{\mathrm{CP}}=\sum_{n=0}^{\infty} \frac{z^{2 n}}{(n!)^{2}} \int_{0}^{l} \prod_{i=1}^{2 n} \frac{d x_{i}}{a} \int_{0}^{l} \prod_{i=1}^{2 n} \frac{d y_{i}}{a} \exp \left\{\frac{1}{T} \sum_{i>j=1}^{2 n} s_{i} s_{j} \ln \left\{\left[\left(y_{i}-y_{j}+a\right)^{2}+\left(x_{i}-x_{j}\right)^{2}\right]^{1 / 2} a^{-1}\right\}\right\}, \tag{1}
$$

where $s_{i}=\pm 1$ is the charge of the $i$th particle (charge neutrality being imposed through the condition $\sum_{i=1}^{2 n} s_{i}=0$, for all $n$), $T$ is the dimensionless temperature (i.e., the Boltzmann constant is set to 1), $z$ is the fugacity, $a^{2}$ is the phase-space area, and $l^{2}$ is the volume of the system. The 2D CPM in the point-charge case can be transformed into the $(1+1)$D SGM by use of a functional integral, $^{9}$ with the advantage that standard quantum field theory can be applied to discuss the thermodynamic properties of the 2D CPM. Equation (1) can be rewritten in the form of a functional integral over a real scalar field, $^{1,10}$

$$
Z_{\mathrm{CP}}=\frac{\int D \Phi \exp \left(-\int d x d y L\right)}{\int D \Phi \exp \left(-\int d x d y \frac{1}{2}(\nabla \Phi)^{2}\right)}, \tag{2}
$$

with Lagrangian density
<|FunctionCallBegin|>bbox coordinates represent the bottom footer area, but since footers are removed, no bbox needed here<|FunctionCallEnd|>

$$
L=-\frac{1}{2}(\nabla \Phi)^{2}+\frac{\alpha}{\beta^{2}} \cos \beta \Phi,
\tag{3}
$$
where
$$
\alpha=\frac{4 \pi z}{a^{2} T},
\tag{4}
$$
$$
\beta^{2}=\frac{2 \pi}{T}.
\tag{5}
$$

If we identify one of the two coordinates as an imaginary time $t$, $y=it$, Eq. (2) shows that the 2D CPM is equivalent to the $(1+1)$D SGM in Minkowski space. The Hamiltonian density of the $(1+1)$D SGM is
$$
H_{\mathrm{SG}}=\frac{1}{2} \Pi^{2}+\frac{1}{2}(\nabla \Phi)^{2}-\frac{\alpha}{\beta^{2}} \cos \beta \Phi,
\tag{6}
$$
where the canonical conjugate momentum $\Pi$ of the real scalar field $\Phi$ is defined as
$$
\Pi=\frac{\partial L}{\partial \dot{\Phi}}=\dot{\Phi}.
\tag{7}
$$

The equivalence of the 2D CPM and the $(1+1)$D SGM implies that the grand canonical potential density $\Omega_{\mathrm{CP}}$ is related to the ground-state energy density $E_{\mathrm{SG}}$ of the $(1+1)$D SGM by
$$
\Omega_{\mathrm{CP}}=T\left(E_{\mathrm{SG}}-E_{\mathrm{SG}}^{0}\right),
\tag{8}
$$
where $E_{\mathrm{SG}}^{0}$ is the energy with no interaction. It is known that the charge-unbinding transition may be characterized by the appearance of the screening length $\lambda,{ }^{1}$ which is equal to the correlation length $m^{-1}$ where $m$ is the renormalized mass of the $(1+1)$D SGM.

The equivalence between the 2D CPM and the $(1+1)$D SGM is thus established. In the following section we will apply the properties of the ground state of the $(1+1)$D SGM obtained by use of the variational Gaussian wave functional to analyze the phase transitions in the 2D CPM.

### III. PHASE TRANSITIONS IN THE 2D CPM

Let us first review some results about the $(1+1)$D SGM. It is well known that the main difficulty for the $(1+1)$D SGM is the infrared divergency in conventional calculations based on perturbation theory, $^{11}$ the problem has been studied by various methods. The method of the variational wave functional has been applied to study the ground-state properties of the $(1+1)$D SGM at large momentum cutoff $1 / a .^{7,12,13}$ The transitions in the ground state of the $(1+1)$D SGM can be regarded as generalizations of Coleman's transition $^{11}$ in the parameter plane. By use of the ground-state properties of the $(1+1)$D SGM, $^{12,13}$ we obtain the grand canonical potential $\Omega_{\mathrm{CP}}$ and screening length $\lambda$,
$$
\Omega_{\mathrm{CP}}=\frac{T}{a^{2}}\left[\frac{1}{4 \pi} \sqrt{1+4 \pi z \xi / T}-2 z K(\xi)-\frac{1}{4 \pi}\right],
\tag{9}
$$
$$
\lambda=\sqrt{a^{2} T / 4 \pi z K(\xi)},
\tag{10}
$$
with
$$
K(\xi)=\exp \left[-\frac{1}{2 T} \ln \frac{1+\sqrt{1+4 \pi z \xi / T}}{\sqrt{4 \pi z \xi / T}}\right],
\tag{11}
$$
where $\xi$ is a renormalized order parameter. We note that, for very large $T, K(\xi) \simeq 1$, and
$$
\lambda \simeq \lambda_{D}=\sqrt{a^{2} T / 4 \pi z}.
\tag{12}
$$

This limit corresponds to the usual Debye-Huckel limit. $^{2}$
The stable state of the 2D CPM satisfies the conditions
$$
\frac{d}{d \xi} \Omega_{\mathrm{CP}}=0,
\tag{13}
$$
$$
\frac{d^{2}}{d \xi^{2}} \Omega_{\mathrm{CP}}>0,
\tag{14}
$$
or
$$
\frac{K(\xi)}{\xi}=1,
\tag{15}
$$
$$
1-\frac{1}{4 T} \frac{1}{\sqrt{1+4 \pi z \xi / T}}>0.
\tag{16}
$$

From Eqs. (15) and (11), we obtain
$$
z=\frac{T}{\pi} \xi^{(1-4 T)}\left[\xi^{(1-4 T)}-\xi\right]^{-2}.
\tag{17}
$$

The curves for $K(\xi)=$ constant in the $z-T$ plane are depicted in Fig. 1. On the solid line 1 $(z \leq z^{*}=1 / 4 \pi, T=T^{*}=\frac{1}{4})$, there is only the zero solution $K(\xi)=0$ for Eq. (15), which starts from the points $(0, \frac{1}{4})$ to $(1 / 4 \pi, \frac{1}{4})$. The dot-dashed line 2 is the envelope of the family of curves for $K(\xi)=$ constant in the $z-T$ plane, i.e.,
$$
z_{c}=\frac{T}{4 \pi}\left(\frac{1+4 T}{1-4 T}\right)^{1 / 4 T}\left[\left(\frac{1}{4 T}\right)^{2}-1\right],
\tag{18}
$$
which can be also obtained from the marginal conditions of stability
$$
\frac{K(\xi)}{\xi}=1,
\tag{19}
$$

![](./images/812771672389058560_1.jpg)

FIG. 1. Phase diagram of the 2D CPM in the $z-T$ plane. Solid line 1 is for $K(\xi)=0$. Dot-dashed line 2 is the envelope of the curves for $K(\xi)=$ constant. Solid line 3 is for $\Omega_{\mathrm{CP}}(0)=\Omega_{\mathrm{CP}}(\xi)$. Dot-dashed line 4 is for $T=T^{*}$, which corresponds to the tadpole summation (Ref. 13).

![](./images/812771672389058560_2.jpg)

FIG. 2 Dependence of $\xi$ on the inverse temperature for different values of $z$. Line 1 is for $z<z^{*}$, line 2 is for $z=z^{*}$, and line 3 is for $z>z^{*}$. The vertical dotted lines show the solutions of $\xi$ for certain $T$. $T_{c}$ corresponds to $z_{c}$ for a certain $\xi$ (in Fig. 1).

$$
1-\frac{1}{4 T} \frac{1}{\sqrt{1+4 \pi z \xi / T}}=0. \quad(20)
$$

The solid line 3 is for $\Omega_{\mathrm{CP}}(0)=\Omega_{\mathrm{CP}}(\xi)$, i.e.,
$$
z_{3}=\frac{T}{\pi}\left(\frac{1}{4 T}\right)^{(1+1 / 4 T)}\left(\frac{1}{4 T}-1\right)^{(1-1 / 4 T)}. \quad(21)
$$

The dot-dashed line 4 is for $T=T^{*}$, with starting point $(1 / 4 \pi, \frac{1}{4})$. Four regions are divided by these lines in the $z-T$ plane.

It is important to understand the behavior of $\Omega_{\mathrm{CP}}$ at the boundary value $\xi=0$. This can be investigated by obtaining the first-order derivative of $\Omega_{\mathrm{CP}}$ in Eq. (9) for van ishing $\xi$,
$$
\begin{aligned}
& \lim _{\xi \to 0} \frac{d}{d \xi} \Omega_{\mathrm{CP}} \\
& \quad=\lim _{\xi \to 0} \frac{z}{2 a^{2}}\left[1-\left(\frac{4 \pi z \xi}{T a^{2}}\right)^{(1 / 4 T-1)} \frac{4 \pi z}{T a^{2}}\left(\frac{4}{a^{2}}\right)^{-1 / 4 T}\right].
\end{aligned}
$$

When $T<\frac{1}{4}$,
$$
\lim _{\xi \to 0} \frac{d}{d \xi} \Omega_{\mathrm{CP}}>0, \quad(23)
$$
which means that $\Omega_{\mathrm{CP}}(0)$ is a minimum of $\Omega_{\mathrm{CP}}$. When $T>\frac{1}{4}$,
$$
\lim _{\xi \to 0} \frac{d}{d \xi} \Omega_{\mathrm{CP}} \to-\infty, \quad(24)
$$
then $\Omega_{\mathrm{CP}}(0)$ is a maximum of $\Omega_{\mathrm{CP}}(\xi)$.

In order to see the behavior of the screening length $\lambda$ in different regions (Fig. 1), we rewrite Eq. (11) as
$$
\frac{1}{4 T}=\frac{\ln \xi}{\ln \frac{4 \pi z \xi / T}{(1+\sqrt{1+4 \pi z \xi / T})^{2}}}. \quad(25)
$$

The curves for $4 \pi z / T=$ constant are depicted in Fig. 2.

When $T>\frac{1}{4}$:
(a) For $z<z^{*}$, there is always a nonzero solution $\left(\xi_{2}^{\prime}\right)$ for a stable state as shown in Fig. 3(a). As $T=\frac{1}{4}+\delta, \delta \to 0$ ( $\delta$ is a small positive value), $\xi_{2}^{\prime}$ moves continuously to zero, i.e., the screening length $\lambda$ increases continuously from a finite value (conductive plasma phase) to infinity (insulator phase).
(b) For $z>z^{*}$, there also exists a nonzero solution $\left(\xi_{2}^{\prime \prime}\right)$ connected to a stable state as shown in Fig. 3(a), but $\xi_{2}^{\prime \prime}$ does not tend to zero as $T=\frac{1}{4}+\delta, \delta \to 0$, i.e., $\lambda$ is finite as $T \to T^{*}$ except at $z=z^{*}$.

When $T<\frac{1}{4}$:
(a) For sufficiently large fugacity $z$ (i.e., $z>z_{c}$, Fig. 1), there are two nonzero solutions $\left(\xi_{1}, \xi_{2}\right)$. One is for a stable state $\left(\xi_{2}\right)$ and the other for an unstable state $\left(\xi_{1}\right)$, which are depicted in Fig. 3(b). We note that $\xi=0$ is the other stable state [see Eq. (23)], which means that two stable states $\Omega_{\mathrm{CP}}(0)$ and $\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$ coexist. Between the stable states, there is a grand canonical potential barrier $\Omega_{\mathrm{CP}}\left(\xi_{1}\right)$. Across the boundary from the state with $\Omega_{\mathrm{CP}}(0)$ to that with $\Omega_{\mathrm{CP}}\left(\xi_{2}\right), \xi$ (or $\lambda$ ) changes discontinu ously.
(b) When $z<z_{c}$, there does not exist a nonvanishing solution $\left(\xi_{2}\right)$ for a stable state, as shown in Fig. 3(c). But

![](./images/812771672389058560_3.jpg)

FIG. 3. Dependence of the grand canonical potential $\Omega$ on $\xi$ in the different regions of the phase diagrams. (a) When $T>0.25$, $z<z^{*}(>z^{*})$, the $\xi_{2}^{\prime}$ (or $\xi_{2}^{\prime \prime}$ ) is the only solution of Eq. (15) for a stable state. (b) When $T<0.25, z>z_{c}, \xi_{1}$ is for a unstable state, $\xi_{2}$ is for a stable state. (c) When $T<0.25, z<z_{c}$, there is no nonzero solution of $K(\xi)$ for a stable state.

![](./images/812771672389058560_4.jpg)

FIG. 4. Continuous phase transition for $z<z^{*}$. Line 1 is for $T<0.25$. Lines 4,3 , and 2 correspond to $T_{4}>T_{3}>T_{2}$ which approaches 0.25 .

from Eq. (23), $\Omega_{\mathrm{CP}}(0)$ is a stable state, i.e., $\lambda$ is always infinite.

Next, we analyze the phase transition in the $\Omega_{\mathrm{CP}}-\xi$ plane. The relations between $\Omega_{\mathrm{CP}}$ and $\xi$ in different regions are depicted in Fig. 4 for $z<z^{*}$. On line 1 (in region I, Fig. 1), $\Omega_{\mathrm{CP}}(0)$ is the only stable state, and $\lambda$ is infinite, i.e., all charges of the Coulomb plasma are bound into dipole pairs (insulator phase). On lines 2, 3, and 4 (in region IV, Fig. 1), the stable state is $\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$, corresponding to finite $\lambda$ (conductive plasma phase); as mentioned above, the conductive plasma phase changes continuously to the insulator phase from region I to region IV (Fig. 1). As has been described by Minnhagen and Wallin, $^{3}$ this process implies the formation of an infinitesimal fraction of charge-binding pairs. So on crossing line 1 (Fig. 1), a continuous phase transition, or KT transition, occurs.

We should mention that our KT transition line is quantitatively somewhat different from that of the Kosterlitz RGT. This is due to the fact that we have not considered the renormalization of the interacting parameter $\beta^{2}$ in the $(1+1)$ D SGM, or the corresponding temperature parameter in the method of the variational Gaussian wave functional.

For $z>z^{*}$, with increasing temperature parameter $T$, one moves successively through regions I, II, III, and IV (see Fig. 1). The corresponding $\Omega_{\mathrm{CP}}-\xi$ curves are shown in Fig. 5. On line 1 (in region I, Fig. 1) the only stable state is $\Omega_{\mathrm{CP}}(0)$, i.e., the insulator phase. On line 2 (in region II, Fig. 1) there are two stable states, $\Omega_{\mathrm{CP}}(0)$ and $\Omega_{\mathrm{CP}}\left(\xi_{2}\right), \Omega_{\mathrm{CP}}(0)<\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$. This implies that the insulator phase is more stable than the conductive plasma phase (metastable state) until on line 3, where $\Omega_{\mathrm{CP}}(0)$ and $\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$ reach equilibrium, i.e., $\Omega_{\mathrm{CP}}(0)=\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$. A phase transition occurs from region I to region II, i.e., from the insulator phase to the coexisting phase. As mentioned above, corresponding to this phase transition, the screening length $\lambda$ changes discontinuously except at $z=z^{*}$. On line 4 (in region III, Fig. 1) there are still two stable-state phases $\Omega_{\mathrm{CP}}(0)$ and $\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$, but $\Omega_{\mathrm{CP}}(0)>\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$, which means that the conductive plasma is more stable than the insulator phase; the latter is a metastable state. On line 5 (in region IV, Fig. 1) there is only one stable state $\Omega_{\mathrm{CP}}\left(\xi_{2}\right)$, which is the conductive plasma phase; hence a phase transition occurs from region III to IV, i.e., from the coexisting phase to the conductive plasma phase. The corresponding phase-transition line is the dot-dashed line 4 (Fig. 1). From line 2 to line 4 in Fig. 5 we see clearly a first-order phase transition, which is obviously different from the KT transition. One find that the curves for both continuous and first-order phase transitions are closely similar to those of the phenomenological Landau theory. $^{14}$

It should be pointed out that the first-order transition lines and the KT transition line join smoothly (i.e., with the same tangents) at the tricritical point $a\left(z^{*}, T^{*}\right)$ in Fig. 1. The physics behind the implied change of behavior at this point may be expressed as follows: As $T=T^{*}+\delta$ approaches $T^{*}$ with $z<z_{*}$, the phase transition is continuous, while for $z>z^{*}$ this phase transition is discontinuous. But as $z \rightarrow z^{*}$ the discontinuity gradually disappears. This picture is qualitatively similar to that of Minnhagen and Wallin. $^{3}$

## IV. CONCLUSION

We have used the ground-state properties of the sineGordon model with the help of a Gaussian wave functional to analyze the phase transitions of the 2D CPM. We find that at small fugacity the charge-unbinding process corresponds to a Kosterlitz-Thouless transition, while at large fugacity the transition is of first order. We may identify $\Omega_{\mathrm{CP}}(\xi)$ and $\xi$ as the free energy and the order parameter respectively; then both types of phase transitions shown in Fig. 4 and 5 bear close similarity to those of the phenomenological Landau theory. We believe this is due to the fact that the Gaussian wave-functional method is essentially a kind of mean-field approximation which self-consistently sums up all orders of tadpole diagrams of the sine-Gordon model.

We also notice that, unlike the situation at higher dimensions, here the (high-temperature) plasma phase appears at high density, while the condensed-dipole phase appears at low density. The results based on renormalization-group methods and numerical computa-

![](./images/812771672389058560_5.jpg)

FIG. 5. First-order phase transition for $z>z^{*}$. (a) Line 1 is in the region I in Fig. 1, line 2 is in the region II, line 3 corresponds to line 3 in Fig 1, line 4 is in the region II, and line 5 in the region IV. (b) The details of (a) in the neighborhood of the origin.

tion show the same tendency. This is due to the special characteristics of the two-dimensional system, in which the competing entropy and energy both behave like $\ln V$; at the critical temperature the phase diagram is deter- mined by the higher-order contributions. In contrast, in a three-dimensional model the entropy changes more rap- idly with increasing volume than the energy, and hence low density is always unfavorable for the condensed phase.

## ACKNOWLEDGMENTS
This project was supported by the Science Fund of the National Education Committee.

$^{1}$P. Minnhagen, Rev. Mod. Phys. 59, 1001 (1987); Phys. Rev. Lett. 54, 2351 (1985); Phys. Rev. B 32, 3088 (1985).
$^{2}$P. Minnhagen, A. Rosengren, and G. Grinstein, Phys. Rev. B 18, 1356 (1978).
$^{3}$P. Minnhagen and M. Wallin, Phys. Rev. B 40, 5109 (1989).
$^{4}$J. M. Kosterlitz and D. J. Thouless, Phys. Rev. B 6, 1181 (1973).
$^{5}$J. M. Kosterlitz, J. Phys. C 7, 1046 (1973).
$^{6}$J. M. Calillo and D. Levesque, Phys. Rev. B 33, 499 (1986).
$^{7}$R. Ingermanson, Nucl. Phys. B 266, 620 (1986).
$^{8}$P. M. Stevenson, Phys. Rev. D 32, 1389 (1985).

$^{9}$D. J. Amit, *Field Theory, the Renormalization Group and Criti- cal Phenomena* (World Scientific, Singapore, 1984).
$^{10}$D. J. Amit, Y. Y. Goldschmidt, and G. Grinstein, J. Phys. A 13, 585 (1980).
$^{11}$S. Coleman, Phys. Rev. D 11, 2088 (1975).
$^{12}$B. W. Xu and Y. M. Zhang, J. Phys. A 25, 1039 (1992).
$^{13}$Y. M. Zhang, M. L. Zhou, and B. W. Xu, Phys. Rev. 47, 898 (1993).
$^{14}$J. C. Toledano and Toledano, *The Landau Theory of Phase Transitions* (World Scientific, Singapore, 1987).