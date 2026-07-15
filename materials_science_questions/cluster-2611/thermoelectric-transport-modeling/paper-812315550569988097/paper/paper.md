![](./images/812315550569988097_1.jpg)

Available online at www.sciencedirect.com

![](./images/812315550569988097_2.jpg)

International Journal of Heat and Mass Transfer 48 (2005) 413-418

![](./images/812315550569988097_3.jpg)

www.elsevier.com/locate/ijhmt

# The influence of the Thomson effect on the performance of a thermoelectric cooler

Mei-Jiau Huang $^{a,*}$, Ruey-Hor Yen $^{a}$, An-Bang Wang $^{b}$

$^{a}$ Mechanical Engineering Department, National Taiwan University, 106 Taiwan, ROC
$^{b}$ Institute of Applied Mechanics, National Taiwan University, 106 Taiwan, ROC

Received 1 May 2004

## Abstract

The temperature distribution of a thermoelectric cooler under the influence of the Thomson effect, the Joule heating, the Fourier's heat conduction, and the radiation and convection heat transfer is derived. The influence of the Thomson effect on the temperature profiles, on the fraction of the Joule's heat that flows back to the low-temperature side, and consequently on the maximum attainable temperature difference and the maximum allowable heat load are emphasized and explored. The results suggest that the cooling efficiency of a thermoelectric cooler can be improved not only by increasing the figure-of-merit of the thermoelectric materials but also by taking advantage of the Thomson effect. A possible development direction for the thermoelectric materials is thus given.

© 2004 Elsevier Ltd. All rights reserved.

Keywords: Thermoelectric cooler; Thomson effect; Thermal analysis

---

## 1. Introduction

A thermoelectric cooler pumps heat, when the electricity is applied, from a low temperature reservoir to a high temperature reservoir through the Peltier effect [1]. Compared to the traditional heat pumps, the thermoelectric cooler has the advantages of compact, high reliability, low maintenance fee, no vibration and easy control (because of no moving parts), no refrigerants and direct electric energy conversion. The major problem of thermoelectric devices is poor cooling efficiency. This is fundamentally limited by the material properties of the n- and p-type semiconductors, regardless how clever the device has been engineered. The performance of a thermoelectric material is measured by a dimensionless thermoelectric parameter, usually written as $ZT$, where $T$ is the temperature (usually the room temperature) and $Z$ characterizes the material's electric and thermal transport properties and is commonly named as the figure of merit of the material. The commonly known thermoelectric materials have $ZT$ values between about 0.6 and 1.0. Different efforts have been made to produce semiconductor materials with large Seebeck coefficients, good electrical conductivity, and poor thermal conductivity [2-5].

It is worthy to note here that most previous investigations [6-8] of the thermoelectric coolers considered only the Fourier's heat conduction and the Joule's heating. The radiation and convection heat transfers between the semiconductors and the ambient gas are found not

* Corresponding author. Tel.: +886 2 23673984; fax: +886 2 23631755.
E-mail address: mjhuang@ntu.edu.tw (M.-J. Huang).

0017-9310/$ - see front matter © 2004 Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijheatmasstransfer.2004.05.040

negligible for micro-coolers [7,8]. Little attention how-ever has been paid to the influence of the Thomson effect (charge carriers must release or absorb heat in order to overcome the non-homogeneity caused by the temperature gradients in the semiconductors) until recently [9,10]. In the present work, the influence of the Thomson effect on the performance of a thermoelectric cooler, such as its maximum attainable temperature difference and maximum allowable heat load, is of interest and investigated. These results provide the theoretical bases for the possible development of thermoelectric materials and for an optimal design of a thermoelectric cooler.

## 2. Thermal model

The basic unit of a thermoelectric cooler (TE cooler) is a thermocouple composed primarily of an n-type and a p-type semiconductor element placed electrically in series and thermally in parallel, as shown in Fig. 1. The attempt is to pump heat from the cold side ($x=0$) through the Peltier heat, transfer it to the hot side ($x=L$) by current, and finally release it to the ambient by some external cooling device. The cooling power however cannot be as large as the Peltier heat pumping rate, because additional heat sources such as the Joule's dissipation heat and the Thomson heat are generated and heat will diffuse back to the cold side through the Fourier's heat conduction. In the present study, a one-dimensional analysis will be employed, which is proper when the length of the beam is sufficiently larger than its width and thickness. According to the nonequilibrium thermodynamics, the steady temperature distribution $T(x)$ is governed by

$$
0=\frac{\mathrm{d}}{\mathrm{d} x}\left(\lambda A \frac{\mathrm{d} T}{\mathrm{~d} x}\right)+\frac{e_{\mathrm{e}}^{2} j_{\mathrm{e}}^{2}}{\sigma} A \mp \frac{\mathrm{d}}{\mathrm{d} x}\left(\beta e_{\mathrm{e}} j_{\mathrm{e}} T A\right)-\gamma P\left(T-T_{\infty}\right)
\tag{1}
$$

Terms on the right-hand-side represent respectively the net axial thermal conduction heat transfer rate, the Joule's heat generation rate, the Thomson heat generation rate, and the thermal radiation and convection heat transfer rates. Symbols $\lambda$ and $\sigma$ represent the thermal and electrical conductivities; $e_{\mathrm{e}}$ and $j_{\mathrm{e}}$ are the electron charge and flux (therefore the current is $I=A e_{\mathrm{e}} j_{\mathrm{e}}$); $\beta$ is the Thomson coefficient; $A$ and $P$ are the local cross-sectional area and perimeter of the semiconductor element. The sign of the term associated with the Thomson heat depends on the current direction. It is a minus if the current flows in the positive $x$-direction (the p-type element in Fig. 1); and a plus otherwise (n-type). Finally, the radiation heat transfer rate has been linearized under the assumption of small temperature difference and combined with the convection heat transfer coefficient $h$ such that $\gamma \equiv 4 \varepsilon \sigma_{\mathrm{B}} T_{\infty}^{3}+h$, where $\varepsilon$, $\sigma_{\mathrm{B}}$, and $T_{\infty}$ are the emissivity, the Stefan-Boltzman constant, and the ambient gas temperature.

Further simplifications can be made by assuming constant properties ($\lambda$, $\beta$, and $\sigma$), constant $A$ and $P$, and constant current $I$. Emphasized is the assumption of constant Thomson coefficient. By definition, the Thomson coefficient $\beta$ is related to the Seebeck coefficient $\alpha$ by

$$
\beta=T\left(\frac{\partial \alpha}{\partial T}\right)_{p}
\tag{2}
$$

where the subscription " $p$ " represents a constant pressure condition under which the derivative is taken. Therefore, a constant Seebeck coefficient means an absence of the Thomson effect. On the other hand, a constant Thomson coefficient implies a Seebeck coefficient having a logarithm dependence on the temperature.

### 2.1. Thomson effect on the temperature profiles

With the boundary conditions $T(0)=T_{\mathrm{c}}$ and $T(L)=T_{\mathrm{h}}$, the solution of Eq. (1) is

$$
\begin{aligned}
\Theta\left(x^{*}\right)= & \frac{\mathrm{e}^{\kappa_{1} x^{*}}-\mathrm{e}^{\kappa_{2} x^{*}}}{\mathrm{e}^{\kappa_{1}}-\mathrm{e}^{\kappa_{2}}} \\
& +\Theta_{\mathrm{c}}\left\{\frac{\left(1-\mathrm{e}^{\kappa_{2}}\right) \mathrm{e}^{\kappa_{1} x^{*}}-\left(1-\mathrm{e}^{\kappa_{1}}\right) \mathrm{e}^{\kappa_{2} x^{*}}}{\mathrm{e}^{\kappa_{1}}-\mathrm{e}^{\kappa_{2}}}\right\} \\
& +\frac{\Psi}{P^{*}}\left\{1-\frac{\left(1-\mathrm{e}^{\kappa_{2}}\right) \mathrm{e}^{\kappa_{1} x^{*}}-\left(1-\mathrm{e}^{\kappa_{1}}\right) \mathrm{e}^{\kappa_{2} x^{*}}}{\mathrm{e}^{\kappa_{1}}-\mathrm{e}^{\kappa_{2}}}\right\}
\end{aligned}
\tag{3}
$$

![](./images/812315550569988097_4.jpg)

Fig. 1. Schematic diagram of a thermoelectric cooler.

where $x^{*} \equiv x/L$, $\Theta \equiv (T-T_{\infty})/\Delta T$, $\Theta_{\mathrm{c}}=(T_{\mathrm{c}}-T_{\infty})/\Delta T$, $\Delta T \equiv T_{\mathrm{h}}-T_{\mathrm{c}}$, $P^{*} \equiv P\gamma L/K$, and $\Psi \equiv I^{2}R/K\Delta T$. Symbols $R \equiv L/\sigma A$ and $K \equiv \lambda A/L$ are the electric resistance and thermal conductance of thermoelement. The dimensionless parameters $\kappa_{1}$ and $\kappa_{2}$ are the two distinct real roots of
$$0=\kappa^{2} \mp \xi \kappa-P^{*}\qquad(4)$$
with $\xi \equiv \beta I/K$ representing the ratio of Thomson heat to the conduction heat. Noticed is that the parameters $\kappa_{1}$ and $\kappa_{2}$ are now both functions of the operating current $I$ because of the Thomson effect.

To highlight the influence of the Thomson effect on the temperature distribution, we choose $\gamma=0$ for the time being. The two roots of Eq. (4) are then $\pm \xi$ and 0 and the temperature distribution becomes
$$\frac{T(x)-T_{\mathrm{c}}}{T_{\mathrm{h}}-T_{\mathrm{c}}}=(1 \mp \zeta) \cdot \frac{1-\exp \left( \pm \xi \frac{x}{L} \right)}{1-\exp( \pm \xi )} \pm \zeta \frac{x}{L}\qquad(5)$$
for the p-type/n-type element with $\zeta \equiv I^{2}R/\beta I\Delta T$ being the ratio of Joule's heat to the Thomson heat. Noticed is that two influence dimensionless parameters, $\xi$ and $\zeta$, appear separately, unlike the case when the Thomson effect is ignored and the temperature profile is then
$$\frac{T(x)-T_{\mathrm{c}}}{T_{\mathrm{h}}-T_{\mathrm{c}}}=\frac{1}{2} \xi \zeta\left(\frac{x}{L}-\frac{x^{2}}{L^{2}}\right)+\frac{x}{L}\qquad(6)$$
where $\xi \zeta=\Psi$ is the ratio of the Joule's heat to the conduction heat. Shown in Fig. 2 are temperature profiles of the p-type element under several values of the Thomson coefficients. As seen, when the Thomson coefficient is negative $(\beta_{\mathrm{p}}<0)$, the temperature near the cold side is increased by the Thomson heat released by the charge carriers. This temperature rise will make a reduction in the cooling power of the TE cooler. On the other hand, if $\beta_{\mathrm{p}}>0$, the temperature gradient is everywhere positive and charge carriers absorb heat all the way as the current moves from $x=0$ to $x=L$. This implies that most of the Joule's heat and the Fourier's conduction heat are luckily absorbed and carried to the hot side by the charge carriers. Therefore, for the sake of improving the cooling power, a TE cooler should employ a p-type (n-type) semiconductor material with a positively (negatively) large Thomson coefficient, in addition to a low electric resistance and a low thermal conductance.

![](./images/812315550569988097_5.jpg)

Fig. 2. The influence of Thomson effect on the temperature profiles where $\Psi=2$ and $-6 \leqslant \xi_{p} \leqslant 6$ are chosen.

### 2.2. Thomson effect on the cooling power

The cooling power $(q_{\mathrm{c}})$ is the net heat flow rate out of the cold side and is computed as
$$q_{\mathrm{c}}=\alpha_{\mathrm{pN}}(T_{\mathrm{c}})I T_{\mathrm{c}}-\lambda_{\mathrm{p}}A_{\mathrm{p}} \frac{\mathrm{d}T_{\mathrm{p}}}{\mathrm{d}x}(0)-\lambda_{\mathrm{n}}A_{\mathrm{n}} \frac{\mathrm{d}T_{\mathrm{n}}}{\mathrm{d}x}(0)\qquad(7)$$
where $\alpha_{\mathrm{pN}} \equiv \alpha_{\mathrm{p}}-\alpha_{\mathrm{n}}$, and subscripts $\mathrm{p}$ and $\mathrm{n}$ represent p-type and n-type materials respectively. Using Eq. (3), it can be shown that the cooling power is equal to
$$q_{\mathrm{c}}=\alpha_{\mathrm{pN}}(T_{\mathrm{c}})I T_{\mathrm{c}}-\widetilde{K}(T_{\mathrm{h}}-T_{\mathrm{c}})-\widetilde{H}(T_{\infty}-T_{\mathrm{c}})-I^{2}\widetilde{R},\qquad(8)$$
where
$$\widetilde{K} \equiv K_{\mathrm{p}}f(\kappa_{\mathrm{p}1},\kappa_{\mathrm{p}2})+K_{\mathrm{n}}f(\kappa_{\mathrm{n}1},\kappa_{\mathrm{n}2})\qquad(9)$$

$$\widetilde{H} \equiv K_{\mathrm{p}}g(\kappa_{\mathrm{p}1},\kappa_{\mathrm{p}2})+K_{\mathrm{n}}g(\kappa_{\mathrm{n}1},\kappa_{\mathrm{n}2})\qquad(10)$$

$$\widetilde{R} \equiv R_{\mathrm{p}}h(\kappa_{\mathrm{p}1},\kappa_{\mathrm{p}2})+R_{\mathrm{n}}h(\kappa_{\mathrm{n}1},\kappa_{\mathrm{n}2})\qquad(11)$$
and functions $f$, $g$, and $h$ are defined as
$$f(\kappa_{1},\kappa_{2}) \equiv \frac{\kappa_{1}-\kappa_{2}}{\mathrm{e}^{\kappa_{1}}-\mathrm{e}^{\kappa_{2}}}\qquad(12)$$

$$g(\kappa_{1},\kappa_{2}) \equiv \frac{\kappa_{1}\mathrm{e}^{\kappa_{2}}-\kappa_{2}\mathrm{e}^{\kappa_{1}}}{\mathrm{e}^{\kappa_{1}}-\mathrm{e}^{\kappa_{2}}}-f(\kappa_{1},\kappa_{2})\qquad(13)$$

$$h(\kappa_{1},\kappa_{2}) \equiv-\frac{g(\kappa_{1},\kappa_{2})}{\kappa_{1}\kappa_{2}}\qquad(14)$$

Firstly of all, it is noticed that the fraction of Joule's heat flowing to the cold side is no longer one half as usual when no Thomson effect is concerned. Instead, it is determined by the function $h(\kappa_{1},\kappa_{2})$ which ranges between 0 and 1. The influence of the radiation and convection heat transfer lies not only in $\widetilde{H}$ but also in $\widetilde{K}$ and $\widetilde{R}$ because $\kappa_{1}$ and $\kappa_{2}$ are also functions of $\gamma$ as observed from Eq. (4).

Again, to illuminate the Thomson effect, we stick to cases in which $\gamma=0$. In those cases, $\widetilde{H}=0$ and the so-called herein modified thermal conductance $\widetilde{K}$ and the modified electric resistance $\widetilde{R}$ become
$$\widetilde{K}=K_{\mathrm{p}}\eta_{K}(\xi_{\mathrm{p}})+K_{\mathrm{n}}\eta_{K}(-\xi_{\mathrm{n}})\qquad(15)$$

$$\widetilde{R}=R_{\mathrm{p}}\eta_{R}(\xi_{\mathrm{p}})+R_{\mathrm{n}}\eta_{R}(-\xi_{\mathrm{n}})\qquad(16)$$

![](./images/812315550569988097_6.jpg)

Fig. 3. The dependence of $\eta_{\text{K}}$ and $\eta_{\text{R}}$ on the dimensionless operating current $\xi$.

where
$$
\eta_{K}(\xi)=\frac{\xi}{\mathrm{e}^{\xi}-1} \approx 1-\frac{\xi}{2} \quad \text { as } \xi \ll 1
$$

$$
\eta_{R}(\xi)=\frac{1}{1-\mathrm{e}^{\xi}}+\frac{1}{\xi} \approx \frac{1}{2}-\frac{\xi}{12} \quad \text { as } \xi \ll 1.
$$

A value of $\eta_{K}$ greater than one implies the additional (Thomson) heat that must diffuse to the cold side through the Fourier's conduction. The value of $\eta_{R}$ $(0 \leqslant \eta_{R} \leqslant 1)$ on the other hand tells the fraction of Joule's heat that will flow to the cold side. Fig. 3 shows the dependence of $\eta_{K}$ and $\eta_{R}$ on $\xi$, the operating current nondimensionalized in terms of the thermal conductance and the Thomson coefficient. It is seen that both the modified thermal conductance and the modified electric resistance can be significantly reduced by properly choosing semiconductor materials with $\beta_{\mathrm{p}}>0$ and $\beta_{\mathrm{n}}<0$.

## 3. Performance

Given a temperature difference $\Delta T=T_{\mathrm{h}}-T_{\mathrm{c}}$, there may exist some optimum operating current that maximizes $q_{\mathrm{c}}$. The maximum attainable temperature difference $\Delta T_{\max }$ is the temperature difference when the corresponding maximum $q_{\mathrm{c}}$ is zero. And the maximum allowable heat load $N_{\max }$ is defined as the maximum cooling power when $\Delta T=0$. The involved algebra is a little troublesome because the modified thermal conductance and modified electric resistance are now functions of $I$. For simplicity and for the sake of illuminating the Thomson effect, $\gamma=0$ is assumed again. Also assumed is that the p-type and n-type materials have the same constant thermoelectric properties except that $\alpha_{\mathrm{pn}}\left(T_{\mathrm{c}}\right)=2 \alpha\left(T_{\mathrm{c}}\right)>0$ and $\beta_{\mathrm{p}}=-\beta_{\mathrm{n}}=\beta>0$.

### 3.1. Maximum attainable temperature difference

After some algebra, it can be shown that the maximum attainable temperature difference $\Delta T_{\max }$ and the corresponding optimum operating current $I_{\text {opt.T }}$ are determined by
$$
Z T_{\mathrm{c}}=\frac{\alpha}{\beta}\left(1-\mathrm{e}^{-\xi_{\text {opt.T }}}\right)
$$

$$
Z \Delta T_{\max }=\frac{\alpha^{2}}{\beta^{2}}\left(\xi_{\text {opt.T }}+\mathrm{e}^{-\xi_{\text {opt.T }}}-1\right)
$$

where $\xi_{\text {opt.T }}=\beta I_{\text {opt.T }} / K$ and $Z=\sigma \alpha^{2} / \lambda$ is the Figure-ofMerit evaluated at $T_{\mathrm{c}}$. The influence of the Thomson effect can be explained in the following way. Given $T_{\mathrm{c}}$ and $\alpha\left(T_{\mathrm{c}}\right)$, Eq. (19) gives the $\beta$-dependent optimum dimensionless operating current and Eq. (20) in turn gives the maximum attainable temperature difference. Moreover, from Eq. (19), it is seen that when $Z T_{\mathrm{c}}$ is less than the value of $\alpha / \beta$ (or $T_{\mathrm{c}}$ is less than $\lambda / \sigma \alpha \beta$ ), there exists an $\xi_{\text {opt.T }}$ with a corresponding maximum attainable temperature difference. Otherwise, there exists no so-called optimum operating current and there is no limit on the temperature difference. This is because most of the Joule's heat will just be absorbed as Thomson heat and carried to the hot side by the current, becoming not an obstacle in creating the desired temperature difference. All of the above are illustrated in Fig. 4. In remark, both parameters, $Z T_{\mathrm{c}}$ and $\alpha / \beta$, play roles in determining the performance of a thermoelectric cooler.

![](./images/812315550569988097_7.jpg)

Fig. 4. The maximum attainable temperature difference $Z \Delta T_{\max }$ versus $Z T_{\mathrm{c}}$. Values of $\alpha / \beta$ range in a geometric progression with a ratio of 1.6 starting from 0.2. The dotted curve is the one corresponding to $\beta=0$ (or $\alpha / \beta=\infty$).

### 3.2. Maximum allowable heat load

Using Eqs. (8) and (15)-(18), the maximum allowable heat load $N_{\max}$ can be found to be
$$
\frac{\beta^{2}}{\alpha^{2}} N_{\max }^{*}=\frac{2 \xi_{\text {opt.N }}^{2}}{\left(1-\mathrm{e}^{\xi_{o p t, N}}\right)}\left(1+\frac{\xi_{\text {opt.N }} \mathrm{e}^{\xi_{\text {opt.N }}}}{\left(1-\mathrm{e}^{\xi_{\text {opt.N }}}\right)}\right)
\tag{21}
$$

$$
\frac{\beta}{\alpha} Z T_{\mathrm{h}}=1+\frac{2 \xi_{\text {opt.N }}^{2}}{1-\mathrm{e}^{\xi_{\text {opt.N }}}}+\frac{\xi_{\text {opt.N }}^{2} e^{\xi_{\text {opt.N }}}}{\left(1-\mathrm{e}^{\xi_{\text {opt.N }}}\right)^{2}}
\tag{22}
$$
where $N_{\max }^{*} \equiv Z N_{\max } / K$ and $\xi_{\text {opt.N }} \equiv \beta I_{\text {opt.N }} / K$ (the optimum dimensionless operating current that results in a maximum allowable heat load), and is shown in Fig. 5.
A careful examination of Eq. (21) finds that there exist two critical values of $Z T_{\mathrm{h}} \beta / \alpha$, namely $Z T_{\mathrm{h}} \beta / \alpha=1$ and $Z T_{\mathrm{h}} \beta / \alpha \approx 1.18$. When $Z T_{\mathrm{h}} \beta / \alpha \leqslant 1$, there exists an optimum operating current $\xi_{\text {opt.N }}$ and a corresponding maximum heat load $N_{\max }^{*}$. As $1<Z T_{\mathrm{h}} \beta / \alpha<1.18$, there is a local maximum heat load at some operating current and a local minimum heat load at some larger operating current. As the operating current becomes even larger, the allowable heat load increases monotonically. These local extremes are presented by the two branches in the region of $1<Z T_{\mathrm{h}} \beta / \alpha<1.18$ in Fig. 5. When $Z T_{\mathrm{h}} \beta / \alpha>1.18$, the heat load increases monotonically with the operating current and there exists thus no so-called maximum allowable heat load. All of the above situations are shown in Fig. 6, in which the dimensionless heat load, $N^{*}=Z N / K$, is plotted as a function of the dimensionless operating current under the constraint $\Delta T=0$ for several values of $Z T_{\mathrm{h}} \beta / \alpha$.

It is not so obvious however why the Thomson effect can enhance the cooling power since the total Thomson heat carried away by the current is in fact zero ($\beta I \Delta T=0$). Recalled is that the Thomson effect can change the temperature profiles (as investigated in Section 2.1) and therefore direct a major portion of the Joule's heat flowing to the hot side (in the sense that charge carriers absorb heat near the cold side and release the same amount of heat in the neighborhood of the hot side). The cooling power is thus increased. When the Thomson effect is sufficiently strong ($Z T_{\mathrm{h}} \beta / \alpha>1$), the fraction of Joule's heat and the Fourier's conduction heat flowing to the cold side become negligible and consequently the cooling power (or the allowable heat load) can be made almost equal to the Peltier heat, which is in turn proportional to the operating current. This limiting behavior however can be only slowly approached as seen from Fig. 3 or from Eq. (18) (i.e. $\eta_{R} \approx 1 / \xi$ as $\xi \gg 1$.)

![](./images/812315550569988097_8.jpg)

Fig. 5. The extreme values of allowable heat load under the constraint $\Delta T=0$ versus $Z T_{\mathrm{h}} \beta / \alpha$. Dotted line is the result without considering Thomson effect.

![](./images/812315550569988097_9.jpg)

Fig. 6. The allowable heat load under the constraint $\Delta T=0$ as a function of the operating current for various values of $Z T_{\mathrm{h}} \beta / \alpha$.

### 4. Illustration

At the end of this paper, we illustrate the present analysis by an example. The properties of the p-type and n-type elements are so chosen [7,8] that, $\sigma_{\mathrm{p}}=$ $\sigma_{\mathrm{n}}=0.1 \quad(\mu \Omega \mathrm{m})^{-1}, \quad \lambda_{\mathrm{p}}=\lambda_{\mathrm{n}}=1.6 \mathrm{W} / \mathrm{mK}, \quad \alpha_{\mathrm{p}}=-\alpha_{\mathrm{n}}=\alpha$, and finally $\beta_{\mathrm{p}}=-\beta_{\mathrm{n}}=\beta>0$. The geometry is chosen to be $L_{\mathrm{p}}=L_{\mathrm{n}}=1 \mathrm{mm}, P_{\mathrm{p}}=P_{\mathrm{n}}=0.4 \mathrm{mm}$, and $A_{\mathrm{p}}=A_{\mathrm{n}}=$ $0.01 \mathrm{mm}^{2}$ The radiation-convection heat transfer coefficient is $\gamma=50 \mathrm{W} / \mathrm{m}^{2} \mathrm{K}$ (a reasonable value for air at normal atmosphere). The ambient temperature $T_{\infty}$ is taken to be 300 K.

Fig. 7 shows the temperature difference as a function of the operating current when no heat load is applied. The cold-side temperature is fixed at 250 K and $\alpha\left(T_{\mathrm{c}}\right)=185 \mu \mathrm{V} / \mathrm{K}$ is assumed. As seen, when the Thomson effect is ignored, the optimum current is about 0.051 A and the maximum temperature difference is about 55 K. The value of $2 \Delta T_{\max } / T_{\mathrm{c}}$ is about 0.44, which

![](./images/812315550569988097_10.jpg)

Fig. 7. The attained temperature difference versus the operating current under no heat load. The Thomson coefficients are given in μV/K.

is smaller than $ZT_{c}$≈0.53 because of the convection and radiation effect. The maximum attainable temperature difference is seen to increase with increasing Thomson coefficient. It is about 114K (2Δ$T_{max}$/$T_{c}$≈0.91) when β=200 μV/K. Finally, the temperature difference becomes unlimited when β is slightly larger than the critical value of $\lambda/\sigma\alpha T_{\mathrm{c}}\approx346\,\mu\mathrm{V/K}$.

## 5. Conclusion
A one-dimensional thermal analysis for the performance of thermoelectric cooler has been conducted under the influence of the Thomson effect, the Joule heating, the Fourier's heat conduction, and the radiation and convection heat transfer. The temperature distribution and the cooling power are analytically derived. For those cases that the Thomson effect is important, two dimensionless influence parameters, i.e., the ratio of the Thomson heat to the conduction heat and the ratio of Joule's heat to the Thomson heat, play roles. Both of the temperature distribution and the cooling power are affected by the Thomson effect. The fraction of both Fourier's conduction heat and Joule's heat that flows back to the cold side can be significantly reduced. It results in higher values of maximum attainable temperature difference and the maximum allowable heat load, providing that the thermoelectric cooler has p-type (n-type) semiconductor material with the positive (negative) Thomson coefficient.

Although a material with a significant Thomson effect is still limited due to the material capability at the present time, however this paper has highlighted a possible development direction for the thermoelectric materials in the future. For example, it was shown [11] that the Seebeck coefficient of a one-band (parabolic band) bulk material is determined by

$$
\alpha=-\frac{k_{\mathrm{B}}}{\mathrm{e}}\left(\frac{5 F_{3 / 2}}{3 F_{1 / 2}}-\zeta^{*}\right)\qquad(23)
$$

where $\zeta^{*}=\zeta^{*}(T)$ is the Fermi energy nondimensionalized by $k_{B}T$ and

$$
F_{i}=F_{i}\left(\zeta^{*}\right)=\int_{0}^{\infty} \frac{x^{i} \mathrm{~d} x}{\exp \left(x-\zeta^{*}\right)+1}\qquad(24)
$$

Equation (23) suggests that it may be possible to control the temperature dependence (derivative) of the Seebeck coefficient (and thus control the Thomson coefficient) through a control of the Fermi energy and even its temperature dependence, say by doping.

## Acknowledgment
The support of this work by the National Science Council, Taiwan, ROC under contract NSC 92-2212-E-002-047 and ITRI under the contract 3000017521 are gratefully acknowledged.

## References
[1] A.I. Burshteyn, Semiconductor Thermoelectric Devices, Temple press, London, 1964.
[2] D.M. Rowe, CRC Handbook of Thermoelectrics, CRC Press LLC, 1995.
[3] D.G. Cahill, K. Goodson, A. Majumdar, Thermometry and thermal transport in micro/nanoscale solid-state devices and structures, J. Heat Transfer 124 (2002) 223-241.
[4] J.P. Fleurial, New thermoelectric materials and devices: New challenges, UCLA, 1997.
[5] R.G. Mahtur, R.M. Mehra, Thermoelectric power in porous silicon, J. Appl. Phys. 83 (1998) 5855-5857.
[6] C. LaBounty, A. Shakouri, J.E. Bowers, Design and characterization of thin film microcoolers, J. Appl. Phys. 89 (2001) 4059-4064.
[7] F. Völklein, Gao Min, D.M. Rowe, Modelling of a mircoelectromechanical thermoelectric cooler, Sensors and Actuators 75 (1999) 95-101.
[8] D.J. Yao, In-plane MEMS thermoelectric mircocooler, Ph.D. Dissertation, UCLA, 2001.
[9] S. Wisniewski, B. Staniszewski, R. Szymanik, Thermodynamics of Nonequilibrium Processes, PWN-Polish Scientific Publishers, 1976.
[10] J. Chen, Z. Yan, L. Wu, The influence of Thomson effect on the maximum power output and maximum efficiency of a thermoelectric generator, J. Appl. Phys. 79 (1996) 8823-8828.
[11] L.D. Hicks, M.S. Dresselhaus, Effect of quantum-well structures on the thermoelectric figure of merit, Phys. Rev. B 47 (1993) 12727-12731.