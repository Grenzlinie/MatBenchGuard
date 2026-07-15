# Thermodynamical properties of the spin-one transverse Ising model*

I.P. Fittipaldi
Departamento de Física, Universidade Federal de Pernambuco, 50739 Recife PE, Brazil

E.F. Sarmento
Departamento de Física, Universidade Federal de Alagoas, 57000 Maceió AL, Brazil

T. Kaneyoshi
Department of Physics, Nagoya University, 464-01 Nagoya, Japan

Received 27 November 1991

A new type of effective-field theory that has recently been used with success for many applications concerning the two-state transverse Ising model (spin-$\frac{1}{2}$ TIM), is herein extended to the spin-1 TIM. The method, which can explicitly and systematically include correlation effects, is illustrated by employing its simplest approximation version, in which multispin correlations are neglected. The lines of critical points in the $T-\Omega$ plane as well as the thermal behavior of all relevant statistical-mechanical quantities are analysed for several lattice structures and compared with the standard mean-field predictions. It is shown that the present formalism, in spite of its simplicity, yields results quite superior to those currently obtained within the molecular-field approximation.

## 1. Introduction

The two-state transverse Ising model was originally introduced by De Gennes [1] as a valuable model for hydrogen-bounded ferroelectrics [2] such as the $\text{KH}_2\text{PO}_4$ type. Since then, it has successfully been used to study a number of problems of phase transitions associated to order-disorder phenomena in several other systems, for example cooperative John-Teller systems [3] (like $\text{DyVO}_4$ and $\text{TbVO}_4$) and some real magnetic materials for which the crystal field ground-state is a singlet [4]. The wider applicability of the model has been extensively reviewed in the literature (see for instance, refs. [5,6]). The model

*Work partially supported by CNPq and FINEP (Brazilian agencies).

is described by a two-state Ising Hamiltonian with a term representing a field transverse to the Ising spins, namely

$$
\mathscr{H}=-\frac{1}{2} \sum_{i, j} J_{i j} \sigma_{i}^{z} \sigma_{j}^{z}-\Omega \sum_{i} \sigma_{i}^{x}, \tag{1}
$$

where $\sigma_{i}^{x}$ and $\sigma_{i}^{z}$ are components of a spin-$\frac{1}{2}$ operator at site $i$, $J_{i j}$ is an exchange interaction, $\Omega$ represents a transverse field and the sums extend over all the points of a lattice.

The model Hamiltonian described by eq. (1) represents one of the simplest spin systems in which a phase transition occurs for a finite value of the external field. The system shows a phase transition somewhat different from the usual Ising model case. In two or more dimensions it presents a finite-temperature phase transition which can be depressed to zero temperature by increasing $\Omega$ to a certain critical value. The one-dimensional case at zero temperature is also critical (having divergent correlation length) at a critical value of $\Omega$. The system has therefore been studied much in the past as the simplest interesting example of quantum critical phenomena at zero temperature.

The thermodynamical properties of the model Hamiltonian (1) have been obtained exactly only for the one-dimensional lattice [7-9] and in order to study higher- dimensional lattices some sort of approximation has to be done (see for instance, Stinchcombe [6] and references therein). The problem of finding a solution for higher-dimensional lattices has generated a number of different approximation schemes [10-14]. However, all these approaches consider only the model Hamiltonian described by eq. (1) (namely, the spin-$\frac{1}{2}$ TIM) and most of them have been restricted to the analysis of particular regimes, either at low or at high temperature regions.

On the other hand, besides the great development of the renormalization-group methodology and other accurate theoretical techniques, in the last few years there has been an increasing number of works dealing with much less sophisticated approximation schemes which represent a remarkable improvement of the traditional mean-field approximation. In particular, we refer to an effective-field approach which has successfully been proposed to study the thermodynamical properties of spin-$\frac{1}{2}$ [15] as well as spin-1 [16] Ising models. The theories are based on the use of rigorous Ising correlation identities as a starting point and utilizes a differential operator technique introduced by Honmura and Kaneyoshi [15]. Although it does not introduce mathematical complexities, this approach, which is conceptually as simple as the standard mean-field theory, shares with other methods a great versatility and has already been applied to a large variety of interesting Ising model problems, including bulk and surface properties in pure [17] and disordered [18] systems, as well as extended to treat more generalized spin Hamiltonians [19].

The objective of this work is to present the extension of the named effective-field approach to the spin-1 Ising model in the presence of an applied transverse field; namely, the spin-1 TIM. This is done by using a differential operator (in the spirit of works cited in ref. [15]) in a generalized but approximate Callen-Suzuki relation, previously derived by Sá Barreto, Fit- tipaldi and Zeks [20] for the transverse Ising model described by the Hamilto- nian (1). This relation has been applied to a great number of interesting problems related to the spin-$\frac{1}{2}$ TIM systems [21], and whenever comparison is possible a satisfactory qualitative (and to a certain extent quantitative) agree- ment with results available in the literature is found. Hence, the main purpose of the present paper is, through the use of the generalized Callen-Suzuki relation, to extend the new type of effective-field theory of ref. [20] to study the thermodynamical properties of a spin-1 transverse Ising model on several lattice structures. The method, unlike other effective-field treatments, may explicitly and systematically include correlation effects. Here, the formalism is illustrated by employing its simplest approximation version, in which spin-spin correlations are neglected. It is shown that the present framework (EFT) provides results which represent a remarkable improvement on the usual mean-field theory (MFT) and other methods of similar complexity. In particu- lar, it is shown that our effective-field approximative procedure leads to coordinate-dependent predictions.

The contents of the present paper are as follows. In section 2 the general formalism is described. In section 3 general formulae, applicable to lattices with coordination number $Z$, are obtained within the effective-field approxi- mation and then used to discuss the ferromagnetic-phase stability limit (phase diagrams) for lattices with $Z=3$, 4 and 6. The lines of critical points in the $T-\Omega$ plane and the results for the temperature dependence of the longitudinal and transverse magnetizations and quadrupolar moments are discussed in section 4. Finally, in section 5 we comment on the results.

## 2. Formalism

We consider a model system, which, instead of by eq. (1), is now described by the following Hamiltonian:

$$
\mathscr{H}=-\frac{1}{2} \sum_{i, j} J_{i j} S_{i}^{z} S_{j}^{z}-\Omega \sum_{i} S_{i}^{x}, \tag{2}
$$

where $S_{i}^{x}$ and $S_{i}^{z}$ are components of a spin-1 operator at site $i$, and the other quantities are defined as before. Following the lines of previous works (ref.

[20]), the thermal expectation value of a general function of spin operator components $\hat{O}_{n}$, at the lattice site $n$, for a general spin-$S$, is approximately given by

$$
\left\langle\hat{O}_{n}\right\rangle=\left\langle\frac{\operatorname{tr}_{\{n\}} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}\right\rangle,
\tag{3}
$$

where $\langle\ldots\rangle$ indicates the canonical thermal average, $\operatorname{tr}_{\{n\}}$ means the partial trace with respect to the lattice site $n$. $\mathscr{H}_{n}$ represents all parts of the total Hamiltonian $\mathscr{H}$ associated with the lattice site $n$, and $\beta=(k_{\mathrm{B}} T)^{-1}$. In order to make this article self-contained, the derivation of eq. (3) is presented in the appendix.

Now, by using the system Hamiltonian (2), the expression for $\mathscr{H}_{n}$ in eq. (3) reads

$$
\mathscr{H}_{n}=-E_{n}^{z} S_{n}^{z}-\Omega S_{n}^{x},
\tag{4}
$$

where $E_{n}^{z}=\sum_{j} J_{j n} S_{j}^{z}$ for $j \neq n$. In order to diagonalize the form of eq. (4) we use a rotation transformation as follows:

$$
\begin{aligned}
& S_{n}^{z}=\cos \theta_{n} S_{n}^{z^{\prime}}-\sin \theta_{n} S_{n}^{x^{\prime}}, \\
& S_{n}^{x}=\sin \theta_{n} S_{n}^{z^{\prime}}+\cos \theta_{n} S_{n}^{x^{\prime}},
\end{aligned}
\tag{5}
$$

where $\cos \theta_{n}=E_{n}^{z}/E_{n}$, $\sin \theta_{n}=\Omega/E_{n}$, and $E_{n}=\left[\Omega^{2}+\left(E_{n}^{z}\right)^{2}\right]^{1/2}$. The diagonalization above leads to the following results for the longitudinal and transverse site magnetizations:

$$
\left\langle S_{n}^{z}\right\rangle=\left\langle\frac{E_{n}^{z}}{E_{n}} \frac{2 \sinh \left(\beta E_{n}\right)}{1+2 \cosh \left(\beta E_{n}\right)}\right\rangle,
\tag{6}
$$

$$
\left\langle S_{n}^{x}\right\rangle=\left\langle\frac{\Omega}{E_{n}} \frac{2 \sinh \left(\beta E_{n}\right)}{1+2 \cosh \left(\beta E_{n}\right)}\right\rangle.
\tag{7}
$$

In the limit of $\Omega=0$, the above results reduce to the Callen-Suzuki identity [22] for the spin-1 Ising model. Eqs. (6) and (7) will be the starting point used here to calculate the thermodynamical properties of the model. Introducing a differential operator $\mathrm{D}=\partial/\partial x$, we may rewrite eqs. (6) and (7) as

$$
\left\langle S_{n}^{z}\right\rangle=\left.\left\langle\mathrm{e}^{\mathrm{D} E_{n}^{z}}\right\rangle f(x)\right|_{x=0},
\tag{8}
$$

$$
\left\langle S_{n}^{x}\right\rangle=\left.\left\langle\mathrm{e}^{\mathrm{D} E_{n}^{z}}\right\rangle g(x)\right|_{x=0},
\tag{9}
$$

where the functions $f(x)$ and $g(x)$ are defined by

$$
f(x)=\frac{x}{\left(\Omega^{2}+x^{2}\right)^{1 / 2}} \frac{2 \sinh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]}{\left\{1+2 \cosh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]\right\}}, \tag{10}
$$

$$
g(x)=\frac{\Omega}{\left(\Omega^{2}+x^{2}\right)^{1 / 2}} \frac{2 \sinh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]}{\left\{1+2 \cosh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]\right\}}. \tag{11}
$$

By using the van der Waerden identity for spin-1,

$$
\exp \left(\alpha S_{j}^{z}\right)=1+S_{j}^{z} \sinh (\alpha)+\left(S_{j}^{z}\right)^{2}[\cosh (\alpha)-1], \tag{12}
$$

we obtain the following relations:

$$
\left\langle S_{n}^{z}\right\rangle=\left.\left\langle\prod_{j}\left\{1+S_{j}^{z} \sinh \left(J_{n j} \mathrm{D}\right)+\left(S_{j}^{z}\right)^{2}\left[\cosh \left(J_{n j} \mathrm{D}\right)-1\right]\right\}\right\rangle f(x)\right|_{x=0}, \quad(13)
$$

$$
\left\langle S_{n}^{x}\right\rangle=\left.\left\langle\prod_{j}\left\{1+S_{j}^{z} \sinh \left(J_{n j} \mathrm{D}\right)+\left(S_{j}^{z}\right)^{2}\left[\cosh \left(J_{n j} \mathrm{D}\right)-1\right]\right\}\right\rangle g(x)\right|_{x=0}. \quad(14)
$$

We note that, in order to solve the problem, we do need to evaluate $\left\langle\left(S_{j}^{z}\right)^{2}\right\rangle$. Thus, from eq. (3) we have

$$
\left\langle\left(S_{n}^{z}\right)^{2}\right\rangle=\left\langle\frac{\operatorname{tr}_{\{n\}}\left(S_{n}^{z}\right)^{2} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}\right\rangle, \tag{15}
$$

and by using the same process as the above evaluation for $\left\langle S_{n}^{z}\right\rangle$, we can easily obtain the equation for $\left\langle\left(S_{n}^{z}\right)^{2}\right\rangle$ as well as that for $\left\langle\left(S_{n}^{x}\right)^{2}\right\rangle$,

$$
\left\langle\left(S_{n}^{z}\right)^{2}\right\rangle=\left.\left\langle\mathrm{e}^{\mathrm{D} E_{n}^{z}}\right\rangle h(x)\right|_{x=0}, \tag{16}
$$

$$
\left\langle\left(S_{n}^{x}\right)^{2}\right\rangle=\left.\left\langle\mathrm{e}^{\mathrm{D} E_{n}^{z}}\right\rangle k(x)\right|_{x=0}, \tag{17}
$$

where the functions $h(x)$ and $k(x)$ are defined by

$$
h(x)=\frac{\Omega^{2}+\left(\Omega^{2}+2 x^{2}\right) \cosh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]}{\left(\Omega^{2}+x^{2}\right)\left\{1+2 \cosh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]\right\}}, \tag{18}
$$

$$
k(x)=\frac{x^{2}+\left(2 \Omega^{2}+x^{2}\right) \cosh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]}{\left(\Omega^{2}+x^{2}\right)\left\{1+2 \cosh \left[\beta\left(\Omega^{2}+x^{2}\right)^{1 / 2}\right]\right\}}. \tag{19}
$$

Finally, we can summarize our basic equations as follows:

$$
\left\{\begin{aligned}
m^{z} \\
m^{x} \\
q^{z} \\
q^{x}
\end{aligned}\right\}=\left\langle\prod_{j} \Lambda_{n}\left[S_{j}^{z},\left(S_{j}^{z}\right)^{2} ; \mathrm{D}\right]\right\rangle\left.\left\{\begin{array}{l}
f(x) \\
g(x) \\
h(x) \\
k(x)
\end{array}\right\}\right|_{x=0},
\tag{20}
$$

where $m^{z} \equiv\left\langle S_{n}^{z}\right\rangle, m^{x} \equiv\left\langle S_{n}^{x}\right\rangle, q^{z} \equiv\left\langle\left(S_{n}^{z}\right)^{2}\right\rangle, q^{x} \equiv\left\langle\left(S_{n}^{x}\right)^{2}\right\rangle$, functions $f(x), g(x)$, $h(x)$ and $k(x)$ are defined in eqs. (10), (11), (18) and (19), and

$$
\Lambda_{n}\left[S_{j}^{z},\left(S_{j}^{z}\right)^{2} ; \mathrm{D}\right]=1+S_{j}^{z} \sinh \left(J_{n j} \mathrm{D}\right)+\left(S_{j}^{z}\right)^{2}\left[\cosh \left(J_{n j} \mathrm{D}\right)-1\right].
\tag{21}
$$

At this point, we should emphasize that in the Ising limit (i.e. $\Omega=0$) the above equations reduce to the exact corresponding quantities of ref. [16]. Eqs. (20) yield a set of relations between the quantities $\left\langle S_{n}^{z}\right\rangle,\left\langle S_{n}^{x}\right\rangle,\left\langle\left(S_{n}^{z}\right)^{2}\right\rangle,\left\langle\left(S_{n}^{x}\right)^{2}\right\rangle$ and the associated thermal multiple corelation functions occurring on the right-hand side, and thus, are amenable to systematic approximations in which the effects of correlations can explicitly be included [15]. For instance, from eqs. (20) we obtain for the case of the honeycomb lattice the following results:

$$
\begin{aligned}
\left\langle S_{n}^{z}\right\rangle= & {\left[\sum _ { j = 1 } ^ { 3 } \left(\alpha_{n j}\left\langle S_{j}^{z}\right\rangle+\sum_{k(\neq j)} \alpha_{n j}\left(\beta_{n k}-1\right)\left\langle S_{j}^{z}\left(S_{k}^{z}\right)^{2}\right\rangle\right.\right.} \\
& +\frac{1}{2!} \sum_{k(\neq j)} \sum_{l(\neq j, k)} \alpha_{n j}\left(\beta_{n k}-1\right)\left(\beta_{n l}-1\right)\left\langle S_{j}^{z}\left(S_{k}^{z}\right)^{2}\left(S_{l}^{z}\right)^{2}\right\rangle \\
& \left.\left.+\frac{1}{3!} \sum_{k(\neq j)} \sum_{l(\neq j, k)} \alpha_{n j} \alpha_{n k} \alpha_{n l}\left\langle S_{j}^{z} S_{k}^{z} S_{l}^{z}\right\rangle\right)\right]\left.f(x)\right|_{x=0},
\end{aligned}
\tag{22}
$$

$$
\begin{aligned}
\left\langle\left(S_{n}^{z}\right)^{2}\right\rangle= & {\left[1+\sum _ { j = 1 } ^ { 3 } \left(\left(\beta_{n j}-1\right)\left\langle\left(S_{j}^{z}\right)^{2}\right\rangle+\frac{1}{2!} \sum_{k(\neq j)} \alpha_{n j} \alpha_{n k}\left\langle S_{j}^{z} S_{k}^{z}\right\rangle\right.\right.} \\
& +\frac{1}{2!} \sum_{k(\neq j)}\left(\beta_{n j}-1\right)\left(\beta_{n k}-1\right)\left\langle\left(S_{j}^{z}\right)^{2}\left(S_{k}^{z}\right)^{2}\right\rangle \\
& +\frac{1}{2!} \sum_{k(\neq j)} \sum_{l(\neq j, k)} \alpha_{n j} \alpha_{n k}\left(\beta_{n l}-1\right)\left\langle S_{j}^{z} S_{k}^{z}\left(S_{l}^{z}\right)^{2}\right\rangle \\
& +\frac{1}{3!} \sum_{k(\neq j)} \sum_{l(\neq j, k)}\left(\beta_{n j}-1\right)\left(\beta_{n k}-1\right)\left(\beta_{n l}-1\right) \\
& \left.\left.\times\left\langle\left(S_{j}^{z}\right)^{2}\left(S_{l}^{z}\right)^{2}\left(S_{k}^{z}\right)^{2}\right\rangle\right)\right]\left.h(x)\right|_{x=0},
\end{aligned}
\tag{23}
$$

in which we have introduced the notation

$$
\alpha_{n j}=\sinh \left(\beta J_{n j} \mathrm{D}\right), \quad \beta_{n j}=\cosh \left(\beta J_{n j} \mathrm{D}\right).
\tag{24}
$$

In arriving at this set of equations, we have used properties of the exponen- tial operator, such as $\Phi_{\text{even}}(\text{D}) \left.f(x)\right|_{x=0}=0$ and $\Phi_{\text{odd}}(\text{D}) \left.h(x)\right|_{x=0}=0$, valid for any even and odd functional $\Phi(\text{D})$. Analogous equations for the transverse magnetization $\langle S_{n}^{x}\rangle$, and the transverse quadrupolar moment $\langle(S_{n}^{x})^{2}\rangle$, can be obtained from eqs. (20). In this case instead of odd we have even correlation functions, and the functions $f(x)$ and $h(x)$ are replaced, respectively, by $g(x)$ and $k(x)$. Thus, eqs. (20) provide a set of relations between the relevant statistical-mechanical quantities $m^{z}$, $m^{x}$, $q^{z}$ and $q^{x}$ and associated multispin correlation functions of the various sites. Eqs. (20) will be used here as the basis for the present formalism.

## 3. Effective-field theory

The main purpose of the present work is to obtain from the set of eqs. (20) of this new formalism the phase diagrams and the behavior of the longitudinal and transverse magnetizations as well as the quadrupolar moments, as func- tions of the parameters $T$ and $\Omega$. However, it is clear that if we try to treat exactly all the spin-spin correlations which appear through the expansion of the right-hand sides of eqs. (20) (see for example, eqs. (22) and (23) for the honeycomb lattice), the problem quickly becomes mathematically untractable. Therefore, some approximations are needed. As discussed in the previous works [20], a first obvious attempt is to ignore correlations by introducing the decoupling approximations

$$
\begin{aligned}
\left\langle S_{i}^{z} S_{j}^{z} \cdots S_{k}^{z}\right\rangle & \approx\left\langle S_{i}^{z}\right\rangle\left\langle S_{j}^{z}\right\rangle \cdots\left\langle S_{k}^{z}\right\rangle, \\
\left\langle S_{m}^{z}\left(S_{n}^{z}\right)^{2} \cdots\left(S_{l}^{z}\right)^{2}\right\rangle & \approx\left\langle S_{m}^{z}\right\rangle\left\langle\left(S_{n}^{z}\right)^{2}\right\rangle \cdots\left\langle\left(S_{l}^{z}\right)^{2}\right\rangle,
\end{aligned}\qquad(25)
$$

with $i \neq j \neq \cdots \neq k$ and $m \neq n \neq \cdots \neq l$. It corresponds essentially to the Zernike approximation for $S=\frac{1}{2}$ Ising system [23]. Nevertheless, this approxi- mation procedure (EFT) is quite superior to the standard mean-field approxi- mation, since within the present framework relations like $(S_{i}^{z})^{2}=1,0$ are taken exactly into account through the identity (12) and, as a consequence, it neglects only correlations between different spin variables. On the other hand, the standard mean-field theory (MFT) neglects all correlations.

Using the decoupling approximation (25) the set of equations (20) reduces, for the nearest-neighbor interaction $J_{nj}=J$, to

$$
\left\{\begin{array}{l}
m^{z} \\
m^{x} \\
q^{z} \\
q^{x}
\end{array}\right\}=\left\{1+m^{z} \sinh (J \mathrm{D})+q^{z}[\cosh (J \mathrm{D})-1]\right\}^{z} ×\left.\left\{\begin{array}{l}
f(x) \\
g(x) \\
h(x) \\
k(x)
\end{array}\right\}\right|_{x=0}, \qquad(26)
$$

where $Z$ is the lattice coordination number.

Before discussing our effective-field approach, it may be worth to mention the MFT here. As is easily understood from eqs. (8), (9), (16) and (17), the magnetizations and quadrupolar moments in the MFT are given by

$$
\begin{aligned}
& m^{z}=\left.\mathrm{e}^{\left\langle E_{n}^{z}\right\rangle \mathrm{D}} f(x)\right|_{x=0}, \quad m^{x}=\left.\mathrm{e}^{\left\langle E_{n}^{z}\right\rangle \mathrm{D}} g(x)\right|_{x=0}, \\
& q^{z}=\left.\mathrm{e}^{\left\langle E_{n}^{z}\right\rangle \mathrm{D}} h(x)\right|_{x=0}, \quad q^{x}=\left.\mathrm{e}^{\left\langle E_{n}^{z}\right\rangle \mathrm{D}} k(x)\right|_{x=0},
\end{aligned}
$$

where $\left\langle E_{n}^{z}\right\rangle=\sum_{j} J_{n j}\left\langle S_{j}^{z}\right\rangle \equiv Z J m^{z}$. Therefore, in the MFT, in contradistinction to our EFT, the quantities $m^{z}$ and $q^{z}$ do not appear in a coupled set of equations. The numerical results obtained from eqs. (27) and (28) are discussed in the next section.

Now, let us exemplify the use of our EFT equations (26) by explicitly considering some limiting cases. For the particular case with $\Omega=0$, the functions in eq. (26) become (see eqs. (10), (11), (18) and (19)):

$$
\begin{aligned}
& f(x)=\frac{2 \sinh (\beta x)}{1+2 \cosh (\beta x)}, \quad g(x) \equiv 0, \\
& h(x)=\frac{2 \cosh (\beta x)}{1+2 \cosh (\beta x)}, \quad k(x)=\frac{1+\cosh (\beta x)}{1+2 \cosh (\beta x)}.
\end{aligned}
$$

Thus, using these functions in eq. (26) we recover the same set of effectivefield equations obtained in previous works for the spin-1 isotropic Ising model (see, for instance, ref. [16,19]). Moreover, the asymptotic behavior of the above functions certainly tells us the limit values of the quantities $m^{z}, m^{x}, q^{z}$ and $q^{x}$ as $T \rightarrow 0\left(\beta \rightarrow \infty\right.$ ) or $T \rightarrow \infty$ ( $\beta \rightarrow 0$ ). Hence, from eq. (26) with functions given by eqs. (29) and (30) one derives, as expected by exact calculations, the following results:

$$
\begin{aligned}
& m_{0}^{z}(\Omega=0) \equiv\left\langle S^{z}\right\rangle_{T=0}=1, \quad m_{0}^{x}(\Omega=0) \equiv\left\langle S^{x}\right\rangle_{T=0} 0, \\
& q_{0}^{z}(\Omega=0) \equiv\left\langle\left(S^{z}\right)^{2}\right\rangle_{T=0}=1, \quad q_{0}^{x}(\Omega=0) \equiv\left\langle\left(S^{x}\right)^{2}\right\rangle_{T=0}=\frac{1}{2},
\end{aligned}
$$

and

$$
\begin{aligned}
& m_{\infty}^{z}(\Omega=0) \equiv\left\langle S^{z}\right\rangle_{T \rightarrow \infty}=0, \quad m_{\infty}^{x}(\Omega=0) \equiv\left\langle S^{x}\right\rangle_{T \rightarrow \infty}=0, \\
& q_{\infty}^{z}(\Omega=0) \equiv\left\langle\left(S^{z}\right)^{2}\right\rangle_{T \rightarrow \infty}=\frac{2}{3}, \quad q_{\infty}^{x}(\Omega=0) \equiv\left\langle\left(S^{x}\right)^{2}\right\rangle_{T \rightarrow \infty}=\frac{2}{3}.
\end{aligned}
$$

In essence, accordingly to the present EFT framework, the four statistical-

mechanical quantities pertinent to the spin-1 TIM (i.e., $m^{z}$, $m^{x}$, $q^{z}$ and $q^{x}$) can be evaluated, for any lattice structure characterized by the coordination number $Z$, from the set of mutually coupled equations given in eq. (26). The temperature dependence of these quantities are presented in the figures of the next section for selected values of the transverse field $\Omega$.

Now let us turn our attention to the study of the transition temperature of the system for honeycomb ($Z=3$), square ($Z=4$) and simple cubic ($Z=6$) lattices. In a finite transverse field $\Omega$, the $S^{z}$ component of this system is disordered at high temperatures, but below a transition temperature $T_{\mathrm{c}}$ it becomes ordered so that $m^{z} \neq 0$ and the directions of the moments change continuously, although there is an order with $m^{x} \neq 0$ at all temperatures. Thus, by expanding the right-hand side of eq. (26) in an interactive procedure for $m^{z}$ and $q^{z}$ with respect to $m^{z}$, and retaining only terms linear in $m^{z}$, we find

$$
m^{z}=Z K m^{z}+\mathcal{O}\left(\left(m^{z}\right)^{3}\right), \tag{35}
$$

$$
q^{z}=q_{\mathrm{c}}^{z}+\mathcal{O}\left(\left(m^{z}\right)^{2}\right), \tag{36}
$$

where

$$
K=\sinh (J \mathrm{D})\left[q_{\mathrm{c}}^{z} \cosh (J \mathrm{D})+1-q_{\mathrm{c}}^{z}\right]^{Z-1} f(x)\big|_{x=0} \tag{37}
$$

and

$$
q_{\mathrm{c}}^{z}=\left.\left[q_{\mathrm{c}}^{z} \cosh (J \mathrm{D})+1-q_{\mathrm{c}}^{z}\right]^{Z} h(x)\right|_{x=0}. \tag{38}
$$

The second-order phase transition line is then determined by $Z K=1$. Here we summarize the results for $Z=3$, 4 and 6.

$Z=3$:
$$
3\left(1-q_{\mathrm{c}}^{z}\right)^{2} A_{1}+6 q_{\mathrm{c}}^{z}\left(1-q_{\mathrm{c}}^{z}\right) A_{2}+3\left(q_{\mathrm{c}}^{z}\right)^{2} A_{3}=1, \tag{39}
$$

$$
q_{\mathrm{c}}^{z}=\left(1-q_{\mathrm{c}}^{z}\right)^{3} h(0)+3 q_{\mathrm{c}}^{z}\left(1-q_{\mathrm{c}}^{z}\right)^{2} B_{1}+3\left(q_{\mathrm{c}}^{z}\right)^{2}\left(1-q_{\mathrm{c}}^{z}\right) B_{2}+\left(q_{\mathrm{c}}^{z}\right)^{3} B_{3} ; \tag{40}
$$

$Z=4$:
$$
4\left(1-q_{\mathrm{c}}^{z}\right) A_{1}+12 q_{\mathrm{c}}^{z}\left(1-q_{\mathrm{c}}^{z}\right)^{2} A_{2}+12\left(q_{\mathrm{c}}^{z}\right)^{2}\left(1-q_{\mathrm{c}}^{z}\right) A_{3}+4\left(q_{\mathrm{c}}^{z}\right)^{3} A_{4}=1, \tag{41}
$$

$$
\begin{aligned}
q_{\mathrm{c}}^{z}= & \left(1-q_{\mathrm{c}}^{z}\right)^{4} h(0)+4 q_{\mathrm{c}}^{z}\left(1-q_{\mathrm{c}}^{z}\right)^{3} B_{1}+6\left(q_{\mathrm{c}}^{z}\right)^{2}\left(1-q_{\mathrm{c}}^{z}\right)^{2} B_{2} \\
& +4\left(q_{\mathrm{c}}^{z}\right)^{3}\left(1-q_{\mathrm{c}}^{z}\right) B_{3}+\left(q_{\mathrm{c}}^{z}\right)^{4} B_{4} ; \tag{42}
\end{aligned}
$$

$Z=6$:
$$
\begin{aligned}
& 6\left(1-q_{\mathrm{c}}^{z}\right)^{5} A_{1}+30 q_{\mathrm{c}}^{z}\left(1-q_{\mathrm{c}}^{z}\right)^{4} A_{2}+60\left(q_{\mathrm{c}}^{z}\right)^{2}\left(1-q_{\mathrm{c}}^{z}\right)^{3} A_{3}+60\left(q_{\mathrm{c}}^{z}\right)^{3}\left(1-q_{\mathrm{c}}^{z}\right)^{2} A_{4} \\
& \quad+30\left(q_{\mathrm{c}}^{z}\right)^{4}\left(1-q_{\mathrm{c}}^{z}\right) A_{5}+6\left(q_{\mathrm{c}}^{z}\right)^{5} A_{6},
\end{aligned}
\tag{43}
$$

$$
\begin{aligned}
q_{\mathrm{c}}^{z}= & \left(1-q_{\mathrm{c}}^{z}\right)^{6} h(0)+6 q_{\mathrm{c}}^{z}\left(1-q_{\mathrm{c}}^{z}\right)^{5} B_{1}+15\left(q_{\mathrm{c}}^{z}\right)^{2}\left(1-q_{\mathrm{c}}^{z}\right)^{4} B_{2} \\
& +20\left(q_{\mathrm{c}}^{z}\right)^{3}\left(1-q_{\mathrm{c}}^{z}\right)^{3} B_{3}+15\left(q_{\mathrm{c}}^{z}\right)^{4}\left(1-q_{\mathrm{c}}^{z}\right)^{2} B_{4}+6\left(q_{\mathrm{c}}^{z}\right)^{5}\left(1-q_{\mathrm{c}}^{z}\right) B_{5},
\end{aligned}
\tag{44}
$$

where the coefficients $A_{n}$ ($n=1,2,\dots,6$) and $B_{n}$ ($n=1,2,\dots,5$) are temperature dependent only and are given as follows:

$$
A_{n}=\left.\sinh (J \mathrm{D}) \cosh ^{n-1}(J \mathrm{D}) f(x)\right|_{x=0} \quad B_{n}=\left.\cosh ^{n}(J \mathrm{D}) h(x)\right|_{x=0}.
\tag{45}
$$

We have solved the above set of coupled equations numerically, which yield the critical frontiers in the $T-\Omega$ plane. The main results are discussed in the next section.

## 4. Results

Fig. 1 shows the phase diagram in the $T-\Omega$ space for the honeycomb ($Z=3$), the square ($Z=4$) and the cubic ($Z=6$) lattices. In the figure, solid and dashed lines denote our EFT and MFT results, respectively. As is seen from fig. 1, on the other hand, when $\Omega$ increases from zero, $T_{\mathrm{c}}$ falls from its value in the Ising system and reaches zero at a critical value $\Omega_{\mathrm{c}}$. For comparison the values of $k_{\mathrm{B}} T_{\mathrm{c}} / Z J$ at $\Omega=0$ and $\Omega_{\mathrm{c}} / Z J$ are collected in table I. Note that the MFT predictions in these units do not distinguish the coordination number $Z$ of the lattice. Thus, our effective-field theory substantially improves the MFT results, as shown in table I and fig. 1.

In fig. 2 the spin-1 (solid curve) phase boundary line in the $T-\Omega$ plane is compared with that of spin-$\frac{1}{2}$ (dashed-dotted curve) for a honeycomb lattice within the present effective-field theory [20]. As one can see from this figure, a more pronounced rate of decrease of $T_{\mathrm{c}}$ with $\Omega$ is found for $S=1$ than for $S=\frac{1}{2}$. This fact indicates that, as expected, the spin-1 TIM favor the order in a more pronounced way than the spin-$\frac{1}{2}$ case. For comparison, the values of $\Omega_{\mathrm{c}}$ for both cases are collected in table II.

In fig. 3 we show the temperature dependence of magnetizations $m^{z}$ and $m^{x}$ (full lines) and the quadrupolar moments $q^{z}$ and $q^{x}$ (dashed-dotted line) for a

![](./images/812446220952797185_1.jpg)

Fig. 1. The critical ferromagnetic frontiers in the $T-\Omega$ plane for $Z=3$, 4 and 6 (numbers associated with each curve) for the spin-1 TIM. The full and broken curves correspond to EFT (present framework) and MFT results, respectively.

honeycomb lattice within the present EFT framework, when the values of $\Omega$ are taken as $\Omega=0$ and $\Omega=1.5 J$. For $\Omega=0$, the transverse magnetization $m^{x}$ is always null (i.e. $m^{x} \equiv 0$ ) and the limit values of $m^{z}, q^{z}$ and $q^{x}$ at $T=0 \mathrm{~K}$ are those given in eqs. (31) and (32). At $T=T_{\mathrm{c}}, m^{z}$ reduces to zero and both $q^{x}$ and $q^{z}$ express the discontinuity for their derivatives which is similar to that known for the spin-1 isotropic Ising model studied in ref. [16]. One the other hand, for $\Omega=1.5 J, m^{z}$ falls below its corresponding curve for $\Omega=0$, and $m^{x}$ has finite values in the whole temperature range; the role of the transverse field $\Omega$ is essentially to inhibit the ordering of $m^{z}$ components. In the ordered phase $m^{x}$ weakly depends on temperature and at $T=T_{\mathrm{c}}$ its derivative shows discon- tinuities. The results are very similar to those found for the spin- $\frac{1}{2}$ TIM [20].

<table>
<caption>Table I<br>Results for the reduced transition temperature $\tau_{\mathrm{c}} \equiv k_{\mathrm{B}} T_{\mathrm{c}} / Z J$ at $\Omega=0$ and reduced transverse critical field $\omega_{\mathrm{c}} \equiv \Omega_{\mathrm{c}} / Z J$ for the $S=1$ TIM for honeycomb $(Z=3)$, square $(Z=4)$ and simple cubic $(Z=6)$ lattice. Standard MFT gives the values $\tau_{\mathrm{c}}(\mathrm{MFT})=0.667$ and $\omega_{\mathrm{c}}(\mathrm{MFT})=1.0$ irrespective of the coordination number $Z$.</caption>
<thead>
<tr>
<th></th>
<th>$Z$</th>
<th></th>
<th></th>
</tr>
<tr>
<th></th>
<th>3</th>
<th>4</th>
<th>6</th>
</tr>
</thead>
<tbody>
<tr>
<th>$\tau_{\mathrm{c}}$</th>
<td>0.506</td>
<td>0.546</td>
<td>0.586</td>
</tr>
<tr>
<th>$\omega_{\mathrm{c}}$</th>
<td>0.747</td>
<td>0.814</td>
<td>0.876</td>
</tr>
</tbody>
</table>

![](./images/812446220952797185_2.jpg)

Fig. 2. Phase boundary line of $S=1$ TIM in comparison with that of $S=\frac{1}{2}$ TIM for a honeycomb lattice $(Z=3)$.

The temperature dependence of $m^{z}$ and $m^{x}$ in the presence of a transverse field $\Omega$ is shown in fig. $4 a$ for a honeycomb lattice. The results are obtained under $\Omega=1.5 J$. Solid and dashed lines denote our EFT and MFT results, respectively. It can be seen from the figure that the longitudinal magnetization ordering is, as predicted by both EFT and MFT procedures, inhibited by the transverse field $\Omega$ and at $T=T_{\mathrm{c}}, m^{z}=0$. However, for the transverse magnetization $m^{x}$, the present results are qualitatively different from MFT behavior. For instance, as we can see in the figure, in the ordered phase $m^{x}$ is very sensitive with temperature in contrast with the constant behavior predicted by MFT. For $T>T_{\mathrm{c}}$ both results are equivalent. The corresponding reduced plots for both quadrupolar moments $q^{z}$ and $q^{x}$ are depicted in fig. $4 \mathrm{~b}$.

Finally, in fig. 5, the transverse field dependencies of the longitudinal $(m^{z})$ and transverse $(m^{x})$ magnetizations at a fixed temperature $(T=0.05 J)$ are

Table II
Comparison of the reduced transverse critical field $\omega_{\mathrm{c}} \equiv \Omega_{\mathrm{c}} / Z J$ for the $S=1$ and $S=\frac{1}{2}$ TIM systems, obtained within the present EFT for the square $(Z=4)$ and simple cubic $(Z=6)$ lattices. Standard MFT gives the value $\omega_{\mathrm{c}}(\mathrm{MFT})=1.0$ irrespective of the spin magnitude. The $\omega_{\mathrm{c}}\left(S=\frac{1}{2}\right)$ results are taken from ref. [20].

<table>
<thead>
<tr>
<th>$Z$</th>
<th>$\omega_{\mathrm{c}}\left(S=\frac{1}{2}\right)$</th>
<th>$\omega_{\mathrm{c}}(S=1)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>4</td>
<td>0.688</td>
<td>0.814</td>
</tr>
<tr>
<td>6</td>
<td>0.784</td>
<td>0.876</td>
</tr>
</tbody>
</table>

![](./images/812446220952797185_3.jpg)

Fig. 3. The temperature dependence of the longitudinal $(m^{z})$ and transverse $(m^{x})$ magnetizations (solid curves) and corresponding longitudinal $(q^{z})$ and transverse $(q^{x})$ quadrupolar moments (dashed-dotted curves) for $Z=3$, when $\Omega$ is taken as $\Omega=0$ and $\Omega=1.5J$.

![](./images/812446220952797185_4.jpg)

Fig. 4. (a) Variation of the longitudinal $(m^{z})$ and transverse $(m^{x})$ magnetizations with the reduced temperature $T/T_{c}$ for a honeycomb lattice $(Z=3)$, when $\Omega$ is fixed as $\Omega=1.5J$; (b) Variation of the longitudinal $(q^{z})$ and transverse $(q^{x})$ quadrupolar moments with the reduced temperature $T/T_{c}$. Full curves present work and dashed curves MFT results.

![](./images/812446220952797185_5.jpg)

Fig. 5. Transverse field dependencies of both $m^{z}$ and $m^{x}$ at a fixed temperature ($T=0.05J$) for the system with $Z=3$. Solid lines EFT and dashed lines MFT results.

presented for a honeycomb lattice. Solid and dashed lines are the EFT and MFT results, respectively. The $m^{z}$ curve decreases monotonically and disappears at the values $\Omega_{\mathrm{c}}$ ($\Omega_{\mathrm{c}}(\mathrm{EFT})=2.24J$; $\Omega_{\mathrm{c}}(\mathrm{MFT})=3.0J$). On the other hand, the $m^{x}$ curve increases with $\Omega$ and changes its inclination at the values $\Omega_{\mathrm{c}}$ at which $m^{z}$ reduces to zero. Again, the present EFT results for the transverse magnetization $m^{x}$ are qualitatively different from the behavior predicted by MFT, as can be seen by comparing the broken (MFT) and full (EFT) curves for $m^{x}$ in fig. 5.

## 5. Concluding remarks

In this work we have extended to the spin-1 Ising model in a transverse field, the new type of effective-field theory previously developed for the usual spin-$\frac{1}{2}$TIM [20]. We have generated a set of formal relations which are suitable to explicity incorporate correlations through some sort of successive approximation scheme. The method is here illustrated in its simplest approximation version, in which correlations are neglected. Within this framework we discuss the temperature dependence of the longitudinal and transverse magnetizations and quadrupolar moments for some selected value of the transverse field $\Omega$ as well as the ferromagnetic-phase stability limit (phase diagrams) for several lattice structures. It is shown that this procedure, without introducing mathe-

matical complexities, provides results which are quite superior to those obtained within the scope of the traditional mean-field theory. In particular, the present method leads to coordinate-dependent predictions (in spite of the fact that it still is an effective-field theory, which does not distinguish the lattice dimensionality), making an important improvement of the ordinary MFT results. Thus, owing to their simplicity, the method developed here can be used to study more complex problems associated with the spin-one TIM Hamilto- nian [24], opening within this context some new possibilities of interesting applications.

## Appendix

We assume that the total Hamiltonian $\mathscr{H}$ of the system can be separated in two parts,

$$
\mathscr{H}=\mathscr{H}_{n}+\mathscr{H}^{\prime}. \tag{A.1}
$$

Here $\mathscr{H}_{n}$ includes all the parts of $\mathscr{H}$ associated with the lattice site $n$, namely $\mathscr{H}_{n}=-E_{n} S_{n}^{z}-\Omega S_{n}^{x}$ with $E_{n}=\sum_{j \neq n} J_{j n} S_{j}^{z}$, and $\mathscr{H}^{\prime}$ represents the rest of the Hamiltonian and does not depend on spin operators on site $n$. Furthermore we assume that $[\mathscr{H}_{n}, \mathscr{H}^{\prime}]=[\mathscr{H}_{n}, \mathscr{H}] \neq 0$.

The average value of a spin operator function $\hat{O}_{n}$ of the lattice site $n$ is given by

$$
\left\langle\hat{O}_{n}\right\rangle=\frac{1}{\mathscr{Z}} \operatorname{tr} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}} \quad\left(\mathscr{Z}=\operatorname{Tr} \mathrm{e}^{-\beta \mathscr{H}}\right). \tag{A.2}
$$

We can rewrite eq. (A.2) as follows:

$$
\left\langle\hat{O}_{n}\right\rangle=\frac{1}{\mathscr{Z}} \operatorname{Tr}^{\prime} \operatorname{tr}_{\{n\}} \hat{O}_{n}\left(\mathrm{e}^{-\beta \mathscr{H}_{n}} \mathrm{e}^{-\beta H^{\prime}}+\Delta\right). \tag{A.3}
$$

Here $\operatorname{Tr}^{\prime}=\prod_{i \neq n} \operatorname{tr}_{\{i\}}$, $\operatorname{tr}_{\{n\}}$ means the partial trace with respect to the lattice site $n$, and $\Delta=\exp[-\beta(\mathscr{H}_{n}+\mathscr{H}^{\prime})]-\exp(-\beta \mathscr{H}_{n}) \exp(-\beta \mathscr{H}^{\prime})$. After a straightforward calculation we obtain

$$
\left\langle\hat{O}_{n}\right\rangle=\left\langle\frac{\operatorname{tr}_{\{n\}} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}\right\rangle-\left\langle\left(\frac{\operatorname{tr}_{\{n\}} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}-\hat{O}_{n}\right) \tilde{\Delta}\right\rangle, \tag{A.4}
$$

with

$$
\tilde{\Delta}=\Delta \exp[\beta \mathscr{H}]=1-\exp(-\beta \mathscr{H}_{n}) \exp(-\beta \mathscr{H}^{\prime}) \exp[\beta(\mathscr{H}_{n}+\mathscr{H}^{\prime})]. \tag{A.5}
$$

A first obvious attempt to deal with the second term of eq. (A.4) is to assume the following decoupling:

$$
\left\langle\left[\frac{\operatorname{tr}_{\{n\}} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}-\hat{O}_{n}\right] \hat{\Delta}\right\rangle \simeq\left\langle\left[\frac{\operatorname{tr}_{\{n\}} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}-\hat{O}_{n}\right]\right\rangle\langle\tilde{\Delta}\rangle. \tag{A.6}
$$

Thus, using (A.6), eq. (A.4) becomes

$$
\left(\left\langle\hat{O}_{n}\right\rangle-\left\langle\frac{\operatorname{tr}_{\{n\}} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}\right\rangle\right)(1-\langle\tilde{\Delta}\rangle) \simeq 0. \tag{A.7}
$$

As can be seen from eq. (A.5), $\langle\tilde{\Delta}\rangle \neq 1$. Therefore we have

$$
\left\langle\hat{O}_{n}\right\rangle \simeq\left\langle\frac{\operatorname{tr}_{\{n\}} \hat{O}_{n} \mathrm{e}^{-\beta \mathscr{H}_{n}}}{\operatorname{tr}_{\{n\}} \mathrm{e}^{-\beta \mathscr{H}_{n}}}\right\rangle, \tag{A.8}
$$

which can be considered as an approximate generalized Callen-Suzuki identity [22].

### References

[1] P.G. de Gennes, Solid State Commun. 1 (1963) 132.
[2] R. Blinc and B. Zeks in: Soft Modes in Ferroelectric and Antiferroelectrics (North-Holland, Amsterdam, 1974).
R.J. Elliott and A.P. Young, Ferroelectrics 7 (1974) 23.
[3] R.J. Elliott, G.A. Gehring, A.P. Malogemoff, S.R.P. Smith, N.S. Staude and R.N. Tyte, J. Phys. C 4 (1971) L179.
[4] Y.L. Wong and B. Cooper, Phys. Rev. 172 (1968) 539.
[5] R. Blinc and B. Zeks, Adv. Phys. Z 1 (1972) 693.
[6] R.B. Stinchcombe, J. Phys. C 6 (1973) 2459.
[7] S. Katsura, Phys. Rev. 127 (1968) 1508.
[8] P. Pfeuty, Ann. Phys. 57 (1970) 79.
[9] M. Suzuki, Phys. Lett. A 34 (1971) 94.
[10] M.E. Fisher, J. Math. Phys. 4 (1963) 124.
[11] R.J. Elliott and C. Wood, J. Phys. C 4 (1971) 2359.
[12] P. Pfeuty and R.J. Elliott, J. Phys. C 4 (1971) 2370.
[13] J.A. Plascak and S.R. Salinas, Phys. Status Solidi, B 113 (1982) 367.
[14] L.G. Ferreira, S.R. Salinas and H.J. Oliveira, Phys. Status Solidi, B 83 (1977) 229.
[15] R. Honmura and T. Kaneyoshi, J. Phys. C 12 (1979) 3979.
T. Kaneyoshi, I.P. Fittapaldi, R. Honmura and T. Manabe, Phys. Rev. B 24 (1981) 481.
G.B. Taggart and I.P. Fittipaldi, Phys. Rev. B 25 (1982) 7016.
[16] A.F. Siqueira and I.P. Fittipaldi, Physica A 138 (1986) 591.
T. Kaneyoshi, J. Phys. Soc. Jpn. 56 (1987) 933.
[17] I. Tamura, E.F. Sarmento, I.P. Fittipaldi and T. Kaneyoshi, Phys. Status Solidi, B 118 (1983) 409.
R. Honmura, E.F. Sarmento, I.P. Fittipaldi and T. Kaneyoshi, Phys. Status Solidi, 121 (1984) 197.

[18] T. Kaneyoshi, I. Tamura and E.F. Sarmento, Phys. Rev. B 28 (1983) 6491.
I.P. Fittipaldi, C. Tsallis and E.F. Sarmento, Solid State Commun. 44 (1982) 777.
E.F. Sarmento, C. Tsallis and I.P. Fittipaldi, J. Magn. Magn. Mat. 31-34 (1983) 1451.
O.F. de Alcantara and I.P. Fittipaldi, Phys. Lett. A 98 (1983) 199.
E.F. Sarmento and C. Tsallis, Phys. Rev. B 27 (1983) 5784.
T. Kaneyoshi, Phys. Rev. B 33 (1986) 7688.
T. Kaneyoshi and Z.Y. Li, Phys. Rev. B 35 (1987) 1869.

[19] R. Honmura, E.F. Sarmento, C. Tsallis and I.P. Fittipaldi, Phys. Rev. B 29 (1984) 2761.
A.F. Siqueira and I.P. Fittipaldi, Phys. Rev. B 31 (1985) 6092.
I.P. Fittipaldi and T. Kaneyoshi, J. Phys.: Condens. Matter 1 (1989) 6513.

[20] F.C. Sá Barreto, I.P. Fittipaldi and B. Zeks, Ferroelectrics 39 (1981) 1103.
F.C. Sá Barreto and I.P. Fittipaldi, Physica A 129 (1985) 360.

[21] E.F. Sarmento, I. Tamura, L.E.M.C. de Oliveira and T. Kaneyoshi, J. Phys. C 17 (1984) 3195.
I. Tamura, E.F. Sarmento and T. Kaneyoshi, J. Phys. 17 (1984) 3194.
I.P. Fittipaldi, F.C. Sá Barreto and P.R. Silva, Physica A 131 (1985) 599.
T. Kaneyoshi, Phys. Rev. B 33 (1986) 526; 34 (1986) 1738.
E.F. Sarmento, R.B. Muniz and S.B. Cavalcanti, Phys. Rev. B 36 (1987) 529.

[22] H.B. Callen, Phys. Lett. 4 (1963) 161.
M. Suzuki, Phys. Lett. 19 (1965) 267.

[23] F. Zernike, Physica 7 (1940) 565.

[24] T. Kaneyoshi, E.F. Sarmento and I.P. Fittipaldi, Phys. Rev. B 38 (1988) 2649.