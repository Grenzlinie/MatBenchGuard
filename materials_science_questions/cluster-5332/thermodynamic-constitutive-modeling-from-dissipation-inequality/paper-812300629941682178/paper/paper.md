Acta Mechanica 42, 263-275 (1982)
ACTA MECHANICA
© by Springer-Verlag 1982

# On the Concept of Stress-Strain Relations in Plasticity

By
Th. Lehmann, Bochum, Federal Republic of Germany

With 6 Figures

(Received October 2, 1980)

## Summary
In some cases the plastic stress-strain relations based on the so-called normality rule lead to an unsatisfactory agreement with experimental results. This is particularly true in bifurcation problems or more generally in problems with non-proportional loading paths. Within the frame of a phenomenological theory of non-isothermic large deformations it is shown how plastic stress-strain relations can be modified in order to improve the agreement with the real material behaviour.

## 1. Introduction
In the early history of the theory of plasticity two different concepts of stress-strain relations have been developed:

(A) the flow theory following the line St. Venant - Levy - Mises - Prandtl - Reuß [1] to [5] which relates the increments of the plastic strain to the actual stresses, and

(B) the deformation theory based on a paper by Hencky [6] which relates the plastic strains themselves to the actual stresses.

Although the deformation theory is physically unsatisfactory this concept leads in some cases to a better agreement with experimental results. This has been shown the first time by Hohenemser and Prager in their classical experiments [7], [8]. Further it was recognized that in bifurcation problems sometimes the classical flow theory fails ([9] to [12]). In the investigation of certain second order effects (e.g. the Poynting effect) the classical flow theory also proves to be unsatisfactory [13].

In order to adjust the flow theory to the experimental results in the mentioned cases different generalizations of the stress-strain relations are proposed. Some of them are based on the assumed existence of vertices in the yield condition due to previous loading history ([10] to [12]). Others (see e.g. [14]) introduce empirically motivated modifications of the stress-strain relations in order to describe the transient process after an abrupt change of the loading path.

In the following it shall be discussed how within the frame of a phenomenological theory a more general concept of plastic stress-strain relations can be

0001-5970/82/0042/0263/$02.60

introduced. This generalization avoids some difficulties which arise from the existence of vertices in the yield condition. It leads, however, to similar results like these theories in some respect. This general concept allows for large, non-isothermic deformations. It can also be extended to viscoplastic materials.

## 2. Thermodynamical Frame

The rate of specific mechanical work is given by

$$
\dot{w}=\frac{1}{\varrho} \sigma_{k}^{i} d_{i}^{k}=\frac{1}{\dot{\varrho}} s_{k}^{i} d_{i}^{k}
\tag{1}
$$

with $\sigma_{k}^{i}=$ Cauchy stress tensor, $\varrho=$ mass density, $s_{k}^{i}=$ weighted Cauchy stress tensor, $d_{k}^{i}=$ strain rate.

All quantities are related to the actual configuration of a body-fixed, co-moving coordinate system.

Without going into details (see [15], [16]) the work rate can be decomposed into its elastic and its inelastic part according to

$$
\dot{w}=\underset{(e)}{\dot{w}}+\underset{(i)}{\dot{w}}=\frac{1}{\dot{\varrho}} \underset{(e)}{s_{k}^{i} d_{i}^{k}}+\frac{1}{\dot{\varrho}} \underset{(i)}{s_{k}^{i} d_{i}^{k}}.
\tag{2}
$$

If the elastic behaviour is isotropic the elastic part of work rate may also written

$$
\underset{(e)}{\dot{w}}=\left.\underset{(e)}{s_{k}^{i} \varepsilon_{i}^{k}}\right|_{0},
\tag{3}
$$

where $\varepsilon_{i}^{k}$ represents the Hencky (logarithmic) strain tensor and $|_{0}$ denotes the covariant (Zaremba-Jaumann) derivative with respect to time [15], [16]. This may be presupposed in the following. The inelastic work rate has to be split once more into one part $\underset{(d)}{w}$ which is dissipated immediately and into another part $\underset{(h)}{w}$ which is correlated to changes of the internal structure of the material (hardening, solid phase transformations etc.). Thus we obtain

$$
\underset{(i)}{\dot{w}}=\underset{(h)}{\dot{w}}+\underset{(d)}{\dot{w}}.
\tag{4}
$$

The first law of thermodynamics states

$$
\dot{u}=\dot{w}-\left.\frac{1}{\varrho}\left(q^{i}+h^{i}\right)\right|_{i}+r.
\tag{5}
$$

In this formula mean:
$u$ specific internal energy,
$q^{i}$ heat flux,
$h^{i}$ other energy fluxes, $\Bigg\} q^{i}+h^{i}$: flux of internal energy
$r$ specific energy supply by sources.

In solid bodies energy fluxes apart from heat may be small under usual conditions. In a general theory, however, they cannot be neglected.

Within the frame of classical thermodynamics each material element can be considered as a local thermodynamical system whose state is uniquely determined

by the actual values of a complete set of (external and internal) variables. There-
fore we may write:
$$
u=u(\underset{(e)}{\varepsilon_{k}^{i}}, s, b, \beta_{k}^{i}).\qquad(6)
$$

In this relation mean:
$s$ specific entropy,
$b,\beta_{k}^{i}$ a set of scalar valued and tensor valued internal variables.

By a double Legendre transformation we introduce a particular form of the
specific free enthalpy (Gibbs function)
$$
\psi=u-\frac{1}{\stackrel{\circ}{\varrho}} \underset{(e)}{s_{k}^{i} \varepsilon_{i}^{k}}-T s=\psi(s_{k}^{i}, T, b, \beta_{k}^{i}).\qquad(7)
$$

Differentiation of these expressions with respect to time yields
$$
\begin{aligned}
\dot{\psi} & =\dot{u}-\frac{1}{\stackrel{\circ}{\varrho}} \underset{(e)}{s_{k}^{i} \varepsilon_{i}^{k}|_{0}}-\frac{1}{\stackrel{\circ}{\varrho}} s_{k|0}^{i} \varepsilon_{i}^{k}-T \dot{s}-\dot{T} s \\
& =\underset{(h)}{\dot{w}}+\underset{(d)}{\dot{w}}-\frac{1}{\varrho}\left(q^{i}+h^{i}\right)|_{i}+r-\frac{1}{\stackrel{\circ}{\varrho}} s_{k|0}^{i} \varepsilon_{i}^{k}-T \dot{s}-\dot{T} s,
\end{aligned}\qquad(8a)
$$
or
$$
\dot{\psi}=\frac{\partial \psi}{\partial s_{k}^{i}} s_{k|0}^{i}+\frac{\partial \psi}{\partial T} \dot{T}+\frac{\partial \psi}{\partial b} \dot{b}+\frac{\partial \psi}{\partial \beta_{k}^{i}} \beta_{k|0}^{i},\qquad(8b)
$$
respectively. From the properties of the Legendre transformations we conclude
immediately
$$
\text { thermic state equation: } \quad \underset{(e)}{\varepsilon_{k}^{i}}=-\stackrel{\circ}{\varrho} \frac{\partial \psi}{\partial s_{k}^{i}}=\underset{(e)}{\varepsilon_{k}^{i}(s_{k}^{i}}, T, b, \beta_{k}^{i})\qquad(9a)
$$

$$
\text { caloric state equation: } \quad s=-\stackrel{\circ}{\varrho} \frac{\partial \psi}{\partial T}=s(s_{k}^{i}, T, b, \beta_{k}^{i}).\qquad(9b)
$$

Substituting these relations into Eq. (8a) we obtain
$$
T \dot{s}=\underset{(h)}{\dot{w}}+\underset{(d)}{\dot{w}}-\frac{1}{\varrho}\left(q^{i}+h^{i}\right)|_{i}+r-\frac{\partial \psi}{\partial b} \dot{b}-\frac{\partial \psi}{\partial \beta_{k}^{i}} \beta_{k|0}^{i}.\qquad(10a)
$$

On the other hand we derive from Eq. (9b)
$$
T \dot{s}=-T\left\{\frac{\partial^{2} \psi}{\partial T^{2}} \dot{T}+\frac{\partial^{2} \psi}{\partial s_{k}^{i} \partial T} s_{k|0}^{i}+\frac{\partial^{2} \psi}{\partial b \partial T} \dot{b}+\frac{\partial^{2} \psi}{\partial \beta_{k}^{i} \partial T} \beta_{k|0}^{i}\right\}.\qquad(10b)
$$

Equating (10a) and (10b) leads to the balance equation for the specific free
enthalpy
$$
\begin{gathered}
\underset{(h)}{\dot{w}}+\underset{(d)}{\dot{w}}-\frac{1}{\varrho}\left(q^{i}+h^{i}\right)|_{i}+r=-T\left\{\frac{\partial^{2} \psi}{\partial T^{2}} \dot{T}+\frac{\partial^{2} \psi}{\partial s_{k}^{i} \partial T} s_{k|0}^{i}\right\} \\
+\frac{\partial}{\partial b}\left\{\psi-T \frac{\partial \psi}{\partial T}\right\} \dot{b}+\frac{\partial}{\partial \beta_{k}^{i}}\left\{\psi-T \frac{\partial \psi}{\partial T}\right\} \beta_{k|0}^{i}.
\end{gathered}\qquad(11)
$$

The reversible part of entropy evolution is given by
$$
\underset{(\text { rev })}{T \dot{s}}=\underset{(h)}{\dot{w}}-\left.\frac{T}{\varrho}\left(\frac{q^{i}}{T}\right)\right|_{i}-\frac{1}{\varrho} h^{i}|_{i}+r-\frac{\partial \psi}{\partial b} \dot{b}-\frac{\partial \psi}{\partial \beta_{k}^{i}} \beta_{k|0}^{i}-T \dot{\eta}.\qquad(12)
$$

266
Th. Lehmann:

In this relation $\dot{\eta}$ represents the entropy production apart from dissipated mechanical work and irreversible heat flux. It is due to irreversible internal processes and to the immediate dissipation of energy which is supplied by sources $r$ and by the divergence of the fluxes $h^{i}$. From Eq. (12) we obtain for the total entropy production which is non-negative according to the second law of thermodynamics

$$
\begin{aligned}
0 \leqq \underset{\text { (irr) }}{T \dot{s}} & =\underset{\text { (rev) }}{T \dot{s}}-\underset{\text { (d) }}{T \dot{s}}=\dot{w}-\frac{1}{\varrho T} q^{i} T|_{i}+T \dot{\eta} \\
& =-\dot{w}+\left.\frac{T}{\varrho}\left(\frac{\varrho^{i}}{T}\right)\right|_{i}+\frac{1}{\varrho} h^{i}|_{i}-r+T \dot{\eta} \\
& +\frac{\partial}{\partial b}\left\{\psi-T \frac{\partial \psi}{\partial T}\right\} \dot{b}+\frac{\partial}{\partial \beta_{k}^{i}}\left\{\psi-T \frac{\partial \psi}{\partial T}\right\}\left.\beta_{k}^{i}\right|_{0} \\
& -T\left\{\frac{\partial^{2} \psi}{\partial T^{2}} \dot{T}+\frac{\partial^{2} \psi}{\partial s_{k}^{i} \partial T}\left.s_{k}^{i}\right|_{0}\right\}.
\end{aligned}
$$

The Eqs. (11) and (13) represent the general thermodynamical frame for the formulation of the constitutive law of the respective material. This constitutive law comprehends

(a) the state function for the specific free enthalpy,
(b) the evolution law for the inelastic strain,
(c) the evolution laws for the internal variables,
(d) the flux of internal energy (heat and others),
(e) the laws of entropy production.

Due to the existence of energy fluxes the constitutive law forms a system of partial differential equations in space and time completed by some side conditions. Only if all energy fluxes are vanishing the constitutive law is reducible to a system of first order ordinary differential equations in time with some side conditions. We obtain, however, a simplified constitutive law, too, if we can disregard at least the energy fluxes apart from heat. In such cases the evolution laws for the strain and the internal variables as well as the entropy production terms $\dot{w}$ and $\dot{\eta}$ degenerate into first order ordinary differential equations in time. Adopting this simplification we obtain the following scheme for the constitutive law

specific free enthalpy:
$$\psi=\psi\left(s_{k}^{i}, T, b, \beta_{k}^{i}\right) \quad(14 \mathrm{a})$$

evolution laws (with side conditions)

total strain:
$$d_{k}^{i}=\dot{d}_{k}^{i}\left(s_{k}^{i}, T, b, \beta_{k}^{i} ;\left.s_{k}^{i}\right|_{0}, \dot{T}\right)\quad(14b)$$

internal variables:
$$\dot{b}=\dot{b}\left(s_{k}^{i}, T, b, \beta_{k}^{i} ;\left.s_{k}^{i}\right|_{0}, \dot{T}\right)\quad(14c)$$

$$\left.\beta_{k}^{i}\right|_{0}=\left.\beta_{k}^{i}\right|_{0}\left(s_{k}^{i}, T, b, \beta_{k}^{i} ;\left.s_{k}^{i}\right|_{0}, \dot{T}\right)\quad(14d)$$

flux law of heat:
$$q^{i}=q^{i}\left(s_{k}^{i}, T, b, \beta_{k}^{i} ;\left.s_{k}^{i}\right|_{r},\left.T\right|_{i}\right)\quad(14e)$$

laws of entropy production: $\underset{(d)}{\dot{w}}=\underset{(d)}{\dot{w}}(s_{k}^{i}, T, b, \beta_{k}^{i} ;s_{k}^{i}|_{0},\dot{T})$
$$\dot{w}=\dot{w}\left(s_{k}^{i}, T, b, \beta_{k}^{i} ;\left.s_{k}^{i}\right|_{0}, \dot{T}\right)\quad(14f)$$

$$T \dot{\eta}=T \dot{\eta}\left(s_{k}^{i}, T, b, \beta_{k}^{i} ;\left.s_{k}^{i}\right|_{0}, \dot{T}\right).\quad(14g)$$

A more detailed discussion of the structure of the constitutive law taking into account internal processes like recrystallization, solid phase transformations etc. is given in [16], [17]. We shall focus our considerations in the following on the evolution law for strain.

### 3. A Generalized Concept for Evolution Law of Strain

The evolution law for the elastic strain can be derived from the thermic state equation (9a). It leads to an expression of the form

$$
\underset{(e)}{d_{k}^{i}}=\underset{(e)}{d_{k}^{i}}\{s_{k}^{i}, T, b, \beta_{k}^{i} ;\left.s_{k}^{i}\right|_{0}, \dot{T}\}. \tag{15}
$$

In most cases we can approximate this by a hypo-elastic law [18]

$$
\underset{(e)}{d_{k}^{i}}=\frac{1}{2 G}\left.t_{k}^{i}\right|_{0}+\left\{\frac{1}{9 K} \dot{s}_{r}^{r}+\alpha \dot{T}\right\} \delta_{k}^{i} \tag{16}
$$

with $G=$ shear modulus, $K=$ bulk modulus, $\alpha=$ coefficient of thermal expansion, $t_{k}^{i}=$ (weighted) stress deviator.

Concerning the inelastic deformations we restrict ourselves in the first step to a plastic behaviour. As usual we assume that plastic deformations only occur if the state variables fulfill a plasticity condition consisting of a yield condition

$$
F(s_{k}^{i}, T, b, \beta_{k}^{i})=0 \tag{17}
$$

and a corresponding loading condition

$$
\hat{H}(s_{k}^{i}, T, b, \beta_{k}^{i}, ;\left.s_{k}^{i}\right|_{0}, \dot{T})>0. \tag{18}
$$

This loading condition follows from the requirement $\dot{F}=0$ during plastic deformations by substituting $\dot{b}$ and $\dot{\beta}_{k|0}^{i}$ in this equation by means of the evolution laws for $b$ and $\beta_{k}^{i}$ [16], [17].

Concerning the evolution law for the plastic strain it is usually assumed that the plastic strain rate obeys the so-called normality rule

$$
\underset{(i)}{d_{k}^{i}}=\dot{\lambda} \frac{\partial F}{\partial s_{i}^{k}}. \tag{19}
$$

This assumption is often accounted for the postulate of Ilyushin [19] or the postulate of Drucker [20]. But these postulates do not offer a general base for the formulation of the evolution law for the plastic strain. They contain restrictions going beyond those given by the thermodynamical frame. Particularly in general non-isothermic processes they loose their capability.

A possible and with the thermodynamical frame compatible generalization can be based on the general approach [21], [22]

$$
\underset{(i)}{d_{k}^{i}}=\dot{\lambda} \frac{\partial F}{\partial s_{i}^{k}}+\varkappa_{k s}^{i r}\left.t_{r}^{s}\right|_{0}. \tag{20}
$$

We are led to expressions of the same formal kind in the usual formulation of the theory with associated flow rule (19) at singular points (verticer, corners) on the yield surface, since the normal to the yield surface becomes ambiguous. This fact is be used by some authors (e.g. [9] to [11]) in connection with bifurcation problems in order to avoid some discrepancies which occure, when the usual theory is applied in combination with smooth yield surfaces.

The approach (20), however, is not restricted to singular points on the yield surface, since it is based on another physical interpretation. Plastic deformations represent a sequence of thermodynamical equilibrium states. The driving forces for the generation and migration of lattice defects are in equilibrium with the resistances due to obstacles (grain boundaries etc.). At constant temperature and constant values of the internal variables the stress increments represent the disturbances of the actual equilibrium state. At the same time stress increments in the sense of loading lead to an increasing internal energy. This latter fact may activate now slip processes which are described by the first therm in (20). We can expect, however, that the stress increments release also one component of the material response, i.e. the plastic strain increments, into the direction of the disturbance of the equilibrium, i.e. the stress increments. This effect corresponds to the second term in (20).

The distribution of the material response to these both different mechanisms is governed by the constitutive law. There exists a wide variety of possibilities within the restrictions given by the thermodynamical frame. Therefore the approach (20) offers a large freedom in adjusting the plastic stress-strain relations to the real material behaviour. The tensor $\varkappa_{k s}^{i r}$ may depend on the whole set of state variables and on the value of a normalized (endochronic) loading condition $\hat{H}$ which represents the deviation between actual loading and proportional loading increments. In this respect the considerations of Christoffersen and Hutchinson [11] can be incorporated immediately into the proposed constitutive law with the only change that it becomes unnecessary to presuppose the existence of corners in the yield condition.

Particularly for isotropic materials the approach (20) may be simplified to

$$
\underset{(i)}{d_{k}^{i}}=\dot{\lambda} \frac{\partial F}{\partial s_{i}^{k}}+\varkappa t_{k \mid 0}^{i}, \tag{21}
$$

where $\varkappa$ may still depend on the whole set of state variables and on $\hat{H}$. From this formula for the plastic strain increments and from the simplified formula (16) for the elastic strain increment we obtain the evolution law for the total strain in the form

$$
\begin{aligned}
d_{k}^{i} & =\underset{(e)}{d_{k}^{i}}+\underset{(i)}{d_{k}^{i}}=\frac{1}{2 G} t_{k \mid 0}^{i}+\left\{\frac{1}{9 K} \dot{s}_{r}^{r}+\alpha \dot{T}\right\} \delta_{k}^{i}+\dot{\lambda} \frac{\partial F}{\partial s_{i}^{k}}+\varkappa t_{k \mid 0}^{i} \\
& =\left\{\frac{1}{2 G}+\varkappa\right\} t_{k \mid 0}^{i}+\left\{\frac{1}{9 K} \dot{s}_{r}^{r}+\alpha \dot{T}\right\} \delta_{k}^{i}+\dot{\lambda} \frac{\partial F}{\partial s_{i}^{k}}.
\end{aligned} \tag{22}
$$

The addition of the second term in (20) or (21), respectively, leads also obviously among others to the effect that the elastic shear modulus appears smaller during

plastic deformations. This effect corresponds to some results obtained by Sewell's approach [12] for the flow rule at a yield vertex.

In proportional loading the influence of the second term in (20) or (21), respectively, vanishes. This term, however, becomes important in non-proportional loading paths particularly after abrupt changes of the direction of the loading path as may happen in bifurcation problems inside certain material elements.

In order to ensure the continuity of the stress-strain relations $\varkappa_{k r}^{i r}$ (or $\varkappa$) should be a continuous function of the direction of the stress increments (i.e. of $\hat{H}$) and it should be zero for neutral loading $(\hat{H}=0)$. Otherwise some difficulties may arise in the investigation of the uniqueness of the solution. In practical problems, however, it may be allowed to choose $\varkappa$ as independent of $\hat{H}$.

![](./images/812300629941682178_1.jpg)

Fig. 1. Unloading and reloading

The introduction of the second term in (20) or (21), respectively, opens further possibilities. We can define different yield conditions for the first and the second term. This enables us to describe certain phenomena which can be observed in unloading and reloading as scetched in Fig. 1. The concept of multiple (nested) yield conditions is not new (see e.g. [14], [23] to [26]). In the context, however, with a generalized evolution law for plastic strain it becomes a new physical meaning and it opens new aspects.

The generalized approach for the evolution law for plastic strain can be easily extended to elastic-viscoplastic materials. This is shown in [16], [27]. We refer to it.

## 4. Some Applications

In the following the developed concept shall be specified to isothermic deformations of elastic-plastic bodies in order to test it by comparison with some experimental results.

The specific free enthalpy may be given as

$$
\psi=\psi\left(s_{k}^{i}, T, b, B\right) \quad \text { with } \quad B=\beta_{k}^{i} \vartheta_{i}^{k}.
\tag{23}
$$

270
Th. Lehmann:

The yield condition taking into account a combination of isotropic and anisotropic hardening may have the form (at $T=\stackrel{\circ}{T}$)

$$F\left(s_{k}^{i}, b, \beta_{k}^{i}\right)=\left(t_{k}^{i}-c \beta_{k}^{i}\right)\left(t_{i}^{k}-c \beta_{i}^{k}\right)-k^{2}(b)=0 \quad \text { with } \quad c=\text { const. } \quad(24)$$

Concerning the evolution laws of the internal variables $b$ and $\beta_{k}^{i}$ we assume with respect to the balance eq. (11) of the free enthalpy

$$\dot{b}=\frac{\zeta^{*}}{\frac{\partial}{\partial b}\left\{\psi-T \frac{\partial \psi}{\partial T}\right\}} \frac{1}{\stackrel{\circ}{\varrho}} \underset{(i)}{s_{k}^{i} d_{i}^{k}}=\zeta \underset{(i)}{\dot{w}}\quad (25a)$$

$$\left.\beta_{k}^{i}\right|_{0}=\frac{\left(1-\zeta^{*}\right) c}{\stackrel{\circ}{\varrho}^{2} \frac{\partial \psi}{\partial B}\left\{\psi-T \frac{\partial \psi}{\partial T}\right\}} \underset{(i)}{d_{k}^{i}}=\xi \underset{(i)}{d_{k}^{i}}.\quad (25b)$$

The quantities $\zeta$ and $\xi$ may still depend on the whole set of state variables. If depends merely on the internal variable $b$ then $b$ becomes an unique function of the plastic work $w$ defined by integration of (25a). In this case and only in this case we can use the plastic work as a thermodynamical state variable.
(i)

Furthermore $\beta_{k}^{i}$ becomes only a unique function of the plastic strain $\varepsilon_{k}^{i}$ if $\xi$ depends merely on $B$ and if the loading ensues proportionally $(\underset{(i)}{t_{k|0}^{i} \sim t_{k}^{i}})$. Only in this particular case the internal variable $\beta_{k}^{i}$ can be replaced by the plastic strain $\varepsilon_{k}^{i}$.
(i)

The loading condition corresponding to the yield condition (24) and to the evolution laws (25a) and (25b) reads

$$\left(t_{k}^{i}-c \beta_{k}^{i}\right)\left.t_{i}^{k}\right|_{0}>0.\quad (26)$$

Choosing the simplified approach (21) for the evolution of plastic strain we obtain finally

$$\underset{(i)}{d_{k}^{i}}=\frac{\left\{2\left(t_{s}^{r}-c \beta_{s}^{r}\right)-\varkappa\left[\frac{\zeta}{\stackrel{\circ}{\varrho}} \frac{d k}{d b} t_{s}^{r}+2 \xi c\left(t_{s}^{r}-c \beta_{s}^{r}\right)\right]\right\} t_{r | 0}^{s}}{\frac{\zeta}{\stackrel{\circ}{\varrho}} \frac{d k^{2}}{d b}\left(t_{n}^{m}-c \beta_{n}^{m}\right) t_{m}^{n}+2 \xi c k^{2}}\left(t_{k}^{i}-c \beta_{k}^{i}\right)+\varkappa t_{k | 0}^{i}.\quad (27)$$

From Eq. (27) it is obvious that the terms containing the parameter $\varkappa$ extinguish one another in proportional loading as already mentioned. Therefore the second term of the generalized approach (20) or (21), respectively, operates only in non-proportional loading like, for instance, in shear processes where the principal axes of stresses rotate against the material elements.

The requirements of the second law of thermodynamics are fulfilled by assuming

$$\underset{(d)}{\dot{w}}=\frac{1-\zeta}{\stackrel{\circ}{\varrho}}\left(t_{k}^{i}-c \beta_{k}^{i}\right) \underset{(i)}{d_{i}^{k}}\quad (28a)$$

$$\stackrel{\circ}{T} \dot{\eta}=0.\quad (28b)$$

In this case results

$$
\underset{(h)}{\dot{w}}=\underset{(i)}{\dot{w}}-\underset{(d)}{\dot{w}}=\frac{\zeta}{\dot{\varrho}} \underset{(i)}{t_{k}^{i} d_{i}^{k}}+\frac{1-\zeta}{\dot{\varrho}} c \underset{(i)}{\beta_{k}^{i} d_{i}^{k}} \lessgtr 0. \tag{28c}
$$

It should be mentioned, however, that the second law of thermodynamics also allows for distributions of the inelastic work which are different from (28a), (28c). This distribution is an open question which has to be answered by careful experi- ments.

In the following applications the weighted stresses $s_{k}^{i}$ are replaced by the stresses $\sigma_{k}^{i}$ which causes only a small error [18]. Furthermore the parameter $x$ in the evolution law for plastic strain is taken as a constant. The theoretical results are compared with some (preliminary) experiments carried out by Blix [28] in the Institute of Mechanics of the Ruhr-University and with experimental results obtained by Hecker [13].

The experiments performed by Blix are achieved with the help of a testing machine which allows for independent (stress or strain controlled) axial and torsional displacements. The scheme of this testing machine is shown in Fig. 2. Thin-walled steel tubes are used as specimens like in the experiments of Hohen- emser and Prager [7], [8].

In a first experiment the material properties were tested in pure tension. The results of this experiment and their description by an isotropic hardening law are shown in Fig. 3. After that two other experiments with different loading paths (each of these both with new specimens) were carried out. In the first one the loading path consists of pure tension in a first step followed by a twisting (with $\varepsilon=$ const.) in a second step. In the second case the sequence of these both steps is interchanged. The experimental data are compared with the theoretical results

![](./images/812300629941682178_2.jpg)

Fig. 2. Scheme of the testing machine

$$F=\tau_{k}^{i} \tau_{i}^{k}-k_{(i)}^{2}(w)=0$$

$$
\begin{aligned}
d_{k}^{i}= & \left.\frac{1}{2 G} \tau_{k}^{i}\right|_{0}+\left.\frac{1}{9 K} g_{r}^{r}\right|_{0} \delta_{k}^{i} \\
& +\dot{\lambda} \frac{\partial F}{\partial \sigma_{i}^{k}}+\left.\varkappa \tau_{k}^{i}\right|_{0}
\end{aligned}
$$

$$k_{(i)}^{2}(w)=\stackrel{\circ}{k}^{2}\left\{1+a\left(\frac{w_{(i)}}{\stackrel{\circ}{k}}+d\right)^{n}\right\}$$

$$\stackrel{\circ}{k}=130,5 \mathrm{~N} / \mathrm{mm}^{2}$$
$$G=81000 \mathrm{~N} / \mathrm{mm}^{2}$$
$$\varkappa 2 G=\quad 3,2$$
$$a=\quad 1,15$$
$$d=\quad 1,72 \cdot 10^{-4}$$
$$n=\quad 0,435$$

![](./images/812300629941682178_3.jpg)

Fig. 3. Specimen (steel CK 15) and material constants

obtained by means of the normality rule $(\varkappa=0)$ and by means of an extended approach (21) as shown in Figs. 4 and 5. It can be seen that the extended approach leads to better results. Some discrepancies, however, still exist. A respective better agreement can be expected by taking into account a combination of iso- tropic and anisotropic hardening. The obtained experimental data, however, were not sufficient, to state such a hardening law. Further improvement of the theo- retical results can be expected by introducing variable values of the parameter $\varkappa$.

The mentioned experiment performed by Hecker [13] with brass tubes con-

![](./images/812300629941682178_4.jpg)

Fig. 4. Stepwise deformation tension-torsion

![](./images/812300629941682178_5.jpg)

Fig. 5. Stepwise deformation torsion--tension

![](./images/812300629941682178_6.jpg)

Fig. 6. Poynting-effect in pure shear (brass Ms 63)

cerns the Poynting-effect in pure shear. From the comparison of theoretical and experimental results as shown in Fig. 6 it can be seen that an approach with
$$x=0$$
leads to an unsatisfactory description of the Poynting-effect

## 5. Final Remarks
More experimental data and their comparison with theoretical results are needed in order to ascertain the material parameters entering into the constitutive law and to check the capability of the different approaches. It can be expected,

however, that an extended approach for the evolution law of plastic strains as given in (20) represents an enlarged frame to fit the constitutive law to the real material behaviour particularly in complex loading histories, bifurcation problems, or, more generally, in problems with rotating principal axes of stresses during loading histories.

References

[1] St. Venant, M. de: Sur l'établissement des équations des mouvements intérieurs opérés dans les corps solides ductiles au delá des limites où l'élasticité pourrait les ramener à leur premier état. C. R. Acad. Sci. Paris 70, 473-478 (1870).

[2] Levy, M.: Mémoire sur les équations générals des mouvements intérieur des corps solides ductiles au delà des limites où l'élasticité pourrait les ramener à leur premierétat. C. R. Acad. Sci. Paris 70, 1323-1325 (1870).

[3] v. Mises, R.: Mechanik der festen Körper im plastisch deformablen Zustand. Nachr. Königl. Ges. Wiss. Göttingen, math.-phys. Kl. 1913, 582-592.

[4] Prandtl, L.: Spannungsverteilung in plastischen Körpern. Proc. 1. Int. Congr. Appl. Mech. Delft, 43-54, 1924.

[5] Reuss, A.: Berücksichtigung der elastischen Formänderung in der Plastizitätslehre. ZAMM 10, 266-274 (1930).

[6] Hencky, H.: Zur Theorie plastischer Deformationen und der hierdurch im Material hervorgerufenen Nachspannungen. ZAMM4, 323-334 (1926), and Proc. 1. Int. Congr. Appl. Mech. Delft, 312-317, 1924.

[7] Hohenemser, K.: Fließversuche an Rohren aus Stahl bei kombinierter Zug- und Torsionsbeanspruchung. ZAMM 11, 15-19 (1931).

[8] Hohenemser, K., Prager, W.: Beitrag zur Mechanik des bildsamen Verhaltens von Fließstahl. ZAMM 12, 1-14 (1932).

[9] Pflüger, A.: Zur plastischen Beulung von Flächenträgern. ZAMM 47, T209-T211(1967).

[10] Rice, J. R.: The localization of plastic deformation. Proc. 14. IUTAM Congr. Delft,207-220 (1976).

[11] Christoffersen, J., Hutchinson, J. W.: A class of phenomenological corner theories of plasticity. J. Mech. Phys. Sol. 27, 465-487 (1979).

[12] Sewell, M. J.: A plastic flow rule at a yield vertex. J. Mech. Phys. Sol. 22, 469-490(1974).

[13] Hecker, F. W.: Die Wirkung des Bauschinger-Effektes bei großen Torsions-Form-änderungen. Diss., TU Hannover, 1967.

[14] Shiratori, E., Ikegami, K., Yoshida, F.: Analysis of stress-strain relations by use of an anisotropic hardening plastic material. J. Mech. Phys. Sol. 27, 213-229 (1979).

[15] Lehmann, Th.: Some aspects of non-isothermic large inelastic deformations. SM Archives 3, 261-317 (1978).

[16] Lehmann, Th.: On constitutive relations in thermoplasticity. Proc. IUTAM Symp. Three dimensional constitutive relationships and ductile fracture. Dourdan, 1980, pp. 289-306. North-Holland 1981.

[17] Lehmann, Th.: Coupling phenomena in thermoplasticity. Nucl. Eng. Des. 57, 323-332(1980).

[18] Lehmann, Th.: On large elastic-plastic deformations, in: Foundations of plasticity(Sawczuk, A., ed.), pp. 571-585. Leyden: Noordhoff 1973.

[19] Hlyushin, A. A.: Foundations of the general mathematical theory of plasticity, in:Plasticity. Moscow: 1948. (Orig. in Russian.)

[20] Drucker, D. C.: A more fundamental approach to plastic stress-strain relations.1. U.S. Nat. Congr. Appl. Mech., 487-491, 1952.

[21] Lehmann, Th.: Zur Beschreibung großer plastischer Formänderungen unter Berück- sichtigung der Werkstoffverfestigung. Rheol. Acta 2, 247-254 (1962).

[22] Lehmann, Th.: Anisotrope plastische Formänderungen. Rheol. Acta 3, 281-285(1964).

[23] Mroz, Z.: An attempt to describe the behaviour of metals under cyclic loads using a more general workhardening model. Acta Mech. 7, 199 (1969).

[24] Mroz, Z., Lind, N. C.: Simplified theories of cyclic plasticity. Acta Mech. 22, 131 (1975).

[25] Eisenberg, M. A., Phillips, A.: A theory of plasticity with non-coincident yield and loading surfaces. Acta Mech. 11, 247 (1971).

[26] Phillips, A., Lee, Chong-Won: Yield surfaces and loading surfaces. Experiments and recommendations. Int. J. Solids Struct. 15, 715 (1979).

[27] Lehmann, Th.: On the theory of large, non-isothermic, elastic-plastic and elastic- viscoplastic deformations. Arch. Mech. 29, 393 (1977).

[28] Blix, U.: Vergleich verschiedener Formänderungsgesetze der Plastizitätstheorie. Thesis, Ruhr-University Bochum.

Prof. Dr.-Ing. Th. Lehmann
Lehrstuhl für Mechanik I
Ruhr-Universität Bochum
Postfach 102148
D-4630 Bochum 1
Federal Republic of Germany