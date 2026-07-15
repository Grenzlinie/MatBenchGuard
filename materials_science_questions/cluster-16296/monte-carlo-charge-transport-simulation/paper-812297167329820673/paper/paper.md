# Model spectral density for hot-electron quantum transport

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1988 Phys. Scr. 38 117

(http://iopscience.iop.org/1402-4896/38/1/022)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 142.132.1.147
This content was downloaded on 25/08/2015 at 11:57

Please note that [terms and conditions apply]().

Physica Scripta. Vol. 38, 117-121, 1988.

# Model Spectral Density for Hot-Electron Quantum Transport*

Lino Reggiani and Paolo Lugli

Dipartimento di Fisica e Centro Interuniversitario di Struttura della Materia, Universita' di Modena, Via Campi 213/A, 41100 Modena, Italy

and

Antti Pekka Jauho

Physics Laboratory, University of Copenhagen, H.C. Ørsted Institute, Universitetsparken 5, DK-2100 Copenhagen, Denmark

Received May 26, 1987; accepted January 20, 1988

## Abstract
Quantum transport theory indicates that a proper treatment of high-field transport in semiconductors should include collisional broadening and intra-collisional field effects. By using the Generalized Kadanoff-Baym method, we construct a computational scheme which includes both of these effects. The central quantity in our theory is the joint spectral density $K(k, k')$ which describes the relation between the initial and final kinetic momenta in a scattering event. Analytical and numerical analyses for several models of interest are presented and discussed.

## 1. Introduction
The fast development in the field of submicron devices has provided a renewed interest in the theory of electron transport beyond the free particle approach, that is beyond the semiclassical Boltzmann equation [1]. The authors [2] have recently derived a quantum kinetic equation which accounts for genuine quantum effects through the introduction of the spectral density $A(k, t)$, $k$ being the kinetic momentum and $t$ the time (herewith we employ the notation introduced by Jauho and Wilkins [3] with $\hbar = e = m_0 = 1$). Our scheme can be included in an ensemble Monte Carlo program thus enabling one to give quantitative estimates of the importance of collisional broadening (CB) and/or intra-collisional field effects (ICFE). Therefore, it is the aim of this paper to derive spectral density models with increasing degree of sophistication and thus accounting for the energy dependence of the collision rate, ICFE and CB.

In Section 2 we survey the quantum kinetic equation at the basis of the theory. In Section 3 we give the prescription for the calculation of the quantities of interest in terms of the appropriate Dyson's equation. In Section 4 we obtain analytical expressions for the spectral density and the joint spectral density for increasingly complicated models. Then, in Section 5 a numerical example for a model semiconductor is reported.

## 2. Model
The theory is formulated in terms of the Generalized Kadanoff-Baym approach [3, 4]. Our physical model is based on the following assumptions:
(i) One isotropic band;
(ii) Time independent and space homogeneous conditions;
(iii) An ansatz which links the single particle Wigner distribution function $f(k)$ to the full correlation function $G^<(k, t)$
[5] $G^<(k, t) = iA(k, t)f(k - (E/2)|t|)$;
(iv) Completed collisions limit.

Within this model, the quantum kinetic Boltzmann equation for $f(k)$ writes [2]:
$$
\begin{align*}
f(\boldsymbol{k}) &= \int \mathrm{d}\boldsymbol{k}' \int_{0}^{\infty} \mathrm{d}t[W^{\mathrm{QM}}(\boldsymbol{k}' - \boldsymbol{E}t, \boldsymbol{k} - \boldsymbol{E}t)f(\boldsymbol{k}' - \boldsymbol{E}t) \\
&\quad - W^{\mathrm{QM}}(\boldsymbol{k} - \boldsymbol{E}t, \boldsymbol{k}' - \boldsymbol{E}t)f(\boldsymbol{k} - \boldsymbol{E}t)]. \tag{1}
\end{align*}
$$

The scattering probability per unit time $W^{\mathrm{QM}}$, for electron phonon interactions, is given by:
$$
W^{\mathrm{QM}}(\boldsymbol{k}_1, \boldsymbol{k}_2) = \sum_{\eta = \pm 1} |V(q)|^2(N_q + \frac{1}{2} + \frac{1}{2}\eta)K(\boldsymbol{k}_1, \boldsymbol{k}_2) \tag{2}
$$
where $K(\boldsymbol{k}_1, \boldsymbol{k}_2)$ is the joint spectral density of the quasi particle which, in the self-consistent Born approximation, is given by:
$$
\begin{align*}
K(\boldsymbol{k}_1, \boldsymbol{k}_2) &= \int_{0}^{\infty} \mathrm{d}t' \, 2\mathrm{Re} \bigg\{ A\bigg(\boldsymbol{k}_1 + \frac{\boldsymbol{E}}{2}t', t'\bigg) \\
&\quad \times A\bigg(\boldsymbol{k}_2 + \frac{\boldsymbol{E}}{2}t', -t'\bigg) \exp(-i\eta\omega_q t') \bigg\}. \tag{3}
\end{align*}
$$

The description of the physical processes is based on a quasi-particle picture, where $\boldsymbol{k}$ and $\boldsymbol{k}'$ are the quasi particle kinetic momenta before and after a scattering event, $q = |\boldsymbol{k} - \boldsymbol{k}'|$ is the transferred momentum, $\boldsymbol{E}$ is the external applied electric field, $|V(q)|^2$ the square of the matrix element for electron phonon collision, $N_q$ the equilibrium phonon population, $\omega_q$ the phonon energy involved in the collision, with $\eta = \pm 1$ referring respectively to emission and absorption processes.

The joint spectral density $K(\boldsymbol{k}_1, \boldsymbol{k}_2)$ is the central quantity in our approach, since it enables us to account for quantum corrections of the otherwise semiclassical free-particle picture.

## 3. The spectral density $A(k, t)$
In the framework of a many-body approach which uses a the Green function formalism [6], the spectral density is defined as:
$$
A(\boldsymbol{k}, t) = i[G^r(\boldsymbol{k}, t) - G^a(\boldsymbol{k}, t)] \tag{4}
$$
where $G^{r,a}(\boldsymbol{k}, t)$ is the retarded (advanced) Green function, respectively.

In the presence of a steady external electric field $\boldsymbol{E}$ and of collisions, $G^r(\boldsymbol{k}, t)$ obeys the Dyson's equation which, when

---
* Paper presented at the 7th General Conference on the CMD-EPS, Pisa, 7-10 April, 1987.

Physica Scripta 38

expressed in terms of gauge invariant variables, has the form:

$$
\begin{aligned}
G^{r}(\boldsymbol{k}, t)= & G_{E}^{r}(\boldsymbol{k}, t)+\iint \mathrm{d} t_{1} \mathrm{~d} t_{2} G_{E}^{r}\left(\boldsymbol{k}-\frac{\boldsymbol{E}}{2}\left(t-t_{1}\right), t_{1}\right) \\
& \times \Sigma^{r}\left(\boldsymbol{k}-\frac{\boldsymbol{E}}{2}\left(t_{2}-t_{1}\right), t-\left(t_{1}+t_{2}\right)\right) G^{r} \\
& \times\left(\boldsymbol{k}-\frac{\boldsymbol{E}}{2}\left(t_{2}-t\right), t_{2}\right).
\end{aligned}
$$

$\Sigma^{r}(\boldsymbol{k}, t)$ is the retarded self energy. The field dependent retarded Green function $G_{E}^{r}(\boldsymbol{k}, t)$ is given by [3]:

$$
G_{E}^{r}(\boldsymbol{k}, t)=-i \theta(t) \exp \left[-i \int_{-t / 2}^{t / 2} \mathrm{~d} u \varepsilon(\boldsymbol{k}-\boldsymbol{E} u)\right]
$$

where $\theta(t)$ is the unit step function, and $\varepsilon$ is the carrier kinetic energy.

An equivalent formulation of eqs. (4)-(6) in the frequency domain can be easily obtained through a Fourier transform- ation.

## 4. Applications

In the following, the explicit expressions for $G^{r}(\boldsymbol{k}, t), A(\boldsymbol{k}, t)$ and $K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)$ will be given for several cases of interest.

### 4.1. Free electrons

In the absence of collisions $\Sigma^{r}=0$, and for zero electric field eqs. (5) and (6) reduce to:

$$
A(\boldsymbol{k}, t)=\exp (-i \varepsilon t)
$$

$$
K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)=2 \pi \delta\left(\varepsilon-\varepsilon^{\prime}+\eta \omega_{q}\right) .
$$

Here a parabolic dispersion relation for the kinetic energy $\varepsilon$ is taken as $\varepsilon=k^{2} /(2 m)$, where $m$ is an electron effective mass. In eq. (8) $\varepsilon$ and $\varepsilon^{\prime}$ are respectively the initial and final kinetic energy of a scattering event. As expected, eq. (8) represents the golden rule result of energy conservation.

### 4.2. Free electrons with ICFE

For free electrons in the presence of an external electric field $\boldsymbol{E}$ we find that:

$$
G_{E}^{r}(\boldsymbol{k}, t)=-i \theta(t) \exp \left[-i\left(\varepsilon t+\frac{E^{2}}{24 m} t^{3}\right)\right]
$$

$$
A(\boldsymbol{k}, t)=\exp \left[-i\left(\varepsilon t+\frac{E^{2}}{24 m} t^{3}\right)\right]
$$

$$
\begin{aligned}
K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)= & \int_{0}^{\infty} \mathrm{d} t^{\prime} 2 \operatorname{Re}\left\{\exp \left[i\left(P t^{\prime}+\frac{Q}{2} t^{\prime 2}\right)\right]\right\} \\
= & \left(\frac{\pi}{|Q|}\right)^{1 / 2}\left\{\cos \left(\frac{P^{2}}{2|Q|}\right)\left[1-2 C\left(\frac{P Q}{\left(2|Q|^{3}\right)^{1 / 2}}\right)\right]\right. \\
& \left.+\sin \left(\frac{P^{2}}{2|Q|}\right)\left[1-2 S\left(\frac{P Q}{\left(2|Q|^{3}\right)^{1 / 2}}\right)\right]\right\}
\end{aligned}
$$

with

$$
P=\varepsilon^{\prime}-\varepsilon-\eta \omega_{q} ; \quad Q=\eta \frac{\boldsymbol{q} \cdot \boldsymbol{E}}{m},
$$

where $C(x)$ and $S(x)$ are the Fresnel integrals given by [7]:

$$
C(x)=\left(\frac{2}{\pi}\right)^{1 / 2} \int_{0}^{x} \mathrm{~d} y \cos \left(y^{2}\right)
$$

$$
S(x)=\left(\frac{2}{\pi}\right)^{1 / 2} \int_{0}^{x} \mathrm{~d} y \sin \left(y^{2}\right) .
$$

Since the introduction of ICFE into the standard transition rates is a debated point in the literature [8] we remark that our eq. (11) fully agrees with Refs. [9-13] while differs with references [14-16]. In particular, the reason why our result differs from Ref. [16], which also employs the Generalized Kadanoff-Baym approach, comes from the use of a different Ansatz [5] (see point (iii) in Section 2 and Ref. (2b)).

The presence of ICFE is responsible for a broadening and skewing of the original energy conserving delta function for the free particle case. We notice that ICFE vanishes for $\boldsymbol{q}$ perpendicular to $\boldsymbol{E}$. Because of the presence of fast oscillations associated to the Fresnel integrals in eqs. (13) and (14), $K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)$ in the form of eq. (11) cannot be used within a Monte Carlo scheme which requires a positive definite quantity. As suggested in Ref. [10], a plausible way of suppressing the oscillations (whose tails integrate to zero) is to approximate the expression (11), with a Lorentzian given by:

$$
K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)=\frac{2(|Q| / 2 \pi)^{1 / 2}}{\frac{|Q|}{2 \pi}+\left[-P-\frac{Q}{[(2 / \pi)|Q|]^{1 / 2}}\right]^{2}}
$$

A plot of the joint spectral densities so obtained is shown in Fig. 1 for different values of the field. As can be seen from the figure, the approximation of eq. (15) accurately locates the main peak, which is responsible for the normalization constraint of $K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)$, and reasonably reproduces the main features of the exact form given in eq. (11). The Lorentzian curve in eq. (15) is well suitable to be used within a Monte Carlo scheme.

### 4.3. Free electrons with ICFE and nonparabolicity

If we expand the previous model to include a nonparabolic energy momentum relationship of the form $k^{2} /(2 m)=$ $\varepsilon(1+\alpha \varepsilon)$, where $\alpha$ is the nonparabolicity parameter, then:

$$
\begin{aligned}
G_{E}^{r}(\boldsymbol{k}, t)= & -i \theta(t) \exp \left\{\frac { - i } { 2 \alpha } \left[(c t+b)\left(a+\frac{c}{4} t^{2}+\frac{b}{2} t\right)^{1 / 2}\right.\right. \\
& +(c t-b)\left(a+\frac{c}{4} t^{2}-b t\right)^{1 / 2} \\
& +\frac{\Delta}{8 c^{3 / 2}}\left(\operatorname{Arsh}\left(\frac{b+c t}{\Delta^{1 / 2}}\right)\right. \\
& \left.\left.\left.-\operatorname{Arsh}\left(\frac{b-c t}{\Delta^{1 / 2}}\right)\right)-t\right]\right\}
\end{aligned}
$$

with

$$
\begin{gathered}
a=1+\frac{2 \alpha k^{2}}{m} ; \quad b=-4 \frac{\alpha}{m} \boldsymbol{k} \cdot \boldsymbol{E} \\
c=\frac{2 \alpha}{m} E^{2} ; \quad \Delta=4 a c-b^{2}
\end{gathered}
$$

The functions $A(\boldsymbol{k}, t)$ and $K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)$ which follow from eqs. (16, 17) are straightforward but enormously complicated. For the purpose of illustration, we give the explicit expression for $K\left(\boldsymbol{k}, \boldsymbol{k}^{\prime}\right)$ under the condition of small nonparabolicity

![](./images/812297167329820673_1.jpg)

Fig. 1. Joint spectral density accounting for ICFE as a function of $P = (\varepsilon' - \varepsilon - \omega_0)$ at different values of the electric field. Continuous dashed lines refer to the exact Lorentzian models reported in the text. (a) $E = 2.5\,\text{kV/cm}$; (b) $E = 10\,\text{kV/cm}$. In the calculations we take the maximum value of $B$ with $\varepsilon = 1\,\text{eV}$, $\omega_0 = 0.04\,\text{eV}$ and $m = 0.3$.

$\alpha\varepsilon \ll 1$, when $k^2/(2m) = 1/(2m\alpha)[1 - (1 - 4m\alpha\varepsilon)^{1/2}]$. Then:
$$
\begin{aligned}
K(\boldsymbol{k}, \boldsymbol{k}') =& \int_0^\infty \mathrm{d}t'\, 2\ \text{Re} \left\{\exp \left[i(Pt' + \frac{1}{2}(1 + \alpha)Qt'^2\right.\right. \\
& \left.\left.+ Dt'^3 + \frac{9}{8}\alpha E^2 Qt'^4\right)\right]\right\}
\end{aligned} \tag{18}
$$
with $P$ and $Q$ given by eq. (12), and
$$
D = \frac{\alpha}{6}\left[\frac{1}{m}(k^2 + k'^2)E^2 + 2Q\right]. \tag{19}
$$

By comparing eq. (18) with eq. (11) it is clear that non-parabolicity further distorts the joint spectral density. It is no longer possible to recover the golden rule even when $\boldsymbol{q}$ is perpendicular to $\boldsymbol{E}$ because of the presence of the extra term $D$.

### 4.4. Collisional broadening (CB)
It is possible to account for collisions within the model described in Section 4.1, by letting $\Sigma'$ be different from zero [i.e., we set $\boldsymbol{E} = 0$ in eq. (5)]. In this case it is convenient to use the frequency-domain representation. We shall confine our interest to the case when $\Sigma'$ is a function of $\omega$ only here $\omega$ has the meaning of the carrier many-body energy, because

![](./images/812297167329820673_2.jpg)

Fig. 2. Joint spectral density accounting for CB as a function of the kinetic energy after a scattering event for several values of the initial kinetic energy. (a) $\varepsilon = 0.05\,\text{eV}$; (b) $\varepsilon = 0.1\,\text{eV}$; (c) $\varepsilon = 1\,\text{eV}$.

this is the only case that can be handled analytically (scattering with non-polar optical, intervalley and acoustic phonons under elastic and energy-equipartition approximations are the corresponding cases of interest [17]). We take the self energy in the lowest order in the electron-phonon coupling (i.e., corrections due to the real part of the self energy are neglected [18]):

$$\operatorname{Re}\left\{\Sigma^{r}(\omega)\right\}=0 ;$$

$$-\operatorname{Im}\left\{\Sigma^{r}(\omega)\right\}=\frac{\Gamma}{2}(\omega)=\gamma\left(\omega-\omega_{0}\right)^{1 / 2}.\tag{20}$$

It is then found:

$$G^{r}(\boldsymbol{k}, \omega)=\frac{(\omega-\varepsilon)^{-1}-i \pi \delta(\omega-\varepsilon)}{1+(i / 2) \Gamma(\omega)\left[(\omega-\varepsilon)^{-1}-i \pi \delta(\omega-\varepsilon)\right]}\tag{21}$$

$$A(\boldsymbol{k}, \omega)=\frac{\Gamma(\omega)}{(\omega-\varepsilon)^{2}+\left[\frac{1}{2} \Gamma(\omega)\right]^{2}}\tag{22}$$

$$
\begin{aligned}
K\left(x_{i}, x_{f}\right)= & \frac{2}{\pi \gamma^{2}}\left\{\int_{2 x_{0}}^{\infty} \mathrm{d} x \frac{\left(x-x_{0}\right)^{1 / 2}\left(x-2 x_{0}\right)^{1 / 2} \theta\left(x_{i}-x_{0}\right) \theta\left(x_{f}-x_{0}\right)}{\left[\left(x-x_{i}\right)^{2}+\left(x-x_{0}\right)\right]\left[\left(x-x_{0}-x_{f}\right)^{2}+\left(x-2 x_{0}\right)\right]}\right. \\
& \left.+\pi \frac{x_{f}^{1 / 2} \theta\left(x_{i}-x_{0}\right) \theta\left(x_{0}-x_{f}\right) \theta\left(x_{f}\right)}{\left(x_{0}+x_{f}-x_{i}\right)^{2}+x_{f}}+\pi^{2} \delta\left(x_{0}+x_{f}-x_{i}\right) \theta\left(x_{0}-x_{i}\right) \theta\left(x_{0}-x_{f}\right)\right\},
\end{aligned}
\tag{23}
$$

where for simplicity only emission processes are considered and dimensionless energies $x=\omega^{2} / \gamma^{2}, x_{i}=\varepsilon / \gamma^{2}, x_{f}=\varepsilon^{\prime} / \gamma^{2}$, $x_{0}=\omega_{0} / \gamma^{2}$ ($\omega_{0}$ is the optical phonon energy) have been introduced.

A plot of the joint spectral density in eq. (23) is shown in Fig. 2. Notice the asymmetric shape of $K$, which is zero for $\varepsilon^{\prime}=0$, while it decays as $\varepsilon^{\prime-3 / 2}$ at a symptotic high energies. This high energy tail may have profound effects on the carrier dynamics as is evident in the numerical results discussed in the next section.

## 5. Application to a simple model semiconductor

The usefulness of the joint spectral density, as included in a standard Monte Carlo procedure [19], is here exemplified by analyzing the main consequences of CB alone for a simple model semiconductor. The model, which considers only nonpolar optical processes at zero temperature (spontaneous emission), basically relies on the three parameters $m=0.3$, $\omega_{0}=40 \mathrm{meV}$ and $\gamma^{2}=1.1 \mathrm{meV}$. The choice of these values can be considered as typical for several cubic semiconductors.

The results obtained from simulations with $10^{4}$ electrons are shown in Figs. 3 and 4.

In Fig. 3 the distribution functions of the kinetic energy, with and without broadening, are compared for an electric field of $500 \mathrm{kV} / \mathrm{cm}$. In the absence of broadening the electron gas achieves the quasi-elastic regime [20]. Accordingly, the distribution function of the kinetic energy agrees quite satisfactorily with a heated Maxwell-Boltzmann distribution. On the contrary, broadening has been found to strongly modify such a distribution. More carriers are found in the low as well as in the high energy tails. In the presence of broadening the kinetic energy has been found to increase significantly (about $60 \%$ ); the drift velocity increases as well, but to a minor extent (about $20 \%$ ).

A few electrons are found at very high energies (above $3 \mathrm{keV}$ ) during the simulation. These "lucky electrons" originate from the tail of the spectral density, therefore this effect is inherent with the model of broadening. Accordingly we will introduce the concept of BROADENING-ASSISTED RUN-AWAY. (The same argument can be used for the case of ionization processes which, by analogy with the previous case, we shall call BROADENING-ASSISTED IMPACT IONIZATION). In real cases, deviations from the simple parabolic energy spectrum and/or the presence of other scattering mechanisms (e.g., intervalley transfer, impact ionization, etc.) will prevent this type of run-away. In any case it is worth noting that collision broadening favours not only the presence of hot electrons in the tails of the distribution function, but also it allows for carrier run-away even if the scattering rate is a monotonically increasing function of energy.

For completeness in Fig. 4 we report the distribution functions of the kinetic energy at lower electric field strengths. At $E=10 \mathrm{kV} / \mathrm{cm}$, when a streaming motion regime is

![](./images/812297167329820673_3.jpg)

Fig. 3. Energy distribution function as a function of the kinetic energy at $E=500 \mathrm{kV} / \mathrm{cm}$. Dashed (continuous) lines refer to calculations without (with) collisional broadening.

![](./images/812297167329820673_4.jpg)

Fig. 4. The same as Fig. 3 at $E=100$ kV/cm (a) and $E=10$ kV/cm (b). In this latter case (b) the results without and with collisional broadening are found to practically coincide.

achieved [20], the calculations show that the effect of collision broadening becomes negligible [see Fig. 4(b)].

## 6. Conclusions
This paper has presented a theoretical framework which enables one to account for genuine quantum effects for the case of hot-electron transport in semiconductors. The main quantities of interest are the spectral density and the associated joint spectral density which can include ICFE as well as CB. After providing the general theory, analytical models for these quantities have been obtained in some cases of interest. Intra-collisional field effects for a parabolic and a non-parabolic band, and collisional broadening have been considered. When quantum effects are neglected, that is carriers behave as a free particle between two scatterings, the semiclassical Boltzmann picture with the collision term determined from the golden rule is recovered. Monte Carlo numerical calculations as applied to a simple semiconductor model for the case of CB, clearly indicate an increase of the carrier population in the low and high energy regions of the kinetic energy distribution function. Accordingly, the concept of a broadening assisted run-away effect has been introduced.

## Acknowledgements
The financial support of the Ministero Pubblica Instruzione (MPI), of the Euopean Research Office (ERO) and of the Computer Center of the Modena University is gratefully acknowledged. The authors wish to thank Drs R. Brunetti and C. Jacoboni for helpful discussions.

## References
1. For a recent review on the subject see: Reggiani, L., Physica **134B**, 123 (1985).
2. (a) Reggiani, L., Lugli, P. and Jauho, A. P., Phys. Rev. **36B**, 6602 (1987); (b) Khan, F. S., Davies, J. H. and Wilkins, J. W., Phys. Rev. **36B**, 2578 (1987); (c) Jauho, A. P., Proc. on Quantum Transport Theory with Applications to Nanometer Microelectronics, S. Miniato (1987) (to be published).
3. Jauho, A. P. and Wilkins, J. W., Phys Rev. **29B**, 1919 (1984).
4. Langreth, D. and Wilkins, J., Phys. Rev. **6B**, 3189 (1972); Langreth, D. C., in Linear and Nonlinear Electron Transport in Solids (Edited by J. T. Devreese and E. Van Doren), Plenum, New York (1976).
5. Lipavsky, P., Spicka, V. and Velicky, B., Phys. Rev. **34B**, 6933 (1986).
6. Mahan, G. D., Phys. Rep. **110**, 321 (1984); **145**, 235 (1987).
7. Gradshteyn, I. S. and Ryzhik, I. M., Table of Integrals, Series and Products, p. 390, Academic Press, New York (1980).
8. Lowe, D., J. Phys. **C18**, L209 (1985).
9. Levinson, I. B. and Yasevichyute, Ya., Sov. Phys. JETP **35**, 991 (1972).
10. J. R. Barker, Sol. State Electron. **21**, 267 (1978).
11. Thornber, K. K., Sol. State Electron. **21**, 259 (1978).
12. Seminozhenko, V. P., Phys. Repts. **3**, 103 (1982).
13. Pottier, N. and Calecki, D., Physica **110A**, 471 (1982).
14. Herbert, D. C. and Till, S. J., J. Phys. **C15**, 5411 (1982).
15. Marsh, A. C. and Inkson, J. C., J. Phys. **C17**, 4501 (1984).
16. Sarker, S. K., Davies, J. H., Khan, F. S. and Wilkins, J. W., Phys. Rev. **33B**, 7263 (1986).
17. Ziep, O. and Keiper, R., Phys. Stat. Sol. **128(b)**, 779 (1985).
18. Chang, Y. C., Ting, D. Z. Y., Tang, J. Y. and Hess, K., Appl. Phys. Lett. **42**, 76 (1983).
19. Jacoboni, C. and Reggiani, L., Rev. Mod. Phys. **55**, 645 (1983).
20. Reggiani, L., Hot-Electron Transport in Semiconductors, Topics in Applied Physics, Vol. **58**, Springer-Verlag, Heidelberg (1985).