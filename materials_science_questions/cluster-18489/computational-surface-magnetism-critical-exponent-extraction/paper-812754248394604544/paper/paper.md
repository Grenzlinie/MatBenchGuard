# Theory of light scattering off the surface of a Heisenberg antiferromagnet

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1978 J. Phys. C: Solid State Phys. 11 151

(http://iopscience.iop.org/0022-3719/11/1/025)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 142.66.3.42
This content was downloaded on 07/09/2015 at 12:24

Please note that terms and conditions apply.

# Theory of light scattering off the surface of a Heisenberg antiferromagnet

M G Cottam

Physics Department, University of Essex, Colchester CO4 3SQ, UK

Received 3 August 1977

Abstract. A theory is presented for one-magnon light scattering by reflection from the surface of a semi-infinite Heisenberg antiferromagnet at low temperatures $T \ll T_{\mathrm{N}}$. The calculations involve deriving expressions for the transverse spin-spin Green functions for the semi-infinite medium, and these results are then employed to obtain the light scattering cross-section. The theory includes an evaluation of the scattering contribution from surface spin-waves, as well as from the bulk spin-waves.

## 1. Introduction

In this paper we present calculations for the scattering of light off the surface of a Heisenberg antiferromagnet at low temperatures $T \ll T_{\mathrm{N}}$. This involves evaluating various correlation functions (or their corresponding Green functions) between any two spin operators in the semi-infinite antiferromagnetic medium, and these correlation functions may then be employed to deduce the cross-section for inelastic light scattering. The results derived in this way provide a description of scattering from bulk spin-wave modes and from the localised surface spin-wave modes.

Our general approach will be similar to corresponding calculations recently carried out for ferromagnetic systems (Cottam 1976a, b, henceforth referred to as I and II). It is of interest to extend the previous theoretical work to the antiferromagnetic case since most light scattering experiments so far carried out on magnetic materials apply to antiferromagnets. Furthermore for certain types of antiferromagnet the surface spin-wave energy at zero wavevector falls outside the continuum of values for the bulk spin-wave excitations, as first noted by Mills and Saslow (1968). Hence light scattering from surface spin-waves in these antiferromagnets would have a different frequency from light scattered from the bulk spin-wave modes, enabling the two types of contribution to be readily distinguished in an experiment. This is in contrast to the situation for a ferromagnet, where scattering from bulk and surface spin-waves occurs essentially at the same frequency (see II).

In this work we shall confine our discussion to antiferromagnets which have a body-centred tetragonal structure (e.g. $\mathrm{MnF}_{2}, \mathrm{FeF}_{2}$, etc.) and we assume a (001) surface. As can be seen from figure 1 the surface layer is then occupied by spins of one sublattice type, and the surface therefore has the effect of removing any equivalence between the symmetries of the two sublattices. Mills and Saslow (1968) and Dewames and Wolfram


![](./images/812754248394604544_1.jpg)

Figure 1. The (001) surface for an antiferromagnet with body-centred tetragonal structure.

(1969) have shown that this type of structure has an acoustic-type surface spin-wave excitation occurring within the energy gap below the bulk spin-wave energies. In contrast antiferromagnets with a simple cubic magnetic structure (e.g. $RbMnF_{3}$) and a (001) surface have equal numbers of spins of each sublattice type in the surface layer. This is a less interesting case to consider from the point of view of observing surface spin-waves by light scattering, since the acoustic surface spin-wave excitations (for $k=0$) are degenerate with the bulk excitations, and we shall not discuss this case here.

The outline of this paper is as follows. In $\S 2$ we derive a series of coupled equations for the spin-dependent Green functions of the semi-infinite medium, and their explicit solution is then given in $\S 3$. The formal results are then employed in $\S 4$ to calculate the intensity for light scattering from the surface of body-centred tetragonal antiferromagnets at $T \ll T_{\mathrm{N}}$. We consider the modification due to the surface of the bulk spin-wave scattering, as well as the additional scattering from localised surface spin-waves. The conclusions are given in $\S 5$.

## 2. Coupled equations for the spin-dependent Green functions

The antiferromagnet will be represented by a Heisenberg Hamiltonian of the form

$$
\mathscr{H}=\sum_{\boldsymbol{r}, \boldsymbol{r}^{\prime}} J\left(\boldsymbol{r}, \boldsymbol{r}^{\prime}\right) \boldsymbol{S}_{\boldsymbol{r}} \cdot \boldsymbol{S}_{\boldsymbol{r}^{\prime}}-g \mu_{\mathrm{B}} \sum_{\boldsymbol{r}}\left(H_{0}+H_{\mathrm{A}}(\boldsymbol{r})\right) S_{\boldsymbol{r}}^{z}-g \mu_{\mathrm{B}} \sum_{\boldsymbol{r}^{\prime}}\left(H_{0}-H_{\mathrm{A}}\left(\boldsymbol{r}^{\prime}\right)\right) S_{\boldsymbol{r}^{\prime}}^{z}
\tag{1}
$$

where $\boldsymbol{r}$ and $\boldsymbol{r}^{\prime}$ refer to sites on sublattice 1 (spins up) and sublattice 2 (spins down) respectively, $J(\boldsymbol{r}, \boldsymbol{r}^{\prime})$ is the exchange interaction, and the summations are over all sublattice sites in the semi-infinite medium. $H_{0}$ is an applied field in the $z$-direction (taken to be the (001) direction), and $H_{\mathrm{A}}(\boldsymbol{r})$ and $H_{\mathrm{A}}(\boldsymbol{r}^{\prime})$ are anisotropy fields (which may be position-dependent).

As mentioned in the Introduction we consider a body-centred tetragonal structure with a (001) surface as in figure 1. To simplify the calculation we shall assume that the only non-zero exchange interactions occur between nearest-neighbour sites on opposite sublattices, having a value $J_{1}$ if one of the spins is in the surface layer and the bulk value $J$ otherwise. Similarly we assume that the anisotropy field has its bulk value $H_{\mathrm{A}}$ except for spins in the surface layer where it has the value $H_{\mathrm{A}}(1)$. Therefore if we label the atomic layers parallel to the surface with a label $n$ (as in figure 1) with $n=1$ corresponding to the surface layer, we note that layer $n$ contains only spin-up sites (sublattice 1)

if $n$ is odd and only spin-down sites (sublattice 2) if $n$ is even. Also the exchange interaction couples sites in layer $n$ with sites in layers $(n+1)$ and $(n-1)$, except for $n=1$ where there is coupling only to layer 2.

In order to investigate the light scattering cross-section later in this paper, we shall be concerned with evaluating Green functions of the type

$$
\left\langle\left\langle S_{\boldsymbol{R}}^{+} ; S_{\boldsymbol{R}^{\prime}}^{-}\right\rangle\right\rangle_{\eta}=\frac{1}{2 \beta} \int_{-\beta}^{\beta} \exp (\mathrm{i} \eta t) \mathrm{d} t\left\langle T_{\mathrm{w}} S_{\boldsymbol{R}}^{+}(t) S_{\boldsymbol{R}^{\prime}}^{-}(0)\right\rangle
\tag{2}
$$

where $\boldsymbol{R}$ and $\boldsymbol{R}^{\prime}$ refer to any sites in the antiferromagnet, $\beta=1 / k_{\mathrm{B}} T, \mathrm{i} \eta=2 \pi m \mathrm{i} / \beta$ (for $m=$ integer) is an imaginary boson frequency which will eventually be analytically continued to a real frequency, and $\hat{T}_{\mathrm{w}}$ is the Wick time-ordering operating (see Abrikosov et al 1965). Since the system is invariant under translations parallel to the surface, we may define a two-dimensional Fourier transform by

$$
F_{n, n^{\prime}}(\boldsymbol{q}, \eta)=\frac{1}{N_{1}} \sum_{\boldsymbol{\rho}, \boldsymbol{\rho}^{\prime}} \exp \left\{-\mathrm{i} \boldsymbol{q} \cdot\left(\boldsymbol{\rho}-\boldsymbol{\rho}^{\prime}\right)\right\}\left\langle\left\langle S_{\boldsymbol{R}}^{+} ; S_{\boldsymbol{R}^{\prime}}^{-}\right\rangle\right\rangle_{\eta}
\tag{3}
$$

where we have written $\boldsymbol{R}=(\boldsymbol{\rho}, z)$ and $\boldsymbol{R}^{\prime}=\left(\boldsymbol{\rho}^{\prime}, z^{\prime}\right)$, so that $\boldsymbol{\rho}$ and $\boldsymbol{\rho}^{\prime}$ are two-dimensional vectors in the $x$-$y$ plane, and $\boldsymbol{q}=\left(q_{x}, q_{y}\right)$ is a two-dimensional wavevector. $N_{1}$ denotes the number of magnetic sites in each layer parallel to the surface and $n$ and $n^{\prime}$ are layer indices for sites $\boldsymbol{R}$ and $\boldsymbol{R}^{\prime}$ respectively.

It is also convenient to define the following summation for the exchange interactions:

$$
v_{n}(\boldsymbol{q})=\sum_{\boldsymbol{\delta}} J(\boldsymbol{R}, \boldsymbol{R}+\boldsymbol{\delta}) \exp \left(-\mathrm{i} \boldsymbol{q} \cdot \boldsymbol{\delta}_{\|}\right)
\tag{4}
$$

where $\boldsymbol{\delta}$ is a vector connecting any site $\boldsymbol{R}$ in layer $n$ with its nearest neighbours in layer $(n+1)$, and $\boldsymbol{\delta}_{\|}$is its two-dimensional projection parallel to the surface. From the assumptions made earlier it follows that $v_{n}(\boldsymbol{q})$ is independent of $n$ for $n \geqslant 2$ and will be denoted by $v_{\mathrm{B}}(\boldsymbol{q})$, whilst $v_{1}(\boldsymbol{q})$ may differ from the bulk value. We have

$$
v_{1}(\boldsymbol{q})=4 J_{1} \xi(\boldsymbol{q}), \quad v_{\mathrm{B}}(\boldsymbol{q})=4 J \xi(\boldsymbol{q})
\tag{5}
$$

$$
\xi(\boldsymbol{q})=\cos \left(\frac{1}{2} q_{x} a\right) \cos \left(\frac{1}{2} q_{y} a\right).
\tag{6}
$$

The calculation of $F_{n, n^{\prime}}(\boldsymbol{q}, \eta)$ will be carried out using a diagrammatic perturbation expansion in powers of the parameter $1 / z$, where $z$ is the number of spins interacting with any given spin. This may be done in a similar manner to the calculations in I for the semi-infinite ferromagnet, except that we now must take into account that there are two sublattices. The detailed calculations may be made using either the drone-fermion perturbation method (see Spencer 1968, Cottam and Stinchcombe 1970) for spin $S=\frac{1}{2}$ or the method due to Vaks et al (1968) which has the advantage of being applicable for general $S$. In a zeroth order $(1 / z)^{0}$ approximation (equivalent to molecular-field theory) we find that the Green function defined in (3) is equal to $F_{n, n^{\prime}}^{0}(\boldsymbol{q}, \eta)$ where

$$
F_{n, n^{\prime}}^{0}(\boldsymbol{q}, \eta)=\delta_{n, n^{\prime}} \frac{(-1)^{n} 2 S}{\gamma(n)-\mathrm{i} \eta}
\tag{7}
$$

where

$$
\gamma(n)=
\begin{cases}
g \mu_{\mathrm{B}} H+g \mu_{\mathrm{B}} H_{\mathrm{A}}(1)+S v_{1}(0), & (n=1) \\
g \mu_{\mathrm{B}} H+(-1)^{n-1}\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}+S v_{n-1}(0)+S v_{n}(0)\right], & (n \geqslant 2).
\end{cases}
\tag{8}
$$

The effect of spin fluctuations (leading to bulk and surface spin-wave excitations) can now be included by considering higher-order terms in the $1/z$ expansion. As in I for the semi-infinite ferromagnet, the contributions in next order $(1/z)^1$ are those involving a single momentum label $\boldsymbol{q}$, and this is exemplified in figure 2(a) by showing some of the simplest diagrammatic contributions to $F_{3,2}(\boldsymbol{q}, \eta)$. Here $F_{n, n}^0$ is represented by

![](./images/812754248394604544_2.jpg)

Figure 2. (a) Some diagrams contributing to $F_{3,2}(\boldsymbol{q}, \eta)$ in order $(1/z)^1$. (b) Recurrence relation satisfied by $F_{n, n'}(\boldsymbol{q}, \eta)$.

wavy lines. The general recurrence relation satisfied by the renormalised $F_{n, n'}(\boldsymbol{q}, \eta)$ is represented in figure 2(b). This may be expressed as

$$
F_{n, n^{\prime}}=F_{n, n}^{0} \delta_{n, n^{\prime}}-\frac{1}{2} F_{n, n}^{0}\left[v_{n}(\boldsymbol{q}) F_{n+1, n^{\prime}}+v_{n-1}(\boldsymbol{q})\left(1-\delta_{n, 1}\right) F_{n-1, n^{\prime}}\right]. \tag{9}
$$

The above relationship may be solved for $F_{n, n'}$ as follows. The equations for $n$ odd can be rewritten with the aid of (5)-(8) as

$$
F_{2 m-1, n^{\prime}}= \begin{cases}S\left[v_{1}(\boldsymbol{q}) F_{2, n^{\prime}}-2 \delta_{1, n^{\prime}}\right] /[\gamma(1)-\mathrm{i} \eta], & (m=1) \\ S\left[v_{\mathrm{B}}(\boldsymbol{q})\left(F_{2 m, n^{\prime}}+F_{2 m-2, n^{\prime}}\right)-2 \delta_{2 m-1, n^{\prime}}\right] /[\gamma(2 m-1)-\mathrm{i} \eta], & (m \geqslant 2)\end{cases}
$$

where $n=(2m-1)$ and $m$ is a positive integer. By now taking the case of $n$ even we obtain from (9) a further series of equations, from which all Green functions of the type $F_{2m-1,n'}$ may then be eliminated using (10). The resulting equations can eventually be expressed in matrix form as

$$
\boldsymbol{A f}=\boldsymbol{b} \tag{11}
$$

where $\boldsymbol{f}$ and $\boldsymbol{b}$ are infinite dimensional column matrices with elements given by (for integer $m$ taking values from 1 to $\infty$):

$$
f_{m}=F_{2 m, n^{\prime}} \tag{12}
$$

$$
b_{m}= \begin{cases}\frac{-1}{2 J \xi(\boldsymbol{q})}\left[\left(\frac{\Gamma-E}{\Gamma_{1}-E}\right)\left(\frac{J_{1}}{J}\right) \delta_{1, n^{\prime}}+\delta_{3, n^{\prime}}+\frac{(\Gamma+E)}{4 S J \xi(\boldsymbol{q})} \delta_{2, n^{\prime}}\right], & (m=1) \\ \frac{-1}{2 J \xi(\boldsymbol{q})}\left[\delta_{2 m-1, n^{\prime}}+\delta_{2 m+1, n^{\prime}}+\frac{(\Gamma-E)}{4 S J \xi(\boldsymbol{q})} \delta_{2 m, n^{\prime}}\right], & (m \geqslant 2).\end{cases}
$$

In (13) we have introduced new quantities $E$, $\Gamma$ and $\Gamma_1$ defined by
$$E=\mathrm{i}\eta - g\mu_{\mathrm{B}}H\tag{14}$$

$$\Gamma = g\mu_{\mathrm{B}}H_{\mathrm{A}}+2Sv_{\mathrm{B}}(0)=g\mu_{\mathrm{B}}H_{\mathrm{A}}+8SJ\tag{15}$$

$$\Gamma_{1}=g\mu_{\mathrm{B}}H_{\mathrm{A}}(1)+Sv_{1}(0)=g\mu_{\mathrm{B}}H_{\mathrm{A}}(1)+4SJ_{1}.\tag{16}$$

The infinite-dimensional matrix $\mathbf{A}$ can be expressed as
$$\mathbf{A}=\begin{pmatrix}
d+\Delta-1&0&\dots&\\
-1&d&-1&0&\dots&\\
0&-1&d&-1&0&\dots&\\
\cdot&\cdot&\cdot&\cdot&\cdot&\\
\cdot&\cdot&\cdot&\cdot&\cdot&\\
\cdot&\cdot&\cdot&\cdot&\cdot&
\end{pmatrix}\tag{17}$$
where
$$d=\frac{(\Gamma^{2}-E^{2})}{(4SJ\xi(\boldsymbol{q}))^{2}}-2\tag{18}$$

$$\Delta=1-\left(\frac{\Gamma-E}{\Gamma_{1}-E}\right)\left(\frac{J_{1}}{J}\right)^{2}-\frac{(J-J_{1})(\Gamma-E)}{4SJ^{2}\xi^{2}(\boldsymbol{q})}.\tag{19}$$

To obtain solutions for $F_{2m,n'}(=f_{m})$ from (11) we need to invert the matrix $\mathbf{A}$. This may simply be achieved by noting that (17) for $\mathbf{A}$ has the same general form (but with differently defined parameters) as the infinite matrix occurring in I for the semi-infinite ferromagnet.$\dagger$ Hence following the same approach as in I we obtain the formal solution
$$f=\frac{1}{(1+x\Delta)}\mathbf{LB}b\tag{20}$$
where the complex parameter $x$ is defined by
$$x+x^{-1}=d,\qquad |x|\leqslant1.\tag{21}$$

Matrix $\mathbf{B}$ is the inverse of $\mathbf{A}$ in the special case of $\Delta=0$, and has elements given by
$$B_{m,m'}=(x^{m+m'}-x^{|m-m'|})/(x-x^{-1})$$
whilst matrix $\mathbf{L}$ is
$$\mathbf{L}=\begin{pmatrix}
1&0&0&0&\\
-\Delta x^{2}&1+x\Delta&0&0&\dots&\\
-\Delta x^{3}&0&1+x\Delta&0&\dots&\\
-\Delta x^{4}&0&0&1+x\Delta&\dots&\\
&\vdots&\vdots&\vdots&
\end{pmatrix}.\tag{23}$$

On evaluating the right-hand side of (20) by ordinary matrix multiplication, and simplifying, results may be obtained for $F_{2m,n'}$ for any positive integral value of $n'$. The results for Green functions of the type $F_{2m-1,n'}$ may then be deduced using (10).

$\dagger$ Equation (17) can be regarded as being analogous to a special case of (32)-(34) of I, where $\Delta_1$ is replaced by $\Delta$ whilst $\Delta_2=\Delta_3=0$.

## 3. Results for the Green functions

### 3.1. Generating functions

The form of the expressions obtained for $F_{n,n'}(\boldsymbol{q},\eta)$ as described above depend on whether labels $n$ and $n'$ are odd or even. The results can be conveniently expressed in terms of generating functions $G_{ij}^{st}(\boldsymbol{q},\eta)$ defined by

$$
\left.
\begin{aligned}
G_{1,1}^{s,t}(\boldsymbol{q},\eta) &= \sum_{m=1}^{\infty} \sum_{m'=1}^{\infty} s^{m}t^{m'} F_{2m-1,2m'-1}(\boldsymbol{q},\eta) \\
G_{1,2}^{s,t}(\boldsymbol{q},\eta) &= \sum_{m=1}^{\infty} \sum_{m'=1}^{\infty} s^{m}t^{m'} F_{2m-1,2m'}(\boldsymbol{q},\eta) \\
G_{2,1}^{s,t}(\boldsymbol{q},\eta) &= \sum_{m=1}^{\infty} \sum_{m'=1}^{\infty} s^{m}t^{m'} F_{2m,2m'-1}(\boldsymbol{q},\eta) \\
G_{2,2}^{s,t}(\boldsymbol{q},\eta) &= \sum_{m=1}^{\infty} \sum_{m'=1}^{\infty} s^{m}t^{m'} F_{2m,2m'}(\boldsymbol{q},\eta).
\end{aligned}
\right\} \tag{24}
$$

The notation is such that subscripts 1 and 2 are sublattice labels for the spin operators appearing in the Green function $F_{n,n'}(\boldsymbol{q},\eta)$. We recall that sublattice 1 is associated with layer index $n$ odd, and sublattice 2 is associated with $n$ even. In (24) $s$ and $t$ are complex quantities sufficiently small in modulus for the double summations to be convergent.

The general results derived in $\S 2$ allow for the possibility that the surface exchange and anisotropy parameters ($J_1$ and $H_{\text{A}}(1)$) may differ from their respective bulk values $J$ and $H_{\text{A}}$. However, for simplicity we shall examine in detail in this section the special case of $J_1 = J$ and $H_{\text{A}}(1) = H_{\text{A}}$. It may then be shown using (20)-(23) that the generating functions defined in (24) are given by

$$
G_{1,1}^{s,t}(\boldsymbol{q},\eta) = \frac{-2S(1 + x)st}{(\Gamma - E)(1 - xs)(1 - xt)} \left[ \left( \frac{1 + xst}{1 - st} \right) - \frac{\Delta(1 + x)}{1 + x\Delta} \right] \tag{25}
$$

$$
G_{1,2}^{s,t}(\boldsymbol{q},\eta) = \frac{xst}{2J\breve{\zeta}(\boldsymbol{q})(1 - xs)(1 - xt)} \left[ \left( \frac{1 + s}{1 - st} \right) - \frac{\Delta(1 + x)}{1 + x\Delta} \right] \tag{26}
$$

$$
G_{2,1}^{s,t}(\boldsymbol{q},\eta) = G_{1,2}^{t,s}(\boldsymbol{q},\eta) \tag{27}
$$

$$
G_{2,2}^{s,t}(\boldsymbol{q},\eta) = \frac{-(\Gamma - E)xst}{8SJ^2\breve{\zeta}^2(\boldsymbol{q})(1 - xs)(1 - xt)} \left[ \left( \frac{1}{1 - st} \right) - \frac{x\Delta}{1 + x\Delta} \right]. \tag{28}
$$

The results for $F_{n,n'}(\boldsymbol{q},\eta)$ are readily obtainable from the appropriate generating function in (25)-(28). For example, $F_{2m,2m'}(\boldsymbol{q},\eta)$ is found from the coefficient of $s^mt^{m'}$ in the expansion of (28) to be

$$
F_{2m,2m'}(\boldsymbol{q},\eta) = \frac{-(\Gamma - E)}{8SJ^2\breve{\zeta}^2(\boldsymbol{q})} \left[ B_{m,m'} - \frac{\Delta x^{m + m'}}{1 + x\Delta} \right]. \tag{29}
$$

We next examine the poles of the Green function results represented by (25)-(28), and by this means we shall obtain expressions for the energies of the surface spin-waves and bulk spin-waves.

### 3.2. Bulk spin-wave modes

From (25)-(28) it can be seen that the poles of $G_{i,j}^{\text{s,t}}(\boldsymbol{q},\eta)$ for complex frequency $\mathrm{i}\eta$ correspond to $(1-xs)=0$, $(1-xt)=0$ or $(1+x\Delta)=0$. Parameter $x$ is related to $\mathrm{i}\eta$ according to equations (18) and (21).

We begin by considering the factors $(1-xs)$ and $(1-xt)$. To get the bulk-mode solution we follow the procedure of I and introduce cyclic boundary conditions over a macroscopically large distance in the $z$-direction (perpendicular to the surface). If we impose periodicity over $N_2$ layers, this implies that $s^{\mathrm{N_2}}=t^{\mathrm{N_2}}=1$, so that
$$
s = \exp(\mathrm{i}q_z c) \quad \text{with} \quad q_z = 2\pi n/N_2 c \tag{30}
$$
with a similar result for $t$, where $n$ is an integer. This gives the $z$-component of a wavevector, and in addition to the two-dimensional wavevector $\boldsymbol{q}=(q_x,q_y)$ we may define a three-dimensional wavevector $\boldsymbol{Q}=(q_x,q_y,q_z)$. The poles corresponding to $(1-xs)=0$ and therefore obtained by putting $x=\exp(-\mathrm{i}q_z c)$ in (21), leading to poles for $\mathrm{i}\eta$ at $g\mu_{\text{B}}H \pm E_{\text{B}}(\boldsymbol{Q})$ where
$$
E_{\text{B}}^2(\boldsymbol{Q}) = \Gamma^2 - \left[8SJ\xi(\boldsymbol{q})\cos(\frac{1}{2}q_z c)\right]^2. \tag{31}
$$

This corresponds to the usual formula for bulk spin-waves of wavevector $\boldsymbol{Q}$ in a body-centred tetragonal lattice. Likewise bulk spin-wave solutions are obtained from the condition $(1-xt)=0$.

### 3.3. Surface spin-wave modes

The surface spin-wave solutions arise from the factor $(1+x\Delta)$ in the denominator of (25)-(28). It follows using the definition of $\Delta$ in (19), and taking the case of $J_1=J$ and $H_{\text{A}}(1)=H_{\text{A}}$, that the corresponding value of $x$ is
$$
x = -\frac{1}{\Delta} = \frac{g\mu_{\text{B}}H_{\text{A}} + 4SJ - E}{4SJ}. \tag{32}
$$

Using this together with (12) and (21) it follows that the corresponding poles for $\mathrm{i}\eta$ are at $g\mu_{\text{B}}H + E_{\text{S}}^{\pm}(q)$, where
$$
\begin{aligned}
E_{\text{S}}^{\pm}(\boldsymbol{q}) = 2SJ[1 - \xi^2(\boldsymbol{q})] &\pm \{(g\mu_{\text{B}}H_{\text{A}} + 8SJ)(g\mu_{\text{B}}H_{\text{A}} + 4SJ[1 - \xi^2(\boldsymbol{q})]) \\
&+ 4S^2J^2[1 - \xi^2(\boldsymbol{q})]^2\}^{1/2}.
\end{aligned} \tag{33}
$$

However, the definition of $x$ in (21) requires that $|x| \leqslant 1$, and together with (32) this restricts the range of physical solutions for $E$ to
$$
g\mu_{\text{B}}H_{\text{A}} \leqslant E \leqslant (g\mu_{\text{B}}H_{\text{A}} + 8SJ). \tag{34}
$$

From this condition it follows that the solution $E_{\text{S}}^{-}(\boldsymbol{q})$, in (33) is unphysical (it would correspond to an excitation whose amplitude grows exponentially with distance from the surface). The solution $E_{\text{S}}^{+}(\boldsymbol{q})$ satisfies $|x| < 1$, which implies a localised surface mode, as can be seen from (29) where the term proportional to $1/(1+x\Delta)$ varies like $x^{m+m'}$, which decreases as $m$ or $m'$ become large. Hence for this model there is a single non-degenerate surface spin-wave excitation $E_{\text{S}}^{+}(q)$, in agreement with the expression found by Mills and Saslow (1968).

158
M G Cottam

In the case of zero wavevector the values of parameter $E$ for the bulk and surface spin-waves become (using (31) and (33))
$$
E_{\mathrm{B}}(0)=\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}\left(g \mu_{\mathrm{B}} H_{\mathrm{A}}+16 S J\right)\right]^{1 / 2}
$$

$$
E_{\mathrm{S}}^{+}(0)=\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}\left(g \mu_{\mathrm{B}} H_{\mathrm{A}}+8 S J\right)\right]^{1 / 2}. \tag{35}
$$

Therefore for weakly anisotropic antiferromagnets, where $g \mu_{\mathrm{B}} H_{\mathrm{A}} \ll 8 S J$, the ratio $E_{\mathrm{B}}(0) / E_{\mathrm{S}}^{+}(0)$ is approximately $\sqrt{ } 2$. Hence the surface spin-wave branch for $\boldsymbol{q}=0$ lies below, and is split off from, the continuum of bulk spin-wave excitations. This is in contrast to the ferromagnetic case discussed in I where the acoustic surface branch for $\boldsymbol{q}=0$ is degenerate with the lower edge of the bulk continuum.

It is now appropriate, as in I, to reformulate the expressions for the generating functions $G_{i, j}^{s, t}(\boldsymbol{q}, \eta)$ for the situation where cyclic boundary conditions are imposed over a macroscopically large distance in the $z$-direction. Here $s$ and $t$ have the form $s=\exp \left(\mathrm{i} q_{z} c\right)$ and $t=\exp \left(-\mathrm{i} q_{z}^{\prime} c\right)$ where $q_{z}$ and $q_{z}^{\prime}$ are $z$-components of a wavevector. The generating functions of (24) can then be recognised as a double Fourier transform of $F_{n, n^{\prime}}(\boldsymbol{q}, \eta)$ and may be re-expressed as

$$
G_{1,1}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \eta\right)=\sum_{m=1}^{\infty} \sum_{m^{\prime}=1}^{\infty} F_{2 m-1,2 m^{\prime}-1}(\boldsymbol{q}, \eta) \exp \left[\mathrm{i}\left(q_{z} z_{2 m-1}-q_{z}^{\prime} z_{2 m^{\prime}-1}\right)\right]
$$

$$
G_{1,2}\left(q_{z}, q_{z}^{\prime}, q ; \eta\right)=\sum_{m=1}^{\infty} \sum_{m^{\prime}=1}^{\infty} F_{2 m-1,2 m^{\prime}}(\boldsymbol{q}, \eta) \exp \left[\mathrm{i}\left(q_{z} z_{2 m-1}-q_{z}^{\prime} z_{2 m}\right)\right] \tag{36}
$$

with similar definitions for $G_{2.1}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \eta\right)$ and $G_{2.2}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \eta\right)$, where $z_{2 m-1}$ and $z_{2 m}$ denote respectively the distances from the surface of layer $(2 m-1)$ on sublattice 1 and layer $2 m$ on sublattice 2 , so that
$$
z_{2 m-1}=(m-1) c, \quad z_{2 m}=\left(m-\frac{1}{2}\right) c. \tag{37}
$$

Using (25)-(28), together with (36) and (37), it may be deduced that

$$
\begin{aligned}
& G_{1,1}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \eta\right)=\frac{-2 S N_{2}(\Gamma+E)}{\left\{E_{\mathrm{B}}^{2}(\boldsymbol{Q})-E^{2}\right\}} \delta_{q_{z}, q_{z}^{\prime}} \\
& +\frac{2 S(\Gamma+E)(\Delta+x)^{2}[4 S J \xi(\boldsymbol{q})]^{4} \exp \left[\mathrm{i}\left(q_{z}-q_{z}^{\prime}\right) c\right]\left[x-\exp \left(\mathrm{i} q_{z} c\right)\right]\left[x-\exp \left(-\mathrm{i} q_{z}^{\prime} c\right)\right]}{x^{2}\left(1-x^{2}\right) \Delta(\Delta-1)\left[E_{\mathrm{S}}^{+}(\boldsymbol{q})-E\right]\left[E_{\mathrm{S}}^{-}(\boldsymbol{q})-E\right]\left[E_{\mathrm{B}}^{2}(\boldsymbol{Q})-E^{2}\right]\left[E_{\mathrm{B}}^{2}\left(\boldsymbol{Q}^{\prime}\right)-E^{2}\right]}
\end{aligned} \tag{38}
$$

$$
\begin{aligned}
& G_{1,2}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \eta\right)=\frac{16 S^{2} N_{2} J \xi(\boldsymbol{q}) \cos \left(\frac{1}{2} q_{z} c\right)}{\left[E_{\mathrm{B}}^{2}(\boldsymbol{Q})-E^{2}\right]} \delta_{q_{z}, q_{z}^{\prime}} \\
& -\frac{2 S(\Delta+x)^{2}[4 S J \xi(\boldsymbol{q})]^{5} \exp \left[\mathrm{i}\left(\frac{1}{2} q_{z}^{\prime}-q_{z}\right) c\right]\left[x-\exp \left(\mathrm{i} q_{z} c\right)\right]\left[x-\exp \left(-\mathrm{i} q_{z}^{\prime} c\right)\right]}{x^{2}(1-x) \Delta(\Delta-1)\left[E_{\mathrm{S}}^{+}(\boldsymbol{q})-E\right]\left[E_{\mathrm{S}}^{-}(\boldsymbol{q})-E\right]\left[E_{\mathrm{B}}^{2}(\boldsymbol{Q})-E^{3}\right]\left[E_{\mathrm{B}}^{2}\left(\boldsymbol{Q}^{\prime}\right)-E^{2}\right]}
\end{aligned} \tag{39}
$$

$$
G_{2,1}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \eta\right)=G_{1,2}\left(-q_{z}^{\prime},-q_{z}, \boldsymbol{q} ; \eta\right) \tag{40}
$$

$$
\begin{aligned}
& G_{2,2}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \eta\right)=\frac{-2 S N_{2}(\Gamma-E)}{\left[E_{\mathrm{B}}^{2}(\boldsymbol{Q})-E^{2}\right]} \delta_{q_{z}, q_{z}^{\prime}} \\
& +\frac{2 S(\Gamma-E)(\Delta+x)^{2}[4 S J \xi(\boldsymbol{q})]^{4} \exp \left[\frac{1}{2} \mathrm{i}\left(q_{z}^{\prime}-q_{z}\right)\right]\left[x-\exp \left(\mathrm{i} q_{z} c\right)\right]\left[x-\exp \left(-\mathrm{i} q_{z}^{\prime} c\right)\right]}{x\left(1-x^{2}\right) \Delta(\Delta-1)\left[E_{\mathrm{S}}^{+}(\boldsymbol{q})-E\right]\left[E_{\mathrm{S}}^{-}(\boldsymbol{q})-E\right]\left[E_{\mathrm{B}}^{2}(\boldsymbol{Q})-E^{2}\right]\left[E_{\mathrm{B}}^{2}\left(\boldsymbol{Q}^{\prime}\right)-E^{2}\right]}
\end{aligned} \tag{41}
$$

where $\boldsymbol{Q}=(\boldsymbol{q}, q_{z}), \boldsymbol{Q}'=(\boldsymbol{q}, q_{z}')$, and the denominators have been expressed in terms of the quantities $E_{\mathrm{B}}(\boldsymbol{Q})$ and $E_{\mathrm{S}}^{\pm}(\boldsymbol{q})$ using the identities:

$$
\left(1-x \mathrm{e}^{\mathrm{i} q_{z} c}\right)\left(1-x \mathrm{e}^{-\mathrm{i} q_{z} c}\right)=\frac{x\left[E_{\mathrm{B}}^{2}(\boldsymbol{Q})-E^{2}\right]}{(4 S J \xi(\boldsymbol{q}))^{2}} \tag{42}
$$

$$
(1+x \Delta)=\frac{x \Delta(\Delta-1)}{(4 S J \xi(\boldsymbol{q}))^{2}(\Delta+x)}\left[E_{\mathrm{S}}^{+}(\boldsymbol{q})-E\right]\left[E_{\mathrm{S}}^{-}(\boldsymbol{q})-E\right]. \tag{43}
$$

In (38)-(41) the first term on the right-hand side of each expression represents the Green function for the infinite crystal, whilst the second term represents the additional effects of the surface and has poles at the bulk and surface spin-wave energies.

## 4. Light scattering results

We now make use of the Green function results derived in $\S 3$ to calculate the cross-section for scattering light from the surface of a semi-infinite antiferromagnet at low temperatures $T \ll T_{\mathrm{N}}$. We shall show that because of the perturbing effect of the surface the intensity due to scattering from the bulk spin-waves will be modified by comparison with previous calculations for infinite crystals (Moriya 1967, Loudon 1970, Cottam 1975), and furthermore there will be a contribution to the intensity due to scattering from the localised surface spin-waves. Additionally, it is necessary to apply transformations to relate the polarisation vectors outside the antiferromagnet to the polarisation vectors inside the medium.

### 4.1. The light scattering cross-section

The calculations will be carried out using a similar approach and notation to our previous calculations II for light scattering from the semi-infinite ferromagnet. For an infinite antiferromagnet the scattering cross-section is related, via a spin-dependent polarisability, to Green functions of the type $\left\langle\left\langle S_{i}^{+} \pm S_{j}^{+} ; S_{i}^{-} \pm S_{j}^{-}\right\rangle\right\rangle$(see Moriya 1967, Loudon 1970), where labels $i$ and $j$ denote sites on opposite sublattices. Generally there may be two types of contribution to the intensity, depending on whether the upper or lower signs are taken. The upper signs correspond to the two sublattices scattering in phase, and this is likely to be the dominant contribution for antiferromagnets of high symmetry. However, for systems where the symmetries of the two sublattices are not equivalent there may be a further contribution with the lower set of signs, and this corresponds to the sublattices scattering out of phase. It may readily be shown that these same type of Green functions contribute to the scattering cross-section for the semi-infinite antiferromagnet. In this case we consider light scattering by reflection from a surface, and analogous to equation (25) of II the differential cross-section $\mathrm{d}^{2} h / \mathrm{d} \Omega \mathrm{d} \omega_{\mathrm{s}}$ for scattering light of incident frequency $\omega_{\mathrm{i}}$ into a solid angle $\mathrm{d} \Omega$ with scattered frequency $\omega_{\mathrm{s}}$ is given by

$$
\begin{aligned}
\frac{\mathrm{d}^{2} h}{\mathrm{~d} \Omega \mathrm{d} \omega_{\mathrm{s}}}= & \frac{B^{ \pm}\left(\omega_{\mathrm{s}}\right)}{N_{2}^{2}} \sum_{q_{z}, q_{z}^{\prime}} \frac{D\left(q_{z}\right) D^{*}\left(q_{z}^{\prime}\right)}{\left(k_{2 \mathrm{i}}^{z}+k_{2 s}^{z}-q_{z}\right)\left(k_{2 \mathrm{i}}^{z}+k_{2 s}^{z}-q_{z}^{\prime}\right)^{*}} \\
& \times \operatorname{Im}\left[G^{ \pm}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \omega_{\mathrm{i}}-\omega_{\mathrm{s}}+\mathrm{i} 0^{+}\right)+G^{ \pm}\left(q_{z}, q_{z}^{\prime}, \boldsymbol{q} ; \omega_{\mathrm{s}}-\omega_{\mathrm{i}}-\mathrm{i} 0^{+}\right)\right] \quad(44)
\end{aligned}
$$

where $k_{2 i}^{z}$ and $k_{2 s}^{z}$ are the $z$-components of the wavevectors for the incident and scattered light inside the magnetic medium, and the factor $D(q_{z})$ is

$$
D(q_{z}) = \{1 - \exp[-\mathrm{i}(k_{2 i}^{z} + k_{2 s}^{z} - q_{z})N_{2}c]\}. \tag{45}
$$

The quantity $G^{\pm}(q_{z}, q_{z}', \boldsymbol{q} ; \eta)$ denotes a combination of spin-spin Green functions of the type already indicated, with + and - referring to in-phase and out-of-phase scattering respectively. Also $B^{\pm}(\omega_{\mathrm{s}})$ is a proportionality factor containing the polarisation terms, surface transmission terms, thermal factors, etc. Its general form is given in II, and in the present case it will have different amplitude factors (from the magneto-optical coupling) depending on whether in-phase $(+)$ or out-of-phase $(-)$ scattering is considered. The form of the Green function $G^{\pm}$ in (44) is given by

$$
\begin{aligned}
G^{\pm}(q_{z}, q_{z}', \boldsymbol{q} ; \eta) = &\left[G_{1,1}(q_{z}, q_{z}', \boldsymbol{q} ; \eta) + G_{2,2}(q_{z}, q_{z}', \boldsymbol{q} ; \eta)\right] \\
& \pm\left[G_{1,2}(q_{z}, q_{z}', \boldsymbol{q} ; \eta) + G_{2,1}(q_{z}, q_{z}', \boldsymbol{q} ; \eta)\right]
\end{aligned} \tag{46}
$$

where the definition of $G_{i, j}(q_{z}, q_{z}', \boldsymbol{q} ; \eta)$ in (36) is now generalised slightly to

$$
G_{1,1}(q_{z}, q_{z}', \boldsymbol{q}, \eta) = \sum_{m=1}^{\infty} \sum_{m'=1}^{\infty} F_{2m-1, 2m'-1}(\boldsymbol{q}, \eta) \exp[\mathrm{i}q_{z}z_{2m-1} - \mathrm{i}(q_{z}')^{*}z_{2m'-1}], \tag{47}
$$

etc. The generalisation is necessary because the summations in (44) extend over all real wavevector components (corresponding to bulk spin-waves) and also over the discrete imaginary values corresponding to the surface spin-wave branch. For scattering from bulk spin-waves (for which $q_{z}$ and $q_{z}'$ are real) this definition of the $G_{i, j}$ is the same as given previously in (36) and evaluated in (38)-(41).

For scattering from the surface spin-waves the imaginary values of $q_{z}$ (and also of $q_{z}'$) correspond to $q_{z}=q_{z}'=\mathrm{i}\lambda_{\mathrm{S}}$ where $\lambda_{\mathrm{S}}$ is the attenuation factor for the surface excitations and is given by

$$
\exp(\mathrm{i}q_{z}c) = \exp(-\lambda_{\mathrm{S}}c) = x \tag{48}
$$

where the appropriate value of $x$ has already been expressed in (32). It may then be shown using (29), together with (47) and (48), that for example:

$$
G_{2,2}(q_{z}, q_{z}', \boldsymbol{q} ; \eta) = \frac{8S^{2}J(\Delta + x)}{\Delta[E_{\mathrm{S}}^{+}(\boldsymbol{q}) - E][E_{\mathrm{S}}^{-}(\boldsymbol{q}) - E]} \delta_{q_{z}, q_{z}'}. \tag{49}
$$

The expressions for $G_{1,1}$, $G_{1,2}$ and $G_{2,1}$ for imaginary $q_{z}$ and $q_{z}'$ can be similarly evaluated.

Finally we may note that the quantities $k_{2 i}^{z}$ and $k_{2 s}^{z}$, which appear in (44) and (45) for $\mathrm{d}^{2}h/\mathrm{d}\Omega\mathrm{d}\omega_{\mathrm{s}}$, are fixed by the scattering geometry

$$
\left.
\begin{aligned}
k_{2 i}^{z} &= -(\omega_{\mathrm{i}}/c_{0})(\epsilon_{2} - \epsilon_{1} \sin^{2}\theta_{\mathrm{i}})^{1/2} \\
k_{2 s}^{z} &= -(\omega_{\mathrm{s}}/c_{0})(\epsilon_{2} - \epsilon_{1} \sin^{2}\theta_{\mathrm{s}})^{1/2}
\end{aligned}
\right\}. \tag{50}
$$

Here the notation is as in II, so that $\epsilon_{1}$ and $\epsilon_{2}$ denote the relative permeabilities of medium 1 (outside the antiferromagnet) and medium 2 (the semi-infinite antiferromagnet) respectively, and $c_{0}$ is the velocity of light in vacuum. Also $\theta_{\mathrm{i}}$ and $\theta_{\mathrm{s}}$ are the angles made by the incident and scattered light beams respectively to the normal ($z$-direction).

### 4.2. Scattering from bulk spin-waves

The bulk-mode scattering contribution is obtained by substituting (38)-(41) and (46) into (44) and simplifying. The summations over $q_z$ and $q_z'$ in (44) are in this case summations over all real wavevector components in the Brillouin zone. It can be seen from (38)-(41) that each Green function has been expressed as the sum of two terms, both with poles at a bulk spin-wave energy. This will lead to two types of contribution to the bulk scattering, which we now discuss separately.

The first term of each Green function in (38)-(41) corresponds to the Green function for an infinite crystal and involves a $\delta_{q_z, q_z'}$ factor. For a transparent crystal this leads to a Stokes scattering contribution of

$$
\begin{aligned}
\left(\frac{\mathrm{d}^{2} h}{\mathrm{~d} \Omega \mathrm{d} \omega_{\mathrm{s}}}\right)_{\mathrm{B} 1} & =\frac{2 \pi S B^{ \pm}\left(\omega_{\mathrm{s}}\right) N_{2} c^{2}\left[\Gamma \mp 8 S J \xi(\boldsymbol{q}) \cos \left(\frac{1}{2} q_{z} c\right)\right]}{E_{\mathrm{B}}(\boldsymbol{Q})} \\
& \times\left[\delta\left(\omega_{\mathrm{i}}-\omega_{\mathrm{s}}-g \mu_{\mathrm{B}} H-E_{\mathrm{B}}(\boldsymbol{Q})\right)+\delta\left(\omega_{\mathrm{i}}-\omega_{\mathrm{s}}+g \mu_{\mathrm{B}} H-E_{\mathrm{B}}(\boldsymbol{Q})\right)\right] \quad(51)
\end{aligned}
$$

where $q_z$ is determined by the wavevector conservation condition

$$
q_{z}=k_{2 \mathrm{i}}^{z}+k_{2 \mathrm{~s}}^{z}
$$

and the upper and lower signs in (51) refer respectively to the in-phase and out-of-phase scattering contributions. It follows therefore that generally there are two Stokes peaks at frequencies given by $\omega_{\mathrm{s}}=\omega_{\mathrm{i}}-g \mu_{\mathrm{B}} H-E_{\mathrm{B}}(\boldsymbol{Q})$ and $\omega_{\mathrm{s}}=\omega_{\mathrm{i}}+g \mu_{\mathrm{B}} H-E_{\mathrm{B}}(\boldsymbol{Q})$, and these will be coincident for the special case of applied field $H=0$. From (51) it is found that each peak of the Stokes doublet has an integrated intensity $\mathrm{d} h / \mathrm{d} \Omega$ given by

$$
\left(\frac{\mathrm{d} h}{\mathrm{~d} \Omega}\right)_{\mathrm{B} 1}^{\text {peak }}=\frac{2 \pi S B^{ \pm}\left(\omega_{\mathrm{s}}\right) N_{2} c^{2}\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}+8 S J \mp 8 S J\right]}{\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}\left(g \mu_{\mathrm{B}} H_{\mathrm{A}}+16 S J\right)\right]^{1 / 2}}
$$

where we have made the usual approximation of replacing $\boldsymbol{q}$ and $q_z$ by zero appropriate to the conditions $q a \ll 1$ and $q_{z} c \ll 1$ satisfied by the optical wavevectors for one-magnon scattering. Note that for in-phase scattering (upper sign) the numerator of (53) is independent of the exchange $J$, as found by Loudon (1970) for an infinite crystal.

For the more general case where the antiferromagnet is optically absorptive, the relative permeability $\epsilon_{2}$ is complex, and this corresponds to the light being attenuated as it penetrates into the antiferromagnet. Wavevector components $k_{2 \mathrm{i}}^{z}$ and $k_{2 \mathrm{~s}}^{z}$ given by (50) will then be complex, and we denote $k_{2 \mathrm{i}}^{z}=k_{2 \mathrm{i}}^{z^{\prime}}+\mathrm{i} k_{2 \mathrm{i}}^{z^{\prime \prime}}$ and $k_{2 \mathrm{~s}}^{z}=k_{2 \mathrm{~s}}^{z^{\prime}}+\mathrm{i} k_{2 \mathrm{~s}}^{z^{\prime \prime}}$ for their decomposition into real and imaginary parts. For $k_{2 \mathrm{i}}^{z^{\prime \prime}}$ and $k_{2 \mathrm{~s}}^{z^{\prime \prime}}$ non-zero the value of $q_z$ is no longer determined by the conservation condition of (52), and it is instead necessary to carry out a summation with $q_z$ ranging over all real wavevector components. Provided $H \neq 0$ two Stokes peaks are again predicted, each having integrated intensity given by

$$
\left(\frac{\mathrm{d} h}{\mathrm{~d} \Omega}\right)_{\mathrm{B} 1}^{\text {peak }}=\frac{S B^{ \pm}\left(\omega_{\mathrm{s}}\right) c\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}+8 S J \mp 8 S J\right]}{\left|k_{2 \mathrm{i}}^{z^{\prime \prime}}+k_{2 \mathrm{~s}}^{z^{\prime \prime}}\right|\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}\left(g \mu_{\mathrm{B}} H_{\mathrm{A}}+16 S J\right)\right]^{1 / 2}}
$$

(upper sign-in-phase; lower sign-out-of-phase), where we have assumed that $k_{2 \mathrm{i}}^{z^{\prime \prime}}$ and $k_{2 \mathrm{~s}}^{z^{\prime \prime}}$ are small in magnitude compared with their real parts $k_{2 \mathrm{i}}^{z^{\prime}}$ and $k_{2 \mathrm{~s}}^{z^{\prime}}$. The peaks are centred at frequencies given by $\omega_{\mathrm{s}}=\omega_{\mathrm{i}}-g \mu_{\mathrm{B}} H-E_{\mathrm{B}}\left(\boldsymbol{Q}_{0}\right)$ and $\omega_{\mathrm{s}}=\omega_{\mathrm{i}}+g \mu_{\mathrm{B}} H-$ $E_{\mathrm{B}}\left(\boldsymbol{Q}_{0}\right)$, where $\boldsymbol{Q}_{0}$ denotes the value of $\boldsymbol{Q}$ corresponding to (52). It can also be shown

that the peaks have a width proportional to $|k_{2\mathrm{i}}^{z''} + k_{2\mathrm{s}}^{z''}|$, which can in some cases be comparable with or larger than the intrinsic width due to magnon-magnon interactions. This 'opacity broadening' effect, together with lineshape calculations for absorptive antiferromagnets, will be discussed in detail in a subsequent paper.

Finally in this section we need to consider the further contributions to the bulk scattering which may arise due to the bulk spin-wave poles occurring in the second term of the Green function results of (38)-(41). These terms lead to scattering peaks at the same frequencies as already discussed in (51)-(54), but the results represent additional contributions to the integrated intensity $\mathrm{d}h/\mathrm{d}\Omega$ associated with each peak. For a transparent antiferromagnet it is found that the additional contribution to the intensity of each Stokes peak is approximately

$$
\left(\frac{\mathrm{d}h}{\mathrm{d}\Omega}\right)_{\mathrm{B}2}^{\mathrm{peak}} = \frac{2\pi S^2 B^{\pm}(\omega_{\mathrm{s}}) c^2 J(\Gamma \mp 8SJ)}{E_{\mathrm{B}}(0)\left[E_{\mathrm{B}}(0) - g\mu_{\mathrm{B}}H_{\mathrm{A}}\right]}. \tag{55}
$$

The total peak intensity for the transparent case is then given by the sum of (53) and (55). However, it can be verified that contribution $(\mathrm{d}h/\mathrm{d}\Omega)_{\mathrm{B}2}$ is very much smaller than $(\mathrm{d}h/\mathrm{d}\Omega)_{\mathrm{B}1}$ derived from the first term of each Green function, typically by a factor of order $1/N_2$. Hence in this case the contribution to the bulk scattering from the second term of each Green function can usually be neglected, and a similar conclusion is found to apply when optical absorption effects are included (provided $|k_{2\mathrm{i}}^{z''} + k_{2\mathrm{s}}^{z''}| \ll |k_{2\mathrm{i}}^{z'} + k_{2\mathrm{s}}^{z'}|$).

### 4.3. Scattering from surface spin-waves

To calculate the scattering from surface spin-waves we substitute equation (49) for the Green function $G_{2,2}$, together with similar results for the other $G_{i,j'}$ into our general formula of (44) for $\mathrm{d}^2 h/\mathrm{d}\Omega d\omega_{\mathrm{s}}$. As already noted, $q_z$ and $q_z'$ take discrete imaginary values given by (48), and this removes the summations in (44). The resulting contribution to the differential cross-section for Stokes scattering is

$$
\begin{aligned}
\left(\frac{\mathrm{d}^2 h}{\mathrm{d}\Omega \mathrm{d}\omega_{\mathrm{s}}}\right)_{\mathrm{S}} &= \frac{4S\pi B^{\pm}(\omega_{\mathrm{s}})(\Delta + 1)\left[\Gamma \mp 4SJ\xi(\boldsymbol{q})(|\Delta|^{1/2} + |\Delta|^{-1/2})\right]}{\Delta^3\left[E_{\mathrm{S}}^+(\boldsymbol{q}) - E_{\mathrm{S}}^-(\boldsymbol{q})\right]\left[(k_{2\mathrm{i}}^{z'} + k_{2\mathrm{s}}^{z'})^2 + (k_{2\mathrm{i}}^{z''} + k_{2\mathrm{s}}^{z''} - \lambda_{\mathrm{s}})^2\right]} \\
&\quad \times \left\{\delta(\omega_{\mathrm{i}} - \omega_{\mathrm{s}} - g\mu_{\mathrm{B}}H - E_{\mathrm{S}}^+(\boldsymbol{q})) + \delta(\omega_{\mathrm{i}} - \omega_{\mathrm{s}} + g\mu_{\mathrm{B}}H - E_{\mathrm{S}}^+(\boldsymbol{q}))\right] \tag{56}
\end{aligned}
$$

where $\lambda_{\mathrm{s}}$ is the surface spin-wave attenuation factor defined in (48), and again the upper and lower signs refer respectively to in-phase and out-of-phase scattering terms. Hence a doublet of Stokes peaks is predicted, at frequencies $\omega_{\mathrm{s}}$ given by $\omega_{\mathrm{i}} - g\mu_{\mathrm{B}}H - E_{\mathrm{S}}^+(\boldsymbol{q})$ and $\omega_{\mathrm{i}} + g\mu_{\mathrm{B}}H - E_{\mathrm{S}}^+(\boldsymbol{q})$. Since $E_{\mathrm{S}}^+(\boldsymbol{q}) \neq E_{\mathrm{B}}(\boldsymbol{Q})$ in the long-wavelength limit, the bulk and surface scattering peaks will occur at different frequencies. We may now make the usual approximation for one-magnon light scattering of putting $\boldsymbol{q} = 0$ in (56), whereupon it follows that the integrated intensity of each surface scattering peak is approximately

$$
\left(\frac{\mathrm{d}h}{\mathrm{d}\Omega}\right)_{\mathrm{S}}^{\mathrm{peak}} = \frac{2\pi SB^{\pm}(\omega_{\mathrm{s}})(\Delta + 1)\left[\Gamma \mp 4SJ(|\Delta|^{1/2} + |\Delta|^{-1/2})\right]}{\Delta^3\left[g\mu_{\mathrm{B}}H_{\mathrm{A}}(g\mu_{\mathrm{B}}H_{\mathrm{A}} + 8SJ)\right]^{1/2}\left[(k_{2\mathrm{i}}^{z'} + k_{2\mathrm{s}}^{z'})^2 + (k_{2\mathrm{i}}^{z''} + k_{2\mathrm{s}}^{z''} - \lambda_{\mathrm{s}})^2\right]}. \tag{57}
$$

Equations (56) and (57) apply in both the transparent limit (when $k_{2\mathrm{i}}^{z''} = k_{2\mathrm{s}}^{z''} = 0$) and in the absorptive case.

The results for the intensities of the Stokes peaks for scattering from either bulk spin-waves or from surface spin-waves simplify considerably for systems where the anisotropy is not too large. If $g\mu_{\mathrm{B}}H_{\mathrm{A}} \ll 8SJ$, which is satisfied in many antiferromagnets

Scattering off the surface of antiferromagnets

(such as $MnF_{2}$), (53), (54) and (57) simplify to

$$
\left(\frac{\mathrm{d} h}{\mathrm{~d} \Omega}\right)_{\mathrm{B} 1}^{\text {peak }}=\frac{\pi S B^{ \pm}\left(\omega_{\mathrm{s}}\right) N_{2} c^{2}\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}+8 S J \mp 8 S J\right]}{2\left[g \mu_{\mathrm{B}} H_{\mathrm{A}} S J\right]^{1 / 2}} \quad \text { (transparent case) }
\tag{58}
$$

$$
\left(\frac{\mathrm{d} h}{\mathrm{~d} \Omega}\right)_{\mathrm{B} 1}^{\text {peak }}=\frac{S B^{ \pm}\left(\omega_{\mathrm{s}}\right) c\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}+8 S J \mp 8 S J\right]}{4\left|k_{2 \mathrm{i}}^{z^{\prime \prime}}+k_{2 \mathrm{~s}}^{z^{\prime \prime}}\right|\left[g \mu_{\mathrm{B}} H_{\mathrm{A}} S J\right]^{1 / 2}} \quad \text { (absorptive case) }
\tag{59}
$$

$$
\left(\frac{\mathrm{d} h}{\mathrm{~d} \Omega}\right)_{\mathrm{S}}^{\text {peak }}=\frac{\pi B^{ \pm}\left(\omega_{\mathrm{s}}\right)\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}+8 S J \mp 8 S J\right]}{2 J\left[\left(k_{2 \mathrm{i}}^{z^{\prime}}+k_{2 \mathrm{~s}}^{z^{\prime}}\right)^{2}+\left(k_{2 \mathrm{i}}^{z^{\prime \prime}}+k_{2 \mathrm{~s}}^{z^{\prime \prime}}-\lambda_{\mathrm{s}}\right)^{2}\right]}
\tag{60}
$$

whilst the expression for $\lambda_{\mathrm{s}}$ reduces to

$$
\lambda_{\mathrm{s}}=\frac{1}{c}\left(\frac{g \mu_{\mathrm{B}} H_{\mathrm{A}}}{2 S J}\right)^{1 / 2}.
\tag{61}
$$

Typically for light scattering $c|k_{2 \mathrm{i}}^{z^{\prime}}+k_{2 \mathrm{~s}}^{z^{\prime}}| \sim 10^{-2}$ or $10^{-3}$, and $c|k_{2 \mathrm{i}}^{z^{\prime \prime}}+k_{2 \mathrm{~s}}^{z^{\prime \prime}}|$ is of the same order or smaller. On the other hand, $(g \mu_{\mathrm{B}} H_{\mathrm{A}} / 2 S J)^{1 / 2}$ is usually larger than $10^{-2}$ (e.g. it is approximately 0.25 for $MnF_{2}$), and in such cases the terms in $k_{2 \mathrm{i}}^{z^{\prime}}, k_{2 \mathrm{~s}}^{z^{\prime}}, k_{2 \mathrm{i}}^{z^{\prime \prime}}$ and $k_{2 \mathrm{~s}}^{z^{\prime \prime}}$ in the denominator of (60) may be neglected compared with $\lambda_{\mathrm{s}}$ to give

$$
\left(\frac{\mathrm{d} h}{\mathrm{~d} \Omega}\right)_{\mathrm{S}}^{\text {peak }} \simeq \frac{\pi S B^{ \pm}\left(\omega_{\mathrm{s}}\right) c^{2}\left[g \mu_{\mathrm{B}} H_{\mathrm{A}}+8 S J \mp 8 S J\right]}{g \mu_{\mathrm{B}} H_{\mathrm{A}}}.
\tag{62}
$$

### 5. Discussion and conclusions

In this paper we have derived expressions for spin-spin Green functions of the form $\ll S_{\boldsymbol{R}}^{+} ; S_{\boldsymbol{R}^{\prime}}^{-} \gg$ for body-centred tetragonal antiferromagnets with a (001) surface at low temperatures $T \ll T_{\mathrm{N}}$. The results were found to provide a description of bulk spin-waves and the localised surface spin-waves, with appropriate weighting factors.

The Green functions were employed to calculate the cross-section and integrated intensity for light scattering from the surface of antiferromagnets. It was shown that scattering from the surface excitations would occur at a different frequency from scattering processes involving bulk spin-waves, and this should enable the two types of contribution to the intensity to be more readily distinguished experimentally (compared with the ferromagnetic case, for example). The relative intensities for scattering from surface and bulk spin-waves can be deduced from equations (58), (59) and (62). It follows that for in-phase or out-of-phase scattering the ratio of intensities is (in the absorptive case)

$$
\frac{(\mathrm{d} h / \mathrm{d} \Omega)_{\mathrm{S}}}{(\mathrm{d} h / \mathrm{d} \Omega)_{\mathrm{B} 1}}=4 \pi c\left|k_{2 \mathrm{i}}^{z^{\prime \prime}}+k_{2 \mathrm{~s}}^{z^{\prime \prime}}\right|\left(\frac{S J}{g \mu_{\mathrm{B}} H_{\mathrm{A}}}\right)^{1 / 2}.
\tag{63}
$$

Assuming $c|k_{2 \mathrm{i}}^{z^{\prime \prime}}+k_{2 \mathrm{~s}}^{z^{\prime \prime}}| \sim 10^{-4}$ to $10^{-3}$, together with exchange and anisotropy parameters as for $MnF_{2}$, this ratio is of order $10^{-2}$ to $10^{-1}$. Hence the surface scattering peaks are predicted to be less intense than the bulk scattering peaks, but it should nevertheless be possible to observe them experimentally.

The calculations in this paper were carried out using a high-density perturbation expansion in powers of $1/z$. This approach has a number of advantages, as discussed in I. In particular the method may be extended to higher temperatures, or alternatively by evaluating contributions to a higher order in the $1/z$ expansion the effect of spin-wave

interactions (leading to damping of the bulk and surface excitations) may be investigated. Some of these extensions to the present work are currently being studied.

In this paper we have considered the cases where the magnetic medium is trans- parent or where the optical absorption is weak $(|k_{2 i}^{z''}+k_{2 s}^{z''}| \ll |k_{2 i}^{z'}+k_{2 s}^{z'}|)$. However if the absorption is stronger $(|k_{2 i}^{z''}+k_{2 s}^{z''}| \sim |k_{2 i}^{z'}+k_{2 s}^{z'}|)$ there are additional effects such as 'opacity broadening' of the scattering peaks and asymmetric lineshapes. Also in evalua- ting the bulk scattering it may in such cases become important to include the contribu- tion B2 as well as B1. This is discussed in the following paper.

## Acknowledgment

The author is grateful to Professor R Loudon for helpful discussions.

## References

Abrikosov A A, Gorkov L P and Dzyaloshinskii I Ye 1965 *Quantum Field Theoretical Methods in Statistical Physics* 2nd edn (Oxford: Pergamon)

Cottam M G 1975 *J. Phys. C: Solid St. Phys.* **8** 1933-49
—— 1976a *J. Phys. C: Solid St. Phys.* **9** 2121-36
—— 1976b *J. Phys. C: Solid St. Phys.* **9** 2137-50

Cottam M G and Stinchcombe R B 1970 *J. Phys. C: Solid St. Phys.* **3** 2283-304

Dewames R E and Wolfram T 1969 *Phys. Rev.* **185** 752-9

Loudon R 1970 *J. Phys. C: Solid St. Phys.* **3** 872-90

Mills D L and Saslow W M 1968 *Phys. Rev.* **171** 488-506

Moriya T 1967 *J. Phys. Soc. Japan* **23** 490-500

Spencer H J 1968 *Phys. Rev.* **167** 434-44

Vaks V G, Larkin A I and Pikin S A 1968 *Sov. Phys.-JETP* **26** 188-99