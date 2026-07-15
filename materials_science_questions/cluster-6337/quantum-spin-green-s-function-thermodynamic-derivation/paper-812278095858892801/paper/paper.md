# IMPURITY IN THE s-d MODEL

V. Čápek

Institute of Physics of the Charles University, Prague*)

A previously suggested model of an impurity in the s-d model of ferromagnetic semiconductors is treated using the method of moments. It is shown how the method may be reconciled with the requirement that the long range parameters (like magnetization) cannot enter the electronic spectrum.

## 1. INTRODUCTION

The problem of temperature dependence of impurity levels in magnetic semiconductors is of high importance for both optical and transport properties of these materials. Unfortunately, the attention devoted to the problem (and consequently the results) does not correspond to its significance. This fact corresponds to the complexity of the problem. Assuming as usual the intraatomic interaction of an electron with a core of magnetic ions to be described by the s-d interaction Hamiltonian

$$
H_{\text{s-d}}=-I \sum_{m \sigma \sigma^{\prime}}\left(S_{m} \sigma\right)_{\sigma \sigma^{\prime}} a_{m \sigma}^{+} a_{m \sigma^{\prime}}
$$

($I, S_{m}, \sigma$ and $a_{m \sigma}^{+}$being the parameter of the s-d coupling, magnetic ion spin at the site $m$, vector Pauli matrix and creation operator of an electron at the site $m$ with spin orientation $_{\sigma}$), it was soon recognized how dangerous it might be to rely upon the perturbation theory, namely when $I S \gg W$ ($S$ being the spin magnitude and $W$ is the relevant band width determined by the electron transfer integrals $t_{m n}$ between neighbouring sites) [1-3]. This may be easily comprehended realizing that the perturbation theory always leads to the dependence of electronic energies on the magnetization $\sim\langle S_{m}^{z}\rangle$ while (especially for a localized level) it is clear that the appearance of any long range parameter (like $\langle S_{m}^{z}\rangle$) in the electron energy is spurious [4-6].

In [5], a model of an electron at a single impurity level described by the Hamiltonian

$$
H=\varepsilon_{0} \sum_{\sigma} a_{\sigma}^{+} a_{\sigma}-I \sum_{m \sigma \sigma^{\prime}}\left|f_{m}\right|^{2}\left(S_{m} \sigma\right)_{\sigma \sigma^{\prime}} a_{\sigma}^{+} a_{\sigma^{\prime}}+H_{\text{d-d}}
$$

was suggested; $\varepsilon_{0}$ is the bare impurity level energy (which will be set zero from now on choosing $\varepsilon_{0}$ as zero of the energy scale), $f_{m}$ is a proper rigid envelope function and $a_{\sigma}^{+}$is the creation operator of an electron in the impurity state with the spin $\sigma$. The interaction between magnetic spins described by $H_{\text{d-d}}$ will not be specified here. We shall ignore $H_{\text{d-d}}$ everywhere (due to the assumed dominating magnitude of $I$

*) Ke Karlovu 5, 121 16 Praha 2, Czechoslovakia.

406
Czech. J. Phys. B 31 [1981]

V: Čápek: Impurity in the s—d model

as compared to d−d exchange integrals) and keep it just implicitly as a cause of the magnetic ordering. The latter is assumed ferromagnetic for simplicity here. The treatment of (2) in [5] based on a complicated decoupling in the Green function method leads to the conclusion that not the magnetization but the spin-spin correla- tions inside the area given by the envelope function $f_{m}$ of the impurity level determine the temperature dependence of the quasiparticle electron energy. On the other hand, the complete lack of $\langle S^{z}\rangle$ in the treatment was formally due to an unusual scheme based on full preserving of the rotational symmetry of the problem. In other words, no breaking of symmetry by an infinitesimal magnetic field (or averaging over its direction in space) was introduced. Then $\langle S^{z}\rangle=0$ by the definition even in the ferromagnetic case. Therefore, it is not apriori known to which extent the above mentioned conclusion is tributary to this scheme.

Here, we break the symmetry (as usual) by an infinitesimal magnetic field directed in parallel with the z-axis. Then $\langle S^{z}\rangle(\neq 0$ for $T<T_{C}$ where $T_{C}$ is the Curie tempera ture) appears explicitly and a special treatment is necessary to reproduce and justify the conclusions achieved in [5]. The method used is that of moments of the spectral function [7] first used in the s−d model by Nolting [8]. We show here how the method may be complemented by the requirement of the smooth behaviour of the electronic spectra in the vicinity of $T \approx T_{C}$ (observed in the experiment), unlike the temperature dependence of $\langle S^{z}\rangle(d\langle S^{z}\rangle/dT$ is singular at $T=T_{C})$.

## 2. MOMENTS OF SPECTRAL FUNCTION

The spectral function $A_{\sigma}(E)$ is introduced as

$$
(3)\qquad A_{\sigma}(E)=\int_{-\infty}^{+\infty} \mathrm{d} t\left\langle\left\{a_{\sigma}(t), a_{\sigma}^{+}\left(t^{\prime}\right)\right\}\right\rangle \exp \left[\frac{\mathrm{i}}{\hbar} E\left(t-t^{\prime}\right)\right].
$$

Here $\langle...\rangle$ means the quantum statistical averaging. In the low electron concentration limit assumed from now on here, (3) turns to

$$
(4)\qquad A_{\sigma}(E)=\int_{-\infty}^{+\infty} \mathrm{d} t\left\langle a_{\sigma}(t) a_{\sigma}^{+}\left(t^{\prime}\right)\right\rangle \exp \left[\frac{\mathrm{i}}{\hbar} E\left(t-t^{\prime}\right)\right],
$$

where the averaging is just over the electron-less eigenstates of the spin system. In general, $A_{\sigma}(E)$ in (3) enters the Zubarev retarded or advanced Green function [7,9]

$$
(5)\qquad \ll a_{\sigma}, a_{\sigma}^{+} ; \omega \pm \mathrm{i} \delta \gg=\int_{-\infty}^{+\infty} \frac{A_{\sigma}(E)}{\hbar(\omega \pm \mathrm{i} \delta)-E} \frac{\mathrm{d} E}{2 \pi \hbar}.
$$

The moments of the spectral function

$$
(6)\qquad M_{\sigma}^{(n)}=\int_{-\infty}^{+\infty} E^{n} A_{\sigma}(E) \frac{\mathrm{d} E}{2 \pi \hbar}, \quad n=0,1,2, \ldots
$$

Czech. J. Phys. B 31 [1981]

V. Čápek: Impurity in the s—d model

may be (for a given Hamiltonian) calculated exactly. From (4), we get

$$
\text { (7) } M_{\sigma}^{(n)}=\left\langle\left[[\ldots\left[a_{\sigma}, \underbrace{H], H] \ldots H}_{r \times}\right]\left[\underbrace{H,[H, \ldots\left[H, a_{\sigma}^{+}\right]] \ldots]}_{s \times}\right\rangle, \quad r+s=n.\right.\right.
$$

Using (2) and neglecting $H_{\text {d-d }}$ as mentioned above, we get

$$
\text { (8a) } \quad M_{\sigma}^{(0)}=1 \text {, }
$$

$$
\text { (8b) } \quad M_{\sigma}^{(1)}=-I \sigma \sum_{m}\left|f_{m}\right|^{2}\left\langle S_{m}^{z}\right\rangle, \quad \sigma= \pm 1 \text {, }
$$

$$
M_{\sigma}^{(2)}=I^{2} \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left[\left\langle S_{m} S_{n}\right\rangle-\sigma \delta_{m n}\left\langle S_{m}^{z}\right\rangle\right],
$$

$$
\text { (8c) } \quad S_{m} S_{n} \equiv S_{m}^{x} S_{n}^{x}+S_{m}^{y} S_{n}^{y}+S_{m}^{z} S_{n}^{z},
$$

$$
\begin{aligned}
M_{\sigma}^{(3)}= & -I^{3} \sum_{m n p}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2} \times \\
& \times\left[\sigma\left\langle\left(S_{m} S_{n}\right) S_{p}^{z}\right\rangle-\delta_{m n}\left\langle S_{m} S_{p}\right\rangle+\sigma \delta_{m n} \delta_{m p}\left\langle S_{m}^{z}\right\rangle\right],
\end{aligned}
$$

$$
\begin{aligned}
M_{\sigma}^{(4)}= & I^{4} \sum_{m n p q}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left|f_{q}\right|^{2}\left[\left\langle\left(S_{m} S_{n}\right)\left(S_{p} S_{q}\right)\right\rangle-\right. \\
& \left.-2 \sigma \delta_{m n}\left\langle S_{m}^{z}\left(S_{p} S_{q}\right)\right\rangle+\delta_{m n} \delta_{p q}\left\langle S_{m} S_{p}\right\rangle-\sigma \delta_{m n} \delta_{p q} \delta_{m p}\left\langle S_{m}^{z}\right\rangle\right]
\end{aligned}
$$

etc.

Now, as corresponds to the spirit of the method of moments, we shall try to fit the lowest moments (as many of them as possible) by an approximate function modeling $A_{\sigma}(E)$. In order to be as general as possible, we set

$$
\text { (9) } \quad A_{\sigma}(E)=\sum_{i=1}^{2} p_{i \sigma} f_{i}\left(E-\varepsilon_{i}\right) \text {. }
$$

Here $p_{i \sigma}$ are weights of quasiparticle peaks. We allow them to be $\sigma$-dependent as well as $\left\langle S^{z}\right\rangle$ dependent. (In fact, we shall always find the product $\sigma\left\langle S^{z}\right\rangle$.) In contrast to that, the functions $f_{i}(E)$ (as well as $\varepsilon_{i}$ ) describing the form (and sometimes even the position) of quasiparticle peaks are required to be $\left\langle S^{z}\right\rangle-$ independent - this is the above mentioned principle of independence of electronic spectra on $\left\langle S^{z}\right\rangle$. The fact that $f_{i}(E)$ do not differ for up and down spins does not mean an assumption about any similarity of $A_{\sigma}(E)$ for $\sigma=+1(\uparrow)$ and $\sigma=-1(\downarrow)$ (see e.g. a special case $p_{1 \uparrow}=p_{2 \downarrow}=0$ ).

Let us designate

$$
\text { (10) } \quad q_{i}^{(n)}=\int \mathrm{d} E f_{i}(E) E^{n}
$$

to be the $n$-th $(n=0,1,2 \ldots)$ moment of $f_{i}$. Due to arbitrariness in the choice of $p_{i \sigma}$ and $\varepsilon_{i}$, we may assume the identities

$$
\text { (11) } \quad q_{i}^{(0)}=1, \quad q_{i}^{(1)}=0, \quad i=1,2
$$

V. Čápek: Impurity in the s—d model

to apply. One should notice here that (though it would seem to be natural), $\varepsilon_{i}$ do not generally have a meaning of quasiparticle energies. Really, due to (11), $\varepsilon_{i}$ is just a centre of gravity of $f_{i}(E-\varepsilon_{i})$ which might differ from a position of a single sharp maximum of $f_{i}(E-\varepsilon_{i})$ (if any) quite appreciably. The fact that the summation in (9) extends over two contributions is compatible with the conclusion of the localiza-

![](./images/812278095858892801_1.jpg)

Fig. 1. A schematic plot of the spectral density (left) and two possible choices of $f_{i}(E-\varepsilon_{i})$'s in (9) (right) for the paramagnetic case as an illustration of a degree of arbitrariness in the momentum method. $f_{1}(E-\varepsilon_{1})=f_{2}(E-\varepsilon_{2})$ (both having two maxima; $\varepsilon_{i}$'s do not correspond to their position) - solid curve and $f_{1}(E-\varepsilon_{1}) \neq f_{2}(E-\varepsilon_{2})$ (each having one maximum; $\varepsilon_{i}$'s describing approximately their position) - dashed and dotted curves.

tion theorem $[10]^{1}$ ) according to which the spectrum should be well localized in two areas on the energy axis. However, even when requiring (as we shall do)

$$(12)\qquad f_{i}(x) \geqq 0$$

the functions $f_{i}(x)$ are not defined by (9) uniquely as they may overlap. This is one of the sources of non-uniqueness in the present approach which might be used to impose some (physically motivated) subsidiary conditions making the conclusions more lucid.

## 3. FITTING OF MOMENTS

We shall not try to find the form of $f_{i}(x)$ explicitly (except some limiting cases). Instead, we shall deduce the moments $q_{i}^{(n)}$ and discuss the physical information mediated by them. Having $q_{i}^{(n)}$ at our disposal, it is just a technical problem to construct a proper form of $f_{i}(x)$ (as long as some trivial requirements like $q_{i}^{(2)} \geqq 0$ are fulfilled - see below). Requiring the zeroth and first moments to be reproduced by (9), we get form (8a-b) and (11)

$$\text { (13) } p_{1 \sigma}+p_{2 \sigma}=1, \quad p_{1 \sigma} \varepsilon_{1}+p_{2 \sigma} \varepsilon_{2}=-I \sigma \sum_{m}\left|f_{m}\right|^{2}\left\langle S^{z}\right\rangle, \quad\left(\left\langle S^{z}\right\rangle \equiv\left\langle S_{m}^{z}\right\rangle\right) \text {. }$$

1) (the problem is in fact single-electronic, which justifies its use)

Czech. J. Phys. B 31 [1981]

### V. Čápek: Impurity in the $s-d$ model

Everywhere, the averaging is over electron-less eigenstates of the total Hamiltonian.
As long as $H_{d-d}$ in (2) is assumed translationally invariant, $\langle S_{m}^{z}\rangle(\equiv\langle S^{z}\rangle)$ is independent of $m$. From (13), we get

$$
(14) \quad p_{1 \sigma}=\frac{1}{\varepsilon_{1}-\varepsilon_{2}}\left[-\varepsilon_{2}-I \sigma\left\langle S^{z}\right\rangle \sum_{m}\left|f_{m}\right|^{2}\right],
$$

$$
p_{2 \sigma}=\frac{1}{\varepsilon_{1}-\varepsilon_{2}}\left[\begin{array}{c}
\varepsilon_{1}+I \sigma\left\langle S^{z}\right\rangle \sum_{m}\left|f_{m}\right|^{2}
\end{array}\right].
$$

Here $\varepsilon_{1}$ and $\varepsilon_{2}$ are yet arbitrary. Nevertheless, from (12) and the fact that

$$
(15) \quad A_{\sigma}(E) \geqq 0
$$

we get the first auxiliary condition limiting the choice of $\varepsilon_{i}$:

$$
(16) \quad \varepsilon_{1} \geqq|I|\left\langle S^{z}\right\rangle \sum_{m}\left|f_{m}\right|^{2},
$$

$$
\varepsilon_{2} \leqq-|I|\left\langle S^{z}\right\rangle \sum_{m}\left|f_{m}\right|^{2}.
$$

(Here, we have assumed $\varepsilon_{1} \geqq \varepsilon_{2}$ ). The conditions (16) are not in principle necessary as long as $f_{i}\left(E-\varepsilon_{i}\right)$ overlap. However, if (16) were not fulfilled, we could not be apriori sure that (15) applies for an approximate choice of (nonnegative) $f_{i}(x)$. Therefore, in view of the above mentioned arbitrariness involved, we shall assume (16) to apply. The right-hand sides of (16) are temperature dependent. So it may be for the left-hand sides though we shall not write down the temperature dependence of $\varepsilon_{i}$ explicitly. The only requirement (see above) is that $\varepsilon_{i}$'s do not behave like $\langle S^{z}\rangle$ when the Curie temperature is approached.

Requiring the second moment to be preserved, we get

$$
(17) \quad I^{2} \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left[\left\langle S_{m} S_{n}\right\rangle-\delta_{m n} \sigma\left\langle S^{z}\right\rangle\right]=p_{1 \sigma}\left[q_{1}^{(2)}+\varepsilon_{1}^{2}\right]+p_{2 \sigma}\left[q_{2}^{(2)}+\varepsilon_{2}^{2}\right].
$$

Separating terms which are $\langle S^{z}\rangle$-dependent, we get two equations

$$
(18a) \quad I^{2} \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle=-\varepsilon_{1} \varepsilon_{2}+\frac{q_{2}^{(2)} \varepsilon_{1}-q_{1}^{(2)} \varepsilon_{2}}{\varepsilon_{1}-\varepsilon_{2}},
$$

$$
(18b) \quad-I^{2} \sum_{m}\left|f_{m}\right|^{4}=I \sum_{m}\left|f_{m}\right|^{2}\left\{-\varepsilon_{1}-\varepsilon_{2}+\frac{q_{2}^{(2)}-q_{1}^{(2)}}{\varepsilon_{1}-\varepsilon_{2}}\right\}.
$$

The equations $(18 \mathrm{a}-\mathrm{b})$ are sufficient but not necessary for $(17)$ to apply. We have arrived at $(18 \mathrm{a}-\mathrm{b})$ starting from (17) using rather physical than mathematical arguments. From $(18 \mathrm{a}-\mathrm{b})$ we get

$$
(19) \quad q_{i}^{(2)}=-\varepsilon_{i}^{2}+I \varepsilon_{i} \frac{\sum_{m}\left|f_{m}\right|^{4}}{\sum_{m}\left|f_{m}\right|^{2}}+I^{2} \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle, \quad i=1,2.
$$

V. Čápek: Impurity in the $s$---$d$ model

Because of (12),
$$(20)\qquad q_{i}^{(2)} \geqq 0$$
which yields trivial limitations on $\varepsilon_{i}$. As combined with (16), it reads
$$
\begin{aligned}
(21 \mathrm{a}) \quad|I|\left\langle S^{z}\right\rangle \sum_{m}\left|f_{m}\right|^{2} & \leqq \varepsilon_{1} \leqq \\
& \leqq \frac{1}{2}\left[I \frac{\sum_{m}\left|f_{m}\right|^{4}}{\sum_{m}\left|f_{m}\right|^{2}}+|I|\left\{\left(\frac{\sum_{m}\left|f_{m}\right|^{4}}{\sum_{m}\left|f_{m}\right|^{2}}\right)^{2}+4 \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle\right\}^{1 / 2}\right],
\end{aligned}
$$

$$
\begin{aligned}
(21 b) & \frac{1}{2}\left[I \frac{\sum_{m}\left|f_{m}\right|^{4}}{\sum_{m}\left|f_{m}\right|^{2}}-|I|\left\{\left(\frac{\sum_{m}\left|f_{m}\right|^{4}}{\sum_{m}\left|f_{m}\right|^{2}}\right)^{2}+4 \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle\right\}^{1 / 2}\right] \leqq \\
& \leqq \varepsilon_{2} \leqq-|I|\left\langle S^{z}\right\rangle \sum_{m}\left|f_{m}\right|^{2}.
\end{aligned}
$$

In this way, one may reproduce even higher moments. For instance, for the third moments, we get
$$
\begin{aligned}
(22) \quad q_{i}^{(3)}= & I^{3} \sum_{m n}\left|f_{m}\right|^{4}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle+ \\
& +\varepsilon_{i} I^{2}\left[\sum_{m n p}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left\langle\left(S_{m} S_{n}\right) S_{p}^{z}\right\rangle+\sum_{m}\left|f_{m}\right|^{6}\left\langle S_{m}^{z}\right\rangle\right]\left[\sum_{m}\left|f_{m}\right|^{2}\left\langle S_{m}^{z}\right\rangle\right]^{-1}+ \\
& +2 \varepsilon_{i}^{3}-3 \varepsilon_{i}^{2} I \frac{\sum_{m}\left|f_{m}\right|^{4}}{\sum_{m}\left|f_{m}\right|^{2}}-3 \varepsilon_{i} I^{2} \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle, \quad i=1,2
\end{aligned}
$$
while for the fourth moments
$$
\begin{aligned}
(23) \quad q_{i}^{(4)}= & I^{4} \sum_{m n p q}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left|f_{q}\right|^{2}\left\{\left\langle\left(S_{m} S_{n}\right)\left(S_{p} S_{q}\right)\right\rangle+\delta_{m n} \delta_{p q}\left\langle\left(S_{m} S_{n}\right)\right\rangle\right\}- \\
& -I^{3} \varepsilon_{i}\left\{\left[\sum_{m n p}\left|f_{m}\right|^{4}\left|f_{p}\right|^{2}\left|f_{q}\right|^{2}\left(-2\left\langle S_{m}^{z}\left(S_{p} S_{q}\right)\right\rangle-\delta_{p q} \delta_{m p}\left\langle S_{m}^{z}\right\rangle\right)\right] ×\right. \\
& ×\left[\sum_{m}\left|f_{m}\right|^{2}\left\langle S_{m}^{z}\right\rangle\right]^{-1}+4 \sum_{m} \sum_{n}\left|f_{m}\right|^{4}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle+ \\
& +I^{2} \varepsilon_{i}^{2}\left\{6 \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle-4\left[\sum_{m n p}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left\langle\left(S_{m} S_{n}\right) S_{p}^{z}\right\rangle+\right.\right. \\
& \left.\left.+\sum_{n}\left|f_{n}\right|^{6}\left\langle S_{n}^{z}\right\rangle\right]\left[\sum_{m}\left|f_{m}\right|^{2}\left\langle S_{m}^{z}\right\rangle\right]^{-1}\right\}+6 I$$

The condition
$$(24)\qquad q_{i}^{(4)} \geqq\left(q_{i}^{(2)}\right)^{2}, \quad i=1,2$$

V. Čápek: Impurity in the s—d model

(following from our choice (11)) yields in principle an additional (to (21a−b)) limitating condition on $\varepsilon_{i}$. Higher moments may be treated in a similar manner.

4. DISCUSSION

First, we devote some attention to the case of a highly localized impurity state
$$(25)\qquad f_{m}=\delta_{m N}$$
(where $N$ is the location of impurity). In this case
$$(26)\qquad q_{i}^{(2)}=-\left[\varepsilon_{i}+I S\right]\left[\varepsilon_{i}-I(S+1)\right],$$
$$q_{i}^{(3)}=\left[\varepsilon_{i}+I S\right]\left[\varepsilon_{i}-I(S+1)\right]\left[2 \varepsilon_{i}-I\right],$$
$$q_{i}^{(4)}=\left[\varepsilon_{i}+I S\right]\left[\varepsilon_{i}-I(S+1)\right]\left[-3 \varepsilon_{i}^{2}+3 \varepsilon_{i} I-I^{2}\left(S^{2}+S+1\right)\right]$$
etc.

The conditions (21a−b) yield
$$(27)\qquad |I|\left\langle S^{z}\right\rangle \leqq \varepsilon_{1} \leqq \frac{1}{2}[I+|I|(2 S+1)],$$
$$\frac{1}{2}[I-|I|(2 S+1)] \leqq \varepsilon_{2} \leqq-|\dot{I}|\left\langle S^{z}\right\rangle.$$

One may check that then (24) is always satisfied. Choosing
$$(28)\qquad \varepsilon_{1}=\frac{1}{2}[I+|I|(2 S+1)]=\left\langle\begin{array}{l}
I(S+1), I>0 \\
-I S, I<0
\end{array}\right.$$

$$\varepsilon_{2}=\frac{1}{2}[I-|I|(2 S+1)]=\left\langle\begin{array}{l}
-I S, I>0 \\
I(S+1), I<0
\end{array}\right.$$
we set zero all the moments $q_{i}^{(n)}$ (except $q_{i}^{(0)}=1-$ see (11)).

Thus
$$(29)\qquad f_{i}(E)=\delta(E)$$
and (9) with (14) yield
$$(30)\qquad A_{\sigma}(E)=\frac{S+1+\sigma\left\langle S^{z}\right\rangle}{2 S+1} \delta(E+I S)+\frac{S-\sigma\left\langle S^{z}\right\rangle}{2 S+1} \delta(E-I(S+1)).$$

It is not difficult to show that (30) is the exact solution. Therefore, in contrast to the perturbational treatment, our approach is correct in the limit of the highly localized impurity state when $\varepsilon_{i}$ are chosen properly. As a by-product, we have got that in this limit, there is no red shift of the electronic spectra; just the weights $p_{i \sigma}$ of quasi particle energies $\varepsilon_{i}$ change with temperature.

In the opposite case of a localized impurity state with a large radius, the situation also simplifies as we are justified to neglect all higher than second powers of $f_{m}$.

### V. Čápek: Impurity in the $s-d$ model

Then
$$
(31)\qquad q_{i}^{(2)}=-\varepsilon_{i}^{2}+I^{2} \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle,
$$

$$
\begin{aligned}
q_{i}^{(3)}= & 2 \varepsilon_{i}^{3}+\varepsilon_{i} I^{2}\left[-3 \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle+\right. \\
& \left.+\left\{\sum_{m n p}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left\langle\left(S_{m} S_{n}\right) S_{p}^{z}\right\rangle\right\}\left\{\sum_{m}\left|f_{m}\right|^{2}\left\langle S_{m}^{z}\right\rangle\right\}^{-1}\right],
\end{aligned}
$$

$$
\begin{aligned}
q_{i}^{(4)}= & -3 \varepsilon_{i}^{4}+I^{2} \varepsilon_{i}^{2}\left[6 \sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle-\right. \\
& -4\left\{\sum_{m n p}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left\langle\left(S_{m} S_{n}\right) S_{p}^{z}\right\rangle\right\}\left\{\sum_{m}\left|f_{m}\right|^{2}\left\langle S_{m}^{z}\right\rangle\right\}^{-1}]+ \\
& +I^{4} \sum_{m n p q}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left|f_{q}\right|^{2}\left\langle\left(S_{m} S_{n}\right)\left(S_{p} S_{q}\right)\right\rangle
\end{aligned}
$$

etc.

The condition (24) may be then treated in a simple manner. However, its practical use is limited due to a complicated expression

$$
(32)\qquad \frac{\sum_{m n p}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left|f_{p}\right|^{2}\left\langle\left(S_{m} S_{n}\right) S_{p}^{z}\right\rangle}{\sum_{m}\left|f_{m}\right|^{2}\left\langle S_{m}^{z}\right\rangle}
$$

(which has to be calculated in the limit $\lim _{\mathscr{H} \rightarrow 0} \lim _{\Omega \rightarrow \infty}, \mathscr{H}$ and $\Omega$ being the external magnetic field and volume of the sample). The expression (32) appears first in $q_{i}^{(3)}$. Therefore, when trying to preserve more than the first three moments $(q_{i}^{(n)}, n=0,1,2)$, one encounters the problem of evaluating expressions like (32). One should notice that calculating (32) has in fact nothing to do with our electronic impurity problem; (32) is determined by the Heisenberg-like $H_{d-d}$ Hamiltonian of magnetic spins only.

Therefore, let us limit our attention just to $q_{i}^{(n)}, n=0,1,2$ moments. It is clear that $q_{i}^{(2)}$ disappear just when

$$
(33)\qquad \varepsilon_{1}=+|I|\left\{\sum_{m n}\left|f_{m}\right|^{2}\left|f_{n}\right|^{2}\left\langle S_{m} S_{n}\right\rangle\right\}^{1 / 2},
$$

$$
\varepsilon_{2}=-\varepsilon_{1}
$$

((33) satisfies (21a-b) in our limit of the large impurity radius). However, (33) is nothing but the result of [5]. Therefore, we have the conclusion that any kind of (approximate) theory preserving the first three $(n=0,1,2)$ moments $M_{\sigma}^{(n)}$ and yielding real quasiparticle energies (zero width of quasiparticle peaks in $A_{\sigma}(E)$, i.e. $q_{i}^{(2)}=0$ ) reproduces our result in [5] which has been got by just an approximate decoupling.

Czech. J. Phys. B 31 [1981]

### V: Čápek: Impurity in the s—d model

Finally, we turn our attention to the zero-temperature limit in the large impurity radius case. Then from (33),

$$
(34)\quad \left.\varepsilon_{2}\right|_{T=0}=-\left.\varepsilon_{1}\right|_{T=0}=-|I| S \sum_{m}\left|f_{m}\right|^{2}.
$$

Comparing with (A1) and (A7) (see Appendix) one may check that our approach with the choice (33) is exact in the zero temperature limit.

## APPENDIX

Here, we want to find some exact solutions of the Schrödinger equation with the Hamiltonian (2) corresponding to the case of an additional electron captured at the impurity with magnetic spins to be originally fully aligned ($T=0$). Designating the ground state of the magnetic spin subsystem (with spins along the $z$-axis) as $|0\rangle$, we have clearly an eigenstate

$$
(\mathrm{A}1)\quad a_{\uparrow}^{+}|0\rangle
$$

of (2) with the corresponding energy

$$
(\mathrm{A}2)\quad E_{1}=-I S \sum_{m}\left|f_{m}\right|^{2}.
$$

Another eigenstate is

$$
(\mathrm{A}3)\quad a_{\downarrow}^{+}|0\rangle+\sum_{p} x_{p} a_{\uparrow}^{+} S_{p}^{-}|0\rangle.
$$

Setting it in the Schrödinger equation and using (2) we get the set of equations

$$
(\mathrm{A}4)\quad \begin{aligned}
E & =I S \sum_{m}\left|f_{m}\right|^{2}\left[1-2 x_{m}\right], \\
E x_{p} & =-I\left|f_{p}\right|^{2}-I \sum_{m}\left|f_{m}\right|^{2}\left(S-\delta_{m p}\right) x_{p}
\end{aligned}
$$

which yields for energy

$$
(\mathrm{A}5)\quad E=I S \sum_{m}\left|f_{m}\right|^{2}+2 I^{2} S \sum_{m}\left|f_{m}\right|^{4} \frac{1}{E+I\left[S \sum_{q}\left|f_{q}\right|^{2}-\left|f_{m}\right|^{2}\right]}.
$$

For the zero impurity radius, $f_{m}=\delta_{m N}$ so that two roots for energy are obtained

$$
(\mathrm{A}6)\quad E_{1,2}=\left\langle\begin{array}{l}
-I S \\
I(S+1)
\end{array}\right.
$$

while for the large impurity radius (i.e. when neglecting formally the term with $|f_{m}|^{4}$ in (A5)) just one root remains

$$
(\mathrm{A}7)\quad E_{2}=I S \sum_{m}\left|f_{m}\right|^{2}.
$$

Received 3. 7. 1980.

Czech. J. Phys. B 31 [1981]

V. Čápek: Impurity in the s—d model

### References

[1] Nagaev E. L.: Phys. Status Solidi (b) 65 (1974) 11.

[2] Nagaev E. L.: Usp. Fiz. Nauk 117 (1975) 437.

[3] Nagaev E. L.: Physics of Magnetic Semiconductors, (in Russian), Nauka, Moscow, 1979.

[4] Nagaev E. L., Zilbervarg V. E.: Fiz. Tverd. Tela 11 (1975) 1261.

[5] Čápek V.: Phys. Status Solidi (b) 81 (1977) 571.

[6] Barvík I., Čápek V., Chvosta P.: J. Magn. & Magn. Mater. 14 (1979) 87.

[7] Kadanoff L. P., Baym G.: Quantum Statistical Mechanics, Benjamin, New York, 1962.

[8] Nolting W.: Phys. Status Solidi (b) 79 (1977) 573.

[9] Zubarev D. N.: Usp. Fiz. Nauk 71 (1960) 71.

[10] Drchal V., Velický B.: J. Phys. & Chem. Sol. 37 (1976) 655.