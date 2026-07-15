Progress of Theoretical Physics, Vol. 58, No. 2, August 1977

# Longitudinal Correlation Function for an Anisotropic Ferromagnet

Yoshiro KONDO and Motoyuki TANAKA*

Department of Physics, Kawasaki Medical School, Kurashiki 701-01
*Department of Physics, Okayama University, Okayama 700

(Received January 17, 1977)

The longitudinal correlation function for the Heisenberg ferromagnet with the single-ion uniaxial anisotropy is derived from generating Green functions obtained in the random phase approximation. To obtain the result available to any values of the anisotropy constant $D$ a method without decoupling is developed for treatment of the higher-order Green functions associated with the anisotropy, then differential equations to determine the generating Green functions and the correlation function are lead. The correlation function actually obtained for $S=1$ is investigated in detail in the paramagnetic range of temperature and shown that it can be expressed in terms of the susceptibility in the form which does not involve $D$ explicitly for small and large values of $D$.

## § 1. Introduction

The correlation function for the longitudinal spin components, called simply the longitudinal correlation function, or its spatial Fourier transform is known to play an important role in studies of critical phenomena on magnetism. Many authors have investigated this function theoretically using various approximations and applied it to such dynamical problems as neutron scattering and magnetic resonance, and also to such static problems as magnetic susceptibility and specific heat. $^{1)\sim 3)}$

One of the methods to investigate the spin correlation functions is an approach using the double-time Green functions. By this method the correlation function for the transverse spin components can easily be derived from the corresponding transverse Green function obtained approximately with the use of the random phase decoupling. $^{4),5)}$ However, it is difficult to apply this method to derivation of the longitudinal correlation function in a similar manner to that used in derivation of the transverse one. Unless a suitable Green function is adopted or the method itself is modified appropriately we are inevitable to take account of the higher-order contributions beyond the simple random phase approximation. A few approaches have been proposed and some of them have succeeded in getting expression of the longitudinal correlation function for the isotropic Heisenberg spin system. $^{6)\sim 9)}$

The method using Green functions has also been applied to derivation of the longitudinal correlation function for an anisotropic Heisenberg spin system with the one-ion uniaxial anisotropy by several authors. $^{10)\sim 12)}$ In their treatments,

Longitudinal Correlation Function for an Anisotropic Ferromagnet 453

however, there arises another difficulty to decouple spin operators at the same lattice site involved in the higher-order Green function associated with the an- isotropy energy. This decoupling ignoring the kinematical interaction is understood as an additional approximation to the random phase approximation ignoring the correlation between different lattice sites in the higher-order Green functions. Some of the results obtained in these approximations have been shown unavailable to the case of strong anisotropy. The longitudinal correlation function obtained so far is solely based on these approximations.

Recently several attempts to treat the higher-order Green function in question without decoupling have been developed. $^{14) \sim 16)}$ We have proposed a method to obtain this Green function without decoupling by constructing a hierarchy of equa- tions for successive $2 S$ higher-order Green functions and terminating it in application of an identity relation for spin operators. $^{17) \sim 20)}$ The results thus obtained are sat isfactory over a whole intensity of the anisotropy. It has been shown that they agree with Lines' results obtained by an improved method to decouple the an- isotropy Green function in the case of weak anisotropy, $^{13)}$ and with molecular-fieldresults in the case of strong anisotropy. $^{17) \sim 22)}$ 

In this paper we make an application of our method to derivation of the longitudinal correlation function, which is defined by $\langle\hat{S}_{i}^{z} \hat{S}_{j}^{z}\rangle$ with $\hat{S}_{i}^{z}=S_{i}^{z}-\langle S^{z}\rangle$ , for the Heisenberg ferromagnet in the presence of the single-ion anisotropy. To simplify the description of the problem a formulation with the aid of generating functions is developed. In $\S 2$ the Green function to lead the generating function $\langle\exp (x S_{i}^{z}) \hat{S}_{j}^{z}\rangle$ , from which $\langle\hat{S}_{i}^{z} \hat{S}_{j}^{z}\rangle$ can be obtained, is derived in application of the random phase decoupling. Using this Green function, we derive in $\S 3$ the generating function as a solution of a differential equation, and show in $\S 4$ that this generating function leads the appropriate longitudinal correlation function which is investigated in detail for $S=1$ .

$\S 2$ . Green functions

We consider a spin system described by the Hamiltonian
$$\mathscr{H}=-\omega_{0} \sum_{i} S_{i}^{z}-J \sum_{i, j}\left(\boldsymbol{S}_{i} \cdot \boldsymbol{S}_{j}\right)-D \sum_{i}\left(S_{i}^{z}\right)^{2}.\qquad(1)$$

The first term is the Zeeman interaction of spins with an external field (ex- pressed in Frequency unit) applied along an easy axis of magnetization, the $z$ -axis, which is preferred by the last term, single-ion anisotropy energy $(D>0)$ . The second term describes the isotropic Heisenberg interaction between nearest neigh- bouring spins, $J$ being its exchange coupling constant. The restriction of the interaction to the nearest-neighbour one is merely due to simplification of notations used in this paper. Units are chosen as $\hbar=1$ throughout this paper.

To obtain a generating correlation function $\Lambda_{i, j}(x)=\langle\exp (x S_{i}^{z}) \hat{S}_{j}^{z}\rangle$ , from which the longitudinal correlation function $\langle\hat{S}_{i}^{z} \hat{S}_{j}^{z}\rangle$ we are interested in can be

derived by differentiating it with respect to $x$ and taking the limit $x \to 0$, we introduce a double-time Green function defined by⁴

$$
G_{i, l, j}\left(x, t-t^{\prime}\right)=\left\langle\left\langle c_{i}{ }^{+}(x, t) \hat{S}_{l}{ }^{z}(t) ; S_{j}{ }^{-}\left(t^{\prime}\right)\right\rangle\right\rangle,
\tag{2}
$$

where an operator $c_{i}{ }^{+}(x, t)$ is defined by

$$
c_{i}{ }^{+}(x, t)=\exp (i \mathcal{H} t) c_{i}{ }^{+}(x) \exp (-i \mathcal{H} t)
$$

with

$$
c_{i}{ }^{+}(x)=S_{i}{ }^{+} \exp \left(x S_{i}{ }^{z}\right),
\tag{3}
$$

and derive in this section its general formula with the aid of the standard equation-of-motion method.

The equation of motion for the Fourier transformed Green function $g_{i, l, j}(x, \omega)$ defined by

$$
\begin{aligned}
g_{i, l, j}(x, \omega) & =\left\langle\left\langle c_{i}{ }^{+}(x) \hat{S}_{l}{ }^{z} ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega} \\
& =\frac{1}{2 \pi} \int_{-\infty}^{\infty} G_{i, l, j}\left(x, t-t^{\prime}\right) e^{i \omega\left(t-t^{\prime}\right)} d\left(t-t^{\prime}\right)
\end{aligned}
\tag{4}
$$

can be written using the Hamiltonian (1) as follows:

$$
\begin{aligned}
& \left(\omega-\omega_{0}-D\right)\left\langle\left\langle c_{i}{ }^{+}(x) \hat{S}_{l}{ }^{z} ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega}=\frac{1}{2 \pi}\left\{\left\langle\left[c_{i}{ }^{+}(x), S_{i}{ }^{-}\right] \hat{S}_{l}{ }^{z}\right\rangle \delta_{i, j}-\left\langle c_{i}{ }^{+}(x) S_{l}{ }^{-}\right\rangle \delta_{l, j}\right. \\
& \quad+2 J \sum_{\delta}\left\langle\left\langle c_{i}{ }^{+}(x) S_{i+\delta}^{z} \hat{S}_{l}{ }^{z} ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega}-J \sum_{\delta}\left\langle\left\langle\left[c_{i}{ }^{+}(x) ; S_{i}{ }^{+}\right] S_{l+\delta}^{-} \hat{S}_{l}{ }^{z} ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega} \\
& \quad-J \sum_{\delta}\left\langle\left\langle\left[c_{i}{ }^{+}(x), S_{i}{ }^{-}\right] S_{i+\delta}^{+} \hat{S}_{l}{ }^{z} ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega}+J \sum_{\delta}\left\langle\left\langle c_{i}{ }^{+}(x)\left(S_{i+\delta}^{+} S_{l}{ }^{-}-S_{l}{ }^{+} S_{l+\delta}^{-}\right) ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega} \\
& \left.\quad+2 D\left\langle\left\langle c_{i}{ }^{+}(x) S_{i}{ }^{z} \hat{S}_{l}{ }^{z} ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega}\right\},
\end{aligned}
\tag{5}
$$

where $\delta_{i, j}$ is a Kronecker delta and the sum $\sum_{\delta}$ should be carried out over nearest-neighbouring spins, respectively. In order to solve this equation in the random phase approximation we neglect correlations between spins located on different lattice sites in the higher-order Green functions on the right-hand side of Eq. (5) and express them in terms of the lower-order Green functions. The equation of motion then becomes

$$
\begin{aligned}
& \left(\omega-\Omega_{0}\right) g_{i, l, j}(x, \omega)=\frac{1}{2 \pi}\left\{\left\langle\left[c_{i}{ }^{+}(x), S_{i}{ }^{-}\right] \hat{S}_{l}{ }^{z}\right\rangle \delta_{i, j}-\left\langle c_{i}{ }^{+}(x) S_{l}{ }^{-}\right\rangle \delta_{l, j}\right\} \\
& \quad+2 J \sum_{\delta}\left\langle\hat{S}_{i+\delta}^{z} \hat{S}_{l}{ }^{z}\right\rangle g_{i, j}(x, \omega)-J\left\langle\left[c^{+}(x), S^{-}\right]\right\rangle \sum_{\delta} g_{i+\delta, l, j}(0, \omega) \\
& \quad-J\left\langle\left[c_{i}{ }^{+}(x), S_{i}{ }^{-}\right] \hat{S}_{l}{ }^{z}\right\rangle \sum_{\delta} g_{i+\delta, j}(0, \omega)+J\left\langle c_{i}{ }^{+}(x) S_{l}{ }^{-}\right\rangle \sum_{\delta} g_{l+\delta, j}(0, \omega) \\
& \quad-J \sum_{\delta}\left\langle c_{i}{ }^{+}(x) S_{l+\delta}^{-}\right\rangle g_{l, j}(0, \omega)+2 D \frac{d}{d x} g_{i, l, j}(x, \omega),
\end{aligned}
\tag{6}
$$

where

$$
\Omega_{0}=\omega_{0}+2 J z\left\langle S^{z}\right\rangle
\tag{7}
$$

for the present lattice with $z$ nearest-neighbouring spins, and $g_{i, j}(x, \omega)$ is the Green function defined by
$$
g_{i, j}(x, \omega)=\left\langle\left\langle c_{i}{ }^{+}(x) ; S_{j}{ }^{-}\right\rangle\right\rangle_{\omega},
\tag{8}
$$
respectively. The first and the third term of the exchange interaction terms in Eq. (6) correspond to those terms corrected by Ishikawa and Oguchi $^{9)}$ to the equation used by Tahir-Kheli and Callen, $^{7)}$ and the present Green function results two more exchange terms, the last two terms of the exchange terms. Contributions of these two terms to the final result will later be discussed. In obtaining Eq. (6) we have retained spin operators at the same lattice point in the higher-order Green functions undecoupled to preserve the kinematical interaction of the system adequately. The forth term on the right-hand side of Eq. (5) is thus negligible in the present approximation because of the fact that $\left\langle\left[c_{i}{ }^{+}(x), S_{i}{ }^{+}\right]\right\rangle=0$ and $\left\langle S_{i+\delta}^{-} \hat{S}_{l}{ }^{z}\right\rangle=0$. The last term of Eq. (5), the anisotropy Green function, is treated without decoupling to take account of the contribution of the anisotropy term adequately for any values of $D$ and written in a form of differential with respect to $x$.

We have obtained the Green function $g_{i, j}(x, \omega)$ in Eq. (6) defined by Eq. (8) in the same approximation. $^{17), 20)}$ The result is summarized in terms of new notations as follows:
$$
g_{i, j}(x, \omega)=\frac{1}{N} \sum_{\boldsymbol{k}} \frac{\Delta(x, \omega)}{1+J(\boldsymbol{k}) \Delta(0, \omega)} e^{-i \boldsymbol{k} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right)},
\tag{9}
$$
where
$$
J(\boldsymbol{k})=J \sum_{\boldsymbol{\delta}} e^{i \boldsymbol{k} \cdot \boldsymbol{\delta}}.
\tag{10}
$$

In Eq. (9) $\Delta(x, \omega)$ is expressed in the form
$$
\Delta(x, \omega)=D_{x}(\omega) I(x),
\tag{11}
$$
where differential operator $D_{x}(\omega)$ operating to $I(x)$ is given by
$$
D_{x}(\omega)=\sum_{n=1}^{2 S} u^{(n)}(\omega)\left(\frac{d}{d x}-S+1\right)_{n-1}
\tag{12}
$$
by the use of
$$
u^{(n)}(\omega)=\left\{\prod_{m=1}^{n} \frac{1}{\omega-\omega_{m}}\right\}(2 D)^{n-1},
\tag{13}
$$
$$
\omega_{m}=\Omega_{0}+(2 S-2 m+1) D
\tag{14}
$$
and an operator $(\alpha)_{n}$ defined by
$$
(\alpha)_{n}=\alpha(\alpha+1)(\alpha+2) \cdots(\alpha+n-1)
\tag{15}
$$

for $n \neq 0$ and $(\alpha)_0=1$ for $n=0$, respectively. $I(x)$ is used to denote the canonical average:
$$
\begin{aligned}
I(x) & =\frac{1}{2 \pi}\left\langle\left[c^{+}(x), S^{-}\right]\right\rangle \\
& =\frac{1}{2 \pi}\left\{\left(e^{-x}-1\right) S(S+1)+\left(e^{-x}+1\right) \frac{d}{d x}-\left(e^{-x}-1\right) \frac{d^{2}}{d x^{2}}\right\} \Omega(x), \quad(16)
\end{aligned}
$$
where $\Omega(x)$ is a generating function to calculate $\left\langle\left(S^{z}\right)^{n}\right\rangle$ and defined by
$$
\Omega(x)=\left\langle e^{x S^{z}}\right\rangle. \quad(17)
$$

In deriving the last equation of Eq. (16) use has been made of a relation such that
$$
S^{+} S^{-}=S(S+1)+S^{z}-\left(S^{z}\right)^{2}. \quad(18)
$$

In order to solve Eq. (6) we rewrite it in terms of spatially Fourier-transformed components $G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega), G_{\boldsymbol{k}}(x, \omega), \chi_{\boldsymbol{k}}^{(1)}(x), \chi_{\boldsymbol{k}}^{(2)}(x)$ and $\chi_{\boldsymbol{k}}{ }^{z z}$ defined by
$$
g_{i, l, j}(x, \omega)=\left(\frac{1}{N}\right)^{2} \sum_{\boldsymbol{k}, \boldsymbol{q}} G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega) e^{-i \boldsymbol{k} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right)-i \boldsymbol{q} \cdot\left(\boldsymbol{r}_{l}-\boldsymbol{r}_{j}\right)},\quad(19)
$$

$$
g_{i, j}(x, \omega)=\frac{1}{N} \sum_{\boldsymbol{k}} G_{\boldsymbol{k}}(x, \omega) e^{-i \boldsymbol{k} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right)},\quad(20)
$$

$$
\left\langle\left[c_{i}^{+}(x), S_{l}^{-}\right] \hat{S}_{l}^{z}\right\rangle=\frac{1}{N} \sum_{\boldsymbol{k}} \chi_{\boldsymbol{k}}^{(1)}(x) e^{-i \boldsymbol{k} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{l}\right)},\quad(21)
$$

$$
\left\langle c_{i}^{+}(x) S_{l}^{-}\right\rangle=\frac{1}{N} \sum_{\boldsymbol{k}} \chi_{\boldsymbol{k}}^{(2)}(x) e^{-i \boldsymbol{k} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{l}\right)},\quad(22)
$$

$$
\left\langle\hat{S}_{i}{ }^{z} \hat{S}_{l}{ }^{z}\right\rangle=\frac{1}{N} \sum_{\boldsymbol{k}} \chi_{\boldsymbol{k}}{ }^{z z} e^{-i \boldsymbol{k} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{l}\right)},\quad(23)
$$

respectively. The equation to determine the component $G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)$ is then written as follows:
$$
2 D \frac{d}{d x} G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)-\left(\omega-\Omega_{0}\right) G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)=-F_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega).\quad(24)
$$

Here $F_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)$ is given by
$$
F_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)=I_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)-J(\boldsymbol{k}) I(x) G_{\boldsymbol{k}, \boldsymbol{q}}(0, \omega)\quad(25)
$$
by the use of
$$
I_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)=\frac{1}{2 \pi} \frac{\chi_{-\boldsymbol{q}}^{(1)}(x)-\{1+J(\boldsymbol{k}) \Delta(0, \omega)\} \chi_{\boldsymbol{k}}^{(2)}(x)+2 J(\boldsymbol{q}) \Delta(x, \omega) \chi_{\boldsymbol{k}}{ }^{z z}}{1+J(\boldsymbol{k}+\boldsymbol{q}) \Delta(0, \omega)}. \quad(26)
$$

In Eq. (26) we have used Eq. (9) for $G_{\boldsymbol{k}}(x, \omega)$. Inhomogeneous equation (24), thus its solution $G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)$, have the same forms as those for $G_{\boldsymbol{k}}(x, \omega) .{ }^{20)}$ It is then immediately found that $G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)$ can formally be written in a simple form

Longitudinal Correlation Function for an Anisotropic Ferromagnet 457

that
$$
G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)=D_{x}(\omega) F_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)
\tag{27}
$$
by the use of the differential operator $D_{x}(\omega)$ defined by Eq. (12) (see also Eq. (10) for $G_{\boldsymbol{k}}(x, \omega)$ in Ref. 20)). Since $G_{\boldsymbol{k}, \boldsymbol{q}}(0, \omega)$ involved in $F_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)$ can be determined from Eq. (27) by putting $x=0$, we obtain $G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)$ expressed in the form
$$
G_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)=\phi_{x}(\boldsymbol{k}+\boldsymbol{q}, \omega) \chi_{-\boldsymbol{q}}^{(1)}(x)+\phi_{x}(\boldsymbol{k}+\boldsymbol{q}, \omega) \nu_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega).
\tag{28}
$$

In the above $\phi_{x}(\boldsymbol{k}, \omega)$ is a differential operator defined by
$$
\phi_{x}(\boldsymbol{k}, \omega)=\frac{D_{x}(\omega)}{1+J(\boldsymbol{k}) \Delta(0, \omega)}=\sum_{n=1}^{2 S} v^{(n)}(\boldsymbol{k}, \omega)\left(\frac{d}{d x}-S+1\right)_{n-1}
\tag{29}
$$
with
$$
v^{(n)}(\boldsymbol{k}, \omega)=\frac{u^{(n)}(\omega)}{1+J(\boldsymbol{k}) \Delta(0, \omega)},
\tag{30}
$$
and $\nu_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)$ is given by
$$
\begin{aligned}
\nu_{\boldsymbol{k}, \boldsymbol{q}} & (x, \omega)=-J(\boldsymbol{k})\left[\phi_{x}(\boldsymbol{k}, \omega) \chi_{-\boldsymbol{q}}^{(1)}(x)\right]_{x=0} I(x) \\
& +2 J(\boldsymbol{q}) \chi_{-\boldsymbol{q}}^{z z}\left\{\Delta(x, \omega)-J(\boldsymbol{k})\left[\phi_{x}(\boldsymbol{k}, \omega) \Delta(x, \omega)\right]_{x=0} I(x)\right\} \\
& -(1+J(\boldsymbol{k}) \Delta(0, \omega))\left\{\chi_{\boldsymbol{k}}{ }^{(2)}(x)-J(\boldsymbol{k})\left[\phi_{x}(\boldsymbol{k}, \omega) \chi_{\boldsymbol{k}}{ }^{(2)}(x)\right]_{x=0} I(x)\right\}, \quad(31)
\end{aligned}
$$
respectively. In obtaining Eq. (28) we have replaced $\left[D_{x}(\omega) I(x)\right]_{x=0}$ by $\Delta(0, \omega)$.

## §3. Correlation function for general spin $S$

Using the Green function obtained in the preceding section we derive in this section the longitudinal spin-correlation function. A procedure to obtain the correlation function $\langle B A\rangle$ from the Green function $\langle\langle A ; B\rangle\rangle_{\omega}$ using the spectral theorem, $^{4)}$ which is written as
$$
\langle B A\rangle=\lim _{\varepsilon \rightarrow 0} i \int_{-\infty}^{\infty}\left\{\langle\langle A ; B\rangle\rangle_{\omega+i \varepsilon}-\langle\langle A ; B\rangle\rangle_{\omega-i \varepsilon}\right\} f(\omega) d \omega
\tag{32}
$$
with
$$
F(\omega)=\frac{1}{e^{\omega / k_{B} T}-1},
\tag{33}
$$
is now abbreviated as
$$
\langle B A\rangle=\mathscr{C}\left(\langle\langle A ; B\rangle\rangle_{\omega}\right),
\tag{34}
$$
using the corresponding operator $\mathscr{C}$. As is mentioned in the preceding section, it is necessary to get the correlation function $\Lambda_{i, j}(x)=\left\langle\exp \left(x S_{i}^{z}\right) \tilde{S}_{j}^{z}\right\rangle$ to generate the longitudinal correlation function. In order to get the equation satisfied by

$\Lambda_{i, j}(x)$ we first examine the operation $\mathscr{C}$ to Eq. (28) and find out a relation satisfied by the correlation function $\langle S_{i}^{-} c_{i}^{+}(x) \hat{S}_{j}^{z}\rangle$. Reminding Eq. (11) and the relation

$$
\chi_{\boldsymbol{k}}{ }^{(2)}=\left\{1+\mathscr{C}\left(\phi_{x}(\boldsymbol{k}, \omega)\right)\right\} I(x),\qquad(35)
$$

which can immediately be derived from

$$
\left\langle c_{i}{ }^{+}(x) S_{l}{ }^{-}\right\rangle=I(x) \delta_{i, l}+\mathscr{C}\left(G_{i, l}(x, \omega)\right),\qquad(36)
$$

using Eqs. (9), (11) and (29), one gets a relation

$$
\left\langle S_{i}^{-} c_{i}{ }^{+}(x) \hat{S}_{j}{ }^{z}\right\rangle=\phi_{x}\left\langle\left[c_{i}{ }^{+}(x), S_{i}{ }^{-}\right] \hat{S}_{j}{ }^{z}\right\rangle+\psi_{x}(i, j) I(x).\qquad(37)
$$

In the above equation differential operators $\phi_{x}$ and $\psi_{x}(i, j)$ are defined by

$$
\phi_{x}=\frac{1}{N} \sum_{\boldsymbol{k}} \phi_{x}(\boldsymbol{k})=\frac{1}{N} \sum_{\boldsymbol{k}} \mathscr{C}\left(\phi_{x}(\boldsymbol{k}, \omega)\right),\qquad(38)
$$

$$
\psi_{x}(i, j)=\frac{1}{N} \sum_{\boldsymbol{q}} e^{-i \boldsymbol{q} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right)} \psi_{x}(\boldsymbol{q}),\qquad(39)
$$

where

$$
\psi_{x}(\boldsymbol{q})=\mathscr{C}\left(\psi_{x}(\boldsymbol{q}, \omega)\right)=\mathscr{C}\left\{\frac{1}{N} \sum_{\boldsymbol{k}} \phi_{x}(\boldsymbol{k}+\boldsymbol{q}, \omega) \tilde{\nu}_{\boldsymbol{k}, \boldsymbol{q}}(x, \omega)\right\}\qquad(40)
$$

with

$$
\begin{aligned}
\tilde{\nu}_{\boldsymbol{k}, \boldsymbol{q}} & (x, \omega)=-J(\boldsymbol{k})\left[\phi_{x}(\boldsymbol{k}, \omega) \chi_{-\boldsymbol{q}}^{(1)}(x)\right]_{x=0} \\
& +2 J(\boldsymbol{q}) \chi_{-\boldsymbol{q}}^{z z}\left\{D_{x}(\omega)-J(\boldsymbol{k})\left[\phi_{x}(\boldsymbol{k}, \omega) \Delta(x, \omega)\right]_{x=0}\right\} \\
& -\left\{1+J(\boldsymbol{k}) \Delta(0, \omega)\right\}\left\{1+\phi_{x}(\boldsymbol{k})-J(\boldsymbol{k})\left[D_{x}(\omega)\left(1+\phi_{x}(\boldsymbol{k})\right) I(x)\right]_{x=0}\right\}, \quad(41)
\end{aligned}
$$

respectively. We now come to set up the equation to determine $\Lambda_{i, j}(x)$ from Eq. (37). Using Eqs. (16) and (18) it can readily be found in the form

$$
\left\{\frac{d^{2}}{d x^{2}}+\frac{d}{d x}-S(S+1)\right\} \tilde{\Lambda}_{i, j}(x)=0,\qquad(42)
$$

where

$$
\tilde{\Lambda}_{i, j}(x)=\left\{1+\phi_{x}-\phi_{x} e^{-x}\right\} \Lambda_{i, j}(x)-\psi_{x}(i, j)\left(e^{-x}-1\right) \Omega(x).\qquad(43)
$$

Thus we need another generating function $\Omega(x)$, which can similarly be obtained from the Green function $g_{i, i}(x, \omega)$ given by Eq. (9). Using Eqs. (11), (16), (29) and (38) one gets a relation

$$
\left\langle S^{-} S^{+} e^{x S^{z}}\right\rangle=\phi_{x} I(x),\qquad(44)
$$

from which it turns out that

$$
\left\{\frac{d^{2}}{d x^{2}}+\frac{d}{d x}-S(S+1)\right\} \tilde{\Omega}(x)=0,\qquad(45)
$$

where
$$
\tilde{\Omega}(x)=\left\{1+\phi_{x}-\phi_{x} e^{-x}\right\} \Omega(x).\qquad(46)
$$

It should be noticed that each of $\tilde{\Lambda}_{i, j}(x)$ and $\tilde{\Omega}(x)$ satisfies the same differential equation with respect to $x$, which must be solved under the following conditions:
$$
\left\{\prod_{m=-S}^{S}\left(\frac{d}{d x}-m\right)\right\} \Lambda_{i, j}(x)=0,\qquad(47)
$$

$$
\Lambda_{i, j}(0)=0,\qquad(48)
$$

$$
\left\{\prod_{m=-S}^{S}\left(\frac{d}{d x}-m\right)\right\} \Omega(x)=0\qquad(49)
$$
and
$$
\Omega(0)=1.\qquad(50)
$$

Equations (47) and (49) are resulted from an identity
$$
\prod_{m=-S}^{S}\left(S^{z}-m\right)=0.\qquad(51)
$$

A solution of Eq. (45), which satisfies conditions Eqs. (49) and (50), can be found as a sum of $(2 S+1)$ terms such that
$$
\Omega(x)=\sum_{m=0}^{2 S} \lambda_{m} e^{(m-S) x},\qquad(52)
$$
where coefficient $\lambda_{m}$ is given by
$$
\lambda_{m}=\left\{\prod_{n=1}^{m} \frac{1+\emptyset(n-S-1)}{\emptyset(n-S-1)}\right\} / \sum_{m=0}^{2 S}\left\{\prod_{n=1}^{m} \frac{1+\emptyset(n-S-1)}{\emptyset(n-S-1)}\right\}\qquad(53)
$$

(For $m=0$ we put $\prod_{n=1}^{m} f(n)=1$ ). In the above $\emptyset(m)$ is defined by
$$
\emptyset(m)=\left[\phi_{x} \cdot e^{m x}\right]_{x=0}=\sum_{n=1}^{2 S}\left\{\frac{1}{N} \sum_{\boldsymbol{k}} \mathscr{C}\left(v^{(n)}(\boldsymbol{k}, \omega)\right)(m-S-1)_{n-1}\right\}\qquad(54)
$$
with $(m-S-1)_{n-1}$ given by Eq. (15), thus $\emptyset(m)$ is a polynomial in $(2 S-1)$-order with respect to $m$. In the same way $\Lambda_{i, j}(x)$ satisfiying conditions (47) and (48) can be obtained using solution $\Omega(x)$ obtained in the above. The result can be expressed as
$$
\Lambda_{i, j}(x)=\sum_{m=0}^{2 S} c_{i j}^{(m)} e^{(-S+m) x},\qquad(55)
$$
where coefficient $c_{i j}^{(m)}$ is given by
$$
\begin{array}{r}
c_{i j}^{(m)}=\left\{\prod_{k=1}^{m} \frac{1+\emptyset(-S+k-1)}{\emptyset(-S+k-1)}\right\} c_{i j}^{(0)}-\sum_{n=1}^{m}\left\{\prod_{k=1}^{n-1} \frac{1+\emptyset(-S+m-n-k)}{\emptyset(-S+m-n-k)}\right\} \frac{A_{i j}^{(m-n)}}{\emptyset(-S+m-n)} \\
(56)
\end{array}
$$
for $m \neq 0$ and

$$
\chi_{\boldsymbol{q}}{ }^{z z}=\frac{\hat{\xi}(S) \frac{1}{N} \sum_{\boldsymbol{k}} f\left(\omega_{\boldsymbol{k}+\boldsymbol{q}}\right)}{1+\hat{\xi}(S) \frac{1}{N} \sum_{\boldsymbol{k}} 2(J(\boldsymbol{q})-J(\boldsymbol{k})) \frac{f\left(\omega_{\boldsymbol{k}+\boldsymbol{q}}\right)-f\left(\omega_{\boldsymbol{k}}\right)}{\omega_{\boldsymbol{k}+\boldsymbol{q}}-\omega_{\boldsymbol{k}}}},
$$

where $\hat{\xi}(S)$ is given by
$$
\xi(S)=\frac{\left\langle\left(S^{z}\right)^{2}\right\rangle-\left\langle S^{z}\right\rangle^{2}}{\emptyset(1+\emptyset)}=1-\frac{(2 S+1)^{2} \emptyset^{2 S}(1+\emptyset)^{2 S}}{\left[(1+\emptyset)^{2 S+1}-\emptyset^{2 S+1}\right]^{2}}.
$$

For $S=1 / 2$ one finds that $\xi(1 / 2)=1 /(1+\emptyset)^{2}=4\left\langle S^{z}\right\rangle^{2}$ and Eq. (66) coincides for small $\boldsymbol{q}$ with the result obtained previously by Kawasaki and Mori for a somewhat different function $(1 / \beta) \int_{0}^{\beta} d \lambda\left\langle S_{\boldsymbol{q}}{ }^{z}(\lambda) S_{-\boldsymbol{q}}^{z}\right\rangle$, which becomes identical with $\chi_{\boldsymbol{q}}{ }^{z z}$ in the present paper for small $\boldsymbol{q}$.

## §5. Conclusion

We have obtained the expression of the longitudinal correlation $\langle\hat{S}_{i}{ }^{z} \hat{S}_{j}{ }^{z}\rangle$ for the Heisenberg ferromagnetic system with the single-ion uniaxial anisotropy energy. To derive it we first get the Green function $\left\langle\left\langle S_{i}{ }^{+}(t) \exp \left(x S_{i}{ }^{z}(t)\right) \hat{S}_{i}{ }^{z}(t) ; S_{j}{ }^{-}\left(t^{\prime}\right)\right\rangle\right\rangle$ using the random phase decoupling and retaining higher-order Green functions associated with the anisotropy term undecoupled so that the result is available for any values of the anisotropy constant $D$ and gives an exact result in the limit of large $D$. Then a generating function $\Lambda_{i, j}(x)=\left\langle\exp \left(x S_{i}{ }^{z}\right) \hat{S}_{j}{ }^{z}\right\rangle$ to give $\langle\hat{S}_{i}{ }^{z} \hat{S}_{j}{ }^{z}\rangle$ is obtained as a solution of a differential equation with respect to $x$. The final expression of $\Lambda_{i, j}(x)$ is shown by Eq. (55) for general spin $S$, and $\langle\hat{S}_{i}{ }^{z} \hat{S}_{j}{ }^{z}\rangle$ or $\chi_{\boldsymbol{q}}{ }^{z z}$ for general spin $S$ is shown in Eq. (66) for the limiting case $D=0$. $\chi_{\boldsymbol{q}}{ }^{z z}$ for $S=1 / 2$ in this case coincides with that obtained by Ishikawa and Oguchi for small values of $\boldsymbol{q}$, who used the Green function $\left\langle\left\langle S_{i}{ }^{+}(t) ; \hat{S}_{i}{ }^{z}\left(t^{\prime}\right) S_{j}{ }^{-}\left(t^{\prime}\right)\right\rangle\right\rangle$ obtained from a different decoupling scheme from ours.

The effects of the anisotropy term to $\chi_{\boldsymbol{q}}{ }^{z z}$ are actually investigated for the case $S=1$. The expression of $\chi_{\boldsymbol{q}}{ }^{z z}$ for $S=1$ is found in Eq. (89), which is ascertained to give an exact result in the limiting case $J=0$ where our treatment of the hierarchy of the Green functions becomes exact. In the paramagnetic range of temperature we have shown that it is reduced to Eq. (92), which is written in the form that $k_{B} T /\left[\left(1 / \chi_{0}\right)+2(J(0)-J(\boldsymbol{q}))\right]$ for small and large values of $D$.

466
Y. Kondo and M. Tanaka

## Appendix
$\Psi_{\boldsymbol{q}}^{(i)}(m)$ in Eq. (88) is defined by

$$
\Psi_{\boldsymbol{q}}^{(i)}(m)=\frac{1}{N} \sum_{\boldsymbol{k}}\left[\Psi_{\boldsymbol{k}, \boldsymbol{q}}^{(i)}(\omega) \cdot e^{m x}\right]_{x=0},
$$

where $\Psi_{\boldsymbol{k}, \boldsymbol{q}}^{(i)}(\omega)$ is given by

$$
\begin{aligned}
\Psi_{\boldsymbol{k}, \boldsymbol{q}}^{(0)}(\omega)= & -\frac{\left(\omega-\Omega_{+}\right)\left(\omega-\Omega_{-}\right)}{\left(\omega-\omega_{1}\right)\left(\omega-\omega_{2}\right)}\left\{1+v^{(1)}+v^{(2)} \frac{d}{d x}\right\} \\
& +\frac{J(\boldsymbol{k})}{\left(\omega-\omega_{1}\right)\left(\omega-\omega_{2}\right)}\left\{2\left\langle S^{z}\right\rangle\left(\omega-\omega_{2}\right)\left(1+v^{(1)}\right)\right. \\
& \left.+\left(\langle Q\rangle-\left\langle S^{z}\right\rangle\right)\left[2 D\left(1+v^{(1)}-v^{(2)}\right)+\left(\omega-\omega_{2}\right) v^{(2)}\right]\right\},
\end{aligned}
$$

$$
\begin{aligned}
\Psi_{\boldsymbol{k}, \boldsymbol{q}}^{(1)}(\omega)= & -\frac{2 J(\boldsymbol{k})\left(\omega-\omega_{2}-D\right)}{\left(\omega-\Omega_{+}\right)\left(\omega-\Omega_{-}\right)}+\frac{2 J(\boldsymbol{q})}{\omega-\omega_{1}}\left\{1+\frac{2 D}{\omega-\omega_{2}} \cdot \frac{d}{d x}\right. \\
& \left.-\frac{2 J(\boldsymbol{k})\left(\omega-\omega_{2}\right)}{\left(\omega-\Omega_{+}\right)\left(\omega-\Omega_{-}\right)}\left[\left\langle S^{z}\right\rangle+\frac{2 D\left(\langle Q\rangle-\left\langle S^{z}\right\rangle\right)\left(\omega-\omega_{2}-D\right)}{\left(\omega-\omega_{2}\right)^{2}}\right]\right\},
\end{aligned}
$$

$$
\Psi_{\boldsymbol{k}, \boldsymbol{q}}^{(2)}(\omega)=-\frac{6 D}{\left(\omega-\Omega_{+}\right)\left(\omega-\Omega_{-}\right)}
$$

for $S=1$, respectively.

## References
1) W. Marshall and R. D. Lowde, Rep. Prog. Phys. 31 II (1968), 706.
2) H. Mori, 1965 Tokyo Summer Lectures in Theoretical Physics, edited by R. Kubo (Sho- kabo, Tokyo, 1966), p. 17.
3) M. E. Fisher, Rep. Prog. Phys. 30 (1967), 615.
4) V. L. Bonch-Bruevich and S. V. Tyablikov, The Green-Function Method in Statistical Mechanics (North-Holland Publishing Company, Amsterdam, 1962).
S. V. Tyablikov, Method in the Quantum Theory of Magnetism (Plenum Press, New York, 1967).
5) H. B. Callen, Phys. Rev. 130 (1963), 890.
6) K. Kawasaki and H. Mori, Prog. Theor. Phys. 28 (1962), 690.
7) R. A. Tahir-Kheli and H. B. Callen, Phys. Rev. 135 (1964), A679.
8) S. H. Liu, Phys. Rev. 139 (1965), A1522.
9) T. Ishikawa and T. Oguchi, Prog. Theor. Phys. 50 (1973), 807.
10) K. Tomita and M. Tanaka, Prog. Theor. Phys. 29 (1963), 528.
11) V. N. Kashcheev, Phys. Status Solidi 11 (1967), 371.
12) H. Tanaka and K. Tani, Prog. Theor. Phys. 41 (1969), 590.
13) M. E. Lines, Phys. Rev. 156 (1967), 534.
14) T. Murao and T. Matsubara, J. Phys. Soc. Japan 25 (1968), 352.
15) J. F. Devlin, Phys. Rev. B4 (1971), 136.
16) S. B. Haley and P. Erdös, Phys. Rev. B5 (1972), 1106.
17) M. Tanaka and Y. Kondo, J. Phys. Soc. Japan 33 (1972), 269.
18) M. Tanaka and Y. Kondo, Prog. Theor. Phys. 48 (1972), 1815.
19) M. Tanaka and Y. Kondo, J. Phys. Soc. Japan 34 (1973), 934.
20) Y. Kondo and M. Tanaka, Prog. Theor. Phys. 50 (1973), 708.
21) M. Tanaka, Y. Kondo and H. Kitaguchi, J. Phys. Soc. Japan 34 (1973), 267.
22) M. Tanaka and Y. Kondo, Prog. Theor. Phys. 50 (1973), 1422; Rep. Res. Lab. for SUR- FACE SCIENCE 4 (1973), 37.
