# AN ITERATIVE APPROACH TO ISING LATTICE MODELS: APPROXIMATE EXPRESSIONS FOR THE SUM OF $\delta$-FUNCTIONS INVESTIGATED

L. Šamaj

Institute of Physics of the Electro-Physical Research Centre, Slov. Acad. Sci.,
Dúbravská cesta 9, 842 28 Bratislava, Czechoslovakia

A special expression for the sum of $\delta$-functions implies a new graphical representation of thermodynamic quantities. The process consisting in the reduction of the number of points on an arbitrarily chosen reference spin in this graphical representation leads to the replacement of basic formulae for thermodynamic quantities by an iterative scheme. Simple assumptions on the form of correlations in the surrounding of the reference spin during the iterative procedure enable us to find equations for correlation functions. We are concerned especially with the influence of different approximate expressions for the sum of $\delta$-functions on the coefficients in resulting equations. It is observed that the dependences of these coefficients on a common parameter are similar in the form but shifted from the exact plot.

## I. INTRODUCTION

Besides rigorous solutions for certain types of one and two-dimensional Ising models [1, 2] there are known, in general, two ways to investigate Ising problems. Rigorous approaches are based on series expansions in powers of some small parameter [3-6]. When it is not possible to find a convenient parameter or the used one acquires large values, one utilizes closed-form expressions for quantities of interest to approximate them by physical assumptions and self-consistency require- ments [7], as it is performed within the mean-field theory (MFT), random-phase approximation (RPA), etc. Such theories cannot essentially take into account the effects of the short-range order. The correlated-effective-field (CEF) approximation [8] removes partly this deficiency by combining the ability of the MF approach to deal with long-range interactions with the ability to allow for correlations caused by short-range interactions [9]. Sometimes one finds the relation between the methods of series expansions and closed-form approximations and then they improve each other [10-13].

In the present paper we report a completely new approach to Ising spin models based on an iterative scheme for the statistical sum and correlation functions. The approximations are very simple and transparent in comparison with some of theories mentioned above.

The paper is outlined as follows. We start by introducing a new graphical re- presentation of thermodynamic quantities above the critical temperature, which originates from a special expression for the sum of $\delta$-functions. This graphical representation serves us to construct the iterative procedure of the calculation of thermodynamic quantities (section II). Provided that correlations in the surroundings

Czech. J. Phys. B 38 (1988)

L. Šamaj: Ising lattice models...

of the reference spin do not depend on its presence or absence, resulting equations for correlation functions are found in section III. Here the influence of approximate re-writings of the sum of $\delta$-functions is investigated.

## II. THE FORMALISM OF THE ITERATIVE METHOD

We study Ising spin systems defined on a regular d-dimensional lattice each site $u$ ($u = 1, ..., N$) of which is occupied by a spin (the respective spin variable $s_u$ takes one of the discrete values $+1, -1$). The spins localised at two different lattice sites $u$, $v$ interact by an exchange integral $J_{uv}$ depending on their distance only. The Hamiltonian of the spins is given by

$$
(2.1) \quad H = -\frac{1}{2} \sum_{u, v=1}^{N} ' s_u J_{uv} s_v
$$

where the prime means the summation with exclusion of the terms $u = v$.

In order to obtain thermodynamic properties of the spin system at the temperature $T$ it is necessary to calculate the statistical sum

$$
(2.2) \quad Z(A) = \lim_{N \to \infty} \sum_{\{s\}} \exp \left(\frac{1}{2} \sum_{u, v=1}^{N} ' s_u A_{uv} s_v\right)
$$

and the correlation function of spins at sites $i$ and $j$

$$
(2.3a) \quad g_{ij}(A) = \frac{G_{ij}(A)}{Z(A)},
$$

$$
(2.3b) \quad G_{ij}(A) = \lim_{N \to \infty} \sum_{\{s\}} s_i s_j \exp \left(\frac{1}{2} \sum_{u, v=1}^{N} ' s_u A_{uv} s_v\right)
$$

where $A_{uv} = J_{uv}/kT$ and the sum is over all possible spin configurations.

The summation over $2^N$ spin configurations can be transformed to the integration over continuous spin variables where the sums of corresponding $\delta$-functions occur. Further we shall use the identity

$$
(2.4a) \quad \delta(s_u + 1) + \delta(s_u - 1) = \lim_{m \to \infty} f_m(s_u),
$$

$$
(2.4b) \quad f_m(s_u) = \frac{2^{2m+1} m^m m!}{(2m)!} \sqrt{\left(\frac{m}{\pi}\right)} s_u^{2m} \exp \left(-m s_u^2\right).
$$

Each of the functions of the sequence $\{f_m(s_u)\}_{m=1}^{\infty}$ has two maximum peaks at the points $s_u = +1$, $s_u = -1$. As $m$ goes to infinity the peaks increase unlimitedly and $f_m(s_u)$ is equal to zero outside the mentioned points $s_u = +1$, $s_u = -1$. The normalization factor assures the normalization of the sum of $\delta$-functions.

The identity (2.4a, b) applied to the continuous version of (2.2) leads to the following expression for the partition sum

130
Czech. J. Phys. B 38 (1988)

$$
\begin{aligned}
&(2.5)\qquad Z(A)=\lim _{N, m \rightarrow \infty}\left[\frac{2^{2 m+1} m^{m} m!}{(2 m)!} \sqrt{\left(\frac{m}{\pi}\right)}\right]^{N} \times \\
& \times \int_{-\infty}^{\infty} \ldots \int_{-\infty}^{\infty} \mathrm{d} s_{1} \ldots \mathrm{d} s_{N} s_{1}^{2 m} \ldots s_{N}^{2 m} \exp \left(\frac{1}{2} \sum_{u, v=1}^{N} s_{u} A_{u v} s_{v}-m \sum_{u=1}^{N} s_{u}^{2}\right).
\end{aligned}
$$

Let us define the matrix $\bar{A}(m)$ by
$$(2.6)\qquad \bar{A}_{u v}(m)=-A_{u v}+2 m \delta_{u v}.$$

Its inverse matrix is found to be
$$\begin{aligned}
(2.7 \mathrm{a}) \quad \bar{A}_{u v}^{-1}(m) & =-\frac{1}{2 m}+O\left(\frac{1}{m^{2}}\right) \text { for } u=v, \\
(2.7 \mathrm{~b}) & =\frac{A_{u v}}{(2 m)^{2}}+O\left(\frac{1}{m^{3}}\right) \text { for } u \neq v
\end{aligned}$$
where the terms $O(1 / m^{2})$ and $O(1 / m^{3})$ are neglected in the limit $m \to \infty$. We apply the Wick's theorem [14] to the gaussian integral (2.5). It gives a new graphical representation of the statistical sum
$$(2.8 \mathrm{a})\qquad Z(A)=\lim _{N, m \rightarrow \infty}[C(m)]^{N} \times$$

![](./images/812281500329312258_1.jpg)

$$(2.8 \mathrm{~b})\qquad C(m)=\frac{2^{2 m+1} m^{m} m!}{(2 m)!}.$$

Here the sum goes over contributions of all diagrams constructed in the following way:
- each spin is represented by $2 m$ points,
- the diagram is constructed by connecting $2 m N$ points into $m N$ pairs by lines,
- the line between the points belonging to spins $u$ and $v$ represents the factor $\bar{A}_{u v}^{-1}(m)$,
- the contribution of a given diagram is the product of all factors occurring in it.

By adding one point to the spins at sites $i$ and $j$ in the graphical representation of $Z(A)$ we obtain $G_{i j}(A)$.

L. Šamaj: Ising lattice models...

By the "dressing" of lines [15] it can be shown that the proposed diagrammatic method can be transformed to the well-known high-temperature lattice decomposition holding in the region above the critical temperature, where the order parameter is equal to zero [16].

The graphical representation of $Z(A)$ (2.8) is only formal and cannot be used for the direct calculation. Let us try to rewrite the sum of $\delta$-functions for an arbitrarily chosen reference spin, 1 for example, by $f_{n}(s_{1})$ ($n$ can be finite) in (2.4). The diagrammatic formalism remains unchanged when the number of points belonging to spin 1 is $2n$, the normalization factor is $C(n)[C(m)]^{N-1}$ and the inverse matrix is modified little when compared to (2.7a, b)

$$
\begin{aligned}
\bar{A}_{1 v}^{-1}(m, n) & =\frac{1}{2 n}+O\left(\frac{1}{m}\right) & & \text { for } v=1, \\
& =\frac{A_{1 v}}{(2 m)(2 n)}+O\left(\frac{1}{m^{2}}\right) & & \text { for } v \neq 1.
\end{aligned}
$$

The choosing of the reference spin 1 containing $2n$ points ($n=1,2,...$) serves as a base of the procedure, which consists in the reduction of the point number on it. We define the functions $\bar{Z}(k), \bar{G}_{1 i}(k), \bar{G}_{i j}(k)$ for $(i \neq j) \neq 1$ obtained from $Z(A)$, $G_{1 i}(A), G_{i j}(A)$, respectively, by taking away $2(n-k)$ points from spin 1. The normalization factor $C(n)[C(m)]^{N-1}$ is forced to be unchanged. The relationships among these functions are found by the exclusion of the last point of the reference spin 1 in the graphical representation of $\bar{Z}(k)$

$$\bar{Z}(k)=\lim _{N, m \rightarrow \infty} C(n)[C(m)]^{N-1} \times$$

![](./images/812281500329312258_2.jpg)

for example. If we link this point with an arbitrary one of $(2k-1)$ points on spin 1 by the line $\bar{A}_{11}^{-1}(m, n)$, the contribution of all remaining pairings is $\bar{Z}(k-1)$. If we connect this point with an arbitrary one of $2m$ points belonging to spin $j \neq 1$ by the line $\bar{A}_{1 j}^{-1}(m, n)$, the contribution of the rest pairings is $\bar{G}_{1 j}(k-1)$ (the finite pair reduction of the point number on spin $j \neq 1$ does not change $\bar{G}_{1 j}(k-1)$ for $m \rightarrow \infty)$. Then we write

$$\text { (2.11a) } \bar{Z}(k)=(2 k-1) \bar{A}_{11}^{-1}(m, n) \bar{Z}(k-1)+\sum_{j \neq 1} 2 m \bar{A}_{1 j}^{-1}(m, n) \bar{G}_{1 j}(k-1).$$


L. Šamaj: Ising lattice models...

The procedure applied to the last point of spin 1 in the graphical representation of $\bar{G}_{1 i}(k)$ yields

$$
\begin{aligned}
(2.11 \mathrm{~b}) \quad \bar{G}_{1 i}(k)=2 k \bar{A}_{11}^{-1}(m, n) & \bar{G}_{1 i}(k-1)+(2 m+1) \bar{A}_{1 i}^{-1}(m, n) \bar{Z}(k)+ \\
& +\sum_{j \neq 1, i} 2 m \bar{A}_{1 j}^{-1}(m, n) \bar{G}_{j i}(k).
\end{aligned}
$$

Let $Z(A_{1 v}'=\sqrt(k / n) A_{1 v}), G_{1 i}(A_{1 v}'=\sqrt(k / n) A_{1 v}), G_{i j}(A_{1 v}'=\sqrt(k / n) A_{1 v})$ be the statistical quantities of the considered spin system, where the interaction between spin 1 and spins $v \neq 1$ is modified to $J_{1 v}'=\sqrt(k / n) J_{1 v}$. The re-writing of the sum of $\delta$-functions for the reference spin 1 by $f_{k}(s_{1})$ in continuous representations of $Z(A_{1 v}'=\sqrt(k / n) A_{1 v}), G_{1 i}(A_{1 v}'=\sqrt(k / n) A_{1 v}), G_{i j}(A_{1 v}' \doteq \sqrt(k / n) A_{1 v})$, leads to

$$
(2.12 \mathrm{a}) \quad Z\left(A_{1 v}^{\prime}=\sqrt{\frac{k}{n}} A_{1 v}\right) \approx \frac{C(k)}{C(n)}\left(\frac{n}{k}\right)^{k} \bar{Z}(k),
$$

$$
(2.12 \mathrm{~b}) \quad G_{1 i}\left(A_{1 v}^{\prime}=\sqrt{\frac{k}{n}} A_{1 v}\right) \approx \frac{C(k)}{C(n)}\left(\frac{n}{k}\right)^{k} \bar{G}_{1 i}(k),
$$

$$
(2.12 \mathrm{c}) \quad G_{i j}\left(A_{1 v}^{\prime}=\sqrt{\frac{k}{n}} A_{1 v}\right) \approx \frac{C(k)}{C(n)}\left(\frac{n}{k}\right)^{k} \bar{G}_{i j}(k).
$$

Finally, the correlation function $g_{1 i}(A)$ of spins $1, i$ is given by

$$
(2.13)\quad g_{1 i}(A)=\frac{\bar{G}_{1 i}(n)}{\bar{Z}(n)}
$$

where $\bar{Z}(n), \bar{G}_{1 i}(n)$ as functions of $\bar{Z}(0)$ are solutions of the iterative procedure

$$
(2.14 \mathrm{a}) \quad \bar{Z}(k)=\frac{2 k-1}{2 n} \bar{Z}(k-1)+\frac{1}{2 n} \sum_{j \neq 1} A_{i j} \bar{G}_{1 j}(k-1),
$$

$$
(2.14 \mathrm{~b}) \quad \bar{G}_{1 i}(k)=\frac{2 k}{2 n} \bar{G}_{1 i}(k-1)+\frac{1}{2 n}\left[A_{1 i} \bar{Z}(k)+\sum_{j \neq 1, i} A_{1 j} \bar{G}_{j i}(k)\right].
$$

Here $\bar{Z}(k), \bar{G}_{1 i}(k), \bar{G}_{i j}(k)$ are related to thermodynamic quantities of the above mentioned spin system with modified interactions via relations (2.12a-c).

## III. EQUATIONS FOR CORRELATIONS FUNCTIONS

The iterative procedure (2.13) and (2.14a, b) is equivalent to basic formulae (2.2), (2.3a, b) for statistical variables. Its advantage consists in finding quantities changing slowly and little during the iteration. Further we utilize the following limitations for the value of $\bar{G}_{i j}(k) / \bar{Z}(k)$:

- $\bar{G}_{i j}(k) / \bar{Z}(k)$ for $k \rightarrow n$ is equal to the correlation function of spins $i, j, g_{i j}$
- $\bar{G}_{i j}(k) / \bar{Z}(k)$ for $k \rightarrow 0$ is equal to the correlation function of spins $i, j$ in the

L. Šamaj: Ising lattice models...

absence of the reference spin 1, $g_{ij}(1)$ (spin 1 is excluded from the lattice Hamilto- nian).

In the case of high-dimensional spin systems the exclusion of one spin from the system does not change correlations in its surroundings essentially. That is why we take
$$
(3.1) \quad \frac{\bar{G}_{i j}(k)}{\bar{Z}(k)}=\max \left\{\frac{\bar{G}_{i j}(k)}{\bar{Z}(k)}\right\}_{k=0}^{n}=g_{i j}
$$
in the simplest approximation in (2.14). The resulting iterative scheme can be simpli- fied by the substitutions
$$
(3.2a) \quad \bar{Z}(k)=\frac{(2 k)!}{2^{k} k!} \frac{1}{(2 n)^{k}} \bar{Z}^{\prime}(k),
$$

$$
(3.2b) \quad \bar{G}_{1 i}(k)=\frac{[2(k+1)]!}{2^{k+1}(k+1)!} \frac{1}{(2 n)^{k+1}} \bar{G}^{\prime}(k)\left[A_{1 i}+\sum_{j \neq 1, i} A_{1 j} g_{j i}\right].
$$

Then the correlation function of spins 1, $i$ can be written as
$$
(3.3a) \quad g_{1 i}=L_{n}(\alpha)\left(A_{1 i}+\sum_{j \neq 1, i} A_{1 j} g_{j i}\right),
$$

$$
(3.3b) \quad L_{n}(\alpha)=\frac{2 n+1}{2 n} \frac{\bar{G}^{\prime}(n)}{\bar{Z}^{\prime}(n)},
$$

$$
(3.3c) \quad \alpha=\sum_{i \neq 1} A_{1 i}^{2}+\sum_{i, j \neq 1}^{\prime} A_{1 i} A_{1 j} g_{i j}
$$
where $\bar{Z}^{\prime}(n)$ and $\bar{G}^{\prime}(n)$, being the functions of $\bar{Z}^{\prime}(0)$, are calculated from the iterative scheme
$$
(3.3d) \quad \bar{Z}^{\prime}(k)=\bar{Z}^{\prime}(k-1)+\frac{\alpha}{2 n} \bar{G}^{\prime}(k-1),
$$

$$
(3.3e) \quad \bar{G}^{\prime}(k)=\frac{2 k}{2 k+1} \bar{G}^{\prime}(k-1)+\frac{1}{2 k+1} \bar{Z}^{\prime}(k).
$$

For $n=1$ it holds
$$
(3.4a) \quad \bar{G}^{\prime}(0)=\bar{Z}^{\prime}(0),
$$

$$
(3.4b) \quad \bar{Z}^{\prime}(1)=\left(1+\frac{1}{2} \alpha\right) \bar{Z}^{\prime}(0),
$$

$$
(3.4c) \quad \bar{G}^{\prime}(1)=\left(1+\frac{1}{6} \alpha\right) \bar{Z}^{\prime}(0),
$$

$$
(3.4d) \quad L_{1}(\alpha)=\frac{3}{2}\left(\frac{1+\frac{1}{6} \alpha}{1+\frac{1}{2} \alpha}\right).
$$

The plots of $L_{1}(\alpha)$ and $L_{2}(\alpha)$, obtained in analogy with (3.4), are represented by pointed and dashed lines in fig. 1, respectively. The special graphical method of the

L. Šamaj: Ising lattice models...

solution of the iterative scheme (3.3d, e) introduced in appendix implies

$$
\begin{align}
(3.5a)\quad L_{\infty}(\alpha) &= \frac{\tanh \sqrt{\alpha}}{\sqrt{\alpha}} \quad \text{for} \quad \alpha \geqq 0, \\
(3.5b)\quad &= \frac{\tan \sqrt{|\alpha|}}{\sqrt{|\alpha|}} \quad \text{for} \quad \alpha < 0.
\end{align}
$$

In fig. 1 we have plotted the coefficient $L_{\infty}(\alpha)$ by a solid line. One sees that the functions of the sequence $\{L_{n}(\alpha)\}_{n=1}^{\infty}$ depending on the common parameter $\alpha$ behave according

![](./images/812281500329312258_3.jpg)

Fig. 1. The plots of $L_{n}(\alpha)$ for $n=1,2$ and $n \to \infty$.

to the following rules:

- $L_{n}(\infty)=1 / 2 n$
- $L_{n}(0)=(2 n+1) / 2 n$
- $L_{n}(\alpha)$ goes to infinity at the certain negative point $\alpha_{n}$ from the interval $\left\langle-\left(\frac{1}{2} \pi\right)^{2},-2\right\rangle$
  $(\alpha_{1}=-2, \alpha_{\infty}=-\left(\frac{1}{2} \pi\right)^{2}).$

Comparing $L_{1}(\alpha), L_{2}(\alpha), L_{\infty}(\alpha)$ with each other we note that the dependences of coefficients $L_{n}$ in resulting equations for correlation functions on the parameter $\alpha$ are similar from the point of view of the form but shifted upwards from the exact

Czech. J. Phys. B 38 (1988)

plot $L_{\infty}(\alpha)$ by $1 / 2 n$. Values of $L_{n}(\alpha)$ ($n = 1, 2, ...$) are higher than the exact ones of $L_{\infty}(\alpha)$ because approximate re-writings of the sum of $\delta$-functions allow the spin variable to attain absolute values higher than one so that the spins are more correlated.

The equations for correlations functions in the limit $n \to \infty$

$$(3.6a) \quad g_{1 i}=\frac{\tanh \sqrt{ } \alpha}{\sqrt{ } \alpha}\left(A_{1 i}+\sum_{j \neq 1, i} A_{1 j} g_{j i}\right),$$

$$(3.6b) \quad \alpha=\sum_{i \neq 1} A_{1 i}^{2}+\sum_{i, j \neq 1}^{\prime} A_{1 i} A_{1 j} g_{i j}$$

($\alpha > 0$ is assumed for simplicity) give the critical point $A_{\mathrm{c}}$, i.e., the point at which the Fourier-transformation of the correlation function diverges at $\boldsymbol{k} = \boldsymbol{O}$, as the solution of the system

$$(3.7a) \quad \frac{\tanh \sqrt{ } \alpha_{\mathrm{c}}}{\sqrt{ } \alpha_{\mathrm{c}}} A_{\mathrm{c}}(\boldsymbol{O})=1,$$

$$(3.7b) \quad \left(\tanh \sqrt{ } \alpha_{\mathrm{c}}\right)^{2}=1-\left\{\int_{\mathrm{BZ}} \frac{\mathrm{d}^{d} k}{V_{\mathrm{BZ}}}\left[\frac{1}{1-A_{\mathrm{c}}(\boldsymbol{k}) / A_{\mathrm{c}}(\boldsymbol{O})}\right]\right\}^{-1},$$

$$(3.7c) \quad A(\boldsymbol{k})=\sum_{j \neq 1} A_{1 j} \exp \left[\mathrm{i} \boldsymbol{k} \cdot\left(\boldsymbol{r}_{j}-\boldsymbol{r}_{1}\right)\right]$$

where the integration is over the first Brillouin zone of the volume $V_{\mathrm{BZ}}$. In the case of the 3-dimensional cubic Ising model with nearest neighbour interactions the critical point $A_{\mathrm{c}} = 0.1907$ calculated within the proposed approximation is lower than $A_{\mathrm{c}} = 0.2217$ obtained by extrapolation of exact series expansions [3], but essentially higher than $A_{\mathrm{c}} = 0.1667$ from the MFT. The approximation fails in two dimensions, where no nontrivial critical point exists. Then more realistic forms of $\bar{G}_{i j}(k) / \bar{Z}(k)$ have to be considered.

## IV. CONCLUDING REMARKS

The aim of the present paper was to investigate the influence of approximate re-writings of the sum of $\delta$-functions by $f_{n}$ ($n = 1, 2, ...$) in (2.4) for an arbitrarily chosen reference spin on resulting equations for correlation functions. All analyses were based on the assumption that the correlations in the surroundings of the reference spin do not depend on its presence or absence. This approximation is suitable for high-dimensional systems, where the exclusion of one spin of the system does not change essentially correlations thereabouts of it. For low-dimensional systems (2-dimensional namely) more exact form of $\bar{G}_{i j}(k) / \bar{Z}(k)$ has to be taken into account. It can be shown that the expression

$$(4.1) \quad \bar{G}_{i j}(k)=\left[\frac{k}{n} g_{i j}+\left(1-\frac{k}{n}\right) g_{i j}(1)\right] \bar{Z}(k)$$

describes very well the small change of $\bar{G}_{i j}(k) / \bar{Z}(k)$ during the iteration procedure

L. Šamaj: Ising lattice models...

and leads to the correct lowest critical dimension $LCD=1$. The disadvantage of equations resulting from (4.1) consists in the fact that there occur two types of correlation functions-with and without the reference spin and so they must be solved perturbatively.

## APPENDIX: SOLUTION OF THE ITERATIVE SCHEME (3.3d, e) FOR $n \to \infty$

From (3.3e) it results

$$
\begin{aligned}
\text { (A.1) } \quad \bar{G}^{\prime}(k) & =\frac{1}{2 k+1} \bar{Z}^{\prime}(k)+\frac{1}{2 k+1} \frac{2 k}{2 k-1} \bar{Z}^{\prime}(k-1)+\ldots \\
& \ldots+\frac{1}{2 k+1} \frac{2 k}{2 k-1} \frac{2 k-2}{2 k-3} \ldots \frac{4}{3} \frac{2}{1} \bar{Z}^{\prime}(0).
\end{aligned}
$$

When put (A.1) into (3.3d) we have

$$
\begin{aligned}
\text { (A.2) } \bar{Z}^{\prime}(k) & =\left[1+\frac{\alpha}{2 n} \frac{1}{2 k-1}\right] \bar{Z}^{\prime}(k-1)+ \\
& +\frac{\alpha}{2 n}\left[\frac{1}{2 k-1} \frac{2 k-2}{2 k-3} \bar{Z}^{\prime}(k-2)+\ldots+\frac{1}{2 k-1} \frac{2 k-2}{2 k-3} \ldots \frac{2}{1} \bar{Z}^{\prime}(0)\right].
\end{aligned}
$$

Then the value of $\bar{Z}^{\prime}(n) / \bar{Z}^{\prime}(0)$ is specified in the following way:

- we construct the basic line with $n+1$ points $i=0,1, \ldots n$,
- the interaction line connecting two points represents the factor

![](./images/812281500329312258_4.jpg)

- the contribution of a given diagram is the product of factors of all lines forming it (1 for zero number of lines),
- $\bar{Z}^{\prime}(n) / \bar{Z}^{\prime}(0)$ is the sum over contributions of all diagrams created by arbitrary number of mutually non-crossing interaction lines.

Let us introduce the following auxiliary quantities:

$a(r ; i)=$ the sum of all diagrams containing $r$ lines to the right of the point $i$ provided that the first line goes out of it,
$\Gamma(r ; i)=$ the sum of all diagrams containing $r$ lines to the right of the point $i$.

Czech. J. Phys. B 38 (1988)

L. Šamaj: Ising lattice models...

They satisfy the recurrent relations

$$
\text { (A.3a) } \quad \Gamma(r ; i)=\sum_{j=i}^{n-r} a(r ; j),
$$

$$
\text { (A.3b) } \quad a(1 ; i)=\frac{1}{2 i+1} \frac{\alpha}{2 n}+\frac{2 i+2}{2 i+1} a(1 ; i+1) ; a(1 ; n)=0,
$$

$$
\begin{gathered}
\text { (A.3c) } \quad a(r ; i)=\frac{1}{2 i+1} \frac{\alpha}{2 n} \Gamma(r-1 ; i+1)+\frac{2 i+2}{2 i+1} a(r ; i+1) ; \\
a(r ; n-r+1)=0 \text { for } r>1
\end{gathered}
$$

from which $\Gamma(r ; 0)$ we are interested in is specified. We define $A_{p}(r)$ by

$$
\text { (A.4a) } \quad A_{p}(r)=\sum_{j=i}^{n-r} i^{p} a(r ; i),
$$

$$
\text { (A.4b) } \quad \Gamma(r ; 0)=A_{0}(r) \text {. }
$$

By simple sum operations in (A.3a-c) one gets

$$
\text { (A.5a) } \quad A_{p}(r)=\frac{1}{(p+1)(2 p+1)} A_{p+1}(r-1) \frac{\alpha}{2 n} \text { for } r>1,
$$

$$
\text { (A.5b) } \quad A_{p}(1)=\frac{1}{(p+1)(2 p+1)} n^{p+1} \frac{\alpha}{2 n} \text {. }
$$

Finally we write down

$$
\text { (A.6) } \quad \bar{Z}^{\prime}(n)=\sum_{r=0}^{n} A_{0}(r) \bar{Z}^{\prime}(0)=\sum_{r=0}^{\infty} \frac{1}{(2 r) !} \alpha^{r} \bar{Z}^{\prime}(0) \text {. }
$$

In order to obtain $\bar{G}^{\prime}(n)$, (A.1) is written in the form

$$
\text { (A.7a) } \quad \bar{G}^{\prime}(n)=\sum_{r=0}^{n} g_{r} \frac{1}{(2 r) !} \alpha^{r} \bar{Z}^{\prime}(0),
$$

$$
\begin{gathered}
\text { (A.7b) } \quad g_{r}=\frac{1}{2 n+1}\left[1+\frac{2 n}{2 n-1}\left(\frac{n-1}{n}\right)^{r}+\right. \\
\left.+\frac{2 n}{2 n-1} \frac{2 n-2}{2 n-3}\left(\frac{n-2}{n}\right)^{r}+\ldots+\frac{2 n}{2 n-1} \frac{2 n-2}{2 n-3} \cdots \frac{2}{1} 0^{r}\right],
\end{gathered}
$$

where the expression for $\bar{Z}^{\prime}(k)$,

$$
\text { (A.8) } \quad \bar{Z}^{\prime}(k)=\sum_{r=0}^{k}\left(\frac{k}{n}\right)^{r} \frac{1}{(2 r) !} \alpha^{r} \bar{Z}^{\prime}(0),
$$

derived in analogy with $\bar{Z}^{\prime}(n)$ was used. The sequence $\left\{b_{j}\right\}_{j=0}^{n}$ defined by

$$
\text { (A.9) } \quad b_{j+1}=b_{j} \frac{2 j+1}{2 j+2}, \quad b_{n}=\frac{1}{2 n+1}
$$


L. Šamaj: Ising lattice models...

yields
$$
\text{(A.10)} \quad g_{r}=\frac{1}{n^{r}} \sum_{j=0}^{n} b_{j} j^{r}=\frac{1}{2 r+1}
$$

so that
$$
\text{(A.11)} \quad \overline{G}^{\prime}(n)=\sum_{r=0}^{n} \frac{1}{(2 r+1)!} \alpha^{r} \overline{Z}^{\prime}(0),
$$

$$
\text{(A.12)} \quad L_{\infty}(\alpha)=\frac{\sum_{r=0}^{\infty} \frac{1}{(2 r+1)!} \alpha^{r}}{\sum_{r=0}^{\infty} \frac{1}{(2 r)!} \alpha^{r}}.
$$

I am grateful to Dr. E. Majerníková for support, illuminating discussions about critical phenomena and careful reading of the manuscript.

Received 15 December 1986

### References
[1] Onsager L.: Phys. Rev. 65 (1944) 117.
[2] Baxter R. J.: Exactly solved models in statistical mechanics. Academic Press, London, 1982.
[3] Sykes M. F., Gaunt D. S., Roberts P. D., Wyles J. A.: J. Phys. A 5 (1972) 640.
[4] Cottam M. G., Stinchcombe R. B.: J. Phys. C 3 (1970) 2283.
[5] Tokar V. I.: Phys. Lett. A 110 (1985) 453.
[6] Onyszkiewicz Z., Wierzbicki A.: Phys. Lett. A 116 (1986) 335.
[7] Burley D. M.: in Phase transitions and critical phenomena Vol. 2 (eds. C. Domb, M. S. Green). Academic Press, London, 1972.
[8] Lines M. E.: Phys. Rev. B 5 (1972) 3690.
[9] Smith S. R.: J. Phys. C 17 (1984) 41.
[10] Honmura R., Kaneyoshi T.: J. Phys. C 11 (1978) 1973.
[11] Honmura R., Kaneyoshi T.: J. Phys. C 12 (1979) 3979.
[12] Zhang H. I., Rajagopal A. K.: J. Phys. C 12 (1979) L227.
[13] Zhang H. I.: J. Phys. C 14 (1981) 57.
[14] Wilson K. G., Kogut J.: Phys. Rep. C 12 (1974) 75.
[15] Šamaj L.: Czech. J. Phys. B 38 (1988) 140 (the next article of this issue).
[16] Ziman J. M.: Models of disorder. Cambridge University Press, London, 1979.