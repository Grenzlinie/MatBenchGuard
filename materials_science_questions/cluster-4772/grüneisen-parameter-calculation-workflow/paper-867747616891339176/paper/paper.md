# Quantum elasticity of graphene: Thermal expansion coefficient and specific heat

I. S. Burmistrov, $^{1,2}$ I. V. Gornyi, $^{1,3,4,5}$ V. Yu. Kachorovskii, $^{1,3,4,5}$ M. I. Katsnelson, $^{6}$ and A. D. Mirlin $^{1,3,4,7}$

$^{1}$ L. D. Landau Institute for Theoretical Physics, Kosygina street 2, 119334 Moscow, Russia
$^{2}$ Laboratory for Condensed Matter Physics, National Research University Higher School of Economics, 101000 Moscow, Russia
$^{3}$ Institut für Nanotechnologie, Karlsruhe Institute of Technology, 76021 Karlsruhe, Germany
$^{4}$ Institut für Theorie der kondensierten Materie, Karlsruhe Institute of Technology, 76128 Karlsruhe, Germany
$^{5}$ A. F. Ioffe Physico-Technical Institute, 194021 St. Petersburg, Russia
$^{6}$ Radboud University, Institute for Molecules and Materials, NL-6525AJ Nijmegen, The Netherlands
$^{7}$ Petersburg Nuclear Physics Institute, 188300, St.Petersburg, Russia

(Dated: October 2, 2018)

We explore thermodynamics of a quantum membrane, with a particular application to suspended graphene membrane and with a particular focus on the thermal expansion coefficient. We show that an interplay between quantum and classical anharmonicity-controlled fluctuations leads to unusual elastic properties of the membrane. The effect of quantum fluctuations is governed by the dimensionless coupling constant, $g_0 \ll 1$, which vanishes in the classical limit ($\hbar \to 0$) and is equal to $\simeq 0.05$ for graphene. We demonstrate that the thermal expansion coefficient $\alpha_T$ of the membrane is negative and remains nearly constant down to extremely low temperatures, $T_0 \propto \exp(-2/g_0)$. We also find that $\alpha_T$ diverges in the classical limit: $\alpha_T \propto -\ln(1/g_0)$ for $g_0 \to 0$. For graphene parameters, we estimate the value of the thermal expansion coefficient as $\alpha_T \simeq -0.23\ \text{eV}^{-1}$, which applies below the temperature $T_{\text{uv}} \sim g_0 \varkappa_0 \sim 500\ \text{K}$ (where $\varkappa_0 \sim 1\ \text{eV}$ is the bending rigidity) down to $T_0 \sim 10^{-14}\ \text{K}$. For $T < T_0$, the thermal expansion coefficient slowly (logarithmically) approaches zero with decreasing temperature. This behavior is surprising since typically the thermal expansion coefficient goes to zero as a power-law function. We discuss possible experimental consequences of this anomaly. We also evaluate classical and quantum contributions to the specific heat of the membrane and investigate the behavior of the Grüneisen parameter.

PACS numbers: 72.80.Vp, 73.23.Ad, 73.63.Bd

## I. INTRODUCTION

The thermal expansion coefficient $\alpha_T$ is one of the most important thermodynamic characteristics of any material. It is well known that $\alpha_T$ is determined by an anharmonicity of interatomic potentials binding atoms into a crystalline lattice [1–6]. Indeed, for a harmonic oscillator, the averaged displacement of the coordinate equals zero independently of the oscillation amplitude. By contrast, for an anharmonic oscillator, an averaged displacement depends on the oscillation amplitude and, consequently, on temperature.

For the most of materials, the thermal expansion coefficients are positive, $\alpha_T > 0$. On the other hand, some exotic systems—including, in particular, complex metal oxides, polymers, and zeolites—are known to contract upon heating [7]. The interest to materials with $\alpha_T < 0$ is motivated, in particular, by the desire to fabricate a composite structure fully compatible with conventional semiconductor nanotechnology and having zero thermal expansion coefficient. A certain progress in this direction is connected with recent observation that carbon nanotubes [8–11] might demonstrate negative thermal expansion (NTE). However, the measured effect was relatively small and observed in a not too wide temperature interval. It is also worth noting that materials demonstrating NTE at very low temperatures (below $0.1\ \text{K}$) are unknown so far.

The goal of this paper is to demonstrate that graphene, a famous two-dimensional (2D) material that has been attracting enormous interest in last decade [12–21], shows NTE with an approximately constant $\alpha_T$ for all experimentally accessible temperatures: from very high (a few hundreds of Kelvin) temperatures down to extremely low temperatures, $T_0 \sim 10^{-14}\ \text{K}$. Only at exponentially small temperatures, $T < T_0$, the thermal expansion coefficient $\alpha_T$ goes to zero. Since measurements of the elasticity of free-standing graphene have recently become accessible to experimental techniques [22–24], the prediction of an approximately temperature-independent negative $\alpha_T$ can be verified experimentally. Our consideration is applicable also to other two-dimensional materials.

The fact that NTE is a natural property of layered and 2D materials due to existence of bending (flexural acoustic) mode which is anomalously sensitive to the deformation has been recognized long time ago [25] and dicussed in a number of recent publications [19, 26–28]). In particular, graphite is known to have NTE at not too high temperatures [29], which may be explained quantitatively within a quasiharmonic theory [2–6] via first-principles calculations of phonon spectra and Grüneisen parameters [26]. The same calculations predicted that graphene should have NTE at any temperatures. More recently, atomistic simulations of graphene [30] confirmed the NTE at moderately high temperatures and also showed that the thermal expansion coefficient changes sign with growing temperature due to anharmonic effects beyond the quasiharmonic approximation. Qualitatively similar results were obtained in Refs. [31, 32]. Experiments confirm that the thermal ex-

pansion coefficient of graphene at room temperature is negative, with the absolute value as large as 0.1 eV⁻¹ [33]. With the temperature increase up to 400 $K$, $\alpha_T$ decreases in absolute value [34], which may be considered as a partial confirmation of the prediction [30]. At very high temperatures, the thermal expansion coefficient of graphene is definitely positive but its precise measurement is difficult [35].

The main focus of the present paper is on the range of relatively low temperatures. The behavior of the thermal expansion coefficient of graphene (or, more generally, of a 2D membrane) in this regime represents a challenging theoretical problem. The microscopic Grüneisen parameter for the bending mode is divergent at the phonon wave vector $q \to 0$ in quasiharmonic approximation as $-1/q^2$ (see Eq. 4 of [27]), which means that relevant phonons determining the thermal expansion are always classical (i.e, their energy is smaller than the temperature). As a result, within the quasiharmonic approximation, the thermal expansion coefficient remains constant down to arbitrary low temperatures [27]. This is in stunning contrast with the conventional behavior, $\alpha_T \to 0$ at $T \to 0$, which is usually associated with the third law of thermodynamics in view of the identity [36]

$$
\left(\frac{\partial V}{\partial T}\right)_{P}=-\left(\frac{\partial S}{\partial P}\right)_{V} \tag{1}
$$

where $V,P,T,S$ are volume, pressure, temperature, and entropy, respectively.

Clearly, one may expect that quantum effects modify the low-$T$ behavior of $\alpha_T$. Quantum corrections to thermodynamic properties have been calculated in Ref.37. Based on perturbative analysis, it was suggested that classical theory becomes inapplicable already at reasonably high temperatures, about 70-90 $K$ and that the thermal expansion coefficient goes to zero in a conventional way—i.e., as a power law—at $T \to 0$. Here we will show that the situation is, in fact, much more exotic and the classical expression for the thermal expansion coefficient [27] remains valid, with some logarithmic corrections, till very low temperatures. The thermal expansion coefficient does go to zero at zero temperature but slower than any power of the temperature.

In this paper, we explore systematically thermodynamic properties of a graphene membrane, with a particular focus on the thermal expansion coefficient $\alpha_T$, in the whole range of the temperatures. We show, in particular, that the behavior of $\alpha_T$ in the limit $T \to 0$ is connected with quantum effects characterized by a dimensionless coupling constant $g$ [definition of $g$ is given by Eq. (12) below], which vanishes in the classical limit $\hbar \to 0$.

As a one of the most important results of the paper, we demonstrate that the thermal expansion coefficient of the membrane remains negative and nearly constant down to all realistic temperatures. For graphene parameters this constant value is about $-0.23\ \mathrm{eV}^{-1}$. For a generic membrane, we find that in the limit of weak coupling, the value of $\alpha_T$ depends logarithmically on the bare value of the coupling $g_0$ (the value of $g$ at the atomic scales):

$$
\alpha_T \propto -\ln(1/g_0), \text{ for } g_0 \ll 1,
$$

and consequently diverges in the classical limit $\hbar \to 0$. We also demonstrate that, with decreasing temperature, $\alpha_T$ starts to approach zero only when $T$ drops below an exponentially small temperature scale $T_0$

$$
T_{0} \sim g_{0} \varkappa_{0} e^{-2 / g_{0}}. \tag{2}
$$

Here $\varkappa_0$ is the bare value of the bending rigidity of the membrane (equal to $\simeq 1\mathrm{eV}$ for graphene). Furthermore, the decay of $|\alpha_T|$ at such exponentially low temperatures is logarithmically slow.

We also calculate the specific heat. In particular, we show that the leading contribution to both $C_V$ and $C_P$ is determined by classical effects, while the difference $C_P - C_V$ is proportional to $g_0$ and, thus, has a purely quantum nature.

The outline of the paper is as follows. Section II contains a qualitative discussion of the physics of fluctuation-induced elasticity of a membrane. In Sec. III we present the classical and quantum renormalization-group (RG) formalism as well as basic equations for the observables of interest. In Sec. IV we use the results of the preceding section to calculate the temperature dependence of the thermal expansion coefficient and of the specific heat. Our results are summarized in Sec. V. Various technical aspects of our analysis are presented in Appendices A-D.

## II. FLUCTUATION-INDUCED ELASTICITY OF A MEMBRANE

A free-standing graphene is a remarkable example of a 2D crystalline membrane [19, 28]. Elastic properties of such a membrane are characterized by the bending rigidity $\varkappa$ (which is quite high for graphene, $\varkappa \simeq 1$ eV), the Young modulus $Y$ and the bulk modulus $B$:

$$
Y=\frac{4 \mu(\mu+\lambda)}{2 \mu+\lambda}, \quad B=\mu+\lambda, \tag{3}
$$

where $\mu$ and $\lambda$ are the Lame coefficients (for graphene $\lambda \simeq 2\ \mathrm{eV\cdot\mathring{A}}^{-2}$ and $\mu \simeq 10\ \mathrm{eV\cdot\mathring{A}}^{-2}$, see Ref.30). A distinct feature of a free-standing 2D membrane is the existence of out-of-plane phonon modes—flexural phonons (FP) [19, 25, 28, 38]. In contrast to in-plane phonons with the conventional linear dispersion, the FP are very soft, $\omega_q \propto q^2$. As a consequence, the out-of-plane thermal fluctuations are unusually strong and tend to destroy a membrane by driving it into the crumpled phase [38].

The tendency of the membrane to crumpling is at the heart of the mechanism leading to NTE. Let us explain this in more detail. The vector $\mathbf{r}$ describing point at the membrane surface depends on the 2D coordinate $\mathbf{x}$ that parametrizes the membrane and can be split into three terms

$$
\mathbf{r}=\xi \boldsymbol{x}+\boldsymbol{u}+\boldsymbol{h}, \tag{4}
$$

![](./images/867747616891339176_1.jpg)

FIG. 1: Temperature-induced shrinking of a graphene membrane. Due to classical and quantum fluctuations, the membrane shrinks in the longitudinal direction (bottom), as compared to the membrane without fluctuations (top).

where vectors $\boldsymbol{u} = \boldsymbol{u}(\boldsymbol{x}, t)$, $\boldsymbol{h} = \boldsymbol{h}(\boldsymbol{x}, t)$ represent in-plane and out-of-plane phonon fields, respectively. The global stretching factor $\xi$ is equal to unity at zero temperature but gets reduced with increasing $T$ due to out-of-plane fluctuations (see Fig. 1), becoming zero at the crumpling transition temperature $T_{\text{cr}}$. Remarkably, the thermal expansion of membrane is nonzero even if one neglects the anharmonicity of in-plane and out-of-plane modes as well as anharmonic coupling between them [25]. Within such an approximation the only relevant anharmonicity is due to the coupling of global stretching and FP. Treating FP as classical random fields yields [39]

$$
\xi^{2}=1-\left\langle\partial_{\alpha} \boldsymbol{h} \partial_{\alpha} \boldsymbol{h}\right\rangle / 2,\qquad(5)
$$

which results in a negative, logarithmically divergent value of $\alpha_{T}=L^{-2} d A / d T$:

$$
\alpha_{T}=\frac{\partial \xi^{2}}{\partial T}=-\frac{1}{4 \pi \varkappa} \ln \left(\frac{L}{L_{\mathrm{uv}}}\right).\qquad(6)
$$

Here, $A=\xi^{2} L^{2}$ is the sample area, $L$ is the system size at zero temperature, and $L_{\mathrm{uv}}$ is the ultraviolet cutoff of the order of the lattice constant. Evidently, if this equation were fully correct, the membrane would not exist in the thermodynamic limit, $L \rightarrow \infty$. Actually, the anharmonic coupling between $\boldsymbol{u}$ and $\boldsymbol{h}$ fields leads to a renormalization of the bending rigidity, which becomes momentum-dependent, $\varkappa \rightarrow \varkappa_{q}$ and flows to infinity, $\varkappa_{q} \rightarrow \infty$, for $q \rightarrow 0$ [19, 28, 38-56]. This cures the logarithmic divergence of $\alpha_{T}$ with the system size, thus yielding a finite value for the crumpling transition temperature, $T_{\text{cr}}<\infty$, for $L \rightarrow \infty$. Below $T_{\text{cr}}$ one gets [39, 57]

$$
\xi^{2}=1-T / T_{\mathrm{cr}},\qquad(7)
$$

and, consequently, a finite negative value of the thermal expansion coefficient, $\alpha_{T}=-1 / T_{\text{cr}}$.

These arguments indicate that the role of anharmonicity in a free-standing 2D membrane is remarkably different as compared to the case of a 3D crystal (or to the case of graphene on substrate). Indeed, in the 3D case, the anharmonic coupling between phonons determines a nonzero value of $\alpha_{T}$ (which is zero in the harmonic approximation). In contrast, in a free-standing 2D membrane, such coupling leads to a suppression of an infinite value of $\alpha_{T}$ predicted within the harmonic description of in-plane and flexural modes down to a finite value.

In order to find $T_{\text{cr}}$ and $\alpha_{T}$, one should investigate the renormalization from the ultraviolet energy scale down to the infrared scale. Such renormalization was intensively discussed more than two decades ago [38, 40-56] in the purely classical approximation (under assumption that the temperature is higher than the relevant frequencies of in-plane and flexural modes) in connection with biological membranes, polymerized layers, and inorganic surfaces. The interest to this topic has been renewed more recently [37, 58-68] after discovery of graphene. It was found [40-47, 53] that the anharmonic coupling of in-plane and out-of-plane phonons leads to power-law renormalization of the bending rigidity, $\varkappa \rightarrow \varkappa_{q}$, where

$$
\varkappa_{q} \simeq \varkappa\left(\frac{q_{*}}{q}\right)^{\eta}, \quad \text { for } q \ll q_{*},\qquad(8)
$$

with a certain critical exponent $\eta$. Here the momentum scale (see e.g. Eq. (154) of Ref. [39])

$$
q_{*}=\sqrt{\frac{3 d_{\mathrm{c}} Y T}{32 \pi \varkappa^{2}}} \sim \frac{\sqrt{d_{\mathrm{c}} \mu T}}{\varkappa}\qquad(9)
$$

is the inverse Ginzburg length which separates the regions of conventional $(q>q_{*})$ and fractal $(q<q_{*})$ scaling [19, 28, 38, 40]. In other words, the anharmonicity of flexural modes becomes important at $q<q_{*}$. The last expression in Eq. (9) is an order-of-magnitude estimate where we have discarded numerical coefficients as well as a difference in values of the elastic moduli, $Y \sim B \sim \mu \sim \lambda$. We will present such estimates also in several cases below in order to emphasize the scaling of observables with parameters of the problem.

The critical exponent $\eta$ was determined within several approximate analytical schemes [43, 45, 46, 53, 58]. In particular, for a 2D membrane embedded into a space of large dimensionality $d \gg 1$, one can find analytically $\eta=2 / d_{\mathrm{c}} \ll 1$, where

$$
d_{\mathrm{c}}=d-2.
$$

Numerical simulations for physical 2D membrane embedded in 3D space $(d_{\mathrm{c}}=1)$ yield $\eta=0.60 \pm 0.10$ [51] and $\eta=0.72 \pm 0.04$ [56]. Atomistic Monte Carlo simulations for graphene gives the value $\eta \approx 0.85$ [28, 65]; approximately the same value has been derived via functional renormalization group approach [58].

In the limit $d_{\mathrm{c}} \gg 1$, the critical temperature of the crumpling transition can be also calculated analytically within a classical approximation, yielding [39, 57]

$$
T_{\mathrm{cr}}=\frac{4 \pi \eta \varkappa}{d_{\mathrm{c}}}=\frac{8 \pi \varkappa}{d_{\mathrm{c}}^{2}}.\qquad(10)
$$

As a consequence, the thermal expansion coefficient is negative and independent of temperature

$$
\alpha_{T}^{d_{c} \rightarrow \infty}=-\frac{d_{c}}{4 \pi \eta \varkappa}. \tag{11}
$$

Evidently, one expects that this result should fail at low enough temperatures due to the quantum effects.

Some aspects of this problem were discussed recently [27, 37, 63, 67]. One scenario of the suppression of $\alpha_{T}$ is the emergence of a "mass" (term quadratic in momentum $q$) in the propagator of flexural phonons or, equivalently, $1/q^{2}$ divergence of the effective bending rigidity [37]. This mass arises naturally within perturbative calculations [37]. However, as it will be shown below by an explicit calculation of the free energy, it is nothing else as the full tension (as was pointed out in Ref. 63) and thus is zero for a free membrane (without external stress).

As was shown in Ref. 62, quantum fluctuations may also lead to renozmalization of elastic coefficients. This renormalization can be described [62, 64] in terms of a flow of the dimensionless quantum coupling constant

$$
g=\frac{3\left(6+d_{c}\right)}{128 \pi} \frac{\hbar Y}{\rho^{1 / 2} \varkappa^{3 / 2}} \sim \frac{\hbar \mu}{\rho^{1 / 2} \varkappa^{3 / 2}}, \tag{12}
$$

where $\rho$ is the mass density of membrane. Since $g \propto \hbar$, it vanishes in the classical limit $\hbar \rightarrow 0$. For graphene, the bare value $g_{0}$ of this constant at the ultraviolet scale, $q \sim q_{\mathrm{uv}}$, on the order of the lattice constant is quite small, $g_{0} \simeq 1 / 20$. Physically, this happens because $g_{0}$ contains $\rho$ and, consequently, the atomic mass in the denominator.

In the sequel, we develop a theory of thermal expansion of an elastic membrane that includes both classical and quantum effects. We show that there is an additional contribution to $\alpha_{T}$, which originates from the region of momenta $q_{*}<q<q_{*} / \sqrt{g}$ and is not taken into account in Eq. (11). This contribution is logarithmically large $[\propto-\ln (1 / g)]$ for small coupling $g$. Quantum fluctuations originate from $q>q_{*} / \sqrt{g}$. Evidently, such interval of $q$ exists only when $q_{*} / \sqrt{g}<q_{\mathrm{uv}}$. The temperature found from the condition $q_{*} / \sqrt{g} \sim q_{\mathrm{uv}}$ is given by $T_{\mathrm{uv}} \sim g_{0} \varkappa_{0}$ ($\sim 500 \mathrm{~K}$ for graphene). This temperature is determined by the bare value $g_{0}$ of the quantum coupling constant and plays the role of the Debye temperature. For $T<T_{\mathrm{uv}}$ the problem becomes quantum in terms of statistics, i.e., some phonons are frozen out. On the other hand, the effect of quantum fluctuations (i.e., those with momenta in the range $q_{*} / \sqrt{g}<q<q_{\mathrm{uv}}$ ) remains negligibly small in a wide temperature interval $T_{0}<T<T_{\mathrm{uv}}$, where $T_{0} \sim T_{\mathrm{uv}} \exp \left(-2 / g_{0}\right)$. Therefore, from the point of view of fluctuation-induced renormalization, the problem remains classical down to the temperature $T_{\mathrm{uv}}$, which is exponentially small for $g_{0} \ll 1$. Only at very low temperatures, $T<T_{0}$, quantum fluctuations come into play and, as a result, the thermal expansion coefficient gets logarithmically suppressed.

Our goal in this paper is to develop a theory of thermal expansion valid for all temperatures in the range $T<T_{\mathrm{uv}}$ where the main contribution to $\alpha_{T}$ originates from the flexural phonons and therefore is negative. This requires a development of formalism incorporating both classical and quantum renormalization effects, which is the subject of the next Section.

## III. FORMALISM

### A. Thermodynamics of an elastic membrane

We consider a generic $2 D$ membrane embedded in the $d$-dimensional space $(d>2)$. The starting point of our analysis is the Lagrangian density

$$
\begin{aligned}
\mathcal{L}(\{\mathbf{r}\}) & =\rho \dot{\mathbf{r}}^{2}+\frac{\varkappa_{0}}{2}(\Delta \mathbf{r})^{2} \tag{13} \\
& +\frac{\mu_{0}}{4}\left(\partial_{\alpha} \mathbf{r} \partial_{\beta} \mathbf{r}-\delta_{\alpha \beta}\right)^{2}+\frac{\lambda_{0}}{8}\left(\partial_{\gamma} \mathbf{r} \partial_{\gamma} \mathbf{r}-2\right)^{2},
\end{aligned}
$$

which can be obtained from the general gradient expansion of elastic energy [42] by using a certain rescaling of coordinates (see discussion in Ref. 39). The subscript 0 in notations for elastic coefficients in Eq. (13) means that these are bare values at $q \simeq q_{\mathrm{uv}}$, where $q_{\mathrm{uv}}$ is the ultraviolet cut off. The $d$-dimensional vector $\mathbf{r}=\mathbf{r}(\mathbf{x}, \tau)$ is given by Eq. (4) with $\mathbf{u}=\left(u_{1}, u_{2}\right), \mathbf{h}=\left(h_{1}, \ldots, h_{d_{c}}\right)$, while $\dot{\mathbf{r}}=d \mathbf{r} / d \tau$, where $\tau$ is imaginary time.

The strategy of calculations is as follows. We assume that the ahrahmonic phonon interaction leads to a renormalization of elastic coefficients $\varkappa_{0} \rightarrow \varkappa_{q}, \mu_{0} \rightarrow \mu_{q}$, $\lambda_{0} \rightarrow \lambda_{q}$. Hence, in order to calculate the free energy, we replace Eq. (13) with a harmonic Lagrangian density containing renormalized elastic moduli. The details of calculation are relegated to Appendice A and B. The obtained free energy has the form [see Eq. (B14)]

$$
\begin{aligned}
\frac{F}{L^{2}} & =-\frac{\sigma^{2}}{2 B_{0}}+\sigma\left(\xi^{2}-1\right) \tag{14} \\
& +\frac{d_{c}}{2} \sum_{\mathbf{q} \omega} \ln \left(\varkappa_{q} q^{4}+\sigma q^{2}+\rho \omega^{2}\right),
\end{aligned}
$$

where

$$
\sigma=\frac{1}{L^{2}} \frac{\partial F}{\partial \xi^{2}}, \tag{15}
$$

is the external stress, $\sum_{\omega}$ stands for $T \sum_{\omega} \int d^{2} \mathbf{q} /(2 \pi)^{2}$, and the summation $\sum_{\omega}$ runs over bosonic Matsubara frequencies. This approximation is in spirit of self-consistent phonon theory [69] where, in analogy to Landau Fermi liquid theory for fermions, it is supposed that the entropy is renormalized by phonon-phonon interaction only via the change of their dispersion relation and phonon damping is neglected. One can assume that, within some numerical factors, this gives correct temperature dependences of all thermodynamic quantities.

Since FP are much softer than in-plane modes, we neglected contribution of in-plane modes in Eq. (14). Although this approximation looks quite natural, it needs some justification. Indeed, as was found in Ref. 37, the anharmonicity induces a small (in adiabatic parameter) ultraviolet-divergent contribution $\sigma_1$ ("built-in tension") to the coefficient in front of the $q^2$ term in the propagator of FP. Such term would suppress $\alpha_T$ (in a power-law way) at low temperatures. In fact, this term is exactly cancelled by another contribution, which was overlooked in Ref. 37. Technically, this additional contribution arises due to the coupling between in-plane phonons and global stretching. Here, we discuss the problem on the qualitative level, relegating the details of calculations to Appendices A and B. Substituting Eq. (4) into strain tensor of the membrane
$$
u_{\alpha \beta}=\frac{1}{2}\left(\partial_{\alpha} \mathbf{r} \partial_{\beta} \mathbf{r}-\delta_{\alpha \beta}\right),
$$
and leaving only linear with respect to fluctuation terms, we find that, in the harmonic approximation, the strain tensor is proportional to the global stretching and to the gradient of in-plane deformations:
$$
u_{\alpha \beta}^{\text {harmonic }}=\xi\left(\partial_{\alpha} u_{\beta}+\partial_{\beta} u_{\alpha}\right) / 2 . \tag{16}
$$

The energy of the in-plane fluctuations $E_{\text {in-plane }}$ is quadratic with respect to $u_{\alpha \beta}$ [38] and, as follows from Eq. (16), is proportional to $\xi^2$. Hence, there exists an contribution to the stress
$$
\delta \sigma=\frac{\left\langle E_{\text {in-plane }}\right\rangle}{\xi^{2} L^{2}},\tag{17}
$$
where averaging is taken with the action corresponding to the Lagrangian (13). As shown in Appendixes A and B
$$
\delta \sigma=\sigma_{1}.\tag{18}
$$

This implies that the quadratic-in-$q$ part of the self-energy of FP is given by $(\sigma+\sigma_1-\delta\sigma)q^2=\sigma q^2$, where $\sigma$ is the external tension. In other words, coupling of in-plane modes to the global stretching $\xi$ leads to additional contribution to the FP's self-energy which exactly cancels the quadratic correction arising due to anharmonic coupling of in-plane modes with FP.

This cancelation has a deep physical meaning. There are two different definitions of the tension $\sigma$. First, it can be obtained from the standard thermodynamic relation, as a derivative of the free energy with respect to system volume, see Eq. (15). Second, the tension can be found as a coefficient in front of the quadratic-in-$q$ term in the FP propagator,
$$
\sigma=\left.\frac{\partial G_{q}^{-1}}{\partial\left(q^{2}\right)}\right|_{q^{2}=0}.\tag{19}
$$

The equivalence of two definitions, while quite transparent physically, represents a very non-trivial Ward identity [44, 47]. We explicitly verify this identity within the one-loop RG analysis in Appendixes A and D.

$$
\frac{d \varkappa}{d \Lambda}=\eta \varkappa \qquad \frac{d \varkappa}{d \Lambda}=\nu g \varkappa
$$

![](./images/867747616891339176_2.jpg)

FIG. 2: Characteristic momentum scales in the problem. Regions of quantum and classical RG are shown, along with the corresponding RG equations for bending rigidity. In these equations, $\eta$ and $\theta$ are the classical and quantum critical indices, respectively, while $g$ is the quantum coupling constant.

In-plane modes lead also to a small ultraviolet renormalization of $\xi$ which we neglect here (see Appendix B for more detail).

The relation between $\xi$ and $\sigma$ is found from the condition $\partial F/\partial\sigma=0$, which yields, after summation over Matsubara frequencies,
$$
\xi^{2}-\xi_{0}^{2}=\frac{\sigma}{B_{0}}+s(\sigma),\tag{20}
$$
where
$$
\xi_{0}^{2}=1-\frac{d_{\mathrm{c}}}{8 \pi \rho} \int_{0}^{q_{\mathrm{uv}}} \frac{d q\ q^{3}}{\omega_{q}^{0}} \operatorname{coth}\left(\frac{\omega_{q}^{0}}{2 T}\right),\tag{21}
$$
is the longitudinal deformation of membrane in the absence of stress, while
$$
s=\frac{d_{\mathrm{c}}}{8 \pi \rho} \int_{0}^{q_{\mathrm{uv}}} d q q^{3}\left[\frac{\operatorname{coth}\left(\omega_{q}^{0} / 2 T\right)}{\omega_{q}^{0}}-\frac{\operatorname{coth}\left(\omega_{q} / 2 T\right)}{\omega_{q}}\right],\tag{22}
$$
is the stress-induced correction $(s_{\sigma\to0}=0)$, which leads, in particular, to anomalous Hooke's law [57]. Here $\omega_q$ and $\omega_q^0$ are FP frequencies for stressed and unstressed membrane, respectively,
$$
\omega_{q}=\sqrt{\frac{\varkappa_{q} q^{4}+\sigma q^{2}}{\rho}}, \quad \omega_{q}^{0}=\sqrt{\frac{\varkappa_{q}}{\rho}} q^{2}.\tag{23}
$$

In order to complete the calculation of $\alpha_T$, we should find renormalization of $\varkappa$ in the whole interval of momenta, $0<q<q_{\text{uv}}$, and substitute the renormalized function $\varkappa_q$ into Eqs. (20)-(23). This will allow us to determine the global stretching factor as a function of the applied stress and temperature, $\xi=\xi(\sigma,T)$, and thus to evaluate the thermal expansion coefficient,
$$
\alpha_{T}=\left[\frac{\partial \xi^{2}(\sigma, T)}{\partial T}\right]_{\sigma}.\tag{24}
$$

Hence, we focus in the next subsection on renormalization of elastic constants.

### B. Renormalization group

In this section, we find the flow of the elastic moduli with decreasing $q$ down from $q_{\rm uv}$ by using the perturbative RG approach (for a recent discussion of a quantum non-perturbative RG see Ref. 68). The classical and quantum RG are separated by $q = q_T$ found from the condition $\hbar\omega_q \simeq T$:

$$
q_T \sim \frac{q_*}{\sqrt{g}}. \tag{25}
$$

For $g \ll 1$, the characteristic scales of the problem are shown in Fig. 2. At large spatial scales (for $q \ll q_*$), a classical RG apply, so that the bending rigidity scales according to Eq. (8). In the interval $q_* < q < q_T$, the FP frequency is still small compared to $T$, so that classical approach remains applicable. However, the renormalization of $\varkappa$ in this region is small [38], $(\varkappa_q - \varkappa)/\varkappa \sim q_*^2/q^2$. The quantum RG operates in the interval between $q_T$ and $q_{\rm uv}$, with the former scale serving as an infrared and the latter as an ultraviolet cutoff. In order to derive quantum RG equations, we notice that for $q < \sqrt{\mu_0/\varkappa_0}$, the FP are much softer than the in-plane modes:

$$
\omega_q \ll \omega_q^{\perp,\parallel}, \tag{26}
$$

where

$$
\omega_q^\perp = q\sqrt{\mu/\rho}, \quad \omega_q^\parallel = q\sqrt{(2\mu+\lambda)/\rho}
$$

are frequencies of the transverse and longitudinal in-plane phonos respectively. We further notice, that for graphene, the value of $\sqrt{\mu_0/\varkappa_0}$ is on the order of the inverse lattice constant. This implies that one can use this value as the ultraviolet atomic momentum scale:

$$
q_{\rm uv} \sim \sqrt{\mu_0/\varkappa_0}. \tag{27}
$$

In view of Eq. (27), the interval $q_T < q < q_{\rm uv}$ for quantum RG exists provided that the temperature is not too high, $T < T_{\rm uv}$, where

$$
T_{\rm uv} \sim g_0\varkappa_0. \tag{28}
$$

For higher temperatures one can fully neglect quantum effects. Equation (28) implies that for graphene ($g_0 \simeq 1/20$, $\varkappa_0 \simeq 1$ eV) the temperature $T_{\rm uv}$ is of the order of 500 K. This temperature plays the role of the Debye temperature in our model.

As follows from Eq. (26), the retardation effects can be neglected and the quantum RG flow can be found in a full analogy with classical RG, [39] where FP field is considered to be static. Technical details are described in Appendices C and D where two alternative derivations of RG equations are presented. For in-plane moduli, one gets the following RG equations:

$$
\frac{d}{d\Lambda} \frac{1}{Y} = \frac{3}{8}\frac{d}{d\Lambda} \frac{1}{B} = \frac{d_c g}{(6+d_c)Y}, \tag{29}
$$

where

$$
\Lambda = \ln(q_{\rm uv}/q)
$$

is the logarithm of the running RG scale $q$, and the coupling $g$ is given by Eq. (12). For $d_c=1$, these equations are equivalent to Eqs. (9) and (10) of Ref. 62. As seen, there is invariant subspace of elastic moduli, $Y=8B/3$, which is conserved by the RG flow.

The RG flow of the bending rigidity $\varkappa$ is given by equation

$$
\frac{d\varkappa}{d\Lambda} = \frac{4g\varkappa}{d_c+6}, \tag{30}
$$

which agrees up to a sign with Eq. (11) of Ref. 62. [The sign was recently corrected in Ref. 64.] From Eqs. (12), (29), and (30), we find

$$
\frac{dg}{d\Lambda} = -g^2, \tag{31}
$$

which again agrees with the result of Ref. 62 once the sign error is corrected [64]. (We notice that the numerical coefficient in definition of $g$ in Ref. 62 is different). The negative sign in Eq. (31) is of key importance: it implies that the quantum anharmonicity effects *stabilize* the membrane increasing the effective bending rigidity. In other words, the flat phase of the membrane is perfectly defined in the limit of zero temperature and infinite system size. This is crucially important for low-temperature behavior of the $\alpha_T$ It is the growing effective bending rigidity at low temperatures which suppresses the thermal expansion coefficient. However, contrary to all previously known situations this provided only logarithm-in-power vanishing of the thermal expansion coefficient at $T \to 0$ rather than power-law.

Solving the RG equations, we get the following flow of the quantum coupling constant $g$, the bending rigidity $\kappa$, and the in-plane moduli $Y$ and $B$:

$$
g = \frac{g_0}{1+g_0\Lambda}, \quad \varkappa = \varkappa_0(1+g_0\Lambda)^\theta, \tag{32}
$$

$$
Y = \frac{Y_0}{(1+g_0\Lambda)^{1-3\theta/2}}, \quad \frac{1}{B} = \frac{1}{B_0} + \frac{8}{3}\left(\frac{1}{Y} - \frac{1}{Y_0}\right). \tag{33}
$$

Here

$$
\theta = \frac{4}{d_c+6} \tag{34}
$$

is the quantum anomalous exponent. For graphene (or, more generally, for a 2D membrane in a 3D space), $d_c=1$ and $\theta=4/7$. The bare coupling constant $g_0$ is quite small for graphene (about $1/20$). With increasing spatial scale, the running coupling constant $g$ decreases according to RG equation (32) from $g_0$ (equal to $\simeq 1/20$ for graphene) down to zero. Hence, at all scales $g \ll 1$. This justifies [62] the applicability of one-loop RG approach.

The quantum RG stops at $q = q_T$. The overall picture of the renormalization of $\varkappa$ is as follows. The RG flow

starts at $q \sim q_{\mathrm{uv}}$, where $\varkappa$ has a bare value $\varkappa_{0}$. In the interval $q_{T}<q<q_{\mathrm{uv}}$, the bending rigidity grows according to Eq. (32). The value of $\varkappa_{q}$ at the edge of the quantum interval (at $q \simeq q_{T}$) and the corresponding value of $g$ are given by
$$
\varkappa=\varkappa\left(\Lambda_{T}\right), \quad g=g\left(\Lambda_{T}\right),
$$
where $\varkappa(\Lambda)$ and $g=g(\Lambda)$ are given by Eq. (32) and
$$
\Lambda_{T}=\ln \left(q_{\mathrm{uv}} / q_{T}\right) \approx \ln \sqrt{T_{\mathrm{uv}} / T}.
$$

Below the couplings without indication of momentum scale (such as $g, \varkappa, B, Y$ ) will be understood as defined on the scale $\Lambda_{T}$ governed by the temperature. It is worth noting that values of $q_{*}$ and $q_{T}$ are determined by the renormalized elastic moduli:
$$
q_{T} \sim \frac{\sqrt{Y T}}{\varkappa \sqrt{g}} \sim \frac{\sqrt{Y_{0} T}}{\varkappa_{0}} \frac{1}{\sqrt{g_{0}}\left(1+g_{0} \Lambda_{T}\right)^{\theta / 4}} ; \quad(35)
$$
$$
q_{*} \sim \frac{\sqrt{Y T}}{\varkappa} \sim \frac{\sqrt{Y_{0} T}}{\varkappa_{0}} \frac{1}{\left(1+g_{0} \Lambda_{T}\right)^{(2+\theta) / 4}}. \quad(36)
$$

In the interval $q_{*}<q<q_{T}$, the bending rigidity does not change essentially (i.e., it changes by a factor of order unity). Finally, at lowest momenta $q<q_{*}$, the bending rigidity scales according to Eq. (8) with $\varkappa=\varkappa\left(\Lambda_{T}\right)$.

Now we are in a position to calculate the integrals entering Eqs. (21) and (22) and to get final formulas governing the thermodynamics of graphene. Results of this analysis are presented in the next section.

## IV. RESULTS
### A. Thermal expansion coefficient: Zero tension

The main contribution to $\xi_{0}$ as given by Eq.(21) comes from the region $q<q_{T}$. For $\eta \ll 1$, a simple calculation yields
$$
\xi_{0}^{2} \approx 1-\frac{d_{c} T}{8 \pi \varkappa}\left[\frac{2}{\eta}+\ln \left(\frac{1}{g}\right)\right].\quad(37)
$$

Here we neglect terms of the order of $g_{0}$ as well as ones of the order of $T / \varkappa$ coming from $q>q_{T}$. We, thus, obtain the thermal expansion coefficient of an unstressed membrane:
$$
\alpha_{T} \approx-\frac{d_{c}}{8 \pi \varkappa}\left[\frac{2}{\eta}+\ln \left(\frac{1}{g}\right)\right].\quad(38)
$$

Two terms in the square brackets represent contributions of momentum intervals $q<q_{*}$ and $q_{*}<q<q_{T}$, respectively. Comparing Eq. (38) with Eq. (11), we observe two differences.

Firstly, a logarithmic-in- $g$ term (reflecting the contribution of the momenta $q_{*}<q<q_{T}$ ) appeared in the square brackets. This term can be neglected for a generic membrane embedded in the space of high dimensionality $(d_{c} \to \infty, \eta \to 0)$ [57]. However, for graphene, where $\eta \simeq 0.8$ and $1 / g_{0} \simeq 20$, the two terms give comparable contributions. On the other hand, for a "nearly classical" 2D membrane in 3D space that has the same $\eta$ and much larger $1 / g_{0}$, the logarithmic contribution would be dominant.

Secondly, $\alpha_{T}$ becomes now a slow function of temperature. This dependence deserves a special attention. As follows from Eqs. (32) and (38), $\alpha_{T}$ remains negative and nearly constant in an extremely wide temperature range:
$$
\alpha_{T} \approx \alpha_{\max }=-\frac{d_{c}}{8 \pi \varkappa_{0}}\left[\frac{2}{\eta}+\ln \left(\frac{1}{g_{0}}\right)\right], \quad T_{0} \ll T \ll T_{\mathrm{uv}}.
$$

Here $T_{0}$ is given by Eq. (2), yielding for graphene $T_{0} \simeq 10^{-14} \mathrm{~K}$. Thus the thermal expansion coefficient of graphene remains nearly constant within almost twenty decades of temperature! Using graphene parameters $(d_{c}=1, \varkappa \simeq 1 \mathrm{eV})$, we get an estimate for this constant value: $\alpha_{T} \simeq-0.23 \mathrm{eV}^{-1}$.

Only at exponentially low temperatures, $T \ll T_{0}$, the thermal expansion coefficient starts to decay logarithmically with decreasing temperature:
$$
\alpha_{T} \simeq-\frac{d_{c}}{8 \pi \varkappa_{0}} \frac{\ln \ln \left(T_{\mathrm{uv}} / T\right)}{\left[\left(g_{0} / 2\right) \ln \left(T_{\mathrm{uv}} / T\right)\right]^{\theta}}, \quad T \ll T_{0}. \quad(40)
$$

The temperature dependence of $\alpha_{T}$ is shown in Fig. 3 for $T \ll T_{\mathrm{uv}}$.

It is instructive to analyze how the classical limit $(\hbar \to 0$, implying $g_{0} \to 0)$, is approached. We recall that the value of $\alpha_{T}$ depends logarithmically on $g_{0}$. Consequently, the thermal expansion coefficient (39) diverges in the classical limit. It should be emphasized, however, that the range of validity of Eq. (39) shrinks in this limit in view of Eq. (28). For temperatures above $T_{\mathrm{uv}}$, the logarithmic term in Eq. (39) gets modified, becoming temperature-dependent:
$$
\alpha_{T} \approx-\frac{d_{c}}{4 \pi \varkappa_{0}}\left[\frac{1}{\eta}+\ln \left(\frac{q_{\mathrm{uv}}}{q_{*}}\right)\right], \quad T \gg T_{\mathrm{uv}}. \quad(41)
$$

In other words, the function $\left|\alpha_{T}(T)\right|$ has a maximum at $T \simeq T_{\mathrm{uv}}$ (this maximum is not shown in Fig. 3, which is plotted for $T \ll T_{\mathrm{uv}}$ ). That is, it is the maximal value $\alpha_{\max }$ that diverges in the classical limit:
$$
\alpha_{\max } \propto-\ln \left(1 / g_{0}\right).
$$

### B. Thermal expansion coefficient: Finite tension

We turn now to a generalization of the above results to the case of non-zero tension, $\sigma \neq 0$. In this case, there appears a new characteristic momentum $q_{\sigma}$ determined by the condition
$$
\varkappa_{q} q_{\sigma}^{2} \sim \sigma.
$$

![](./images/867747616891339176_3.jpg)

FIG. 3: Temperature dependence of the thermal expansion coefficient for unstressed ($\sigma=0$) and stressed ($\sigma\neq0$) membrane. The tension $\sigma$ suppresses the thermal expansion at $T<T_{\sigma}$.

This momentum increases with $\sigma$, reaching the value of $q_{*}$ for $\sigma=\sigma_{*}$, where
$$
\sigma_{*} \varkappa_{q_{*}} q_{*}^{2} \sim \frac{d_{\mathrm{c}} Y T}{\varkappa}. \tag{42}
$$

We remind the reader that, for temperatures below $T_{\mathrm{uv}}$, couplings without the momentum indicated [such as $Y$ and $\varkappa$ in Eq. (42)] are understood as those including the quantum renormalization, i.e., defined on the temperature scale $q_{T}$. We have also taken into account in Eq. (42) that there is no essential renormalization of $\varkappa$ between the scales $q_{T}$ and $q_{*}$.

The physical meaning of $\sigma_{*}$ was discussed in Ref. 57. For $\sigma>\sigma_{*}$ the membrane shows linear Hooke's law, [57], while for $\sigma<\sigma_{*}$ the stress-strain relation is of a power-law form,
$$
\xi-\xi_{0} \propto \sigma^{\alpha},
$$
with an anomalous exponent $\alpha$ given by
$$
\alpha=\frac{\eta}{2-\eta}.
$$

One can express $\sigma_{*}$ in terms of the bulk modulus
$$
\sigma_{*}=\frac{d_{\mathrm{c}} C B T}{4 \pi \varkappa}, \tag{43}
$$
where $C$ is a numerical coefficient of order unity, which is chosen from the requirement that the low-stress deformation takes the form given by upper line of Eq. (48) below. This coefficient is determined by relations between values of elastic constants. (In principle, $C$ depends on the ratio of elastic module and, therefore, is a slow function of temperature [70].) The room-temperature value of $C$ for graphene, $C \simeq 0.25$, was found in Ref. 57 from a comparison of the analytic strain-stress relation with results of atomistic simulations of Ref. 71. [The definition of the coefficient $C$ in Eq. (43) differs from that in Ref. 57 by an additional factor $2 / \eta$, which is $\simeq 3$ for physical membranes.]

With further increase of $\sigma$ up to the value $\sigma_{*}/g$, the momentum $q_{\sigma}$ reaches the boundary of the quantum region:
$$
q_{\sigma} \simeq q_{T} \quad \text { for } \quad \sigma \simeq \sigma_{*} / g. \tag{44}
$$

Since we want to analyze a temperature dependence of membrane properties at non-zero tension $\sigma$, it is useful to introduce a characteristic temperature $T_{\sigma}$ determined by the condition $\sigma=\sigma_{*}(T)$,
$$
T_{\sigma}=\frac{4 \pi \varkappa \sigma}{d_{\mathrm{c}} C B} \sim \varkappa \frac{\sigma}{B}. \tag{45}
$$

The stress-induced deformation $s(\sigma)$ can be separated into classical and quantum parts:
$$
s(\sigma)=s_{\mathrm{cl}}(\sigma)+s_{\mathrm{quant}}(\sigma),
$$
where
$$
s_{\mathrm{cl}} \approx \frac{d_{\mathrm{c}} T}{4 \pi \rho} \int_{0}^{q_{T}} d q q^{3}\left(\frac{1}{\left(\omega_{q}^{0}\right)^{2}}-\frac{1}{\omega_{q}^{2}}\right), \tag{46}
$$
$$
s_{\text {quant }} \approx \frac{d_{\mathrm{c}}}{8 \pi \rho} \int_{q_{T}}^{q_{\mathrm{uv}}} d q q^{3}\left(\frac{1}{\omega_{q}^{0}}-\frac{1}{\omega_{q}}\right). \tag{47}
$$

For $\sigma<\sigma_{*}/g$, the classical contribution is essentially non-perturbative with respect to $\sigma$ (see Ref. 57):
$$
s_{\mathrm{cl}} \approx \frac{\sigma_{*}}{B} \begin{cases}(1 / \alpha)\left(\sigma / \sigma_{*}\right)^{\alpha}, & \text { for } \sigma<\sigma_{*} \\ (1 / 2 C)\left[2 / \eta+\ln \left(\sigma / \sigma_{*}\right)\right], & \text { for } \sigma_{*}<\sigma<\sigma_{*} / g.\end{cases}
$$

In contrast, the quantum contribution can be calculated perturbatively by expansion to the leading order in $\sigma$:
$$
\begin{aligned}
s_{\text {quant }} & =-\frac{d_{\mathrm{c}} \sigma}{8 \pi \rho} \int_{q_{T}}^{q_{\mathrm{uv}}} d q q^{3}\left(\frac{\partial \omega_{q}^{-1}}{\partial \sigma}\right)_{\sigma=0} \\
& =\sigma \int_{0}^{\Lambda_{T}} d \Lambda \frac{\partial B^{-1}}{\partial \Lambda}=\frac{\sigma}{B}-\frac{\sigma}{B_{0}}. \tag{49}
\end{aligned}
$$

Here we have used Eq. (29). Substituting $s_{\text {quant }}$ into Eq. (20), we see that quantum effects lead to a simple renormalization of the first term in the r.h.s. of Eq. (20): $\sigma/B_{0} \to \sigma/B$.

For a sufficiently large stress (or for a sufficiently low temperature), $\sigma>\sigma_{*}/g$, the momentum $q_{\sigma}$ becomes larger than $q_{T}$, so that one can neglect the term $\varkappa q q^{4}$ in Eq. (23) in comparison with $\sigma q^{2}$ in the whole classical region. In this case, Eq. (20) takes the form
$$
\xi^{2}=\xi_{\sigma}^{2}+\frac{\sigma}{B_{\sigma}},
$$

where $B_\sigma$ is the renormalized value of the bulk modulus
[see Eq. (33)] at the scale $q_\sigma \simeq \sqrt{\sigma/\varkappa}$, and

$$
\xi_{\sigma}^{2} \approx 1-\frac{d_{\mathrm{c}}}{8 \pi \sqrt{\rho \sigma}} \int d q q^{2}\left[\operatorname{coth}\left(\frac{\sqrt{\sigma} q}{2 \sqrt{\rho} T}\right)-1\right].
$$

Here we neglected small $(\sim g)$ terms. The integral in this
formula scales with decreasing temperature as $T^{3}$.

Summarizing the obtained results, we find

$$
\xi^{2}-1 \approx\left\{\begin{aligned}
-\frac{d_{\mathrm{c}} T}{8 \pi \varkappa}\left[\frac{2}{\eta}+\ln \left(\frac{1}{g}\right)\right]+\frac{\sigma_{*}}{\alpha B}\left(\frac{\sigma}{\sigma_{*}}\right)^{\alpha}, & \text { for } \sigma<\sigma_{*}, \\
\frac{\sigma}{B}-\frac{d_{\mathrm{c}} T}{8 \pi \varkappa} \ln \left(\frac{\sigma_{*}}{\sigma g}\right), & \text { for } \sigma_{*}<\sigma<\sigma_{*} / g, \\
\frac{\sigma}{B_{\sigma}}-\frac{d_{\mathrm{c}} \rho T^{3} \zeta(3)}{2 \pi \sigma^{2}}, & \text { for } \sigma_{*} / g<\sigma .
\end{aligned}\right.
$$

From Eqs. (24) and (50), we obtain the thermal expan-
sion coefficient $\alpha_{T}$ as a function of applied stress:

$$
\alpha_{T} \approx-\frac{d_{\mathrm{c}}}{8 \pi \varkappa}\left\{\begin{aligned}
2 / \eta+\ln (1 / g)-C_{1}\left(\sigma / \sigma_{*}\right)^{\alpha}, & \text { for } \sigma<\sigma_{*}, \\
\ln \left(\sigma_{*} / \sigma g\right), & \text { for } \sigma_{*}<\sigma<\sigma_{*} / g, \\
12 \zeta(3) \rho T^{2} \varkappa / \sigma^{2}, & \text { for } \sigma_{*} / g<\sigma,
\end{aligned}\right.
$$

where $C_{1}=4 C(1-\eta) / \eta$ and $\zeta(3) \simeq 1.202$ is the Reimann
zeta function.

The dependence of $\alpha_{T}$ on $T$ for stressed and unstressed
membrane following from Eq. (51) is shown in Fig. 3. (In
this figure, we assume for the stressed case that $g_{0} T_{\sigma} \gg$
$T_{0}$.) At high temperatures, $T \gg T_{\sigma}$, the external tension
results in a power-law dependence of $\alpha_{T}$ on temperature:

$$
\alpha_{T} \approx-\frac{d_{\mathrm{c}}}{8 \pi \varkappa}\left[\frac{2}{\eta}+\ln \frac{1}{g}-C_{1}\left(\frac{T_{\sigma}}{T}\right)^{\alpha}\right]. \quad (52)
$$

Below $T_{\sigma}$, the absolute value of the thermal expansion
coefficient decreases logarithmically:

$$
\alpha_{T} \approx-\frac{d_{\mathrm{c}}}{8 \pi \varkappa} \ln \frac{T}{g T_{\sigma}}, \quad g T_{\sigma} \ll T \ll T_{\sigma}. \quad (53)
$$

Finally, at still lower temperatures, $T \ll g T_{\sigma}$, we find
$\alpha_{T} \propto T^{2}$, see the third line in Eq. (51).

### C. Effective bulk modulus

Differentiating Eq. (50) over $\sigma$, we find expression for
effective bulk modulus

$$
\begin{aligned}
& \frac{1}{B_{\text {eff }}}=\left(\frac{\partial \xi^{2}}{\partial \sigma}\right)_{T} \\
& =\left\{\begin{aligned}
(1 / B)\left(\sigma_{*} / \sigma\right)^{1-\alpha}, & \text { for } \sigma<\sigma_{*}, \\
1 / B+d_{\mathrm{c}} T / 8 \pi \varkappa \sigma, & \text { for } \sigma_{*}<\sigma<\sigma_{*} / g, \\
1 / B_{\sigma}+d_{\mathrm{c}} \zeta(3) \rho T^{3} / \pi \sigma^{3}, & \text { for } \sigma_{*} / g<\sigma,
\end{aligned}\right.
\end{aligned}
$$

![](./images/867747616891339176_4.jpg)

FIG. 4. Temperature dependences of (a) strain $\xi$ for fixed
stress $\sigma$, and (b) stress for fixed strain. Positions of crumpling
(in the left panel) and buckling (in the right panel, for $\xi<1$ )
transitions are indicated.

Two upper lines of Eq. (54) were obtained previously in
Ref. 57. In the second and third line we took into account
small temperature-dependent corrections. The third line
shows that $B_{\text {eff }}$ slowly increases with $\sigma$ at $\sigma>\sigma_{*} / g$ due
to suppression of quantum RG by external stress:

$$
B_{\mathrm{eff}} \simeq B_{\sigma}=\frac{B_{0}}{\left[1+\left(g_{0} / 2\right) \ln \left(\mu_{0} / \sigma\right)\right]^{1-3 \theta / 2}}. \quad (55)
$$

[Here we assume for simplicity that $Y=8 B / 3$, use
Eq. (27) and write $\ln \left(q_{\mathrm{uv}} / q_{\sigma}\right)$ with the logarithmic pre-
cision].

### D. General phase diagram of membrane

In Fig. 4, we plot the temperature dependence of the
strain $\xi$ for fixed stress $\sigma$ (Fig. 4a) as well as the temper-
ature dependence of the stress for fixed strain (Fig. 4b).

As seen from Fig. 4a, with increasing temperature for the fixed $\sigma$, the membrane undergoes crumpling transition ($\xi \to 0$). Corresponding critical temperature increases with the applied stress [57]. The dependence $T_{\text{cr}}(\sigma)$ can be found from the upper line of Eq. (50) by requirement $\xi = 0$ and by taking into account Eqs. (43) and (32). The plot shown in Fig. 4b corresponds to an experimental setup in which the membrane in-plane area is kept fixed, while the temperature is varied. If this area is smaller than the intrinsic zero-temperature area of the membrane (i.e., $\xi < 1$), the membrane undergoes in the process of cooling a buckling transition.

### E. Specific heat

We evaluate now the temperature dependence of the specific heat. Similar to the thermal expansion coefficient $\alpha_T$, both constant-volume ($C_V$) and constant-pressure ($C_P$) specific heat capacities are determined by FP. To evaluate them, we first determine the entropy of the membrane,
$$
S = -L^{-2}(\partial F/\partial T)_{\xi},
$$
where $F$ is the free energy given by Eq. (14). We find
$$
\begin{aligned}
S &= d_{\mathrm{c}} \int \frac{d^{2} \mathbf{q}}{(2 \pi)^{2}}\left[\left(N_{q}+1\right) \ln \left(N_{q}+1\right)-N_{q} \ln N_{q}\right. \\
& \left.-\left(N_{q}+1 / 2\right)\left(\partial \omega_{q} / \partial T\right)_{\sigma}\right],
\end{aligned}\qquad(56)
$$
where $N_q = [\exp(\omega_q/T)-1]^{-1}$ is the Bose function. It is worth noting that the last term in the square brackets in Eq. (56) is nonzero because of the temperature-dependent renormalization of the bending rigidity $\varkappa$ [see Eq. (8)]. By using Eq. (56), one can calculate the specific heat capacities,
$$
C_{P,V} = -T\left(\partial S/\partial T\right)_{P,V}.
$$

A straightforward calculation shows that, in the leading order, both $C_P$ and $C_V$ are given by the classical formula for phonons with a parabolic spectrum,
$$
C_{P} \approx C_{V} \approx d_{\mathrm{c}} \int \frac{d^{2} \mathbf{q}}{(2 \pi)^{2}} \omega_{q} \frac{\partial N_{q}}{\partial T} \approx \frac{\pi d_{\mathrm{c}} \sqrt{\rho} T}{12 \sqrt{\varkappa}}.\qquad(57)
$$

In the presence of a finite tension, this result is valid for temperatures $T \gg gT_{\sigma}$ (or, equivalently, the tension $\sigma \ll \ast_*/g$). At low temperatures, $T \ll gT_{\sigma}$, the specific heat is proportional to $T^2$:
$$
C_{P} \approx C_{V} \approx \frac{3 \zeta(3) d_{\mathrm{c}} \rho}{\pi \sigma} T^{2}.\qquad(58)
$$

While the leading contribution to both $C_P$ and $C_V$ is due to classical fluctuations, the difference $C_P - C_V$ is small, proportional to $g$, and, therefore, is due to the quantum effects:
$$
\frac{C_{P}-C_{V}}{C_{P}}=T \frac{\left(\partial \xi^{2} / \partial T\right)_{\sigma}^{2}}{C_{P}\left(\partial \xi^{2} / \partial \sigma\right)_{T}}\qquad(59)
$$

$$
\sim g \begin{cases}\ln ^{2}(1 / g)\left(\sigma / \sigma_{*}\right)^{1-\alpha}, & \text { for } \sigma \ll \sigma_{*}, \\ {\left[\ln \left(\sigma_{*} / g \sigma\right)\right]^{2},} & \text { for } \sigma_{*} \ll \sigma \ll \sigma_{*} / g, \\ \left(B_{\sigma} / B\right)\left(\sigma_{*} / g \sigma\right)^{3}, & \text { for } \sigma_{*} / g \ll \sigma\end{cases}
$$

Hence, at high temperatures, $T \gg T_{\sigma}$, we find
$$
\frac{C_{P}-C_{V}}{C_{P}} \sim g \ln ^{2}\left(\frac{1}{g}\right)\left(\frac{T_{\sigma}}{T}\right)^{1-\alpha}.\qquad(60)
$$

At intermediate temperatures, $gT_{\sigma} \ll T \ll T_{\sigma}$, the result reads
$$
\frac{C_{P}-C_{V}}{C_{P}} \sim g \ln ^{2} \frac{T}{g T_{\sigma}},\qquad(61)
$$
while at very law temperature $T \ll gT_{\sigma}$, we obtain
$$
\frac{C_{P}-C_{V}}{C_{P}} \sim g\left(\frac{T}{g T_{\sigma}}\right)^{3} \frac{B_{\sigma}}{B} \sim \frac{\rho T^{3} B_{\sigma}}{\sigma^{3}}.\qquad(62)
$$

We emphasize that $C_P - C_V$ vanishes in the absence of the external tension ($\sigma = 0$), as follows from Eq. (60) with $T_{\sigma} = 0$.

### F. Grüneisen parameter

Finally, we consider the macroscopic Grüneisen parameter
$$
\gamma=\frac{\alpha_{T}\left(\partial \sigma / \partial \xi^{2}\right)_{T}}{C_{V}},\qquad(63)
$$
which is an important characteristics of thermomechanical properties of a system. We find that the Grüneisen parameter is negative for all values of stress:
$$
\gamma \sim-\frac{g \varkappa}{T} \begin{cases}\ln (1 / g)\left(\sigma / \sigma_{*}\right)^{1-\alpha}, & \text { for } \sigma \ll \sigma_{*}, \\ \ln \left(\sigma_{*} / g \sigma\right), & \text { for } \sigma_{*} \ll \sigma \ll \sigma_{*} / g, \\ \left(B_{\sigma} / B\right)\left(\sigma_{*} / g \sigma\right), & \text { for } \sigma_{*} / g \ll \sigma.\end{cases}
$$

Several points deserves special attention. First of all, we see that the absolute value of $\gamma$ has a maximum as a function of $\sigma$ at $\sigma \simeq \sigma_*$. On the other hand, for fixed $\sigma$, $|\gamma|$ is a monotonously decreasing function of $T$. Most importantly, in the limit of low temperature, $\gamma$ turns out to be non-zero
$$
-\gamma \sim \frac{B_{\sigma}}{\sigma}, \quad \text { for } T \rightarrow 0.\qquad(65)
$$

Schematic dependence of the Grüneisen parameter on tension and temperature is illustrated in Fig. 5.

![](./images/867747616891339176_5.jpg)

FIG. 5: Schematic dependence of the Grüneisen parameter on tension at fixed temperature (a) and on temperature for fixed tension (b).

### G. Third law of thermodynamics

Let us point out that the third law of thermodynamics manifests itself in this problem in a somewhat curious way. Indeed, the entropy (56) vanishes in the limit $T \to 0$ for any $\sigma$ even if the quantum renormalization effects are neglected. On the other hand, it is easy to see from the first line of Eq. (51) that $\left.\alpha_{T}\right|_{\sigma=0}$ remains finite in the limit $T \to 0$. At first glance, this may seem to contradict to Eq. (1) that yields $\alpha_{T}=\partial S / \partial \sigma$. This apparent contradiction is resolved by noticing that non-analyticity of $S$ at $T=0$, $\sigma=0$ leads to non-commutativity of limits $T \to 0$ and $\sigma \to 0$ for the function $\alpha_{T}(T, \sigma)$. Quantum renormalization effects restore the vanishing of the thermal expansion coefficient at $T=0$ independently of the order of the limits, which is conventionally considered as a manifestation of the third law.

## V. CONCLUSION

To summarize, we have developed a theory of thermomechanical properties of a suspended graphene membrane. We have shown that at zero tension the thermal expansion coefficient $\alpha_{T}$ of free-standing graphene is negative and temperature-independent in a very broad temperature range, see Eq. (39). The underlying physics of the negative expansion is the global shrinking of the graphene membrane in the longitudinal direction due to classical transverse fluctuations.

The second term in Eq. (39) for $\alpha_{T}$ is governed by the dimensionless quantum coupling constant, $g_{0} \ll 1$. This coupling constant vanishes in the classical limit $\hbar \to 0$ (thus implying a divergence of $\alpha_{T}$ ) and is equal to $\simeq 0.05$ for graphene. The small value of $g_{0}$ ensures that $\alpha_{T}$ remains $T$-independent down to extremely low temperature $T_{0}$, Eq. (2). For graphene parameters, we estimate the value of the thermal expansion coefficient as $\alpha_{T} \simeq-0.23 \mathrm{eV}^{-1}$, which applies below the temperature $T_{\mathrm{uv}} \sim g_{0} \varkappa_{0} \sim 500 \mathrm{~K}$ (where $\varkappa_{0} \sim 1 \mathrm{eV}$ is the bending rigidity) down to $T_{0} \sim 10^{-14} \mathrm{~K}$. For $T<T_{0}$, the absolute value of the thermal expansion coefficient starts to decrease logarithmically slowly with decreasing temperature, Eq. (40), since quantum effects lead to increase of the bending rigidity. Our results imply that, contrary to naive expectations, quantum fluctuations do not lead to the melting or crumpling of a 2D crystal but instead stabilize the membrane due to enhanced role of the anharmonicity.

A finite tension $\sigma$ suppresses the thermal expansion at $T<T_{\sigma}$, where $T_{\sigma} \propto \sigma$ is the characteristic temperature which separates regimes of conventional $\left(T<T_{\sigma}\right)$ and anomalous $\left(T>T_{\sigma}\right)$ elasticity, see Fig. 3.

We have also evaluated the temperature dependence of tension in a graphene membrane placed into a frame of a fixed size $\xi L$. With lowering temperature, a membrane with $\xi<1$ undergoes then a buckling transition, see Fig. 4b.

Finally, we have calculated the specific heat of the membrane. We have found that in the leading order both $C_{P}$ and $C_{V}$ are dominated by classical effects and are given by a standard expression for phonons with parabolic spectrum. On the other hand, a small difference $C_{P}-C_{V}$ is due to quantum fluctuations and shows a very non-trivial behavior as a function of the ratio $T / T_{\sigma}$, see Eqs. (60), (61), and (62). The same ratio $T / T_{\sigma}$ determines the temperature and stress dependence of the Grüneisen parameter, which turns out to be negative for all temperatures and tensions, being monotonous function of $T$ (for fixed $\sigma$ ) and showing a minimum as a function of $\sigma$ (for fixed $T$ ) for $\sigma \simeq \sigma_{*}$.

Our results demonstrate that 2D materials are dramatically different from 3D ones where, according to Grüneisen law, the thermal expansion coefficient is proportional to the heat capacity and goes to zero as $T \to 0$ as a power law of temperature. It would be very interesting to check our prediction for the low-temperature behavior of $\alpha_{T}$ experimentally. In particular, the thermal expansion coefficient can be measured from the temperature shift of Raman spectra [34]. An alternative (and possibly an easier) way of determining $\alpha_{T}$ is provided by studies of van der Waals heterostructures such as

graphene/hBN, graphene/MoS₂, etc. [72, 73]. In this setting, large thermal expansions of 2D materials at low temperatures would result in a strong temperature de- pendence of lattice mismatch which can be seen via re- construction of Moire patterns [74-76] or via character- istics of graphene bubbles on a substrate [77].

## VI. ACKNOWLEDGEMENT

We thank E. I. Kats, V. V. Lebedev, and K. S. Novoselov for useful discussions. The work was sup- ported by the Russian Science Foundation (grant No. 14-42-00044). MIK acknowledges a support by NWO via Spinoza Prize.

### Appendix A: Calculation of free energy

In this Appendix we calculate the free energy corre- sponding to the Lagrangian (13). The partition function reads
$$
Z=\int\{D \mathbf{r}\} e^{-S}, \quad S=\int_{0}^{\beta} d \tau \int d^{2} \mathbf{x} \mathcal{L}, \quad \text { (A1) }
$$
where $\beta=1 / T$. In terms of $\mathbf{u}, \mathbf{h}$, and $\xi$ introduced in Eq. (4), the Lagrangian density becomes
$$
\mathcal{L}=\frac{\rho}{2}\left(\dot{\mathbf{u}}^{2}+\dot{\mathbf{h}}^{2}\right)+\frac{\mu+\lambda}{2}\left[\left(\xi^{2}-1+\frac{K}{2}\right)^{2}-\frac{K^{2}}{4}\right]+\mathcal{L}_{0}, \quad (\mathrm{~A} 2)
$$
where $\dot{\mathbf{u}}=\partial \mathbf{u} / \partial \tau, \dot{\mathbf{h}}=\partial \mathbf{h} / \partial \tau$,
$$
K=2\left\langle u_{\alpha \alpha}\right\rangle_{\mathbf{x}, \tau}=\left\langle\partial_{\alpha} \mathbf{h} \partial_{\alpha} \mathbf{h}+\partial_{\alpha} \mathbf{u} \partial_{\alpha} \mathbf{u}\right\rangle_{\mathbf{x}, \tau}, \quad \text { (A3) }
$$

$$
u_{\alpha \beta}=\left[\xi\left(\partial_{\alpha} u_{\beta}+\partial_{\beta} u_{\alpha}\right)+\partial_{\alpha} \mathbf{h} \partial_{\beta} \mathbf{h}+\partial_{\alpha} \mathbf{u} \partial_{\beta} \mathbf{u}\right] / 2, \text { (A4) }
$$
$\langle\cdots\rangle_{\mathbf{x}, \tau}$ denotes the spatial and time averaging,
$$
\langle\cdots\rangle_{\mathbf{x}, \tau}=\int \frac{d^{2} \mathbf{x}}{L^{2}} \int_{0}^{\beta} \frac{d \tau}{\beta} \cdots,
$$
and
$$
\mathcal{L}_{0}=\frac{\varkappa}{2}\left[(\Delta \mathbf{h})^{2}+(\Delta \mathbf{u})^{2}\right]+\mu u_{i j}^{2}+\frac{\lambda}{2} u_{i i}^{2}. \quad \text { (A5) }
$$

Equation (A4) coincides with the conventional expression for the strain tensor of the membrane provided that $\xi=1$ and the term $\partial_{\alpha} \mathbf{u} \partial_{\beta} \mathbf{u}$ in the square brackets (which is of the second order in $\partial_{\alpha} \mathbf{u}$ and thus much smaller than the first term) is neglected. Within such an approximation, and neglecting also a small term $\varkappa(\Delta \mathbf{u})^{2} / 2$ in Eq. (A5), the Lagrangian $\mathcal{L}_{0}(\mathbf{u}, \mathbf{h})$ coincides with the textbook ex- pression for elastic energy of a nearly flat membrane. [38]

The term $(\mu+\lambda) K^{2} / 8$ in Eq. (A2) represents a quatric interaction (with $h^{4}, u^{4}$, and $h^{2} u^{2}$ couplings) with zero transferred momentum and energy, $q=0$ and $\Omega=0$ (zero mode). After combining this term with the analogous quartic zero-mode term coming from $\mathcal{L}_{0}$, the zero-mode contribution can be safely neglected because it gives a negligibly small correction to the self-energies of both flexural and in-plain phonons (see detailed discussion in the Supplementary Material of Ref. 57)

In the $(\mathbf{q}, \omega)$ representation, the action we are left with reads
$$
\begin{aligned}
S & =\int_{\mathbf{q} \omega}\left[\frac{\rho \omega^{2}+\varkappa q^{4}}{2}\left(\left|\mathbf{h}^{\mathbf{q}, \omega}\right|^{2}+\left|\mathbf{u}^{\mathbf{q}, \omega}\right|^{2}\right)\right. \quad \text { (A6) } \\
& \left.+\mu\left|u_{\alpha \beta}^{\mathbf{q}, \omega}\right|^{2}+\frac{\lambda}{2}\left|u_{\alpha \alpha}^{\mathbf{q}, \omega}\right|^{2}\right]+\frac{\mu+\lambda}{2} \frac{L^{2}}{T}\left(\xi^{2}-1+\frac{K}{2}\right)^{2}.
\end{aligned}
$$

Here $\int_{\mathbf{q} \omega}$ stands for $T \sum_{\omega} \int d^{2} \mathbf{q} /(2 \pi)^{2}$ and summation goes over Matsubara frequencies $\omega=2 \pi n T$. The next step is to integrate $\exp (-S)$ over $\mathbf{u}$ and $\mathbf{h}$. To carry out this integration, we first perform a Hubbard-Stratonovich de- coupling of the last term in Eq. (A7) by an integral over an auxiliary field $\chi$,
$$
\begin{aligned}
& \exp \left[-\frac{L^{2}(\mu+\lambda)}{2 T}\left(\xi^{2}-1+\frac{K}{2}\right)^{2}\right]=\frac{L}{\sqrt{2 \pi(\mu+\lambda) T}} \\
& \times \int d \chi \exp \left\{-\left[\frac{\chi^{2}}{2(\mu+\lambda)}-i \chi\left(\xi^{2}-1+\frac{K}{2}\right)\right] \frac{L^{2}}{T}\right\}.
\end{aligned}
$$

This yields
$$
\begin{aligned}
e^{-S} & =\frac{L}{\sqrt{2 \pi(\mu+\lambda) T}} \int d \chi e^{-S_{\chi}} \quad \text { (A7) } \\
& \times \exp \left\{\frac{L^{2}}{T}\left[-\frac{\chi^{2}}{2(\mu+\lambda)}+i \chi\left(\xi^{2}-1\right)\right]\right\},
\end{aligned}
$$
where
$$
\begin{aligned}
S_{\chi} & =\int_{\mathbf{q} \omega}\left[\frac{\rho \omega^{2}+\varkappa q^{4}-i \chi}{2}\left(\left|\mathbf{h}^{\mathbf{q}, \omega}\right|^{2}+\left|\mathbf{u}^{\mathbf{q}, \omega}\right|^{2}\right)\right. \\
& \left.+\mu\left|u_{\alpha \beta}^{\mathbf{q}, \omega}\right|^{2}+\frac{\lambda}{2}\left|u_{\alpha \alpha}^{\mathbf{q}, \omega}\right|^{2}\right].
\end{aligned}
$$

We will first discuss what happens in the harmonic ap- proximation and later include the anharmonic coupling between the in-plane and out-of-plane modes. In the har- monic approximation, $S_{\chi}$ simplifies,
$$
\begin{aligned}
S_{\chi} & =\int_{\mathbf{q} \omega}\left[\frac{\rho \omega^{2}+\varkappa q^{4}-i \chi}{2}\left(\left|\mathbf{h}^{\mathbf{q}, \omega}\right|^{2}+\left|\mathbf{u}^{\mathbf{q}, \omega}\right|^{2}\right)\right. \\
& \left.+\frac{\mu \xi^{2}}{2} q^{2}\left|\mathbf{u}^{\mathbf{q}, \omega}\right|^{2}+\frac{(\mu+\lambda) \xi^{2}}{2}\left|\mathbf{q} \mathbf{u}^{\mathbf{q}, \omega}\right|^{2}\right]. \quad \text { (A9) }
\end{aligned}
$$

After having performed here the Gaussian integration over $u$ and $h$, we are left with an integral over $d \chi$, which

can be calculated by the stationary-phase method. De- noting the value of $\chi$ obeying the stationary-phase con dition as
$$\chi_{0}=i \sigma_{0},$$
we express the free energy $F$ in terms of $\sigma_{0}$ and $\xi$ :
$$\begin{aligned}
\frac{F}{L^{2}}= & -\frac{\sigma_{0}^{2}}{2(\mu+\lambda)}+\sigma_{0}\left(\xi^{2}-1\right) \quad \text { (A10) } \\
& +\frac{1}{2} \int_{\mathbf{q} \omega}\left\{d_{c} \ln \left(\varkappa q^{4}+\sigma_{0} q^{2}+\rho \omega^{2}\right)\right. \\
& +\ln \left[\varkappa q^{4}+\left(\sigma_{0}+\mu \xi^{2}\right) q^{2}+\rho \omega^{2}\right] \\
& \left.+\ln \left[\varkappa q^{4}+\left(\sigma_{0}+[2 \mu+\lambda] \xi^{2}\right) q^{2}+\rho \omega^{2}\right]\right\}.
\end{aligned}$$

Effects of the anharmonic coupling between in-plane and flexural modes lead to the following modifications of Eq. (A10). First, the bending rigidity $\varkappa$ gets renormal ized, $\varkappa \to \varkappa_{q}$ , as discussed in Sec. I. Second, there arises a self-energy correction [37] $\sigma_{1}$ to $\sigma_{0}$ in the arguments of logarithms. We will calculate $\sigma_{1}$ in Appendix B. As discussed in Sec. III A and in Appendix B, the total coef- ficient of the $q^{2}$ term in the phonon propagator is exactly the external tension $\sigma$ ,
$$\sigma_{0}+\sigma_{1}=\sigma. \quad \text { (A11) }$$

This relation is a manifestation of a Ward identity that is verified within the RG analysis (in one-loop order) in Appendix D.
The stationary-point condition $\partial F / \partial \sigma_{0}=0$ yields
$$\begin{aligned}
\frac{\sigma_{0}}{\mu+\lambda}= & \xi^{2}-1+\frac{1}{2} \int_{\mathbf{q} \omega}\left[\frac{d_{c} q^{2}}{\varkappa q^{4}+\left(\sigma_{0}+\sigma_{1}\right) q^{2}+\rho \omega^{2}}\right. \\
& +\frac{q^{2}}{\left(\sigma_{0}+\sigma_{1}+\mu \xi^{2}\right) q^{2}+\rho \omega^{2}} \\
& \left.+\frac{q^{2}}{\left[\sigma_{0}+\sigma_{1}+(2 \mu+\lambda) \xi^{2}\right] q^{2}+\rho \omega^{2}}\right].
\end{aligned}$$

Here, we have neglected the term $\varkappa q^{4}$ which is small compared to $\mu \xi^{2} q^{2}$ and $(2 \mu+\lambda) \xi^{2} q^{2}$ . The stretching pa rameter $\xi$ entering this equation is fixed by the external tension $\sigma$ , which is given by a derivative of the free en ergy with respect to the "projected area" of the sample, A = 2L2 (see Eq. (15)). Substituting Eq. (A10) into Eq. (15), we get
$$\begin{aligned}
\sigma= & \sigma_{0}+\frac{1}{2} \int_{\mathbf{q} \omega}\left[\frac{\mu q^{2}}{\left(\sigma_{0}+\sigma_{1}+\mu \xi^{2}\right) q^{2}+\rho \omega^{2}}\right. \\
& \left.+\frac{(2 \mu+\lambda) q^{2}}{\left[\sigma_{0}+\sigma_{1}+(2 \mu+\lambda) \xi^{2}\right] q^{2}+\rho \omega^{2}}\right].
\end{aligned}$$

Neglecting in the denominator the tension $\sigma_{0}+\sigma_{1}=\sigma$ (which is assumed to be much smaller than the in-plane elastic moduli $\mu$ and $\lambda$ ), we get
$$\sigma=\sigma_{0}+\delta \sigma, \quad \text { (A14) }$$
where
$$\delta \sigma=\frac{1}{2} \int_{\mathbf{q} \omega}\left[\frac{\mu q^{2}}{\mu \xi^{2} q^{2}+\rho \omega^{2}}+\frac{(2 \mu+\lambda) q^{2}}{(2 \mu+\lambda) \xi^{2} q^{2}+\rho \omega^{2}}\right]. \quad(\mathrm{A} 15)$$

We will show in Appendix B that the one-loop contri- butions $\sigma_{1}$ and $\delta \sigma$ arising in the analysis of the tension on the basis of the FP Green function and of the ther- modynamic relation, Eq. (15), respectively, are identical,01 = oo, so that Eqs. (A11) and (A14) are fully consis- tent.

## Appendix B: Anharmonic coupling between in-plane and out-of-plane phonons
In this Appendix, we provide a derivation of the self- energy correction $\sigma_{1}$ in Eq. (A12), which is generated by the anharmonic coupling between in-plane and out-of- plane modes. In combination with results of Appendix A, this allows us to derive equations (14) and (20) the main text used there for the analysis of thermomechanical properties of the membrane.
We begin with the action (A8). Integrating out the in-plane modes, we get an energy functional which onlydepends on h-fields: [37]
$$E[h]=\frac{1}{2} \int_{\mathbf{q} \Omega}\left(\varkappa q^{4}+\rho \omega^{2}\right)\left|\mathbf{h}^{\mathbf{q} \omega}\right|^{2}+\frac{1}{8} \int_{\mathbf{q} \Omega} \int_{\mathbf{Q} \omega} \int_{\mathbf{Q}^{\prime} \omega^{\prime}} R^{\alpha \beta \gamma \theta}(\mathbf{q}, \Omega)\left(Q_{\alpha}-q_{\alpha}\right) Q_{\beta}\left(Q_{\gamma}^{\prime}+q_{\gamma}\right) Q_{\theta}^{\prime}\left(\mathbf{h}_{\mathbf{Q}}^{\omega} \mathbf{h}_{\mathbf{q}-\mathbf{Q}}^{\Omega-\omega}\right)\left(\mathbf{h}_{\mathbf{Q}^{\prime}}^{\omega^{\prime}} \mathbf{h}_{-\mathbf{q}-\mathbf{Q}^{\prime}}^{\Omega-\omega^{\prime}}\right) \quad(\mathrm{B} 1)$$

Here $R^{\alpha \beta \gamma \theta}(q, \Omega)$ is the coupling tensor with the following nonzero components [in the basis of vectors n=

$(-q_y, q_x)/|q|$, $\mathbf{m} = \mathbf{q}/|q|]$:

$$
R^{nnnn} = \frac{4\mu(\mu+\lambda)}{2\mu+\lambda}+\frac{\rho\Omega^2\lambda^2}{(2\mu+\lambda)[q^2(2\mu+\lambda)\xi^2+\rho\Omega^2]}, \tag{B2}
$$

$$
R^{mmmm} = \frac{\rho\Omega^2(2\mu+\lambda)}{q^2(2\mu+\lambda)\xi^2+\rho\Omega^2}, \tag{B3}
$$

$$
R^{mmnn}=R^{nnmm}=\frac{\rho\Omega^2\lambda}{q^2(2\mu+\lambda)\xi^2+\rho\Omega^2}, \tag{B4}
$$

$$
R^{mnmn} = \frac{4\rho\Omega^2\mu}{q^2\mu\xi^2+\rho\Omega^2}. \tag{B5}
$$

The $R^{\alpha\beta\gamma\theta}$ couplings characterize the quartic interaction of the out-of-plane modes. This interaction generates self-energies the $hh$ correlation functions. The coupling constant $R^{nnnn}$ leads to a self-energy that scales as $q^4\ln q$ and, therefore, is responsible for the power-law renormalization of $\varkappa$. On the other hand, the couplings $R^{mmmm}$ and $R^{mnmn}$ lead to self-energy corrections that scale as $q^2$. Specifically, the self-energy originating from the coupling $R^{mmmm}$ reads

$$
\begin{aligned}
\Sigma_{\mathbf{Q},\Omega}^{mmmm} &= \int_{\mathbf{q}\omega} \frac{(\mathbf{Qq}-q^2)^2(\mathbf{Qq})^2}{q^4} \frac{\rho(2\mu+\lambda)\omega^2}{(2\mu+\lambda)q^2\xi^2+\rho\omega^2} \\
&\times \frac{1}{\varkappa(\mathbf{q-Q})^4+\rho(\omega-\Omega)^2} \tag{B6}
\end{aligned}
$$

(the factor $1/8$ in the coupling is cancelled due to 8 pairing possibilities of $h$ fields.) In the limit $\Omega\rightarrow0$ $Q\rightarrow0$, we get

$$
\Sigma_{Q\rightarrow0,\Omega\rightarrow0}^{mmmm} = \frac{Q^2}{2} \int_{\mathbf{q}\omega} \frac{\rho(2\mu+\lambda)q^2\omega^2}{(2\mu+\lambda)\xi^2q^2+\rho\omega^2} \frac{1}{\varkappa q^4+\rho\omega^2}
\tag{B7}
$$

The integral is determined by the ultraviolet cut-off of the theory $q_{\text{uv}}$. For $q<q_{\text{uv}}$, one can neglect the term $\varkappa q^4$ in the denominator. This yields

$$
\Sigma^{mmmm} \simeq Q^2\sigma_1^{mmmm},
$$

with

$$
\sigma_1^{mmmm} \approx \frac{1}{2} \int_{\mathbf{q}\omega} \frac{(2\mu+\lambda)q^2}{(2\mu+\lambda)\xi^2q^2+\rho\omega^2}. \tag{B8}
$$

Proceeding in the same way, we find

$$
\sigma_1^{mnmn} \approx \frac{1}{2} \int_{\mathbf{q}\omega} \frac{\mu q^2}{\mu\xi^2q^2+\rho\omega^2}. \tag{B9}
$$

Combining these contributions, we get the following result for the total one-loop coefficient

$$
\sigma_1 = \sigma_1^{mmmm} + \sigma_1^{mnmn}
$$

of the $Q^2$ self-energy:

$$
\sigma_1 \approx \frac{1}{2} \int_{\mathbf{q}\omega} q^2 \left[ \frac{2\mu+\lambda}{(2\mu+\lambda)\xi^2q^2+\rho\omega^2} + \frac{\mu}{\mu\xi^2q^2+\rho\omega^2}. \right]
\tag{B10}
$$

Comparing this equation with Eq. (A15), we satisfy ourselves that

$$
\sigma_1 = \delta\sigma, \tag{B11}
$$

as was stated in the end of Appendix A. In combination with Eq. (A14), this yields Eq. (A11).

We have thus explicitly demonstrated that Eq. (A12) can be written in terms of the applied tension $\sigma$,

$$
\frac{\sigma}{\mu+\lambda} = \xi^2 - 1 + \frac{1}{2} \int_{\mathbf{q}\omega} \frac{d_c q^2}{\varkappa q^4+\sigma q^2+\rho\omega^2} + a, \tag{B12}
$$

where

$$
\begin{aligned}
a &= \frac{1}{2(\mu+\lambda)} \int_{\mathbf{q}\omega} q^2 \left[ \frac{2\mu+\lambda}{(\sigma+\mu\xi^2)q^2+\rho\omega^2} \right. \\
&\quad \left. + \frac{3\mu+2\lambda}{[\sigma+(2\mu+\lambda)\xi^2]q^2+\rho\omega^2} \right]
\end{aligned} \tag{B13}
$$

is an ultraviolet correction that can be fully absorbed in the renormalization of $\xi$. Equation (B12) is the generalized Hooke's law. We emphasize once more that the denominator in the r.h.s. of Eq. (B12) contains only the external tension $\sigma$ and is not sensitive to the ultraviolet cutoff of the theory.

Since $a$ depends on $T$, it leads to a correction to $\alpha_T$. One can show that this correction is of the order of

$$
\delta\alpha_T \sim \frac{1}{\varkappa} \left( \frac{T}{g\varkappa} \right)^2,
$$

and is thus small in comparison with Eq. (38) under the condition $T < g\varkappa\sqrt{2/\eta}+\ln(1/g)$ (for graphene $T < 1000$ K). Therefore, one can safely discard this contribution for not too high temperatures, $T<T_{\text{uv}}$, with $T_{\text{uv}}$ given by Eq. (28), which is the temperature range of our interest in this paper. Neglecting $a$ in Eq. (B12), we get Eq. (20) of the main text.

Using the identity (A11), we can also cast the free energy of renormalized out-of-plane modes in Eq. (A10) in the form
$$
\begin{aligned}
\frac{F}{L^{2}} & =-\frac{\sigma^{2}}{2 B_{0}}+\sigma\left(\xi^{2}-1\right) \\
& +\frac{d_{\mathrm{c}}}{2} \sum_{\mathbf{q} \omega} \ln \left(\varkappa_{q} q^{4}+\sigma q^{2}+\rho \omega^{2}\right),
\end{aligned}
$$
which is Eq. (14) of the main text.

### Appendix C: Quantum renormalization group.

In this Appendix, we derive the quantum RG equations that are presented in Sec. III B of the main text. An alternative derivation is presented in Appendix D.

The quantum renormalization grouo operates in the region of momenta $q_{T}<q<q_{\mathrm{uv}}$. For momenta $q$ below $q_{\mathrm{uv}} \sim \sqrt{\mu / \varkappa}$, the flexural phonons are softer than the in-plane modes: $\omega_{q}<\omega_{q}^{\perp, \|}$. Here $\omega_{q}^{\perp}=\sqrt{\mu / \rho} q$ and $\omega_{q}^{\|}=\sqrt{(2 \mu+\lambda) / \rho} q$. Since in the considered region of momenta $\hbar \omega_{q} \gg T$, the flexural phonons are frozen out, so that the relevant RG equations are of zero-temperature character [62].

Here, we derive RG equations by using the energy functional Eq. (B1) where in-plane modes have been integrated out.

We have demonstrated above that the terms scaling as $q^{2}$ in the flexural phonons self-energy cancel (for zero external tension $\sigma=0$ ). After this cancellation is taken into account, all remaining effects related to retardation turn out to be small for $q<q_{\mathrm{uv}}$ and can be safely neglected. Hence, it is sufficient to keep the only component of the interaction tensor $R^{\alpha \beta \gamma \theta}$,
$$
R^{n n n n} \approx \frac{4 \mu(\mu+\lambda)}{2 \mu+\lambda}=Y. \quad \text { (C1) }
$$

To proceed, we use the approach analogous to one developed in Ref. 39 for high-temperature case. To find the renormalization of elastic coefficients within this approach, we have to calculate the polarization operator and the self-energy of $h$-fields. The bare Green function for $h$-field reads
$$
G_{\omega, \mathbf{k}}^{0}=\frac{1}{\varkappa k^{4}+\rho \omega^{2}}. \quad \text { (C2) }
$$

The polarization operator is given by the following equation
$$
\Pi_{\Omega, \mathbf{q}}=\frac{d_{\mathrm{c}}}{3} \int \frac{d \omega d^{2} \mathbf{k}}{(2 \pi)^{3}} k_{\perp}^{4} G_{\omega, \mathbf{k}}^{0} G_{\Omega-\omega, \mathbf{q}-\mathbf{k}}^{0}, \quad \text { (C3) }
$$
where $\mathbf{k}_{\perp}=[\mathbf{k} \times \mathbf{q}] / q$. Equation (C3) is a quantum counterpart of Eq. (37) of Ref. 39 derived there for the high-temperature classical regime. Performing the integration over $d \omega$, we get
$$
\Pi_{\Omega, \mathbf{q}}=\frac{d_{\mathrm{c}}}{6 \rho^{2}} \int \frac{d^{2} \mathbf{k}}{(2 \pi)^{2}} \frac{k_{\perp}^{4}\left(\omega_{\mathbf{k}-\mathbf{q}}^{0}+\omega_{\mathbf{k}}^{0}\right)}{\omega_{\mathbf{k}-\mathbf{q}}^{0} \omega_{\mathbf{k}}^{0}\left[\left(\omega_{\mathbf{k}-\mathbf{q}}^{0}+\omega_{\mathbf{k}}^{0}\right)^{2}+\Omega^{2}\right]} \quad (\mathrm{C} 4)
$$

Carrying out the remaining momentum integration we find, in the limit $\Omega=0$ and $q \rightarrow 0$,
$$
\Pi_{\mathbf{q}}=\Pi_{\Omega=0, \mathbf{q} \rightarrow 0} \approx \frac{d_{\mathrm{c}}}{64 \pi \rho^{1 / 2} \varkappa^{3 / 2}} \ln \left(\frac{q_{\mathrm{uv}}}{q}\right). \quad (\mathrm{C} 5)
$$

Next, we use Eqs. (33) and (34) of Ref. 39 to find screening of coupling constants $Y$ and $\mu$ :
$$
Y_{\mathbf{q}}=\frac{Y}{1+3 Y \Pi_{\mathbf{q}} / 2} \approx Y-3 Y^{2} \Pi_{\mathbf{q}} / 2, \quad \text { (C6) }
$$
$$
\mu_{\mathbf{q}}=\frac{\mu}{1+2 \mu \Pi_{\mathbf{q}}} \approx \mu-2 \mu^{2} \Pi_{\mathbf{q}}. \quad \text { (C7) }
$$

We notice that for $D=2$ the interaction between $h$-fields in Eq. (B1) depends on coupling $Y=$ $R^{n n n n}(\Omega \rightarrow 0)$ only, while $\mu$ drops out from Eq. (B1). Therefore, in order to obtain Eq. (C7), one should first consider $D \neq 2$, and then take the limit $D \rightarrow 2$.

Substituting Eq. (C5) into Eqs. (C6) and (C7), we find RG equations for in-plane elastic moduli:
$$
\frac{d Y}{d \Lambda}=-\frac{3 d_{\mathrm{c}} Y^{2}}{128 \pi \rho^{1 / 2} \varkappa^{3 / 2}}, \quad \text { (C8) }
$$
$$
\frac{d(\mu+\lambda)}{d \Lambda}=-\frac{d_{\mathrm{c}}(\mu+\lambda)^{2}}{16 \pi \rho^{1 / 2} \varkappa^{3 / 2}}, \quad \text { (C9) }
$$
where $\Lambda=\ln \left(q_{\mathrm{uv}} / q\right)$. These equations are equivalent to Eqs. (9) and (10) of Ref. 62. Renormalization of self-energy of $h$-field is given by an equation similar to Eq. (43) of Ref. 39:
$$
\Sigma_{\omega, \mathbf{k}}=\int \frac{d \Omega d^{2} \mathbf{q}}{(2 \pi)^{3}} k_{\perp}^{4} Y_{\mathbf{q}} G_{\omega-\Omega, \mathbf{k}-\mathbf{q}}^{0}. \quad \text { (C10) }
$$

Integrating over $d \Omega$, taking the limit $\omega \rightarrow 0$, and neglecting the dependence of $Y$ on $q$, we get
$$
\Sigma_{\omega \rightarrow 0, \mathbf{k}}=\frac{Y}{2 \sqrt{\varkappa \rho}} \int \frac{d^{2} \mathbf{q}}{(2 \pi)^{2}} \frac{k_{\perp}^{4}}{|\mathbf{k}-\mathbf{q}|^{2}}. \quad \text { (C11) }
$$

A straightforward analysis of this integral shows that $\Sigma$ scales as $k^{4} \ln k$, which implies a renormalization of $\varkappa$,
$$
\frac{d \varkappa}{d \Lambda}=\frac{3 Y}{32 \pi \sqrt{\varkappa \rho}}. \quad \text { (C12) }
$$

The Eq. (C12) coincides up to the sign with Eq. (11) of Ref. 62. From Eqs. (C6),(C7) and (C12), one easily obtains Eqs. (29) and (30) of the main text, with $g$ given by Eq. (12).

### Appendix D: Background-field renormalization

In this Appendix, we perform a derivation of quantum RG equations (Sec. III B of the main text) alternative to that presented in Appendix C. For this purpose, we evaluate the self-energies of the propagators of in- and out-of-plane phonons within one-loop approximation by using the approach of Ref. [62].

We start from the Lagrangian given by Eq. (A2). Using definition (15), we obtain formally exact relation between the external tension and the global stretching factor:

$$
\begin{aligned}
\frac{\sigma}{B}=\xi^{2}-1+\int_{\boldsymbol{q}, \omega} q^{2}\left(\frac{d_{\mathrm{c}}}{2} G_{\omega, q}+\frac{2 \mu+\lambda}{2 B} F_{\omega, q}^{(t)}+\frac{3 \mu+2 \lambda}{2 B} F_{\omega, q}^{(l)}\right)+\frac{1}{2 \xi B}\left(\mu \delta_{\gamma \beta} \delta_{\eta \alpha}+\lambda \delta_{\gamma \alpha} \delta_{\eta \beta}\right)\left\langle\partial_{\alpha} u_{\gamma}\left(\partial_{\eta} \boldsymbol{u} \partial_{\beta} \boldsymbol{u}+\partial_{\eta} \boldsymbol{h} \partial_{\beta} \boldsymbol{h}\right)\right\rangle .
\\
(\mathrm{D} 1)
\end{aligned}
$$

Here $F_{\omega, q}^{(t, l)}$ and $G_{\omega, q}$ are exact (with respect to the full Lagrangian (A2)) propagators of in- and out-of plane phonons, respectively:

$$
\left\langle u_{\alpha}(\boldsymbol{q}, i \omega) u_{\beta}(-\boldsymbol{q},-i \omega)\right\rangle=F_{\omega, q}^{(l)} \frac{q_{\alpha} q_{\beta}}{q^{2}}+F_{\omega, q}^{(t)}\left(\delta_{\alpha \beta}-\frac{q_{\alpha} q_{\beta}}{q^{2}}\right), \quad\left\langle\boldsymbol{h}(\boldsymbol{q}, i \omega) \boldsymbol{h}(-\boldsymbol{q},-i \omega)\right\rangle=d_{\mathrm{c}} G_{\omega, q}. \qquad(\mathrm{D}2)
$$

The exact propagators can be cast in the following form

$$
\begin{aligned}
& {\left[F_{\omega, q}^{(l)}\right]^{-1}=\rho \omega^{2}+\left[(2 \mu+\lambda) \xi^{2}+(\mu+\lambda)\left(\xi^{2}-1\right)\right] q^{2}+\varkappa q^{4}-\Sigma_{\omega, q}^{(l)},} \\
& {\left[F_{\omega, q}^{(t)}\right]^{-1}=\rho \omega^{2}+\left[\mu \xi^{2}+(\mu+\lambda)\left(\xi^{2}-1\right)\right] q^{2}+\varkappa q^{4}-\Sigma_{\omega, q}^{(t)},} \\
& {\left[G_{\omega, q}\right]^{-1}=\rho \omega^{2}+(\mu+\lambda)\left(\xi^{2}-1\right) q^{2}+\varkappa q^{4}-\Sigma_{\omega, q},}
\end{aligned} \qquad(\mathrm{D}3)
$$

where the self-energies $\Sigma_{\omega, q}^{(l, t)}$ and $\Sigma_{\omega, q}$ take into account interaction of in- and out-of-plane modes encoded in the Lagrangian (A5). The expressions (D3) in the absence of self-energies corresponds to the Gaussian part of the Lagrangian (A2). We emphasize the appearance of linear in $q^{2}$ term in the propagator of the out-of-plane phonon due to the linear in $K$ term in the Lagrangian (A2). As we will see below it will be compensated by the linear in $q^{2}$ term from the self-energy $\Sigma_{\omega, q}$. To avoid confusion, we note that the definition of the self-energies used in Appendixes A, B, and C is different compared to the definition which we use here. Of course, this does not change the physical propagators and, in particular, the cancelation of $\propto q^{2}$ contributions to the inverse propagator of out-of-plane phonons in the absence of the external stress $(\sigma=0)$. This statement can be written as $\sigma_{0}+\sigma_{1}=0$ (as was done in Appendixes A, B, C), or, equivalently, as $B\left(\xi^{2}-1\right)-\lim _{q \rightarrow 0} \Sigma_{\omega=0, q} / q^{2}=0$ within background-filed renormalization approach used in this Appendix.

In order to find the corresponding self-energies $\Sigma_{\omega, q}^{(l, t)}$ and $\Sigma_{\omega, q}$, we use the background field method. We split the fields $\boldsymbol{u}$ and $\boldsymbol{h}$ on slow $\boldsymbol{u}^{\prime}, \boldsymbol{h}^{\prime}$ and fast $\tilde{\boldsymbol{u}}, \tilde{\boldsymbol{h}}$ components in the momentum and frequency spaces, $\boldsymbol{u}=\boldsymbol{u}^{\prime}+\tilde{\boldsymbol{u}}$ and $\boldsymbol{h}=\boldsymbol{h}^{\prime}+\tilde{\boldsymbol{h}}$. We denote the corresponding momentum scale which separates fast and slow modes as $q_{\Lambda}^{\text {sf }}$. Then the interaction terms in the Lagrangian (A5) generates the following interaction terms between slow and fast components. For a sake of simplicity, we consider the case of $d_{\mathrm{c}}=1$ and restore arbitrary dimensionality in the final results for the

self-energies only. Then, limiting ourselves to the first and second orders in slow components, we find

$$
S_{\boldsymbol{u}^{\prime}, \tilde{h}}^{(1), 2}=\int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x}\left(\mu \xi \partial_{\alpha} u_{\beta}^{\prime}+\frac{\lambda \xi}{2} \delta_{\alpha \beta} \partial_{\eta} u_{\eta}^{\prime}\right) \partial_{\alpha} \tilde{h} \partial_{\beta} \tilde{h},
$$

$$
S_{h^{\prime}, \tilde{\boldsymbol{u}}, \tilde{h}}^{(1), 1,1}=\int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x}\left[\mu \xi\left(\partial_{\alpha} \tilde{u}_{\beta}+\partial_{\beta} \tilde{u}_{\alpha}\right)+\lambda \xi \delta_{\alpha \beta} \partial_{\eta} \tilde{u}_{\eta}\right] \partial_{\alpha} h^{\prime} \partial_{\beta} \tilde{h},
$$

$$
S_{\boldsymbol{u}^{\prime}, \tilde{\boldsymbol{u}}}^{(1), 2}=\int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x}\left[\left(\mu \xi \partial_{\alpha} u_{\beta}^{\prime}+\frac{\lambda \xi}{2} \delta_{\alpha \beta} \partial_{\eta} u_{\eta}^{\prime}\right) \partial_{\alpha} \tilde{u}_{\gamma} \partial_{\beta} \tilde{u}_{\gamma}+\left(\mu \xi\left(\partial_{\alpha} \tilde{u}_{\beta}+\partial_{\beta} \tilde{u}_{\alpha}\right)+\lambda \xi \delta_{\alpha \beta} \partial_{\eta} \tilde{u}_{\eta}\right)\right] \partial_{\alpha} u_{\gamma}^{\prime} \partial_{\beta} \tilde{u}_{\gamma},
$$

$$
S_{\boldsymbol{u}^{\prime}, \tilde{\boldsymbol{u}}}^{(2), 2}=\frac{1}{2}\left(\mu \delta_{\alpha \theta} \delta_{\beta \eta}+\frac{\lambda}{2} \delta_{\alpha \eta} \delta_{\beta \theta}\right) \int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x}\left(\partial_{\alpha} u_{\gamma}^{\prime} \partial_{\eta} u_{\gamma}^{\prime} \partial_{\theta} \tilde{u}_{\zeta} \partial_{\beta} \tilde{u}_{\zeta}+\partial_{\alpha} u_{\gamma}^{\prime} \partial_{\eta} \tilde{u}_{\gamma} \partial_{\theta} \tilde{u}_{\zeta} \partial_{\beta} u_{\zeta}^{\prime}+\partial_{\alpha} u_{\gamma}^{\prime} \partial_{\eta} \tilde{u}_{\gamma} \partial_{\theta} u_{\zeta}^{\prime} \partial_{\beta} \tilde{u}_{\zeta}\right),
$$

$$
S_{h^{\prime}, \tilde{h}}^{(2), 2}=\frac{1}{4}\left(\mu \delta_{\alpha \theta} \delta_{\beta \eta}+\frac{\lambda}{2} \delta_{\alpha \eta} \delta_{\beta \theta}\right) \int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x}\left(2 \partial_{\alpha} h^{\prime} \partial_{\eta} h^{\prime} \partial_{\theta} \tilde{h} \partial_{\beta} \tilde{h}+\left(\partial_{\alpha} h^{\prime} \partial_{\eta} \tilde{h}+\partial_{\alpha} \tilde{h} \partial_{\eta} h^{\prime}\right)\left(\partial_{\theta} \tilde{h} \partial_{\beta} h^{\prime}+\partial_{\theta} h^{\prime} \partial_{\beta} \tilde{h}\right)\right),
$$

$$
S_{\boldsymbol{u}^{\prime}, \tilde{h}}^{(2), 2}=\frac{1}{2}\left(\mu \delta_{\alpha \theta} \delta_{\beta \eta}+\frac{\lambda}{2} \delta_{\alpha \eta} \delta_{\beta \theta}\right) \int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x} \partial_{\alpha} u_{\gamma}^{\prime} \partial_{\eta} u_{\gamma}^{\prime} \partial_{\theta} \tilde{h} \partial_{\beta} \tilde{h},
$$

$$
S_{h^{\prime}, \tilde{\boldsymbol{u}}}^{(2), 2}=\frac{1}{2}\left(\mu \delta_{\alpha \theta} \delta_{\beta \eta}+\frac{\lambda}{2} \delta_{\alpha \eta} \delta_{\beta \theta}\right) \int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x} \partial_{\alpha} h^{\prime} \partial_{\eta} h^{\prime} \partial_{\theta} \tilde{u}_{\gamma} \partial_{\beta} \tilde{u}_{\gamma},
$$

$$
S_{h^{\prime}, \boldsymbol{u}^{\prime}, \tilde{h}, \tilde{\boldsymbol{u}}}^{(1,1), 1,1}=\frac{1}{2}\left(\mu \delta_{\alpha \theta} \delta_{\beta \eta}+\frac{\lambda}{2} \delta_{\alpha \eta} \delta_{\beta \theta}\right) \int_{0}^{\beta} d \tau \int d^{2} \boldsymbol{x}\left(\partial_{\alpha} u_{\gamma}^{\prime} \partial_{\eta} \tilde{u}_{\gamma}+\partial_{\alpha} \tilde{u}_{\gamma} \partial_{\eta} u_{\gamma}^{\prime}\right)\left(\partial_{\theta} \tilde{h} \partial_{\beta} h^{\prime}+\partial_{\theta} h^{\prime} \partial_{\beta} \tilde{h}\right). \tag{D4}
$$

After integration over fast variables we find the correction to the Gaussian part of the action for the in-plane ($\delta S_{u}^{(2)}$)
and out-of-plane ($\delta S_{h}^{(2)}$) slow modes:

$$
\delta S_{u}^{(2)}=\left\langle S_{\boldsymbol{u}^{\prime}, \tilde{h}}^{(2), 2}\right\rangle_{0}+\left\langle S_{\boldsymbol{u}^{\prime}, \tilde{\boldsymbol{u}}}^{(2), 2}\right\rangle_{0}-\frac{1}{2}\left\langle\left[S_{\boldsymbol{u}^{\prime}, \tilde{\boldsymbol{u}}}^{(1), 2}\right]^{2}\right\rangle_{0}-\frac{1}{2}\left\langle\left[S_{\boldsymbol{u}^{\prime}, \tilde{h}}^{(1), 2}\right]^{2}\right\rangle_{0}, \tag{D5}
$$

$$
\delta S_{h}^{(2)}=\left\langle S_{h^{\prime}, \tilde{h}}^{(2), 2}\right\rangle_{0}+\left\langle S_{h^{\prime}, \tilde{\boldsymbol{u}}}^{(2), 2}\right\rangle_{0}-\frac{1}{2}\left\langle\left[S_{h^{\prime}, \tilde{\boldsymbol{u}}, \tilde{h}}^{(1), 1,1}\right]^{2}\right\rangle_{0}. \tag{D6}
$$

Here the average $\langle\ldots\rangle_{0}$ is with respect to the Gaussian part of the full Lagrangian (A2). The self-energies can be
found from the following expressions

$$
\begin{aligned}
\delta S_{u}^{(2)}=-\frac{1}{2} \int_{\boldsymbol{q}, \omega} u_{\alpha}^{\prime}(\boldsymbol{q}, i \omega) u_{\beta}^{\prime}(-\boldsymbol{q},-i \omega)\left[\Sigma_{\omega, q}^{(l)} \frac{q_{\alpha} q_{\beta}}{q^{2}}+\Sigma_{\omega, q}^{(t)}\left(\delta_{\alpha \beta}-\frac{q_{\alpha} q_{\beta}}{q^{2}}\right)\right], \\
\delta S_{h}^{(2)}=-\frac{1}{2} \int_{\boldsymbol{q}, \omega} \boldsymbol{h}^{\prime}(\boldsymbol{q}, i \omega) \boldsymbol{h}^{\prime}(-\boldsymbol{k},-i \omega) \Sigma_{\omega, q}. \tag{D7}
\end{aligned}
$$

Evaluation of averages in $\delta S_{h}^{(2)}$ yields

$$
\begin{gathered}
\Sigma_{\omega, q}=-q^{2} \int_{\boldsymbol{k}, \Omega}\left[(2 \mu+\lambda) k^{2} G_{\Omega, k}^{(0)}+\frac{\lambda+\mu}{2} k^{2}\left(F_{\Omega, k}^{(l),(0)}+F_{\Omega, k}^{(t),(0)}\right)\right]-\int_{\boldsymbol{k}, \Omega} \xi^{2} G_{\omega+\Omega, \boldsymbol{q}+\boldsymbol{k}}^{(0)}\left\{[(2 \mu+\lambda)^{2} k^{2}(\boldsymbol{q} \cdot \boldsymbol{k})^{2}\right. \\
\left.+4 \mu(2 \mu+\lambda)(\boldsymbol{q} \cdot \boldsymbol{k})^{3}+2 \lambda(2 \mu+\lambda)(\boldsymbol{q} \cdot \boldsymbol{k}) q^{2} k^{2}+4 \mu^{2}(\boldsymbol{q} \cdot \boldsymbol{k})^{4} k^{-2}+4 \mu \lambda(\boldsymbol{q} \cdot \boldsymbol{k})^{2} q^{2}+\lambda^{2} k^{2} q^{4}\right] F_{\Omega, k}^{(l),(0)} \\
\left.+\mu^{2} \frac{[\boldsymbol{k} \times \boldsymbol{q}]^{2}}{k^{2}}\left(k^{2}+2(\boldsymbol{k} \cdot \boldsymbol{q})^{2}\right) F_{\Omega, k}^{(t),(0)}\right\}. \tag{D8}
\end{gathered}
$$

Here $F_{\Omega, k}^{(l, t),(0)}$ and $G_{\Omega, k}^{(0)}$ denote the propagators of in- and out-of-plane modes within the Gaussian approximation to
the full Lagrangian (A2). In Eq. (D8) the terms linear in the propagators corresponds to the contributions from
$\langle S_{h^{\prime}, \tilde{h}}^{(2), 2}\rangle_{0}$ and $\langle S_{h^{\prime}, \tilde{\boldsymbol{u}}}^{(2), 2}\rangle_{0}$ whereas the terms proportional to the product of propagators for the in-plane and out-of-plane
modes corresponds to the last contribution in the right hand side of Eq. (D6). We note that the first and last terms in
the right hand side of Eq. (D8) corresponds to the self-energy contribution due to effective interaction tensor $R^{\alpha \beta \gamma \theta}$.
The second term in the right hand side of Eq. (D8) appears due to the interaction of two flexural phonons with two

<table>
<caption>TABLE I: The linear in $q^2$ contributions to $\Sigma_{\omega=0,q}^{(l,t)}$ from different terms in Eq. (D5).</caption>
<tr>
<td>
</td>
<td>
$-\Sigma_{\omega=0,q}^{(t)}/q^2$
</td>
<td>
$-(\Sigma_{\omega=0,q}^{(l)}-\Sigma_{\omega=0,q}^{(t)})/q^2$
</td>
</tr>
<tr>
<td>
$\langle S_{u',\tilde{h}}^{(2),2}\rangle$
</td>
<td>
$\frac{\mu+\lambda}{2}\int_{k,\Omega}k^2G_{\Omega,k}^{(0)}$
</td>
<td>
$0$
</td>
</tr>
<tr>
<td>
$\langle S_{u',\tilde{u}}^{(2),2}\rangle$
</td>
<td>
$\int_{k,\Omega}k^2\left(\frac{9\mu+5\lambda}{8}F_{\Omega,k}^{(l),(0)}+\frac{11\mu+7\lambda}{8}F_{\Omega,k}^{(t),(0)}\right)$
</td>
<td>
$\frac{\mu+\lambda}{4}\int_{k,\Omega}k^2\left(F_{\Omega,k}^{(l),(0)}-F_{\Omega,k}^{(t),(0)}\right)$
</td>
</tr>
<tr>
<td>
$-\frac{1}{2}\left\langle\left[S_{u',\tilde{u}}^{(1),2}\right]^2\right\rangle$
</td>
<td>
$-\int_{k,\Omega}k^4\xi^2F_{\Omega,k}^{(l),(0)}\left(\frac{(3\mu+\lambda)^2}{4}F_{\Omega,k}^{(l),(0)}\right.$
</td>
<td>
$-\int_{k,\Omega}k^4\xi^2\left(\frac{(3\mu+2\lambda)^2}{2}\left[F_{\Omega,k}^{(l),(0)}\right]^2+\frac{(2\mu+\lambda)^2}{2}\left[F_{\Omega,k}^{(t),(0)}\right]^2\right.$
</td>
</tr>
<tr>
<td>
</td>
<td>
$\left.+\frac{11\mu^2+10\mu\lambda+3\lambda^2}{8}F_{\Omega,k}^{(t),(0)}\right)$
</td>
<td>
$\left.-\frac{(\mu+\lambda)^2}{4}F_{\Omega,k}^{(l),(0)}F_{\Omega,k}^{(t),(0)}\right)$
</td>
</tr>
<tr>
<td>
$-\frac{1}{2}\left\langle\left[S_{u',\tilde{h}}^{(1),2}\right]^2\right\rangle$
</td>
<td>
$-\frac{\mu^2\xi^2}{4}\int_{k,\Omega}k^4\left[G_{\Omega,k}^{(0)}\right]^2$
</td>
<td>
$-\frac{(\mu+\lambda)^2\xi^2}{4}\int_{k,\Omega}k^4\left[G_{\Omega,k}^{(0)}\right]^2$
</td>
</tr>
</table>

in-plane phonons. This vertex is not included in the interaction tensor $R^{\alpha\beta\gamma\theta}$. However, as we shall demonstrate below, this interaction is taken into account in the approach of Appendix A.

In the limit $q\rightarrow0$ and $\omega=0$ we find from Eq. (D8)

$$
\Sigma_{\omega=0,q}=-q^2\int_{k,\omega}\left[(2\mu+\lambda)k^2G_{\Omega,k}^{(0)}+\frac{\lambda+\mu}{2}k^2\left(F_{\Omega,k}^{(l),(0)}+F_{\Omega,k}^{(t),(0)}\right)\right]+\frac{q^2\xi^2}{2}\int_{k,\Omega}k^4G_{\Omega,k}^{(0)}\left[(2\mu+\lambda)^2F_{\Omega,k}^{(l),(0)}+\mu^2F_{\Omega,k}^{(t),(0)}\right].\ \text{(D9)}
$$

It is convenient to regroup various terms in Eq. (D9) in the following way:

$$
\begin{aligned}
\Sigma_{\omega=0,q}=-q^2\frac{\mu+\lambda}{2}\int_{k,\omega}k^2\left[G_{\Omega,k}^{(0)}+F_{\Omega,k}^{(l),(0)}+F_{\Omega,k}^{(t),(0)}\right]+\frac{q^2}{2}\int_{k,\Omega}k^2G_{\Omega,k}^{(0)}\left[(2\mu+\lambda)^2\xi^2k^2F_{\Omega,k}^{(l),(0)}+\mu^2\xi^2k^2F_{\Omega,k}^{(t),(0)}-(3\mu+\lambda)\right].
\\
\text{(D10)}
\end{aligned}
$$

As one can check, Eq. (D10) can be written as $\Sigma_{\omega=0,q}=\left[\sigma_0+\sigma_1-B(\xi^2-1)\right]q^2$. Using the precise form of the Gaussian propagators the result (D10) can be equivalently rewritten as follows

$$
\Sigma_{\omega=0,q}=-\frac{q^2}{2}\int_{k,\Omega}k^2\left\{d_c(\mu+\lambda)G_{\Omega,k}^{(0)}+(3\mu+2\lambda)F_{\Omega,k}^{(l),(0)}+(2\mu+\lambda)F_{\Omega,k}^{(t),(0)}\right\}.\ \text{(D11)}
$$

Here we restore arbitrary value of $d_c$. Comparing this result with the expression (D1) evaluated within the Gaussian theory, we conclude that within one-loop approximation the following identity holds

$$
\sigma=B(\xi^2-1)-\lim_{q\rightarrow0}\Sigma_{\omega=0,q}/q^2.\ \text{(D12)}
$$

Although at present we cannot prove this relation beyond the one-loop approximation, we believe that it should be satisfied in general (see discussion in the main text).

Expansion of the self-energy (D8) to the second in $q^2$ determines the one-loop renormalization of the bending rigidity:

$$
\varkappa'=\varkappa-\left.\frac{1}{4!}\frac{\partial^4}{\partial q^4}\Sigma_{\omega=0,q}\right|_{q=0}.\ \text{(D13)}
$$

As one can check by inspection of various terms in Eq. (D8), $\partial^4\Sigma_{\omega=0,q}/\partial q^4$, the logarithmically divergent contributions appear only for external momentum scale $q_T<q<q_{\rm uv}\sim\sqrt{\min\{\lambda,\mu\}/\varkappa}$. Simplifying Eq. (D8) in this regime, we obtain Eq. (C11) where the integration over momentum is limited to $k>q_{\Lambda}^{\rm sf}$ whereas $q\ll q_{\Lambda}^{\rm sf}$. Performing integration over momentum, we find the following RG equation:

$$
\frac{d\varkappa}{d\Lambda}=\frac{3d_c}{8\pi\rho^{1/2}\varkappa^{1/2}}\frac{\mu(\mu+\lambda)}{2\mu+\lambda},\ \text{(D14)}
$$

where $\Lambda=\ln q_{\rm uv}/q$ since the minimal value of $q_{\Lambda}^{\rm sf}$ is given by the external momentum $q$. This equation coincides with Eq. (30) in the main text.

19

The self-energies $\Sigma_{\omega,q}^{(t)}$ and $\Sigma_{\omega,q}^{(l)}$ determine renormalization of the Lame coefficients:
$$
\mu^{\prime}=\mu-\lim _{q \rightarrow 0}\left[\Sigma_{\omega=0, q}^{(t)}-\Sigma_{\omega=0, q}\right] /\left(\xi^{2} q^{2}\right), \quad (\lambda+\mu)^{\prime}=\lambda+\mu-\lim _{q \rightarrow 0}\left[\Sigma_{\omega=0, q}^{(l)}-\Sigma_{\omega=0, q}\right] /\left(\xi^{2} q^{2}\right). \tag{D15}
$$

We do not present the full expressions for the self-energies $\Sigma_{\omega,q}^{(l,t)}$ since they are too cumbersome. The linear in $k^2$ contributions to $\Sigma_{\omega=0,q}^{(l,t)}$ from different terms in Eq. (D5) are summarized in Table I. Using Eq. (D15) and Table I, we find
$$
\mu^{\prime}=\mu-\frac{1}{4} \int_{\boldsymbol{k}, \Omega} k^{4}\left\{d_{\mathrm{c}} \mu^{2}\left[G_{\Omega, k}^{(0)}\right]^{2}+(3 \mu+\lambda)^{2}\left[F_{\Omega, k}^{(l),(0)}\right]^{2}+2 \mu(\lambda+2 \mu) F_{\Omega, k}^{(l),(0)} F_{\Omega, k}^{(t),(0)}\right\}, \tag{D16}
$$

$$
(\lambda+\mu)^{\prime}=\lambda+\mu-\frac{1}{2} \int_{\boldsymbol{k}, \Omega} k^{4}\left\{d_{\mathrm{c}}(\mu+\lambda)^{2}\left[G_{\Omega, k}^{(0)}\right]^{2}+(3 \mu+2 \lambda)^{2}\left[F_{\Omega, k}^{(l),(0)}\right]^{2}+(2 \mu+\lambda)^{2}\left[F_{\Omega, k}^{(t),(0)}\right]^{2}\right\}. \tag{D17}
$$

Here we restore arbitrary value of $d_{\mathrm{c}}$.

Assuming that the infrared moment scale (which separates the slow and fast modes in the moment space) lies in the range $q_{T}<q<q_{\mathrm{uv}} \sim \sqrt{\min \{\lambda, \mu\}} / \varkappa$ we find that only the terms proportional to $d_{\mathrm{c}}$ provide logarithmically divergent contributions in Eqs. (D16) and (D17). Hence, we find
$$
\begin{aligned}
& \frac{d \mu}{d \tilde{\Lambda}}=-\frac{d_{\mathrm{c}}}{32 \pi \rho^{1 / 2} \varkappa^{3 / 2}} \mu^{2}, \\
& \frac{d \lambda}{d \tilde{\Lambda}}=-\frac{d_{\mathrm{c}}}{32 \pi \rho^{1 / 2} \varkappa^{3 / 2}}\left(\mu^{2}+4 \lambda \mu+2 \lambda^{2}\right).
\end{aligned} \tag{D18}
$$

From Eqs. (D14) and (D18) we obtain the renormalization group equations (29) and (30) of the main text. We see that $q_{\mathrm{uv}} \sim \sqrt{\min \{\lambda, \mu\}} / \varkappa$ is a natural ultraviolet cut-off for the renormalization group equations (29) and (30).

As we mentioned in the main text, the momentum $q_{\mathrm{uv}} \sim \sqrt{\min \{\lambda, \mu\}} / \varkappa$ is on the order of the inverse lattice constant $a^{-1}$ for graphene. However, one can imagine a generic membrane, where $q_{\mathrm{uv}} \ll 1 / a$. Let us briefly discuss what happens for $q_{\mathrm{uv}}<q<Q_{\mathrm{uv}} \sim 1 / a$. Within this interval, there is no difference in the spectrum of in-plane and out-of-plane phonons. Then all terms in the right hand side of Eqs. (D16) and (D17) provide logarithmic contributions. Then we find the following renor-malization group equations for the Lame coefficients in the range $q_{\mathrm{uv}}<q<Q_{\mathrm{uv}}$:
$$
\begin{aligned}
& \frac{d \mu}{d \tilde{\Lambda}}=-\frac{(\lambda+4 \mu)^{2}+\left(d_{\mathrm{c}}-3\right) \mu^{2}}{32 \pi \rho^{1 / 2} \varkappa^{3 / 2}}, \\
& \frac{d \lambda}{d \tilde{\Lambda}}=-\frac{2 d_{\mathrm{c}}(\lambda+\mu)^{2}+(3 \lambda+2 \mu)^{2}+\left(7-d_{\mathrm{c}}\right) \mu^{2}}{32 \pi \rho^{1 / 2} \varkappa^{3 / 2}}.
\end{aligned} \tag{D19}
$$
where $\tilde{\Lambda}=\ln Q_{\mathrm{uv}} / q$. We note that in the range $q_{\mathrm{uv}}<q<$ $Q_{\mathrm{uv}}$ there is no renormalization of the bending rigidity:
$$
\frac{d \varkappa}{d \tilde{\Lambda}}=0. \tag{D20}
$$

[1] R. Peierls, *Quantum Theory of Solids* (Oxford Univ. Press, Oxford, 2001).
[2] R. A. Cowley, Adv. Phys. **12**, 421 (1963).
[3] R. A. Cowley, Rep. Prog. Phys. **31**, 123 (1968).
[4] G. Leibfried and W. Ludwig, Solid State Physics **12**, 275 (1961).
[5] M. I. Katsnelson and A. V. Trefilov, *Crystal Lattice Dynamics and Thermodynamics* (Atomizdat, Moscow, 2002).
[6] M. I. Katsnelson, Lattice dynamics: anharmonic effects. In: *Encyclopedia of Condensed Matter Physics* (Elsevier, Amsterdam, 2005), ed. by G. F. Bassani, G. L. Liedl, and P. Wyder, p. 77.
[7] W. Miller, C. W. Smith, D. S. MacKenzie, K. E. Evans, Journal of Materials Science **44** 5441 (2009).
[8] Y. Maniwa, R. Fujiwara, H. Kira, H. Tou, H. Kataura, S. Suzuki, Y. Achiba, E. Nishibori, M. Takata, M. Sakata, A. Fujiwara, and H. Suematsu, Phys. Rev. B **64**, 241402(R) (2001)
[9] D. Tomanek, J. Phys.: Condens. Matter **17** R413 (2005).
[10] Y.-K. Kwon, S. Berber, and D. Tomanek, Phys. Rev. Lett. **92**, 015901 (2004).
[11] S. Brown, J. Cao, J. L. Musfeldt, N. Dragoe, F. Cim-poesu, S. Ito, H. Takagi, and R. J. Cross, Phys. Rev. B **73**, 125446 (2006).
[12] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva and A.A. Firsov, Science **306**, 666 (2004).
[13] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I.V. Grigorieva, S.V. Dubonos and A. A. Firsov, Nature **438**, 197 (2005).
[14] Y. Zhang, Y.-W. Tan, H. L. Stormer and P. Kim, Nature **438**, 201 (2005).
[15] A. K. Geim and K. S. Novoselov, Nature Materials **6**, 183

(2007).

[16] A. H. Castro Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, Rev. Mod. Phys. 81, 109 (2009).

[17] S. Das Sarma, S. Adam, E. H. Hwang, and E. Rossi, Rev. Mod. Phys. 83, 407 (2011).

[18] V. N. Kotov, B. Uchoa, V. M. Pereira, F. Guinea, and A. H. Castro Neto, Rev. Mod. Phys. 84, 1067 (2012).

[19] M. I. Katsnelson, *Graphene: Carbon in Two Dimensions* Hardcover, Cambridge University Press (2012).

[20] E. L. Wolf, *Graphene: A New Paradigm in Condensed Matter and Device Physics*, Oxford University Press (2014).

[21] L. E. F. Foa Torres, S. Roche, J.-C. Charlier, *Introduction to Graphene-Based Nanomaterials From Electronic Structure to Quantum Transport*, Cambridge University Press (2014).

[22] M. K. Blees, A.W. Barnard, P. A. Rose, S. P. Roberts, K. L. McGill, P. Y. Huang, A. R. Ruyack, J. W. Kevek, B. Kobrin, D. A. Muller, and P. L. McEuen, *Nature* 524, 204 (2015).

[23] G. Lopez-Polin, C. Gomez-Navarro, V. Parente, F. Guinea, M. I. Katsnelson, F. Perez-Murano, and J. Gomez-Herrero, *Nature Physics* 11, 26 (2015); G. Lopez- Polin, M. Jaafar, F. Guinea, R. Roldan, C. Gomez- Navarro, and J. Gomez-Herrero, arXiv:1504.05521.

[24] R. J. Nicholl, H. J. Conley, N. V. Lavrik, I. Vlas- siouk, Y. S. Puzyrev, V. P. Sreenivas, S. T. Pantelides, and K. I. Bolotin, *Nature Communications* 6:8789 doi: 10.1038/ncomms9789 (2015).

[25] I. M. Lifshitz, *Sov. Phys. JETP* 52, 472 (1952).

[26] N. Mounet and N. Marzari, *Phys. Rev. B* 71, 205214 (2005).

[27] P. L. de Andres, F. Guinea, and M. I. Katsnelson, *Phys. Rev. B* 86, 144103 (2012).

[28] M. I. Katsnelson and A. Fasolino, *Acc. Chem. Res.* 46, 97 (2013).

[29] E. G. Steward, B. P. Cook, and E. A. Kellert, *Nature* 1960 187, 1015.

[30] K. V. Zakharchenko, M. I. Katsnelson, and A. Fasolino, *Phys. Rev. Lett.* 102, 046808 (2009).

[31] A. L. C. da Silva, Ladir Cândido, J. N. Teixeira Ra- belo, G.-Q. Hai, and F. M. Peeters, *Europhys. Lett.*, 107, 56004 (2014).

[32] K. H. Michel, S. Costamagna, and F. M. Peeters, *Phys. Rev. B* 91, 134302 (2015).

[33] W. Bao, F. Miao, Z. Chen, H. Zhang, W. Jang, C. Dames, and C. N. Lau, *Nature Nanotech.* 2009 4, 562.

[34] D. Yoon, Y.-W. Son, and H. Cheong, *Nano Lett.* 2011 11, 3227.

[35] F. Boerrnert, A. Barreiro, D. Wolf, M. I. Katsnelson, B. Buechner, L. M. K. Vandersypen, and M. H. Ruemmeli, *Nano Lett.* 12, 4455 (2012).

[36] L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part I* (Pergamon Press, Oxford, 1980).

[37] B. Amorim, R. Roldan, E. Cappelluti, A. Fasolino, F. Guinea, and M. I. Katsnelson, *Phys. Rev. B* 89, 224307 (2014).

[38] D. Nelson, T. Piran, and S. Weinberg (Eds.) *Statistical Mechanics of Membranes and Surfaces* (World Scientific, Singapore, 1989).

[39] I. V. Gornyi, V. Yu. Kachorovskii, and A. D. Mirlin, *Phys. Rev. B* 92, 155428 (2015).

[40] D. R. Nelson and L. Peliti, *J. Phys. (Paris)* 48, 1085 (1987).

[41] Y. Kantor and D. R. Nelson, *Phys. Rev. Lett.* 58, 2774 (1987); *Phys. Rev. A* 36, 4020 (1987);

[42] M. Paczuski, M. Kardar, and D. R. Nelson, *Phys. Rev. Lett.* 60, 2638 (1988).

[43] F. David and E. Guitter, *Europhys. Lett.* 5, 709 (1988).

[44] E. Guitter, F. David, S. Leibler, and L. Peliti, *Phys. Rev. Lett.* 61, 2949 (1988).

[45] J. A. Aronovitz and T. C. Lubensky, *Phys. Rev. Lett.* 60, 2634 (1988).

[46] E. Guitter, F. David, S. Leibler, and L. Peliti, *J.Phys. France* 50 1787 (1989).

[47] J. Aronovitz, L. Golubović, and T. C. Lubensky, *J. Phys. France* 50 609 (1989).

[48] M. Paczuski and M. Kardar, *Phys. Rev. A* 39, 6086 (1989).

[49] L. Radzihovsky and D. R. Nelson, *Phys. Rev. A* 44, 3525 (1991).

[50] D. R. Nelson and L. Radzihovsky, *Europhys. Lett.* 16, 79 (1991).

[51] G. Gompper and D. M. Kroll, *Europhys. Lett.* 15, 783 (1991).

[52] L. Radzihovsky and P. Le Doussal, *J.Phys. I France* 2 599 (1992).

[53] P. Le Doussal and L. Radzihovsky, *Phys. Rev. Lett.* 69, 1209 (1992).

[54] D. C. Morse, T. C. Lubensky, and G. S. Grest, *Phys. Rev. A* 45, R2151 (1992).

[55] P. Le Doussal and L. Radzihovsky, *Phys. Rev. B* 48, 3548 (1993).

[56] M. J. Bowick, S. M. Catterall, M. Falcioni, G. Thorleif- sson, and K. N. Anagnostopoulos, *J. Phys. I France* 6, 1321 (1996).

[57] I.V. Gornyi, V. Yu. Kachorovskii, and A. D. Mirlin, *2D Materials* 4, 011003 (2016).

[58] J.-P. Kownacki, and D. Mouhanna, *Phys. Rev. E* 79, 040101(R) (2009).

[59] D. Gazit, *Phys. Rev. E* 80, 041117 (2009).

[60] F. L. Braghin and N. Hasselmann, *Phys. Rev. B* 82, 035407 (2010).

[61] V. V. Lebedev and E. I. Kats, *Phys. Rev. B* 85, 045416 (2012).

[62] E. I. Kats and V. V. Lebedev, *Phys. Rev. B* 89, 125433 (2014).

[63] E. I. Kats and V. V. Lebedev, *Phys. Rev. B* 90, 176301 (2014).

[64] E. I. Kats and V. V. Lebedev, *Phys. Rev. B* 94, 079904(E) (2016).

[65] J. H. Los, M. I. Katsnelson, O. V. Yazyev, K. V. Za- kharchenko, and A. Fasolino, *Phys. Rev. B* 80, 121405 (2009).

[66] E. I. Kats and V. V. Lebedev, *Phys. Rev. E* 91, 032415 (2015).

[67] B. Amorim, R. Roldan, E. Cappelluti, F. Guinea, A. Fasolino, and M. I. Katsnelson, *Phys. Rev. B* 90, 176302 (2014)

[68] O. Coquand, D. Mouhanna, unpublished, cond-mat arxiv 1607.03335

[69] P. Souvatzis, S. Arapan, O. Eriksson, and M. I. Katsnel- son, *Europhys. Lett.* 96, 66006 (2011).

[70] Analyzing integral Eq. (46), one can find that its low $\sigma$ asymptotics has form of the upper line in Eq. (48) pro-

vided that
$$
C^{2(1-\eta)}=\left[\frac{A(\eta)}{2-\eta}\right]^{2-\eta}\left(\frac{8 B}{3 Y}\right)^{\eta},
$$
where
$$
A(\eta)=\int_{0}^{\infty} \frac{\eta d y}{y^{1-\eta}\left(1+y^{2-\eta}\right)}=\frac{2-\eta}{2} \Gamma\left(\frac{4-\eta}{2-\eta}\right) \Gamma\left(\frac{2-2 \eta}{2-\eta}\right).
$$

We notice, that for invariant subspace of elastic moduli, $Y=8 B / 3$, the coefficient $C$ is temperature-independent. For $d_{c} \rightarrow \infty(\eta \rightarrow 0)$, we get $C=1 / 2$.

[71] J. H. Los, A. Fasolino, and M. I. Katsnelson, Phys. Rev. Lett. 116, 015901 (2016).

[72] A. K. Geim and I. V. Grigorieva, Nature 499, 419 (2013).

[73] K. S. Novoselov, A. Mishchenko, A. Carvalho, and A. H. Castro Neto, Science 353, 461 (2016).

[74] C. R.Woods, L. Britnell, A. Eckmann, R. S. Ma, J. C. Lu, H. M. Guo, X. Lin, G. L. Yu, Y. Cao, R. V. Gor- bachev, A. V. Kretinin, J. Park, L. A. Ponomarenko, M. I. Katsnelson, Yu. N. Gornostyrev, K. Watanabe, T. Taniguchi, C. Casiraghi, H.-J. Gao, A. K. Geim, and K. S. Novoselov, Nature Phys. 10, 451 (2014).

[75] M. M. van Wijk, A. Schuring, M. I. Katsnelson, and A. Fasolino, Phys. Rev. Lett. 113, 135504 (2014).

[76] C. R. Woods, F. Withers, M. J. Zhu, Y. Cao, G.Yu, A. Kozikov, M. Ben Shalom, S. V. Morozov, M. M. van Wijk, A. Fasolino, M. I. Katsnelson, K.Watanabe, T.Taniguchi, A. K. Geim, A. Mishchenko, and K. S. Novoselov, Nature Communications 7, 10800 (2016)

[77] E. Khestanova, F. Guinea, L. Fumagalli, A. K. Geim, and I. V. Grigorieva, Nature Commun. 7, 12587 (2016).