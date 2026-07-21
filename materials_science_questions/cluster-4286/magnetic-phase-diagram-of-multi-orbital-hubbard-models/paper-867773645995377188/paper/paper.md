# Symmetries and boundary conditions with a twist

Krissia Zawadzki, $^1$ Irene D'Amico, $^{2,1}$ and Luiz N. Oliveira$^1$

$^1$Departamento de Física e Ciência Interdisciplinar,
Instituto de Física de São Carlos, University of São Paulo,
Caixa Postal 369, 13560-970 São Carlos, SP, Brazil

$^2$Department of Physics, University of York, York, YO10 5DD, United Kingdom

(Dated: July 10, 2017)

## Abstract

Interest in finite-size systems has risen in the last decades, due to the focus on nanotechnological applications and because they are convenient for numerical treatment that can subsequently be extrapolated to infinite lattices. Independently of the envisioned application, special attention must be given to boundary condition, which may or may not preserve the symmetry of the infinite lattice. Here we present a detailed study of the compatibility between boundary conditions and conservation laws. The conflict between open boundary conditions and momentum conservation is well understood, but we examine other symmetries, as well: we discuss gauge invariance, inversion, spin, and particle-hole symmetry and their compatibility with open, periodic, and twisted boundary conditions. In the interest of clarity, we develop the reasoning in the framework of the one-dimensional half-filled Hubbard model, whose Hamiltonian displays a variety of symmetries. Our discussion includes analytical and numerical results. Our analytical survey shows that, as a rule, boundary conditions break one or more symmetries of the infinite-lattice Hamiltonian. The exception is twisted boundary condition with the special torsion $\Theta = \pi L/2$, where $L$ is the lattice size. Our numerical results for the ground-state energy at half-filling and the energy gap for $L = 2$-$7$ show how the breaking of symmetry affects the convergence to the $L \to \infty$ limit. We compare the computed energies and gaps with the exact results for the infinite lattice drawn from the Bethe-Ansatz solution. The deviations are boundary-condition dependent. The special torsion yields more rapid convergence than open or periodic boundary conditions. For sizes as small as $L = 7$, the numerical results for twisted condition are very close to the $L \to \infty$ limit. We also discuss the ground-state electronic density and magnetization at half filling under the three boundary conditions.


## I. INTRODUCTION

Boundary conditions are of crucial importance to solve physical problems, as they affect the symmetries of the system and hence may modify fundamental properties, such as ground state energies and conserved quantities. For small systems the effect of boundary conditions – and of related symmetries – is particularly acute: this is becoming of more and more practical relevance as the size of samples considered in experiments is shrinking to the nanoscale, and even down to just few atoms or spins, spurred by interest in nano and quantum technologies.

In this respect, the importance of the Hubbard model has grown with time. Originally seen as a sketchy depiction of a strongly correlated solid, the model has found recent experimental expression e.g. in Bose-Einstein condensates¹⁻³ or ultracold fermionic atoms.⁴ The (infinite) model exhibits various symmetries. The Hubbard Hamiltonian conserves charge and spin. In one dimension, it remains invariant under left-right inversion and therefore conserves parity. The infinite system is invariant under lattice translations and hence conserves momentum. Finally, if the chemical potential is chosen to make the number of electrons equal to the number of sites, the Hamiltonian remains invariant under particle-hole transformation.

Most of the research on the one-dimensional Hubbard Hamiltonian has been focused on the infinite system. Here, we consider small Hubbard lattices, to compare the effects of different boundary conditions. Small lattices are in fact important for comparisons to experiments with Bose-Einstein condensates, molecules, and other physical systems.⁵⁻¹⁰ More specifically, we compute the ground-state energy, energy gap, and electronic and magnetization densities at half filling for open (OBC), periodic (PBC), and twisted (TBC) boundary conditions for lattices with $L$ ($L=2,3,\dots,7$) sites. We compare the results with those determined by the Bethe-Ansatz solution. Our results show that TBC ensures the fastest convergence to the $L\rightarrow\infty$ limit, giving accurate results in most interaction regimes already for chains of only 5 sites. We expect this finding to have practical value for future numerical treatment of model Hamiltonians. It may also help identifying under which conditions a Bose-Einstein condensate or other nanoscale structure can be used to simulate an infinite Hubbard-model chain.


## OVERVIEW OF TWISTED BOUNDARY CONDITIONS

Twisted boundary conditions are less used and known than open or periodic ones; however, we will demonstrate that they are of particular importance for short Hubbard chains. In this section we summarize their history and usage so far.

In the early 1960's, Kohn found inspiration in the by-then famous paper by Aharonov and Bohm$^{11}$ and added a magnetic flux threading the center of a ring-shaped system to study its transport properties.$^{12}$ From this formulation he derived a criterion allowing detection of metal-insulator transitions, of Mott transitions in particular. He also pointed out that the magnetic flux is equivalent to substituting twisted boundary condition for the periodic condition defining the ring.

Various analytical developments have directly benefited from Kohn's formulation.$^{13-17}$ More recently, however, numerical applications have given especial prominence to twisted boundary condition. A method to compute excitation properties of dilute magnetic alloys was reported three decades ago.$^{18,19}$ A few years later, a procedure applying twisted boundary conditions to the quantum Monte Carlo method$^{20-22}$ and allowing efficient, accurate scaling to the thermodynamical limit of physical properties computed on relatively small lattices opened new avenues exploited by recent applications in Condensed Matter,$^{23,24}$ Nuclear,$^{25}$ and High-Energy Physics.$^{26-33}$

Twisted boundary condition can be regarded as an extension of Born-von-Karmann, or periodic, boundary condition. Under periodic boundary condition, opposite ends of a system are coupled as if they were nearest neighbors inside the system. Under twisted boundary condition, if the coupling between nearest neighbors is $t_0$, the coupling between the ends is $t_0 \exp(i\Theta)$, where the phase $\Theta$, known as the torsion, is a real number.

## ONE-DIMENSIONAL HUBBARD MODEL

The Hubbard model can be defined on a linear chain, with $L$ sites. Each site can accommodate up to two electrons. A penalty $U>0$ is imposed on double occupation, to mimic Coulomb repulsion between electrons of opposite spins, and a coupling $t_0$, a complex number, allows hopping between a site and its nearest neighbors. The coupling between the first site $(\ell=1)$ and the last one $(\ell=L)$ defines the boundary condition.

3

### A. Hamiltonian

The model Hamiltonian reads

$$
\mathbf{H}=-\sum_{\ell=1}^{L-1}\left(t_{0} c_{\ell+1}^{\dagger} c_{\ell}+\text { H. c. }\right)-\left(\tau c_{1}^{\dagger} c_{L}+\text { H. c. }\right)+U \sum_{\ell=1}^{L} \mathbf{n}_{\ell \uparrow} \mathbf{n}_{\ell \downarrow}-\mu \sum_{\ell=1}^{L} \mathbf{n}_{\ell},
\tag{1}
$$

where $\tau$ depends on the boundary condition. The Fermi operator $c_{\ell}^{\dagger}$ creates an electron at site $\ell$. The symbols $\mathbf{n}_{\ell \mu}$ ($\mu=\uparrow, \downarrow$) denote the number $\mathbf{n}_{\ell \mu} \equiv c_{\ell \mu}^{\dagger} c_{\ell \mu}$ of $\mu$-spin electrons at site $\ell$, and $\mathbf{n}_{\ell} \equiv \mathbf{n}_{\ell \uparrow}+\mathbf{n}_{\ell \downarrow}$ denotes the site occupation. Sums over the spin-component index $\sigma=\uparrow, \downarrow$ are implicit in the first, second, and fourth terms on the right-hand side.

The fourth term introduces the chemical potential $\mu$, which controls the number of electrons in the ground state. For fixed number $N$ of electrons, this term is a constant, which merely shifts the ground-state energy and could have been left out. We nonetheless prefer to include it in the definition of the Hamiltonian because attention to the chemical potential will prove instructive (see Section V B, in particular).

As explained, we will discuss open, periodic, and twisted boundary conditions. The coupling $\tau$ between the first and last chain sites specifies these conditions:

$$
\tau=
\begin{cases}
0 & \text { open } \\
t_{0} & \text { periodic }, \\
t_{0} e^{i \Theta} & \text { twisted }
\end{cases}
\tag{2}
$$

where the torsion $\Theta$ is an arbitrary real number. Of course, $\Theta$ is only defined modulo $2 \pi$. For $\Theta=0$, TBC is equivalent to PBC. $\Theta=\pi$ defines antiperiodic boundary condition, of secondary importance in our discussion. Figure 1 schematically depicts the couplings under OBC, PBC, and TBC for $L=10$.

As $L \rightarrow \infty$, the physical properties of the model become independent of boundary condition. For small $L$ on the contrary, the properties are markedly affected by the option on the right-hand side of Eq. (2). Even the symmetry of the Hamiltonian is affected, as detailed in the following section.

### B. Symmetry

In the thermodynamical limit, i. e., for $L \rightarrow \infty$, the Hubbard model possesses a number of symmetries. Of special importance to our discussion are the invarances under gauge

![](./images/867773645995377188_1.jpg)

FIG. 1. Boundary conditions. The three panels display the couplings in a ten-site Hubbard lattice under (a) open, (b) periodic, and (c) twisted boundary conditions.

transformation, rotation, particle-hole inversion, translation, and mirror reflection. For finite $L$, the latter three depend on boundary condition. An itemized discussion of the symmetries seems therefore appropriate.

### 1. Global gauge transformation

Inspection of Eq. (1) shows that the Hamiltonian remains invariant under the global gauge transformation

$$
c_{\ell} \rightarrow e^{i \varphi} c_{\ell}, \tag{3}
$$

where $\varphi$ is a real constant.

Global gauge invariance is equivalent to charge conservation

$$
[\mathbf{H}, \mathbf{q}]=0, \tag{4}
$$

where $\mathbf{q}=\sum_{\ell} \mathbf{n}_{\ell}$.

That Eqs. (3) and (4) must be related follows from simple considerations. For example, let us examine the first term on the right-hand side of Eq. (1) under PBC. The product $c_{1}^{\dagger} c_{L}$ will only remain invariant under Eq. (3) if both operators, $c_{1}^{\dagger}$ and $c_{L}$, undergo the same transformation. If we apply the gauge-transformation (3) to the entire lattice $(\ell=1, \ldots, L)$, the terms proportional to $\tau$ will be invariant. At the same time, charge is conserved, because an electron can only hop from one site to another, both within the lattice.

Let us now split the lattice in two sublattices, one comprising sites $\ell=1,2, \ldots, L-1$ and the other, site $\ell=L$. If we apply the gauge-transformation (3) to the former, but not to the latter, the terms proportional to $\tau$ on the right-hand side of Eq. (1) will acquire phases. The Hamiltonian will hence be modified. At the same time, charge will not be conserved within each sublattice, since electrons can hop from one to the other.

As this simple example indicates, gauge invariance and charge conservation are intimately related. In fact, they are equivalent. The proof considers model Hamiltonians analogous to Eq. (1), comprising terms such as the ones on the right-hand side, of the general form

$$
\hat{h}=\sum_{\substack{m_{1}, \ldots m_{M}, \\ p_{1} \ldots p_{P}=1}}^{L} A_{m_{1} \ldots m_{M}}^{p_{1} \ldots p_{P}} c_{m_{1}}^{\dagger} \ldots c_{m_{M}}^{\dagger} c_{p_{1}} \ldots c_{p_{P}}, \tag{5}
$$

where $M$ and $P$ are integers. For instance, $M=P=2$ in the Coulomb-repulsion term on the right-hand side of Eq. (1), while $M=P=1$ in the other terms.

Under Eq. (3), the Hamiltonian (5) transforms as

$$
\hat{h} \rightarrow e^{i(P-M) \varphi} \sum_{\substack{m_{1}, \ldots m_{M}, \\ p_{1} \ldots p_{P}=1}}^{L} A_{m_{1} \ldots m_{M}}^{p_{1} \ldots p_{P}} c_{m_{1}}^{\dagger} \ldots c_{m_{M}}^{\dagger} c_{p_{1}} \ldots c_{p_{P}}, \tag{6}
$$

and hence remains invariant if and only if $M=P$.

Likewise, charge is conserved if and only if $M=P$. To prove that, it is expedient to evaluate the commutator

$$
[\hat{h}, q]=\sum_{\ell}\left(\left[\hat{h}, c_{\ell}^{\dagger}\right] c_{\ell}+c_{\ell}^{\dagger}\left[\hat{h}, c_{\ell}\right]\right). \tag{7}
$$

6

Computation of each commutator on the right-hand side of Eq. (7) shows that

$$
\left[\hat{h}, c_{\ell}^{\dagger}\right] c_{\ell}=\sum_{\substack{m_{1}, \ldots m_{M}, \\ p_{1}, \ldots p_{P}=1}}^{L}\left[A_{m_{1} \ldots m_{M}}^{p_{1} \ldots p_{P}} c_{m_{1}}^{\dagger} \ldots c_{m_{M}}^{\dagger} c_{p_{1}} \ldots c_{p_{P}}\left(\delta_{\ell, p_{1}}+\ldots+\delta_{\ell, p_{P}}\right)\right],
\tag{8}
$$

and

$$
c_{\ell}^{\dagger}\left[\hat{h}, c_{\ell}\right]=-\sum_{\substack{m_{1}, \ldots m_{M}, \\ p_{1}, \ldots p_{P}=1}}^{L}\left[A_{m_{1} \ldots m_{M}}^{p_{1} \ldots p_{P}} c_{m_{1}}^{\dagger} \ldots c_{m_{M}}^{\dagger} c_{p_{1}} \ldots c_{p_{P}}\left(\delta_{\ell, m_{1}}+\ldots+\delta_{\ell, m_{M}}\right)\right],
\tag{9}
$$

and therefore

$$
[\hat{h}, q]=(P-M) \hat{h},
\tag{10}
$$

which shows that $[\hat{h}, q]=0$ if and only if $P=M$.

Since each term on the right-hand side of Eq. (1) is unaffected by the transformation (3), the Hubbard Hamiltonian is gauge invariant and conserves charge under any of the boundary conditions in Eq. (2) To reach the same conclusion in an alternative way, we only have to compute the commutator on the left-hand side of Eq. (4), which yields zero.

### 2. Local gauge transformation

Unlike the global transformation in Eq. (3), local gauge transformations tend to modify the form of the Hamiltonian (1) Of special interest is the transformation

$$
c_{\ell} \equiv e^{i \ell \alpha} a_{\ell} \quad(\ell=1, \ldots, L),
\tag{11}
$$

where $\alpha$ ($0 \leq \alpha < 2\pi$) is a constant, so that the phase $\ell\alpha$ grows uniformly along the lattice.

Substitution of the right-hand side of Eq. (11) for the $c_{\ell}$ in Eq. (1) yields the expression

$$
\mathbf{H}=-\sum_{\ell=1}^{L-1}\left(t_{0} e^{-i \alpha} a_{\ell+1}^{\dagger} a_{\ell}+\text { H. c. }\right)-\left(\tau e^{i(L-1) \alpha} a_{1}^{\dagger} a_{L}+\text { H. c. }\right)+U \sum_{\ell=1}^{L} \overline{\mathfrak{n}}_{\ell \uparrow} \overline{\mathfrak{n}}_{\ell \downarrow}-\mu \sum_{\ell=1}^{L} \overline{\mathfrak{n}}_{\ell},
\tag{12}
$$

where $\overline{\mathfrak{n}}_{\ell} \equiv a_{\ell}^{\dagger} a_{\ell}$.

If $t_{0}$ is a complex number with phase $\beta$, i. e., if $t_{0}=|t_{0}| e^{i \beta}$, we can choose $\alpha=\beta$ to make real the coefficients $t_{0} e^{-i \alpha}$ and $t_{0}^{*} e^{i \alpha}$ on the right-hand side of Eq. (12). The torsion $\Theta$ is then transformed to

$$
\Theta' = \Theta + L\beta.
\tag{13}
$$


With no loss of generality, therefore, we can take the coefficients $t_0$ on the right-hand side of Eq. (1) to be real and will do so henceforth.

### 3. Rotation in spin space

Clearly, the Hamiltonian (1) remains invariant under the spin-component transformation $c_{\ell\sigma} \to c_{\ell-\sigma}$ ($\sigma=\uparrow,\downarrow$). More generally, it possesses SU(2) symmetry in spin space and hence conserves spin. The boundary term $(\tau c_{1\uparrow}^\dagger c_{L\uparrow} + \tau c_{1\downarrow}^\dagger c_{L\downarrow} + \text{H. c.})$ is likewise symmetric and conserves spin, for OBC, PBC, or TBC.

### 4. Inversion

The last two terms on the right-hand side of Eq. (1) remain invariant under the transformation $\ell \to L+1-\ell$ ($\ell=1,2,\dots,L$), which reverses the ordering of the lattice sites. Whether the first and second terms also remain invariant is less evident. Define, therefore, the Fermi operators

$$
a_{L+1-\ell} \equiv c_\ell \quad (\ell=1,2,\dots,L). \tag{14}
$$

Substitution of the $a_{L+1-\ell}$ for the $c_\ell$ on the right-hand side of Eq. (1) expresses the model Hamiltonian on the basis of the former:

$$
\begin{aligned}
\mathbf{H} = -\sum_{\ell=1}^{L-1} t_0(a_{L-\ell}^\dagger a_{L+1-\ell} + \text{H. c.}) - (\tau a_L^\dagger a_1 + \text{H. c.}) + U\sum_{\ell=1}^L \bar{\mathbf{n}}_{\mathbf{L}+\mathbf{1}-\ell\uparrow} \bar{\mathbf{n}}_{\mathbf{L}+\mathbf{1}-\ell\downarrow} - \mu\sum_{\ell=1}^L \bar{\mathbf{n}}_{\mathbf{L}+\mathbf{1}-\ell}
\tag{15}
\end{aligned}
$$

We then relabel the summation indices on the right-hand side of Eq. (15), letting $\ell \to L-\ell$ in the first sum, and $\ell \to L+1-\ell$ in the third and fourth ones, to show that

$$
\begin{aligned}
\mathbf{H} = -\sum_{\ell=1}^{L-1} t_0(a_\ell^\dagger a_{\ell+1} + a_{\ell+1}^\dagger a_\ell) - (\tau a_L^\dagger a_1 + \tau^* a_1^\dagger a_L) + U\sum_{\ell=1}^L \bar{\mathbf{n}}_{\ell\uparrow} \bar{\mathbf{n}}_{\ell\downarrow} - \mu\sum_{\ell=1}^L \bar{\mathbf{n}}_\ell,
\tag{16}
\end{aligned}
$$

where we have spelled out the second terms within the parentheses on the right-hand side to recall that $t_0$ is real, while $\tau$ may be complex.

The first, third, and fourth terms on the right-hand side of Eq. (16) are equivalent to the corresponding terms on the right-hand side of Eq. (1). The second term, however, is equivalent to the Hermitian conjugate of the second term on the right-hand side of Eq. (1).

8

In other words, inversion maps $\tau$ onto $\tau^*$. As long as $\tau$ is real, i. e., for OBC ($\tau=0$), PBC ($\tau=t_0$) or for anti-periodic boundary condition ($\tau=-t_0$), we can see that $\mathbf{H}$ remains invariant under inversion. Twisted boundary condition breaks inversion symmetry, except for $\Theta=0 \mod \pi$.

### 5. Particle-hole transformation

The standard electron-hole transformation, which exchanges the roles of filled states below the Fermi level and vacant states above the Fermi level, merely shifts the chemical potential of the infinite-lattice Hubbard Hamiltonian, from $\mu$ to $U-\mu.^{34}$ If $\mu=U / 2$, the Hamiltonian remains invariant. Extensions to finite lattices calls for special attention to boundary condition, as shown next.

We start with the equality defining the conventional electron-hole transformation:
$$
a_{\ell} \equiv(-1)^{\ell} c_{\ell}^{\dagger}. \tag{17}
$$

Substitution of Eq. (17) for the Fermi operators on the right-hand side of Eq. (1) shows that
$$
\begin{aligned}
\mathbf{H}=\sum_{\ell=1}^{L-1} t_{0}\left(a_{\ell+1} a_{\ell}^{\dagger}+\text { H. c. }\right)+(-1)^{L}\left(\tau a_{1} a_{L}^{\dagger}+\text { H. c. }\right)+U \sum_{\ell=1}^{L}\left(1-\overline{\mathbf{n}}_{\ell \uparrow}\right)\left(1-\overline{\mathbf{n}}_{\ell \downarrow}\right)-\mu \sum_{\ell=1}^{L}\left(2-\overline{\mathbf{n}}_{\ell}\right),
\end{aligned}
\tag{18}
$$
where $\overline{\mathbf{n}}_{\ell} \equiv a_{\ell}^{\dagger} a_{\ell}$.

We now bring the first two terms on the right-hand side of Eq. (18) to normal order and simplify the last two to obtain the expression
$$
\begin{aligned}
\mathbf{H}= & -\sum_{\ell=1}^{L-1} t_{0}\left(a_{\ell}^{\dagger} a_{\ell+1}+\text { H. c. }\right)-(-1)^{L}\left(\tau^{*} a_{1}^{\dagger} a_{L}+\tau a_{L}^{\dagger} a_{1}\right) \\
& +(U-2 \mu) L+U \sum_{\ell=1}^{L} \overline{\mathbf{n}}_{\ell \uparrow} \overline{\mathbf{n}}_{\ell \downarrow}-(U-\mu) \sum_{\ell=1}^{L} \overline{\mathbf{n}}_{\ell}.
\end{aligned}
\tag{19}
$$

The third term on the right-hand side of (19) is a constant that merely shifts the zero of energy. We leave it aside and compare the other terms with those on the right-hand side of Eq. (1). The first terms on the right-hand sides of the two equalities and the terms proportional to $U$ have the same form. Comparison between the last terms shows that the

particle-hole inversion maps $\mu \to U - \mu$. These conclusions are independent of boundary condition and lattice size. By contrast, the second term on the right-hand side of Eq. (19), which enforces boundary condition, is a function of $L$. Equivalence with the corresponding term on the right-hand side of Eq. (1) is insured if and only if

$$
\tau = \tau^*(-1)^L. \tag{20}
$$

Under OBC, $\tau = \tau^* = 0$, and Eq. (20) is always satisfied. Under PBC, $\tau = \tau^* = t_0$, and it follows that Eq. (20) is only satisfied for even $L$. Finally, under TBC, $\tau = t_0 \exp(i\Theta)$, while $\tau^* = t_0 \exp(-i\Theta)$, and it follows that Eq. (20) is equivalent to the condition

$$
\Theta = \frac{\pi}{2}L \mod \pi. \tag{21}
$$

Given that $\Theta$ is only defined modulo $2\pi$, we can see that Eq. (20) is equivalent to the requirement that $\Theta$ be either $0$ or $\pi$ for even $L$ and $\Theta = \pm\pi/2$ for odd $L$. For the illustrative purposes of our discussion, it is more convenient to consider the sufficient condition

$$
\Theta = \frac{\pi}{2}L, \tag{22}
$$

which can be spelled out as follows:

$$
\Theta =
\begin{cases}
0 & (L = 4\ell) \\
\frac{\pi}{2} & (L = 4\ell + 1) \\
\pi & (L = 4\ell + 2) \\
-\frac{\pi}{2} & (L = 4\ell + 3)
\end{cases}, \tag{23}
$$

where $\ell = 0,1,2\ldots$ With $\Theta = 0$ ($\Theta = \pi$) the model is under periodic (anti-periodic) boundary condition.

As long as Eq. (22) is satisfied, Eq. (19) reads

$$
\mathbf{H} = -\sum_{\ell=1}^{L-1} t_0(a_{\ell+1}^{\dagger}a_{\ell} + \text{H. c.}) - (\tau a_1^{\dagger}a_L + \text{H. c.}) + (U - 2\mu)L + U\sum_{\ell=1}^L \bar{\mathbf{n}}_{\ell\uparrow}\bar{\mathbf{n}}_{\ell\downarrow} - (U - \mu)\sum_{\ell=1}^L \bar{\mathbf{n}}_{\ell}. \tag{24}
$$

With the substitution $\mu \to U-\mu$, Eq. (24) reproduces Eq. (1). For $\mu = U/2$, in particular, the right-hand side remains invariant under particle-hole transformation. Equation (22) therefore insures particle-hole symmetry.

### 6. Translation

The last two terms on the right-hand side of Eq. (1) are invariant under the transformation

$$
\ell \to \ell+1 \quad (\ell=1,2, \ldots, L-1) \tag{25a}
$$

$$
\ell \to 1 \quad (\ell=L). \tag{25b}
$$

The first term on the right-hand of Eq. (1), however, is modified by the same transformation. With $\tau = t_0$ (PBC), the sum of the first and second terms remains invariant. For any $L$, therefore, under PBC, the Hamiltonian is translationally invariant. With $\tau = 0$ (OBC), by contrast, translational symmetry is lost. At first sight, TBC may seem to also break translational invariance, but the following reasoning leads to the opposite conclusion.

Given a torsion $\Theta$, define the local torsion
$$
\theta \equiv \frac{\Theta}{L} \tag{26}
$$
and the Fermi operators
$$
a_{\ell} \equiv c_{\ell} e^{i \ell \theta}, \tag{27}
$$
so that $a_{\ell \sigma}^{\dagger} a_{\ell \sigma}=c_{\ell \sigma}^{\dagger} c_{\ell \sigma} \equiv \mathbf{n}_{\ell \sigma}$.

Equation (1) can then be written in the form

$$
\begin{aligned}
\mathbf{H}=-\sum_{\ell=1}^{L-1}\left(t_{0} e^{i \theta} a_{\ell+1}^{\dagger} a_{\ell}+\text { H. c. }\right)+U \sum_{\ell=1}^{L} \mathbf{n}_{\ell \uparrow} \overline{\mathbf{n}}_{\ell \downarrow}- & \left(t_{0} e^{i L \theta} e^{i(1-L) \theta} a_{1}^{\dagger} a_{L}+\text { H. c. }\right) \\
& -\mu \sum_{\ell=1}^{L} \overline{\mathbf{n}}_{\ell},
\end{aligned} \tag{28}
$$

which simplifies to the expression

$$
\mathbf{H}=-\sum_{\ell=1}^{L}\left(t a_{\ell+1}^{\dagger} a_{\ell}+\text { H. c. }\right)+U \sum_{\ell=1}^{L} \overline{\mathbf{n}}_{\ell \uparrow} \overline{\mathbf{n}}_{\ell \downarrow}-\mu \sum_{\ell=1}^{L} \overline{\mathbf{n}}_{\ell}, \tag{29}
$$

where we have defined the complex coupling $t \equiv t_{0} e^{i \theta}$ and identified $a_{L+1}$ with $a_{1}$.

Equation (29) is equivalent to Eq. (1) with $\tau = t$. Moreover, its right-hand side remains invariant under the lattice translations (25a) and (25b). The one-dimensional Hubbard Hamiltonian under PBC or TBC is therefore covered by Bloch's Theorem. $^{35}$ The discussion in Sec. IV will benefit from the ensuing momentum-conservation law.

Table I summarizes the properties of the model under inversion, translation, and particle- hole transformation.

<table>
  <thead>
    <tr>
      <th>BC</th>
      <th>Transform</th>
      <th>$L$</th>
      <th>Invariant?ᵃ</th>
      <th>$\Theta'$</th>
      <th>$\mu'$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>OBC</th>
      <td>inversion</td>
      <td>any</td>
      <td>yes</td>
      <td>–</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>translation</td>
      <td>any</td>
      <td>no</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <th></th>
      <td>p-h</td>
      <td>any</td>
      <td>yes</td>
      <td>–</td>
      <td>$U - \mu$</td>
    </tr>
    <tr>
      <th>PBC</th>
      <td>inversion</td>
      <td>any</td>
      <td>yes</td>
      <td>$\Theta$</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>translation</td>
      <td>any</td>
      <td>yes</td>
      <td>$\Theta$</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>p-h</td>
      <td>even</td>
      <td>yes</td>
      <td>$0$</td>
      <td>$U - \mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>p-h</td>
      <td>odd</td>
      <td>no</td>
      <td>$\pi$</td>
      <td>$U - \mu$</td>
    </tr>
    <tr>
      <th>TBCᵇ</th>
      <td>inversion</td>
      <td>any</td>
      <td>no</td>
      <td>$-\Theta$</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>translation</td>
      <td>any</td>
      <td>yes</td>
      <td>$\Theta$</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>p-h</td>
      <td>any</td>
      <td>no</td>
      <td>$\pi L - \Theta$</td>
      <td>$U - \mu$</td>
    </tr>
    <tr>
      <th>$\boldsymbol{\Theta = \frac{\pi}{2}L}$</th>
      <td>inversion</td>
      <td>even</td>
      <td>no</td>
      <td>$\Theta \mod 2\pi$</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>inversion</td>
      <td>odd</td>
      <td>no</td>
      <td>$-\Theta$</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>translation</td>
      <td>any</td>
      <td>yes</td>
      <td>$\Theta$</td>
      <td>$\mu$</td>
    </tr>
    <tr>
      <th></th>
      <td>p-h</td>
      <td>any</td>
      <td>yes</td>
      <td>$\Theta$</td>
      <td>$U - \mu$</td>
    </tr>
  </tbody>
</table>

ᵃ At half-filling, i. e., $\mu = U/2$
ᵇ Except $\Theta = (\pi/2)L$

TABLE I. Behavior of the finite-size Hubbard Hamiltonian under left-right inversion, translation, and particle-hole transformation. Open, periodic, or twisted boundary conditions are considered, with even or odd number $L$ of sites. The symbol '–' indicates that the corresponding parameter is undefined. Under particle-hole transformations, the Coulomb chemical potential $\mu$ is mapped onto $U - \mu$, while the ground-state energy is shifted by $\mu' - \mu \equiv U - 2\mu$. For convenience, the last four rows describe the model under twisted boundary condition with the special torsion $\Theta = (\pi/2)L$, which is particle-hole symmetric at half filling for any $L$.

## IV. ANALYTICAL RESULTS

We are interested in the physical properties of the finite-size unidimensional Hubbard model under different boundary conditions. Numerical results for the ground-state energy,
12

electronic density and magnetization, and for the energy gap of the small-$L$ Hamiltonian at half filling will be discussed in Section V. Preparatory to that discussion and to gain preliminary physical insight, we survey analytical expressions covering special limits, leaving more detailed discussion to the appendices. For the uncorrelated model ($U=0$), Appendix A identifies the dispersion relation pertaining to each boundary condition, from which the ground-state energy and gap can be easily obtained, and also discusses the electronic and magnetization densities. For $U>0$, Appendix B recapitulates results extracted from the Bethe-Ansatz diagonalization of the model Hamiltonian, which become simple only in the $U \to \infty$ limit.

### A. $U=0$
With $U=0$ the Hamiltonian (1) becomes quadratic. We can easily diagonalize it, under PBC, TBC, or OBC. Since Bloch's Theorem covers only the former two boundary conditions, however, Appendix A follows distinct procedures and obtains distinct results, depending on whether one is dealing with closed (PBC or TBC) or OBC. The results are summarized in Table II. In the infinite model, the per-particle ground-state energy is

$$
E_{\Omega}=-\frac{4 t_{0}}{\pi} \approx-1.27 t_{0}. \tag{30}
$$

The same result can be obtained from the $L \to \infty$ limit of each expression for the ground-state energy in the table.

Results for $3 \leq L \leq 30$ are displayed in Fig. 2. The arrow pointing to the right-hand vertical axis shows that, as the lattice size $L$ grows, the three sets of data representing TBC with $\Theta=(\pi / 2) L$ (half-filled circles), PBC (filled triangles), and OBC (open squares) approach $-(4 / \pi) t_{0}$, the per-particle ground-state energy for $L \to \infty$. The convergence is staggered, rather than smooth, and boundary-condition dependent. The open squares representing OBC stagger the least, but converge relatively slowly to the horizontal line marking the infinite-lattice limit. Periodic boundary condition ensures faster convergence, but the filled triangles for $L=4 n+2$ ($n=1,2,3$, and 4) lie below the horizontal line, while the triangles for the other lattice sizes lie above it. Finally, under TBC, the per-particle energies $\mathcal{E}_{\Omega} \equiv E_{\Omega} / N$ decay rapidly to the horizontal line. For $L=4 \ell$ ($\ell=1,2,3,4$, and 5), the half-filled circles coincide with the filled triangles, as one would expect from Table II or

<table>
  <thead>
    <tr>
      <th>Boundary<br>Condition</th>
      <th>$L$</th>
      <th>$-E_\Omega/(2t_0)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Open</td>
      <td>even</td>
      <td>$\dfrac{1}{\sin\left(\dfrac{\pi}{2(L+1)}\right)} - 1$</td>
    </tr>
    <tr>
      <td></td>
      <td>odd</td>
      <td>$\dfrac{1}{\tan\left(\dfrac{\pi}{2(L+1)}\right)} - 1$</td>
    </tr>
    <tr>
      <td>Periodic</td>
      <td>$4n$</td>
      <td>$\dfrac{2}{\tan\left(\dfrac{\pi}{L}\right)}$</td>
    </tr>
    <tr>
      <td></td>
      <td>$4n+2$</td>
      <td>$\dfrac{2}{\sin\left(\dfrac{\pi}{L}\right)}$</td>
    </tr>
    <tr>
      <td></td>
      <td>odd</td>
      <td>$\dfrac{\cos\left(\dfrac{\pi}{2L}\right)}{\tan\left(\dfrac{\pi}{2L}\right)}$</td>
    </tr>
    <tr>
      <td>Twisted</td>
      <td>even</td>
      <td>$\dfrac{2}{\tan\left(\dfrac{\pi}{L}\right)}$</td>
    </tr>
    <tr>
      <td></td>
      <td>odd</td>
      <td>$\dfrac{1}{\tan\left(\dfrac{\pi}{2L}\right)}$</td>
    </tr>
  </tbody>
</table>

TABLE II. Ground-state energies for $U=0$ and $N=L$ under open, periodic, and twisted $[\Theta = (\pi/2)L]$ boundary conditions.

from recalling from Eq. (23) that $\Theta = (\pi/2)L$ is equivalent to $\Theta = 0$ when $L$ is a multiple of four.

The sequence of odd-$L$ half-filled circles show especially rapid convergence. In fact, comparison of the last two rows in Table II shows that the per-particle energies at half-filling for odd lattice size $L$ coincide with the per-particle energies at half-filling for lattice size $2L$. The even $L$ convergence is substantially slower, since, as the figure shows, the deviation from the $L \to \infty$ limit for $L=3,5,7$, and $9$, for instance, are equal to the deviations for $L=6,10,14$, and $18$, respectively. Section V A will discuss this coincidence further.

## B. Density and magnetization density

Other ground-state properties of interest are the electronic density $n_\ell = n_{\ell\uparrow} + n_{\ell\downarrow}$ ($\ell = 1,\dots,L$) and magnetization density $m_\ell = n_{\ell\uparrow} - n_{\ell\downarrow}$, two functions of paramount importance

![](./images/867773645995377188_2.jpg)

FIG. 2. Per-particle ground-state energies for $U=0$ under OBC (open squares), PBC (filled triangles), and TBC with the special torsion $\Theta=(\pi/2)L$ (half-filled circles). To avoid compression of the vertical axis, we have left out the $L=2$ data, for which the per-particle ground-state energy vanishes under TBC. The horizontal, magenta solid line shows the $L\rightarrow\infty$ limit, Eq. (30). For $L=4,8,12,16$, and 20, i. e., for multiples of four, the filled triangles and half-filled circles coincide. Under TBC, the per-site energies for $L=3,5,7$, and 9 are equal to the per-site energies for $L=6,10,14$, and 18, respectively.

in Density Functional Theory.³⁶

As explained by Sec. IV C 1, the electronic density at half-filling is uniformly unitary for all $U$ and $L$. When $L$ is even, the magnetization density vanishes for all $U$. For finite, odd $L$, however, the magnetization density is nonzero and must be computed numerically for $U\neq0$. An exception is the $U\rightarrow\infty$ limit of the $L=3$ model, which yields analytical results.

In the large $U$ limit, the charge degrees of freedom being frozen at $n_\ell=1$ ($\ell=1,2,3$), each site is equivalent to a spin-1/2 variable—a doublet. There are, therefore, $2^3=8$ states, which can be classified by the total spin $S$, because as explained in Sec. III B 3, $S$ is

conserved.

The total spin resulting from the addition of three individual spins can either be $S=3/2$ or $S=1/2$. The quadruplet ($S=3/2$) comprises four of the eight states; the other four must belong to two doublets ($S=1/2$).

Consider the $S_z=1/2$ components of the two $S=1/2$ states. Since they have the same spin, we are free to choose any pair of orthonormal states that are orthogonal to the $S_z=1/2$ component of the triplet. The latter has the expression

$$
\left|S=\frac{3}{2}, S_{z}=\frac{1}{2}\right\rangle=\frac{1}{\sqrt{3}}\left(c_{1 \uparrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \downarrow}^{\dagger}+c_{1 \uparrow}^{\dagger} c_{2 \downarrow}^{\dagger} c_{3 \uparrow}^{\dagger}+c_{1 \downarrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \uparrow}^{\dagger}\right)|\emptyset\rangle . \tag{31}
$$

Two convenient choices for $S_z=S=1/2$ are

$$
\left|\frac{1}{2}, \frac{1}{2}, u\right\rangle=\frac{1}{\sqrt{2}}\left(c_{1 \uparrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \downarrow}^{\dagger}-c_{1 \downarrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \uparrow}^{\dagger}\right)|\emptyset\rangle, \tag{32}
$$

which is odd ($u$) under spatial inversion, and

$$
\left|\frac{1}{2}, \frac{1}{2}, g\right\rangle=\frac{1}{\sqrt{6}}\left(c_{1 \uparrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \downarrow}^{\dagger}-2 c_{1 \uparrow}^{\dagger} c_{2 \downarrow}^{\dagger} c_{3 \uparrow}^{\dagger}+c_{1 \downarrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \uparrow}^{\dagger}\right)|\emptyset\rangle, \tag{33}
$$

which is even ($g$).

Straightforward computation shows the right-hand sides of Eqs. (32) and (33) to be orthogonal to the right-hand side of Eq. (31). In addition, since they have opposite parities, $|1/2,1/2,u\rangle$ and $|1/2,1/2,g\rangle$ are mutually orthogonal.

For infinite $U$, the quadruplet and the two doublets are degenerate, with zero energy. For large, finite $U$, however, the kinetic terms in the model Hamiltonian can contribute energies of the order of $-t_0^2/U$. From Eq. (31) we find that

$$
\mathbf{H}\left|\frac{3}{2}, \frac{1}{2}\right\rangle=0, \tag{34}
$$

which shows that $|\frac{3}{2}, \frac{1}{2}\rangle$ is an eigenstate with zero energy, for all $U$. In fact, given spin-rotation symmetry, it shows that each component of the quadruplet is an eigenstate, with $E=0$. Second-order perturbation theory$^{37}$ on the other hand shows that, for large $U/t_0$, the two doublet components in Eqs. (32) and (33) have negative energies that differ by $\mathcal{O}(t_0^2/U)$, the even combination $|\frac{1}{2}, \frac{1}{2}, g\rangle$ being the ground state.

From Eq. (33), we can now compute the magnetization density for $|1/2,1/2,g\rangle$:

$$
m_{\ell}^{g}=\left\{\begin{array}{cc}
\frac{2}{3} & (\ell=1,3) \\
-\frac{1}{3} & (\ell=2)
\end{array}. \tag{35}\right.
$$


Neither this attractively simple result, nor the simple analysis leading to it can be extended to $N = L > 3$. As the lattice becomes larger, the number of spin states grows exponentially, and so does the dimension of the $Q,S,S_z,\Pi$ (where $\Pi$ denotes parity under lattice inversion) sector containing the ground state. Already for $L = 7$ the matrix resulting from the projection of the Hamiltonian is too big to be analytically diagonalized, and numerical treatment becomes necessary.

### C. $U \to \infty$

The Coulomb repulsion $U$ penalizes double occupation of the $c_\ell$ orbitals. The eigenstates of the $U \neq 0$ model Hamiltonian are no longer mutually independent, and the single-particle description breaks down. As $U \to \infty$, the energetic cost of double occupation becomes prohibitive and, for $N \leq L$, each orbital $c_\ell$ ($\ell = 1,\dots,L$) can hold no more than one electron. In this limit, in analogy with the depictions in Fig. 12, one might hope to recover a simple picture of the ground state comprising $L$ levels labeled by momenta $k$. The lowest $N$ levels would then be singly occupied, and the remaining $L - N$ ones would be empty.

This description is ratified by the Bethe-Ansatz solution, $^{38,39}$ but the computation of the allowed momenta requires special attention. Under OBC Eq. (A19) is still valid. Under PBC or TBC, however, the conditions determining the allowed $k$ depend not only on $L$, but also on the ground-state spin $S$ and its component $S_z$. Given this distinction, Appendix B discusses open and closed (PBC or TBC) boundary conditions under separate headings.

Under OBC, the computation of ground-state energies is relatively simple (see Appendix B1). For closed boundary conditions, however, one must refer to the Bethe-Ansatz solution. The procedure developed by Lieb and $Wu^{38,39}$ yields two sets of exact nonlinear equations —the Lieb-Wu Equations—that determine the ground-state energy. In most cases, these equations yield only to numerical treatment. In the $U \to \infty$ limit, however, the two sets of Lieb-Wu Equations can be uncoupled, one of them being mapped onto a gas of noninteracting particles, as detailed in Appendix B 2 c.

As illustrations, Table III shows the resulting ground-state energies (shifted by $\mu N$) for $N = L - 1$ for $L = 2,\dots,10$. In all rows, the energy is $E_\Omega = -2t_0\sin(k)$, where $k$ is either $\pi/2$ or a multiple of $2\pi/NL$ that is close to $\pi/2$. The ground state is degenerate. In particular, its spin can have multiple values. The ground-state spin is $S = N/2$ if and only

if $L$ is a multiple of four. This result contrasts with Nagaoka's theorem, $^{40-42}$ which states that, for various two- or three-dimensional lattices, the $U \to \infty$ ground state of the Hubbard Hamiltonian acquires the maximal spin $S = N/2$ at $N = L - 1$, where $L$ is the number of lattice sites.

<table>
  <thead>
    <tr>
      <th>$L$</th>
      <th>$N$</th>
      <th>$2S+1$</th>
      <th>$-(E_\Omega+\mu N)/2t_0$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2</td>
      <td>1,3</td>
      <td>$\sin(\frac{\pi}{3})$</td>
    </tr>
    <tr>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>5</td>
      <td>2,4</td>
      <td>$\sin(\frac{8\pi}{15})$</td>
    </tr>
    <tr>
      <td>7</td>
      <td>6</td>
      <td>1,3,5</td>
      <td>$\sin(\frac{11\pi}{21})$</td>
    </tr>
    <tr>
      <td>8</td>
      <td>7</td>
      <td>2,4,8</td>
      <td>1</td>
    </tr>
    <tr>
      <td>9</td>
      <td>8</td>
      <td>1,3,5,7</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>9</td>
      <td>2,4,6,8</td>
      <td>$\sin(\frac{23\pi}{45})$</td>
    </tr>
  </tbody>
</table>

TABLE III. Ground-state energies for $U \to \infty$ Hubbard Hamiltonians with different lengths $L$ and twisted boundary conditions with torsion $\Theta = (\pi/2)L$, for $N = L - 1$. The third column displays the ground-state spin multiplicities $2S + 1$.

### 1. Density and magnetization density

While the density and magnetization for the half-filled Hubbard chain under PBC or TBC, and the density under OBC can be easily understood on the basis of symmetry, the magnetization under OBC requires special discussion.

#### a. Periodic and twisted boundary conditions
Under PBC or TBC, arbitrary lattice translations leave physical properties unchanged. Both $n_\ell$ and $m_\ell$ must therefore be independent of $\ell$, i. e., uniform. At half-filling, with $N = L$, the density must be unitary, $n_\ell = 1$ ($\ell = 1,2,\dots,L$).

The magnetization density depends on the parity of $L$. For even $L$, the $N = L$ electrons can be divided into $N/2$ $\uparrow$-spin and $N/2$ $\downarrow$-spin electrons. The ground state is a singlet and the magnetization vanishes. It follows that $m_\ell = 0$ ($\ell = 1,2,\dots,L$). For odd $L$, the ground

state is a doublet $(S=1/2)$. If $S_z=1/2$, the numbers of $\uparrow$-spin and $\downarrow$-spin electrons must be $N_\uparrow=(L+1)/2$ and $N_\downarrow=(L-1)/2$, respectively, and the resulting magnetization is $M=1$. The magnetization density is therefore $m_\ell=1/L$ ($\ell=1,2,\dots,L$).

b. Open boundary condition Under OBC translation invariance is broken, and one would expect the density and the magnetization density to be position dependent. For $N=L$, particle-hole symmetry nonetheless forces the density to be uniform, as a simple argument shows. Under particle-hole transformation, the density $n_\ell$ at site $\ell$ is transformed to $2-n_\ell$. The $N=L$ Hamiltonian being particle-hole symmetric, we can conclude that $n_\ell=2-n_\ell$, and hence that $n_\ell=1$.

The magnetization density, on the other hand, may or may not be uniform, depending on the parity of $N=L$. For even $L$, the numbers $N_\uparrow$ and $N_\downarrow$ of $\uparrow$- and $\downarrow$-spin electrons in the ground state are equal, $N_\uparrow=N_\downarrow=N/2$. The ground state is a singlet, hence invariant under the transformation $S_z\to-S_z$, which turns the $\sigma$-spin density $n_\sigma$ into $n_{-\sigma}$ ($\sigma=\uparrow,\downarrow$). It follows that $n_\uparrow=n_\downarrow$ and that the magnetization vanishes for $\ell=1,\dots,L$.

For odd $L$, the ground state is a doublet and therefore not invariant under the $S_z\to-S_z$ transformation: its $\uparrow$-spin component of doublet is transformed into the $\downarrow$-spin component. Like the magnetization density under PBC or TBC, the average magnetization in the ground-state is $1/L$. We cannot expect it to be uniform, however, and the following analytical calculation of the magnetization density for the $U=0$ model shows that $m_\ell$ is staggered, a conclusion that will be numerically extended to $U\neq0$ in Sec. V C.

With $U=0$, the model Hamiltonian can be written in the diagonal form (A25). For odd $N=L$, in order of increasing energy $\epsilon_k$, the $\uparrow$-spin component of the ground state comprises $(N-1)/2$ doubly-occupied single-particle levels $d_k$ and one level with $\uparrow$-spin occupation. The doubly occupied levels make no contribution to the magnetization. The magnetization is entirely due to the contribution from the lone $\uparrow$-spin electron, which lies at the Fermi level. Its momentum $k_F$ is the middle element in the sequence on the right-hand side of Eq. (A19), i. e.,

$$
k_F=\frac{\pi}{2}. \tag{36}
$$

The magnetization density $m_\ell$, which is the ground-state expectation value of $c_{\ell\uparrow}^\dagger c_{\ell\uparrow}-c_{\ell\downarrow}^\dagger c_{\ell\downarrow}$, can therefore be calculated from the expression

$$
m_\ell=\langle\emptyset|d_{k_F\uparrow}(c_{\ell\uparrow}^\dagger c_{\ell\uparrow}-c_{\ell\downarrow}^\dagger c_{\ell\downarrow})d_{k_F\uparrow}^\dagger|\emptyset\rangle. \tag{37}
$$

The expectation value of $d_{k_{F} \uparrow} c_{\ell \downarrow}^{\dagger} c_{\ell \downarrow} d_{k_{F} \uparrow}^{\dagger}$ being equal to zero, Eq. (37) reduces to the expression

$$
m_{\ell}=\left\{d_{k_{F} \uparrow}, c_{\ell \uparrow}^{\dagger}\right\}\left\{c_{\ell \uparrow}, d_{k_{F} \uparrow}^{\dagger}\right\},
\tag{38}
$$

which, according to Eq. (A18), is equivalent to the relation

$$
m_{\ell}=\frac{2}{L+1} \sin ^{2}\left(\frac{\pi \ell}{2}\right).
\tag{39}
$$

For $U=0$, the magnetization density is therefore $2 /(L+1)$ at the odd sites and zero at the even ones. As Appendix B 1 shows, Coulomb repulsion enhances the amplitude of this staggering, without affecting its phase.

## V. NUMERICAL RESULTS

This section presents results for the ground-state energies, and energy gaps for the one-dimensional half-filled Hubbard model under OBC, PBC, and TBC (global twist $\Theta=\pi L / 2$) with $L=2-7$, and for the magnetization densities for $L=3$ and 7 . We have fixed the chemical potential at $\mu=-U / 2$, which enforces particle-hole symmetry, and have computed the gap for excitations from the $N=L-1$ to the $N=L$ ground states. In all cases, we compare the energies and gaps with the Lieb-Wu prediction for the infinite system.

To compute energies, gaps, and magnetization, we have projected the model Hamiltonian upon a real-space basis comprising the $4^{L}$ states corresponding to the four possible occupations $(|\emptyset\rangle, c_{j \uparrow}^{\dagger}|\emptyset\rangle, c_{j \downarrow}^{\dagger}|\emptyset\rangle$, and $c_{j \uparrow}^{\dagger} c_{j \downarrow}^{\dagger}|\emptyset\rangle)$ of each site $j$. To take advantage of the conservation laws, we have (i) constructed a basis of states with well defined charge $N$ and $z$-component $S_{z}$ of the spin; (ii) diagonalized the spin operator $S^{2}$ on that basis; and (iii), taken advantage of Bloch's Theorem (inversion symmetry) to obtain new basis states that are eigenstates of $N, S^{2}, S_{z}$, and the momentum (parity) operator $p$ (П), for PBC and TBC (OBC).

Projected on the basis of the eigenstates, the model Hamiltonian reduces to a block-diagonal matrix. Each block corresponds to a sector, labeled by $N, S^{2}, S_{z}$, and $p$ or $\Pi$. Given the degeneracy among states belonging to $2 S+1$-multiplet, only the matrices for $S_{z}=S$ had to be diagonalized. For $L \leq 7$, the computational effort to numerically diagonalize the block matrices is relatively small. Even for $L=9$, the computational cost is moderate: the largest matrix that must be diagonalized has dimension 8820. As shown by the following

figures, however, the results for $L \leq 7$ suffice for our discussion, so fast is the convergence to the $L \to \infty$ limit.

For $L=2$ under TBC since $\tau=-t_{0}$, the kinetic term $-t_{0} c_{1}^{\dagger} c_{2}+$ H. c. cancels out against the twisted term $-\tau(c_{2}^{\dagger} c_{1}+$ H. c.), and the two sites become decoupled. The model Hamiltonian is then trivially diagonalized. Under OBC or PBC, the largest Hamiltonian blocks have dimension 2 and can also be analytically diagonalized. In all other cases, the ground-state energies and gaps were computed from the numerical diagonalization of the matrices into which the conservation laws separated the projected Hamiltonian. The ground-state energy $E_{\Omega}$ is the lowest eigenvalue resulting from all diagonalizations.

To determine the energy gap $E_{g}$, we have computed the difference

$$
E_{g}=E_{\text {min }}^{N-1}-E_{\Omega}, \tag{40}
$$

between the ground-state energy and the minimum energy among the sectors with $N-1$ electrons. An alternative gap can be computed from the difference

$$
\tilde{E}_{g}=E_{\text {min }}^{N+1}-E_{\Omega}, \tag{41}
$$

where $E_{\text {min }}^{N+1}$ is the minimum energy among the sectors with $N+1$ electrons.

At half filling, a particle-hole transformation takes $E_{\text {min }}^{N-1} \rightleftharpoons E_{\text {min }}^{N+1}$ and leaves $E_{\Omega}$ unchanged. It follows from the invariance of the Hamiltonian under the transformation and from Eqs. (40) and (41) that the two gaps are identical.

### A. Ground-state energy
Figure 3 shows the per-site ground-state energies $\mathcal{E}_{\Omega}$ for the $L=2$ model as functions of the Coulomb repulsion $U$. Under TBC, with the special torsion $\Theta=(\pi / 2) L$, the two sites are decoupled from each other. Each site then accommodates one electron, and the ground-state energy vanishes for all $U$. The squares representing OBC and the triangles representing PBC follow the trend set by the blue solid line, which represents the Bethe-Ansatz expression (B30). The squares come substantially closer to the $L \to \infty$ data than the triangles.

The three insets show the $U=0, L \to \infty$ dispersion relations under the three boundary conditions. The bold blue dashes display the allowed levels for $L=2$, and the arrows


![](./images/867773645995377188_3.jpg)

FIG. 3. Per-site ground-state energies for a Hubbard dimer under periodic (triangles), open (open squares), and twisted (half-filled circles) boundary conditions as a function of the Coulomb parameter. The half-filled circles were computed with the special torsion $\Theta = (\pi/2)L = \pi$, so that the kinetic energy on the right-hand side of Eq. (29) vanishes, because the term with $\ell = 1$ in the sum defining the kinetic energy cancels the term with $\ell = 2$. The blue solid line represents $N = L \to \infty$ limit, Eq. (B30).$^{38,39}$ The insets show the $L \to \infty$, $U = 0$ dispersion relation for $U = 0$ under each boundary condition, the allowed levels for $L = 2$ and their occupations for $N = 2$.

indicate their occupation for $N=2$. The ground-state energy is the sum of the single-particle energies for the occupied levels, which coincides with the $U \to 0$ limits of the corresponding curves in the main plot, that is, $\mathcal{E}_{\Omega}=0,-t_{0}$, and $-2 t_{0}$ for TBC, OBC, and PBC, respectively.

Clearly, the dimer is exceptional, especially so under TBC. We therefore turn to larger lattices. Since, as discussed in Section III B, even- and odd-$L$ Hamiltonians behave differently under particle-hole transformations, we will consider $L=3,5$, and 7 first, and then $L=4$, and 6.

Figure 4 shows the per-site energies as functions of $U$ for $L=3,5$ and 7. Particle-hole symmetry being incompatible with PBC for odd $L$, only the results for OBC and TBC $[\Theta=(\pi / 2) L]$ are shown. As can be seen from the sequence of panels, the red half-filled circles representing $\Theta=(\pi / 2) L$ rapidly approach the $L \to \infty$ limit, the disagreement with the blue solid line being substantially smaller than the deviations between the green open squares (OBC) and the blue line.

As suggested by the data in Fig 2, however, the convergence for even $L$ is significantly slower. Figure 5 depicts the per-particle ground-state energies for $L=4$ (top panel), and $L=6$ (bottom panel) under OBC, and PBC. For $L=4$ the latter condition is equivalent to the special torsion $\Theta=(\pi / 2) L=2 \pi$. For comparison, the top panel also shows results for $\Theta=\pi / 2$, which conflicts with Eq. (21), and $\Theta=\pi$. The red diamonds representing the energies for $\Theta=\pi / 2$ show very good agreement with solid black curve representing the $L \to \infty$ limit, in contrast with the large deviations associated with PBC. Nevertheless, as discussed in Section V B, neither $\Theta=\pi / 2$, nor $\Theta=\pi$ yield the zero-energy single particle level at $k=0$ shown in the inset $(\Theta=2 \pi)$. In the absence of this level the energy gap fails to vanish as $U \to 0$. For this reason, the results for TBC in the bottom panel and elsewhere in this paper are restricted to $\Theta=(\pi / 2) L$, which satisfies Eq. (21) and, for $U=0$, positions the $k=0$ single-particle eigenvalue at $\epsilon_{k}=0$, as the inset of Fig. 5 shows.

Section V A has pointed out that, under torsion $\Theta=(\pi / 2) L$, the $U=0$ per-site ground-state energies for $L=2 n(n=1,3, \ldots)$ converge relatively slowly to the $L \to \infty$ limit because they are equivalent to the $L=n$ per-site energies. That the equivalence is only exact for $U=0$ is shown by Fig. 6, which compares the per-site energies for $L=3$ (halffilled circles) and $L=6$ (filled circles) as functions of $U$. While the two curves are nearly congruent for small $U$, for larger Coulomb repulsion the filled circles approach the $L \to \infty$


![](./images/867773645995377188_4.jpg)

FIG. 4. Per-site ground-state energies for the one-dimensional Hubbard model with $L=3$ (top panel), $L=5$ (central panel), and $L=7$ (bottom panel) under twisted ($\Theta=L\pi/2$) and open boundary conditions as functions of Coulomb repulsion. The symbol convention follows that in Fig. 3. The inset shows the $L\rightarrow\infty$, $U=0$ dispersion relation for twisted boundary condition, the allowed levels for $L$ sites, and their ground-state filling for $N=L$.

![](./images/867773645995377188_5.jpg)

FIG. 5. Per-site ground-state energies for the Hubbard Hamiltonian with $L=4$ (top panel), and $L=6$ (bottom panel) under various conditions, as functions of Coulomb repulsion. The blue solid line depicts the $L\rightarrow\infty$ limit, Eq. (B30). In the top panel, $\Theta=(\pi/2)L$ yields $\Theta=2\pi$, which is equivalent to periodic boundary condition, and results for two other torsions are shown: $\Theta=\pi/2$, and $\pi$. The bottom panel shows the ground-state energy for open, periodic, and twisted $[\Theta=(\pi/2)L]$ boundary conditions. The top and bottom insets show the $U=0$, $L\rightarrow\infty$ dispersion relation for $\Theta=(\pi/2)L$, the allowed levels for $L=4$ and $L=6$, and their ground-state fillings for $N=4$ and $N=6$, respectively.

limit faster than the half-filled circles.

![](./images/867773645995377188_6.jpg)

FIG. 6. Comparison between the per-site ground-state energies for $L=3$ and $L=6$ under twisted boundary condition, with $\Theta=(\pi/2)L$. For small $U$ the red and green curves are virtually coincident, but the $L=6$ data approach the $L\rightarrow\infty$ limit faster as $U$ grows. The inset shows the three $U=0$ single-particle energy levels for $L=3$ (blue) and the three additional levels for $L=6$ (red).

The inset explains the coincidence between the $L=3$ and $L=6$ per-site ground-state energies for $U=0$. The single-particle energies for $L=3$ and for $L=6$ are represented by bold dashes on top of the $\Theta=(\pi/2)L$ dispersion relation. Blue dashes depict the three $L=3$ single-particle levels, which correspond to $k=0,\pm2\pi/3$. For $L=6$, the allowed momenta are $k=0,\pm\pi/3,\pm2\pi/3$, and $\pi$, a sequence that can equally well be written as $k=0,\pm\pi/3,\pi-(\pm\pi/3)$, and $\pi-0$. In other words, to each $k$ in the $L=3$ sequence there correspond two momenta in the $L=6$ sequence, one with momentum $k$, the other

with momentum $\pi - k$. It follows that the ground-state energy for $L=6$ is twice the one for $L=3$, and the per-site energies are identical. The same reasoning identifies the $U=0$ per-site ground-state energies for $L=5,7,9,\dots$ with those for $L=10,14,18,\dots$, respectively.

### 1. Convergence as a function of filling

Figure 7 shows the ground-state energies calculated under twisted boundary condition with the special torsion $\Theta = (\pi/2)L$ for $L=7$ with one (magenta triangles), three (cyan circles), five (orange squares), and seven (blue diamonds) electrons. For comparison, the ground-state energies for the infinite lattice with the same uniform electron densities are shown by the solid lines of the same colors. Given particle-hole symmetry, we need not display results between $n=1$ and $n=2$, since $\mathcal{E}_\Omega(n) = \mathcal{E}_\Omega(2-n)$.

For the intermediate densities $n=3/7$ and $n=5/7$, the numerical results at large $U/t_0$ can be seen to slightly underestimate the infinite-size model, in contrast with the very good agreements for $n=1$ and $n=1/7$. At small $U$ the finite-size energies slightly overestimate those of the infinite system at every density. In all cases, however, the $L=7$ energies represent the infinite limit well, with less than 5% deviations. Although our discussion in other sections is limited to half filling, the conclusions are general.

### B. Energy gap

Figure 8 displays the energy gaps for $L=3,5$ and $7$ as functions of the Coulomb repulsion, for OBC and TBC $[\Theta = (\pi/2)L]$. The gaps are measured from the chemical potential, so that they approach a finite limit, $\mu_-^\infty - U/2 = -2t_0$, as $U,L \to \infty$. For $U \to \infty$ with finite $L$, the horizontal arrows pointing to the right-hand vertical axes indicate the gaps expected from Eqs. (B1) and (B3), under OBC, or from Table III, under TBC.

For small $U$, the open squares, which represent OBC, lie close to the solid line representing the Lieb-Wu result. $^{38,39}$ The deviations between the squares and the continous line grow with $U$ and monotonically approach the $U \to \infty$ limits. The red half-filled circles, which represent TBC, show similar behavior, but two distinctions are noteworthy: (i) only for $L=3$ there is significant vertical separations between the red arrows and the $U,L \to \infty$ limit; and (ii) in

![](./images/867773645995377188_7.jpg)

FIG. 7. (Color online) Ground-state energies as functions of the Coulomb repulstion $U$ for the indicated uniform densities, under twisted boundary condition with torsion $\Theta = (\pi/2)L$. The solid lines are the ground-state energies resulting from the solution of the Lieb-Wu equations for the infinite lattice with $n = 1/7$ (magenta), $3/7$ (cyan), $5/7$ (orange), and 1 (blue). The symbols represent the ground-state energies for lattice-size $L = 7$ with one, three, five, and seven electrons, respectively.

all panels, the half-open circles approach the solid line much faster than the open squares.

The apparent oscillations and plateaus in the red curves reflect the $U$ dependence of the ground-state spin $S$. For $L = 5$, $N = 4$, for instance, the ground-state is a singlet for $U = 0$, but $S$ evolves as $U$ grows and imposes an increasing penalty on double occupation. Let $E_S$ denote the minimum energy in the sector with spin $S$. Relative to $E_1$, the energy $E_0$ grows with $U$ until it exceeds $E_1$, at which point the ground state shifts from the $S = 0$ to the $S = 1$ sector. Table III confirms that, in the $U \to \infty$ limit, the ground state has spin $S = 1$.

More explicit information is provided by Fig. 9, which show the energy gaps as functions of Coulomb repulsion for $L = 4$ and 6. The triangles and diamonds represent the gaps under

![](./images/867773645995377188_8.jpg)

FIG. 8. Energy gaps as functions of Coulomb energy for $L=3,5,7$. The gap is always measured from the chemical potential $\mu=U/2$ so that the plot approaches a finite limit as $U\rightarrow\infty$.

![](./images/867773645995377188_9.jpg)

FIG. 9. Energy gap as a function of Coulomb energy for $L=4$ and 6, top and bottom panels, respectively. The gaps are measured from the chemical potential $\mu=U/2$ to insure convergence to a finite limit as $U\rightarrow\infty$. In both panels, the open squares represent open boundary condition. The triangles and diamonds represent the gaps measured from the lowest energies in the sectors with spin $S=1/2$ and $S=3/2$, respectively under twisted boundary condition with the special torsion $\Theta=(\pi L)/2$. The solid curve represents the gap in the $L\rightarrow\infty$ limit.

TBC, computed as the differences between the lowest energies in the $N = L-1$ sectors with $S=1/2$ and $S=3/2$, respectively, and the ground-state energy for $N = L$. For small $U$, in both panels, the lowest energy in the $S=1/2$ sector is smaller than in the $S=3/2$ sector and hence yields the smaller gap. As $U/t_0$ grows, however, the curve through the diamonds drops faster than the curve through the triangles. In the top panel, the two curves cross around $U = 20t_0$. For $U > 20t_0$, the lower energy lies in the sector with $S=3/2$. The energy gap under TBC therefore follows the triangles from $U=0$ to $U \approx 20t_0$ and the diamonds for $U > 20t_0$. In the bottom panel, the lowest energies in the two sectors become degenerate in the $U \to \infty$ limit, and the energy gap is described by the triangles for any Coulomb repulsion. The $U \to \infty$ limits of both panels agree with the results in Table III, which show that the $N = L-1$ ground state has spin $S=3/2$ for $L=4$ and spins $S=1/2$ or $3/2$ for $L=6$, and yield the gaps indicated by the orange horizontal arrows pointing to the right-hand vertical axes.

Under OBC, for $U=0$, the single-particle spectra contain no zero energy, as a result of which a gap of the order of $1/L$ opens, in disagreement with the zero gap predicted by the Bethe-Ansatz solution. $^{38,39}$ The open squares representing OBC in Fig. 9 show similar discrepancies for all Coulomb repulsions. Compared with the results under TBC, the plots in the two panels show inferior agreement with the $L \to \infty$ limit both for $U \ll t_0$ and $U \gg t_0$. Only for intermediate Coulomb repulsions are the deviations between the gaps under OBC comparable to those computed under TBC.

### C. Magnetization density

As explained in Sec. IV C 1, at half filling the electronic density is uniform, $n_\ell = 1$ ($\ell = 1, \dots, L$), under OBC, PBC, or TBC. The magnetization density vanishes identically under OBC, PBC, or TBC for even $N = L$. For odd $N = L$, it is uniform under PBC and TBC: $m_\ell = 1/L$ ($\ell = 1, \dots, L$). For odd $N = L$ under OBC we have found the $U=0$ magnetization density to be staggered. Here we present numerical results for $U \neq 0$.

Figure 10 plots the magnetization density as a function of site position for the half-filled Hubbard trimer under OBC. With $L=3$, the $U \to \infty$ magnetization density is given by Eq. (35), which is depicted by open circles. The filled triangles, squares, and circles show that the magnetization density at the borders ($\ell = 1, 3$) progressively rises from $m_\ell = 1/2$ to

$m_\ell = 2/3$ as $U/t_0$ grows. At the center $(\ell=2)$ the magnetization density becomes negative and likewise progresses towards the $U \to \infty$ limit $(m_2=-1/3)$.

![](./images/867773645995377188_10.jpg)

FIG. 10. Magnetization density as a function of lattice position for the Hubbard trimer under open boundary condition. The solid black line represents Eq. (39). The filled triangles, filled squares, and filled circles were obtained via numerical diagonalization of the model Hamiltonian, for the indicated Coulomb repulsions $U$. The open circles represent the $U \to \infty$ limits obtained in Sec..

For longer lattices with odd $L$, the evolution of the magnetization density as $U$ grows is similar, as illustrated by Fig. 11. The staggered pattern in Fig. 10 is reproduced. In particular, the amplitude of the oscillations is enhanced as $U$ grows and the magnetization becomes negative at the even-$\ell$ sites. The enhancement is more pronounced in the central region than near the borders. Inspection of our results for different lattice sizes has shown that the amplitude of the oscillation is of $\mathcal{O}(1/L)$. The magnetization density therefore vanishes uniformly as $L \to \infty$.

![](./images/867773645995377188_11.jpg)

FIG. 11. Magnetization density for the seven-site Hubbard model with the indicated Coulomb repulsions. The solid line represents the analytical expression for $U=0$, Eq. (39). All other data were calculated numerically. The open circles were obtained from the ground state of the $U=250t_0$ model and cannot be distinguished, on the scale of the figure from the magnetization densities computed for larger $U/t_0$.

## VI. CONCLUSIONS

In this paper, we have focused on the effect of boundary conditions on small systems, which are of increasing importance with the progressive shrinking and control of nanoscale systems. Our results could be already of relevance for recent experiment on, e. g., Bose- Einstein condensates$^{1-3}$ or ultracold fermionic atoms.$^{4}$ We have examined the finite-size one- dimensional Hubbard model and compared two of its ground-state properties, the ground- state energy and the energy gap, with those of the infinite system. We have concentrated our attention on the energy of the half-filled and nearly half-filled one-dimensional mod- els because the corresponding eigenvalues of the infinite-lattice model have been exactly computed by Lieb and Wu, allowing meaningful comparisons.

The chosen model Hamiltonian is also convenient because it remains invariant under a number of symmetry operations, which have served as beacons in our analysis. Not all

boundary conditions preserve the symmetry of the infinite lattice. Open boundary condition, for instance, is inconsistent with translational invariance, and PBC only preserves particle-hole when the number $L$ of lattice sites is even. The numerical results in Sec. V have shown that the $L$ dependent ground-state energy and gap can display rapid or slow convergence to the infinite limit, depending on whether the symmetries are or not preserved.

Chiefly important, in this context, is torsion. As Sec. III B has shown, TBC preserves translational symmetry. The special torsion $\Theta = (\pi/2)L \mod \pi$ also preserves particle-hole symmetry. Left-right inversion symmetry is only preserved for $\Theta = 0 \mod \pi$, which is inconsistent with the special torsion for odd $L$. Left-right asymmetry has no effect upon the computed properties, however, since inversion amounts to relabeling the momenta, $k \rightarrow -k$. Overall, small $L$ models under TBC with $\Theta = (\pi/2)L \mod \pi$ offer the most faithful representation for the properties of the infinite model. As illustrated by the diamonds in the top panel of Fig. 5, the torsion can be adjusted to yield nearly perfect agreement with the ground-state energy of the infinite model; the adjustment nonetheless breaks particle-hole symmetry and hence yields poor agreement for the energy gap.

The ground-state energy is sensitive to translational invariance, and the energy gap to particle-hole symmetry. Neither is preserved under OBC, which hence yields relatively slow convergence to the infinite-lattice limit. Under PBC, translational symmetry is always preserved, but the odd-$L$ models are particle-hole asymmetric. It results that, for odd $L$, the gap deviations from the $L \rightarrow \infty$ limit under PBC are comparable to those under OBC. Under TBC with $\Theta = (\pi/2)L \mod \pi$, both the ground-state energy and the gap for finite-size models rapidly approach the $L \rightarrow \infty$ limit.

Twisted boundary condition has proved instrumental in numerical analyses of finite-size models targeting the thermodynamical limit. We have shown that the symmetry-preserving torsion $\Theta = (\pi/2)L \mod \pi$ insures rapid convergence and may hence be especially valuable in studies of models that remain invariant under particle-hole transformation.

## ACKNOWLEDGMENTS

KZ and LNO gratefully acknowledge financial support from the FAPESP (Fellowship grant no. 12/02702-0), CNPq (grants no. 312658/2013-3 and 140703/2014-4) and CAPES (Scholarship grant no. 88881.135185/2016-01). ID likewise acknowledges support from the

Royal Society through the Newton Advanced Fellowship scheme (grant no. NA140436). Finally, this work would not have been possible without a PVE grant (no. 401414/2014-0) from the CNPq.

## Appendix A: Analytical results for $U=0$

### 1. Closed boundary conditions

For PBC or TBC, Bloch's Theorem associates each single-particle eigenstate of $\mathbf{H}$ with a unique momentum $k$. Since the number of basis states $a_\ell^\dagger$ is $L$, we will have to define $L$ distinct momenta. For now, however, we let the $k$'s be undetermined parameters.

Since $\mathbf{H}$ remains invariant under lattice translations, the model Hamiltonian commutes with the unit-translation operator $T_1$, defined by the identity

$$
T_1 a_\ell^\dagger|\emptyset\rangle = a_{\ell+1}^\dagger|\emptyset\rangle. \tag{A1}
$$

with the operators $a_\ell$ defined by Eq. (27).

We seek eigenvectors of $T_1$. Promising candidates are defined by the normalized Fermi operator

$$
b_k^\dagger = \frac{1}{\sqrt{L}} \sum_{\ell=1}^L e^{-ik\ell} a_\ell^\dagger. \tag{A2}
$$

To verify that the $b_k^\dagger$ diagonalize $T_1$, we only have to compute $T_1 b_k^\dagger|\emptyset\rangle$. From Eqs. (A1) and (A2) we can see that

$$
T_1 b_k^\dagger|\emptyset\rangle = \frac{1}{\sqrt{L}} \left( \sum_{\ell=1}^{L-1} e^{-ik\ell} a_{\ell+1}^\dagger + e^{-ikL} a_1^\dagger \right) |\emptyset\rangle, \tag{A3}
$$

where we have separated the last term from the sum on the right-hand side to emphasize that, under PBC or TBC, the translation displaces $a_L^\dagger$ to $a_1^\dagger$, as prescribed by Eq. (25b).

We then change the summation index to $\ell' = \ell+1$ in the sum on the right-hand side of Eq. (A3), which shows that

$$
T_1 b_k^\dagger|\emptyset\rangle = \frac{1}{\sqrt{L}} \left( \sum_{\ell'=2}^L e^{-ik(\ell'-1)} a_{\ell'}^\dagger + e^{-ikL} a_1^\dagger \right) |\emptyset\rangle. \tag{A4}
$$


To include the last term within parentheses in the sum on the right-hand side, we now impose the condition

$$
e^{ikL}=1, \tag{A5}
$$

so that Eq. (A4) reduces to the compact expression

$$
T_{1} b_{k}^{\dagger}|\emptyset\rangle=\frac{1}{\sqrt{L}} \sum_{\ell^{\prime}=1}^{L} e^{-i k\left(\ell^{\prime}-1\right)} a_{\ell^{\prime}}^{\dagger}|\emptyset\rangle, \tag{A6}
$$

which shows that

$$
T_{1} b_{k}^{\dagger}|\emptyset\rangle=e^{i k} b_{k}^{\dagger}|\emptyset\rangle. \tag{A7}
$$

From Eq. (A7) we can see that, for momenta satisfying Eq. (A5), the $b_{k}^{\dagger}$ are eigenstates of the translation operator. Equation (A5) is equivalent to the expression

$$
k=\frac{2 n \pi}{L}, \tag{A8}
$$

where $n$ is an integer.

To generate $L$ distinct eigenstates, we could let $n$ run from unity to $L$ on the right-hand side of Eq. (A8). It is nonetheless customary to choose the integers so that the momenta lie in the first Brillouin Zone, i. e., for $-\pi<k \leq \pi$. The following sequences are therefore defined:

$$
n= \begin{cases}-\frac{L}{2}+1, \ldots, \frac{L}{2} & (L=\text { even }) \\ -\frac{L-1}{2}, \ldots, \frac{L-1}{2} & (L=\text { odd }).\end{cases} \tag{A9}
$$

Equations (A2), (A8), and (A9) define a set of $L$ non-degenerate eigenstates of the translation operator $T_{1}$. Since the latter commutes with the Hubbard Hamiltonian $\mathbf{H}$ under PBC or TBC, we can see that the $b_{k}^{\dagger}$ also diagonalize $\mathbf{H}$.

To complete the diagonalization, we have to find the eigenvalues associated with the $b_{k}^{\dagger}$. On the basis of the latter, the Hubbard Hamiltonian takes the form

$$
\mathbf{H}=\sum_{k}\left(\epsilon_{k}-\mu\right) b_{k}^{\dagger} b_{k}, \tag{A10}
$$

from which we have that

$$
\left[\mathbf{H}, b_{k}^{\dagger}\right]=\left(\epsilon_{k}-\mu\right) b_{k}^{\dagger}. \tag{A11}
$$

36

To identify the eigenvalues $\epsilon_k$ we therefore need to compute the commutator on the left-hand side of Eq. (A11) and start out by computing the commutator $[\mathbf{H}, a_\ell^\dagger]$ between the Hamiltonian and a local operator $a_\ell^\dagger$ ($\ell = 1, \dots, L$). From Eq. (29), with $U = 0$, we have that

$$
[\mathbf{H}, a_\ell^\dagger] = -t a_{\ell+1}^\dagger - t^* a_{\ell-1}^\dagger - \mu a_\ell^\dagger \qquad (\ell = 1, \dots, L). \tag{A12}
$$

Reference to Eq. (A2) now shows that

$$
\sqrt{L}[\mathbf{H}, b_k^\dagger] = -t \sum_{\ell=1}^L \left(e^{-ik\ell} a_{\ell+1}^\dagger\right) - t^* \sum_{\ell=1}^L \left(e^{-ik\ell} a_{\ell-1}^\dagger\right) - \mu - \sum_{\ell=1}^L e^{-ik\ell} a_\ell^\dagger. \tag{A13}
$$

We then let $\ell \to \ell-1$ in the first sum on the right-hand side and $\ell \to \ell+1$ in the second sum. The limits of the first and second sums will change. Nonetheless, thanks to boundary condition, which makes $\ell = 0$ ($\ell = N+1$) equivalent to $\ell = N$ ($\ell = 1$), the sums will still cover all lattice sites, $\ell = 1, \dots, L$. It therefore follows that

$$
[\mathbf{H}, b_k^\dagger] = -t e^{ik} b_k^\dagger - t^* e^{-ik} b_k^\dagger - \mu b_k^\dagger. \tag{A14}
$$

We next recall that $t \equiv t_0 e^{i\theta}$, and compare with Eq. (A11) to see that

$$
\epsilon_k = -2 t_0 \cos(k + \theta). \tag{A15}
$$

In particular, under PBC ($\theta = 0$) Eq. (A15) reduces to the equality

$$
\epsilon_k = -2 t_0 \cos(k), \tag{A16}
$$

and under TBC with the special torsion $\Theta = (\pi/2)L$, to the equality

$$
\epsilon_k = 2 t_0 \sin(k). \tag{A17}
$$

### 2. Open boundary condition

Open boundary condition invalidates Bloch's Theorem. Instead of a running wave, we may visualize a wave-function that vanishes at $\ell = 0$ and $\ell = L+1$, an image that associates the following single-particle operator with the single-particle eigenvectors:

$$
d_k^\dagger = \sqrt{\frac{2}{L+1}} \sum_{\ell=1}^L \sin(k\ell) c_\ell^\dagger, \tag{A18}
$$

subject to the condition that $\sin(k\ell)$ vanish for $\ell = L + 1$, i. e., for momenta given by the equality

$$
k = \frac{\ell\pi}{L + 1} \quad (\ell = 1, \ldots, L). \tag{A19}
$$

To show that the $d_k^\dagger$ in Eq. (A18) diagonalize Eq. (1), we again compute the commutator $[\mathbf{H}, c_\ell^\dagger]$. Under OBC we find that

$$
\begin{aligned}
{[\mathbf{H}, c_\ell^\dagger]} &= -\mu c_\ell^\dagger - t_0 c_2^\dagger & & (\ell = 1); \\
{[\mathbf{H}, c_\ell^\dagger]} &= -\mu c_\ell^\dagger - t_0 c_{\ell+1}^\dagger - t_0 c_{\ell-1}^\dagger & & (1 < \ell < L); \\
{[\mathbf{H}, c_\ell^\dagger]} &= -\mu c_\ell^\dagger - t_0 c_{L-1}^\dagger & & (\ell = L).
\end{aligned} \tag{A20}
$$

From Eqs. (A18) and (A20) we then have that

$$
[\mathbf{H}, d_k^\dagger] = -\sqrt{\frac{2}{L + 1}} t_0 \left( \sum_{\ell=2}^L \sin\left(k(\ell - 1)\right) c_\ell^\dagger + \sum_{\ell=1}^{L-1} \sin\left(k(\ell + 1)\right) c_\ell^\dagger \right) - \mu d_k^\dagger. \tag{A21}
$$

Since $\sin(k\ell)$ vanishes for $\ell = 0$, we can let the summation index in the first sum on the right-hand side of Eq. (A21) run from $\ell = 1$ to $\ell = L$. Likewise, given that $\sin[k(L+1)] = 0$ [see Eq. (A19)], we can extend the second sum to $\ell = L$, to obtain the expression

$$
[\mathbf{H}, d_k^\dagger] = -\sqrt{\frac{2}{L + 1}} t_0 \sum_{\ell=1}^L \left( \sin\left(k(\ell - 1)\right) + \sin\left(k(\ell + 1)\right) \right) c_\ell^\dagger - \mu d_k^\dagger. \tag{A22}
$$

Expansion of the sines in the summand on the right-hand side reduces Eq. (A22) to the form

$$
[\mathbf{H}, d_k^\dagger] = -2 t_0 \cos(k) \sqrt{\frac{2}{L + 1}} \sum_{\ell=1}^L \sin(k\ell) c_\ell^\dagger - \mu d_k^\dagger. \tag{A23}
$$

Comparison with Eq. (A18) then shows that

$$
[\mathbf{H}, d_k^\dagger] = \left( -2 t_0 \cos(k) - \mu \right) d_k^\dagger, \tag{A24}
$$

which allows us to write the OBC Hamiltonian in a diagonal form akin to Eq. (A10):

$$
\mathbf{H} = \sum_k (\epsilon_k - \mu) d_k^\dagger d_k, \tag{A25}
$$

with the $\epsilon_k$ from Eq. (A16).

Equation (A16) describes the dispersion relations for both OBC and PBC. Nonetheless, the single-particle energies $\epsilon_k$ for OBC are distinct from the $\epsilon_k$ for PBC, because the allowed momenta are boundary-condition dependent. For OBC, the $k$ are given by Eq. (A19); for PBC, they are determined by Eqs. (A8) and (A9).

### 3. Dispersion relations

Figure 12 compares the dispersion relations for PBC, TBC, and OBC. As an illustration, the single-particle levels for $L = 4$ are depicted for each condition. The single-particle levels for PBC or OBC are given by Eqs. (A16) with $k$ defined by Eqs. (A8) or (A19), respectively. Under TBC the levels are given by (A15), with $k$ defined by Eq. (A8). With $\mu = 0$, which corresponds to ground-state occupation $N = 4$, the levels with $\epsilon_{k} < 0$ are doubly occupied in the ground state, while the levels at $\epsilon_{k} = 0$ have single occupation.

With $L = 4$, the special torsion in Eq. (22) is $\Theta = 2\pi$, equivalent to $\Theta = 0$. The energy levels for PBC and for TBC must therefore be identical. Comparison between panels (a) and (b) in the figure shows how two distinct sets of allowed moment can yield the same single-particle energies. Under TBC with $\Theta \neq 2\pi$ [panel (c) in Fig. 12] or OBC [panel (d)] the single-particle energies are different; there is no zero-energy level, for instance.

The single-particle spectra in panels (a), (b), and (d) of Fig. 12 are particle-hole symmetric. The bold dashes occur in pairs with energies $\pm\epsilon$, even though their momenta are changed under particle-hole transformation: for positive $k$, for instance, $k \to \pi - k$ in panels (a), (b), and (d). The dispersion relation in panel (b), TBC with torsion $\Theta = (\pi/2)L$, is an odd function of $k$, a symmetry that, for all $L$, introduces a zero-energy level, at $k = 0$ in the single-particle energy spectrum. The special torsion $\Theta = (\pi/2)L$ therefore reproduces the feature of the infinite-lattice $U = 0$ model responsible for the vanishing energy gap at half-filling. No such zero-energy level is found in panel (c) of Fig. 12, which is particle-hole asymmetric, like all spectra for TBC with $\Theta \neq (\pi/2)L$.

Depending on boundary condition, the $U = 0$ infinite-lattice Hamiltonian can have any of the dispersion relations represented by red solid lines in Fig. 12. With $L \to \infty$, all momenta in the range $-\pi < k \leq \pi$ are allowed, and at least one of them will satisfy $\epsilon_{k} = 0$. Under OBC, for example, the single-particle energy vanishes at $k = \pi/2$. If $N = L$, at zero temperature all levels below (above) $\epsilon_{k} = 0$ will be filled (vacant), and the zero-energy level guarantees that it will cost zero energy to add or to remove an electron from the ground state. There is no energy gap.


![](./images/867773645995377188_12.jpg)

FIG. 12. Dispersion relations for (a) periodic boundary condition, (b) twisted boundary condition with torsion $\Theta = (\pi/2)L$ (local torsion $\theta = \pi/2$), (c) twisted boundary condition with torsion $\Theta = (\pi/6)L$ (local torsion $\theta = \pi/6$), and (d) open boundary condition. In each plot bold blue dashes indicate the single-particle levels for $L = 4$. At half filling, the chemical potential is $\mu = 0$, the negative-energy levels are doubly occupied, the zero-energy levels are singly occupied, and the positive-energy levels are vacant, as indicated by the vertical arrows. The dispersion relation is an even function of $k$ for periodic boundary condition, and an odd function for twisted boundary condition with the special torsion $\Theta = (\pi/2)L$. By contrast, for $\Theta = (\pi/6)L$ the dispersion relation is asymmetric.

### 4. Ground-state energy

In the ground state, all levels below the Fermi level are filled. If we introduce the notation $k = \text{occ}$ to denote the momenta of the occupied levels, the expression for the ground-state energy under PBC or OBC reads

$$
E_{\Omega} = -4t_0 \sum_{k=\text{occ}} \cos(k), \tag{A26}
$$

where the momenta are specified by Eqs. (A8) or (A19), respectively, and the single-particle energies from (A16) have been doubled to account for spin degeneracy.

Under TBC the momenta are again given by Eq. (A8), and the single-particle energies, from (A15), which yields

$$
E_{\Omega} = -4t_0 \sum_{k=\text{occ}} \cos(k + \theta), \tag{A27}
$$

which for the special torsion $\Theta \equiv L\theta = (\pi/2)L$ reduces to the form

$$
E_{\Omega} = 4t_0 \sum_{k=\text{occ}} \sin(k). \tag{A28}
$$

For all $L$, the ground-state energy can always be analytically computed, but the computation depends on boundary condition and $L$ parity. For OBC and even $L$, for instance, Eq. (A26) reads

$$
E_{\Omega} = -4t_0 \sum_{\ell=1}^{L/2} \cos\left( \frac{\pi \ell}{L+1} \right). \tag{A29}
$$

It proves convenient to rewrite the right-hand side of Eq. (A29) as the real part of a complex number:

$$
E_{\Omega} = -4t_0 \Re \sum_{\ell=1}^{L/2} \exp\left( \frac{i\pi \ell}{L+1} \right), \tag{A30}
$$

because the summand then defines a geometric progression, which can be easily summed. The following expression results:

$$
E_{\Omega} = -4t_0 \Re \frac{i \exp\left( \frac{i\pi}{2(L+1)} \right) - \exp\left( \frac{i\pi}{L+1} \right)}{\exp\left( \frac{i\pi}{L+1} \right) - 1}. \tag{A31}
$$


We then multiply the fraction on the right-hand side of Eq. (A31) by the complex conjugate of the denominator to show that

$$
E_{\Omega}=-2 t_{0} \frac{2 \sin \left(\frac{\pi}{2(L+1)}\right)-1+\cos \left(\frac{\pi}{L+1}\right)}{1-\cos \left(\frac{\pi}{L+1}\right)}. \tag{A32}
$$

which immediately leads to the expression

$$
E_{\Omega}=2 t_{0}\left(1-\frac{1}{\sin \left(\frac{\pi}{2(L+1)}\right)}\right). \tag{A33}
$$

Similar analyses yield the other expressions in Table II, which compares the ground-state energies for OBC, PBC, and TBC. In the $L \rightarrow \infty$ limit, the right-hand sides of Eqs. (A26) or (A27) can be more easily computed. For PBC, for instance, we find that

$$
E_{\Omega}=\frac{L}{\pi} \int_{-\pi / 2}^{\pi / 2} \epsilon_{k} \mathrm{~d} k. \tag{A34}
$$

Here the prefactor of the integral on the right-hand side is the density $L/(2\pi)$ of allowed $k$ levels in momentum space multiplied by the spin degeneracy, and the energies $\epsilon_{k}$ are given by Eq. (A16). The integral on the right-hand side of Eq. (A34) computed, we find that

$$
E_{\Omega}=-\frac{4 L}{\pi} t_{0}, \tag{A35}
$$

which amounts to the per-particle energy in Eq. (30).

### Appendix B: Analytical results for $U \rightarrow \infty$.

#### 1. Open boundary condition

Under OBC, the energy levels are given by Eq. (A16), with $k$ defined by Eq. (A19). At half filling, with $N=L$, each level is singly occupied in the ground state. Since the distribution of energy levels is particle-hole symmetric, the contribution of the kinetic energy to the ground-state energy vanishes, so that

$$
E_{\Omega}^{N=L}=-\mu L. \tag{B1}
$$

By contrast, in the $N=L-1$ ground state the topmost level, with single-particle level

$$
\epsilon_{k_{\max }}=2 t_{0} \cos \left(\frac{\pi L}{L+1}\right), \tag{B2}
$$

is vacant, and the corresponding many-body eigenvalue will include the negative of $\epsilon_{k_{max}}$, that is

$$
E_{\Omega}^{L-1}=-2 t_{0} \cos \left(\frac{\pi}{L+1}\right)-\mu(L-1). \tag{B3}
$$

## 2. Closed boundary conditions

The exact results under $PBC^{34,39,43}$ support the attractive image of individual levels labeled by momenta. The same image holds under TBC. Either under PBC or TBC, however, only for $U=0$ are the allowed $k$ given by Eq. (A8). Without Coulomb interaction, the momentum states are decoupled from each other, and the allowed $k$ are solely determined by boundary condition. For $U \neq 0$, by contrast, the $k$ states are interdependent, and the allowed momenta depend on the spin degrees of freedom. Even in the $U \rightarrow \infty$ limit, which is relatively simple under OBC, as discussed in Sec. B 1, the conditions determining the allowed momenta under PBC or TBC depend on the total spin $S$ and its component, $S_{z}$.

As an illustration consider the Hamiltonian (1) with $L=4$ under TBC with the special torsion $\Theta=(\pi / 2) L$, which is equivalent to PBC, and let $U \rightarrow \infty$. The conservation laws divide the Fock space into sectors labeled by the charge $N$, total spin $S$, total spin component $S_{z}$ and momentum $k$. We choose the chemical potential $\mu$ so that the ground state lies in one of the sectors with $N=3$.

Coulomb repulsion forces the three electrons to occupy three distinct sites. For definiteness, let us assume that the unoccupied state is at site $\ell=4$. The total spin $S$ is the sum of three spin-1/2 variables. Each variable can have $S_{z}=\uparrow$ or $S_{z}=\downarrow$. The three spins can therefore be found in $2^{3}=8$ configurations. The maximum spin resulting from addition of the three variables is $S=3 / 2$. The minimum is $S=1 / 2$. With $S=3 / 2, S_{z}$ can take four distinct values—a quadruplet. Out of the eight possible configurations, four states must therefore constitute two doublets, with $S=1 / 2$.

### a. Quadruplet.
The $S_{z}=S=3 / 2$ member of the quadruplet, known as the fully-stretched state because the three spin components are aligned, is given by the expression

$$
\left|\frac{3}{2}, \frac{3}{2} ; \ell=4\right\rangle=c_{1 \uparrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \uparrow}^{\dagger}|\emptyset\rangle, \tag{B4}
$$

where the label $\ell=4$ on the left-hand side reminds us that the fourth site is vacant.


Cyclic permutation of both sides of Eq. (B4) yields the spin eigenstates $|3/2,3/2,\ell\rangle$ ($\ell = 1,2,3$). In analogy with Eq. (A2), we can then construct four eigenstates of the translation operator $T_1$:

$$
\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle=\frac{1}{2} \sum_{\ell=1}^{4} e^{-i k \ell}\left|\frac{3}{2}, \frac{3}{2} ; \ell\right\rangle. \tag{B5}
$$

To determine the allowed momenta $k$ in Eq. (B5), we translate both sides by one lattice parameter, that is,

$$
T_{1}\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle=\frac{1}{2} \sum_{\ell=1}^{4} e^{-i k \ell}\left|\frac{3}{2}, \frac{3}{2} ; \ell+1\right\rangle, \tag{B6}
$$

or if we let $\ell \to \ell-1$ in the sum on the right-hand side,

$$
T_{1}\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle=e^{i k} \frac{1}{2} \sum_{\ell=0}^{3} e^{-i k \ell}\left|\frac{3}{2}, \frac{3}{2} ; \ell\right\rangle. \tag{B7}
$$

Under closed boundary condition, $\ell=0$ is equivalent to $\ell=L \equiv 4$, and it follows that

$$
T_{1}\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle=e^{i k}\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle, \tag{B8}
$$

provided that $e^{i k L}=1$, which condition determines the allowed momenta:

$$
k=-\frac{\pi}{2}, 0, \frac{\pi}{2}, \pi. \tag{B9}
$$

According to Eqs. (B8) and (B9), the $\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle$ are non-degenerate eigenstates of the translation operator $T_1$, which commutes with the model Hamiltonian. It follows that the momentum eigenvectors $\left|\frac{3}{2}, \frac{3}{2}, k=n \pi / 2\right\rangle$ ($n=-1, \ldots, 2$) are eigenstates of $\mathbf{H}$. In fact, straightforward algebra shows that

$$
\mathbf{H}\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle=\left(2 t_{0} \sin k-3 \mu\right)\left|\frac{3}{2}, \frac{3}{2}, k\right\rangle \quad \left(k=-\frac{\pi}{2}, 0, \frac{\pi}{2}, \pi\right). \tag{B10}
$$

The momentum $k=-\pi/2$ yields the lowest eigenvalue,

$$
E_{S=3 / 2}=-2 t_{0}-3 \mu. \tag{B11}
$$

Equation (B10) has simple physical interpretation. The vacancy—a hole—at site $\ell$ in the state $|3/2,3/2;\ell\rangle$ ($\ell=1,2,3,4$) can hop to either neighboring site, $\ell-1$ or $\ell+1$, just as the electron at site $\ell$ in Eq. (A2) can hop to the neighboring sites. The spectrum of the model Hamiltonian in the $S=S_z=3/2$ sector therefore define single-particle energies forming a band analogous to the ones in Fig. 12(b), with single-particle energies given by Eq. (A17).

44

b. Doublets. The quadruplet (B4) is unique, but the two doublets are not. Two doublets are the symmetric combinations

$$
\left|\frac{1}{2}, \frac{1}{2}, g ; \ell=4\right\rangle=\frac{1}{\sqrt{6}}\left(c_{1 \uparrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \downarrow}^{\dagger}-2 c_{1 \uparrow}^{\dagger} c_{2 \downarrow}^{\dagger} c_{3 \uparrow}^{\dagger}+c_{1 \downarrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \uparrow}^{\dagger}\right),\qquad(\text{B12})
$$

which is even ($g$) under left-right inversion of the lattice segment $\ell=1,2,3$, and

$$
\left|\frac{1}{2}, \frac{1}{2}, u ; \ell=4\right\rangle=\frac{1}{\sqrt{2}}\left(c_{1 \uparrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \downarrow}^{\dagger}-c_{1 \downarrow}^{\dagger} c_{2 \uparrow}^{\dagger} c_{3 \uparrow}^{\dagger}\right),\qquad(\text{B13})
$$

which is odd ($u$). To verify that the right-hand sides are doublets, we only have to check that $S_{+}\left|\frac{1}{2}, \frac{1}{2}, p ; \ell=4\right\rangle=0$ ($p=g, u$), where the raising operator is $S_{+} \equiv \sum_{\ell} c_{\ell \uparrow}^{\dagger} c_{\ell \downarrow}$.

The choices defined by Eqs. (B12) and (B13) are not unique, because any linear combination between their right-hand sides will also have spin 1/2. One can easily verify that they are normalized and mutually orthogonal. Cyclic permutation of Eqs. (B12) and (B13) yields three other pairs with vacancies at sites $\ell=1,2$, and 3, from which eight eigenstates of the translation operator $T_{1}$ can be constructed, as in Eq. (B5). The allowed momenta are once more given by Eq. (B9). For each sector with $S=S_{z}=1 / 2$ and given $k$, two states $|1 / 2,1 / 2, p, k\rangle$ ($p=g, u$) result. Projection of the model Hamiltonian upon the orthonormal basis formed by these two states yields a $2 \times 2$ matrix:

$$
\mathcal{H}_{S=1 / 2, k}=-t_{0}\left[\begin{array}{cc}
\sin (k) & -\sqrt{3} i \cos (k) \\
\sqrt{3} i \cos (k) & \sin (k)
\end{array}\right]-3 \mu.\qquad(\text{B14})
$$

Diagonalization yields the two eigenvalues of the Hamiltonian in the $S=S_{z}=1 / 2, k$ sector:

$$
E_{1 / 2, k}^{ \pm}=-t_{0}\left(\sin (k) \pm \sqrt{3} \cos (k)\right)-3 \mu.\qquad(\text{B15})
$$

The lowest eigenvalues among the four $S=S_{z}=1 / 2, k$ ($k=-\pi / 2,0, \pi / 2, \pi$) sectors lie in the $k=0$ and $k=\pi$ sectors:

$$
E_{1 / 2,0}^{+}=E_{1 / 2, \pi}^{-}=-\sqrt{3} t_{0}-3 \mu.\qquad(\text{B16})
$$

c. Bethe-Ansatz approach. Unfortunately, the same analysis cannot be extended to longer lattices, because the number of basis states grows exponentially with $L$. The alternative is the Bethe-Ansatz solution. $^{38,39}$

The Bethe-Ansatz solution covers any lattice size $L$, under OBC, PBC, or TBC. Instead of a closed expression for the eigenvalues of the Hamiltonian, it yields a set of coupled nonlinear

45

equations, known as the Lieb-Wu equations. For most choices of the model parameters, the Lieb-Wu equations are notoriously difficult to solve, even numerically. The exceptions are the $U=0$ limit, discussed in Section IV A, the infinite system, $L \to \infty$, to be discussed in Section B 3, and the $U \to \infty$ limit, to which we now turn.

The notation we have adopted, in which $N$ denotes the number of electrons and $M$, the number of $\downarrow$-spin electrons, follows Lieb and Wu. $^{38}$ The Bethe Ansatz approach seeks $N$-electron eigenstates described by real-space eigenfunctions $\Psi(x_{1}, x_{2},..., x_{N} ; \sigma_{1},..., \sigma_{N})$, dependent on the particle positions $x_{j}$ and spin components $\sigma_{j}(j=1,..., N)$.

The eigenfunctions are parametrized by two sets of quantum numbers: $k_{n}(n=1,..., N)$ and $\lambda_{m}(m=1,..., M)$, associated with the charge and spin degrees of freedom, respectively. To determine the $k_{n}$ and $\lambda_{m}$, a system of $N+M$ non-linear coupled algebraic equations must be solved.

The eigenvalues of the Hamiltonian depend only on the $k_{n}$, which can be formally identified with momenta. If $U=0$, the $k_{n}$ coincide with the single-particle momenta $k$ in Sec. IV A. With $U \neq 0$ they are no longer given by Eq. (A8) or by Eq. (A19) and have to be determined from the Lieb-Wu equations.

Once the $k_{n}$ are found, the eigenvalues of the Hamiltonian under OBC or PBC can be computed from a sum analogous to Eq. (A26): $^{34,38,39}$

$$
E=-2 t_{0} \sum_{n=1}^{N} \cos \left(k_{n}\right)-\mu N, \qquad \text{(B17)}
$$

where the sum runs over the $N$ occupied $k_{n}$.

For TBC, the sum is analogous to the right-hand side of Eq. (A27)

$$
E=-2 t_{0} \sum_{n=1}^{N} \cos \left(k_{n}+\theta\right)-\mu N, \qquad \text{(B18)}
$$

which for the special torsion $\Theta \equiv L \theta=(\pi / 2) L$ reads

$$
E=2 t_{0} \sum_{n=1}^{N} \sin \left(k_{n}\right)-\mu N. \qquad \text{(B19)}
$$

The chemical potential is determined by the condition $\partial \bar{E} / \partial N=0$, where $\bar{E}$ is the thermodynamical average of the eigenvalues $E$. At zero temperature, $\mu$ is such that the $N$ occupied $k_{n}$ satisfy the inequality $-2 t \cos (k_{n}) \leq \mu(n=1,..., N)$.

![](./images/867773645995377188_13.jpg)

FIG. 13. Computation of the ground-state energy from the solution of the Lieb-Wu equations in the $U \to \infty$ limit, under TBC with the special torsion $\Theta = (\pi/2)L$. $L$, $N$, and $M$ are the lattice size, the number of electrons, and the number of $\downarrow$-electrons respectively. The ground-state energy is computed from Eq. (B19), where the $k_n$, given by Eq. (B21), can be regarded as momenta of spinless electrons. To determine the phase $\Lambda$, one starts out by considering a subsidiary gas of non-interacting particles with momenta $q_m$. The $M$ integers $m$ are chosen so that the resulting $q_m$, given by Eq. (B22), lie in the First Brillouin Zone. Given the $q_m$, Eq. (B24) determines the phase $\Lambda$. The next steps are depicted on the right-hand panel. We start by determining the $L$ allowed momenta $k_n$. The integers $n$ are chosen to position the $k_n$ in the First Brillouin Zone and to minimize the energy in Eq. (B18). The resulting minimum energy $E_{\mathcal{M}}$ depends on $\Lambda$ and hence upon our choice of the set $\mathcal{M}$. To find the ground-state energy, we have to repeat the procedure for all possible $\mathcal{M}$s. The lowest overal $E_{\mathcal{M}}$ is the ground-state energy.

The $U \to \infty$ limit simplifies the Lieb-Wu equations. A schematic depiction of the procedure determining the ground-state energy is presented in Fig. 13. The charge and spin degrees of freedom decouple and can be described separately. The $k_n$ satisfy a relatively simple equation, analogous to Eq. (A5):$^{34,38,39}$

$$
e^{ik_n L} = e^{i\Lambda}, \tag{B20}
$$

where the phase $\Lambda$ depends only on the spin degrees of freedom.

Equation (B20) allows momenta of the form

$$
k_{n}=\frac{2 \pi n+\Lambda}{L}, \tag{B21}
$$

where the $n$'s are integers that define the eigenstate of the Hamiltonian. The integers defining the ground state for TBC, for example, are those that minimize the sum on the right-hand side of Eq. (B19).

To determine the allowed momenta, we therefore need the phase $\Lambda$ and have to examine the spin degrees of freedom. Again, we let the number $M$ of electrons with $\downarrow$ spin be smaller or equal to the number $N-M$ of $\uparrow$ electrons. Although the Lieb-Wu equation describing the spin degrees of freedom seem unwieldy, they have been found to be identical with the equations describing a simpler system, a subsidiary gas with a Hamiltonian that can be trivially diagonalized. $^{43}$ The eigenvalues of the latter Hamiltonian determine the phase $\Lambda$, which can then be substituted on the right-hand side of Eq. (B21) to yield the allowed momenta $k_{n}$.

More specifically, to determine $\Lambda$ one has to find the total momentum of a subsidiary system with $M$ particles on an $N$-site one-dimensional lattice. The particles in the subsidiary system occupy $M$ distinct states labeled by their momenta $q_{m}$ (where $1 \leq m \leq N$), which lie on a flat band, with dispersion relation $\epsilon_{q}=0$. The subsidiary particles must satisfy either anti-periodic or periodic boundary conditions, depending on whether $M$ is even or odd, respectively. The $M$ allowed momenta must therefore satisfy the equalities

$$
e^{i q_{m} N}= \begin{cases}-1 & (M=\text { even }) \\ 1 & (M=\text { odd }),\end{cases} \tag{B22}
$$

which are equivalent to the expressions

$$
q_{m}= \begin{cases}\frac{(2 m+1) \pi}{N} & (M=\text { even }) \\ \frac{2 m \pi}{N} & (M=\text { odd })\end{cases}, \tag{B23}
$$

with integers $1 \leq m \leq N$ that depend on the desired eigenstate of the Hamiltonian.

Given a set of $M$ occupied momenta $q_{m}$, the phase $\Lambda$ is the total momentum

$$
\Lambda=\sum_{m=1}^{M} q_{m}. \tag{B24}
$$

48

This explained, we are ready to find the eigenvalues of the $L=4$, $U \to \infty$ Hubbard Hamiltonian for $N=3$.

First, we set $M=0$, which is equivalent to letting $S_z = S = 3/2$. With $M=0$, the number of particles in the subsidiary gas is zero and it follows from Eq. (B24) that $\Lambda=0$. As in Sec. A 1, we choose the $k_n$ to lie in the first Brillouin Zone. Equation (B21) then yields the allowed momenta:

$$
k_n = \frac{\pi n}{2} \quad (n=-1,0,1,2). \tag{B25}
$$

To obtain the smallest eigenvalue of the Hamiltonian associated to the $k_n$ in Eq. (B25), we fill the three levels making the smallest contribution to the right-hand side of Eq. (B19), i. e., the levels associated with $k_{-1}, k_0$ and $k_2$. The resulting eigenvalue coincides with the right-hand side of Eq. (B11).

Consider now $M=1$. With $M=1$, the $q_m$ allowed by Eq. (B23) are

$$
q_m = \frac{2m\pi}{3} \quad (n=-1,0,1). \tag{B26}
$$

Equation (B24) then determines $\Lambda$. Since $M=1$, the sum on the right-hand side is restricted to a single $q_m$, namely one of the three values in Eq. (B26). The resulting phases are given by the equality

$$
\Lambda = -\frac{2\pi}{3}, 0, \frac{2\pi}{3}. \tag{B27}
$$

Substitution of the right-hand side of Eq. (B27) for $\Lambda$ in Eq. (B21) yields the following allowed momenta:

$$
k = \begin{cases}
-\frac{2\pi}{3}, -\frac{\pi}{6}, \frac{\pi}{3}, -\frac{5\pi}{6} & \left(\Lambda = -\frac{2\pi}{3}\right) \\
\frac{\pi}{2}, 0, \frac{\pi}{2}, -\pi & (\Lambda = 0) \\
\frac{\pi}{3}, -\frac{5\pi}{6}, \frac{\pi}{6}, -\frac{2\pi}{3} & \left(\Lambda = \frac{2\pi}{3}\right)
\end{cases}. \tag{B28}
$$

To obtain the corresponding eigenvalues, from Eq. (B19), for each $\Lambda$ we have to occupy three of the four allowed $k$-states, i. e., leave one level vacant. The resulting energies are given by the equality

$$
E + 3\mu = \begin{cases}
\pm\sqrt{3}t_0, \pm t_0 & \left(\Lambda = \pm\frac{2\pi}{3}\right) \\
0, -2t_0, 2t_0 & (\Lambda = 0),
\end{cases} \tag{B29}
$$

the eigenvalues for $\Lambda=2\pi/3$ being degenerate with those for $\Lambda=-2\pi/3$, and the first eigenvalue for $\Lambda=0$ being doubly degenerate. The lowest eigenvalues for $\Lambda=\pm2\pi/3$ and for $\Lambda=0$ are $-\sqrt{3}t_0-3\mu$ and $-2t_0-3\mu$, respectively.

Comparison of Eq. (B29) with Eqs. (B11) and (B16) shows that with $M=1$ the phase $\Lambda=0$ corresponds to $S=3/2$, $S_z=1/2$ [Eq. (B11)], while $\Lambda=\pm2\pi/3$ corresponds to $S=S_z=1/2$ [Eq. (B16)]. This concludes our illustrative discussion.

The same procedure can be applied to other lattice lengths $L$ and electron numbers $N$. We are especially interested in the minimum energies in the sectors with $N=L$ and $N=L-1$, from which we can compute the $U\rightarrow\infty$ ground-state energy $E_\Omega$ and the energy gap $E_g$ at half filling.

With $N=L$, the ground-state energy vanishes in the $U\rightarrow\infty$ limit. Since each $k$-level can host at most one electron, all levels must be occupied for $N=L$. Particle-hole symmetry then guarantees that the positive contributions to $E_\Omega$ cancel the negative contributions. The ground-state energy is therefore zero.

With $N=L-1$, except for the special length $L=2$, the ground-state energy is negative. For fixed $\Lambda$, Eq. (B21) defines the allowed momenta. In the ground state all levels are filled, except for the highest one, with energy $\epsilon_{max}$. The ground-state energy is $-\epsilon_{max}$. With $\Theta=(\pi L)/2$, provided that the momentum $k_n=\pi/2$ be allowed, the highest allowed energy is $\epsilon_{max}=\epsilon_{k_n=\pi/2}=2t_0$. If $k_n=\pi/2$ is not allowed, the ground-state energy will be $-2t_0\sin(\bar{k})$, where $\bar{k}$ is the allowed momentum closest to $\pi/2$.

For lengths $L$ that are multiples of four, one of the momenta allowed by Eq. (B21) is $k_n=\pi/2+\Lambda/L$. The phase $\Lambda=0$ is always allowed, since we can always choose $M=0$. The momentum $k_n=\pi/2$ is therefore allowed, and the ground-state energy is $-2t_0$.

The ground-state energy is also $-2t_0$ if $N=L-1$ is a multiple of four. Given $\Lambda$, the momentum $k_{n=0}=\Lambda$ is always allowed by Eq. (B21). We choose $M=1$. According to Eq. (B23), the subsidiary momentum $q_{N/4}=\pi/2$ is allowed, and hence the phase can take the value $\Lambda=\pi/2$. It follows that $k_n=\pi/2$ is allowed, and that the ground-state energy is $-2t_0$.

If neither $L$ nor $N$ are multiples of four, $k_n$ cannot equal $\pi/2$, and the ground-state energy $E_\Omega$ is positive. To compute it we must first let $M$ run from zero to $N$, consider all subsidiary momenta $q_m$ momenta compatible with Eq. (B23) for each $M$ and obtain the resulting phases $\Lambda$ from Eq. (B24). Once the $\Lambda$ are computed, the allowed $k_n$ are given by

Eq. (B21). The ground-state energy under TBC is given by the set of $N$ momenta $k_n$ thus determined that minimizes the right-hand side of Eq. (B19).

### 3. Ground-state energy for $L \to \infty$

As $L \to \infty$, the quantum numbers $k_n$ and $\lambda_m$ characterizing the Bethe-Ansatz solution form continua. When the ground state is considered, the Lieb-Wu equations reduce to two coupled integral equations for the densities of the $k_n$ and $\lambda_n$. For the special case $2M = N = L$, i. e., for the spin-unpolarized half-filled band, Lieb and Wu were able to solve the integral equations and derive closed expressions for the ground-state energy $E_\Omega$ and chemical potential. $^{34,38,39}$ Their expression for the ground-state energy, which excludes the contribution from the term proportional to $\mu$ on the right-hand side of Eq. (1), reads

$$
E_{\Omega, N=L}^{L W}=-4 L \int_{0}^{\infty} \frac{J_{0}(\omega) J_{1}(\omega)}{\omega\left(1+e^{\omega U / 2}\right)} \mathrm{d} \omega \tag{B30}
$$

where $J_\nu$ denotes the $\nu$-th order Bessel function.

The chemical potential, defined as the energy difference $E_{\Omega, N+1}^{L W}-E_{\Omega, N}^{L W}$ needed to add a particle to the ground state, is given by the equality

$$
\mu_{+}=\frac{U}{2}-2+4 \int_{0}^{\infty} \frac{J_{1}(\omega)}{\omega\left(1+e^{\omega U / 2}\right)} \mathrm{d} \omega. \tag{B31}
$$

### 4. Energy gap for $L \to \infty$

The subscript $+$ on the left-hand side of Eq. (B31) is necessary, because the chemical potential is discontinuous for $U \neq 0$. The chemical potential $\mu_-$, equal to the energy $E_{\Omega, N}^{L W}-E_{\Omega, N-1}^{L W}$ needed to add a particle to the $N-1$-electron ground state, can be obtained from the particle-hole transformation in Sec. III B 5:

$$
\mu_{-}=U-\mu_{+}. \tag{B32}
$$

The energy gap $E_g = \mu_+ - \mu_-$ is therefore given by the closed expression

$$
E_{g}=U-4+8 \int_{0}^{\infty} \frac{J_{1}(\omega)}{\omega\left(1+e^{\omega U / 2}\right)} \mathrm{d} \omega, \tag{B33}
$$


the right-hand side of which vanishes as $U \to 0$.

1  Lawrence W. Cheuk, Matthew A. Nichols, Katherine R. Lawrence, Melih Okan, Hao Zhang, Ehsan Khatami, Nandini Trivedi, Thereza Paiva, Marcos Rigol, and Martin W. Zwierlein, "Observation of spatial charge and spin correlations in the 2d fermi-hubbard model," Science **353**, 1260–1264 (2016), http://science.sciencemag.org/content/353/6305/1260.full.pdf.

2  Martin Boll, Timon A. Hilker, Guillaume Salomon, Ahmed Omran, Jacopo Nespolo, Lode Pollet, Immanuel Bloch, and Christian Gross, "Spin- and density-resolved microscopy of antiferromagnetic correlations in fermi-hubbard chains," Science **353**, 1257–1260 (2016), http://science.sciencemag.org/content/353/6305/1257.full.pdf.

3  Maxwell F. Parsons, Anton Mazurenko, Christie S. Chiu, Geoffrey Ji, Daniel Greif, and Markus Greiner, "Site-resolved measurement of the spin- correlation function in the fermi-hubbard model," Science **353**, 1253–1256 (2016), http://science.sciencemag.org/content/353/6305/1253.full.pdf.

4  Simon Murmann, Andrea Bergschneider, Vincent M. Klinkhamer, Gerhard Zürn, Thomas Lompe, and Selim Jochim, "Two fermions in a double well: Exploring a fundamental building block of the hubbard model," Phys. Rev. Lett. **114**, 080402 (2015).

5  A. Ghirri, A. Candini, M. Evangelisti, M. Affronte, S. Carretta, P. Santini, G. Amoretti, R. S. G. Davies, G. Timco, and R. E. P. Winpenny, "Elementary excitations in antiferromagnetic heisen- berg spin segments," Phys. Rev. B **76**, 214405 (2007).

6  A. Candini, G. Lorusso, F. Troiani, A. Ghirri, S. Carretta, P. Santini, G. Amoretti, C. Muryn, F. Tuna, G. Timco, E. J. L. McInnes, R. E. P. Winpenny, W. Wernsdorfer, and M. Affronte, "Entanglement in supramolecular spin systems of two weakly coupled antiferromagnetic rings (purple-$Cr_7$Ni)," Phys. Rev. Lett. **104**, 037203 (2010).

7  T. H. Johnson, Y. Yuan, W. Bao, S. R. Clark, C. Foot, and D. Jaksch, "Hubbard model for atomic impurities bound by the vortex lattice of a rotating bose-einstein condensate," Phys. Rev. Lett. **116**, 240402 (2016).

8  A. Gallemí, G. Queraltó, M. Guilleumas, R. Mayol, and A. Sanpera, "Quantum spin models with mesoscopic bose-einstein condensates," Phys. Rev. A **94**, 063626 (2016).

9  J. Salfi, J. A. Mol, R. Rahman, G. Klimeck, M. Y. Simmons, L. C. L. Hollenberg, and S. Rogge,

"Quantum simulation of the Hubbard model with dopant atoms in silicon," Nat. Commun. 7,
11342 (2016).

10 J. Ferrando-Soria, E. Moreno Pineda, A. Chiesa, A. Fernandez, S. A. Magee, S. Carretta,
P. Santini, I. J. Vitorica-Yrezabal, F. Tuna, G. A. Timco, E. J. L. McInnes, and R. E. P.
Winpenny, "A modular design of molecular qubits to implement universal quantum gates,"
Nat. Commun. 7, 11377 EP – (2016).

11 Y. Aharonov and D. Bohm, "Significance of electromagnetic potentials in the quantum theory,"
Phys. Rev. 115, 485-491 (1959).

12 W. Kohn, "Theory of the insulating state," Phys. Rev. 133, A171-A181 (1964).

13 D. J. Thouless, "Long-range order in the antiferromagnetic ground state," Proc. Phys. Soc.
(London) 90, 243 (1967).

14 B. S. Shastry and B. Sutherland, "Twisted boundary conditions and effective mass in heisenberg-
ising and Hubbard chains," Phys. Rev. Lett. 65, 243-246 (1990).

15 B. Sutherland and B. S. Shastry, "Adiabatic transport properties of an exactly soluble one-
dimensional quantum many-body problem," Phys. Rev. Lett. 65, 1833-1837 (1990).

16 M. J. Martins and R. M. Fye, "Bethe ansatz results for Hubbard chains with toroidal boundary
conditions," J. Stat. Phys. 64, 271-276 (1991).

17 M. Shiroishi and M. Wadati, "Integrable boundary conditions for the one-dimensional Hubbard
model," J. Phys. Soc. Jpn. 66, 2288-2301 (1997).

18 H. O. Frota and L. N. Oliveira, "Photoemission spectroscopy for the spin-degenerate Anderson
model," Phys. Rev. B 33, 7871-7874 (1986).

19 M. Yoshida, M. A. Whitaker, and L. N. Oliveira, "Renormalization-group calculation of exci-
tation properties for impurity models," Phys. Rev. B 41, 9403-9414 (1990).

20 J. Tinka Gammel, D.K. Campbell, and E. Y. Loh, "Extracting infinite system properties from
finite size clusters: phase randomization/boundary condition averaging," Synthetic Metals 57,
4437 - 4442 (1993).

21 C. Gros, "Control of the finite-size corrections in exact diagonalization studies," Phys. Rev. B
53, 6865-6868 (1996).

22 C. Lin, F. H. Zong, and D. M. Ceperley, "Twist-averaged boundary conditions in continuum
quantum monte carlo algorithms," Phys. Rev. E 64, 016702 (2001).

23 S. Chiesa, P. B. Chakraborty, W. E. Pickett, and R. T. Scalettar, "Disorder-induced stabiliza-


tion of the pseudogap in strongly correlated systems," Phys. Rev. Lett. 101, 086401 (2008).

24 T. Mendes-Santos, T. Paiva, and R. R. dos Santos, "Size and shape of Mott regions for fermionic atoms in a two-dimensional optical lattice," Phys. Rev. A 91, 023632 (2015).

25 B. Schuetrumpf, W. Nazarewicz, and P. G. Reinhard, "Time-dependent density functional theory with twist-averaged boundary conditions," Phys. Rev. C 93 (2016), 10.1103/Phys- RevC.93.054304.

26 G.M. de Divitiis, R. Petronzio, and N. Tantalo, "On the discretization of physical momenta in lattice QCD," Physics Letters B 595, 408 - 413 (2004).

27 C.T. Sachrajda and G. Villadoro, "Twisted boundary conditions in lattice simulations," Physics Letters B 609, 73 - 85 (2005).

28 P. F. Bedaque and J.-W. Chen, "Twisted valence quarks and hadron interactions on the lattice," Physics Letters B 616, 208 - 214 (2005).

29 J.M. Flynn, A. Jüttner, and C.T. Sachrajda, "A numerical study of partially twisted boundary conditions," Physics Letters B 632, 313 - 318 (2006).

30 F.-J. Jiang and B.C. Tiburzi, "Flavor twisted boundary conditions, pion momentum, and the pion electromagnetic form factor," Physics Letters B 645, 314 - 321 (2007).

31 D. Agadjanov, F. K. Guo, G. Rios, and A. Rusetsky, "Bound states on the lattice with partially twisted boundary conditions," J. High Energy Phys. (2015), 10.1007/JHEP01(2015)118.

32 M. Nitta, "Fractional instantons and bions in the principal chiral model on $R-2\times S-1$ with twisted boundary conditions," J. High Energy Phys. (2015), 10.1007/JHEP08(2015)063.

33 G. Colangelo and A. Vaghi, "Pseudoscalar mesons in a finite cubic volume with twisted boundary conditions," J. High Energy Phys. (2016), 10.1007/JHEP07(2016)134.

34 F. H. L. Essler, H. Frahm, A. Klümper, and V. E. Korepin, The one-dimensional Hubbard model (Cambridge University Press, 2005) available online at http://max2.physics.sunysb.edu/ kore- pin/Hubbard.pdf.

35 N. W. Ashcroft and N. D. Mermin, Solid State Physics (Holt-Saunders International Editions, 1976).

36 See, for instance, W. Kohn and P. Vashista, "General density functional theory," in Theory of the Inhomogeneous Electron Gas, edited by S. Lundqvist and N. H. March (Springer Science + Business Media, LLC, 1983) p. 79.

37 See, for instance, D. J. Griffiths, Introduction to Quantum Mechanics (Prentice Hall, 1994).

38 E. H. Lieb and F. Y. Wu, "Absence of Mott-transition in an exact solution of the short-range, one-band model in one dimension," Phys. Rev. Lett. 20, 1445-1448 (1968).

39 E. Lieb and F. Y. Wu, "The one-dimensional Hubbard model: a reminiscence," Physica A 321, 1-27 (2003).

40 Y. Nagaoka, "Ferromagnetism in a narrow, almost half-filled s band," Phys. Rev. 147, 392-405 (1966).

41 Y. Nagaoka, "Ground state of correlated electrons in a narrow almost half-filled s band," Solid State Commun. 3, 409 - 412 (1965).

42 Hal Tasaki, "Extension of Nagaoka's theorem on the large-$U$ Hubbard model," Phys. Rev. B 40, 9192-9193 (1989).

43 A. G. Izergin, A. G. Pronko, and N. I. Abarenkova, "Temperature correlators in the two- component one-dimensional Hubbard model in the strong coupling limit," Phys. Lett. A 245, 537 (1998).