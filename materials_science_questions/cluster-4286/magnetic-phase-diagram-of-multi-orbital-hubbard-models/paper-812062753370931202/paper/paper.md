# Strong coupling anomalous dimensions of $\mathcal{N} = 4$ super Yang-Mills

This content has been downloaded from IOPscience. Please scroll down to see the full text.

JHEP09(2006)016

(http://iopscience.iop.org/1126-6708/2006/09/016)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 130.237.165.40
This content was downloaded on 08/09/2015 at 04:38

Please note that [terms and conditions apply].

![](./images/812062753370931202_1.jpg)

PUBLISHED BY INSTITUTE OF PHYSICS PUBLISHING FOR SISSA

RECEIVED: June 16, 2006
ACCEPTED: August 16, 2006
PUBLISHED: September 7, 2006

# Strong coupling anomalous dimensions of $\mathcal{N}=4$ super Yang-Mills

Matteo Beccaria*

Dipartimento di Fisica, Universita' di Lecce,
Via Arnesano, 73100 Lecce;
INFN, Sezione di Lecce
E-mail: matteo.beccaria@le.infn.it

Carmine Ortix†

Dipartimento di Fisica, Universita' di Lecce,
Via Arnesano, 73100 Lecce;
INFN, Sezione di Lecce
E-mail: carmine.ortix@le.infn.it

ABSTRACT: We study the strong coupling behaviour of fixed length single trace operators in the scalar SU(2) sector of $\mathcal{N}=4$ SYM. We assume the recently proposed connection with a twisted half-filled Hubbard model. By explicit direct diagonalization of operators with length $L=4,6,8$ we study the full perturbative multiplet of those lattice states which have a clear correspondence with gauge theory composite operators. For this multiplet, we follow the weak-strong coupling flow to free fermion states and identify in particular the precise asymptotic fermion configuration. Next, we analyze the Lieb-Wu equations of the twisted Hubbard model. For the antiferromagnetic state we derive its strong coupling expansion working at $L$ up to 32. We also study the lightest state in the perturbative multiplet. This state is non trivial since involves complex solutions of the Lieb-Wu equations. It is particularly interesting for $AdS_5 \times S^5$ duality since it is dual to the folded string semiclassical solution in the thermodynamical limit. We are able to perform the full analysis and compute the next-to-next-to leading terms in the strong coupling expansion for the non trivial lengths $L=12$ and $L=20$. A general formula is proposed for the NLO expansion for any $L=4(2k+1), k \in \mathbb{N}$.

KEYWORDS: Lattice Integrable Models, AdS-CFT Correspondence.

*Partially supported by INFN, IS-RM62
†Partially supported by INFN, IS-RM62

© SISSA 2006
http://jhep.sissa.it/archive/papers/jhep092006016/jhep092006016.pdf

JHEP09(2006)016

Contents

1. Introduction 1

2. Anomalous dimensions in $\mathcal{N}=4$ SYM and the Hubbard model 4

3. The perturbative multiplet 6
3.1 The antiferromagnetic state 6
3.2 The light states 8

4. Analysis of the full spectrum 9
4.1 Review of the $L=4$ case 10
4.2 Extension to longer operators 11
4.3 The non degenerate $L=6$ case 13
4.4 The degenerate $L=8$ case 15
4.5 Summary of the results for $L=8$ 19

5. Direct analysis of the Lieb-Wu equations 19
5.1 Real solution: the antiferromagnetic state 20
5.2 A complex solution: the $|\text{FS}\rangle$ state 21
5.2.1 $L=12$ 22
5.2.2 $L=16$ 25
5.2.3 $L=20$ 25
5.2.4 Conjecture for the $|\text{FS}\rangle$ state at general $L=4(2k+1)$ 28

6. Summary of results and discussion 28

7. Conclusions 30

A. Exact diagonalization of the $S=0$ sector of the Heisenberg model 31

---

1. Introduction

The quantum behavior of $\mathcal{N}=4$ super Yang-Mills in the planar limit is crucial in the context of AdS/CFT correspondence [1–5]. In particular, the anomalous dimensions of certain single trace operators in the planar limit of the $\mathcal{N}=4$ theory can be compared with the masses of string states on $AdS_5 \times S^5$ [6]. For instance, the comparison turns out to be particularly favorable for BMN states [7] where the gauge-string matching can be done at the perturbative level in the planar gauge theory at the price of analyzing *long* composite operators with a large number of constituent fields and few impurities.

Apart from the gauge-string connections, the $\mathcal{N}=4$ quantum theory has a rich internal structure suggesting its quantum integrability. The calculation of anomalous dimensions in specific sectors of the $\mathcal{N}=4$ theory can be cast in algebraic form by computing the loop corrected dilatation operator [8]. The huge mixing problem is then reduced to the analysis of the eigensystem of the finite dimensional matrix representing the dilatation operator.

Remarkably, at one-loop, the dilatation operator can be identified with the Hamiltonian of the integrable XXX spin 1/2 lattice model [9]. In the SU(2) sector, Beisert, Dipple and Staudaucher (BDS) [8, 10, 11] proposed a Bethe Ansatz for the 2-body $S$-matrix in agreement with the explicit three loop dilatation operator and consistent with all loop BMN scaling [7]. The BDS equations describe a spin model of the Heisenberg-type with long range couplings. The range of the spin interaction increases as the loop order is increased. After having built the five loop BDS Hamiltonian, they could match the gauge theory predictions known up to three loops. A disagreement with the gauge theory calculation for operators with classical dimension $L$ is expected precisely at $L$ loop order due to wrapping terms. In the thermodynamical limit, these terms are negligible and an all-loop Bethe Ansatz was proposed.

Using the BDS equations it is possible to compute the largest energy state on the chain [12, 13]. In the Heisenberg model language, it the non trivial antiferromagnetic state. Its energy in the thermodynamical limit perfectly agrees with the ground state energy of a (twisted) one-dimensional Hubbard model at half-filling [14]. The connection between the spin model and the itinerant fermion model can be understood as follows. The spin model is nothing but the strong coupling expansion of the fermion model, where strong means the the hopping term is treated perturbatively. The effective Hamiltonian for the strong coupling of the Hubbard model contains interactions with a range increasing with the order of the expansion. This is because successive applications of the hopping operators connect lattice sites with increasing distance.

With an impressive breakthrough, Rej, Serban and Staudacher (RSS) proposed the Hubbard model as the correct microscopic model behind the integrable structure of the $\mathcal{N}=4$ SYM dilatation operator [12]. In other words, they suggest that it could predict at all loops and non perturbatively the anomalous dimensions of the gauge theory operators for any finite $L$. This proposal also overcomes the problems related to the wrapping interactions in the long range spin model [15]. The RSS proposal is still a conjecture although with robust theoretical motivations. To pursue its assessment, it would be necessary to perform a four loop calculation in the gauge theory. Waiting for this check, the Hubbard model can be considered as a powerful Ansatz for the description of the gauge theory at finite operator lengths and beyond the perturbative regime.

Actually, the appearance of the Hubbard model remains somewhat mysterious and intriguing [16]. In particular, the Hubbard model describes fermions with spin and admits states with two fermions in the same site. This extra states cannot be identified immediately with gauge theory operators. Indeed, it is not clear what is the role of its extra states which at strong coupling definitely mix with the perturbative states. Waiting for a better understanding of the role of Hubbard model, we can assume an optimistic attitude and exploit it to investigate the weak-strong coupling behavior of anomalous dimensions.

- 2 -

The main technical tool in the analysis of states in the Hubbard model are its Lieb-
Wu equations which encode integrability. The Lieb-Wu equations are precious in the study of the thermodynamical limit including finite size corrections [17–19]. However, the machinery works well only for particular states. In the thermodynamical limit, the Bethe roots accumulate on a discrete set of non trivial curves in the complex plane. The integral equations for the root density are quite difficult due to unknown shape (and number) of the contours. At weak coupling, the Lieb-Wu equations reduce to the BDS Ansatz of Heisenberg type. In some favorable cases a solution for the thermodynamical limit can be found. Remarkably, the solution can also be matched with specific semiclassical string states [20–24]. The analysis of the Lieb-Wu equations is more problematic and the full spectrum of the twisted Hubbard model at finite large $L$ remains a quite difficult task.

As an alternative approach to solving the Lieb-Wu equations, J. Minahan has recently proposed [25] to analyze directly the twisted Hubbard model Hamiltonian on small lattices to understand the features of the spectrum. This is an interesting approach aimed at un- derstanding the strong coupling behavior of states associated to gauge invariant operators.

In this paper, we analyze single trace cyclic operators with zero SU(2) spin of the form

$$
\operatorname{Tr}\left(Z^{J} \Phi^{J}\right)+\ldots \tag{1.1}
$$

with large $J$. Here, $Z$, and $\Phi$ are the charged scalar fields in the $\mathcal{N}=4$ supermultiplet. As usual, dots stand for various other orderings of the scalar fields required to obtain eigen- states of the dilatation operator. The above set of operators, all with classical dimension $2 J$ is closed under perturbative renormalization. It is not clear what happens at strong coupling. Indeed, it has been suggested that some surprise could occur [26]. In this di- rection, it seems to be important to understand the mutual role of the perturbative states and the additional states in the Hubbard model.

As a first step of our analysis, we collect and explain some general features of the states belonging to what we call the *perturbative multiplet*. These are the states in the Hubbard model with a clear identification with single trace operators in the gauge theory. Then, we exploit the direct approach of [25] to study the full spectrum at $L=4,6,8$. The case $L=4$ is discussed in [26] and here it is reviewed to present the method and prepare for larger $L$. The cases $L=6$ and 8 are more involved and reveal interesting features. In all cases, we determine precisely the flow to large $g$.

The direct analysis can hardly be pushed to much larger values of $L$. Hence, we revert to the numerical exploration of the complete Lieb-Wu equations. We perform the analysis of the antiferromagnetic state (the one with highest anomalous dimension) working with up to $L=32$ sites and providing the NNLO strong coupling expansion of its anomalous dimension.

Next, we consider the lightest state in the perturbative multiplet. Exploiting some features of this state in the thermodynamical limit, we solve numerically the Lieb-Wu equations at $L=12,20$ (the first non trivial cases of $L=8 k+4, k \in \mathbb{N}$ ). These are remarkable values of the composite operators length. Nevertheless, the analysis is per- formed in full details obtaining also in this case the NNLO strong coupling expansion of

the anomalous dimension. This analysis is important in our opinion since it is an explicit study of the Lieb-Wu equations at large but finite $L$.

The paper is closed by a conjecture about the general form of the lightest state for lengths $L$ of the form $4(2k+1)$, $k\in\mathbb{N}$. A discussion of the comparison with the BMN limit is also discussed.

### 2. Anomalous dimensions in $\mathcal{N}=4$ SYM and the Hubbard model

The four dimensional $\mathcal{N}=4$ SYM theory is finite. Its non trivial quantum properties are encoded in the behavior of gauge invariant composite operators. The gauge group is $SU(N)$ and we are interested in the planar limit $N\rightarrow\infty$. We introduce the coupling $g$ related to the large $N$ 't Hooft coupling $\lambda$

$$
g^{2}=\frac{\lambda}{8\pi^{2}},\quad\lambda=g_{\mathrm{YM}}^{2}N.\tag{2.1}
$$

In the so-called SU(2) sector of $\mathcal{N}=4$ SYM, we consider gauge invariant composite operators of definite scaling dimension

$$
\mathrm{Tr}\left(Z^{L-M}\Phi^{M}\right)+\dots\tag{2.2}
$$

where $Z$, $\Phi$ are charged scalar fields. The classical dimension is $L$, the number of fields. In the following, we shall simply call $L$ the length due to the lattice representation that we are going to introduce. The above composite operators have non trivial renormalization properties and acquire anomalous dimensions with all-loop corrections

$$
\Delta(g)=L+\sum_{\ell\geq1}\Delta_{\ell}g^{2\ell}.\tag{2.3}
$$

As we discussed in the Introduction, they can be computed as the eigenvalues of a charge $\mathcal{D}$. It is the dilatation operator and belongs to an infinite tower of commuting charges. Its perturbative expansion (at two loops) is

$$
\mathcal{D}=L+\frac{g^{2}}{2}\sum_{i}(1-\sigma_{i}\cdot\sigma_{i+1})-\frac{g^{4}}{4}\sum_{i}(3-4\sigma_{i}\cdot\sigma_{i+1}+\sigma_{i}\cdot\sigma_{i+2})+\cdots,\tag{2.4}
$$

where the $\sigma_{i}$ matrices act on the cyclic states of a spin $1/2$ chain. A particular operator is mapped to a spin chain state in the natural way, e.g.

$$
\mathrm{Tr}\left(Z Z\Phi Z\cdots\right)\longrightarrow\left|\uparrow\uparrow\downarrow\uparrow\cdots\right\rangle+\text{cyclic translations}\tag{2.5}
$$

The dilatation operator at finite $g$ is thus non local. The RSS proposal identifies the up and down spin with fermions in two spin states. It also add states with two fermions occupying the same site. On this enlarged state space, RSS define an Hubbard-type Hamiltonian. In the following we shall consider the case $L\in2\mathbb{N}$ and $M=L/2$ and look at operators with zero SU(2) spin. The explicit local Hubbard Hamiltonian is

$$
H=H_{0}+\frac{g}{\sqrt{2}}H_{1},\tag{2.6}
$$

- 4 -

where

$$
H_{0}=L-\sum_{i=1}^{L} n_{\uparrow, i} n_{\downarrow, i}, \quad n_{\sigma, i}=c_{\sigma, i}^{\dagger} c_{\sigma, i},
\tag{2.7}
$$

$$
H_{1}=\sum_{\sigma=\uparrow, \downarrow}\left(\sum_{i=1}^{L-1} c_{\sigma, i}^{\dagger} c_{\sigma, i+1}+e^{i \phi} c_{\sigma, L}^{\dagger} c_{\sigma, 1}\right)+\text { h.c. }
\tag{2.8}
$$

The fermion creation and annihilation operators satisfy canonical anticommutation relations

$$
\left\{c_{\sigma, i}, c_{\sigma^{\prime}, j}^{\dagger}\right\}=\delta_{\sigma, \sigma^{\prime}} \delta_{i, j},
\tag{2.9}
$$

$$
\left\{c_{\sigma, i}, c_{\sigma^{\prime}, j}\right\}=\left\{c_{\sigma, i}^{\dagger}, c_{\sigma^{\prime}, j}^{\dagger}\right\}=0.
\tag{2.10}
$$

Periodic boundary conditions are understood. The twisting phase in the boundary link is fixed at $\phi=\pi / 2$.

The Hamiltonian (2.6) is symmetric under the SU(2) generators

$$
S_{z}=\frac{1}{2} \sum_{i=1}^{L}\left(n_{\uparrow, i}-n_{\downarrow, i}\right),
\tag{2.11}
$$

$$
S^{+}=\sum_{i=1}^{L} c_{\uparrow, i}^{\dagger} c_{\downarrow, i}, \quad S^{-}=\left(S^{+}\right)^{\dagger}.
\tag{2.12}
$$

At half-filling and with an equal number of up and down fermions the $z$-component is automatically zero.

The Hamiltonian (2.6) is also invariant under the shift

$$
c_{\sigma, j} \rightarrow e^{i \phi / L} c_{\sigma, j+1}, \quad j=1, \ldots, L-1,
\tag{2.13}
$$

$$
c_{\sigma, L} \rightarrow e^{i \phi(L+1) / L} c_{\sigma, 1},
\tag{2.14}
$$

with related transformation properties of the $c^{\dagger}$ operators. The states invariant under this symmetry will be called cyclic states and are the relevant ones to represent single trace operators in the gauge theory.

The Hamiltonian can be written in a simpler form after the transformation

$$
c_{n}=e^{i n \phi / L} \widetilde{c}_{n}.
\tag{2.15}
$$

The on-site Coulombian term $H_{0}$ is unchanged. The hopping part $H_{1}$ becomes

$$
H_{1}=\sum_{\sigma=\uparrow, \downarrow} \sum_{i=1}^{L} e^{i \phi / L} \widetilde{c}_{\sigma, i}^{\dagger} \widetilde{c}_{\sigma, i+1}+\text { h.c. },
\tag{2.16}
$$

and the shift symmetry is written simply

$$
\widetilde{c}_{n} \rightarrow e^{2 i \phi / L} \widetilde{c}_{n+1}.
\tag{2.17}
$$


The hopping term is diagonalized by introducing fermion operators in momentum space
$$
a_{\sigma,p} = \frac{1}{\sqrt{L}} \sum_{n=1}^L e^{-i p n} \widetilde{c}_{\sigma,n}, \tag{2.18}
$$
where the lattice momenta can take the values
$$
p_n = \frac{2\pi\, n}{L}, \quad n = 0,1,\dots,L-1. \tag{2.19}
$$

The dispersion relation for the scaled Hamiltonian $H_1/\sqrt{2}$ is then
$$
\varepsilon_n = \sqrt{2} \cos\left( \frac{2\pi n}{L} + \frac{\pi}{2L} \right). \tag{2.20}
$$

Cyclic states of the original Hamiltonian with $L$ fermions can be built in momentum spaces by acting on the vacuum with $L$ $a_{\sigma,p}^\dagger$ operators with a total momentum $\sum p$ being an odd multiple of $\pi$ due to the phase factor $e^{2i\phi/L}$.

## 3. The perturbative multiplet

As we have seen, the RSS construction introduces additional states with fermion double occupancy which do not have a direct correspondence with the gauge theory composite operators. As we remarked in the Introduction, the role of these states is not totally clear. However, we can exploit them as an auxiliary device and focus on what we shall denote the **perturbative multiplet**. This is the set of states which at $g \to 0$ reduce to states with no double occupancy and have $\Delta(g) \to L$, the maximal value at $g=0$. In other words, these are the states which flow at weak coupling to states that can be naturally mapped to gauge invariant single trace operators. As $g$ increases, they are no more the maximal energy states and mix with all the extra states.

At very large $g$, any state flows to a free fermion state which is an eigenstate of the hopping term $H_1$. Our aim is to understand the asymptotic free fermion content of specific states in the perturbative multiplet. In particular, at large $g$ we find $\Delta(g) \sim \delta\, g+\mathcal{O}(1)$ where $\delta$ is the hopping energy of the asymptotic free fermion state. We show in figure (1) the qualitative description of the spectrum. The up most state is the so-called antiferromagnetic state (AF). The bottom part of the perturbative multiplet is composed of what we shall call light states, where light means that the anomalous dimension is small in the weak coupling region. The multiplets of extra states with double occupation are also schematically shown. In principle they can cross the perturbative multiplet. In the following sections, we shall discuss some general features of the AF and light states that can be derived from general principles and an analysis of the BDS equations.

### 3.1 The antiferromagnetic state

At even $L$ the AF state is non degenerate. Its anomalous dimension is known in the thermodynamical limit. In terms of the planar coupling $\lambda=8\pi^2 g^2$, it reads [13]
$$
\lim_{L\to\infty} \frac{\Delta_{\text{AF}}(\lambda,L)}{L} = 1 + \frac{\sqrt{\lambda}}{\pi} f\left( \frac{\pi}{\sqrt{\lambda}} \right), \tag{3.1}
$$

- 6 -

![](./images/812062753370931202_2.jpg)

Figure 1: Qualitative description of the Hubbard model spectrum. The upper line is the AF state.
The lowest dashed lines in the perturbative multiplet are the light states. We also show two states
from a different multiplet. One of them crosses a light state. At large g all lines are linear in g. At
small $g$, $\Delta(g) = L + \mathcal{O}(g^2)$ in the perturbative multiplet.

where
$$
f(x)=\int_{0}^{\infty} d k \frac{J_{0}(k)}{k} \frac{J_{1}(k)}{1+e^{2 k x}}. \tag{3.2}
$$

This function is well known to be non-analytic in $x=0$. However, it admits the asymptotic
expansion [27]
$$
f(x)=\frac{1}{\pi}-\frac{x}{4}+\sum_{m=1}^{N} \mu_{m} x^{2 m}+\mathcal{O}\left(x^{2 N+2}\right), \tag{3.3}
$$
where
$$
\mu_{m}=\frac{(2 m-1)\left(2^{2 m+1}-1\right)[(2 m-3) ! !]^{3}}{2^{3 m-1}(m-1) !} \frac{\zeta(2 m+1)}{\pi^{2 m+1}}, \quad(-1) ! ! \equiv 1. \tag{3.4}
$$

Despite being only asymptotic and not convergent, the above expansion has been shown to
reproduce correctly the second order perturbative correction at large $\lambda$. This means that
we can expand the anomalous dimension at large $\lambda$ as
$$
\Delta_{\mathrm{AF}}(\lambda, L)=a_{1}(L) \sqrt{\lambda}+a_{2}(L)+a_{3}(L) \frac{1}{\sqrt{\lambda}}+\ldots, \tag{3.5}
$$
and the limits $\lim _{L \rightarrow \infty} a_{k}(L)$ are obtained by replacing $f(x)$ by its asymptotic expansion.
At second order, we have
$$
f(x)=\frac{1}{\pi}-\frac{x}{4}+\frac{7}{4} \frac{\zeta(3)}{\pi^{3}} x^{2}+\ldots \tag{3.6}
$$
and we obtain
$$
\lim _{L \rightarrow \infty} \frac{\Delta_{\mathrm{AF}}^{\text {strong }}(\lambda, L)}{L}=1+\frac{\sqrt{\lambda}}{\pi} f\left(\frac{\pi}{\sqrt{\lambda}}\right)=\frac{\sqrt{\lambda}}{\pi^{2}}+\frac{3}{4}+\frac{7}{4} \frac{\zeta(3)}{\pi^{2}} \frac{1}{\sqrt{\lambda}}+\ldots=
$$


$$
= \frac{2\sqrt{2}}{\pi} g + \frac{3}{4} + \frac{7}{8\pi^3\sqrt{2}} \zeta(3) \frac{1}{g} + \dots
\tag{3.7}
$$

Here, $\Delta_{\text{AF}}^{\text{strong}}(\lambda, L)$ stands for the expansion eq. (3.5). Later, we shall compare this prediction with the finite $L$ analysis of the Lieb-Wu equations.

### 3.2 The light states

At the bottom of the perturbative multiplet there are light states. These are light in the sense that their anomalous dimension is small in the perturbative region. These states are highly non trivial in the BDS description. In the Heisenberg language, up to a change of sign in the anomalous dimension, they are states which can be built adding many excitation over the antiferromagnetic state respecting the constraint of zero spin and cyclicity. Not very much is known about these states since they correspond to non trivial distributions of Bethe roots in the thermodynamical limit [28]. In some cases, the Bethe Ansatz equations can be solved at $L \to \infty$. An example is the lightest state which is associated with a limiting double contour distribution [20, 21]. For brevity, we shall denote this state as $|\text{FS}\rangle$ since in the BMN limit it is dual to the so-called folded string solution [29].

The state $|\text{FS}\rangle$ can be studied at finite $L$ and its anomalous dimension can be loop expanded. If we express the result in terms of the 't Hooft coupling $\lambda$ we find

$$
\Delta_{\text{FS}}(\lambda, L) = L + \sum_{\ell \geq 1} \frac{c_{\ell}(L)}{L^{2\ell-1}} \lambda^{\ell}.
\tag{3.8}
$$

The reason for the various explicit powers of $L$ is that all the coefficients $c_{\ell}(L)$ have finite limits as $L \to \infty$. Hence, the state $|\text{FS}\rangle$ admits the BMN limit

$$
L \to \infty, \quad \text{fixed } \frac{\lambda}{L^2} = 8\pi^2 \left( \frac{g}{L} \right)^2.
\tag{3.9}
$$

It is usual to introduce the coupling $\lambda' = \lambda/J^2$ where $J = L/2$ is the angular momentum of the folded string. The coupling $\lambda'$ is fixed in the BMN limit. The BMN limit of the anomalous dimension is then

$$
\lim_{L \to \infty} \frac{1}{L} \Delta_{\text{FS}} \left( \lambda' L^2, L \right) = F(\lambda'), \quad \lambda' \text{ fixed}.
\tag{3.10}
$$

The function $F(\lambda')$ has been first computed in [29]. At small $\lambda'$, it reproduces the gauge theory perturbative expansion

$$
F(\lambda') = 1 + \frac{0.7120}{8} \lambda' + \dots
\tag{3.11}
$$

At large $\lambda'$, $F(\lambda') \simeq \frac{1}{\sqrt{2}} (\lambda')^{1/4}$, the typical behavior expected from AdS/CFT duality [30].

In this paper, we work at finite $L$ and cannot access the limit eq. (3.10). Instead we are studying the $|\text{FS}\rangle$ state at fixed $L$, expanding $\Delta_{\text{FS}}$ at large $\lambda'$. This is the same procedure we followed for the AF state and is the kind of investigation described in [25]. We remark

\pagebreak

![](./images/812062753370931202_3.jpg)

Figure 2: Spin correlation function for the lightest |FS⟩ state of the Heisenberg chain (under the cyclic and $S=0$ constraints).

that there can be important differences between this and the BMN limits. At finite $L$ and $\lambda'$ there can be terms with ambiguous $\lambda',L\rightarrow\infty$ limit. An example could be, for instance,
$$
\frac{\lambda'/L}{1+\lambda'/L}, \tag{3.12}
$$
tending to 1 when $\lambda'\rightarrow\infty$ and to 0 when $L\rightarrow\infty$.

BMN scaling appears to be a general feature of the light states and is quite effective in the search for the corresponding dual string states. It is natural to look at BMN scaling as an infinite volume limit where the fixed ratio $\sqrt{\lambda'}\sim g/L$ is interpreted as a finite size scaling variable. This smooth thermodynamical limit on the lattice can be explored more explicitly by evaluating in the Heisenberg model the SU(2) invariant correlation function
$$
G_k=\langle \text{FS} | \sigma_i \cdot \sigma_{i+k} | \text{FS} \rangle. \tag{3.13}
$$

In figure (2) we show its behavior at various $L$. Details of the calculation are reported in appendix A. The correlation function $G_k$ expressed in terms of the scaled position $k/L-1/2$ tends to a smooth curve at large $L$. Similar results can be obtained for the other low lying states in the perturbative multiplet. For completeness, we also show in figure (3) the spectra of one loop anomalous dimensions for all $S=0$ cyclic states of the Heisenberg model with even $8\leq L\leq16$.

## 4. Analysis of the full spectrum

In this section, we begin the analysis of the information that can be derived in the frame- work of the full Hubbard model. In order to understand the general features of the weak to

![](./images/812062753370931202_4.jpg)

Figure 3: Spectra of one loop anomalous dimensions at even $8 \leq L \leq 16$. The anomalous dimension of the n-th state is written $\Delta_{n}=L+\Delta_{n}^{(1)} g^{2}+\cdots$ and the plot shows $\Delta_{n}^{(1)}$.

strong coupling flow we analyze the full spectrum at variable $g$ and $L=4,6,8$. We follow the direct approach of Minahan [25] already applied to the case $L=4$ that we also review to fix the approach, extending it to somewhat larger values of $L$. Later we shall discuss a different approach based on the numerical solution of the Lieb-Wu equations.

### 4.1 Review of the $L=4$ case
As explained in the very nice investigation [25], in the $L=4$ case and after restricting to cyclic states with $S=0$, there are only 6 remaining states. The antiferromagnetic state is non degenerate. Its perturbative expansion involves only even powers of $g$ as an exact discrete symmetry of the model

$$
\Delta=4+\sum_{\ell \geq 1} c_{\ell} g^{2 \ell}. \tag{4.1}
$$

The full spectrum can be easily evaluated numerically and leads to the weak-strong coupling flow shown in figure (4).

As explained in [25], the perturbative expansion of $\Delta$ can be recovered quite efficiently from the expansion of the secular determinant

$$
P(\Delta, g)=\operatorname{det}\left(H_{0}+\frac{g}{\sqrt{2}} H_{1}-\Delta\right). \tag{4.2}
$$

One finds,

$$
\begin{aligned}
P(\Delta, g)= & \Delta^{6}-17 \Delta^{5}+\left(119-16 g^{2}\right) \Delta^{4}+\left(-439+176 g^{2}\right) \Delta^{3}+\left(900-716 g^{2}+32 g^{4}\right) \Delta^{2}+ \\
& +\left(-972+1276 g^{2}-160 g^{4}\right) \Delta+432-840 g^{2}+200 g^{4}. \tag{4.3}
\end{aligned}
$$

- 10 -

![](./images/812062753370931202_5.jpg)

Figure 4: Spectrum flow for the Hubbard model at $L=4$. The boldface line is the highest eigenvalue.

Replacing the expansion (4.1) and matching the coefficients we find immediately

$$
\begin{aligned}
\Delta =& 4+6\ g^2-12\ g^4+42\ g^6-318\ g^8+4524\ g^{10}-63786\ g^{12}+783924\ g^{14}-8728086\ g^{16}+ \\
& +93893622\ g^{18}-1038217494\ g^{20}+12181236666\ g^{22}+\cdots
\end{aligned} \tag{4.4}
$$

At strong coupling (large $g$) the leading behavior of the eigenvalues is linear in $g$ with a slope given by the eigenvalues of $H_1/\sqrt{2}$. These are not immediately obtained from the dispersion relation because not all multifermion states are allowed by the cyclic and $S=0$ conditions. The explicit eigenvalues of the $6\times6$ matrix $H_1/\sqrt{2}$ can be computed analytically and are

$$
0,0,-2\sqrt{2-\sqrt{2}},2\sqrt{2-\sqrt{2}},-2\sqrt{2+\sqrt{2}},2\sqrt{2+\sqrt{2}}. \tag{4.5}
$$

From the free fermion dispersion relation eq. (2.20) we see that the highest state has a slope that unambiguously identifies it with the free fermion state with the following level occupation

$$
\mathbf{n}_\uparrow=(0,3),\quad \mathbf{n}_\downarrow=(0,3). \tag{4.6}
$$

The notation means that the components of $\mathbf{n}_\sigma$ are the energy modes of the $\sigma$ type fermions according to eq. (2.20). This is nothing but the ground state of the Hubbard hopping term.

### 4.2 Extension to longer operators

The extension of the above direct approach to longer operators is in principle straightforward. However, some technical issues must be clarified in order to make the procedure systematic. We now illustrate the general features and then discuss the $L=6$ and $L=8$ cases.

To build the relevant states we first enforce the $S=0$ condition. Since $N_\uparrow=N_\downarrow$, we have automatically $S_z=0$. The operators $S^\pm$ are ineffective on doubly occupied sites.

- 11 -

Also, they cannot move around the unpaired fermions. As a consequence, we can partition the problem of listing $S=0$ states according to several sectors where we fix (a) the number and positions of the paired fermions, (b) the positions of the unpaired fermions.

Given such a sector, the fermions are no more itinerant from the point of view of the spin calculation. Then, spin zero states are simply the spin zero component of the SU(2) decomposition of the product of $N$ fundamental representations. The actual wave function of these states is obtained by taking independent antisymmetrizations with respect to pairs of up and down fermions. The independent antisymmetrizations are explicitly given by the SU(2) Young tableaux with two rows and $N/2$ columns. The Young tableaux entries in each column determine the independent antisymmetrizations.

To give an example. Suppose that we have $3+3$ fermions on a $L=6$ lattice. In a sector where there is one paired couple in the rightmost site and the unpaired fermions are in the 1, 2, 3, 4 position, we have 6 states
$$
|*,*,*,*,0,\uparrow\downarrow\rangle, \quad *\equiv\uparrow \text{ or } \downarrow, \tag{4.7}
$$
with 3+3 fermions in total. Then, the relevant two Young Tableaux with their associated antisymmetrization prescriptions are
$$
\boxed{\begin{array}{|c|c|}
\hline 1 & 2 \\
\hline 3 & 4 \\
\hline
\end{array}} \quad \boxed{\begin{array}{|c|c|}
\hline 1 & 3 \\
\hline 2 & 4 \\
\hline
\end{array}}, \tag{4.8}
$$
giving two spin zero states, in this sector.

The number of Young tableaux with $S=0$ constructed with $L/2$ up and $L/2$ down fermions is the first coefficient in (as usual $(-n)!\equiv0$ when $n\in\mathbb{N}$)
$$
\left[\frac{1}{2}\right]^{\otimes 2N}=\bigoplus_{s=0,1,2,\ldots}\frac{(2s+1)(2N)!}{(N+s+1)!(N-s)!}\,[s], \tag{4.9}
$$
where $[s]$ is the spin $s$ representation of SU(2). Hence the desired number is the Catalan number $C_{L/2}$
$$
\left[\frac{1}{2}\right]^{\otimes L}=C_{L/2}\mathbf{0}\oplus\cdots, \quad C_{L/2}=\frac{L!}{(L/2)!(L/2+1)!}. \tag{4.10}
$$

Summing over sectors with $p$ doubly occupied sites, we find the total number of $S=0$ states
$$
N_{S=0}=\sum_{p=0}^{L/2}\binom{L}{p}\binom{L-p}{L-2p}\frac{(L-2p)!}{(L/2-p)!(L/2-p+1)!}=\frac{L!(L+1)!}{((L/2)!(L/2+1)!)^2}. \tag{4.11}
$$

This number is reduced roughly by the factor $1/L$ after the cyclic projection. This is implemented rather easily as follows. We denote by $U$ the unitary operator which implements the shift symmetry. It can be checked that $U^L=1$ on half-filled states. Cyclic states $|s\rangle$ satisfy $U|s\rangle=|s\rangle$. We then consider the shift symmetrizer
$$
S=\frac{1}{L}(1+U+\cdots+U^{L-2}+U^{L-1}). \tag{4.12}
$$

$-12-$

![](./images/812062753370931202_6.jpg)

Figure 5: Spectrum flow for the Hubbard model at $L=6$. The boldface line is the highest eigenvalue.

If $\mathcal{H}_0$ is the space of zero spin states and $\mathcal{C}_0$ the space of cyclic zero spin states, it is clear that the image $S\mathcal{H}_0$ contains a basis of $\mathcal{C}_0$. Indeed, any state $|s\rangle \in \mathcal{C}_0$ can be written $|s\rangle = S|s\rangle$ and thus belongs to is in $S\mathcal{H}_0$. Hence, we can compute the image $S\mathcal{H}_0$ and apply the Gram-Schmidt orthonormalization algorithm to simultaneously produce an orthonormal basis and also remove linearly dependent states. Of course, this procedure can be applied to the states in each of the sectors that have been identified in the construction of $S=0$ states. This means, we repeat, sectors with fixed paired fermions and fixed positions of unpaired fermions. In addition, the cyclic structure of the fermion configurations in the cyclic states greatly helps in performing the orthonormalization by restricting to states with the same configurations modulo translations.

After these technical remarks, we analyze in turn the $L=6,8$ cases which, as we shall discuss, illustrate in our opinion some interesting features valid in more complicated cases.

### 4.3 The non degenerate $L=6$ case
After the spin zero and cyclic constraints, there is 1 state with no paired fermions. Thus, the antiferromagnetic state is again non degenerate. Also, there are 10 states with two pairs, 14 states with three pairs and 4 states with all fermions paired. The total dimension is 29. figure (5) illustrates the weak-strong coupling flow of the spectrum. As compared with the $L=4$ cases, we observe several crossings of the coupling dependent levels. Such crossings are well known in integrable models, where they are explained in terms of additional conserved charges commuting with the Hamiltonian [31].

It is not feasible to evaluate the secular determinant $P(\Delta,g)$ at least if we do not want to resort to numerical evaluations. Instead, we can determine the analytical perturbative expansion of the highest eigenvalue by standard perturbation theory of non degenerate eigenvalues. Let $\psi_0$ be the normalized eigenvector of $H_0$ associated with the non degenerate

eigenvalue $L$. Then, we set $\varepsilon_0 = L$ and iterate for $n \geq 1$

$$
v_{n}=-H_{1} \psi_{n-1}+\sum_{k=1}^{n-1} \varepsilon_{n-k} \psi_{k}, \tag{4.13}
$$

$$
\varepsilon_{n}=-\left(\psi_{0}, v_{n}\right), \tag{4.14}
$$

$$
\psi_{n}=\frac{1}{H_{0}-L}\left(\varepsilon_{n} \psi_{0}+v_{n}\right). \tag{4.15}
$$

The last equation is evaluated in the subspace $(\psi_0, \psi_n) = 0$ where the (pseudo) inverse operator $(H_0 - E_0)^{-1}$ exists. The perturbative expansion of the eigenvalue of $H_0 + \frac{g}{\sqrt{2}} H_1$ is then

$$
\varepsilon(g)=\sum_{n \geq 0} \varepsilon_{n}\left(\frac{g}{\sqrt{2}}\right)^{n}. \tag{4.16}
$$

This algorithm is quite fast since it is based on matrix vector multiplications only. Applying it, we find

$$
\begin{aligned}
\Delta & =6+6 g^{2}-9 g^{4}+\frac{63 g^{6}}{2}-\frac{621 g^{8}}{4}+\frac{7047 g^{10}}{8}-\frac{100953 g^{12}}{16}+ \\
& +\frac{2006127 g^{14}}{32}-\frac{46992069 g^{16}}{64}+\frac{1100850183 g^{18}}{128}-\frac{24465145473 g^{20}}{256}+ \\
& +\frac{514257122079 g^{22}}{512}-\frac{10323764001117 g^{24}}{1024}+\cdots
\end{aligned} \tag{4.17}
$$

This expansion can be compared with the BDS approach based on the Heisenberg model [11]. The agreement is perfect up to five loop order which is where the long-range Heisenberg Hamiltonian is reliable at $L = 6$. As we remarked, the Hubbard model calculation is conjectured to be exact at all orders in the loop expansions, although a proof is lacking. Of course, knowing the one-loop Bethe roots, the above expansion can also be obtained by perturbative expansion of the Lieb-Wu equations. We do not insist on this point, since we are mainly concerned with strong coupling properties.

Again, we can exploit the direct diagonalization approach to identify the free fermion state to which the $g = 0$ highest state flows. Comparing the slope of the highest eigenvalue (the maximum eigenvalue of $H_1/\sqrt{2}$) with the dispersion relation eq. (2.20) we find the two possibilities

$$
\mathbf{n}_{\uparrow}=(0, n, 5), \quad \mathbf{n}_{\downarrow}=\left(0, n^{\prime}, 5\right). \tag{4.18}
$$

where $(n, n')$ can be $(1,4)$ or $(4,1)$. The contribution of these two fermions cancels in the energy. Indeed, $\varepsilon_1 + \varepsilon_4 = 0$. This means that we flow to an excited state of the full Hubbard model. This is a clear consequence of the cyclic projection. Indeed, the ground state of the Hubbard hopping term for $L = 6$ is not cyclic and is instead odd under the transformation eq. (2.13).

The spin zero condition determines uniquely the correct combination of states which is the antisymmetric combination

$$
\frac{1}{\sqrt{2}}\left(|0,1,5\rangle_{\uparrow} \otimes|0,4,5\rangle_{\downarrow}-|0,4,5\rangle_{\uparrow} \otimes|0,1,5\rangle_{\downarrow}\right) \tag{4.19}
$$

As a check, we see that the largest eigenvalue of the explicit $29 \times 29$ matrix $H_1$ on the cyclic spin zero states is non degenerate.

$-$14 $-$

### 4.4 The degenerate $L=8$ case

On a $L=8$ lattice there are 4900 half-filled states in the full Hubbard model. After the spin zero and cyclic constraints, there are 3 states with no paired fermions, 35 states with two pairs, 108 states with three pairs, 70 states with four pairs, and 10 fully paired states. The total dimension is thus reduced to 226. This is a remarkable reduction, but the dimension remains rather high. Nevertheless, we shall be able to complete the analysis. The maximum eigenvalue of $H_0$ is threefold degenerate. It contains the antiferromagnetic state and other two states with lower anomalous dimensions. We postpone the discussion of flow. Again, it is clearly not feasible to evaluate the secular determinant. Also, we must deal with the complication that there are 3 states with eigenvalue $L=8$ at $g=0$.

We can determine the perturbative expansion of the highest eigenvalue by quantum mechanical formulae for perturbation theory of degenerate eigenvalues. In the case under consideration the degeneration is removed at second order in $g$. A very simple practical algorithm is then the following.

Let $P_0$ be the projector onto the degenerate eigenspace $\mathcal{E}_0$ with eigenvalue $E_0=L=8$. Let
$$
\mathcal{D}=P_0 H_1\left(1-P_0\right) \frac{1}{H_0-E_0}\left(1-P_0\right) H_1 P_0\tag{4.20}
$$
be a $3 \times 3$ matrix restricted to $\mathcal{E}_0$. Let its three eigenvectors be $\psi_0, \psi_0^{\prime}, \psi_0^{\prime \prime}$ in some order. They have distinct eigenvalues. We iterate for $n \geq 0$
$$
\psi_{2 n+1}=\frac{1}{H_0-E_0}\left(\sum_{\substack{k=1, \text { odd }}}^{2 n-1} \varepsilon_{2 n+1-k} \psi_k-H_1 \psi_{2 n}\right),\tag{4.21}
$$
$$
v_{2 n+2}=\sum_{\substack{k=2, \text { even }}}^{2 n} \varepsilon_{2 n+2-k} \psi_k-H_1 \psi_{2 n+1},\tag{4.22}
$$
$$
\varepsilon_{2 n+2}=-\left(\psi_0, v_{2 n+2}\right),\tag{4.23}
$$
$$
\psi_{2 n+2}=\frac{1}{H_0-E_0}\left(\varepsilon_{2 n+2} \psi_0+v_{2 n+2}\right)+\alpha_{2 n+2}^{\prime} \psi_0^{\prime}+\alpha_{2 n+2}^{\prime \prime} \psi_0^{\prime \prime}.\tag{4.24}
$$

The coefficients $\alpha_{2 n}^{\prime}, \alpha_{2 n}^{\prime \prime}$ are fixed by the condition $P_0 v_{2 n-2}=0$.

The explicit matrix $\mathcal{D}$ is rather complicated. Its eigenvalues are the three roots of the equation (of course in agreement with the one loop calculation in [8])
$$
\lambda^3+40 \lambda^2+464 \lambda+1600=0.\tag{4.25}
$$

Finding numerically the eigenvectors and applying the above algorithm with the three possible choices for $\psi_0$, we immediately find the three perturbative expansions
$$
\begin{aligned}
\Delta= & 8+11.3022 g^2-22.1706 g^4+79.5035 g^6-352.94 g^8+ \\
& +1777.24 g^{10}-9743.47 g^{12}+56739.6 g^{14}-825617 g^{16}+\cdots,
\end{aligned}\tag{4.26}
$$
$$
\begin{aligned}
\Delta^{\prime}= & 8+5.45222 g^2-7.94042 g^4+31.2193 g^6-159.093 g^8+ \\
& +896.064 g^{10}-5378.33 g^{12}+33796.9 g^{14}-222137 g^{16}+\cdots,
\end{aligned}\tag{4.27}
$$
$$
\begin{aligned}
\Delta^{\prime \prime}= & 8+3.24559 g^2-1.88899 g^4+1.2772 g^6+1.0331 g^8+ \\
& -8.2996 g^{10}+27.3006 g^{12}-70.9279 g^{14}+159.235 g^{16}+\cdots
\end{aligned}\tag{4.28}
$$

$-$15$-$

![](./images/812062753370931202_7.jpg)

Figure 6: Spectrum flow for the Hubbard model at $L=8$.

They are unavoidably numeric since they involve the algebraic irrational $\lambda$.

Again, we can compare with the BDS prediction at five loop. It is given in [11] terms of an algebraic number (denoted $\psi$) which agrees with the above three $\lambda$ roots. The agreement is complete. Of course, beyond five-loop, the above expansions derived in the Hubbard model are new and must be checked against gauge theory perturbation theory.

Coming to the analysis of the weak-strong coupling spectrum flow, we see that it is quite complicated as illustrated in figure (6). The identification of the asymptotic free fermion state is less easy but straightforward. Let us denote by

$$
|\Delta\rangle,\left|\Delta^{\prime}\right\rangle,\left|\Delta^{\prime \prime}\right\rangle,
\tag{4.29}
$$

the three states with eigenvalues expressed by the above expansion. The highest state $|\Delta\rangle$ is the antiferromagnetic state and does not cross the other states along the flow. Instead, the other two degenerate states undergo several crossing as $g$ is increased. However, it is easy to follow them along the crosses. We enumerate states starting from the highest. The two subleading states turns out to be 3rd and 8th asymptotic free fermion states. This is more clearly illustrated in figure (7) where we show the first 9 ordered eigenvalues. Several crossings can be observed and in the end, the asymptotic eigenvalues remain separated. Remarkably, at large $g$ the states $\left|\Delta^{\prime}\right\rangle$ and $\left|\Delta^{\prime \prime}\right\rangle$ are close (in energy) to partner states $\left|\widetilde{\Delta}^{\prime}\right\rangle$ and $\left|\widetilde{\Delta}^{\prime \prime}\right\rangle$ that we shall now discuss.

As a first step toward the identification of the asymptotic states with free fermion states, we analyze the eigenvalues of the matrix $H_{1} / \sqrt{2}$ and compare them with the dispersion relation. If we denote by $s, s^{\prime}, s^{\prime \prime}$ the asymptotic slopes of the energies of the three states $|\Delta\rangle,\left|\Delta^{\prime}\right\rangle,\left|\Delta^{\prime \prime}\right\rangle$, with respect to the coupling $g$, we find the following (unique) match in terms of the free fermion energies eq. (2.20),

$$
s=2\left(\varepsilon_{0}+\varepsilon_{1}+\varepsilon_{6}+\varepsilon_{7}\right),
\tag{4.30}
$$

- 16 -

![](./images/812062753370931202_8.jpg)

Figure 7: Spectrum flow for the Hubbard model at $L=8$. A detailed view of the highest 9 eigenvalues.

$$
s' = 2(\varepsilon_0 + \varepsilon_7), \tag{4.31}
$$

$$
s'' = 2(\varepsilon_1 + \varepsilon_7). \tag{4.32}
$$

The first relation permits to conclude that the highest states is nothing but the Hubbard model hopping term ground state. The other two relations identify two levels which are occupied by an up-down doublet $\uparrow\downarrow$ in momentum space. The remaining 4 fermions (two up and two down) must be placed in the remaining levels with a total zero additional energy and respecting the cyclicity and zero spin conditions. This can only be achieved by leaving the four fermions unpaired and placing them symmetrical around the zero energy value. The level population is shown in figure (8).

The first state on the left is the Hubbard model hopping ground state, as discussed. In the other states we have shown the two levels which are unambiguously filled with a pair $\uparrow\downarrow$. We have also shown a particular admissible distribution of the remaining two up, and two down fermions on the allowed four symmetrical levels. We have circled them with dashed ellipses to emphasize that this is just one component of the exact state. Indeed there are several possible distributions of the unpaired fermions. To further analyze, we take into account the spin zero condition. For both $|\Delta'\rangle$ and $|\Delta''\rangle$ the allowed states reduced to the two independent states that are obtained by antisymmetrizing two pairs of up and down fermions.

Of course, there are two states because of the SU(2) decomposition

$$
\mathbf{\frac{1}{2}} \otimes \mathbf{\frac{1}{2}} \otimes \mathbf{\frac{1}{2}} \otimes \mathbf{\frac{1}{2}} = \mathbf{2} \oplus \mathbf{1} \oplus \mathbf{1} \oplus \mathbf{1} \oplus \mathbf{0} \oplus \mathbf{0}. \tag{4.33}
$$

To be explicit, in the case of $|\Delta'\rangle$, two orthonormal states can be taken to be

$$
\begin{aligned}
|e'_1\rangle = \frac{1}{2}(|& \uparrow, \uparrow, \downarrow, \uparrow, \downarrow, \uparrow, 0, 0\rangle_p - |\uparrow, \uparrow, \downarrow, \uparrow, \uparrow, \downarrow, 0, 0\rangle_p + \\
-& |\uparrow, \uparrow, \uparrow, \downarrow, \downarrow, \uparrow, 0, 0\rangle_p + |\uparrow, \uparrow, \uparrow, \downarrow, \uparrow, \downarrow, 0, 0\rangle_p),
\end{aligned} \tag{4.34}
$$


![](./images/812062753370931202_9.jpg)

Figure 8: Asymptotic free fermion states for the perturbative multiplet at $L=8$. As explained in the text, the fermions encircled by dashed ellipses indicate one of the various (spin) components of the actual state.

$$
\begin{aligned}
|e_{2}'\rangle =& \frac{1}{2\sqrt{3}}(2| \uparrow,\uparrow,\downarrow,\downarrow,\uparrow,\uparrow,0,0\rangle_{p} - | \uparrow,\uparrow,\downarrow,\uparrow,\downarrow,\uparrow,0,0\rangle_{p} - | \uparrow,\uparrow,\downarrow,\uparrow,\uparrow,\downarrow,0,0\rangle_{p} + \\
&-| \uparrow,\uparrow,\uparrow,\downarrow,\downarrow,\uparrow,0,0\rangle_{p} - | \uparrow,\uparrow,\uparrow,\downarrow,\uparrow,\downarrow,0,0\rangle_{p} + 2| \uparrow,\uparrow,\uparrow,\uparrow,\downarrow,\downarrow,0,0\rangle_{p})
\end{aligned}
\tag{4.35}
$$

where the states $|\cdots\rangle_{p}$ are labeled with the fermion occupancy in momentum space and the momentum sites are ordered from the largest $\varepsilon_{n}$ ($\varepsilon_{0}$) to the smallest ($\varepsilon_{4}=-\varepsilon_{0}$). With this notation, the Hubbard model hopping term ground state is $|\uparrow,\uparrow,\uparrow,\uparrow,0,0,0,0\rangle$.

Introducing analogous orthonormal states $|e_{1,2}''\rangle$ for the sector spanned by $|\Delta''\rangle$ and $|\widetilde{\Delta}''\rangle$, the free fermion asymptotic states associated with $|\Delta'\rangle$ and $|\Delta''\rangle$ are suitable linear combinations of $|e_{1,2}'\rangle$ and $|e_{1,2}''\rangle$ that can be determined by perturbation theory in $H_{0}$. In both cases, the relevant asymptotic state is the one with (slightly) larger energy as can be seen from figure (8).

At first order, the degeneration is not removed. We find the same constant shift in both doublets. At second order, we find a non trivial energy splitting. We do not report the expression of the asymptotic eigenvectors which is really not useful. Instead, we give a closed form for the split eigenvalues.

If we denote by $\Delta_{\pm}'$ and $\Delta_{\pm}''$ the strong coupling expansion at second order of the doublets eigenvalues, we find

$$
\Delta_{\pm}' = 2g\left(\varepsilon_{0}+\varepsilon_{7}\right)+\frac{23}{4}+\frac{1}{g}\delta_{\pm}'+\dots
\tag{4.36}
$$

where

$$
\delta_{\pm}' = \frac{1}{128\sqrt{2}}\sqrt{882+584\sqrt{2}+\sqrt{25906+16303\sqrt{2}}}
\tag{4.37}
$$

- 18 -

$$
\pm \frac{1}{64} \sqrt{132+88 \sqrt{2}-2 \sqrt{7330+5183 \sqrt{2}}}=\left\{\begin{array}{l}
0.301715 \\
0.183563
\end{array}\right.\tag{4.38}
$$

The expansion of the second eigenvalue is instead
$$
\Delta_{ \pm}^{\prime \prime}=2 g\left(\varepsilon_{1}+\varepsilon_{7}\right)+\frac{23}{4}+\frac{1}{g} \delta_{ \pm}^{\prime \prime}+\ldots\tag{4.39}
$$
where
$$
\delta_{ \pm}^{\prime \prime}=\frac{1}{128} \sqrt{1026+79 \sqrt{2}+\sqrt{724177-\frac{157633}{\sqrt{2}}}}\tag{4.40}
$$

$$
\pm \frac{1}{16} \sqrt{10-3 \sqrt{2}-\sqrt{29-\frac{1}{\sqrt{2}}}}=\left\{\begin{array}{l}
0.383745 \\
0.300994
\end{array}\right.\tag{4.41}
$$

Notice that this is correct for $g>0$. Indeed, in general, the above strong coupling expansions must be written with $g \rightarrow|g|$ to respect the exact $g \rightarrow-g$ symmetry of the spectrum.

As a final comment, we remark that the above complicated expressions have been checked explicitly against the numerical evaluation of the levels with full agreement.

### 4.5 Summary of the results for $L=8$

In conclusion, taking the upper states and evaluating the energy levels, we find the following result in the case $L=8$. The AF state has been already discussed. The other two states in the perturbative multiplet have the following strong coupling expression of the anomalous dimensions
$$
\Delta_{+}^{\prime}=\sqrt{2\left(4+2 \sqrt{2}+\sqrt{20+14 \sqrt{2}}\right)} g+\frac{23}{4}+\frac{1}{g} \delta_{+}^{\prime} \ldots,\tag{4.42}
$$

$$
\Delta_{+}^{\prime \prime} \equiv \Delta_{\mathrm{FS}}=2 \sqrt{2+\sqrt{2+\sqrt{2}}} g+\frac{23}{4}+\frac{1}{g} \delta_{+}^{\prime \prime}+\ldots\tag{4.43}
$$

## 5. Direct analysis of the Lieb-Wu equations

A posteriori, we can make some general comments on the previous analysis based on direct diagonalization. We are considering an Hamiltonian of the form
$$
H=H_{A}+g H_{B},\tag{5.1}
$$
where $g$ is a coupling. As $g$ flows from 0 to $\infty$, each eigenstate of $H$ flows from an eigenstate of $H_{A}$ to an eigenstate of $H_{B}$. It is clear that exact diagonalization permits to follow the flow for generic $H_{A}, H_{B}$, however the method is unrealistic for large dimension of the Hilbert space. The problem is very general and, as such, has no simple solution. Of course, what saves the day in our context is integrability. In principle, the Lieb-Wu equations can

be solved for a particular state, i.e. typical configuration of Bethe roots, without the need for huge calculations of eigensystems. Extending the calculation from $g=0$, where the Bethe roots are those of the Heisenberg model, up to large $g$ should permit in principle to determine the strong coupling behavior of any state.

However, it is also clear that the general task of solving the Lieb-Wu equations for all states in the perturbative multiplet and fixed $L$ (possibly large) is not easy [32]. However, there are exceptions. These are the states where some general knowledge is available about the limiting distribution of Bethe roots at large $L$. In the next sections, we shall discuss two important examples. The first is the AF state. At half-filling, it is the unique state with completely real solutions to the Lieb-Wu equations. The second example is the lightest state $|\mathrm{FS}\rangle$. Here, we know that at large $L$ the Bethe roots condense on two symmetric curves in the complex plane and we can exploit this information to evaluate them at least numerically. This case is considerably more difficult than the AF state because the Bethe Ansatz solution is complex.

Notice that in principle, one could use the original all-loop BDS equations. This calculation would be reliable in the thermodynamical limit including finite size corrections if needed. In this paper, we are concerned with finite $L$ properties, and therefore we have explored the explicit (numerical) solution of the more difficult Lieb-Wu equations.

### 5.1 Real solution: the antiferromagnetic state

At half filling, the AF state is described by the only genuine real solution of the Lieb-Wu equations. They read

$$
L q_{n}=2 \pi I_{n}+2 \sum_{j=1}^{L / 2} \tan ^{-1}\left[2\left(u_{j}-\sqrt{2} g \sin \left(q_{n}+\phi\right)\right)\right],\qquad(5.2)
$$

$$
2 \pi J_{k}=2 \sum_{j=1}^{L / 2} \tan ^{-1}\left(u_{k}-u_{j}\right)-2 \sum_{m=1}^{L} \tan ^{-1}\left[2\left(u_{k}-\sqrt{2} g \sin \left(q_{m}+\phi\right)\right)\right],\qquad(5.3)
$$

where, in our problem, $n=1, \ldots, L$, and $k=1, \ldots, L / 2$. We focus on the case $N=4 p$ where $\phi=\pi /(2 L)$ and the Bethe quantum numbers are

$$
\left\{I_{n}\right\}=\{0,1,2, \ldots, L-1\},\qquad(5.4)
$$

$$
\left\{J_{k}\right\}=\left\{-\frac{2 p-1}{2},-\frac{2 p-3}{2}, \ldots, \frac{2 p-3}{2}, \frac{2 p-1}{2}\right\}.\qquad(5.5)
$$

The iterative solution of the above equations is quite stable, as it is common when dealing with real solutions. Following the evolution at $g \rightarrow \infty$ of the energy of the highest state, we have checked that it flows at strong coupling to the ground state $\left|\psi_{0}\right\rangle$ of the Hubbard model hopping term. In momentum space, this is the state where all positive energy levels are doubly occupied

$$
\left|\psi_{0}\right\rangle=\prod_{n=1}^{L-1} \prod_{\sigma=\uparrow, \downarrow} a_{\sigma, p_{n}}^{\dagger}|0\rangle.\qquad(5.6)
$$

- 20 -

<table>
<thead>
<tr>
<th>$L$</th>
<th>8</th>
<th>12</th>
<th>16</th>
<th>20</th>
<th>24</th>
<th>28</th>
<th>32</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\delta_L$</td>
<td>0.0250979</td>
<td>0.0245631</td>
<td>0.0243433</td>
<td>0.0242308</td>
<td>0.0241652</td>
<td>0.0241234</td>
<td>0.024095</td>
</tr>
</tbody>
</table>

Table 1: Coefficient of the second order correction to the energy of the AF state at finite $L \in 4\mathbb{N}$ and large $g$. A simple polynomial extrapolation at $L \to \infty$ gives $\lim_{L \to \infty} \delta_L = 0.0240(1)$.

The AF state remains non degenerate at all couplings and we can apply first order perturbation theory to determine the first subleading correction at large $g$. Also, from the numerical solution of the Lieb-Wu equations, we can evaluate the finite $L$ next-to-subleading correction $\sim 1/g$.

Summing up, our result for the expansion of the anomalous dimension of the AF state at finite $L$ and large $g$ reads

$$
\frac{\Delta_{\mathrm{AF}}(g, L)}{L}=\frac{\sqrt{2}}{L \sin \frac{\pi}{2 L}} g+\frac{3}{4}+\delta_{L} \frac{1}{g}+\cdots
\tag{5.7}
$$

The first term is the energy of the Hubbard model hopping term ground state with twist. Its explicit formula comes from the sum

$$
2 \sqrt{2} \sum_{n=-L / 4}^{L / 4-1} \cos \left(\frac{2 \pi n}{L}+\frac{\pi}{2 L}\right)=\frac{\sqrt{2}}{\sin \frac{\pi}{2 L}}.
\tag{5.8}
$$

The coupling independent term is a universal constant. It is evaluated by computing the matrix element

$$
L-\frac{1}{L}\left\langle\psi_{0}\right| \sum_{p, q} a_{\uparrow, p}^{\dagger} a_{\uparrow, p} a_{\downarrow, q}^{\dagger} a_{\downarrow, q}\left|\psi_{0}\right\rangle=L-\frac{1}{L}\left(\frac{L}{2}\right)^{2}=\frac{3}{4} L.
\tag{5.9}
$$

The next correction takes the numerical values reported in table (1). The above result is an exact expansion in inverse powers of $g$ at fixed $L$. As a non trivial check, it can be compared with the result eq. (3.7) by taking the $L \to \infty$ limit term by term. We obtain

$$
\lim _{L \rightarrow \infty} \frac{\Delta_{\mathrm{AF}}^{\text {strong }}(g, L)}{L}=\frac{2 \sqrt{2}}{\pi} g+\frac{3}{4}+0.0240(1) \frac{1}{g}+\ldots.
\tag{5.10}
$$

This is in full agreement with eq. (3.7) since

$$
\delta_{\infty} \equiv \lim _{L \rightarrow \infty} \delta_{L}=\frac{7}{8 \pi^{3} \sqrt{2}} \zeta(3)=0.0239866.
\tag{5.11}
$$

### 5.2 A complex solution: the $|\mathrm{FS}\rangle$ state

The general geometry and symmetry of the Bethe roots for the $|\mathrm{FS}\rangle$ state at large $L$ are of great utility in determining them at finite $L \in 4\mathbb{N}$. As we shall discuss, there are numerical difficulties when $L=4 p$ with even $p$, i.e. $L \bmod 8=0$. Instead the case $L=4 p$ with odd $p$, i.e. $L \bmod 8=4$, can be treated successfully. In the next sections we shall present our detailed results for the non trivial cases $L=12,20$.

- 21 -

#### 5.2.1 $L=12$

At $L=12$ there are 14 states in the perturbative multiplet and many more extra states in the full Hubbard model. We have determined the one loop Bethe roots for the $|\text{FS}\rangle$ state as we now discuss. The six Bethe roots are non zero and symmetric under $u \to -u$. This reduces the problem to solving three polynomial equations in three variables. Four roots are expected to be complex and the other two real. Applying the resultant technique we find that the complex roots are among the solutions of the following polynomial

$$
\begin{aligned}
R(x) &= 1 - 291816\,x^2 + 2476695728\,x^4 - 4740875459840\,x^6 + 2716015001869568\,x^8 \\
&\quad -587934012140484608\,x^{10} + 5336517749102178304\,x^{12} \\
&\quad -1893188143985026269184\,x^{14} + 2703610477708125093888\,x^{16} \\
&\quad -119124909860572824600576\,x^{18} - 345397582972412910108672\,x^{20} \\
&\quad +1499936486421645590790144\,x^{22} + 8744914427777415217414144\,x^{24} \\
&\quad -1155658862325646445510656\,x^{26} + 7466630646963993812402176\,x^{28} \\
&\quad -273168717774897644721668096\,x^{30} + 46033164223912000241008640\,x^{32} \\
&\quad -219403347416043302531629056\,x^{34} + 965423684859142279840923648\,x^{36} \\
&\quad +4267809644452908595622707200\,x^{38} + 886394409006105612647399424\,x^{40} \\
&\quad -2540126101042720433221140480\,x^{42} - 10295374756958736948626718720\,x^{44} \\
&\quad -27408343376808874282372300800\,x^{46} - 16677333147947189938421760000\,x^{48} \\
&\quad +23395667776149943429890048000\,x^{50} + 48702367142746624075235328000\,x^{52} \\
&\quad +43027672720198395903344640000\,x^{54} + 21488277238759969133690880000\,x^{56} \\
&\quad +5377757322242364014592000000\,x^{58} +4964083682069874475008000000x^{60}. \tag{5.12}
\end{aligned}
$$

This polynomial contains several spurious solutions and is perhaps not the most economical choice. Nevertheless, it contains the exact roots and we quote it for the reader's convenience. $^1$ The roots associated with the $|\text{FS}\rangle$ state are

$$
u_1 = -u_2 = \alpha, \tag{5.13}
$$

$$
u_3 = -u_4 = \overline{\alpha}, \tag{5.14}
$$

$$
u_5 = -u_6 = \beta, \tag{5.15}
$$

where

$$
\alpha = 0.6762450414055523 + 0.9936333912043784\ i, \tag{5.16}
$$

$$
\beta = 0.6780174422473694, \tag{5.17}
$$

in agreement with the results in [20]. We start from this solution plus the condition for the momenta $q$

$$
q_n = \frac{2\pi}{L}(n-1),\quad 1 \leq n \leq L, \tag{5.18}
$$

---
$^1$A single polynomial for the case $L=8$ is quoted in [11]. However, there is a misprint in one coefficient. The correct resolvent is $R(x) = -1 + 648\ x^2 - 36464\ x^4 + 81664\ x^6 - 16128\ x^8 + 460800\ x^{10} + 552960\ x^{12}$.

---
$-$22$-$

![](./images/812062753370931202_10.jpg)

![](./images/812062753370931202_11.jpg)

Figure 10: State $|\text{FS}\rangle$ at $L=12$. Evolution of the Bethe parameters $q_1,\dots,q_{12}$ up to $g=15$.

which is valid at $g=0$. Then, we increase $g$ and determine step by step the new solution of the full Lieb-Wu equations. This procedure is numerically stable and permits to determine the energy flow as well as the change in the Bethe momenta and $u$ variables.

We show in figure (9), the evolution of the Bethe Ansatz solution $\{u_i\}$ as $g$ is increased up to $g=15$. More interestingly, we show in figure (10), the evolution of the momenta. The flow permits to derive the asymptotic occupancy in the free fermion limit. In terms of the indices $n$, the final occupation of states is as follows. There are singly occupied modes with mode indices

$$n=0,11,2,9,3,8,5,6,\tag{5.19}$$

![](./images/812062753370931202_12.jpg)

**Figure 11:** State $|\text{FS}\rangle$ at $L=12$. Coupling dependence of $\Delta_{\text{FS}}(g)$.

and two doubly occupied levels at modes

$$n=1,10.\tag{5.20}$$

As in the $L=8$ case, the singly occupied levels contain 4 up fermions and 4 down fermions in a $S=0$ combination. There are several possibilities and only one can be selected by perturbation theory. We do not pursue the strong coupling correction analytically. Instead we determine the leading term at large $g$ and the subleading contribution that can be obtained by first order perturbation theory. The leading contribution (the coefficient of $g$ at large $g$) is

$$2(\varepsilon_1+\varepsilon_{10})=2\sqrt{2}\left(\cos\frac{5\pi}{24}+\cos\frac{41\pi}{24}\right)=4\cos\frac{\pi}{24}=2\sqrt{2+\sqrt{2+\sqrt{3}}}.\tag{5.21}$$

The subleading term can be computed analytically and is $26/3$. Hence we have found that for the $|\text{FS}\rangle$ state at $L=12$ we have

$$\Delta_{\text{FS}}=2\sqrt{2+\sqrt{2+\sqrt{3}}}\,g+\frac{26}{3}+0.597(1)\frac{1}{g}+\cdots,\tag{5.22}$$

where we have also indicated the fitted coefficient of the NNLO term in the strong coupling expansion. The agreement with the calculated energy is shown in figure (11).

The asymptotic fermion configuration is shown in figure (12) where we simply draw the single particle level and their occupation without specifying the spin of the singly occupied levels.

$-$ $24$ $-$

![](./images/812062753370931202_13.jpg)

Figure 12: State |FS⟩ at $L=12$. Fermion configuration at strong coupling.

### 5.2.2 $L=16$

We can repeat the analysis for $L=16$. In this case, we failed to obtain an exact resultant encapsulating the exact one loop Bethe roots. Instead, we have computed them numerically.
The symmetry of the 8 roots is

$$
u_1 = -u_2 = \alpha, \tag{5.23}
$$

$$
u_3 = -u_4 = \overline{\alpha}, \tag{5.24}
$$

$$
u_5 = -u_6 = \beta, \tag{5.25}
$$

$$
u_7 = -u_8 = \overline{\beta}, \tag{5.26}
$$

where

$$
\alpha = 0.9011983985707239 + 0.5000879064837407\,i, \tag{5.27}
$$

$$
\beta = 0.915478863907937 + 1.4850185722704357\,i. \tag{5.28}
$$

The imaginary part of $\alpha$ is quite near to $\frac{1}{2}$. This is a source of instability in the solution of the Lieb-Wu equations. Indeed, as $g$ is increased, we numerically observe that four of the Bethe roots tend quickly to a singular configuration. This problem does not occur if $L \bmod 8 = 4$. We do not try to deal with the singularities of the $L=16$ case and instead study the more involved, but more stable case $L=20$.

### 5.2.3 $L=20$

The 10 one-loop Bethe roots satisfy the following conditions:

$$
u_1 = -u_2 = \alpha \in \mathbb{R}_{>0}, \tag{5.29}
$$

$$
u_3 = -u_4 = \beta, \tag{5.30}
$$


![](./images/812062753370931202_14.jpg)

Figure 13: State $|\text{FS}\rangle$ at $L=20$. Evolution of the Bethe parameters $u_1,\dots,u_{10}$ up to $g=18$.

$$
u_{5}=-u_{6}=\overline{\beta}, \tag{5.31}
$$

$$
u_{7}=-u_{8}=\gamma, \tag{5.32}
$$

$$
u_{9}=-u_{10}=\overline{\gamma}. \tag{5.33}
$$

We find the following numerical solution

$$
\alpha=1.1309564538305164, \tag{5.34}
$$

$$
\beta=1.1310261843923932+0.9998455911389437 i, \tag{5.35}
$$

$$
\gamma=1.1784184821892867+1.980402937535511 i. \tag{5.36}
$$

We show in figure (13), the evolution of the Bethe Ansatz solution $\{u_i\}$ as $g$ is increased up to $g \simeq 18$. figure (14) shows the evolution of the momenta. Again, we can derive the asymptotic occupancy in the free fermion limit. In terms of the indices $n$, the singly occupied modes are

$$
n=0,1,3,4,5,6,7,9,10,11,13,14,15,16,18,19, \tag{5.37}
$$

and there are again 2 doubly occupied levels at modes

$$
n=2,17. \tag{5.38}
$$

The singly occupied levels contain 8 up fermions and 8 down fermions in a $S=0$ combination. The leading contribution to the anomalous dimension (the coefficient of $g$ at large $g$) is

$$
2(\varepsilon_{2}+\varepsilon_{17})=2 \sqrt{2}\left(\cos \frac{9 \pi}{40}+\cos \frac{69 \pi}{40}\right)=4 \cos \frac{\pi}{40}. \tag{5.39}
$$

- 26 -

![](./images/812062753370931202_15.jpg)

= 18.

![](./images/812062753370931202_16.jpg)

Figure 15: State $|\text{FS}\rangle$ at $L=20$. Coupling dependence of $\Delta_{\text{FS}}(g)$.

The subleading term can be computed analytically and is $73/5$. Hence, in summary, the $|\text{FS}\rangle$ state at $L=20$ admits the strong coupling expansion

$$
\Delta_{\text{FS}}=4 \cos \frac{\pi}{40} g+\frac{73}{5}+0.953(1) \frac{1}{g}+\cdots, \tag{5.40}
$$

where we have also indicated the fitted coefficient of the NNLO term in the strong coupling expansion. As before, we shown the agreement with the calculated energy is shown in figure (15).

The asymptotic fermion configuration is completely similar to the $L=12$ case. The doubly occupied levels are in the middle of the single particle positive energy levels. The other positive energy levels are singly occupied, as well as their mirror levels with negative energy.

### 5.2.4 Conjecture for the $|\mathrm{FS}\rangle$ state at general $L=4(2 k+1)$

The results at $L=12$ and 20 are quite symmetric and completely similar. It is natural to conjecture that for all $L=4(2 k+1)$, the pattern is identical. This means that the $|\mathrm{FS}\rangle$ state is obtained at strong coupling as the state with the following properties.

1.  The positive energy single fermion levels are all occupied with one fermion, with the exception of the central levels with mode numbers
    $$
    n=k, L-k-1. \tag{5.41}
    $$
    These are doubly occupied.

2.  The negative energy levels which are mirror of singly occupied levels are also singly occupied.

3.  The negative energy levels which are mirror of doubly occupied levels are empty.

Evaluating the leading and subleading contributions to the anomalous dimension gives the strong coupling expansion
$$
\Delta_{\mathrm{FS}}(g, L)=4 \cos \frac{\pi}{2 L} g+\frac{3 L^{2}-2 L+8}{4 L}+\mathcal{O}\left(\frac{1}{g}\right). \tag{5.42}
$$

Eq. (5.42) is expected to be the exact strong coupling expansion at any fixed $L=4(2 k+1)$. We conclude with a comment about the other cases $L=4(2 k)$. The explicit results at $L=8$ and preliminary data at $L=16$ suggest that the $|\mathrm{FS}\rangle$ state is again flowing to a state like the above with the same expressions for the leading and subleading terms in the strong coupling expansion. Indeed, at $L=8$, the above parametrization reproduces the exact result that we derived by exact diagonalization. However, we have not enough empirical support to firmly establish this result.

## 6. Summary of results and discussion

To summarize, we report our main results for the large $g$ expansion at fixed $L$ of the anomalous dimension of the antiferromagnetic and $|\mathrm{FS}\rangle$ states. For the antiferromagnetic operator we have found
$$
\frac{\Delta_{\mathrm{AF}}(g, L)}{L}=\frac{\sqrt{2}}{L \sin \frac{\pi}{2 L}} g+\frac{3}{4}+\delta_{\mathrm{AF}, L} \frac{1}{g}+\cdots. \tag{6.1}
$$

The first two terms are exact. About the last one, we have shown how to compute it for large $L$. We have also provided the asymptotic limit
$$
\delta_{\mathrm{AF}, \infty}=\frac{7}{8 \pi^{3} \sqrt{2}} \zeta(3). \tag{6.2}
$$

- 28 -

For the folded string dual, we have found (at finite $L \bmod 8 = 4$)

$$
\Delta_{\mathrm{FS}}(g, L)=4 \cos \frac{\pi}{2 L} g+\frac{3 L^{2}-2 L+8}{4 L}+\delta_{\lambda, L} \frac{L}{g}+\cdots,
\tag{6.3}
$$

where we have explicitly computed

$$
\delta_{\lambda, 12}=0.0498(1), \quad \delta_{\lambda, 20}=0.0477(1).
\tag{6.4}
$$

In particular, the leading and subleading terms of these expressions are exact at all finite $L$. As such they are beyond the region of applicability of the BDS approximation which, due to wrapping terms, is limited to $L \to \infty$. Indeed, they are a genuine result provided by the Hubbard model framework where they express properties of specific free fermion states.

As we remarked, our expansions are obtained by taking $\lambda'$ large at fixed $L$. An important issue if then the comparison with the BMN limit. Indeed, as pointed out by Minahan [25], it is not totally clear how to recover the $(\lambda')^{1 / 4}$ behavior of string states from the strong coupling expansion of the Hubbard model. The tricky proposal in [25] is based on the assumption that at large $g$ there are doubly occupied levels with small single particle energy of order $1 / L$. Unfortunately, we have seen that this is not valid for the considered states with many excitations. The doubly occupied levels give an asymptotic slope $\Delta / g$ which is of order 1 for the minimal energy state $|\mathrm{FS}\rangle$.

The BMN limit is obtained by fixing $\lambda'=\lambda / J^{2}$ and taking $J \to \infty$ where $J=L / 2$ is the angular momentum of the semiclassical dual state. We have seen that at finite $L$ there can be correction terms (like eq. (3.12)) with an ambiguity in the $L, \lambda' \to \infty$ limit. If we want to compare with the BMN limit we have to enforce the correct ordering and require $\lambda' \ll L$. Let us see the role of this constraint in the case of our data at $L=12$ and 20.
The BMN anomalous dimension of the folded string can be written

$$
\lim _{L \rightarrow \infty} \frac{\Delta_{\mathrm{FS}}\left(\lambda^{\prime} L^{2}, L\right)}{L} \equiv F\left(\lambda^{\prime}\right)=\frac{1}{2} K(q)\left[\frac{4 q \lambda^{\prime}}{\pi^{2}}+\frac{1}{E(q)^{2}}\right]^{1 / 2},
\tag{6.5}
$$

where $q=q\left(\lambda^{\prime}\right)$ is the solution of

$$
\frac{4 \lambda^{\prime}}{\pi^{2}}=\frac{1}{(K(q)-E(q))^{2}}-\frac{1}{E(q)^{2}},
\tag{6.6}
$$

and $K(q), E(q)$ are standard complete elliptic integrals of the first and second kind.

We show in figure (16) the comparison of $F\left(\lambda^{\prime}\right)$ and the ratio $\Delta / L$ for the lightest state at $L=12$ and 20. The left panel shows that there is good agreement for $\lambda'$ up to about $3-4$, reasonably within the BMN scaling window. This is a rather large value suggesting that the agreement is working beyond perturbation theory. Indeed, we show in the same figure the 8th and 9th order perturbative expansions of $F\left(\lambda^{\prime}\right)$ which read

$$
\begin{aligned}
F\left(\lambda^{\prime}\right)= & 1+0.089004 \lambda^{\prime}-0.013272\left(\lambda^{\prime}\right)^{2}+0.002839\left(\lambda^{\prime}\right)^{3}-0.000676\left(\lambda^{\prime}\right)^{4} \\
& +0.000172\left(\lambda^{\prime}\right)^{5}-0.000047\left(\lambda^{\prime}\right)^{6}+0.000014\left(\lambda^{\prime}\right)^{7}-4.315511 \cdot 10^{-6}\left(\lambda^{\prime}\right)^{8} \\
& +1.424401 \cdot 10^{-6}\left(\lambda^{\prime}\right)^{9}+\ldots.
\end{aligned}
\tag{6.7}
$$

$-$29 $-$

![](./images/812062753370931202_17.jpg)

Figure 16: Ratio $\Delta/L$ for the state $|{\rm FS}\rangle$ as a function of $\lambda'$ at $L=12,20$, and in the BMN limit $L\rightarrow\infty$.

The two curves suggest a convergence radius around $\lambda'\simeq3$, somewhat smaller than the region of agreement. If so, this could be a signal that we are slowly recovering the BMN result.

## 7. Conclusions

In this paper we have considered a particular class of gauge invariant operators in the planar limit of $\mathcal{N}=4$ SYM. These are length $L$ single trace operators in the SU(2) sector with zero spin. Remarkable members of this class are the so-called antiferromagnetic operator and the dual of the semiclassical folded string state.

We have assumed a recently proposed relation between the gauge theory and a Hubbard-like model of itinerant fermions. This approach permits to evaluate the anomalous dimensions of the gauge invariant operators at all couplings. In particular, we access the strongly coupled region at fixed $L$.

Our investigation has been based on two complementary techniques. First, we have evaluated the full spectrum of the model for operators with $L=4,6,8$. This has provided useful information about the mutual relation between the states of the Hubbard model and the perturbative multiplet of states with a clean relation to gauge invariant operators.

Then, we have investigated the numerical solutions of the Lieb-Wu equations. They are a powerful tool that permits, in principle, to follow a particular state from weak to strong coupling in a totally controlled way. Our results are very simple explicit formulas for the strong coupling expansion of the anomalous dimensions. They are expressed in terms of specific free fermion states whose properties are easily computable.

We hope that this investigation will be useful to shed some additional light over the non perturbative features of the states in the multiplet as well as over the connection

- 30 -

between the gauge theory and the underlying integrable Hubbard model. This work can be extended in several directions. Some are rather obvious like (a) $S \neq 0$ states in the SU(2) sector, (b) sectors different than SU(2), (c) other particular states like for instance the dual of the semiclassical circular string solution. In principle, it should be possible to study the strong coupling region by direct perturbative expansion of the Lieb-Wu equations although this is a delicate analysis [33]. This could be a valuable effort. It would be very nice to reproduce in some limit of the Hubbard model the true strong coupling behavior of string states, i.e. the typical relation $\Delta \sim(\lambda')^{1 / 4}$ for the light states. This is non trivial at the numerical level since large $\lambda'$ and irrelevance of possible corrections like (3.12) would require quite large lattice sizes $L$.

The most interesting extension seems to be a detailed study of the other light states in the perturbative multiplet, perhaps exploiting in a deeper way their nearly-BPS nature [34]. As $L$ increases, our investigation shows that there is a growing number of states with a smooth $L \rightarrow \infty$ limit. This is not unexpected and they should be described by a suitable effective theory in the continuum. This line of analysis have been discussed in [35] in the context of the loop-corrected Heisenberg model and should be extended to the Hubbard model [36]. For these states, the finite $L$ analysis of their associated Lieb-Wu solution could provide some hindsight on the possible limiting distribution of Bethe roots and suggest a strategy to evaluate their thermodynamical limit. In the end, this could lead to new examples of AdS/CFT specific dualities. Indeed, the search of new string states dual to novel Bethe Ansatz solutions seems to be far from the end [36].

## Acknowledgments
We thank G. F. De Angelis for conversations about rigorous results on lattice fermion models.

## A. Exact diagonalization of the $S=0$ sector of the Heisenberg model
In this appendix, we report some useful techniques for exact diagonalization of Heisenberg- like models in sectors with fixed SU(2) spin. As discussed in the analysis of RSS, the two loop dilatation operator is

$$
\mathcal{D}=L+\frac{g^{2}}{2} \sum_{i}\left(1-\sigma_{i} \cdot \sigma_{i+1}\right)-\frac{g^{4}}{4} \sum_{i}\left(3-4 \sigma_{i} \cdot \sigma_{i+1}+\sigma_{i} \cdot \sigma_{i+2}\right)+\cdots, \quad \text { (A.1) }
$$

where we assume periodic boundary conditions. This operator acts in the perturbative multiplets, i.e. on the $S=0$ cyclic states of the Heisenberg spin model. We can write the various $\sigma_{i} \cdot \sigma_{j}$ terms by means of transpositions operators flipping spins at sites $i, j$

$$
P_{i, j}=\frac{1}{2}\left(1+\sigma_{i} \cdot \sigma_{j}\right). \quad \text { (A.2) }
$$

The dilatation operator can be rewritten

$$
\mathcal{D}=L+g^{2} \sum_{i}\left(1-P_{i, i+1}\right)+\frac{g^{2}}{2} \sum_{i}\left(4 P_{i, i+1}-P_{i, i+2}-3\right)+\cdots \quad \text { (A.3) }
$$

- 31 -

where we notice that under periodic identification of the boundaries

$$
P_{i, i+2}=P_{i, i+1} P_{i+1, i+2} P_{i, i+1}, \tag{A.4}
$$

and the full operator is written in terms of elementary transpositions only, i.e. transpositions of nearest neighboring spins. Also, cyclic states are states invariant under a lattice shift $T$ that can also be written in terms of elementary transpositions as the product

$$
T=P_{L-1, L} \cdots P_{2,3} P_{1,2}. \tag{A.5}
$$

We are interested in diagonalizing the dilatation operator in the $S=0$ sector. The states in this sector are associated with standard SU(2) Young tableaux with two rows and $L/2$ columns, as already discussed. However, now we are no more interested in the detailed spin positions and we do not need translating the YT in explicit anti-symmetrized states. Instead, we can exploit an old computationally efficient parametrization of orthogonal states [37] which turns out to be very suitable for our problem.

We associate a state $|Y\rangle$ to each distinct spin zero Young tableaux $Y$. Then, the nearest-neighbor transposition $P_{k,k+1}$ has the following matrix elements

$$
\left\langle Y^{\prime}\left|P_{k, k+1}\right| Y\right\rangle=\left\{\begin{aligned}
\rho_{k}(Y) \equiv \frac{1}{d_{k}(Y)}, & & Y=Y^{\prime} \\
\sqrt{1-\rho^{2}}, & & Y^{\prime} \text { is obtained from } Y \text { by } k \leftrightarrow k+1 \\
0, & & \text { otherwise. }
\end{aligned}\right. \tag{A.6}
$$

The number $d_{k}(Y)$ is the axial distance between the labels $k$ and $k+1$ inside $Y$. It is defined as the sum of steps which are required to move from $k$ to $k+1$. The steps are positive on the right and upward and negative otherwise.

The above representation of states is not very convenient for the analysis of generic correlation functions. However, it is quite efficient for energies and SU(2) invariant correlation functions.

## References

[1] J.M. Maldacena, *The large-N limit of superconformal field theories and supergravity*, Adv. Theor. Math. Phys. **2** 1998 231 [hep-th/9711200].

[2] S.S. Gubser, I.R. Klebanov and A.M. Polyakov, *Gauge theory correlators from non-critical string theory*, Phys. Lett. B **428** 1998 105 [hep-th/9802109].

[3] E. Witten, *Anti-de Sitter space and holography*, Adv. Theor. Math. Phys. **2** 1998 253 [hep-th/9802150].

[4] V.A. Kazakov, A. Marshakov, J.A. Minahan and K. Zarembo, *Classical / quantum integrability in AdS/CFT*, JHEP **05** 2004 024 [hep-th/0402207].

[5] I.R. Klebanov, *Tasi lectures: introduction to the AdS/CFT correspondence*, hep-th/0009139.

- 32 -

[6] For recent reviews, see for instance: J. Plefka, *Spinning strings and integrable spin chains in the AdS/CFT correspondence*, hep-th/0507136;
K. Zarembo, *Semiclassical bethe ansatz and AdS/CFT*, Comptes Rendus Physique **5** (2004) 1081–1090 [hep-th/0411191];
N. Beisert, *Higher-loop integrability in $N=4$ gauge theory*, Comptes Rendus Physique **5** (2004) 1039–1048 [hep-th/0409147].

[7] D. Berenstein, J.M. Maldacena and H. Nastase, *Strings in flat space and pp waves from $N=4$ super Yang-Mills*, JHEP **04** (2002) 013 [hep-th/0202021].

[8] N. Beisert, C. Kristjansen and M. Staudacher, *The dilatation operator of $N=4$ super Yang-Mills theory*, Nucl. Phys. **B 664** (2003) 131 [hep-th/0303060]; *The dilatation operator of $N=4$ super Yang-Mills theory and integrability*, Phys. Rept. **405** (2005) 1 [hep-th/0407277].

[9] J.A. Minahan and K. Zarembo, *The bethe-ansatz for $N=4$ super Yang-Mills*, JHEP **03** (2003) 013 [hep-th/0212208].

[10] D. Serban and M. Staudacher, *Planar $N=4$ gauge theory and the inozemtsev long range spin chain*, JHEP **06** (2004) 001 [hep-th/0401057].

[11] N. Beisert, V. Dippel and M. Staudacher, *A novel long range spin chain and planar $N=4$ super Yang-Mills*, JHEP **07** (2004) 075 [hep-th/0405001].

[12] A. Rej, D. Serban and M. Staudacher, *Planar $N=4$ gauge theory and the Hubbard model*, JHEP **03** (2006) 018 [hep-th/0512077].

[13] K. Zarembo, *Antiferromagnetic operators in $N=4$ supersymmetric yang- mills theory*, Phys. Lett. **B 634** (2006) 552 [hep-th/0512079];

[14] E.H. Lieb and F.Y. Wu, *Absence of Mott transition in an exact solution of the short-range, one-band model in one dimension*, Phys. Rev. Lett. **20** (1968) 1445
Erratum, Phys. Rev. Lett. **21** (1968) 192.

[15] J. Ambjørn, R.A. Janik and C. Kristjansen, *Wrapping interactions and a new source of corrections to the spin-chain/string duality*, Nucl. Phys. **B 736** (2006) 288 [hep-th/0510171].

[16] N. Mann, *The SU(2) long range bethe ansatz and continuous integrable systems*, hep-th/0605028.

[17] R. Hernandez, E. Lopez, A. Perianez and G. Sierra, *Finite size effects in ferromagnetic spin chains and quantum corrections to classical strings*, JHEP **06** (2005) 011 [hep-th/0502188].

[18] N. Beisert, A.A. Tseytlin and K. Zarembo, *Matching quantum strings to quantum spins: one-loop vs. finite-size corrections*, Nucl. Phys. **B 715** (2005) 190 [hep-th/0502173];
S. Schafer-Nameki, M. Zamaklar and K. Zarembo, *Quantum corrections to spinning strings in $AdS_5\times S^5$ and Bethe ansatz: a comparative study*, JHEP **09** (2005) 051 [hep-th/0507189];
S. Schafer-Nameki and M. Zamaklar, *Stringy sums and corrections to the quantum string Bethe ansatz*, JHEP **10** (2005) 044 [hep-th/0509096];
G. Arutyunov, S. Frolov and M. Zamaklar, *Finite-size effects from giant magnons*, [hep-th/0606126].

– 33 –

[19] G. Feverati, D. Fioravanti, P. Grinza and M. Rossi, *On the finite size corrections of anti-ferromagnetic anomalous dimensions in $N=4$ sym*, JHEP **05** (2006) 068
[hep-th/0602189].

[20] N. Beisert, J.A. Minahan, M. Staudacher and K. Zarembo, *Stringing spins and spinning strings*, JHEP **09** (2003) 010 [hep-th/0306139].

[21] N. Beisert, S. Frolov, M. Staudacher and A.A. Tseytlin, *Precision spectroscopy of AdS/CFT*,
JHEP **10** (2003) 037 [hep-th/0308117].

[22] N. Beisert, V.A. Kazakov, K. Sakai and K. Zarembo, *Complete spectrum of long operators in $N=4$ sym at one loop*, JHEP **07** (2005) 030 [hep-th/0503200].

[23] S. Frolov and A.A. Tseytlin, *Multi-spin string solutions in $AdS_5\times S^5$*, Nucl. Phys. B **668** (2003) 77 [hep-th/0304255].

[24] I.Y. Park, A. Tirziu and A.A. Tseytlin, *Semiclassical circular strings in $AdS_5$ and 'long' gauge field strength operators*, Phys. Rev. D **71** (2005) 126008 [hep-th/0505130].

[25] J.A. Minahan, *Strong coupling from the Hubbard model*, hep-th/0603175.

[26] J.A. Minahan, *The SU(2) sector in AdS/CFT*, Fortschr. Phys. **53** (2005) 828
[hep-th/0503143].

[27] E.N. Economou and P.N. Poulopoulos, *Ground-state energy of the half-filled one-dimensional Hubbard model*, Phys. Rev. B **20** (1979) 4756;
W. Metzner and D. Vollhardt, *Ground-state energy of the d=1,2,3 dimensional Hubbard model in the weak-coupling limit*, Phys. Rev. B **39** (1989) 4462.

[28] B. Sutherland, *Low-lying eigenstates of the one-dimensional Heisenberg ferromagnet for any magnetization and momentum*, Phys. Rev. Lett. **74** (1995) 816;
A. Dhar and B. Shastry, *Bloch walls and macroscopic string states in Bethe's solution of the Heisenberg ferromagnetic linear chain*, Phys. Rev. Lett. **85** (2000) 2813.

[29] S. Frolov and A.A. Tseytlin, *Rotating string solutions: adS/CFT duality in non-supersymmetric sectors*, Phys. Lett. B **570** (2003) 96 [hep-th/0306143].

[30] G. Arutyunov, S. Frolov and M. Staudacher, *Bethe ansatz for quantum strings*, JHEP **10** (2004) 016 [hep-th/0406256].

[31] E.A. Yuzbashyan, B.L. Altshuler and B.S. Shastry, *The origin of degeneracies and crossings in the 1d Hubbard model*, J. Phys. A **35** (2002) 7525 [cond-mat/0201551].

[32] T. Deguchi, F.H.L. Essler, F. Göhmann, A. Klümper, V.E. Korepin and K. Kusakabe,
*Thermodynamics and excitations of the one-dimensional Hubbard model*, Phys. Rept. **331** (2000) 197 [cond-mat/9904398].

[33] G. Arutyunov and A.A. Tseytlin, *On highest-energy state in the $su(1-1)$ sector of $N=4$ super Yang-Mills theory*, JHEP **05** (2006) 033 [hep-th/0603113].

[34] D. Mateos, T. Mateos and P.K. Townsend, *Supersymmetry of tensionless rotating strings in $AdS_5\times S^5$ and nearly-BPS operators*, JHEP **12** (2003) 017 [hep-th/0309114].

[35] M. Kruczenski, *Spin chains and string theory*, Phys. Rev. Lett. **93** (2004) 161602
[hep-th/0311203].

[36] R. Roiban, A. Tirziu and A.A. Tseytlin, *Slow-string limit and 'antiferromagnetic' state in AdS/CFT*, Phys. Rev. D **73** (2006) 066003 [hep-th/0601074].

- 34 -

[37] N. Flocke, and J. Karwowski, *Symmetric-group approach to the studies of spin-1/2 lattices*,
Phys. Rev. B **55** (1997) 8287;
Yu Zurong et al., *Applications of permutation group theory to Heisenberg spin-1/2 chain*, J.
Phys. A Math. Gen.**26** (1993) 881.
<br>
<br>
![](./images/812062753370931202_18.jpg)
<br>
![](./images/812062753370931202_19.jpg)