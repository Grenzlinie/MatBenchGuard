# RESEARCH ARTICLE

## Monte Carlo study of the XY-model on Sierpinski gasket

Božidar Mitrović* and Shyamal K. Bose

Department of Physics, Brock University, St. Catharines, Ontario, Canada L2S 3A1

()

We have performed a Monte Carlo study of the classical XY-model on two-dimensional Sier- pinski gaskets of several cluster sizes. From the dependence of the helicity modulus on the cluster size we conclude that there is no phase transition in this system at a finite temperature. This is in agreement with previous findings for the harmonic approximation to the XY-model on Sierpinski gasket and is analogous to the absence of finite temperature phase transition for the Ising model on fractals with a finite order of ramification.

Keywords: XY-model; fractals; Sierpinski gasket; Monte Carlo simulations

## 1. Introduction

In a series of papers Gefen, Mandelbrot and Aharony [1–4] examined the possibility of phase transitions for discrete-symmetry spin models (e.g. the Ising model) on self-similar fractal structures. By applying renormalization-group techniques they found that the critical properties of such systems vary with several topological characteristics: the (noninteger) fractal dimensionality $D$, the order of ramification $R$ and lacunarity [1]. They established that a lower critical dimensionality is not defined and found that the Ising model on systems with given $D$ have transition temperature $T_c=0$ if the minimum order of ramification $R_{min}$ is finite, and $T_c >0$ if $R_{min}$ is infinite. The order of ramification $R$ at a point $P$ of a structure is defined as the number of bonds which one must cut in order to isolate an arbitrarily large bounded set of points connected to $P$. For two-dimensional Sierpinski gasket (SG) $R_{min}$=3 and $R_{max}$=4 [1]. Subsequently, Monceau and Hsiao [5] did a Monte Carlo study of the Ising model on fractals with infinite $R_{min}$ which had the same fractal dimension $1< D <3$ but different structure. They found direct evidence of so-called weak universality in such systems, i.e. the critical exponents depend not only on $D$, the symmetry of the order parameter and the range of interactions but also on topological features of the fractal, in particular on lacunarity which measures the deviation from translational symmetry.

The question remained as to what happens in the case of $n$-component spin models, with $n \geq 2$, on fractal structures. In [3, 4] a correspondence between pure resistor network connecting sites of a given lattice and the low-temperature prop- erties of the spins with continuous symmetry $(n \geq 2)$ on the same lattice [6] was used to conclude that there is no long-range order at any finite temperature if the fractal dimension $D <2$ even in the case of infinite order of ramification. For

*Corresponding author. Email: bmitrovic@brocku.ca

ISSN: 0141-1594 print/ISSN 1029-0338 online
© 200x Taylor & Francis
DOI: 10.1080/0141159YYxxxxxxxx
http://www.informaworld.com

![](./images/867765956762402903_1.jpg)

Figure 1. The first step in creating Sierpinski gaskets.

two-dimensional SG $D = \ln3/\ln2$=1.585. Subsequently, in their study of the effect of phase fluctuations of the superconducting order parameter in two-dimensional Sierpinski gasket wire networks [7] Vallat, Korshunov and Beck [8] examined the XY-model on such a lattice in the harmonic approximation. They found that the energy of a vortex is always finite on the two-dimensional Sierpinski gasket imply- ing that there is no Berezinskii-Kosterlitz-Thouless transition [9] associated with vortex-antivortex unbinding as free vortices are always present.

Here we present a Monte Carlo study of the XY-model on two-dimensional Sier- pinski gaskets described by the Hamiltonian

$$
H = -J \sum_{\langle i,j \rangle} \cos(\theta_i - \theta_j), \tag{1}
$$

where $0\leq \theta_i <2\pi$ is the angle variable on site $i$, $\langle i,j \rangle$ denotes the nearest neighbors and $J >0$ is the coupling constant. In the case of XY-model on periodic and quasiperiodic lattices [10] the most important excitations at low temperatures are the spin-waves and the harmonic approximation to (1) used in [8] is quite good for the purpose of studying the low-temperature behavior. We compute the heat capacity, the helicity modulus and susceptibility for Sierpinski gaskets of several sizes. The size dependence of the helicity modulus and its sensitivity to the bound- ary conditions clearly indicate that in the thermodynamic limit there is no phase transition at finite temperature.

The rest of the paper is organized as follows. In Section 2 we describe numerical procedure used in calculations and present our numerical results. In Section 3 we summarize our conclusions.

## 2. The numerical procedure and the results

The procedure which we used to generate two-dimensional Sierpinski gaskets is illustrated in Figure 1, which shows the transition from the zeroth-order Sierpinski gasket (the equilateral triangle of side $a$) to the first order gasket. Our basic unit was the fourth order Sierpinski gasket with 123 sites (a gasket of order $m$ has $N$=$3(3^m$$+1)/2$ sites) and the list of the nearest neighbors of each site. The higher order Sierpinski gaskets were created as subsequent generations of the fourth order gasket and we considered gaskets up to order $m$=7 with 3282 sites. In going from the gasket of order $m$ to the gasket of order $m$+1 the list of the nearest neighbors for sites close to the three corners of each of the three $m$th order gaskets had to be modified.

To study the statistical mechanics of the Hamiltonian (1) on Sierpinski gaskets we have used Monte Carlo (MC) simulations based on Metropolis algorithm [11]. For a gasket of given order the simulation would start at a low temperature with

![](./images/867765956762402903_2.jpg)

Figure 2. Calculated heat capacity per site as a function of temperature.

all phases aligned. The first $k$ MC steps per site (sps) were thrown away, followed by seven MC links of $k$ MC sps each. The values of $k$ which we used were 120000, 360000, and 600000, depending on the system size and statistical errors. At each temperature the range over which each angle $\theta_i$ was allowed to vary [12] was adjusted to ensure an MC acceptance rate of about 50%. The errors were calculated by breaking up each link into six blocks of $k/6$ sps, then calculating the average values for each of 42 blocks and finally taking the standard deviation $\sigma$ of these 42 average values as an estimate of the error. The final configuration of the angles $\{\theta_1,\dots,\theta_N\}$ at a given temperature was used as a starting configuration for the next higher temperature. Two types of boundary conditions were considered: closed, where the three corners of an $m$th order gasket were considered to be coupled to each other (then each site has four nearest neighbors) and open, where the three corners are uncoupled to each other.

In Figure 2 we show the results for the heat capacity per site calculated from the fluctuation theorem
$$
C=\frac{1}{N} \frac{\left\langle H^{2}\right\rangle-\langle H\rangle^{2}}{k_{B} T^{2}},\tag{2}
$$
where $k_B$ is the Boltzmann constant, $T$ is the absolute temperature and $\langle\cdots\rangle$ denotes the MC average. The results for the four Sierpinski gaskets were obtained with the closed boundary conditions. In the case of heat capacity the results do not depend on boundary conditions as illustrated in Figure 3. For comparison, we have included in Figure 2 the results obtained for the Hamiltonian (1) on three square lattices with the periodic boundary conditions. The sizes of the square lattices were chosen so that the number of sites is similar to the number of sites for the three

![](./images/867765956762402903_3.jpg)

Figure 3. The heat capacity per site as a function of temperature for the sixth order SG calculated with closed boundary condition (full triangles) and with the open boundary condition (open triangles).

smaller Sierpinski gaskets. As there is no long-range order in two dimensions the heat capacity per site of the square lattices saturates with increasing system size [13]. In the case of Sierpinski gaskets there is virtually no size dependence of the heat capacity per site. This, however, does not mean that the model (1) on two- dimensional SG also leads to the Berezinskii-Kosterlitz-Thouless (BKT) transition resulting from vortex-antivortex unbinding at transition temperature $T_{c}$. The peak in the heat capacity of the square lattices is above the BKT transition temperature where the heat capacity has an unobservable essential singularity [14]. The peak is caused by unbinding of vortex clusters [13] with increasing temperature above $T_{c}$. In the case of Sierpinski gaskets the broad peak in $C$ could result from the average energy per site $\langle E\rangle$ changing monotonically from the values near -2J (each site has four nearest neighbors) at low temperatures to near zero at high temperatures (disordered paramagnetic phase).

A much better indicator of BKT transition is temperature dependence of the helicity modulus. It measures the stiffness of the angles $\{\theta_{i}\}$ with respect to a twist at the boundary of the system. When the Hamiltonian (1) is used to model a set of identical superconducting grains coupled via Josephson tunneling, in which case $\theta_{i}$ is the phase of the superconducting order parameter on grain $i$, the effect of applied magnetic field described by the vector potential $\mathbf{A}$ is included via shift in the phase difference $\theta_{i}-\theta_{j}$ by

$$
A_{i j}=\frac{2 \pi}{\Phi_{0}} \int_{\mathbf{r}_{i}}^{\mathbf{r}_{j}} d \mathbf{r} \cdot \mathbf{A}, \tag{3}
$$

where the line integral is taken along the line joining sites $i$ and $j$ and $\Phi_{0}=h c / 2 e$

is the flux quantum [15]. For a uniform vector potential $\mathbf{A}$ one has $A_{i j}=2 \pi \mathbf{A} \cdot$ $(\mathbf{r}_{j}-\mathbf{r}_{i}) / \Phi_{0}$. Then, the helicity modulus can be defined [15] as

$$
\gamma=\left(\frac{\partial^{2} F}{\partial A^{2}}\right)_{A=0} \quad(4)
$$

where $F$ is the Helmholtz free energy. Using $\partial^{2} F / \partial A^{2}=\left\langle\partial^{2} H / \partial A^{2}\right\rangle-$ $\left\langle(\partial H / \partial A)^{2}\right\rangle /\left(k_{B} T\right)+\left\langle(\partial H / \partial A)\right\rangle^{2} /\left(k_{B} T\right)$ one finds an expression for the helicity modulus which is analogous to (2). For the Sierpinski gaskets $\mathbf{A}$ was taken to be parallel to one of the sides of the triangles (Figure 1) and for the square latices $\mathbf{A}$ was taken to be parallel to one of the sides of the squares. Our MC results for $\gamma$ obtained with closed boundary condition for the Sierpinski gaskets and with periodic boundary conditions for the square lattices are shown in Figure 4. One expects a finite $\gamma$ at low temperature when the angles are in an ordered configuration and zero stiffness in high temperature paramagnetic phase. Nelson and Kosterlitz [16] predicted a discontinuous jump in $\gamma$ at the BKT transition temperature $T_{c}$ with a universal value $\gamma(T_{c}) / T_{c}=2 / \pi$, and the straight line in Figure 4 gives the value of the jump at different temperatures. For a finite system the jump in $\gamma$ is replaced by continuous decrease with increasing $T$ which becomes steeper near the (putative) $T_{c}$ with increasing system size, as indicated by the results for the square lattices in Figure 4. The two important aspects of our results are: (1) For all lattices considered a rapid downturn in $\gamma$ starts near the universal $2 / \pi$-line. (2) While the low temperature values of $\gamma$ for the square lattices do not depend on the system size, for the Sierpinski gaskets they clearly decrease with increasing system size and the onset of the downturn in $\gamma$, which is in the vicinity of the universal $2 / \pi$-line, moves to the lower temperatures. This suggests that in the thermodynamic limit (i.e. when the order of the SG $m \to \infty$ ) the angle stiffness $\gamma$ would be zero at any finite temperature implying no BKT transition at a finite temperature.

We have examined the effect of boundary conditions (closed vs. open boundary conditions) and the results for the sixth order SG are shown in Figure 5. While the boundary conditions had no effect on the specific heat (see Figure 3) their effect on the helicity modulus is dramatic. The open boundary conditions give zero helicity modulus at all temperatures within the error bars, which are much larger when the three corners of the sixth order SG are not coupled to each other. Such a dramatic change in $\gamma$ implies that the closed boundary condition introduces significant additional correlations in two-dimensional SG fractal structure. Results obtained with the open boundary condition reinforce our conclusion about the absence of phase transition at any finite $T$.

Finally, for completeness, in Figure 6 we show our results for the linear susceptibility per site computed from

$$
\chi=\frac{\left\langle M^{2}\right\rangle-\langle M\rangle^{2}}{N^{2} k_{B} T}, \quad(5)
$$

where $M$ is the magnetization of the system when Hamiltonian (1) is used to describe magnetic systems. For BKT transition Kosterlitz predicted [17] that above $T_{c}$ the susceptibility diverges as $\chi \sim \exp [(2-\eta) b(T / T_{c}-1)^{-\nu}]$, with $\eta=0.25, b \approx 1.5$ and $\nu=0.5$, and is infinite below $T_{c}$. For finite systems one gets finite peaks in $\chi$ above $T_{c}$ which increase in height and move to lower temperatures with increasing system size, as illustrated by our results for three square lattices in Figure 6. This trend is analogous to what one finds for (1) in three dimensions where there is long-range order below the transition temperature. Therefore the simulation results

![](./images/867765956762402903_4.jpg)

Figure 4. The helicity modulus $\gamma$ as a function of temperature for Sierpinski gaskets and square lattices of different sizes. The straight line gives the size of Kosterlitz-Thouless discontinuous jump in $\gamma$ at various temperatures.

for susceptibility are not useful in diagnosing BKT transition unless one has the results for very large cluster size and attempts to fit them according to prediction by Kosterlitz [10]. We note that the susceptibilities for Sierpinski gaskets obtained with closed boundary condition are considerably higher than those for the square lattices of comparable sizes. Also, the error bars are considerably larger than what was obtained for the square lattices. The effect of boundary conditions on linear susceptibility for Sierpinski gaskets is shown in Figure 7. The main difference is that open boundary condition leads to much larger error bars at low temperatures which is consistent with our earlier observation that the closed boundary condition introduces additional correlations in the system.

### 3. Summary
Our Monte Carlo results for the specific heat for the XY-model on two-dimensional Sierpinski gaskets show that there is no long range order at any finite temperature as the specific heat is virtually independent of the system size. Moreover, the cluster-size dependence of the low temperature helicity modulus clearly indicates that there is no Berezinski-Kosterlitz-Thouless transition in this planar fractal structure in the thermodynamic limit. The low temperature values of the helicity modulus $\gamma$ decrease with increasing system size while they are size-independent for square lattices where the BKT transition does take place. Moreover, in the case of Sierpinski gaskets the onset of the downturn in helicity modulus near the universal $2/\pi$-line moves to the lower temperatures with increasing size of the clusters while

![](./images/867765956762402903_5.jpg)

Figure 5. The effect of boundary conditions on the temperature dependence of the the helicity modulus for SG of order $m$=6.

for the square lattices only the rate of decline in $\gamma$ beyond the $2/\pi$-line increases with the system size approaching a discontinuous jump in the thermodynamic limit. Our results are consistent with previous findings of Gefen et al. [3] who suggested, based on their exact renormalization group treatment of the resistor network on Sierpinski gasket, that spin systems with continuous symmetry on this structure do not display a finite temperature phase transition. Also, our findings are consistent with the results of Vallat et al. [8] obtained for the quadratic approximation to the XY-model on two-dimensional Sierpinski gasket, who found that the vortex energy is finite and hence free vortices are present at any temperature.

### 3.1. Acknowledgements
This work was supported in part by the Natural Sciences and Engineering Research Council of Canada.

### Note added in proof
After this manuscript was accepted for publication it came to our attention that the possibility of phase transitions on lattices of effectively nonintegral dimensionality was first examined by Dhar (D. Dhar, *Lattices of effectively nonintegral dimensionality*, J. Math. Phys. 18 (1977),pp. 577-585). In the case of the classical XY-model on the truncated tetrahedron lattice (the effective dimensionality $2\log2/\log5$) no phase transition at any finite temperature was obtained.

![](./images/867765956762402903_6.jpg)

Figure 6. The linear susceptibility for Sierpinski gaskets and square lattices.

## References

[1] Y. Gefen, B.B. Mandelbrot, and A. Aharony, *Critical Phenomena on Fractal Lattices*, Phys. Rev. Lett. 45 (1980), pp. 855–858.

[2] Y. Gefen, A. Aharony, and B.B. Mandelbrot, *Phase transitions on fractals: I. Quasi-linear lattices*, J. Phys. A: Math. Gen. 16 (1983), pp. 1267–1278.

[3] Y. Gefen, A. Aharony, Y. Shapir, and B.B. Mandelbrot, *Phase transitions on fractals: II. Sierpinski gaskets*, J. Phys. A: Math. Gen. 17 (1984), pp. 435–444.

[4] Y. Gefen, A. Aharony, and B.B. Mandelbrot, *Phase transitions on fractals: III. Infinitely ramified lattices*, J. Phys. A: Math. Gen. 17 (1984), pp. 1277–1289.

[5] P. Monceau and P.-Y. Hsiao, *Direct evidence for weak universality on fractal structures*, Physica A 331 (2004), pp. 1–9.

[6] R.B. Stinchcombe, *Position space treatment of diluted classical Heisenberg ferromagnet*, J. Phys. C: Solid State Phys. 12 (1979), pp. 2625–2636.

[7] J.M Gordon, A.M. Goldman, J. Maps, D. Costello, R. Tiberio, and B. Whitehead, *Superconducting-Normal Phase Boundary of a Fractal Network in a Magnetic Field*, Phys. Rev. Lett. 56 (1986), pp. 2280–2283.

[8] A. Vallat, S.E. Korshunov, and H. Beck, *XY model on a Sierpinski gasket*, Phys. Rev. B 43 (1991), pp. 8482–8486.

[9] See, for example, K.J. Strandburg, *Two-dimensional melting*, Rev. Mod. Phys. 60 (1988), pp. 162–207 and the references therein.

[10] R.W. Reid, S.K. Bose, and B. Mitrović, *Monte Carlo study of the XY-model on Penrose lattices*, J. Phys.: Condens. Matter 10 (1998), pp. 2301–2321.

[11] N.C. Metropolis, A.W. Rosenbluth, M.N. Rosenbluth, A.H. Teller, and E. Teller, *Equation of State Calculations by Fast Computing Machines*, J. Chem. Phys. 21 (1953), pp. 1087–1092.

[12] K. Binder and D.W. Heerman, *Monte Carlo Simulation in Statistical Physics*, Springer-Verlag, Berlin, 1988.

[13] J. Tobocnik and G.V. Chester, *Monte Carlo study of the planar spin model*, Phys. Rev. B 20 (1979), pp. 3761–3769.

[14] A.N. Berker and D.R. Nelson, *Superfluidity and phase separation in helium films*, Phys. Rev. B 19 (1979), pp. 2488–2503.

[15] C. Ebner and D. Stroud, *Superfluid density, penetration depth, and integrated fluctuation conductivity of a model granular superconductor*, Phys. Rev. B 28 (1983), pp. 5053–5060.

[16] D.R. Nelson and J.M. Kosterlitz, *Universal Jump in the Superfluid Density of Two-Dimensional Superfluids*, Phys. Rev. Lett. 39 (1977),pp. 1201–1205.

[17] J.M. Kosterlitz, *The critical properties of the two-dimensional xy model*, J. Phys. C: Solid State

![](./images/867765956762402903_7.jpg)

Figure 7. The effect of boundary conditions on the temperature dependence of the the susceptibility for the Sierpinski gasket of order $m$=6.

Phys. 7 (1974),pp. 1046–1060.