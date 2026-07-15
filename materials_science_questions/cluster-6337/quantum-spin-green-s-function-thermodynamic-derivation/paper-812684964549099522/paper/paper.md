![](./images/812684964549099522_1.jpg)

# Universal magnetic fluctuations in the two-dimensional XY model

P. Archambault, S. T. Bramwell, J.-Y. Fortin, P. C. W. Holdsworth, S. Peysson, and J.-F. Pinton

Citation: *Journal of Applied Physics* **83**, 7234 (1998); doi: 10.1063/1.367855

View online: http://dx.doi.org/10.1063/1.367855

View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/83/11?ver=pdfcov

Published by the AIP Publishing

![](./images/812684964549099522_2.jpg)

# Universal magnetic fluctuations in the two-dimensional XY model
P. Archambault
Laboratoire de Physique, Ecole Normale Supérieure, 46 Allée d'Italie,
F-69364 Lyon Cedex 07, France

S. T. Bramwell
Department of Chemistry, University College London, 20 Gordon Street, London, United Kingdom

J.-Y. Fortin, P. C. W. Holdsworth,${}^{\mathrm{a)}}$ S. Peysson, and J.-F. Pinton
Laboratoire de Physique, Ecole Normale Supérieure, 46 Allée d'Italie,
F-69364 Lyon Cedex 07, France

We discuss the probability distribution function for the magnetic order parameter $M$, in the low temperature phase of the two-dimensional $XY$ model. In this phase the system is critical over the whole range of temperature. The thermally averaged value of the order parameter $\langle M\rangle$, which is zero in the thermodynamic limit, has abnormally large finite size corrections. An exact result, within a spin wave calculation gives $\langle M\rangle=(1/2N)^{T/8\pi J}$, where $J$ is the magnetic exchange constant and $N$ the number of spins. We show, using Monte Carlo simulation, that the distribution function, $Q(y-\langle y\rangle)$, $y=T^{-1}L^{T/4\pi J}M$, is an asymmetric universal function. Using a diagramatic technique, we show that the asymmetry comes from three-spin and higher correlations. If only two-spin correlations are considered, the distribution is Gaussian. However, as there are contributions from two-spin terms separated by all distances, the distribution remains broad and is consistent with a divergent susceptibility. © 1998 American Institute of Physics. [S0021-8979(98)51911-1]

The long-ranged correlations that characterize a critical point mean that at this special point finite size effects are much more important than the $1/\sqrt{N}$ corrections given by the central limit theorem. $^{1}$ For example scaling arguments give, for the magnetization, $\langle M\rangle$, at a critical point$^{2}$ $\langle M\rangle \sim L^{-\beta/\nu}$, with $\beta$ and $\nu$ the critical exponents for the magnetization and the correlation length. For strong fluctuations $\beta$ is small and $\nu$ is large, leaving the finite size magnetization measurable right into the physical domain. This is nowhere better observed than in the low temperature phase of the two-dimensional $XY$ model, where the system is critical over a whole range of temperature. In fact it is an ideal system in which to study finite size fluctuations near a critical point as it shows critical behavior over a range of temperatures below the Kosterlitz-Thouless transition temperature $T_{\text{KT}}$, $^{3}$ it is extremely accessible to analytic techniques and is of broad experimental relevance. $^{4}$

The model is defined with the Hamiltonian
$$
H=-J\sum_{\langle i,j\rangle}\cos(\theta_{i}-\theta_{j}), \tag{1}
$$
where $J$ is the ferromagnetic coupling constant and $\theta_{i}$ the angle of orientation of spin vector $\mathbf{S}_{i}$, constrained to lie in a plane. The summation is over nearest neighbors and we take the spins to be on the sites of a square lattice with periodic boundary conditions. We use a system of units with Boltzmann’s constant $k_{B}$ equal to unity throughout. We simplify this to what we refer to as the harmonic $XY$ or $HXY$ model. $^{5}$
Its Hamiltonian is
$$
H=-J\sum_{\langle i,j\rangle}\left[1-\frac{1}{2}\left(\theta_{i}-\theta_{j}-2\pi n\right)^{2}\right], \tag{2}
$$
where $n=0,\pm 1$ is an integer chosen so that $(\theta_{i}-\theta_{j}-2\pi n)$ lies between $\pm\pi$. This model is almost the Villain model, $^{6}$ but is more practical from a numerical point of view, as the vortex variable $n$ is not a thermodynamic variable, but is constrained to the values $n=0,\pm 1$. $^{7}$ We concentrate, in this article, on the temperature regime well below $T_{\text{KT}}$ where the vortex density is exponentially small and the $HXY$ reduces to a model of harmonic spin waves, which can be solved exactly. $^{8}$

We define an instantaneous scalar order parameter $M$:
$$
M=\frac{1}{N}\sqrt{\left(\sum_{i=1,N}\mathbf{S}_{i}\right)\cdot\left(\sum_{i=1,N}\mathbf{S}_{i}\right)}. \tag{3}
$$

Within the spin wave approximation one can derive the following result for the equilibrium magnetization $\langle M\rangle$, exact to leading order in $N$: $^{8}$
$$
\langle M\rangle=\left(\frac{1}{2N}\right)^{T/8\pi J}. \tag{4}
$$

$\langle M\rangle$ falls to zero in the thermodynamic limit, which confirms the Mermin-Wagner theorem $^{9}$ that the thermodynamic magnetization is zero at all finite temperature. However, putting in numbers for $T\sim O(J)$ one can easily convince oneself that $\langle M\rangle$ is measurable throughout the physical domain.

The susceptibility per spin, defined as

${}^{\mathrm{a)}}$Electronic mail: pcwh@enslapp.ens-lyon.fr

![](./images/812684964549099522_3.jpg)

FIG. 1. $\log[\sigma Q(M)]$ vs $(M-\langle M\rangle)/\sigma$ for $T/J=0.5$ for $N=100$ (stars), $N=1024$ (circles), $N=10\,000$ (squares), and for $T/J=1.0$ for $N=1024$ (triangles).

$$
\chi=\frac{N}{T}\left(\left\langle M^{2}\right\rangle-\langle M\rangle^{2}\right), \tag{5}
$$

is given by the expression

$$
\chi=\frac{\langle M\rangle^{2}}{T} \sum_{r}\left\{\exp \left[\frac{T}{J} \times G(r)\right]-1\right\}, \tag{6}
$$

where $G(r)$ is the lattice Green's function for a square lattice

$$
\begin{aligned}
& G(r)=\frac{1}{N} \sum_{q \neq 0} \frac{e^{i \mathbf{q} \cdot \mathbf{r}}}{\gamma_{\mathbf{q}}}, \\
& \gamma_{\mathbf{q}}=4-2 \cos \left(q_{x}\right)-2 \cos \left(q_{y}\right). \tag{7}
\end{aligned}
$$

To an excellent approximation one finds

$$
\chi=\frac{1}{2 a_{2 \mathrm{D}}} \frac{N\langle M\rangle^{2} T}{J^{2}}, \quad a_{2 \mathrm{D}}=258.6, \tag{8}
$$

with the susceptibility per spin therefore diverging as $\chi \sim N^{1-T / 4 \pi J}$.

From Eq. (8) we see that the prefactor of the $\cdots$ 