PHYSICAL REVIEW E 88, 012134 (2013)

# Reentrant disordered phase in a system of repulsive rods on a Bethe-like lattice

Joyjit Kundu* and R. Rajesh†

The Institute of Mathematical Sciences, C.I.T. Campus, Taramani, Chennai 600113, India

(Received 6 June 2013; published 29 July 2013)

We solve exactly a model of monodispersed rigid rods of length $k$ with repulsive interactions on the random locally tree-like layered lattice. For $k \geqslant 4$ we show that with increasing density, the system undergoes two phase transitions: first, from a low-density disordered phase to an intermediate density nematic phase and, second, from the nematic phase to a high-density reentrant disordered phase. When the coordination number is four, both phase transitions are continuous and in the mean field Ising universality class. For an even coordination number larger than four, the first transition is discontinuous, while the nature of the second transition depends on the rod length $k$ and the interaction parameters.

DOI: 10.1103/PhysRevE.88.012134

PACS number(s): 64.60.Cn, 64.70.mf, 64.60.F−, 05.50.+q

## I. INTRODUCTION

A system of long hard rods in three dimensions undergoes a phase transition from a disordered phase with no orientational order to an orientationally ordered nematic phase as the density of rods is increased beyond a critical value [1–3] and has applications in the theory of liquid crystals [4,5]. In two dimensions, though an ordered phase that breaks a continuous symmetry is disallowed [6], the system undergoes a Kosterlitz-Thouless-type transition from an isotropic phase with exponential decay of orientational correlation to a high-density critical phase [7–10]. On two-dimensional lattices, remarkably, there are two entropy-driven transitions for long rods: first, from a low-density disordered (LDD) phase to an intermediate density nematic phase, and, second, from the nematic phase to a high-density disordered (HDD) phase [11]. While the existence of the first transition has been proved rigorously [12], the second transition has been demonstrated only numerically [13]. In this paper, we consider a model of rods interacting via a repulsive potential on the random locally tree-like layered lattice and through an exact solution show the existence of two phase transitions as the density is varied.

We describe the lattice problem in more detail. Rods occupying $k$ consecutive lattice sites along any lattice direction will be called $k$-mers. No two $k$-mers are allowed to intersect, and all allowed configurations have the same energy. For dimers ($k=2$), it is known that the system remains disordered at all packing densities [14]. For $k \geqslant k_{\text{min}}$, it was argued that the system of hard rods would undergo two phase transitions as density is increased [11]. On both the square and the triangular lattices $k_{\text{min}}=7$ [11,15]. Monte Carlo studies show that the first transition from LDD phase to nematic phase is continuous and is in the Ising universality class for the square lattice and in the three-state Potts model universality class for the triangular lattice [15–19]. The existence of this transition has been proved rigorously for large $k$ [12]. The second transition from the nematic to HDD phase was studied using an efficient algorithm that ensures equilibration of the system at densities close to full packing [13,20]. On the square lattice the second transition is continuous with effective critical exponents that are different from the two-dimensional Ising exponents, though a crossover to the Ising universality class at larger length scales could not be ruled out [13]. On the triangular lattice the second transition is continuous, and the critical exponents are numerically close to those of the first transition. This raises the question whether the LDD and HDD phases are the same or different.

Is there a solvable model of $k$-mers that shows two transitions with increasing density and throws light on the HDD phase? The hard core $k$-mer problem was solved exactly on the random locally tree-like layered lattice (RLTL), a Bethe-like lattice [21]. This lattice was introduced because a uniform nematic order is unstable on the more conventional Bethe lattice when the coordination number is larger than four. However, on the RLTL, while a stable nematic phase exists for all even coordination numbers greater than or equal to four, the second transition is absent for hard rods [21]. In this paper, we relax the hard-core constraint and allow $k$-mers of different orientations to intersect at a lattice site. Weights $u,v, \dots$ are associated with sites that are occupied by two, three, $\dots$, $k$-mers. When the weights are zero, we recover the hard rod problem. We solve this model on the RLTL and show that for a range of $u,v, \dots$, the system undergoes two transitions as the density is increased: first, from a LDD phase to a nematic phase and, second, from the nematic phase to a HDD phase. For coordination number $q=4$, the two transitions are continuous and belong to the mean field Ising universality class. For $q \geqslant 6$, where $q$ is an even integer, while the first transition is first order, the second transition is first order or continuous depending on the values of $k,u,v, \dots$. In all cases, it is possible to continuously transform the LDD phase into the HDD phase in the $\rho$-interaction parameters phase diagram without crossing any phase boundary, showing that the LDD and HDD phases are qualitatively similar, and hence the HDD phase is a reentrant LDD phase.

The rest of the paper is organized as follows. In Sec. II we recapitulate the construction of RLTL and formulate the model of rods on this lattice. In Sec III we derive the analytic expression for free energy for fixed density of horizontal and

*joyjit@imsc.res.in
†rrajesh@imsc.res.in

1539-3755/2013/88(1)/012134(8)

012134-1

©2013 American Physical Society

vertical $k$-mers on the four-coordinated RLTL. It is shown that the system undergoes two continuous phase transitions for $k \geqslant 4$. In Sec. IV the free energy is computed for coordination number $q=6$, and the dependence of the nature of the transition on the different parameters is detailed. Section V summarizes the main results of the paper and discusses some possible extensions.

## II. THE RLTL AND DEFINITION OF THE MODEL
The RLTL was introduced in Ref. [21]. In this section, we recapitulate its construction for coordination number $q=4$. Generalization to larger even values of $q$ is straightforward. Consider a collection of $M$ layers, each having $N$ sites. Each site in layer $m$ is connected to the sites in layer $(m-1)$ by two bonds. To distinguish between two orientations, the bonds are divided into two types: $X$ and $Y$. Each site in the $m$th layer is connected with exactly one randomly chosen site in the $(m-1)$-th layer with a bond of type $X$. Similarly bonds of type $Y$ are also connected by random pairing of sites in the two adjacent layers. Hence, the total number of such possible pairing between two layers is $(N!)^{2}$. A typical bond configuration is shown in Fig. 1. For a $q$-coordinated lattice with periodic boundary conditions, the total number of different possible graphs is $(N!)^{q M / 2}$, and with open boundary conditions there are $(N!)^{q(M-1) / 2}$ different possible graphs. In the thermodynamic limit, the RLTL contains few short loops and locally resembles a Bethe lattice.

We consider a system of monodispersed rods of length $k$ on the RLTL. A $k$-mer occupies $(k-1)$ consecutive bonds of same type. Rods on an $X$ ($Y$)-type of bonds will be called $x$-mers ($y$-mers). Weights $e^{\mu_{1}}$ and $e^{\mu_{2}}$ are associated with each $x$-mer and $y$-mer, where $\mu$'s are chemical potentials. Linear rods comprising $k$ monomers are placed on the RLTL such that a site can be occupied by utmost two $k$-mers. Two $k$-mers of the same type cannot intersect. A weight $u$ is associated with every site that is occupied by two $k$-mers of different type. The limiting case $u=0$ corresponds to the hard core problem. For even $q \geqslant 6$, a site can be occupied by utmost $q / 2$ $k$-mers, each of different type.

![](./images/813207440823681025_1.jpg)

FIG. 1. (Color online) Schematic diagram of the RLTL with $N=6$ sites per layer and coordination number 4. A typical bond configuration between layers $m-1$ and $m$ is shown with $X$ bonds in red (solid) lines and $Y$ bonds in blue (dotted) lines.

For a given bond configuration $\mathcal{R}$, let $Z_{\mathcal{R}}(M, N)$ denote the partition function, the weighted sum over all possible rod configurations. We then define the average partition function as

$$
Z_{\mathrm{av}}(M, N)=\frac{1}{N_{\mathcal{R}}} \sum_{\mathcal{R}} Z_{\mathcal{R}}(M, N),\qquad(1)
$$

where $N_{\mathcal{R}}$ is the number of different bond configurations on the lattice. In the thermodynamic limit the mean free energy per site is obtained by

$$
f=-\lim _{M, N \rightarrow \infty} \frac{1}{M N} \ln Z_{\mathrm{av}},\qquad(2)
$$

where the temperature and Boltzmann constant have been set equal to 1.

## III. $k$-MERS ON RLTL WITH COORDINATION NUMBER 4
In this section, we calculate the free energy of the system on the RLTL of coordination number four for fixed $u$ and fixed densities of $x$-mers and $y$-mers. The phase diagram of the system is obtained by minimizing the free energy with respect to $x$-mer and $y$-mer densities for a fixed total density.

### A. Calculation of free energy
To calculate the partition function, consider the operation of adding the $m$th layer, given the configuration up to the $(m-1)$-th layer. The number of ways of adding the $m$th layer is denoted by $C_{m}$. $C_{m}$ will be a function of the number of $x$-mers and $y$-mers passing through the $m$th layer and the number of intersections between $x$-mers and $y$-mers at the $m$th layer.

Let $x_{m}$ ($y_{m}$) be the number of $x$-mers ($y$-mers) whose leftmost sites or heads are in the $m$th layer. $X_{m}$ and $Y_{m}$ are the number of sites in the $m$th layer occupied by $x$-mers and $y$-mers, respectively, but where the site is not the head of the $k$-mer. Clearly,

$$
X_{m}=\sum_{j=1}^{k-1} x_{m-j}, \quad Y_{m}=\sum_{j=1}^{k-1} y_{m-j}, \quad 1 \leqslant m \leqslant M, \quad(3)
$$

with $x_{m}=y_{m}=0$, for $m \leqslant 0$. To have all $k$-mer fully contained with in the lattice for open boundary condition we need to impose, $x_{m}=y_{m}=0$ for, $m \geqslant M-k+2$.

In a $k$-mer, let $h$ denote its head or left most site and $b$ denote the other $k-1$ sites. Then we define $\Gamma_{i j}^{m}$, where $i, j=h, b$, to be the number of intersections at the $m$th layer between site $i$ of an $x$-mer and site $j$ of a $y$-mer. For instance, $\Gamma_{h h}^{m}$ is the number of sites in the $m$th layer, occupied simultaneously by the heads of an $x$-mer and a $y$-mer.

Given $\{x_{m}\},\{y_{m}\}$, and $\{\Gamma_{i j}^{m}\}$, the calculation of $C_{m}$ reduces to an enumeration problem. The details of the enumeration are

given in the Appendix. We obtain
$$
\begin{aligned}
C_{m}= & \frac{N! X_{m}! Y_{m}!\left(N-X_{m}\right)!\left(N-Y_{m}\right)!}{\left(x_{m}-\Gamma_{h h}^{m}-\Gamma_{h b}^{m}\right)!\left(y_{m}-\Gamma_{h h}^{m}-\Gamma_{b h}^{m}\right)!\left(X_{m}-\Gamma_{b b}^{m}-\Gamma_{b h}^{m}\right)!\left(Y_{m}-\Gamma_{b b}^{m}-\Gamma_{h b}^{m}\right)!} \\
& \times \frac{1}{\left(N-X_{m}-Y_{m}-x_{m}-y_{m}+\sum_{i, j=b, h} \Gamma_{i j}^{m}\right)! \prod_{i, j=b, h} \Gamma_{i j}^{m}!}.
\end{aligned}\qquad(4)
$$

The partition function is then the weighted sum of the product of $C_{m}$ for different layers:
$$
Z_{\mathrm{av}}=\frac{1}{(N!)^{2 M}} \sum_{\left\{x_{m}\right\},\left\{y_{m}\right\},\left\{\Gamma_{i j}^{m}\right\}} \prod_{m}\left(C_{m} e^{\mu_{1} x_{m}} e^{\mu_{2} y_{m}} u^{\sum_{i j} \Gamma_{i j}^{m}}\right), \quad(5)
$$
where the sum is over all possible number of x-mers, y-mers, and number of doubly occupied sites. Each term in the sum in Eq. (5) is of order $\exp (N M)$. Hence, for large $N, M$, we replace the summation with the largest summand with negligible error. To find the summand that maximizes the sum, we extremize the summand with respect to the variables that are summed over. For example, to maximize with respect to $x_{l}$, we set
$$
\frac{C\left(\left\{x_{m}+\delta_{m, l}\right\},\left\{y_{m}\right\},\left\{\Gamma_{i j}^{m}\right\}\right) e^{\mu_{1}}}{C\left(\left\{x_{m}\right\},\left\{y_{m}\right\},\left\{\Gamma_{i j}^{m}\right\}\right)} \approx 1, \quad(6)
$$
where $C=\prod_{m} C_{m}$. Likewise, we can write equations for each of the variables.

We look for homogeneous solutions such that $\rho_{x}=x_{m} k / N$, $\rho_{y}=y_{m} k / N$, and $\gamma_{i j}=\Gamma_{i j}^{m} / N$ are variables that are independent of $N$ and have no spatial dependence. Here $\rho_{x}$ and $\rho_{y}$ are fractions of sites in any layer that are occupied by $x$-mers and $y$-mers, respectively. In terms of these variables, Eq. (6) and the corresponding one obtained by maximizing with respect to $y_{j}$ reduce to
$$
\frac{\left(\rho_{x}-\frac{\rho_{x}}{k}\right)^{k-1}\left(1-\rho+\sum_{i j} \gamma_{i j}\right)^{k}\left(\frac{\rho_{x}}{k}-\gamma_{h h}-\gamma_{h b}\right)^{-1}}{\left(1-\rho_{x}+\frac{\rho_{x}}{k}\right)^{k-1}\left(\rho_{x}-\frac{\rho_{x}}{k}-\gamma_{b b}-\gamma_{b h}\right)^{k-1}}=e^{-\mu_{1}}
\qquad(7)
$$
and
$$
\frac{\left(\rho_{y}-\frac{\rho_{y}}{k}\right)^{k-1}\left(1-\rho+\sum_{i j} \gamma_{i j}\right)^{k}\left(\frac{\rho_{y}}{k}-\gamma_{h h}-\gamma_{b h}\right)^{-1}}{\left(1-\rho_{y}+\frac{\rho_{y}}{k}\right)^{k-1}\left(\rho_{y}-\frac{\rho_{y}}{k}-\gamma_{b b}-\gamma_{h b}\right)^{k-1}}=e^{-\mu_{2}},
\qquad(8)
$$
where $\rho=\rho_{x}+\rho_{y}$ is the total density.

The summand in Eq. (5) has to be now maximized with respect to the intersection parameters $\{\Gamma_{i j}^{l}\}$. On doing so, we obtain
$$
\frac{\left[\rho_{x}\left(1-\frac{1}{k}\right)-\gamma_{b b}-\gamma_{b h}\right]\left[\rho_{y}\left(1-\frac{1}{k}\right)-\gamma_{b b}-\gamma_{h b}\right]}{\gamma_{b b}\left(1-\rho+\sum_{i j} \gamma_{i j}\right)}=\frac{1}{u},
\qquad(9a)
$$

$$
\frac{\left(\frac{\rho_{x}}{k}-\gamma_{h h}-\gamma_{h b}\right)\left(\frac{\rho_{y}}{k}-\gamma_{h h}-\gamma_{b h}\right)}{\gamma_{h h}\left(1-\rho+\sum_{i j} \gamma_{i j}\right)}=\frac{1}{u},
\qquad(9b)
$$

$$
\frac{\left(\frac{\rho_{x}}{k}-\gamma_{h h}-\gamma_{h b}\right)\left[\rho_{y}\left(1-\frac{1}{k}\right)-\gamma_{b b}-\gamma_{h b}\right]}{\gamma_{h b}\left(1-\rho+\sum_{i j} \gamma_{i j}\right)}=\frac{1}{u},
\qquad(9c)
$$

$$
\frac{\left(\frac{\rho_{y}}{k}-\gamma_{h h}-\gamma_{b h}\right)\left[\rho_{x}\left(1-\frac{1}{k}\right)-\gamma_{b b}-\gamma_{b h}\right]}{\gamma_{b h}\left(1-\rho+\sum_{i j} \gamma_{i j}\right)}=\frac{1}{u},
\qquad(9d)
$$
where $i, j=h, b$. Equation (9) can easily be solved to express $\gamma_{b b}, \gamma_{h b}$, and $\gamma_{b h}$ in terms of $\gamma_{h h}$:
$$
\gamma_{b b}=(k-1)^{2} \gamma_{h h}, \quad \gamma_{b h}=\gamma_{h b}=(k-1) \gamma_{h h}, \quad(10)
$$
and $\gamma_{h h}$ satisfies the quadratic equation
$$
\gamma_{h h}^{2}-\gamma_{h h} \frac{\rho-\rho u-1}{k^{2}(1-u)}-\frac{u \rho_{x} \rho_{y}}{k^{4}(1-u)}=0. \quad(11)
$$

Equation (10) has a simple interpretation. Given that a $x$-mer and $y$-mer have intersected, the intersecting site is chosen from the head (h) or one of the other $k-1$ sites (b) of the $k$-mers randomly. In addition, the choice of $h$ or $b$ for the $x$-mer and $y$-mer are independent of each other. Thus, the probability of choosing 2 $b$'s is $(k-1)^{2}$ times that of choosing 2 $h$'s and leads to the first relation in Eq. (10). Similar reasoning also gives the second relation in Eq. (10).

From Eq. (5), the free energy is calculated using Eq. (2). Eliminating the chemical potentials using Legendre transforms, we may express the free energy in terms of $\rho_{x}, \rho_{y}$, and $u$ as
$$
\begin{aligned}
f\left(\rho_{x}, \rho_{y}, u\right)= & -\frac{k-1}{k} \sum_{i} \rho_{i} \ln \rho_{i}-\sum_{i}\left[1-\frac{(k-1) \rho_{i}}{k}\right] \ln \left[1-\frac{(k-1) \rho_{i}}{k}\right]+\sum_{i}\left(\rho_{i}-k^{2} \gamma_{h h}\right) \ln \left(\rho_{i}-k^{2} \gamma_{h h}\right) \\
& +\left(1-\rho+k^{2} \gamma_{h h}\right) \ln \left(1-\rho+k^{2} \gamma_{h h}\right)-\frac{\rho}{k} \ln k+k^{2} \gamma_{h h} \ln \left(\frac{k^{2} \gamma_{h h}}{u}\right),
\end{aligned}
\qquad(12)
$$


where $\gamma_{hh}$ is a function of $\rho_x$, $\rho_y$, and $u$ through Eq. (11). This expression for the free energy will turn out to be not convex everywhere. The true free energy $\bar{f}(\rho_x,\rho_y,u)$ is obtained by the Maxwell construction such that

$$
\bar{f}(\rho_x,\rho_y,u) = \mathcal{CE}[f(\rho_x,\rho_y,u)], \tag{13}
$$

where $\mathcal{CE}$ denotes the convex envelope. The densities $\rho_x$ and $\rho_y$ are free parameters. Given total density $\rho$, we minimize the free energy with respect to $\rho_x$ and $\rho_y$ subject to the constraint $\rho_x + \rho_y = \rho$. The isotropic solution corresponds to $\rho_x = \rho_y$, while a solution $\rho_x \neq \rho_y$ corresponds to a nematic phase.

### B. Two phase transitions

To study the phase transitions we define the nematic order parameter as

$$
\psi = \frac{\rho_x - \rho_y}{\rho}. \tag{14}
$$

A nonzero $\psi$ corresponds to a nematic phase. The free energy when expressed as a power series in $\psi$, has the form

$$
\begin{aligned}
f(\rho_x,\rho_y,u) = A_0(\rho,u) + A_2(\rho,u)\psi^2 + A_4(\rho,u)\psi^4 + \cdots, \tag{15}
\end{aligned}
$$

such that $f(\rho_x,\rho_y,u)$ is unchanged when $\psi \leftrightarrow -\psi$. The expressions for the coefficients $A_0(\rho,u), A_2(\rho,u)$, and $A_4(\rho,u)$ are unwieldy, and we do not reproduce them here. However, we find that the coefficient $A_4(\rho,u) > 0$. For small densities, the coefficient of the quadratic term $A_2(\rho,u)$ is positive, and the free energy has a minimum at $\psi = 0$ corresponding to the LDD phase. However, for $k \geqslant 4$, if $u$ is smaller than a critical value $u_c$, then $A_2(\rho,u)$ changes sign continuously at a critical density $\rho_{c1}$, and the free energy has two symmetric minima at $\psi \neq 0$, corresponding to the nematic phase. This qualitative change in the behavior of the free energy for densities close to $\rho_{c1}$ is shown in Fig. 2. As density is further increased, $A_2(\rho,u)$ changes sign continuously from negative to positive at a second critical density $\rho_{c2}$, such that the free energy has a minimum at $\psi = 0$, corresponding to the HDD phase. The dependence of the free energy on $\psi$ for densities close to $\rho_{c2}$ is similar to that shown in Fig. 2.

![](./images/813207440823681025_2.jpg)

FIG. 2. (Color online) Free energy $f(\psi)$ as a function of the order parameter $\psi$ for $\rho \approx \rho_{c1}$. The data are for $k = 6$, $u = 0.15$, and $q = 4$. The curves have been shifted for clarity. The dotted line denotes the convex envelope.

![](./images/813207440823681025_3.jpg)

FIG. 3. (Color online) Order parameter $\psi$ as a function of density $\rho$. For low and high densities, $\psi = 0$, while for intermediate densities, $\psi \neq 0$. The data are for $q = 4$ and $k = 6$.

The variation of the order parameter $\psi$ with density $\rho$ is shown in Fig. 3 for different values of $u$. $\psi$ increases continuously from zero at $\rho_{c1}$ and decreases continuously to zero at $\rho_{c2}$. The average number of intersections between the rods per site, though continuous, also shows nonanalytic behavior at $\rho_{c1}$ and $\rho_{c2}$ (see Fig. 4). The power series expansion of free energy in Eq. (15) has the same form as that of a system with scalar order parameter that has two broken symmetry phases. Thus, the two transitions will be in the mean field Ising universality class. The nematic phase does not exist for $k < 4$.

The phase diagram in the $\rho$-$u$ plane is determined by solving $A_2(\rho,u) = 0$ for $\rho$ and is shown in Fig. 5 for different values of $k$. The difference between the two critical densities decreases with increasing $u$. Beyond a maximum value $u_c(k)$, there is no phase transition, and the system remains disordered at all densities. The critical densities $\rho_{c1}$ and $\rho_{c2}$ may be solved as

![](./images/813207440823681025_4.jpg)

FIG. 4. (Color online) Average number of interactions per site, $N_{\text{ints}}$, as a function of density $\rho$ for different values of $u$. Inset: The region between the two critical points is magnified. The data are for $q = 4$ and $k = 6$.


![](./images/813207440823681025_5.jpg)

FIG. 5. (Color online) Phase diagram when $q=4$ for different values of $k$.

an expansion in $u$. For example, when $k=4$,
$$
\rho_{c 1}=\frac{2}{k-1}+2 u+12 u^{2}+O\left(u^{3}\right), \quad k=4 \quad(16)
$$
and
$$
\begin{array}{r}
\rho_{c 2}=1.13148-2.38675 u-12.2726 u^{2}+O\left(u^{3}\right), \quad k=4. \\
(17)
\end{array}
$$

It is of interest to determine $\rho_{c 2}$ for large $k$. For the hard rod problem, it was conjectured that $\rho_{c 2} \approx 1-a / k^{2}$, when $k \rightarrow \infty$ [11]. For our model, we find
$$
\begin{aligned}
\rho_{c 2} & =\frac{-1+2 k-\sqrt{-3+4 k}}{-1+k}, \quad u \rightarrow 0, \\
& =2-\frac{2}{\sqrt{k}}+\frac{1}{k}-\frac{5}{4 k^{3 / 2}}+\frac{1}{k^{2}}+O\left(k^{-5 / 2}\right). \quad(18)
\end{aligned}
$$

Thus the leading correction is $O(1 / \sqrt{k})$, and not $O(1 / k^{2})$.

$u_c(k)$, the largest value of $u$ for which the nematic phase exists, is determined by solving the equations $A_2(\rho,u)=0$ and $dA_2(\rho,u)/d\rho=0$ simultaneously. $u_c(k)$ increases with $k$ (see Fig. 6) and approaches 1 from below as $k \rightarrow \infty$. At $u_c(k)$ two mean-field Ising critical lines meet.

![](./images/813207440823681025_6.jpg)

FIG. 6. (Color online) $u_c$, the maximum value of $u$ for which the transitions exists as a function of $k$. The data are for $q=4$.

![](./images/813207440823681025_7.jpg)

FIG. 7. (Color online) Free energy $f(\psi)$ as a function of the order parameter $\psi$ for $\rho \approx \rho_{c 1}$ when $q=6$. The data are for $k=6, v=u^{2}$, and $u=0.15$. The dotted lines denote the convex envelopes.

## IV. $k$-MERS ON RLTL WITH $q=6$

The calculation presented in Sec. III may be extended to the case when the coordination number $q \geqslant 6$. We discuss the results when $q=6$. In this case, we associate a weight $u$ ($v$) to a site occupied by two (three) $k$-mers of different type. The calculation of the free energy now involves many more combinatorial factors than for the case $q=4$, but is straightforward. The details of the calculation may be found in Supplemental Material [22]. Let $\rho_x$, $\rho_y$, and $\rho_z$ be the fraction of sites occupied by $x$-mers, $y$-mers, and $z$-mers respectively. We define the order parameter to be $\psi=(\rho_x-\rho_y)/\rho$, where we set $\rho_y=\rho_z$. We find that for $u < u_c(k)$ and $v < u$, the system undergoes two transitions as for the case $q=4$, at critical densities $\rho_{c1}$ and $\rho_{c2}$.

The three-dimensional $\rho$-$u$-$v$ phase diagram may be visualized by studying the phase diagram along three different lines in the $u$-$v$ plane: $v=u^2$, $v=u^3$, and $v=u^4$. The free energy, expressed as a power series in $\psi$, now has the form
$$
\begin{aligned}
f\left(\rho_{x}, \rho_{y}, u, v\right)= & A_{0}(\rho, u, v)+A_{2}(\rho, u, v) \psi^{2}+A_{3}(\rho, u, v) \psi^{3} \\
& +A_{4}(\rho, u, v) \psi^{4}+\cdots,
\end{aligned}
$$
where $A_4(\rho,u,v)>0$ and $A_3(\rho,u,v)$ is in general nonzero. At low densities, $A_2(\rho,u,v)$ is positive, and the free energy has a global minimum at $\psi=0$. With increasing density it develops a second local minimum at $\psi \neq 0$. At $\rho_{c1}$ the two minima become degenerate, and for $\rho_{c1} < \rho < \rho_{c2}$, the free energy has a minimum at $\psi \neq 0$, corresponding to the nematic phase. A typical example is shown in Fig. 7. The order parameter thus shows a discontinuity at $\rho_{c1}$, and the transition is first order. In all the cases we have studied, we find that the first transition from disordered to nematic phase is discontinuous.

On the other hand, the nature of the second transition from the nematic to HDD phase depends on the value of $k$, $u$, and $v$. When $v=u^2$, the second transition is first order for all $k$. However, when $v=u^3$, the second transition could be

![](./images/813207440823681025_8.jpg)

FIG. 8. (Color online) Order parameter $\psi$ as a function of density $\rho$ for different values of $u$ for $k = 7$, $q = 6$, and $v = u^3$. The second transition is first order for $u > u^{*}(k)$ and continuous for $u \leqslant u^{*}(k)$. Here $u^{*}(7) \approx 0.09563$. Regions shown by the thick lines denote coexistence region.

first order or continuous. We find that for $k < 7$, the second transition is always first order, while for $k \geqslant 7$, the order of transition depends on $u$. In Fig. 8 we show the variation of the order parameter $\psi$ with density $\rho$ for different values of $u$ for fixed $k = 7$. The second transition is continuous for small values of $u$ and first order for larger values of $u$. For the transitions that are first order, the system shows coexistence near the transition point. In the coexistence region, the system no longer has uniform density, but instead has regions of the ordered and disordered phases. The order parameter for these densities are obtained from the Maxwell construction. In Fig. 8 the coexistence regions are marked with thick lines. Qualitatively similar behavior is seen for $k > 7$. The second transition is continuous for $u \leqslant u^{*}(k)$ and first order for $u > u^{*}(k)$. The value of $u^{*}(k)$ increases with $k$. When $v = u^4$, the phenomenology is qualitatively similar to that for the case $v = u^3$.

![](./images/813207440823681025_9.jpg)

FIG. 9. (Color online) The number of interactions per site, $N_{\text{ints}}$, as a function of density $\rho$ for two different values of $u$. The data are for $q = 6$, $k = 7$, and $v = u^4$. Inset: The variation with density of (a) order parameter $\psi$, (b) fraction of sites occupied by two $k$-mers, and (c) fraction of sites occupied by three $k$-mers. Here $u = 0.20$.

![](./images/813207440823681025_10.jpg)

FIG. 10. (Color online) Phase diagram for $q = 6$ and $k = 7$ for (a) $v = u^2$, (b) $v = u^3$, and (c) $v = u^4$. Shaded portions denote coexistence regions. Dotted lines denote continuous transitions.

The first order or continuous nature of the second transition is also reflected in the average number of intersections. In Fig. 9 we show the variation for the number of intersections per site with density for $k = 7$ for two values of $u$: one corresponding to a first order and the other to continuous transition. In addition to $\psi$, the average number of intersections between rods per site also shows a discontinuity when the transition is first order. This discontinuity vanishes when the transition becomes continuous.

These observations are summarized in the $\rho$-$u$ phase diagram for $k = 7$ shown in Fig. 10. Shaded portions denote the coexistence regions in the $\rho$-$u$ plane. For $v = u^3$ and $v = u^4$, a second order line terminates at a tricritical point beyond which the transition becomes first order.

The exponents describing the continuous transitions may be found from the Landau-type free energy, Eq. (19). At the first transition $A_2(\rho,u,v) > 0$ and $A_3(\rho,u,v) < 0$. At the

![](./images/813207440823681025_11.jpg)

FIG. 11. (Color online) The order parameter $\psi$ as the density $\rho$ approaches the critical density $\rho_{c2}$ for $u < u^{*}$ and at the tricritical point $u = u^{*}$ when $k = 7$, $q = 6$ and $v = u^3$. The solid lines are power laws (a) $(\rho_{c2} - \rho)^{1/2}$ and (b) $(\rho_{c2} - \rho)$.


spinodal point $A_2(\rho,u,v)$ changes sign to negative. As density is further increased $A_2(\rho,u,v)$ changes sign back to positive. When this occurs, $A_3(\rho,u,v)$ could be positive or negative. If positive, then the transition will be continuous. Now the critical exponents are determined from a Landau free energy functional of the form $A_2\psi^2 + A_3\psi^3$, and hence the critical exponent $\beta=1$, where $\psi\sim(\rho_{c2}-\rho)^\beta$ as $\rho$ approaches $\rho_{c2}$ from below. At the tricritical point $A_3(\rho,u,v)=0$, and the transition is in the mean field Ising universality class with $\beta=1/2$ (see Fig. 11).

## V. SUMMARY AND DISCUSSION

In this paper we studied the problem of monodispersed long rigid rods on the RLTL, a Bethe-like lattice where rods of different orientations are allowed to intersect with weight $u,v,\dots$ depending on whether a site is occupied by two, three, $\dots$, $k$-mers. We showed that the system undergoes two phase transitions with increasing density for $k\geqslant k_{\text{min}}$ and appropriate choice of interaction parameters. For coordination number $q=4$, the two transitions are continuous and in the mean field Ising universality class. For $q=6$, while the first transition is first order, the nature of the second transition depends on the values $k$, $u$, and $v$, giving rise to a rich phase diagram. To the best of our knowledge, it is the only solvable model on interacting rods that shows two phase transitions.

The limit $u\rightarrow0$ is different from $u=0$ (the hard rod problem). When $u=0$, the second transition in absent [21]. When $u$, $v>0$, the fully packed phase is disordered by construction, and if the first phase transition exists, so does a second phase transition. The relaxation of the restriction that only rods of different orientations may intersect at a lattice site does not change the qualitative behavior of the system as the high-density phase remains disordered. There are still two transitions, both in the mean field Ising universality class (when $q=4$). However, the solution becomes more cumbersome.

Similarly when $q=6$, the limit $v\rightarrow0$ is different from $v=0$ when $u>0$. When $v=0$, a lattice site may occupied by utmost two $k$-mers of different type. In this case, the fully packed phase is not necessarily disordered, and for certain values of $k$ and $u$, only one transition is present for increasing density.

For hard rods on the square lattice, Monte Carlo simulations were unable to give a clear answer to the question whether the HDD and LDD phases are qualitatively similar or not [13]. It was argued that the HDD phase on the square lattice has a large crossover length scale $\xi^{*}\sim1500$, and for length scales larger than $\xi^{*}$ it is possible that the HDD phase is not qualitatively different from the LDD phase. This was based on the evidence that vacancies in the HDD phase do not form a bound state. In this paper, by expanding the phase diagram from a one-dimensional $\rho$ phase diagram to a multidimensional $\rho$-interaction parameters phase diagram, we showed that it is always possible to continuously transform the LDD phase into the HDD phase without crossing any phase boundary. This means that the LDD and HDD phases are qualitatively similar, at least for the model on RLTL. It would thus be worthwhile to simulate the hard rods problem on the square lattice for system sizes larger than 1500 and verify the same.

It would also be possible to study the problem with repulsive interactions on the square lattice. The algorithm presented in Refs. [13,20] is generalizable to the case when intersections are allowed. Confirming whether the qualitative behavior is similar to that seen for RLTL would be interesting. Measuring the exponents for the second transition might be easier for such a model as the critical density would be away from the fully packed limit.

For the RLTL with coordination number $q=4$, we showed that for large $k$, $\rho_{c2}\approx2-a/\sqrt{k}+O(k^{-1})$. This is at variance from the prediction from entropy based arguments for the hard rod problem that $\rho_{c2}$ approaches 1 as $k^{-2}$ [11]. It would be interesting to resolve this discrepancy.

The RLTL is suitable for studying hard core models of anisotropic particles. An example is polydispersed systems of hard rods which can show multiple phases [23,24]. Its solution on the RLTL would make rigorous some of the qualitative features of the problem. Another interesting problem is that of percolation of a system of long rods. Using simulations, the dependence of the critical percolation threshold on the rod length, and the probabilities of horizontal and vertical rods being present, has been conjectured [25,26]. These conjectures may be checked on the RLTL through an exact solution. These are promising areas for future study.

## ACKNOWLEDGMENTS

We thank Deepak Dhar and Jürgen F. Stilck for very helpful discussions.

## APPENDIX: CALCULATION OF $C_m$ FOR $q=4$

In this appendix, we derive the expression for $C_m$ as given in Eq. (4). $C_m$ is the total number of ways of connecting the $X$ and $Y$ bonds from the $(m-1)$-th layer to the $m$-th layer consistent with the number of $x$-mers, $y$-mers, and intersections at the $m$th layer.

In the $(m-1)$-th layer, there are $X_m$ and $Y_m$ sites occupied by $x$-mers and $y$-mers that extend to the $m$th layer. These $X_m$ bonds of type $X$ have to be connected to $X_m$ different sites out of the $N$ sites in the $m$th layer. This can be done in

$$
\frac{N!}{(N-X_m)!}
$$

ways. Among the $Y_m$ bonds of type $Y$, $\Gamma_{bb}^m$ of them are connected to sites occupied by an $x$-mer and the remaining $Y_m-\Gamma_{bb}^m$ bonds are connected to empty sites in the $m$th layer. The number of ways of connecting the $Y$ bonds is a product of the two enumerations and is equal to

$$
\frac{Y_m!X_m!}{\Gamma_{bb}^m!(Y-\Gamma_{bb}^m)!(X_m-\Gamma_{bb}^m)!} \times \frac{(N-X_m)!}{(N-X_m-Y_m+\Gamma_{bb}^m)!}.
$$

Now connect the remaining $(N-X_m)$ free bonds of type $X$ and $(N-Y_m)$ free bonds of type $Y$ to sites in layer $m$ that are not occupied by $x$-mers and $y$-mers, respectively. This can be done in

$$
(N-X_m)!(N-Y_m)!
$$

ways.

JOYJIT KUNDU AND R. RAJESH
PHYSICAL REVIEW E 88, 012134 (2013)

We have to now assign sites to $x_m$ and $y_m$ heads in layer $m$. Out of $x_m$ ($y_m$) heads, $\Gamma_{hb}^m$ ($\Gamma_{bh}^m$) of them will be on sites already occupied by only a $y$-mer ($x$-mer). The number of ways of doing this is

$$
\frac{\left(X_{m}-\Gamma_{b b}^{m}\right)!}{\Gamma_{b h}^{m}!\left(X_{m}-\Gamma_{b b}^{m}-\Gamma_{b h}^{m}\right)!} \times \frac{\left(Y_{m}-\Gamma_{b b}^{m}\right)!}{\Gamma_{h b}^{m}!\left(Y_{m}-\Gamma_{b b}^{m}-\Gamma_{h b}^{m}\right)!}.
$$

There are $(N - X_m - Y_m + \Gamma_{bb}^m)$ sites in the $m^{th}$ layer which are unoccupied so far. They can be divided into four groups: $\Gamma_{hh}^m$ sites, each occupied by the heads of an $x$-mer and a $y$-mer, $(x_m - \Gamma_{hh}^m - \Gamma_{hb}^m)$ sites occupied by only a head of an $x$-mer, $(y_m - \Gamma_{hh}^m - \Gamma_{bh}^m)$ sites occupied by only a head of a $y$-mer, and $(N - X_m - Y_m - x_m - y_m + \sum_{ij} \Gamma_{ij}^m)$ unoccupied sites. The number of ways of arranging them is

$$
\begin{aligned}
&\frac{\left(N-X_{m}-Y_{m}+\Gamma_{b b}^{m}\right)!}{\Gamma_{h h}^{m}!\left(x_{m}-\Gamma_{h h}^{m}-\Gamma_{h b}^{m}\right)!\left(y_{m}-\Gamma_{h h}^{m}-\Gamma_{b h}^{m}\right)!} \\
&\quad \times \frac{1}{\left(N-X_{m}-Y_{m}-x_{m}-y_{m}+\sum_{i j} \Gamma_{i j}^{m}\right)!}.
\end{aligned}
$$

The product of all these factors gives $C_m$ as given in Eq. (4).

[1] L. Onsager, Ann. NY Acad. Sci. 51, 627 (1949).
[2] P. J. Flory, Proc. R. Soc. 234, 60 (1956).
[3] R. Zwanzig, J. Chem. Phys. 39, 1714 (1963).
[4] G. J. Vroege and H. N. W. Lekkerkerker, Rep. Prog. Phys. 55, 1241 (1992).
[5] P. G. de Gennes and J. Prost, The Physics of Liquid Crystals (Oxford University Press, Oxford, 1993).
[6] N. D. Mermin and H. Wagner, Phys. Rev. Lett. 17, 1133 (1966).
[7] J. P. Straley, Phys. Rev. A 4, 675 (1971).
[8] D. Frenkel and R. Eppenga, Phys. Rev. A 31, 1776 (1985).
[9] M. D. Khandkar and M. Barma, Phys. Rev. E 72, 051717 (2005).
[10] R. L. C. Vink, Euro. Phys. J. B 72, 225 (2009).
[11] A. Ghosh and D. Dhar, Euro. Phys. Lett. 78, 20003 (2007).
[12] M. Disertori and A. Giuliani, Comm. Math. Phys. doi: 10.1007/s00220-013-1767-1.
[13] J. Kundu, R. Rajesh, D. Dhar, and J. F. Stilck, Phys. Rev. E 87, 032103 (2013).
[14] O. J. Heilmann and E. Lieb, Commun. Math. Phys. 25, 190 (1972).
[15] D. A. Matoz-Fernandez, D. H. Linares, and A. J. Ramirez-Pastor, J. Chem. Phys. 128, 214902 (2008).

[16] D. A. Matoz-Fernandez, D. H. Linares, and A. J. Ramirez-Pastor, Euro. Phys. Lett 82, 50007 (2008).
[17] D. A. Matoz-Fernandez, D. H. Linares, and A. J. Ramirez-Pastor, Physica A 387, 6513 (2008).
[18] D. H. Linares, F. Romá, and A. J. Ramirez-Pastor, J. Stat. Mech. (2008) P03013.
[19] T. Fischer and R. L. C. Vink, Euro. Phys. Lett. 85, 56003 (2009).
[20] J. Kundu, R. Rajesh, D. Dhar, and J. F. Stilck, AIP Conf. Proc. 1447, 113 (2012).
[21] D. Dhar, R. Rajesh, and J. F. Stilck, Phys. Rev. E 84, 011140 (2011).
[22] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevE.88.012134 for details of the calculation for $q=6$.
[23] A. Speranza and P. Sollich, Phys. Rev. E 67, 061702 (2003).
[24] M. Fasolo and P. Sollich, Phys. Rev. Lett. 91, 068301 (2003).
[25] P. Longone, P. M. Centres, and A. J. Ramirez-Pastor, Phys. Rev. E 85, 011108 (2012).
[26] Y. Y. Tarasevich, N. I. Lebovka, and V. V. Laptev, Phys. Rev. E 86, 061116 (2012).

012134-8