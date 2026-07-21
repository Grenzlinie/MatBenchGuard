# Double Exchange Model in Triangular Lattice
## Studied by Truncated Polynomial Expansion Method

Gui-Ping Zhang*

Department of Physics, Renmin University of China, Beijing 100872, China.

Received 16 April 2010; Accepted (in revised version) 24 September 2010
Communicated by Michel A. Van Hove
Available online 27 April 2011

Abstract. The low temperature properties of double exchange model in triangular lattice are investigated via truncated polynomial expansion method (TPEM), which reduces the computational complexity and enables parallel computation. We found that for the half-filling case a stable $120^\circ$ spin configuration phase occurs owing to the frustration of triangular lattice and is further stabilized by antiferromagnetic (AF) superexchange interaction, while a transition between a stable ferromagnetic (FM) phase and a unique flux phase with small finite-size effect is induced by AF superexchange interaction for the quarter-filling case.

AMS subject classifications: 82B05, 26C99, 65F99, 15A30

Key words: Manganite, Monte Carlo simulation, polynomial moment expansion, triangular lattice, frustration, finite-size effect.

## 1 Introduction

Doped manganite has become one of the most important strongly correlated systems, since colossal magnetoresistance (CMR) effect was discovered in 1990s (see [1,2]). CMR is referred to the resistivity of material change orders of magnitude under external magnetic field and it may have a potential application in computer technology or even spintronics. There are rich phase diagrams and many ordered phase [3], rising from delicate interaction between electron, spin and orbit degree of freedoms. Further it is found that the phase separation [4] (PS) may be crucial to CMR effect.

Double-exchange model, as a starting point to study manganite, describes the Hund interaction between itinerant electron and localized spin of $Mn$ atoms and is expressed by
$$
H_{D E}=-t \sum_{\langle i j\rangle, \alpha}\left(\mathrm{C}_{i, \alpha}^{\dagger} \mathrm{C}_{j, \alpha}+h. c.\right)-J_{H} \sum_{i, \alpha, \beta} \mathrm{C}_{i, \alpha}^{\dagger} \sigma_{\alpha \beta} \mathrm{C}_{i, \beta} \cdot S_{i}, \tag{1.1}
$$

*Corresponding author. Email address: zhanggp96@ruc.edu.cn (G.-P. Zhang)

where the nearest-neighbor hopping integral $t$ is adopted as the energy unit, $J_H$ is the Hund interaction strength, $C_{i,\alpha}^\dagger$ ($C_{i,\alpha}$) creates (annihilates) one electron at site $i$ with spin $\alpha$, $\langle ij\rangle$ stands for the nearest neighbors of lattice site, and $\sigma_{\alpha\beta}$ is the Pauli matrix. The localized spin $S_i$ at site $i$ is assumed as 1 here. In addition, antiferromagnetic (AF) superexchange is crucial to stabilize AF phase of some underdopped narrow-band manganite, and this interaction is expressed by $H_{AF}=J_{AF}\sum_{\langle ij\rangle}S_i\cdot S_j$. So the total hamiltonian is $H=H_{DE}+H_{AF}$. In this model, localized spins is treated as a classic field $\phi$ and electron degree of freedom can be integrated for any given localized spin configuration. The partition function is expressed by

$$
Z=\operatorname{Tr}_{\mathrm{c}} \operatorname{Tr}_{\mathrm{F}}\left(e^{-\beta\left[H(\phi)-\mu n_{e}\right]}\right)=\operatorname{Tr}_{\mathrm{c}} e^{-S_{\mathrm{eff}}(\phi)},
$$

and the effective action is

$$
S_{\text {eff }}(\phi)=-\sum_{\nu} \ln \left(1+e^{-\beta\left(\epsilon_{\nu}-\mu\right)}\right)+\beta E(\phi).
$$

Here $\epsilon_v$ is the $v$-th eigenvalue of one-electron sector's Hamiltonian matrix $H(\phi)$, $E(\phi)$ is the interaction energy between spins, $\beta$ is the inverse temperature, $\mu$ is the chemical potential, and $n_e$ is the electron number operator, respectively. The fluctuation of localized spins is suitable for Monte Carlo (MC) simulation, and the partition sum is replaced by stochastic samplings with the Boltzmann weight $e^{-S_{\text {eff }}(\phi)} / Z$. With MC simulation, an intrinsic PS between high electron density and low electron density has been reproduced in doped manganites [5].

Despite the success of reproducing PS, the above method is suffered from finite-size effect, since the computational complexity of exact diagonalizing (DIAG) $H(\phi)$ scales as $\mathcal{O}(N^4)$, with $N$ being the system size. In order to overcome the above restriction, Furukawa and Motome [6,7] proposed Chebyshev polynomials expansion method(PEM) and the computational complexity became $\mathcal{O}(MN^3)$ at a finite cutoff $M$. In 2004 they further reduced the computational complexity to $\mathcal{O}(N)$ via truncated polynomial expansion method (TPEM) [8,9]. The system size [10] is extended to $40 \times 40$, compared with $10 \times 10$ via DIAG [5]. Not only the computational complexity is greatly reduced, but also parallel computation is capable under PEM and TPEM, which would increase the computational speed very much. Finally, from the viewpoint of physical properties, one-body quantity such as energy and electron density, but also dynamical quantity or two-body quantity such as conductance are able to be investigated under PEM and TPEM, and there have been several examples of application to large scale system [10–13].

Up to date, most studies focus on the double-exchange model in one- and two-dimensional square lattice. In this paper, we present our results on this model in two dimensional triangular lattice. One famous layered triangular lattice is the superconductor $Na_{0.35}CoO_2\cdot1.35H_2O$ discovered in 2003 (see [14]). Though triangular lattice structure is not found in manganite yet, it is still meaningful to study the interplay between electron, spin and lattice for double exchange model in two dimensional triangular lattice.

With the frustration, there is $120^\circ$ spin configuration in low temperature for the half-filling case, and this phase becomes more stable by AF superexchange interaction; but for the quarter-filling case, we found a stable long-range ferromagnetic (FM) ordered phase turns into a unique flux phase induced by AF superexchange interaction. This paper is arranged as follows: we briefly describe PEM and TPEM (more details please refer to [6-9]) and give some benchmark in Section 2, in Section 3 show results in triangular lattice, and finally we summarize in Section 4.

## 2 The method and benchmark
The core of Chebyshev polynomial expansion method (PEM) is that the mean value of physical quantity is expressed by the sum of the moment multiplied with physical quantity expansion coefficients, and it converges to exact value guaranteed by rapidly decaying expansion coefficients. It is important that the accuracy is controlled only by the cutoff $M$, the thresholds $\epsilon_p$ and $\epsilon_{tr}$, not by the system size and/or the chemical potential. It is further verified that the error does not accumulate with Monte Carlo sweep. It is advantageous that the application to large-scale system is capable, as the computational speed is greatly improved due to reduced computational complexity. In following, we will give a brief description of PEM and TPEM, and some benchmark.

### 2.1 Polynomial expansion method
The Chebyshev polynomials $T_m(x)$ are recursively defined by: $T_0(x)=1$, $T_1(x)=x$, and $T_m(x)=2xT_{m-1}(x)-T_{m-2}(x)$, with $-1\leq x\leq 1$. These polynomials are orthonormal in a form that
$$
\int_{-1}^{1} \frac{d x}{\sqrt{1-x^{2}}} T_{m}(x) T_{m^{\prime}}(x)=\alpha_{m} \delta_{m m^{\prime}},
$$
where
$$
\alpha_{m}=\left\{\begin{array}{ll}
1, & m=0, \\
\frac{1}{2}, & m \neq 0.
\end{array}\right.
$$

The density of states (DOS) can be expressed as
$$
D(\epsilon)=\frac{1}{2 \pi \sqrt{1-\epsilon^{2}}} \sum_{m=0}^{\infty} \mu_{m} T_{m}(\epsilon),
$$
with the moment being $\mu_{m}=\int_{-1}^{1} T_{m}(\epsilon) D(\epsilon) d \epsilon$. Then the mean value of any physical operator $f$ can be expressed by
$$
\langle f\rangle=\int_{-1}^{1} d \epsilon D(\epsilon) f(\epsilon)=\sum_{m} \mu_{m} f_{m}, \tag{2.1}
$$

with expansion coefficients

$$
f_{m}=\frac{1}{\alpha_{m}} \int_{-1}^{1} \frac{d x}{\sqrt{1-x^{2}}} f(x) T_{m}(x),
$$

which decay exponentially for $m \gg 1$ and ensure the accuracy at finite cutoff $M$ [7]. Here $f(x)$ may be the effective action function $S(x)=-\ln \left[1+e^{\beta(x-\mu)}\right]$ or electron number func- tion $n(x)=\left[1+e^{\beta(x-\mu)}\right]^{-1}$, and $f_{m}$ is easily calculated.

The moment

$$
\mu_{m}=\sum_{v=1}^{N_{\mathrm{dim}}} T_{m}\left(\epsilon_{v}\right)=\operatorname{Tr}\left(T_{m}(H)\right),
$$

can be evaluated under any set of orthonormal basis $e(k)$,

$$
\mu_{m}=\sum_{k=1}^{N_{\mathrm{dim}}}\left\langle e(k)\left|T_{m}(H)\right| e(k)\right\rangle=\sum_{k=1}^{N_{\mathrm{dim}}} \mu_{m}(k). \tag{2.2}
$$

Here we define a vector $v(k, m)=T_{m}(H)|e(k)\rangle$, and a partial moment $\mu_{m}(k)=$ $\langle e(k)|v(k, m)\rangle$. From the definition, it is easy to calculate the vector $v(k, m)$ recursively and the element $i$ in the vector $v(k, m)$ is expressed as

$$
v_{i}(k, 0)=e_{i}(k), \tag{2.3a}
$$

$$
v_{i}(k, 1)=\sum_{j} H_{i j} v_{j}(k, 0), \tag{2.3b}
$$

$$
v_{i}(k, m)=2 \sum_{j} H_{i j} v_{j}(k, m-1)-v_{i}(k, m-2). \tag{2.3c}
$$

### 2.2 Truncation of matrix-vector product and trace operator

For a sparse hamiltonian matrix $H_{i j}$ with $\mathcal{O}(N)$ nonzero elements, the multiplication can be confined to nonzero elements that scale as $\mathcal{O}\left(M^{D}\right)$, where $D$ is the system dimension. The computational complexity of $M$-th moment $\mu_{M}(k)$ is $\mathcal{O}\left(M^{D+1}\right)$ and further reduced to $\mathcal{O}\left(M^{D / 2+1}\right)$ if elements less than the threshold $\epsilon_{p}$ are neglected. A subspace $N_{\epsilon_{p}}(k, m)$ is defined by $N_{\epsilon_{p}}(k, m)=\bigcup_{m^{\prime}=0}^{m}\{i\},\left|v_{i}\left(k, m^{\prime}\right)\right| \geq \epsilon_{p}$. The total error of the Boltzmann weight is $\mathcal{O}\left(M^{D+1} \epsilon_{p}\right)$.

Based on the importance sampling method, during each MC sweep a new configura- tion is accepted as the ratio $r=\exp \left[-\triangle S_{\text {eff }}\right]$ is larger than a random number uniformly distributed between 0 and 1. The update of the effective action $\triangle S_{\text {eff }}=\sum_{m k}\left[\mu_{m}^{\text {new }}(k)-\right.$ $\left.\mu_{m}^{\text {old }}(k)\right] S_{m}$ is expressed by

$$
\triangle S_{\mathrm{eff}}=\sum_{m} S_{m} \sum_{k=1}^{N_{\mathrm{dim}}} \triangle \mu_{m}(k), \tag{2.4}
$$

and the update of the moment is

$$
\triangle \mu_{m}(k)=\left\langle e(k)\left|v^{\text {new }}(k, m)\right\rangle-\langle e(k)\right| v^{\text {old }}(k, m)\rangle. \tag{2.5}
$$

Due to local update of the classical field, only a few elements of the Hamiltonian matrix $H$ are modulated, there are only a limited amount of $v(k,m)$ to be updated, and a new threshold $\epsilon_{\text{tr}}$ can be taken to reduce the computational complexity. The total computational complexity of one MC sweep is $\mathcal{O}(M^{D+1}N)$. As Eq. (2.2) is shown, each basis is inter-independent and the calculation of the moment $\mu_m$ can be parallelized.

### 2.3 Benchmark for double exchange model

Here we present some benchmark, such as the accuracy of the physical quantity, the number of nonzero elements, and the sweep time. One basic factor of the algorithm is the accuracy. As we mention above, the error can be controlled systematically by $M$, $\epsilon_{\text{p}}$ and $\epsilon_{\text{tr}}$, and the result is often reliable at finite $M$. In Fig. 1 we show the error of the effective action $S_{\text{eff}}$ and the electron occupation $n_e$ under a random spin configuration in two dimensional triangle lattice. As $M$ increases, the error is smaller and smaller, and the result eventually converges to the exact value. From Fig. 1(a) and (b), both the effective action and the electron density are very accurate for $20\leq M\leq40$, though $M\sim40$ is required at lower temperature due to slowly decaying $f_m$. Fortunately, the error does not depend on other physical parameters, such as the chemical potential $\mu$ (Fig. 1(c) and (d)) and the system size (Fig. 1(e) and (f)). Moreover, the error of the effective action does not accumulate during Monte Carlo update process (not shown here). These facts show that PEM combined with MC simulation is reliable to study large-scale system.

The other important factor of the algorithm is the computation speed controlled by computational complexity. For TPEM, the complexity is usually associated with $N$, the

![](./images/811663779958882305_1.jpg)

Figure 1: The error of $S_{eff}$ (a, c, e) and $n_e$ (b, d, f) vs the cutoff $M$ for a given spin configuration in triangular lattice. $J_H=8$ and $J_{AF}=0$. Other parameters are (a) and (b) $N=6\times6$, $\mu=-8$; (c) and (d) $N=6\times6$, $\beta=50$; and (e) and (f) $\beta=50$, $\mu=-8$.

![](./images/811663779958882305_2.jpg)

Figure 2: $N_e$ elements in the subspace $N_{\epsilon_p}$ vs (a) the system size $N$ in one dimension, and vs (b, c) the cutoff $M$ in one and two dimension. $\beta=75$, $J_H=8$, $\mu=-8$, $J_{AF}=0$. (a) $M=16$, (b) $N=40$, and (c) $N=40\times40$.

![](./images/811663779958882305_3.jpg)

Figure 3: Comparison of one MC sweep CPU time (sec) via TPEM and DIAG in (a) one and (b) two dimension. $M=30$, $\epsilon_{pr}=10^{-5}$ and $\epsilon_{tr}=10^{-3}$.

system dimension $D$, $M$, $\epsilon_{\rm p}$ and $\epsilon_{\rm tr}$. In Fig. 2(a), we show how the number of elements in the subspace $N_{\epsilon_{\rm p}}$ ($N_e$) change with $N$. While not surprisingly $N_e$ decreases with higher $\epsilon_{\rm p}$, it is interesting that $N_e$ saturates no matter how large $N$ is. That is why the complexity is linear with $N$ for one MC sweep. In Fig. 2(b) and (c) the asymptotic behavior of $N_e$ changes from $\mathcal{O}(M^D)$ to $\mathcal{O}(M^{D/2})$ once the truncation $\epsilon_{\rm p}$ is taken. Now we compare the computational speed. Fig. 3 illustrates the CPU time cost by one MC sweep via DIAG and TPEM, respectively. In one dimension TPEM is prior as $N\geq64$, and it is 1000 times faster than DIAG at $N\geq512$. In two dimension, TPEM is advantageous as the system is larger than $14\times14$. The sweep time is the same in square lattice and triangular lattice by DIAG, but it is shorter in square lattice than in triangular lattice by TPEM, as the hamiltonian is sparser owning to electron hopping between less nearest-neighbors in square lattice. Due to the dimensionality, the scaling behavior of time with respect to the system size is the same in triangular lattice as in square lattice. Once parallel computation is realized, TPEM will be more efficient.

## 3 Double exchange model in triangular lattice

In triangular lattice with the lattice constant $a$, two basic lattice vectors are $\vec{a}_{1}=(1,0) a$, and $\vec{a}_{2}=\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right) a$. The reciprocal lattices are

$$
\vec{b}_{1}=\frac{4 \pi}{\sqrt{3} a}\left(\frac{\sqrt{3}}{2},-\frac{1}{2}\right), \quad \vec{b}_{2}=\frac{4 \pi}{\sqrt{3} a}(0,1).
$$

For $L \times L$ triangular lattice, the momentum $\vec{q}=m \vec{b}_{1} / L+n \vec{b}_{2} / L$ is shortened as $\left(q_{1}, q_{2}\right)$, with $q_{1}=m / L, q_{2}=n / L$, and $m, n$ as integers from 0 to $L$. Here we mainly focus on the spin structure factor $S(q)$ defined by

$$
S(\vec{q})=\frac{1}{N} \sum_{i, j}\left\langle S_{i} \cdot S_{j}\right\rangle e^{i \vec{q} \cdot \vec{r}_{i j}},
\tag{3.1}
$$

where $\left\langle S_{i} \cdot S_{j}\right\rangle$ is the mean spin-spin correlation, $\vec{r}_{i j}$ is the displacement between site $i$ and $j$, and $N=L \times L$.

In order to understand the interplay between electron, spin and lattice, we study the spin-spin correlation for different filling case. First we will check the accuracy of the mean spin-spin correlation. The maximal monte carlo step is 10000, and the physical quantity is evaluated every 20 steps after first 2000 warmup steps. The parameters are $M=30, \epsilon_{p}=10^{-5}$ and $\epsilon_{t r}=10^{-3}$. Due to periodic boundary condition (PBC), we only show $\left\langle S_{1} \cdot S_{j}\right\rangle$ with $1 \leq j \leq N$ in Fig. 4. For half-filling case (Fig. 4(a) and (d)) and low-filling case (Fig. 4(c) and (f)) regions, the accuracy are enough. But for quarter-filling case

![](./images/811663779958882305_4.jpg)

Figure 4: The spin-spin correlation $\langle S_{1} \cdot S_{j}\rangle$ of $6 \times 6$ triangular lattice. $\beta=75$ and $J_{H}=8$. $\epsilon_{p}=10^{-5}$ and $\epsilon_{tr}=10^{-3}$. (a) $J_{AF}=0, \mu=-6$ and $\langle n\rangle=0.9272$, (b) $J_{AF}=0, \mu=-8$ and $\langle n\rangle=0.4512$, (c) $J_{AF}=0, \mu=-10$ and $\langle n\rangle=0.1944$, (d) $J_{AF}=0.1, \mu=-6$ and $\langle n\rangle=0.9146$, (e) $J_{AF}=0.1, \mu=-8$ and $\langle n\rangle=0.5$, (f) $J_{AF}=0.1$, $\mu=-10$ and $\langle n\rangle=0.2101$.

(Fig. 4(b)), the accuracy is not good, and higher $M$ is required. For the spin flux phase, $M=30$ is enough for the accuracy as Fig. 4(e) shows, and the accuracy was verified in $6 \times 6$ to $12 \times 12$ triangular lattice. Therefore it is not necessary to use large $M$ as the basic physical phenomenon still remains.

### 3.1 Half-filling case

For half-filling case one lattice has one electron and electron hops between adjacent lattices will reduce the total energy. According to Pauli exclusion rule two electrons on one lattice site should have opposite spins, hence the nearest-neighbor localized spins tend to be antiparallel, but there exists frustration effect induced by triangular lattice. Therefore $120^{\circ}$ spin configuration occurs, where three localized spins of each triangle are coplaner with angle between any two being $120^{\circ}$. Using the method in [16], the coplane is verified by the fact that $(S_{i} \times S_{j}) \cdot S_{k}$ statistically equals to zero, where site $i$, $j$ and $k$ are located in one triangle; and the angle between any two being $120^{\circ}$ is verified by the spin-spin correlation of adjacent sites being $-0.48$, very close to the limit $-0.5$. Regarding to $S(\vec{q})$, two peaks are located at $(1/3,1/3)$ and $(2/3,2/3)$, respectively, and $S(\vec{q})/N$=0.408 (Fig. 5(a)). This phase is stabilized by AF superexchange interaction with $S(\vec{q})/N$=0.464 (Fig. 5(d)).

### 3.2 Low- and mediate-filling case

For low- and mediate-filling case, there is less than one electron on each lattice site and adjacent spins tend to be parallel. Hence the system is in FM phase and the peak $S(\overrightarrow{0,0})/N=0.821$ is close to the maximum value 1 (Fig. 5(c)). But in the presence of superexchange interaction, the system is paramagnetic (Fig. 5(f)) because of the competition between electron-mediated FM correlation and AF superexchange interaction. The spin structure factor is almost flat at all vector $\vec{q}$ and has no peak at all. But for near zero filling case, $120^{\circ}$ spin configuration will be induced by AF interaction with the interplay between spins and lattice.

### 3.3 Quarter-filling case

For quarter-filling case in one- and two-dimensional square lattice with PBC, the FM phase is not stable, that is positive spin-spin correlation at short distance and negative at long distance. This phenomenon has been observed long before (see [5] and the references inside). Open boundary condition (OBC) or other kind of boundary condition is chosen to stabilize FM phase [5]. In two-dimensional triangular lattice with PBC, the effect of lattice on FM phase is significant. Each site has 6 nearest-neighbors, and their spins tend to be parallel. It is found that electron-mediated FM phase is stabilized even at long distance and $S(\overrightarrow{0,0})/N=0.899$ (Fig. 5(b)). So the FM phase is strengthened by triangular lattice, compared with square lattice.

![](./images/811663779958882305_5.jpg)

Figure 5: The spin structure factor $S(q_{1}, q_{2})$ of $6 \times 6$ triangular lattice. $\beta=75$, and $J_{H}=8$. (a) $J_{A F}=0, \mu=-6$ and $\langle n\rangle=0.9272$, (b) $J_{A F}=0, \mu=-8$ and $\langle n\rangle=0.4512$, (c) $J_{A F}=0, \mu=-10$ and $\langle n\rangle=0.1944$, (d) $J_{A F}=0.1$, $\mu=-6$ and $\langle n\rangle=0.9146$, (e) $J_{A F}=0.1, \mu=-8$ and $\langle n\rangle=0.5$, and (f) $J_{A F}=0.1, \mu=-10$ and $\langle n\rangle=0.2101$.

![](./images/811663779958882305_6.jpg)

Figure 6: The peak $S(\vec{q})$ vs the size $L$ in two dimensional triangular lattices. $\beta=75, J_{H}=8, J_{A F}=0.1, \mu=-8$ and $\langle n\rangle=0.5$.

Now we consider the effect on AF superexchange interaction on spin-spin correla- tion. A spin-flux phase [10, 16] occurs in the square lattice, where four localized spins within each square lie (anti) clockwise at the same plane. In the triangular lattice, as $J_{A F}$ increases from 0 to 0.4 (in fact $J_{A F}$ does not exceed 0.1 in material), the system is in FM phase at first and then turns into a specific flux phase and eventually evolves into $120^{\circ}$ spin configuration phase. For the specific flux phase corresponding to the mediate AF superexchange interaction, $(S_{i} \times S_{j}) \cdot S_{k}$ with the sites $i, j$ and $k$ belonging to one triangle statistically equals to 0.7, and the spin-spin correlation of adjacent sites is -0.3. So this phase is different from both FM phase and $120^{\circ}$ configuration phase. The peak $S(\vec{q})$ is located at vectors $(1 / 2,0),(0,1 / 2)$ and $(1 / 2,1 / 2)$, respectively, and $S(\vec{q}) / N \sim 0.29$ very close to its maximum value $1 / 3$ (Fig. 5(e)). We further extend the system size from $6 \times 6$ to $12 \times 12$, and find that the peaks position does not change and the normalized peak value $S(\vec{q}) / N$ converges to 0.285 (Fig. 6). So finite-size effect is small and this flux phase is very stable.

We systematically investigate the behavior of the spin-spin correlation and spin structure factor at high temperature. The peak value of spin structure factor decreases with the temperature, and eventually at $\beta$=10 the system is paramagnetic as $J_{AF}$ ranges from 0 to 0.1. So there is no phase transition at high temperature and the system is still subjected to the dimensionality of system.

## 4 Conclusions

Double exchange model with antiferromagnetic spin-spin superexchange interaction has been studied for two dimensional triangular lattice with the truncated polynomial expansion method. For the half-filling case we obtained $120^\circ$ spin configuration at low temperature, and it is further stabilized by superexchange interaction. For the quarter-filling case, we found that the FM phase is quite stable, and superexchange interaction results in a unique spin-flux configuration with very small finite-size effect.

## Acknowledgments

The author would like to thank Prof. X.-Q. Wang for proposing this interesting project and for his many insightful discussions, and thank Dr. Q.-L. Zhang for discussing Monte Carlo simulation of double exchange model. This work was supported by the NFSC grants No. 10425417 and No. 10674142.

## References

[1] R. von Helmot, J. Wecker, B. Holzapfel, L. Schultz, and K. Samwer, Giant negative magnetoresistance in perovskitelike $La_{2/3}Ba_{1/3}MnO_x$ ferromagnetic films, Phys. Rev. Lett., 71 (1993), 2331–2333.

[2] S. Jin, T. H. Tiefel, M. McCormakc, R. A. Fastnacht, R. Ramesh, and L. H. Chen, Thousandfold change in resistivity in magnetoresistive LaCaMnO films, Sci., 264 (1994), 413–415.

[3] A. Urushibara, Y. Moritomo, T. Arima, A. Asamitsu, G. Kido, and Y. Tokura, Insulator-metal transition and giant magnetoresistance in $La_{1-x}Sr_xMnO_3$, Phys. Rev. B., 51 (1995), 14103–14109.

[4] Y.-D. Chuang, A. D. Gromko, D. S. Dessau, T. Kimura, and Y. Tokura, Fermi surface nesting and nanoscale fluctuating charge/orbital ordering in colossal magnetoresistive oxides, Sci., 292 (2001), 1509–1513.

[5] S. Yunoki, J. Hu, A. L. Malvezzi, A. Moreo, N. Furukawa, and E. Dagotto, Phase separation in electronic models for manganites, Phys. Rev. Lett., 80 (1998), 845–848.

[6] Y. Motome, and N. Furukawa, A Monte Carlo method for fermion systems coupled with classical degrees of freedom, J. Phys. Soc. Jpn., 68 (1998), 3853–3858.

[7] N. Furukawa, and Y. Motome, Monte carlo algorithm for the double exchange model optimized for parallel computations, Comput. Phys. Commun., 142 (2001), 410–413.

[8] N. Furukawa, and Y. Motome, Order $N$ Monte Carlo algorithm for fermion systems coupled with fluctuating adiabatical fields, J. Phys. Soc. Jpn., 73 (2004), 1482–1489.

[9] G. Alvarez, C. Sen, N. Furukawa, Y. Motome, and E. Dagotto, The truncated polynomial expansion Monte Carlo method for fermion systems coupled to classical fields: a model independent implementation, Comput. Phys. Commun., 168 (2005), 32-45.

[10] C. Sen, G. Alvarez, Y. Motome, N. Furukawa, I. A. Sergienko, T. C. Schulthess, A. Moreo, and E. Dagotto, One- and two-band models for colossal magnetoresistive manganites studied using the truncated polynomial expansion method, Phys. Rev. B., 73 (2006), 224430-224444.

[11] G. Alvarez, and T. C. Schulthess, Calculation of dynamical and many-body observables for spin-fermion models using the polynomial expansion method, Phys. Rev. B., 73 (2006), 035117-035125.

[12] G. Alvarez, H. Aliaga, C. Sen, and E. Dagotto, Fragility of the A-type AF and CE phases of manganites: insulator-to-metal transition induced by quenched disorder, Phys. Rev. B., 73 (2006), 224426-224438.

[13] C. Sen, G. Alvarez, H. Aliaga, and E. Dagotto, Colossal magnetoresistance observed in Monte Carlo simulations of the one- and two-orbital models for manganites, Phys. Rev. B., 73 (2006), 224441-224453.

[14] K. Takada, H. Sakurai, E. Takayama-Muromachi, F. Izumi, R. A. Dilanian, and T. Sasaki, Superconductivity in two-dimensional $CoO_2$ layers, Nature., 422 (2003), 53-55.

[15] J. L. Alonso, L. A. Fernández, F. Guinea, V. Laliena, and V. Martín-Mayo, Hybrid Monte Carlo algorithm for the double exchange model, Nucl. Phys. B., 596 (2001), 587-610.

[16] D. F. Agterberg, and S. Yunoki, Spin-flux phase in the Kondo lattice model with classical localized spins, Phys. Rev. B., 62 (2000), 13816-13819.