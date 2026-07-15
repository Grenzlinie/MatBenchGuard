ZAMM · Z. angew. Math. Mech. 72 (1992) 12, 667-674
Akademie Verlag

MIHÃILESCU-SULICIU, M.; SULICIU, I.

# On the Method of Characteristics in Rate-Type Viscoelasticity with Non-Monotone Equilibrium Curve

Die Standard-Charakteristenmethode wird auf ein hyperbolisches System von partiellen Differentialgleichungen, die die Bewegung eines viskoelastischen Körpers beschreiben, angewandt. Die Gleichgewichtskurve kann vom van der Waals-Typ sein, so daß das System Phasenübergangsphänomene beschreiben kann. Für Probleme isolierter Körper werden notwendige Bedingungen über die Stufen der Zeitintegration der ersten und zweiten numerischen Approximationen gegeben, so daß die Gesamtenergie der numerischen Lösung eine nicht wachsende Funktion der Zahl der zeitlichen Integrationsstufen ist. Diese Eigenschaft wird verlangt, weil die Gesamtenergie der exakten Lösung eine nicht wachsende Funktion der Zeit ist, wie es der zweite Hauptsatz der Thermodynamik erfordert. Numerische Beispiele für Probleme isolierter Körper, wenn die Störungen obiger Bedingungen zu numerischen Instabilitäten führen, werden woanders vorgestellt (siehe Einleitung).

The standard method of characteristics is applied to a hyperbolic system of partial differential equations describing the motion of a viscoelastic body. The equilibrium curve can be of the van der Waals type such that the system may describe phase transition phenomena. For isolated body problems, sufficient conditions are given on the time integration steps of the first and second numerical approximations such that the total energy of the numerical solution be a nonincreasing function of the number of time integration steps. This property is required since the total energy of the exact solution is a nonincreasing function of time as required by the second law of thermodynamics. Numerical examples of nonisolated body problems when the violations of the above conditions lead to numerical instabilities are presented elsewhere (see Introduction).

Стандардный метод характеристик применяется на гиперболистическую систему уравений в частных производных, которая описывает движение вязко-упругого тела. Кривая равновесия может быть типа ван-дер-Вальса так, что система может описать феномены фазового перехода. Для задачи изолированных тел даются достаточные условия на шаги временной интеграции первых и вторых приближений так, что полная энергия численного решения является невозрастающей функцией от числа шагов временного интегрирования. Это свойство требуется потому, что полная энергия точного решения является невозрастающей функцией от времени, что требуется от второго закона тремодинамики. В другом месте (см. Введение) даются численные примеры задач неизолированных тел, если нарушение вышеупомянутых свойств ведет к численным неустойчивостям.

MSC (1980): 82A25, 73U05

## Introduction

We deal here as in [1] with a system of hyperbolic partial differential equations describing the one-dimensional motion of a rate-type viscoelastic body. In contrast to [1] we allow the equilibrium curve $(\varepsilon, \sigma=\sigma_{R}(\varepsilon)), \varepsilon \in R$ to have negative slope on some strain intervals. However, under general enough conditions a non negative free energy can still be constructed which is no longer convex but the necessary energy estimates can be obtained as it is summarized in Section I.

In order to make the paper selfcontained or close to we describe shortly the method of characteristics in Section II. In Section III we prove our main results consisting of Theorem 1 and especially of Theorem 2 which give upper bounds, in terms of the material constants, on the time integration steps $h_{m}'$ and $h_{m}'' \leqq h_{m}'$ for the first and second approximations, respectively. These upper bounds are obtained from the requirement that the total numerical energy be a non increasing function of the time integration step as the total energy of the exact solution is a non increasing function of time for an isolated body problem and for the Cauchy problem. We note that both $h_{m}'$ and $h_{m}''$ as well as $h_{m}$ of [1] are independent of the input data (here the initial data).

The present conditions (I.6) on the equilibrium function $\sigma_{R}(\varepsilon)$ make the constitutive equation (I.1) $)_{3}$ able to incorporate physical instabilities which are characteristic to phase transitions as discussed in [5] for the piecewise linear model (I.7). The problem we are concerned with here is the way to isolate the possible numerical instabilities from the physical ones, i.e. to select properly the time integration step in the method of characteristics such that numerical instabilities are avoided.

The example given in [1] shows that if the time integration step exceeds the energetic bound $h_{m}$ then both numerical approximations of the relaxation process considered there are numerically unstable.

We remind the reader that in [1] the energetic bound $h_{m}$ was obtained for isolated body problems and Cauchy problems only. Here the energetic bound $h_{m}'$ for the first approximation and $h_{m}''$ for the second approximation (see formulas (III.4) and (III.6)) are obtained for the same problems too. The numerical experiments of [7] show that if the bound $h_{m}$ is exceeded in a non isolated body problem then the numerical instabilities do appear. For the situation presented here numerical experiments for non isolated body problems with an equilibrium curve of van der Waals type (see (I.11) and (I.13)) were performed in [3] with the purpose of studying phase transition properties. A viscoelastic model with an equilibrium curve given by (I.7) was used in [9] in order to study the shock wave structure when phase transitions are involved. The numerical experiments of [3] and [9] show that when the energetic bounds on the time integration step are violated, the numerical instabilities do appear for the non isolated body problem too.

The results obtained here apply to one-dimensional isothermal problems involving phase transitions in solids as well as in fluids. Examples of the behaviour of the equilibrium curves as discussed here are typical to shape memory alloys (see for instance [9], [10]) and to liquid-gas transitions when the temperature $T$ is below the critical value $T_c$ (see for instance RowLINSON [11]). A reviewer pointed us the reference [12] which may be related to our work but we could not locate it here.

## I. Preliminaries

### 1. Statement of the problem

We consider as in [1] the semilinear system of partial differential equations describing the one dimensional motion of a viscoelastic body

$$
\varrho_{0} \frac{\partial v}{\partial t}-\frac{\partial \sigma}{\partial x}=0, \quad \frac{\partial \varepsilon}{\partial t}-\frac{\partial v}{\partial x}=0, \quad \frac{\partial \sigma}{\partial t}-E \frac{\partial \varepsilon}{\partial t}=g(\varepsilon, \sigma)
\tag{1}
$$

and we state for it the initial or initial-boundary value problems

$$
v(x, 0)=v_{0}(x), \quad \sigma(x, 0)=\sigma_{0}(x), \quad \varepsilon(x, 0)=\varepsilon_{0}(x), \quad x \in R
\tag{2}
$$

or

$$
\begin{aligned}
& v(x, 0)=v_{0}(x), \quad \sigma(x, 0)=\sigma_{0}(x), \quad \varepsilon(x, 0)=\varepsilon_{0}(x), \quad x \in[0, l] \\
& v(0, t)=v(l, t)=0, \quad t \geqq 0.
\end{aligned}
$$

The material function $g(\varepsilon, \sigma)$ is taken again as a linear function of the overstress $\sigma-\sigma_{R}(\varepsilon)$, i.e.

$$
g(\varepsilon, \sigma)=-k(\varepsilon, \sigma)\left[\sigma-\sigma_{R}(\varepsilon)\right]
\tag{4}
$$

with $k: R^{2} \rightarrow R$, a continuous function such that

$$
\begin{aligned}
& 0<k_{1} \leqq k(\varepsilon, \sigma) \leqq k_{2} \quad \text { for any } \quad(\varepsilon, \sigma) \in R^{2} \\
& k_{1}=\text { const. }, \quad k_{2}=\text { const. }
\end{aligned}
\tag{5}
$$

We release now the assumptions of [1] on the equilibrium curve $\sigma=\sigma_{R}(\varepsilon)$ and adopt the assumption stated in [2] on this function, i.e. we suppose $\sigma_{R}: R \rightarrow R$ to be a piecewise smooth function that everywhere $\sigma_{R}^{\prime}(\varepsilon)$ exists, it satisfies

$$
-M \leqq \sigma_{R}^{\prime}(\varepsilon) \leqq E_{3}<E, \quad \sigma_{R}(0)=0 \quad \text { and also } \quad \int_{0}^{\varepsilon} \sigma_{R}(s) \mathrm{d} s \geqq 0
\tag{6}
$$

for any $\varepsilon$, where $M$ and $E_{3}$ are positive constants.

We now give some comments on the hypotheses (4) and (6). In several examples encountered in rate-type viscoelasticity or viscoplasticity the function $g(\varepsilon, \sigma)$ may not be linear in the overstress $\sigma-\sigma_{R}(\varepsilon)$. The results of the same type as presented in [1], Section E, are obtained in [3] for the numerical stability of relaxation processes in the case when $g(\varepsilon, \sigma)$ is proportional to $\left|\sigma-\sigma_{R}(\varepsilon)\right|^{\lambda} \cdot \operatorname{sgn}\left(\sigma-\sigma_{R}(\varepsilon)\right), \lambda=$ const. $>0$.

The hypotheses (6) are used in [2] to get a positive free energy function and the approach to the equilibrium when it is appropriate. The piecewise smoothness assumption of the equilibrium curve can be omitted and still get the same result (see [4]). The assumption (6) allows us to get simpler estimates on the time integration step for both useful approximations for the characteristics method.

In some cases $\sigma_{R}(\varepsilon)$ is not defined on $R$ but on some interval $I \subset R$ containing $\varepsilon=0$ and $\sigma_{R}^{\prime}(\varepsilon)$ is not bounded on $I$ (see the van der Waals example below) but if we know a priori that $\varepsilon(x, t) \in I^{\prime} \subset I$ for all $x$ and $t$ and that (6) holds for all $\varepsilon \in I^{\prime}$ then our estimates still hold.

We give two examples of equilibrium curves $\sigma_{R}(\varepsilon)$ verifying (6) and which are useful when studying phase transitions (see also the examples considered in [2]).

#### A piecewise linear and continuous example [5]

$$
\sigma_{R}(\varepsilon)=\left\{\begin{array}{l}
E_{3} \varepsilon \quad \varepsilon \leqq \varepsilon_{M} \\
\left.\begin{array}{l}
\sigma_{M}-E_{2}\left(\varepsilon-\varepsilon_{M}\right) \\
\sigma_{m}-E_{2}\left(\varepsilon-\varepsilon_{m}\right)
\end{array}\right\} \varepsilon_{M}<\varepsilon<\varepsilon_{m} \\
\sigma_{m}+E_{1}\left(\varepsilon-\varepsilon_{m}\right) \quad \varepsilon \geqq \varepsilon_{m}
\end{array}\right.
\tag{7}
$$

where

$$
\begin{aligned}
& 0<\varepsilon_{M}<\varepsilon_{m}, \quad 0<E_{1}<E_{3}<E, \quad E_{2}>0 \\
& \sigma_{M}=E_{3} \varepsilon_{M}, \quad \sigma_{M}-\sigma_{m}=E_{2}\left(\varepsilon_{m}-\varepsilon_{M}\right).
\end{aligned}
\tag{8}
$$

The condition (6) on $\sigma_{R}'(\varepsilon)$ given by (7) is verified with $M = E_{2}$. In order to see the physical meaning of the integral condition (6) we introduce the Maxwell's line $\sigma = \sigma_{\mu} \in (\sigma_{m}, \sigma_{M})$ which determines together with $\sigma = \sigma_{R}(\varepsilon)$ given above two triangles of equal areas. The interval $(\varepsilon_{\alpha}, \varepsilon_{\beta})$, $\varepsilon_{\alpha} < \varepsilon_{M}$ and $\varepsilon_{\beta} > \varepsilon_{m}$ such that

$$
\sigma_{\mu} = \sigma_{R}(\varepsilon_{\alpha}) = \sigma_{R}(\varepsilon_{\beta})
\tag{9}
$$

is called Maxwell's interval. We have

$$
\begin{align*}
\sigma_{\mu} &= (\sigma_{m} + a\sigma_{M})/(1 + a), & a = [E_{1}(E_{2} + E_{3})/(E_{3}(E_{1} + E_{2}))]^{1/2} < 1 \\
\varepsilon_{\alpha} &= \sigma_{\mu}/E_{3}, & \varepsilon_{\beta} = \varepsilon_{m} + a\sigma_{M}/[E_{1}(1 + a)].
\end{align*}
\tag{10}
$$

Now one can see easily that the constitutive equation (7) verifies the integral condition (6) if and only if the Maxwell's stress $\sigma_{\mu}$ is non negative or, equivalently, the strain $\varepsilon = 0$ is not in the Maxwell's interval. This condition can also be expressed in terms of the relative free energy as it was shortly discussed in [5].

A constitutive equation of van der Waals type. The van der Waals constitutive equation is

$$
p = p_{R}(V, T) = \frac{RT}{V - b} - \frac{a}{V^{2}}, \quad V > b
\tag{11}
$$

where $p$ is the pressure, $V$ is the specific volume, $T$ is the absolute temperature, $a =$ constant here, and $R, a, b$ are positive constants. When a one-dimensional motion $y = y(x, t)$ with respect to a homogeneous and equilibrium configuration of specific volume $V_{0} = 1/\varrho_{0}$ and pressure $p_{0} = p_{R}(V_{0}, T)$ is considered, we can define the strain by $\varepsilon = \partial y/\partial x - 1$. The balance of mass relates $\varepsilon$ and $V$ by

$$
\varepsilon = V/V_{0} - 1, \quad \varepsilon \in \left( \frac{b}{V_{0}} - 1, \infty \right).
\tag{12}
$$

We can define the equilibrium stress for a fixed absolute temperature by

$$
\sigma_{R}(\varepsilon) = p_{0} - p_{R}(V_{0}(1 + \varepsilon), T).
\tag{13}
$$

This curve is smooth and it has a similar behaviour with $\sigma_{R}(\varepsilon)$ given by (7) when $T$ is in the interval $(T_{0}, T_{c})$, $T_{c} = 8a/(27Rb)$, $T_{0} = a/(4Rb)$, i.e. it has an interval of strains where $\sigma_{R}'(\varepsilon) < 0$. If we know a priori that there is a small enough strain $\varepsilon_{\text{min}} \in \left( \frac{b}{V_{0}} - 1, 0 \right)$, $\sigma_{R}'(\varepsilon_{\text{min}}) > 0$ such that $\varepsilon(x, t) > \varepsilon_{\text{min}}$ for all $(x, t)$ then we can take

$$
E = \text{const.} > E_{3} = \sigma_{R}'(\varepsilon_{\text{min}})
\tag{14}
$$

and $M$ as the maximum of $-\sigma_{R}'(\varepsilon)$ on the strain interval where $\sigma_{R}'(\varepsilon)$ is negative. Then the condition (6) on $\sigma_{R}'(\varepsilon)$ is verified. The integral condition (6) is verified if $V_{0}$ is chosen outside the Maxwell's interval of equation (11).

### 2. Energy

As in [1] (see also [2]) the constitutive equation $(1)_{3}$ with $g(\varepsilon, \sigma)$ given by (4) and its entries $k(\varepsilon, \sigma)$ and $\sigma_{R}(\varepsilon)$ verifying (5) and (6) has a unique, smooth and non negative free energy function $\psi(\varepsilon, \sigma)$ which satisfies

$$
\frac{\partial \psi}{\partial \varepsilon} + E \frac{\partial \psi}{\partial \sigma} = \sigma/\varrho_{0}, \quad \psi(0, 0) = 0, \quad \frac{\partial \psi}{\partial \sigma} g \leqq 0
\tag{15}
$$

and has the form

$$
\varrho_{0}\psi(\varepsilon, \sigma) = \frac{\sigma^{2}}{2E} + \varphi(\sigma - E\varepsilon) \geqq 0 \quad \text{for all} \quad (\varepsilon, \sigma)
\tag{16}
$$

where $\varphi$ is a function of the argument $\sigma - E\varepsilon$. In addition

$$
\frac{k(\varepsilon, \sigma)}{E + M} (\sigma - \sigma_{R}(\varepsilon))^{2} \leqq -\varrho_{0} \frac{\partial \psi}{\partial \sigma} g \leqq \frac{k(\varepsilon, \sigma)}{E - E_{3}} (\sigma - \sigma_{R}(\varepsilon))^{2}
\tag{17}
$$

and for any $r$ and $s$ the following Lagrange type formula (see [2]) is verified by $\varphi$

$$
\varphi(r + s) = \varphi(r) + s\varphi'(r) + \frac{s^{2}}{2} m
\tag{18}
$$

where $m$ is an appropriate real number subjected to the restriction

$$
-\frac{M}{E(E+M)} \leqq m \leqq \frac{E_{3}}{E\left(E-E_{3}\right)}.
\tag{19}
$$

We note that the relations (17) and (18) represent a substitute of the relations (P.12) and (P.13) of [1] obtained under the much weaker condition (6) of this paper than condition (P.6) of [1].

As in [1] anywhere where the solutions of the problems (1) + (2) or (1) + (3) are smooth the same energy identity

$$
\varrho_{0} \frac{\partial e^{*}}{\partial t}-\frac{\partial}{\partial x}(\sigma v)-\varrho_{0} \frac{\partial \psi(\varepsilon, \sigma)}{\partial \sigma} g(\varepsilon, \sigma)=0, \quad e^{*}=\frac{v^{2}}{2}+\psi(\varepsilon, \sigma)
\tag{20}
$$

holds. The total energy of the isolated body problem (1) + (3) is

$$
e(t)=\int_{0}^{l} \varrho_{0} e^{*}(v(x, t), \sigma(x, t), \varepsilon(x, t)) \mathrm{d} x, \quad t \geqq 0.
\tag{21}
$$

The total energy for the Cauchy problem (1) + (2) has the same form except the integral is taken on $R$ instead of $[0, l]$.

We have from (20), using (17) and (21), the following energy inequality

$$
\frac{\mathrm{d} e(t)}{\mathrm{d} t} \leqq 0, \quad 0 \leqq e(t) \leqq e(0), \quad t \geqq 0
\tag{22}
$$

and the following approach to the equilibrium

$$
\int_{0}^{t} \int_{0}^{l}\left[\sigma(x, s)-\sigma_{R}(\varepsilon(x, s))\right]^{2} \mathrm{~d} x \mathrm{~d} s \leqq \frac{(E+M)}{k_{1}}(e(0)-e(t)).
\tag{23}
$$

The last inequality tells us that for large $k_{1}$ the solution of the viscoelastic problem approaches the solution of the elastic problem, i.e. when the constitutive equation $(1)_{3}$ is replaced by $\sigma=\sigma_{R}(\varepsilon)$ and the initial condition is $\sigma_{0}(x)=\sigma_{R}\left(\varepsilon_{0}(x)\right)$.

## II. The method of characteristics

The system (I.1) is written in the characteristic form

$$
\frac{\partial p}{\partial t}-c \frac{\partial p}{\partial x}=G(p, q, r), \quad \frac{\partial q}{\partial t}+c \frac{\partial q}{\partial x}=G(p, q, r), \quad \frac{\partial r}{\partial t}=G(p, q, r)
\tag{1}
$$

by the change of dependent variables

$$
p=\sigma+\sqrt{\varrho_{0} E} v, \quad q=\sigma-\sqrt{\varrho_{0} E} v, \quad r=\sigma-E \varepsilon
\tag{2}
$$

where

$$
G(p, q, r)=g\left(\frac{1}{E}\left(\frac{p+q}{2}-r\right), \frac{p+q}{2}\right), \quad c=\sqrt{E / \varrho_{0}}.
\tag{3}
$$

The data (I.2) and (I.3) become

$$
p(x, 0)=p_{0}(x), \quad q(x, 0)=q_{0}(x), \quad r(x, 0)=r_{0}(x), \quad x \in R
\tag{4}
$$

and

$$
\begin{aligned}
& p(x, 0)=p_{0}(x), \quad q(x, 0)=q_{0}(x), \quad r(x, 0)=r_{0}(x), \quad x \in[0, l] \\
& p(0, t)=q(0, t), \quad p(l, t)=q(l, t), \quad t \geqq 0
\end{aligned}
\tag{5}
$$

respectively.

The system (1) can also be written under the form

$$
\begin{aligned}
& \mathrm{d} q=G(p, q, r) \mathrm{d} t \quad \text { on } \mathrm{d} x=c \mathrm{~d} t, \quad \mathrm{~d} p=G(p, q, r) \mathrm{d} t \quad \text { on } \mathrm{d} x=-c \mathrm{~d} t, \\
& \mathrm{~d} r=G(p, q, r) \mathrm{d} t \quad \text { on } \mathrm{d} x=0
\end{aligned}
\tag{6}
$$

which is used in order to construct a numerical solution for the problem (1) + (5) (and (1) + (4)).

The first numerical approximation for the problem (1) + (5) is a set of three functions $p, q, r$ defined on a discrete set

$$
D^{*}=\left\{\left(x_{i}, t_{j}\right), x_{i}=i c h, t_{j}=j h, h=\text { const., } i=0,1, \ldots, N, j=0,1,2, \ldots, N=l /(c h)\right\}
\tag{7}
$$

which satisfy the following iterative relations

$$
\begin{align*}
p^{i} &= p_{i+1} + hG_{i+1}, & q^{i} &= q_{i-1} + hG_{i-1}, & r^{i} &= r_{i} + hG_{i}, & &i=1,2,...,N-1 \\
p^{0} &= p_{1} + hG_{1}, & q^{0} &= p^{0}, & r^{0} &= r_{0} + hG_{0} \\
p^{N} &= q^{N}, & q^{N} &= q_{N-1} + hG_{N-1}, & r^{N} &= r_{N} + hG_{N}
\end{align*}
\tag{8}
$$

where

$$
\begin{align*}
(p_i, q_i, r_i) &= (p, q, r)(x_i, t_j), & (p^i, q^i, r^i) &= (p, q, r)(x_i, t_{j+1}) \\
G_i &= G(p_i, q_i, r_i), & &i=0,1,...,N, & &j=0,1,2,...
\end{align*}
\tag{9}
$$

and for $j=0$

$$
(p_i, q_i, r_i) = (p, q, r)(x_i, 0) = (p_0, q_0, r_0)(x_i), \quad i=0,1,...,N.
\tag{10}
$$

The second numerical approximation for the problem (1) + (5) is a set of three functions $p, q, r$ defined on the same discrete set (7) and which satisfy the following relations

$$
\begin{align*}
p^{i} &= p_{i+1} + \frac{h}{2}\left(G_{i+1}+\tilde{G}^{i}\right), & q^{i} &= q_{i-1} + \frac{h}{2}\left(G_{i-1}+\tilde{G}^{i}\right), & r^{i} &= r_{i} + \frac{h}{2}\left(G_{i}+\tilde{G}^{i}\right), & &i=1,2,...,N-1 \\
p^{0} &= p_{1} + \frac{h}{2}\left(G_{1}+\tilde{G}^{0}\right), & q^{0} &= p^{0}, & r^{0} &= r_{0} + \frac{h}{2}\left(G_{0}+\tilde{G}^{0}\right), \\
p^{N} &= q^{N}, & q^{N} &= q_{N-1} + \frac{h}{2}\left(G_{N-1}+\tilde{G}^{N}\right), & r^{N} &= r_{N} + \frac{h}{2}\left(G_{N}+\tilde{G}^{N}\right),
\end{align*}
\tag{11}
$$

where $(p_i, q_i, r_i), (p^i, q^i, r^i), G_i$ are defined by (9) and

$$
\tilde{G}^{i}=G\left(p_{i+1}+h G_{i+1}, q_{i-1}+h G_{i-1}, r_{i}+h G_{i}\right).
\tag{12}
$$

For $j=0$ condition (10) is assumed.

We must note again that when we compare the exact solution with its first approximation the difference is of order $h$ and for the second approximation the difference is of order $h^2$. Sometimes in the literature the iteration suggested by the way the second approximation is obtained from the first one is repeated several times with the hope that better results are obtained. It is known that such repeated iterations remain of the same order $h^2$ as the second one (see [6] pg. 434). Therefore this procedure leads to waste of computation time and moreover one may give examples when higher order approximations give slightly worse results than the second approximation.

For the Cauchy problem (1) + (4) the first and the second approximations are similarly defined.

### III. The energetic estimates on the size of the time integration step

The density of the total energy $e^{*}$ defined by (I.20)$_2$ and $\frac{\partial \psi}{\partial \sigma} g$ can be written in the variables $p, q, r$ as

$$
e^{*}(p, q, r)=\left[\frac{p^{2}+q^{2}}{4 E}+\varphi(r)\right] / \varrho_{0}, \quad \left(\frac{\partial \psi}{\partial \sigma} g\right)(\varepsilon, \sigma)=G(p, q, r)\left[\frac{p+q}{2 E}+\varphi^{\prime}(r)\right]
\tag{1}
$$

if we take into account (I.16) and (II.2).

The total numerical energy for the problem (I.1) + (I.3) or equivalently of the problem (II.1) + (II.5) at time $t=jh$ is defined by

$$
e^{j}=\frac{1}{2}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left[\frac{\left(p^{i}\right)^{2}+\left(q^{i}\right)^{2}}{4 E}+\varphi\left(r^{i}\right)\right]
\tag{2}
$$

and the time $t=(j-1)h$ by

$$
e_{j-1}=\frac{1}{2}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left[\frac{p_{i}^{2}+q_{i}^{2}}{4 E}+\varphi\left(r_{i}\right)\right].
\tag{3}
$$

Since the non increasing property (I.22) of the total energy of the exact solution is a consequence of the second law of thermodynamics we have to require the same property to hold for the numerical solution too. This requirement implies an upper bound for the time integration step $h$. In fact we have the following

Theorem 1. Assume $g(\varepsilon, \sigma)$ is of the form (I.4), $k(\varepsilon, \sigma)$ verifies (I.5) and $\sigma_{R}(\varepsilon)$ verifies (I.6). Then the first numerical approximation has the following properties:

$$0 \leqq \ldots \leqq e^{j} \leqq e_{j-1} \leqq \ldots \leqq e_{0} \quad \text{for} \quad h \leqq h_{m}^{\prime}=\frac{2\left(E-E_{3}\right)}{k_{2}(E+M)}, \quad j=1,2, \ldots \tag{4}$$

$$e^{j} \geqq e_{j-1} \geqq \ldots \geqq e_{0} \geqq 0 \quad \text{for} \quad h \geqq h_{M}^{\prime}=\frac{2(E+M)}{k_{1}\left(E-E_{3}\right)}, \quad j=1,2, \ldots. \tag{5}$$

The proof of this theorem follows the same way as the proof of the corresponding theorem from [1] if we take into account the relations (I.17)-(I.19) (see also the proof of the next theorem).

Theorem 2. Under the same assumptions of Theorem 1 the second numerical approximation has the property

$$0 \leqq \ldots \leqq e^{j} \leqq e_{j-1} \leqq \ldots \leqq e_{0} \quad \text{for} \quad h \leqq h_{m}^{\prime \prime}=\frac{2}{k_{2}} \cdot \frac{E\left(E-E_{3}\right)}{E(E+M)+M\left(E-E_{3}\right)} \leqq h_{m}^{\prime}. \tag{6}$$

Proof. We can not apply the same argument as it was done in [1] to prove this theorem since $\varphi(r)$ is no longer convex; however part of the proof goes the same way. We introduce the notations (as in [1])

$$
\begin{aligned}
& \tilde{p}^{i}=p_{i+1}+h G_{i+1}, \quad i=0,1, \ldots, N-1, \quad \tilde{p}^{N}=\tilde{q}^{N}, \\
& \tilde{q}^{i}=q_{i-1}+h G_{i-1}, \quad i=1,2, \ldots, N, \quad \tilde{q}^{0}=\tilde{p}^{0}, \\
& \tilde{r}^{i}=r_{i}+h G_{i}, \quad \tilde{G}^{i}=G\left(\tilde{p}^{i}, \tilde{q}^{i}, \tilde{r}^{i}\right), \quad i=0,1, \ldots, N
\end{aligned} \tag{7}
$$

for the first approximation and

$$\bar{p}^{i}=\tilde{p}^{i}+h \tilde{G}^{i}, \quad \bar{q}^{i}=\tilde{q}^{i}+h \tilde{G}^{i}, \quad \bar{r}^{i}=\tilde{r}^{i}+h \tilde{G}^{i}, \quad i=0,1, \ldots, N. \tag{8}$$

Then from (II.11) we have for the second numerical approximation

$$
\begin{aligned}
& p^{i}=\frac{1}{2}\left(p_{i+1}+\bar{p}^{i}\right), \quad i=0, \ldots, N-1, \quad q^{i}=\frac{1}{2}\left(q_{i-1}+\bar{q}^{i}\right), \quad i=1, \ldots, N \\
& p^{N}=q^{N}, \quad p^{0}=q^{0}, \quad r^{i}=\frac{1}{2}\left(r_{i}+\bar{r}^{i}\right), \quad i=0,1, \ldots, N.
\end{aligned} \tag{9}
$$

In order to compute the numerical energy $e^{j}$ given by (2) we prove first the following formula

$$\varphi\left(\frac{r_{i}+\bar{r}^{i}}{2}\right)=\frac{1}{2}\left(\varphi\left(r_{i}\right)+\varphi\left(\bar{r}^{i}\right)\right)-\frac{\lambda_{i}\left(\bar{r}^{i}-r_{i}\right)^{2}}{4} m_{i} \tag{10}$$

where $\lambda_{i}$ and $m_{i}$ are appropriate numbers such that $\lambda_{i} \in(0,1)$ and $m_{i}$ verify (I.19), $i=0, \ldots, N$.

Since $\varphi^{\prime}(r)$ is continuous and piecewise smooth we have the Lagrange type formula (see [2])

$$\varphi^{\prime}(r+h)=\varphi^{\prime}(r)+h m$$

where $m$ satisfies (I.19).

To prove (10) we consider the function

$$f_{i}(\lambda)=\varphi\left(r_{i}+\frac{\lambda}{2}\left(\bar{r}^{i}-r_{i}\right)-\frac{1}{2}\left[\varphi\left(r_{i}\right)+\varphi\left(r_{i}+\lambda\left(\bar{r}^{i}-r_{i}\right)\right)\right], \quad \lambda \in[0,1].\right.$$

For this we have $f_{i}(0)=0$,

$$
\begin{aligned}
& f_{i}(1)=f_{i}^{\prime}\left(\lambda_{i}\right), \quad \lambda_{i} \in(0,1), \quad f_{i}(1)=\varphi\left(\frac{r_{i}+\bar{r}^{i}}{2}\right)-\frac{1}{2}\left(\varphi\left(r_{i}\right)+\varphi\left(\bar{r}^{i}\right)\right), \\
& f_{i}^{\prime}\left(\lambda_{i}\right)=\frac{1}{2}\left(\bar{r}^{i}-r_{i}\right)\left[\varphi^{\prime}\left(r_{i}+\frac{\lambda_{i}}{2}\left(\bar{r}^{i}-r_{i}\right)\right)-\varphi^{\prime}\left(r_{i}+\lambda_{i}\left(\bar{r}^{i}-r_{i}\right)\right)\right].
\end{aligned}
$$

We apply the above Lagrange formula and write

$$\varphi^{\prime}\left(r_{i}+\lambda_{i}\left(\bar{r}^{i}-r_{i}\right)\right)=\varphi^{\prime}\left(r_{i}+\frac{\lambda_{i}}{2}\left(\bar{r}^{i}-r_{i}\right)\right)+\frac{\lambda_{i}\left(\bar{r}^{i}-r_{i}\right)}{2} m_{i}$$

and thus formula (10) follows.

We now use (9) and (10) in formula (2) to get, after some long algebra, to the expression

$$e^{j}=\frac{1}{2}\left(e_{j-1}+\bar{e}^{j}\right)-\frac{1}{16 E}\left[\sum_{i=0}^{N-1}\left(\tilde{p}^{i}-p_{i+1}\right)^{2}+\sum_{i=1}^{N}\left(\tilde{q}^{i}-q_{i-1}\right)^{2}\right]-\frac{1}{8}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left[\lambda_{i}\left(\bar{r}^{i}-r_{i}\right)^{2} m_{i}\right] \tag{11}$$

where

$$
\vec{e}^{j}=\frac{1}{2}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left[\frac{\left(\tilde{p}^{i}\right)^{2}+\left(\tilde{q}^{i}\right)^{2}}{4 E}+\varphi\left(\tilde{r}^{i}\right)\right]. \tag{12}
$$

We note that (11) has the same form as (I.13) of [1].

By (8) and the use of (II.18) the energy $\vec{e}^{j}$ can be written as

$$
\vec{e}^{j}=\tilde{e}^{j}+\frac{h}{2}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left\{\tilde{G}^{i}\left[\frac{\tilde{p}^{i}+\tilde{q}^{i}}{2 E}+\varphi^{\prime}\left(\tilde{r}^{i}\right)\right]+\frac{h}{2}\left(\tilde{G}^{i}\right)^{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)\right\} \tag{13}
$$

where $\vec{e}^{j}$ is the numerical energy at $t=j h$ computed on the first approximation. We also have

$$
\hat{e}^{j}=e_{j-1}+\frac{h}{2}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left\{G_{i}\left[\frac{p_{i}+q_{i}}{2 E}+\varphi^{\prime}\left(r_{i}\right)\right]+\frac{h}{2} G_{i}^{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)\right\}. \tag{14}
$$

Finally we observe that with the use of (8) and (7) we have

$$
\begin{aligned}
& \tilde{p}^{i}-p_{i+1}=h\left(\tilde{G}^{i}+G_{i+1}\right), \quad i=0,1, \ldots, N-1, \quad \tilde{q}^{i}-q_{i-1}=h\left(\tilde{G}^{i}+G_{i-1}\right), \\
& i=1, \ldots, N, \quad \tilde{r}^{i}-r_{i}=h\left(\tilde{G}^{i}+G_{i}\right), \quad i=0,1, \ldots, N.
\end{aligned} \tag{15}
$$

The numerical energy $e^{j}$ computed, at time $t=j h$, on the second approximation takes its final form by using (12)-(15) in (11), i.e.

$$
\begin{aligned}
e^{j}= & e_{j-1}+\frac{h}{4}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left\{G_{i}\left[\frac{p_{i}+q_{i}}{2 E}+\varphi^{\prime}\left(r_{i}\right)\right]+\frac{h G_{i}^{2}}{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)+\tilde{G}^{i}\left[\frac{\tilde{p}^{i}+\tilde{q}^{i}}{2 E}+\varphi^{\prime}\left(\tilde{r}^{i}\right)\right]+\frac{h\left(\tilde{G}^{i}\right)^{2}}{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)\right\} \\
& -\frac{h^{2}}{8}\left(\sum_{i=0}^{N-1}+\sum_{i=1}^{N}\right)\left[\lambda_{i}\left(\tilde{G}^{i}+G_{i}\right)^{2} m_{i}\right]-\frac{h^{2}}{16 E}\left[\sum_{i=0}^{N-1}\left(\tilde{G}^{i}+G_{i+1}\right)^{2}+\sum_{i=1}^{N}\left(\tilde{G}^{i}+G_{i-1}\right)^{2}\right].
\end{aligned} \tag{16}
$$

We can now prove Theorem 2 in the following way. 1) If $m_{i} \geqq 0$ for all $i=0,1, \ldots, N$ then taking $h \leqq h_{m}^{\prime}$ where $h_{m}^{\prime}$ is given by (4), the right hand side of (16) is negative except for $e_{j-1}$ since all

$$
F_{i}=G_{i}\left[\frac{p_{i}+q_{i}}{2 E}+\varphi^{\prime}\left(r_{i}\right)\right]+\frac{h G_{i}^{2}}{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)
$$

$$
\tilde{F}^{i}=\tilde{G}^{i}\left[\frac{\tilde{p}^{i}+\tilde{q}^{i}}{2 E}+\varphi^{\prime}\left(\tilde{r}^{i}\right)\right]+\frac{h\left(\tilde{G}^{i}\right)^{2}}{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)
$$

are non positive and thus

$$
e^{j} \leqq e_{j-1} \quad \text { if } \quad h \leqq h_{m}^{\prime} \quad \text { and } \quad m_{i} \geqq 0, \quad i=0, \ldots, N.
$$

Theorem 2 of [1] consisted only from this first part since there $\sigma_{R}(\varepsilon)$ was assumed monotone which implied $m_{i} \geqq 0$. 2) If $m_{i}<0$ for some $i \in\{0,1, \ldots, N\}$ then

$$
-\lambda_{i}\left(\tilde{G}^{i}+G_{i}\right)^{2} m_{i} \leqq-2\left[\left(\tilde{G}^{i}\right)^{2}+G_{i}^{2}\right] m_{i}
$$

and for those $i$ we have

$$
\begin{aligned}
& \frac{h}{4}\left\{G_{i}\left[\frac{p_{i}+q_{i}}{2 E}+\varphi^{\prime}\left(r_{i}\right)\right]+\frac{h G_{i}^{2}}{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)+\tilde{G}^{i}\left[\frac{\tilde{p}^{i}+\tilde{q}^{i}}{2 E}+\varphi^{\prime}\left(\tilde{r}^{i}\right)\right]+\frac{h\left(\tilde{G}^{i}\right)^{2}}{2}\left(\frac{1}{E}+\tilde{m}_{i}\right)\right\}-\frac{h^{2}}{8} \lambda_{i}\left(\tilde{G}^{i}+G_{i}\right)^{2} m_{i} \\
& \leqq \frac{h}{4}\left\{G_{i}\left[\frac{p_{i}+q_{i}}{2 E}+\varphi^{\prime}\left(r_{i}\right)\right]+\frac{h G_{i}^{2}}{2}\left(\frac{1}{E}+\tilde{m}-2 m_{i}\right)+\tilde{G}^{i}\left[\frac{\tilde{p}^{i}+\tilde{q}^{i}}{2 E}+\varphi^{\prime}\left(\tilde{r}^{i}\right)\right]+\frac{h\left(\tilde{G}^{i}\right)^{2}}{2}\left(\frac{1}{E}+\tilde{m}-2 m_{i}\right)\right\} \leqq 0
\end{aligned}
$$

if we can choose $h>0$ such that

$$
A=\left[\frac{p+q}{2 E}+\varphi^{\prime}(r)\right] G+\frac{h}{2}\left(\frac{1}{E}+m^{*}-2 m\right) G^{2} \leqq 0.
$$

By $(1)_{2},(\mathrm{I} .4)$ and $(\mathrm{I} .17)$ we can write

$$
A \leqq k^{2}(\varepsilon, \sigma)\left[\sigma-\sigma_{R}(\varepsilon)\right]^{2}\left[-\frac{1}{(E+M) k}+\frac{h}{2}\left(\frac{1}{E}+m^{*}-2 m\right)\right].
$$

We use (I.19) and (I.5) to get
$$
-\frac{1}{(E+M) k}+\frac{h}{2}\left(\frac{1}{E}+m^{*}-2 m\right) \leqq \frac{1}{E+M}\left(-\frac{1}{k_{2}}+\frac{h}{2 E} \cdot \frac{E(E+M)+M\left(E-E_{3}\right)}{E-E_{3}}\right)
$$
which is negative if
$$
h \leqq \frac{2}{k_{2}} \cdot \frac{E\left(E-E_{3}\right)}{E(E+M)+M\left(E-E_{3}\right)}=h_{m}^{\prime \prime}.
$$

The proof is now complete since $h_{m}^{\prime \prime} \leqq h_{m}^{\prime}$.

Since $0<E_{3}/E<1$ and $M/E$ may be any positive number, the ratio $h_{m}^{\prime\prime}/h_{m}^{\prime}$ verifies
$$
\frac{1}{2}<\frac{1}{2-\left(E_{3} / E\right)}<\frac{h_{m}^{\prime \prime}}{h_{m}^{\prime}}=\frac{1+(M / E)}{1+2(M / E)-(M / E)\left(E_{3} / E\right)} \leqq 1 .\tag{17}
$$

The same results apply to the Cauchy problem if one assumes that the total energy of the initial data is finite.

## References
1 MIHAILESCU-SULICIU, M.; SULICIU, I.: On the method of characteristics in rate-type viscoelasticity. ZAMM 65 (1985), 479-486.
2 SULICIU, I.; ŞABAC, M.: Energy estimates in one-dimensional rate-type viscoplasticity. J. Math. Analysis & Appl. 131 (1988), 354-372.
3 FĂCIU, C.: An energetic study of some initial-boundary value problems in viscoplasticity. Ph. D. Thesis, INCREST, Bucharest, Romania 1989.
4 FĂCIU, C.; MIHAILESCU-SULICIU, M.: The energy in one-dimensional rate-type semilinear viscoelasticity. Int. J. Solids Structures 23 (1987), 1505-1520.
5 SULICIU, I.: On the description of the dynamics of phase transitions by means of rate-type constitutive equations. A model problem. Proceedings of the Second International Symposium of Plasticity and Its Current Applications, July 31-August 4, 1989, Mie University, Tsu, Japan, Pergamon Press, Oxford 1989.
6 ROZHDESTVENSKI, B. L.; YANENKO, N. N.: Systems of quasilinear equations and application to gas dynamics (Russian). Nauka, Moscow 1978.
7 MIHAILESCU-SULICIU, M.; SULICIU, I.: On tensile shock waves in rubberlike materials. ASME, J. Appl. Mech. 54 (1987), 498-502.
8 SULICIU, I.: On modelling phase transitions by means of rate-type constitutive equations. Int. J. Engineering Sci. (to appear).
9 MÜLLER, I.: On the size of hysterezis in pseudoelasticity. Cont. Mech., Thermodyn. 1 (1989), 1-18.
10 ACHENBACH, M.: A model for an alloy with shape memory. Int. J. Plasticity 5 (1989), 371-395.
11 ROWLINSON, J. S.: Liquid and liquid mixtures. Butterworth, London 1969, Chs. II, III.
12 KLUSHNIKOV, V. D.: Elementi opredeljajuschich sootnoschenii i ustoichivosti. Plastichnost i Rasrushenie Tverdich Tel. Nauka, Moskva 1988, pp. 85-95 (in Russian).

Received September 26, 1989, revised version May 24, 1990

Address: Dr. M. MIHAILESCU-SILICIU; Dr. I. SULICIU, Institute of Mathematics, Str. Academiei No. 14, Bucharest, Romania